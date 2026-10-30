# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 15:27:09 IST` (`2026-10-30 09:57:09 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `1` | `0x5b5d...c060` | `SHORT` | 228,804,095.55 USD | `102,676.40` | `2322.74` | `2228.00` | `3723.47` | 9,686,817.59 USD | `+4.23%` | `5X Cross` |
| `5` | `0xb83d...6e36` | `SHORT` | 110,201,397.85 USD | `49,455.37` | `2375.30` | `2228.00` | `4631.54` | 7,270,260.58 USD | `+6.60%` | `5X Cross` |
| `9` | `0x77dd...e0e9` | `LONG` | 68,297,935.30 USD | `30,641.99` | `2610.31` | `2228.00` | `2121.80` | -11,687,239.74 USD | `-17.11%` | `10X Cross` |
| `10` | `0xde8d...9524` | `LONG` | 67,484,336.20 USD | `30,282.40` | `2134.45` | `2228.00` | `1786.06` | 2,848,005.62 USD | `+4.22%` | `20X Cross` |
| `15` | `0x0392...d7d9` | `LONG` | 57,996,826.38 USD | `26,025.05` | `2518.71` | `2228.00` | `2129.08` | -7,552,895.71 USD | `-13.02%` | `9X Cross` |
| `22` | `0x8add...7d2c` | `SHORT` | 49,129,509.84 USD | `22,046.99` | `2271.09` | `2228.00` | `2476.86` | 941,387.46 USD | `+1.92%` | `25X Cross` |
| `25` | `0x15a4...dfdb` | `SHORT` | 44,568,000.00 USD | `20,000.00` | `2228.11` | `2228.00` | `3187.77` | -5,672.32 USD | `-0.01%` | `20X Cross` |
| `26` | `0xdf95...7d72` | `SHORT` | 43,935,955.79 USD | `19,716.37` | `2402.53` | `2228.00` | `4232.41` | 3,433,301.30 USD | `+7.81%` | `25X Cross` |
| `33` | `0x6046...b21d` | `LONG` | 35,493,040.89 USD | `15,927.59` | `2410.19` | `2228.00` | `1785.07` | -2,895,578.76 USD | `-8.16%` | `6X Cross` |
| `35` | `0xefe4...194b` | `SHORT` | 33,664,123.60 USD | `15,108.89` | `2250.33` | `2228.00` | `2904.56` | 335,893.15 USD | `+1.00%` | `20X Cross` |
| `37` | `0xb695...a92d` | `SHORT` | 32,978,204.83 USD | `14,795.73` | `2557.74` | `2228.00` | `3779.16` | 4,865,509.29 USD | `+14.75%` | `20X Cross` |
| `38` | `0xeced...6210` | `SHORT` | 32,726,857.51 USD | `14,687.58` | `2522.09` | `2228.00` | `3647.34` | 4,316,660.02 USD | `+13.19%` | `20X Cross` |
| `40` | `0x45d2...4029` | `SHORT` | 31,087,575.00 USD | `13,950.00` | `2443.60` | `2228.00` | `5365.02` | 3,000,707.46 USD | `+9.65%` | `20X Cross` |
| `42` | `0xa61c...66b9` | `LONG` | 28,719,619.20 USD | `12,888.00` | `2369.69` | `2228.00` | `1488.35` | -1,821,035.34 USD | `-6.34%` | `10X Cross` |
| `45` | `0x2371...0883` | `LONG` | 26,739,600.00 USD | `12,000.00` | `2421.77` | `2228.00` | `1279.04` | -2,321,694.85 USD | `-8.68%` | `20X Cross` |
| `46` | `0xbd1c...ff0e` | `LONG` | 26,737,200.00 USD | `12,000.00` | `2419.91` | `2228.00` | `1519.94` | -2,301,832.39 USD | `-8.61%` | `20X Cross` |
| `53` | `0xa9de...e049` | `LONG` | 24,512,400.00 USD | `11,000.00` | `2481.81` | `2228.00` | `1643.68` | -2,787,579.46 USD | `-11.37%` | `20X Cross` |
| `54` | `0x0c5d...36b3` | `LONG` | 24,512,400.00 USD | `11,000.00` | `2482.20` | `2228.00` | `1644.01` | -2,791,853.24 USD | `-11.39%` | `20X Cross` |
| `55` | `0x6c93...59a4` | `LONG` | 24,512,400.00 USD | `11,000.00` | `2441.15` | `2228.00` | `1601.97` | -2,340,272.73 USD | `-9.55%` | `20X Cross` |
| `56` | `0x09dc...c094` | `LONG` | 24,509,100.00 USD | `11,000.00` | `2465.31` | `2228.00` | `1637.01` | -2,609,323.04 USD | `-10.65%` | `20X Cross` |
| `68` | `0xa2ce...3126` | `LONG` | 22,318,599.63 USD | `10,016.88` | `2162.83` | `2228.00` | `1558.36` | 653,797.58 USD | `+2.93%` | `10X Cross` |
| `69` | `0xb37f...66ca` | `SHORT` | 22,286,000.00 USD | `10,000.00` | `2290.69` | `2228.00` | `2623.84` | 620,991.85 USD | `+2.79%` | `25X Cross` |
| `71` | `0x6646...6de5` | `LONG` | 22,281,000.00 USD | `10,000.00` | `1765.80` | `2228.00` | `1719.85` | 4,622,942.55 USD | `+20.75%` | `25X Cross` |
| `72` | `0xec7f...df39` | `LONG` | 22,281,000.00 USD | `10,000.00` | `2719.35` | `2228.00` | `1720.53` | -4,912,548.52 USD | `-22.05%` | `20X Cross` |
| `73` | `0xecb6...2b00` | `SHORT` | 22,066,349.52 USD | `9,903.66` | `2239.95` | `2228.00` | `5427.21` | 117,407.37 USD | `+0.53%` | `15X Cross` |
| `75` | `0x939f...04d2` | `LONG` | 21,891,384.67 USD | `9,823.81` | `2427.28` | `2228.00` | `1707.49` | -1,953,765.94 USD | `-8.92%` | `25X Cross` |
| `77` | `0xaeaa...2416` | `SHORT` | 21,616,450.00 USD | `9,700.00` | `2311.92` | `2228.00` | `2657.69` | 809,232.40 USD | `+3.74%` | `25X Cross` |
| `84` | `0xf517...c032` | `SHORT` | 20,782,831.88 USD | `9,326.35` | `2202.91` | `2228.00` | `3117.81` | -237,693.66 USD | `-1.14%` | `25X Cross` |
| `86` | `0xca49...53c8` | `SHORT` | 20,464,589.52 USD | `9,181.89` | `2549.39` | `2228.00` | `3897.76` | 2,943,687.87 USD | `+14.38%` | `25X Cross` |
| `87` | `0xba5d...a352` | `SHORT` | 20,174,394.86 USD | `9,054.12` | `2493.89` | `2228.00` | `2766.59` | 2,405,612.40 USD | `+11.92%` | `20X Cross` |
| `88` | `0xea00...a918` | `LONG` | 20,065,026.91 USD | `9,003.83` | `2003.01` | `2228.00` | `1449.02` | 2,030,248.04 USD | `+10.12%` | `5X Cross` |
| `114` | `0x9eec...daab` | `LONG` | 18,037,266.49 USD | `8,092.45` | `1658.44` | `2228.00` | `1930.29` | 4,616,401.96 USD | `+25.59%` | `15X Cross` |
| `115` | `0x5f91...65aa` | `LONG` | 17,749,235.67 USD | `7,964.66` | `1626.99` | `2228.00` | `1843.86` | 4,790,792.61 USD | `+26.99%` | `16X Cross` |
| `125` | `0xec0b...b078` | `LONG` | 15,616,179.07 USD | `7,007.80` | `2065.97` | `2228.00` | `1056.89` | 1,138,249.48 USD | `+7.29%` | `25X Cross` |
| `130` | `0xf02d...5eb3` | `LONG` | 15,277,878.09 USD | `6,855.99` | `2383.33` | `2228.00` | `1126.46` | -1,062,210.68 USD | `-6.95%` | `20X Cross` |
| `131` | `0xcf53...ee11` | `SHORT` | 15,159,163.32 USD | `6,803.63` | `1862.69` | `2228.00` | `4192.91` | -2,486,057.93 USD | `-16.40%` | `7X Cross` |
| `136` | `0x4ff9...38d3` | `LONG` | 14,626,124.72 USD | `6,564.10` | `2447.40` | `2228.00` | `1669.63` | -1,438,898.02 USD | `-9.84%` | `3X Isolated` |
| `138` | `0xf78c...c581` | `LONG` | 14,485,743.61 USD | `6,500.22` | `2521.53` | `2228.00` | `1913.11` | -1,904,797.33 USD | `-13.15%` | `20X Cross` |
| `139` | `0x1ee7...edf5` | `LONG` | 14,485,250.00 USD | `6,500.00` | `2301.55` | `2228.00` | `2068.84` | -474,843.66 USD | `-3.28%` | `25X Cross` |
| `141` | `0x4e23...20c3` | `LONG` | 14,184,454.35 USD | `6,365.31` | `2228.10` | `2228.00` | `290.47` | 1,876.92 USD | `+0.01%` | `20X Cross` |
| `145` | `0x799f...5f4c` | `LONG` | 14,063,216.91 USD | `6,310.90` | `2390.33` | `2228.00` | `1867.55` | -1,021,947.70 USD | `-7.27%` | `20X Cross` |
| `149` | `0x08bf...7872` | `SHORT` | 13,869,667.23 USD | `6,224.05` | `2258.00` | `2228.00` | `2584.91` | 184,248.88 USD | `+1.33%` | `20X Cross` |
| `151` | `0xec4a...cf62` | `LONG` | 13,741,720.74 USD | `6,166.63` | `2225.41` | `2228.00` | `1959.28` | 18,401.31 USD | `+0.13%` | `25X Cross` |
| `153` | `0x524e...0de0` | `LONG` | 13,371,000.00 USD | `6,000.00` | `2246.48` | `2228.00` | `2002.81` | -107,885.04 USD | `-0.81%` | `10X Cross` |
| `154` | `0xd9e7...4aff` | `LONG` | 13,370,400.00 USD | `6,000.00` | `2480.18` | `2228.00` | `1407.40` | -1,510,724.33 USD | `-11.30%` | `20X Cross` |
| `156` | `0xc179...e0c8` | `LONG` | 13,046,096.20 USD | `5,854.73` | `2294.94` | `2228.00` | `1204.50` | -390,175.98 USD | `-2.99%` | `10X Cross` |
| `163` | `0x0c4a...1b19` | `LONG` | 12,611,829.25 USD | `5,660.10` | `2373.06` | `2228.00` | `2081.45` | -819,928.88 USD | `-6.50%` | `25X Isolated` |
| `169` | `0x7fda...17d1` | `LONG` | 11,844,041.74 USD | `5,315.76` | `2211.05` | `2228.00` | `0.000000` | 90,599.49 USD | `+0.76%` | `25X Cross` |
| `186` | `0x45ab...6cbc` | `LONG` | 10,966,364.26 USD | `4,920.96` | `2727.66` | `2228.00` | `1376.87` | -2,456,379.53 USD | `-22.40%` | `7X Cross` |
| `190` | `0x64b7...9da9` | `LONG` | 10,822,980.47 USD | `4,856.84` | `2604.61` | `2228.00` | `592.93` | -1,827,233.94 USD | `-16.88%` | `25X Cross` |
| `195` | `0xfb18...eb17` | `SHORT` | 10,627,276.35 USD | `4,768.16` | `2315.53` | `2228.00` | `2623.50` | 413,553.35 USD | `+3.89%` | `25X Cross` |
| `198` | `0x5559...d43b` | `SHORT` | 10,598,103.94 USD | `4,755.93` | `2262.69` | `2228.00` | `2744.42` | 163,101.94 USD | `+1.54%` | `25X Cross` |
| `208` | `0xe091...6705` | `SHORT` | 10,027,800.45 USD | `4,500.00` | `2467.33` | `2228.00` | `2463.03` | 1,075,208.06 USD | `+10.72%` | `20X Cross` |
| `210` | `0x418a...8888` | `SHORT` | 10,026,450.00 USD | `4,500.00` | `2494.55` | `2228.00` | `2993.17` | 1,199,034.41 USD | `+11.96%` | `25X Cross` |
| `218` | `0xb829...3a81` | `LONG` | 9,792,301.20 USD | `4,394.91` | `2398.60` | `2228.00` | `1455.73` | -749,340.75 USD | `-7.65%` | `20X Cross` |
| `235` | `0x28bb...fca6` | `SHORT` | 9,380,704.28 USD | `4,209.61` | `1896.10` | `2228.00` | `3034.27` | -1,398,821.72 USD | `-14.91%` | `20X Cross` |
| `238` | `0x6ea4...0ea7` | `SHORT` | 9,321,561.00 USD | `4,184.01` | `2602.13` | `2228.00` | `3424.97` | 1,565,785.66 USD | `+16.80%` | `20X Cross` |
| `252` | `0x5e9e...35ee` | `SHORT` | 8,932,040.14 USD | `4,007.56` | `1796.39` | `2228.00` | `2585.47` | -1,732,890.05 USD | `-19.40%` | `20X Cross` |
| `253` | `0xfb94...0ddf` | `SHORT` | 8,917,882.33 USD | `4,002.10` | `2382.44` | `2228.00` | `5104.36` | 616,901.82 USD | `+6.92%` | `20X Cross` |
| `254` | `0x8cc9...2b6a` | `SHORT` | 8,913,600.00 USD | `4,000.00` | `1791.18` | `2228.00` | `3532.31` | -1,748,853.33 USD | `-19.62%` | `25X Cross` |
| `255` | `0x3dc9...54b0` | `SHORT` | 8,913,309.61 USD | `3,999.69` | `2480.32` | `2228.00` | `6620.72` | 1,007,226.94 USD | `+11.30%` | `20X Cross` |
| `270` | `0x4b67...f4e7` | `LONG` | 8,513,982.01 USD | `3,820.84` | `2591.51` | `2228.00` | `1347.83` | -1,387,791.54 USD | `-16.30%` | `20X Cross` |
| `277` | `0x12d2...f97f` | `LONG` | 8,372,680.86 USD | `3,757.26` | `2446.50` | `2228.00` | `1794.39` | -819,485.53 USD | `-9.79%` | `20X Cross` |
| `295` | `0x8ae4...3d60` | `LONG` | 7,935,849.67 USD | `3,558.20` | `2482.21` | `2228.00` | `518.88` | -896,348.37 USD | `-11.29%` | `10X Cross` |
| `300` | `0x469e...58a5` | `SHORT` | 7,873,679.70 USD | `3,533.33` | `2203.63` | `2228.00` | `3081.20` | -87,516.61 USD | `-1.11%` | `25X Cross` |
| `308` | `0x218a...7da2` | `SHORT` | 7,721,557.98 USD | `3,465.07` | `2208.16` | `2228.00` | `3101.69` | -70,128.72 USD | `-0.91%` | `10X Cross` |
| `337` | `0x9c2a...f6a8` | `SHORT` | 6,690,823.22 USD | `3,002.39` | `2515.77` | `2228.00` | `2583.61` | 862,514.68 USD | `+12.89%` | `20X Cross` |
| `338` | `0x007d...67a0` | `LONG` | 6,687,000.00 USD | `3,000.00` | `2400.00` | `2228.00` | `1470.68` | -513,000.00 USD | `-7.67%` | `25X Cross` |
| `339` | `0x4a20...3c26` | `LONG` | 6,685,800.00 USD | `3,000.00` | `2428.72` | `2228.00` | `623.71` | -600,360.28 USD | `-8.98%` | `20X Cross` |
| `340` | `0xb823...9763` | `SHORT` | 6,684,300.00 USD | `3,000.00` | `2229.66` | `2228.00` | `3233.36` | 4,696.68 USD | `+0.07%` | `25X Cross` |
| `394` | `0x8328...f54a` | `SHORT` | 5,741,105.99 USD | `2,576.45` | `2292.01` | `2228.00` | `3279.21` | 164,165.30 USD | `+2.86%` | `25X Cross` |
| `397` | `0xed48...7c9b` | `SHORT` | 5,684,939.21 USD | `2,551.13` | `2460.02` | `2228.00` | `3225.61` | 590,907.20 USD | `+10.39%` | `20X Cross` |
| `400` | `0x970c...2a93` | `SHORT` | 5,571,000.00 USD | `2,500.00` | `2229.57` | `2228.00` | `5078.78` | 2,944.49 USD | `+0.05%` | `20X Cross` |
| `401` | `0x1c98...7fc7` | `LONG` | 5,570,510.03 USD | `2,500.00` | `2452.60` | `2228.00` | `1916.60` | -561,011.54 USD | `-10.07%` | `10X Cross` |
| `413` | `0xa445...329d` | `LONG` | 5,363,036.08 USD | `2,406.14` | `2354.86` | `2228.00` | `1769.07` | -303,079.20 USD | `-5.65%` | `25X Cross` |
| `417` | `0xfbe2...c8ea` | `SHORT` | 5,315,670.09 USD | `2,385.21` | `2041.57` | `2228.00` | `2624.22` | -446,103.44 USD | `-8.39%` | `20X Cross` |
| `418` | `0x6749...ce07` | `SHORT` | 5,314,498.24 USD | `2,384.89` | `2220.92` | `2228.00` | `3630.19` | -17,835.20 USD | `-0.34%` | `20X Cross` |
| `419` | `0x645b...87b8` | `SHORT` | 5,302,823.63 USD | `2,379.98` | `2421.64` | `2228.00` | `11599.52` | 460,623.32 USD | `+8.69%` | `10X Cross` |
| `428` | `0x77ee...2902` | `SHORT` | 5,104,118.13 USD | `2,290.69` | `2476.53` | `2228.00` | `6160.58` | 568,854.10 USD | `+11.15%` | `25X Cross` |
| `452` | `0xd507...c948` | `SHORT` | 4,840,084.58 USD | `2,172.00` | `2387.49` | `2228.00` | `2600.21` | 345,556.45 USD | `+7.14%` | `5X Isolated` |
| `458` | `0x023a...2355` | `LONG` | 4,775,064.54 USD | `2,142.82` | `2328.93` | `2228.00` | `0.000000` | -215,439.31 USD | `-4.51%` | `25X Cross` |
| `463` | `0x382b...3e39` | `SHORT` | 4,745,257.55 USD | `2,129.54` | `2296.66` | `2228.00` | `4551.10` | 145,579.67 USD | `+3.07%` | `25X Cross` |
| `495` | `0x3453...b323` | `SHORT` | 4,457,274.33 USD | `2,000.12` | `2322.47` | `2228.00` | `2398.01` | 187,961.51 USD | `+4.22%` | `25X Cross` |
| `496` | `0xe02e...d78b` | `LONG` | 4,456,800.00 USD | `2,000.00` | `2228.11` | `2228.00` | `2171.55` | 576.53 USD | `+0.01%` | `25X Cross` |
| `501` | `0xf3dc...1672` | `SHORT` | 4,413,037.12 USD | `1,980.36` | `2240.44` | `2228.00` | `2791.01` | 23,850.43 USD | `+0.54%` | `20X Cross` |
| `505` | `0x7a6d...f79c` | `SHORT` | 4,393,156.00 USD | `1,971.44` | `2418.41` | `2228.00` | `2543.09` | 374,605.17 USD | `+8.53%` | `25X Cross` |
| `506` | `0xac48...3201` | `SHORT` | 4,377,597.43 USD | `1,964.37` | `2272.04` | `2228.00` | `3080.95` | 85,544.87 USD | `+1.95%` | `20X Cross` |
| `519` | `0x8376...9a1e` | `SHORT` | 4,257,158.24 USD | `1,910.50` | `2477.72` | `2228.00` | `3186.33` | 476,529.93 USD | `+11.19%` | `20X Cross` |
| `523` | `0x739c...cfb2` | `SHORT` | 4,234,150.00 USD | `1,900.00` | `2418.12` | `2228.00` | `2443.38` | 360,296.38 USD | `+8.51%` | `25X Cross` |
| `529` | `0x0622...8088` | `SHORT` | 4,183,335.65 USD | `1,877.28` | `2229.25` | `2228.00` | `7452.43` | 1,599.71 USD | `+0.04%` | `5X Cross` |
| `549` | `0x7265...91a5` | `LONG` | 4,015,285.77 USD | `1,801.87` | `2533.96` | `2228.00` | `1987.07` | -550,580.69 USD | `-13.71%` | `20X Cross` |
| `550` | `0xbb34...1696` | `LONG` | 4,011,300.00 USD | `1,800.00` | `2313.95` | `2228.00` | `1990.76` | -153,818.23 USD | `-3.83%` | `25X Cross` |
| `551` | `0xc619...10f5` | `LONG` | 4,011,120.00 USD | `1,800.00` | `2313.55` | `2228.00` | `1824.14` | -153,275.83 USD | `-3.82%` | `25X Cross` |
| `563` | `0x91a9...3f70` | `SHORT` | 3,938,475.68 USD | `1,767.48` | `2156.23` | `2228.00` | `3672.61` | -127,371.60 USD | `-3.23%` | `4X Cross` |
| `564` | `0xbcd4...0dd2` | `SHORT` | 3,935,057.88 USD | `1,766.10` | `2233.24` | `2228.00` | `2744.57` | 9,092.99 USD | `+0.23%` | `25X Cross` |
| `595` | `0xfeec...4e9c` | `SHORT` | 3,770,026.73 USD | `1,691.81` | `2566.49` | `2228.00` | `2509.55` | 571,997.78 USD | `+15.17%` | `10X Cross` |
| `618` | `0xeee0...0b53` | `LONG` | 3,648,003.19 USD | `1,637.12` | `2468.64` | `2228.00` | `180.78` | -393,472.87 USD | `-10.79%` | `7X Cross` |
| `622` | `0x27b8...12fc` | `LONG` | 3,631,196.26 USD | `1,628.12` | `2468.73` | `2228.00` | `635.34` | -388,198.38 USD | `-10.69%` | `10X Cross` |
| `625` | `0x982b...4606` | `LONG` | 3,625,362.35 USD | `1,626.82` | `2575.24` | `2228.00` | `1547.35` | -564,090.72 USD | `-15.56%` | `5X Isolated` |
| `632` | `0x73d7...8be1` | `LONG` | 3,569,666.60 USD | `1,601.47` | `2410.40` | `2228.00` | `1766.64` | -290,512.32 USD | `-8.14%` | `25X Cross` |
| `633` | `0xad54...6203` | `LONG` | 3,559,761.37 USD | `1,597.45` | `2591.98` | `2228.00` | `2043.76` | -580,816.68 USD | `-16.32%` | `10X Isolated` |
| `637` | `0x880a...311c` | `LONG` | 3,516,990.21 USD | `1,578.40` | `2209.72` | `2228.00` | `0.000000` | 29,166.36 USD | `+0.83%` | `9X Cross` |
| `644` | `0x936c...bb0f` | `LONG` | 3,495,096.81 USD | `1,568.64` | `2232.92` | `2228.00` | `0.000000` | -7,572.81 USD | `-0.22%` | `20X Cross` |
| `659` | `0xe170...9300` | `SHORT` | 3,417,028.56 USD | `1,533.40` | `2076.39` | `2228.00` | `3110.75` | -233,079.06 USD | `-6.82%` | `25X Cross` |
| `661` | `0x4b86...df9d` | `SHORT` | 3,396,081.60 USD | `1,524.00` | `2287.40` | `2228.00` | `2759.56` | 89,916.00 USD | `+2.65%` | `9X Isolated` |
| `669` | `0x2e2b...2fab` | `LONG` | 3,359,038.91 USD | `1,507.38` | `2245.53` | `2228.00` | `1259.04` | -25,834.19 USD | `-0.77%` | `25X Cross` |
| `673` | `0x251f...6e5d` | `LONG` | 3,342,600.00 USD | `1,500.00` | `2346.68` | `2228.00` | `1895.72` | -177,430.49 USD | `-5.31%` | `20X Cross` |
| `674` | `0xde6b...3361` | `LONG` | 3,342,600.00 USD | `1,500.00` | `2216.98` | `2228.00` | `2168.48` | 17,119.26 USD | `+0.51%` | `25X Cross` |
| `693` | `0xb885...3c54` | `LONG` | 3,232,794.40 USD | `1,450.00` | `2274.34` | `2228.00` | `31.92` | -65,013.73 USD | `-2.01%` | `20X Cross` |
| `695` | `0xef70...a84c` | `SHORT` | 3,215,009.39 USD | `1,442.74` | `2424.73` | `2228.00` | `3244.53` | 283,261.43 USD | `+8.81%` | `25X Cross` |
| `704` | `0xbadb...9ee6` | `LONG` | 3,182,511.74 USD | `1,428.16` | `1936.00` | `2228.00` | `1081.85` | 417,590.10 USD | `+13.12%` | `20X Cross` |
| `708` | `0x4487...c92d` | `LONG` | 3,167,625.60 USD | `1,421.67` | `2232.11` | `2228.00` | `1582.84` | -5,701.99 USD | `-0.18%` | `10X Cross` |
| `747` | `0x020c...5872` | `LONG` | 3,063,637.50 USD | `1,375.00` | `2226.32` | `2228.00` | `2142.75` | 2,436.55 USD | `+0.08%` | `25X Cross` |
| `757` | `0x53f8...ceff` | `LONG` | 3,005,341.24 USD | `1,348.65` | `2276.73` | `2228.00` | `0.000000` | -65,183.23 USD | `-2.17%` | `20X Cross` |
| `777` | `0xa0fb...96be` | `LONG` | 2,934,613.58 USD | `1,317.09` | `2277.10` | `2228.00` | `1519.85` | -64,548.71 USD | `-2.20%` | `3X Cross` |
| `780` | `0x0dd5...f6ee` | `LONG` | 2,930,085.95 USD | `1,314.88` | `2288.48` | `2228.00` | `1559.39` | -78,998.69 USD | `-2.70%` | `5X Cross` |
| `809` | `0x1f16...6d07` | `LONG` | 2,821,154.40 USD | `1,266.00` | `2261.43` | `2228.00` | `1379.16` | -41,816.83 USD | `-1.48%` | `7X Cross` |
| `815` | `0xc435...c905` | `SHORT` | 2,781,043.20 USD | `1,248.00` | `2704.38` | `2228.00` | `3795.68` | 594,027.15 USD | `+21.36%` | `20X Cross` |
| `820` | `0x6859...7e1e` | `SHORT` | 2,756,873.53 USD | `1,237.15` | `2200.39` | `2228.00` | `4868.59` | -34,646.37 USD | `-1.26%` | `25X Cross` |
| `835` | `0x7277...0b98` | `SHORT` | 2,717,077.43 USD | `1,219.45` | `2206.05` | `2228.00` | `3405.60` | -26,889.63 USD | `-0.99%` | `20X Cross` |
| `836` | `0x7178...0854` | `LONG` | 2,715,598.43 USD | `1,218.63` | `2461.81` | `2228.00` | `1187.89` | -284,447.97 USD | `-10.47%` | `10X Cross` |
| `842` | `0xaaa1...ab8c` | `SHORT` | 2,674,200.00 USD | `1,200.00` | `2276.29` | `2228.00` | `2365.18` | 57,357.58 USD | `+2.14%` | `25X Isolated` |
| `858` | `0x07fd...689d` | `LONG` | 2,622,259.01 USD | `1,176.69` | `2416.34` | `2228.00` | `0.000000` | -221,040.93 USD | `-8.43%` | `25X Cross` |
| `873` | `0xfc27...9d9d` | `LONG` | 2,558,665.68 USD | `1,148.31` | `2237.33` | `2228.00` | `0.000000` | -10,490.26 USD | `-0.41%` | `25X Cross` |
| `914` | `0x2f80...f203` | `SHORT` | 2,426,269.66 USD | `1,088.94` | `1984.00` | `2228.00` | `2959.28` | -265,802.48 USD | `-10.96%` | `20X Cross` |
| `920` | `0x8eb7...b90f` | `LONG` | 2,401,741.81 USD | `1,077.74` | `2396.38` | `2228.00` | `1880.88` | -180,936.24 USD | `-7.53%` | `5X Isolated` |
| `923` | `0x2b61...2f6c` | `SHORT` | 2,398,873.88 USD | `1,076.60` | `2681.75` | `2228.00` | `6291.43` | 488,298.86 USD | `+20.36%` | `10X Cross` |
| `950` | `0x30af...393e` | `SHORT` | 2,320,027.75 USD | `1,041.16` | `2252.26` | `2228.00` | `2296.87` | 24,954.58 USD | `+1.08%` | `25X Cross` |
| `954` | `0x6f11...0389` | `SHORT` | 2,313,183.00 USD | `1,038.00` | `2333.39` | `2228.00` | `3002.54` | 108,876.88 USD | `+4.71%` | `25X Cross` |
| `960` | `0x2577...4897` | `LONG` | 2,293,847.00 USD | `1,029.51` | `2231.93` | `2228.00` | `0.000000` | -3,945.10 USD | `-0.17%` | `15X Cross` |
| `965` | `0x1b2a...f7a6` | `LONG` | 2,284,827.51 USD | `1,025.37` | `2737.51` | `2228.00` | `882.02` | -522,132.42 USD | `-22.85%` | `10X Cross` |
| `979` | `0x001a...fef6` | `SHORT` | 2,244,723.03 USD | `1,007.33` | `2022.19` | `2228.00` | `3089.66` | -207,715.07 USD | `-9.25%` | `10X Cross` |
| `980` | `0x02aa...1806` | `SHORT` | 2,244,221.86 USD | `1,007.10` | `2654.68` | `2228.00` | `3612.66` | 429,310.24 USD | `+19.13%` | `20X Cross` |
| `982` | `0xdb3a...cf3b` | `LONG` | 2,235,664.85 USD | `1,003.22` | `2705.01` | `2228.00` | `0.000000` | -478,042.04 USD | `-21.38%` | `4X Cross` |
| `986` | `0x8c02...b73f` | `SHORT` | 2,228,500.00 USD | `1,000.00` | `2250.37` | `2228.00` | `8098.34` | 21,871.47 USD | `+0.98%` | `20X Cross` |
| `987` | `0x5272...fcd9` | `SHORT` | 2,228,400.00 USD | `1,000.00` | `2241.82` | `2228.00` | `2830.71` | 13,424.49 USD | `+0.60%` | `5X Cross` |
| `988` | `0xf929...d1f9` | `SHORT` | 2,228,400.00 USD | `1,000.00` | `2423.37` | `2228.00` | `2926.09` | 194,970.17 USD | `+8.75%` | `25X Cross` |
| `989` | `0x6463...42f5` | `SHORT` | 2,228,100.00 USD | `1,000.00` | `2223.43` | `2228.00` | `3704.81` | -4,665.05 USD | `-0.21%` | `5X Cross` |
| `990` | `0xd7b8...9f55` | `LONG` | 2,226,171.60 USD | `999.00` | `2195.00` | `2228.00` | `0.000000` | 33,366.60 USD | `+1.50%` | `15X Cross` |
| `1016` | `0xb002...ed8a` | `SHORT` | 2,145,371.59 USD | `962.78` | `2299.66` | `2228.00` | `4197.53` | 68,706.32 USD | `+3.20%` | `25X Cross` |
| `1034` | `0xb1ec...e86a` | `SHORT` | 2,080,613.17 USD | `933.64` | `2272.72` | `2228.00` | `12551.60` | 41,293.78 USD | `+1.98%` | `25X Cross` |
| `1042` | `0xb812...b5e0` | `LONG` | 2,065,590.42 USD | `927.02` | `2263.21` | `2228.00` | `1164.66` | -32,459.16 USD | `-1.57%` | `25X Cross` |
| `1064` | `0xede2...f971` | `LONG` | 2,037,179.24 USD | `914.31` | `2208.16` | `2228.00` | `1462.93` | 18,222.25 USD | `+0.89%` | `5X Cross` |
| `1066` | `0x9606...4e5d` | `SHORT` | 2,034,521.85 USD | `913.00` | `2478.70` | `2228.00` | `3778.68` | 228,531.76 USD | `+11.23%` | `20X Cross` |
| `1083` | `0x5f10...d49d` | `LONG` | 2,005,380.00 USD | `900.00` | `2249.83` | `2228.00` | `1816.38` | -19,473.47 USD | `-0.97%` | `25X Cross` |
| `1095` | `0x51f6...2b39` | `LONG` | 1,983,782.72 USD | `890.15` | `2226.49` | `2228.00` | `747.76` | 1,875.83 USD | `+0.09%` | `25X Cross` |
| `1174` | `0x2828...93a0` | `LONG` | 1,870,969.10 USD | `839.60` | `2242.41` | `2228.00` | `2192.48` | -11,763.09 USD | `-0.63%` | `25X Cross` |
| `1176` | `0xcd27...52a8` | `LONG` | 1,865,718.70 USD | `837.21` | `2553.56` | `2228.00` | `1403.16` | -272,146.08 USD | `-14.59%` | `2X Cross` |
| `1232` | `0x04a9...95aa` | `LONG` | 1,782,800.00 USD | `800.00` | `2595.13` | `2228.00` | `1876.18` | -293,306.74 USD | `-16.45%` | `5X Cross` |
| `1233` | `0x7737...bf66` | `SHORT` | 1,782,256.27 USD | `799.79` | `2494.83` | `2228.00` | `25141.68` | 213,089.76 USD | `+11.96%` | `15X Cross` |
| `1263` | `0x458d...ab3b` | `LONG` | 1,726,368.74 USD | `774.75` | `2740.41` | `2228.00` | `1886.92` | -396,760.44 USD | `-22.98%` | `3X Isolated` |
| `1327` | `0xaa53...9cb7` | `LONG` | 1,627,270.50 USD | `730.34` | `2389.70` | `2228.00` | `1934.85` | -118,019.13 USD | `-7.25%` | `20X Cross` |
| `1328` | `0x3fc5...c0c1` | `SHORT` | 1,626,563.09 USD | `729.92` | `2702.11` | `2228.00` | `4725.60` | 345,779.11 USD | `+21.26%` | `25X Cross` |
| `1341` | `0xa189...94d7` | `SHORT` | 1,604,761.19 USD | `719.98` | `2691.84` | `2228.00` | `2914.81` | 333,311.47 USD | `+20.77%` | `25X Cross` |
| `1348` | `0x039c...0ebd` | `LONG` | 1,585,959.35 USD | `711.80` | `2226.24` | `2228.00` | `0.000000` | 1,323.57 USD | `+0.08%` | `25X Cross` |
| `1356` | `0x2f93...4404` | `LONG` | 1,576,317.25 USD | `707.47` | `1700.45` | `2228.00` | `1368.55` | 373,290.88 USD | `+23.68%` | `4X Isolated` |
| `1365` | `0x5605...fe0f` | `SHORT` | 1,564,446.16 USD | `702.14` | `2566.90` | `2228.00` | `3095.03` | 237,886.49 USD | `+15.21%` | `20X Cross` |
| `1374` | `0x26e6...6b28` | `LONG` | 1,559,950.00 USD | `700.00` | `1835.24` | `2228.00` | `2042.98` | 275,278.47 USD | `+17.65%` | `20X Cross` |
| `1375` | `0x0deb...0bc5` | `LONG` | 1,559,880.00 USD | `700.00` | `2071.05` | `2228.00` | `1597.14` | 110,144.21 USD | `+7.06%` | `20X Cross` |
| `1376` | `0x9599...c60a` | `LONG` | 1,559,295.27 USD | `699.74` | `2233.08` | `2228.00` | `0.000000` | -3,275.56 USD | `-0.21%` | `20X Cross` |
| `1421` | `0x7b22...8a34` | `LONG` | 1,525,925.71 USD | `684.73` | `2228.49` | `2228.00` | `2181.55` | 2.14 USD | `+0.00%` | `25X Cross` |
| `1431` | `0x248e...6be2` | `SHORT` | 1,517,176.35 USD | `680.93` | `2282.89` | `2228.00` | `3370.98` | 37,309.32 USD | `+2.46%` | `20X Cross` |
| `1433` | `0xdbd1...29dd` | `SHORT` | 1,516,673.24 USD | `680.70` | `3030.57` | `2228.00` | `3780.23` | 546,247.88 USD | `+36.02%` | `6X Cross` |
| `1440` | `0x71e5...be04` | `LONG` | 1,510,112.70 USD | `677.67` | `2727.27` | `2228.00` | `1470.70` | -338,072.91 USD | `-22.39%` | `20X Cross` |
| `1443` | `0x0b23...f37b` | `LONG` | 1,504,035.00 USD | `675.00` | `2238.15` | `2228.00` | `594.74` | -6,721.64 USD | `-0.45%` | `5X Cross` |
| `1465` | `0x0cac...6170` | `SHORT` | 1,465,436.00 USD | `657.50` | `2146.55` | `2228.00` | `2839.16` | -54,073.80 USD | `-3.69%` | `20X Cross` |
| `1494` | `0xf00e...fe3d` | `SHORT` | 1,432,593.79 USD | `642.88` | `2333.21` | `2228.00` | `2480.37` | 67,384.18 USD | `+4.70%` | `20X Cross` |
| `1495` | `0xb15b...dbae` | `SHORT` | 1,432,066.11 USD | `642.64` | `2290.80` | `2228.00` | `2325.78` | 40,101.37 USD | `+2.80%` | `25X Cross` |
| `1502` | `0xffb2...5ed6` | `SHORT` | 1,427,756.58 USD | `640.77` | `2672.96` | `2228.00` | `2490.47` | 284,991.76 USD | `+19.96%` | `20X Cross` |
| `1517` | `0x8505...1821` | `SHORT` | 1,412,780.53 USD | `633.96` | `2239.93` | `2228.00` | `3895.50` | 7,251.07 USD | `+0.51%` | `20X Cross` |
| `1537` | `0xfce0...f4c0` | `SHORT` | 1,389,692.60 USD | `623.60` | `3129.61` | `2228.00` | `2807.76` | 561,933.98 USD | `+40.44%` | `20X Cross` |
| `1585` | `0x7050...5fff` | `SHORT` | 1,339,443.16 USD | `601.11` | `2245.52` | `2228.00` | `3279.88` | 10,356.95 USD | `+0.77%` | `25X Cross` |
| `1586` | `0xad02...eb65` | `LONG` | 1,338,482.12 USD | `600.62` | `2460.69` | `2228.00` | `1078.62` | -139,458.44 USD | `-10.42%` | `5X Cross` |
| `1588` | `0x24fb...ed0f` | `LONG` | 1,337,253.93 USD | `600.10` | `2199.85` | `2228.00` | `0.000000` | 17,130.49 USD | `+1.28%` | `15X Cross` |
| `1589` | `0x638f...f5f0` | `LONG` | 1,337,100.00 USD | `600.00` | `4011.50` | `2228.00` | `431.17` | -1,069,803.53 USD | `-80.01%` | `25X Cross` |
| `1623` | `0xb8eb...1dd5` | `LONG` | 1,300,373.24 USD | `583.55` | `2232.72` | `2228.00` | `0.000000` | -2,521.24 USD | `-0.19%` | `25X Cross` |
| `1664` | `0x9362...7d7c` | `SHORT` | 1,263,488.32 USD | `566.99` | `2226.19` | `2228.00` | `2518.61` | -1,252.50 USD | `-0.10%` | `20X Cross` |
| `1668` | `0xfb99...37f3` | `LONG` | 1,259,862.64 USD | `565.34` | `2362.35` | `2228.00` | `1254.46` | -75,673.71 USD | `-6.01%` | `3X Cross` |
| `1683` | `0x844b...7f42` | `SHORT` | 1,250,132.40 USD | `561.00` | `2026.17` | `2228.00` | `3028.52` | -113,448.99 USD | `-9.07%` | `25X Cross` |
| `1699` | `0xabe6...1d99` | `SHORT` | 1,238,999.31 USD | `556.00` | `2484.68` | `2228.00` | `3123.96` | 142,496.58 USD | `+11.50%` | `20X Cross` |
| `1703` | `0x2a76...9a53` | `LONG` | 1,236,828.85 USD | `555.03` | `2231.40` | `2228.00` | `0.000000` | -1,667.25 USD | `-0.13%` | `25X Cross` |
| `1709` | `0xbef3...0d3e` | `LONG` | 1,230,750.25 USD | `552.33` | `2233.44` | `2228.00` | `2068.58` | -2,840.57 USD | `-0.23%` | `20X Cross` |
| `1713` | `0x6a41...a3b9` | `LONG` | 1,227,164.73 USD | `550.69` | `2233.05` | `2228.00` | `2074.03` | -2,561.63 USD | `-0.21%` | `20X Cross` |
| `1714` | `0x825c...465e` | `LONG` | 1,225,620.00 USD | `550.00` | `2208.12` | `2228.00` | `1189.21` | 11,150.50 USD | `+0.91%` | `4X Cross` |
| `1720` | `0xad21...fb6a` | `LONG` | 1,219,395.60 USD | `547.26` | `2565.80` | `2228.00` | `1734.74` | -184,757.40 USD | `-15.15%` | `6X Cross` |
| `1772` | `0x2e30...4cb5` | `SHORT` | 1,162,315.85 USD | `521.57` | `2316.72` | `2228.00` | `11909.50` | 46,016.02 USD | `+3.96%` | `2X Cross` |
| `1793` | `0x6dae...90de` | `SHORT` | 1,152,150.98 USD | `517.05` | `2292.28` | `2228.00` | `3857.44` | 33,082.43 USD | `+2.87%` | `25X Cross` |
| `1798` | `0xfc66...ca06` | `SHORT` | 1,148,928.68 USD | `515.65` | `2275.19` | `2228.00` | `17253.63` | 24,287.19 USD | `+2.11%` | `20X Cross` |
| `1825` | `0x0089...2410` | `SHORT` | 1,130,568.94 USD | `507.35` | `2308.88` | `2228.00` | `3365.57` | 40,831.32 USD | `+3.61%` | `20X Cross` |
| `1839` | `0xe282...df29` | `LONG` | 1,114,250.00 USD | `500.00` | `2309.84` | `2228.00` | `2045.06` | -40,674.21 USD | `-3.65%` | `10X Isolated` |
| `1840` | `0x6936...9417` | `SHORT` | 1,114,250.00 USD | `500.00` | `2315.11` | `2228.00` | `2358.66` | 43,305.21 USD | `+3.89%` | `25X Isolated` |
| `1841` | `0x4044...794c` | `LONG` | 1,114,250.00 USD | `500.00` | `2260.80` | `2228.00` | `0.000000` | -16,150.00 USD | `-1.45%` | `25X Cross` |
| `1842` | `0xb322...d51f` | `SHORT` | 1,114,200.00 USD | `500.00` | `2268.03` | `2228.00` | `3739.78` | 19,816.32 USD | `+1.78%` | `20X Cross` |
| `1843` | `0xa559...ff95` | `LONG` | 1,114,150.00 USD | `500.00` | `2260.68` | `2228.00` | `1057.07` | -16,194.36 USD | `-1.45%` | `20X Cross` |
| `1844` | `0x89b2...9ca6` | `LONG` | 1,114,050.00 USD | `500.00` | `2363.45` | `2228.00` | `1622.40` | -67,677.42 USD | `-6.07%` | `25X Cross` |
| `1848` | `0x7298...7d6c` | `SHORT` | 1,110,125.72 USD | `498.15` | `3426.75` | `2228.00` | `5421.37` | 596,910.11 USD | `+53.77%` | `20X Cross` |
| `1862` | `0x9c68...7783` | `SHORT` | 1,099,237.77 USD | `493.31` | `2273.58` | `2228.00` | `3909.12` | 22,341.48 USD | `+2.03%` | `25X Cross` |
| `1870` | `0x404c...5f03` | `SHORT` | 1,091,290.63 USD | `489.79` | `2671.94` | `2228.00` | `5006.36` | 217,388.93 USD | `+19.92%` | `20X Cross` |
| `1877` | `0x321f...1c84` | `SHORT` | 1,087,493.52 USD | `488.02` | `2370.09` | `2228.00` | `3061.23` | 69,151.08 USD | `+6.36%` | `10X Cross` |
| `1881` | `0x94b6...e5b3` | `SHORT` | 1,083,163.76 USD | `486.05` | `2260.75` | `2228.00` | `2357.74` | 15,678.83 USD | `+1.45%` | `25X Cross` |
| `1935` | `0x82c6...fe42` | `LONG` | 1,030,681.25 USD | `462.50` | `2501.38` | `2228.00` | `2053.40` | -126,209.32 USD | `-12.25%` | `5X Isolated` |
| `1937` | `0x2de3...486d` | `LONG` | 1,030,265.09 USD | `462.33` | `2286.03` | `2228.00` | `1158.92` | -26,647.49 USD | `-2.59%` | `25X Cross` |
| `1945` | `0xe330...77a1` | `SHORT` | 1,027,648.07 USD | `461.20` | `2206.97` | `2228.00` | `6448.53` | -9,790.70 USD | `-0.95%` | `20X Cross` |
| `1956` | `0xd6e1...f256` | `LONG` | 1,022,259.80 USD | `458.64` | `2213.70` | `2228.00` | `915.36` | 6,968.91 USD | `+0.68%` | `25X Cross` |
| `1959` | `0x617e...0f97` | `SHORT` | 1,020,282.74 USD | `457.85` | `2205.60` | `2228.00` | `3347.51` | -10,438.91 USD | `-1.02%` | `10X Cross` |
| `1985` | `0xae55...2236` | `LONG` | 1,003,005.00 USD | `450.00` | `2510.21` | `2228.00` | `0.000000` | -126,592.50 USD | `-12.62%` | `25X Cross` |

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
| `7D` | `Long Liquidation` | `1972.30` | 744,330,000.00 USD | 744,330,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1975.00` | 1,950,000.00 USD | 224,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1975.10` | 744,200,000.00 USD | 744,200,000.00 USD | 0.00 USD | 0.00 USD | 49,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1977.90` | 744,150,000.00 USD | 744,150,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1983.50` | 741,910,000.00 USD | 741,910,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1985.00` | 8,110,000.00 USD | 222,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1986.30` | 741,700,000.00 USD | 741,700,000.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1989.10` | 737,970,000.00 USD | 737,970,000.00 USD | 0.00 USD | 1,780,000.00 USD | 38,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1991.90` | 736,160,000.00 USD | 736,160,000.00 USD | 1,390,000.00 USD | 1,320,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1994.70` | 733,450,000.00 USD | 733,450,000.00 USD | 0.00 USD | 0.00 USD | 808,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1995.00` | 1,720,000.00 USD | 214,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1997.50` | 732,640,000.00 USD | 732,640,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1999.00` | 618,630,000.00 USD | 618,630,000.00 USD | 43,520.00 USD | 104,180.00 USD | 486,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2001.40` | 618,000,000.00 USD | 618,000,000.00 USD | 471,940.00 USD | 381,880.00 USD | 433,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2003.10` | 731,300,000.00 USD | 731,300,000.00 USD | 0.00 USD | 266,430.00 USD | 594,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2003.80` | 616,710,000.00 USD | 616,710,000.00 USD | 390,870.00 USD | 455,960.00 USD | 524,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2005.00` | 12,670,000.00 USD | 212,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2005.90` | 730,440,000.00 USD | 730,440,000.00 USD | 0.00 USD | 475,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2006.20` | 615,340,000.00 USD | 615,340,000.00 USD | 507,510.00 USD | 35,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2008.60` | 614,790,000.00 USD | 614,790,000.00 USD | 0.00 USD | 548,050.00 USD | 126,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2008.70` | 729,960,000.00 USD | 729,960,000.00 USD | 807,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2011.00` | 614,120,000.00 USD | 614,120,000.00 USD | 533,480.00 USD | 478,500.00 USD | 366,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2011.50` | 729,160,000.00 USD | 729,160,000.00 USD | 170,840.00 USD | 92,470.00 USD | 689,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2013.40` | 612,740,000.00 USD | 612,740,000.00 USD | 300,160.00 USD | 270,490.00 USD | 21,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2015.00` | 5,010,000.00 USD | 200,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2015.80` | 612,150,000.00 USD | 612,150,000.00 USD | 358,460.00 USD | 605,010.00 USD | 197,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2017.10` | 728,200,000.00 USD | 728,200,000.00 USD | 0.00 USD | 0.00 USD | 21,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2018.20` | 610,990,000.00 USD | 610,990,000.00 USD | 798,920.00 USD | 885,870.00 USD | 714,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2020.60` | 608,590,000.00 USD | 608,590,000.00 USD | 622,680.00 USD | 1,280,000.00 USD | 673,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2022.70` | 728,180,000.00 USD | 728,180,000.00 USD | 1,070,000.00 USD | 0.00 USD | 934,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2023.00` | 606,010,000.00 USD | 606,010,000.00 USD | 792,850.00 USD | 271,500.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2025.00` | 1,440,000.00 USD | 195,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2025.40` | 603,510,000.00 USD | 603,510,000.00 USD | 414,330.00 USD | 1,100,000.00 USD | 231,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2025.50` | 726,180,000.00 USD | 726,180,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2027.80` | 601,770,000.00 USD | 601,770,000.00 USD | 2,770,000.00 USD | 978,910.00 USD | 312,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2028.30` | 726,000,000.00 USD | 726,000,000.00 USD | 1,100,000.00 USD | 0.00 USD | 35,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2030.20` | 597,710,000.00 USD | 597,710,000.00 USD | 87,180.00 USD | 366,120.00 USD | 957,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2031.10` | 724,860,000.00 USD | 724,860,000.00 USD | 0.00 USD | 3,520,000.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2032.60` | 596,300,000.00 USD | 596,300,000.00 USD | 1,360,000.00 USD | 1,490,000.00 USD | 707,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2033.90` | 720,300,000.00 USD | 720,300,000.00 USD | 0.00 USD | 0.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2035.00` | 592,740,000.00 USD | 592,740,000.00 USD | 1,150,000.00 USD | 19,490.00 USD | 165,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2035.00` | 423,740.00 USD | 193,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2036.70` | 718,940,000.00 USD | 718,940,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2037.40` | 591,400,000.00 USD | 591,400,000.00 USD | 396,700.00 USD | 458,110.00 USD | 378,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2039.50` | 718,610,000.00 USD | 718,610,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2039.80` | 590,170,000.00 USD | 590,170,000.00 USD | 542,670.00 USD | 178,560.00 USD | 24,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2042.20` | 589,420,000.00 USD | 589,420,000.00 USD | 626,840.00 USD | 0.00 USD | 174,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2044.60` | 588,620,000.00 USD | 588,620,000.00 USD | 0.00 USD | 0.00 USD | 26,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2045.00` | 6,640,000.00 USD | 193,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2045.10` | 717,150,000.00 USD | 717,150,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2047.00` | 588,590,000.00 USD | 588,590,000.00 USD | 467,370.00 USD | 0.00 USD | 367,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2049.40` | 587,760,000.00 USD | 587,760,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2050.70` | 716,860,000.00 USD | 716,860,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2053.50` | 716,630,000.00 USD | 716,630,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2054.20` | 586,650,000.00 USD | 586,650,000.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2055.00` | 3,920,000.00 USD | 186,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2056.60` | 586,530,000.00 USD | 586,530,000.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2059.00` | 586,290,000.00 USD | 586,290,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2059.10` | 714,350,000.00 USD | 714,350,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2061.40` | 585,540,000.00 USD | 585,540,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2061.90` | 714,000,000.00 USD | 714,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2063.80` | 585,460,000.00 USD | 585,460,000.00 USD | 563,140.00 USD | 494,150.00 USD | 510,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2064.70` | 708,750,000.00 USD | 708,750,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2065.00` | 15,310,000.00 USD | 182,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2066.20` | 583,890,000.00 USD | 583,890,000.00 USD | 387,410.00 USD | 42,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2067.50` | 706,280,000.00 USD | 706,280,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2068.60` | 583,460,000.00 USD | 583,460,000.00 USD | 57,300.00 USD | 624,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2070.30` | 704,640,000.00 USD | 704,640,000.00 USD | 3,600,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2071.00` | 582,780,000.00 USD | 582,780,000.00 USD | 47,910.00 USD | 534,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2073.10` | 697,080,000.00 USD | 697,080,000.00 USD | 2,870,000.00 USD | 2,180,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2073.40` | 582,190,000.00 USD | 582,190,000.00 USD | 25,660.00 USD | 20,640.00 USD | 420,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 2,710,000.00 USD | 167,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2075.80` | 581,730,000.00 USD | 581,730,000.00 USD | 354,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2075.90` | 690,000,000.00 USD | 690,000,000.00 USD | 3,910,000.00 USD | 4,290,000.00 USD | 4,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2078.20` | 581,370,000.00 USD | 581,370,000.00 USD | 0.00 USD | 25,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2078.70` | 677,490,000.00 USD | 677,490,000.00 USD | 4,160,000.00 USD | 3,730,000.00 USD | 2,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2080.60` | 581,350,000.00 USD | 581,350,000.00 USD | 77,960.00 USD | 29,610.00 USD | 199,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2081.50` | 667,550,000.00 USD | 667,550,000.00 USD | 4,400,000.00 USD | 1,290,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2083.00` | 581,040,000.00 USD | 581,040,000.00 USD | 827,940.00 USD | 4,240.00 USD | 206,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2084.30` | 660,640,000.00 USD | 660,640,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 3,500,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 13,760,000.00 USD | 164,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2085.40` | 580,000,000.00 USD | 580,000,000.00 USD | 528,660.00 USD | 207,610.00 USD | 821,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2087.10` | 653,250,000.00 USD | 653,250,000.00 USD | 2,920,000.00 USD | 2,750,000.00 USD | 3,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2087.80` | 578,450,000.00 USD | 578,450,000.00 USD | 525,540.00 USD | 383,220.00 USD | 304,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2089.90` | 644,560,000.00 USD | 644,560,000.00 USD | 4,130,000.00 USD | 948,120.00 USD | 3,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2090.20` | 577,230,000.00 USD | 577,230,000.00 USD | 745,390.00 USD | 214,870.00 USD | 256,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2092.60` | 576,020,000.00 USD | 576,020,000.00 USD | 510,840.00 USD | 338,080.00 USD | 370,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2092.70` | 636,330,000.00 USD | 636,330,000.00 USD | 4,680,000.00 USD | 737,060.00 USD | 6,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2095.00` | 574,800,000.00 USD | 574,800,000.00 USD | 2,100,000.00 USD | 956,940.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 1,710,000.00 USD | 150,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2095.50` | 624,690,000.00 USD | 624,690,000.00 USD | 2,480,000.00 USD | 2,010,000.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2097.40` | 570,410,000.00 USD | 570,410,000.00 USD | 175,830.00 USD | 381,000.00 USD | 674,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2098.30` | 619,190,000.00 USD | 619,190,000.00 USD | 3,020,000.00 USD | 3,130,000.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2099.80` | 569,180,000.00 USD | 569,180,000.00 USD | 307,340.00 USD | 1,070,000.00 USD | 20,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2101.10` | 611,570,000.00 USD | 611,570,000.00 USD | 631,640.00 USD | 1,240,000.00 USD | 3,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2102.20` | 567,780,000.00 USD | 567,780,000.00 USD | 211,840.00 USD | 371,740.00 USD | 513,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2103.90` | 606,290,000.00 USD | 606,290,000.00 USD | 1,130,000.00 USD | 738,240.00 USD | 2,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2104.60` | 566,680,000.00 USD | 566,680,000.00 USD | 3,570,000.00 USD | 1,160,000.00 USD | 677,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 2,380,000.00 USD | 149,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2106.70` | 602,100,000.00 USD | 602,100,000.00 USD | 1,700,000.00 USD | 834,660.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2107.00` | 561,270,000.00 USD | 561,270,000.00 USD | 677,650.00 USD | 0.00 USD | 502,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2109.40` | 560,090,000.00 USD | 560,090,000.00 USD | 118,210.00 USD | 31,550.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2109.50` | 598,380,000.00 USD | 598,380,000.00 USD | 7,750,000.00 USD | 1,800,000.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2111.80` | 559,940,000.00 USD | 559,940,000.00 USD | 490,860.00 USD | 90,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2112.30` | 587,060,000.00 USD | 587,060,000.00 USD | 3,920,000.00 USD | 1,480,000.00 USD | 3,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2114.20` | 559,360,000.00 USD | 559,360,000.00 USD | 614,540.00 USD | 501,000.00 USD | 249,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 1,330,000.00 USD | 146,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2115.10` | 577,950,000.00 USD | 577,950,000.00 USD | 923,330.00 USD | 3,210,000.00 USD | 1,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2116.60` | 557,990,000.00 USD | 557,990,000.00 USD | 3,030,000.00 USD | 1,180,000.00 USD | 935,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2117.90` | 571,880,000.00 USD | 571,880,000.00 USD | 8,390,000.00 USD | 578,010.00 USD | 2,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2119.00` | 552,840,000.00 USD | 552,840,000.00 USD | 3,990,000.00 USD | 3,070,000.00 USD | 905,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2120.70` | 560,330,000.00 USD | 560,330,000.00 USD | 7,060,000.00 USD | 5,780,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2121.40` | 544,880,000.00 USD | 544,880,000.00 USD | 5,220,000.00 USD | 3,760,000.00 USD | 903,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2123.50` | 545,670,000.00 USD | 545,670,000.00 USD | 7,150,000.00 USD | 7,720,000.00 USD | 1,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2123.80` | 534,990,000.00 USD | 534,990,000.00 USD | 6,610,000.00 USD | 1,520,000.00 USD | 2,310,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 123,770,000.00 USD | 145,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2126.20` | 524,560,000.00 USD | 524,560,000.00 USD | 3,480,000.00 USD | 2,840,000.00 USD | 837,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2126.30` | 529,390,000.00 USD | 529,390,000.00 USD | 2,740,000.00 USD | 4,400,000.00 USD | 4,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2128.60` | 517,390,000.00 USD | 517,390,000.00 USD | 3,180,000.00 USD | 1,860,000.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2129.10` | 517,460,000.00 USD | 517,460,000.00 USD | 4,770,000.00 USD | 1,270,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2131.00` | 510,840,000.00 USD | 510,840,000.00 USD | 350,450.00 USD | 61,560.00 USD | 344,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2131.90` | 510,320,000.00 USD | 510,320,000.00 USD | 2,170,000.00 USD | 1,620,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2133.40` | 510,080,000.00 USD | 510,080,000.00 USD | 294,890.00 USD | 654,710.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2134.70` | 505,170,000.00 USD | 505,170,000.00 USD | 1,630,000.00 USD | 790,240.00 USD | 898,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 2,100,000.00 USD | 21,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2135.80` | 507,610,000.00 USD | 507,610,000.00 USD | 1,820,000.00 USD | 2,590,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2137.50` | 501,860,000.00 USD | 501,860,000.00 USD | 2,120,000.00 USD | 2,390,000.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2138.20` | 501,370,000.00 USD | 501,370,000.00 USD | 752,380.00 USD | 1,010,000.00 USD | 537,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2140.30` | 495,820,000.00 USD | 495,820,000.00 USD | 3,990,000.00 USD | 1,870,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2140.60` | 499,070,000.00 USD | 499,070,000.00 USD | 1,530,000.00 USD | 898,980.00 USD | 317,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2143.00` | 496,320,000.00 USD | 496,320,000.00 USD | 1,080,000.00 USD | 3,170,000.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2143.10` | 489,160,000.00 USD | 489,160,000.00 USD | 2,380,000.00 USD | 618,280.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 1,020,000.00 USD | 19,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2145.40` | 490,900,000.00 USD | 490,900,000.00 USD | 3,170,000.00 USD | 2,110,000.00 USD | 605,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2145.90` | 485,900,000.00 USD | 485,900,000.00 USD | 978,940.00 USD | 1,450,000.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2147.80` | 485,010,000.00 USD | 485,010,000.00 USD | 728,710.00 USD | 1,050,000.00 USD | 79,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2148.70` | 481,740,000.00 USD | 481,740,000.00 USD | 26,270.00 USD | 538,910.00 USD | 399,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2150.20` | 483,150,000.00 USD | 483,150,000.00 USD | 7,510,000.00 USD | 3,090,000.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2151.50` | 480,780,000.00 USD | 480,780,000.00 USD | 11,200,000.00 USD | 363,770.00 USD | 107,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2152.60` | 469,890,000.00 USD | 469,890,000.00 USD | 2,050,000.00 USD | 2,710,000.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2154.30` | 469,110,000.00 USD | 469,110,000.00 USD | 48,150.00 USD | 2,020,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2155.00` | 463,290,000.00 USD | 463,290,000.00 USD | 2,550,000.00 USD | 3,560,000.00 USD | 2,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 2,970,000.00 USD | 18,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2157.10` | 465,460,000.00 USD | 465,460,000.00 USD | 4,270,000.00 USD | 1,330,000.00 USD | 5,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2157.40` | 454,750,000.00 USD | 454,750,000.00 USD | 4,310,000.00 USD | 1,790,000.00 USD | 3,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2159.80` | 444,680,000.00 USD | 444,680,000.00 USD | 3,850,000.00 USD | 4,490,000.00 USD | 2,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2159.90` | 454,810,000.00 USD | 454,810,000.00 USD | 2,980,000.00 USD | 737,260.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2162.20` | 433,420,000.00 USD | 433,420,000.00 USD | 15,610,000.00 USD | 10,080,000.00 USD | 546,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2162.70` | 449,250,000.00 USD | 449,250,000.00 USD | 17,980,000.00 USD | 1,990,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2164.60` | 407,180,000.00 USD | 407,180,000.00 USD | 13,600,000.00 USD | 7,570,000.00 USD | 4,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 6,050,000.00 USD | 15,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2165.50` | 429,270,000.00 USD | 429,270,000.00 USD | 8,990,000.00 USD | 17,170,000.00 USD | 2,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2167.00` | 381,980,000.00 USD | 381,980,000.00 USD | 9,890,000.00 USD | 8,800,000.00 USD | 5,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2168.30` | 400,170,000.00 USD | 400,170,000.00 USD | 12,770,000.00 USD | 16,150,000.00 USD | 3,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2169.40` | 357,780,000.00 USD | 357,780,000.00 USD | 16,830,000.00 USD | 7,640,000.00 USD | 6,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2171.10` | 367,480,000.00 USD | 367,480,000.00 USD | 1,860,000.00 USD | 6,380,000.00 USD | 5,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2171.80` | 327,020,000.00 USD | 327,020,000.00 USD | 19,540,000.00 USD | 9,060,000.00 USD | 5,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2173.90` | 353,680,000.00 USD | 353,680,000.00 USD | 35,100,000.00 USD | 0.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2174.20` | 293,170,000.00 USD | 293,170,000.00 USD | 6,960,000.00 USD | 1,040,000.00 USD | 2,310,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 6,220,000.00 USD | 9,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2176.60` | 282,860,000.00 USD | 282,860,000.00 USD | 1,390,000.00 USD | 569,650.00 USD | 2,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2176.70` | 317,570,000.00 USD | 317,570,000.00 USD | 0.00 USD | 1,460,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2179.00` | 278,520,000.00 USD | 278,520,000.00 USD | 1,670,000.00 USD | 2,280,000.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2179.50` | 313,290,000.00 USD | 313,290,000.00 USD | 2,400,000.00 USD | 133,210.00 USD | 4,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2181.40` | 272,020,000.00 USD | 272,020,000.00 USD | 3,960,000.00 USD | 3,990,000.00 USD | 7,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2182.30` | 306,600,000.00 USD | 306,600,000.00 USD | 1,760,000.00 USD | 2,160,000.00 USD | 2,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2183.80` | 257,050,000.00 USD | 257,050,000.00 USD | 3,630,000.00 USD | 657,360.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2185.00` | 661,930.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2185.10` | 300,030,000.00 USD | 300,030,000.00 USD | 41,350,000.00 USD | 20,450,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2186.20` | 251,500,000.00 USD | 251,500,000.00 USD | 4,150,000.00 USD | 2,860,000.00 USD | 4,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2187.90` | 236,940,000.00 USD | 236,940,000.00 USD | 2,370,000.00 USD | 0.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2188.60` | 239,630,000.00 USD | 239,630,000.00 USD | 3,500,000.00 USD | 4,680,000.00 USD | 9,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2190.70` | 232,970,000.00 USD | 232,970,000.00 USD | 12,430,000.00 USD | 27,960,000.00 USD | 6,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2191.00` | 222,010,000.00 USD | 222,010,000.00 USD | 7,830,000.00 USD | 4,330,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2193.40` | 206,290,000.00 USD | 206,290,000.00 USD | 5,190,000.00 USD | 5,050,000.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2193.50` | 186,150,000.00 USD | 186,150,000.00 USD | 0.00 USD | 7,340,000.00 USD | 8,120,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 2,240,000.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2195.80` | 194,680,000.00 USD | 194,680,000.00 USD | 8,720,000.00 USD | 1,520,000.00 USD | 4,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2196.30` | 170,690,000.00 USD | 170,690,000.00 USD | 383,690.00 USD | 243,760.00 USD | 109,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2198.20` | 179,550,000.00 USD | 179,550,000.00 USD | 488,220.00 USD | 2,990,000.00 USD | 4,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2199.10` | 169,960,000.00 USD | 169,960,000.00 USD | 0.00 USD | 1,460,000.00 USD | 7,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2200.60` | 171,300,000.00 USD | 171,300,000.00 USD | 9,250,000.00 USD | 5,850,000.00 USD | 11,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2201.90` | 161,060,000.00 USD | 161,060,000.00 USD | 9,110,000.00 USD | 266,430.00 USD | 18,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2203.00` | 144,240,000.00 USD | 144,240,000.00 USD | 12,320,000.00 USD | 12,690,000.00 USD | 12,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2204.70` | 133,050,000.00 USD | 133,050,000.00 USD | 5,350,000.00 USD | 4,330,000.00 USD | 4,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 455,190.00 USD | 455,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2205.40` | 106,560,000.00 USD | 106,560,000.00 USD | 8,540,000.00 USD | 1,580,000.00 USD | 2,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2207.50` | 118,940,000.00 USD | 118,940,000.00 USD | 19,630,000.00 USD | 3,390,000.00 USD | 3,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2207.80` | 93,560,000.00 USD | 93,560,000.00 USD | 11,640,000.00 USD | 6,260,000.00 USD | 2,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2210.20` | 73,610,000.00 USD | 73,610,000.00 USD | 4,040,000.00 USD | 5,850,000.00 USD | 6,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2210.30` | 92,280,000.00 USD | 92,280,000.00 USD | 4,740,000.00 USD | 0.00 USD | 11,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2212.60` | 57,430,000.00 USD | 57,430,000.00 USD | 12,700,000.00 USD | 6,410,000.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2213.10` | 76,230,000.00 USD | 76,230,000.00 USD | 1,710,000.00 USD | 1,980,000.00 USD | 8,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2215.00` | 36,380,000.00 USD | 36,380,000.00 USD | 2,300,000.00 USD | 2,930,000.00 USD | 139,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 412.88 USD | 412.88 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2215.90` | 63,690,000.00 USD | 63,690,000.00 USD | 0.00 USD | 0.00 USD | 565,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2217.40` | 31,010,000.00 USD | 31,010,000.00 USD | 748,080.00 USD | 3,550,000.00 USD | 3,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2218.70` | 63,120,000.00 USD | 63,120,000.00 USD | 22,400,000.00 USD | 487,520.00 USD | 218,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2219.80` | 22,760,000.00 USD | 22,760,000.00 USD | 6,340,000.00 USD | 2,000,000.00 USD | 1,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2221.50` | 40,020,000.00 USD | 40,020,000.00 USD | 0.00 USD | 12,220,000.00 USD | 18,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2222.20` | 12,540,000.00 USD | 12,540,000.00 USD | 0.00 USD | 4,290,000.00 USD | 2,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2224.30` | 8,930,000.00 USD | 8,930,000.00 USD | 0.00 USD | 0.00 USD | 911,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2224.60` | 5,690,000.00 USD | 5,690,000.00 USD | 374,450.00 USD | 94,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2225.00` | 778.75 USD | 778.75 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2227.00` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 5,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2227.10` | 8,020,000.00 USD | 8,020,000.00 USD | 557,870.00 USD | 0.00 USD | 7,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2229.40` | 12,290,000.00 USD | 12,290,000.00 USD | 0.00 USD | 12,070,000.00 USD | 224,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2229.90` | 20,990,000.00 USD | 20,990,000.00 USD | 1,910,000.00 USD | 0.00 USD | 19,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2231.80` | 53,120,000.00 USD | 53,120,000.00 USD | 40,420,000.00 USD | 0.00 USD | 411,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2232.70` | 21,950,000.00 USD | 21,950,000.00 USD | 0.00 USD | 0.00 USD | 959,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2235.00` | 2,120.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2235.50` | 47,190,000.00 USD | 47,190,000.00 USD | 3,260,000.00 USD | 21,640,000.00 USD | 350,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2236.60` | 59,920,000.00 USD | 59,920,000.00 USD | 6,800,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2238.30` | 61,230,000.00 USD | 61,230,000.00 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2239.00` | 68,340,000.00 USD | 68,340,000.00 USD | 8,420,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2241.10` | 93,140,000.00 USD | 93,140,000.00 USD | 31,910,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2241.40` | 68,470,000.00 USD | 68,470,000.00 USD | 81,700.00 USD | 0.00 USD | 50,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2243.80` | 69,420,000.00 USD | 69,420,000.00 USD | 381,040.00 USD | 569,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2243.90` | 95,000,000.00 USD | 95,000,000.00 USD | 1,590,000.00 USD | 268,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2246.20` | 83,650,000.00 USD | 83,650,000.00 USD | 5,570,000.00 USD | 4,370,000.00 USD | 4,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2246.70` | 112,030,000.00 USD | 112,030,000.00 USD | 6,720,000.00 USD | 1,300,000.00 USD | 9,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2248.60` | 100,000,000.00 USD | 100,000,000.00 USD | 5,090,000.00 USD | 5,320,000.00 USD | 5,930,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2249.50` | 122,610,000.00 USD | 122,610,000.00 USD | 2,960,000.00 USD | 6,990,000.00 USD | 640,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2251.00` | 107,420,000.00 USD | 107,420,000.00 USD | 6,720,000.00 USD | 630,890.00 USD | 77,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2252.30` | 144,330,000.00 USD | 144,330,000.00 USD | 10,050,000.00 USD | 11,670,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2253.40` | 113,820,000.00 USD | 113,820,000.00 USD | 893,130.00 USD | 3,370,000.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2255.00` | 20,070.00 USD | 22,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2255.10` | 161,500,000.00 USD | 161,500,000.00 USD | 10,050,000.00 USD | 6,600,000.00 USD | 514,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2255.80` | 148,930,000.00 USD | 148,930,000.00 USD | 18,730,000.00 USD | 7,340,000.00 USD | 9,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2257.90` | 201,190,000.00 USD | 201,190,000.00 USD | 20,510,000.00 USD | 12,290,000.00 USD | 6,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2258.20` | 173,740,000.00 USD | 173,740,000.00 USD | 16,130,000.00 USD | 6,840,000.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2260.60` | 195,150,000.00 USD | 195,150,000.00 USD | 9,590,000.00 USD | 9,340,000.00 USD | 2,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2260.70` | 205,520,000.00 USD | 205,520,000.00 USD | 0.00 USD | 0.00 USD | 4,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2263.00` | 226,460,000.00 USD | 226,460,000.00 USD | 14,130,000.00 USD | 10,400,000.00 USD | 6,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2263.50` | 213,910,000.00 USD | 213,910,000.00 USD | 6,720,000.00 USD | 1,460,000.00 USD | 218,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2265.00` | 13,280.00 USD | 36,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2265.40` | 250,860,000.00 USD | 250,860,000.00 USD | 3,490,000.00 USD | 9,180,000.00 USD | 11,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2266.30` | 228,400,000.00 USD | 228,400,000.00 USD | 0.00 USD | 8,160,000.00 USD | 6,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2267.80` | 284,550,000.00 USD | 284,550,000.00 USD | 14,030,000.00 USD | 10,980,000.00 USD | 8,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2269.10` | 257,710,000.00 USD | 257,710,000.00 USD | 11,010,000.00 USD | 133,210.00 USD | 18,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2270.20` | 326,860,000.00 USD | 326,860,000.00 USD | 15,300,000.00 USD | 7,980,000.00 USD | 19,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2271.90` | 286,490,000.00 USD | 286,490,000.00 USD | 18,240,000.00 USD | 3,640,000.00 USD | 6,900,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2272.60` | 352,700,000.00 USD | 352,700,000.00 USD | 15,500,000.00 USD | 4,860,000.00 USD | 5,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2274.70` | 313,020,000.00 USD | 313,020,000.00 USD | 19,630,000.00 USD | 6,900,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2275.00` | 394,530,000.00 USD | 394,530,000.00 USD | 26,690,000.00 USD | 11,580,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2275.00` | 1,610,000.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2277.40` | 434,430,000.00 USD | 434,430,000.00 USD | 10,430,000.00 USD | 17,510,000.00 USD | 11,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2277.50` | 339,270,000.00 USD | 339,270,000.00 USD | 6,890,000.00 USD | 8,890,000.00 USD | 10,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2279.80` | 472,780,000.00 USD | 472,780,000.00 USD | 17,260,000.00 USD | 9,050,000.00 USD | 12,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2280.30` | 383,590,000.00 USD | 383,590,000.00 USD | 854,200.00 USD | 39,830,000.00 USD | 3,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2282.20` | 520,490,000.00 USD | 520,490,000.00 USD | 22,980,000.00 USD | 21,840,000.00 USD | 2,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2283.10` | 475,410,000.00 USD | 475,410,000.00 USD | 5,600,000.00 USD | 72,520,000.00 USD | 13,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2284.60` | 565,750,000.00 USD | 565,750,000.00 USD | 22,570,000.00 USD | 11,280,000.00 USD | 11,410,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2285.00` | 183,890.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2285.90` | 479,110,000.00 USD | 479,110,000.00 USD | 1,010,000.00 USD | 2,590,000.00 USD | 109,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2287.00` | 593,810,000.00 USD | 593,810,000.00 USD | 8,540,000.00 USD | 12,040,000.00 USD | 7,470,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2288.70` | 511,750,000.00 USD | 511,750,000.00 USD | 8,380,000.00 USD | 9,320,000.00 USD | 14,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2289.40` | 619,360,000.00 USD | 619,360,000.00 USD | 9,320,000.00 USD | 13,110,000.00 USD | 3,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2291.50` | 523,630,000.00 USD | 523,630,000.00 USD | 4,310,000.00 USD | 517,070.00 USD | 7,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2291.80` | 653,440,000.00 USD | 653,440,000.00 USD | 19,670,000.00 USD | 5,470,000.00 USD | 8,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2294.20` | 686,500,000.00 USD | 686,500,000.00 USD | 15,170,000.00 USD | 6,680,000.00 USD | 11,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2294.30` | 544,960,000.00 USD | 544,960,000.00 USD | 14,670,000.00 USD | 1,490,000.00 USD | 5,180,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2295.00` | 3,010,000.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2296.60` | 723,200,000.00 USD | 723,200,000.00 USD | 19,950,000.00 USD | 13,010,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2297.10` | 594,710,000.00 USD | 594,710,000.00 USD | 25,900,000.00 USD | 8,070,000.00 USD | 15,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2299.00` | 769,230,000.00 USD | 769,230,000.00 USD | 20,870,000.00 USD | 15,020,000.00 USD | 10,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2299.90` | 637,630,000.00 USD | 637,630,000.00 USD | 16,200,000.00 USD | 20,940,000.00 USD | 5,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2301.40` | 803,120,000.00 USD | 803,120,000.00 USD | 12,570,000.00 USD | 6,810,000.00 USD | 14,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2302.70` | 692,300,000.00 USD | 692,300,000.00 USD | 26,960,000.00 USD | 10,860,000.00 USD | 16,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2303.80` | 832,430,000.00 USD | 832,430,000.00 USD | 14,800,000.00 USD | 11,390,000.00 USD | 3,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2305.00` | 670,610.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2305.50` | 718,310,000.00 USD | 718,310,000.00 USD | 6,340,000.00 USD | 8,820,000.00 USD | 10,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2306.20` | 866,350,000.00 USD | 866,350,000.00 USD | 13,350,000.00 USD | 11,600,000.00 USD | 8,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2308.30` | 720,610,000.00 USD | 720,610,000.00 USD | 1,240,000.00 USD | 930,630.00 USD | 134,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2308.60` | 870,320,000.00 USD | 870,320,000.00 USD | 477,740.00 USD | 3,320,000.00 USD | 182,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2311.00` | 888,180,000.00 USD | 888,180,000.00 USD | 6,170,000.00 USD | 877,090.00 USD | 10,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2311.10` | 751,110,000.00 USD | 751,110,000.00 USD | 11,560,000.00 USD | 2,790,000.00 USD | 16,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2313.40` | 905,700,000.00 USD | 905,700,000.00 USD | 6,490,000.00 USD | 8,560,000.00 USD | 2,470,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2313.90` | 761,930,000.00 USD | 761,930,000.00 USD | 1,100,000.00 USD | 7,460,000.00 USD | 2,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2315.00` | 5,890,000.00 USD | 11,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2315.80` | 939,630,000.00 USD | 939,630,000.00 USD | 10,440,000.00 USD | 15,940,000.00 USD | 7,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2316.70` | 767,630,000.00 USD | 767,630,000.00 USD | 1,020,000.00 USD | 3,640,000.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2318.20` | 954,490,000.00 USD | 954,490,000.00 USD | 5,950,000.00 USD | 6,680,000.00 USD | 2,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2319.50` | 796,900,000.00 USD | 796,900,000.00 USD | 5,530,000.00 USD | 15,850,000.00 USD | 7,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2320.60` | 974,700,000.00 USD | 974,700,000.00 USD | 5,860,000.00 USD | 11,510,000.00 USD | 2,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2322.30` | 802,760,000.00 USD | 802,760,000.00 USD | 2,300,000.00 USD | 3,450,000.00 USD | 108,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2323.00` | 995,800,000.00 USD | 995,800,000.00 USD | 4,360,000.00 USD | 12,060,000.00 USD | 4,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2325.00` | 1,780,000.00 USD | 13,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2325.10` | 825,790,000.00 USD | 825,790,000.00 USD | 10,150,000.00 USD | 2,770,000.00 USD | 10,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2325.40` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 2,050,000.00 USD | 6,790,000.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2327.80` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 494,310.00 USD | 1,240,000.00 USD | 4,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2327.90` | 837,690,000.00 USD | 837,690,000.00 USD | 3,860,000.00 USD | 0.00 USD | 8,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2330.20` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 11,050,000.00 USD | 2,970,000.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2330.70` | 853,910,000.00 USD | 853,910,000.00 USD | 15,800,000.00 USD | 363,770.00 USD | 54,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2332.60` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 2,430,000.00 USD | 2,150,000.00 USD | 5,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2333.50` | 895,000,000.00 USD | 895,000,000.00 USD | 20,270,000.00 USD | 12,860,000.00 USD | 7,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2335.00` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 9,140,000.00 USD | 5,110,000.00 USD | 5,680,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2335.00` | 427,950.00 USD | 13,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2336.30` | 932,260,000.00 USD | 932,260,000.00 USD | 24,310,000.00 USD | 7,570,000.00 USD | 5,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2337.40` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 12,780,000.00 USD | 1,030,000.00 USD | 5,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2339.10` | 958,660,000.00 USD | 958,660,000.00 USD | 14,040,000.00 USD | 0.00 USD | 12,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2339.80` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 10,420,000.00 USD | 6,440,000.00 USD | 12,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2341.90` | 999,090,000.00 USD | 999,090,000.00 USD | 8,610,000.00 USD | 17,820,000.00 USD | 14,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2342.20` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 5,460,000.00 USD | 3,720,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2344.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 6,740,000.00 USD | 8,550,000.00 USD | 6,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2344.70` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 2,480,000.00 USD | 16,920,000.00 USD | 8,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2345.00` | 417,120.00 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2347.00` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 4,320,000.00 USD | 3,650,000.00 USD | 4,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2347.50` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 8,220,000.00 USD | 18,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2349.40` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 16,880,000.00 USD | 6,200,000.00 USD | 5,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2350.30` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 1,630,000.00 USD | 20,110,000.00 USD | 15,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2351.80` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 13,580,000.00 USD | 2,340,000.00 USD | 7,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2353.10` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 2,710,000.00 USD | 35,770,000.00 USD | 4,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2354.20` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 3,750,000.00 USD | 5,600,000.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 1,790,000.00 USD | 15,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2355.90` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 18,560,000.00 USD | 10,720,000.00 USD | 3,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2356.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 4,660,000.00 USD | 1,150,000.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2358.70` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 6,870,000.00 USD | 512,220.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2359.00` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 6,170,000.00 USD | 5,570,000.00 USD | 7,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2361.40` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 7,910,000.00 USD | 8,680,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2361.50` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 3,150,000.00 USD | 3,430,000.00 USD | 374,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2363.80` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 5,570,000.00 USD | 2,830,000.00 USD | 8,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2364.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 3,860,000.00 USD | 373,740.00 USD | 10,920,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 5,520,000.00 USD | 21,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2366.20` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 3,150,000.00 USD | 827,140.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2367.10` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 6,340,000.00 USD | 1,310,000.00 USD | 307,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2368.60` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 5,640,000.00 USD | 4,130,000.00 USD | 3,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2369.90` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 24,940,000.00 USD | 475,460.00 USD | 18,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2371.00` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 14,100,000.00 USD | 6,060,000.00 USD | 4,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2372.70` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 15,600,000.00 USD | 0.00 USD | 39,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2373.40` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 12,300,000.00 USD | 1,570,000.00 USD | 5,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 885,750.00 USD | 22,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2375.50` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 9,700,000.00 USD | 1,050,000.00 USD | 11,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2375.80` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 6,150,000.00 USD | 2,810,000.00 USD | 4,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2378.20` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 1,650,000.00 USD | 1,010,000.00 USD | 3,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2378.30` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 11,180,000.00 USD | 7,020,000.00 USD | 23,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2380.60` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 6,120,000.00 USD | 6,700,000.00 USD | 5,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2381.10` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 4,540,000.00 USD | 2,390,000.00 USD | 16,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2383.00` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 15,730,000.00 USD | 9,480,000.00 USD | 9,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2383.90` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 8,840,000.00 USD | 21,750,000.00 USD | 30,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 726,570.00 USD | 22,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2385.40` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 7,510,000.00 USD | 10,280,000.00 USD | 4,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2386.70` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 17,720,000.00 USD | 32,140,000.00 USD | 42,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2387.80` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 9,900,000.00 USD | 5,870,000.00 USD | 2,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2389.50` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 5,670,000.00 USD | 35,860,000.00 USD | 28,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2390.20` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 4,300,000.00 USD | 3,310,000.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2392.30` | 1,730,000,000.00 USD | 1,730,000,000.00 USD | 26,840,000.00 USD | 45,530,000.00 USD | 39,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2392.60` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 2,380,000.00 USD | 2,660,000.00 USD | 3,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2395.00` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 2,380,000.00 USD | 2,830,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 4,840,000.00 USD | 27,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2395.10` | 1,820,000,000.00 USD | 1,820,000,000.00 USD | 39,180,000.00 USD | 24,870,000.00 USD | 29,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2397.40` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 64,150.00 USD | 3,720,000.00 USD | 3,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2397.90` | 1,920,000,000.00 USD | 1,920,000,000.00 USD | 34,290,000.00 USD | 36,430,000.00 USD | 23,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2399.80` | 1,490,000,000.00 USD | 1,490,000,000.00 USD | 2,150,000.00 USD | 637,690.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2400.70` | 2,010,000,000.00 USD | 2,010,000,000.00 USD | 42,030,000.00 USD | 25,390,000.00 USD | 24,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2402.20` | 1,490,000,000.00 USD | 1,490,000,000.00 USD | 1,140,000.00 USD | 315,710.00 USD | 552,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2403.50` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 51,300,000.00 USD | 24,760,000.00 USD | 30,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2404.60` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 4,740,000.00 USD | 3,420,000.00 USD | 4,440,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 156,110.00 USD | 27,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2406.30` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 29,700,000.00 USD | 33,710,000.00 USD | 14,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2407.00` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 8,030,000.00 USD | 3,500,000.00 USD | 2,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2409.10` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 25,090,000.00 USD | 21,480,000.00 USD | 27,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2409.40` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 3,280,000.00 USD | 3,650,000.00 USD | 3,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2411.80` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 6,680,000.00 USD | 3,520,000.00 USD | 2,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2411.90` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 15,970,000.00 USD | 21,640,000.00 USD | 13,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2414.20` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 1,120,000.00 USD | 1,530,000.00 USD | 28,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2414.70` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 22,250,000.00 USD | 19,630,000.00 USD | 21,720,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 143,210.00 USD | 28,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2416.60` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 2,830,000.00 USD | 1,520,000.00 USD | 3,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2417.50` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 22,310,000.00 USD | 8,700,000.00 USD | 21,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2419.00` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 4,830,000.00 USD | 1,420,000.00 USD | 2,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2420.30` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 29,980,000.00 USD | 18,780,000.00 USD | 9,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2421.40` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 3,950,000.00 USD | 4,860,000.00 USD | 5,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2423.10` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 17,920,000.00 USD | 17,260,000.00 USD | 21,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2423.80` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 440,460.00 USD | 1,280,000.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 243,520.00 USD | 28,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2425.90` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 12,980,000.00 USD | 15,310,000.00 USD | 17,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2426.20` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 2,090,000.00 USD | 1,100,000.00 USD | 40,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2428.60` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 670,680.00 USD | 885,270.00 USD | 1,470,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2428.70` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 12,800,000.00 USD | 7,090,000.00 USD | 8,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2431.00` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 3,120,000.00 USD | 2,130,000.00 USD | 677,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2431.50` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 9,420,000.00 USD | 12,660,000.00 USD | 8,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2433.40` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 1,770,000.00 USD | 1,680,000.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2434.30` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 13,090,000.00 USD | 3,830,000.00 USD | 3,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 187,830.00 USD | 28,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2435.80` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 2,490,000.00 USD | 1,050,000.00 USD | 161,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2437.10` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 7,130,000.00 USD | 7,440,000.00 USD | 6,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2438.20` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 476,020.00 USD | 153,260.00 USD | 15,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2439.90` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 12,730,000.00 USD | 4,970,000.00 USD | 3,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2440.60` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 1,230,000.00 USD | 1,130,000.00 USD | 858,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2442.70` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 5,050,000.00 USD | 5,320,000.00 USD | 7,900,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2443.00` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 1,040,000.00 USD | 42,810.00 USD | 747,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 135,670.00 USD | 28,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2445.40` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 13,780.00 USD | 703,990.00 USD | 755,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2445.50` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 9,990,000.00 USD | 7,470,000.00 USD | 10,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2447.80` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 1,210,000.00 USD | 888,690.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2448.30` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 10,750,000.00 USD | 3,770,000.00 USD | 15,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2450.20` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 486,110.00 USD | 69,580.00 USD | 26,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2451.10` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 8,450,000.00 USD | 7,240,000.00 USD | 7,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2452.60` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 3,200,000.00 USD | 1,840,000.00 USD | 2,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2453.90` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 4,220,000.00 USD | 2,980,000.00 USD | 3,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2455.00` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 2,270,000.00 USD | 1,990,000.00 USD | 905,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 5,180,000.00 USD | 33,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2456.70` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 8,340,000.00 USD | 7,380,000.00 USD | 7,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2457.40` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 1,720,000.00 USD | 1,920,000.00 USD | 845,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2459.50` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 3,220,000.00 USD | 4,870,000.00 USD | 6,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2459.80` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 1,240,000.00 USD | 1,370,000.00 USD | 366,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2462.10` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 0.00 USD | 551,660.00 USD | 829,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2462.30` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 6,600,000.00 USD | 5,990,000.00 USD | 5,150,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 67,480,000.00 USD | 101,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2465.10` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 4,900,000.00 USD | 3,130,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2467.90` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 2,900,000.00 USD | 1,870,000.00 USD | 23,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2470.70` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 3,960,000.00 USD | 2,050,000.00 USD | 522,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2473.50` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 5,300,000.00 USD | 2,920,000.00 USD | 3,180,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 197,560.00 USD | 101,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2476.30` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 2,070,000.00 USD | 1,710,000.00 USD | 872,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2479.10` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 3,070,000.00 USD | 4,130,000.00 USD | 540,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2481.90` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 601,420.00 USD | 3,680,000.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2484.70` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 52,650.00 USD | 101,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2487.50` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 275,450.00 USD | 211,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2490.30` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 338,890.00 USD | 286,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2491.80` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 2,580,000.00 USD | 733,870.00 USD | 445,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 2,220,000.00 USD | 103,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `7D` | `1972.30` | 744,330,000.00 USD | 0.00 USD | 744,330,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD |
| `7D` | `1975.10` | 744,200,000.00 USD | 0.00 USD | 744,200,000.00 USD | 0.00 USD | 0.00 USD | 49,530.00 USD |
| `7D` | `1977.90` | 744,150,000.00 USD | 0.00 USD | 744,150,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1983.50` | 741,910,000.00 USD | 0.00 USD | 741,910,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD |
| `7D` | `1986.30` | 741,700,000.00 USD | 0.00 USD | 741,700,000.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1989.10` | 737,970,000.00 USD | 0.00 USD | 737,970,000.00 USD | 0.00 USD | 1,780,000.00 USD | 38,060.00 USD |
| `7D` | `1991.90` | 736,160,000.00 USD | 0.00 USD | 736,160,000.00 USD | 1,390,000.00 USD | 1,320,000.00 USD | 0.00 USD |
| `7D` | `1994.70` | 733,450,000.00 USD | 0.00 USD | 733,450,000.00 USD | 0.00 USD | 0.00 USD | 808,380.00 USD |
| `7D` | `1997.50` | 732,640,000.00 USD | 0.00 USD | 732,640,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1999.00` | 618,630,000.00 USD | 0.00 USD | 618,630,000.00 USD | 43,520.00 USD | 104,180.00 USD | 486,830.00 USD |
| `1D` | `2001.40` | 618,000,000.00 USD | 0.00 USD | 618,000,000.00 USD | 471,940.00 USD | 381,880.00 USD | 433,510.00 USD |
| `7D` | `2003.10` | 731,300,000.00 USD | 0.00 USD | 731,300,000.00 USD | 0.00 USD | 266,430.00 USD | 594,510.00 USD |
| `1D` | `2003.80` | 616,710,000.00 USD | 0.00 USD | 616,710,000.00 USD | 390,870.00 USD | 455,960.00 USD | 524,290.00 USD |
| `7D` | `2005.90` | 730,440,000.00 USD | 0.00 USD | 730,440,000.00 USD | 0.00 USD | 475,660.00 USD | 0.00 USD |
| `1D` | `2006.20` | 615,340,000.00 USD | 0.00 USD | 615,340,000.00 USD | 507,510.00 USD | 35,460.00 USD | 0.00 USD |
| `1D` | `2008.60` | 614,790,000.00 USD | 0.00 USD | 614,790,000.00 USD | 0.00 USD | 548,050.00 USD | 126,940.00 USD |
| `7D` | `2008.70` | 729,960,000.00 USD | 0.00 USD | 729,960,000.00 USD | 807,770.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2011.00` | 614,120,000.00 USD | 0.00 USD | 614,120,000.00 USD | 533,480.00 USD | 478,500.00 USD | 366,100.00 USD |
| `7D` | `2011.50` | 729,160,000.00 USD | 0.00 USD | 729,160,000.00 USD | 170,840.00 USD | 92,470.00 USD | 689,450.00 USD |
| `1D` | `2013.40` | 612,740,000.00 USD | 0.00 USD | 612,740,000.00 USD | 300,160.00 USD | 270,490.00 USD | 21,620.00 USD |
| `1D` | `2015.80` | 612,150,000.00 USD | 0.00 USD | 612,150,000.00 USD | 358,460.00 USD | 605,010.00 USD | 197,000.00 USD |
| `7D` | `2017.10` | 728,200,000.00 USD | 0.00 USD | 728,200,000.00 USD | 0.00 USD | 0.00 USD | 21,830.00 USD |
| `1D` | `2018.20` | 610,990,000.00 USD | 0.00 USD | 610,990,000.00 USD | 798,920.00 USD | 885,870.00 USD | 714,280.00 USD |
| `1D` | `2020.60` | 608,590,000.00 USD | 0.00 USD | 608,590,000.00 USD | 622,680.00 USD | 1,280,000.00 USD | 673,150.00 USD |
| `7D` | `2022.70` | 728,180,000.00 USD | 0.00 USD | 728,180,000.00 USD | 1,070,000.00 USD | 0.00 USD | 934,340.00 USD |
| `1D` | `2023.00` | 606,010,000.00 USD | 0.00 USD | 606,010,000.00 USD | 792,850.00 USD | 271,500.00 USD | 1,430,000.00 USD |
| `1D` | `2025.40` | 603,510,000.00 USD | 0.00 USD | 603,510,000.00 USD | 414,330.00 USD | 1,100,000.00 USD | 231,680.00 USD |
| `7D` | `2025.50` | 726,180,000.00 USD | 0.00 USD | 726,180,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD |
| `1D` | `2027.80` | 601,770,000.00 USD | 0.00 USD | 601,770,000.00 USD | 2,770,000.00 USD | 978,910.00 USD | 312,840.00 USD |
| `7D` | `2028.30` | 726,000,000.00 USD | 0.00 USD | 726,000,000.00 USD | 1,100,000.00 USD | 0.00 USD | 35,180.00 USD |
| `1D` | `2030.20` | 597,710,000.00 USD | 0.00 USD | 597,710,000.00 USD | 87,180.00 USD | 366,120.00 USD | 957,140.00 USD |
| `7D` | `2031.10` | 724,860,000.00 USD | 0.00 USD | 724,860,000.00 USD | 0.00 USD | 3,520,000.00 USD | 1,050,000.00 USD |
| `1D` | `2032.60` | 596,300,000.00 USD | 0.00 USD | 596,300,000.00 USD | 1,360,000.00 USD | 1,490,000.00 USD | 707,170.00 USD |
| `7D` | `2033.90` | 720,300,000.00 USD | 0.00 USD | 720,300,000.00 USD | 0.00 USD | 0.00 USD | 1,350,000.00 USD |
| `1D` | `2035.00` | 592,740,000.00 USD | 0.00 USD | 592,740,000.00 USD | 1,150,000.00 USD | 19,490.00 USD | 165,760.00 USD |
| `7D` | `2036.70` | 718,940,000.00 USD | 0.00 USD | 718,940,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD |
| `1D` | `2037.40` | 591,400,000.00 USD | 0.00 USD | 591,400,000.00 USD | 396,700.00 USD | 458,110.00 USD | 378,700.00 USD |
| `7D` | `2039.50` | 718,610,000.00 USD | 0.00 USD | 718,610,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2039.80` | 590,170,000.00 USD | 0.00 USD | 590,170,000.00 USD | 542,670.00 USD | 178,560.00 USD | 24,030.00 USD |
| `1D` | `2042.20` | 589,420,000.00 USD | 0.00 USD | 589,420,000.00 USD | 626,840.00 USD | 0.00 USD | 174,290.00 USD |
| `1D` | `2044.60` | 588,620,000.00 USD | 0.00 USD | 588,620,000.00 USD | 0.00 USD | 0.00 USD | 26,280.00 USD |
| `7D` | `2045.10` | 717,150,000.00 USD | 0.00 USD | 717,150,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD |
| `1D` | `2047.00` | 588,590,000.00 USD | 0.00 USD | 588,590,000.00 USD | 467,370.00 USD | 0.00 USD | 367,650.00 USD |
| `1D` | `2049.40` | 587,760,000.00 USD | 0.00 USD | 587,760,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD |
| `7D` | `2050.70` | 716,860,000.00 USD | 0.00 USD | 716,860,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2053.50` | 716,630,000.00 USD | 0.00 USD | 716,630,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD |
| `1D` | `2054.20` | 586,650,000.00 USD | 0.00 USD | 586,650,000.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD |
| `1D` | `2056.60` | 586,530,000.00 USD | 0.00 USD | 586,530,000.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2059.00` | 586,290,000.00 USD | 0.00 USD | 586,290,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `7D` | `2059.10` | 714,350,000.00 USD | 0.00 USD | 714,350,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD |
| `1D` | `2061.40` | 585,540,000.00 USD | 0.00 USD | 585,540,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD |
| `7D` | `2061.90` | 714,000,000.00 USD | 0.00 USD | 714,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD |
| `1D` | `2063.80` | 585,460,000.00 USD | 0.00 USD | 585,460,000.00 USD | 563,140.00 USD | 494,150.00 USD | 510,200.00 USD |
| `7D` | `2064.70` | 708,750,000.00 USD | 0.00 USD | 708,750,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD |
| `1D` | `2066.20` | 583,890,000.00 USD | 0.00 USD | 583,890,000.00 USD | 387,410.00 USD | 42,880.00 USD | 0.00 USD |
| `7D` | `2067.50` | 706,280,000.00 USD | 0.00 USD | 706,280,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD |
| `1D` | `2068.60` | 583,460,000.00 USD | 0.00 USD | 583,460,000.00 USD | 57,300.00 USD | 624,040.00 USD | 0.00 USD |
| `7D` | `2070.30` | 704,640,000.00 USD | 0.00 USD | 704,640,000.00 USD | 3,600,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD |
| `1D` | `2071.00` | 582,780,000.00 USD | 0.00 USD | 582,780,000.00 USD | 47,910.00 USD | 534,600.00 USD | 0.00 USD |
| `7D` | `2073.10` | 697,080,000.00 USD | 0.00 USD | 697,080,000.00 USD | 2,870,000.00 USD | 2,180,000.00 USD | 2,030,000.00 USD |
| `1D` | `2073.40` | 582,190,000.00 USD | 0.00 USD | 582,190,000.00 USD | 25,660.00 USD | 20,640.00 USD | 420,170.00 USD |
| `1D` | `2075.80` | 581,730,000.00 USD | 0.00 USD | 581,730,000.00 USD | 354,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2075.90` | 690,000,000.00 USD | 0.00 USD | 690,000,000.00 USD | 3,910,000.00 USD | 4,290,000.00 USD | 4,300,000.00 USD |
| `1D` | `2078.20` | 581,370,000.00 USD | 0.00 USD | 581,370,000.00 USD | 0.00 USD | 25,190.00 USD | 0.00 USD |
| `7D` | `2078.70` | 677,490,000.00 USD | 0.00 USD | 677,490,000.00 USD | 4,160,000.00 USD | 3,730,000.00 USD | 2,060,000.00 USD |
| `1D` | `2080.60` | 581,350,000.00 USD | 0.00 USD | 581,350,000.00 USD | 77,960.00 USD | 29,610.00 USD | 199,420.00 USD |
| `7D` | `2081.50` | 667,550,000.00 USD | 0.00 USD | 667,550,000.00 USD | 4,400,000.00 USD | 1,290,000.00 USD | 1,220,000.00 USD |
| `1D` | `2083.00` | 581,040,000.00 USD | 0.00 USD | 581,040,000.00 USD | 827,940.00 USD | 4,240.00 USD | 206,010.00 USD |
| `7D` | `2084.30` | 660,640,000.00 USD | 0.00 USD | 660,640,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 3,500,000.00 USD |
| `1D` | `2085.40` | 580,000,000.00 USD | 0.00 USD | 580,000,000.00 USD | 528,660.00 USD | 207,610.00 USD | 821,110.00 USD |
| `7D` | `2087.10` | 653,250,000.00 USD | 0.00 USD | 653,250,000.00 USD | 2,920,000.00 USD | 2,750,000.00 USD | 3,020,000.00 USD |
| `1D` | `2087.80` | 578,450,000.00 USD | 0.00 USD | 578,450,000.00 USD | 525,540.00 USD | 383,220.00 USD | 304,860.00 USD |
| `7D` | `2089.90` | 644,560,000.00 USD | 0.00 USD | 644,560,000.00 USD | 4,130,000.00 USD | 948,120.00 USD | 3,160,000.00 USD |
| `1D` | `2090.20` | 577,230,000.00 USD | 0.00 USD | 577,230,000.00 USD | 745,390.00 USD | 214,870.00 USD | 256,340.00 USD |
| `1D` | `2092.60` | 576,020,000.00 USD | 0.00 USD | 576,020,000.00 USD | 510,840.00 USD | 338,080.00 USD | 370,060.00 USD |
| `7D` | `2092.70` | 636,330,000.00 USD | 0.00 USD | 636,330,000.00 USD | 4,680,000.00 USD | 737,060.00 USD | 6,220,000.00 USD |
| `1D` | `2095.00` | 574,800,000.00 USD | 0.00 USD | 574,800,000.00 USD | 2,100,000.00 USD | 956,940.00 USD | 1,330,000.00 USD |
| `7D` | `2095.50` | 624,690,000.00 USD | 0.00 USD | 624,690,000.00 USD | 2,480,000.00 USD | 2,010,000.00 USD | 1,020,000.00 USD |
| `1D` | `2097.40` | 570,410,000.00 USD | 0.00 USD | 570,410,000.00 USD | 175,830.00 USD | 381,000.00 USD | 674,450.00 USD |
| `7D` | `2098.30` | 619,190,000.00 USD | 0.00 USD | 619,190,000.00 USD | 3,020,000.00 USD | 3,130,000.00 USD | 1,480,000.00 USD |
| `1D` | `2099.80` | 569,180,000.00 USD | 0.00 USD | 569,180,000.00 USD | 307,340.00 USD | 1,070,000.00 USD | 20,670.00 USD |
| `7D` | `2101.10` | 611,570,000.00 USD | 0.00 USD | 611,570,000.00 USD | 631,640.00 USD | 1,240,000.00 USD | 3,400,000.00 USD |
| `1D` | `2102.20` | 567,780,000.00 USD | 0.00 USD | 567,780,000.00 USD | 211,840.00 USD | 371,740.00 USD | 513,570.00 USD |
| `7D` | `2103.90` | 606,290,000.00 USD | 0.00 USD | 606,290,000.00 USD | 1,130,000.00 USD | 738,240.00 USD | 2,320,000.00 USD |
| `1D` | `2104.60` | 566,680,000.00 USD | 0.00 USD | 566,680,000.00 USD | 3,570,000.00 USD | 1,160,000.00 USD | 677,380.00 USD |
| `7D` | `2106.70` | 602,100,000.00 USD | 0.00 USD | 602,100,000.00 USD | 1,700,000.00 USD | 834,660.00 USD | 1,180,000.00 USD |
| `1D` | `2107.00` | 561,270,000.00 USD | 0.00 USD | 561,270,000.00 USD | 677,650.00 USD | 0.00 USD | 502,840.00 USD |
| `1D` | `2109.40` | 560,090,000.00 USD | 0.00 USD | 560,090,000.00 USD | 118,210.00 USD | 31,550.00 USD | 6,190.00 USD |
| `7D` | `2109.50` | 598,380,000.00 USD | 0.00 USD | 598,380,000.00 USD | 7,750,000.00 USD | 1,800,000.00 USD | 1,770,000.00 USD |
| `1D` | `2111.80` | 559,940,000.00 USD | 0.00 USD | 559,940,000.00 USD | 490,860.00 USD | 90,560.00 USD | 0.00 USD |
| `7D` | `2112.30` | 587,060,000.00 USD | 0.00 USD | 587,060,000.00 USD | 3,920,000.00 USD | 1,480,000.00 USD | 3,710,000.00 USD |
| `1D` | `2114.20` | 559,360,000.00 USD | 0.00 USD | 559,360,000.00 USD | 614,540.00 USD | 501,000.00 USD | 249,040.00 USD |
| `7D` | `2115.10` | 577,950,000.00 USD | 0.00 USD | 577,950,000.00 USD | 923,330.00 USD | 3,210,000.00 USD | 1,930,000.00 USD |
| `1D` | `2116.60` | 557,990,000.00 USD | 0.00 USD | 557,990,000.00 USD | 3,030,000.00 USD | 1,180,000.00 USD | 935,080.00 USD |
| `7D` | `2117.90` | 571,880,000.00 USD | 0.00 USD | 571,880,000.00 USD | 8,390,000.00 USD | 578,010.00 USD | 2,580,000.00 USD |
| `1D` | `2119.00` | 552,840,000.00 USD | 0.00 USD | 552,840,000.00 USD | 3,990,000.00 USD | 3,070,000.00 USD | 905,640.00 USD |
| `7D` | `2120.70` | 560,330,000.00 USD | 0.00 USD | 560,330,000.00 USD | 7,060,000.00 USD | 5,780,000.00 USD | 1,820,000.00 USD |
| `1D` | `2121.40` | 544,880,000.00 USD | 0.00 USD | 544,880,000.00 USD | 5,220,000.00 USD | 3,760,000.00 USD | 903,010.00 USD |
| `7D` | `2123.50` | 545,670,000.00 USD | 0.00 USD | 545,670,000.00 USD | 7,150,000.00 USD | 7,720,000.00 USD | 1,410,000.00 USD |
| `1D` | `2123.80` | 534,990,000.00 USD | 0.00 USD | 534,990,000.00 USD | 6,610,000.00 USD | 1,520,000.00 USD | 2,310,000.00 USD |
| `1D` | `2126.20` | 524,560,000.00 USD | 0.00 USD | 524,560,000.00 USD | 3,480,000.00 USD | 2,840,000.00 USD | 837,670.00 USD |
| `7D` | `2126.30` | 529,390,000.00 USD | 0.00 USD | 529,390,000.00 USD | 2,740,000.00 USD | 4,400,000.00 USD | 4,790,000.00 USD |
| `1D` | `2128.60` | 517,390,000.00 USD | 0.00 USD | 517,390,000.00 USD | 3,180,000.00 USD | 1,860,000.00 USD | 1,510,000.00 USD |
| `7D` | `2129.10` | 517,460,000.00 USD | 0.00 USD | 517,460,000.00 USD | 4,770,000.00 USD | 1,270,000.00 USD | 1,100,000.00 USD |
| `1D` | `2131.00` | 510,840,000.00 USD | 0.00 USD | 510,840,000.00 USD | 350,450.00 USD | 61,560.00 USD | 344,350.00 USD |
| `7D` | `2131.90` | 510,320,000.00 USD | 0.00 USD | 510,320,000.00 USD | 2,170,000.00 USD | 1,620,000.00 USD | 1,360,000.00 USD |
| `1D` | `2133.40` | 510,080,000.00 USD | 0.00 USD | 510,080,000.00 USD | 294,890.00 USD | 654,710.00 USD | 1,530,000.00 USD |
| `7D` | `2134.70` | 505,170,000.00 USD | 0.00 USD | 505,170,000.00 USD | 1,630,000.00 USD | 790,240.00 USD | 898,290.00 USD |
| `1D` | `2135.80` | 507,610,000.00 USD | 0.00 USD | 507,610,000.00 USD | 1,820,000.00 USD | 2,590,000.00 USD | 1,820,000.00 USD |
| `7D` | `2137.50` | 501,860,000.00 USD | 0.00 USD | 501,860,000.00 USD | 2,120,000.00 USD | 2,390,000.00 USD | 1,530,000.00 USD |
| `1D` | `2138.20` | 501,370,000.00 USD | 0.00 USD | 501,370,000.00 USD | 752,380.00 USD | 1,010,000.00 USD | 537,470.00 USD |
| `7D` | `2140.30` | 495,820,000.00 USD | 0.00 USD | 495,820,000.00 USD | 3,990,000.00 USD | 1,870,000.00 USD | 801,910.00 USD |
| `1D` | `2140.60` | 499,070,000.00 USD | 0.00 USD | 499,070,000.00 USD | 1,530,000.00 USD | 898,980.00 USD | 317,350.00 USD |
| `1D` | `2143.00` | 496,320,000.00 USD | 0.00 USD | 496,320,000.00 USD | 1,080,000.00 USD | 3,170,000.00 USD | 1,160,000.00 USD |
| `7D` | `2143.10` | 489,160,000.00 USD | 0.00 USD | 489,160,000.00 USD | 2,380,000.00 USD | 618,280.00 USD | 268,500.00 USD |
| `1D` | `2145.40` | 490,900,000.00 USD | 0.00 USD | 490,900,000.00 USD | 3,170,000.00 USD | 2,110,000.00 USD | 605,300.00 USD |
| `7D` | `2145.90` | 485,900,000.00 USD | 0.00 USD | 485,900,000.00 USD | 978,940.00 USD | 1,450,000.00 USD | 1,720,000.00 USD |
| `1D` | `2147.80` | 485,010,000.00 USD | 0.00 USD | 485,010,000.00 USD | 728,710.00 USD | 1,050,000.00 USD | 79,080.00 USD |
| `7D` | `2148.70` | 481,740,000.00 USD | 0.00 USD | 481,740,000.00 USD | 26,270.00 USD | 538,910.00 USD | 399,680.00 USD |
| `1D` | `2150.20` | 483,150,000.00 USD | 0.00 USD | 483,150,000.00 USD | 7,510,000.00 USD | 3,090,000.00 USD | 2,660,000.00 USD |
| `7D` | `2151.50` | 480,780,000.00 USD | 0.00 USD | 480,780,000.00 USD | 11,200,000.00 USD | 363,770.00 USD | 107,200.00 USD |
| `1D` | `2152.60` | 469,890,000.00 USD | 0.00 USD | 469,890,000.00 USD | 2,050,000.00 USD | 2,710,000.00 USD | 1,830,000.00 USD |
| `7D` | `2154.30` | 469,110,000.00 USD | 0.00 USD | 469,110,000.00 USD | 48,150.00 USD | 2,020,000.00 USD | 1,580,000.00 USD |
| `1D` | `2155.00` | 463,290,000.00 USD | 0.00 USD | 463,290,000.00 USD | 2,550,000.00 USD | 3,560,000.00 USD | 2,430,000.00 USD |
| `7D` | `2157.10` | 465,460,000.00 USD | 0.00 USD | 465,460,000.00 USD | 4,270,000.00 USD | 1,330,000.00 USD | 5,050,000.00 USD |
| `1D` | `2157.40` | 454,750,000.00 USD | 0.00 USD | 454,750,000.00 USD | 4,310,000.00 USD | 1,790,000.00 USD | 3,970,000.00 USD |
| `1D` | `2159.80` | 444,680,000.00 USD | 0.00 USD | 444,680,000.00 USD | 3,850,000.00 USD | 4,490,000.00 USD | 2,920,000.00 USD |
| `7D` | `2159.90` | 454,810,000.00 USD | 0.00 USD | 454,810,000.00 USD | 2,980,000.00 USD | 737,260.00 USD | 1,830,000.00 USD |
| `1D` | `2162.20` | 433,420,000.00 USD | 0.00 USD | 433,420,000.00 USD | 15,610,000.00 USD | 10,080,000.00 USD | 546,650.00 USD |
| `7D` | `2162.70` | 449,250,000.00 USD | 0.00 USD | 449,250,000.00 USD | 17,980,000.00 USD | 1,990,000.00 USD | 0.00 USD |
| `1D` | `2164.60` | 407,180,000.00 USD | 0.00 USD | 407,180,000.00 USD | 13,600,000.00 USD | 7,570,000.00 USD | 4,030,000.00 USD |
| `7D` | `2165.50` | 429,270,000.00 USD | 0.00 USD | 429,270,000.00 USD | 8,990,000.00 USD | 17,170,000.00 USD | 2,950,000.00 USD |
| `1D` | `2167.00` | 381,980,000.00 USD | 0.00 USD | 381,980,000.00 USD | 9,890,000.00 USD | 8,800,000.00 USD | 5,510,000.00 USD |
| `7D` | `2168.30` | 400,170,000.00 USD | 0.00 USD | 400,170,000.00 USD | 12,770,000.00 USD | 16,150,000.00 USD | 3,760,000.00 USD |
| `1D` | `2169.40` | 357,780,000.00 USD | 0.00 USD | 357,780,000.00 USD | 16,830,000.00 USD | 7,640,000.00 USD | 6,290,000.00 USD |
| `7D` | `2171.10` | 367,480,000.00 USD | 0.00 USD | 367,480,000.00 USD | 1,860,000.00 USD | 6,380,000.00 USD | 5,570,000.00 USD |
| `1D` | `2171.80` | 327,020,000.00 USD | 0.00 USD | 327,020,000.00 USD | 19,540,000.00 USD | 9,060,000.00 USD | 5,250,000.00 USD |
| `7D` | `2173.90` | 353,680,000.00 USD | 0.00 USD | 353,680,000.00 USD | 35,100,000.00 USD | 0.00 USD | 1,010,000.00 USD |
| `1D` | `2174.20` | 293,170,000.00 USD | 0.00 USD | 293,170,000.00 USD | 6,960,000.00 USD | 1,040,000.00 USD | 2,310,000.00 USD |
| `1D` | `2176.60` | 282,860,000.00 USD | 0.00 USD | 282,860,000.00 USD | 1,390,000.00 USD | 569,650.00 USD | 2,390,000.00 USD |
| `7D` | `2176.70` | 317,570,000.00 USD | 0.00 USD | 317,570,000.00 USD | 0.00 USD | 1,460,000.00 USD | 2,820,000.00 USD |
| `1D` | `2179.00` | 278,520,000.00 USD | 0.00 USD | 278,520,000.00 USD | 1,670,000.00 USD | 2,280,000.00 USD | 2,550,000.00 USD |
| `7D` | `2179.50` | 313,290,000.00 USD | 0.00 USD | 313,290,000.00 USD | 2,400,000.00 USD | 133,210.00 USD | 4,150,000.00 USD |
| `1D` | `2181.40` | 272,020,000.00 USD | 0.00 USD | 272,020,000.00 USD | 3,960,000.00 USD | 3,990,000.00 USD | 7,020,000.00 USD |
| `7D` | `2182.30` | 306,600,000.00 USD | 0.00 USD | 306,600,000.00 USD | 1,760,000.00 USD | 2,160,000.00 USD | 2,650,000.00 USD |
| `1D` | `2183.80` | 257,050,000.00 USD | 0.00 USD | 257,050,000.00 USD | 3,630,000.00 USD | 657,360.00 USD | 1,260,000.00 USD |
| `7D` | `2185.10` | 300,030,000.00 USD | 0.00 USD | 300,030,000.00 USD | 41,350,000.00 USD | 20,450,000.00 USD | 1,290,000.00 USD |
| `1D` | `2186.20` | 251,500,000.00 USD | 0.00 USD | 251,500,000.00 USD | 4,150,000.00 USD | 2,860,000.00 USD | 4,860,000.00 USD |
| `7D` | `2187.90` | 236,940,000.00 USD | 0.00 USD | 236,940,000.00 USD | 2,370,000.00 USD | 0.00 USD | 1,600,000.00 USD |
| `1D` | `2188.60` | 239,630,000.00 USD | 0.00 USD | 239,630,000.00 USD | 3,500,000.00 USD | 4,680,000.00 USD | 9,450,000.00 USD |
| `7D` | `2190.70` | 232,970,000.00 USD | 0.00 USD | 232,970,000.00 USD | 12,430,000.00 USD | 27,960,000.00 USD | 6,420,000.00 USD |
| `1D` | `2191.00` | 222,010,000.00 USD | 0.00 USD | 222,010,000.00 USD | 7,830,000.00 USD | 4,330,000.00 USD | 3,550,000.00 USD |
| `1D` | `2193.40` | 206,290,000.00 USD | 0.00 USD | 206,290,000.00 USD | 5,190,000.00 USD | 5,050,000.00 USD | 1,370,000.00 USD |
| `7D` | `2193.50` | 186,150,000.00 USD | 0.00 USD | 186,150,000.00 USD | 0.00 USD | 7,340,000.00 USD | 8,120,000.00 USD |
| `1D` | `2195.80` | 194,680,000.00 USD | 0.00 USD | 194,680,000.00 USD | 8,720,000.00 USD | 1,520,000.00 USD | 4,890,000.00 USD |
| `7D` | `2196.30` | 170,690,000.00 USD | 0.00 USD | 170,690,000.00 USD | 383,690.00 USD | 243,760.00 USD | 109,160.00 USD |
| `1D` | `2198.20` | 179,550,000.00 USD | 0.00 USD | 179,550,000.00 USD | 488,220.00 USD | 2,990,000.00 USD | 4,770,000.00 USD |
| `7D` | `2199.10` | 169,960,000.00 USD | 0.00 USD | 169,960,000.00 USD | 0.00 USD | 1,460,000.00 USD | 7,440,000.00 USD |
| `1D` | `2200.60` | 171,300,000.00 USD | 0.00 USD | 171,300,000.00 USD | 9,250,000.00 USD | 5,850,000.00 USD | 11,970,000.00 USD |
| `7D` | `2201.90` | 161,060,000.00 USD | 0.00 USD | 161,060,000.00 USD | 9,110,000.00 USD | 266,430.00 USD | 18,630,000.00 USD |
| `1D` | `2203.00` | 144,240,000.00 USD | 0.00 USD | 144,240,000.00 USD | 12,320,000.00 USD | 12,690,000.00 USD | 12,670,000.00 USD |
| `7D` | `2204.70` | 133,050,000.00 USD | 0.00 USD | 133,050,000.00 USD | 5,350,000.00 USD | 4,330,000.00 USD | 4,430,000.00 USD |
| `1D` | `2205.40` | 106,560,000.00 USD | 0.00 USD | 106,560,000.00 USD | 8,540,000.00 USD | 1,580,000.00 USD | 2,870,000.00 USD |
| `7D` | `2207.50` | 118,940,000.00 USD | 0.00 USD | 118,940,000.00 USD | 19,630,000.00 USD | 3,390,000.00 USD | 3,660,000.00 USD |
| `1D` | `2207.80` | 93,560,000.00 USD | 0.00 USD | 93,560,000.00 USD | 11,640,000.00 USD | 6,260,000.00 USD | 2,050,000.00 USD |
| `1D` | `2210.20` | 73,610,000.00 USD | 0.00 USD | 73,610,000.00 USD | 4,040,000.00 USD | 5,850,000.00 USD | 6,290,000.00 USD |
| `7D` | `2210.30` | 92,280,000.00 USD | 0.00 USD | 92,280,000.00 USD | 4,740,000.00 USD | 0.00 USD | 11,300,000.00 USD |
| `1D` | `2212.60` | 57,430,000.00 USD | 0.00 USD | 57,430,000.00 USD | 12,700,000.00 USD | 6,410,000.00 USD | 1,950,000.00 USD |
| `7D` | `2213.10` | 76,230,000.00 USD | 0.00 USD | 76,230,000.00 USD | 1,710,000.00 USD | 1,980,000.00 USD | 8,850,000.00 USD |
| `1D` | `2215.00` | 36,380,000.00 USD | 0.00 USD | 36,380,000.00 USD | 2,300,000.00 USD | 2,930,000.00 USD | 139,270.00 USD |
| `7D` | `2215.90` | 63,690,000.00 USD | 0.00 USD | 63,690,000.00 USD | 0.00 USD | 0.00 USD | 565,690.00 USD |
| `1D` | `2217.40` | 31,010,000.00 USD | 0.00 USD | 31,010,000.00 USD | 748,080.00 USD | 3,550,000.00 USD | 3,960,000.00 USD |
| `7D` | `2218.70` | 63,120,000.00 USD | 0.00 USD | 63,120,000.00 USD | 22,400,000.00 USD | 487,520.00 USD | 218,310.00 USD |
| `1D` | `2219.80` | 22,760,000.00 USD | 0.00 USD | 22,760,000.00 USD | 6,340,000.00 USD | 2,000,000.00 USD | 1,880,000.00 USD |
| `7D` | `2221.50` | 40,020,000.00 USD | 0.00 USD | 40,020,000.00 USD | 0.00 USD | 12,220,000.00 USD | 18,870,000.00 USD |
| `1D` | `2222.20` | 12,540,000.00 USD | 0.00 USD | 12,540,000.00 USD | 0.00 USD | 4,290,000.00 USD | 2,560,000.00 USD |
| `7D` | `2224.30` | 8,930,000.00 USD | 0.00 USD | 8,930,000.00 USD | 0.00 USD | 0.00 USD | 911,920.00 USD |
| `1D` | `2224.60` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 374,450.00 USD | 94,480.00 USD | 0.00 USD |
| `1D` | `2227.00` | 5,220,000.00 USD | 0.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 5,220,000.00 USD |
| `7D` | `2227.10` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 557,870.00 USD | 0.00 USD | 7,460,000.00 USD |
| `7D` | `2228.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2229.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2229.40` | 12,290,000.00 USD | 12,290,000.00 USD | 0.00 USD | 0.00 USD | 12,070,000.00 USD | 224,760.00 USD |
| `7D` | `2229.90` | 20,990,000.00 USD | 20,990,000.00 USD | 0.00 USD | 1,910,000.00 USD | 0.00 USD | 19,080,000.00 USD |
| `1D` | `2231.80` | 53,120,000.00 USD | 53,120,000.00 USD | 0.00 USD | 40,420,000.00 USD | 0.00 USD | 411,180.00 USD |
| `7D` | `2232.70` | 21,950,000.00 USD | 21,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 959,630.00 USD |
| `7D` | `2235.50` | 47,190,000.00 USD | 47,190,000.00 USD | 0.00 USD | 3,260,000.00 USD | 21,640,000.00 USD | 350,840.00 USD |
| `1D` | `2236.60` | 59,920,000.00 USD | 59,920,000.00 USD | 0.00 USD | 6,800,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2238.30` | 61,230,000.00 USD | 61,230,000.00 USD | 0.00 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2239.00` | 68,340,000.00 USD | 68,340,000.00 USD | 0.00 USD | 8,420,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2241.10` | 93,140,000.00 USD | 93,140,000.00 USD | 0.00 USD | 31,910,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2241.40` | 68,470,000.00 USD | 68,470,000.00 USD | 0.00 USD | 81,700.00 USD | 0.00 USD | 50,930.00 USD |
| `1D` | `2243.80` | 69,420,000.00 USD | 69,420,000.00 USD | 0.00 USD | 381,040.00 USD | 569,860.00 USD | 0.00 USD |
| `7D` | `2243.90` | 95,000,000.00 USD | 95,000,000.00 USD | 0.00 USD | 1,590,000.00 USD | 268,650.00 USD | 0.00 USD |
| `1D` | `2246.20` | 83,650,000.00 USD | 83,650,000.00 USD | 0.00 USD | 5,570,000.00 USD | 4,370,000.00 USD | 4,290,000.00 USD |
| `7D` | `2246.70` | 112,030,000.00 USD | 112,030,000.00 USD | 0.00 USD | 6,720,000.00 USD | 1,300,000.00 USD | 9,020,000.00 USD |
| `1D` | `2248.60` | 100,000,000.00 USD | 100,000,000.00 USD | 0.00 USD | 5,090,000.00 USD | 5,320,000.00 USD | 5,930,000.00 USD |
| `7D` | `2249.50` | 122,610,000.00 USD | 122,610,000.00 USD | 0.00 USD | 2,960,000.00 USD | 6,990,000.00 USD | 640,060.00 USD |
| `1D` | `2251.00` | 107,420,000.00 USD | 107,420,000.00 USD | 0.00 USD | 6,720,000.00 USD | 630,890.00 USD | 77,860.00 USD |
| `7D` | `2252.30` | 144,330,000.00 USD | 144,330,000.00 USD | 0.00 USD | 10,050,000.00 USD | 11,670,000.00 USD | 0.00 USD |
| `1D` | `2253.40` | 113,820,000.00 USD | 113,820,000.00 USD | 0.00 USD | 893,130.00 USD | 3,370,000.00 USD | 2,130,000.00 USD |
| `7D` | `2255.10` | 161,500,000.00 USD | 161,500,000.00 USD | 0.00 USD | 10,050,000.00 USD | 6,600,000.00 USD | 514,610.00 USD |
| `1D` | `2255.80` | 148,930,000.00 USD | 148,930,000.00 USD | 0.00 USD | 18,730,000.00 USD | 7,340,000.00 USD | 9,040,000.00 USD |
| `7D` | `2257.90` | 201,190,000.00 USD | 201,190,000.00 USD | 0.00 USD | 20,510,000.00 USD | 12,290,000.00 USD | 6,890,000.00 USD |
| `1D` | `2258.20` | 173,740,000.00 USD | 173,740,000.00 USD | 0.00 USD | 16,130,000.00 USD | 6,840,000.00 USD | 1,830,000.00 USD |
| `1D` | `2260.60` | 195,150,000.00 USD | 195,150,000.00 USD | 0.00 USD | 9,590,000.00 USD | 9,340,000.00 USD | 2,480,000.00 USD |
| `7D` | `2260.70` | 205,520,000.00 USD | 205,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,320,000.00 USD |
| `1D` | `2263.00` | 226,460,000.00 USD | 226,460,000.00 USD | 0.00 USD | 14,130,000.00 USD | 10,400,000.00 USD | 6,780,000.00 USD |
| `7D` | `2263.50` | 213,910,000.00 USD | 213,910,000.00 USD | 0.00 USD | 6,720,000.00 USD | 1,460,000.00 USD | 218,310.00 USD |
| `1D` | `2265.40` | 250,860,000.00 USD | 250,860,000.00 USD | 0.00 USD | 3,490,000.00 USD | 9,180,000.00 USD | 11,740,000.00 USD |
| `7D` | `2266.30` | 228,400,000.00 USD | 228,400,000.00 USD | 0.00 USD | 0.00 USD | 8,160,000.00 USD | 6,330,000.00 USD |
| `1D` | `2267.80` | 284,550,000.00 USD | 284,550,000.00 USD | 0.00 USD | 14,030,000.00 USD | 10,980,000.00 USD | 8,680,000.00 USD |
| `7D` | `2269.10` | 257,710,000.00 USD | 257,710,000.00 USD | 0.00 USD | 11,010,000.00 USD | 133,210.00 USD | 18,160,000.00 USD |
| `1D` | `2270.20` | 326,860,000.00 USD | 326,860,000.00 USD | 0.00 USD | 15,300,000.00 USD | 7,980,000.00 USD | 19,030,000.00 USD |
| `7D` | `2271.90` | 286,490,000.00 USD | 286,490,000.00 USD | 0.00 USD | 18,240,000.00 USD | 3,640,000.00 USD | 6,900,000.00 USD |
| `1D` | `2272.60` | 352,700,000.00 USD | 352,700,000.00 USD | 0.00 USD | 15,500,000.00 USD | 4,860,000.00 USD | 5,480,000.00 USD |
| `7D` | `2274.70` | 313,020,000.00 USD | 313,020,000.00 USD | 0.00 USD | 19,630,000.00 USD | 6,900,000.00 USD | 0.00 USD |
| `1D` | `2275.00` | 394,530,000.00 USD | 394,530,000.00 USD | 0.00 USD | 26,690,000.00 USD | 11,580,000.00 USD | 3,550,000.00 USD |
| `1D` | `2277.40` | 434,430,000.00 USD | 434,430,000.00 USD | 0.00 USD | 10,430,000.00 USD | 17,510,000.00 USD | 11,960,000.00 USD |
| `7D` | `2277.50` | 339,270,000.00 USD | 339,270,000.00 USD | 0.00 USD | 6,890,000.00 USD | 8,890,000.00 USD | 10,480,000.00 USD |
| `1D` | `2279.80` | 472,780,000.00 USD | 472,780,000.00 USD | 0.00 USD | 17,260,000.00 USD | 9,050,000.00 USD | 12,040,000.00 USD |
| `7D` | `2280.30` | 383,590,000.00 USD | 383,590,000.00 USD | 0.00 USD | 854,200.00 USD | 39,830,000.00 USD | 3,640,000.00 USD |
| `1D` | `2282.20` | 520,490,000.00 USD | 520,490,000.00 USD | 0.00 USD | 22,980,000.00 USD | 21,840,000.00 USD | 2,900,000.00 USD |
| `7D` | `2283.10` | 475,410,000.00 USD | 475,410,000.00 USD | 0.00 USD | 5,600,000.00 USD | 72,520,000.00 USD | 13,690,000.00 USD |
| `1D` | `2284.60` | 565,750,000.00 USD | 565,750,000.00 USD | 0.00 USD | 22,570,000.00 USD | 11,280,000.00 USD | 11,410,000.00 USD |
| `7D` | `2285.90` | 479,110,000.00 USD | 479,110,000.00 USD | 0.00 USD | 1,010,000.00 USD | 2,590,000.00 USD | 109,160.00 USD |
| `1D` | `2287.00` | 593,810,000.00 USD | 593,810,000.00 USD | 0.00 USD | 8,540,000.00 USD | 12,040,000.00 USD | 7,470,000.00 USD |
| `7D` | `2288.70` | 511,750,000.00 USD | 511,750,000.00 USD | 0.00 USD | 8,380,000.00 USD | 9,320,000.00 USD | 14,930,000.00 USD |
| `1D` | `2289.40` | 619,360,000.00 USD | 619,360,000.00 USD | 0.00 USD | 9,320,000.00 USD | 13,110,000.00 USD | 3,120,000.00 USD |
| `7D` | `2291.50` | 523,630,000.00 USD | 523,630,000.00 USD | 0.00 USD | 4,310,000.00 USD | 517,070.00 USD | 7,060,000.00 USD |
| `1D` | `2291.80` | 653,440,000.00 USD | 653,440,000.00 USD | 0.00 USD | 19,670,000.00 USD | 5,470,000.00 USD | 8,940,000.00 USD |
| `1D` | `2294.20` | 686,500,000.00 USD | 686,500,000.00 USD | 0.00 USD | 15,170,000.00 USD | 6,680,000.00 USD | 11,210,000.00 USD |
| `7D` | `2294.30` | 544,960,000.00 USD | 544,960,000.00 USD | 0.00 USD | 14,670,000.00 USD | 1,490,000.00 USD | 5,180,000.00 USD |
| `1D` | `2296.60` | 723,200,000.00 USD | 723,200,000.00 USD | 0.00 USD | 19,950,000.00 USD | 13,010,000.00 USD | 3,750,000.00 USD |
| `7D` | `2297.10` | 594,710,000.00 USD | 594,710,000.00 USD | 0.00 USD | 25,900,000.00 USD | 8,070,000.00 USD | 15,780,000.00 USD |
| `1D` | `2299.00` | 769,230,000.00 USD | 769,230,000.00 USD | 0.00 USD | 20,870,000.00 USD | 15,020,000.00 USD | 10,140,000.00 USD |
| `7D` | `2299.90` | 637,630,000.00 USD | 637,630,000.00 USD | 0.00 USD | 16,200,000.00 USD | 20,940,000.00 USD | 5,780,000.00 USD |
| `1D` | `2301.40` | 803,120,000.00 USD | 803,120,000.00 USD | 0.00 USD | 12,570,000.00 USD | 6,810,000.00 USD | 14,500,000.00 USD |
| `7D` | `2302.70` | 692,300,000.00 USD | 692,300,000.00 USD | 0.00 USD | 26,960,000.00 USD | 10,860,000.00 USD | 16,850,000.00 USD |
| `1D` | `2303.80` | 832,430,000.00 USD | 832,430,000.00 USD | 0.00 USD | 14,800,000.00 USD | 11,390,000.00 USD | 3,130,000.00 USD |
| `7D` | `2305.50` | 718,310,000.00 USD | 718,310,000.00 USD | 0.00 USD | 6,340,000.00 USD | 8,820,000.00 USD | 10,860,000.00 USD |
| `1D` | `2306.20` | 866,350,000.00 USD | 866,350,000.00 USD | 0.00 USD | 13,350,000.00 USD | 11,600,000.00 USD | 8,970,000.00 USD |
| `7D` | `2308.30` | 720,610,000.00 USD | 720,610,000.00 USD | 0.00 USD | 1,240,000.00 USD | 930,630.00 USD | 134,160.00 USD |
| `1D` | `2308.60` | 870,320,000.00 USD | 870,320,000.00 USD | 0.00 USD | 477,740.00 USD | 3,320,000.00 USD | 182,210.00 USD |
| `1D` | `2311.00` | 888,180,000.00 USD | 888,180,000.00 USD | 0.00 USD | 6,170,000.00 USD | 877,090.00 USD | 10,810,000.00 USD |
| `7D` | `2311.10` | 751,110,000.00 USD | 751,110,000.00 USD | 0.00 USD | 11,560,000.00 USD | 2,790,000.00 USD | 16,150,000.00 USD |
| `1D` | `2313.40` | 905,700,000.00 USD | 905,700,000.00 USD | 0.00 USD | 6,490,000.00 USD | 8,560,000.00 USD | 2,470,000.00 USD |
| `7D` | `2313.90` | 761,930,000.00 USD | 761,930,000.00 USD | 0.00 USD | 1,100,000.00 USD | 7,460,000.00 USD | 2,260,000.00 USD |
| `1D` | `2315.80` | 939,630,000.00 USD | 939,630,000.00 USD | 0.00 USD | 10,440,000.00 USD | 15,940,000.00 USD | 7,540,000.00 USD |
| `7D` | `2316.70` | 767,630,000.00 USD | 767,630,000.00 USD | 0.00 USD | 1,020,000.00 USD | 3,640,000.00 USD | 1,040,000.00 USD |
| `1D` | `2318.20` | 954,490,000.00 USD | 954,490,000.00 USD | 0.00 USD | 5,950,000.00 USD | 6,680,000.00 USD | 2,230,000.00 USD |
| `7D` | `2319.50` | 796,900,000.00 USD | 796,900,000.00 USD | 0.00 USD | 5,530,000.00 USD | 15,850,000.00 USD | 7,890,000.00 USD |
| `1D` | `2320.60` | 974,700,000.00 USD | 974,700,000.00 USD | 0.00 USD | 5,860,000.00 USD | 11,510,000.00 USD | 2,840,000.00 USD |
| `7D` | `2322.30` | 802,760,000.00 USD | 802,760,000.00 USD | 0.00 USD | 2,300,000.00 USD | 3,450,000.00 USD | 108,040.00 USD |
| `1D` | `2323.00` | 995,800,000.00 USD | 995,800,000.00 USD | 0.00 USD | 4,360,000.00 USD | 12,060,000.00 USD | 4,670,000.00 USD |
| `7D` | `2325.10` | 825,790,000.00 USD | 825,790,000.00 USD | 0.00 USD | 10,150,000.00 USD | 2,770,000.00 USD | 10,120,000.00 USD |
| `1D` | `2325.40` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 0.00 USD | 2,050,000.00 USD | 6,790,000.00 USD | 1,510,000.00 USD |
| `1D` | `2327.80` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 0.00 USD | 494,310.00 USD | 1,240,000.00 USD | 4,530,000.00 USD |
| `7D` | `2327.90` | 837,690,000.00 USD | 837,690,000.00 USD | 0.00 USD | 3,860,000.00 USD | 0.00 USD | 8,030,000.00 USD |
| `1D` | `2330.20` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 0.00 USD | 11,050,000.00 USD | 2,970,000.00 USD | 1,390,000.00 USD |
| `7D` | `2330.70` | 853,910,000.00 USD | 853,910,000.00 USD | 0.00 USD | 15,800,000.00 USD | 363,770.00 USD | 54,580.00 USD |
| `1D` | `2332.60` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 0.00 USD | 2,430,000.00 USD | 2,150,000.00 USD | 5,980,000.00 USD |
| `7D` | `2333.50` | 895,000,000.00 USD | 895,000,000.00 USD | 0.00 USD | 20,270,000.00 USD | 12,860,000.00 USD | 7,960,000.00 USD |
| `1D` | `2335.00` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 9,140,000.00 USD | 5,110,000.00 USD | 5,680,000.00 USD |
| `7D` | `2336.30` | 932,260,000.00 USD | 932,260,000.00 USD | 0.00 USD | 24,310,000.00 USD | 7,570,000.00 USD | 5,390,000.00 USD |
| `1D` | `2337.40` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 0.00 USD | 12,780,000.00 USD | 1,030,000.00 USD | 5,770,000.00 USD |
| `7D` | `2339.10` | 958,660,000.00 USD | 958,660,000.00 USD | 0.00 USD | 14,040,000.00 USD | 0.00 USD | 12,370,000.00 USD |
| `1D` | `2339.80` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 10,420,000.00 USD | 6,440,000.00 USD | 12,080,000.00 USD |
| `7D` | `2341.90` | 999,090,000.00 USD | 999,090,000.00 USD | 0.00 USD | 8,610,000.00 USD | 17,820,000.00 USD | 14,000,000.00 USD |
| `1D` | `2342.20` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 5,460,000.00 USD | 3,720,000.00 USD | 2,170,000.00 USD |
| `1D` | `2344.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 6,740,000.00 USD | 8,550,000.00 USD | 6,430,000.00 USD |
| `7D` | `2344.70` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 0.00 USD | 2,480,000.00 USD | 16,920,000.00 USD | 8,520,000.00 USD |
| `1D` | `2347.00` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 4,320,000.00 USD | 3,650,000.00 USD | 4,800,000.00 USD |
| `7D` | `2347.50` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 0.00 USD | 8,220,000.00 USD | 18,860,000.00 USD |
| `1D` | `2349.40` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 16,880,000.00 USD | 6,200,000.00 USD | 5,410,000.00 USD |
| `7D` | `2350.30` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 1,630,000.00 USD | 20,110,000.00 USD | 15,150,000.00 USD |
| `1D` | `2351.80` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 13,580,000.00 USD | 2,340,000.00 USD | 7,250,000.00 USD |
| `7D` | `2353.10` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 2,710,000.00 USD | 35,770,000.00 USD | 4,640,000.00 USD |
| `1D` | `2354.20` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 3,750,000.00 USD | 5,600,000.00 USD | 1,030,000.00 USD |
| `7D` | `2355.90` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 18,560,000.00 USD | 10,720,000.00 USD | 3,950,000.00 USD |
| `1D` | `2356.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 4,660,000.00 USD | 1,150,000.00 USD | 1,180,000.00 USD |
| `7D` | `2358.70` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 6,870,000.00 USD | 512,220.00 USD | 3,190,000.00 USD |
| `1D` | `2359.00` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 6,170,000.00 USD | 5,570,000.00 USD | 7,330,000.00 USD |
| `1D` | `2361.40` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 0.00 USD | 7,910,000.00 USD | 8,680,000.00 USD | 1,350,000.00 USD |
| `7D` | `2361.50` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 3,150,000.00 USD | 3,430,000.00 USD | 374,770.00 USD |
| `1D` | `2363.80` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 0.00 USD | 5,570,000.00 USD | 2,830,000.00 USD | 8,900,000.00 USD |
| `7D` | `2364.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 3,860,000.00 USD | 373,740.00 USD | 10,920,000.00 USD |
| `1D` | `2366.20` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 0.00 USD | 3,150,000.00 USD | 827,140.00 USD | 1,830,000.00 USD |
| `7D` | `2367.10` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 6,340,000.00 USD | 1,310,000.00 USD | 307,410.00 USD |
| `1D` | `2368.60` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 0.00 USD | 5,640,000.00 USD | 4,130,000.00 USD | 3,390,000.00 USD |
| `7D` | `2369.90` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 0.00 USD | 24,940,000.00 USD | 475,460.00 USD | 18,790,000.00 USD |
| `1D` | `2371.00` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 0.00 USD | 14,100,000.00 USD | 6,060,000.00 USD | 4,800,000.00 USD |
| `7D` | `2372.70` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 0.00 USD | 15,600,000.00 USD | 0.00 USD | 39,640,000.00 USD |
| `1D` | `2373.40` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 12,300,000.00 USD | 1,570,000.00 USD | 5,900,000.00 USD |
| `7D` | `2375.50` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 9,700,000.00 USD | 1,050,000.00 USD | 11,870,000.00 USD |
| `1D` | `2375.80` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 6,150,000.00 USD | 2,810,000.00 USD | 4,130,000.00 USD |
| `1D` | `2378.20` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 0.00 USD | 1,650,000.00 USD | 1,010,000.00 USD | 3,240,000.00 USD |
| `7D` | `2378.30` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 11,180,000.00 USD | 7,020,000.00 USD | 23,870,000.00 USD |
| `1D` | `2380.60` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 0.00 USD | 6,120,000.00 USD | 6,700,000.00 USD | 5,230,000.00 USD |
| `7D` | `2381.10` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 4,540,000.00 USD | 2,390,000.00 USD | 16,460,000.00 USD |
| `1D` | `2383.00` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 15,730,000.00 USD | 9,480,000.00 USD | 9,300,000.00 USD |
| `7D` | `2383.90` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 0.00 USD | 8,840,000.00 USD | 21,750,000.00 USD | 30,520,000.00 USD |
| `1D` | `2385.40` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 7,510,000.00 USD | 10,280,000.00 USD | 4,890,000.00 USD |
| `7D` | `2386.70` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 0.00 USD | 17,720,000.00 USD | 32,140,000.00 USD | 42,040,000.00 USD |
| `1D` | `2387.80` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 0.00 USD | 9,900,000.00 USD | 5,870,000.00 USD | 2,790,000.00 USD |
| `7D` | `2389.50` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 5,670,000.00 USD | 35,860,000.00 USD | 28,760,000.00 USD |
| `1D` | `2390.20` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 0.00 USD | 4,300,000.00 USD | 3,310,000.00 USD | 1,520,000.00 USD |
| `7D` | `2392.30` | 1,730,000,000.00 USD | 1,730,000,000.00 USD | 0.00 USD | 26,840,000.00 USD | 45,530,000.00 USD | 39,160,000.00 USD |
| `1D` | `2392.60` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,660,000.00 USD | 3,320,000.00 USD |
| `1D` | `2395.00` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,830,000.00 USD | 2,170,000.00 USD |
| `7D` | `2395.10` | 1,820,000,000.00 USD | 1,820,000,000.00 USD | 0.00 USD | 39,180,000.00 USD | 24,870,000.00 USD | 29,410,000.00 USD |
| `1D` | `2397.40` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 0.00 USD | 64,150.00 USD | 3,720,000.00 USD | 3,400,000.00 USD |
| `7D` | `2397.90` | 1,920,000,000.00 USD | 1,920,000,000.00 USD | 0.00 USD | 34,290,000.00 USD | 36,430,000.00 USD | 23,570,000.00 USD |
| `1D` | `2399.80` | 1,490,000,000.00 USD | 1,490,000,000.00 USD | 0.00 USD | 2,150,000.00 USD | 637,690.00 USD | 1,390,000.00 USD |
| `7D` | `2400.70` | 2,010,000,000.00 USD | 2,010,000,000.00 USD | 0.00 USD | 42,030,000.00 USD | 25,390,000.00 USD | 24,070,000.00 USD |
| `1D` | `2402.20` | 1,490,000,000.00 USD | 1,490,000,000.00 USD | 0.00 USD | 1,140,000.00 USD | 315,710.00 USD | 552,090.00 USD |
| `7D` | `2403.50` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 0.00 USD | 51,300,000.00 USD | 24,760,000.00 USD | 30,980,000.00 USD |
| `1D` | `2404.60` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 0.00 USD | 4,740,000.00 USD | 3,420,000.00 USD | 4,440,000.00 USD |
| `7D` | `2406.30` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 0.00 USD | 29,700,000.00 USD | 33,710,000.00 USD | 14,210,000.00 USD |
| `1D` | `2407.00` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 0.00 USD | 8,030,000.00 USD | 3,500,000.00 USD | 2,400,000.00 USD |
| `7D` | `2409.10` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 0.00 USD | 25,090,000.00 USD | 21,480,000.00 USD | 27,910,000.00 USD |
| `1D` | `2409.40` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 0.00 USD | 3,280,000.00 USD | 3,650,000.00 USD | 3,080,000.00 USD |
| `1D` | `2411.80` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 0.00 USD | 6,680,000.00 USD | 3,520,000.00 USD | 2,050,000.00 USD |
| `7D` | `2411.90` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 0.00 USD | 15,970,000.00 USD | 21,640,000.00 USD | 13,990,000.00 USD |
| `1D` | `2414.20` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 0.00 USD | 1,120,000.00 USD | 1,530,000.00 USD | 28,750.00 USD |
| `7D` | `2414.70` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 0.00 USD | 22,250,000.00 USD | 19,630,000.00 USD | 21,720,000.00 USD |
| `1D` | `2416.60` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 0.00 USD | 2,830,000.00 USD | 1,520,000.00 USD | 3,320,000.00 USD |
| `7D` | `2417.50` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 0.00 USD | 22,310,000.00 USD | 8,700,000.00 USD | 21,160,000.00 USD |
| `1D` | `2419.00` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 0.00 USD | 4,830,000.00 USD | 1,420,000.00 USD | 2,120,000.00 USD |
| `7D` | `2420.30` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 0.00 USD | 29,980,000.00 USD | 18,780,000.00 USD | 9,160,000.00 USD |
| `1D` | `2421.40` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 3,950,000.00 USD | 4,860,000.00 USD | 5,110,000.00 USD |
| `7D` | `2423.10` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 0.00 USD | 17,920,000.00 USD | 17,260,000.00 USD | 21,330,000.00 USD |
| `1D` | `2423.80` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 440,460.00 USD | 1,280,000.00 USD | 1,300,000.00 USD |
| `7D` | `2425.90` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 0.00 USD | 12,980,000.00 USD | 15,310,000.00 USD | 17,380,000.00 USD |
| `1D` | `2426.20` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 2,090,000.00 USD | 1,100,000.00 USD | 40,970.00 USD |
| `1D` | `2428.60` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 670,680.00 USD | 885,270.00 USD | 1,470,000.00 USD |
| `7D` | `2428.70` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 0.00 USD | 12,800,000.00 USD | 7,090,000.00 USD | 8,840,000.00 USD |
| `1D` | `2431.00` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 3,120,000.00 USD | 2,130,000.00 USD | 677,240.00 USD |
| `7D` | `2431.50` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 0.00 USD | 9,420,000.00 USD | 12,660,000.00 USD | 8,750,000.00 USD |
| `1D` | `2433.40` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 1,770,000.00 USD | 1,680,000.00 USD | 1,680,000.00 USD |
| `7D` | `2434.30` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 0.00 USD | 13,090,000.00 USD | 3,830,000.00 USD | 3,220,000.00 USD |
| `1D` | `2435.80` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 2,490,000.00 USD | 1,050,000.00 USD | 161,010.00 USD |
| `7D` | `2437.10` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 0.00 USD | 7,130,000.00 USD | 7,440,000.00 USD | 6,120,000.00 USD |
| `1D` | `2438.20` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 476,020.00 USD | 153,260.00 USD | 15,480.00 USD |
| `7D` | `2439.90` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 0.00 USD | 12,730,000.00 USD | 4,970,000.00 USD | 3,700,000.00 USD |
| `1D` | `2440.60` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 1,230,000.00 USD | 1,130,000.00 USD | 858,540.00 USD |
| `7D` | `2442.70` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 0.00 USD | 5,050,000.00 USD | 5,320,000.00 USD | 7,900,000.00 USD |
| `1D` | `2443.00` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 1,040,000.00 USD | 42,810.00 USD | 747,370.00 USD |
| `1D` | `2445.40` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 13,780.00 USD | 703,990.00 USD | 755,960.00 USD |
| `7D` | `2445.50` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 0.00 USD | 9,990,000.00 USD | 7,470,000.00 USD | 10,400,000.00 USD |
| `1D` | `2447.80` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 1,210,000.00 USD | 888,690.00 USD | 1,540,000.00 USD |
| `7D` | `2448.30` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 0.00 USD | 10,750,000.00 USD | 3,770,000.00 USD | 15,050,000.00 USD |
| `1D` | `2450.20` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 486,110.00 USD | 69,580.00 USD | 26,770.00 USD |
| `7D` | `2451.10` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 8,450,000.00 USD | 7,240,000.00 USD | 7,080,000.00 USD |
| `1D` | `2452.60` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 3,200,000.00 USD | 1,840,000.00 USD | 2,370,000.00 USD |
| `7D` | `2453.90` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 4,220,000.00 USD | 2,980,000.00 USD | 3,870,000.00 USD |
| `1D` | `2455.00` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 2,270,000.00 USD | 1,990,000.00 USD | 905,110.00 USD |
| `7D` | `2456.70` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 8,340,000.00 USD | 7,380,000.00 USD | 7,500,000.00 USD |
| `1D` | `2457.40` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 1,720,000.00 USD | 1,920,000.00 USD | 845,630.00 USD |
| `7D` | `2459.50` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 0.00 USD | 3,220,000.00 USD | 4,870,000.00 USD | 6,000,000.00 USD |
| `1D` | `2459.80` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 0.00 USD | 1,240,000.00 USD | 1,370,000.00 USD | 366,800.00 USD |
| `1D` | `2462.10` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 0.00 USD | 0.00 USD | 551,660.00 USD | 829,050.00 USD |
| `7D` | `2462.30` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 0.00 USD | 6,600,000.00 USD | 5,990,000.00 USD | 5,150,000.00 USD |
| `7D` | `2465.10` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 0.00 USD | 4,900,000.00 USD | 3,130,000.00 USD | 2,820,000.00 USD |
| `7D` | `2467.90` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 0.00 USD | 2,900,000.00 USD | 1,870,000.00 USD | 23,760.00 USD |
| `7D` | `2470.70` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 0.00 USD | 3,960,000.00 USD | 2,050,000.00 USD | 522,210.00 USD |
| `7D` | `2473.50` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 0.00 USD | 5,300,000.00 USD | 2,920,000.00 USD | 3,180,000.00 USD |
| `7D` | `2476.30` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 0.00 USD | 2,070,000.00 USD | 1,710,000.00 USD | 872,130.00 USD |
| `7D` | `2479.10` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 0.00 USD | 3,070,000.00 USD | 4,130,000.00 USD | 540,990.00 USD |
| `7D` | `2481.90` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 0.00 USD | 601,420.00 USD | 3,680,000.00 USD | 1,050,000.00 USD |
| `7D` | `2484.70` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD |
| `7D` | `2487.50` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 275,450.00 USD | 211,130.00 USD | 0.00 USD |
| `7D` | `2490.30` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 338,890.00 USD | 286,610.00 USD | 0.00 USD |
| `7D` | `2491.80` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 2,580,000.00 USD | 733,870.00 USD | 445,140.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `28.47B` | Total OI Tokens: `12,781,182.2 ETH`
  * 1h OI Change: `+0.16%` | 4h OI Change: `-2.02%` | 24h OI Change: `-5.79%`
  * Exchange Breakdown: Binance=`8.40B` | Bybit=`2.10B` | OKX=`1.75B` | Hyperliquid=`2.35B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-134.89K` | Last 24h: `195.10K` | Last 3d: `5.21M` | Last 7d: `11.81M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0026%` | **USDT OKX** | `-0.0026%` |
| **USDT Bybit** | `-0.0028%` | **USDT KuCoin** | `-0.0043%` |
| **USDT MEXC** | `-0.0026%` | **USDT BingX** | `0.0015%` |
| **USDT Gate** | `0.0072%` | **USDT Bitget** | `0.0016%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0020%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `51.06%` | `48.94%` | `1.04` | 339,870,000.00 USD |
| `15M` | `Binance` | `52.24%` | `47.76%` | `1.09` | 106,100,000.00 USD |
| `15M` | `OKX` | `51.51%` | `48.49%` | `1.06` | 70,900,000.00 USD |
| `15M` | `Bybit` | `57.56%` | `42.44%` | `1.36` | 20,800,000.00 USD |
| `15M` | `KuCoin` | `34.7%` | `65.3%` | `0.53` | 1,710,000.00 USD |
| `15M` | `Gate` | `53.83%` | `46.17%` | `1.17` | 55,150,000.00 USD |
| `15M` | `Bitget` | `62.12%` | `37.88%` | `1.64` | 10,050,000.00 USD |
| `15M` | `BingX` | `34.16%` | `65.84%` | `0.52` | 6,830,000.00 USD |
| `15M` | `MEXC` | `47.88%` | `52.12%` | `0.92` | 11,000,000.00 USD |
| `15M` | `Bitunix` | `49.37%` | `50.63%` | `0.98` | 11,590,000.00 USD |
| `15M` | `Hyperliquid` | `38.52%` | `61.48%` | `0.63` | 24,530,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.4%` | `50.6%` | `0.98` | 827,390.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0.82%` | `99.18%` | `0.01` | 3,220,000.00 USD |
| `15M` | `HTX` | `53.57%` | `46.43%` | `1.15` | 5,100,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `54.78%` | `45.22%` | `1.21` | 3,300,000.00 USD |
| `15M` | `Bitfinex` | `66.44%` | `33.56%` | `1.98` | 31,940.00 USD |
| `15M` | `Kraken` | `35.4%` | `64.6%` | `0.55` | 772,220.00 USD |
| `15M` | `Aster` | `59.58%` | `40.42%` | `1.47` | 2,000,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `64.54%` | `35.46%` | `1.82` | 5,980,000.00 USD |
| `15M` | `Whale Positions` | `52.24%` | `47.76%` | `1.09` | 106,100,000.00 USD |
| `15M` | `Global Accounts` | `51.06%` | `48.94%` | `1.04` | 339,870,000.00 USD |
| `1H` | `ETH` | `55.27%` | `44.73%` | `1.24` | 1,340,000,000.00 USD |
| `1H` | `Binance` | `49.6%` | `50.4%` | `0.98` | 366,400,000.00 USD |
| `1H` | `OKX` | `48.19%` | `51.81%` | `0.93` | 232,960,000.00 USD |
| `1H` | `Bybit` | `52.72%` | `47.28%` | `1.12` | 72,970,000.00 USD |
| `1H` | `KuCoin` | `44.77%` | `55.23%` | `0.81` | 4,740,000.00 USD |
| `1H` | `Gate` | `51.75%` | `48.25%` | `1.07` | 184,090,000.00 USD |
| `1H` | `Bitget` | `50.25%` | `49.75%` | `1.01` | 37,580,000.00 USD |
| `1H` | `BingX` | `49.24%` | `50.76%` | `0.97` | 18,280,000.00 USD |
| `1H` | `MEXC` | `50.05%` | `49.95%` | `1.00` | 35,780,000.00 USD |
| `1H` | `Bitunix` | `46.92%` | `53.08%` | `0.88` | 39,310,000.00 USD |
| `1H` | `Hyperliquid` | `54.72%` | `45.28%` | `1.21` | 68,680,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.48%` | `51.52%` | `0.94` | 4,150,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `85.45%` | `14.55%` | `5.87` | 208,450,000.00 USD |
| `1H` | `HTX` | `29.05%` | `70.95%` | `0.41` | 24,160,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `50.73%` | `49.27%` | `1.03` | 13,310,000.00 USD |
| `1H` | `Bitfinex` | `56.63%` | `43.37%` | `1.31` | 449,120.00 USD |
| `1H` | `Kraken` | `41.18%` | `58.82%` | `0.70` | 3,980,000.00 USD |
| `1H` | `Aster` | `41.31%` | `58.69%` | `0.70` | 6,370,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `57.58%` | `42.42%` | `1.36` | 13,340,000.00 USD |
| `1H` | `Whale Positions` | `49.6%` | `50.4%` | `0.98` | 366,400,000.00 USD |
| `1H` | `Global Accounts` | `55.27%` | `44.73%` | `1.24` | 1,340,000,000.00 USD |
| `4H` | `ETH` | `50.05%` | `49.95%` | `1.00` | 6,470,000,000.00 USD |
| `4H` | `Binance` | `49.71%` | `50.29%` | `0.99` | 2,100,000,000.00 USD |
| `4H` | `OKX` | `49.06%` | `50.94%` | `0.96` | 1,160,000,000.00 USD |
| `4H` | `Bybit` | `45.86%` | `54.14%` | `0.85` | 383,700,000.00 USD |
| `4H` | `KuCoin` | `45.85%` | `54.15%` | `0.85` | 19,360,000.00 USD |
| `4H` | `Gate` | `50.53%` | `49.47%` | `1.02` | 951,260,000.00 USD |
| `4H` | `Bitget` | `48.93%` | `51.07%` | `0.96` | 220,180,000.00 USD |
| `4H` | `BingX` | `44.33%` | `55.67%` | `0.80` | 72,800,000.00 USD |
| `4H` | `MEXC` | `52.48%` | `47.52%` | `1.10` | 252,670,000.00 USD |
| `4H` | `Bitunix` | `50.02%` | `49.98%` | `1.00` | 209,910,000.00 USD |
| `4H` | `Hyperliquid` | `42.08%` | `57.92%` | `0.73` | 285,500,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.36%` | `49.64%` | `1.01` | 35,620,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `62.94%` | `37.06%` | `1.70` | 486,410,000.00 USD |
| `4H` | `HTX` | `43.44%` | `56.56%` | `0.77` | 82,920,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `44.47%` | `55.53%` | `0.80` | 68,590,000.00 USD |
| `4H` | `Bitfinex` | `36.96%` | `63.04%` | `0.59` | 1,900,000.00 USD |
| `4H` | `Kraken` | `48.79%` | `51.21%` | `0.95` | 10,740,000.00 USD |
| `4H` | `Aster` | `49.29%` | `50.71%` | `0.97` | 52,010,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `52.17%` | `47.83%` | `1.09` | 79,020,000.00 USD |
| `4H` | `Whale Positions` | `49.71%` | `50.29%` | `0.99` | 2,100,000,000.00 USD |
| `4H` | `Global Accounts` | `50.05%` | `49.95%` | `1.00` | 6,470,000,000.00 USD |


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
| `5:00 UTC` | `2227.25` | `2227.86` | `2227.25` | `2229.75` | `2226.25` | 44,206,290.46 USD | 23,100,296.60 USD | 21,105,993.85 USD | 1,994,302.75 USD | `+4.51%` | `0B / 0S` |

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
| `5m` | 163,880.00 USD | 2,340,000.00 USD | **`ACCUMULATION`** |
| `15m` | 2,110,000.00 USD | 7,230,000.00 USD | **`ACCUMULATION`** |
| `30m` | 56,620.00 USD | 17,980,000.00 USD | **`ACCUMULATION`** |
| `1h` | -14,600,000.00 USD | -7,270,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -20,850,000.00 USD | -19,640,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -13,860,000.00 USD | -74,480,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -16,930,000.00 USD | -80,860,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -2,430,000.00 USD | -166,520,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -76,930,000.00 USD | -678,200,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -150,950,000.00 USD | -1,960,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -218,390,000.00 USD | -3,080,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,180,000,000.00 USD | -9,790,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+163.88K` | 15m=`+2.11M` | 1h=`-14.60M` | 24h=`-150.95M`
* Futures Capital Netflows: 5m=`+2.34M` | 15m=`+7.23M` | 1h=`-7.27M` | 24h=`-1.96B`
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
  * `2026-10-30 15:18:36 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:36 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:36 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:37:36 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:36 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:32:36 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)


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
