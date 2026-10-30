# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 10:37:50 IST` (`2026-10-30 05:07:50 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2237.50` | **Live Ask Quote**: `2241.20` | **Mid Price**: `2239.35`
- **Spread Points**: `370.00` | **Spread BPS**: `16.52 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2212.02` | VWAP Z-Score: `+1.60` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `16.32` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `51.05` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2257.67` | Lower -3.00σ Band: `2166.37`
  * Upper +2.51σ Band: `2250.21` | Lower -2.51σ Band: `2173.82`
  * Upper +2.01σ Band: `2242.60` | Lower -2.01σ Band: `2181.43`
  * Upper +2.00σ Band: `2242.45` | Lower -2.00σ Band: `2181.59`
  * Upper +1.28σ Band: `2231.50` | Lower -1.28σ Band: `2192.54`
  * Upper +1.00σ Band: `2227.23` | Lower -1.00σ Band: `2196.80`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2227.95` | EMA-20=`2228.75` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2255.12` (Slope: `+0.0000`) | EMA-100=`2281.85`
  * Institutional Anchors: EMA-144=`2293.76` | EMA-200=`2303.01` (Slope: `-0.4550`) | EMA-233=`2308.02`
- **Range Boundaries**: 24H High=`2374.90` | 24H Low=`2167.70` | Weekly High=`2387.80` | Weekly Low=`2167.70`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2280.60` (Distance: `-1.76%`)
  * Point of Control (POC) = `2264.42` (Distance: `-1.06%`)
  * Value Area Low (VAL) = `2208.57` (Distance: `+1.44%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2339.52` | POC=`2321.58` | VAL=`2296.66`
  * Prior Day Extremes: PDH=`2374.90` | PDL=`2225.40` | PDC=`2252.70`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2351.85` | Weekly POC=`2309.30` | Weekly VAL=`2300.49`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2289.10` | Low=`2167.70`
  * London Session (08:00-16:00 UTC): High=`2241.60` | Low=`2235.00`
  * New York Session (13:00-21:00 UTC): High=`2252.79` | Low=`2225.91`
  * Initial Balance (First Hour): IB High=`2241.60` | IB Low=`2235.00`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2230.39` - `2248.31`
  * Optimal Trade Entry (OTE 0.705): `2243.83`
  * Structural Invalidation Anchor (0.786): `2257.26`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2245.94` | `2246.94` | `2243.62` | `2245.26` | `13,604` | 30,547,061.72 USD | 2,311,786.48 USD | `+7.57%` | -1,033,797,567.33 USD | `+0.15` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `2245.25` | `2245.26` | `2241.38` | `2242.81` | `14,248` | 31,958,562.75 USD | 1,427,156.66 USD | `+4.47%` | -1,032,370,410.67 USD | `+0.03` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `2242.81` | `2248.08` | `2241.55` | `2244.49` | `13,733` | 30,827,023.62 USD | 2,253,910.56 USD | `+7.31%` | -1,030,116,500.11 USD | `+0.18` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `2243.26` | `2246.30` | `2242.57` | `2245.14` | `58,155` | 130,536,562.11 USD | -7,028,617.44 USD | `-5.38%` | -1,070,290,499.21 USD | `+0.17` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `2245.13` | `2246.94` | `2241.38` | `2242.81` | `37,225` | 83,556,134.35 USD | 4,187,969.92 USD | `+5.01%` | -1,066,102,529.29 USD | `+0.40` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `2242.81` | `2248.08` | `2241.55` | `2244.30` | `13,647` | 30,633,945.58 USD | 2,295,958.46 USD | `+7.49%` | -1,063,806,570.83 USD | `+0.32` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `2209.27` | `2238.00` | `2208.12` | `2236.82` | `225,707` | 502,124,659.31 USD | 34,201,688.52 USD | `+6.81%` | -1,027,139,167.10 USD | `+0.73` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `2236.81` | `2246.94` | `2225.47` | `2242.81` | `206,764` | 463,074,415.24 USD | -1,345,167.52 USD | `-0.29%` | -1,028,484,334.62 USD | `+0.41` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `2242.81` | `2248.08` | `2241.55` | `2244.50` | `13,727` | 30,813,870.91 USD | 2,266,030.80 USD | `+7.35%` | -1,026,218,303.81 USD | `+0.44` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2252.34` | `2,564,135` | 5,830,064,162.53 USD | -554,237,569.32 USD | `-9.51%` | -701,515,761.74 USD | `-1.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -963,151,175.97 USD | `-0.31` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2248.08` | `2225.47` | `2244.30` | `220,412` | 493,708,360.81 USD | 950,790.94 USD | `+0.19%` | -962,200,385.03 USD | `+0.75` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | 54,877,924.52 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -147,278,192.42 USD | `-1.22` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2252.34` | `2,564,135` | 5,830,064,162.53 USD | -554,237,569.32 USD | `-9.51%` | -701,515,761.74 USD | `-1.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -963,151,175.97 USD | `-0.31` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2248.08` | `2225.47` | `2244.30` | `220,412` | 493,708,360.81 USD | 950,790.94 USD | `+0.19%` | -962,200,385.03 USD | `+0.75` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`2239.35`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2242.50` | `134.4321` | 301,463.98 USD | 10,373,584.50 USD | `8 orders` | `-0.09%` | `-` |
| `BID` | `2242.60` | `34.1836` | 76,660.14 USD | 10,072,120.52 USD | `7 orders` | `-0.08%` | `-` |
| `BID` | `2242.70` | `352.1158` | 789,690.10 USD | 9,995,460.38 USD | `8 orders` | `-0.08%` | `-` |
| `BID` | `2242.80` | `283.3874` | 635,581.26 USD | 9,205,770.27 USD | `8 orders` | `-0.07%` | `-` |
| `BID` | `2242.90` | `361.3782` | 810,535.16 USD | 8,570,189.01 USD | `8 orders` | `-0.07%` | `-` |
| `BID` | `2243.00` | `127.1662` | 285,233.79 USD | 7,759,653.85 USD | `9 orders` | `-0.06%` | `-` |
| `BID` | `2243.10` | `267.6046` | 600,263.88 USD | 7,474,420.06 USD | `6 orders` | `-0.06%` | `-` |
| `BID` | `2243.20` | `484.3763` | 1,086,552.92 USD | 6,874,156.18 USD | `9 orders` | `-0.06%` | `-` |
| `BID` | `2243.30` | `263.3437` | 590,758.92 USD | 5,787,603.27 USD | `7 orders` | `-0.05%` | `-` |
| `BID` | `2243.40` | `418.7982` | 939,531.88 USD | 5,196,844.34 USD | `6 orders` | `-0.05%` | `-` |
| `BID` | `2243.50` | `442.9089` | 993,666.12 USD | 4,257,312.46 USD | `9 orders` | `-0.04%` | `-` |
| `BID` | `2243.60` | `323.7290` | 726,318.38 USD | 3,263,646.34 USD | `9 orders` | `-0.04%` | `-` |
| `BID` | `2243.70` | `330.4207` | 741,364.92 USD | 2,537,327.96 USD | `6 orders` | `-0.03%` | `-` |
| `BID` | `2243.80` | `126.2399` | 283,257.09 USD | 1,795,963.04 USD | `6 orders` | `-0.03%` | `-` |
| `BID` | `2243.90` | `63.6247` | 142,767.46 USD | 1,512,705.95 USD | `7 orders` | `-0.02%` | `-` |
| `BID` | `2244.00` | `96.8789` | 217,396.25 USD | 1,369,938.48 USD | `11 orders` | `-0.02%` | `-` |
| `BID` | `2244.10` | `13.5928` | 30,503.60 USD | 1,152,542.23 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `2244.20` | `130.6868` | 293,287.32 USD | 1,122,038.63 USD | `16 orders` | `-0.01%` | `-` |
| `BID` | `2244.30` | `178.5088` | 400,627.30 USD | 828,751.31 USD | `24 orders` | `-0.01%` | `-` |
| `BID` | `2244.40` | `190.7521` | 428,124.01 USD | 428,124.01 USD | `21 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2244.45` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,244.45` | `0.00%` | `-` |
| `ASK` | `2244.50` | `52.2553` | 117,287.02 USD | 117,287.02 USD | `6 orders` | `+0.00%` | `-` |
| `ASK` | `2244.60` | `24.7018` | 55,445.66 USD | 172,732.68 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `2244.70` | `38.1147` | 85,556.07 USD | 258,288.75 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `2244.80` | `32.8451` | 73,730.68 USD | 332,019.43 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `2244.90` | `133.1361` | 298,877.23 USD | 630,896.66 USD | `7 orders` | `+0.02%` | `-` |
| `ASK` | `2245.00` | `46.6476` | 104,723.86 USD | 735,620.52 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `2245.10` | `536.0250` | 1,203,429.73 USD | 1,939,050.25 USD | `10 orders` | `+0.03%` | `-` |
| `ASK` | `2245.20` | `159.4004` | 357,885.78 USD | 2,296,936.03 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `2245.30` | `357.4265` | 802,529.72 USD | 3,099,465.75 USD | `10 orders` | `+0.04%` | `-` |
| `ASK` | `2245.40` | `470.5144` | 1,056,493.03 USD | 4,155,958.78 USD | `9 orders` | `+0.04%` | `-` |
| `ASK` | `2245.50` | `68.9723` | 154,877.30 USD | 4,310,836.08 USD | `8 orders` | `+0.05%` | `-` |
| `ASK` | `2245.60` | `308.7678` | 693,368.97 USD | 5,004,205.05 USD | `11 orders` | `+0.05%` | `-` |
| `ASK` | `2245.70` | `279.6996` | 628,121.39 USD | 5,632,326.44 USD | `4 orders` | `+0.06%` | `-` |
| `ASK` | `2245.80` | `586.3267` | 1,316,772.50 USD | 6,949,098.95 USD | `22 orders` | `+0.06%` | `-` |
| `ASK` | `2245.90` | `308.4582` | 692,766.27 USD | 7,641,865.22 USD | `16 orders` | `+0.06%` | `-` |
| `ASK` | `2246.00` | `284.8404` | 639,751.54 USD | 8,281,616.76 USD | `14 orders` | `+0.07%` | `-` |
| `ASK` | `2246.10` | `58.3927` | 131,155.84 USD | 8,412,772.60 USD | `17 orders` | `+0.07%` | `-` |
| `ASK` | `2246.20` | `374.4121` | 841,004.46 USD | 9,253,777.06 USD | `13 orders` | `+0.08%` | `-` |
| `ASK` | `2246.30` | `479.7579` | 1,077,680.17 USD | 10,331,457.23 USD | `10 orders` | `+0.08%` | `-` |
| `ASK` | `2246.40` | `79.7764` | 179,209.70 USD | 10,510,666.94 USD | `11 orders` | `+0.09%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:34:32 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1844.19` | `7,964.66` | 14,688,299.29 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-30 10:34:32 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 10:34:32 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1913.44` | `6,500.22` | 12,437,784.60 USD | `AT_RISK_LIQ` | `0xf78c5d8d4b` | `2026-10-30 10:34:32 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `10,000.00` | 19,261,000.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-30 10:34:32 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1927.82` | `8,092.45` | 15,600,828.40 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 10:34:32 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2122.13` | `30,641.99` | 65,026,386.86 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 10:34:32 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2129.41` | `26,025.05` | 55,418,031.50 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 10:34:32 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2175.00` | `3,000.00` | 6,525,000.00 USD | `TRIGGER_STOP` | `0x469e9a7f62` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2206.80` | `244.00` | 538,459.20 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x24fb652303` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2207.40` | `266.00` | 587,168.40 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x24fb652303` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2208.60` | `2,009.90` | 4,439,057.63 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2210.10` | `4,701.86` | 10,391,585.21 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2219.70` | `1,395.09` | 3,096,689.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2219.80` | `358.01` | 794,719.92 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2219.80` | `343.24` | 761,925.48 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2221.00` | `458.19` | 1,017,637.99 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x9362ca4dfd` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2226.70` | `2,422.48` | 5,394,146.68 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2228.70` | `1,006.69` | 2,243,599.97 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2234.50` | `707.18` | 1,580,184.77 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2235.30` | `1,793.23` | 4,008,409.92 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2236.70` | `353.28` | 790,171.98 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2236.90` | `1,234.71` | 2,761,928.84 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2237.90` | `1,343.37` | 3,006,324.14 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2238.30` | `480.45` | 1,075,382.06 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2238.70` | `895.25` | 2,004,206.70 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2239.60` | `259.12` | 580,316.19 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x07fd7e702b` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2241.10` | `670.68` | 1,503,057.36 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2242.20` | `350.72` | 786,381.92 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2242.50` | `446.87` | 1,002,114.50 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2243.40` | `335.01` | 751,560.99 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2243.90` | `222.62` | 499,528.72 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2577367690` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2244.40` | `245.57` | 551,150.13 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2244.50` | `361.68` | 811,780.44 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x57df61a52b` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2247.50` | `245.25` | 551,190.61 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2247.80` | `222.44` | 499,999.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2577367690` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2248.20` | `334.31` | 751,603.16 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2249.50` | `222.27` | 499,999.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2577367690` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2250.10` | `350.42` | 788,476.89 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2250.20` | `445.41` | 1,002,253.48 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2251.70` | `667.63` | 1,503,310.13 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2253.00` | `681.28` | 1,534,933.30 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2253.10` | `1,236.12` | 2,785,097.47 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2253.40` | `889.42` | 2,004,219.48 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2256.00` | `1,332.61` | 3,006,361.17 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2256.20` | `350.11` | 789,925.63 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2256.40` | `724.51` | 1,634,775.11 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2257.90` | `1,775.30` | 4,008,451.22 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2261.30` | `2,422.48` | 5,477,964.65 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2264.60` | `965.34` | 2,186,116.66 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2269.50` | `350.17` | 794,719.89 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2269.70` | `620.97` | 1,409,408.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x674982e841` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2272.20` | `2,200.51` | 4,999,999.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb1ec7febea` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2273.10` | `1,419.14` | 3,225,843.27 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2275.10` | `334.90` | 761,925.53 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2275.70` | `4,696.65` | 10,688,176.87 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2278.00` | `240.63` | 548,166.53 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x81cb8a0a3b` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2284.60` | `2,124.01` | 4,852,504.56 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 10:34:32 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2289.80` | `3,258.62` | 7,461,591.51 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 10:34:32 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2300.00` | `4,002.10` | 9,204,832.99 USD | `TRIGGER_STOP` | `0xfb941d2344` | `2026-10-30 10:34:32 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2457.31` | `22,046.99` | 54,176,241.78 USD | `AT_RISK_LIQ` | `0x8added25f8` | `2026-10-30 10:34:32 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `2,733.67` | 6,872,176.53 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-30 10:34:32 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2624.15` | `10,000.00` | 26,241,459.22 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-30 10:34:32 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2658.00` | `9,700.00` | 25,782,604.68 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-30 10:34:32 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 238,875,836.33 USD | `106,417.71` | `2322.74` | `2244.70` | `3780.55` | 8,305,175.82 USD | `+3.48%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 145,220,928.47 USD | `64,680.62` | `2375.30` | `2244.70` | `4317.20` | 8,415,369.02 USD | `+5.79%` | `5X Cross` |
| `10` | `0x77dd...e0e9` | `LONG` | 68,763,693.57 USD | `30,641.99` | `2610.31` | `2244.70` | `2122.05` | -11,221,481.46 USD | `-16.32%` | `10X Cross` |
| `11` | `0xde8d...9524` | `LONG` | 67,980,967.62 USD | `30,282.40` | `2134.45` | `2244.70` | `1786.31` | 3,344,637.04 USD | `+4.92%` | `20X Cross` |
| `17` | `0x0392...d7d9` | `LONG` | 58,428,842.22 USD | `26,025.05` | `2518.71` | `2244.70` | `2129.33` | -7,120,879.86 USD | `-12.19%` | `9X Cross` |
| `23` | `0x8add...7d2c` | `SHORT` | 49,488,875.76 USD | `22,046.99` | `2271.09` | `2244.70` | `2455.35` | 582,021.54 USD | `+1.18%` | `25X Cross` |
| `27` | `0xdf95...7d72` | `SHORT` | 44,840,502.89 USD | `19,972.61` | `2402.53` | `2244.70` | `4181.37` | 3,144,378.93 USD | `+7.01%` | `25X Cross` |
| `34` | `0xeced...6210` | `SHORT` | 37,458,602.52 USD | `16,687.58` | `2522.09` | `2244.70` | `3478.73` | 4,629,112.48 USD | `+12.36%` | `20X Cross` |
| `35` | `0xb695...a92d` | `SHORT` | 36,266,884.66 USD | `16,153.08` | `2557.74` | `2244.70` | `3913.74` | 5,048,570.70 USD | `+13.92%` | `20X Cross` |
| `36` | `0x6046...b21d` | `LONG` | 35,752,660.60 USD | `15,927.59` | `2410.19` | `2244.70` | `1752.20` | -2,635,959.05 USD | `-7.37%` | `6X Cross` |
| `39` | `0x45d2...4029` | `SHORT` | 31,305,195.00 USD | `13,950.00` | `2443.60` | `2244.70` | `5260.13` | 2,783,087.46 USD | `+8.89%` | `20X Cross` |
| `44` | `0xa61c...66b9` | `LONG` | 28,934,848.80 USD | `12,888.00` | `2369.69` | `2244.70` | `1432.12` | -1,605,805.74 USD | `-5.55%` | `10X Cross` |
| `47` | `0x2371...0883` | `LONG` | 26,942,400.00 USD | `12,000.00` | `2421.77` | `2244.70` | `1279.29` | -2,118,894.85 USD | `-7.86%` | `20X Cross` |
| `48` | `0xbd1c...ff0e` | `LONG` | 26,917,200.00 USD | `12,000.00` | `2419.91` | `2244.70` | `1520.19` | -2,121,832.39 USD | `-7.88%` | `20X Cross` |
| `55` | `0x09dc...c094` | `LONG` | 24,696,100.00 USD | `11,000.00` | `2465.31` | `2244.70` | `1637.26` | -2,422,323.04 USD | `-9.81%` | `20X Cross` |
| `56` | `0xa9de...e049` | `LONG` | 24,691,700.00 USD | `11,000.00` | `2481.81` | `2244.70` | `1643.93` | -2,608,279.46 USD | `-10.56%` | `20X Cross` |
| `57` | `0x0c5d...36b3` | `LONG` | 24,691,700.00 USD | `11,000.00` | `2482.20` | `2244.70` | `1644.26` | -2,612,553.24 USD | `-10.58%` | `20X Cross` |
| `58` | `0x6c93...59a4` | `LONG` | 24,686,200.00 USD | `11,000.00` | `2441.15` | `2244.70` | `1602.22` | -2,166,472.73 USD | `-8.78%` | `20X Cross` |
| `70` | `0xa2ce...3126` | `LONG` | 22,485,881.45 USD | `10,016.88` | `2162.83` | `2244.70` | `1528.11` | 821,079.40 USD | `+3.65%` | `10X Cross` |
| `72` | `0xec7f...df39` | `LONG` | 22,451,000.00 USD | `10,000.00` | `2719.35` | `2244.70` | `1720.78` | -4,742,548.52 USD | `-21.12%` | `20X Cross` |
| `73` | `0x6646...6de5` | `LONG` | 22,448,000.00 USD | `10,000.00` | `1765.80` | `2244.70` | `1724.44` | 4,789,942.55 USD | `+21.34%` | `25X Cross` |
| `74` | `0x15a4...dfdb` | `LONG` | 22,447,000.00 USD | `10,000.00` | `1761.94` | `2244.70` | `258.67` | 4,827,518.97 USD | `+21.51%` | `20X Cross` |
| `75` | `0xb37f...66ca` | `SHORT` | 22,439,700.00 USD | `10,000.00` | `2290.69` | `2244.70` | `2624.07` | 467,291.85 USD | `+2.08%` | `25X Cross` |
| `76` | `0x939f...04d2` | `LONG` | 22,051,512.82 USD | `9,823.81` | `2427.28` | `2244.70` | `1791.03` | -1,793,637.79 USD | `-8.13%` | `25X Cross` |
| `78` | `0xaeaa...2416` | `SHORT` | 21,778,440.00 USD | `9,700.00` | `2311.92` | `2244.70` | `2657.93` | 647,242.40 USD | `+2.97%` | `25X Cross` |
| `83` | `0xf517...c032` | `SHORT` | 20,937,649.24 USD | `9,326.35` | `2202.91` | `2244.70` | `3167.16` | -392,511.03 USD | `-1.87%` | `25X Cross` |
| `85` | `0xca49...53c8` | `SHORT` | 20,635,251.78 USD | `9,195.75` | `2549.39` | `2244.70` | `3862.89` | 2,808,355.41 USD | `+13.61%` | `25X Cross` |
| `87` | `0xba5d...a352` | `SHORT` | 20,323,787.88 USD | `9,054.12` | `2493.89` | `2244.70` | `2905.90` | 2,256,219.38 USD | `+11.10%` | `20X Cross` |
| `88` | `0xea00...a918` | `LONG` | 20,212,689.66 USD | `9,003.83` | `2003.01` | `2244.70` | `1352.97` | 2,177,910.80 USD | `+10.77%` | `5X Cross` |
| `93` | `0xefe4...194b` | `SHORT` | 19,803,952.07 USD | `8,820.57` | `2267.42` | `2244.70` | `3540.84` | 196,062.32 USD | `+0.99%` | `20X Cross` |
| `114` | `0x9eec...daab` | `LONG` | 18,159,219.74 USD | `8,092.45` | `1658.44` | `2244.70` | `1927.55` | 4,738,355.21 USD | `+26.09%` | `15X Cross` |
| `115` | `0x5f91...65aa` | `LONG` | 17,879,856.03 USD | `7,964.66` | `1626.99` | `2244.70` | `1844.11` | 4,921,412.96 USD | `+27.52%` | `16X Cross` |
| `119` | `0xecb6...2b00` | `SHORT` | 17,488,013.90 USD | `7,789.07` | `2242.49` | `2244.70` | `5971.54` | -21,055.49 USD | `-0.12%` | `15X Cross` |
| `126` | `0xec0b...b078` | `LONG` | 15,732,508.53 USD | `7,007.80` | `2065.97` | `2244.70` | `1055.43` | 1,254,578.94 USD | `+7.97%` | `25X Cross` |
| `131` | `0xf02d...5eb3` | `LONG` | 15,386,202.66 USD | `6,855.99` | `2383.33` | `2244.70` | `1117.70` | -953,886.11 USD | `-6.20%` | `20X Cross` |
| `133` | `0xcf53...ee11` | `SHORT` | 15,266,660.64 USD | `6,803.63` | `1862.69` | `2244.70` | `4204.00` | -2,593,555.26 USD | `-16.99%` | `7X Cross` |
| `135` | `0x418a...8888` | `SHORT` | 15,096,239.39 USD | `6,724.38` | `2494.55` | `2244.70` | `3008.34` | 1,678,083.79 USD | `+11.12%` | `25X Cross` |
| `140` | `0x4ff9...38d3` | `LONG` | 14,734,432.35 USD | `6,564.10` | `2447.40` | `2244.70` | `1669.88` | -1,330,590.39 USD | `-9.03%` | `3X Isolated` |
| `142` | `0xf78c...c581` | `LONG` | 14,593,647.29 USD | `6,500.22` | `2521.53` | `2244.70` | `1913.36` | -1,796,893.66 USD | `-12.31%` | `20X Cross` |
| `143` | `0x1ee7...edf5` | `LONG` | 14,591,850.00 USD | `6,500.00` | `2301.55` | `2244.70` | `2069.10` | -368,243.66 USD | `-2.52%` | `25X Cross` |
| `145` | `0xc179...e0c8` | `LONG` | 14,311,207.90 USD | `6,374.14` | `2294.94` | `2244.70` | `1215.81` | -317,067.69 USD | `-2.22%` | `10X Cross` |
| `147` | `0x799f...5f4c` | `LONG` | 14,167,977.91 USD | `6,310.90` | `2390.33` | `2244.70` | `1829.95` | -917,186.71 USD | `-6.47%` | `20X Cross` |
| `150` | `0x08bf...7872` | `SHORT` | 13,968,007.18 USD | `6,224.05` | `2258.00` | `2244.70` | `2585.15` | 85,908.93 USD | `+0.62%` | `20X Cross` |
| `155` | `0xd9e7...4aff` | `LONG` | 13,468,200.00 USD | `6,000.00` | `2480.18` | `2244.70` | `1407.65` | -1,412,924.33 USD | `-10.49%` | `20X Cross` |
| `163` | `0x0c4a...1b19` | `LONG` | 12,706,918.89 USD | `5,660.10` | `2373.06` | `2244.70` | `2081.70` | -724,839.24 USD | `-5.70%` | `25X Isolated` |
| `168` | `0x7fda...17d1` | `LONG` | 11,934,941.21 USD | `5,315.76` | `2211.05` | `2244.70` | `0.000000` | 181,498.96 USD | `+1.52%` | `25X Cross` |
| `178` | `0x218a...7da2` | `SHORT` | 11,723,772.25 USD | `5,222.87` | `2208.16` | `2244.70` | `2792.80` | -190,837.19 USD | `-1.63%` | `10X Cross` |
| `188` | `0x45ab...6cbc` | `LONG` | 11,047,068.04 USD | `4,920.96` | `2727.66` | `2244.70` | `1370.20` | -2,375,675.75 USD | `-21.51%` | `7X Cross` |
| `193` | `0x64b7...9da9` | `LONG` | 10,904,089.69 USD | `4,856.84` | `2604.61` | `2244.70` | `579.33` | -1,746,124.73 USD | `-16.01%` | `25X Cross` |
| `198` | `0xfb18...eb17` | `SHORT` | 10,703,617.42 USD | `4,768.18` | `2315.53` | `2244.70` | `2592.54` | 337,264.37 USD | `+3.15%` | `25X Cross` |
| `200` | `0x5559...d43b` | `SHORT` | 10,675,625.52 USD | `4,755.93` | `2262.69` | `2244.70` | `2781.09` | 85,580.36 USD | `+0.80%` | `25X Cross` |
| `212` | `0xe091...6705` | `SHORT` | 10,101,150.45 USD | `4,500.00` | `2467.33` | `2244.70` | `2463.27` | 1,001,858.06 USD | `+9.92%` | `20X Cross` |
| `222` | `0xb829...3a81` | `LONG` | 9,867,454.18 USD | `4,394.91` | `2398.60` | `2244.70` | `1463.10` | -674,187.77 USD | `-6.83%` | `20X Cross` |
| `237` | `0x28bb...fca6` | `SHORT` | 9,451,004.84 USD | `4,209.61` | `1896.10` | `2244.70` | `3036.99` | -1,469,122.28 USD | `-15.54%` | `20X Cross` |
| `239` | `0x6ea4...0ea7` | `SHORT` | 9,393,107.61 USD | `4,184.01` | `2602.13` | `2244.70` | `3425.22` | 1,494,239.05 USD | `+15.91%` | `20X Cross` |
| `253` | `0x5e9e...35ee` | `SHORT` | 8,994,958.77 USD | `4,007.56` | `1796.39` | `2244.70` | `2585.71` | -1,795,808.68 USD | `-19.96%` | `20X Cross` |
| `254` | `0xfb94...0ddf` | `SHORT` | 8,984,317.21 USD | `4,002.10` | `2382.44` | `2244.70` | `5104.61` | 550,466.94 USD | `+6.13%` | `20X Cross` |
| `255` | `0x3dc9...54b0` | `SHORT` | 8,979,704.47 USD | `3,999.69` | `2480.32` | `2244.70` | `6508.29` | 940,832.08 USD | `+10.48%` | `20X Cross` |
| `256` | `0x8cc9...2b6a` | `SHORT` | 8,978,800.00 USD | `4,000.00` | `1791.18` | `2244.70` | `3544.88` | -1,814,053.33 USD | `-20.20%` | `25X Cross` |
| `273` | `0x4b67...f4e7` | `LONG` | 8,577,407.98 USD | `3,820.84` | `2591.51` | `2244.70` | `1344.64` | -1,324,365.56 USD | `-15.44%` | `20X Cross` |
| `277` | `0x12d2...f97f` | `LONG` | 8,435,427.12 USD | `3,757.26` | `2446.50` | `2244.70` | `1774.26` | -756,739.27 USD | `-8.97%` | `20X Cross` |
| `296` | `0x8ae4...3d60` | `LONG` | 7,988,155.18 USD | `3,558.20` | `2482.21` | `2244.70` | `491.71` | -844,042.85 USD | `-10.57%` | `10X Cross` |
| `336` | `0xb823...9763` | `SHORT` | 6,735,300.00 USD | `3,000.00` | `2229.66` | `2244.70` | `3233.61` | -46,303.32 USD | `-0.69%` | `25X Cross` |
| `337` | `0x469e...58a5` | `SHORT` | 6,734,100.00 USD | `3,000.00` | `2195.70` | `2244.70` | `3243.20` | -146,992.76 USD | `-2.18%` | `25X Cross` |
| `338` | `0x007d...67a0` | `LONG` | 6,732,300.00 USD | `3,000.00` | `2400.00` | `2244.70` | `1473.20` | -467,700.00 USD | `-6.95%` | `25X Cross` |
| `339` | `0x4a20...3c26` | `LONG` | 6,731,910.00 USD | `3,000.00` | `2428.72` | `2244.70` | `547.15` | -554,250.28 USD | `-8.23%` | `20X Cross` |
| `363` | `0x0622...8088` | `LONG` | 6,353,104.58 USD | `2,829.64` | `2210.49` | `2244.70` | `0.000000` | 98,189.36 USD | `+1.55%` | `5X Cross` |
| `364` | `0x9c2a...f6a8` | `SHORT` | 6,338,837.34 USD | `2,823.41` | `2533.78` | `2244.70` | `2627.61` | 815,073.48 USD | `+12.86%` | `20X Cross` |
| `389` | `0x8328...f54a` | `SHORT` | 5,783,359.78 USD | `2,576.45` | `2292.01` | `2244.70` | `3279.45` | 121,911.50 USD | `+2.11%` | `25X Cross` |
| `392` | `0xed48...7c9b` | `SHORT` | 5,724,660.31 USD | `2,551.13` | `2460.02` | `2244.70` | `3244.18` | 551,186.10 USD | `+9.63%` | `20X Cross` |
| `397` | `0x1c98...7fc7` | `LONG` | 5,612,510.10 USD | `2,500.00` | `2452.60` | `2244.70` | `1916.85` | -519,011.46 USD | `-9.25%` | `10X Cross` |
| `398` | `0x970c...2a93` | `SHORT` | 5,611,750.00 USD | `2,500.00` | `2229.57` | `2244.70` | `5050.90` | -37,805.51 USD | `-0.67%` | `20X Cross` |
| `413` | `0xa445...329d` | `LONG` | 5,401,293.64 USD | `2,406.14` | `2354.86` | `2244.70` | `1701.16` | -264,821.64 USD | `-4.90%` | `25X Cross` |
| `416` | `0xfbe2...c8ea` | `SHORT` | 5,354,310.43 USD | `2,385.21` | `2041.57` | `2244.70` | `2626.35` | -484,743.77 USD | `-9.05%` | `20X Cross` |
| `417` | `0x6749...ce07` | `SHORT` | 5,352,179.56 USD | `2,384.89` | `2220.92` | `2244.70` | `3630.24` | -55,516.53 USD | `-1.04%` | `20X Cross` |
| `418` | `0x645b...87b8` | `SHORT` | 5,343,521.22 USD | `2,379.98` | `2421.64` | `2244.70` | `11265.97` | 419,925.74 USD | `+7.86%` | `10X Cross` |
| `427` | `0x77ee...2902` | `SHORT` | 5,142,601.74 USD | `2,290.69` | `2476.53` | `2244.70` | `5914.24` | 530,370.49 USD | `+10.31%` | `25X Cross` |
| `433` | `0xbcd4...0dd2` | `SHORT` | 5,082,009.53 USD | `2,263.50` | `2233.24` | `2244.70` | `2662.92` | -27,051.96 USD | `-0.53%` | `25X Cross` |
| `454` | `0xd507...c948` | `SHORT` | 4,875,053.78 USD | `2,172.00` | `2387.49` | `2244.70` | `2600.45` | 310,587.25 USD | `+6.37%` | `5X Isolated` |
| `461` | `0x382b...3e39` | `SHORT` | 4,781,246.80 USD | `2,129.54` | `2296.66` | `2244.70` | `4647.06` | 109,590.41 USD | `+2.29%` | `25X Cross` |
| `463` | `0x023a...2355` | `LONG` | 4,767,343.26 USD | `2,123.54` | `2330.15` | `2244.70` | `0.000000` | -180,830.56 USD | `-3.79%` | `25X Cross` |
| `501` | `0x3453...b323` | `SHORT` | 4,490,076.35 USD | `2,000.12` | `2322.47` | `2244.70` | `2377.00` | 155,159.49 USD | `+3.46%` | `25X Cross` |
| `502` | `0x7a6d...f79c` | `SHORT` | 4,489,400.00 USD | `2,000.00` | `2418.41` | `2244.70` | `2545.89` | 347,432.11 USD | `+7.74%` | `25X Cross` |
| `503` | `0xe02e...d78b` | `LONG` | 4,488,000.00 USD | `2,000.00` | `2228.11` | `2244.70` | `2171.80` | 31,776.53 USD | `+0.71%` | `25X Cross` |
| `506` | `0xf3dc...1672` | `SHORT` | 4,446,109.15 USD | `1,980.36` | `2240.44` | `2244.70` | `2768.77` | -9,221.60 USD | `-0.21%` | `20X Cross` |
| `513` | `0xac48...3201` | `SHORT` | 4,409,813.09 USD | `1,964.37` | `2272.04` | `2244.70` | `3115.34` | 53,329.21 USD | `+1.21%` | `20X Cross` |
| `525` | `0x8376...9a1e` | `SHORT` | 4,288,872.47 USD | `1,910.50` | `2477.72` | `2244.70` | `3179.40` | 444,815.70 USD | `+10.37%` | `20X Cross` |
| `556` | `0x7265...91a5` | `LONG` | 4,044,115.68 USD | `1,801.87` | `2533.96` | `2244.70` | `1987.33` | -521,750.78 USD | `-12.90%` | `20X Cross` |
| `558` | `0x739c...cfb2` | `SHORT` | 4,041,180.00 USD | `1,800.00` | `2427.60` | `2244.70` | `2513.65` | 328,516.38 USD | `+8.13%` | `25X Cross` |
| `566` | `0x91a9...3f70` | `SHORT` | 3,968,346.10 USD | `1,767.48` | `2156.23` | `2244.70` | `3649.47` | -157,242.02 USD | `-3.96%` | `4X Cross` |
| `575` | `0xbb34...1696` | `LONG` | 3,928,575.00 USD | `1,750.00` | `2315.81` | `2244.70` | `1934.54` | -124,093.23 USD | `-3.16%` | `25X Cross` |
| `576` | `0xc619...10f5` | `LONG` | 3,928,225.00 USD | `1,750.00` | `2315.39` | `2244.70` | `1761.30` | -123,720.83 USD | `-3.15%` | `25X Cross` |
| `602` | `0xfeec...4e9c` | `SHORT` | 3,796,757.31 USD | `1,691.81` | `2566.49` | `2244.70` | `2508.96` | 545,267.21 USD | `+14.36%` | `10X Cross` |
| `616` | `0xeee0...0b53` | `LONG` | 3,674,852.02 USD | `1,637.12` | `2468.64` | `2244.70` | `152.39` | -366,624.04 USD | `-9.98%` | `7X Cross` |
| `620` | `0x27b8...12fc` | `LONG` | 3,655,129.62 USD | `1,628.12` | `2468.73` | `2244.70` | `594.44` | -364,265.01 USD | `-9.97%` | `10X Cross` |
| `622` | `0x982b...4606` | `LONG` | 3,652,042.16 USD | `1,626.82` | `2575.24` | `2244.70` | `1547.61` | -537,410.92 USD | `-14.72%` | `5X Isolated` |
| `628` | `0x73d7...8be1` | `LONG` | 3,594,489.31 USD | `1,601.47` | `2410.40` | `2244.70` | `1760.98` | -265,689.61 USD | `-7.39%` | `25X Cross` |
| `629` | `0xad54...6203` | `LONG` | 3,585,799.83 USD | `1,597.45` | `2591.98` | `2244.70` | `2051.96` | -554,778.21 USD | `-15.47%` | `10X Isolated` |
| `636` | `0x880a...311c` | `LONG` | 3,543,823.01 USD | `1,578.40` | `2209.72` | `2244.70` | `0.000000` | 55,999.15 USD | `+1.58%` | `9X Cross` |
| `654` | `0xe170...9300` | `SHORT` | 3,441,562.96 USD | `1,533.40` | `2076.39` | `2244.70` | `3146.85` | -257,613.46 USD | `-7.49%` | `25X Cross` |
| `660` | `0x4b86...df9d` | `SHORT` | 3,420,922.80 USD | `1,524.00` | `2287.40` | `2244.70` | `2759.80` | 65,074.80 USD | `+1.90%` | `9X Isolated` |
| `664` | `0x2e2b...2fab` | `LONG` | 3,384,362.84 USD | `1,507.38` | `2245.53` | `2244.70` | `1204.48` | -510.26 USD | `-0.02%` | `25X Cross` |
| `667` | `0xde6b...3361` | `LONG` | 3,367,500.00 USD | `1,500.00` | `2216.98` | `2244.70` | `2168.73` | 42,019.26 USD | `+1.25%` | `25X Cross` |
| `669` | `0xf929...d1f9` | `SHORT` | 3,367,050.00 USD | `1,500.00` | `2423.37` | `2244.70` | `2677.84` | 268,005.26 USD | `+7.96%` | `25X Cross` |
| `670` | `0x251f...6e5d` | `LONG` | 3,366,750.00 USD | `1,500.00` | `2346.68` | `2244.70` | `1836.81` | -153,280.49 USD | `-4.55%` | `20X Cross` |
| `690` | `0xb885...3c54` | `LONG` | 3,257,864.94 USD | `1,450.00` | `2274.34` | `2244.70` | `25.78` | -39,943.19 USD | `-1.23%` | `20X Cross` |
| `692` | `0x3440...32c5` | `SHORT` | 3,251,788.80 USD | `1,448.97` | `2198.21` | `2244.70` | `3799.17` | -66,637.83 USD | `-2.05%` | `25X Cross` |
| `694` | `0xef70...a84c` | `SHORT` | 3,239,103.21 USD | `1,442.74` | `2424.73` | `2244.70` | `3257.01` | 259,167.62 USD | `+8.00%` | `25X Cross` |
| `703` | `0x4b5f...0dd8` | `LONG` | 3,215,029.41 USD | `1,431.96` | `2339.45` | `2244.70` | `2147.89` | -134,963.54 USD | `-4.20%` | `10X Cross` |
| `706` | `0xbadb...9ee6` | `LONG` | 3,205,790.75 USD | `1,428.16` | `1936.00` | `2244.70` | `1056.43` | 440,869.11 USD | `+13.75%` | `20X Cross` |
| `759` | `0x53f8...ceff` | `LONG` | 3,027,863.77 USD | `1,348.65` | `2276.73` | `2244.70` | `0.000000` | -42,660.70 USD | `-1.41%` | `20X Cross` |
| `777` | `0x0dd5...f6ee` | `LONG` | 2,951,780.50 USD | `1,315.00` | `2306.05` | `2244.70` | `1560.22` | -80,683.88 USD | `-2.73%` | `5X Cross` |
| `806` | `0x1f16...6d07` | `LONG` | 2,840,904.00 USD | `1,266.00` | `2261.43` | `2244.70` | `1388.15` | -22,067.23 USD | `-0.78%` | `7X Cross` |
| `818` | `0xc435...c905` | `SHORT` | 2,800,137.60 USD | `1,248.00` | `2704.38` | `2244.70` | `4241.72` | 574,932.75 USD | `+20.53%` | `20X Cross` |
| `825` | `0x6859...7e1e` | `SHORT` | 2,777,410.28 USD | `1,237.15` | `2200.39` | `2244.70` | `4649.47` | -55,183.12 USD | `-1.99%` | `25X Cross` |
| `833` | `0x7277...0b98` | `SHORT` | 2,736,698.44 USD | `1,219.45` | `2206.05` | `2244.70` | `3366.73` | -46,510.64 USD | `-1.70%` | `20X Cross` |
| `834` | `0x7178...0854` | `LONG` | 2,735,462.13 USD | `1,218.63` | `2461.81` | `2244.70` | `1159.63` | -264,584.27 USD | `-9.67%` | `10X Cross` |
| `843` | `0xd911...961e` | `LONG` | 2,714,588.30 USD | `1,209.44` | `2213.60` | `2244.70` | `338.56` | 37,366.51 USD | `+1.38%` | `25X Cross` |
| `850` | `0xaaa1...ab8c` | `SHORT` | 2,693,880.00 USD | `1,200.00` | `2276.29` | `2244.70` | `2365.42` | 37,677.58 USD | `+1.40%` | `25X Isolated` |
| `858` | `0x07fd...689d` | `LONG` | 2,664,450.71 USD | `1,186.89` | `2416.34` | `2244.70` | `0.000000` | -203,491.64 USD | `-7.64%` | `25X Cross` |
| `893` | `0x0a97...347d` | `LONG` | 2,534,472.10 USD | `1,128.94` | `2267.88` | `2244.70` | `1508.92` | -25,832.52 USD | `-1.02%` | `20X Cross` |
| `907` | `0x6e6f...82a6` | `LONG` | 2,498,964.01 USD | `1,113.07` | `2266.07` | `2244.70` | `1358.09` | -23,352.28 USD | `-0.93%` | `20X Cross` |
| `908` | `0xa70a...4be9` | `LONG` | 2,498,939.36 USD | `1,113.11` | `2259.47` | `2244.70` | `952.75` | -16,112.44 USD | `-0.64%` | `20X Cross` |
| `926` | `0x2f80...f203` | `SHORT` | 2,444,672.77 USD | `1,088.94` | `1984.00` | `2244.70` | `2963.99` | -284,205.58 USD | `-11.63%` | `20X Cross` |
| `932` | `0x6f11...0389` | `SHORT` | 2,422,570.80 USD | `1,079.00` | `2333.39` | `2244.70` | `3198.91` | 95,158.11 USD | `+3.93%` | `25X Cross` |
| `934` | `0x8eb7...b90f` | `LONG` | 2,419,416.73 USD | `1,077.74` | `2396.38` | `2244.70` | `1881.14` | -163,261.31 USD | `-6.75%` | `5X Isolated` |
| `937` | `0x2b61...2f6c` | `SHORT` | 2,416,637.73 USD | `1,076.60` | `2681.75` | `2244.70` | `6352.90` | 470,535.00 USD | `+19.47%` | `10X Cross` |
| `960` | `0x30af...393e` | `SHORT` | 2,337,623.43 USD | `1,041.16` | `2252.26` | `2244.70` | `2297.11` | 7,358.89 USD | `+0.31%` | `25X Cross` |
| `972` | `0x1b2a...f7a6` | `LONG` | 2,301,643.55 USD | `1,025.37` | `2737.51` | `2244.70` | `882.27` | -505,316.39 USD | `-21.95%` | `10X Cross` |
| `979` | `0x02aa...1806` | `SHORT` | 2,261,040.43 USD | `1,007.10` | `2654.68` | `2244.70` | `3612.90` | 412,491.67 USD | `+18.24%` | `20X Cross` |
| `980` | `0x001a...fef6` | `SHORT` | 2,260,638.77 USD | `1,007.33` | `2022.19` | `2244.70` | `3075.74` | -223,630.81 USD | `-9.89%` | `10X Cross` |
| `986` | `0xdb3a...cf3b` | `LONG` | 2,252,418.54 USD | `1,003.22` | `2705.01` | `2244.70` | `0.000000` | -461,288.35 USD | `-20.48%` | `4X Cross` |
| `989` | `0x8c02...b73f` | `SHORT` | 2,245,100.00 USD | `1,000.00` | `2250.37` | `2244.70` | `8098.58` | 5,271.47 USD | `+0.23%` | `20X Cross` |
| `990` | `0x5272...fcd9` | `SHORT` | 2,245,000.00 USD | `1,000.00` | `2241.82` | `2244.70` | `2830.96` | -3,175.51 USD | `-0.14%` | `5X Cross` |
| `992` | `0xd7b8...9f55` | `LONG` | 2,242,455.30 USD | `999.00` | `2195.00` | `2244.70` | `0.000000` | 49,650.30 USD | `+2.21%` | `15X Cross` |
| `998` | `0x4487...c92d` | `LONG` | 2,223,453.75 USD | `990.49` | `2228.23` | `2244.70` | `1541.13` | 16,404.94 USD | `+0.74%` | `10X Cross` |
| `1014` | `0xb002...ed8a` | `SHORT` | 2,161,161.24 USD | `962.78` | `2299.66` | `2244.70` | `4199.28` | 52,916.66 USD | `+2.45%` | `25X Cross` |
| `1030` | `0xb812...b5e0` | `LONG` | 2,112,208.83 USD | `940.98` | `2263.21` | `2244.70` | `1185.22` | -17,421.64 USD | `-0.82%` | `25X Cross` |
| `1037` | `0xb1ec...e86a` | `SHORT` | 2,096,111.57 USD | `933.64` | `2272.72` | `2244.70` | `12700.55` | 25,795.38 USD | `+1.23%` | `25X Cross` |
| `1056` | `0xb8eb...1dd5` | `LONG` | 2,059,273.17 USD | `917.27` | `2227.70` | `2244.70` | `113.64` | 15,864.59 USD | `+0.77%` | `25X Cross` |
| `1058` | `0xef96...9383` | `LONG` | 2,058,762.80 USD | `917.57` | `2235.00` | `2244.70` | `0.000000` | 7,979.15 USD | `+0.39%` | `25X Cross` |
| `1063` | `0xede2...f971` | `LONG` | 2,051,625.37 USD | `914.31` | `2208.16` | `2244.70` | `1463.18` | 32,668.38 USD | `+1.59%` | `5X Cross` |
| `1064` | `0x9606...4e5d` | `SHORT` | 2,049,403.69 USD | `913.00` | `2478.70` | `2244.70` | `4299.86` | 213,649.91 USD | `+10.42%` | `20X Cross` |
| `1083` | `0x5f10...d49d` | `LONG` | 2,019,780.00 USD | `900.00` | `2249.83` | `2244.70` | `1800.19` | -5,073.47 USD | `-0.25%` | `25X Cross` |
| `1101` | `0x82f6...12ec` | `SHORT` | 1,991,087.06 USD | `887.02` | `2199.66` | `2244.70` | `2249.47` | -39,944.23 USD | `-2.01%` | `25X Cross` |
| `1139` | `0xa0fb...96be` | `LONG` | 1,949,528.54 USD | `868.35` | `2293.96` | `2244.70` | `1121.99` | -42,430.13 USD | `-2.18%` | `3X Cross` |
| `1166` | `0x24fb...ed0f` | `LONG` | 1,908,635.54 USD | `850.10` | `2199.85` | `2244.70` | `0.000000` | 38,548.67 USD | `+2.02%` | `15X Cross` |
| `1182` | `0xcd27...52a8` | `LONG` | 1,879,700.08 USD | `837.21` | `2553.56` | `2244.70` | `1403.42` | -258,164.70 USD | `-13.73%` | `2X Cross` |
| `1199` | `0xbef3...0d3e` | `LONG` | 1,857,100.92 USD | `827.33` | `2227.10` | `2244.70` | `2132.94` | 14,556.42 USD | `+0.78%` | `20X Cross` |
| `1204` | `0x6a41...a3b9` | `LONG` | 1,853,020.68 USD | `825.69` | `2226.70` | `2244.70` | `2136.70` | 14,448.23 USD | `+0.78%` | `20X Cross` |
| `1231` | `0xb15b...dbae` | `SHORT` | 1,803,417.48 USD | `803.30` | `2290.80` | `2244.70` | `2262.58` | 36,791.87 USD | `+2.04%` | `25X Cross` |
| `1237` | `0x04a9...95aa` | `LONG` | 1,796,160.00 USD | `800.00` | `2595.13` | `2244.70` | `1866.88` | -279,946.74 USD | `-15.59%` | `5X Cross` |
| `1239` | `0x7737...bf66` | `SHORT` | 1,795,292.88 USD | `799.79` | `2494.83` | `2244.70` | `24207.64` | 200,053.15 USD | `+11.14%` | `15X Cross` |
| `1271` | `0x458d...ab3b` | `LONG` | 1,739,074.59 USD | `774.75` | `2740.41` | `2244.70` | `1887.17` | -384,054.59 USD | `-22.08%` | `3X Isolated` |
| `1326` | `0x2e30...4cb5` | `SHORT` | 1,642,867.18 USD | `732.12` | `2334.97` | `2244.70` | `8977.60` | 66,606.50 USD | `+4.05%` | `2X Cross` |
| `1328` | `0xaa53...9cb7` | `LONG` | 1,639,021.62 USD | `730.34` | `2389.70` | `2244.70` | `1962.83` | -106,268.01 USD | `-6.48%` | `20X Cross` |
| `1329` | `0x3fc5...c0c1` | `SHORT` | 1,638,752.82 USD | `729.92` | `2702.11` | `2244.70` | `4553.32` | 333,589.38 USD | `+20.36%` | `25X Cross` |
| `1335` | `0x6463...42f5` | `LONG` | 1,631,848.97 USD | `726.88` | `2214.40` | `2244.70` | `0.000000` | 22,238.30 USD | `+1.36%` | `1X Cross` |
| `1343` | `0xa189...94d7` | `SHORT` | 1,615,704.87 USD | `719.98` | `2691.84` | `2244.70` | `2915.03` | 322,367.79 USD | `+19.95%` | `25X Cross` |
| `1362` | `0x2f93...4404` | `LONG` | 1,586,929.32 USD | `707.47` | `1700.45` | `2244.70` | `1368.80` | 383,902.95 USD | `+24.19%` | `4X Isolated` |
| `1370` | `0x5605...fe0f` | `SHORT` | 1,576,382.60 USD | `702.14` | `2566.90` | `2244.70` | `3062.37` | 225,950.05 USD | `+14.33%` | `20X Cross` |
| `1373` | `0x7743...e4fe` | `SHORT` | 1,572,818.72 USD | `700.56` | `2298.56` | `2244.70` | `6178.16` | 37,456.36 USD | `+2.38%` | `25X Cross` |
| `1377` | `0x0deb...0bc5` | `LONG` | 1,570,940.00 USD | `700.00` | `2071.05` | `2244.70` | `1597.39` | 121,204.21 USD | `+7.72%` | `20X Cross` |
| `1405` | `0x51f6...2b39` | `LONG` | 1,552,219.93 USD | `691.38` | `2223.60` | `2244.70` | `333.77` | 14,858.91 USD | `+0.96%` | `25X Cross` |
| `1428` | `0xdbd1...29dd` | `SHORT` | 1,529,402.38 USD | `680.70` | `3030.57` | `2244.70` | `3786.55` | 533,518.75 USD | `+34.88%` | `6X Cross` |
| `1431` | `0x248e...6be2` | `SHORT` | 1,528,684.03 USD | `680.93` | `2282.89` | `2244.70` | `3458.58` | 25,801.63 USD | `+1.69%` | `20X Cross` |
| `1438` | `0x71e5...be04` | `LONG` | 1,520,819.83 USD | `677.67` | `2727.27` | `2244.70` | `1470.95` | -327,365.77 USD | `-21.53%` | `20X Cross` |
| `1444` | `0x0b23...f37b` | `LONG` | 1,515,375.00 USD | `675.00` | `2238.15` | `2244.70` | `593.09` | 4,618.36 USD | `+0.30%` | `5X Cross` |
| `1471` | `0x0cac...6170` | `SHORT` | 1,475,495.75 USD | `657.50` | `2146.55` | `2244.70` | `2839.40` | -64,133.55 USD | `-4.35%` | `20X Cross` |
| `1508` | `0xf00e...fe3d` | `SHORT` | 1,442,751.30 USD | `642.88` | `2333.21` | `2244.70` | `2481.57` | 57,226.67 USD | `+3.97%` | `20X Cross` |
| `1511` | `0xffb2...5ed6` | `SHORT` | 1,438,329.24 USD | `640.77` | `2672.96` | `2244.70` | `2504.82` | 274,419.11 USD | `+19.08%` | `20X Cross` |
| `1518` | `0x8505...1821` | `SHORT` | 1,423,304.27 USD | `633.96` | `2239.93` | `2244.70` | `3892.74` | -3,272.67 USD | `-0.23%` | `20X Cross` |
| `1537` | `0xfce0...f4c0` | `SHORT` | 1,400,044.36 USD | `623.60` | `3129.61` | `2244.70` | `2799.75` | 551,582.22 USD | `+39.40%` | `20X Cross` |
| `1588` | `0xad02...eb65` | `LONG` | 1,348,452.41 USD | `600.62` | `2460.69` | `2244.70` | `1078.87` | -129,488.15 USD | `-9.60%` | `5X Cross` |
| `1590` | `0x26e6...6b28` | `LONG` | 1,346,940.00 USD | `600.00` | `1769.78` | `2244.70` | `2004.67` | 285,068.47 USD | `+21.16%` | `20X Cross` |
| `1591` | `0x638f...f5f0` | `LONG` | 1,346,460.00 USD | `600.00` | `4011.50` | `2244.70` | `341.49` | -1,060,443.53 USD | `-78.76%` | `25X Cross` |
| `1598` | `0x7c90...d129` | `LONG` | 1,333,974.43 USD | `594.17` | `2286.01` | `2244.70` | `1855.37` | -24,308.45 USD | `-1.82%` | `20X Cross` |
| `1650` | `0x9599...c60a` | `LONG` | 1,284,718.36 USD | `572.39` | `2231.08` | `2244.70` | `0.000000` | 7,681.27 USD | `+0.60%` | `20X Cross` |
| `1653` | `0x31de...13f2` | `LONG` | 1,282,052.31 USD | `571.02` | `2251.82` | `2244.70` | `0.000000` | -3,780.40 USD | `-0.29%` | `20X Cross` |
| `1662` | `0xfc66...ca06` | `SHORT` | 1,273,943.60 USD | `567.43` | `2275.19` | `2244.70` | `7320.97` | 17,079.61 USD | `+1.34%` | `20X Cross` |
| `1665` | `0x9362...7d7c` | `SHORT` | 1,272,730.31 USD | `566.99` | `2226.19` | `2244.70` | `2518.86` | -10,494.49 USD | `-0.82%` | `20X Cross` |
| `1668` | `0xfb99...37f3` | `LONG` | 1,269,134.24 USD | `565.34` | `2362.35` | `2244.70` | `1243.64` | -66,402.12 USD | `-5.23%` | `3X Cross` |
| `1683` | `0x844b...7f42` | `SHORT` | 1,259,276.70 USD | `561.00` | `2026.17` | `2244.70` | `3008.33` | -122,593.29 USD | `-9.74%` | `25X Cross` |
| `1690` | `0xabe6...1d99` | `SHORT` | 1,247,950.98 USD | `556.00` | `2484.68` | `2244.70` | `3100.41` | 133,544.91 USD | `+10.70%` | `20X Cross` |
| `1693` | `0x2a76...9a53` | `LONG` | 1,246,008.05 USD | `554.99` | `2231.40` | `2244.70` | `0.000000` | 7,600.99 USD | `+0.61%` | `25X Cross` |
| `1710` | `0x936c...bb0f` | `LONG` | 1,235,058.92 USD | `550.09` | `2218.31` | `2244.70` | `0.000000` | 14,791.65 USD | `+1.20%` | `20X Cross` |
| `1711` | `0x825c...465e` | `LONG` | 1,234,750.00 USD | `550.00` | `2208.12` | `2244.70` | `1189.46` | 20,280.50 USD | `+1.64%` | `4X Cross` |
| `1717` | `0xad21...fb6a` | `LONG` | 1,228,042.24 USD | `547.26` | `2565.80` | `2244.70` | `1733.47` | -176,110.76 USD | `-14.34%` | `6X Cross` |
| `1819` | `0x0c7a...2f50` | `SHORT` | 1,142,746.45 USD | `509.25` | `2122.56` | `2244.70` | `4107.61` | -61,841.02 USD | `-5.41%` | `20X Cross` |
| `1824` | `0x0089...2410` | `SHORT` | 1,138,585.00 USD | `507.35` | `2308.88` | `2244.70` | `3408.70` | 32,815.26 USD | `+2.88%` | `20X Cross` |
| `1839` | `0xe282...df29` | `LONG` | 1,122,600.00 USD | `500.00` | `2309.84` | `2244.70` | `2045.31` | -32,324.21 USD | `-2.88%` | `10X Isolated` |
| `1840` | `0x6936...9417` | `SHORT` | 1,122,550.00 USD | `500.00` | `2315.11` | `2244.70` | `2358.91` | 35,005.21 USD | `+3.12%` | `25X Isolated` |
| `1841` | `0xb322...d51f` | `SHORT` | 1,122,550.00 USD | `500.00` | `2268.03` | `2244.70` | `3767.11` | 11,466.32 USD | `+1.02%` | `20X Cross` |
| `1842` | `0x4044...794c` | `LONG` | 1,122,450.00 USD | `500.00` | `2260.80` | `2244.70` | `0.000000` | -7,950.00 USD | `-0.71%` | `25X Cross` |
| `1843` | `0x89b2...9ca6` | `LONG` | 1,122,400.00 USD | `500.00` | `2363.45` | `2244.70` | `1622.65` | -59,327.42 USD | `-5.29%` | `25X Cross` |
| `1844` | `0xa559...ff95` | `LONG` | 1,122,350.00 USD | `500.00` | `2260.68` | `2244.70` | `1062.32` | -7,994.36 USD | `-0.71%` | `20X Cross` |
| `1850` | `0x7298...7d6c` | `SHORT` | 1,118,295.36 USD | `498.15` | `3426.75` | `2244.70` | `5421.61` | 588,740.46 USD | `+52.65%` | `20X Cross` |
| `1863` | `0x9c68...7783` | `SHORT` | 1,107,328.02 USD | `493.31` | `2273.58` | `2244.70` | `3944.39` | 14,251.23 USD | `+1.29%` | `25X Cross` |
| `1869` | `0x404c...5f03` | `SHORT` | 1,099,029.23 USD | `489.79` | `2671.94` | `2244.70` | `5000.95` | 209,650.32 USD | `+19.08%` | `20X Cross` |
| `1873` | `0x321f...1c84` | `SHORT` | 1,095,448.17 USD | `488.02` | `2370.09` | `2244.70` | `3047.35` | 61,196.43 USD | `+5.59%` | `10X Cross` |
| `1890` | `0x71d0...8c26` | `LONG` | 1,079,249.18 USD | `480.73` | `2225.97` | `2244.70` | `0.000000` | 9,144.42 USD | `+0.85%` | `25X Cross` |
| `1903` | `0x34fb...93de` | `LONG` | 1,066,828.41 USD | `475.18` | `2219.83` | `2244.70` | `0.000000` | 12,005.56 USD | `+1.13%` | `20X Cross` |
| `1929` | `0xe86b...3664` | `LONG` | 1,049,239.32 USD | `467.39` | `2231.29` | `2244.70` | `0.000000` | 6,358.39 USD | `+0.61%` | `25X Cross` |
| `1941` | `0x94b6...e5b3` | `SHORT` | 1,042,279.65 USD | `463.86` | `2261.12` | `2244.70` | `2405.55` | 6,563.02 USD | `+0.63%` | `25X Cross` |
| `1949` | `0x82c6...fe42` | `LONG` | 1,038,358.75 USD | `462.50` | `2501.38` | `2244.70` | `2053.65` | -118,531.82 USD | `-11.42%` | `5X Isolated` |
| `1956` | `0xe330...77a1` | `SHORT` | 1,035,257.88 USD | `461.20` | `2206.97` | `2244.70` | `6426.54` | -17,400.52 USD | `-1.68%` | `20X Cross` |
| `1960` | `0x2de3...486d` | `LONG` | 1,033,229.68 USD | `460.40` | `2286.27` | `2244.70` | `1191.99` | -19,371.23 USD | `-1.87%` | `25X Cross` |
| `1974` | `0x617e...0f97` | `SHORT` | 1,027,883.13 USD | `457.85` | `2205.60` | `2244.70` | `3350.61` | -18,039.29 USD | `-1.75%` | `10X Cross` |
| `2003` | `0x0514...bdfe` | `SHORT` | 1,010,160.00 USD | `450.00` | `1988.74` | `2244.70` | `3818.26` | -115,223.16 USD | `-11.41%` | `25X Cross` |
| `2004` | `0xc10f...23b3` | `LONG` | 1,010,115.00 USD | `450.00` | `2366.44` | `2244.70` | `2016.72` | -54,783.27 USD | `-5.42%` | `25X Cross` |
| `2005` | `0xae55...2236` | `LONG` | 1,009,845.00 USD | `450.00` | `2510.21` | `2244.70` | `0.000000` | -119,752.50 USD | `-11.86%` | `25X Cross` |
| `2012` | `0xaa7a...af37` | `LONG` | 1,005,384.71 USD | `448.03` | `2212.37` | `2244.70` | `0.000000` | 14,168.47 USD | `+1.41%` | `20X Cross` |
| `2018` | `0xac26...a9c7` | `SHORT` | 1,001,173.57 USD | `446.14` | `2192.58` | `2244.70` | `8631.08` | -22,983.03 USD | `-2.30%` | `20X Cross` |

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
  * 24H Horizon: Short MP=`2251.83` (Vol: 25,800,000.00 USD, Dist: `+0.39%`) | Long MP=`2174.37` (Vol: 35,800,000.00 USD, Dist: `--3.06%`)
  * 48H Horizon: Short MP=`2402.29` (Vol: 25,600,000.00 USD, Dist: `+7.10%`) | Long MP=`2174.00` (Vol: 35,800,000.00 USD, Dist: `--3.08%`)
  * 3D Horizon: Short MP=`2402.29` (Vol: 31,100,000.00 USD, Dist: `+7.10%`) | Long MP=`2174.00` (Vol: 35,800,000.00 USD, Dist: `--3.08%`)
  * 7D Horizon: Short MP=`2401.80` (Vol: 50,700,000.00 USD, Dist: `+7.08%`) | Long MP=`2175.27` (Vol: 44,800,000.00 USD, Dist: `--3.02%`)
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
| `7D` | `Long Liquidation` | `1972.00` | 999,240,000.00 USD | 999,240,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1975.00` | 1,950,000.00 USD | 213,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1975.30` | 999,110,000.00 USD | 999,110,000.00 USD | 0.00 USD | 0.00 USD | 49,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1978.60` | 999,060,000.00 USD | 999,060,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1981.90` | 996,820,000.00 USD | 996,820,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1985.00` | 5,060,000.00 USD | 211,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1985.90` | 654,590,000.00 USD | 654,590,000.00 USD | 1,930,000.00 USD | 1,230,000.00 USD | 20,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1988.40` | 651,410,000.00 USD | 651,410,000.00 USD | 1,010,000.00 USD | 660,220.00 USD | 357,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1988.50` | 996,610,000.00 USD | 996,610,000.00 USD | 3,730,000.00 USD | 1,780,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1990.90` | 649,380,000.00 USD | 649,380,000.00 USD | 1,580,000.00 USD | 569,330.00 USD | 444,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1991.80` | 991,110,000.00 USD | 991,110,000.00 USD | 1,390,000.00 USD | 1,320,000.00 USD | 38,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1993.40` | 646,780,000.00 USD | 646,780,000.00 USD | 202,370.00 USD | 596,570.00 USD | 21,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1995.00` | 1,560,000.00 USD | 206,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1995.10` | 988,360,000.00 USD | 988,360,000.00 USD | 1,340,000.00 USD | 0.00 USD | 808,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1995.90` | 645,960,000.00 USD | 645,960,000.00 USD | 412,250.00 USD | 61,370.00 USD | 304,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2000.90` | 645,190,000.00 USD | 645,190,000.00 USD | 0.00 USD | 18,870.00 USD | 487,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2003.40` | 644,680,000.00 USD | 644,680,000.00 USD | 0.00 USD | 198,200.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2005.00` | 986,210,000.00 USD | 986,210,000.00 USD | 0.00 USD | 266,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2005.00` | 2,090,000.00 USD | 204,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2005.90` | 644,480,000.00 USD | 644,480,000.00 USD | 14,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2008.40` | 644,470,000.00 USD | 644,470,000.00 USD | 0.00 USD | 224,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2010.90` | 644,240,000.00 USD | 644,240,000.00 USD | 48,560.00 USD | 308,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2011.60` | 985,940,000.00 USD | 985,940,000.00 USD | 170,840.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2013.40` | 643,880,000.00 USD | 643,880,000.00 USD | 250,530.00 USD | 241,730.00 USD | 17,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2015.00` | 5,730,000.00 USD | 202,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2015.90` | 643,370,000.00 USD | 643,370,000.00 USD | 303,600.00 USD | 497,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2018.40` | 642,570,000.00 USD | 642,570,000.00 USD | 737,290.00 USD | 872,060.00 USD | 550,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2020.90` | 640,410,000.00 USD | 640,410,000.00 USD | 973,110.00 USD | 985,760.00 USD | 145,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2023.40` | 638,310,000.00 USD | 638,310,000.00 USD | 0.00 USD | 27,630.00 USD | 479,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2024.80` | 985,770,000.00 USD | 985,770,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2025.00` | 2,100,000.00 USD | 196,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2025.90` | 637,800,000.00 USD | 637,800,000.00 USD | 0.00 USD | 1,100,000.00 USD | 28,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2028.10` | 985,590,000.00 USD | 985,590,000.00 USD | 0.00 USD | 0.00 USD | 35,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2028.40` | 636,670,000.00 USD | 636,670,000.00 USD | 1,430,000.00 USD | 978,910.00 USD | 598,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2030.90` | 633,670,000.00 USD | 633,670,000.00 USD | 677,540.00 USD | 366,120.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2031.40` | 985,560,000.00 USD | 985,560,000.00 USD | 0.00 USD | 3,520,000.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2033.40` | 631,550,000.00 USD | 631,550,000.00 USD | 941,100.00 USD | 1,490,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2034.70` | 980,990,000.00 USD | 980,990,000.00 USD | 0.00 USD | 186,130.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2035.00` | 1,080,000.00 USD | 194,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2035.90` | 629,120,000.00 USD | 629,120,000.00 USD | 985,830.00 USD | 19,490.00 USD | 176,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2038.00` | 979,450,000.00 USD | 979,450,000.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2038.40` | 627,940,000.00 USD | 627,940,000.00 USD | 939,380.00 USD | 458,110.00 USD | 377,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2040.90` | 626,160,000.00 USD | 626,160,000.00 USD | 626,840.00 USD | 178,560.00 USD | 176,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2043.40` | 625,180,000.00 USD | 625,180,000.00 USD | 0.00 USD | 0.00 USD | 20,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2044.60` | 977,850,000.00 USD | 977,850,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2045.00` | 2,000,000.00 USD | 193,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2045.90` | 625,160,000.00 USD | 625,160,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2048.40` | 625,130,000.00 USD | 625,130,000.00 USD | 518,440.00 USD | 0.00 USD | 357,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2050.90` | 624,260,000.00 USD | 624,260,000.00 USD | 0.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2051.20` | 977,550,000.00 USD | 977,550,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2053.40` | 623,200,000.00 USD | 623,200,000.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2054.50` | 977,330,000.00 USD | 977,330,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2055.00` | 5,940,000.00 USD | 191,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2055.90` | 623,080,000.00 USD | 623,080,000.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2057.80` | 975,040,000.00 USD | 975,040,000.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2058.40` | 622,840,000.00 USD | 622,840,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2060.90` | 622,090,000.00 USD | 622,090,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2061.10` | 974,990,000.00 USD | 974,990,000.00 USD | 1,700,000.00 USD | 1,310,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2063.40` | 622,010,000.00 USD | 622,010,000.00 USD | 563,140.00 USD | 494,150.00 USD | 510,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2064.40` | 970,270,000.00 USD | 970,270,000.00 USD | 1,230,000.00 USD | 1,080,000.00 USD | 945,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2065.00` | 13,860,000.00 USD | 185,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2065.90` | 620,440,000.00 USD | 620,440,000.00 USD | 387,410.00 USD | 42,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2067.70` | 967,010,000.00 USD | 967,010,000.00 USD | 292,400.00 USD | 1,180,000.00 USD | 927,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2068.40` | 620,010,000.00 USD | 620,010,000.00 USD | 57,300.00 USD | 624,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2070.90` | 619,330,000.00 USD | 619,330,000.00 USD | 47,910.00 USD | 534,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2071.00` | 964,610,000.00 USD | 964,610,000.00 USD | 4,230,000.00 USD | 3,040,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2073.40` | 618,750,000.00 USD | 618,750,000.00 USD | 65,350.00 USD | 20,640.00 USD | 428,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2074.30` | 956,110,000.00 USD | 956,110,000.00 USD | 4,000,000.00 USD | 2,720,000.00 USD | 3,720,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 2,720,000.00 USD | 171,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2075.90` | 618,230,000.00 USD | 618,230,000.00 USD | 574,450.00 USD | 373,260.00 USD | 178,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2077.60` | 945,670,000.00 USD | 945,670,000.00 USD | 4,430,000.00 USD | 4,400,000.00 USD | 2,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2078.40` | 617,100,000.00 USD | 617,100,000.00 USD | 990,930.00 USD | 763,220.00 USD | 335,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2080.90` | 615,010,000.00 USD | 615,010,000.00 USD | 973,430.00 USD | 785,280.00 USD | 206,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2080.90` | 934,570,000.00 USD | 934,570,000.00 USD | 5,690,000.00 USD | 3,540,000.00 USD | 2,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2083.40` | 613,050,000.00 USD | 613,050,000.00 USD | 1,030,000.00 USD | 886,730.00 USD | 423,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2084.20` | 922,360,000.00 USD | 922,360,000.00 USD | 1,660,000.00 USD | 1,490,000.00 USD | 3,500,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 13,600,000.00 USD | 169,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2085.90` | 610,700,000.00 USD | 610,700,000.00 USD | 944,060.00 USD | 293,180.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2087.50` | 915,710,000.00 USD | 915,710,000.00 USD | 5,220,000.00 USD | 3,230,000.00 USD | 3,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2088.40` | 607,950,000.00 USD | 607,950,000.00 USD | 1,380,000.00 USD | 497,110.00 USD | 220,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2090.80` | 904,210,000.00 USD | 904,210,000.00 USD | 4,410,000.00 USD | 976,840.00 USD | 6,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2090.90` | 605,840,000.00 USD | 605,840,000.00 USD | 1,250,000.00 USD | 318,880.00 USD | 548,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2093.40` | 603,730,000.00 USD | 603,730,000.00 USD | 1,270,000.00 USD | 406,630.00 USD | 979,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2094.10` | 891,840,000.00 USD | 891,840,000.00 USD | 5,350,000.00 USD | 1,660,000.00 USD | 2,950,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 1,380,000.00 USD | 155,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2095.90` | 601,080,000.00 USD | 601,080,000.00 USD | 1,190,000.00 USD | 1,660,000.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2097.40` | 881,890,000.00 USD | 881,890,000.00 USD | 2,280,000.00 USD | 3,580,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2098.40` | 596,570,000.00 USD | 596,570,000.00 USD | 296,850.00 USD | 1,460,000.00 USD | 248,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2100.70` | 874,740,000.00 USD | 874,740,000.00 USD | 1,830,000.00 USD | 1,850,000.00 USD | 3,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2100.90` | 594,560,000.00 USD | 594,560,000.00 USD | 98,430.00 USD | 353,390.00 USD | 231,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2103.40` | 593,870,000.00 USD | 593,870,000.00 USD | 315,200.00 USD | 119,690.00 USD | 306,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2104.00` | 867,750,000.00 USD | 867,750,000.00 USD | 1,190,000.00 USD | 738,240.00 USD | 3,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 2,280,000.00 USD | 154,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2105.90` | 593,130,000.00 USD | 593,130,000.00 USD | 3,610,000.00 USD | 1,160,000.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2107.30` | 862,790,000.00 USD | 862,790,000.00 USD | 8,720,000.00 USD | 1,150,000.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2108.40` | 587,190,000.00 USD | 587,190,000.00 USD | 656,240.00 USD | 21,400.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2110.60` | 851,730,000.00 USD | 851,730,000.00 USD | 2,970,000.00 USD | 2,360,000.00 USD | 2,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2110.90` | 586,500,000.00 USD | 586,500,000.00 USD | 36,110.00 USD | 81,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2113.40` | 586,390,000.00 USD | 586,390,000.00 USD | 866,490.00 USD | 520,660.00 USD | 249,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2113.90` | 843,870,000.00 USD | 843,870,000.00 USD | 1,780,000.00 USD | 1,810,000.00 USD | 3,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 2,910,000.00 USD | 151,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2115.90` | 584,750,000.00 USD | 584,750,000.00 USD | 722,960.00 USD | 1,180,000.00 USD | 935,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2117.20` | 836,690,000.00 USD | 836,690,000.00 USD | 2,410,000.00 USD | 2,380,000.00 USD | 2,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2118.40` | 581,910,000.00 USD | 581,910,000.00 USD | 5,570,000.00 USD | 3,070,000.00 USD | 888,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2120.50` | 829,430,000.00 USD | 829,430,000.00 USD | 13,880,000.00 USD | 5,790,000.00 USD | 2,800,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2120.90` | 572,380,000.00 USD | 572,380,000.00 USD | 4,680,000.00 USD | 1,980,000.00 USD | 904,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2123.40` | 564,820,000.00 USD | 564,820,000.00 USD | 8,080,000.00 USD | 3,300,000.00 USD | 2,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2123.80` | 806,960,000.00 USD | 806,960,000.00 USD | 7,610,000.00 USD | 7,900,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 123,240,000.00 USD | 148,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2125.90` | 551,110,000.00 USD | 551,110,000.00 USD | 3,480,000.00 USD | 2,220,000.00 USD | 837,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2127.10` | 789,630,000.00 USD | 789,630,000.00 USD | 2,760,000.00 USD | 4,420,000.00 USD | 5,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2128.40` | 544,570,000.00 USD | 544,570,000.00 USD | 3,180,000.00 USD | 2,480,000.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2130.40` | 776,910,000.00 USD | 776,910,000.00 USD | 5,410,000.00 USD | 2,580,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2130.90` | 537,400,000.00 USD | 537,400,000.00 USD | 296,080.00 USD | 18,610.00 USD | 344,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2133.40` | 536,740,000.00 USD | 536,740,000.00 USD | 20,600.00 USD | 590,650.00 USD | 1,280,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2133.70` | 767,220,000.00 USD | 767,220,000.00 USD | 2,550,000.00 USD | 715,940.00 USD | 323,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 4,840,000.00 USD | 25,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2135.90` | 534,850,000.00 USD | 534,850,000.00 USD | 21,090.00 USD | 1,010,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2137.00` | 763,630,000.00 USD | 763,630,000.00 USD | 746,340.00 USD | 1,510,000.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2138.40` | 533,820,000.00 USD | 533,820,000.00 USD | 36,740.00 USD | 142,010.00 USD | 64,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2140.30` | 761,330,000.00 USD | 761,330,000.00 USD | 2,260,000.00 USD | 1,200,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2140.90` | 533,580,000.00 USD | 533,580,000.00 USD | 130,510.00 USD | 830,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2143.40` | 532,610,000.00 USD | 532,610,000.00 USD | 539,840.00 USD | 2,100,000.00 USD | 17,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2143.60` | 757,070,000.00 USD | 757,070,000.00 USD | 1,200,000.00 USD | 1,420,000.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 5,020,000.00 USD | 20,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2145.90` | 529,950,000.00 USD | 529,950,000.00 USD | 945,130.00 USD | 1,500,000.00 USD | 124,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2146.90` | 754,180,000.00 USD | 754,180,000.00 USD | 1,060,000.00 USD | 938,520.00 USD | 134,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2148.40` | 527,380,000.00 USD | 527,380,000.00 USD | 6,600,000.00 USD | 1,740,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2150.20` | 752,050,000.00 USD | 752,050,000.00 USD | 485,890.00 USD | 838,260.00 USD | 331,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2150.90` | 517,680,000.00 USD | 517,680,000.00 USD | 3,200,000.00 USD | 2,580,000.00 USD | 359,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2153.40` | 511,550,000.00 USD | 511,550,000.00 USD | 830,850.00 USD | 1,760,000.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2153.50` | 750,400,000.00 USD | 750,400,000.00 USD | 11,310,000.00 USD | 311,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 3,970,000.00 USD | 15,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2155.90` | 507,360,000.00 USD | 507,360,000.00 USD | 3,700,000.00 USD | 2,530,000.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2156.80` | 738,780,000.00 USD | 738,780,000.00 USD | 2,560,000.00 USD | 2,010,000.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2158.40` | 500,030,000.00 USD | 500,030,000.00 USD | 774,060.00 USD | 739,710.00 USD | 904,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2160.10` | 732,160,000.00 USD | 732,160,000.00 USD | 2,190,000.00 USD | 2,550,000.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2160.90` | 497,610,000.00 USD | 497,610,000.00 USD | 5,680,000.00 USD | 5,490,000.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2163.40` | 484,900,000.00 USD | 484,900,000.00 USD | 12,860,000.00 USD | 10,630,000.00 USD | 2,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2163.40` | 726,160,000.00 USD | 726,160,000.00 USD | 21,210,000.00 USD | 11,130,000.00 USD | 518,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 5,390,000.00 USD | 11,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2165.90` | 459,060,000.00 USD | 459,060,000.00 USD | 11,060,000.00 USD | 11,880,000.00 USD | 4,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2166.70` | 693,300,000.00 USD | 693,300,000.00 USD | 5,300,000.00 USD | 15,400,000.00 USD | 2,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2168.40` | 431,520,000.00 USD | 431,520,000.00 USD | 16,140,000.00 USD | 6,570,000.00 USD | 5,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2170.00` | 669,630,000.00 USD | 669,630,000.00 USD | 10,280,000.00 USD | 15,310,000.00 USD | 5,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2170.90` | 403,750,000.00 USD | 403,750,000.00 USD | 23,580,000.00 USD | 10,800,000.00 USD | 6,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2173.30` | 638,550,000.00 USD | 638,550,000.00 USD | 30,550,000.00 USD | 828,350.00 USD | 5,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2173.40` | 362,530,000.00 USD | 362,530,000.00 USD | 7,740,000.00 USD | 1,390,000.00 USD | 3,800,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 5,680,000.00 USD | 6,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2175.90` | 349,600,000.00 USD | 349,600,000.00 USD | 1,960,000.00 USD | 355,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2176.60` | 601,620,000.00 USD | 601,620,000.00 USD | 5,390,000.00 USD | 1,330,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2178.40` | 347,290,000.00 USD | 347,290,000.00 USD | 771,300.00 USD | 94,350.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2180.90` | 343,600,000.00 USD | 343,600,000.00 USD | 853,380.00 USD | 1,360,000.00 USD | 4,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2183.20` | 592,090,000.00 USD | 592,090,000.00 USD | 1,760,000.00 USD | 0.00 USD | 3,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2183.40` | 337,340,000.00 USD | 337,340,000.00 USD | 73,470.00 USD | 26,540.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2185.00` | 618,490.00 USD | 731,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2185.90` | 335,980,000.00 USD | 335,980,000.00 USD | 310,640.00 USD | 1,660,000.00 USD | 4,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2186.50` | 586,390,000.00 USD | 586,390,000.00 USD | 37,310,000.00 USD | 19,060,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2188.40` | 329,790,000.00 USD | 329,790,000.00 USD | 3,960,000.00 USD | 2,270,000.00 USD | 6,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2189.80` | 530,020,000.00 USD | 530,020,000.00 USD | 12,430,000.00 USD | 19,940,000.00 USD | 4,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2190.90` | 317,390,000.00 USD | 317,390,000.00 USD | 5,380,000.00 USD | 3,630,000.00 USD | 3,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2193.10` | 493,080,000.00 USD | 493,080,000.00 USD | 0.00 USD | 14,900,000.00 USD | 8,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2193.40` | 304,880,000.00 USD | 304,880,000.00 USD | 5,150,000.00 USD | 5,220,000.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 107,420.00 USD | 112,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2195.90` | 293,460,000.00 USD | 293,460,000.00 USD | 8,270,000.00 USD | 745,290.00 USD | 2,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2196.40` | 470,090,000.00 USD | 470,090,000.00 USD | 383,690.00 USD | 243,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2198.40` | 281,460,000.00 USD | 281,460,000.00 USD | 217,090.00 USD | 2,760,000.00 USD | 3,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2199.70` | 469,470,000.00 USD | 469,470,000.00 USD | 0.00 USD | 0.00 USD | 7,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2200.90` | 275,170,000.00 USD | 275,170,000.00 USD | 7,060,000.00 USD | 188,700.00 USD | 6,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2203.00` | 462,030,000.00 USD | 462,030,000.00 USD | 4,310,000.00 USD | 0.00 USD | 3,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2203.40` | 261,110,000.00 USD | 261,110,000.00 USD | 821,280.00 USD | 3,440,000.00 USD | 128,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 5,310.00 USD | 5,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2205.90` | 256,720,000.00 USD | 256,720,000.00 USD | 146,940.00 USD | 108,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2206.30` | 454,400,000.00 USD | 454,400,000.00 USD | 1,490,000.00 USD | 588,950.00 USD | 4,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2208.40` | 256,460,000.00 USD | 256,460,000.00 USD | 0.00 USD | 3,680,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2209.60` | 447,680,000.00 USD | 447,680,000.00 USD | 0.00 USD | 0.00 USD | 9,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2210.90` | 252,780,000.00 USD | 252,780,000.00 USD | 104,760.00 USD | 3,480,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2212.90` | 438,520,000.00 USD | 438,520,000.00 USD | 1,710,000.00 USD | 1,060,000.00 USD | 4,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2213.40` | 249,190,000.00 USD | 249,190,000.00 USD | 5,680,000.00 USD | 3,100,000.00 USD | 63,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2215.90` | 240,340,000.00 USD | 240,340,000.00 USD | 0.00 USD | 1,650,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2216.20` | 431,660,000.00 USD | 431,660,000.00 USD | 0.00 USD | 0.00 USD | 495,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2218.40` | 238,690,000.00 USD | 238,690,000.00 USD | 7,310,000.00 USD | 1,490,000.00 USD | 64,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2219.50` | 431,160,000.00 USD | 431,160,000.00 USD | 22,400,000.00 USD | 487,520.00 USD | 3,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2220.90` | 229,830,000.00 USD | 229,830,000.00 USD | 988,750.00 USD | 4,370,000.00 USD | 944,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2222.80` | 404,580,000.00 USD | 404,580,000.00 USD | 815,570.00 USD | 12,070,000.00 USD | 17,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2223.40` | 223,530,000.00 USD | 223,530,000.00 USD | 14,680,000.00 USD | 7,600.00 USD | 3,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2225.90` | 204,980,000.00 USD | 204,980,000.00 USD | 10,100,000.00 USD | 2,470,000.00 USD | 2,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2226.10` | 373,990,000.00 USD | 373,990,000.00 USD | 9,390,000.00 USD | 15,470,000.00 USD | 13,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2228.40` | 189,640,000.00 USD | 189,640,000.00 USD | 20,850,000.00 USD | 15,540,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2229.40` | 335,550,000.00 USD | 335,550,000.00 USD | 47,950,000.00 USD | 33,560,000.00 USD | 21,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2230.90` | 152,020,000.00 USD | 152,020,000.00 USD | 41,560,000.00 USD | 0.00 USD | 15,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2232.70` | 233,010,000.00 USD | 233,010,000.00 USD | 24,580,000.00 USD | 46,390,000.00 USD | 28,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2233.40` | 94,840,000.00 USD | 94,840,000.00 USD | 22,450,000.00 USD | 6,600,000.00 USD | 15,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2235.00` | 14,960.00 USD | 14,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2235.90` | 50,580,000.00 USD | 50,580,000.00 USD | 7,610,000.00 USD | 0.00 USD | 21,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2236.00` | 134,040,000.00 USD | 134,040,000.00 USD | 30,150,000.00 USD | 23,260,000.00 USD | 26,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2238.40` | 21,460,000.00 USD | 21,460,000.00 USD | 11,960,000.00 USD | 0.00 USD | 2,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2239.30` | 54,150,000.00 USD | 54,150,000.00 USD | 39,050,000.00 USD | 0.00 USD | 8,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2240.90` | 6,520,000.00 USD | 6,520,000.00 USD | 3,570,000.00 USD | 0.00 USD | 2,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2242.60` | 6,760,000.00 USD | 6,760,000.00 USD | 6,760,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2243.40` | 192,730.00 USD | 192,730.00 USD | 0.00 USD | 141,810.00 USD | 50,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2245.00` | 1,800,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2245.90` | 3,130,000.00 USD | 3,130,000.00 USD | 488,000.00 USD | 2,300,000.00 USD | 148,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2245.90` | 3,210,000.00 USD | 3,210,000.00 USD | 2,070,000.00 USD | 1,030,000.00 USD | 102,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2248.40` | 9,180,000.00 USD | 9,180,000.00 USD | 2,350,000.00 USD | 2,340,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2249.20` | 10,470,000.00 USD | 10,470,000.00 USD | 3,350,000.00 USD | 2,660,000.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2250.90` | 27,960,000.00 USD | 27,960,000.00 USD | 10,350,000.00 USD | 7,210,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2252.50` | 40,270,000.00 USD | 40,270,000.00 USD | 20,930,000.00 USD | 8,880,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2253.40` | 44,930,000.00 USD | 44,930,000.00 USD | 8,890,000.00 USD | 6,290,000.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2255.00` | 2,970,000.00 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2255.80` | 58,310,000.00 USD | 58,310,000.00 USD | 7,010,000.00 USD | 10,520,000.00 USD | 514,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2255.90` | 65,050,000.00 USD | 65,050,000.00 USD | 10,100,000.00 USD | 6,820,000.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2258.40` | 87,730,000.00 USD | 87,730,000.00 USD | 13,730,000.00 USD | 7,120,000.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2259.10` | 88,610,000.00 USD | 88,610,000.00 USD | 18,800,000.00 USD | 7,450,000.00 USD | 4,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2260.90` | 105,450,000.00 USD | 105,450,000.00 USD | 9,070,000.00 USD | 6,920,000.00 USD | 1,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2262.40` | 96,990,000.00 USD | 96,990,000.00 USD | 6,720,000.00 USD | 1,460,000.00 USD | 210,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2263.40` | 134,000,000.00 USD | 134,000,000.00 USD | 13,630,000.00 USD | 8,540,000.00 USD | 6,380,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2265.00` | 2,310,000.00 USD | 7,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2265.70` | 103,320,000.00 USD | 103,320,000.00 USD | 0.00 USD | 0.00 USD | 6,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2265.90` | 152,530,000.00 USD | 152,530,000.00 USD | 2,890,000.00 USD | 9,340,000.00 USD | 6,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2268.40` | 173,460,000.00 USD | 173,460,000.00 USD | 14,840,000.00 USD | 2,990,000.00 USD | 3,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2269.00` | 117,590,000.00 USD | 117,590,000.00 USD | 8,610,000.00 USD | 5,650,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2270.90` | 180,850,000.00 USD | 180,850,000.00 USD | 1,520,000.00 USD | 2,550,000.00 USD | 3,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2272.30` | 126,610,000.00 USD | 126,610,000.00 USD | 7,540,000.00 USD | 1,480,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2273.40` | 184,300,000.00 USD | 184,300,000.00 USD | 297,120.00 USD | 3,160,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2275.00` | 276,460.00 USD | 7,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2275.60` | 132,110,000.00 USD | 132,110,000.00 USD | 0.00 USD | 5,500,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2275.90` | 218,530,000.00 USD | 218,530,000.00 USD | 16,110,000.00 USD | 13,670,000.00 USD | 4,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2278.40` | 233,360,000.00 USD | 233,360,000.00 USD | 0.00 USD | 8,290,000.00 USD | 6,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2278.90` | 156,050,000.00 USD | 156,050,000.00 USD | 854,200.00 USD | 12,550,000.00 USD | 10,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2280.90` | 298,020,000.00 USD | 298,020,000.00 USD | 31,700,000.00 USD | 25,110,000.00 USD | 7,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2282.20` | 253,600,000.00 USD | 253,600,000.00 USD | 0.00 USD | 83,870,000.00 USD | 13,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2283.40` | 353,880,000.00 USD | 353,880,000.00 USD | 30,290,000.00 USD | 15,240,000.00 USD | 10,320,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2285.00` | 767,790.00 USD | 8,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2285.50` | 287,260,000.00 USD | 287,260,000.00 USD | 6,610,000.00 USD | 26,950,000.00 USD | 105,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2285.90` | 374,630,000.00 USD | 374,630,000.00 USD | 4,320,000.00 USD | 11,700,000.00 USD | 4,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2288.40` | 399,810,000.00 USD | 399,810,000.00 USD | 11,850,000.00 USD | 7,800,000.00 USD | 5,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2288.80` | 318,710,000.00 USD | 318,710,000.00 USD | 8,380,000.00 USD | 8,140,000.00 USD | 14,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2290.90` | 429,650,000.00 USD | 429,650,000.00 USD | 16,890,000.00 USD | 8,780,000.00 USD | 4,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2292.10` | 327,780,000.00 USD | 327,780,000.00 USD | 7,890,000.00 USD | 517,070.00 USD | 658,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2293.40` | 449,380,000.00 USD | 449,380,000.00 USD | 12,050,000.00 USD | 2,960,000.00 USD | 4,720,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2295.00` | 3,840,000.00 USD | 11,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2295.40` | 364,250,000.00 USD | 364,250,000.00 USD | 22,930,000.00 USD | 6,820,000.00 USD | 6,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2295.90` | 471,160,000.00 USD | 471,160,000.00 USD | 4,070,000.00 USD | 12,540,000.00 USD | 5,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2298.40` | 515,860,000.00 USD | 515,860,000.00 USD | 24,240,000.00 USD | 13,280,000.00 USD | 7,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2298.70` | 387,090,000.00 USD | 387,090,000.00 USD | 897,290.00 USD | 11,270,000.00 USD | 10,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2300.90` | 546,940,000.00 USD | 546,940,000.00 USD | 8,900,000.00 USD | 10,100,000.00 USD | 12,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2302.00` | 462,400,000.00 USD | 462,400,000.00 USD | 29,960,000.00 USD | 23,280,000.00 USD | 22,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2303.40` | 582,830,000.00 USD | 582,830,000.00 USD | 18,880,000.00 USD | 10,330,000.00 USD | 6,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2305.00` | 266,780.00 USD | 12,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2305.30` | 497,570,000.00 USD | 497,570,000.00 USD | 17,280,000.00 USD | 6,960,000.00 USD | 10,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2305.90` | 617,050,000.00 USD | 617,050,000.00 USD | 13,120,000.00 USD | 12,830,000.00 USD | 8,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2308.40` | 624,940,000.00 USD | 624,940,000.00 USD | 3,440,000.00 USD | 3,270,000.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2308.60` | 501,810,000.00 USD | 501,810,000.00 USD | 1,240,000.00 USD | 2,780,000.00 USD | 231,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2310.90` | 641,570,000.00 USD | 641,570,000.00 USD | 5,900,000.00 USD | 177,810.00 USD | 10,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2311.90` | 532,050,000.00 USD | 532,050,000.00 USD | 11,460,000.00 USD | 2,650,000.00 USD | 16,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2313.40` | 655,220,000.00 USD | 655,220,000.00 USD | 4,690,000.00 USD | 7,870,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2315.00` | 1,010,000.00 USD | 13,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2315.20` | 540,800,000.00 USD | 540,800,000.00 USD | 0.00 USD | 8,120,000.00 USD | 627,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2315.90` | 686,490,000.00 USD | 686,490,000.00 USD | 9,790,000.00 USD | 14,850,000.00 USD | 6,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2318.40` | 699,800,000.00 USD | 699,800,000.00 USD | 4,480,000.00 USD | 6,580,000.00 USD | 2,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2318.50` | 555,730,000.00 USD | 555,730,000.00 USD | 4,540,000.00 USD | 4,550,000.00 USD | 5,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2320.90` | 718,040,000.00 USD | 718,040,000.00 USD | 5,820,000.00 USD | 10,490,000.00 USD | 1,940,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2321.80` | 575,470,000.00 USD | 575,470,000.00 USD | 1,110,000.00 USD | 15,930,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2323.40` | 734,510,000.00 USD | 734,510,000.00 USD | 1,710,000.00 USD | 11,180,000.00 USD | 3,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2325.00` | 1,990,000.00 USD | 15,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2325.10` | 596,540,000.00 USD | 596,540,000.00 USD | 10,150,000.00 USD | 2,540,000.00 USD | 8,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2325.90` | 749,090,000.00 USD | 749,090,000.00 USD | 1,950,000.00 USD | 6,910,000.00 USD | 5,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2328.40` | 752,930,000.00 USD | 752,930,000.00 USD | 3,010,000.00 USD | 574,320.00 USD | 261,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2328.40` | 608,540,000.00 USD | 608,540,000.00 USD | 3,860,000.00 USD | 121,880.00 USD | 8,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2330.90` | 770,540,000.00 USD | 770,540,000.00 USD | 13,640,000.00 USD | 2,780,000.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2331.70` | 638,020,000.00 USD | 638,020,000.00 USD | 29,230,000.00 USD | 241,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2333.40` | 794,580,000.00 USD | 794,580,000.00 USD | 10,900,000.00 USD | 4,910,000.00 USD | 8,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2335.00` | 690,280,000.00 USD | 690,280,000.00 USD | 20,390,000.00 USD | 19,830,000.00 USD | 12,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2335.00` | 828,820.00 USD | 16,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2335.90` | 813,210,000.00 USD | 813,210,000.00 USD | 14,240,000.00 USD | 1,440,000.00 USD | 2,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2338.30` | 720,840,000.00 USD | 720,840,000.00 USD | 22,110,000.00 USD | 0.00 USD | 8,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2338.40` | 823,500,000.00 USD | 823,500,000.00 USD | 6,390,000.00 USD | 456,810.00 USD | 3,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2340.90` | 846,660,000.00 USD | 846,660,000.00 USD | 8,120,000.00 USD | 5,180,000.00 USD | 9,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2341.60` | 757,370,000.00 USD | 757,370,000.00 USD | 4,720,000.00 USD | 17,820,000.00 USD | 14,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2343.40` | 866,070,000.00 USD | 866,070,000.00 USD | 5,780,000.00 USD | 8,480,000.00 USD | 5,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2344.90` | 784,220,000.00 USD | 784,220,000.00 USD | 1,350,000.00 USD | 16,920,000.00 USD | 8,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2345.00` | 109,700.00 USD | 16,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2345.90` | 878,480,000.00 USD | 878,480,000.00 USD | 3,680,000.00 USD | 3,280,000.00 USD | 5,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2348.20` | 820,340,000.00 USD | 820,340,000.00 USD | 561,950.00 USD | 12,390,000.00 USD | 23,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2348.40` | 893,020,000.00 USD | 893,020,000.00 USD | 5,180,000.00 USD | 6,610,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2350.90` | 937,100,000.00 USD | 937,100,000.00 USD | 27,950,000.00 USD | 4,950,000.00 USD | 11,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2351.50` | 859,010,000.00 USD | 859,010,000.00 USD | 2,930,000.00 USD | 20,680,000.00 USD | 15,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2353.40` | 944,010,000.00 USD | 944,010,000.00 USD | 3,230,000.00 USD | 3,020,000.00 USD | 652,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2354.80` | 915,860,000.00 USD | 915,860,000.00 USD | 17,130,000.00 USD | 38,220,000.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 1,220,000.00 USD | 17,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2355.90` | 963,090,000.00 USD | 963,090,000.00 USD | 4,610,000.00 USD | 11,820,000.00 USD | 2,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2358.10` | 933,010,000.00 USD | 933,010,000.00 USD | 7,110,000.00 USD | 4,040,000.00 USD | 6,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2358.40` | 979,870,000.00 USD | 979,870,000.00 USD | 5,840,000.00 USD | 4,560,000.00 USD | 6,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2360.90` | 995,600,000.00 USD | 995,600,000.00 USD | 8,480,000.00 USD | 4,940,000.00 USD | 2,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2361.40` | 941,290,000.00 USD | 941,290,000.00 USD | 4,470,000.00 USD | 3,430,000.00 USD | 374,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2363.40` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 5,380,000.00 USD | 7,760,000.00 USD | 8,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2364.70` | 957,160,000.00 USD | 957,160,000.00 USD | 4,570,000.00 USD | 373,740.00 USD | 10,920,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 3,880,000.00 USD | 21,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2365.90` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 4,890,000.00 USD | 827,140.00 USD | 2,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2368.00` | 970,990,000.00 USD | 970,990,000.00 USD | 11,660,000.00 USD | 1,780,000.00 USD | 396,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2368.40` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 6,080,000.00 USD | 4,160,000.00 USD | 3,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2370.90` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 14,780,000.00 USD | 7,330,000.00 USD | 8,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2371.30` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 25,000,000.00 USD | 0.00 USD | 54,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2373.40` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 13,840,000.00 USD | 1,790,000.00 USD | 5,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2374.60` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 19,920,000.00 USD | 121,480.00 USD | 6,980,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 894,650.00 USD | 22,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2375.90` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 6,910,000.00 USD | 4,350,000.00 USD | 4,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2377.90` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 11,180,000.00 USD | 6,190,000.00 USD | 29,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2378.40` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 1,650,000.00 USD | 2,990,000.00 USD | 3,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2380.90` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 7,600,000.00 USD | 7,600,000.00 USD | 5,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2381.20` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 4,540,000.00 USD | 4,150,000.00 USD | 19,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2383.40` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 14,580,000.00 USD | 8,580,000.00 USD | 10,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2384.50` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 22,580,000.00 USD | 22,660,000.00 USD | 45,970,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 5,770,000.00 USD | 27,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2385.90` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 7,850,000.00 USD | 10,450,000.00 USD | 3,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2387.80` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 5,540,000.00 USD | 49,830,000.00 USD | 47,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2388.40` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 11,940,000.00 USD | 6,510,000.00 USD | 4,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2390.90` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 1,700,000.00 USD | 4,340,000.00 USD | 3,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2391.10` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 5,910,000.00 USD | 52,770,000.00 USD | 41,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2393.40` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 2,570,000.00 USD | 3,590,000.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2394.40` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 60,000,000.00 USD | 32,420,000.00 USD | 40,070,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 155,990.00 USD | 28,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2395.90` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 2,220,000.00 USD | 331,850.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2397.70` | 1,680,000,000.00 USD | 1,680,000,000.00 USD | 31,080,000.00 USD | 41,130,000.00 USD | 26,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2398.40` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 1,760,000.00 USD | 4,010,000.00 USD | 3,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2400.90` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 3,930,000.00 USD | 3,570,000.00 USD | 2,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2401.00` | 1,780,000,000.00 USD | 1,780,000,000.00 USD | 51,130,000.00 USD | 28,060,000.00 USD | 25,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2403.40` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 5,860,000.00 USD | 2,250,000.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2404.30` | 1,900,000,000.00 USD | 1,900,000,000.00 USD | 61,130,000.00 USD | 29,350,000.00 USD | 31,410,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 190,970.00 USD | 28,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2405.90` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 7,520,000.00 USD | 5,810,000.00 USD | 5,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2407.60` | 1,990,000,000.00 USD | 1,990,000,000.00 USD | 29,050,000.00 USD | 35,150,000.00 USD | 19,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2408.40` | 1,300,000,000.00 USD | 1,300,000,000.00 USD | 8,160,000.00 USD | 5,490,000.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2410.90` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 4,500,000.00 USD | 4,960,000.00 USD | 5,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2410.90` | 2,070,000,000.00 USD | 2,070,000,000.00 USD | 25,670,000.00 USD | 27,460,000.00 USD | 31,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2413.40` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 6,710,000.00 USD | 3,310,000.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2414.20` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 21,950,000.00 USD | 25,190,000.00 USD | 22,860,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 164,460.00 USD | 28,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2415.90` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 3,430,000.00 USD | 2,600,000.00 USD | 3,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2417.50` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 31,300,000.00 USD | 11,500,000.00 USD | 24,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2418.40` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 3,890,000.00 USD | 2,690,000.00 USD | 3,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2420.80` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 32,960,000.00 USD | 25,550,000.00 USD | 16,800,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2420.90` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 6,230,000.00 USD | 4,640,000.00 USD | 4,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2423.40` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 825,760.00 USD | 3,030,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.10` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 20,380,000.00 USD | 29,890,000.00 USD | 23,700,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 1,180,000.00 USD | 29,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2425.90` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 1,220,000.00 USD | 1,330,000.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2427.40` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 22,390,000.00 USD | 17,570,000.00 USD | 20,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2428.40` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 1,620,000.00 USD | 1,180,000.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2430.70` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 8,890,000.00 USD | 15,370,000.00 USD | 9,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2430.90` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 3,040,000.00 USD | 2,400,000.00 USD | 677,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2433.40` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 1,850,000.00 USD | 1,680,000.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2434.00` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 19,530,000.00 USD | 9,570,000.00 USD | 13,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 198,530.00 USD | 29,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2435.90` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 2,490,000.00 USD | 1,050,000.00 USD | 161,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2437.30` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 15,680,000.00 USD | 15,080,000.00 USD | 6,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2438.40` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 476,020.00 USD | 558,660.00 USD | 15,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2440.60` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 16,940,000.00 USD | 10,790,000.00 USD | 9,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2440.90` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 2,260,000.00 USD | 723,100.00 USD | 858,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2443.40` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 412,840.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2443.90` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 5,830,000.00 USD | 12,180,000.00 USD | 8,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 66,330.00 USD | 29,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2445.90` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 472,100.00 USD | 360,870.00 USD | 10,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2447.20` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 13,820,000.00 USD | 7,510,000.00 USD | 16,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2448.40` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 321,220.00 USD | 198,200.00 USD | 687,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2450.50` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 10,570,000.00 USD | 11,560,000.00 USD | 10,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2450.90` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 1,380,000.00 USD | 56,170.00 USD | 709,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2453.40` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 3,640,000.00 USD | 3,140,000.00 USD | 2,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2453.80` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 7,240,000.00 USD | 4,290,000.00 USD | 6,910,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 186,790.00 USD | 30,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2455.90` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 622,030.00 USD | 354,570.00 USD | 318,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2457.10` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 8,340,000.00 USD | 8,890,000.00 USD | 7,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2458.40` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 1,660,000.00 USD | 1,840,000.00 USD | 479,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2460.40` | 2,730,000,000.00 USD | 2,730,000,000.00 USD | 7,080,000.00 USD | 8,140,000.00 USD | 9,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2460.90` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 515,180.00 USD | 1,330,000.00 USD | 384,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2463.40` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 303,600.00 USD | 987,360.00 USD | 829,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2463.70` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 9,430,000.00 USD | 8,280,000.00 USD | 6,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 65,770,000.00 USD | 95,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2465.90` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 448,360.00 USD | 872,060.00 USD | 550,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2467.00` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 4,840,000.00 USD | 2,920,000.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2468.40` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 288,920.00 USD | 1,680,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2470.30` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 3,190,000.00 USD | 3,080,000.00 USD | 496,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2470.90` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 973,110.00 USD | 0.00 USD | 694,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2473.40` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 0.00 USD | 308,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2473.60` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 5,860,000.00 USD | 2,920,000.00 USD | 2,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 641,630.00 USD | 96,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2475.60` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 1,100,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2476.90` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 2,660,000.00 USD | 2,410,000.00 USD | 872,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2480.20` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 1,580,000.00 USD | 6,190,000.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2483.50` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 1,750,000.00 USD | 2,280,000.00 USD | 77,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 1,640,000.00 USD | 98,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2486.80` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 30,880.00 USD | 0.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2490.10` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 1,480,000.00 USD | 1,050,000.00 USD | 188,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2493.40` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 3,210,000.00 USD | 1,830,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 6,380,000.00 USD | 104,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2496.70` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 1,370,000.00 USD | 3,690,000.00 USD | 4,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2500.00` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 358,770.00 USD | 1,980,000.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2503.30` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 27,220.00 USD | 125,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 4,450,000.00 USD | 108,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2506.60` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 2,540,000.00 USD | 903,900.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2509.90` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 2,290,000.00 USD | 2,160,000.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 700,300.00 USD | 109,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2516.50` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2519.80` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2523.10` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 945,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 5,130,000.00 USD | 114,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2526.40` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 292,400.00 USD | 1,090,000.00 USD | 200,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2529.70` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 1,510,000.00 USD | 2,770,000.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2533.00` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 4,460,000.00 USD | 1,850,000.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2535.00` | 854,240.00 USD | 115,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2536.30` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 3,170,000.00 USD | 2,460,000.00 USD | 4,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2539.60` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 4,190,000.00 USD | 3,730,000.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2542.90` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 4,070,000.00 USD | 2,950,000.00 USD | 2,920,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2545.00` | 173,450.00 USD | 115,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2546.20` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 1,900,000.00 USD | 1,140,000.00 USD | 1,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2549.50` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 4,150,000.00 USD | 3,470,000.00 USD | 4,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2552.80` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 1,920,000.00 USD | 580,780.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2555.00` | 12,390,000.00 USD | 128,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2556.10` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 4,340,000.00 USD | 549,010.00 USD | 7,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2559.40` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 5,200,000.00 USD | 1,660,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2562.70` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 1,940,000.00 USD | 3,320,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2565.00` | 60,800.00 USD | 128,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2566.00` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 1,880,000.00 USD | 1,520,000.00 USD | 2,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2569.30` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 125,250.00 USD | 739,480.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2572.60` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 2,000,000.00 USD | 890,480.00 USD | 2,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2575.00` | 41,530.00 USD | 128,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2575.90` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 2,180,000.00 USD | 440,740.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2579.20` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 1,870,000.00 USD | 1,940,000.00 USD | 1,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2582.50` | 2,970,000,000.00 USD | 2,970,000,000.00 USD | 2,830,000.00 USD | 1,030,000.00 USD | 3,720,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2585.00` | 26,520,000.00 USD | 154,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2585.80` | 2,970,000,000.00 USD | 2,970,000,000.00 USD | 883,660.00 USD | 2,700,000.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2589.10` | 2,980,000,000.00 USD | 2,980,000,000.00 USD | 2,540,000.00 USD | 536,380.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2590.30` | 2,980,000,000.00 USD | 2,980,000,000.00 USD | 1,180,000.00 USD | 304,000.00 USD | 447,590.00 USD | `Tier 1 CEX` |
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
| `7D` | `1972.00` | 999,240,000.00 USD | 0.00 USD | 999,240,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD |
| `7D` | `1975.30` | 999,110,000.00 USD | 0.00 USD | 999,110,000.00 USD | 0.00 USD | 0.00 USD | 49,530.00 USD |
| `7D` | `1978.60` | 999,060,000.00 USD | 0.00 USD | 999,060,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1981.90` | 996,820,000.00 USD | 0.00 USD | 996,820,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD |
| `1D` | `1985.90` | 654,590,000.00 USD | 0.00 USD | 654,590,000.00 USD | 1,930,000.00 USD | 1,230,000.00 USD | 20,230.00 USD |
| `1D` | `1988.40` | 651,410,000.00 USD | 0.00 USD | 651,410,000.00 USD | 1,010,000.00 USD | 660,220.00 USD | 357,670.00 USD |
| `7D` | `1988.50` | 996,610,000.00 USD | 0.00 USD | 996,610,000.00 USD | 3,730,000.00 USD | 1,780,000.00 USD | 0.00 USD |
| `1D` | `1990.90` | 649,380,000.00 USD | 0.00 USD | 649,380,000.00 USD | 1,580,000.00 USD | 569,330.00 USD | 444,540.00 USD |
| `7D` | `1991.80` | 991,110,000.00 USD | 0.00 USD | 991,110,000.00 USD | 1,390,000.00 USD | 1,320,000.00 USD | 38,060.00 USD |
| `1D` | `1993.40` | 646,780,000.00 USD | 0.00 USD | 646,780,000.00 USD | 202,370.00 USD | 596,570.00 USD | 21,590.00 USD |
| `7D` | `1995.10` | 988,360,000.00 USD | 0.00 USD | 988,360,000.00 USD | 1,340,000.00 USD | 0.00 USD | 808,380.00 USD |
| `1D` | `1995.90` | 645,960,000.00 USD | 0.00 USD | 645,960,000.00 USD | 412,250.00 USD | 61,370.00 USD | 304,820.00 USD |
| `1D` | `2000.90` | 645,190,000.00 USD | 0.00 USD | 645,190,000.00 USD | 0.00 USD | 18,870.00 USD | 487,740.00 USD |
| `1D` | `2003.40` | 644,680,000.00 USD | 0.00 USD | 644,680,000.00 USD | 0.00 USD | 198,200.00 USD | 0.00 USD |
| `7D` | `2005.00` | 986,210,000.00 USD | 0.00 USD | 986,210,000.00 USD | 0.00 USD | 266,430.00 USD | 0.00 USD |
| `1D` | `2005.90` | 644,480,000.00 USD | 0.00 USD | 644,480,000.00 USD | 14,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2008.40` | 644,470,000.00 USD | 0.00 USD | 644,470,000.00 USD | 0.00 USD | 224,500.00 USD | 0.00 USD |
| `1D` | `2010.90` | 644,240,000.00 USD | 0.00 USD | 644,240,000.00 USD | 48,560.00 USD | 308,260.00 USD | 0.00 USD |
| `7D` | `2011.60` | 985,940,000.00 USD | 0.00 USD | 985,940,000.00 USD | 170,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2013.40` | 643,880,000.00 USD | 0.00 USD | 643,880,000.00 USD | 250,530.00 USD | 241,730.00 USD | 17,710.00 USD |
| `1D` | `2015.90` | 643,370,000.00 USD | 0.00 USD | 643,370,000.00 USD | 303,600.00 USD | 497,090.00 USD | 0.00 USD |
| `1D` | `2018.40` | 642,570,000.00 USD | 0.00 USD | 642,570,000.00 USD | 737,290.00 USD | 872,060.00 USD | 550,280.00 USD |
| `1D` | `2020.90` | 640,410,000.00 USD | 0.00 USD | 640,410,000.00 USD | 973,110.00 USD | 985,760.00 USD | 145,320.00 USD |
| `1D` | `2023.40` | 638,310,000.00 USD | 0.00 USD | 638,310,000.00 USD | 0.00 USD | 27,630.00 USD | 479,950.00 USD |
| `7D` | `2024.80` | 985,770,000.00 USD | 0.00 USD | 985,770,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD |
| `1D` | `2025.90` | 637,800,000.00 USD | 0.00 USD | 637,800,000.00 USD | 0.00 USD | 1,100,000.00 USD | 28,770.00 USD |
| `7D` | `2028.10` | 985,590,000.00 USD | 0.00 USD | 985,590,000.00 USD | 0.00 USD | 0.00 USD | 35,180.00 USD |
| `1D` | `2028.40` | 636,670,000.00 USD | 0.00 USD | 636,670,000.00 USD | 1,430,000.00 USD | 978,910.00 USD | 598,090.00 USD |
| `1D` | `2030.90` | 633,670,000.00 USD | 0.00 USD | 633,670,000.00 USD | 677,540.00 USD | 366,120.00 USD | 1,080,000.00 USD |
| `7D` | `2031.40` | 985,560,000.00 USD | 0.00 USD | 985,560,000.00 USD | 0.00 USD | 3,520,000.00 USD | 1,050,000.00 USD |
| `1D` | `2033.40` | 631,550,000.00 USD | 0.00 USD | 631,550,000.00 USD | 941,100.00 USD | 1,490,000.00 USD | 0.00 USD |
| `7D` | `2034.70` | 980,990,000.00 USD | 0.00 USD | 980,990,000.00 USD | 0.00 USD | 186,130.00 USD | 1,350,000.00 USD |
| `1D` | `2035.90` | 629,120,000.00 USD | 0.00 USD | 629,120,000.00 USD | 985,830.00 USD | 19,490.00 USD | 176,820.00 USD |
| `7D` | `2038.00` | 979,450,000.00 USD | 0.00 USD | 979,450,000.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2038.40` | 627,940,000.00 USD | 0.00 USD | 627,940,000.00 USD | 939,380.00 USD | 458,110.00 USD | 377,350.00 USD |
| `1D` | `2040.90` | 626,160,000.00 USD | 0.00 USD | 626,160,000.00 USD | 626,840.00 USD | 178,560.00 USD | 176,570.00 USD |
| `1D` | `2043.40` | 625,180,000.00 USD | 0.00 USD | 625,180,000.00 USD | 0.00 USD | 0.00 USD | 20,290.00 USD |
| `7D` | `2044.60` | 977,850,000.00 USD | 0.00 USD | 977,850,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD |
| `1D` | `2045.90` | 625,160,000.00 USD | 0.00 USD | 625,160,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD |
| `1D` | `2048.40` | 625,130,000.00 USD | 0.00 USD | 625,130,000.00 USD | 518,440.00 USD | 0.00 USD | 357,950.00 USD |
| `1D` | `2050.90` | 624,260,000.00 USD | 0.00 USD | 624,260,000.00 USD | 0.00 USD | 338,980.00 USD | 717,780.00 USD |
| `7D` | `2051.20` | 977,550,000.00 USD | 0.00 USD | 977,550,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2053.40` | 623,200,000.00 USD | 0.00 USD | 623,200,000.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD |
| `7D` | `2054.50` | 977,330,000.00 USD | 0.00 USD | 977,330,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD |
| `1D` | `2055.90` | 623,080,000.00 USD | 0.00 USD | 623,080,000.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2057.80` | 975,040,000.00 USD | 0.00 USD | 975,040,000.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2058.40` | 622,840,000.00 USD | 0.00 USD | 622,840,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `1D` | `2060.90` | 622,090,000.00 USD | 0.00 USD | 622,090,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD |
| `7D` | `2061.10` | 974,990,000.00 USD | 0.00 USD | 974,990,000.00 USD | 1,700,000.00 USD | 1,310,000.00 USD | 1,710,000.00 USD |
| `1D` | `2063.40` | 622,010,000.00 USD | 0.00 USD | 622,010,000.00 USD | 563,140.00 USD | 494,150.00 USD | 510,200.00 USD |
| `7D` | `2064.40` | 970,270,000.00 USD | 0.00 USD | 970,270,000.00 USD | 1,230,000.00 USD | 1,080,000.00 USD | 945,860.00 USD |
| `1D` | `2065.90` | 620,440,000.00 USD | 0.00 USD | 620,440,000.00 USD | 387,410.00 USD | 42,880.00 USD | 0.00 USD |
| `7D` | `2067.70` | 967,010,000.00 USD | 0.00 USD | 967,010,000.00 USD | 292,400.00 USD | 1,180,000.00 USD | 927,620.00 USD |
| `1D` | `2068.40` | 620,010,000.00 USD | 0.00 USD | 620,010,000.00 USD | 57,300.00 USD | 624,040.00 USD | 0.00 USD |
| `1D` | `2070.90` | 619,330,000.00 USD | 0.00 USD | 619,330,000.00 USD | 47,910.00 USD | 534,600.00 USD | 0.00 USD |
| `7D` | `2071.00` | 964,610,000.00 USD | 0.00 USD | 964,610,000.00 USD | 4,230,000.00 USD | 3,040,000.00 USD | 1,230,000.00 USD |
| `1D` | `2073.40` | 618,750,000.00 USD | 0.00 USD | 618,750,000.00 USD | 65,350.00 USD | 20,640.00 USD | 428,640.00 USD |
| `7D` | `2074.30` | 956,110,000.00 USD | 0.00 USD | 956,110,000.00 USD | 4,000,000.00 USD | 2,720,000.00 USD | 3,720,000.00 USD |
| `1D` | `2075.90` | 618,230,000.00 USD | 0.00 USD | 618,230,000.00 USD | 574,450.00 USD | 373,260.00 USD | 178,780.00 USD |
| `7D` | `2077.60` | 945,670,000.00 USD | 0.00 USD | 945,670,000.00 USD | 4,430,000.00 USD | 4,400,000.00 USD | 2,270,000.00 USD |
| `1D` | `2078.40` | 617,100,000.00 USD | 0.00 USD | 617,100,000.00 USD | 990,930.00 USD | 763,220.00 USD | 335,490.00 USD |
| `1D` | `2080.90` | 615,010,000.00 USD | 0.00 USD | 615,010,000.00 USD | 973,430.00 USD | 785,280.00 USD | 206,930.00 USD |
| `7D` | `2080.90` | 934,570,000.00 USD | 0.00 USD | 934,570,000.00 USD | 5,690,000.00 USD | 3,540,000.00 USD | 2,980,000.00 USD |
| `1D` | `2083.40` | 613,050,000.00 USD | 0.00 USD | 613,050,000.00 USD | 1,030,000.00 USD | 886,730.00 USD | 423,380.00 USD |
| `7D` | `2084.20` | 922,360,000.00 USD | 0.00 USD | 922,360,000.00 USD | 1,660,000.00 USD | 1,490,000.00 USD | 3,500,000.00 USD |
| `1D` | `2085.90` | 610,700,000.00 USD | 0.00 USD | 610,700,000.00 USD | 944,060.00 USD | 293,180.00 USD | 1,520,000.00 USD |
| `7D` | `2087.50` | 915,710,000.00 USD | 0.00 USD | 915,710,000.00 USD | 5,220,000.00 USD | 3,230,000.00 USD | 3,060,000.00 USD |
| `1D` | `2088.40` | 607,950,000.00 USD | 0.00 USD | 607,950,000.00 USD | 1,380,000.00 USD | 497,110.00 USD | 220,490.00 USD |
| `7D` | `2090.80` | 904,210,000.00 USD | 0.00 USD | 904,210,000.00 USD | 4,410,000.00 USD | 976,840.00 USD | 6,980,000.00 USD |
| `1D` | `2090.90` | 605,840,000.00 USD | 0.00 USD | 605,840,000.00 USD | 1,250,000.00 USD | 318,880.00 USD | 548,900.00 USD |
| `1D` | `2093.40` | 603,730,000.00 USD | 0.00 USD | 603,730,000.00 USD | 1,270,000.00 USD | 406,630.00 USD | 979,140.00 USD |
| `7D` | `2094.10` | 891,840,000.00 USD | 0.00 USD | 891,840,000.00 USD | 5,350,000.00 USD | 1,660,000.00 USD | 2,950,000.00 USD |
| `1D` | `2095.90` | 601,080,000.00 USD | 0.00 USD | 601,080,000.00 USD | 1,190,000.00 USD | 1,660,000.00 USD | 1,660,000.00 USD |
| `7D` | `2097.40` | 881,890,000.00 USD | 0.00 USD | 881,890,000.00 USD | 2,280,000.00 USD | 3,580,000.00 USD | 1,290,000.00 USD |
| `1D` | `2098.40` | 596,570,000.00 USD | 0.00 USD | 596,570,000.00 USD | 296,850.00 USD | 1,460,000.00 USD | 248,570.00 USD |
| `7D` | `2100.70` | 874,740,000.00 USD | 0.00 USD | 874,740,000.00 USD | 1,830,000.00 USD | 1,850,000.00 USD | 3,310,000.00 USD |
| `1D` | `2100.90` | 594,560,000.00 USD | 0.00 USD | 594,560,000.00 USD | 98,430.00 USD | 353,390.00 USD | 231,410.00 USD |
| `1D` | `2103.40` | 593,870,000.00 USD | 0.00 USD | 593,870,000.00 USD | 315,200.00 USD | 119,690.00 USD | 306,410.00 USD |
| `7D` | `2104.00` | 867,750,000.00 USD | 0.00 USD | 867,750,000.00 USD | 1,190,000.00 USD | 738,240.00 USD | 3,030,000.00 USD |
| `1D` | `2105.90` | 593,130,000.00 USD | 0.00 USD | 593,130,000.00 USD | 3,610,000.00 USD | 1,160,000.00 USD | 1,180,000.00 USD |
| `7D` | `2107.30` | 862,790,000.00 USD | 0.00 USD | 862,790,000.00 USD | 8,720,000.00 USD | 1,150,000.00 USD | 1,190,000.00 USD |
| `1D` | `2108.40` | 587,190,000.00 USD | 0.00 USD | 587,190,000.00 USD | 656,240.00 USD | 21,400.00 USD | 6,190.00 USD |
| `7D` | `2110.60` | 851,730,000.00 USD | 0.00 USD | 851,730,000.00 USD | 2,970,000.00 USD | 2,360,000.00 USD | 2,530,000.00 USD |
| `1D` | `2110.90` | 586,500,000.00 USD | 0.00 USD | 586,500,000.00 USD | 36,110.00 USD | 81,050.00 USD | 0.00 USD |
| `1D` | `2113.40` | 586,390,000.00 USD | 0.00 USD | 586,390,000.00 USD | 866,490.00 USD | 520,660.00 USD | 249,040.00 USD |
| `7D` | `2113.90` | 843,870,000.00 USD | 0.00 USD | 843,870,000.00 USD | 1,780,000.00 USD | 1,810,000.00 USD | 3,580,000.00 USD |
| `1D` | `2115.90` | 584,750,000.00 USD | 0.00 USD | 584,750,000.00 USD | 722,960.00 USD | 1,180,000.00 USD | 935,080.00 USD |
| `7D` | `2117.20` | 836,690,000.00 USD | 0.00 USD | 836,690,000.00 USD | 2,410,000.00 USD | 2,380,000.00 USD | 2,470,000.00 USD |
| `1D` | `2118.40` | 581,910,000.00 USD | 0.00 USD | 581,910,000.00 USD | 5,570,000.00 USD | 3,070,000.00 USD | 888,380.00 USD |
| `7D` | `2120.50` | 829,430,000.00 USD | 0.00 USD | 829,430,000.00 USD | 13,880,000.00 USD | 5,790,000.00 USD | 2,800,000.00 USD |
| `1D` | `2120.90` | 572,380,000.00 USD | 0.00 USD | 572,380,000.00 USD | 4,680,000.00 USD | 1,980,000.00 USD | 904,880.00 USD |
| `1D` | `2123.40` | 564,820,000.00 USD | 0.00 USD | 564,820,000.00 USD | 8,080,000.00 USD | 3,300,000.00 USD | 2,320,000.00 USD |
| `7D` | `2123.80` | 806,960,000.00 USD | 0.00 USD | 806,960,000.00 USD | 7,610,000.00 USD | 7,900,000.00 USD | 1,820,000.00 USD |
| `1D` | `2125.90` | 551,110,000.00 USD | 0.00 USD | 551,110,000.00 USD | 3,480,000.00 USD | 2,220,000.00 USD | 837,670.00 USD |
| `7D` | `2127.10` | 789,630,000.00 USD | 0.00 USD | 789,630,000.00 USD | 2,760,000.00 USD | 4,420,000.00 USD | 5,540,000.00 USD |
| `1D` | `2128.40` | 544,570,000.00 USD | 0.00 USD | 544,570,000.00 USD | 3,180,000.00 USD | 2,480,000.00 USD | 1,510,000.00 USD |
| `7D` | `2130.40` | 776,910,000.00 USD | 0.00 USD | 776,910,000.00 USD | 5,410,000.00 USD | 2,580,000.00 USD | 1,690,000.00 USD |
| `1D` | `2130.90` | 537,400,000.00 USD | 0.00 USD | 537,400,000.00 USD | 296,080.00 USD | 18,610.00 USD | 344,350.00 USD |
| `1D` | `2133.40` | 536,740,000.00 USD | 0.00 USD | 536,740,000.00 USD | 20,600.00 USD | 590,650.00 USD | 1,280,000.00 USD |
| `7D` | `2133.70` | 767,220,000.00 USD | 0.00 USD | 767,220,000.00 USD | 2,550,000.00 USD | 715,940.00 USD | 323,430.00 USD |
| `1D` | `2135.90` | 534,850,000.00 USD | 0.00 USD | 534,850,000.00 USD | 21,090.00 USD | 1,010,000.00 USD | 0.00 USD |
| `7D` | `2137.00` | 763,630,000.00 USD | 0.00 USD | 763,630,000.00 USD | 746,340.00 USD | 1,510,000.00 USD | 43,560.00 USD |
| `1D` | `2138.40` | 533,820,000.00 USD | 0.00 USD | 533,820,000.00 USD | 36,740.00 USD | 142,010.00 USD | 64,360.00 USD |
| `7D` | `2140.30` | 761,330,000.00 USD | 0.00 USD | 761,330,000.00 USD | 2,260,000.00 USD | 1,200,000.00 USD | 801,910.00 USD |
| `1D` | `2140.90` | 533,580,000.00 USD | 0.00 USD | 533,580,000.00 USD | 130,510.00 USD | 830,230.00 USD | 0.00 USD |
| `1D` | `2143.40` | 532,610,000.00 USD | 0.00 USD | 532,610,000.00 USD | 539,840.00 USD | 2,100,000.00 USD | 17,490.00 USD |
| `7D` | `2143.60` | 757,070,000.00 USD | 0.00 USD | 757,070,000.00 USD | 1,200,000.00 USD | 1,420,000.00 USD | 268,500.00 USD |
| `1D` | `2145.90` | 529,950,000.00 USD | 0.00 USD | 529,950,000.00 USD | 945,130.00 USD | 1,500,000.00 USD | 124,070.00 USD |
| `7D` | `2146.90` | 754,180,000.00 USD | 0.00 USD | 754,180,000.00 USD | 1,060,000.00 USD | 938,520.00 USD | 134,420.00 USD |
| `1D` | `2148.40` | 527,380,000.00 USD | 0.00 USD | 527,380,000.00 USD | 6,600,000.00 USD | 1,740,000.00 USD | 1,360,000.00 USD |
| `7D` | `2150.20` | 752,050,000.00 USD | 0.00 USD | 752,050,000.00 USD | 485,890.00 USD | 838,260.00 USD | 331,330.00 USD |
| `1D` | `2150.90` | 517,680,000.00 USD | 0.00 USD | 517,680,000.00 USD | 3,200,000.00 USD | 2,580,000.00 USD | 359,110.00 USD |
| `1D` | `2153.40` | 511,550,000.00 USD | 0.00 USD | 511,550,000.00 USD | 830,850.00 USD | 1,760,000.00 USD | 1,600,000.00 USD |
| `7D` | `2153.50` | 750,400,000.00 USD | 0.00 USD | 750,400,000.00 USD | 11,310,000.00 USD | 311,060.00 USD | 0.00 USD |
| `1D` | `2155.90` | 507,360,000.00 USD | 0.00 USD | 507,360,000.00 USD | 3,700,000.00 USD | 2,530,000.00 USD | 1,110,000.00 USD |
| `7D` | `2156.80` | 738,780,000.00 USD | 0.00 USD | 738,780,000.00 USD | 2,560,000.00 USD | 2,010,000.00 USD | 2,040,000.00 USD |
| `1D` | `2158.40` | 500,030,000.00 USD | 0.00 USD | 500,030,000.00 USD | 774,060.00 USD | 739,710.00 USD | 904,560.00 USD |
| `7D` | `2160.10` | 732,160,000.00 USD | 0.00 USD | 732,160,000.00 USD | 2,190,000.00 USD | 2,550,000.00 USD | 1,270,000.00 USD |
| `1D` | `2160.90` | 497,610,000.00 USD | 0.00 USD | 497,610,000.00 USD | 5,680,000.00 USD | 5,490,000.00 USD | 1,550,000.00 USD |
| `1D` | `2163.40` | 484,900,000.00 USD | 0.00 USD | 484,900,000.00 USD | 12,860,000.00 USD | 10,630,000.00 USD | 2,360,000.00 USD |
| `7D` | `2163.40` | 726,160,000.00 USD | 0.00 USD | 726,160,000.00 USD | 21,210,000.00 USD | 11,130,000.00 USD | 518,640.00 USD |
| `1D` | `2165.90` | 459,060,000.00 USD | 0.00 USD | 459,060,000.00 USD | 11,060,000.00 USD | 11,880,000.00 USD | 4,590,000.00 USD |
| `7D` | `2166.70` | 693,300,000.00 USD | 0.00 USD | 693,300,000.00 USD | 5,300,000.00 USD | 15,400,000.00 USD | 2,970,000.00 USD |
| `1D` | `2168.40` | 431,520,000.00 USD | 0.00 USD | 431,520,000.00 USD | 16,140,000.00 USD | 6,570,000.00 USD | 5,060,000.00 USD |
| `7D` | `2170.00` | 669,630,000.00 USD | 0.00 USD | 669,630,000.00 USD | 10,280,000.00 USD | 15,310,000.00 USD | 5,480,000.00 USD |
| `1D` | `2170.90` | 403,750,000.00 USD | 0.00 USD | 403,750,000.00 USD | 23,580,000.00 USD | 10,800,000.00 USD | 6,840,000.00 USD |
| `7D` | `2173.30` | 638,550,000.00 USD | 0.00 USD | 638,550,000.00 USD | 30,550,000.00 USD | 828,350.00 USD | 5,540,000.00 USD |
| `1D` | `2173.40` | 362,530,000.00 USD | 0.00 USD | 362,530,000.00 USD | 7,740,000.00 USD | 1,390,000.00 USD | 3,800,000.00 USD |
| `1D` | `2175.90` | 349,600,000.00 USD | 0.00 USD | 349,600,000.00 USD | 1,960,000.00 USD | 355,620.00 USD | 0.00 USD |
| `7D` | `2176.60` | 601,620,000.00 USD | 0.00 USD | 601,620,000.00 USD | 5,390,000.00 USD | 1,330,000.00 USD | 2,820,000.00 USD |
| `1D` | `2178.40` | 347,290,000.00 USD | 0.00 USD | 347,290,000.00 USD | 771,300.00 USD | 94,350.00 USD | 2,830,000.00 USD |
| `1D` | `2180.90` | 343,600,000.00 USD | 0.00 USD | 343,600,000.00 USD | 853,380.00 USD | 1,360,000.00 USD | 4,040,000.00 USD |
| `7D` | `2183.20` | 592,090,000.00 USD | 0.00 USD | 592,090,000.00 USD | 1,760,000.00 USD | 0.00 USD | 3,950,000.00 USD |
| `1D` | `2183.40` | 337,340,000.00 USD | 0.00 USD | 337,340,000.00 USD | 73,470.00 USD | 26,540.00 USD | 1,260,000.00 USD |
| `1D` | `2185.90` | 335,980,000.00 USD | 0.00 USD | 335,980,000.00 USD | 310,640.00 USD | 1,660,000.00 USD | 4,220,000.00 USD |
| `7D` | `2186.50` | 586,390,000.00 USD | 0.00 USD | 586,390,000.00 USD | 37,310,000.00 USD | 19,060,000.00 USD | 0.00 USD |
| `1D` | `2188.40` | 329,790,000.00 USD | 0.00 USD | 329,790,000.00 USD | 3,960,000.00 USD | 2,270,000.00 USD | 6,170,000.00 USD |
| `7D` | `2189.80` | 530,020,000.00 USD | 0.00 USD | 530,020,000.00 USD | 12,430,000.00 USD | 19,940,000.00 USD | 4,580,000.00 USD |
| `1D` | `2190.90` | 317,390,000.00 USD | 0.00 USD | 317,390,000.00 USD | 5,380,000.00 USD | 3,630,000.00 USD | 3,500,000.00 USD |
| `7D` | `2193.10` | 493,080,000.00 USD | 0.00 USD | 493,080,000.00 USD | 0.00 USD | 14,900,000.00 USD | 8,080,000.00 USD |
| `1D` | `2193.40` | 304,880,000.00 USD | 0.00 USD | 304,880,000.00 USD | 5,150,000.00 USD | 5,220,000.00 USD | 1,050,000.00 USD |
| `1D` | `2195.90` | 293,460,000.00 USD | 0.00 USD | 293,460,000.00 USD | 8,270,000.00 USD | 745,290.00 USD | 2,990,000.00 USD |
| `7D` | `2196.40` | 470,090,000.00 USD | 0.00 USD | 470,090,000.00 USD | 383,690.00 USD | 243,760.00 USD | 0.00 USD |
| `1D` | `2198.40` | 281,460,000.00 USD | 0.00 USD | 281,460,000.00 USD | 217,090.00 USD | 2,760,000.00 USD | 3,320,000.00 USD |
| `7D` | `2199.70` | 469,470,000.00 USD | 0.00 USD | 469,470,000.00 USD | 0.00 USD | 0.00 USD | 7,440,000.00 USD |
| `1D` | `2200.90` | 275,170,000.00 USD | 0.00 USD | 275,170,000.00 USD | 7,060,000.00 USD | 188,700.00 USD | 6,800,000.00 USD |
| `7D` | `2203.00` | 462,030,000.00 USD | 0.00 USD | 462,030,000.00 USD | 4,310,000.00 USD | 0.00 USD | 3,320,000.00 USD |
| `1D` | `2203.40` | 261,110,000.00 USD | 0.00 USD | 261,110,000.00 USD | 821,280.00 USD | 3,440,000.00 USD | 128,720.00 USD |
| `1D` | `2205.90` | 256,720,000.00 USD | 0.00 USD | 256,720,000.00 USD | 146,940.00 USD | 108,050.00 USD | 0.00 USD |
| `7D` | `2206.30` | 454,400,000.00 USD | 0.00 USD | 454,400,000.00 USD | 1,490,000.00 USD | 588,950.00 USD | 4,640,000.00 USD |
| `1D` | `2208.40` | 256,460,000.00 USD | 0.00 USD | 256,460,000.00 USD | 0.00 USD | 3,680,000.00 USD | 0.00 USD |
| `7D` | `2209.60` | 447,680,000.00 USD | 0.00 USD | 447,680,000.00 USD | 0.00 USD | 0.00 USD | 9,150,000.00 USD |
| `1D` | `2210.90` | 252,780,000.00 USD | 0.00 USD | 252,780,000.00 USD | 104,760.00 USD | 3,480,000.00 USD | 0.00 USD |
| `7D` | `2212.90` | 438,520,000.00 USD | 0.00 USD | 438,520,000.00 USD | 1,710,000.00 USD | 1,060,000.00 USD | 4,100,000.00 USD |
| `1D` | `2213.40` | 249,190,000.00 USD | 0.00 USD | 249,190,000.00 USD | 5,680,000.00 USD | 3,100,000.00 USD | 63,100.00 USD |
| `1D` | `2215.90` | 240,340,000.00 USD | 0.00 USD | 240,340,000.00 USD | 0.00 USD | 1,650,000.00 USD | 0.00 USD |
| `7D` | `2216.20` | 431,660,000.00 USD | 0.00 USD | 431,660,000.00 USD | 0.00 USD | 0.00 USD | 495,340.00 USD |
| `1D` | `2218.40` | 238,690,000.00 USD | 0.00 USD | 238,690,000.00 USD | 7,310,000.00 USD | 1,490,000.00 USD | 64,320.00 USD |
| `7D` | `2219.50` | 431,160,000.00 USD | 0.00 USD | 431,160,000.00 USD | 22,400,000.00 USD | 487,520.00 USD | 3,700,000.00 USD |
| `1D` | `2220.90` | 229,830,000.00 USD | 0.00 USD | 229,830,000.00 USD | 988,750.00 USD | 4,370,000.00 USD | 944,450.00 USD |
| `7D` | `2222.80` | 404,580,000.00 USD | 0.00 USD | 404,580,000.00 USD | 815,570.00 USD | 12,070,000.00 USD | 17,700,000.00 USD |
| `1D` | `2223.40` | 223,530,000.00 USD | 0.00 USD | 223,530,000.00 USD | 14,680,000.00 USD | 7,600.00 USD | 3,850,000.00 USD |
| `1D` | `2225.90` | 204,980,000.00 USD | 0.00 USD | 204,980,000.00 USD | 10,100,000.00 USD | 2,470,000.00 USD | 2,770,000.00 USD |
| `7D` | `2226.10` | 373,990,000.00 USD | 0.00 USD | 373,990,000.00 USD | 9,390,000.00 USD | 15,470,000.00 USD | 13,580,000.00 USD |
| `1D` | `2228.40` | 189,640,000.00 USD | 0.00 USD | 189,640,000.00 USD | 20,850,000.00 USD | 15,540,000.00 USD | 1,220,000.00 USD |
| `7D` | `2229.40` | 335,550,000.00 USD | 0.00 USD | 335,550,000.00 USD | 47,950,000.00 USD | 33,560,000.00 USD | 21,030,000.00 USD |
| `1D` | `2230.90` | 152,020,000.00 USD | 0.00 USD | 152,020,000.00 USD | 41,560,000.00 USD | 0.00 USD | 15,630,000.00 USD |
| `7D` | `2232.70` | 233,010,000.00 USD | 0.00 USD | 233,010,000.00 USD | 24,580,000.00 USD | 46,390,000.00 USD | 28,000,000.00 USD |
| `1D` | `2233.40` | 94,840,000.00 USD | 0.00 USD | 94,840,000.00 USD | 22,450,000.00 USD | 6,600,000.00 USD | 15,210,000.00 USD |
| `1D` | `2235.90` | 50,580,000.00 USD | 0.00 USD | 50,580,000.00 USD | 7,610,000.00 USD | 0.00 USD | 21,500,000.00 USD |
| `7D` | `2236.00` | 134,040,000.00 USD | 0.00 USD | 134,040,000.00 USD | 30,150,000.00 USD | 23,260,000.00 USD | 26,480,000.00 USD |
| `1D` | `2238.40` | 21,460,000.00 USD | 0.00 USD | 21,460,000.00 USD | 11,960,000.00 USD | 0.00 USD | 2,980,000.00 USD |
| `7D` | `2239.30` | 54,150,000.00 USD | 0.00 USD | 54,150,000.00 USD | 39,050,000.00 USD | 0.00 USD | 8,330,000.00 USD |
| `1D` | `2240.90` | 6,520,000.00 USD | 0.00 USD | 6,520,000.00 USD | 3,570,000.00 USD | 0.00 USD | 2,950,000.00 USD |
| `1D` | `2242.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2242.60` | 6,760,000.00 USD | 0.00 USD | 6,760,000.00 USD | 6,760,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2243.40` | 192,730.00 USD | 192,730.00 USD | 0.00 USD | 0.00 USD | 141,810.00 USD | 50,930.00 USD |
| `7D` | `2243.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2245.90` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 488,000.00 USD | 2,300,000.00 USD | 148,420.00 USD |
| `7D` | `2245.90` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 2,070,000.00 USD | 1,030,000.00 USD | 102,060.00 USD |
| `1D` | `2248.40` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 2,350,000.00 USD | 2,340,000.00 USD | 1,350,000.00 USD |
| `7D` | `2249.20` | 10,470,000.00 USD | 10,470,000.00 USD | 0.00 USD | 3,350,000.00 USD | 2,660,000.00 USD | 1,250,000.00 USD |
| `1D` | `2250.90` | 27,960,000.00 USD | 27,960,000.00 USD | 0.00 USD | 10,350,000.00 USD | 7,210,000.00 USD | 1,230,000.00 USD |
| `7D` | `2252.50` | 40,270,000.00 USD | 40,270,000.00 USD | 0.00 USD | 20,930,000.00 USD | 8,880,000.00 USD | 0.00 USD |
| `1D` | `2253.40` | 44,930,000.00 USD | 44,930,000.00 USD | 0.00 USD | 8,890,000.00 USD | 6,290,000.00 USD | 1,790,000.00 USD |
| `7D` | `2255.80` | 58,310,000.00 USD | 58,310,000.00 USD | 0.00 USD | 7,010,000.00 USD | 10,520,000.00 USD | 514,610.00 USD |
| `1D` | `2255.90` | 65,050,000.00 USD | 65,050,000.00 USD | 0.00 USD | 10,100,000.00 USD | 6,820,000.00 USD | 3,190,000.00 USD |
| `1D` | `2258.40` | 87,730,000.00 USD | 87,730,000.00 USD | 0.00 USD | 13,730,000.00 USD | 7,120,000.00 USD | 1,830,000.00 USD |
| `7D` | `2259.10` | 88,610,000.00 USD | 88,610,000.00 USD | 0.00 USD | 18,800,000.00 USD | 7,450,000.00 USD | 4,040,000.00 USD |
| `1D` | `2260.90` | 105,450,000.00 USD | 105,450,000.00 USD | 0.00 USD | 9,070,000.00 USD | 6,920,000.00 USD | 1,730,000.00 USD |
| `7D` | `2262.40` | 96,990,000.00 USD | 96,990,000.00 USD | 0.00 USD | 6,720,000.00 USD | 1,460,000.00 USD | 210,470.00 USD |
| `1D` | `2263.40` | 134,000,000.00 USD | 134,000,000.00 USD | 0.00 USD | 13,630,000.00 USD | 8,540,000.00 USD | 6,380,000.00 USD |
| `7D` | `2265.70` | 103,320,000.00 USD | 103,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,330,000.00 USD |
| `1D` | `2265.90` | 152,530,000.00 USD | 152,530,000.00 USD | 0.00 USD | 2,890,000.00 USD | 9,340,000.00 USD | 6,290,000.00 USD |
| `1D` | `2268.40` | 173,460,000.00 USD | 173,460,000.00 USD | 0.00 USD | 14,840,000.00 USD | 2,990,000.00 USD | 3,100,000.00 USD |
| `7D` | `2269.00` | 117,590,000.00 USD | 117,590,000.00 USD | 0.00 USD | 8,610,000.00 USD | 5,650,000.00 USD | 0.00 USD |
| `1D` | `2270.90` | 180,850,000.00 USD | 180,850,000.00 USD | 0.00 USD | 1,520,000.00 USD | 2,550,000.00 USD | 3,320,000.00 USD |
| `7D` | `2272.30` | 126,610,000.00 USD | 126,610,000.00 USD | 0.00 USD | 7,540,000.00 USD | 1,480,000.00 USD | 0.00 USD |
| `1D` | `2273.40` | 184,300,000.00 USD | 184,300,000.00 USD | 0.00 USD | 297,120.00 USD | 3,160,000.00 USD | 0.00 USD |
| `7D` | `2275.60` | 132,110,000.00 USD | 132,110,000.00 USD | 0.00 USD | 0.00 USD | 5,500,000.00 USD | 0.00 USD |
| `1D` | `2275.90` | 218,530,000.00 USD | 218,530,000.00 USD | 0.00 USD | 16,110,000.00 USD | 13,670,000.00 USD | 4,440,000.00 USD |
| `1D` | `2278.40` | 233,360,000.00 USD | 233,360,000.00 USD | 0.00 USD | 0.00 USD | 8,290,000.00 USD | 6,540,000.00 USD |
| `7D` | `2278.90` | 156,050,000.00 USD | 156,050,000.00 USD | 0.00 USD | 854,200.00 USD | 12,550,000.00 USD | 10,540,000.00 USD |
| `1D` | `2280.90` | 298,020,000.00 USD | 298,020,000.00 USD | 0.00 USD | 31,700,000.00 USD | 25,110,000.00 USD | 7,850,000.00 USD |
| `7D` | `2282.20` | 253,600,000.00 USD | 253,600,000.00 USD | 0.00 USD | 0.00 USD | 83,870,000.00 USD | 13,670,000.00 USD |
| `1D` | `2283.40` | 353,880,000.00 USD | 353,880,000.00 USD | 0.00 USD | 30,290,000.00 USD | 15,240,000.00 USD | 10,320,000.00 USD |
| `7D` | `2285.50` | 287,260,000.00 USD | 287,260,000.00 USD | 0.00 USD | 6,610,000.00 USD | 26,950,000.00 USD | 105,230.00 USD |
| `1D` | `2285.90` | 374,630,000.00 USD | 374,630,000.00 USD | 0.00 USD | 4,320,000.00 USD | 11,700,000.00 USD | 4,730,000.00 USD |
| `1D` | `2288.40` | 399,810,000.00 USD | 399,810,000.00 USD | 0.00 USD | 11,850,000.00 USD | 7,800,000.00 USD | 5,530,000.00 USD |
| `7D` | `2288.80` | 318,710,000.00 USD | 318,710,000.00 USD | 0.00 USD | 8,380,000.00 USD | 8,140,000.00 USD | 14,930,000.00 USD |
| `1D` | `2290.90` | 429,650,000.00 USD | 429,650,000.00 USD | 0.00 USD | 16,890,000.00 USD | 8,780,000.00 USD | 4,160,000.00 USD |
| `7D` | `2292.10` | 327,780,000.00 USD | 327,780,000.00 USD | 0.00 USD | 7,890,000.00 USD | 517,070.00 USD | 658,480.00 USD |
| `1D` | `2293.40` | 449,380,000.00 USD | 449,380,000.00 USD | 0.00 USD | 12,050,000.00 USD | 2,960,000.00 USD | 4,720,000.00 USD |
| `7D` | `2295.40` | 364,250,000.00 USD | 364,250,000.00 USD | 0.00 USD | 22,930,000.00 USD | 6,820,000.00 USD | 6,720,000.00 USD |
| `1D` | `2295.90` | 471,160,000.00 USD | 471,160,000.00 USD | 0.00 USD | 4,070,000.00 USD | 12,540,000.00 USD | 5,170,000.00 USD |
| `1D` | `2298.40` | 515,860,000.00 USD | 515,860,000.00 USD | 0.00 USD | 24,240,000.00 USD | 13,280,000.00 USD | 7,170,000.00 USD |
| `7D` | `2298.70` | 387,090,000.00 USD | 387,090,000.00 USD | 0.00 USD | 897,290.00 USD | 11,270,000.00 USD | 10,670,000.00 USD |
| `1D` | `2300.90` | 546,940,000.00 USD | 546,940,000.00 USD | 0.00 USD | 8,900,000.00 USD | 10,100,000.00 USD | 12,080,000.00 USD |
| `7D` | `2302.00` | 462,400,000.00 USD | 462,400,000.00 USD | 0.00 USD | 29,960,000.00 USD | 23,280,000.00 USD | 22,080,000.00 USD |
| `1D` | `2303.40` | 582,830,000.00 USD | 582,830,000.00 USD | 0.00 USD | 18,880,000.00 USD | 10,330,000.00 USD | 6,690,000.00 USD |
| `7D` | `2305.30` | 497,570,000.00 USD | 497,570,000.00 USD | 0.00 USD | 17,280,000.00 USD | 6,960,000.00 USD | 10,920,000.00 USD |
| `1D` | `2305.90` | 617,050,000.00 USD | 617,050,000.00 USD | 0.00 USD | 13,120,000.00 USD | 12,830,000.00 USD | 8,260,000.00 USD |
| `1D` | `2308.40` | 624,940,000.00 USD | 624,940,000.00 USD | 0.00 USD | 3,440,000.00 USD | 3,270,000.00 USD | 1,180,000.00 USD |
| `7D` | `2308.60` | 501,810,000.00 USD | 501,810,000.00 USD | 0.00 USD | 1,240,000.00 USD | 2,780,000.00 USD | 231,420.00 USD |
| `1D` | `2310.90` | 641,570,000.00 USD | 641,570,000.00 USD | 0.00 USD | 5,900,000.00 USD | 177,810.00 USD | 10,560,000.00 USD |
| `7D` | `2311.90` | 532,050,000.00 USD | 532,050,000.00 USD | 0.00 USD | 11,460,000.00 USD | 2,650,000.00 USD | 16,120,000.00 USD |
| `1D` | `2313.40` | 655,220,000.00 USD | 655,220,000.00 USD | 0.00 USD | 4,690,000.00 USD | 7,870,000.00 USD | 1,090,000.00 USD |
| `7D` | `2315.20` | 540,800,000.00 USD | 540,800,000.00 USD | 0.00 USD | 0.00 USD | 8,120,000.00 USD | 627,210.00 USD |
| `1D` | `2315.90` | 686,490,000.00 USD | 686,490,000.00 USD | 0.00 USD | 9,790,000.00 USD | 14,850,000.00 USD | 6,630,000.00 USD |
| `1D` | `2318.40` | 699,800,000.00 USD | 699,800,000.00 USD | 0.00 USD | 4,480,000.00 USD | 6,580,000.00 USD | 2,260,000.00 USD |
| `7D` | `2318.50` | 555,730,000.00 USD | 555,730,000.00 USD | 0.00 USD | 4,540,000.00 USD | 4,550,000.00 USD | 5,830,000.00 USD |
| `1D` | `2320.90` | 718,040,000.00 USD | 718,040,000.00 USD | 0.00 USD | 5,820,000.00 USD | 10,490,000.00 USD | 1,940,000.00 USD |
| `7D` | `2321.80` | 575,470,000.00 USD | 575,470,000.00 USD | 0.00 USD | 1,110,000.00 USD | 15,930,000.00 USD | 2,690,000.00 USD |
| `1D` | `2323.40` | 734,510,000.00 USD | 734,510,000.00 USD | 0.00 USD | 1,710,000.00 USD | 11,180,000.00 USD | 3,590,000.00 USD |
| `7D` | `2325.10` | 596,540,000.00 USD | 596,540,000.00 USD | 0.00 USD | 10,150,000.00 USD | 2,540,000.00 USD | 8,390,000.00 USD |
| `1D` | `2325.90` | 749,090,000.00 USD | 749,090,000.00 USD | 0.00 USD | 1,950,000.00 USD | 6,910,000.00 USD | 5,720,000.00 USD |
| `1D` | `2328.40` | 752,930,000.00 USD | 752,930,000.00 USD | 0.00 USD | 3,010,000.00 USD | 574,320.00 USD | 261,590.00 USD |
| `7D` | `2328.40` | 608,540,000.00 USD | 608,540,000.00 USD | 0.00 USD | 3,860,000.00 USD | 121,880.00 USD | 8,020,000.00 USD |
| `1D` | `2330.90` | 770,540,000.00 USD | 770,540,000.00 USD | 0.00 USD | 13,640,000.00 USD | 2,780,000.00 USD | 1,190,000.00 USD |
| `7D` | `2331.70` | 638,020,000.00 USD | 638,020,000.00 USD | 0.00 USD | 29,230,000.00 USD | 241,890.00 USD | 0.00 USD |
| `1D` | `2333.40` | 794,580,000.00 USD | 794,580,000.00 USD | 0.00 USD | 10,900,000.00 USD | 4,910,000.00 USD | 8,230,000.00 USD |
| `7D` | `2335.00` | 690,280,000.00 USD | 690,280,000.00 USD | 0.00 USD | 20,390,000.00 USD | 19,830,000.00 USD | 12,040,000.00 USD |
| `1D` | `2335.90` | 813,210,000.00 USD | 813,210,000.00 USD | 0.00 USD | 14,240,000.00 USD | 1,440,000.00 USD | 2,960,000.00 USD |
| `7D` | `2338.30` | 720,840,000.00 USD | 720,840,000.00 USD | 0.00 USD | 22,110,000.00 USD | 0.00 USD | 8,450,000.00 USD |
| `1D` | `2338.40` | 823,500,000.00 USD | 823,500,000.00 USD | 0.00 USD | 6,390,000.00 USD | 456,810.00 USD | 3,440,000.00 USD |
| `1D` | `2340.90` | 846,660,000.00 USD | 846,660,000.00 USD | 0.00 USD | 8,120,000.00 USD | 5,180,000.00 USD | 9,870,000.00 USD |
| `7D` | `2341.60` | 757,370,000.00 USD | 757,370,000.00 USD | 0.00 USD | 4,720,000.00 USD | 17,820,000.00 USD | 14,000,000.00 USD |
| `1D` | `2343.40` | 866,070,000.00 USD | 866,070,000.00 USD | 0.00 USD | 5,780,000.00 USD | 8,480,000.00 USD | 5,150,000.00 USD |
| `7D` | `2344.90` | 784,220,000.00 USD | 784,220,000.00 USD | 0.00 USD | 1,350,000.00 USD | 16,920,000.00 USD | 8,580,000.00 USD |
| `1D` | `2345.90` | 878,480,000.00 USD | 878,480,000.00 USD | 0.00 USD | 3,680,000.00 USD | 3,280,000.00 USD | 5,440,000.00 USD |
| `7D` | `2348.20` | 820,340,000.00 USD | 820,340,000.00 USD | 0.00 USD | 561,950.00 USD | 12,390,000.00 USD | 23,170,000.00 USD |
| `1D` | `2348.40` | 893,020,000.00 USD | 893,020,000.00 USD | 0.00 USD | 5,180,000.00 USD | 6,610,000.00 USD | 2,760,000.00 USD |
| `1D` | `2350.90` | 937,100,000.00 USD | 937,100,000.00 USD | 0.00 USD | 27,950,000.00 USD | 4,950,000.00 USD | 11,190,000.00 USD |
| `7D` | `2351.50` | 859,010,000.00 USD | 859,010,000.00 USD | 0.00 USD | 2,930,000.00 USD | 20,680,000.00 USD | 15,060,000.00 USD |
| `1D` | `2353.40` | 944,010,000.00 USD | 944,010,000.00 USD | 0.00 USD | 3,230,000.00 USD | 3,020,000.00 USD | 652,430.00 USD |
| `7D` | `2354.80` | 915,860,000.00 USD | 915,860,000.00 USD | 0.00 USD | 17,130,000.00 USD | 38,220,000.00 USD | 1,500,000.00 USD |
| `1D` | `2355.90` | 963,090,000.00 USD | 963,090,000.00 USD | 0.00 USD | 4,610,000.00 USD | 11,820,000.00 USD | 2,640,000.00 USD |
| `7D` | `2358.10` | 933,010,000.00 USD | 933,010,000.00 USD | 0.00 USD | 7,110,000.00 USD | 4,040,000.00 USD | 6,010,000.00 USD |
| `1D` | `2358.40` | 979,870,000.00 USD | 979,870,000.00 USD | 0.00 USD | 5,840,000.00 USD | 4,560,000.00 USD | 6,380,000.00 USD |
| `1D` | `2360.90` | 995,600,000.00 USD | 995,600,000.00 USD | 0.00 USD | 8,480,000.00 USD | 4,940,000.00 USD | 2,310,000.00 USD |
| `7D` | `2361.40` | 941,290,000.00 USD | 941,290,000.00 USD | 0.00 USD | 4,470,000.00 USD | 3,430,000.00 USD | 374,770.00 USD |
| `1D` | `2363.40` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 0.00 USD | 5,380,000.00 USD | 7,760,000.00 USD | 8,500,000.00 USD |
| `7D` | `2364.70` | 957,160,000.00 USD | 957,160,000.00 USD | 0.00 USD | 4,570,000.00 USD | 373,740.00 USD | 10,920,000.00 USD |
| `1D` | `2365.90` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 0.00 USD | 4,890,000.00 USD | 827,140.00 USD | 2,400,000.00 USD |
| `7D` | `2368.00` | 970,990,000.00 USD | 970,990,000.00 USD | 0.00 USD | 11,660,000.00 USD | 1,780,000.00 USD | 396,420.00 USD |
| `1D` | `2368.40` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 0.00 USD | 6,080,000.00 USD | 4,160,000.00 USD | 3,440,000.00 USD |
| `1D` | `2370.90` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 0.00 USD | 14,780,000.00 USD | 7,330,000.00 USD | 8,560,000.00 USD |
| `7D` | `2371.30` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 25,000,000.00 USD | 0.00 USD | 54,480,000.00 USD |
| `1D` | `2373.40` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 13,840,000.00 USD | 1,790,000.00 USD | 5,900,000.00 USD |
| `7D` | `2374.60` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 0.00 USD | 19,920,000.00 USD | 121,480.00 USD | 6,980,000.00 USD |
| `1D` | `2375.90` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 6,910,000.00 USD | 4,350,000.00 USD | 4,130,000.00 USD |
| `7D` | `2377.90` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 11,180,000.00 USD | 6,190,000.00 USD | 29,810,000.00 USD |
| `1D` | `2378.40` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 1,650,000.00 USD | 2,990,000.00 USD | 3,240,000.00 USD |
| `1D` | `2380.90` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 7,600,000.00 USD | 7,600,000.00 USD | 5,230,000.00 USD |
| `7D` | `2381.20` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 4,540,000.00 USD | 4,150,000.00 USD | 19,270,000.00 USD |
| `1D` | `2383.40` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 14,580,000.00 USD | 8,580,000.00 USD | 10,590,000.00 USD |
| `7D` | `2384.50` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 22,580,000.00 USD | 22,660,000.00 USD | 45,970,000.00 USD |
| `1D` | `2385.90` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 7,850,000.00 USD | 10,450,000.00 USD | 3,670,000.00 USD |
| `7D` | `2387.80` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 5,540,000.00 USD | 49,830,000.00 USD | 47,300,000.00 USD |
| `1D` | `2388.40` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 11,940,000.00 USD | 6,510,000.00 USD | 4,210,000.00 USD |
| `1D` | `2390.90` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 1,700,000.00 USD | 4,340,000.00 USD | 3,350,000.00 USD |
| `7D` | `2391.10` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 0.00 USD | 5,910,000.00 USD | 52,770,000.00 USD | 41,810,000.00 USD |
| `1D` | `2393.40` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 2,570,000.00 USD | 3,590,000.00 USD | 1,110,000.00 USD |
| `7D` | `2394.40` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 60,000,000.00 USD | 32,420,000.00 USD | 40,070,000.00 USD |
| `1D` | `2395.90` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 2,220,000.00 USD | 331,850.00 USD | 1,620,000.00 USD |
| `7D` | `2397.70` | 1,680,000,000.00 USD | 1,680,000,000.00 USD | 0.00 USD | 31,080,000.00 USD | 41,130,000.00 USD | 26,250,000.00 USD |
| `1D` | `2398.40` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 1,760,000.00 USD | 4,010,000.00 USD | 3,310,000.00 USD |
| `1D` | `2400.90` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 0.00 USD | 3,930,000.00 USD | 3,570,000.00 USD | 2,310,000.00 USD |
| `7D` | `2401.00` | 1,780,000,000.00 USD | 1,780,000,000.00 USD | 0.00 USD | 51,130,000.00 USD | 28,060,000.00 USD | 25,770,000.00 USD |
| `1D` | `2403.40` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 0.00 USD | 5,860,000.00 USD | 2,250,000.00 USD | 1,500,000.00 USD |
| `7D` | `2404.30` | 1,900,000,000.00 USD | 1,900,000,000.00 USD | 0.00 USD | 61,130,000.00 USD | 29,350,000.00 USD | 31,410,000.00 USD |
| `1D` | `2405.90` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 0.00 USD | 7,520,000.00 USD | 5,810,000.00 USD | 5,840,000.00 USD |
| `7D` | `2407.60` | 1,990,000,000.00 USD | 1,990,000,000.00 USD | 0.00 USD | 29,050,000.00 USD | 35,150,000.00 USD | 19,040,000.00 USD |
| `1D` | `2408.40` | 1,300,000,000.00 USD | 1,300,000,000.00 USD | 0.00 USD | 8,160,000.00 USD | 5,490,000.00 USD | 1,870,000.00 USD |
| `1D` | `2410.90` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 0.00 USD | 4,500,000.00 USD | 4,960,000.00 USD | 5,420,000.00 USD |
| `7D` | `2410.90` | 2,070,000,000.00 USD | 2,070,000,000.00 USD | 0.00 USD | 25,670,000.00 USD | 27,460,000.00 USD | 31,240,000.00 USD |
| `1D` | `2413.40` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 0.00 USD | 6,710,000.00 USD | 3,310,000.00 USD | 1,650,000.00 USD |
| `7D` | `2414.20` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 0.00 USD | 21,950,000.00 USD | 25,190,000.00 USD | 22,860,000.00 USD |
| `1D` | `2415.90` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 3,430,000.00 USD | 2,600,000.00 USD | 3,610,000.00 USD |
| `7D` | `2417.50` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 0.00 USD | 31,300,000.00 USD | 11,500,000.00 USD | 24,160,000.00 USD |
| `1D` | `2418.40` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 3,890,000.00 USD | 2,690,000.00 USD | 3,150,000.00 USD |
| `7D` | `2420.80` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 0.00 USD | 32,960,000.00 USD | 25,550,000.00 USD | 16,800,000.00 USD |
| `1D` | `2420.90` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 0.00 USD | 6,230,000.00 USD | 4,640,000.00 USD | 4,040,000.00 USD |
| `1D` | `2423.40` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 825,760.00 USD | 3,030,000.00 USD | 4,020,000.00 USD |
| `7D` | `2424.10` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 20,380,000.00 USD | 29,890,000.00 USD | 23,700,000.00 USD |
| `1D` | `2425.90` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 1,220,000.00 USD | 1,330,000.00 USD | 31,040.00 USD |
| `7D` | `2427.40` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 0.00 USD | 22,390,000.00 USD | 17,570,000.00 USD | 20,240,000.00 USD |
| `1D` | `2428.40` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 1,620,000.00 USD | 1,180,000.00 USD | 1,480,000.00 USD |
| `7D` | `2430.70` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 0.00 USD | 8,890,000.00 USD | 15,370,000.00 USD | 9,660,000.00 USD |
| `1D` | `2430.90` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 0.00 USD | 3,040,000.00 USD | 2,400,000.00 USD | 677,240.00 USD |
| `1D` | `2433.40` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 0.00 USD | 1,850,000.00 USD | 1,680,000.00 USD | 1,680,000.00 USD |
| `7D` | `2434.00` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 0.00 USD | 19,530,000.00 USD | 9,570,000.00 USD | 13,090,000.00 USD |
| `1D` | `2435.90` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 2,490,000.00 USD | 1,050,000.00 USD | 161,010.00 USD |
| `7D` | `2437.30` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 0.00 USD | 15,680,000.00 USD | 15,080,000.00 USD | 6,290,000.00 USD |
| `1D` | `2438.40` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 476,020.00 USD | 558,660.00 USD | 15,480.00 USD |
| `7D` | `2440.60` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 0.00 USD | 16,940,000.00 USD | 10,790,000.00 USD | 9,240,000.00 USD |
| `1D` | `2440.90` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 2,260,000.00 USD | 723,100.00 USD | 858,540.00 USD |
| `1D` | `2443.40` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 412,840.00 USD | 1,390,000.00 USD |
| `7D` | `2443.90` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 0.00 USD | 5,830,000.00 USD | 12,180,000.00 USD | 8,020,000.00 USD |
| `1D` | `2445.90` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 472,100.00 USD | 360,870.00 USD | 10,310.00 USD |
| `7D` | `2447.20` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 0.00 USD | 13,820,000.00 USD | 7,510,000.00 USD | 16,330,000.00 USD |
| `1D` | `2448.40` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 321,220.00 USD | 198,200.00 USD | 687,270.00 USD |
| `7D` | `2450.50` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 0.00 USD | 10,570,000.00 USD | 11,560,000.00 USD | 10,410,000.00 USD |
| `1D` | `2450.90` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 1,380,000.00 USD | 56,170.00 USD | 709,270.00 USD |
| `1D` | `2453.40` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 3,640,000.00 USD | 3,140,000.00 USD | 2,150,000.00 USD |
| `7D` | `2453.80` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 0.00 USD | 7,240,000.00 USD | 4,290,000.00 USD | 6,910,000.00 USD |
| `1D` | `2455.90` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 622,030.00 USD | 354,570.00 USD | 318,110.00 USD |
| `7D` | `2457.10` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 0.00 USD | 8,340,000.00 USD | 8,890,000.00 USD | 7,910,000.00 USD |
| `1D` | `2458.40` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 1,660,000.00 USD | 1,840,000.00 USD | 479,530.00 USD |
| `7D` | `2460.40` | 2,730,000,000.00 USD | 2,730,000,000.00 USD | 0.00 USD | 7,080,000.00 USD | 8,140,000.00 USD | 9,350,000.00 USD |
| `1D` | `2460.90` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 515,180.00 USD | 1,330,000.00 USD | 384,500.00 USD |
| `1D` | `2463.40` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 303,600.00 USD | 987,360.00 USD | 829,050.00 USD |
| `7D` | `2463.70` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 0.00 USD | 9,430,000.00 USD | 8,280,000.00 USD | 6,170,000.00 USD |
| `1D` | `2465.90` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 448,360.00 USD | 872,060.00 USD | 550,280.00 USD |
| `7D` | `2467.00` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 4,840,000.00 USD | 2,920,000.00 USD | 1,330,000.00 USD |
| `1D` | `2468.40` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 288,920.00 USD | 1,680,000.00 USD | 0.00 USD |
| `7D` | `2470.30` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 3,190,000.00 USD | 3,080,000.00 USD | 496,280.00 USD |
| `1D` | `2470.90` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 973,110.00 USD | 0.00 USD | 694,070.00 USD |
| `1D` | `2473.40` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 308,280.00 USD |
| `7D` | `2473.60` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 0.00 USD | 5,860,000.00 USD | 2,920,000.00 USD | 2,270,000.00 USD |
| `1D` | `2475.60` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 0.00 USD | 1,100,000.00 USD | 0.00 USD |
| `7D` | `2476.90` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 0.00 USD | 2,660,000.00 USD | 2,410,000.00 USD | 872,130.00 USD |
| `7D` | `2480.20` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 0.00 USD | 1,580,000.00 USD | 6,190,000.00 USD | 1,590,000.00 USD |
| `7D` | `2483.50` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 0.00 USD | 1,750,000.00 USD | 2,280,000.00 USD | 77,610.00 USD |
| `7D` | `2486.80` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 0.00 USD | 30,880.00 USD | 0.00 USD | 1,350,000.00 USD |
| `7D` | `2490.10` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 0.00 USD | 1,480,000.00 USD | 1,050,000.00 USD | 188,520.00 USD |
| `7D` | `2493.40` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 0.00 USD | 3,210,000.00 USD | 1,830,000.00 USD | 1,960,000.00 USD |
| `7D` | `2496.70` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 1,370,000.00 USD | 3,690,000.00 USD | 4,660,000.00 USD |
| `7D` | `2500.00` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 358,770.00 USD | 1,980,000.00 USD | 1,170,000.00 USD |
| `7D` | `2503.30` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 0.00 USD | 27,220.00 USD | 125,600.00 USD |
| `7D` | `2506.60` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 2,540,000.00 USD | 903,900.00 USD | 1,990,000.00 USD |
| `7D` | `2509.90` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 2,290,000.00 USD | 2,160,000.00 USD | 1,190,000.00 USD |
| `7D` | `2516.50` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD |
| `7D` | `2519.80` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD |
| `7D` | `2523.10` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 1,230,000.00 USD | 249,960.00 USD | 945,860.00 USD |
| `7D` | `2526.40` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 292,400.00 USD | 1,090,000.00 USD | 200,040.00 USD |
| `7D` | `2529.70` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 1,510,000.00 USD | 2,770,000.00 USD | 1,300,000.00 USD |
| `7D` | `2533.00` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 0.00 USD | 4,460,000.00 USD | 1,850,000.00 USD | 1,550,000.00 USD |
| `7D` | `2536.30` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 0.00 USD | 3,170,000.00 USD | 2,460,000.00 USD | 4,010,000.00 USD |
| `7D` | `2539.60` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 0.00 USD | 4,190,000.00 USD | 3,730,000.00 USD | 1,140,000.00 USD |
| `7D` | `2542.90` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 0.00 USD | 4,070,000.00 USD | 2,950,000.00 USD | 2,920,000.00 USD |
| `7D` | `2546.20` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 0.00 USD | 1,900,000.00 USD | 1,140,000.00 USD | 1,850,000.00 USD |
| `7D` | `2549.50` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 0.00 USD | 4,150,000.00 USD | 3,470,000.00 USD | 4,160,000.00 USD |
| `7D` | `2552.80` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 0.00 USD | 1,920,000.00 USD | 580,780.00 USD | 1,140,000.00 USD |
| `7D` | `2556.10` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 0.00 USD | 4,340,000.00 USD | 549,010.00 USD | 7,010,000.00 USD |
| `7D` | `2559.40` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 0.00 USD | 5,200,000.00 USD | 1,660,000.00 USD | 2,340,000.00 USD |
| `7D` | `2562.70` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 1,940,000.00 USD | 3,320,000.00 USD | 1,290,000.00 USD |
| `7D` | `2566.00` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 1,880,000.00 USD | 1,520,000.00 USD | 2,070,000.00 USD |
| `7D` | `2569.30` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 0.00 USD | 125,250.00 USD | 739,480.00 USD | 2,000,000.00 USD |
| `7D` | `2572.60` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 890,480.00 USD | 2,220,000.00 USD |
| `7D` | `2575.90` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 0.00 USD | 2,180,000.00 USD | 440,740.00 USD | 1,090,000.00 USD |
| `7D` | `2579.20` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 0.00 USD | 1,870,000.00 USD | 1,940,000.00 USD | 1,730,000.00 USD |
| `7D` | `2582.50` | 2,970,000,000.00 USD | 2,970,000,000.00 USD | 0.00 USD | 2,830,000.00 USD | 1,030,000.00 USD | 3,720,000.00 USD |
| `7D` | `2585.80` | 2,970,000,000.00 USD | 2,970,000,000.00 USD | 0.00 USD | 883,660.00 USD | 2,700,000.00 USD | 1,870,000.00 USD |
| `7D` | `2589.10` | 2,980,000,000.00 USD | 2,980,000,000.00 USD | 0.00 USD | 2,540,000.00 USD | 536,380.00 USD | 2,830,000.00 USD |
| `7D` | `2590.30` | 2,980,000,000.00 USD | 2,980,000,000.00 USD | 0.00 USD | 1,180,000.00 USD | 304,000.00 USD | 447,590.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `29.12B` | Total OI Tokens: `12,974,927.6 ETH`
  * 1h OI Change: `+0.70%` | 4h OI Change: `+0.58%` | 24h OI Change: `-3.15%`
  * Exchange Breakdown: Binance=`8.48B` | Bybit=`2.09B` | OKX=`1.81B` | Hyperliquid=`2.36B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-202.26K` | Last 24h: `1.05M` | Last 3d: `6.29M` | Last 7d: `12.86M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0020%` | **USDT OKX** | `-0.0090%` |
| **USDT Bybit** | `-0.0161%` | **USDT KuCoin** | `-0.0106%` |
| **USDT MEXC** | `0.0021%` | **USDT BingX** | `0.0021%` |
| **USDT Gate** | `-0.0120%` | **USDT Bitget** | `-0.0002%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0065%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `53.96%` | `46.04%` | `1.17` | 1,280,000,000.00 USD |
| `15M` | `Binance` | `52.62%` | `47.38%` | `1.11` | 122,730,000.00 USD |
| `15M` | `OKX` | `43.87%` | `56.13%` | `0.78` | 79,420,000.00 USD |
| `15M` | `Bybit` | `54.37%` | `45.63%` | `1.19` | 40,390,000.00 USD |
| `15M` | `KuCoin` | `63.07%` | `36.93%` | `1.71` | 904,700.00 USD |
| `15M` | `Gate` | `45.47%` | `54.53%` | `0.83` | 53,240,000.00 USD |
| `15M` | `Bitget` | `49.09%` | `50.91%` | `0.96` | 18,520,000.00 USD |
| `15M` | `BingX` | `45.13%` | `54.87%` | `0.82` | 2,660,000.00 USD |
| `15M` | `MEXC` | `34.63%` | `65.37%` | `0.53` | 10,520,000.00 USD |
| `15M` | `Bitunix` | `54.14%` | `45.86%` | `1.18` | 13,800,000.00 USD |
| `15M` | `Hyperliquid` | `40.68%` | `59.32%` | `0.69` | 11,800,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `91.39%` | `8.61%` | `10.61` | 2,040,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `55.97%` | `44.03%` | `1.27` | 905,220,000.00 USD |
| `15M` | `HTX` | `69.15%` | `30.85%` | `2.24` | 8,300,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `42.93%` | `57.07%` | `0.75` | 2,500,000.00 USD |
| `15M` | `Bitfinex` | `13.29%` | `86.71%` | `0.15` | 219,680.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `30.66%` | `69.34%` | `0.44` | 4,230,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `45.21%` | `54.79%` | `0.83` | 3,030,000.00 USD |
| `15M` | `Whale Positions` | `52.62%` | `47.38%` | `1.11` | 122,730,000.00 USD |
| `15M` | `Global Accounts` | `53.96%` | `46.04%` | `1.17` | 1,280,000,000.00 USD |
| `1H` | `ETH` | `53.75%` | `46.25%` | `1.16` | 2,430,000,000.00 USD |
| `1H` | `Binance` | `52.5%` | `47.5%` | `1.11` | 557,340,000.00 USD |
| `1H` | `OKX` | `49.1%` | `50.9%` | `0.96` | 344,490,000.00 USD |
| `1H` | `Bybit` | `57.5%` | `42.5%` | `1.35` | 117,260,000.00 USD |
| `1H` | `KuCoin` | `34.34%` | `65.66%` | `0.52` | 5,950,000.00 USD |
| `1H` | `Gate` | `49.8%` | `50.2%` | `0.99` | 234,680,000.00 USD |
| `1H` | `Bitget` | `50.78%` | `49.22%` | `1.03` | 74,340,000.00 USD |
| `1H` | `BingX` | `61.92%` | `38.08%` | `1.63` | 19,020,000.00 USD |
| `1H` | `MEXC` | `50.18%` | `49.82%` | `1.01` | 45,220,000.00 USD |
| `1H` | `Bitunix` | `52.87%` | `47.13%` | `1.12` | 66,620,000.00 USD |
| `1H` | `Hyperliquid` | `56.55%` | `43.45%` | `1.30` | 36,460,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `52.6%` | `47.4%` | `1.11` | 7,420,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `56.65%` | `43.35%` | `1.31` | 837,400,000.00 USD |
| `1H` | `HTX` | `79.99%` | `20.01%` | `4.00` | 38,720,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `45.61%` | `54.39%` | `0.84` | 7,770,000.00 USD |
| `1H` | `Bitfinex` | `18.77%` | `81.23%` | `0.23` | 1,140,000.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `40.5%` | `59.5%` | `0.68` | 12,920,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `50.27%` | `49.73%` | `1.01` | 24,070,000.00 USD |
| `1H` | `Whale Positions` | `52.5%` | `47.5%` | `1.11` | 557,340,000.00 USD |
| `1H` | `Global Accounts` | `53.75%` | `46.25%` | `1.16` | 2,430,000,000.00 USD |
| `4H` | `ETH` | `52.33%` | `47.67%` | `1.10` | 15,780,000,000.00 USD |
| `4H` | `Binance` | `51.4%` | `48.6%` | `1.06` | 4,880,000,000.00 USD |
| `4H` | `OKX` | `50.83%` | `49.17%` | `1.03` | 2,240,000,000.00 USD |
| `4H` | `Bybit` | `53.05%` | `46.95%` | `1.13` | 1,430,000,000.00 USD |
| `4H` | `KuCoin` | `60.5%` | `39.5%` | `1.53` | 56,280,000.00 USD |
| `4H` | `Gate` | `48.21%` | `51.79%` | `0.93` | 1,750,000,000.00 USD |
| `4H` | `Bitget` | `49.87%` | `50.13%` | `0.99` | 788,140,000.00 USD |
| `4H` | `BingX` | `48.61%` | `51.39%` | `0.95` | 215,240,000.00 USD |
| `4H` | `MEXC` | `47.18%` | `52.82%` | `0.89` | 670,120,000.00 USD |
| `4H` | `Bitunix` | `51.03%` | `48.97%` | `1.04` | 688,030,000.00 USD |
| `4H` | `Hyperliquid` | `53.13%` | `46.87%` | `1.13` | 1,080,000,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `63.92%` | `36.08%` | `1.77` | 113,670,000.00 USD |
| `4H` | `Crypto.com` | `50.16%` | `49.84%` | `1.01` | 54,440,000.00 USD |
| `4H` | `WhiteBIT` | `77.1%` | `22.9%` | `3.37` | 814,880,000.00 USD |
| `4H` | `HTX` | `49.46%` | `50.54%` | `0.98` | 64,110,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `51%` | `49%` | `1.04` | 575,950,000.00 USD |
| `4H` | `Bitfinex` | `55.42%` | `44.58%` | `1.24` | 12,470,000.00 USD |
| `4H` | `Kraken` | `51.36%` | `48.64%` | `1.06` | 30,520,000.00 USD |
| `4H` | `Aster` | `51.8%` | `48.2%` | `1.07` | 160,310,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.55%` | `51.45%` | `0.94` | 158,500,000.00 USD |
| `4H` | `Whale Positions` | `51.4%` | `48.6%` | `1.06` | 4,880,000,000.00 USD |
| `4H` | `Global Accounts` | `52.33%` | `47.67%` | `1.10` | 15,780,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `2208.25` | `2209.85` | `2208.25` | `2215.75` | `2207.25` | 69,365,754.50 USD | 25,046,876.87 USD | 44,318,877.64 USD | -19,272,000.77 USD | `-27.78%` | `0B / 4S` |
| `0:00 UTC` | `2215.25` | `2214.70` | `2215.25` | `2218.75` | `2208.25` | 100,318,327.91 USD | 51,517,721.13 USD | 48,800,606.78 USD | 2,717,114.35 USD | `+2.71%` | `2B / 2S` |
| `5:00 UTC` | `2219.75` | `2216.05` | `2219.75` | `2221.25` | `2210.25` | 81,002,689.38 USD | 47,369,805.78 USD | 33,632,883.60 USD | 13,736,922.17 USD | `+16.96%` | `0B / 0S` |
| `0:00 UTC` | `2229.75` | `2226.55` | `2229.75` | `2232.75` | `2219.75` | 182,767,345.67 USD | 98,774,699.85 USD | 83,992,645.82 USD | 14,782,054.04 USD | `+8.09%` | `1B / 2S` |
| `5:00 UTC` | `2234.75` | `2234.69` | `2234.75` | `2238.25` | `2230.25` | 138,036,296.36 USD | 70,500,947.16 USD | 67,535,349.20 USD | 2,965,597.96 USD | `+2.15%` | `1B / 0S` |
| `0:00 UTC` | `2229.75` | `2230.64` | `2229.75` | `2236.75` | `2225.25` | 125,588,915.24 USD | 57,499,740.21 USD | 68,089,175.03 USD | -10,589,434.83 USD | `-8.43%` | `0B / 2S` |
| `5:00 UTC` | `2241.25` | `2240.18` | `2241.25` | `2243.25` | `2233.75` | 123,392,803.54 USD | 67,738,859.18 USD | 55,653,944.36 USD | 12,084,914.83 USD | `+9.79%` | `1B / 2S` |
| `0:00 UTC` | `2245.25` | `2244.67` | `2245.25` | `2246.25` | `2242.75` | 130,536,562.11 USD | 61,753,972.34 USD | 68,782,589.78 USD | -7,028,617.44 USD | `-5.38%` | `0B / 0S` |
| `5:00 UTC` | `2246.25` | `2244.65` | `2246.25` | `2246.75` | `2241.25` | 83,556,134.35 USD | 43,872,052.14 USD | 39,684,082.21 USD | 4,187,969.92 USD | `+5.01%` | `0B / 0S` |
| `0:00 UTC` | `2242.25` | `2242.37` | `2242.25` | `2243.25` | `2241.75` | 8,017,663.14 USD | 3,984,355.76 USD | 4,033,307.38 USD | -48,951.62 USD | `-0.61%` | `1B / 0S` |

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
| `5m` | -21,120.00 USD | 12,730,000.00 USD | **`ACCUMULATION`** |
| `15m` | -2,200,000.00 USD | -1,540,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 432,470.00 USD | -12,390,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -6,070,000.00 USD | 32,210,000.00 USD | **`ACCUMULATION`** |
| `2h` | 5,120,000.00 USD | 94,040,000.00 USD | **`ACCUMULATION`** |
| `4h` | -29,390,000.00 USD | -125,700,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -48,990,000.00 USD | -592,620,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -68,490,000.00 USD | -1,780,000,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -162,770,000.00 USD | -1,960,000,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -131,330,000.00 USD | -1,990,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -158,150,000.00 USD | -3,060,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,160,000,000.00 USD | -9,640,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-21.12K` | 15m=`-2.20M` | 1h=`-6.07M` | 24h=`-131.33M`
* Futures Capital Netflows: 5m=`+12.73M` | 15m=`-1.54M` | 1h=`+32.21M` | 24h=`-1.99B`
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
  * `2026-10-30 09:51:10 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:29:10 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:31:10 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:31:10 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `2183.44` (Risk Distance: `25.13` pts)
  * +2.5R Take Profit: `2271.40`
  * Mathematical Lot Sizing: **`0.39 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2280.60` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2305.73` (Risk Distance: `25.13` pts)
  * +2.5R Take Profit: `2217.77`
  * Mathematical Lot Sizing: **`0.39 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2257.26`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
