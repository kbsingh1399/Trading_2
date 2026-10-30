# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 15:21:06 IST` (`2026-10-30 09:51:06 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2224.50` | **Live Ask Quote**: `2227.70` | **Mid Price**: `2226.10`
- **Spread Points**: `320.00` | **Spread BPS**: `14.37 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2219.84` | VWAP Z-Score: `+0.37` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `11.82` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `45.84` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2269.04` | Lower -3.00σ Band: `2170.64`
  * Upper +2.51σ Band: `2261.00` | Lower -2.51σ Band: `2178.68`
  * Upper +2.01σ Band: `2252.80` | Lower -2.01σ Band: `2186.88`
  * Upper +2.00σ Band: `2252.64` | Lower -2.00σ Band: `2187.04`
  * Upper +1.28σ Band: `2240.83` | Lower -1.28σ Band: `2198.85`
  * Upper +1.00σ Band: `2236.24` | Lower -1.00σ Band: `2203.44`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2225.68` | EMA-20=`2229.18` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2242.67` (Slope: `+0.0000`) | EMA-100=`2266.29`
  * Institutional Anchors: EMA-144=`2280.05` | EMA-200=`2292.55` (Slope: `-0.3533`) | EMA-233=`2297.57`
- **Range Boundaries**: 24H High=`2374.90` | 24H Low=`2167.70` | Weekly High=`2387.80` | Weekly Low=`2167.70`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2252.28` (Distance: `-1.16%`)
  * Point of Control (POC) = `2241.75` (Distance: `-0.69%`)
  * Value Area Low (VAL) = `2194.81` (Distance: `+1.43%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2339.52` | POC=`2321.58` | VAL=`2296.66`
  * Prior Day Extremes: PDH=`2374.90` | PDL=`2225.40` | PDC=`2252.70`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2354.78` | Weekly POC=`2309.30` | Weekly VAL=`2300.49`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2289.10` | Low=`2167.70`
  * London Session (08:00-16:00 UTC): High=`2251.30` | Low=`2215.10`
  * New York Session (13:00-21:00 UTC): High=`2239.46` | Low=`2212.74`
  * Initial Balance (First Hour): IB High=`2246.50` | IB Low=`2230.60`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2217.20` - `2235.00`
  * Optimal Trade Entry (OTE 0.705): `2230.55`
  * Structural Invalidation Anchor (0.786): `2243.91`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2229.67` | `2231.18` | `2227.81` | `2229.82` | `12,704` | 28,324,681.02 USD | -2,906,841.49 USD | `-10.26%` | -964,094,117.36 USD | `-0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `2229.81` | `2229.81` | `2226.60` | `2228.73` | `12,547` | 27,951,584.00 USD | 1,768,767.95 USD | `+6.33%` | -962,325,349.41 USD | `+0.38` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `2228.72` | `2229.13` | `2227.84` | `2228.05` | `719` | 1,603,316.35 USD | -85,287.16 USD | `-5.32%` | -962,410,636.56 USD | `+0.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `2223.00` | `2226.00` | `2220.44` | `2225.84` | `32,324` | 71,858,619.15 USD | 5,514,896.63 USD | `+7.67%` | -964,308,443.49 USD | `+0.38` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `2225.85` | `2231.18` | `2220.24` | `2229.82` | `36,513` | 81,297,282.61 USD | 604,420.51 USD | `+0.74%` | -963,704,022.98 USD | `+0.05` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `2229.81` | `2229.81` | `2226.60` | `2227.84` | `13,252` | 29,522,244.37 USD | 1,653,190.78 USD | `+5.60%` | -962,050,832.20 USD | `+0.13` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `2252.91` | `2253.96` | `2228.21` | `2235.54` | `253,701` | 568,308,333.87 USD | -3,920,812.04 USD | `-0.69%` | -926,664,438.18 USD | `+0.36` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `2235.54` | `2236.80` | `2223.18` | `2227.93` | `164,265` | 366,023,334.59 USD | -37,825,356.97 USD | `-10.33%` | -964,489,795.15 USD | `+0.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2227.92` | `2231.18` | `2220.24` | `2227.84` | `111,690` | 248,534,105.33 USD | 2,438,962.95 USD | `+0.98%` | -962,050,832.20 USD | `+0.43` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -913,988,928.25 USD | `-0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2257.30` | `2225.47` | `2235.54` | `766,584` | 1,719,026,962.60 USD | 26,122,859.80 USD | `+1.52%` | -887,866,068.44 USD | `+0.88` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `2235.54` | `2236.80` | `2220.24` | `2227.84` | `275,955` | 614,557,439.92 USD | -35,386,394.02 USD | `-5.76%` | -923,252,462.46 USD | `+0.54` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -98,115,944.70 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2252.34` | `2,564,135` | 5,830,064,162.53 USD | -554,237,569.32 USD | `-9.51%` | -652,353,514.01 USD | `-1.25` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -913,988,928.25 USD | `-0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2257.30` | `2225.47` | `2235.54` | `766,584` | 1,719,026,962.60 USD | 26,122,859.80 USD | `+1.52%` | -887,866,068.44 USD | `+0.88` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `2235.54` | `2236.80` | `2220.24` | `2227.84` | `275,955` | 614,557,439.92 USD | -35,386,394.02 USD | `-5.76%` | -923,252,462.46 USD | `+0.54` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`2226.10`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2226.00` | `221.5618` | 493,196.57 USD | 11,645,419.38 USD | `8 orders` | `-0.09%` | `-` |
| `BID` | `2226.10` | `465.9889` | 1,037,337.89 USD | 11,152,222.81 USD | `5 orders` | `-0.08%` | `-` |
| `BID` | `2226.20` | `265.1942` | 590,375.33 USD | 10,114,884.92 USD | `9 orders` | `-0.08%` | `-` |
| `BID` | `2226.30` | `320.4988` | 713,526.48 USD | 9,524,509.59 USD | `13 orders` | `-0.07%` | `-` |
| `BID` | `2226.40` | `343.0546` | 763,776.76 USD | 8,810,983.11 USD | `5 orders` | `-0.07%` | `-` |
| `BID` | `2226.50` | `109.6134` | 244,054.24 USD | 8,047,206.35 USD | `8 orders` | `-0.07%` | `-` |
| `BID` | `2226.60` | `233.7238` | 520,409.41 USD | 7,803,152.12 USD | `8 orders` | `-0.06%` | `-` |
| `BID` | `2226.70` | `461.0126` | 1,026,536.76 USD | 7,282,742.70 USD | `7 orders` | `-0.06%` | `-` |
| `BID` | `2226.80` | `137.9719` | 307,235.83 USD | 6,256,205.95 USD | `7 orders` | `-0.05%` | `-` |
| `BID` | `2226.90` | `261.6395` | 582,645.00 USD | 5,948,970.12 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `2227.00` | `678.7061` | 1,511,478.48 USD | 5,366,325.12 USD | `15 orders` | `-0.04%` | `-` |
| `BID` | `2227.10` | `48.7227` | 108,510.33 USD | 3,854,846.63 USD | `7 orders` | `-0.04%` | `-` |
| `BID` | `2227.20` | `567.4468` | 1,263,817.51 USD | 3,746,336.31 USD | `12 orders` | `-0.03%` | `-` |
| `BID` | `2227.30` | `286.0025` | 637,013.37 USD | 2,482,518.79 USD | `6 orders` | `-0.03%` | `-` |
| `BID` | `2227.40` | `157.5489` | 350,924.42 USD | 1,845,505.43 USD | `9 orders` | `-0.02%` | `-` |
| `BID` | `2227.50` | `79.3996` | 176,862.61 USD | 1,494,581.01 USD | `7 orders` | `-0.02%` | `-` |
| `BID` | `2227.60` | `202.4938` | 451,075.19 USD | 1,317,718.40 USD | `9 orders` | `-0.02%` | `-` |
| `BID` | `2227.70` | `57.3494` | 127,757.26 USD | 866,643.21 USD | `8 orders` | `-0.01%` | `-` |
| `BID` | `2227.80` | `113.4354` | 252,711.38 USD | 738,885.95 USD | `7 orders` | `-0.01%` | `-` |
| `BID` | `2227.90` | `218.2210` | 486,174.57 USD | 486,174.57 USD | `30 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2227.95` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,227.95` | `0.00%` | `-` |
| `ASK` | `2228.00` | `2.3345` | 5,201.27 USD | 5,201.27 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `2228.10` | `10.4605` | 23,307.04 USD | 28,508.31 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `2228.20` | `2.2202` | 4,947.05 USD | 33,455.36 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `2228.30` | `6.8453` | 15,253.38 USD | 48,708.74 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `2228.40` | `65.1323` | 145,140.82 USD | 193,849.55 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `2228.50` | `101.2708` | 225,681.98 USD | 419,531.53 USD | `11 orders` | `+0.02%` | `-` |
| `ASK` | `2228.60` | `166.6786` | 371,459.93 USD | 790,991.46 USD | `9 orders` | `+0.03%` | `-` |
| `ASK` | `2228.70` | `201.0153` | 448,002.80 USD | 1,238,994.26 USD | `8 orders` | `+0.03%` | `-` |
| `ASK` | `2228.80` | `727.8980` | 1,622,339.06 USD | 2,861,333.32 USD | `7 orders` | `+0.04%` | `-` |
| `ASK` | `2228.90` | `90.0673` | 200,751.00 USD | 3,062,084.33 USD | `10 orders` | `+0.04%` | `-` |
| `ASK` | `2229.00` | `56.6775` | 126,334.15 USD | 3,188,418.47 USD | `4 orders` | `+0.05%` | `-` |
| `ASK` | `2229.10` | `229.3936` | 511,341.27 USD | 3,699,759.75 USD | `9 orders` | `+0.05%` | `-` |
| `ASK` | `2229.20` | `632.0486` | 1,408,962.74 USD | 5,108,722.49 USD | `5 orders` | `+0.06%` | `-` |
| `ASK` | `2229.30` | `342.4143` | 763,344.20 USD | 5,872,066.69 USD | `10 orders` | `+0.06%` | `-` |
| `ASK` | `2229.40` | `134.3418` | 299,501.61 USD | 6,171,568.30 USD | `8 orders` | `+0.07%` | `-` |
| `ASK` | `2229.50` | `166.7027` | 371,663.67 USD | 6,543,231.97 USD | `7 orders` | `+0.07%` | `-` |
| `ASK` | `2229.60` | `311.0690` | 693,559.44 USD | 7,236,791.41 USD | `9 orders` | `+0.07%` | `-` |
| `ASK` | `2229.70` | `467.7810` | 1,043,011.30 USD | 8,279,802.70 USD | `12 orders` | `+0.08%` | `-` |
| `ASK` | `2229.80` | `3.5608` | 7,939.87 USD | 8,287,742.58 USD | `4 orders` | `+0.08%` | `-` |
| `ASK` | `2229.90` | `153.9542` | 343,302.47 USD | 8,631,045.05 USD | `6 orders` | `+0.09%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:20:42 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1786.14` | `30,282.40` | 54,088,732.77 USD | `AT_RISK_LIQ` | `0xde8d9e530b` | `2026-10-30 15:20:42 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1843.94` | `7,964.66` | 14,686,315.60 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-30 15:20:42 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 15:20:42 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `10,000.00` | 19,261,000.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-30 15:20:42 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1929.22` | `8,092.45` | 15,612,143.31 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 15:20:42 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2121.88` | `30,641.99` | 65,018,755.10 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 15:20:42 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2129.16` | `26,025.05` | 55,411,549.64 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 15:20:42 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2175.00` | `3,533.33` | 7,684,999.71 USD | `TRIGGER_STOP` | `0x469e9a7f62` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2189.80` | `2,065.07` | 4,522,097.51 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2191.10` | `500.00` | 1,095,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2193.90` | `4,250.16` | 9,324,427.12 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 15:20:42 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2195.00` | `839.60` | 1,842,926.39 USD | `TRIGGER_STOP` | `0x28280399d9` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2195.10` | `508.10` | 1,115,321.53 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2201.10` | `500.00` | 1,100,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2201.30` | `1,481.20` | 3,260,562.26 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2203.10` | `500.00` | 1,101,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xf929122994` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2206.10` | `360.24` | 794,719.95 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2208.50` | `508.47` | 1,122,947.16 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2210.00` | `430.01` | 950,326.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2210.20` | `1,016.99` | 2,247,755.06 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2211.10` | `500.00` | 1,105,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2211.10` | `500.00` | 1,105,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xf929122994` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2213.90` | `508.52` | 1,125,805.79 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2214.30` | `2,185.59` | 4,839,541.97 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2215.00` | `1,808.43` | 4,005,681.31 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2216.20` | `685.15` | 1,518,423.45 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2217.80` | `344.01` | 762,944.93 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2218.00` | `1,354.51` | 3,004,307.39 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2218.60` | `475.35` | 1,054,607.07 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 15:20:42 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2219.00` | `439.90` | 976,147.64 USD | `TRIGGER_STOP` | `0x369fd6445f` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2219.50` | `355.75` | 789,593.78 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2220.40` | `902.04` | 2,002,894.72 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2221.00` | `566.99` | 1,259,292.56 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x9362ca4dfd` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2221.10` | `476.69` | 1,058,778.16 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2221.80` | `1,115.09` | 2,477,517.63 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2221.90` | `676.06` | 1,502,145.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2223.60` | `353.97` | 787,089.47 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2223.70` | `450.35` | 1,001,437.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2229.70` | `449.14` | 1,001,446.57 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2229.70` | `351.05` | 782,726.15 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2231.20` | `673.27` | 1,502,199.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2233.60` | `476.14` | 1,063,504.52 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2234.50` | `896.35` | 2,002,903.01 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2235.60` | `475.31` | 1,062,594.09 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2236.30` | `348.64` | 779,657.37 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2236.40` | `344.01` | 769,343.52 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2237.10` | `1,342.97` | 3,004,358.86 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2237.10` | `1,116.21` | 2,497,072.27 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2238.00` | `698.33` | 1,562,853.14 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2238.20` | `1,789.71` | 4,005,719.75 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2239.30` | `508.37` | 1,138,397.42 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2244.10` | `430.01` | 964,990.38 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2244.20` | `508.54` | 1,141,263.22 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2247.00` | `2,185.59` | 4,911,010.62 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2250.20` | `353.18` | 794,719.79 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2254.00` | `4,250.16` | 9,579,861.77 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2254.50` | `1,417.47` | 3,195,685.89 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2261.80` | `508.09` | 1,149,200.22 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2264.40` | `2,011.67` | 4,555,230.98 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:20:42 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2269.70` | `620.97` | 1,409,408.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x674982e841` | `2026-10-30 15:20:42 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2300.00` | `4,002.10` | 9,204,832.99 USD | `TRIGGER_STOP` | `0xfb941d2344` | `2026-10-30 15:20:42 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2468.87` | `22,046.99` | 54,431,199.08 USD | `AT_RISK_LIQ` | `0x8added25f8` | `2026-10-30 15:20:42 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `3,002.39` | 7,547,704.95 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-30 15:20:42 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2623.92` | `10,000.00` | 26,239,195.38 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-30 15:20:42 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2657.77` | `9,700.00` | 25,780,366.97 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-30 15:20:42 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 228,804,095.55 USD | `102,676.40` | `2322.74` | `2228.80` | `3722.11` | 9,686,817.59 USD | `+4.23%` | `5X Cross` |
| `5` | `0xb83d...6e36` | `SHORT` | 110,231,071.07 USD | `49,455.37` | `2375.30` | `2228.80` | `4628.55` | 7,240,587.35 USD | `+6.57%` | `5X Cross` |
| `9` | `0x77dd...e0e9` | `LONG` | 68,307,127.90 USD | `30,641.99` | `2610.31` | `2228.80` | `2121.80` | -11,678,047.14 USD | `-17.10%` | `10X Cross` |
| `10` | `0xde8d...9524` | `LONG` | 67,517,646.84 USD | `30,282.40` | `2134.45` | `2228.80` | `1786.06` | 2,881,316.27 USD | `+4.27%` | `20X Cross` |
| `15` | `0x0392...d7d9` | `LONG` | 58,025,453.93 USD | `26,025.05` | `2518.71` | `2228.80` | `2129.08` | -7,524,268.16 USD | `-12.97%` | `9X Cross` |
| `22` | `0x8add...7d2c` | `SHORT` | 49,129,509.84 USD | `22,046.99` | `2271.09` | `2228.80` | `2476.93` | 941,387.46 USD | `+1.92%` | `25X Cross` |
| `25` | `0x15a4...dfdb` | `SHORT` | 44,540,000.00 USD | `20,000.00` | `2228.11` | `2228.80` | `3187.77` | 22,327.68 USD | `+0.05%` | `20X Cross` |
| `26` | `0xdf95...7d72` | `SHORT` | 43,945,813.97 USD | `19,716.37` | `2402.53` | `2228.80` | `4233.34` | 3,423,443.11 USD | `+7.79%` | `25X Cross` |
| `33` | `0x6046...b21d` | `LONG` | 35,506,420.06 USD | `15,927.59` | `2410.19` | `2228.80` | `1784.12` | -2,882,199.59 USD | `-8.12%` | `6X Cross` |
| `35` | `0xefe4...194b` | `SHORT` | 33,676,210.72 USD | `15,108.89` | `2250.33` | `2228.80` | `2919.18` | 323,806.03 USD | `+0.96%` | `20X Cross` |
| `37` | `0xb695...a92d` | `SHORT` | 32,970,806.96 USD | `14,795.73` | `2557.74` | `2228.80` | `3779.21` | 4,872,907.15 USD | `+14.78%` | `20X Cross` |
| `38` | `0xeced...6210` | `SHORT` | 32,728,326.27 USD | `14,687.58` | `2522.09` | `2228.80` | `3649.30` | 4,315,191.27 USD | `+13.18%` | `20X Cross` |
| `40` | `0x45d2...4029` | `SHORT` | 31,099,014.00 USD | `13,950.00` | `2443.60` | `2228.80` | `5355.69` | 2,989,268.46 USD | `+9.61%` | `20X Cross` |
| `42` | `0xa61c...66b9` | `LONG` | 28,731,218.40 USD | `12,888.00` | `2369.69` | `2228.80` | `1475.54` | -1,809,436.14 USD | `-6.30%` | `10X Cross` |
| `44` | `0xbd1c...ff0e` | `LONG` | 26,756,400.00 USD | `12,000.00` | `2419.91` | `2228.80` | `1519.94` | -2,282,632.39 USD | `-8.53%` | `20X Cross` |
| `46` | `0x2371...0883` | `LONG` | 26,751,600.00 USD | `12,000.00` | `2421.77` | `2228.80` | `1279.04` | -2,309,694.85 USD | `-8.63%` | `20X Cross` |
| `52` | `0x0c5d...36b3` | `LONG` | 24,521,640.00 USD | `11,000.00` | `2482.20` | `2228.80` | `1644.01` | -2,782,613.24 USD | `-11.35%` | `20X Cross` |
| `53` | `0xa9de...e049` | `LONG` | 24,521,200.00 USD | `11,000.00` | `2481.81` | `2228.80` | `1643.68` | -2,778,779.46 USD | `-11.33%` | `20X Cross` |
| `54` | `0x6c93...59a4` | `LONG` | 24,512,400.00 USD | `11,000.00` | `2441.15` | `2228.80` | `1601.97` | -2,340,272.73 USD | `-9.55%` | `20X Cross` |
| `55` | `0x09dc...c094` | `LONG` | 24,508,000.00 USD | `11,000.00` | `2465.31` | `2228.80` | `1637.01` | -2,610,423.04 USD | `-10.65%` | `20X Cross` |
| `69` | `0xa2ce...3126` | `LONG` | 22,333,624.95 USD | `10,016.88` | `2162.83` | `2228.80` | `1557.16` | 668,822.90 USD | `+2.99%` | `10X Cross` |
| `70` | `0x6646...6de5` | `LONG` | 22,296,000.00 USD | `10,000.00` | `1765.80` | `2228.80` | `1720.15` | 4,637,942.55 USD | `+20.80%` | `25X Cross` |
| `71` | `0xb37f...66ca` | `SHORT` | 22,284,000.00 USD | `10,000.00` | `2290.69` | `2228.80` | `2623.84` | 622,991.85 USD | `+2.80%` | `25X Cross` |
| `72` | `0xec7f...df39` | `LONG` | 22,280,000.00 USD | `10,000.00` | `2719.35` | `2228.80` | `1720.53` | -4,913,548.52 USD | `-22.05%` | `20X Cross` |
| `73` | `0xecb6...2b00` | `SHORT` | 22,169,503.92 USD | `9,948.62` | `2240.08` | `2228.80` | `5405.87` | 116,221.38 USD | `+0.52%` | `15X Cross` |
| `75` | `0x939f...04d2` | `LONG` | 21,899,636.67 USD | `9,823.81` | `2427.28` | `2228.80` | `1713.78` | -1,945,513.93 USD | `-8.88%` | `25X Cross` |
| `78` | `0xaeaa...2416` | `SHORT` | 21,624,210.00 USD | `9,700.00` | `2311.92` | `2228.80` | `2657.69` | 801,472.40 USD | `+3.71%` | `25X Cross` |
| `85` | `0xf517...c032` | `SHORT` | 20,791,225.59 USD | `9,326.35` | `2202.91` | `2228.80` | `3119.45` | -246,087.38 USD | `-1.18%` | `25X Cross` |
| `86` | `0xca49...53c8` | `SHORT` | 20,470,833.21 USD | `9,181.89` | `2549.39` | `2228.80` | `3893.77` | 2,937,444.18 USD | `+14.35%` | `25X Cross` |
| `87` | `0xba5d...a352` | `SHORT` | 20,176,205.69 USD | `9,054.12` | `2493.89` | `2228.80` | `2773.68` | 2,403,801.57 USD | `+11.91%` | `20X Cross` |
| `89` | `0xea00...a918` | `LONG` | 20,074,931.12 USD | `9,003.83` | `2003.01` | `2228.80` | `1428.16` | 2,040,152.25 USD | `+10.16%` | `5X Cross` |
| `114` | `0x9eec...daab` | `LONG` | 18,039,694.22 USD | `8,092.45` | `1658.44` | `2228.80` | `1930.12` | 4,618,829.69 USD | `+25.60%` | `15X Cross` |
| `115` | `0x5f91...65aa` | `LONG` | 17,757,996.79 USD | `7,964.66` | `1626.99` | `2228.80` | `1843.86` | 4,799,553.73 USD | `+27.03%` | `16X Cross` |
| `124` | `0xec0b...b078` | `LONG` | 15,622,486.09 USD | `7,007.80` | `2065.97` | `2228.80` | `1057.30` | 1,144,556.50 USD | `+7.33%` | `25X Cross` |
| `130` | `0xf02d...5eb3` | `LONG` | 15,286,105.27 USD | `6,855.99` | `2383.33` | `2228.80` | `1122.45` | -1,053,983.50 USD | `-6.90%` | `20X Cross` |
| `132` | `0xcf53...ee11` | `SHORT` | 15,155,217.22 USD | `6,803.63` | `1862.69` | `2228.80` | `4196.09` | -2,482,111.83 USD | `-16.38%` | `7X Cross` |
| `136` | `0x4ff9...38d3` | `LONG` | 14,627,437.54 USD | `6,564.10` | `2447.40` | `2228.80` | `1669.63` | -1,437,585.20 USD | `-9.83%` | `3X Isolated` |
| `138` | `0xf78c...c581` | `LONG` | 14,492,893.86 USD | `6,500.22` | `2521.53` | `2228.80` | `1913.11` | -1,897,647.09 USD | `-13.09%` | `20X Cross` |
| `139` | `0x1ee7...edf5` | `LONG` | 14,492,400.00 USD | `6,500.00` | `2301.55` | `2228.80` | `2068.84` | -467,693.66 USD | `-3.23%` | `25X Cross` |
| `143` | `0x799f...5f4c` | `LONG` | 14,068,896.73 USD | `6,310.90` | `2390.33` | `2228.80` | `1867.21` | -1,016,267.89 USD | `-7.22%` | `20X Cross` |
| `148` | `0x08bf...7872` | `SHORT` | 13,876,140.24 USD | `6,224.05` | `2258.00` | `2228.80` | `2584.91` | 177,775.87 USD | `+1.28%` | `20X Cross` |
| `150` | `0xec4a...cf62` | `LONG` | 13,747,270.71 USD | `6,166.63` | `2225.41` | `2228.80` | `1958.79` | 23,951.27 USD | `+0.17%` | `25X Cross` |
| `152` | `0x524e...0de0` | `LONG` | 13,375,800.00 USD | `6,000.00` | `2246.48` | `2228.80` | `2002.81` | -103,085.04 USD | `-0.77%` | `10X Cross` |
| `153` | `0xd9e7...4aff` | `LONG` | 13,375,440.00 USD | `6,000.00` | `2480.18` | `2228.80` | `1407.40` | -1,505,684.33 USD | `-11.26%` | `20X Cross` |
| `154` | `0xc179...e0c8` | `LONG` | 13,049,023.56 USD | `5,854.73` | `2294.94` | `2228.80` | `1192.87` | -387,248.61 USD | `-2.97%` | `10X Cross` |
| `162` | `0x0c4a...1b19` | `LONG` | 12,612,961.27 USD | `5,660.10` | `2373.06` | `2228.80` | `2081.45` | -818,796.86 USD | `-6.49%` | `25X Isolated` |
| `169` | `0x7fda...17d1` | `LONG` | 11,848,294.34 USD | `5,315.76` | `2211.05` | `2228.80` | `0.000000` | 94,852.10 USD | `+0.80%` | `25X Cross` |
| `186` | `0x45ab...6cbc` | `LONG` | 10,971,777.32 USD | `4,920.96` | `2727.66` | `2228.80` | `1380.08` | -2,450,966.48 USD | `-22.34%` | `7X Cross` |
| `190` | `0x64b7...9da9` | `LONG` | 10,827,351.63 USD | `4,856.84` | `2604.61` | `2228.80` | `599.95` | -1,822,862.79 USD | `-16.84%` | `25X Cross` |
| `197` | `0xfb18...eb17` | `SHORT` | 10,627,276.35 USD | `4,768.16` | `2315.53` | `2228.80` | `2622.21` | 413,553.35 USD | `+3.89%` | `25X Cross` |
| `198` | `0x5559...d43b` | `SHORT` | 10,602,098.92 USD | `4,755.93` | `2262.69` | `2228.80` | `2745.77` | 159,106.96 USD | `+1.50%` | `25X Cross` |
| `210` | `0xe091...6705` | `SHORT` | 10,031,580.45 USD | `4,500.00` | `2467.33` | `2228.80` | `2463.03` | 1,071,428.06 USD | `+10.68%` | `20X Cross` |
| `211` | `0x418a...8888` | `SHORT` | 10,026,000.00 USD | `4,500.00` | `2494.55` | `2228.80` | `2993.09` | 1,199,484.41 USD | `+11.96%` | `25X Cross` |
| `217` | `0xb829...3a81` | `LONG` | 9,791,861.71 USD | `4,394.91` | `2398.60` | `2228.80` | `1454.49` | -749,780.24 USD | `-7.66%` | `20X Cross` |
| `236` | `0x28bb...fca6` | `SHORT` | 9,384,492.94 USD | `4,209.61` | `1896.10` | `2228.80` | `3035.01` | -1,402,610.37 USD | `-14.95%` | `20X Cross` |
| `238` | `0x4e23...20c3` | `LONG` | 9,339,503.12 USD | `4,190.37` | `2228.42` | `2228.80` | `0.000000` | 1,571.70 USD | `+0.02%` | `20X Cross` |
| `239` | `0x6ea4...0ea7` | `SHORT` | 9,323,234.61 USD | `4,184.01` | `2602.13` | `2228.80` | `3424.97` | 1,564,112.06 USD | `+16.78%` | `20X Cross` |
| `251` | `0x5e9e...35ee` | `SHORT` | 8,935,246.19 USD | `4,007.56` | `1796.39` | `2228.80` | `2585.47` | -1,736,096.10 USD | `-19.43%` | `20X Cross` |
| `252` | `0xfb94...0ddf` | `SHORT` | 8,923,085.06 USD | `4,002.10` | `2382.44` | `2228.80` | `5104.36` | 611,699.09 USD | `+6.86%` | `20X Cross` |
| `253` | `0x3dc9...54b0` | `SHORT` | 8,917,709.27 USD | `3,999.69` | `2480.32` | `2228.80` | `6605.39` | 1,002,827.28 USD | `+11.25%` | `20X Cross` |
| `254` | `0x8cc9...2b6a` | `SHORT` | 8,916,800.00 USD | `4,000.00` | `1791.18` | `2228.80` | `3537.76` | -1,752,053.33 USD | `-19.65%` | `25X Cross` |
| `270` | `0x4b67...f4e7` | `LONG` | 8,509,014.91 USD | `3,820.84` | `2591.51` | `2228.80` | `1348.28` | -1,392,758.63 USD | `-16.37%` | `20X Cross` |
| `279` | `0x12d2...f97f` | `LONG` | 8,376,062.39 USD | `3,757.26` | `2446.50` | `2228.80` | `1796.32` | -816,104.00 USD | `-9.74%` | `20X Cross` |
| `296` | `0x8ae4...3d60` | `LONG` | 7,929,089.09 USD | `3,558.20` | `2482.21` | `2228.80` | `522.98` | -903,108.94 USD | `-11.39%` | `10X Cross` |
| `300` | `0x469e...58a5` | `SHORT` | 7,875,446.37 USD | `3,533.33` | `2203.63` | `2228.80` | `3083.95` | -89,283.28 USD | `-1.13%` | `25X Cross` |
| `308` | `0x218a...7da2` | `SHORT` | 7,724,468.63 USD | `3,465.07` | `2208.16` | `2228.80` | `3101.69` | -73,039.38 USD | `-0.95%` | `10X Cross` |
| `337` | `0x9c2a...f6a8` | `SHORT` | 6,694,125.85 USD | `3,002.39` | `2515.77` | `2228.80` | `2587.62` | 859,212.05 USD | `+12.84%` | `20X Cross` |
| `338` | `0x4a20...3c26` | `LONG` | 6,687,600.00 USD | `3,000.00` | `2428.72` | `2228.80` | `613.60` | -598,560.28 USD | `-8.95%` | `20X Cross` |
| `339` | `0x007d...67a0` | `LONG` | 6,686,400.00 USD | `3,000.00` | `2400.00` | `2228.80` | `1470.85` | -513,600.00 USD | `-7.68%` | `25X Cross` |
| `340` | `0xb823...9763` | `SHORT` | 6,676,200.00 USD | `3,000.00` | `2229.66` | `2228.80` | `3233.36` | 12,796.68 USD | `+0.19%` | `25X Cross` |
| `393` | `0x8328...f54a` | `SHORT` | 5,743,527.85 USD | `2,576.45` | `2292.01` | `2228.80` | `3279.21` | 161,743.44 USD | `+2.82%` | `25X Cross` |
| `395` | `0xed48...7c9b` | `SHORT` | 5,686,980.11 USD | `2,551.13` | `2460.02` | `2228.80` | `3226.73` | 588,866.30 USD | `+10.35%` | `20X Cross` |
| `398` | `0x970c...2a93` | `SHORT` | 5,572,250.00 USD | `2,500.00` | `2229.57` | `2228.80` | `5077.37` | 1,694.49 USD | `+0.03%` | `20X Cross` |
| `399` | `0x1c98...7fc7` | `LONG` | 5,571,010.03 USD | `2,500.00` | `2452.60` | `2228.80` | `1916.60` | -560,511.54 USD | `-10.06%` | `10X Cross` |
| `413` | `0xa445...329d` | `LONG` | 5,363,757.93 USD | `2,406.14` | `2354.86` | `2228.80` | `1764.61` | -302,357.36 USD | `-5.64%` | `25X Cross` |
| `415` | `0xfbe2...c8ea` | `SHORT` | 5,317,101.22 USD | `2,385.21` | `2041.57` | `2228.80` | `2623.66` | -447,534.56 USD | `-8.42%` | `20X Cross` |
| `416` | `0x6749...ce07` | `SHORT` | 5,316,644.64 USD | `2,384.89` | `2220.92` | `2228.80` | `3631.10` | -19,981.61 USD | `-0.38%` | `20X Cross` |
| `417` | `0x645b...87b8` | `SHORT` | 5,303,537.63 USD | `2,379.98` | `2421.64` | `2228.80` | `11554.51` | 459,909.33 USD | `+8.67%` | `10X Cross` |
| `427` | `0x77ee...2902` | `SHORT` | 5,104,576.27 USD | `2,290.69` | `2476.53` | `2228.80` | `6114.92` | 568,395.97 USD | `+11.14%` | `25X Cross` |
| `451` | `0xd507...c948` | `SHORT` | 4,842,039.38 USD | `2,172.00` | `2387.49` | `2228.80` | `2600.21` | 343,601.65 USD | `+7.10%` | `5X Isolated` |
| `458` | `0x023a...2355` | `LONG` | 4,777,635.93 USD | `2,142.82` | `2328.93` | `2228.80` | `0.000000` | -212,867.92 USD | `-4.46%` | `25X Cross` |
| `464` | `0x382b...3e39` | `SHORT` | 4,748,025.95 USD | `2,129.54` | `2296.66` | `2228.80` | `4555.74` | 142,811.26 USD | `+3.01%` | `25X Cross` |
| `498` | `0x3453...b323` | `SHORT` | 4,459,474.46 USD | `2,000.12` | `2322.47` | `2228.80` | `2397.25` | 185,761.38 USD | `+4.17%` | `25X Cross` |
| `499` | `0xe02e...d78b` | `LONG` | 4,458,600.00 USD | `2,000.00` | `2228.11` | `2228.80` | `2171.55` | 2,376.53 USD | `+0.05%` | `25X Cross` |
| `503` | `0xf3dc...1672` | `SHORT` | 4,415,611.59 USD | `1,980.36` | `2240.44` | `2228.80` | `2788.43` | 21,275.96 USD | `+0.48%` | `20X Cross` |
| `506` | `0x7a6d...f79c` | `SHORT` | 4,394,812.01 USD | `1,971.44` | `2418.41` | `2228.80` | `2544.84` | 372,949.16 USD | `+8.49%` | `25X Cross` |
| `509` | `0xac48...3201` | `SHORT` | 4,379,758.24 USD | `1,964.37` | `2272.04` | `2228.80` | `3081.81` | 83,384.06 USD | `+1.90%` | `20X Cross` |
| `524` | `0x8376...9a1e` | `SHORT` | 4,256,011.94 USD | `1,910.50` | `2477.72` | `2228.80` | `3186.26` | 477,676.23 USD | `+11.22%` | `20X Cross` |
| `525` | `0x739c...cfb2` | `SHORT` | 4,236,240.00 USD | `1,900.00` | `2418.12` | `2228.80` | `2448.28` | 358,206.38 USD | `+8.46%` | `25X Cross` |
| `552` | `0xbcd4...0dd2` | `SHORT` | 4,018,589.03 USD | `1,803.03` | `2233.24` | `2228.80` | `2745.51` | 8,020.98 USD | `+0.20%` | `25X Cross` |
| `553` | `0x7265...91a5` | `LONG` | 4,016,727.27 USD | `1,801.87` | `2533.96` | `2228.80` | `1987.07` | -549,139.19 USD | `-13.67%` | `20X Cross` |
| `554` | `0xbb34...1696` | `LONG` | 4,013,280.00 USD | `1,800.00` | `2313.95` | `2228.80` | `1986.21` | -151,838.23 USD | `-3.78%` | `25X Cross` |
| `555` | `0xc619...10f5` | `LONG` | 4,008,780.00 USD | `1,800.00` | `2313.55` | `2228.80` | `1818.48` | -155,615.83 USD | `-3.88%` | `25X Cross` |
| `565` | `0x91a9...3f70` | `SHORT` | 3,940,773.41 USD | `1,767.48` | `2156.23` | `2228.80` | `3669.82` | -129,669.33 USD | `-3.29%` | `4X Cross` |
| `601` | `0xfeec...4e9c` | `SHORT` | 3,772,056.90 USD | `1,691.81` | `2566.49` | `2228.80` | `2509.42` | 569,967.61 USD | `+15.11%` | `10X Cross` |
| `625` | `0xeee0...0b53` | `LONG` | 3,650,131.45 USD | `1,637.12` | `2468.64` | `2228.80` | `191.67` | -391,344.61 USD | `-10.72%` | `7X Cross` |
| `627` | `0x27b8...12fc` | `LONG` | 3,628,102.83 USD | `1,628.12` | `2468.73` | `2228.80` | `637.98` | -391,291.80 USD | `-10.79%` | `10X Cross` |
| `628` | `0x982b...4606` | `LONG` | 3,627,151.85 USD | `1,626.82` | `2575.24` | `2228.80` | `1547.35` | -562,301.22 USD | `-15.50%` | `5X Isolated` |
| `635` | `0x73d7...8be1` | `LONG` | 3,569,346.31 USD | `1,601.47` | `2410.40` | `2228.80` | `1766.74` | -290,832.61 USD | `-8.15%` | `25X Cross` |
| `636` | `0xad54...6203` | `LONG` | 3,561,039.33 USD | `1,597.45` | `2591.98` | `2228.80` | `2043.76` | -579,538.72 USD | `-16.27%` | `10X Isolated` |
| `640` | `0x880a...311c` | `LONG` | 3,517,305.89 USD | `1,578.40` | `2209.72` | `2228.80` | `0.000000` | 29,482.04 USD | `+0.84%` | `9X Cross` |
| `645` | `0x936c...bb0f` | `LONG` | 3,496,351.73 USD | `1,568.64` | `2232.92` | `2228.80` | `0.000000` | -6,317.89 USD | `-0.18%` | `20X Cross` |
| `659` | `0xe170...9300` | `SHORT` | 3,418,255.28 USD | `1,533.40` | `2076.39` | `2228.80` | `3108.42` | -234,305.78 USD | `-6.85%` | `25X Cross` |
| `664` | `0x4b86...df9d` | `SHORT` | 3,397,300.80 USD | `1,524.00` | `2287.40` | `2228.80` | `2759.56` | 88,696.80 USD | `+2.61%` | `9X Isolated` |
| `669` | `0x2e2b...2fab` | `LONG` | 3,360,998.50 USD | `1,507.38` | `2245.53` | `2228.80` | `1251.62` | -23,874.60 USD | `-0.71%` | `25X Cross` |
| `671` | `0x4487...c92d` | `LONG` | 3,359,084.15 USD | `1,506.59` | `2232.11` | `2228.80` | `1578.07` | -3,782.68 USD | `-0.11%` | `10X Cross` |
| `672` | `0x251f...6e5d` | `LONG` | 3,343,950.00 USD | `1,500.00` | `2346.68` | `2228.80` | `1893.26` | -176,080.49 USD | `-5.27%` | `20X Cross` |
| `673` | `0xde6b...3361` | `LONG` | 3,342,600.00 USD | `1,500.00` | `2216.98` | `2228.80` | `2168.48` | 17,119.26 USD | `+0.51%` | `25X Cross` |
| `693` | `0xb885...3c54` | `LONG` | 3,232,750.90 USD | `1,450.00` | `2274.34` | `2228.80` | `32.20` | -65,057.23 USD | `-2.01%` | `20X Cross` |
| `699` | `0xef70...a84c` | `SHORT` | 3,216,307.86 USD | `1,442.74` | `2424.73` | `2228.80` | `3253.32` | 281,962.96 USD | `+8.77%` | `25X Cross` |
| `707` | `0xbadb...9ee6` | `LONG` | 3,183,654.27 USD | `1,428.16` | `1936.00` | `2228.80` | `1079.42` | 418,732.63 USD | `+13.15%` | `20X Cross` |
| `713` | `0x0622...8088` | `SHORT` | 3,163,828.18 USD | `1,419.52` | `2229.57` | `2228.80` | `9151.23` | 1,096.04 USD | `+0.03%` | `5X Cross` |
| `748` | `0x020c...5872` | `LONG` | 3,065,150.00 USD | `1,375.00` | `2226.32` | `2228.80` | `2139.26` | 3,949.05 USD | `+0.13%` | `25X Cross` |
| `761` | `0x53f8...ceff` | `LONG` | 3,007,094.49 USD | `1,348.65` | `2276.73` | `2228.80` | `0.000000` | -63,429.98 USD | `-2.11%` | `20X Cross` |
| `779` | `0xa0fb...96be` | `LONG` | 2,934,876.99 USD | `1,317.09` | `2277.10` | `2228.80` | `1519.85` | -64,285.29 USD | `-2.19%` | `3X Cross` |
| `781` | `0x0dd5...f6ee` | `LONG` | 2,930,808.82 USD | `1,314.74` | `2288.50` | `2228.80` | `1559.31` | -77,969.53 USD | `-2.66%` | `5X Cross` |
| `792` | `0x039c...0ebd` | `LONG` | 2,874,645.76 USD | `1,289.71` | `2226.24` | `2228.80` | `0.000000` | 3,429.96 USD | `+0.12%` | `25X Cross` |
| `813` | `0x1f16...6d07` | `LONG` | 2,822,293.80 USD | `1,266.00` | `2261.43` | `2228.80` | `1382.61` | -40,677.43 USD | `-1.44%` | `7X Cross` |
| `817` | `0xc435...c905` | `SHORT` | 2,782,091.52 USD | `1,248.00` | `2704.38` | `2228.80` | `3799.95` | 592,978.83 USD | `+21.31%` | `20X Cross` |
| `824` | `0x6859...7e1e` | `SHORT` | 2,757,986.97 USD | `1,237.15` | `2200.39` | `2228.80` | `4853.68` | -35,759.81 USD | `-1.30%` | `25X Cross` |
| `833` | `0x7277...0b98` | `SHORT` | 2,717,431.07 USD | `1,219.45` | `2206.05` | `2228.80` | `3407.79` | -27,243.27 USD | `-1.00%` | `20X Cross` |
| `834` | `0x7178...0854` | `LONG` | 2,716,573.34 USD | `1,218.63` | `2461.81` | `2228.80` | `1185.63` | -283,473.06 USD | `-10.43%` | `10X Cross` |
| `845` | `0xaaa1...ab8c` | `SHORT` | 2,675,520.00 USD | `1,200.00` | `2276.29` | `2228.80` | `2365.18` | 56,037.58 USD | `+2.09%` | `25X Isolated` |
| `861` | `0x07fd...689d` | `LONG` | 2,622,612.02 USD | `1,176.69` | `2416.34` | `2228.80` | `0.000000` | -220,687.92 USD | `-8.41%` | `25X Cross` |
| `872` | `0xfc27...9d9d` | `LONG` | 2,559,354.67 USD | `1,148.31` | `2237.33` | `2228.80` | `0.000000` | -9,801.27 USD | `-0.38%` | `25X Cross` |
| `917` | `0x2f80...f203` | `SHORT` | 2,426,160.77 USD | `1,088.94` | `1984.00` | `2228.80` | `2959.32` | -265,693.58 USD | `-10.95%` | `20X Cross` |
| `921` | `0x6f11...0389` | `SHORT` | 2,405,414.70 USD | `1,079.00` | `2333.39` | `2228.80` | `2971.51` | 112,314.21 USD | `+4.67%` | `25X Cross` |
| `922` | `0x8eb7...b90f` | `LONG` | 2,402,927.32 USD | `1,077.74` | `2396.38` | `2228.80` | `1880.88` | -179,750.72 USD | `-7.48%` | `5X Isolated` |
| `924` | `0x2b61...2f6c` | `SHORT` | 2,399,089.20 USD | `1,076.60` | `2681.75` | `2228.80` | `6292.27` | 488,083.54 USD | `+20.34%` | `10X Cross` |
| `955` | `0x30af...393e` | `SHORT` | 2,321,068.91 USD | `1,041.16` | `2252.26` | `2228.80` | `2296.87` | 23,913.41 USD | `+1.03%` | `25X Cross` |
| `958` | `0x2577...4897` | `LONG` | 2,318,513.15 USD | `1,040.21` | `2231.95` | `2228.80` | `0.000000` | -3,178.66 USD | `-0.14%` | `15X Cross` |
| `968` | `0x1b2a...f7a6` | `LONG` | 2,286,160.49 USD | `1,025.37` | `2737.51` | `2228.80` | `882.02` | -520,799.45 USD | `-22.78%` | `10X Cross` |
| `979` | `0x001a...fef6` | `SHORT` | 2,245,629.62 USD | `1,007.33` | `2022.19` | `2228.80` | `3088.63` | -208,621.67 USD | `-9.29%` | `10X Cross` |
| `980` | `0x02aa...1806` | `SHORT` | 2,245,128.25 USD | `1,007.10` | `2654.68` | `2228.80` | `3612.66` | 428,403.85 USD | `+19.08%` | `20X Cross` |
| `984` | `0xdb3a...cf3b` | `LONG` | 2,236,467.42 USD | `1,003.22` | `2705.01` | `2228.80` | `0.000000` | -477,239.47 USD | `-21.34%` | `4X Cross` |
| `987` | `0x5272...fcd9` | `SHORT` | 2,229,600.00 USD | `1,000.00` | `2241.82` | `2228.80` | `2830.71` | 12,224.49 USD | `+0.55%` | `5X Cross` |
| `988` | `0x8c02...b73f` | `SHORT` | 2,229,600.00 USD | `1,000.00` | `2250.37` | `2228.80` | `8098.34` | 20,771.47 USD | `+0.93%` | `20X Cross` |
| `989` | `0xf929...d1f9` | `SHORT` | 2,229,200.00 USD | `1,000.00` | `2423.37` | `2228.80` | `2926.09` | 194,170.17 USD | `+8.71%` | `25X Cross` |
| `990` | `0x6463...42f5` | `SHORT` | 2,228,000.00 USD | `1,000.00` | `2223.43` | `2228.80` | `3706.78` | -4,565.05 USD | `-0.20%` | `5X Cross` |
| `991` | `0xd7b8...9f55` | `LONG` | 2,226,970.80 USD | `999.00` | `2195.00` | `2228.80` | `0.000000` | 34,165.80 USD | `+1.53%` | `15X Cross` |
| `1021` | `0xb002...ed8a` | `SHORT` | 2,146,623.21 USD | `962.78` | `2299.66` | `2228.80` | `4198.27` | 67,454.70 USD | `+3.14%` | `25X Cross` |
| `1041` | `0xb1ec...e86a` | `SHORT` | 2,081,733.54 USD | `933.64` | `2272.72` | `2228.80` | `12597.97` | 40,173.42 USD | `+1.93%` | `25X Cross` |
| `1048` | `0xb812...b5e0` | `LONG` | 2,065,969.70 USD | `927.11` | `2263.21` | `2228.80` | `1165.36` | -32,276.78 USD | `-1.56%` | `25X Cross` |
| `1064` | `0xede2...f971` | `LONG` | 2,037,819.25 USD | `914.31` | `2208.16` | `2228.80` | `1462.93` | 18,862.27 USD | `+0.93%` | `5X Cross` |
| `1066` | `0x9606...4e5d` | `SHORT` | 2,034,978.34 USD | `913.00` | `2478.70` | `2228.80` | `3786.82` | 228,075.26 USD | `+11.21%` | `20X Cross` |
| `1087` | `0x5f10...d49d` | `LONG` | 2,005,560.00 USD | `900.00` | `2249.83` | `2228.80` | `1815.47` | -19,293.47 USD | `-0.96%` | `25X Cross` |
| `1096` | `0x51f6...2b39` | `LONG` | 1,984,530.44 USD | `890.15` | `2226.49` | `2228.80` | `741.47` | 2,623.55 USD | `+0.13%` | `25X Cross` |
| `1175` | `0x2828...93a0` | `LONG` | 1,871,640.78 USD | `839.60` | `2242.41` | `2228.80` | `2192.48` | -11,091.41 USD | `-0.59%` | `25X Cross` |
| `1177` | `0xcd27...52a8` | `LONG` | 1,866,388.46 USD | `837.21` | `2553.56` | `2228.80` | `1403.16` | -271,476.31 USD | `-14.55%` | `2X Cross` |
| `1236` | `0x04a9...95aa` | `LONG` | 1,783,440.00 USD | `800.00` | `2595.13` | `2228.80` | `1872.60` | -292,666.74 USD | `-16.41%` | `5X Cross` |
| `1237` | `0x7737...bf66` | `SHORT` | 1,782,896.10 USD | `799.79` | `2494.83` | `2228.80` | `24878.17` | 212,449.92 USD | `+11.92%` | `15X Cross` |
| `1266` | `0x458d...ab3b` | `LONG` | 1,727,097.00 USD | `774.75` | `2740.41` | `2228.80` | `1886.92` | -396,032.18 USD | `-22.93%` | `3X Isolated` |
| `1325` | `0x3fc5...c0c1` | `SHORT` | 1,627,511.99 USD | `729.92` | `2702.11` | `2228.80` | `4708.32` | 344,830.21 USD | `+21.19%` | `25X Cross` |
| `1326` | `0xaa53...9cb7` | `LONG` | 1,627,482.30 USD | `730.34` | `2389.70` | `2228.80` | `1933.11` | -117,807.33 USD | `-7.24%` | `20X Cross` |
| `1340` | `0xa189...94d7` | `SHORT` | 1,605,149.98 USD | `719.98` | `2691.84` | `2228.80` | `2914.81` | 332,922.68 USD | `+20.74%` | `25X Cross` |
| `1352` | `0x2f93...4404` | `LONG` | 1,577,519.95 USD | `707.47` | `1700.45` | `2228.80` | `1368.55` | 374,493.58 USD | `+23.74%` | `4X Isolated` |
| `1364` | `0x5605...fe0f` | `SHORT` | 1,564,375.94 USD | `702.14` | `2566.90` | `2228.80` | `3092.08` | 237,956.71 USD | `+15.21%` | `20X Cross` |
| `1370` | `0x26e6...6b28` | `LONG` | 1,560,720.00 USD | `700.00` | `1835.24` | `2228.80` | `2042.98` | 276,048.47 USD | `+17.69%` | `20X Cross` |
| `1372` | `0x9599...c60a` | `LONG` | 1,559,645.14 USD | `699.74` | `2233.08` | `2228.80` | `0.000000` | -2,925.69 USD | `-0.19%` | `20X Cross` |
| `1375` | `0x0deb...0bc5` | `LONG` | 1,558,480.00 USD | `700.00` | `2071.05` | `2228.80` | `1597.14` | 108,744.21 USD | `+6.98%` | `20X Cross` |
| `1427` | `0xdbd1...29dd` | `SHORT` | 1,517,149.73 USD | `680.70` | `3030.57` | `2228.80` | `3790.94` | 545,771.39 USD | `+35.97%` | `6X Cross` |
| `1428` | `0x248e...6be2` | `SHORT` | 1,517,108.25 USD | `680.93` | `2282.89` | `2228.80` | `3385.39` | 37,377.41 USD | `+2.46%` | `20X Cross` |
| `1438` | `0x71e5...be04` | `LONG` | 1,510,112.70 USD | `677.67` | `2727.27` | `2228.80` | `1470.70` | -338,072.91 USD | `-22.39%` | `20X Cross` |
| `1442` | `0x0b23...f37b` | `LONG` | 1,504,170.00 USD | `675.00` | `2238.15` | `2228.80` | `594.10` | -6,586.64 USD | `-0.44%` | `5X Cross` |
| `1459` | `0xb8eb...1dd5` | `LONG` | 1,477,485.91 USD | `662.67` | `2232.77` | `2228.80` | `0.000000` | -2,103.64 USD | `-0.14%` | `25X Cross` |
| `1465` | `0x0cac...6170` | `SHORT` | 1,465,436.00 USD | `657.50` | `2146.55` | `2228.80` | `2839.16` | -54,073.80 USD | `-3.69%` | `20X Cross` |
| `1492` | `0xf00e...fe3d` | `SHORT` | 1,433,172.38 USD | `642.88` | `2333.21` | `2228.80` | `2486.86` | 66,805.59 USD | `+4.66%` | `20X Cross` |
| `1494` | `0xb15b...dbae` | `SHORT` | 1,432,580.22 USD | `642.64` | `2290.80` | `2228.80` | `2324.58` | 39,587.26 USD | `+2.76%` | `25X Cross` |
| `1499` | `0xffb2...5ed6` | `SHORT` | 1,427,884.74 USD | `640.77` | `2672.96` | `2228.80` | `2492.35` | 284,863.61 USD | `+19.95%` | `20X Cross` |
| `1506` | `0xef96...9383` | `LONG` | 1,425,007.13 USD | `639.36` | `2234.39` | `2228.80` | `0.000000` | -3,574.49 USD | `-0.25%` | `25X Cross` |
| `1514` | `0x8505...1821` | `SHORT` | 1,413,287.70 USD | `633.96` | `2239.93` | `2228.80` | `3888.25` | 6,743.90 USD | `+0.48%` | `20X Cross` |
| `1538` | `0xfce0...f4c0` | `SHORT` | 1,390,378.56 USD | `623.60` | `3129.61` | `2228.80` | `2807.76` | 561,248.03 USD | `+40.37%` | `20X Cross` |
| `1586` | `0x7050...5fff` | `SHORT` | 1,340,224.60 USD | `601.11` | `2245.52` | `2228.80` | `3270.96` | 9,575.51 USD | `+0.71%` | `25X Cross` |
| `1587` | `0xad02...eb65` | `LONG` | 1,338,962.61 USD | `600.62` | `2460.69` | `2228.80` | `1078.62` | -138,977.95 USD | `-10.38%` | `5X Cross` |
| `1589` | `0x24fb...ed0f` | `LONG` | 1,337,974.04 USD | `600.10` | `2199.85` | `2228.80` | `0.000000` | 17,850.61 USD | `+1.33%` | `15X Cross` |
| `1591` | `0x638f...f5f0` | `LONG` | 1,337,700.00 USD | `600.00` | `4011.50` | `2228.80` | `422.82` | -1,069,203.53 USD | `-79.93%` | `25X Cross` |
| `1667` | `0x9362...7d7c` | `SHORT` | 1,263,488.32 USD | `566.99` | `2226.19` | `2228.80` | `2518.61` | -1,252.50 USD | `-0.10%` | `20X Cross` |
| `1671` | `0xfb99...37f3` | `LONG` | 1,260,484.52 USD | `565.34` | `2362.35` | `2228.80` | `1253.87` | -75,051.84 USD | `-5.95%` | `3X Cross` |
| `1681` | `0x844b...7f42` | `SHORT` | 1,250,132.40 USD | `561.00` | `2026.17` | `2228.80` | `3037.52` | -113,448.99 USD | `-9.07%` | `25X Cross` |
| `1699` | `0xabe6...1d99` | `SHORT` | 1,239,499.72 USD | `556.00` | `2484.68` | `2228.80` | `3123.90` | 141,996.17 USD | `+11.46%` | `20X Cross` |
| `1702` | `0x2a76...9a53` | `LONG` | 1,237,494.89 USD | `555.03` | `2231.40` | `2228.80` | `0.000000` | -1,001.21 USD | `-0.08%` | `25X Cross` |
| `1709` | `0xbef3...0d3e` | `LONG` | 1,231,468.28 USD | `552.33` | `2233.44` | `2228.80` | `2068.58` | -2,122.54 USD | `-0.17%` | `20X Cross` |
| `1711` | `0xa70a...4be9` | `LONG` | 1,229,307.19 USD | `551.33` | `2251.37` | `2228.80` | `0.000000` | -11,950.81 USD | `-0.97%` | `20X Cross` |
| `1713` | `0x6a41...a3b9` | `LONG` | 1,227,164.73 USD | `550.69` | `2233.05` | `2228.80` | `2074.03` | -2,561.63 USD | `-0.21%` | `20X Cross` |
| `1715` | `0x825c...465e` | `LONG` | 1,226,115.00 USD | `550.00` | `2208.12` | `2228.80` | `1189.21` | 11,645.50 USD | `+0.95%` | `4X Cross` |
| `1719` | `0xad21...fb6a` | `LONG` | 1,219,915.49 USD | `547.26` | `2565.80` | `2228.80` | `1734.07` | -184,237.51 USD | `-15.10%` | `6X Cross` |
| `1757` | `0xfc66...ca06` | `SHORT` | 1,174,622.18 USD | `527.02` | `2275.19` | `2228.80` | `17002.19` | 24,453.61 USD | `+2.08%` | `20X Cross` |
| `1778` | `0x2e30...4cb5` | `SHORT` | 1,161,912.12 USD | `521.13` | `2316.80` | `2228.80` | `11922.57` | 45,442.86 USD | `+3.91%` | `2X Cross` |
| `1794` | `0x6dae...90de` | `SHORT` | 1,152,823.15 USD | `517.05` | `2292.28` | `2228.80` | `3857.12` | 32,410.26 USD | `+2.81%` | `25X Cross` |
| `1828` | `0x0089...2410` | `SHORT` | 1,130,568.94 USD | `507.35` | `2308.88` | `2228.80` | `3369.78` | 40,831.32 USD | `+3.61%` | `20X Cross` |
| `1841` | `0xa559...ff95` | `LONG` | 1,114,800.00 USD | `500.00` | `2260.68` | `2228.80` | `1055.91` | -15,544.36 USD | `-1.39%` | `20X Cross` |
| `1842` | `0x6936...9417` | `SHORT` | 1,114,800.00 USD | `500.00` | `2315.11` | `2228.80` | `2358.66` | 42,755.21 USD | `+3.84%` | `25X Isolated` |
| `1843` | `0xe282...df29` | `LONG` | 1,114,650.00 USD | `500.00` | `2309.84` | `2228.80` | `2045.06` | -40,274.21 USD | `-3.61%` | `10X Isolated` |
| `1844` | `0xb322...d51f` | `SHORT` | 1,114,650.00 USD | `500.00` | `2268.03` | `2228.80` | `3747.72` | 19,366.32 USD | `+1.74%` | `20X Cross` |
| `1845` | `0x89b2...9ca6` | `LONG` | 1,114,400.00 USD | `500.00` | `2363.45` | `2228.80` | `1622.40` | -67,327.42 USD | `-6.04%` | `25X Cross` |
| `1848` | `0x4044...794c` | `LONG` | 1,113,850.00 USD | `500.00` | `2260.80` | `2228.80` | `0.000000` | -16,550.00 USD | `-1.49%` | `25X Cross` |
| `1852` | `0x7298...7d6c` | `SHORT` | 1,110,673.68 USD | `498.15` | `3426.75` | `2228.80` | `5421.37` | 596,362.14 USD | `+53.69%` | `20X Cross` |
| `1862` | `0x0a97...347d` | `LONG` | 1,100,490.20 USD | `493.58` | `2259.32` | `2228.80` | `560.73` | -14,671.82 USD | `-1.33%` | `20X Cross` |
| `1863` | `0x9c68...7783` | `SHORT` | 1,099,879.07 USD | `493.31` | `2273.58` | `2228.80` | `3909.61` | 21,700.18 USD | `+1.97%` | `25X Cross` |
| `1874` | `0x404c...5f03` | `SHORT` | 1,091,006.55 USD | `489.79` | `2671.94` | `2228.80` | `5030.37` | 217,673.01 USD | `+19.95%` | `20X Cross` |
| `1877` | `0x321f...1c84` | `SHORT` | 1,087,883.93 USD | `488.02` | `2370.09` | `2228.80` | `3058.62` | 68,760.67 USD | `+6.32%` | `10X Cross` |
| `1883` | `0x94b6...e5b3` | `SHORT` | 1,083,640.09 USD | `486.05` | `2260.75` | `2228.80` | `2359.01` | 15,202.50 USD | `+1.40%` | `25X Cross` |
| `1903` | `0x7a76...b16d` | `LONG` | 1,058,736.25 USD | `474.83` | `2228.14` | `2228.80` | `2038.31` | 739.38 USD | `+0.07%` | `25X Cross` |
| `1941` | `0x82c6...fe42` | `LONG` | 1,031,190.00 USD | `462.50` | `2501.38` | `2228.80` | `2053.40` | -125,700.57 USD | `-12.19%` | `5X Isolated` |
| `1951` | `0xe330...77a1` | `SHORT` | 1,027,740.31 USD | `461.20` | `2206.97` | `2228.80` | `6448.55` | -9,882.94 USD | `-0.96%` | `20X Cross` |
| `1954` | `0x2de3...486d` | `LONG` | 1,025,955.36 USD | `460.40` | `2286.27` | `2228.80` | `1139.93` | -26,645.55 USD | `-2.60%` | `25X Cross` |
| `1958` | `0xd6e1...f256` | `LONG` | 1,022,397.39 USD | `458.64` | `2213.70` | `2228.80` | `913.94` | 7,106.51 USD | `+0.70%` | `25X Cross` |
| `1961` | `0x617e...0f97` | `SHORT` | 1,020,758.91 USD | `457.85` | `2205.60` | `2228.80` | `3355.83` | -10,915.08 USD | `-1.07%` | `10X Cross` |
| `1964` | `0x6e6f...82a6` | `LONG` | 1,019,802.62 USD | `457.47` | `2257.18` | `2228.80` | `82.30` | -12,784.89 USD | `-1.25%` | `20X Cross` |
| `1992` | `0xae55...2236` | `LONG` | 1,003,194.00 USD | `450.00` | `2510.21` | `2228.80` | `0.000000` | -126,403.50 USD | `-12.60%` | `25X Cross` |

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
  * 24H Horizon: Short MP=`2275.30` (Vol: 35,200,000.00 USD, Dist: `+2.08%`) | Long MP=`2174.37` (Vol: 35,800,000.00 USD, Dist: `--2.45%`)
  * 48H Horizon: Short MP=`2270.12` (Vol: 33,600,000.00 USD, Dist: `+1.85%`) | Long MP=`2174.00` (Vol: 35,800,000.00 USD, Dist: `--2.46%`)
  * 3D Horizon: Short MP=`2270.12` (Vol: 33,600,000.00 USD, Dist: `+1.85%`) | Long MP=`2174.00` (Vol: 35,800,000.00 USD, Dist: `--2.46%`)
  * 7D Horizon: Short MP=`2401.80` (Vol: 50,700,000.00 USD, Dist: `+7.76%`) | Long MP=`2175.27` (Vol: 44,800,000.00 USD, Dist: `--2.40%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
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
| `7D` | `Long Liquidation` | `1972.10` | 765,320,000.00 USD | 765,320,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1974.90` | 765,190,000.00 USD | 765,190,000.00 USD | 0.00 USD | 0.00 USD | 49,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1975.00` | 1,950,000.00 USD | 224,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1977.70` | 765,140,000.00 USD | 765,140,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1983.30` | 762,900,000.00 USD | 762,900,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1985.00` | 8,110,000.00 USD | 222,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1986.10` | 762,690,000.00 USD | 762,690,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1988.90` | 760,400,000.00 USD | 760,400,000.00 USD | 1,440,000.00 USD | 1,780,000.00 USD | 38,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1991.70` | 757,150,000.00 USD | 757,150,000.00 USD | 1,390,000.00 USD | 1,320,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1994.50` | 754,440,000.00 USD | 754,440,000.00 USD | 0.00 USD | 0.00 USD | 808,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1995.00` | 1,720,000.00 USD | 214,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1997.30` | 753,630,000.00 USD | 753,630,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1998.80` | 630,440,000.00 USD | 630,440,000.00 USD | 29,740.00 USD | 104,180.00 USD | 486,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2001.20` | 629,820,000.00 USD | 629,820,000.00 USD | 485,720.00 USD | 381,880.00 USD | 433,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2002.90` | 752,290,000.00 USD | 752,290,000.00 USD | 0.00 USD | 0.00 USD | 594,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2003.60` | 628,510,000.00 USD | 628,510,000.00 USD | 390,870.00 USD | 455,960.00 USD | 524,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2005.00` | 12,670,000.00 USD | 212,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2005.70` | 751,690,000.00 USD | 751,690,000.00 USD | 0.00 USD | 742,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2006.00` | 627,140,000.00 USD | 627,140,000.00 USD | 493,990.00 USD | 35,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2008.40` | 626,610,000.00 USD | 626,610,000.00 USD | 0.00 USD | 548,050.00 USD | 126,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2008.50` | 750,950,000.00 USD | 750,950,000.00 USD | 807,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2010.80` | 625,940,000.00 USD | 625,940,000.00 USD | 533,480.00 USD | 478,500.00 USD | 366,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2011.30` | 750,140,000.00 USD | 750,140,000.00 USD | 170,840.00 USD | 92,470.00 USD | 689,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2013.20` | 624,560,000.00 USD | 624,560,000.00 USD | 300,160.00 USD | 270,490.00 USD | 21,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2015.00` | 5,010,000.00 USD | 200,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2015.60` | 623,970,000.00 USD | 623,970,000.00 USD | 330,880.00 USD | 605,010.00 USD | 197,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2016.90` | 749,190,000.00 USD | 749,190,000.00 USD | 0.00 USD | 0.00 USD | 21,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2018.00` | 622,840,000.00 USD | 622,840,000.00 USD | 537,580.00 USD | 885,870.00 USD | 550,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2020.40` | 620,860,000.00 USD | 620,860,000.00 USD | 548,260.00 USD | 1,280,000.00 USD | 696,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2022.50` | 749,170,000.00 USD | 749,170,000.00 USD | 1,070,000.00 USD | 0.00 USD | 934,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2022.80` | 618,330,000.00 USD | 618,330,000.00 USD | 1,160,000.00 USD | 178,550.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2025.00` | 1,440,000.00 USD | 195,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2025.20` | 615,420,000.00 USD | 615,420,000.00 USD | 414,330.00 USD | 1,010,000.00 USD | 231,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2025.30` | 747,160,000.00 USD | 747,160,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2027.60` | 613,770,000.00 USD | 613,770,000.00 USD | 2,550,000.00 USD | 1,160,000.00 USD | 167,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2028.10` | 746,990,000.00 USD | 746,990,000.00 USD | 1,100,000.00 USD | 0.00 USD | 35,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2030.00` | 609,890,000.00 USD | 609,890,000.00 USD | 307,680.00 USD | 366,120.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2030.90` | 745,850,000.00 USD | 745,850,000.00 USD | 0.00 USD | 3,320,000.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2032.40` | 608,120,000.00 USD | 608,120,000.00 USD | 1,360,000.00 USD | 1,490,000.00 USD | 707,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2033.70` | 741,480,000.00 USD | 741,480,000.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2034.80` | 604,560,000.00 USD | 604,560,000.00 USD | 1,150,000.00 USD | 19,490.00 USD | 165,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2035.00` | 423,740.00 USD | 193,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2036.50` | 739,930,000.00 USD | 739,930,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2037.20` | 603,220,000.00 USD | 603,220,000.00 USD | 0.00 USD | 458,110.00 USD | 378,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2039.30` | 739,590,000.00 USD | 739,590,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2039.60` | 602,380,000.00 USD | 602,380,000.00 USD | 939,380.00 USD | 178,560.00 USD | 24,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2042.00` | 601,240,000.00 USD | 601,240,000.00 USD | 626,840.00 USD | 0.00 USD | 174,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2044.40` | 600,440,000.00 USD | 600,440,000.00 USD | 0.00 USD | 0.00 USD | 26,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2044.90` | 738,140,000.00 USD | 738,140,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2045.00` | 6,640,000.00 USD | 193,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2046.80` | 600,410,000.00 USD | 600,410,000.00 USD | 467,370.00 USD | 0.00 USD | 367,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2049.20` | 599,580,000.00 USD | 599,580,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2050.50` | 737,840,000.00 USD | 737,840,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2053.30` | 737,620,000.00 USD | 737,620,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2054.00` | 598,470,000.00 USD | 598,470,000.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2055.00` | 3,920,000.00 USD | 186,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2056.40` | 598,350,000.00 USD | 598,350,000.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2058.80` | 598,110,000.00 USD | 598,110,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2058.90` | 735,330,000.00 USD | 735,330,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2061.20` | 597,360,000.00 USD | 597,360,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2061.70` | 734,990,000.00 USD | 734,990,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2063.60` | 597,280,000.00 USD | 597,280,000.00 USD | 563,140.00 USD | 494,150.00 USD | 510,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2064.50` | 729,730,000.00 USD | 729,730,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 945,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2065.00` | 15,310,000.00 USD | 182,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2066.00` | 595,710,000.00 USD | 595,710,000.00 USD | 387,410.00 USD | 42,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2067.30` | 727,300,000.00 USD | 727,300,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 262,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2068.40` | 595,280,000.00 USD | 595,280,000.00 USD | 57,300.00 USD | 624,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2070.10` | 725,630,000.00 USD | 725,630,000.00 USD | 2,170,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2070.80` | 594,600,000.00 USD | 594,600,000.00 USD | 47,910.00 USD | 534,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2072.90` | 719,500,000.00 USD | 719,500,000.00 USD | 4,160,000.00 USD | 1,850,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2073.20` | 594,010,000.00 USD | 594,010,000.00 USD | 25,660.00 USD | 20,640.00 USD | 420,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 2,710,000.00 USD | 167,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2075.60` | 593,550,000.00 USD | 593,550,000.00 USD | 354,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2075.70` | 711,450,000.00 USD | 711,450,000.00 USD | 3,720,000.00 USD | 3,490,000.00 USD | 4,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2078.00` | 593,190,000.00 USD | 593,190,000.00 USD | 0.00 USD | 25,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2078.50` | 699,960,000.00 USD | 699,960,000.00 USD | 4,400,000.00 USD | 3,190,000.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2080.40` | 593,170,000.00 USD | 593,170,000.00 USD | 77,960.00 USD | 29,610.00 USD | 199,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2081.30` | 691,030,000.00 USD | 691,030,000.00 USD | 4,470,000.00 USD | 2,960,000.00 USD | 1,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2082.80` | 592,860,000.00 USD | 592,860,000.00 USD | 827,940.00 USD | 4,240.00 USD | 206,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2084.10` | 681,630,000.00 USD | 681,630,000.00 USD | 1,090,000.00 USD | 1,030,000.00 USD | 3,500,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 13,760,000.00 USD | 164,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2085.20` | 591,820,000.00 USD | 591,820,000.00 USD | 528,660.00 USD | 207,610.00 USD | 821,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2086.90` | 676,000,000.00 USD | 676,000,000.00 USD | 4,210,000.00 USD | 3,190,000.00 USD | 3,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2087.60` | 590,270,000.00 USD | 590,270,000.00 USD | 525,540.00 USD | 375,440.00 USD | 304,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2089.70` | 665,580,000.00 USD | 665,580,000.00 USD | 4,130,000.00 USD | 983,760.00 USD | 2,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2090.00` | 589,060,000.00 USD | 589,060,000.00 USD | 506,080.00 USD | 222,650.00 USD | 253,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2092.40` | 588,080,000.00 USD | 588,080,000.00 USD | 750,150.00 USD | 335,770.00 USD | 270,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2092.50` | 658,090,000.00 USD | 658,090,000.00 USD | 3,640,000.00 USD | 737,060.00 USD | 6,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2094.80` | 586,720,000.00 USD | 586,720,000.00 USD | 2,100,000.00 USD | 959,250.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 1,710,000.00 USD | 150,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2095.30` | 646,720,000.00 USD | 646,720,000.00 USD | 3,520,000.00 USD | 1,990,000.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2097.20` | 582,230,000.00 USD | 582,230,000.00 USD | 175,830.00 USD | 381,000.00 USD | 674,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2098.10` | 640,200,000.00 USD | 640,200,000.00 USD | 3,020,000.00 USD | 2,830,000.00 USD | 1,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2099.60` | 581,000,000.00 USD | 581,000,000.00 USD | 307,340.00 USD | 1,070,000.00 USD | 20,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2100.90` | 632,890,000.00 USD | 632,890,000.00 USD | 575,630.00 USD | 1,560,000.00 USD | 3,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2102.00` | 579,600,000.00 USD | 579,600,000.00 USD | 211,840.00 USD | 371,740.00 USD | 513,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2103.70` | 627,330,000.00 USD | 627,330,000.00 USD | 679,880.00 USD | 554,710.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2104.40` | 578,500,000.00 USD | 578,500,000.00 USD | 3,570,000.00 USD | 1,160,000.00 USD | 677,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 2,380,000.00 USD | 149,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2106.50` | 624,140,000.00 USD | 624,140,000.00 USD | 2,210,000.00 USD | 1,020,000.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2106.80` | 573,090,000.00 USD | 573,090,000.00 USD | 583,020.00 USD | 0.00 USD | 502,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2109.20` | 572,010,000.00 USD | 572,010,000.00 USD | 212,850.00 USD | 31,550.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2109.30` | 619,370,000.00 USD | 619,370,000.00 USD | 7,690,000.00 USD | 1,570,000.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2111.60` | 571,760,000.00 USD | 571,760,000.00 USD | 490,860.00 USD | 79,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2112.10` | 608,340,000.00 USD | 608,340,000.00 USD | 3,990,000.00 USD | 1,140,000.00 USD | 3,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2114.00` | 571,190,000.00 USD | 571,190,000.00 USD | 614,540.00 USD | 511,750.00 USD | 249,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2114.90` | 599,990,000.00 USD | 599,990,000.00 USD | 173,320.00 USD | 3,250,000.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 1,330,000.00 USD | 146,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2116.40` | 569,810,000.00 USD | 569,810,000.00 USD | 924,300.00 USD | 1,180,000.00 USD | 935,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2117.70` | 594,950,000.00 USD | 594,950,000.00 USD | 3,340,000.00 USD | 1,110,000.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2118.80` | 566,770,000.00 USD | 566,770,000.00 USD | 5,240,000.00 USD | 3,070,000.00 USD | 905,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2120.50` | 587,110,000.00 USD | 587,110,000.00 USD | 12,860,000.00 USD | 5,600,000.00 USD | 1,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2121.20` | 557,550,000.00 USD | 557,550,000.00 USD | 4,600,000.00 USD | 3,760,000.00 USD | 903,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2123.30` | 567,250,000.00 USD | 567,250,000.00 USD | 7,150,000.00 USD | 6,010,000.00 USD | 1,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2123.60` | 548,280,000.00 USD | 548,280,000.00 USD | 8,080,000.00 USD | 1,520,000.00 USD | 2,310,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 123,770,000.00 USD | 145,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2126.00` | 536,370,000.00 USD | 536,370,000.00 USD | 3,480,000.00 USD | 2,840,000.00 USD | 837,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2126.10` | 552,780,000.00 USD | 552,780,000.00 USD | 2,740,000.00 USD | 6,270,000.00 USD | 5,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2128.40` | 529,210,000.00 USD | 529,210,000.00 USD | 3,180,000.00 USD | 1,860,000.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2128.90` | 538,660,000.00 USD | 538,660,000.00 USD | 4,770,000.00 USD | 1,040,000.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2130.80` | 522,660,000.00 USD | 522,660,000.00 USD | 316,500.00 USD | 61,560.00 USD | 344,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2131.70` | 531,560,000.00 USD | 531,560,000.00 USD | 1,810,000.00 USD | 1,880,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2133.20` | 521,940,000.00 USD | 521,940,000.00 USD | 308,240.00 USD | 654,710.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2134.50` | 526,520,000.00 USD | 526,520,000.00 USD | 1,980,000.00 USD | 790,240.00 USD | 898,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 2,100,000.00 USD | 21,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2135.60` | 519,450,000.00 USD | 519,450,000.00 USD | 1,840,000.00 USD | 2,080,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2137.30` | 522,840,000.00 USD | 522,840,000.00 USD | 2,120,000.00 USD | 2,360,000.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2138.00` | 513,700,000.00 USD | 513,700,000.00 USD | 699,110.00 USD | 1,510,000.00 USD | 537,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2140.10` | 516,840,000.00 USD | 516,840,000.00 USD | 3,990,000.00 USD | 1,700,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2140.40` | 510,950,000.00 USD | 510,950,000.00 USD | 1,530,000.00 USD | 898,980.00 USD | 317,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2142.80` | 508,210,000.00 USD | 508,210,000.00 USD | 1,080,000.00 USD | 2,810,000.00 USD | 733,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2142.90` | 510,350,000.00 USD | 510,350,000.00 USD | 1,200,000.00 USD | 804,740.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 1,020,000.00 USD | 19,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2145.20` | 503,580,000.00 USD | 503,580,000.00 USD | 2,350,000.00 USD | 2,390,000.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2145.70` | 508,080,000.00 USD | 508,080,000.00 USD | 2,160,000.00 USD | 1,460,000.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2147.60` | 497,800,000.00 USD | 497,800,000.00 USD | 1,550,000.00 USD | 1,140,000.00 USD | 69,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2148.50` | 502,730,000.00 USD | 502,730,000.00 USD | 26,270.00 USD | 538,910.00 USD | 152,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2150.00` | 495,040,000.00 USD | 495,040,000.00 USD | 7,000,000.00 USD | 2,810,000.00 USD | 2,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2151.30` | 502,010,000.00 USD | 502,010,000.00 USD | 11,200,000.00 USD | 363,770.00 USD | 354,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2152.40` | 482,910,000.00 USD | 482,910,000.00 USD | 2,570,000.00 USD | 2,990,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2154.10` | 490,100,000.00 USD | 490,100,000.00 USD | 48,150.00 USD | 2,020,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2154.80` | 475,180,000.00 USD | 475,180,000.00 USD | 2,320,000.00 USD | 3,560,000.00 USD | 2,310,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 2,970,000.00 USD | 18,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2156.90` | 486,450,000.00 USD | 486,450,000.00 USD | 2,480,000.00 USD | 293,550.00 USD | 3,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2157.20` | 466,990,000.00 USD | 466,990,000.00 USD | 4,540,000.00 USD | 1,600,000.00 USD | 3,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2159.60` | 457,560,000.00 USD | 457,560,000.00 USD | 3,550,000.00 USD | 4,690,000.00 USD | 3,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2159.70` | 479,730,000.00 USD | 479,730,000.00 USD | 4,780,000.00 USD | 1,770,000.00 USD | 2,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2162.00` | 445,730,000.00 USD | 445,730,000.00 USD | 11,780,000.00 USD | 10,080,000.00 USD | 675,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2162.50` | 470,750,000.00 USD | 470,750,000.00 USD | 17,980,000.00 USD | 1,990,000.00 USD | 514,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2164.40` | 423,200,000.00 USD | 423,200,000.00 USD | 17,650,000.00 USD | 7,570,000.00 USD | 3,970,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 6,050,000.00 USD | 15,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2165.30` | 450,260,000.00 USD | 450,260,000.00 USD | 8,990,000.00 USD | 17,170,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2166.80` | 394,000,000.00 USD | 394,000,000.00 USD | 6,670,000.00 USD | 8,800,000.00 USD | 5,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2168.10` | 421,350,000.00 USD | 421,350,000.00 USD | 12,770,000.00 USD | 16,150,000.00 USD | 3,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2169.20` | 372,970,000.00 USD | 372,970,000.00 USD | 16,780,000.00 USD | 6,520,000.00 USD | 5,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2170.90` | 388,730,000.00 USD | 388,730,000.00 USD | 1,860,000.00 USD | 6,380,000.00 USD | 5,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2171.60` | 344,420,000.00 USD | 344,420,000.00 USD | 22,900,000.00 USD | 9,830,000.00 USD | 6,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2173.70` | 374,660,000.00 USD | 374,660,000.00 USD | 33,340,000.00 USD | 0.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2174.00` | 305,410,000.00 USD | 305,410,000.00 USD | 6,570,000.00 USD | 1,390,000.00 USD | 2,310,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 6,220,000.00 USD | 9,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2176.40` | 295,140,000.00 USD | 295,140,000.00 USD | 1,700,000.00 USD | 569,650.00 USD | 2,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2176.50` | 340,310,000.00 USD | 340,310,000.00 USD | 1,750,000.00 USD | 1,460,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2178.80` | 290,480,000.00 USD | 290,480,000.00 USD | 1,740,000.00 USD | 1,550,000.00 USD | 934,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2179.30` | 334,280,000.00 USD | 334,280,000.00 USD | 196,330.00 USD | 133,210.00 USD | 4,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2181.20` | 286,260,000.00 USD | 286,260,000.00 USD | 3,890,000.00 USD | 4,690,000.00 USD | 8,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2182.10` | 329,790,000.00 USD | 329,790,000.00 USD | 3,960,000.00 USD | 2,160,000.00 USD | 2,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2183.60` | 269,040,000.00 USD | 269,040,000.00 USD | 3,600,000.00 USD | 153,590.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2184.90` | 321,020,000.00 USD | 321,020,000.00 USD | 41,350,000.00 USD | 2,700,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2185.00` | 661,930.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2186.00` | 264,030,000.00 USD | 264,030,000.00 USD | 310,640.00 USD | 2,460,000.00 USD | 4,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2187.70` | 275,670,000.00 USD | 275,670,000.00 USD | 2,370,000.00 USD | 17,750,000.00 USD | 380,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2188.40` | 256,410,000.00 USD | 256,410,000.00 USD | 7,340,000.00 USD | 4,820,000.00 USD | 8,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2190.50` | 255,170,000.00 USD | 255,170,000.00 USD | 12,430,000.00 USD | 27,960,000.00 USD | 7,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2190.80` | 235,760,000.00 USD | 235,760,000.00 USD | 7,610,000.00 USD | 4,390,000.00 USD | 4,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2193.20` | 219,270,000.00 USD | 219,270,000.00 USD | 5,420,000.00 USD | 5,760,000.00 USD | 368,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2193.30` | 207,140,000.00 USD | 207,140,000.00 USD | 0.00 USD | 7,340,000.00 USD | 8,120,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 2,240,000.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2195.60` | 207,720,000.00 USD | 207,720,000.00 USD | 8,100,000.00 USD | 1,230,000.00 USD | 5,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2196.10` | 191,680,000.00 USD | 191,680,000.00 USD | 383,690.00 USD | 243,760.00 USD | 109,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2198.00` | 192,760,000.00 USD | 192,760,000.00 USD | 1,110,000.00 USD | 3,280,000.00 USD | 4,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2198.90` | 190,940,000.00 USD | 190,940,000.00 USD | 0.00 USD | 1,460,000.00 USD | 7,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2200.40` | 183,890,000.00 USD | 183,890,000.00 USD | 7,310,000.00 USD | 3,670,000.00 USD | 10,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2201.70` | 182,050,000.00 USD | 182,050,000.00 USD | 9,110,000.00 USD | 266,430.00 USD | 18,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2202.80` | 162,450,000.00 USD | 162,450,000.00 USD | 14,180,000.00 USD | 11,600,000.00 USD | 14,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2204.50` | 154,040,000.00 USD | 154,040,000.00 USD | 5,350,000.00 USD | 4,330,000.00 USD | 4,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 455,190.00 USD | 455,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2205.20` | 121,940,000.00 USD | 121,940,000.00 USD | 7,470,000.00 USD | 4,810,000.00 USD | 2,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2207.30` | 139,930,000.00 USD | 139,930,000.00 USD | 17,370,000.00 USD | 3,390,000.00 USD | 3,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2207.60` | 106,800,000.00 USD | 106,800,000.00 USD | 12,580,000.00 USD | 4,890,000.00 USD | 2,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2210.00` | 87,270,000.00 USD | 87,270,000.00 USD | 4,040,000.00 USD | 7,220,000.00 USD | 6,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2210.10` | 115,520,000.00 USD | 115,520,000.00 USD | 7,000,000.00 USD | 0.00 USD | 11,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2212.40` | 69,730,000.00 USD | 69,730,000.00 USD | 11,460,000.00 USD | 5,440,000.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2212.90` | 97,220,000.00 USD | 97,220,000.00 USD | 1,710,000.00 USD | 1,980,000.00 USD | 8,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2214.80` | 50,880,000.00 USD | 50,880,000.00 USD | 3,530,000.00 USD | 3,900,000.00 USD | 102,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 412.88 USD | 412.88 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2215.70` | 84,680,000.00 USD | 84,680,000.00 USD | 0.00 USD | 0.00 USD | 565,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2217.20` | 43,340,000.00 USD | 43,340,000.00 USD | 472,330.00 USD | 2,460,000.00 USD | 4,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2218.50` | 84,110,000.00 USD | 84,110,000.00 USD | 22,400,000.00 USD | 487,520.00 USD | 218,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2219.60` | 36,420,000.00 USD | 36,420,000.00 USD | 6,620,000.00 USD | 3,090,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2221.30` | 61,010,000.00 USD | 61,010,000.00 USD | 0.00 USD | 12,220,000.00 USD | 18,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2222.00` | 24,890,000.00 USD | 24,890,000.00 USD | 0.00 USD | 4,090,000.00 USD | 2,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2224.10` | 30,760,000.00 USD | 30,760,000.00 USD | 0.00 USD | 0.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2224.40` | 18,190,000.00 USD | 18,190,000.00 USD | 374,450.00 USD | 300,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2225.00` | 778.75 USD | 778.75 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2226.80` | 17,510,000.00 USD | 17,510,000.00 USD | 0.00 USD | 0.00 USD | 3,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2226.90` | 29,250,000.00 USD | 29,250,000.00 USD | 447,040.00 USD | 0.00 USD | 7,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2229.20` | 14,060,000.00 USD | 14,060,000.00 USD | 0.00 USD | 12,070,000.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2229.70` | 21,100,000.00 USD | 21,100,000.00 USD | 2,020,000.00 USD | 0.00 USD | 19,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2231.60` | 40,790,000.00 USD | 40,790,000.00 USD | 40,420,000.00 USD | 0.00 USD | 369,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2232.50` | 959,630.00 USD | 959,630.00 USD | 0.00 USD | 0.00 USD | 959,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2234.00` | 40,830,000.00 USD | 40,830,000.00 USD | 0.00 USD | 0.00 USD | 41,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2235.00` | 2,120.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2235.30` | 26,210,000.00 USD | 26,210,000.00 USD | 3,260,000.00 USD | 21,640,000.00 USD | 350,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2236.40` | 47,630,000.00 USD | 47,630,000.00 USD | 6,800,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2238.10` | 38,720,000.00 USD | 38,720,000.00 USD | 12,520,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2238.80` | 56,050,000.00 USD | 56,050,000.00 USD | 8,420,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2240.90` | 70,640,000.00 USD | 70,640,000.00 USD | 31,920,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2241.20` | 56,180,000.00 USD | 56,180,000.00 USD | 81,700.00 USD | 0.00 USD | 50,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2243.60` | 57,080,000.00 USD | 57,080,000.00 USD | 327,260.00 USD | 569,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2243.70` | 73,450,000.00 USD | 73,450,000.00 USD | 2,540,000.00 USD | 268,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2246.00` | 71,350,000.00 USD | 71,350,000.00 USD | 5,630,000.00 USD | 4,370,000.00 USD | 4,280,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2246.50` | 90,310,000.00 USD | 90,310,000.00 USD | 7,160,000.00 USD | 1,300,000.00 USD | 8,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2248.40` | 86,320,000.00 USD | 86,320,000.00 USD | 3,770,000.00 USD | 5,270,000.00 USD | 5,930,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2249.30` | 101,630,000.00 USD | 101,630,000.00 USD | 3,080,000.00 USD | 6,990,000.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2250.80` | 94,580,000.00 USD | 94,580,000.00 USD | 7,670,000.00 USD | 505,690.00 USD | 77,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2252.10` | 123,350,000.00 USD | 123,350,000.00 USD | 10,050,000.00 USD | 11,670,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2253.20` | 100,330,000.00 USD | 100,330,000.00 USD | 943,690.00 USD | 3,380,000.00 USD | 1,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2254.90` | 140,400,000.00 USD | 140,400,000.00 USD | 10,050,000.00 USD | 6,600,000.00 USD | 406,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2255.00` | 20,070.00 USD | 22,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2255.60` | 132,150,000.00 USD | 132,150,000.00 USD | 16,490,000.00 USD | 6,560,000.00 USD | 8,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2257.70` | 180,210,000.00 USD | 180,210,000.00 USD | 20,510,000.00 USD | 12,290,000.00 USD | 7,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2258.00` | 160,670,000.00 USD | 160,670,000.00 USD | 18,030,000.00 USD | 7,740,000.00 USD | 2,740,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2260.40` | 180,880,000.00 USD | 180,880,000.00 USD | 8,330,000.00 USD | 9,340,000.00 USD | 2,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2260.50` | 184,320,000.00 USD | 184,320,000.00 USD | 0.00 USD | 0.00 USD | 4,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2262.80` | 211,480,000.00 USD | 211,480,000.00 USD | 14,550,000.00 USD | 9,830,000.00 USD | 6,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2263.30` | 192,920,000.00 USD | 192,920,000.00 USD | 6,720,000.00 USD | 1,460,000.00 USD | 428,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2265.00` | 13,280.00 USD | 36,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2265.20` | 237,350,000.00 USD | 237,350,000.00 USD | 4,700,000.00 USD | 9,750,000.00 USD | 11,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2266.10` | 207,410,000.00 USD | 207,410,000.00 USD | 0.00 USD | 8,160,000.00 USD | 6,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2267.60` | 267,890,000.00 USD | 267,890,000.00 USD | 11,510,000.00 USD | 9,470,000.00 USD | 9,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2268.90` | 227,380,000.00 USD | 227,380,000.00 USD | 11,010,000.00 USD | 133,210.00 USD | 8,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2270.00` | 313,470,000.00 USD | 313,470,000.00 USD | 17,860,000.00 USD | 8,740,000.00 USD | 18,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2271.70` | 265,500,000.00 USD | 265,500,000.00 USD | 18,240,000.00 USD | 3,640,000.00 USD | 16,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2272.40` | 340,010,000.00 USD | 340,010,000.00 USD | 15,430,000.00 USD | 5,600,000.00 USD | 5,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2274.50` | 292,030,000.00 USD | 292,030,000.00 USD | 19,630,000.00 USD | 6,900,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2274.80` | 375,290,000.00 USD | 375,290,000.00 USD | 24,410,000.00 USD | 8,560,000.00 USD | 2,320,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2275.00` | 1,610,000.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2277.20` | 417,300,000.00 USD | 417,300,000.00 USD | 10,420,000.00 USD | 18,400,000.00 USD | 13,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2277.30` | 309,390,000.00 USD | 309,390,000.00 USD | 6,890,000.00 USD | 0.00 USD | 10,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2279.60` | 453,870,000.00 USD | 453,870,000.00 USD | 16,500,000.00 USD | 8,760,000.00 USD | 11,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2280.10` | 359,200,000.00 USD | 359,200,000.00 USD | 854,200.00 USD | 45,440,000.00 USD | 3,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2282.00` | 506,500,000.00 USD | 506,500,000.00 USD | 26,040,000.00 USD | 23,280,000.00 USD | 3,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2282.90` | 448,500,000.00 USD | 448,500,000.00 USD | 5,600,000.00 USD | 69,990,000.00 USD | 13,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2284.40` | 550,690,000.00 USD | 550,690,000.00 USD | 21,550,000.00 USD | 11,720,000.00 USD | 10,920,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2285.00` | 183,890.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2285.70` | 458,130,000.00 USD | 458,130,000.00 USD | 1,010,000.00 USD | 8,400,000.00 USD | 214,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2286.80` | 581,110,000.00 USD | 581,110,000.00 USD | 9,570,000.00 USD | 12,590,000.00 USD | 8,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2288.50` | 490,760,000.00 USD | 490,760,000.00 USD | 8,380,000.00 USD | 9,320,000.00 USD | 14,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2289.20` | 600,410,000.00 USD | 600,410,000.00 USD | 8,210,000.00 USD | 9,130,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2291.30` | 497,970,000.00 USD | 497,970,000.00 USD | 4,310,000.00 USD | 517,070.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2291.60` | 638,410,000.00 USD | 638,410,000.00 USD | 20,470,000.00 USD | 9,410,000.00 USD | 8,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2294.00` | 672,690,000.00 USD | 672,690,000.00 USD | 15,480,000.00 USD | 6,720,000.00 USD | 12,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2294.10` | 518,250,000.00 USD | 518,250,000.00 USD | 8,930,000.00 USD | 1,490,000.00 USD | 9,850,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2295.00` | 3,010,000.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2296.40` | 703,570,000.00 USD | 703,570,000.00 USD | 13,600,000.00 USD | 12,430,000.00 USD | 4,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2296.90` | 573,730,000.00 USD | 573,730,000.00 USD | 31,630,000.00 USD | 8,070,000.00 USD | 15,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2298.80` | 756,530,000.00 USD | 756,530,000.00 USD | 27,220,000.00 USD | 15,600,000.00 USD | 10,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2299.70` | 616,650,000.00 USD | 616,650,000.00 USD | 16,200,000.00 USD | 20,940,000.00 USD | 5,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2301.20` | 783,880,000.00 USD | 783,880,000.00 USD | 9,830,000.00 USD | 6,810,000.00 USD | 10,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2302.50` | 671,310,000.00 USD | 671,310,000.00 USD | 26,960,000.00 USD | 10,860,000.00 USD | 16,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2303.60` | 815,420,000.00 USD | 815,420,000.00 USD | 14,740,000.00 USD | 10,150,000.00 USD | 6,650,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2305.00` | 670,610.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2305.30` | 695,470,000.00 USD | 695,470,000.00 USD | 6,340,000.00 USD | 6,960,000.00 USD | 10,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2306.00` | 850,240,000.00 USD | 850,240,000.00 USD | 13,720,000.00 USD | 12,830,000.00 USD | 8,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2308.10` | 699,630,000.00 USD | 699,630,000.00 USD | 1,240,000.00 USD | 2,780,000.00 USD | 134,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2308.40` | 857,590,000.00 USD | 857,590,000.00 USD | 2,860,000.00 USD | 3,320,000.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2310.80` | 874,630,000.00 USD | 874,630,000.00 USD | 5,990,000.00 USD | 241,880.00 USD | 10,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2310.90` | 729,960,000.00 USD | 729,960,000.00 USD | 11,460,000.00 USD | 2,720,000.00 USD | 16,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2313.20` | 892,370,000.00 USD | 892,370,000.00 USD | 6,680,000.00 USD | 8,970,000.00 USD | 2,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2313.70` | 736,920,000.00 USD | 736,920,000.00 USD | 1,200,000.00 USD | 3,490,000.00 USD | 2,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2315.00` | 5,890,000.00 USD | 11,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2315.60` | 926,890,000.00 USD | 926,890,000.00 USD | 10,440,000.00 USD | 16,170,000.00 USD | 7,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2316.50` | 746,540,000.00 USD | 746,540,000.00 USD | 1,020,000.00 USD | 7,560,000.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2318.00` | 938,210,000.00 USD | 938,210,000.00 USD | 2,450,000.00 USD | 6,630,000.00 USD | 2,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2319.30` | 775,920,000.00 USD | 775,920,000.00 USD | 5,530,000.00 USD | 15,960,000.00 USD | 7,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2320.40` | 961,940,000.00 USD | 961,940,000.00 USD | 9,330,000.00 USD | 11,570,000.00 USD | 2,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2322.10` | 781,770,000.00 USD | 781,770,000.00 USD | 2,300,000.00 USD | 3,450,000.00 USD | 108,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2322.80` | 979,770,000.00 USD | 979,770,000.00 USD | 3,860,000.00 USD | 9,300,000.00 USD | 4,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2324.90` | 799,340,000.00 USD | 799,340,000.00 USD | 4,680,000.00 USD | 2,770,000.00 USD | 10,120,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2325.00` | 1,780,000.00 USD | 13,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2325.20` | 992,950,000.00 USD | 992,950,000.00 USD | 2,550,000.00 USD | 9,140,000.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2327.60` | 999,400,000.00 USD | 999,400,000.00 USD | 494,310.00 USD | 1,410,000.00 USD | 4,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2327.70` | 816,650,000.00 USD | 816,650,000.00 USD | 9,330,000.00 USD | 0.00 USD | 7,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2330.00` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 10,740,000.00 USD | 3,070,000.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2330.50` | 832,920,000.00 USD | 832,920,000.00 USD | 15,800,000.00 USD | 363,770.00 USD | 107,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2332.40` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 2,430,000.00 USD | 1,710,000.00 USD | 6,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2333.30` | 864,180,000.00 USD | 864,180,000.00 USD | 20,270,000.00 USD | 9,410,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2334.80` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 8,950,000.00 USD | 5,310,000.00 USD | 5,680,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2335.00` | 427,950.00 USD | 13,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2336.10` | 911,270,000.00 USD | 911,270,000.00 USD | 24,310,000.00 USD | 11,020,000.00 USD | 11,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2337.20` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 11,530,000.00 USD | 1,400,000.00 USD | 5,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2338.90` | 937,670,000.00 USD | 937,670,000.00 USD | 14,040,000.00 USD | 0.00 USD | 12,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2339.60` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 11,750,000.00 USD | 6,440,000.00 USD | 12,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2341.70` | 976,960,000.00 USD | 976,960,000.00 USD | 7,470,000.00 USD | 17,820,000.00 USD | 14,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2342.00` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 4,950,000.00 USD | 1,960,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2344.40` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 7,670,000.00 USD | 10,300,000.00 USD | 5,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2344.50` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 3,630,000.00 USD | 16,920,000.00 USD | 5,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2345.00` | 417,120.00 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2346.80` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 3,930,000.00 USD | 3,250,000.00 USD | 5,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2347.30` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 0.00 USD | 8,220,000.00 USD | 21,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2349.20` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 11,390,000.00 USD | 4,080,000.00 USD | 5,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2350.10` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 1,630,000.00 USD | 18,920,000.00 USD | 14,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2351.60` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 19,450,000.00 USD | 4,850,000.00 USD | 7,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2352.90` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 2,710,000.00 USD | 33,320,000.00 USD | 5,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2354.00` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 2,640,000.00 USD | 5,600,000.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 1,790,000.00 USD | 15,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2355.70` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 18,560,000.00 USD | 14,360,000.00 USD | 2,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2356.40` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 5,770,000.00 USD | 1,070,000.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2358.50` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 6,870,000.00 USD | 512,220.00 USD | 4,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2358.80` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 4,520,000.00 USD | 5,650,000.00 USD | 7,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2361.20` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 8,330,000.00 USD | 8,630,000.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2361.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 2,430,000.00 USD | 3,430,000.00 USD | 374,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2363.60` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 5,120,000.00 USD | 2,870,000.00 USD | 8,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2364.10` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 4,570,000.00 USD | 373,740.00 USD | 9,630,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 5,520,000.00 USD | 21,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2366.00` | 1,270,000,000.00 USD | 1,270,000,000.00 USD | 4,830,000.00 USD | 827,140.00 USD | 2,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2366.90` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 6,340,000.00 USD | 1,310,000.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2368.40` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 4,680,000.00 USD | 3,870,000.00 USD | 3,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2369.70` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 24,570,000.00 USD | 475,460.00 USD | 13,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2370.80` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 14,000,000.00 USD | 5,860,000.00 USD | 4,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2372.50` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 15,970,000.00 USD | 0.00 USD | 44,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2373.20` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 11,920,000.00 USD | 2,030,000.00 USD | 5,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 885,750.00 USD | 22,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2375.30` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 9,700,000.00 USD | 121,480.00 USD | 12,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2375.60` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 7,590,000.00 USD | 1,830,000.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2378.00` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 1,460,000.00 USD | 1,920,000.00 USD | 5,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2378.10` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 11,180,000.00 USD | 7,790,000.00 USD | 21,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2380.40` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 6,310,000.00 USD | 5,360,000.00 USD | 3,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2380.90` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 4,540,000.00 USD | 2,540,000.00 USD | 16,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2382.80` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 15,730,000.00 USD | 9,540,000.00 USD | 11,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2383.70` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 8,720,000.00 USD | 16,800,000.00 USD | 33,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 726,570.00 USD | 22,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2385.20` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 7,510,000.00 USD | 11,630,000.00 USD | 4,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2386.50` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 17,480,000.00 USD | 37,020,000.00 USD | 38,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2387.60` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 9,800,000.00 USD | 5,870,000.00 USD | 3,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2389.30` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 3,900,000.00 USD | 32,580,000.00 USD | 31,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2390.00` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 4,390,000.00 USD | 3,120,000.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2392.10` | 1,690,000,000.00 USD | 1,690,000,000.00 USD | 17,810,000.00 USD | 45,470,000.00 USD | 39,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2392.40` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 2,380,000.00 USD | 2,850,000.00 USD | 3,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2394.80` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 2,380,000.00 USD | 2,780,000.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2394.90` | 1,800,000,000.00 USD | 1,800,000,000.00 USD | 46,520,000.00 USD | 28,270,000.00 USD | 28,920,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 4,840,000.00 USD | 27,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2397.20` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 64,150.00 USD | 3,730,000.00 USD | 2,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2397.70` | 1,890,000,000.00 USD | 1,890,000,000.00 USD | 30,700,000.00 USD | 35,140,000.00 USD | 25,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2399.60` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 2,150,000.00 USD | 680,850.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2400.50` | 1,990,000,000.00 USD | 1,990,000,000.00 USD | 49,430,000.00 USD | 26,510,000.00 USD | 21,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2402.00` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 1,140,000.00 USD | 0.00 USD | 543,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2403.30` | 2,090,000,000.00 USD | 2,090,000,000.00 USD | 51,300,000.00 USD | 23,260,000.00 USD | 29,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2404.40` | 1,490,000,000.00 USD | 1,490,000,000.00 USD | 3,690,000.00 USD | 3,730,000.00 USD | 2,060,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 156,110.00 USD | 27,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2406.10` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 25,510,000.00 USD | 29,700,000.00 USD | 17,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2406.80` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 9,080,000.00 USD | 3,500,000.00 USD | 4,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2408.90` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 29,270,000.00 USD | 25,210,000.00 USD | 24,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2409.20` | 1,510,000,000.00 USD | 1,510,000,000.00 USD | 3,280,000.00 USD | 3,590,000.00 USD | 3,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2411.60` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 5,500,000.00 USD | 3,590,000.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2411.70` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 15,360,000.00 USD | 23,030,000.00 USD | 18,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2414.00` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 2,260,000.00 USD | 644,590.00 USD | 762,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2414.50` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 19,450,000.00 USD | 19,740,000.00 USD | 21,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 143,210.00 USD | 28,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2416.40` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 2,870,000.00 USD | 2,240,000.00 USD | 3,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2417.30` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 22,080,000.00 USD | 4,990,000.00 USD | 20,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2418.80` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 2,610,000.00 USD | 1,590,000.00 USD | 2,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2420.10` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 31,570,000.00 USD | 20,780,000.00 USD | 9,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2421.20` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 6,090,000.00 USD | 4,540,000.00 USD | 5,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2422.90` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 15,870,000.00 USD | 19,430,000.00 USD | 22,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2423.60` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 526,140.00 USD | 1,140,000.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 243,520.00 USD | 28,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2425.70` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 15,760,000.00 USD | 13,390,000.00 USD | 15,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2426.00` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 1,470,000.00 USD | 1,010,000.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2428.40` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 1,290,000.00 USD | 1,180,000.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2428.50` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 13,950,000.00 USD | 8,940,000.00 USD | 10,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2430.80` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 1,910,000.00 USD | 2,400,000.00 USD | 460,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2431.30` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 8,950,000.00 USD | 12,070,000.00 USD | 8,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2433.20` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 2,980,000.00 USD | 1,680,000.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2434.10` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 13,720,000.00 USD | 4,490,000.00 USD | 3,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 187,830.00 USD | 28,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2435.60` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 1,920,000.00 USD | 623,860.00 USD | 401,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2436.90` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 6,210,000.00 USD | 6,860,000.00 USD | 6,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2438.00` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 1,050,000.00 USD | 517,090.00 USD | 15,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2439.70` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 13,650,000.00 USD | 5,510,000.00 USD | 3,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2440.40` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 1,230,000.00 USD | 1,190,000.00 USD | 858,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2442.50` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 5,050,000.00 USD | 4,770,000.00 USD | 7,900,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2442.80` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 1,040,000.00 USD | 42,810.00 USD | 269,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 135,670.00 USD | 28,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2445.20` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 13,780.00 USD | 703,990.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2445.30` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 9,990,000.00 USD | 8,050,000.00 USD | 10,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2447.60` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 1,210,000.00 USD | 650,590.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2448.10` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 7,630,000.00 USD | 3,230,000.00 USD | 15,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2450.00` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 472,590.00 USD | 307,670.00 USD | 26,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2450.90` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 11,570,000.00 USD | 7,800,000.00 USD | 7,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2452.40` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 3,200,000.00 USD | 1,620,000.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2453.70` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 4,220,000.00 USD | 2,980,000.00 USD | 3,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2454.80` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 2,270,000.00 USD | 2,210,000.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 5,180,000.00 USD | 33,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2456.50` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 8,170,000.00 USD | 6,240,000.00 USD | 7,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2457.20` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 1,720,000.00 USD | 1,920,000.00 USD | 841,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2459.30` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 3,390,000.00 USD | 5,570,000.00 USD | 5,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2459.60` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 1,580,000.00 USD | 1,430,000.00 USD | 383,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2462.00` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 551,660.00 USD | 829,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2462.10` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 4,880,000.00 USD | 6,420,000.00 USD | 5,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2464.10` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 303,600.00 USD | 280,900.00 USD | 179,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2464.90` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 6,130,000.00 USD | 3,130,000.00 USD | 2,800,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 67,480,000.00 USD | 101,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2467.70` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 3,400,000.00 USD | 1,870,000.00 USD | 45,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2470.50` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 2,410,000.00 USD | 2,050,000.00 USD | 522,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2473.30` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 6,230,000.00 USD | 2,920,000.00 USD | 3,180,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 197,560.00 USD | 101,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2476.10` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 2,600,000.00 USD | 1,680,000.00 USD | 872,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2478.90` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 3,150,000.00 USD | 4,160,000.00 USD | 540,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2481.70` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 601,420.00 USD | 3,680,000.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2484.50` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 52,650.00 USD | 101,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2487.30` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 275,450.00 USD | 211,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2490.10` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 385,480.00 USD | 14,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2492.90` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 2,960,000.00 USD | 1,020,000.00 USD | 1,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 2,220,000.00 USD | 103,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2495.10` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 773,650.00 USD | 736,470.00 USD | 2,640,000.00 USD | `Tier 1 CEX` |
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
| `7D` | `1972.10` | 765,320,000.00 USD | 0.00 USD | 765,320,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD |
| `7D` | `1974.90` | 765,190,000.00 USD | 0.00 USD | 765,190,000.00 USD | 0.00 USD | 0.00 USD | 49,530.00 USD |
| `7D` | `1977.70` | 765,140,000.00 USD | 0.00 USD | 765,140,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1983.30` | 762,900,000.00 USD | 0.00 USD | 762,900,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD |
| `7D` | `1986.10` | 762,690,000.00 USD | 0.00 USD | 762,690,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1988.90` | 760,400,000.00 USD | 0.00 USD | 760,400,000.00 USD | 1,440,000.00 USD | 1,780,000.00 USD | 38,060.00 USD |
| `7D` | `1991.70` | 757,150,000.00 USD | 0.00 USD | 757,150,000.00 USD | 1,390,000.00 USD | 1,320,000.00 USD | 0.00 USD |
| `7D` | `1994.50` | 754,440,000.00 USD | 0.00 USD | 754,440,000.00 USD | 0.00 USD | 0.00 USD | 808,380.00 USD |
| `7D` | `1997.30` | 753,630,000.00 USD | 0.00 USD | 753,630,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1998.80` | 630,440,000.00 USD | 0.00 USD | 630,440,000.00 USD | 29,740.00 USD | 104,180.00 USD | 486,830.00 USD |
| `1D` | `2001.20` | 629,820,000.00 USD | 0.00 USD | 629,820,000.00 USD | 485,720.00 USD | 381,880.00 USD | 433,510.00 USD |
| `7D` | `2002.90` | 752,290,000.00 USD | 0.00 USD | 752,290,000.00 USD | 0.00 USD | 0.00 USD | 594,510.00 USD |
| `1D` | `2003.60` | 628,510,000.00 USD | 0.00 USD | 628,510,000.00 USD | 390,870.00 USD | 455,960.00 USD | 524,290.00 USD |
| `7D` | `2005.70` | 751,690,000.00 USD | 0.00 USD | 751,690,000.00 USD | 0.00 USD | 742,090.00 USD | 0.00 USD |
| `1D` | `2006.00` | 627,140,000.00 USD | 0.00 USD | 627,140,000.00 USD | 493,990.00 USD | 35,460.00 USD | 0.00 USD |
| `1D` | `2008.40` | 626,610,000.00 USD | 0.00 USD | 626,610,000.00 USD | 0.00 USD | 548,050.00 USD | 126,940.00 USD |
| `7D` | `2008.50` | 750,950,000.00 USD | 0.00 USD | 750,950,000.00 USD | 807,770.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2010.80` | 625,940,000.00 USD | 0.00 USD | 625,940,000.00 USD | 533,480.00 USD | 478,500.00 USD | 366,100.00 USD |
| `7D` | `2011.30` | 750,140,000.00 USD | 0.00 USD | 750,140,000.00 USD | 170,840.00 USD | 92,470.00 USD | 689,450.00 USD |
| `1D` | `2013.20` | 624,560,000.00 USD | 0.00 USD | 624,560,000.00 USD | 300,160.00 USD | 270,490.00 USD | 21,620.00 USD |
| `1D` | `2015.60` | 623,970,000.00 USD | 0.00 USD | 623,970,000.00 USD | 330,880.00 USD | 605,010.00 USD | 197,000.00 USD |
| `7D` | `2016.90` | 749,190,000.00 USD | 0.00 USD | 749,190,000.00 USD | 0.00 USD | 0.00 USD | 21,830.00 USD |
| `1D` | `2018.00` | 622,840,000.00 USD | 0.00 USD | 622,840,000.00 USD | 537,580.00 USD | 885,870.00 USD | 550,280.00 USD |
| `1D` | `2020.40` | 620,860,000.00 USD | 0.00 USD | 620,860,000.00 USD | 548,260.00 USD | 1,280,000.00 USD | 696,790.00 USD |
| `7D` | `2022.50` | 749,170,000.00 USD | 0.00 USD | 749,170,000.00 USD | 1,070,000.00 USD | 0.00 USD | 934,340.00 USD |
| `1D` | `2022.80` | 618,330,000.00 USD | 0.00 USD | 618,330,000.00 USD | 1,160,000.00 USD | 178,550.00 USD | 1,570,000.00 USD |
| `1D` | `2025.20` | 615,420,000.00 USD | 0.00 USD | 615,420,000.00 USD | 414,330.00 USD | 1,010,000.00 USD | 231,680.00 USD |
| `7D` | `2025.30` | 747,160,000.00 USD | 0.00 USD | 747,160,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD |
| `1D` | `2027.60` | 613,770,000.00 USD | 0.00 USD | 613,770,000.00 USD | 2,550,000.00 USD | 1,160,000.00 USD | 167,580.00 USD |
| `7D` | `2028.10` | 746,990,000.00 USD | 0.00 USD | 746,990,000.00 USD | 1,100,000.00 USD | 0.00 USD | 35,180.00 USD |
| `1D` | `2030.00` | 609,890,000.00 USD | 0.00 USD | 609,890,000.00 USD | 307,680.00 USD | 366,120.00 USD | 1,100,000.00 USD |
| `7D` | `2030.90` | 745,850,000.00 USD | 0.00 USD | 745,850,000.00 USD | 0.00 USD | 3,320,000.00 USD | 1,050,000.00 USD |
| `1D` | `2032.40` | 608,120,000.00 USD | 0.00 USD | 608,120,000.00 USD | 1,360,000.00 USD | 1,490,000.00 USD | 707,170.00 USD |
| `7D` | `2033.70` | 741,480,000.00 USD | 0.00 USD | 741,480,000.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD |
| `1D` | `2034.80` | 604,560,000.00 USD | 0.00 USD | 604,560,000.00 USD | 1,150,000.00 USD | 19,490.00 USD | 165,760.00 USD |
| `7D` | `2036.50` | 739,930,000.00 USD | 0.00 USD | 739,930,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD |
| `1D` | `2037.20` | 603,220,000.00 USD | 0.00 USD | 603,220,000.00 USD | 0.00 USD | 458,110.00 USD | 378,700.00 USD |
| `7D` | `2039.30` | 739,590,000.00 USD | 0.00 USD | 739,590,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2039.60` | 602,380,000.00 USD | 0.00 USD | 602,380,000.00 USD | 939,380.00 USD | 178,560.00 USD | 24,030.00 USD |
| `1D` | `2042.00` | 601,240,000.00 USD | 0.00 USD | 601,240,000.00 USD | 626,840.00 USD | 0.00 USD | 174,290.00 USD |
| `1D` | `2044.40` | 600,440,000.00 USD | 0.00 USD | 600,440,000.00 USD | 0.00 USD | 0.00 USD | 26,280.00 USD |
| `7D` | `2044.90` | 738,140,000.00 USD | 0.00 USD | 738,140,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD |
| `1D` | `2046.80` | 600,410,000.00 USD | 0.00 USD | 600,410,000.00 USD | 467,370.00 USD | 0.00 USD | 367,650.00 USD |
| `1D` | `2049.20` | 599,580,000.00 USD | 0.00 USD | 599,580,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD |
| `7D` | `2050.50` | 737,840,000.00 USD | 0.00 USD | 737,840,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2053.30` | 737,620,000.00 USD | 0.00 USD | 737,620,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD |
| `1D` | `2054.00` | 598,470,000.00 USD | 0.00 USD | 598,470,000.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD |
| `1D` | `2056.40` | 598,350,000.00 USD | 0.00 USD | 598,350,000.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2058.80` | 598,110,000.00 USD | 0.00 USD | 598,110,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `7D` | `2058.90` | 735,330,000.00 USD | 0.00 USD | 735,330,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD |
| `1D` | `2061.20` | 597,360,000.00 USD | 0.00 USD | 597,360,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD |
| `7D` | `2061.70` | 734,990,000.00 USD | 0.00 USD | 734,990,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD |
| `1D` | `2063.60` | 597,280,000.00 USD | 0.00 USD | 597,280,000.00 USD | 563,140.00 USD | 494,150.00 USD | 510,200.00 USD |
| `7D` | `2064.50` | 729,730,000.00 USD | 0.00 USD | 729,730,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 945,860.00 USD |
| `1D` | `2066.00` | 595,710,000.00 USD | 0.00 USD | 595,710,000.00 USD | 387,410.00 USD | 42,880.00 USD | 0.00 USD |
| `7D` | `2067.30` | 727,300,000.00 USD | 0.00 USD | 727,300,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 262,430.00 USD |
| `1D` | `2068.40` | 595,280,000.00 USD | 0.00 USD | 595,280,000.00 USD | 57,300.00 USD | 624,040.00 USD | 0.00 USD |
| `7D` | `2070.10` | 725,630,000.00 USD | 0.00 USD | 725,630,000.00 USD | 2,170,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD |
| `1D` | `2070.80` | 594,600,000.00 USD | 0.00 USD | 594,600,000.00 USD | 47,910.00 USD | 534,600.00 USD | 0.00 USD |
| `7D` | `2072.90` | 719,500,000.00 USD | 0.00 USD | 719,500,000.00 USD | 4,160,000.00 USD | 1,850,000.00 USD | 2,030,000.00 USD |
| `1D` | `2073.20` | 594,010,000.00 USD | 0.00 USD | 594,010,000.00 USD | 25,660.00 USD | 20,640.00 USD | 420,170.00 USD |
| `1D` | `2075.60` | 593,550,000.00 USD | 0.00 USD | 593,550,000.00 USD | 354,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2075.70` | 711,450,000.00 USD | 0.00 USD | 711,450,000.00 USD | 3,720,000.00 USD | 3,490,000.00 USD | 4,280,000.00 USD |
| `1D` | `2078.00` | 593,190,000.00 USD | 0.00 USD | 593,190,000.00 USD | 0.00 USD | 25,190.00 USD | 0.00 USD |
| `7D` | `2078.50` | 699,960,000.00 USD | 0.00 USD | 699,960,000.00 USD | 4,400,000.00 USD | 3,190,000.00 USD | 1,340,000.00 USD |
| `1D` | `2080.40` | 593,170,000.00 USD | 0.00 USD | 593,170,000.00 USD | 77,960.00 USD | 29,610.00 USD | 199,420.00 USD |
| `7D` | `2081.30` | 691,030,000.00 USD | 0.00 USD | 691,030,000.00 USD | 4,470,000.00 USD | 2,960,000.00 USD | 1,970,000.00 USD |
| `1D` | `2082.80` | 592,860,000.00 USD | 0.00 USD | 592,860,000.00 USD | 827,940.00 USD | 4,240.00 USD | 206,010.00 USD |
| `7D` | `2084.10` | 681,630,000.00 USD | 0.00 USD | 681,630,000.00 USD | 1,090,000.00 USD | 1,030,000.00 USD | 3,500,000.00 USD |
| `1D` | `2085.20` | 591,820,000.00 USD | 0.00 USD | 591,820,000.00 USD | 528,660.00 USD | 207,610.00 USD | 821,110.00 USD |
| `7D` | `2086.90` | 676,000,000.00 USD | 0.00 USD | 676,000,000.00 USD | 4,210,000.00 USD | 3,190,000.00 USD | 3,020,000.00 USD |
| `1D` | `2087.60` | 590,270,000.00 USD | 0.00 USD | 590,270,000.00 USD | 525,540.00 USD | 375,440.00 USD | 304,860.00 USD |
| `7D` | `2089.70` | 665,580,000.00 USD | 0.00 USD | 665,580,000.00 USD | 4,130,000.00 USD | 983,760.00 USD | 2,390,000.00 USD |
| `1D` | `2090.00` | 589,060,000.00 USD | 0.00 USD | 589,060,000.00 USD | 506,080.00 USD | 222,650.00 USD | 253,790.00 USD |
| `1D` | `2092.40` | 588,080,000.00 USD | 0.00 USD | 588,080,000.00 USD | 750,150.00 USD | 335,770.00 USD | 270,770.00 USD |
| `7D` | `2092.50` | 658,090,000.00 USD | 0.00 USD | 658,090,000.00 USD | 3,640,000.00 USD | 737,060.00 USD | 6,990,000.00 USD |
| `1D` | `2094.80` | 586,720,000.00 USD | 0.00 USD | 586,720,000.00 USD | 2,100,000.00 USD | 959,250.00 USD | 1,430,000.00 USD |
| `7D` | `2095.30` | 646,720,000.00 USD | 0.00 USD | 646,720,000.00 USD | 3,520,000.00 USD | 1,990,000.00 USD | 1,020,000.00 USD |
| `1D` | `2097.20` | 582,230,000.00 USD | 0.00 USD | 582,230,000.00 USD | 175,830.00 USD | 381,000.00 USD | 674,450.00 USD |
| `7D` | `2098.10` | 640,200,000.00 USD | 0.00 USD | 640,200,000.00 USD | 3,020,000.00 USD | 2,830,000.00 USD | 1,460,000.00 USD |
| `1D` | `2099.60` | 581,000,000.00 USD | 0.00 USD | 581,000,000.00 USD | 307,340.00 USD | 1,070,000.00 USD | 20,670.00 USD |
| `7D` | `2100.90` | 632,890,000.00 USD | 0.00 USD | 632,890,000.00 USD | 575,630.00 USD | 1,560,000.00 USD | 3,420,000.00 USD |
| `1D` | `2102.00` | 579,600,000.00 USD | 0.00 USD | 579,600,000.00 USD | 211,840.00 USD | 371,740.00 USD | 513,570.00 USD |
| `7D` | `2103.70` | 627,330,000.00 USD | 0.00 USD | 627,330,000.00 USD | 679,880.00 USD | 554,710.00 USD | 1,950,000.00 USD |
| `1D` | `2104.40` | 578,500,000.00 USD | 0.00 USD | 578,500,000.00 USD | 3,570,000.00 USD | 1,160,000.00 USD | 677,380.00 USD |
| `7D` | `2106.50` | 624,140,000.00 USD | 0.00 USD | 624,140,000.00 USD | 2,210,000.00 USD | 1,020,000.00 USD | 1,550,000.00 USD |
| `1D` | `2106.80` | 573,090,000.00 USD | 0.00 USD | 573,090,000.00 USD | 583,020.00 USD | 0.00 USD | 502,840.00 USD |
| `1D` | `2109.20` | 572,010,000.00 USD | 0.00 USD | 572,010,000.00 USD | 212,850.00 USD | 31,550.00 USD | 6,190.00 USD |
| `7D` | `2109.30` | 619,370,000.00 USD | 0.00 USD | 619,370,000.00 USD | 7,690,000.00 USD | 1,570,000.00 USD | 1,770,000.00 USD |
| `1D` | `2111.60` | 571,760,000.00 USD | 0.00 USD | 571,760,000.00 USD | 490,860.00 USD | 79,810.00 USD | 0.00 USD |
| `7D` | `2112.10` | 608,340,000.00 USD | 0.00 USD | 608,340,000.00 USD | 3,990,000.00 USD | 1,140,000.00 USD | 3,220,000.00 USD |
| `1D` | `2114.00` | 571,190,000.00 USD | 0.00 USD | 571,190,000.00 USD | 614,540.00 USD | 511,750.00 USD | 249,040.00 USD |
| `7D` | `2114.90` | 599,990,000.00 USD | 0.00 USD | 599,990,000.00 USD | 173,320.00 USD | 3,250,000.00 USD | 1,620,000.00 USD |
| `1D` | `2116.40` | 569,810,000.00 USD | 0.00 USD | 569,810,000.00 USD | 924,300.00 USD | 1,180,000.00 USD | 935,080.00 USD |
| `7D` | `2117.70` | 594,950,000.00 USD | 0.00 USD | 594,950,000.00 USD | 3,340,000.00 USD | 1,110,000.00 USD | 3,380,000.00 USD |
| `1D` | `2118.80` | 566,770,000.00 USD | 0.00 USD | 566,770,000.00 USD | 5,240,000.00 USD | 3,070,000.00 USD | 905,640.00 USD |
| `7D` | `2120.50` | 587,110,000.00 USD | 0.00 USD | 587,110,000.00 USD | 12,860,000.00 USD | 5,600,000.00 USD | 1,410,000.00 USD |
| `1D` | `2121.20` | 557,550,000.00 USD | 0.00 USD | 557,550,000.00 USD | 4,600,000.00 USD | 3,760,000.00 USD | 903,010.00 USD |
| `7D` | `2123.30` | 567,250,000.00 USD | 0.00 USD | 567,250,000.00 USD | 7,150,000.00 USD | 6,010,000.00 USD | 1,310,000.00 USD |
| `1D` | `2123.60` | 548,280,000.00 USD | 0.00 USD | 548,280,000.00 USD | 8,080,000.00 USD | 1,520,000.00 USD | 2,310,000.00 USD |
| `1D` | `2126.00` | 536,370,000.00 USD | 0.00 USD | 536,370,000.00 USD | 3,480,000.00 USD | 2,840,000.00 USD | 837,670.00 USD |
| `7D` | `2126.10` | 552,780,000.00 USD | 0.00 USD | 552,780,000.00 USD | 2,740,000.00 USD | 6,270,000.00 USD | 5,100,000.00 USD |
| `1D` | `2128.40` | 529,210,000.00 USD | 0.00 USD | 529,210,000.00 USD | 3,180,000.00 USD | 1,860,000.00 USD | 1,510,000.00 USD |
| `7D` | `2128.90` | 538,660,000.00 USD | 0.00 USD | 538,660,000.00 USD | 4,770,000.00 USD | 1,040,000.00 USD | 1,300,000.00 USD |
| `1D` | `2130.80` | 522,660,000.00 USD | 0.00 USD | 522,660,000.00 USD | 316,500.00 USD | 61,560.00 USD | 344,350.00 USD |
| `7D` | `2131.70` | 531,560,000.00 USD | 0.00 USD | 531,560,000.00 USD | 1,810,000.00 USD | 1,880,000.00 USD | 1,360,000.00 USD |
| `1D` | `2133.20` | 521,940,000.00 USD | 0.00 USD | 521,940,000.00 USD | 308,240.00 USD | 654,710.00 USD | 1,530,000.00 USD |
| `7D` | `2134.50` | 526,520,000.00 USD | 0.00 USD | 526,520,000.00 USD | 1,980,000.00 USD | 790,240.00 USD | 898,290.00 USD |
| `1D` | `2135.60` | 519,450,000.00 USD | 0.00 USD | 519,450,000.00 USD | 1,840,000.00 USD | 2,080,000.00 USD | 1,820,000.00 USD |
| `7D` | `2137.30` | 522,840,000.00 USD | 0.00 USD | 522,840,000.00 USD | 2,120,000.00 USD | 2,360,000.00 USD | 1,530,000.00 USD |
| `1D` | `2138.00` | 513,700,000.00 USD | 0.00 USD | 513,700,000.00 USD | 699,110.00 USD | 1,510,000.00 USD | 537,470.00 USD |
| `7D` | `2140.10` | 516,840,000.00 USD | 0.00 USD | 516,840,000.00 USD | 3,990,000.00 USD | 1,700,000.00 USD | 801,910.00 USD |
| `1D` | `2140.40` | 510,950,000.00 USD | 0.00 USD | 510,950,000.00 USD | 1,530,000.00 USD | 898,980.00 USD | 317,350.00 USD |
| `1D` | `2142.80` | 508,210,000.00 USD | 0.00 USD | 508,210,000.00 USD | 1,080,000.00 USD | 2,810,000.00 USD | 733,530.00 USD |
| `7D` | `2142.90` | 510,350,000.00 USD | 0.00 USD | 510,350,000.00 USD | 1,200,000.00 USD | 804,740.00 USD | 268,500.00 USD |
| `1D` | `2145.20` | 503,580,000.00 USD | 0.00 USD | 503,580,000.00 USD | 2,350,000.00 USD | 2,390,000.00 USD | 1,030,000.00 USD |
| `7D` | `2145.70` | 508,080,000.00 USD | 0.00 USD | 508,080,000.00 USD | 2,160,000.00 USD | 1,460,000.00 USD | 1,720,000.00 USD |
| `1D` | `2147.60` | 497,800,000.00 USD | 0.00 USD | 497,800,000.00 USD | 1,550,000.00 USD | 1,140,000.00 USD | 69,830.00 USD |
| `7D` | `2148.50` | 502,730,000.00 USD | 0.00 USD | 502,730,000.00 USD | 26,270.00 USD | 538,910.00 USD | 152,010.00 USD |
| `1D` | `2150.00` | 495,040,000.00 USD | 0.00 USD | 495,040,000.00 USD | 7,000,000.00 USD | 2,810,000.00 USD | 2,320,000.00 USD |
| `7D` | `2151.30` | 502,010,000.00 USD | 0.00 USD | 502,010,000.00 USD | 11,200,000.00 USD | 363,770.00 USD | 354,860.00 USD |
| `1D` | `2152.40` | 482,910,000.00 USD | 0.00 USD | 482,910,000.00 USD | 2,570,000.00 USD | 2,990,000.00 USD | 2,170,000.00 USD |
| `7D` | `2154.10` | 490,100,000.00 USD | 0.00 USD | 490,100,000.00 USD | 48,150.00 USD | 2,020,000.00 USD | 1,580,000.00 USD |
| `1D` | `2154.80` | 475,180,000.00 USD | 0.00 USD | 475,180,000.00 USD | 2,320,000.00 USD | 3,560,000.00 USD | 2,310,000.00 USD |
| `7D` | `2156.90` | 486,450,000.00 USD | 0.00 USD | 486,450,000.00 USD | 2,480,000.00 USD | 293,550.00 USD | 3,940,000.00 USD |
| `1D` | `2157.20` | 466,990,000.00 USD | 0.00 USD | 466,990,000.00 USD | 4,540,000.00 USD | 1,600,000.00 USD | 3,300,000.00 USD |
| `1D` | `2159.60` | 457,560,000.00 USD | 0.00 USD | 457,560,000.00 USD | 3,550,000.00 USD | 4,690,000.00 USD | 3,580,000.00 USD |
| `7D` | `2159.70` | 479,730,000.00 USD | 0.00 USD | 479,730,000.00 USD | 4,780,000.00 USD | 1,770,000.00 USD | 2,430,000.00 USD |
| `1D` | `2162.00` | 445,730,000.00 USD | 0.00 USD | 445,730,000.00 USD | 11,780,000.00 USD | 10,080,000.00 USD | 675,370.00 USD |
| `7D` | `2162.50` | 470,750,000.00 USD | 0.00 USD | 470,750,000.00 USD | 17,980,000.00 USD | 1,990,000.00 USD | 514,130.00 USD |
| `1D` | `2164.40` | 423,200,000.00 USD | 0.00 USD | 423,200,000.00 USD | 17,650,000.00 USD | 7,570,000.00 USD | 3,970,000.00 USD |
| `7D` | `2165.30` | 450,260,000.00 USD | 0.00 USD | 450,260,000.00 USD | 8,990,000.00 USD | 17,170,000.00 USD | 2,760,000.00 USD |
| `1D` | `2166.80` | 394,000,000.00 USD | 0.00 USD | 394,000,000.00 USD | 6,670,000.00 USD | 8,800,000.00 USD | 5,560,000.00 USD |
| `7D` | `2168.10` | 421,350,000.00 USD | 0.00 USD | 421,350,000.00 USD | 12,770,000.00 USD | 16,150,000.00 USD | 3,690,000.00 USD |
| `1D` | `2169.20` | 372,970,000.00 USD | 0.00 USD | 372,970,000.00 USD | 16,780,000.00 USD | 6,520,000.00 USD | 5,250,000.00 USD |
| `7D` | `2170.90` | 388,730,000.00 USD | 0.00 USD | 388,730,000.00 USD | 1,860,000.00 USD | 6,380,000.00 USD | 5,840,000.00 USD |
| `1D` | `2171.60` | 344,420,000.00 USD | 0.00 USD | 344,420,000.00 USD | 22,900,000.00 USD | 9,830,000.00 USD | 6,290,000.00 USD |
| `7D` | `2173.70` | 374,660,000.00 USD | 0.00 USD | 374,660,000.00 USD | 33,340,000.00 USD | 0.00 USD | 1,010,000.00 USD |
| `1D` | `2174.00` | 305,410,000.00 USD | 0.00 USD | 305,410,000.00 USD | 6,570,000.00 USD | 1,390,000.00 USD | 2,310,000.00 USD |
| `1D` | `2176.40` | 295,140,000.00 USD | 0.00 USD | 295,140,000.00 USD | 1,700,000.00 USD | 569,650.00 USD | 2,390,000.00 USD |
| `7D` | `2176.50` | 340,310,000.00 USD | 0.00 USD | 340,310,000.00 USD | 1,750,000.00 USD | 1,460,000.00 USD | 2,820,000.00 USD |
| `1D` | `2178.80` | 290,480,000.00 USD | 0.00 USD | 290,480,000.00 USD | 1,740,000.00 USD | 1,550,000.00 USD | 934,090.00 USD |
| `7D` | `2179.30` | 334,280,000.00 USD | 0.00 USD | 334,280,000.00 USD | 196,330.00 USD | 133,210.00 USD | 4,150,000.00 USD |
| `1D` | `2181.20` | 286,260,000.00 USD | 0.00 USD | 286,260,000.00 USD | 3,890,000.00 USD | 4,690,000.00 USD | 8,630,000.00 USD |
| `7D` | `2182.10` | 329,790,000.00 USD | 0.00 USD | 329,790,000.00 USD | 3,960,000.00 USD | 2,160,000.00 USD | 2,650,000.00 USD |
| `1D` | `2183.60` | 269,040,000.00 USD | 0.00 USD | 269,040,000.00 USD | 3,600,000.00 USD | 153,590.00 USD | 1,260,000.00 USD |
| `7D` | `2184.90` | 321,020,000.00 USD | 0.00 USD | 321,020,000.00 USD | 41,350,000.00 USD | 2,700,000.00 USD | 1,290,000.00 USD |
| `1D` | `2186.00` | 264,030,000.00 USD | 0.00 USD | 264,030,000.00 USD | 310,640.00 USD | 2,460,000.00 USD | 4,860,000.00 USD |
| `7D` | `2187.70` | 275,670,000.00 USD | 0.00 USD | 275,670,000.00 USD | 2,370,000.00 USD | 17,750,000.00 USD | 380,620.00 USD |
| `1D` | `2188.40` | 256,410,000.00 USD | 0.00 USD | 256,410,000.00 USD | 7,340,000.00 USD | 4,820,000.00 USD | 8,490,000.00 USD |
| `7D` | `2190.50` | 255,170,000.00 USD | 0.00 USD | 255,170,000.00 USD | 12,430,000.00 USD | 27,960,000.00 USD | 7,640,000.00 USD |
| `1D` | `2190.80` | 235,760,000.00 USD | 0.00 USD | 235,760,000.00 USD | 7,610,000.00 USD | 4,390,000.00 USD | 4,490,000.00 USD |
| `1D` | `2193.20` | 219,270,000.00 USD | 0.00 USD | 219,270,000.00 USD | 5,420,000.00 USD | 5,760,000.00 USD | 368,240.00 USD |
| `7D` | `2193.30` | 207,140,000.00 USD | 0.00 USD | 207,140,000.00 USD | 0.00 USD | 7,340,000.00 USD | 8,120,000.00 USD |
| `1D` | `2195.60` | 207,720,000.00 USD | 0.00 USD | 207,720,000.00 USD | 8,100,000.00 USD | 1,230,000.00 USD | 5,630,000.00 USD |
| `7D` | `2196.10` | 191,680,000.00 USD | 0.00 USD | 191,680,000.00 USD | 383,690.00 USD | 243,760.00 USD | 109,160.00 USD |
| `1D` | `2198.00` | 192,760,000.00 USD | 0.00 USD | 192,760,000.00 USD | 1,110,000.00 USD | 3,280,000.00 USD | 4,480,000.00 USD |
| `7D` | `2198.90` | 190,940,000.00 USD | 0.00 USD | 190,940,000.00 USD | 0.00 USD | 1,460,000.00 USD | 7,440,000.00 USD |
| `1D` | `2200.40` | 183,890,000.00 USD | 0.00 USD | 183,890,000.00 USD | 7,310,000.00 USD | 3,670,000.00 USD | 10,460,000.00 USD |
| `7D` | `2201.70` | 182,050,000.00 USD | 0.00 USD | 182,050,000.00 USD | 9,110,000.00 USD | 266,430.00 USD | 18,630,000.00 USD |
| `1D` | `2202.80` | 162,450,000.00 USD | 0.00 USD | 162,450,000.00 USD | 14,180,000.00 USD | 11,600,000.00 USD | 14,730,000.00 USD |
| `7D` | `2204.50` | 154,040,000.00 USD | 0.00 USD | 154,040,000.00 USD | 5,350,000.00 USD | 4,330,000.00 USD | 4,430,000.00 USD |
| `1D` | `2205.20` | 121,940,000.00 USD | 0.00 USD | 121,940,000.00 USD | 7,470,000.00 USD | 4,810,000.00 USD | 2,870,000.00 USD |
| `7D` | `2207.30` | 139,930,000.00 USD | 0.00 USD | 139,930,000.00 USD | 17,370,000.00 USD | 3,390,000.00 USD | 3,660,000.00 USD |
| `1D` | `2207.60` | 106,800,000.00 USD | 0.00 USD | 106,800,000.00 USD | 12,580,000.00 USD | 4,890,000.00 USD | 2,050,000.00 USD |
| `1D` | `2210.00` | 87,270,000.00 USD | 0.00 USD | 87,270,000.00 USD | 4,040,000.00 USD | 7,220,000.00 USD | 6,290,000.00 USD |
| `7D` | `2210.10` | 115,520,000.00 USD | 0.00 USD | 115,520,000.00 USD | 7,000,000.00 USD | 0.00 USD | 11,300,000.00 USD |
| `1D` | `2212.40` | 69,730,000.00 USD | 0.00 USD | 69,730,000.00 USD | 11,460,000.00 USD | 5,440,000.00 USD | 1,950,000.00 USD |
| `7D` | `2212.90` | 97,220,000.00 USD | 0.00 USD | 97,220,000.00 USD | 1,710,000.00 USD | 1,980,000.00 USD | 8,850,000.00 USD |
| `1D` | `2214.80` | 50,880,000.00 USD | 0.00 USD | 50,880,000.00 USD | 3,530,000.00 USD | 3,900,000.00 USD | 102,250.00 USD |
| `7D` | `2215.70` | 84,680,000.00 USD | 0.00 USD | 84,680,000.00 USD | 0.00 USD | 0.00 USD | 565,690.00 USD |
| `1D` | `2217.20` | 43,340,000.00 USD | 0.00 USD | 43,340,000.00 USD | 472,330.00 USD | 2,460,000.00 USD | 4,000,000.00 USD |
| `7D` | `2218.50` | 84,110,000.00 USD | 0.00 USD | 84,110,000.00 USD | 22,400,000.00 USD | 487,520.00 USD | 218,310.00 USD |
| `1D` | `2219.60` | 36,420,000.00 USD | 0.00 USD | 36,420,000.00 USD | 6,620,000.00 USD | 3,090,000.00 USD | 1,820,000.00 USD |
| `7D` | `2221.30` | 61,010,000.00 USD | 0.00 USD | 61,010,000.00 USD | 0.00 USD | 12,220,000.00 USD | 18,020,000.00 USD |
| `1D` | `2222.00` | 24,890,000.00 USD | 0.00 USD | 24,890,000.00 USD | 0.00 USD | 4,090,000.00 USD | 2,620,000.00 USD |
| `7D` | `2224.10` | 30,760,000.00 USD | 0.00 USD | 30,760,000.00 USD | 0.00 USD | 0.00 USD | 1,510,000.00 USD |
| `1D` | `2224.40` | 18,190,000.00 USD | 0.00 USD | 18,190,000.00 USD | 374,450.00 USD | 300,160.00 USD | 0.00 USD |
| `1D` | `2226.80` | 17,510,000.00 USD | 0.00 USD | 17,510,000.00 USD | 0.00 USD | 0.00 USD | 3,450,000.00 USD |
| `7D` | `2226.90` | 29,250,000.00 USD | 0.00 USD | 29,250,000.00 USD | 447,040.00 USD | 0.00 USD | 7,710,000.00 USD |
| `1D` | `2229.20` | 14,060,000.00 USD | 0.00 USD | 14,060,000.00 USD | 0.00 USD | 12,070,000.00 USD | 2,000,000.00 USD |
| `1D` | `2229.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2229.70` | 21,100,000.00 USD | 0.00 USD | 21,100,000.00 USD | 2,020,000.00 USD | 0.00 USD | 19,080,000.00 USD |
| `7D` | `2229.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2231.60` | 40,790,000.00 USD | 40,790,000.00 USD | 0.00 USD | 40,420,000.00 USD | 0.00 USD | 369,680.00 USD |
| `7D` | `2232.50` | 959,630.00 USD | 959,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 959,630.00 USD |
| `1D` | `2234.00` | 40,830,000.00 USD | 40,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 41,500.00 USD |
| `7D` | `2235.30` | 26,210,000.00 USD | 26,210,000.00 USD | 0.00 USD | 3,260,000.00 USD | 21,640,000.00 USD | 350,840.00 USD |
| `1D` | `2236.40` | 47,630,000.00 USD | 47,630,000.00 USD | 0.00 USD | 6,800,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2238.10` | 38,720,000.00 USD | 38,720,000.00 USD | 0.00 USD | 12,520,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2238.80` | 56,050,000.00 USD | 56,050,000.00 USD | 0.00 USD | 8,420,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2240.90` | 70,640,000.00 USD | 70,640,000.00 USD | 0.00 USD | 31,920,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2241.20` | 56,180,000.00 USD | 56,180,000.00 USD | 0.00 USD | 81,700.00 USD | 0.00 USD | 50,930.00 USD |
| `1D` | `2243.60` | 57,080,000.00 USD | 57,080,000.00 USD | 0.00 USD | 327,260.00 USD | 569,860.00 USD | 0.00 USD |
| `7D` | `2243.70` | 73,450,000.00 USD | 73,450,000.00 USD | 0.00 USD | 2,540,000.00 USD | 268,650.00 USD | 0.00 USD |
| `1D` | `2246.00` | 71,350,000.00 USD | 71,350,000.00 USD | 0.00 USD | 5,630,000.00 USD | 4,370,000.00 USD | 4,280,000.00 USD |
| `7D` | `2246.50` | 90,310,000.00 USD | 90,310,000.00 USD | 0.00 USD | 7,160,000.00 USD | 1,300,000.00 USD | 8,410,000.00 USD |
| `1D` | `2248.40` | 86,320,000.00 USD | 86,320,000.00 USD | 0.00 USD | 3,770,000.00 USD | 5,270,000.00 USD | 5,930,000.00 USD |
| `7D` | `2249.30` | 101,630,000.00 USD | 101,630,000.00 USD | 0.00 USD | 3,080,000.00 USD | 6,990,000.00 USD | 1,250,000.00 USD |
| `1D` | `2250.80` | 94,580,000.00 USD | 94,580,000.00 USD | 0.00 USD | 7,670,000.00 USD | 505,690.00 USD | 77,860.00 USD |
| `7D` | `2252.10` | 123,350,000.00 USD | 123,350,000.00 USD | 0.00 USD | 10,050,000.00 USD | 11,670,000.00 USD | 0.00 USD |
| `1D` | `2253.20` | 100,330,000.00 USD | 100,330,000.00 USD | 0.00 USD | 943,690.00 USD | 3,380,000.00 USD | 1,420,000.00 USD |
| `7D` | `2254.90` | 140,400,000.00 USD | 140,400,000.00 USD | 0.00 USD | 10,050,000.00 USD | 6,600,000.00 USD | 406,400.00 USD |
| `1D` | `2255.60` | 132,150,000.00 USD | 132,150,000.00 USD | 0.00 USD | 16,490,000.00 USD | 6,560,000.00 USD | 8,780,000.00 USD |
| `7D` | `2257.70` | 180,210,000.00 USD | 180,210,000.00 USD | 0.00 USD | 20,510,000.00 USD | 12,290,000.00 USD | 7,000,000.00 USD |
| `1D` | `2258.00` | 160,670,000.00 USD | 160,670,000.00 USD | 0.00 USD | 18,030,000.00 USD | 7,740,000.00 USD | 2,740,000.00 USD |
| `1D` | `2260.40` | 180,880,000.00 USD | 180,880,000.00 USD | 0.00 USD | 8,330,000.00 USD | 9,340,000.00 USD | 2,540,000.00 USD |
| `7D` | `2260.50` | 184,320,000.00 USD | 184,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,110,000.00 USD |
| `1D` | `2262.80` | 211,480,000.00 USD | 211,480,000.00 USD | 0.00 USD | 14,550,000.00 USD | 9,830,000.00 USD | 6,220,000.00 USD |
| `7D` | `2263.30` | 192,920,000.00 USD | 192,920,000.00 USD | 0.00 USD | 6,720,000.00 USD | 1,460,000.00 USD | 428,780.00 USD |
| `1D` | `2265.20` | 237,350,000.00 USD | 237,350,000.00 USD | 0.00 USD | 4,700,000.00 USD | 9,750,000.00 USD | 11,410,000.00 USD |
| `7D` | `2266.10` | 207,410,000.00 USD | 207,410,000.00 USD | 0.00 USD | 0.00 USD | 8,160,000.00 USD | 6,330,000.00 USD |
| `1D` | `2267.60` | 267,890,000.00 USD | 267,890,000.00 USD | 0.00 USD | 11,510,000.00 USD | 9,470,000.00 USD | 9,560,000.00 USD |
| `7D` | `2268.90` | 227,380,000.00 USD | 227,380,000.00 USD | 0.00 USD | 11,010,000.00 USD | 133,210.00 USD | 8,820,000.00 USD |
| `1D` | `2270.00` | 313,470,000.00 USD | 313,470,000.00 USD | 0.00 USD | 17,860,000.00 USD | 8,740,000.00 USD | 18,990,000.00 USD |
| `7D` | `2271.70` | 265,500,000.00 USD | 265,500,000.00 USD | 0.00 USD | 18,240,000.00 USD | 3,640,000.00 USD | 16,240,000.00 USD |
| `1D` | `2272.40` | 340,010,000.00 USD | 340,010,000.00 USD | 0.00 USD | 15,430,000.00 USD | 5,600,000.00 USD | 5,500,000.00 USD |
| `7D` | `2274.50` | 292,030,000.00 USD | 292,030,000.00 USD | 0.00 USD | 19,630,000.00 USD | 6,900,000.00 USD | 0.00 USD |
| `1D` | `2274.80` | 375,290,000.00 USD | 375,290,000.00 USD | 0.00 USD | 24,410,000.00 USD | 8,560,000.00 USD | 2,320,000.00 USD |
| `1D` | `2277.20` | 417,300,000.00 USD | 417,300,000.00 USD | 0.00 USD | 10,420,000.00 USD | 18,400,000.00 USD | 13,190,000.00 USD |
| `7D` | `2277.30` | 309,390,000.00 USD | 309,390,000.00 USD | 0.00 USD | 6,890,000.00 USD | 0.00 USD | 10,480,000.00 USD |
| `1D` | `2279.60` | 453,870,000.00 USD | 453,870,000.00 USD | 0.00 USD | 16,500,000.00 USD | 8,760,000.00 USD | 11,320,000.00 USD |
| `7D` | `2280.10` | 359,200,000.00 USD | 359,200,000.00 USD | 0.00 USD | 854,200.00 USD | 45,440,000.00 USD | 3,510,000.00 USD |
| `1D` | `2282.00` | 506,500,000.00 USD | 506,500,000.00 USD | 0.00 USD | 26,040,000.00 USD | 23,280,000.00 USD | 3,320,000.00 USD |
| `7D` | `2282.90` | 448,500,000.00 USD | 448,500,000.00 USD | 0.00 USD | 5,600,000.00 USD | 69,990,000.00 USD | 13,710,000.00 USD |
| `1D` | `2284.40` | 550,690,000.00 USD | 550,690,000.00 USD | 0.00 USD | 21,550,000.00 USD | 11,720,000.00 USD | 10,920,000.00 USD |
| `7D` | `2285.70` | 458,130,000.00 USD | 458,130,000.00 USD | 0.00 USD | 1,010,000.00 USD | 8,400,000.00 USD | 214,390.00 USD |
| `1D` | `2286.80` | 581,110,000.00 USD | 581,110,000.00 USD | 0.00 USD | 9,570,000.00 USD | 12,590,000.00 USD | 8,260,000.00 USD |
| `7D` | `2288.50` | 490,760,000.00 USD | 490,760,000.00 USD | 0.00 USD | 8,380,000.00 USD | 9,320,000.00 USD | 14,930,000.00 USD |
| `1D` | `2289.20` | 600,410,000.00 USD | 600,410,000.00 USD | 0.00 USD | 8,210,000.00 USD | 9,130,000.00 USD | 1,960,000.00 USD |
| `7D` | `2291.30` | 497,970,000.00 USD | 497,970,000.00 USD | 0.00 USD | 4,310,000.00 USD | 517,070.00 USD | 2,380,000.00 USD |
| `1D` | `2291.60` | 638,410,000.00 USD | 638,410,000.00 USD | 0.00 USD | 20,470,000.00 USD | 9,410,000.00 USD | 8,130,000.00 USD |
| `1D` | `2294.00` | 672,690,000.00 USD | 672,690,000.00 USD | 0.00 USD | 15,480,000.00 USD | 6,720,000.00 USD | 12,070,000.00 USD |
| `7D` | `2294.10` | 518,250,000.00 USD | 518,250,000.00 USD | 0.00 USD | 8,930,000.00 USD | 1,490,000.00 USD | 9,850,000.00 USD |
| `1D` | `2296.40` | 703,570,000.00 USD | 703,570,000.00 USD | 0.00 USD | 13,600,000.00 USD | 12,430,000.00 USD | 4,860,000.00 USD |
| `7D` | `2296.90` | 573,730,000.00 USD | 573,730,000.00 USD | 0.00 USD | 31,630,000.00 USD | 8,070,000.00 USD | 15,780,000.00 USD |
| `1D` | `2298.80` | 756,530,000.00 USD | 756,530,000.00 USD | 0.00 USD | 27,220,000.00 USD | 15,600,000.00 USD | 10,140,000.00 USD |
| `7D` | `2299.70` | 616,650,000.00 USD | 616,650,000.00 USD | 0.00 USD | 16,200,000.00 USD | 20,940,000.00 USD | 5,780,000.00 USD |
| `1D` | `2301.20` | 783,880,000.00 USD | 783,880,000.00 USD | 0.00 USD | 9,830,000.00 USD | 6,810,000.00 USD | 10,700,000.00 USD |
| `7D` | `2302.50` | 671,310,000.00 USD | 671,310,000.00 USD | 0.00 USD | 26,960,000.00 USD | 10,860,000.00 USD | 16,850,000.00 USD |
| `1D` | `2303.60` | 815,420,000.00 USD | 815,420,000.00 USD | 0.00 USD | 14,740,000.00 USD | 10,150,000.00 USD | 6,650,000.00 USD |
| `7D` | `2305.30` | 695,470,000.00 USD | 695,470,000.00 USD | 0.00 USD | 6,340,000.00 USD | 6,960,000.00 USD | 10,860,000.00 USD |
| `1D` | `2306.00` | 850,240,000.00 USD | 850,240,000.00 USD | 0.00 USD | 13,720,000.00 USD | 12,830,000.00 USD | 8,260,000.00 USD |
| `7D` | `2308.10` | 699,630,000.00 USD | 699,630,000.00 USD | 0.00 USD | 1,240,000.00 USD | 2,780,000.00 USD | 134,160.00 USD |
| `1D` | `2308.40` | 857,590,000.00 USD | 857,590,000.00 USD | 0.00 USD | 2,860,000.00 USD | 3,320,000.00 USD | 1,180,000.00 USD |
| `1D` | `2310.80` | 874,630,000.00 USD | 874,630,000.00 USD | 0.00 USD | 5,990,000.00 USD | 241,880.00 USD | 10,810,000.00 USD |
| `7D` | `2310.90` | 729,960,000.00 USD | 729,960,000.00 USD | 0.00 USD | 11,460,000.00 USD | 2,720,000.00 USD | 16,150,000.00 USD |
| `1D` | `2313.20` | 892,370,000.00 USD | 892,370,000.00 USD | 0.00 USD | 6,680,000.00 USD | 8,970,000.00 USD | 2,090,000.00 USD |
| `7D` | `2313.70` | 736,920,000.00 USD | 736,920,000.00 USD | 0.00 USD | 1,200,000.00 USD | 3,490,000.00 USD | 2,260,000.00 USD |
| `1D` | `2315.60` | 926,890,000.00 USD | 926,890,000.00 USD | 0.00 USD | 10,440,000.00 USD | 16,170,000.00 USD | 7,920,000.00 USD |
| `7D` | `2316.50` | 746,540,000.00 USD | 746,540,000.00 USD | 0.00 USD | 1,020,000.00 USD | 7,560,000.00 USD | 1,040,000.00 USD |
| `1D` | `2318.00` | 938,210,000.00 USD | 938,210,000.00 USD | 0.00 USD | 2,450,000.00 USD | 6,630,000.00 USD | 2,230,000.00 USD |
| `7D` | `2319.30` | 775,920,000.00 USD | 775,920,000.00 USD | 0.00 USD | 5,530,000.00 USD | 15,960,000.00 USD | 7,890,000.00 USD |
| `1D` | `2320.40` | 961,940,000.00 USD | 961,940,000.00 USD | 0.00 USD | 9,330,000.00 USD | 11,570,000.00 USD | 2,840,000.00 USD |
| `7D` | `2322.10` | 781,770,000.00 USD | 781,770,000.00 USD | 0.00 USD | 2,300,000.00 USD | 3,450,000.00 USD | 108,040.00 USD |
| `1D` | `2322.80` | 979,770,000.00 USD | 979,770,000.00 USD | 0.00 USD | 3,860,000.00 USD | 9,300,000.00 USD | 4,670,000.00 USD |
| `7D` | `2324.90` | 799,340,000.00 USD | 799,340,000.00 USD | 0.00 USD | 4,680,000.00 USD | 2,770,000.00 USD | 10,120,000.00 USD |
| `1D` | `2325.20` | 992,950,000.00 USD | 992,950,000.00 USD | 0.00 USD | 2,550,000.00 USD | 9,140,000.00 USD | 1,490,000.00 USD |
| `1D` | `2327.60` | 999,400,000.00 USD | 999,400,000.00 USD | 0.00 USD | 494,310.00 USD | 1,410,000.00 USD | 4,550,000.00 USD |
| `7D` | `2327.70` | 816,650,000.00 USD | 816,650,000.00 USD | 0.00 USD | 9,330,000.00 USD | 0.00 USD | 7,980,000.00 USD |
| `1D` | `2330.00` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 0.00 USD | 10,740,000.00 USD | 3,070,000.00 USD | 1,250,000.00 USD |
| `7D` | `2330.50` | 832,920,000.00 USD | 832,920,000.00 USD | 0.00 USD | 15,800,000.00 USD | 363,770.00 USD | 107,200.00 USD |
| `1D` | `2332.40` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 0.00 USD | 2,430,000.00 USD | 1,710,000.00 USD | 6,120,000.00 USD |
| `7D` | `2333.30` | 864,180,000.00 USD | 864,180,000.00 USD | 0.00 USD | 20,270,000.00 USD | 9,410,000.00 USD | 1,580,000.00 USD |
| `1D` | `2334.80` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 0.00 USD | 8,950,000.00 USD | 5,310,000.00 USD | 5,680,000.00 USD |
| `7D` | `2336.10` | 911,270,000.00 USD | 911,270,000.00 USD | 0.00 USD | 24,310,000.00 USD | 11,020,000.00 USD | 11,760,000.00 USD |
| `1D` | `2337.20` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 11,530,000.00 USD | 1,400,000.00 USD | 5,710,000.00 USD |
| `7D` | `2338.90` | 937,670,000.00 USD | 937,670,000.00 USD | 0.00 USD | 14,040,000.00 USD | 0.00 USD | 12,370,000.00 USD |
| `1D` | `2339.60` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 11,750,000.00 USD | 6,440,000.00 USD | 12,140,000.00 USD |
| `7D` | `2341.70` | 976,960,000.00 USD | 976,960,000.00 USD | 0.00 USD | 7,470,000.00 USD | 17,820,000.00 USD | 14,000,000.00 USD |
| `1D` | `2342.00` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 4,950,000.00 USD | 1,960,000.00 USD | 2,170,000.00 USD |
| `1D` | `2344.40` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 7,670,000.00 USD | 10,300,000.00 USD | 5,960,000.00 USD |
| `7D` | `2344.50` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 0.00 USD | 3,630,000.00 USD | 16,920,000.00 USD | 5,900,000.00 USD |
| `1D` | `2346.80` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 3,930,000.00 USD | 3,250,000.00 USD | 5,670,000.00 USD |
| `7D` | `2347.30` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 0.00 USD | 0.00 USD | 8,220,000.00 USD | 21,480,000.00 USD |
| `1D` | `2349.20` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 11,390,000.00 USD | 4,080,000.00 USD | 5,410,000.00 USD |
| `7D` | `2350.10` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 0.00 USD | 1,630,000.00 USD | 18,920,000.00 USD | 14,120,000.00 USD |
| `1D` | `2351.60` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 19,450,000.00 USD | 4,850,000.00 USD | 7,250,000.00 USD |
| `7D` | `2352.90` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 2,710,000.00 USD | 33,320,000.00 USD | 5,670,000.00 USD |
| `1D` | `2354.00` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 2,640,000.00 USD | 5,600,000.00 USD | 1,030,000.00 USD |
| `7D` | `2355.70` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 18,560,000.00 USD | 14,360,000.00 USD | 2,630,000.00 USD |
| `1D` | `2356.40` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 5,770,000.00 USD | 1,070,000.00 USD | 1,140,000.00 USD |
| `7D` | `2358.50` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 6,870,000.00 USD | 512,220.00 USD | 4,510,000.00 USD |
| `1D` | `2358.80` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 4,520,000.00 USD | 5,650,000.00 USD | 7,350,000.00 USD |
| `1D` | `2361.20` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 8,330,000.00 USD | 8,630,000.00 USD | 1,260,000.00 USD |
| `7D` | `2361.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 2,430,000.00 USD | 3,430,000.00 USD | 374,770.00 USD |
| `1D` | `2363.60` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 0.00 USD | 5,120,000.00 USD | 2,870,000.00 USD | 8,440,000.00 USD |
| `7D` | `2364.10` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 4,570,000.00 USD | 373,740.00 USD | 9,630,000.00 USD |
| `1D` | `2366.00` | 1,270,000,000.00 USD | 1,270,000,000.00 USD | 0.00 USD | 4,830,000.00 USD | 827,140.00 USD | 2,400,000.00 USD |
| `7D` | `2366.90` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 6,340,000.00 USD | 1,310,000.00 USD | 1,600,000.00 USD |
| `1D` | `2368.40` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 0.00 USD | 4,680,000.00 USD | 3,870,000.00 USD | 3,390,000.00 USD |
| `7D` | `2369.70` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 24,570,000.00 USD | 475,460.00 USD | 13,570,000.00 USD |
| `1D` | `2370.80` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 0.00 USD | 14,000,000.00 USD | 5,860,000.00 USD | 4,800,000.00 USD |
| `7D` | `2372.50` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 0.00 USD | 15,970,000.00 USD | 0.00 USD | 44,190,000.00 USD |
| `1D` | `2373.20` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 11,920,000.00 USD | 2,030,000.00 USD | 5,900,000.00 USD |
| `7D` | `2375.30` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 0.00 USD | 9,700,000.00 USD | 121,480.00 USD | 12,540,000.00 USD |
| `1D` | `2375.60` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 7,590,000.00 USD | 1,830,000.00 USD | 1,380,000.00 USD |
| `1D` | `2378.00` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 1,460,000.00 USD | 1,920,000.00 USD | 5,990,000.00 USD |
| `7D` | `2378.10` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 11,180,000.00 USD | 7,790,000.00 USD | 21,060,000.00 USD |
| `1D` | `2380.40` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 0.00 USD | 6,310,000.00 USD | 5,360,000.00 USD | 3,110,000.00 USD |
| `7D` | `2380.90` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 4,540,000.00 USD | 2,540,000.00 USD | 16,690,000.00 USD |
| `1D` | `2382.80` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 15,730,000.00 USD | 9,540,000.00 USD | 11,420,000.00 USD |
| `7D` | `2383.70` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 8,720,000.00 USD | 16,800,000.00 USD | 33,100,000.00 USD |
| `1D` | `2385.20` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 7,510,000.00 USD | 11,630,000.00 USD | 4,560,000.00 USD |
| `7D` | `2386.50` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 0.00 USD | 17,480,000.00 USD | 37,020,000.00 USD | 38,780,000.00 USD |
| `1D` | `2387.60` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 0.00 USD | 9,800,000.00 USD | 5,870,000.00 USD | 3,120,000.00 USD |
| `7D` | `2389.30` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 3,900,000.00 USD | 32,580,000.00 USD | 31,000,000.00 USD |
| `1D` | `2390.00` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 0.00 USD | 4,390,000.00 USD | 3,120,000.00 USD | 1,520,000.00 USD |
| `7D` | `2392.10` | 1,690,000,000.00 USD | 1,690,000,000.00 USD | 0.00 USD | 17,810,000.00 USD | 45,470,000.00 USD | 39,140,000.00 USD |
| `1D` | `2392.40` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,850,000.00 USD | 3,320,000.00 USD |
| `1D` | `2394.80` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,780,000.00 USD | 1,120,000.00 USD |
| `7D` | `2394.90` | 1,800,000,000.00 USD | 1,800,000,000.00 USD | 0.00 USD | 46,520,000.00 USD | 28,270,000.00 USD | 28,920,000.00 USD |
| `1D` | `2397.20` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 0.00 USD | 64,150.00 USD | 3,730,000.00 USD | 2,880,000.00 USD |
| `7D` | `2397.70` | 1,890,000,000.00 USD | 1,890,000,000.00 USD | 0.00 USD | 30,700,000.00 USD | 35,140,000.00 USD | 25,100,000.00 USD |
| `1D` | `2399.60` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 0.00 USD | 2,150,000.00 USD | 680,850.00 USD | 2,940,000.00 USD |
| `7D` | `2400.50` | 1,990,000,000.00 USD | 1,990,000,000.00 USD | 0.00 USD | 49,430,000.00 USD | 26,510,000.00 USD | 21,160,000.00 USD |
| `1D` | `2402.00` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 0.00 USD | 1,140,000.00 USD | 0.00 USD | 543,740.00 USD |
| `7D` | `2403.30` | 2,090,000,000.00 USD | 2,090,000,000.00 USD | 0.00 USD | 51,300,000.00 USD | 23,260,000.00 USD | 29,090,000.00 USD |
| `1D` | `2404.40` | 1,490,000,000.00 USD | 1,490,000,000.00 USD | 0.00 USD | 3,690,000.00 USD | 3,730,000.00 USD | 2,060,000.00 USD |
| `7D` | `2406.10` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 0.00 USD | 25,510,000.00 USD | 29,700,000.00 USD | 17,560,000.00 USD |
| `1D` | `2406.80` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 0.00 USD | 9,080,000.00 USD | 3,500,000.00 USD | 4,810,000.00 USD |
| `7D` | `2408.90` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 0.00 USD | 29,270,000.00 USD | 25,210,000.00 USD | 24,260,000.00 USD |
| `1D` | `2409.20` | 1,510,000,000.00 USD | 1,510,000,000.00 USD | 0.00 USD | 3,280,000.00 USD | 3,590,000.00 USD | 3,010,000.00 USD |
| `1D` | `2411.60` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 0.00 USD | 5,500,000.00 USD | 3,590,000.00 USD | 1,390,000.00 USD |
| `7D` | `2411.70` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 0.00 USD | 15,360,000.00 USD | 23,030,000.00 USD | 18,500,000.00 USD |
| `1D` | `2414.00` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 0.00 USD | 2,260,000.00 USD | 644,590.00 USD | 762,340.00 USD |
| `7D` | `2414.50` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 19,450,000.00 USD | 19,740,000.00 USD | 21,570,000.00 USD |
| `1D` | `2416.40` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 0.00 USD | 2,870,000.00 USD | 2,240,000.00 USD | 3,410,000.00 USD |
| `7D` | `2417.30` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 0.00 USD | 22,080,000.00 USD | 4,990,000.00 USD | 20,810,000.00 USD |
| `1D` | `2418.80` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 0.00 USD | 2,610,000.00 USD | 1,590,000.00 USD | 2,010,000.00 USD |
| `7D` | `2420.10` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 0.00 USD | 31,570,000.00 USD | 20,780,000.00 USD | 9,510,000.00 USD |
| `1D` | `2421.20` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 0.00 USD | 6,090,000.00 USD | 4,540,000.00 USD | 5,240,000.00 USD |
| `7D` | `2422.90` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 0.00 USD | 15,870,000.00 USD | 19,430,000.00 USD | 22,020,000.00 USD |
| `1D` | `2423.60` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 0.00 USD | 526,140.00 USD | 1,140,000.00 USD | 1,300,000.00 USD |
| `7D` | `2425.70` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 0.00 USD | 15,760,000.00 USD | 13,390,000.00 USD | 15,470,000.00 USD |
| `1D` | `2426.00` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 0.00 USD | 1,470,000.00 USD | 1,010,000.00 USD | 31,040.00 USD |
| `1D` | `2428.40` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 1,290,000.00 USD | 1,180,000.00 USD | 1,480,000.00 USD |
| `7D` | `2428.50` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 0.00 USD | 13,950,000.00 USD | 8,940,000.00 USD | 10,770,000.00 USD |
| `1D` | `2430.80` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 1,910,000.00 USD | 2,400,000.00 USD | 460,930.00 USD |
| `7D` | `2431.30` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 0.00 USD | 8,950,000.00 USD | 12,070,000.00 USD | 8,780,000.00 USD |
| `1D` | `2433.20` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 2,980,000.00 USD | 1,680,000.00 USD | 1,660,000.00 USD |
| `7D` | `2434.10` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 0.00 USD | 13,720,000.00 USD | 4,490,000.00 USD | 3,210,000.00 USD |
| `1D` | `2435.60` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 1,920,000.00 USD | 623,860.00 USD | 401,450.00 USD |
| `7D` | `2436.90` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 0.00 USD | 6,210,000.00 USD | 6,860,000.00 USD | 6,070,000.00 USD |
| `1D` | `2438.00` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 1,050,000.00 USD | 517,090.00 USD | 15,480.00 USD |
| `7D` | `2439.70` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 0.00 USD | 13,650,000.00 USD | 5,510,000.00 USD | 3,760,000.00 USD |
| `1D` | `2440.40` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 1,230,000.00 USD | 1,190,000.00 USD | 858,540.00 USD |
| `7D` | `2442.50` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 0.00 USD | 5,050,000.00 USD | 4,770,000.00 USD | 7,900,000.00 USD |
| `1D` | `2442.80` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 1,040,000.00 USD | 42,810.00 USD | 269,940.00 USD |
| `1D` | `2445.20` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 13,780.00 USD | 703,990.00 USD | 1,230,000.00 USD |
| `7D` | `2445.30` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 0.00 USD | 9,990,000.00 USD | 8,050,000.00 USD | 10,380,000.00 USD |
| `1D` | `2447.60` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 1,210,000.00 USD | 650,590.00 USD | 1,540,000.00 USD |
| `7D` | `2448.10` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 7,630,000.00 USD | 3,230,000.00 USD | 15,070,000.00 USD |
| `1D` | `2450.00` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 472,590.00 USD | 307,670.00 USD | 26,770.00 USD |
| `7D` | `2450.90` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 0.00 USD | 11,570,000.00 USD | 7,800,000.00 USD | 7,080,000.00 USD |
| `1D` | `2452.40` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 3,200,000.00 USD | 1,620,000.00 USD | 2,240,000.00 USD |
| `7D` | `2453.70` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 0.00 USD | 4,220,000.00 USD | 2,980,000.00 USD | 3,870,000.00 USD |
| `1D` | `2454.80` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 2,270,000.00 USD | 2,210,000.00 USD | 1,030,000.00 USD |
| `7D` | `2456.50` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 8,170,000.00 USD | 6,240,000.00 USD | 7,490,000.00 USD |
| `1D` | `2457.20` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 1,720,000.00 USD | 1,920,000.00 USD | 841,740.00 USD |
| `7D` | `2459.30` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 3,390,000.00 USD | 5,570,000.00 USD | 5,720,000.00 USD |
| `1D` | `2459.60` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 1,580,000.00 USD | 1,430,000.00 USD | 383,730.00 USD |
| `1D` | `2462.00` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 0.00 USD | 551,660.00 USD | 829,050.00 USD |
| `7D` | `2462.10` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 0.00 USD | 4,880,000.00 USD | 6,420,000.00 USD | 5,440,000.00 USD |
| `1D` | `2464.10` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 303,600.00 USD | 280,900.00 USD | 179,670.00 USD |
| `7D` | `2464.90` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 0.00 USD | 6,130,000.00 USD | 3,130,000.00 USD | 2,800,000.00 USD |
| `7D` | `2467.70` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 0.00 USD | 3,400,000.00 USD | 1,870,000.00 USD | 45,590.00 USD |
| `7D` | `2470.50` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 0.00 USD | 2,410,000.00 USD | 2,050,000.00 USD | 522,210.00 USD |
| `7D` | `2473.30` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 0.00 USD | 6,230,000.00 USD | 2,920,000.00 USD | 3,180,000.00 USD |
| `7D` | `2476.10` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 0.00 USD | 2,600,000.00 USD | 1,680,000.00 USD | 872,130.00 USD |
| `7D` | `2478.90` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 0.00 USD | 3,150,000.00 USD | 4,160,000.00 USD | 540,990.00 USD |
| `7D` | `2481.70` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 0.00 USD | 601,420.00 USD | 3,680,000.00 USD | 1,050,000.00 USD |
| `7D` | `2484.50` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 0.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD |
| `7D` | `2487.30` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 0.00 USD | 275,450.00 USD | 211,130.00 USD | 0.00 USD |
| `7D` | `2490.10` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 0.00 USD | 385,480.00 USD | 14,400.00 USD | 0.00 USD |
| `7D` | `2492.90` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 0.00 USD | 2,960,000.00 USD | 1,020,000.00 USD | 1,470,000.00 USD |
| `7D` | `2495.10` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 0.00 USD | 773,650.00 USD | 736,470.00 USD | 2,640,000.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `28.47B` | Total OI Tokens: `12,776,725.7 ETH`
  * 1h OI Change: `+0.14%` | 4h OI Change: `-2.07%` | 24h OI Change: `-5.67%`
  * Exchange Breakdown: Binance=`8.41B` | Bybit=`2.10B` | OKX=`1.75B` | Hyperliquid=`2.35B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-135.98K` | Last 24h: `195.10K` | Last 3d: `5.21M` | Last 7d: `11.81M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0029%` | **USDT OKX** | `-0.0034%` |
| **USDT Bybit** | `-0.0018%` | **USDT KuCoin** | `-0.0045%` |
| **USDT MEXC** | `-0.0029%` | **USDT BingX** | `0.0011%` |
| **USDT Gate** | `0.0073%` | **USDT Bitget** | `0.0012%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0019%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `48.28%` | `51.72%` | `0.93` | 600,460,000.00 USD |
| `15M` | `Binance` | `40.87%` | `59.13%` | `0.69` | 195,290,000.00 USD |
| `15M` | `OKX` | `46.51%` | `53.49%` | `0.87` | 76,260,000.00 USD |
| `15M` | `Bybit` | `58.39%` | `41.61%` | `1.40` | 49,780,000.00 USD |
| `15M` | `KuCoin` | `57.61%` | `42.39%` | `1.36` | 1,210,000.00 USD |
| `15M` | `Gate` | `49.1%` | `50.9%` | `0.96` | 66,010,000.00 USD |
| `15M` | `Bitget` | `45.69%` | `54.31%` | `0.84` | 26,540,000.00 USD |
| `15M` | `BingX` | `50.11%` | `49.89%` | `1.00` | 20,430,000.00 USD |
| `15M` | `MEXC` | `46.96%` | `53.04%` | `0.89` | 43,790,000.00 USD |
| `15M` | `Bitunix` | `46.33%` | `53.67%` | `0.86` | 30,480,000.00 USD |
| `15M` | `Hyperliquid` | `71.6%` | `28.4%` | `2.52` | 42,790,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `68.64%` | `31.36%` | `2.19` | 4,520,000.00 USD |
| `15M` | `Crypto.com` | `46.08%` | `53.92%` | `0.85` | 1,540,000.00 USD |
| `15M` | `WhiteBIT` | `99.24%` | `0.76%` | `130.58` | 1,630,000.00 USD |
| `15M` | `HTX` | `45.24%` | `54.76%` | `0.83` | 1,580,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `46.77%` | `53.23%` | `0.88` | 23,260,000.00 USD |
| `15M` | `Bitfinex` | `72.14%` | `27.86%` | `2.59` | 332,270.00 USD |
| `15M` | `Kraken` | `54.78%` | `45.22%` | `1.21` | 3,700,000.00 USD |
| `15M` | `Aster` | `49.86%` | `50.14%` | `0.99` | 4,760,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `47.38%` | `52.62%` | `0.90` | 6,580,000.00 USD |
| `15M` | `Whale Positions` | `40.87%` | `59.13%` | `0.69` | 195,290,000.00 USD |
| `15M` | `Global Accounts` | `48.28%` | `51.72%` | `0.93` | 600,460,000.00 USD |
| `1H` | `ETH` | `43.30%` | `56.70%` | `0.76` | 2,440,000,000.00 USD |
| `1H` | `Binance` | `42.05%` | `57.95%` | `0.73` | 670,330,000.00 USD |
| `1H` | `OKX` | `42.71%` | `57.29%` | `0.75` | 349,800,000.00 USD |
| `1H` | `Bybit` | `43.91%` | `56.09%` | `0.78` | 227,040,000.00 USD |
| `1H` | `KuCoin` | `42.93%` | `57.07%` | `0.75` | 7,050,000.00 USD |
| `1H` | `Gate` | `49.36%` | `50.64%` | `0.97` | 235,740,000.00 USD |
| `1H` | `Bitget` | `44.19%` | `55.81%` | `0.79` | 118,790,000.00 USD |
| `1H` | `BingX` | `50.81%` | `49.19%` | `1.03` | 56,230,000.00 USD |
| `1H` | `MEXC` | `42.07%` | `57.93%` | `0.73` | 147,960,000.00 USD |
| `1H` | `Bitunix` | `48.51%` | `51.49%` | `0.94` | 114,700,000.00 USD |
| `1H` | `Hyperliquid` | `49.62%` | `50.38%` | `0.98` | 188,920,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `58.74%` | `41.26%` | `1.42` | 39,090,000.00 USD |
| `1H` | `Crypto.com` | `44.69%` | `55.31%` | `0.81` | 7,810,000.00 USD |
| `1H` | `WhiteBIT` | `3.95%` | `96.05%` | `0.04` | 97,970,000.00 USD |
| `1H` | `HTX` | `46.6%` | `53.4%` | `0.87` | 7,790,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `49.68%` | `50.32%` | `0.99` | 109,340,000.00 USD |
| `1H` | `Bitfinex` | `38.2%` | `61.8%` | `0.62` | 1,440,000.00 USD |
| `1H` | `Kraken` | `30.19%` | `69.81%` | `0.43` | 18,350,000.00 USD |
| `1H` | `Aster` | `36.98%` | `63.02%` | `0.59` | 16,150,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `51.99%` | `48.01%` | `1.08` | 25,330,000.00 USD |
| `1H` | `Whale Positions` | `42.05%` | `57.95%` | `0.73` | 670,330,000.00 USD |
| `1H` | `Global Accounts` | `43.30%` | `56.70%` | `0.76` | 2,440,000,000.00 USD |
| `4H` | `ETH` | `44.30%` | `55.70%` | `0.80` | 9,730,000,000.00 USD |
| `4H` | `Binance` | `43.04%` | `56.96%` | `0.76` | 2,890,000,000.00 USD |
| `4H` | `OKX` | `45.43%` | `54.57%` | `0.83` | 1,380,000,000.00 USD |
| `4H` | `Bybit` | `42.28%` | `57.72%` | `0.73` | 837,960,000.00 USD |
| `4H` | `KuCoin` | `44.1%` | `55.9%` | `0.79` | 22,950,000.00 USD |
| `4H` | `Gate` | `48.94%` | `51.06%` | `0.96` | 951,940,000.00 USD |
| `4H` | `Bitget` | `43.77%` | `56.23%` | `0.78` | 441,820,000.00 USD |
| `4H` | `BingX` | `41.62%` | `58.38%` | `0.71` | 198,010,000.00 USD |
| `4H` | `MEXC` | `43.3%` | `56.7%` | `0.76` | 441,370,000.00 USD |
| `4H` | `Bitunix` | `44.12%` | `55.88%` | `0.79` | 375,970,000.00 USD |
| `4H` | `Hyperliquid` | `35.29%` | `64.71%` | `0.55` | 548,050,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.87%` | `49.13%` | `1.04` | 696,900,000.00 USD |
| `4H` | `Crypto.com` | `46.06%` | `53.94%` | `0.85` | 30,010,000.00 USD |
| `4H` | `WhiteBIT` | `27.36%` | `72.64%` | `0.38` | 204,060,000.00 USD |
| `4H` | `HTX` | `44.69%` | `55.31%` | `0.81` | 34,300,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `51.36%` | `48.64%` | `1.06` | 452,000,000.00 USD |
| `4H` | `Bitfinex` | `31.41%` | `68.59%` | `0.46` | 5,010,000.00 USD |
| `4H` | `Kraken` | `41.42%` | `58.58%` | `0.71` | 28,500,000.00 USD |
| `4H` | `Aster` | `48.25%` | `51.75%` | `0.93` | 81,250,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `53.31%` | `46.69%` | `1.14` | 112,630,000.00 USD |
| `4H` | `Whale Positions` | `43.04%` | `56.96%` | `0.76` | 2,890,000,000.00 USD |
| `4H` | `Global Accounts` | `44.30%` | `55.70%` | `0.80` | 9,730,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `2230.25` | `2237.42` | `2230.25` | `2248.75` | `2228.25` | 239,005,598.88 USD | 101,154,920.14 USD | 137,850,678.73 USD | -36,695,758.59 USD | `-15.35%` | `0B / 8S` |
| `5:00 UTC` | `2232.75` | `2233.33` | `2232.75` | `2238.25` | `2228.25` | 153,884,513.89 USD | 97,714,432.25 USD | 56,170,081.64 USD | 41,544,350.61 USD | `+27.00%` | `5B / 1S` |
| `0:00 UTC` | `2227.75` | `2228.98` | `2227.75` | `2236.75` | `2223.25` | 107,078,982.08 USD | 47,873,893.40 USD | 59,205,088.68 USD | -11,331,195.28 USD | `-10.58%` | `0B / 1S` |
| `5:00 UTC` | `2233.25` | `2230.29` | `2233.25` | `2234.75` | `2224.25` | 95,342,735.21 USD | 45,163,958.47 USD | 50,178,776.75 USD | -5,014,818.28 USD | `-5.26%` | `0B / 3S` |
| `0:00 UTC` | `2224.25` | `2226.52` | `2224.25` | `2230.75` | `2223.25` | 103,679,050.63 USD | 41,811,152.44 USD | 61,867,898.19 USD | -20,056,745.75 USD | `-19.35%` | `0B / 2S` |
| `5:00 UTC` | `2223.75` | `2226.83` | `2223.75` | `2231.75` | `2223.25` | 59,922,094.97 USD | 29,249,984.51 USD | 30,672,110.46 USD | -1,422,125.96 USD | `-2.37%` | `1B / 1S` |
| `0:00 UTC` | `2222.75` | `2224.81` | `2222.75` | `2229.75` | `2221.25` | 65,855,959.19 USD | 30,261,207.11 USD | 35,594,752.09 USD | -5,333,544.98 USD | `-8.10%` | `0B / 4S` |
| `5:00 UTC` | `2221.75` | `2223.05` | `2221.75` | `2226.25` | `2220.25` | 71,858,619.15 USD | 38,686,757.89 USD | 33,171,861.26 USD | 5,514,896.63 USD | `+7.67%` | `0B / 0S` |
| `0:00 UTC` | `2229.25` | `2226.54` | `2229.25` | `2231.25` | `2220.25` | 81,297,282.61 USD | 40,950,851.56 USD | 40,346,431.05 USD | 604,420.51 USD | `+0.74%` | `0B / 2S` |
| `5:00 UTC` | `2227.25` | `2227.90` | `2227.25` | `2229.75` | `2226.75` | 16,523,576.57 USD | 8,352,031.60 USD | 8,171,544.97 USD | 180,486.62 USD | `+1.09%` | `0B / 1S` |

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
| `5m` | 1,660,000.00 USD | 11,560,000.00 USD | **`ACCUMULATION`** |
| `15m` | 1,280,000.00 USD | 29,340,000.00 USD | **`ACCUMULATION`** |
| `30m` | -4,720,000.00 USD | 17,800,000.00 USD | **`ACCUMULATION`** |
| `1h` | -19,440,000.00 USD | -23,820,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -24,830,000.00 USD | -84,440,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -11,900,000.00 USD | -87,640,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -11,770,000.00 USD | -51,480,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,150,000.00 USD | -351,770,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -85,650,000.00 USD | -734,140,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -150,950,000.00 USD | -1,950,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -218,170,000.00 USD | -3,080,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,180,000,000.00 USD | -9,790,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+1.66M` | 15m=`+1.28M` | 1h=`-19.44M` | 24h=`-150.95M`
* Futures Capital Netflows: 5m=`+11.56M` | 15m=`+29.34M` | 1h=`-23.82M` | 24h=`-1.95B`
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
  * `2026-10-30 15:12:05 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:05 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:05 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:34:05 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:05 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:15:05 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:15:05 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `2194.81` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2175.82` (Risk Distance: `18.99` pts)
  * +2.5R Take Profit: `2242.28`
  * Mathematical Lot Sizing: **`0.52 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2252.28` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2271.27` (Risk Distance: `18.99` pts)
  * +2.5R Take Profit: `2204.81`
  * Mathematical Lot Sizing: **`0.52 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2243.91`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
