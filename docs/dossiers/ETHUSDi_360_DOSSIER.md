# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 10:25:42 IST` (`2026-10-30 04:55:42 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2239.10` | **Live Ask Quote**: `2242.70` | **Mid Price**: `2240.90`
- **Spread Points**: `360.00` | **Spread BPS**: `16.06 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2211.30` | VWAP Z-Score: `+1.85` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `17.10` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `52.39` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2255.75` | Lower -3.00σ Band: `2166.84`
  * Upper +2.51σ Band: `2248.49` | Lower -2.51σ Band: `2174.10`
  * Upper +2.01σ Band: `2241.08` | Lower -2.01σ Band: `2181.51`
  * Upper +2.00σ Band: `2240.93` | Lower -2.00σ Band: `2181.66`
  * Upper +1.28σ Band: `2230.27` | Lower -1.28σ Band: `2192.33`
  * Upper +1.00σ Band: `2226.12` | Lower -1.00σ Band: `2196.48`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2225.83` | EMA-20=`2227.95` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2255.89` (Slope: `+0.0000`) | EMA-100=`2282.78`
  * Institutional Anchors: EMA-144=`2294.55` | EMA-200=`2303.59` (Slope: `-0.4793`) | EMA-233=`2308.57`
- **Range Boundaries**: 24H High=`2374.90` | 24H Low=`2167.70` | Weekly High=`2387.80` | Weekly Low=`2167.70`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2280.60` (Distance: `-1.76%`)
  * Point of Control (POC) = `2264.42` (Distance: `-1.06%`)
  * Value Area Low (VAL) = `2207.76` (Distance: `+1.48%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2339.52` | POC=`2321.58` | VAL=`2296.66`
  * Prior Day Extremes: PDH=`2374.90` | PDL=`2225.40` | PDC=`2252.70`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2351.85` | Weekly POC=`2309.30` | Weekly VAL=`2300.49`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2289.10` | Low=`2167.70`
  * London Session (08:00-16:00 UTC): High=`2249.86` | Low=`2231.94`
  * New York Session (13:00-21:00 UTC): High=`2254.35` | Low=`2227.45`
  * Initial Balance (First Hour): IB High=`2247.62` | IB Low=`2234.18`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2231.94` - `2249.86`
  * Optimal Trade Entry (OTE 0.705): `2245.38`
  * Structural Invalidation Anchor (0.786): `2258.83`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2243.26` | `2245.83` | `2242.57` | `2243.36` | `21,837` | 49,002,965.20 USD | -1,156,398.46 USD | `-2.36%` | -1,030,824,899.58 USD | `-0.39` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `2243.36` | `2245.99` | `2243.00` | `2245.49` | `22,137` | 49,687,433.71 USD | -2,899,438.65 USD | `-5.84%` | -1,033,724,338.22 USD | `-0.64` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `2245.49` | `2246.30` | `2244.63` | `2245.00` | `11,638` | 26,134,304.40 USD | -995,012.12 USD | `-3.81%` | -1,034,719,350.34 USD | `-0.31` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `2236.83` | `2243.26` | `2233.91` | `2243.25` | `55,082` | 123,392,803.54 USD | 12,084,914.83 USD | `+9.79%` | -1,040,789,482.89 USD | `+0.62` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `2243.26` | `2246.30` | `2242.57` | `2245.14` | `58,155` | 130,536,562.11 USD | -7,028,617.44 USD | `-5.38%` | -1,047,818,100.33 USD | `+0.17` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `2245.13` | `2246.94` | `2243.62` | `2245.43` | `22,132` | 49,700,364.28 USD | 3,580,054.84 USD | `+7.20%` | -1,044,238,045.48 USD | `+0.38` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `2194.71` | `2218.96` | `2181.22` | `2209.27` | `270,460` | 596,517,649.16 USD | 43,347,954.49 USD | `+7.27%` | -1,076,486,651.41 USD | `+0.85` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `2209.27` | `2238.00` | `2208.12` | `2236.82` | `225,707` | 502,124,659.31 USD | 34,201,688.52 USD | `+6.81%` | -1,042,284,962.89 USD | `+0.73` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `2236.81` | `2246.94` | `2225.47` | `2245.43` | `191,671` | 429,218,645.17 USD | -1,953,082.60 USD | `-0.46%` | -1,044,238,045.48 USD | `+0.41` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2252.34` | `2,564,135` | 5,830,064,162.53 USD | -554,237,569.32 USD | `-9.51%` | -701,515,761.74 USD | `-1.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -963,151,175.97 USD | `-0.31` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2246.30` | `2225.47` | `2245.00` | `166,996` | 373,806,422.08 USD | -3,555,369.23 USD | `-0.95%` | -966,706,545.19 USD | `+0.74` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | 54,877,924.52 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -147,278,192.42 USD | `-1.22` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2252.34` | `2,564,135` | 5,830,064,162.53 USD | -554,237,569.32 USD | `-9.51%` | -701,515,761.74 USD | `-1.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -963,151,175.97 USD | `-0.31` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2246.94` | `2225.47` | `2245.48` | `191,632` | 429,129,554.11 USD | -1,864,395.73 USD | `-0.43%` | -965,015,571.69 USD | `+0.74` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`2240.90`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2242.70` | `338.4720` | 759,091.15 USD | 9,539,564.34 USD | `4 orders` | `-0.09%` | `-` |
| `BID` | `2242.80` | `85.7636` | 192,350.60 USD | 8,780,473.19 USD | `6 orders` | `-0.08%` | `-` |
| `BID` | `2242.90` | `87.2263` | 195,639.87 USD | 8,588,122.59 USD | `8 orders` | `-0.08%` | `-` |
| `BID` | `2243.00` | `67.6584` | 151,757.79 USD | 8,392,482.72 USD | `5 orders` | `-0.07%` | `-` |
| `BID` | `2243.10` | `202.9039` | 455,133.74 USD | 8,240,724.93 USD | `9 orders` | `-0.07%` | `-` |
| `BID` | `2243.20` | `149.2314` | 334,755.88 USD | 7,785,591.19 USD | `10 orders` | `-0.06%` | `-` |
| `BID` | `2243.30` | `372.9413` | 836,619.22 USD | 7,450,835.31 USD | `11 orders` | `-0.06%` | `-` |
| `BID` | `2243.40` | `119.0409` | 267,056.36 USD | 6,614,216.10 USD | `10 orders` | `-0.06%` | `-` |
| `BID` | `2243.50` | `472.2804` | 1,059,561.08 USD | 6,347,159.74 USD | `10 orders` | `-0.05%` | `-` |
| `BID` | `2243.60` | `218.4971` | 490,220.09 USD | 5,287,598.66 USD | `12 orders` | `-0.05%` | `-` |
| `BID` | `2243.70` | `52.8959` | 118,682.53 USD | 4,797,378.57 USD | `12 orders` | `-0.04%` | `-` |
| `BID` | `2243.80` | `358.2152` | 803,763.27 USD | 4,678,696.04 USD | `10 orders` | `-0.04%` | `-` |
| `BID` | `2243.90` | `334.1064` | 749,701.35 USD | 3,874,932.77 USD | `8 orders` | `-0.03%` | `-` |
| `BID` | `2244.00` | `348.4225` | 781,860.09 USD | 3,125,231.42 USD | `13 orders` | `-0.03%` | `-` |
| `BID` | `2244.10` | `291.3142` | 653,738.20 USD | 2,343,371.33 USD | `14 orders` | `-0.02%` | `-` |
| `BID` | `2244.20` | `181.6783` | 407,722.44 USD | 1,689,633.14 USD | `12 orders` | `-0.02%` | `-` |
| `BID` | `2244.30` | `243.2254` | 545,870.77 USD | 1,281,910.69 USD | `14 orders` | `-0.02%` | `-` |
| `BID` | `2244.40` | `272.1767` | 610,873.39 USD | 736,039.93 USD | `8 orders` | `-0.01%` | `-` |
| `BID` | `2244.50` | `44.7287` | 100,393.57 USD | 125,166.54 USD | `5 orders` | `-0.01%` | `-` |
| `BID` | `2244.60` | `11.0367` | 24,772.98 USD | 24,772.98 USD | `3 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2244.65` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,244.65` | `0.00%` | `-` |
| `ASK` | `2244.70` | `73.4083` | 164,779.61 USD | 164,779.61 USD | `10 orders` | `+0.00%` | `-` |
| `ASK` | `2244.80` | `216.5261` | 486,057.79 USD | 650,837.40 USD | `34 orders` | `+0.01%` | `-` |
| `ASK` | `2244.90` | `76.3463` | 171,389.81 USD | 822,227.21 USD | `11 orders` | `+0.01%` | `-` |
| `ASK` | `2245.00` | `27.4526` | 61,631.09 USD | 883,858.30 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `2245.10` | `41.7851` | 93,811.73 USD | 977,670.02 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `2245.20` | `58.7965` | 132,009.90 USD | 1,109,679.93 USD | `7 orders` | `+0.02%` | `-` |
| `ASK` | `2245.30` | `134.4740` | 301,934.47 USD | 1,411,614.40 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `2245.40` | `292.3829` | 656,516.56 USD | 2,068,130.96 USD | `11 orders` | `+0.03%` | `-` |
| `ASK` | `2245.50` | `280.3109` | 629,438.13 USD | 2,697,569.09 USD | `10 orders` | `+0.04%` | `-` |
| `ASK` | `2245.60` | `93.3608` | 209,651.01 USD | 2,907,220.10 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `2245.70` | `111.4711` | 250,330.65 USD | 3,157,550.75 USD | `9 orders` | `+0.05%` | `-` |
| `ASK` | `2245.80` | `230.2378` | 517,068.05 USD | 3,674,618.80 USD | `8 orders` | `+0.05%` | `-` |
| `ASK` | `2245.90` | `694.9023` | 1,560,681.08 USD | 5,235,299.88 USD | `14 orders` | `+0.06%` | `-` |
| `ASK` | `2246.00` | `106.1862` | 238,494.21 USD | 5,473,794.08 USD | `12 orders` | `+0.06%` | `-` |
| `ASK` | `2246.10` | `153.0571` | 343,781.55 USD | 5,817,575.63 USD | `10 orders` | `+0.06%` | `-` |
| `ASK` | `2246.20` | `136.8671` | 307,430.88 USD | 6,125,006.51 USD | `7 orders` | `+0.07%` | `-` |
| `ASK` | `2246.30` | `131.6455` | 295,715.29 USD | 6,420,721.80 USD | `10 orders` | `+0.07%` | `-` |
| `ASK` | `2246.40` | `82.1330` | 184,503.57 USD | 6,605,225.37 USD | `8 orders` | `+0.08%` | `-` |
| `ASK` | `2246.50` | `562.7222` | 1,264,155.42 USD | 7,869,380.79 USD | `14 orders` | `+0.08%` | `-` |
| `ASK` | `2246.60` | `110.5893` | 248,449.92 USD | 8,117,830.72 USD | `15 orders` | `+0.09%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:24:51 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1844.27` | `7,964.66` | 14,688,972.62 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-30 10:24:51 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 10:24:51 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1913.52` | `6,500.22` | 12,438,334.12 USD | `AT_RISK_LIQ` | `0xf78c5d8d4b` | `2026-10-30 10:24:51 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `10,000.00` | 19,261,000.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-30 10:24:51 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1928.81` | `8,092.45` | 15,608,770.69 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 10:24:51 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2122.22` | `30,641.99` | 65,028,977.30 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 10:24:51 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2129.50` | `26,025.05` | 55,420,231.63 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 10:24:51 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2175.00` | `3,000.00` | 6,525,000.00 USD | `TRIGGER_STOP` | `0x469e9a7f62` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2207.40` | `266.00` | 587,168.40 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x24fb652303` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2207.90` | `2,011.52` | 4,441,235.67 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2209.90` | `505.00` | 1,115,999.50 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2210.10` | `4,701.86` | 10,391,585.21 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2219.00` | `1,405.55` | 3,118,915.89 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2221.00` | `458.19` | 1,017,637.99 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x9362ca4dfd` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2226.10` | `357.00` | 794,719.93 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2226.10` | `342.27` | 761,925.47 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2226.70` | `2,422.48` | 5,394,146.68 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2226.70` | `504.71` | 1,123,839.98 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2227.50` | `982.33` | 2,188,136.73 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2232.00` | `504.79` | 1,126,686.82 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2234.20` | `1,794.21` | 4,008,613.93 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2234.30` | `715.66` | 1,599,005.39 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2235.80` | `355.25` | 794,263.70 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2236.30` | `1,344.36` | 3,006,382.43 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2236.60` | `471.77` | 1,055,151.84 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2237.40` | `1,234.64` | 2,762,390.02 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2238.10` | `895.53` | 2,004,275.62 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2238.80` | `483.51` | 1,082,492.49 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2240.10` | `671.01` | 1,503,138.24 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2241.50` | `447.03` | 1,002,015.50 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2242.20` | `354.91` | 795,777.18 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2243.60` | `334.99` | 751,585.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2247.80` | `334.38` | 751,608.13 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2248.70` | `445.71` | 1,002,257.73 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2249.20` | `250.98` | 564,501.97 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2249.40` | `354.74` | 797,961.38 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2249.90` | `668.12` | 1,503,211.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2252.20` | `889.91` | 2,004,254.63 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2252.30` | `478.75` | 1,078,296.51 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2253.50` | `471.98` | 1,063,606.93 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2253.70` | `1,235.96` | 2,785,486.88 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2254.40` | `1,333.59` | 3,006,436.50 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2256.10` | `352.47` | 795,206.66 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2256.70` | `1,776.28` | 4,008,525.66 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2256.80` | `679.17` | 1,532,754.69 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2257.10` | `504.77` | 1,139,325.40 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2261.30` | `2,422.48` | 5,477,964.65 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2263.60` | `981.79` | 2,222,387.09 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2263.60` | `504.46` | 1,141,902.45 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2266.30` | `336.20` | 761,925.53 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2269.70` | `620.97` | 1,409,408.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x674982e841` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2269.80` | `350.13` | 794,719.85 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2272.20` | `2,200.51` | 4,999,999.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb1ec7febea` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2272.30` | `1,432.02` | 3,253,975.41 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2275.70` | `4,696.65` | 10,688,176.87 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2278.00` | `504.78` | 1,149,879.73 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2283.70` | `2,099.23` | 4,794,022.51 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:24:51 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2289.80` | `3,258.62` | 7,461,591.51 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 10:24:51 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2300.00` | `4,002.10` | 9,204,832.99 USD | `TRIGGER_STOP` | `0xfb941d2344` | `2026-10-30 10:24:51 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2463.82` | `22,046.99` | 54,319,767.92 USD | `AT_RISK_LIQ` | `0x8added25f8` | `2026-10-30 10:24:51 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `2,733.67` | 6,872,176.53 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-30 10:24:51 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2624.22` | `10,000.00` | 26,242,230.56 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-30 10:24:51 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2658.08` | `9,700.00` | 25,783,366.12 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-30 10:24:51 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 238,939,686.96 USD | `106,417.71` | `2322.74` | `2246.30` | `3785.59` | 8,241,325.20 USD | `+3.45%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 145,207,992.35 USD | `64,680.62` | `2375.30` | `2246.30` | `4325.98` | 8,428,305.15 USD | `+5.80%` | `5X Cross` |
| `10` | `0x77dd...e0e9` | `LONG` | 68,772,886.17 USD | `30,641.99` | `2610.31` | `2246.30` | `2122.13` | -11,212,288.87 USD | `-16.30%` | `10X Cross` |
| `11` | `0xde8d...9524` | `LONG` | 67,993,080.58 USD | `30,282.40` | `2134.45` | `2246.30` | `1786.39` | 3,356,750.00 USD | `+4.94%` | `20X Cross` |
| `17` | `0x0392...d7d9` | `LONG` | 58,426,239.72 USD | `26,025.05` | `2518.71` | `2246.30` | `2129.41` | -7,123,482.37 USD | `-12.19%` | `9X Cross` |
| `23` | `0x8add...7d2c` | `SHORT` | 49,491,080.46 USD | `22,046.99` | `2271.09` | `2246.30` | `2458.58` | 579,816.84 USD | `+1.17%` | `25X Cross` |
| `27` | `0xdf95...7d72` | `SHORT` | 44,847,222.75 USD | `19,980.94` | `2402.53` | `2246.30` | `4187.68` | 3,157,679.39 USD | `+7.04%` | `25X Cross` |
| `35` | `0xeced...6210` | `SHORT` | 37,471,952.58 USD | `16,687.58` | `2522.09` | `2246.30` | `3476.10` | 4,615,762.41 USD | `+12.32%` | `20X Cross` |
| `36` | `0xb695...a92d` | `SHORT` | 36,387,103.97 USD | `16,214.56` | `2557.74` | `2246.30` | `3916.05` | 5,085,624.86 USD | `+13.98%` | `20X Cross` |
| `37` | `0x6046...b21d` | `LONG` | 35,762,217.15 USD | `15,927.59` | `2410.19` | `2246.30` | `1756.34` | -2,626,402.49 USD | `-7.34%` | `6X Cross` |
| `40` | `0x45d2...4029` | `SHORT` | 31,306,590.00 USD | `13,950.00` | `2443.60` | `2246.30` | `5300.65` | 2,781,692.46 USD | `+8.89%` | `20X Cross` |
| `44` | `0xa61c...66b9` | `LONG` | 28,929,693.60 USD | `12,888.00` | `2369.69` | `2246.30` | `1429.43` | -1,610,960.94 USD | `-5.57%` | `10X Cross` |
| `47` | `0x2371...0883` | `LONG` | 26,940,000.00 USD | `12,000.00` | `2421.77` | `2246.30` | `1279.37` | -2,121,294.85 USD | `-7.87%` | `20X Cross` |
| `48` | `0xbd1c...ff0e` | `LONG` | 26,934,000.00 USD | `12,000.00` | `2419.91` | `2246.30` | `1520.27` | -2,105,032.39 USD | `-7.82%` | `20X Cross` |
| `54` | `0x09dc...c094` | `LONG` | 24,700,500.00 USD | `11,000.00` | `2465.31` | `2246.30` | `1637.34` | -2,417,923.04 USD | `-9.79%` | `20X Cross` |
| `55` | `0xa9de...e049` | `LONG` | 24,698,300.00 USD | `11,000.00` | `2481.81` | `2246.30` | `1644.01` | -2,601,679.46 USD | `-10.53%` | `20X Cross` |
| `56` | `0x0c5d...36b3` | `LONG` | 24,698,300.00 USD | `11,000.00` | `2482.20` | `2246.30` | `1644.34` | -2,605,953.24 USD | `-10.55%` | `20X Cross` |
| `57` | `0x6c93...59a4` | `LONG` | 24,692,140.00 USD | `11,000.00` | `2441.15` | `2246.30` | `1602.30` | -2,160,532.73 USD | `-8.75%` | `20X Cross` |
| `70` | `0xa2ce...3126` | `LONG` | 22,482,876.39 USD | `10,016.88` | `2162.83` | `2246.30` | `1535.51` | 818,074.34 USD | `+3.64%` | `10X Cross` |
| `71` | `0x15a4...dfdb` | `LONG` | 22,453,000.00 USD | `10,000.00` | `1761.94` | `2246.30` | `268.47` | 4,833,518.97 USD | `+21.53%` | `20X Cross` |
| `72` | `0xb37f...66ca` | `SHORT` | 22,443,000.00 USD | `10,000.00` | `2290.69` | `2246.30` | `2624.15` | 463,991.85 USD | `+2.07%` | `25X Cross` |
| `73` | `0xec7f...df39` | `LONG` | 22,442,000.00 USD | `10,000.00` | `2719.35` | `2246.30` | `1720.86` | -4,751,548.52 USD | `-21.17%` | `20X Cross` |
| `74` | `0x6646...6de5` | `LONG` | 22,440,000.00 USD | `10,000.00` | `1765.80` | `2246.30` | `1726.34` | 4,781,942.55 USD | `+21.31%` | `25X Cross` |
| `76` | `0x939f...04d2` | `LONG` | 22,057,407.10 USD | `9,823.81` | `2427.28` | `2246.30` | `1764.84` | -1,787,743.50 USD | `-8.10%` | `25X Cross` |
| `78` | `0xaeaa...2416` | `SHORT` | 21,776,500.00 USD | `9,700.00` | `2311.92` | `2246.30` | `2658.00` | 649,182.40 USD | `+2.98%` | `25X Cross` |
| `83` | `0xf517...c032` | `SHORT` | 20,934,851.34 USD | `9,326.35` | `2202.91` | `2246.30` | `3144.50` | -389,713.12 USD | `-1.86%` | `25X Cross` |
| `85` | `0xca49...53c8` | `SHORT` | 20,648,622.98 USD | `9,200.88` | `2549.39` | `2246.30` | `3870.26` | 2,808,084.55 USD | `+13.60%` | `25X Cross` |
| `86` | `0xba5d...a352` | `SHORT` | 20,324,693.29 USD | `9,054.12` | `2493.89` | `2246.30` | `2912.83` | 2,255,313.97 USD | `+11.10%` | `20X Cross` |
| `88` | `0xea00...a918` | `LONG` | 20,213,590.04 USD | `9,003.83` | `2003.01` | `2246.30` | `1358.12` | 2,178,811.18 USD | `+10.78%` | `5X Cross` |
| `93` | `0xefe4...194b` | `SHORT` | 19,806,598.24 USD | `8,820.57` | `2267.42` | `2246.30` | `3576.48` | 193,416.15 USD | `+0.98%` | `20X Cross` |
| `114` | `0x9eec...daab` | `LONG` | 18,161,890.25 USD | `8,092.45` | `1658.44` | `2246.30` | `1928.17` | 4,741,025.72 USD | `+26.10%` | `15X Cross` |
| `115` | `0x5f91...65aa` | `LONG` | 17,883,041.89 USD | `7,964.66` | `1626.99` | `2246.30` | `1844.18` | 4,924,598.83 USD | `+27.54%` | `16X Cross` |
| `119` | `0xecb6...2b00` | `SHORT` | 17,087,745.44 USD | `7,609.43` | `2242.36` | `2246.30` | `5889.24` | -24,625.59 USD | `-0.14%` | `15X Cross` |
| `126` | `0xec0b...b078` | `LONG` | 15,730,406.19 USD | `7,007.80` | `2065.97` | `2246.30` | `1061.17` | 1,252,476.60 USD | `+7.96%` | `25X Cross` |
| `131` | `0xf02d...5eb3` | `LONG` | 15,389,904.89 USD | `6,855.99` | `2383.33` | `2246.30` | `1122.56` | -950,183.88 USD | `-6.17%` | `20X Cross` |
| `132` | `0xcf53...ee11` | `SHORT` | 15,270,062.46 USD | `6,803.63` | `1862.69` | `2246.30` | `4208.26` | -2,596,957.07 USD | `-17.01%` | `7X Cross` |
| `135` | `0x418a...8888` | `SHORT` | 15,099,601.58 USD | `6,724.38` | `2494.55` | `2246.30` | `3010.01` | 1,674,721.60 USD | `+11.09%` | `25X Cross` |
| `139` | `0x4ff9...38d3` | `LONG` | 14,735,088.76 USD | `6,564.10` | `2447.40` | `2246.30` | `1669.96` | -1,329,933.98 USD | `-9.03%` | `3X Isolated` |
| `141` | `0xf78c...c581` | `LONG` | 14,592,997.27 USD | `6,500.22` | `2521.53` | `2246.30` | `1913.44` | -1,797,543.68 USD | `-12.32%` | `20X Cross` |
| `142` | `0x1ee7...edf5` | `LONG` | 14,592,500.00 USD | `6,500.00` | `2301.55` | `2246.30` | `2069.17` | -367,593.66 USD | `-2.52%` | `25X Cross` |
| `145` | `0x799f...5f4c` | `LONG` | 14,166,337.07 USD | `6,310.90` | `2390.33` | `2246.30` | `1837.52` | -918,827.54 USD | `-6.49%` | `20X Cross` |
| `148` | `0x08bf...7872` | `SHORT` | 13,969,874.39 USD | `6,224.05` | `2258.00` | `2246.30` | `2585.23` | 84,041.72 USD | `+0.60%` | `20X Cross` |
| `154` | `0xd9e7...4aff` | `LONG` | 13,471,800.00 USD | `6,000.00` | `2480.18` | `2246.30` | `1407.73` | -1,409,324.33 USD | `-10.46%` | `20X Cross` |
| `163` | `0x0c4a...1b19` | `LONG` | 12,709,748.94 USD | `5,660.10` | `2373.06` | `2246.30` | `2081.78` | -722,009.19 USD | `-5.68%` | `25X Isolated` |
| `168` | `0x7fda...17d1` | `LONG` | 11,937,067.51 USD | `5,315.76` | `2211.05` | `2246.30` | `0.000000` | 183,625.27 USD | `+1.54%` | `25X Cross` |
| `171` | `0xc179...e0c8` | `LONG` | 11,883,521.40 USD | `5,291.91` | `2306.49` | `2246.30` | `978.96` | -322,226.24 USD | `-2.71%` | `10X Cross` |
| `178` | `0x218a...7da2` | `SHORT` | 11,726,905.97 USD | `5,222.87` | `2208.16` | `2246.30` | `2792.88` | -193,970.91 USD | `-1.65%` | `10X Cross` |
| `187` | `0x45ab...6cbc` | `LONG` | 11,049,036.43 USD | `4,920.96` | `2727.66` | `2246.30` | `1376.57` | -2,373,707.37 USD | `-21.48%` | `7X Cross` |
| `192` | `0x64b7...9da9` | `LONG` | 10,902,146.95 USD | `4,856.84` | `2604.61` | `2246.30` | `587.27` | -1,748,067.46 USD | `-16.03%` | `25X Cross` |
| `198` | `0xfb18...eb17` | `SHORT` | 10,700,756.51 USD | `4,768.18` | `2315.53` | `2246.30` | `2592.69` | 340,125.28 USD | `+3.18%` | `25X Cross` |
| `200` | `0x5559...d43b` | `SHORT` | 10,678,479.08 USD | `4,755.93` | `2262.69` | `2246.30` | `2779.02` | 82,726.80 USD | `+0.77%` | `25X Cross` |
| `211` | `0xe091...6705` | `SHORT` | 10,103,850.45 USD | `4,500.00` | `2467.33` | `2246.30` | `2463.35` | 999,158.06 USD | `+9.89%` | `20X Cross` |
| `221` | `0xb829...3a81` | `LONG` | 9,869,212.14 USD | `4,394.91` | `2398.60` | `2246.30` | `1460.46` | -672,429.81 USD | `-6.81%` | `20X Cross` |
| `237` | `0x28bb...fca6` | `SHORT` | 9,449,320.99 USD | `4,209.61` | `1896.10` | `2246.30` | `3036.91` | -1,467,438.43 USD | `-15.53%` | `20X Cross` |
| `238` | `0x6ea4...0ea7` | `SHORT` | 9,395,199.62 USD | `4,184.01` | `2602.13` | `2246.30` | `3425.29` | 1,492,147.05 USD | `+15.88%` | `20X Cross` |
| `249` | `0x5e9e...35ee` | `SHORT` | 8,994,477.86 USD | `4,007.56` | `1796.39` | `2246.30` | `2585.78` | -1,795,327.77 USD | `-19.96%` | `20X Cross` |
| `250` | `0xfb94...0ddf` | `SHORT` | 8,985,918.05 USD | `4,002.10` | `2382.44` | `2246.30` | `5104.68` | 548,866.10 USD | `+6.11%` | `20X Cross` |
| `251` | `0x3dc9...54b0` | `SHORT` | 8,979,304.50 USD | `3,999.69` | `2480.32` | `2246.30` | `6545.91` | 941,232.05 USD | `+10.48%` | `20X Cross` |
| `252` | `0x8cc9...2b6a` | `SHORT` | 8,978,000.00 USD | `4,000.00` | `1791.18` | `2246.30` | `3553.63` | -1,813,253.33 USD | `-20.20%` | `25X Cross` |
| `258` | `0x0622...8088` | `LONG` | 8,863,021.88 USD | `3,946.84` | `2209.72` | `2246.30` | `0.000000` | 141,612.44 USD | `+1.60%` | `5X Cross` |
| `272` | `0x4b67...f4e7` | `LONG` | 8,578,936.32 USD | `3,820.84` | `2591.51` | `2246.30` | `1334.47` | -1,322,837.22 USD | `-15.42%` | `20X Cross` |
| `278` | `0x12d2...f97f` | `LONG` | 8,433,924.22 USD | `3,757.26` | `2446.50` | `2246.30` | `1781.45` | -758,242.17 USD | `-8.99%` | `20X Cross` |
| `297` | `0x8ae4...3d60` | `LONG` | 7,985,308.62 USD | `3,558.20` | `2482.21` | `2246.30` | `504.15` | -846,889.41 USD | `-10.61%` | `10X Cross` |
| `337` | `0xb823...9763` | `SHORT` | 6,736,500.00 USD | `3,000.00` | `2229.66` | `2246.30` | `3233.68` | -47,503.32 USD | `-0.71%` | `25X Cross` |
| `338` | `0x469e...58a5` | `SHORT` | 6,733,500.00 USD | `3,000.00` | `2195.70` | `2246.30` | `3218.25` | -146,392.76 USD | `-2.17%` | `25X Cross` |
| `339` | `0x007d...67a0` | `LONG` | 6,733,200.00 USD | `3,000.00` | `2400.00` | `2246.30` | `1472.50` | -466,800.00 USD | `-6.93%` | `25X Cross` |
| `340` | `0x4a20...3c26` | `LONG` | 6,732,900.00 USD | `3,000.00` | `2428.72` | `2246.30` | `572.71` | -553,260.28 USD | `-8.22%` | `20X Cross` |
| `365` | `0x9c2a...f6a8` | `SHORT` | 6,338,555.00 USD | `2,823.41` | `2533.78` | `2246.30` | `2624.42` | 815,355.82 USD | `+12.86%` | `20X Cross` |
| `391` | `0x8328...f54a` | `SHORT` | 5,784,905.65 USD | `2,576.45` | `2292.01` | `2246.30` | `3279.52` | 120,365.63 USD | `+2.08%` | `25X Cross` |
| `393` | `0xed48...7c9b` | `SHORT` | 5,725,502.18 USD | `2,551.13` | `2460.02` | `2246.30` | `3240.37` | 550,344.23 USD | `+9.61%` | `20X Cross` |
| `397` | `0x1c98...7fc7` | `LONG` | 5,613,760.10 USD | `2,500.00` | `2452.60` | `2246.30` | `1916.93` | -517,761.46 USD | `-9.22%` | `10X Cross` |
| `398` | `0x970c...2a93` | `SHORT` | 5,611,250.00 USD | `2,500.00` | `2229.57` | `2246.30` | `5058.12` | -37,305.51 USD | `-0.66%` | `20X Cross` |
| `411` | `0xa445...329d` | `LONG` | 5,400,331.19 USD | `2,406.14` | `2354.86` | `2246.30` | `1710.62` | -265,784.09 USD | `-4.92%` | `25X Cross` |
| `414` | `0x6749...ce07` | `SHORT` | 5,353,467.41 USD | `2,384.89` | `2220.92` | `2246.30` | `3630.13` | -56,804.38 USD | `-1.06%` | `20X Cross` |
| `415` | `0xfbe2...c8ea` | `SHORT` | 5,353,356.35 USD | `2,385.21` | `2041.57` | `2246.30` | `2622.97` | -483,789.69 USD | `-9.04%` | `20X Cross` |
| `418` | `0x645b...87b8` | `SHORT` | 5,341,855.23 USD | `2,379.98` | `2421.64` | `2246.30` | `11385.37` | 421,591.72 USD | `+7.89%` | `10X Cross` |
| `426` | `0x77ee...2902` | `SHORT` | 5,143,747.09 USD | `2,290.69` | `2476.53` | `2246.30` | `5892.88` | 529,225.15 USD | `+10.29%` | `25X Cross` |
| `432` | `0xbcd4...0dd2` | `SHORT` | 5,081,556.83 USD | `2,263.50` | `2233.24` | `2246.30` | `2685.06` | -26,599.26 USD | `-0.52%` | `25X Cross` |
| `453` | `0xd507...c948` | `SHORT` | 4,875,488.18 USD | `2,172.00` | `2387.49` | `2246.30` | `2600.53` | 310,152.85 USD | `+6.36%` | `5X Isolated` |
| `460` | `0x382b...3e39` | `SHORT` | 4,782,098.62 USD | `2,129.54` | `2296.66` | `2246.30` | `4657.66` | 108,738.60 USD | `+2.27%` | `25X Cross` |
| `464` | `0x023a...2355` | `LONG` | 4,766,281.49 USD | `2,123.54` | `2330.15` | `2246.30` | `0.000000` | -181,892.33 USD | `-3.82%` | `25X Cross` |
| `497` | `0x7a6d...f79c` | `SHORT` | 4,490,600.00 USD | `2,000.00` | `2418.41` | `2246.30` | `2510.13` | 346,232.11 USD | `+7.71%` | `25X Cross` |
| `498` | `0x3453...b323` | `SHORT` | 4,490,276.36 USD | `2,000.12` | `2322.47` | `2246.30` | `2380.95` | 154,959.48 USD | `+3.45%` | `25X Cross` |
| `500` | `0xe02e...d78b` | `LONG` | 4,489,000.00 USD | `2,000.00` | `2228.11` | `2246.30` | `2171.88` | 32,776.53 USD | `+0.73%` | `25X Cross` |
| `506` | `0xf3dc...1672` | `SHORT` | 4,445,911.12 USD | `1,980.36` | `2240.44` | `2246.30` | `2766.69` | -9,023.56 USD | `-0.20%` | `20X Cross` |
| `508` | `0xac48...3201` | `SHORT` | 4,410,009.53 USD | `1,964.37` | `2272.04` | `2246.30` | `3140.76` | 53,132.77 USD | `+1.20%` | `20X Cross` |
| `521` | `0x8376...9a1e` | `SHORT` | 4,289,636.67 USD | `1,910.50` | `2477.72` | `2246.30` | `3180.77` | 444,051.50 USD | `+10.35%` | `20X Cross` |
| `554` | `0x7265...91a5` | `LONG` | 4,045,737.36 USD | `1,801.87` | `2533.96` | `2246.30` | `1987.40` | -520,129.09 USD | `-12.86%` | `20X Cross` |
| `555` | `0x739c...cfb2` | `SHORT` | 4,041,000.00 USD | `1,800.00` | `2427.60` | `2246.30` | `2502.52` | 328,696.38 USD | `+8.13%` | `25X Cross` |
| `564` | `0x91a9...3f70` | `SHORT` | 3,967,992.60 USD | `1,767.48` | `2156.23` | `2246.30` | `3659.99` | -156,888.52 USD | `-3.95%` | `4X Cross` |
| `573` | `0xbb34...1696` | `LONG` | 3,929,275.00 USD | `1,750.00` | `2315.81` | `2246.30` | `1950.44` | -123,393.23 USD | `-3.14%` | `25X Cross` |
| `574` | `0xc619...10f5` | `LONG` | 3,927,875.00 USD | `1,750.00` | `2315.39` | `2246.30` | `1780.19` | -124,070.83 USD | `-3.16%` | `25X Cross` |
| `598` | `0xfeec...4e9c` | `SHORT` | 3,797,670.89 USD | `1,691.81` | `2566.49` | `2246.30` | `2509.11` | 544,353.63 USD | `+14.33%` | `10X Cross` |
| `613` | `0xeee0...0b53` | `LONG` | 3,675,834.29 USD | `1,637.12` | `2468.64` | `2246.30` | `176.51` | -365,641.77 USD | `-9.95%` | `7X Cross` |
| `619` | `0x27b8...12fc` | `LONG` | 3,655,943.68 USD | `1,628.12` | `2468.73` | `2246.30` | `601.82` | -363,450.95 USD | `-9.94%` | `10X Cross` |
| `620` | `0x982b...4606` | `LONG` | 3,652,692.88 USD | `1,626.82` | `2575.24` | `2246.30` | `1547.68` | -536,760.19 USD | `-14.69%` | `5X Isolated` |
| `628` | `0x73d7...8be1` | `LONG` | 3,594,008.88 USD | `1,601.47` | `2410.40` | `2246.30` | `1764.41` | -266,170.05 USD | `-7.41%` | `25X Cross` |
| `629` | `0xad54...6203` | `LONG` | 3,586,758.30 USD | `1,597.45` | `2591.98` | `2246.30` | `2052.04` | -553,819.74 USD | `-15.44%` | `10X Isolated` |
| `635` | `0x880a...311c` | `LONG` | 3,544,454.37 USD | `1,578.40` | `2209.72` | `2246.30` | `0.000000` | 56,630.51 USD | `+1.60%` | `9X Cross` |
| `651` | `0xe170...9300` | `SHORT` | 3,441,716.30 USD | `1,533.40` | `2076.39` | `2246.30` | `3156.13` | -257,766.80 USD | `-7.49%` | `25X Cross` |
| `658` | `0x4b86...df9d` | `SHORT` | 3,421,837.20 USD | `1,524.00` | `2287.40` | `2246.30` | `2759.88` | 64,160.40 USD | `+1.88%` | `9X Isolated` |
| `665` | `0x2e2b...2fab` | `LONG` | 3,384,061.37 USD | `1,507.38` | `2245.53` | `2246.30` | `1225.71` | -811.73 USD | `-0.02%` | `25X Cross` |
| `667` | `0xde6b...3361` | `LONG` | 3,368,250.00 USD | `1,500.00` | `2216.98` | `2246.30` | `2168.81` | 42,769.26 USD | `+1.27%` | `25X Cross` |
| `668` | `0xf929...d1f9` | `SHORT` | 3,367,950.00 USD | `1,500.00` | `2423.37` | `2246.30` | `2677.92` | 267,105.26 USD | `+7.93%` | `25X Cross` |
| `669` | `0x251f...6e5d` | `LONG` | 3,367,050.00 USD | `1,500.00` | `2346.68` | `2246.30` | `1856.11` | -152,980.49 USD | `-4.54%` | `20X Cross` |
| `680` | `0xd911...961e` | `LONG` | 3,329,629.27 USD | `1,482.73` | `2212.07` | `2246.30` | `698.68` | 49,709.62 USD | `+1.49%` | `25X Cross` |
| `693` | `0xb885...3c54` | `LONG` | 3,254,355.94 USD | `1,450.00` | `2274.34` | `2246.30` | `32.56` | -43,452.20 USD | `-1.34%` | `20X Cross` |
| `695` | `0x3440...32c5` | `SHORT` | 3,252,571.24 USD | `1,448.97` | `2198.21` | `2246.30` | `3813.83` | -67,420.28 USD | `-2.07%` | `25X Cross` |
| `697` | `0xef70...a84c` | `SHORT` | 3,238,958.93 USD | `1,442.74` | `2424.73` | `2246.30` | `3267.36` | 259,311.89 USD | `+8.01%` | `25X Cross` |
| `703` | `0x4b5f...0dd8` | `LONG` | 3,214,743.02 USD | `1,431.96` | `2339.45` | `2246.30` | `2147.97` | -135,249.93 USD | `-4.21%` | `10X Cross` |
| `709` | `0xbadb...9ee6` | `LONG` | 3,206,647.65 USD | `1,428.16` | `1936.00` | `2246.30` | `1067.99` | 441,726.00 USD | `+13.78%` | `20X Cross` |
| `764` | `0x53f8...ceff` | `LONG` | 3,027,728.90 USD | `1,348.65` | `2276.73` | `2246.30` | `0.000000` | -42,795.56 USD | `-1.41%` | `20X Cross` |
| `781` | `0x0dd5...f6ee` | `LONG` | 2,952,569.50 USD | `1,315.00` | `2306.05` | `2246.30` | `1560.29` | -79,894.88 USD | `-2.71%` | `5X Cross` |
| `807` | `0x1f16...6d07` | `LONG` | 2,841,537.00 USD | `1,266.00` | `2261.43` | `2246.30` | `1390.05` | -21,434.23 USD | `-0.75%` | `7X Cross` |
| `817` | `0xc435...c905` | `SHORT` | 2,802,134.40 USD | `1,248.00` | `2704.38` | `2246.30` | `4239.84` | 572,935.95 USD | `+20.45%` | `20X Cross` |
| `819` | `0x6859...7e1e` | `SHORT` | 2,777,039.13 USD | `1,237.15` | `2200.39` | `2246.30` | `4688.82` | -54,811.98 USD | `-1.97%` | `25X Cross` |
| `835` | `0x7277...0b98` | `SHORT` | 2,737,064.28 USD | `1,219.45` | `2206.05` | `2246.30` | `3359.30` | -46,876.48 USD | `-1.71%` | `20X Cross` |
| `836` | `0x7178...0854` | `LONG` | 2,735,218.40 USD | `1,218.63` | `2461.81` | `2246.30` | `1166.24` | -264,828.00 USD | `-9.68%` | `10X Cross` |
| `848` | `0xaaa1...ab8c` | `SHORT` | 2,694,360.00 USD | `1,200.00` | `2276.29` | `2246.30` | `2365.50` | 37,197.58 USD | `+1.38%` | `25X Isolated` |
| `860` | `0x07fd...689d` | `LONG` | 2,664,332.02 USD | `1,186.89` | `2416.34` | `2246.30` | `0.000000` | -203,610.33 USD | `-7.64%` | `25X Cross` |
| `877` | `0x6e6f...82a6` | `LONG` | 2,599,157.51 USD | `1,157.75` | `2266.07` | `2246.30` | `1393.41` | -24,405.42 USD | `-0.94%` | `20X Cross` |
| `879` | `0x0a97...347d` | `LONG` | 2,588,326.41 USD | `1,153.06` | `2267.88` | `2246.30` | `1525.39` | -26,684.28 USD | `-1.03%` | `20X Cross` |
| `885` | `0xa70a...4be9` | `LONG` | 2,568,224.28 USD | `1,144.29` | `2259.47` | `2246.30` | `991.80` | -17,273.21 USD | `-0.67%` | `20X Cross` |
| `926` | `0x2f80...f203` | `SHORT` | 2,445,217.24 USD | `1,088.94` | `1984.00` | `2246.30` | `2963.42` | -284,750.05 USD | `-11.65%` | `20X Cross` |
| `933` | `0x6f11...0389` | `SHORT` | 2,422,355.00 USD | `1,079.00` | `2333.39` | `2246.30` | `3198.98` | 95,373.91 USD | `+3.94%` | `25X Cross` |
| `935` | `0x8eb7...b90f` | `LONG` | 2,419,847.83 USD | `1,077.74` | `2396.38` | `2246.30` | `1881.22` | -162,830.22 USD | `-6.73%` | `5X Isolated` |
| `936` | `0x2b61...2f6c` | `SHORT` | 2,417,499.01 USD | `1,076.60` | `2681.75` | `2246.30` | `6442.16` | 469,673.73 USD | `+19.43%` | `10X Cross` |
| `956` | `0xb8eb...1dd5` | `LONG` | 2,342,189.33 USD | `1,043.41` | `2226.79` | `2246.30` | `377.35` | 18,725.34 USD | `+0.80%` | `25X Cross` |
| `960` | `0x30af...393e` | `SHORT` | 2,337,415.20 USD | `1,041.16` | `2252.26` | `2246.30` | `2297.19` | 7,567.13 USD | `+0.32%` | `25X Cross` |
| `974` | `0x1b2a...f7a6` | `LONG` | 2,302,258.77 USD | `1,025.37` | `2737.51` | `2246.30` | `882.35` | -504,701.17 USD | `-21.92%` | `10X Cross` |
| `984` | `0x001a...fef6` | `SHORT` | 2,260,940.96 USD | `1,007.33` | `2022.19` | `2246.30` | `3079.39` | -223,933.01 USD | `-9.90%` | `10X Cross` |
| `985` | `0x02aa...1806` | `SHORT` | 2,260,939.72 USD | `1,007.10` | `2654.68` | `2246.30` | `3612.98` | 412,592.38 USD | `+18.25%` | `20X Cross` |
| `986` | `0xdb3a...cf3b` | `LONG` | 2,252,217.90 USD | `1,003.22` | `2705.01` | `2246.30` | `0.000000` | -461,488.99 USD | `-20.49%` | `4X Cross` |
| `990` | `0x834c...dd93` | `SHORT` | 2,245,300.00 USD | `1,000.00` | `2191.89` | `2246.30` | `2262.27` | -53,407.36 USD | `-2.38%` | `25X Cross` |
| `991` | `0x8c02...b73f` | `SHORT` | 2,245,000.00 USD | `1,000.00` | `2250.37` | `2246.30` | `8098.66` | 5,371.47 USD | `+0.24%` | `20X Cross` |
| `992` | `0x5272...fcd9` | `SHORT` | 2,244,500.00 USD | `1,000.00` | `2241.82` | `2246.30` | `2831.03` | -2,675.51 USD | `-0.12%` | `5X Cross` |
| `994` | `0xd7b8...9f55` | `LONG` | 2,243,054.70 USD | `999.00` | `2195.00` | `2246.30` | `0.000000` | 50,249.70 USD | `+2.24%` | `15X Cross` |
| `1017` | `0xb002...ed8a` | `SHORT` | 2,161,738.92 USD | `962.78` | `2299.66` | `2246.30` | `4199.33` | 52,338.99 USD | `+2.42%` | `25X Cross` |
| `1031` | `0xb812...b5e0` | `LONG` | 2,112,961.61 USD | `940.98` | `2263.21` | `2246.30` | `1184.98` | -16,668.86 USD | `-0.79%` | `25X Cross` |
| `1040` | `0xb1ec...e86a` | `SHORT` | 2,096,018.21 USD | `933.64` | `2272.72` | `2246.30` | `12533.18` | 25,888.75 USD | `+1.24%` | `25X Cross` |
| `1048` | `0x4487...c92d` | `LONG` | 2,088,079.69 USD | `929.85` | `2227.19` | `2246.30` | `1547.98` | 17,117.69 USD | `+0.82%` | `10X Cross` |
| `1059` | `0xef96...9383` | `LONG` | 2,059,772.14 USD | `917.57` | `2235.00` | `2246.30` | `0.000000` | 8,988.48 USD | `+0.44%` | `25X Cross` |
| `1064` | `0xede2...f971` | `LONG` | 2,052,082.53 USD | `914.31` | `2208.16` | `2246.30` | `1463.26` | 33,125.54 USD | `+1.61%` | `5X Cross` |
| `1066` | `0x9606...4e5d` | `SHORT` | 2,049,221.09 USD | `913.00` | `2478.70` | `2246.30` | `4303.08` | 213,832.51 USD | `+10.43%` | `20X Cross` |
| `1086` | `0x5f10...d49d` | `LONG` | 2,020,050.00 USD | `900.00` | `2249.83` | `2246.30` | `1804.58` | -4,803.47 USD | `-0.24%` | `25X Cross` |
| `1102` | `0x82f6...12ec` | `SHORT` | 1,991,619.27 USD | `887.02` | `2199.66` | `2246.30` | `2249.55` | -40,476.45 USD | `-2.03%` | `25X Cross` |
| `1138` | `0xa0fb...96be` | `LONG` | 1,949,875.88 USD | `868.35` | `2293.96` | `2246.30` | `1122.07` | -42,082.79 USD | `-2.16%` | `3X Cross` |
| `1165` | `0x24fb...ed0f` | `LONG` | 1,908,465.52 USD | `850.10` | `2199.85` | `2246.30` | `0.000000` | 38,378.65 USD | `+2.01%` | `15X Cross` |
| `1183` | `0xcd27...52a8` | `LONG` | 1,879,532.63 USD | `837.21` | `2553.56` | `2246.30` | `1403.49` | -258,332.14 USD | `-13.74%` | `2X Cross` |
| `1188` | `0xbef3...0d3e` | `LONG` | 1,857,597.31 USD | `827.33` | `2227.10` | `2246.30` | `2133.02` | 15,052.82 USD | `+0.81%` | `20X Cross` |
| `1191` | `0x6a41...a3b9` | `LONG` | 1,853,466.55 USD | `825.69` | `2226.70` | `2246.30` | `2136.78` | 14,894.11 USD | `+0.80%` | `20X Cross` |
| `1230` | `0xb15b...dbae` | `SHORT` | 1,803,015.83 USD | `803.30` | `2290.80` | `2246.30` | `2270.18` | 37,193.52 USD | `+2.06%` | `25X Cross` |
| `1239` | `0x04a9...95aa` | `LONG` | 1,796,000.00 USD | `800.00` | `2595.13` | `2246.30` | `1863.02` | -280,106.74 USD | `-15.60%` | `5X Cross` |
| `1242` | `0x7737...bf66` | `SHORT` | 1,795,132.92 USD | `799.79` | `2494.83` | `2246.30` | `24035.18` | 200,213.11 USD | `+11.15%` | `15X Cross` |
| `1271` | `0x458d...ab3b` | `LONG` | 1,739,539.44 USD | `774.75` | `2740.41` | `2246.30` | `1887.25` | -383,589.74 USD | `-22.05%` | `3X Isolated` |
| `1323` | `0x2e30...4cb5` | `SHORT` | 1,646,432.77 USD | `733.54` | `2335.09` | `2246.30` | `8930.80` | 66,456.19 USD | `+4.04%` | `2X Cross` |
| `1330` | `0xaa53...9cb7` | `LONG` | 1,639,240.72 USD | `730.34` | `2389.70` | `2246.30` | `1952.45` | -106,048.91 USD | `-6.47%` | `20X Cross` |
| `1331` | `0x3fc5...c0c1` | `SHORT` | 1,638,679.83 USD | `729.92` | `2702.11` | `2246.30` | `4577.20` | 333,662.37 USD | `+20.36%` | `25X Cross` |
| `1339` | `0x6463...42f5` | `LONG` | 1,631,194.77 USD | `726.88` | `2214.40` | `2246.30` | `0.000000` | 21,584.11 USD | `+1.32%` | `1X Cross` |
| `1347` | `0xa189...94d7` | `SHORT` | 1,615,920.87 USD | `719.98` | `2691.84` | `2246.30` | `2915.10` | 322,151.79 USD | `+19.94%` | `25X Cross` |
| `1367` | `0x2f93...4404` | `LONG` | 1,587,834.89 USD | `707.47` | `1700.45` | `2246.30` | `1368.88` | 384,808.51 USD | `+24.23%` | `4X Isolated` |
| `1374` | `0x5605...fe0f` | `SHORT` | 1,575,680.45 USD | `702.14` | `2566.90` | `2246.30` | `3076.86` | 226,652.20 USD | `+14.38%` | `20X Cross` |
| `1379` | `0x7743...e4fe` | `SHORT` | 1,572,748.67 USD | `700.56` | `2298.56` | `2246.30` | `6178.21` | 37,526.42 USD | `+2.39%` | `25X Cross` |
| `1381` | `0x0deb...0bc5` | `LONG` | 1,571,318.00 USD | `700.00` | `2071.05` | `2246.30` | `1597.47` | 121,582.21 USD | `+7.74%` | `20X Cross` |
| `1413` | `0x51f6...2b39` | `LONG` | 1,551,805.10 USD | `691.38` | `2223.60` | `2246.30` | `378.19` | 14,444.08 USD | `+0.93%` | `25X Cross` |
| `1437` | `0x248e...6be2` | `SHORT` | 1,528,139.29 USD | `680.93` | `2282.89` | `2246.30` | `3442.37` | 26,346.37 USD | `+1.72%` | `20X Cross` |
| `1438` | `0xdbd1...29dd` | `SHORT` | 1,527,836.76 USD | `680.70` | `3030.57` | `2246.30` | `3786.43` | 535,084.36 USD | `+35.02%` | `6X Cross` |
| `1443` | `0x71e5...be04` | `LONG` | 1,521,185.77 USD | `677.67` | `2727.27` | `2246.30` | `1471.03` | -326,999.83 USD | `-21.50%` | `20X Cross` |
| `1451` | `0x0b23...f37b` | `LONG` | 1,515,712.50 USD | `675.00` | `2238.15` | `2246.30` | `594.77` | 4,955.86 USD | `+0.33%` | `5X Cross` |
| `1475` | `0x0cac...6170` | `SHORT` | 1,475,561.50 USD | `657.50` | `2146.55` | `2246.30` | `2839.47` | -64,199.30 USD | `-4.35%` | `20X Cross` |
| `1505` | `0xf00e...fe3d` | `SHORT` | 1,443,098.45 USD | `642.88` | `2333.21` | `2246.30` | `2495.93` | 56,879.52 USD | `+3.94%` | `20X Cross` |
| `1513` | `0xffb2...5ed6` | `SHORT` | 1,437,944.78 USD | `640.77` | `2672.96` | `2246.30` | `2499.81` | 274,803.57 USD | `+19.11%` | `20X Cross` |
| `1524` | `0x8505...1821` | `SHORT` | 1,423,240.87 USD | `633.96` | `2239.93` | `2246.30` | `3887.93` | -3,209.27 USD | `-0.23%` | `20X Cross` |
| `1540` | `0xfce0...f4c0` | `SHORT` | 1,399,982.00 USD | `623.60` | `3129.61` | `2246.30` | `2798.05` | 551,644.58 USD | `+39.40%` | `20X Cross` |
| `1581` | `0x9599...c60a` | `LONG` | 1,365,767.29 USD | `608.44` | `2231.08` | `2246.30` | `0.000000` | 8,286.81 USD | `+0.61%` | `20X Cross` |
| `1591` | `0xad02...eb65` | `LONG` | 1,348,392.35 USD | `600.62` | `2460.69` | `2246.30` | `1078.95` | -129,548.21 USD | `-9.61%` | `5X Cross` |
| `1592` | `0x26e6...6b28` | `LONG` | 1,347,000.00 USD | `600.00` | `1769.78` | `2246.30` | `2004.75` | 285,128.47 USD | `+21.17%` | `20X Cross` |
| `1593` | `0x638f...f5f0` | `LONG` | 1,346,520.00 USD | `600.00` | `4011.50` | `2246.30` | `367.33` | -1,060,383.53 USD | `-78.75%` | `25X Cross` |
| `1602` | `0x7c90...d129` | `LONG` | 1,333,736.77 USD | `594.17` | `2286.01` | `2246.30` | `1855.42` | -24,546.12 USD | `-1.84%` | `20X Cross` |
| `1641` | `0x31de...13f2` | `LONG` | 1,291,505.64 USD | `575.13` | `2252.09` | `2246.30` | `0.000000` | -3,736.89 USD | `-0.29%` | `20X Cross` |
| `1660` | `0xfc66...ca06` | `SHORT` | 1,274,170.58 USD | `567.43` | `2275.19` | `2246.30` | `7327.97` | 16,852.63 USD | `+1.32%` | `20X Cross` |
| `1665` | `0xfb99...37f3` | `LONG` | 1,269,360.37 USD | `565.34` | `2362.35` | `2246.30` | `1245.44` | -66,175.98 USD | `-5.21%` | `3X Cross` |
| `1680` | `0x844b...7f42` | `SHORT` | 1,259,332.80 USD | `561.00` | `2026.17` | `2246.30` | `3016.25` | -122,649.39 USD | `-9.74%` | `25X Cross` |
| `1692` | `0xabe6...1d99` | `SHORT` | 1,248,062.18 USD | `556.00` | `2484.68` | `2246.30` | `3106.66` | 133,433.71 USD | `+10.69%` | `20X Cross` |
| `1696` | `0x2a76...9a53` | `LONG` | 1,245,952.55 USD | `554.99` | `2231.40` | `2246.30` | `0.000000` | 7,545.49 USD | `+0.61%` | `25X Cross` |
| `1705` | `0x936c...bb0f` | `LONG` | 1,235,278.96 USD | `550.09` | `2218.31` | `2246.30` | `0.000000` | 15,011.69 USD | `+1.22%` | `20X Cross` |
| `1707` | `0x825c...465e` | `LONG` | 1,234,585.00 USD | `550.00` | `2208.12` | `2246.30` | `1189.54` | 20,115.50 USD | `+1.63%` | `4X Cross` |
| `1713` | `0xad21...fb6a` | `LONG` | 1,228,206.42 USD | `547.26` | `2565.80` | `2246.30` | `1733.41` | -175,946.58 USD | `-14.33%` | `6X Cross` |
| `1823` | `0x0c7a...2f50` | `SHORT` | 1,143,001.08 USD | `509.25` | `2122.56` | `2246.30` | `4110.42` | -62,095.64 USD | `-5.43%` | `20X Cross` |
| `1830` | `0x0089...2410` | `SHORT` | 1,138,737.20 USD | `507.35` | `2308.88` | `2246.30` | `3391.50` | 32,663.06 USD | `+2.87%` | `20X Cross` |
| `1843` | `0xa559...ff95` | `LONG` | 1,122,650.00 USD | `500.00` | `2260.68` | `2246.30` | `1045.80` | -7,694.36 USD | `-0.69%` | `20X Cross` |
| `1844` | `0x4044...794c` | `LONG` | 1,122,650.00 USD | `500.00` | `2260.80` | `2246.30` | `0.000000` | -7,750.00 USD | `-0.69%` | `25X Cross` |
| `1845` | `0xe282...df29` | `LONG` | 1,122,500.00 USD | `500.00` | `2309.84` | `2246.30` | `2045.39` | -32,424.21 USD | `-2.89%` | `10X Isolated` |
| `1846` | `0x6936...9417` | `SHORT` | 1,122,500.00 USD | `500.00` | `2315.11` | `2246.30` | `2358.98` | 35,055.21 USD | `+3.12%` | `25X Isolated` |
| `1847` | `0xb322...d51f` | `SHORT` | 1,122,350.00 USD | `500.00` | `2268.03` | `2246.30` | `3760.49` | 11,666.32 USD | `+1.04%` | `20X Cross` |
| `1848` | `0x89b2...9ca6` | `LONG` | 1,122,000.00 USD | `500.00` | `2363.45` | `2246.30` | `1622.73` | -59,727.42 USD | `-5.32%` | `25X Cross` |
| `1854` | `0x7298...7d6c` | `SHORT` | 1,118,494.62 USD | `498.15` | `3426.75` | `2246.30` | `5421.69` | 588,541.20 USD | `+52.62%` | `20X Cross` |
| `1864` | `0x9c68...7783` | `SHORT` | 1,107,229.36 USD | `493.31` | `2273.58` | `2246.30` | `3883.72` | 14,349.89 USD | `+1.30%` | `25X Cross` |
| `1865` | `0x34fb...93de` | `LONG` | 1,106,997.26 USD | `492.96` | `2219.83` | `2246.30` | `0.000000` | 12,701.31 USD | `+1.15%` | `20X Cross` |
| `1872` | `0x404c...5f03` | `SHORT` | 1,099,323.11 USD | `489.79` | `2671.94` | `2246.30` | `5016.94` | 209,356.45 USD | `+19.04%` | `20X Cross` |
| `1878` | `0x321f...1c84` | `SHORT` | 1,095,350.57 USD | `488.02` | `2370.09` | `2246.30` | `3050.51` | 61,294.03 USD | `+5.60%` | `10X Cross` |
| `1895` | `0x71d0...8c26` | `LONG` | 1,079,153.03 USD | `480.73` | `2225.97` | `2246.30` | `0.000000` | 9,048.27 USD | `+0.84%` | `25X Cross` |
| `1932` | `0xe86b...3664` | `LONG` | 1,049,426.28 USD | `467.39` | `2231.29` | `2246.30` | `0.000000` | 6,545.34 USD | `+0.62%` | `25X Cross` |
| `1946` | `0x94b6...e5b3` | `SHORT` | 1,041,500.37 USD | `463.86` | `2261.12` | `2246.30` | `2432.23` | 7,342.30 USD | `+0.70%` | `25X Cross` |
| `1949` | `0x82c6...fe42` | `LONG` | 1,038,312.50 USD | `462.50` | `2501.38` | `2246.30` | `2053.73` | -118,578.07 USD | `-11.42%` | `5X Isolated` |
| `1958` | `0xe330...77a1` | `SHORT` | 1,035,304.00 USD | `461.20` | `2206.97` | `2246.30` | `6429.84` | -17,446.64 USD | `-1.69%` | `20X Cross` |
| `1962` | `0x2de3...486d` | `LONG` | 1,033,367.80 USD | `460.40` | `2286.27` | `2246.30` | `1180.62` | -19,233.11 USD | `-1.86%` | `25X Cross` |
| `1972` | `0x9362...7d7c` | `SHORT` | 1,028,222.16 USD | `458.19` | `2221.70` | `2246.30` | `2594.60` | -10,263.09 USD | `-1.00%` | `20X Cross` |
| `1975` | `0x617e...0f97` | `SHORT` | 1,027,654.20 USD | `457.85` | `2205.60` | `2246.30` | `3369.68` | -17,810.37 USD | `-1.73%` | `10X Cross` |
| `2005` | `0xc10f...23b3` | `LONG` | 1,010,160.00 USD | `450.00` | `2366.44` | `2246.30` | `2016.80` | -54,738.27 USD | `-5.42%` | `25X Cross` |
| `2006` | `0x0514...bdfe` | `SHORT` | 1,009,971.00 USD | `450.00` | `1988.74` | `2246.30` | `3827.96` | -115,034.16 USD | `-11.39%` | `25X Cross` |
| `2007` | `0xae55...2236` | `LONG` | 1,009,890.00 USD | `450.00` | `2510.21` | `2246.30` | `0.000000` | -119,707.50 USD | `-11.85%` | `25X Cross` |
| `2014` | `0xaa7a...af37` | `LONG` | 1,005,519.12 USD | `448.03` | `2212.37` | `2246.30` | `0.000000` | 14,302.88 USD | `+1.42%` | `20X Cross` |
| `2020` | `0xac26...a9c7` | `SHORT` | 1,001,307.41 USD | `446.14` | `2192.58` | `2246.30` | `8572.26` | -23,116.87 USD | `-2.31%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `ANNOUNCEMENT` | `INFO` | `2308.10` | 108,950.17 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 108.95K USD at 2308.1000 USD [API] | `2026-10-29 02:18:56` |
| `ANNOUNCEMENT` | `INFO` | `2300.40` | 41,119.19 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 41.12K USD at 2300.4000 USD [API] | `2026-10-29 02:34:40` |
| `ANNOUNCEMENT` | `INFO` | `2298.30` | 19.08 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2298.3000 USD [API] | `2026-10-29 02:30:54` |
| `ANNOUNCEMENT` | `INFO` | `2298.30` | 29.42 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.03K USD at 2298.3000 USD [API] | `2026-10-29 02:30:54` |
| `ANNOUNCEMENT` | `INFO` | `2332.40` | 222.74 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.22K USD at 2332.4000 USD [API] | `2026-10-29 01:39:01` |


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
| `7D` | `Long Liquidation` | `1972.00` | 999,440,000.00 USD | 999,440,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1975.00` | 1,950,000.00 USD | 213,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1975.30` | 999,310,000.00 USD | 999,310,000.00 USD | 0.00 USD | 0.00 USD | 49,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1978.60` | 999,260,000.00 USD | 999,260,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1981.90` | 997,020,000.00 USD | 997,020,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1985.00` | 5,060,000.00 USD | 211,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1985.10` | 647,890,000.00 USD | 647,890,000.00 USD | 1,800,000.00 USD | 1,260,000.00 USD | 20,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1987.60` | 644,810,000.00 USD | 644,810,000.00 USD | 534,990.00 USD | 0.00 USD | 19,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1988.50` | 996,810,000.00 USD | 996,810,000.00 USD | 3,730,000.00 USD | 1,780,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1990.10` | 644,260,000.00 USD | 644,260,000.00 USD | 1,460,000.00 USD | 1,230,000.00 USD | 547,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1991.80` | 991,310,000.00 USD | 991,310,000.00 USD | 1,390,000.00 USD | 1,320,000.00 USD | 38,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1992.60` | 641,020,000.00 USD | 641,020,000.00 USD | 742,220.00 USD | 77,290.00 USD | 256,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1995.00` | 1,560,000.00 USD | 206,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1995.10` | 639,940,000.00 USD | 639,940,000.00 USD | 602,100.00 USD | 580,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1995.10` | 988,560,000.00 USD | 988,560,000.00 USD | 1,340,000.00 USD | 0.00 USD | 808,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1997.60` | 638,760,000.00 USD | 638,760,000.00 USD | 0.00 USD | 0.00 USD | 304,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2000.10` | 638,450,000.00 USD | 638,450,000.00 USD | 0.00 USD | 0.00 USD | 487,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2002.60` | 637,970,000.00 USD | 637,970,000.00 USD | 0.00 USD | 217,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2005.00` | 986,410,000.00 USD | 986,410,000.00 USD | 0.00 USD | 266,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2005.00` | 2,090,000.00 USD | 204,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2005.10` | 637,750,000.00 USD | 637,750,000.00 USD | 14,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2007.60` | 637,730,000.00 USD | 637,730,000.00 USD | 0.00 USD | 224,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2010.10` | 637,510,000.00 USD | 637,510,000.00 USD | 0.00 USD | 308,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2011.60` | 986,140,000.00 USD | 986,140,000.00 USD | 170,840.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2012.60` | 637,200,000.00 USD | 637,200,000.00 USD | 299,090.00 USD | 210,450.00 USD | 17,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2015.00` | 5,730,000.00 USD | 202,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2015.10` | 636,670,000.00 USD | 636,670,000.00 USD | 303,600.00 USD | 51,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2017.60` | 636,320,000.00 USD | 636,320,000.00 USD | 404,950.00 USD | 1,350,000.00 USD | 550,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2020.10` | 634,020,000.00 USD | 634,020,000.00 USD | 510,810.00 USD | 771,060.00 USD | 4,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2022.60` | 632,730,000.00 USD | 632,730,000.00 USD | 751,210.00 USD | 27,630.00 USD | 459,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2024.80` | 985,970,000.00 USD | 985,970,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2025.00` | 2,100,000.00 USD | 196,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2025.10` | 631,490,000.00 USD | 631,490,000.00 USD | 0.00 USD | 914,780.00 USD | 32,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2027.60` | 630,540,000.00 USD | 630,540,000.00 USD | 1,430,000.00 USD | 1,160,000.00 USD | 11,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2028.10` | 985,790,000.00 USD | 985,790,000.00 USD | 0.00 USD | 0.00 USD | 35,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2030.10` | 627,940,000.00 USD | 627,940,000.00 USD | 87,180.00 USD | 366,120.00 USD | 957,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2031.40` | 985,760,000.00 USD | 985,760,000.00 USD | 0.00 USD | 3,520,000.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2032.60` | 626,530,000.00 USD | 626,530,000.00 USD | 1,360,000.00 USD | 1,490,000.00 USD | 707,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2034.70` | 981,190,000.00 USD | 981,190,000.00 USD | 0.00 USD | 186,130.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2035.00` | 1,080,000.00 USD | 194,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2035.10` | 622,970,000.00 USD | 622,970,000.00 USD | 1,150,000.00 USD | 19,490.00 USD | 165,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2037.60` | 621,630,000.00 USD | 621,630,000.00 USD | 396,700.00 USD | 458,110.00 USD | 378,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2038.00` | 979,650,000.00 USD | 979,650,000.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2040.10` | 620,400,000.00 USD | 620,400,000.00 USD | 542,670.00 USD | 178,560.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2042.60` | 619,650,000.00 USD | 619,650,000.00 USD | 626,840.00 USD | 0.00 USD | 174,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2044.60` | 978,050,000.00 USD | 978,050,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2045.00` | 2,000,000.00 USD | 193,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2045.10` | 618,850,000.00 USD | 618,850,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2047.60` | 618,820,000.00 USD | 618,820,000.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2050.10` | 617,990,000.00 USD | 617,990,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2051.20` | 977,750,000.00 USD | 977,750,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2054.50` | 977,530,000.00 USD | 977,530,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2055.00` | 5,940,000.00 USD | 191,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2055.10` | 616,880,000.00 USD | 616,880,000.00 USD | 242,080.00 USD | 88,880.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2057.80` | 975,240,000.00 USD | 975,240,000.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2060.10` | 616,530,000.00 USD | 616,530,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2061.10` | 975,190,000.00 USD | 975,190,000.00 USD | 1,700,000.00 USD | 1,310,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2062.60` | 615,770,000.00 USD | 615,770,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2064.40` | 970,470,000.00 USD | 970,470,000.00 USD | 1,230,000.00 USD | 1,080,000.00 USD | 945,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2065.00` | 13,860,000.00 USD | 185,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2065.10` | 615,690,000.00 USD | 615,690,000.00 USD | 563,140.00 USD | 537,030.00 USD | 510,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2067.60` | 614,080,000.00 USD | 614,080,000.00 USD | 387,410.00 USD | 304,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2067.70` | 967,210,000.00 USD | 967,210,000.00 USD | 292,400.00 USD | 1,180,000.00 USD | 927,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2070.10` | 613,390,000.00 USD | 613,390,000.00 USD | 57,300.00 USD | 319,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2071.00` | 964,810,000.00 USD | 964,810,000.00 USD | 4,230,000.00 USD | 3,040,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2072.60` | 613,010,000.00 USD | 613,010,000.00 USD | 67,060.00 USD | 555,250.00 USD | 428,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2074.30` | 956,310,000.00 USD | 956,310,000.00 USD | 4,000,000.00 USD | 2,720,000.00 USD | 3,720,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 2,720,000.00 USD | 171,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2075.10` | 611,960,000.00 USD | 611,960,000.00 USD | 67,780.00 USD | 224,070.00 USD | 3,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2077.60` | 611,670,000.00 USD | 611,670,000.00 USD | 1,540,000.00 USD | 765,660.00 USD | 510,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2077.60` | 945,870,000.00 USD | 945,870,000.00 USD | 4,430,000.00 USD | 4,400,000.00 USD | 2,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2080.10` | 608,850,000.00 USD | 608,850,000.00 USD | 586,070.00 USD | 922,510.00 USD | 206,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2080.90` | 934,770,000.00 USD | 934,770,000.00 USD | 5,690,000.00 USD | 3,540,000.00 USD | 2,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2082.60` | 607,130,000.00 USD | 607,130,000.00 USD | 858,220.00 USD | 315,330.00 USD | 215,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2084.20` | 922,560,000.00 USD | 922,560,000.00 USD | 1,660,000.00 USD | 1,490,000.00 USD | 3,500,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 13,600,000.00 USD | 169,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2085.10` | 605,740,000.00 USD | 605,740,000.00 USD | 1,410,000.00 USD | 790,900.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2087.50` | 915,910,000.00 USD | 915,910,000.00 USD | 5,220,000.00 USD | 3,230,000.00 USD | 3,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2087.60` | 602,290,000.00 USD | 602,290,000.00 USD | 1,460,000.00 USD | 565,380.00 USD | 682,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2090.10` | 599,580,000.00 USD | 599,580,000.00 USD | 787,350.00 USD | 225,190.00 USD | 269,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2090.80` | 904,410,000.00 USD | 904,410,000.00 USD | 4,410,000.00 USD | 976,840.00 USD | 6,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2092.60` | 598,290,000.00 USD | 598,290,000.00 USD | 773,260.00 USD | 513,660.00 USD | 874,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2094.10` | 892,040,000.00 USD | 892,040,000.00 USD | 5,350,000.00 USD | 1,660,000.00 USD | 2,950,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 1,380,000.00 USD | 155,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2095.10` | 596,130,000.00 USD | 596,130,000.00 USD | 2,100,000.00 USD | 1,170,000.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2097.40` | 882,090,000.00 USD | 882,090,000.00 USD | 2,280,000.00 USD | 3,580,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2097.60` | 591,530,000.00 USD | 591,530,000.00 USD | 175,830.00 USD | 1,280,000.00 USD | 984,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2100.10` | 589,100,000.00 USD | 589,100,000.00 USD | 307,340.00 USD | 928,890.00 USD | 50,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2100.70` | 874,940,000.00 USD | 874,940,000.00 USD | 1,830,000.00 USD | 1,850,000.00 USD | 3,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2102.60` | 587,810,000.00 USD | 587,810,000.00 USD | 211,840.00 USD | 222,480.00 USD | 483,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2104.00` | 867,950,000.00 USD | 867,950,000.00 USD | 1,190,000.00 USD | 738,240.00 USD | 3,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 2,280,000.00 USD | 154,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2105.10` | 586,890,000.00 USD | 586,890,000.00 USD | 3,570,000.00 USD | 1,160,000.00 USD | 691,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2107.30` | 862,990,000.00 USD | 862,990,000.00 USD | 8,720,000.00 USD | 1,150,000.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2107.60` | 581,470,000.00 USD | 581,470,000.00 USD | 734,860.00 USD | 0.00 USD | 488,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2110.10` | 580,240,000.00 USD | 580,240,000.00 USD | 61,010.00 USD | 31,550.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2110.60` | 851,930,000.00 USD | 851,930,000.00 USD | 2,970,000.00 USD | 2,360,000.00 USD | 2,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2112.60` | 580,140,000.00 USD | 580,140,000.00 USD | 902,600.00 USD | 360,140.00 USD | 221,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2113.90` | 844,070,000.00 USD | 844,070,000.00 USD | 1,780,000.00 USD | 1,810,000.00 USD | 3,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 2,910,000.00 USD | 151,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2115.10` | 578,660,000.00 USD | 578,660,000.00 USD | 202,800.00 USD | 411,610.00 USD | 962,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2117.20` | 836,890,000.00 USD | 836,890,000.00 USD | 2,410,000.00 USD | 2,380,000.00 USD | 2,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2117.60` | 577,080,000.00 USD | 577,080,000.00 USD | 4,750,000.00 USD | 4,080,000.00 USD | 302,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2120.10` | 567,950,000.00 USD | 567,950,000.00 USD | 3,950,000.00 USD | 22,470.00 USD | 645,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2120.50` | 829,630,000.00 USD | 829,630,000.00 USD | 13,880,000.00 USD | 5,790,000.00 USD | 2,800,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2122.60` | 563,340,000.00 USD | 563,340,000.00 USD | 4,520,000.00 USD | 3,800,000.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2123.80` | 807,160,000.00 USD | 807,160,000.00 USD | 7,610,000.00 USD | 7,900,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 123,240,000.00 USD | 148,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2125.10` | 553,160,000.00 USD | 553,160,000.00 USD | 6,940,000.00 USD | 1,830,000.00 USD | 2,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2127.10` | 789,830,000.00 USD | 789,830,000.00 USD | 2,760,000.00 USD | 4,420,000.00 USD | 5,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2127.60` | 542,280,000.00 USD | 542,280,000.00 USD | 4,430,000.00 USD | 4,180,000.00 USD | 782,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2130.10` | 532,890,000.00 USD | 532,890,000.00 USD | 1,230,000.00 USD | 172,040.00 USD | 762,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2130.40` | 777,110,000.00 USD | 777,110,000.00 USD | 5,410,000.00 USD | 2,580,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2132.60` | 530,730,000.00 USD | 530,730,000.00 USD | 0.00 USD | 177,810.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2133.70` | 767,420,000.00 USD | 767,420,000.00 USD | 2,550,000.00 USD | 715,940.00 USD | 323,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 4,840,000.00 USD | 25,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2135.10` | 529,020,000.00 USD | 529,020,000.00 USD | 20,600.00 USD | 1,170,000.00 USD | 86,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2137.00` | 763,830,000.00 USD | 763,830,000.00 USD | 746,340.00 USD | 1,510,000.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2137.60` | 527,740,000.00 USD | 527,740,000.00 USD | 21,090.00 USD | 379,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2140.10` | 527,340,000.00 USD | 527,340,000.00 USD | 36,740.00 USD | 265,280.00 USD | 64,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2140.30` | 761,530,000.00 USD | 761,530,000.00 USD | 2,260,000.00 USD | 1,200,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2142.60` | 526,970,000.00 USD | 526,970,000.00 USD | 670,350.00 USD | 2,130,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2143.60` | 757,270,000.00 USD | 757,270,000.00 USD | 1,200,000.00 USD | 1,420,000.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 5,020,000.00 USD | 20,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2145.10` | 524,170,000.00 USD | 524,170,000.00 USD | 121,400.00 USD | 1,690,000.00 USD | 118,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2146.90` | 754,380,000.00 USD | 754,380,000.00 USD | 1,060,000.00 USD | 938,520.00 USD | 134,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2147.60` | 522,240,000.00 USD | 522,240,000.00 USD | 1,450,000.00 USD | 1,100,000.00 USD | 60,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2150.10` | 519,630,000.00 USD | 519,630,000.00 USD | 6,930,000.00 USD | 2,570,000.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2150.20` | 752,250,000.00 USD | 752,250,000.00 USD | 485,890.00 USD | 838,260.00 USD | 331,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2152.60` | 508,440,000.00 USD | 508,440,000.00 USD | 2,240,000.00 USD | 2,180,000.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2153.50` | 750,600,000.00 USD | 750,600,000.00 USD | 11,310,000.00 USD | 311,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 3,970,000.00 USD | 15,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2155.10` | 502,650,000.00 USD | 502,650,000.00 USD | 1,940,000.00 USD | 2,480,000.00 USD | 576,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2156.80` | 738,980,000.00 USD | 738,980,000.00 USD | 2,560,000.00 USD | 2,210,000.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2157.60` | 497,650,000.00 USD | 497,650,000.00 USD | 2,480,000.00 USD | 834,590.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2160.10` | 493,080,000.00 USD | 493,080,000.00 USD | 1,450,000.00 USD | 4,910,000.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2160.10` | 732,160,000.00 USD | 732,160,000.00 USD | 2,190,000.00 USD | 2,550,000.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2162.60` | 485,170,000.00 USD | 485,170,000.00 USD | 14,140,000.00 USD | 9,870,000.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2163.40` | 726,160,000.00 USD | 726,160,000.00 USD | 21,210,000.00 USD | 11,130,000.00 USD | 518,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 5,390,000.00 USD | 11,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2165.10` | 459,590,000.00 USD | 459,590,000.00 USD | 10,390,000.00 USD | 9,640,000.00 USD | 4,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2166.70` | 693,300,000.00 USD | 693,300,000.00 USD | 5,300,000.00 USD | 15,400,000.00 USD | 2,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2167.60` | 435,390,000.00 USD | 435,390,000.00 USD | 17,280,000.00 USD | 7,820,000.00 USD | 5,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2170.00` | 669,630,000.00 USD | 669,630,000.00 USD | 10,280,000.00 USD | 15,310,000.00 USD | 5,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2170.10` | 405,090,000.00 USD | 405,090,000.00 USD | 13,580,000.00 USD | 9,360,000.00 USD | 4,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2172.60` | 377,390,000.00 USD | 377,390,000.00 USD | 16,900,000.00 USD | 5,140,000.00 USD | 4,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2173.30` | 638,550,000.00 USD | 638,550,000.00 USD | 30,550,000.00 USD | 828,350.00 USD | 5,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 5,680,000.00 USD | 6,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2175.10` | 350,720,000.00 USD | 350,720,000.00 USD | 5,700,000.00 USD | 0.00 USD | 2,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2176.60` | 601,620,000.00 USD | 601,620,000.00 USD | 5,390,000.00 USD | 1,330,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2177.60` | 342,700,000.00 USD | 342,700,000.00 USD | 730,100.00 USD | 355,620.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2180.10` | 338,790,000.00 USD | 338,790,000.00 USD | 894,580.00 USD | 1,460,000.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2182.60` | 335,070,000.00 USD | 335,070,000.00 USD | 73,470.00 USD | 26,540.00 USD | 3,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2183.20` | 592,090,000.00 USD | 592,090,000.00 USD | 1,760,000.00 USD | 0.00 USD | 3,950,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2185.00` | 618,490.00 USD | 731,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2185.10` | 331,930,000.00 USD | 331,930,000.00 USD | 310,640.00 USD | 1,660,000.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2186.50` | 586,390,000.00 USD | 586,390,000.00 USD | 37,310,000.00 USD | 19,060,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2187.60` | 326,770,000.00 USD | 326,770,000.00 USD | 3,960,000.00 USD | 1,250,000.00 USD | 5,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2189.80` | 530,020,000.00 USD | 530,020,000.00 USD | 12,430,000.00 USD | 19,940,000.00 USD | 4,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2190.10` | 316,200,000.00 USD | 316,200,000.00 USD | 4,530,000.00 USD | 3,550,000.00 USD | 5,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2192.60` | 303,050,000.00 USD | 303,050,000.00 USD | 4,810,000.00 USD | 5,200,000.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2193.10` | 493,080,000.00 USD | 493,080,000.00 USD | 0.00 USD | 14,900,000.00 USD | 8,080,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 107,420.00 USD | 112,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2195.10` | 291,860,000.00 USD | 291,860,000.00 USD | 5,420,000.00 USD | 1,880,000.00 USD | 4,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2196.40` | 470,090,000.00 USD | 470,090,000.00 USD | 383,690.00 USD | 243,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2197.60` | 280,560,000.00 USD | 280,560,000.00 USD | 4,050,000.00 USD | 0.00 USD | 2,750,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2199.70` | 469,470,000.00 USD | 469,470,000.00 USD | 0.00 USD | 0.00 USD | 7,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2200.10` | 273,760,000.00 USD | 273,760,000.00 USD | 4,340,000.00 USD | 1,680,000.00 USD | 6,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2202.60` | 261,160,000.00 USD | 261,160,000.00 USD | 2,810,000.00 USD | 3,630,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2203.00` | 462,030,000.00 USD | 462,030,000.00 USD | 4,310,000.00 USD | 0.00 USD | 3,320,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 5,310.00 USD | 5,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2205.10` | 254,720,000.00 USD | 254,720,000.00 USD | 146,940.00 USD | 53,080.00 USD | 128,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2206.30` | 454,400,000.00 USD | 454,400,000.00 USD | 1,490,000.00 USD | 588,950.00 USD | 4,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2207.60` | 254,390,000.00 USD | 254,390,000.00 USD | 0.00 USD | 3,740,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2209.60` | 447,680,000.00 USD | 447,680,000.00 USD | 0.00 USD | 0.00 USD | 9,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2210.10` | 250,650,000.00 USD | 250,650,000.00 USD | 104,760.00 USD | 399,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2212.60` | 250,140,000.00 USD | 250,140,000.00 USD | 3,780,000.00 USD | 5,190,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2212.90` | 438,520,000.00 USD | 438,520,000.00 USD | 1,710,000.00 USD | 1,060,000.00 USD | 4,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2215.10` | 241,170,000.00 USD | 241,170,000.00 USD | 1,900,000.00 USD | 2,640,000.00 USD | 63,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2216.20` | 431,660,000.00 USD | 431,660,000.00 USD | 0.00 USD | 0.00 USD | 495,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2217.60` | 236,560,000.00 USD | 236,560,000.00 USD | 199,510.00 USD | 1,490,000.00 USD | 64,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2219.50` | 431,160,000.00 USD | 431,160,000.00 USD | 22,400,000.00 USD | 487,520.00 USD | 3,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2220.10` | 234,810,000.00 USD | 234,810,000.00 USD | 7,510,000.00 USD | 0.00 USD | 61,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2222.60` | 227,230,000.00 USD | 227,230,000.00 USD | 8,650,000.00 USD | 2,230,000.00 USD | 3,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2222.80` | 404,580,000.00 USD | 404,580,000.00 USD | 815,570.00 USD | 12,070,000.00 USD | 17,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2225.10` | 213,180,000.00 USD | 213,180,000.00 USD | 12,220,000.00 USD | 1,710,000.00 USD | 2,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2226.10` | 373,990,000.00 USD | 373,990,000.00 USD | 9,390,000.00 USD | 15,470,000.00 USD | 13,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2227.60` | 196,550,000.00 USD | 196,550,000.00 USD | 10,780,000.00 USD | 10,690,000.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2229.40` | 335,550,000.00 USD | 335,550,000.00 USD | 47,950,000.00 USD | 33,560,000.00 USD | 21,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2230.10` | 173,990,000.00 USD | 173,990,000.00 USD | 35,750,000.00 USD | 5,630,000.00 USD | 7,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2232.60` | 125,130,000.00 USD | 125,130,000.00 USD | 26,640,000.00 USD | 6,600,000.00 USD | 21,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2232.70` | 233,010,000.00 USD | 233,010,000.00 USD | 24,580,000.00 USD | 46,390,000.00 USD | 28,000,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2235.00` | 14,960.00 USD | 14,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2235.10` | 70,370,000.00 USD | 70,370,000.00 USD | 22,090,000.00 USD | 0.00 USD | 21,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2236.00` | 134,040,000.00 USD | 134,040,000.00 USD | 30,150,000.00 USD | 23,260,000.00 USD | 26,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2237.60` | 26,450,000.00 USD | 26,450,000.00 USD | 8,000,000.00 USD | 0.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2239.30` | 54,150,000.00 USD | 54,150,000.00 USD | 39,050,000.00 USD | 0.00 USD | 8,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2240.10` | 16,730,000.00 USD | 16,730,000.00 USD | 7,530,000.00 USD | 0.00 USD | 5,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2242.60` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 711,240.00 USD | 50,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2242.60` | 6,760,000.00 USD | 6,760,000.00 USD | 6,760,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2245.00` | 1,800,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2245.10` | 2,510,000.00 USD | 2,510,000.00 USD | 82,400.00 USD | 2,270,000.00 USD | 148,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2245.90` | 3,210,000.00 USD | 3,210,000.00 USD | 2,070,000.00 USD | 1,030,000.00 USD | 102,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2247.60` | 3,450,000.00 USD | 3,450,000.00 USD | 1,330,000.00 USD | 773,950.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2249.20` | 10,470,000.00 USD | 10,470,000.00 USD | 3,350,000.00 USD | 2,660,000.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2250.10` | 20,550,000.00 USD | 20,550,000.00 USD | 9,110,000.00 USD | 7,940,000.00 USD | 55,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2252.50` | 40,270,000.00 USD | 40,270,000.00 USD | 20,930,000.00 USD | 8,880,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2252.60` | 33,030,000.00 USD | 33,030,000.00 USD | 7,890,000.00 USD | 3,320,000.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2255.00` | 2,970,000.00 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2255.10` | 52,830,000.00 USD | 52,830,000.00 USD | 8,570,000.00 USD | 8,490,000.00 USD | 2,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2255.80` | 58,310,000.00 USD | 58,310,000.00 USD | 7,010,000.00 USD | 10,520,000.00 USD | 514,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2257.60` | 78,970,000.00 USD | 78,970,000.00 USD | 15,520,000.00 USD | 6,780,000.00 USD | 3,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2259.10` | 88,610,000.00 USD | 88,610,000.00 USD | 18,800,000.00 USD | 7,450,000.00 USD | 4,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2260.10` | 98,900,000.00 USD | 98,900,000.00 USD | 8,800,000.00 USD | 9,260,000.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2262.40` | 96,990,000.00 USD | 96,990,000.00 USD | 6,720,000.00 USD | 1,460,000.00 USD | 210,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2262.60` | 119,130,000.00 USD | 119,130,000.00 USD | 12,430,000.00 USD | 4,850,000.00 USD | 2,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2265.00` | 2,310,000.00 USD | 7,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2265.10` | 141,110,000.00 USD | 141,110,000.00 USD | 7,350,000.00 USD | 9,080,000.00 USD | 5,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2265.70` | 103,320,000.00 USD | 103,320,000.00 USD | 0.00 USD | 0.00 USD | 6,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2267.60` | 160,020,000.00 USD | 160,020,000.00 USD | 8,550,000.00 USD | 4,670,000.00 USD | 5,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2269.00` | 117,590,000.00 USD | 117,590,000.00 USD | 8,610,000.00 USD | 5,650,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2270.10` | 172,580,000.00 USD | 172,580,000.00 USD | 6,330,000.00 USD | 2,910,000.00 USD | 3,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2272.30` | 126,610,000.00 USD | 126,610,000.00 USD | 7,540,000.00 USD | 1,480,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2272.60` | 172,940,000.00 USD | 172,940,000.00 USD | 138,720.00 USD | 216,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2275.00` | 276,460.00 USD | 7,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2275.10` | 199,340,000.00 USD | 199,340,000.00 USD | 12,750,000.00 USD | 12,270,000.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2275.60` | 132,110,000.00 USD | 132,110,000.00 USD | 0.00 USD | 5,500,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2277.60` | 221,140,000.00 USD | 221,140,000.00 USD | 3,520,000.00 USD | 11,950,000.00 USD | 6,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2278.90` | 156,050,000.00 USD | 156,050,000.00 USD | 854,200.00 USD | 12,550,000.00 USD | 10,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2280.10` | 269,620,000.00 USD | 269,620,000.00 USD | 27,000,000.00 USD | 10,430,000.00 USD | 11,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2282.20` | 253,600,000.00 USD | 253,600,000.00 USD | 0.00 USD | 83,870,000.00 USD | 13,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2282.60` | 331,330,000.00 USD | 331,330,000.00 USD | 25,620,000.00 USD | 29,040,000.00 USD | 7,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2285.00` | 767,790.00 USD | 8,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2285.10` | 357,190,000.00 USD | 357,190,000.00 USD | 11,240,000.00 USD | 8,450,000.00 USD | 6,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2285.50` | 287,260,000.00 USD | 287,260,000.00 USD | 6,610,000.00 USD | 26,950,000.00 USD | 105,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2287.60` | 385,160,000.00 USD | 385,160,000.00 USD | 14,080,000.00 USD | 7,330,000.00 USD | 6,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2288.80` | 318,710,000.00 USD | 318,710,000.00 USD | 8,380,000.00 USD | 8,140,000.00 USD | 14,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2290.10` | 413,210,000.00 USD | 413,210,000.00 USD | 13,750,000.00 USD | 12,430,000.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2292.10` | 327,780,000.00 USD | 327,780,000.00 USD | 7,890,000.00 USD | 517,070.00 USD | 658,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2292.60` | 432,800,000.00 USD | 432,800,000.00 USD | 12,380,000.00 USD | 2,980,000.00 USD | 4,230,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2295.00` | 3,840,000.00 USD | 11,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2295.10` | 456,720,000.00 USD | 456,720,000.00 USD | 4,970,000.00 USD | 10,960,000.00 USD | 7,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2295.40` | 364,250,000.00 USD | 364,250,000.00 USD | 22,930,000.00 USD | 6,820,000.00 USD | 6,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2297.60` | 494,420,000.00 USD | 494,420,000.00 USD | 22,220,000.00 USD | 10,280,000.00 USD | 5,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2298.70` | 387,090,000.00 USD | 387,090,000.00 USD | 897,290.00 USD | 11,270,000.00 USD | 10,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2300.10` | 530,190,000.00 USD | 530,190,000.00 USD | 9,490,000.00 USD | 14,360,000.00 USD | 11,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2302.00` | 462,400,000.00 USD | 462,400,000.00 USD | 29,960,000.00 USD | 23,280,000.00 USD | 22,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2302.60` | 560,490,000.00 USD | 560,490,000.00 USD | 18,720,000.00 USD | 2,700,000.00 USD | 8,880,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2305.00` | 266,780.00 USD | 12,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2305.10` | 599,220,000.00 USD | 599,220,000.00 USD | 14,970,000.00 USD | 17,660,000.00 USD | 6,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2305.30` | 497,570,000.00 USD | 497,570,000.00 USD | 17,280,000.00 USD | 6,960,000.00 USD | 10,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2307.60` | 611,280,000.00 USD | 611,280,000.00 USD | 4,370,000.00 USD | 4,480,000.00 USD | 3,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2308.60` | 501,810,000.00 USD | 501,810,000.00 USD | 1,240,000.00 USD | 2,780,000.00 USD | 231,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2310.10` | 629,570,000.00 USD | 629,570,000.00 USD | 4,910,000.00 USD | 2,720,000.00 USD | 10,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2311.90` | 532,050,000.00 USD | 532,050,000.00 USD | 11,460,000.00 USD | 2,650,000.00 USD | 16,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2312.60` | 641,330,000.00 USD | 641,330,000.00 USD | 5,030,000.00 USD | 6,600,000.00 USD | 135,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2315.00` | 1,010,000.00 USD | 13,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2315.10` | 658,950,000.00 USD | 658,950,000.00 USD | 4,800,000.00 USD | 11,700,000.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2315.20` | 540,800,000.00 USD | 540,800,000.00 USD | 0.00 USD | 8,120,000.00 USD | 627,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2317.60` | 683,220,000.00 USD | 683,220,000.00 USD | 6,110,000.00 USD | 10,220,000.00 USD | 7,940,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2318.50` | 555,730,000.00 USD | 555,730,000.00 USD | 4,540,000.00 USD | 4,550,000.00 USD | 5,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2320.10` | 707,020,000.00 USD | 707,020,000.00 USD | 9,790,000.00 USD | 11,280,000.00 USD | 2,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2321.80` | 575,470,000.00 USD | 575,470,000.00 USD | 1,110,000.00 USD | 15,930,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2322.60` | 720,820,000.00 USD | 720,820,000.00 USD | 1,730,000.00 USD | 8,480,000.00 USD | 3,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2325.00` | 1,990,000.00 USD | 15,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2325.10` | 733,230,000.00 USD | 733,230,000.00 USD | 1,950,000.00 USD | 8,990,000.00 USD | 1,470,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2325.10` | 596,540,000.00 USD | 596,540,000.00 USD | 10,150,000.00 USD | 2,540,000.00 USD | 8,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2327.60` | 739,120,000.00 USD | 739,120,000.00 USD | 363,810.00 USD | 1,140,000.00 USD | 4,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2328.40` | 608,540,000.00 USD | 608,540,000.00 USD | 3,860,000.00 USD | 121,880.00 USD | 8,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2330.10` | 755,060,000.00 USD | 755,060,000.00 USD | 12,640,000.00 USD | 2,830,000.00 USD | 472,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2331.70` | 638,020,000.00 USD | 638,020,000.00 USD | 29,230,000.00 USD | 241,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2332.60` | 773,970,000.00 USD | 773,970,000.00 USD | 12,420,000.00 USD | 1,230,000.00 USD | 5,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2335.00` | 690,280,000.00 USD | 690,280,000.00 USD | 20,390,000.00 USD | 19,830,000.00 USD | 12,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2335.00` | 828,820.00 USD | 16,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2335.10` | 792,860,000.00 USD | 792,860,000.00 USD | 10,810,000.00 USD | 3,850,000.00 USD | 4,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2337.60` | 807,940,000.00 USD | 807,940,000.00 USD | 11,300,000.00 USD | 779,680.00 USD | 3,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2338.30` | 720,840,000.00 USD | 720,840,000.00 USD | 22,110,000.00 USD | 0.00 USD | 8,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2340.10` | 831,860,000.00 USD | 831,860,000.00 USD | 8,010,000.00 USD | 5,120,000.00 USD | 10,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2341.60` | 757,370,000.00 USD | 757,370,000.00 USD | 4,720,000.00 USD | 17,820,000.00 USD | 14,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2342.60` | 843,820,000.00 USD | 843,820,000.00 USD | 5,180,000.00 USD | 4,030,000.00 USD | 2,750,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2344.90` | 784,220,000.00 USD | 784,220,000.00 USD | 1,350,000.00 USD | 16,920,000.00 USD | 8,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2345.00` | 109,700.00 USD | 16,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2345.10` | 865,030,000.00 USD | 865,030,000.00 USD | 4,550,000.00 USD | 7,950,000.00 USD | 8,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2347.60` | 873,090,000.00 USD | 873,090,000.00 USD | 1,960,000.00 USD | 3,520,000.00 USD | 2,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2348.20` | 820,340,000.00 USD | 820,340,000.00 USD | 561,950.00 USD | 12,390,000.00 USD | 23,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2350.10` | 918,850,000.00 USD | 918,850,000.00 USD | 28,790,000.00 USD | 6,880,000.00 USD | 10,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2351.50` | 859,010,000.00 USD | 859,010,000.00 USD | 2,930,000.00 USD | 20,680,000.00 USD | 15,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2352.60` | 930,320,000.00 USD | 930,320,000.00 USD | 5,380,000.00 USD | 3,400,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2354.80` | 915,860,000.00 USD | 915,860,000.00 USD | 17,130,000.00 USD | 38,220,000.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 1,220,000.00 USD | 17,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2355.10` | 946,360,000.00 USD | 946,360,000.00 USD | 2,410,000.00 USD | 12,010,000.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2357.60` | 957,990,000.00 USD | 957,990,000.00 USD | 3,860,000.00 USD | 4,290,000.00 USD | 3,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2358.10` | 933,010,000.00 USD | 933,010,000.00 USD | 7,110,000.00 USD | 4,040,000.00 USD | 6,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2360.10` | 976,970,000.00 USD | 976,970,000.00 USD | 9,250,000.00 USD | 4,260,000.00 USD | 5,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2361.40` | 941,290,000.00 USD | 941,290,000.00 USD | 4,470,000.00 USD | 3,430,000.00 USD | 374,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2362.60` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 9,140,000.00 USD | 6,710,000.00 USD | 7,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2364.70` | 957,160,000.00 USD | 957,160,000.00 USD | 4,570,000.00 USD | 373,740.00 USD | 10,920,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 3,880,000.00 USD | 21,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2365.10` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 4,830,000.00 USD | 3,140,000.00 USD | 3,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2367.60` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 3,090,000.00 USD | 1,110,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2368.00` | 970,990,000.00 USD | 970,990,000.00 USD | 11,660,000.00 USD | 1,780,000.00 USD | 396,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2370.10` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 13,080,000.00 USD | 9,420,000.00 USD | 7,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2371.30` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 25,000,000.00 USD | 0.00 USD | 54,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2372.60` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 14,360,000.00 USD | 3,280,000.00 USD | 7,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2374.60` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 19,920,000.00 USD | 121,480.00 USD | 6,980,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 894,650.00 USD | 22,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2375.10` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 8,950,000.00 USD | 2,300,000.00 USD | 1,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2377.60` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 4,110,000.00 USD | 4,760,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2377.90` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 11,180,000.00 USD | 6,190,000.00 USD | 29,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2380.10` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 6,310,000.00 USD | 880,980.00 USD | 4,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2381.20` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 4,540,000.00 USD | 4,150,000.00 USD | 19,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2382.60` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 15,650,000.00 USD | 14,510,000.00 USD | 11,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2384.50` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 22,580,000.00 USD | 22,660,000.00 USD | 45,970,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 5,770,000.00 USD | 27,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2385.10` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 7,540,000.00 USD | 11,520,000.00 USD | 4,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2387.60` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 9,850,000.00 USD | 5,970,000.00 USD | 3,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2387.80` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 5,540,000.00 USD | 49,830,000.00 USD | 47,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2390.10` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 4,390,000.00 USD | 3,310,000.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2391.10` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 5,910,000.00 USD | 52,770,000.00 USD | 41,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2392.60` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 2,380,000.00 USD | 2,660,000.00 USD | 3,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2394.40` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 60,000,000.00 USD | 32,420,000.00 USD | 40,070,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 155,990.00 USD | 28,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2395.10` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 2,430,000.00 USD | 2,830,000.00 USD | 2,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2397.60` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 169,460.00 USD | 4,290,000.00 USD | 3,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2397.70` | 1,680,000,000.00 USD | 1,680,000,000.00 USD | 31,080,000.00 USD | 41,130,000.00 USD | 26,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2400.10` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 3,260,000.00 USD | 1,820,000.00 USD | 2,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2401.00` | 1,780,000,000.00 USD | 1,780,000,000.00 USD | 51,130,000.00 USD | 28,060,000.00 USD | 25,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2402.60` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 3,880,000.00 USD | 2,480,000.00 USD | 825,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2404.30` | 1,900,000,000.00 USD | 1,900,000,000.00 USD | 61,130,000.00 USD | 29,350,000.00 USD | 31,410,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 190,970.00 USD | 28,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2405.10` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 7,750,000.00 USD | 6,890,000.00 USD | 5,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2407.60` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 10,210,000.00 USD | 5,620,000.00 USD | 3,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2407.60` | 1,990,000,000.00 USD | 1,990,000,000.00 USD | 29,050,000.00 USD | 35,150,000.00 USD | 19,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2410.10` | 1,300,000,000.00 USD | 1,300,000,000.00 USD | 5,260,000.00 USD | 4,440,000.00 USD | 4,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2410.90` | 2,070,000,000.00 USD | 2,070,000,000.00 USD | 25,670,000.00 USD | 27,460,000.00 USD | 31,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2412.60` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 7,690,000.00 USD | 3,810,000.00 USD | 2,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2414.20` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 21,950,000.00 USD | 25,190,000.00 USD | 22,860,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 164,460.00 USD | 28,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2415.10` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 2,960,000.00 USD | 2,950,000.00 USD | 2,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2417.50` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 31,300,000.00 USD | 13,490,000.00 USD | 24,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2417.60` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 3,340,000.00 USD | 2,420,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2420.10` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 6,880,000.00 USD | 3,710,000.00 USD | 3,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2420.80` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 32,960,000.00 USD | 26,760,000.00 USD | 16,800,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2422.60` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 1,770,000.00 USD | 3,880,000.00 USD | 4,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.10` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 20,380,000.00 USD | 29,890,000.00 USD | 23,700,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 1,180,000.00 USD | 29,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2425.10` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 510,650.00 USD | 1,610,000.00 USD | 888,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2427.40` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 22,390,000.00 USD | 17,570,000.00 USD | 20,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2427.60` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 2,250,000.00 USD | 1,520,000.00 USD | 603,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2430.10` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 1,370,000.00 USD | 1,550,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2430.70` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 8,890,000.00 USD | 15,370,000.00 USD | 9,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2432.60` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 2,770,000.00 USD | 2,230,000.00 USD | 691,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2434.00` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 19,530,000.00 USD | 9,570,000.00 USD | 13,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 198,530.00 USD | 29,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2435.10` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 2,480,000.00 USD | 559,660.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2437.30` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 15,680,000.00 USD | 15,080,000.00 USD | 6,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2437.60` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 1,360,000.00 USD | 1,040,000.00 USD | 30,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2440.10` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 1,240,000.00 USD | 502,040.00 USD | 304,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2440.60` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 16,940,000.00 USD | 10,790,000.00 USD | 9,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2442.60` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 1,030,000.00 USD | 700,830.00 USD | 819,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2443.90` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 5,830,000.00 USD | 13,790,000.00 USD | 8,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 66,330.00 USD | 29,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2445.10` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 0.00 USD | 486,350.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2447.20` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 13,820,000.00 USD | 7,510,000.00 USD | 16,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2447.60` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 472,100.00 USD | 485,550.00 USD | 687,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2450.10` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 335,910.00 USD | 56,170.00 USD | 26,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2450.50` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 10,570,000.00 USD | 11,560,000.00 USD | 10,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2452.60` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 2,730,000.00 USD | 1,820,000.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2453.80` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 7,240,000.00 USD | 4,290,000.00 USD | 6,910,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 186,790.00 USD | 30,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2455.10` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 2,270,000.00 USD | 1,660,000.00 USD | 905,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2457.10` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 8,340,000.00 USD | 8,890,000.00 USD | 7,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2457.60` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 1,290,000.00 USD | 1,810,000.00 USD | 479,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2460.10` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 1,510,000.00 USD | 1,350,000.00 USD | 384,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2460.40` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 7,080,000.00 USD | 8,140,000.00 USD | 9,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2462.60` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 303,600.00 USD | 521,540.00 USD | 829,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2463.70` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 9,430,000.00 USD | 8,280,000.00 USD | 6,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 65,770,000.00 USD | 95,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2465.10` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 404,950.00 USD | 897,320.00 USD | 336,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2467.00` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 4,840,000.00 USD | 2,920,000.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2467.60` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 288,920.00 USD | 752,230.00 USD | 213,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2470.10` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 973,110.00 USD | 1,190,000.00 USD | 537,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2470.30` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 3,190,000.00 USD | 3,080,000.00 USD | 496,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2472.60` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 0.00 USD | 308,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2473.60` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 5,860,000.00 USD | 2,920,000.00 USD | 2,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 641,630.00 USD | 96,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2475.10` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 914,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2475.60` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 185,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2476.90` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 2,660,000.00 USD | 2,410,000.00 USD | 872,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2480.20` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 1,580,000.00 USD | 6,190,000.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2483.50` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 1,750,000.00 USD | 2,280,000.00 USD | 77,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 1,640,000.00 USD | 98,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2486.80` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 30,880.00 USD | 0.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2490.10` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 1,480,000.00 USD | 1,850,000.00 USD | 188,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2493.40` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 3,210,000.00 USD | 1,830,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 6,380,000.00 USD | 104,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2496.70` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 1,370,000.00 USD | 3,690,000.00 USD | 4,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2500.00` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 358,770.00 USD | 1,980,000.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2503.30` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 27,220.00 USD | 125,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 4,450,000.00 USD | 108,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2506.60` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 2,540,000.00 USD | 903,900.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2509.90` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 2,290,000.00 USD | 2,160,000.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 700,300.00 USD | 109,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2516.50` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2519.80` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2523.10` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 945,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 5,130,000.00 USD | 114,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2526.40` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 292,400.00 USD | 1,090,000.00 USD | 200,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2529.70` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 1,510,000.00 USD | 2,770,000.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2533.00` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 4,460,000.00 USD | 1,850,000.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2535.00` | 854,240.00 USD | 115,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2536.30` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 3,170,000.00 USD | 2,460,000.00 USD | 4,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2539.60` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 4,190,000.00 USD | 3,730,000.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2542.90` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 4,070,000.00 USD | 2,950,000.00 USD | 2,920,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2545.00` | 173,450.00 USD | 115,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2546.20` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 1,900,000.00 USD | 1,140,000.00 USD | 1,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2549.50` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 4,150,000.00 USD | 3,470,000.00 USD | 4,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2552.80` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 1,920,000.00 USD | 580,780.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2555.00` | 12,390,000.00 USD | 128,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2556.10` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 4,340,000.00 USD | 549,010.00 USD | 7,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2559.40` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 5,200,000.00 USD | 1,660,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2562.70` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 1,940,000.00 USD | 3,320,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2565.00` | 60,800.00 USD | 128,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2566.00` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 1,880,000.00 USD | 1,520,000.00 USD | 2,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2569.30` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 125,250.00 USD | 739,480.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2572.60` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 2,000,000.00 USD | 890,480.00 USD | 2,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2575.00` | 41,530.00 USD | 128,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2575.90` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 2,180,000.00 USD | 440,740.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2579.20` | 2,970,000,000.00 USD | 2,970,000,000.00 USD | 1,870,000.00 USD | 1,940,000.00 USD | 1,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2582.50` | 2,970,000,000.00 USD | 2,970,000,000.00 USD | 2,830,000.00 USD | 1,030,000.00 USD | 3,720,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2585.00` | 26,520,000.00 USD | 154,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2585.80` | 2,980,000,000.00 USD | 2,980,000,000.00 USD | 883,660.00 USD | 2,700,000.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2589.10` | 2,990,000,000.00 USD | 2,990,000,000.00 USD | 2,540,000.00 USD | 536,380.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2590.30` | 2,990,000,000.00 USD | 2,990,000,000.00 USD | 1,180,000.00 USD | 304,000.00 USD | 447,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2595.00` | 41,560.00 USD | 154,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2605.00` | 6,100,000.00 USD | 160,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2615.00` | 190,200.00 USD | 161,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2625.00` | 33,170,000.00 USD | 194,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `7D` | `1972.00` | 999,440,000.00 USD | 0.00 USD | 999,440,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD |
| `7D` | `1975.30` | 999,310,000.00 USD | 0.00 USD | 999,310,000.00 USD | 0.00 USD | 0.00 USD | 49,530.00 USD |
| `7D` | `1978.60` | 999,260,000.00 USD | 0.00 USD | 999,260,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1981.90` | 997,020,000.00 USD | 0.00 USD | 997,020,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD |
| `1D` | `1985.10` | 647,890,000.00 USD | 0.00 USD | 647,890,000.00 USD | 1,800,000.00 USD | 1,260,000.00 USD | 20,230.00 USD |
| `1D` | `1987.60` | 644,810,000.00 USD | 0.00 USD | 644,810,000.00 USD | 534,990.00 USD | 0.00 USD | 19,740.00 USD |
| `7D` | `1988.50` | 996,810,000.00 USD | 0.00 USD | 996,810,000.00 USD | 3,730,000.00 USD | 1,780,000.00 USD | 0.00 USD |
| `1D` | `1990.10` | 644,260,000.00 USD | 0.00 USD | 644,260,000.00 USD | 1,460,000.00 USD | 1,230,000.00 USD | 547,380.00 USD |
| `7D` | `1991.80` | 991,310,000.00 USD | 0.00 USD | 991,310,000.00 USD | 1,390,000.00 USD | 1,320,000.00 USD | 38,060.00 USD |
| `1D` | `1992.60` | 641,020,000.00 USD | 0.00 USD | 641,020,000.00 USD | 742,220.00 USD | 77,290.00 USD | 256,670.00 USD |
| `1D` | `1995.10` | 639,940,000.00 USD | 0.00 USD | 639,940,000.00 USD | 602,100.00 USD | 580,650.00 USD | 0.00 USD |
| `7D` | `1995.10` | 988,560,000.00 USD | 0.00 USD | 988,560,000.00 USD | 1,340,000.00 USD | 0.00 USD | 808,380.00 USD |
| `1D` | `1997.60` | 638,760,000.00 USD | 0.00 USD | 638,760,000.00 USD | 0.00 USD | 0.00 USD | 304,820.00 USD |
| `1D` | `2000.10` | 638,450,000.00 USD | 0.00 USD | 638,450,000.00 USD | 0.00 USD | 0.00 USD | 487,740.00 USD |
| `1D` | `2002.60` | 637,970,000.00 USD | 0.00 USD | 637,970,000.00 USD | 0.00 USD | 217,070.00 USD | 0.00 USD |
| `7D` | `2005.00` | 986,410,000.00 USD | 0.00 USD | 986,410,000.00 USD | 0.00 USD | 266,430.00 USD | 0.00 USD |
| `1D` | `2005.10` | 637,750,000.00 USD | 0.00 USD | 637,750,000.00 USD | 14,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2007.60` | 637,730,000.00 USD | 0.00 USD | 637,730,000.00 USD | 0.00 USD | 224,500.00 USD | 0.00 USD |
| `1D` | `2010.10` | 637,510,000.00 USD | 0.00 USD | 637,510,000.00 USD | 0.00 USD | 308,260.00 USD | 0.00 USD |
| `7D` | `2011.60` | 986,140,000.00 USD | 0.00 USD | 986,140,000.00 USD | 170,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2012.60` | 637,200,000.00 USD | 0.00 USD | 637,200,000.00 USD | 299,090.00 USD | 210,450.00 USD | 17,710.00 USD |
| `1D` | `2015.10` | 636,670,000.00 USD | 0.00 USD | 636,670,000.00 USD | 303,600.00 USD | 51,960.00 USD | 0.00 USD |
| `1D` | `2017.60` | 636,320,000.00 USD | 0.00 USD | 636,320,000.00 USD | 404,950.00 USD | 1,350,000.00 USD | 550,280.00 USD |
| `1D` | `2020.10` | 634,020,000.00 USD | 0.00 USD | 634,020,000.00 USD | 510,810.00 USD | 771,060.00 USD | 4,960.00 USD |
| `1D` | `2022.60` | 632,730,000.00 USD | 0.00 USD | 632,730,000.00 USD | 751,210.00 USD | 27,630.00 USD | 459,540.00 USD |
| `7D` | `2024.80` | 985,970,000.00 USD | 0.00 USD | 985,970,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD |
| `1D` | `2025.10` | 631,490,000.00 USD | 0.00 USD | 631,490,000.00 USD | 0.00 USD | 914,780.00 USD | 32,670.00 USD |
| `1D` | `2027.60` | 630,540,000.00 USD | 0.00 USD | 630,540,000.00 USD | 1,430,000.00 USD | 1,160,000.00 USD | 11,450.00 USD |
| `7D` | `2028.10` | 985,790,000.00 USD | 0.00 USD | 985,790,000.00 USD | 0.00 USD | 0.00 USD | 35,180.00 USD |
| `1D` | `2030.10` | 627,940,000.00 USD | 0.00 USD | 627,940,000.00 USD | 87,180.00 USD | 366,120.00 USD | 957,140.00 USD |
| `7D` | `2031.40` | 985,760,000.00 USD | 0.00 USD | 985,760,000.00 USD | 0.00 USD | 3,520,000.00 USD | 1,050,000.00 USD |
| `1D` | `2032.60` | 626,530,000.00 USD | 0.00 USD | 626,530,000.00 USD | 1,360,000.00 USD | 1,490,000.00 USD | 707,170.00 USD |
| `7D` | `2034.70` | 981,190,000.00 USD | 0.00 USD | 981,190,000.00 USD | 0.00 USD | 186,130.00 USD | 1,350,000.00 USD |
| `1D` | `2035.10` | 622,970,000.00 USD | 0.00 USD | 622,970,000.00 USD | 1,150,000.00 USD | 19,490.00 USD | 165,760.00 USD |
| `1D` | `2037.60` | 621,630,000.00 USD | 0.00 USD | 621,630,000.00 USD | 396,700.00 USD | 458,110.00 USD | 378,700.00 USD |
| `7D` | `2038.00` | 979,650,000.00 USD | 0.00 USD | 979,650,000.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2040.10` | 620,400,000.00 USD | 0.00 USD | 620,400,000.00 USD | 542,670.00 USD | 178,560.00 USD | 31,670.00 USD |
| `1D` | `2042.60` | 619,650,000.00 USD | 0.00 USD | 619,650,000.00 USD | 626,840.00 USD | 0.00 USD | 174,920.00 USD |
| `7D` | `2044.60` | 978,050,000.00 USD | 0.00 USD | 978,050,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD |
| `1D` | `2045.10` | 618,850,000.00 USD | 0.00 USD | 618,850,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD |
| `1D` | `2047.60` | 618,820,000.00 USD | 0.00 USD | 618,820,000.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD |
| `1D` | `2050.10` | 617,990,000.00 USD | 0.00 USD | 617,990,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD |
| `7D` | `2051.20` | 977,750,000.00 USD | 0.00 USD | 977,750,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2054.50` | 977,530,000.00 USD | 0.00 USD | 977,530,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD |
| `1D` | `2055.10` | 616,880,000.00 USD | 0.00 USD | 616,880,000.00 USD | 242,080.00 USD | 88,880.00 USD | 28,160.00 USD |
| `7D` | `2057.80` | 975,240,000.00 USD | 0.00 USD | 975,240,000.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2060.10` | 616,530,000.00 USD | 0.00 USD | 616,530,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `7D` | `2061.10` | 975,190,000.00 USD | 0.00 USD | 975,190,000.00 USD | 1,700,000.00 USD | 1,310,000.00 USD | 1,710,000.00 USD |
| `1D` | `2062.60` | 615,770,000.00 USD | 0.00 USD | 615,770,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD |
| `7D` | `2064.40` | 970,470,000.00 USD | 0.00 USD | 970,470,000.00 USD | 1,230,000.00 USD | 1,080,000.00 USD | 945,860.00 USD |
| `1D` | `2065.10` | 615,690,000.00 USD | 0.00 USD | 615,690,000.00 USD | 563,140.00 USD | 537,030.00 USD | 510,200.00 USD |
| `1D` | `2067.60` | 614,080,000.00 USD | 0.00 USD | 614,080,000.00 USD | 387,410.00 USD | 304,560.00 USD | 0.00 USD |
| `7D` | `2067.70` | 967,210,000.00 USD | 0.00 USD | 967,210,000.00 USD | 292,400.00 USD | 1,180,000.00 USD | 927,620.00 USD |
| `1D` | `2070.10` | 613,390,000.00 USD | 0.00 USD | 613,390,000.00 USD | 57,300.00 USD | 319,490.00 USD | 0.00 USD |
| `7D` | `2071.00` | 964,810,000.00 USD | 0.00 USD | 964,810,000.00 USD | 4,230,000.00 USD | 3,040,000.00 USD | 1,230,000.00 USD |
| `1D` | `2072.60` | 613,010,000.00 USD | 0.00 USD | 613,010,000.00 USD | 67,060.00 USD | 555,250.00 USD | 428,640.00 USD |
| `7D` | `2074.30` | 956,310,000.00 USD | 0.00 USD | 956,310,000.00 USD | 4,000,000.00 USD | 2,720,000.00 USD | 3,720,000.00 USD |
| `1D` | `2075.10` | 611,960,000.00 USD | 0.00 USD | 611,960,000.00 USD | 67,780.00 USD | 224,070.00 USD | 3,490.00 USD |
| `1D` | `2077.60` | 611,670,000.00 USD | 0.00 USD | 611,670,000.00 USD | 1,540,000.00 USD | 765,660.00 USD | 510,780.00 USD |
| `7D` | `2077.60` | 945,870,000.00 USD | 0.00 USD | 945,870,000.00 USD | 4,430,000.00 USD | 4,400,000.00 USD | 2,270,000.00 USD |
| `1D` | `2080.10` | 608,850,000.00 USD | 0.00 USD | 608,850,000.00 USD | 586,070.00 USD | 922,510.00 USD | 206,930.00 USD |
| `7D` | `2080.90` | 934,770,000.00 USD | 0.00 USD | 934,770,000.00 USD | 5,690,000.00 USD | 3,540,000.00 USD | 2,980,000.00 USD |
| `1D` | `2082.60` | 607,130,000.00 USD | 0.00 USD | 607,130,000.00 USD | 858,220.00 USD | 315,330.00 USD | 215,500.00 USD |
| `7D` | `2084.20` | 922,560,000.00 USD | 0.00 USD | 922,560,000.00 USD | 1,660,000.00 USD | 1,490,000.00 USD | 3,500,000.00 USD |
| `1D` | `2085.10` | 605,740,000.00 USD | 0.00 USD | 605,740,000.00 USD | 1,410,000.00 USD | 790,900.00 USD | 1,260,000.00 USD |
| `7D` | `2087.50` | 915,910,000.00 USD | 0.00 USD | 915,910,000.00 USD | 5,220,000.00 USD | 3,230,000.00 USD | 3,060,000.00 USD |
| `1D` | `2087.60` | 602,290,000.00 USD | 0.00 USD | 602,290,000.00 USD | 1,460,000.00 USD | 565,380.00 USD | 682,400.00 USD |
| `1D` | `2090.10` | 599,580,000.00 USD | 0.00 USD | 599,580,000.00 USD | 787,350.00 USD | 225,190.00 USD | 269,320.00 USD |
| `7D` | `2090.80` | 904,410,000.00 USD | 0.00 USD | 904,410,000.00 USD | 4,410,000.00 USD | 976,840.00 USD | 6,980,000.00 USD |
| `1D` | `2092.60` | 598,290,000.00 USD | 0.00 USD | 598,290,000.00 USD | 773,260.00 USD | 513,660.00 USD | 874,240.00 USD |
| `7D` | `2094.10` | 892,040,000.00 USD | 0.00 USD | 892,040,000.00 USD | 5,350,000.00 USD | 1,660,000.00 USD | 2,950,000.00 USD |
| `1D` | `2095.10` | 596,130,000.00 USD | 0.00 USD | 596,130,000.00 USD | 2,100,000.00 USD | 1,170,000.00 USD | 1,330,000.00 USD |
| `7D` | `2097.40` | 882,090,000.00 USD | 0.00 USD | 882,090,000.00 USD | 2,280,000.00 USD | 3,580,000.00 USD | 1,290,000.00 USD |
| `1D` | `2097.60` | 591,530,000.00 USD | 0.00 USD | 591,530,000.00 USD | 175,830.00 USD | 1,280,000.00 USD | 984,190.00 USD |
| `1D` | `2100.10` | 589,100,000.00 USD | 0.00 USD | 589,100,000.00 USD | 307,340.00 USD | 928,890.00 USD | 50,560.00 USD |
| `7D` | `2100.70` | 874,940,000.00 USD | 0.00 USD | 874,940,000.00 USD | 1,830,000.00 USD | 1,850,000.00 USD | 3,310,000.00 USD |
| `1D` | `2102.60` | 587,810,000.00 USD | 0.00 USD | 587,810,000.00 USD | 211,840.00 USD | 222,480.00 USD | 483,690.00 USD |
| `7D` | `2104.00` | 867,950,000.00 USD | 0.00 USD | 867,950,000.00 USD | 1,190,000.00 USD | 738,240.00 USD | 3,030,000.00 USD |
| `1D` | `2105.10` | 586,890,000.00 USD | 0.00 USD | 586,890,000.00 USD | 3,570,000.00 USD | 1,160,000.00 USD | 691,960.00 USD |
| `7D` | `2107.30` | 862,990,000.00 USD | 0.00 USD | 862,990,000.00 USD | 8,720,000.00 USD | 1,150,000.00 USD | 1,190,000.00 USD |
| `1D` | `2107.60` | 581,470,000.00 USD | 0.00 USD | 581,470,000.00 USD | 734,860.00 USD | 0.00 USD | 488,260.00 USD |
| `1D` | `2110.10` | 580,240,000.00 USD | 0.00 USD | 580,240,000.00 USD | 61,010.00 USD | 31,550.00 USD | 6,190.00 USD |
| `7D` | `2110.60` | 851,930,000.00 USD | 0.00 USD | 851,930,000.00 USD | 2,970,000.00 USD | 2,360,000.00 USD | 2,530,000.00 USD |
| `1D` | `2112.60` | 580,140,000.00 USD | 0.00 USD | 580,140,000.00 USD | 902,600.00 USD | 360,140.00 USD | 221,490.00 USD |
| `7D` | `2113.90` | 844,070,000.00 USD | 0.00 USD | 844,070,000.00 USD | 1,780,000.00 USD | 1,810,000.00 USD | 3,580,000.00 USD |
| `1D` | `2115.10` | 578,660,000.00 USD | 0.00 USD | 578,660,000.00 USD | 202,800.00 USD | 411,610.00 USD | 962,630.00 USD |
| `7D` | `2117.20` | 836,890,000.00 USD | 0.00 USD | 836,890,000.00 USD | 2,410,000.00 USD | 2,380,000.00 USD | 2,470,000.00 USD |
| `1D` | `2117.60` | 577,080,000.00 USD | 0.00 USD | 577,080,000.00 USD | 4,750,000.00 USD | 4,080,000.00 USD | 302,800.00 USD |
| `1D` | `2120.10` | 567,950,000.00 USD | 0.00 USD | 567,950,000.00 USD | 3,950,000.00 USD | 22,470.00 USD | 645,650.00 USD |
| `7D` | `2120.50` | 829,630,000.00 USD | 0.00 USD | 829,630,000.00 USD | 13,880,000.00 USD | 5,790,000.00 USD | 2,800,000.00 USD |
| `1D` | `2122.60` | 563,340,000.00 USD | 0.00 USD | 563,340,000.00 USD | 4,520,000.00 USD | 3,800,000.00 USD | 1,860,000.00 USD |
| `7D` | `2123.80` | 807,160,000.00 USD | 0.00 USD | 807,160,000.00 USD | 7,610,000.00 USD | 7,900,000.00 USD | 1,820,000.00 USD |
| `1D` | `2125.10` | 553,160,000.00 USD | 0.00 USD | 553,160,000.00 USD | 6,940,000.00 USD | 1,830,000.00 USD | 2,110,000.00 USD |
| `7D` | `2127.10` | 789,830,000.00 USD | 0.00 USD | 789,830,000.00 USD | 2,760,000.00 USD | 4,420,000.00 USD | 5,540,000.00 USD |
| `1D` | `2127.60` | 542,280,000.00 USD | 0.00 USD | 542,280,000.00 USD | 4,430,000.00 USD | 4,180,000.00 USD | 782,350.00 USD |
| `1D` | `2130.10` | 532,890,000.00 USD | 0.00 USD | 532,890,000.00 USD | 1,230,000.00 USD | 172,040.00 USD | 762,060.00 USD |
| `7D` | `2130.40` | 777,110,000.00 USD | 0.00 USD | 777,110,000.00 USD | 5,410,000.00 USD | 2,580,000.00 USD | 1,690,000.00 USD |
| `1D` | `2132.60` | 530,730,000.00 USD | 0.00 USD | 530,730,000.00 USD | 0.00 USD | 177,810.00 USD | 1,540,000.00 USD |
| `7D` | `2133.70` | 767,420,000.00 USD | 0.00 USD | 767,420,000.00 USD | 2,550,000.00 USD | 715,940.00 USD | 323,430.00 USD |
| `1D` | `2135.10` | 529,020,000.00 USD | 0.00 USD | 529,020,000.00 USD | 20,600.00 USD | 1,170,000.00 USD | 86,940.00 USD |
| `7D` | `2137.00` | 763,830,000.00 USD | 0.00 USD | 763,830,000.00 USD | 746,340.00 USD | 1,510,000.00 USD | 43,560.00 USD |
| `1D` | `2137.60` | 527,740,000.00 USD | 0.00 USD | 527,740,000.00 USD | 21,090.00 USD | 379,920.00 USD | 0.00 USD |
| `1D` | `2140.10` | 527,340,000.00 USD | 0.00 USD | 527,340,000.00 USD | 36,740.00 USD | 265,280.00 USD | 64,360.00 USD |
| `7D` | `2140.30` | 761,530,000.00 USD | 0.00 USD | 761,530,000.00 USD | 2,260,000.00 USD | 1,200,000.00 USD | 801,910.00 USD |
| `1D` | `2142.60` | 526,970,000.00 USD | 0.00 USD | 526,970,000.00 USD | 670,350.00 USD | 2,130,000.00 USD | 0.00 USD |
| `7D` | `2143.60` | 757,270,000.00 USD | 0.00 USD | 757,270,000.00 USD | 1,200,000.00 USD | 1,420,000.00 USD | 268,500.00 USD |
| `1D` | `2145.10` | 524,170,000.00 USD | 0.00 USD | 524,170,000.00 USD | 121,400.00 USD | 1,690,000.00 USD | 118,750.00 USD |
| `7D` | `2146.90` | 754,380,000.00 USD | 0.00 USD | 754,380,000.00 USD | 1,060,000.00 USD | 938,520.00 USD | 134,420.00 USD |
| `1D` | `2147.60` | 522,240,000.00 USD | 0.00 USD | 522,240,000.00 USD | 1,450,000.00 USD | 1,100,000.00 USD | 60,040.00 USD |
| `1D` | `2150.10` | 519,630,000.00 USD | 0.00 USD | 519,630,000.00 USD | 6,930,000.00 USD | 2,570,000.00 USD | 1,680,000.00 USD |
| `7D` | `2150.20` | 752,250,000.00 USD | 0.00 USD | 752,250,000.00 USD | 485,890.00 USD | 838,260.00 USD | 331,330.00 USD |
| `1D` | `2152.60` | 508,440,000.00 USD | 0.00 USD | 508,440,000.00 USD | 2,240,000.00 USD | 2,180,000.00 USD | 1,380,000.00 USD |
| `7D` | `2153.50` | 750,600,000.00 USD | 0.00 USD | 750,600,000.00 USD | 11,310,000.00 USD | 311,060.00 USD | 0.00 USD |
| `1D` | `2155.10` | 502,650,000.00 USD | 0.00 USD | 502,650,000.00 USD | 1,940,000.00 USD | 2,480,000.00 USD | 576,110.00 USD |
| `7D` | `2156.80` | 738,980,000.00 USD | 0.00 USD | 738,980,000.00 USD | 2,560,000.00 USD | 2,210,000.00 USD | 2,040,000.00 USD |
| `1D` | `2157.60` | 497,650,000.00 USD | 0.00 USD | 497,650,000.00 USD | 2,480,000.00 USD | 834,590.00 USD | 1,260,000.00 USD |
| `1D` | `2160.10` | 493,080,000.00 USD | 0.00 USD | 493,080,000.00 USD | 1,450,000.00 USD | 4,910,000.00 USD | 1,560,000.00 USD |
| `7D` | `2160.10` | 732,160,000.00 USD | 0.00 USD | 732,160,000.00 USD | 2,190,000.00 USD | 2,550,000.00 USD | 1,270,000.00 USD |
| `1D` | `2162.60` | 485,170,000.00 USD | 0.00 USD | 485,170,000.00 USD | 14,140,000.00 USD | 9,870,000.00 USD | 1,560,000.00 USD |
| `7D` | `2163.40` | 726,160,000.00 USD | 0.00 USD | 726,160,000.00 USD | 21,210,000.00 USD | 11,130,000.00 USD | 518,640.00 USD |
| `1D` | `2165.10` | 459,590,000.00 USD | 0.00 USD | 459,590,000.00 USD | 10,390,000.00 USD | 9,640,000.00 USD | 4,180,000.00 USD |
| `7D` | `2166.70` | 693,300,000.00 USD | 0.00 USD | 693,300,000.00 USD | 5,300,000.00 USD | 15,400,000.00 USD | 2,970,000.00 USD |
| `1D` | `2167.60` | 435,390,000.00 USD | 0.00 USD | 435,390,000.00 USD | 17,280,000.00 USD | 7,820,000.00 USD | 5,200,000.00 USD |
| `7D` | `2170.00` | 669,630,000.00 USD | 0.00 USD | 669,630,000.00 USD | 10,280,000.00 USD | 15,310,000.00 USD | 5,480,000.00 USD |
| `1D` | `2170.10` | 405,090,000.00 USD | 0.00 USD | 405,090,000.00 USD | 13,580,000.00 USD | 9,360,000.00 USD | 4,760,000.00 USD |
| `1D` | `2172.60` | 377,390,000.00 USD | 0.00 USD | 377,390,000.00 USD | 16,900,000.00 USD | 5,140,000.00 USD | 4,630,000.00 USD |
| `7D` | `2173.30` | 638,550,000.00 USD | 0.00 USD | 638,550,000.00 USD | 30,550,000.00 USD | 828,350.00 USD | 5,540,000.00 USD |
| `1D` | `2175.10` | 350,720,000.00 USD | 0.00 USD | 350,720,000.00 USD | 5,700,000.00 USD | 0.00 USD | 2,310,000.00 USD |
| `7D` | `2176.60` | 601,620,000.00 USD | 0.00 USD | 601,620,000.00 USD | 5,390,000.00 USD | 1,330,000.00 USD | 2,820,000.00 USD |
| `1D` | `2177.60` | 342,700,000.00 USD | 0.00 USD | 342,700,000.00 USD | 730,100.00 USD | 355,620.00 USD | 2,830,000.00 USD |
| `1D` | `2180.10` | 338,790,000.00 USD | 0.00 USD | 338,790,000.00 USD | 894,580.00 USD | 1,460,000.00 USD | 1,370,000.00 USD |
| `1D` | `2182.60` | 335,070,000.00 USD | 0.00 USD | 335,070,000.00 USD | 73,470.00 USD | 26,540.00 USD | 3,040,000.00 USD |
| `7D` | `2183.20` | 592,090,000.00 USD | 0.00 USD | 592,090,000.00 USD | 1,760,000.00 USD | 0.00 USD | 3,950,000.00 USD |
| `1D` | `2185.10` | 331,930,000.00 USD | 0.00 USD | 331,930,000.00 USD | 310,640.00 USD | 1,660,000.00 USD | 3,190,000.00 USD |
| `7D` | `2186.50` | 586,390,000.00 USD | 0.00 USD | 586,390,000.00 USD | 37,310,000.00 USD | 19,060,000.00 USD | 0.00 USD |
| `1D` | `2187.60` | 326,770,000.00 USD | 0.00 USD | 326,770,000.00 USD | 3,960,000.00 USD | 1,250,000.00 USD | 5,360,000.00 USD |
| `7D` | `2189.80` | 530,020,000.00 USD | 0.00 USD | 530,020,000.00 USD | 12,430,000.00 USD | 19,940,000.00 USD | 4,580,000.00 USD |
| `1D` | `2190.10` | 316,200,000.00 USD | 0.00 USD | 316,200,000.00 USD | 4,530,000.00 USD | 3,550,000.00 USD | 5,080,000.00 USD |
| `1D` | `2192.60` | 303,050,000.00 USD | 0.00 USD | 303,050,000.00 USD | 4,810,000.00 USD | 5,200,000.00 USD | 1,180,000.00 USD |
| `7D` | `2193.10` | 493,080,000.00 USD | 0.00 USD | 493,080,000.00 USD | 0.00 USD | 14,900,000.00 USD | 8,080,000.00 USD |
| `1D` | `2195.10` | 291,860,000.00 USD | 0.00 USD | 291,860,000.00 USD | 5,420,000.00 USD | 1,880,000.00 USD | 4,000,000.00 USD |
| `7D` | `2196.40` | 470,090,000.00 USD | 0.00 USD | 470,090,000.00 USD | 383,690.00 USD | 243,760.00 USD | 0.00 USD |
| `1D` | `2197.60` | 280,560,000.00 USD | 0.00 USD | 280,560,000.00 USD | 4,050,000.00 USD | 0.00 USD | 2,750,000.00 USD |
| `7D` | `2199.70` | 469,470,000.00 USD | 0.00 USD | 469,470,000.00 USD | 0.00 USD | 0.00 USD | 7,440,000.00 USD |
| `1D` | `2200.10` | 273,760,000.00 USD | 0.00 USD | 273,760,000.00 USD | 4,340,000.00 USD | 1,680,000.00 USD | 6,580,000.00 USD |
| `1D` | `2202.60` | 261,160,000.00 USD | 0.00 USD | 261,160,000.00 USD | 2,810,000.00 USD | 3,630,000.00 USD | 0.00 USD |
| `7D` | `2203.00` | 462,030,000.00 USD | 0.00 USD | 462,030,000.00 USD | 4,310,000.00 USD | 0.00 USD | 3,320,000.00 USD |
| `1D` | `2205.10` | 254,720,000.00 USD | 0.00 USD | 254,720,000.00 USD | 146,940.00 USD | 53,080.00 USD | 128,720.00 USD |
| `7D` | `2206.30` | 454,400,000.00 USD | 0.00 USD | 454,400,000.00 USD | 1,490,000.00 USD | 588,950.00 USD | 4,640,000.00 USD |
| `1D` | `2207.60` | 254,390,000.00 USD | 0.00 USD | 254,390,000.00 USD | 0.00 USD | 3,740,000.00 USD | 0.00 USD |
| `7D` | `2209.60` | 447,680,000.00 USD | 0.00 USD | 447,680,000.00 USD | 0.00 USD | 0.00 USD | 9,150,000.00 USD |
| `1D` | `2210.10` | 250,650,000.00 USD | 0.00 USD | 250,650,000.00 USD | 104,760.00 USD | 399,720.00 USD | 0.00 USD |
| `1D` | `2212.60` | 250,140,000.00 USD | 0.00 USD | 250,140,000.00 USD | 3,780,000.00 USD | 5,190,000.00 USD | 0.00 USD |
| `7D` | `2212.90` | 438,520,000.00 USD | 0.00 USD | 438,520,000.00 USD | 1,710,000.00 USD | 1,060,000.00 USD | 4,100,000.00 USD |
| `1D` | `2215.10` | 241,170,000.00 USD | 0.00 USD | 241,170,000.00 USD | 1,900,000.00 USD | 2,640,000.00 USD | 63,100.00 USD |
| `7D` | `2216.20` | 431,660,000.00 USD | 0.00 USD | 431,660,000.00 USD | 0.00 USD | 0.00 USD | 495,340.00 USD |
| `1D` | `2217.60` | 236,560,000.00 USD | 0.00 USD | 236,560,000.00 USD | 199,510.00 USD | 1,490,000.00 USD | 64,320.00 USD |
| `7D` | `2219.50` | 431,160,000.00 USD | 0.00 USD | 431,160,000.00 USD | 22,400,000.00 USD | 487,520.00 USD | 3,700,000.00 USD |
| `1D` | `2220.10` | 234,810,000.00 USD | 0.00 USD | 234,810,000.00 USD | 7,510,000.00 USD | 0.00 USD | 61,180.00 USD |
| `1D` | `2222.60` | 227,230,000.00 USD | 0.00 USD | 227,230,000.00 USD | 8,650,000.00 USD | 2,230,000.00 USD | 3,170,000.00 USD |
| `7D` | `2222.80` | 404,580,000.00 USD | 0.00 USD | 404,580,000.00 USD | 815,570.00 USD | 12,070,000.00 USD | 17,700,000.00 USD |
| `1D` | `2225.10` | 213,180,000.00 USD | 0.00 USD | 213,180,000.00 USD | 12,220,000.00 USD | 1,710,000.00 USD | 2,710,000.00 USD |
| `7D` | `2226.10` | 373,990,000.00 USD | 0.00 USD | 373,990,000.00 USD | 9,390,000.00 USD | 15,470,000.00 USD | 13,580,000.00 USD |
| `1D` | `2227.60` | 196,550,000.00 USD | 0.00 USD | 196,550,000.00 USD | 10,780,000.00 USD | 10,690,000.00 USD | 1,080,000.00 USD |
| `7D` | `2229.40` | 335,550,000.00 USD | 0.00 USD | 335,550,000.00 USD | 47,950,000.00 USD | 33,560,000.00 USD | 21,030,000.00 USD |
| `1D` | `2230.10` | 173,990,000.00 USD | 0.00 USD | 173,990,000.00 USD | 35,750,000.00 USD | 5,630,000.00 USD | 7,470,000.00 USD |
| `1D` | `2232.60` | 125,130,000.00 USD | 0.00 USD | 125,130,000.00 USD | 26,640,000.00 USD | 6,600,000.00 USD | 21,520,000.00 USD |
| `7D` | `2232.70` | 233,010,000.00 USD | 0.00 USD | 233,010,000.00 USD | 24,580,000.00 USD | 46,390,000.00 USD | 28,000,000.00 USD |
| `1D` | `2235.10` | 70,370,000.00 USD | 0.00 USD | 70,370,000.00 USD | 22,090,000.00 USD | 0.00 USD | 21,830,000.00 USD |
| `7D` | `2236.00` | 134,040,000.00 USD | 0.00 USD | 134,040,000.00 USD | 30,150,000.00 USD | 23,260,000.00 USD | 26,480,000.00 USD |
| `1D` | `2237.60` | 26,450,000.00 USD | 0.00 USD | 26,450,000.00 USD | 8,000,000.00 USD | 0.00 USD | 1,720,000.00 USD |
| `7D` | `2239.30` | 54,150,000.00 USD | 0.00 USD | 54,150,000.00 USD | 39,050,000.00 USD | 0.00 USD | 8,330,000.00 USD |
| `1D` | `2240.10` | 16,730,000.00 USD | 0.00 USD | 16,730,000.00 USD | 7,530,000.00 USD | 0.00 USD | 5,940,000.00 USD |
| `1D` | `2242.60` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 0.00 USD | 711,240.00 USD | 50,930.00 USD |
| `7D` | `2242.60` | 6,760,000.00 USD | 0.00 USD | 6,760,000.00 USD | 6,760,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2245.10` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 82,400.00 USD | 2,270,000.00 USD | 148,420.00 USD |
| `7D` | `2245.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2245.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2245.90` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 2,070,000.00 USD | 1,030,000.00 USD | 102,060.00 USD |
| `1D` | `2247.60` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 1,330,000.00 USD | 773,950.00 USD | 1,350,000.00 USD |
| `7D` | `2249.20` | 10,470,000.00 USD | 10,470,000.00 USD | 0.00 USD | 3,350,000.00 USD | 2,660,000.00 USD | 1,250,000.00 USD |
| `1D` | `2250.10` | 20,550,000.00 USD | 20,550,000.00 USD | 0.00 USD | 9,110,000.00 USD | 7,940,000.00 USD | 55,780.00 USD |
| `7D` | `2252.50` | 40,270,000.00 USD | 40,270,000.00 USD | 0.00 USD | 20,930,000.00 USD | 8,880,000.00 USD | 0.00 USD |
| `1D` | `2252.60` | 33,030,000.00 USD | 33,030,000.00 USD | 0.00 USD | 7,890,000.00 USD | 3,320,000.00 USD | 1,270,000.00 USD |
| `1D` | `2255.10` | 52,830,000.00 USD | 52,830,000.00 USD | 0.00 USD | 8,570,000.00 USD | 8,490,000.00 USD | 2,740,000.00 USD |
| `7D` | `2255.80` | 58,310,000.00 USD | 58,310,000.00 USD | 0.00 USD | 7,010,000.00 USD | 10,520,000.00 USD | 514,610.00 USD |
| `1D` | `2257.60` | 78,970,000.00 USD | 78,970,000.00 USD | 0.00 USD | 15,520,000.00 USD | 6,780,000.00 USD | 3,840,000.00 USD |
| `7D` | `2259.10` | 88,610,000.00 USD | 88,610,000.00 USD | 0.00 USD | 18,800,000.00 USD | 7,450,000.00 USD | 4,040,000.00 USD |
| `1D` | `2260.10` | 98,900,000.00 USD | 98,900,000.00 USD | 0.00 USD | 8,800,000.00 USD | 9,260,000.00 USD | 1,870,000.00 USD |
| `7D` | `2262.40` | 96,990,000.00 USD | 96,990,000.00 USD | 0.00 USD | 6,720,000.00 USD | 1,460,000.00 USD | 210,470.00 USD |
| `1D` | `2262.60` | 119,130,000.00 USD | 119,130,000.00 USD | 0.00 USD | 12,430,000.00 USD | 4,850,000.00 USD | 2,960,000.00 USD |
| `1D` | `2265.10` | 141,110,000.00 USD | 141,110,000.00 USD | 0.00 USD | 7,350,000.00 USD | 9,080,000.00 USD | 5,560,000.00 USD |
| `7D` | `2265.70` | 103,320,000.00 USD | 103,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,330,000.00 USD |
| `1D` | `2267.60` | 160,020,000.00 USD | 160,020,000.00 USD | 0.00 USD | 8,550,000.00 USD | 4,670,000.00 USD | 5,690,000.00 USD |
| `7D` | `2269.00` | 117,590,000.00 USD | 117,590,000.00 USD | 0.00 USD | 8,610,000.00 USD | 5,650,000.00 USD | 0.00 USD |
| `1D` | `2270.10` | 172,580,000.00 USD | 172,580,000.00 USD | 0.00 USD | 6,330,000.00 USD | 2,910,000.00 USD | 3,320,000.00 USD |
| `7D` | `2272.30` | 126,610,000.00 USD | 126,610,000.00 USD | 0.00 USD | 7,540,000.00 USD | 1,480,000.00 USD | 0.00 USD |
| `1D` | `2272.60` | 172,940,000.00 USD | 172,940,000.00 USD | 0.00 USD | 138,720.00 USD | 216,810.00 USD | 0.00 USD |
| `1D` | `2275.10` | 199,340,000.00 USD | 199,340,000.00 USD | 0.00 USD | 12,750,000.00 USD | 12,270,000.00 USD | 1,390,000.00 USD |
| `7D` | `2275.60` | 132,110,000.00 USD | 132,110,000.00 USD | 0.00 USD | 0.00 USD | 5,500,000.00 USD | 0.00 USD |
| `1D` | `2277.60` | 221,140,000.00 USD | 221,140,000.00 USD | 0.00 USD | 3,520,000.00 USD | 11,950,000.00 USD | 6,320,000.00 USD |
| `7D` | `2278.90` | 156,050,000.00 USD | 156,050,000.00 USD | 0.00 USD | 854,200.00 USD | 12,550,000.00 USD | 10,540,000.00 USD |
| `1D` | `2280.10` | 269,620,000.00 USD | 269,620,000.00 USD | 0.00 USD | 27,000,000.00 USD | 10,430,000.00 USD | 11,050,000.00 USD |
| `7D` | `2282.20` | 253,600,000.00 USD | 253,600,000.00 USD | 0.00 USD | 0.00 USD | 83,870,000.00 USD | 13,670,000.00 USD |
| `1D` | `2282.60` | 331,330,000.00 USD | 331,330,000.00 USD | 0.00 USD | 25,620,000.00 USD | 29,040,000.00 USD | 7,040,000.00 USD |
| `1D` | `2285.10` | 357,190,000.00 USD | 357,190,000.00 USD | 0.00 USD | 11,240,000.00 USD | 8,450,000.00 USD | 6,170,000.00 USD |
| `7D` | `2285.50` | 287,260,000.00 USD | 287,260,000.00 USD | 0.00 USD | 6,610,000.00 USD | 26,950,000.00 USD | 105,230.00 USD |
| `1D` | `2287.60` | 385,160,000.00 USD | 385,160,000.00 USD | 0.00 USD | 14,080,000.00 USD | 7,330,000.00 USD | 6,560,000.00 USD |
| `7D` | `2288.80` | 318,710,000.00 USD | 318,710,000.00 USD | 0.00 USD | 8,380,000.00 USD | 8,140,000.00 USD | 14,930,000.00 USD |
| `1D` | `2290.10` | 413,210,000.00 USD | 413,210,000.00 USD | 0.00 USD | 13,750,000.00 USD | 12,430,000.00 USD | 1,870,000.00 USD |
| `7D` | `2292.10` | 327,780,000.00 USD | 327,780,000.00 USD | 0.00 USD | 7,890,000.00 USD | 517,070.00 USD | 658,480.00 USD |
| `1D` | `2292.60` | 432,800,000.00 USD | 432,800,000.00 USD | 0.00 USD | 12,380,000.00 USD | 2,980,000.00 USD | 4,230,000.00 USD |
| `1D` | `2295.10` | 456,720,000.00 USD | 456,720,000.00 USD | 0.00 USD | 4,970,000.00 USD | 10,960,000.00 USD | 7,980,000.00 USD |
| `7D` | `2295.40` | 364,250,000.00 USD | 364,250,000.00 USD | 0.00 USD | 22,930,000.00 USD | 6,820,000.00 USD | 6,720,000.00 USD |
| `1D` | `2297.60` | 494,420,000.00 USD | 494,420,000.00 USD | 0.00 USD | 22,220,000.00 USD | 10,280,000.00 USD | 5,200,000.00 USD |
| `7D` | `2298.70` | 387,090,000.00 USD | 387,090,000.00 USD | 0.00 USD | 897,290.00 USD | 11,270,000.00 USD | 10,670,000.00 USD |
| `1D` | `2300.10` | 530,190,000.00 USD | 530,190,000.00 USD | 0.00 USD | 9,490,000.00 USD | 14,360,000.00 USD | 11,920,000.00 USD |
| `7D` | `2302.00` | 462,400,000.00 USD | 462,400,000.00 USD | 0.00 USD | 29,960,000.00 USD | 23,280,000.00 USD | 22,080,000.00 USD |
| `1D` | `2302.60` | 560,490,000.00 USD | 560,490,000.00 USD | 0.00 USD | 18,720,000.00 USD | 2,700,000.00 USD | 8,880,000.00 USD |
| `1D` | `2305.10` | 599,220,000.00 USD | 599,220,000.00 USD | 0.00 USD | 14,970,000.00 USD | 17,660,000.00 USD | 6,110,000.00 USD |
| `7D` | `2305.30` | 497,570,000.00 USD | 497,570,000.00 USD | 0.00 USD | 17,280,000.00 USD | 6,960,000.00 USD | 10,920,000.00 USD |
| `1D` | `2307.60` | 611,280,000.00 USD | 611,280,000.00 USD | 0.00 USD | 4,370,000.00 USD | 4,480,000.00 USD | 3,210,000.00 USD |
| `7D` | `2308.60` | 501,810,000.00 USD | 501,810,000.00 USD | 0.00 USD | 1,240,000.00 USD | 2,780,000.00 USD | 231,420.00 USD |
| `1D` | `2310.10` | 629,570,000.00 USD | 629,570,000.00 USD | 0.00 USD | 4,910,000.00 USD | 2,720,000.00 USD | 10,660,000.00 USD |
| `7D` | `2311.90` | 532,050,000.00 USD | 532,050,000.00 USD | 0.00 USD | 11,460,000.00 USD | 2,650,000.00 USD | 16,120,000.00 USD |
| `1D` | `2312.60` | 641,330,000.00 USD | 641,330,000.00 USD | 0.00 USD | 5,030,000.00 USD | 6,600,000.00 USD | 135,490.00 USD |
| `1D` | `2315.10` | 658,950,000.00 USD | 658,950,000.00 USD | 0.00 USD | 4,800,000.00 USD | 11,700,000.00 USD | 1,120,000.00 USD |
| `7D` | `2315.20` | 540,800,000.00 USD | 540,800,000.00 USD | 0.00 USD | 0.00 USD | 8,120,000.00 USD | 627,210.00 USD |
| `1D` | `2317.60` | 683,220,000.00 USD | 683,220,000.00 USD | 0.00 USD | 6,110,000.00 USD | 10,220,000.00 USD | 7,940,000.00 USD |
| `7D` | `2318.50` | 555,730,000.00 USD | 555,730,000.00 USD | 0.00 USD | 4,540,000.00 USD | 4,550,000.00 USD | 5,830,000.00 USD |
| `1D` | `2320.10` | 707,020,000.00 USD | 707,020,000.00 USD | 0.00 USD | 9,790,000.00 USD | 11,280,000.00 USD | 2,740,000.00 USD |
| `7D` | `2321.80` | 575,470,000.00 USD | 575,470,000.00 USD | 0.00 USD | 1,110,000.00 USD | 15,930,000.00 USD | 2,690,000.00 USD |
| `1D` | `2322.60` | 720,820,000.00 USD | 720,820,000.00 USD | 0.00 USD | 1,730,000.00 USD | 8,480,000.00 USD | 3,590,000.00 USD |
| `1D` | `2325.10` | 733,230,000.00 USD | 733,230,000.00 USD | 0.00 USD | 1,950,000.00 USD | 8,990,000.00 USD | 1,470,000.00 USD |
| `7D` | `2325.10` | 596,540,000.00 USD | 596,540,000.00 USD | 0.00 USD | 10,150,000.00 USD | 2,540,000.00 USD | 8,390,000.00 USD |
| `1D` | `2327.60` | 739,120,000.00 USD | 739,120,000.00 USD | 0.00 USD | 363,810.00 USD | 1,140,000.00 USD | 4,390,000.00 USD |
| `7D` | `2328.40` | 608,540,000.00 USD | 608,540,000.00 USD | 0.00 USD | 3,860,000.00 USD | 121,880.00 USD | 8,020,000.00 USD |
| `1D` | `2330.10` | 755,060,000.00 USD | 755,060,000.00 USD | 0.00 USD | 12,640,000.00 USD | 2,830,000.00 USD | 472,010.00 USD |
| `7D` | `2331.70` | 638,020,000.00 USD | 638,020,000.00 USD | 0.00 USD | 29,230,000.00 USD | 241,890.00 USD | 0.00 USD |
| `1D` | `2332.60` | 773,970,000.00 USD | 773,970,000.00 USD | 0.00 USD | 12,420,000.00 USD | 1,230,000.00 USD | 5,260,000.00 USD |
| `7D` | `2335.00` | 690,280,000.00 USD | 690,280,000.00 USD | 0.00 USD | 20,390,000.00 USD | 19,830,000.00 USD | 12,040,000.00 USD |
| `1D` | `2335.10` | 792,860,000.00 USD | 792,860,000.00 USD | 0.00 USD | 10,810,000.00 USD | 3,850,000.00 USD | 4,230,000.00 USD |
| `1D` | `2337.60` | 807,940,000.00 USD | 807,940,000.00 USD | 0.00 USD | 11,300,000.00 USD | 779,680.00 USD | 3,000,000.00 USD |
| `7D` | `2338.30` | 720,840,000.00 USD | 720,840,000.00 USD | 0.00 USD | 22,110,000.00 USD | 0.00 USD | 8,450,000.00 USD |
| `1D` | `2340.10` | 831,860,000.00 USD | 831,860,000.00 USD | 0.00 USD | 8,010,000.00 USD | 5,120,000.00 USD | 10,780,000.00 USD |
| `7D` | `2341.60` | 757,370,000.00 USD | 757,370,000.00 USD | 0.00 USD | 4,720,000.00 USD | 17,820,000.00 USD | 14,000,000.00 USD |
| `1D` | `2342.60` | 843,820,000.00 USD | 843,820,000.00 USD | 0.00 USD | 5,180,000.00 USD | 4,030,000.00 USD | 2,750,000.00 USD |
| `7D` | `2344.90` | 784,220,000.00 USD | 784,220,000.00 USD | 0.00 USD | 1,350,000.00 USD | 16,920,000.00 USD | 8,580,000.00 USD |
| `1D` | `2345.10` | 865,030,000.00 USD | 865,030,000.00 USD | 0.00 USD | 4,550,000.00 USD | 7,950,000.00 USD | 8,700,000.00 USD |
| `1D` | `2347.60` | 873,090,000.00 USD | 873,090,000.00 USD | 0.00 USD | 1,960,000.00 USD | 3,520,000.00 USD | 2,590,000.00 USD |
| `7D` | `2348.20` | 820,340,000.00 USD | 820,340,000.00 USD | 0.00 USD | 561,950.00 USD | 12,390,000.00 USD | 23,170,000.00 USD |
| `1D` | `2350.10` | 918,850,000.00 USD | 918,850,000.00 USD | 0.00 USD | 28,790,000.00 USD | 6,880,000.00 USD | 10,080,000.00 USD |
| `7D` | `2351.50` | 859,010,000.00 USD | 859,010,000.00 USD | 0.00 USD | 2,930,000.00 USD | 20,680,000.00 USD | 15,060,000.00 USD |
| `1D` | `2352.60` | 930,320,000.00 USD | 930,320,000.00 USD | 0.00 USD | 5,380,000.00 USD | 3,400,000.00 USD | 2,690,000.00 USD |
| `7D` | `2354.80` | 915,860,000.00 USD | 915,860,000.00 USD | 0.00 USD | 17,130,000.00 USD | 38,220,000.00 USD | 1,500,000.00 USD |
| `1D` | `2355.10` | 946,360,000.00 USD | 946,360,000.00 USD | 0.00 USD | 2,410,000.00 USD | 12,010,000.00 USD | 1,620,000.00 USD |
| `1D` | `2357.60` | 957,990,000.00 USD | 957,990,000.00 USD | 0.00 USD | 3,860,000.00 USD | 4,290,000.00 USD | 3,480,000.00 USD |
| `7D` | `2358.10` | 933,010,000.00 USD | 933,010,000.00 USD | 0.00 USD | 7,110,000.00 USD | 4,040,000.00 USD | 6,010,000.00 USD |
| `1D` | `2360.10` | 976,970,000.00 USD | 976,970,000.00 USD | 0.00 USD | 9,250,000.00 USD | 4,260,000.00 USD | 5,480,000.00 USD |
| `7D` | `2361.40` | 941,290,000.00 USD | 941,290,000.00 USD | 0.00 USD | 4,470,000.00 USD | 3,430,000.00 USD | 374,770.00 USD |
| `1D` | `2362.60` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 0.00 USD | 9,140,000.00 USD | 6,710,000.00 USD | 7,950,000.00 USD |
| `7D` | `2364.70` | 957,160,000.00 USD | 957,160,000.00 USD | 0.00 USD | 4,570,000.00 USD | 373,740.00 USD | 10,920,000.00 USD |
| `1D` | `2365.10` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 0.00 USD | 4,830,000.00 USD | 3,140,000.00 USD | 3,680,000.00 USD |
| `1D` | `2367.60` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 0.00 USD | 3,090,000.00 USD | 1,110,000.00 USD | 1,990,000.00 USD |
| `7D` | `2368.00` | 970,990,000.00 USD | 970,990,000.00 USD | 0.00 USD | 11,660,000.00 USD | 1,780,000.00 USD | 396,420.00 USD |
| `1D` | `2370.10` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 13,080,000.00 USD | 9,420,000.00 USD | 7,020,000.00 USD |
| `7D` | `2371.30` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 25,000,000.00 USD | 0.00 USD | 54,480,000.00 USD |
| `1D` | `2372.60` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 0.00 USD | 14,360,000.00 USD | 3,280,000.00 USD | 7,730,000.00 USD |
| `7D` | `2374.60` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 0.00 USD | 19,920,000.00 USD | 121,480.00 USD | 6,980,000.00 USD |
| `1D` | `2375.10` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 8,950,000.00 USD | 2,300,000.00 USD | 1,840,000.00 USD |
| `1D` | `2377.60` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 4,110,000.00 USD | 4,760,000.00 USD | 4,820,000.00 USD |
| `7D` | `2377.90` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 11,180,000.00 USD | 6,190,000.00 USD | 29,810,000.00 USD |
| `1D` | `2380.10` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 6,310,000.00 USD | 880,980.00 USD | 4,780,000.00 USD |
| `7D` | `2381.20` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 4,540,000.00 USD | 4,150,000.00 USD | 19,270,000.00 USD |
| `1D` | `2382.60` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 15,650,000.00 USD | 14,510,000.00 USD | 11,550,000.00 USD |
| `7D` | `2384.50` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 22,580,000.00 USD | 22,660,000.00 USD | 45,970,000.00 USD |
| `1D` | `2385.10` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 7,540,000.00 USD | 11,520,000.00 USD | 4,750,000.00 USD |
| `1D` | `2387.60` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 9,850,000.00 USD | 5,970,000.00 USD | 3,120,000.00 USD |
| `7D` | `2387.80` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 5,540,000.00 USD | 49,830,000.00 USD | 47,300,000.00 USD |
| `1D` | `2390.10` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 4,390,000.00 USD | 3,310,000.00 USD | 1,520,000.00 USD |
| `7D` | `2391.10` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 0.00 USD | 5,910,000.00 USD | 52,770,000.00 USD | 41,810,000.00 USD |
| `1D` | `2392.60` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,660,000.00 USD | 3,320,000.00 USD |
| `7D` | `2394.40` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 60,000,000.00 USD | 32,420,000.00 USD | 40,070,000.00 USD |
| `1D` | `2395.10` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 2,430,000.00 USD | 2,830,000.00 USD | 2,190,000.00 USD |
| `1D` | `2397.60` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 169,460.00 USD | 4,290,000.00 USD | 3,410,000.00 USD |
| `7D` | `2397.70` | 1,680,000,000.00 USD | 1,680,000,000.00 USD | 0.00 USD | 31,080,000.00 USD | 41,130,000.00 USD | 26,250,000.00 USD |
| `1D` | `2400.10` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 3,260,000.00 USD | 1,820,000.00 USD | 2,600,000.00 USD |
| `7D` | `2401.00` | 1,780,000,000.00 USD | 1,780,000,000.00 USD | 0.00 USD | 51,130,000.00 USD | 28,060,000.00 USD | 25,770,000.00 USD |
| `1D` | `2402.60` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 3,880,000.00 USD | 2,480,000.00 USD | 825,510.00 USD |
| `7D` | `2404.30` | 1,900,000,000.00 USD | 1,900,000,000.00 USD | 0.00 USD | 61,130,000.00 USD | 29,350,000.00 USD | 31,410,000.00 USD |
| `1D` | `2405.10` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 0.00 USD | 7,750,000.00 USD | 6,890,000.00 USD | 5,200,000.00 USD |
| `1D` | `2407.60` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 0.00 USD | 10,210,000.00 USD | 5,620,000.00 USD | 3,320,000.00 USD |
| `7D` | `2407.60` | 1,990,000,000.00 USD | 1,990,000,000.00 USD | 0.00 USD | 29,050,000.00 USD | 35,150,000.00 USD | 19,040,000.00 USD |
| `1D` | `2410.10` | 1,300,000,000.00 USD | 1,300,000,000.00 USD | 0.00 USD | 5,260,000.00 USD | 4,440,000.00 USD | 4,640,000.00 USD |
| `7D` | `2410.90` | 2,070,000,000.00 USD | 2,070,000,000.00 USD | 0.00 USD | 25,670,000.00 USD | 27,460,000.00 USD | 31,240,000.00 USD |
| `1D` | `2412.60` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 0.00 USD | 7,690,000.00 USD | 3,810,000.00 USD | 2,420,000.00 USD |
| `7D` | `2414.20` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 0.00 USD | 21,950,000.00 USD | 25,190,000.00 USD | 22,860,000.00 USD |
| `1D` | `2415.10` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 0.00 USD | 2,960,000.00 USD | 2,950,000.00 USD | 2,900,000.00 USD |
| `7D` | `2417.50` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 0.00 USD | 31,300,000.00 USD | 13,490,000.00 USD | 24,160,000.00 USD |
| `1D` | `2417.60` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 3,340,000.00 USD | 2,420,000.00 USD | 2,820,000.00 USD |
| `1D` | `2420.10` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 6,880,000.00 USD | 3,710,000.00 USD | 3,680,000.00 USD |
| `7D` | `2420.80` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 32,960,000.00 USD | 26,760,000.00 USD | 16,800,000.00 USD |
| `1D` | `2422.60` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 1,770,000.00 USD | 3,880,000.00 USD | 4,560,000.00 USD |
| `7D` | `2424.10` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 20,380,000.00 USD | 29,890,000.00 USD | 23,700,000.00 USD |
| `1D` | `2425.10` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 0.00 USD | 510,650.00 USD | 1,610,000.00 USD | 888,640.00 USD |
| `7D` | `2427.40` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 0.00 USD | 22,390,000.00 USD | 17,570,000.00 USD | 20,240,000.00 USD |
| `1D` | `2427.60` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 0.00 USD | 2,250,000.00 USD | 1,520,000.00 USD | 603,040.00 USD |
| `1D` | `2430.10` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 1,370,000.00 USD | 1,550,000.00 USD | 1,350,000.00 USD |
| `7D` | `2430.70` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 0.00 USD | 8,890,000.00 USD | 15,370,000.00 USD | 9,660,000.00 USD |
| `1D` | `2432.60` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 2,770,000.00 USD | 2,230,000.00 USD | 691,800.00 USD |
| `7D` | `2434.00` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 0.00 USD | 19,530,000.00 USD | 9,570,000.00 USD | 13,090,000.00 USD |
| `1D` | `2435.10` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 0.00 USD | 2,480,000.00 USD | 559,660.00 USD | 1,370,000.00 USD |
| `7D` | `2437.30` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 0.00 USD | 15,680,000.00 USD | 15,080,000.00 USD | 6,290,000.00 USD |
| `1D` | `2437.60` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 0.00 USD | 1,360,000.00 USD | 1,040,000.00 USD | 30,250.00 USD |
| `1D` | `2440.10` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 0.00 USD | 1,240,000.00 USD | 502,040.00 USD | 304,820.00 USD |
| `7D` | `2440.60` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 0.00 USD | 16,940,000.00 USD | 10,790,000.00 USD | 9,240,000.00 USD |
| `1D` | `2442.60` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 0.00 USD | 1,030,000.00 USD | 700,830.00 USD | 819,120.00 USD |
| `7D` | `2443.90` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 0.00 USD | 5,830,000.00 USD | 13,790,000.00 USD | 8,020,000.00 USD |
| `1D` | `2445.10` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 0.00 USD | 0.00 USD | 486,350.00 USD | 1,140,000.00 USD |
| `7D` | `2447.20` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 0.00 USD | 13,820,000.00 USD | 7,510,000.00 USD | 16,330,000.00 USD |
| `1D` | `2447.60` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 472,100.00 USD | 485,550.00 USD | 687,270.00 USD |
| `1D` | `2450.10` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 335,910.00 USD | 56,170.00 USD | 26,770.00 USD |
| `7D` | `2450.50` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 0.00 USD | 10,570,000.00 USD | 11,560,000.00 USD | 10,410,000.00 USD |
| `1D` | `2452.60` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 2,730,000.00 USD | 1,820,000.00 USD | 2,240,000.00 USD |
| `7D` | `2453.80` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 0.00 USD | 7,240,000.00 USD | 4,290,000.00 USD | 6,910,000.00 USD |
| `1D` | `2455.10` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 2,270,000.00 USD | 1,660,000.00 USD | 905,110.00 USD |
| `7D` | `2457.10` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 0.00 USD | 8,340,000.00 USD | 8,890,000.00 USD | 7,910,000.00 USD |
| `1D` | `2457.60` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 1,290,000.00 USD | 1,810,000.00 USD | 479,530.00 USD |
| `1D` | `2460.10` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 1,510,000.00 USD | 1,350,000.00 USD | 384,500.00 USD |
| `7D` | `2460.40` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 0.00 USD | 7,080,000.00 USD | 8,140,000.00 USD | 9,350,000.00 USD |
| `1D` | `2462.60` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 303,600.00 USD | 521,540.00 USD | 829,050.00 USD |
| `7D` | `2463.70` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 0.00 USD | 9,430,000.00 USD | 8,280,000.00 USD | 6,170,000.00 USD |
| `1D` | `2465.10` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 404,950.00 USD | 897,320.00 USD | 336,380.00 USD |
| `7D` | `2467.00` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 4,840,000.00 USD | 2,920,000.00 USD | 1,330,000.00 USD |
| `1D` | `2467.60` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 288,920.00 USD | 752,230.00 USD | 213,900.00 USD |
| `1D` | `2470.10` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 973,110.00 USD | 1,190,000.00 USD | 537,210.00 USD |
| `7D` | `2470.30` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 0.00 USD | 3,190,000.00 USD | 3,080,000.00 USD | 496,280.00 USD |
| `1D` | `2472.60` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 308,280.00 USD |
| `7D` | `2473.60` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 0.00 USD | 5,860,000.00 USD | 2,920,000.00 USD | 2,270,000.00 USD |
| `1D` | `2475.10` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 0.00 USD | 914,780.00 USD | 0.00 USD |
| `1D` | `2475.60` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 0.00 USD | 185,860.00 USD | 0.00 USD |
| `7D` | `2476.90` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 0.00 USD | 2,660,000.00 USD | 2,410,000.00 USD | 872,130.00 USD |
| `7D` | `2480.20` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 0.00 USD | 1,580,000.00 USD | 6,190,000.00 USD | 1,590,000.00 USD |
| `7D` | `2483.50` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 0.00 USD | 1,750,000.00 USD | 2,280,000.00 USD | 77,610.00 USD |
| `7D` | `2486.80` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 0.00 USD | 30,880.00 USD | 0.00 USD | 1,350,000.00 USD |
| `7D` | `2490.10` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 0.00 USD | 1,480,000.00 USD | 1,850,000.00 USD | 188,520.00 USD |
| `7D` | `2493.40` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 3,210,000.00 USD | 1,830,000.00 USD | 1,960,000.00 USD |
| `7D` | `2496.70` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 1,370,000.00 USD | 3,690,000.00 USD | 4,660,000.00 USD |
| `7D` | `2500.00` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 358,770.00 USD | 1,980,000.00 USD | 1,170,000.00 USD |
| `7D` | `2503.30` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 0.00 USD | 27,220.00 USD | 125,600.00 USD |
| `7D` | `2506.60` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 2,540,000.00 USD | 903,900.00 USD | 1,990,000.00 USD |
| `7D` | `2509.90` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 2,290,000.00 USD | 2,160,000.00 USD | 1,190,000.00 USD |
| `7D` | `2516.50` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD |
| `7D` | `2519.80` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD |
| `7D` | `2523.10` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 1,230,000.00 USD | 249,960.00 USD | 945,860.00 USD |
| `7D` | `2526.40` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 292,400.00 USD | 1,090,000.00 USD | 200,040.00 USD |
| `7D` | `2529.70` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 0.00 USD | 1,510,000.00 USD | 2,770,000.00 USD | 1,300,000.00 USD |
| `7D` | `2533.00` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 0.00 USD | 4,460,000.00 USD | 1,850,000.00 USD | 1,550,000.00 USD |
| `7D` | `2536.30` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 0.00 USD | 3,170,000.00 USD | 2,460,000.00 USD | 4,010,000.00 USD |
| `7D` | `2539.60` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 0.00 USD | 4,190,000.00 USD | 3,730,000.00 USD | 1,140,000.00 USD |
| `7D` | `2542.90` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 0.00 USD | 4,070,000.00 USD | 2,950,000.00 USD | 2,920,000.00 USD |
| `7D` | `2546.20` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 0.00 USD | 1,900,000.00 USD | 1,140,000.00 USD | 1,850,000.00 USD |
| `7D` | `2549.50` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 0.00 USD | 4,150,000.00 USD | 3,470,000.00 USD | 4,160,000.00 USD |
| `7D` | `2552.80` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 0.00 USD | 1,920,000.00 USD | 580,780.00 USD | 1,140,000.00 USD |
| `7D` | `2556.10` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 0.00 USD | 4,340,000.00 USD | 549,010.00 USD | 7,010,000.00 USD |
| `7D` | `2559.40` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 5,200,000.00 USD | 1,660,000.00 USD | 2,340,000.00 USD |
| `7D` | `2562.70` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 1,940,000.00 USD | 3,320,000.00 USD | 1,290,000.00 USD |
| `7D` | `2566.00` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 0.00 USD | 1,880,000.00 USD | 1,520,000.00 USD | 2,070,000.00 USD |
| `7D` | `2569.30` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 0.00 USD | 125,250.00 USD | 739,480.00 USD | 2,000,000.00 USD |
| `7D` | `2572.60` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 890,480.00 USD | 2,220,000.00 USD |
| `7D` | `2575.90` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 0.00 USD | 2,180,000.00 USD | 440,740.00 USD | 1,090,000.00 USD |
| `7D` | `2579.20` | 2,970,000,000.00 USD | 2,970,000,000.00 USD | 0.00 USD | 1,870,000.00 USD | 1,940,000.00 USD | 1,730,000.00 USD |
| `7D` | `2582.50` | 2,970,000,000.00 USD | 2,970,000,000.00 USD | 0.00 USD | 2,830,000.00 USD | 1,030,000.00 USD | 3,720,000.00 USD |
| `7D` | `2585.80` | 2,980,000,000.00 USD | 2,980,000,000.00 USD | 0.00 USD | 883,660.00 USD | 2,700,000.00 USD | 1,870,000.00 USD |
| `7D` | `2589.10` | 2,990,000,000.00 USD | 2,990,000,000.00 USD | 0.00 USD | 2,540,000.00 USD | 536,380.00 USD | 2,830,000.00 USD |
| `7D` | `2590.30` | 2,990,000,000.00 USD | 2,990,000,000.00 USD | 0.00 USD | 1,180,000.00 USD | 304,000.00 USD | 447,590.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `29.15B` | Total OI Tokens: `12,982,893.4 ETH`
  * 1h OI Change: `+0.51%` | 4h OI Change: `+1.13%` | 24h OI Change: `-2.86%`
  * Exchange Breakdown: Binance=`8.48B` | Bybit=`2.09B` | OKX=`1.80B` | Hyperliquid=`2.36B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-192.20K` | Last 24h: `1.05M` | Last 3d: `6.29M` | Last 7d: `12.86M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0021%` | **USDT OKX** | `-0.0088%` |
| **USDT Bybit** | `-0.0163%` | **USDT KuCoin** | `-0.0107%` |
| **USDT MEXC** | `0.0020%` | **USDT BingX** | `0.0015%` |
| **USDT Gate** | `-0.0121%` | **USDT Bitget** | `-0.0004%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0062%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `49.80%` | `50.20%` | `0.99` | 540,960,000.00 USD |
| `15M` | `Binance` | `50.95%` | `49.05%` | `1.04` | 174,140,000.00 USD |
| `15M` | `OKX` | `42.62%` | `57.38%` | `0.74` | 80,400,000.00 USD |
| `15M` | `Bybit` | `51.2%` | `48.8%` | `1.05` | 41,050,000.00 USD |
| `15M` | `KuCoin` | `54.81%` | `45.19%` | `1.21` | 1,280,000.00 USD |
| `15M` | `Gate` | `45%` | `55%` | `0.82` | 59,100,000.00 USD |
| `15M` | `Bitget` | `42.89%` | `57.11%` | `0.75` | 33,450,000.00 USD |
| `15M` | `BingX` | `45.09%` | `54.91%` | `0.82` | 8,910,000.00 USD |
| `15M` | `MEXC` | `47.05%` | `52.95%` | `0.89` | 26,480,000.00 USD |
| `15M` | `Bitunix` | `53.22%` | `46.78%` | `1.14` | 35,460,000.00 USD |
| `15M` | `Hyperliquid` | `68.49%` | `31.51%` | `2.17` | 46,520,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `53.41%` | `46.59%` | `1.15` | 2,900,000.00 USD |
| `15M` | `Crypto.com` | `59.24%` | `40.76%` | `1.45` | 1,040,000.00 USD |
| `15M` | `WhiteBIT` | `3.8%` | `96.2%` | `0.04` | 129,760.00 USD |
| `15M` | `HTX` | `46.77%` | `53.23%` | `0.88` | 2,090,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `48.43%` | `51.57%` | `0.94` | 18,910,000.00 USD |
| `15M` | `Bitfinex` | `52.11%` | `47.89%` | `1.09` | 92,660.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `48.18%` | `51.82%` | `0.93` | 4,480,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `44.55%` | `55.45%` | `0.80` | 4,530,000.00 USD |
| `15M` | `Whale Positions` | `50.95%` | `49.05%` | `1.04` | 174,140,000.00 USD |
| `15M` | `Global Accounts` | `49.80%` | `50.20%` | `0.99` | 540,960,000.00 USD |
| `1H` | `ETH` | `51.87%` | `48.13%` | `1.08` | 2,990,000,000.00 USD |
| `1H` | `Binance` | `51.71%` | `48.29%` | `1.07` | 944,800,000.00 USD |
| `1H` | `OKX` | `50.14%` | `49.86%` | `1.01` | 418,640,000.00 USD |
| `1H` | `Bybit` | `54.84%` | `45.16%` | `1.21` | 278,970,000.00 USD |
| `1H` | `KuCoin` | `62.47%` | `37.53%` | `1.66` | 8,100,000.00 USD |
| `1H` | `Gate` | `46.11%` | `53.89%` | `0.86` | 305,030,000.00 USD |
| `1H` | `Bitget` | `50.24%` | `49.76%` | `1.01` | 188,460,000.00 USD |
| `1H` | `BingX` | `47.9%` | `52.1%` | `0.92` | 47,440,000.00 USD |
| `1H` | `MEXC` | `48.16%` | `51.84%` | `0.93` | 135,010,000.00 USD |
| `1H` | `Bitunix` | `49.76%` | `50.24%` | `0.99` | 159,900,000.00 USD |
| `1H` | `Hyperliquid` | `50.88%` | `49.12%` | `1.04` | 226,510,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `71.77%` | `28.23%` | `2.54` | 45,630,000.00 USD |
| `1H` | `Crypto.com` | `51.51%` | `48.49%` | `1.06` | 8,190,000.00 USD |
| `1H` | `WhiteBIT` | `97.41%` | `2.59%` | `37.61` | 61,630,000.00 USD |
| `1H` | `HTX` | `48.17%` | `51.83%` | `0.93` | 10,920,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `49.77%` | `50.23%` | `0.99` | 87,150,000.00 USD |
| `1H` | `Bitfinex` | `59.15%` | `40.85%` | `1.45` | 1,140,000.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `50.25%` | `49.75%` | `1.01` | 27,800,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `46.78%` | `53.22%` | `0.88` | 36,080,000.00 USD |
| `1H` | `Whale Positions` | `51.71%` | `48.29%` | `1.07` | 944,800,000.00 USD |
| `1H` | `Global Accounts` | `51.87%` | `48.13%` | `1.08` | 2,990,000,000.00 USD |
| `4H` | `ETH` | `52.37%` | `47.63%` | `1.10` | 16,600,000,000.00 USD |
| `4H` | `Binance` | `51.19%` | `48.81%` | `1.05` | 5,140,000,000.00 USD |
| `4H` | `OKX` | `51.13%` | `48.87%` | `1.05` | 2,330,000,000.00 USD |
| `4H` | `Bybit` | `53.45%` | `46.55%` | `1.15` | 1,570,000,000.00 USD |
| `4H` | `KuCoin` | `59.52%` | `40.48%` | `1.47` | 57,690,000.00 USD |
| `4H` | `Gate` | `48.47%` | `51.53%` | `0.94` | 1,800,000,000.00 USD |
| `4H` | `Bitget` | `49.48%` | `50.52%` | `0.98` | 808,420,000.00 USD |
| `4H` | `BingX` | `48.91%` | `51.09%` | `0.96` | 225,040,000.00 USD |
| `4H` | `MEXC` | `47.13%` | `52.87%` | `0.89` | 693,130,000.00 USD |
| `4H` | `Bitunix` | `52.1%` | `47.9%` | `1.09` | 748,740,000.00 USD |
| `4H` | `Hyperliquid` | `55.17%` | `44.83%` | `1.23` | 1,180,000,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `64.72%` | `35.28%` | `1.83` | 114,630,000.00 USD |
| `4H` | `Crypto.com` | `50.45%` | `49.55%` | `1.02` | 58,820,000.00 USD |
| `4H` | `WhiteBIT` | `75.21%` | `24.79%` | `3.03` | 808,480,000.00 USD |
| `4H` | `HTX` | `49.65%` | `50.35%` | `0.99` | 68,000,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `50.78%` | `49.22%` | `1.03` | 604,520,000.00 USD |
| `4H` | `Bitfinex` | `56.74%` | `43.26%` | `1.31` | 13,430,000.00 USD |
| `4H` | `Kraken` | `46.18%` | `53.82%` | `0.86` | 39,770,000.00 USD |
| `4H` | `Aster` | `50.67%` | `49.33%` | `1.03` | 161,200,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `47.91%` | `52.09%` | `0.92` | 169,030,000.00 USD |
| `4H` | `Whale Positions` | `51.19%` | `48.81%` | `1.05` | 5,140,000,000.00 USD |
| `4H` | `Global Accounts` | `52.37%` | `47.63%` | `1.10` | 16,600,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `2217.25` | `2215.50` | `2217.25` | `2218.75` | `2209.75` | 102,137,358.80 USD | 50,758,296.06 USD | 51,379,062.74 USD | -620,766.68 USD | `-0.61%` | `0B / 3S` |
| `5:00 UTC` | `2208.25` | `2209.85` | `2208.25` | `2215.75` | `2207.25` | 69,365,754.50 USD | 25,046,876.87 USD | 44,318,877.64 USD | -19,272,000.77 USD | `-27.78%` | `0B / 4S` |
| `0:00 UTC` | `2215.25` | `2214.70` | `2215.25` | `2218.75` | `2208.25` | 100,318,327.91 USD | 51,517,721.13 USD | 48,800,606.78 USD | 2,717,114.35 USD | `+2.71%` | `2B / 2S` |
| `5:00 UTC` | `2219.75` | `2216.05` | `2219.75` | `2221.25` | `2210.25` | 81,002,689.38 USD | 47,369,805.78 USD | 33,632,883.60 USD | 13,736,922.17 USD | `+16.96%` | `0B / 0S` |
| `0:00 UTC` | `2229.75` | `2226.55` | `2229.75` | `2232.75` | `2219.75` | 182,767,345.67 USD | 98,774,699.85 USD | 83,992,645.82 USD | 14,782,054.04 USD | `+8.09%` | `1B / 2S` |
| `5:00 UTC` | `2234.75` | `2234.69` | `2234.75` | `2238.25` | `2230.25` | 138,036,296.36 USD | 70,500,947.16 USD | 67,535,349.20 USD | 2,965,597.96 USD | `+2.15%` | `1B / 0S` |
| `0:00 UTC` | `2229.75` | `2230.64` | `2229.75` | `2236.75` | `2225.25` | 125,588,915.24 USD | 57,499,740.21 USD | 68,089,175.03 USD | -10,589,434.83 USD | `-8.43%` | `0B / 2S` |
| `5:00 UTC` | `2241.25` | `2240.18` | `2241.25` | `2243.25` | `2233.75` | 123,392,803.54 USD | 67,738,859.18 USD | 55,653,944.36 USD | 12,084,914.83 USD | `+9.79%` | `1B / 2S` |
| `0:00 UTC` | `2245.25` | `2244.67` | `2245.25` | `2246.25` | `2242.75` | 130,536,562.11 USD | 61,753,972.34 USD | 68,782,589.78 USD | -7,028,617.44 USD | `-5.38%` | `0B / 0S` |
| `5:00 UTC` | `2246.25` | `2245.62` | `2246.25` | `2246.75` | `2243.75` | 40,659,061.75 USD | 22,793,895.40 USD | 17,865,166.35 USD | 4,928,729.06 USD | `+12.12%` | `0B / 0S` |

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
| `5m` | -579,230.00 USD | -781,050.00 USD | **`DISTRIBUTION`** |
| `15m` | 1,790,000.00 USD | -6,920,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -4,440,000.00 USD | -5,880,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -8,440,000.00 USD | 11,770,000.00 USD | **`ACCUMULATION`** |
| `2h` | 5,860,000.00 USD | 111,220,000.00 USD | **`ACCUMULATION`** |
| `4h` | -30,570,000.00 USD | -129,660,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -59,740,000.00 USD | -573,100,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -73,170,000.00 USD | -1,760,000,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -161,380,000.00 USD | -1,970,000,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -131,270,000.00 USD | -2,000,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -159,110,000.00 USD | -3,000,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,160,000,000.00 USD | -9,680,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-579.23K` | 15m=`+1.79M` | 1h=`-8.44M` | 24h=`-131.27M`
* Futures Capital Netflows: 5m=`-781.05K` | 15m=`-6.92M` | 1h=`+11.77M` | 24h=`-2.00B`
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
  * `2026-10-30 09:51:07 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:19:07 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:21:07 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:21:07 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `2207.76` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2181.84` (Risk Distance: `25.92` pts)
  * +2.5R Take Profit: `2272.55`
  * Mathematical Lot Sizing: **`0.38 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2280.60` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2306.52` (Risk Distance: `25.92` pts)
  * +2.5R Take Profit: `2215.81`
  * Mathematical Lot Sizing: **`0.38 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2258.83`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
