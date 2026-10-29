# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 03:07:05 IST` (`2026-10-29 21:37:05 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2281.20` | **Live Ask Quote**: `2284.60` | **Mid Price**: `2282.90`
- **Spread Points**: `340.00` | **Spread BPS**: `14.89 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2317.15` | VWAP Z-Score: `-1.66` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `19.61` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `33.81` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2392.92` | Lower -3.00σ Band: `2241.38`
  * Upper +2.51σ Band: `2380.55` | Lower -2.51σ Band: `2253.75`
  * Upper +2.01σ Band: `2367.92` | Lower -2.01σ Band: `2266.38`
  * Upper +2.00σ Band: `2367.67` | Lower -2.00σ Band: `2266.64`
  * Upper +1.28σ Band: `2349.48` | Lower -1.28σ Band: `2284.82`
  * Upper +1.00σ Band: `2342.41` | Lower -1.00σ Band: `2291.89`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2288.50` | EMA-20=`2307.97` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2320.36` (Slope: `+0.0000`) | EMA-100=`2325.50`
  * Institutional Anchors: EMA-144=`2327.04` | EMA-200=`2327.17` (Slope: `-0.1383`) | EMA-233=`2327.76`
- **Range Boundaries**: 24H High=`2374.90` | 24H Low=`2225.40` | Weekly High=`2387.80` | Weekly Low=`2225.40`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2288.67` (Distance: `-0.25%`)
  * Point of Control (POC) = `2263.20` (Distance: `+0.87%`)
  * Value Area Low (VAL) = `2263.20` (Distance: `+0.87%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2339.52` | POC=`2321.58` | VAL=`2296.66`
  * Prior Day Extremes: PDH=`2374.90` | PDL=`2225.40` | PDC=`2252.70`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2341.79` | Weekly POC=`2310.39` | Weekly VAL=`2299.56`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2289.10` | Low=`2245.70`
  * London Session (08:00-16:00 UTC): High=`2292.03` | Low=`2273.77`
  * New York Session (13:00-21:00 UTC): High=`2296.60` | Low=`2269.20`
  * Initial Balance (First Hour): IB High=`2289.75` | IB Low=`2276.05`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2273.77` - `2292.03`
  * Optimal Trade Entry (OTE 0.705): `2287.47`
  * Structural Invalidation Anchor (0.786): `2301.16`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2249.49` | `2265.66` | `2246.04` | `2265.00` | `74,954` | 169,271,301.10 USD | 14,388,488.70 USD | `+8.50%` | -835,455,431.72 USD | `+0.79` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `2265.01` | `2273.04` | `2258.59` | `2269.57` | `67,412` | 152,593,050.73 USD | 12,791,449.23 USD | `+8.38%` | -822,663,982.48 USD | `+0.74` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `2269.57` | `2270.33` | `2269.55` | `2270.33` | `625` | 1,419,169.06 USD | -155,160.48 USD | `-10.93%` | -822,819,142.96 USD | `+0.48` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `2254.29` | `2277.10` | `2230.20` | `2256.63` | `375,405` | 846,756,637.45 USD | -79,128,177.15 USD | `-9.34%` | -832,067,145.09 USD | `-0.68` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `2256.63` | `2273.04` | `2245.02` | `2269.57` | `268,719` | 606,671,993.02 USD | -5,484,083.31 USD | `-0.90%` | -837,551,228.40 USD | `+0.40` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `2269.57` | `2270.33` | `2269.55` | `2270.33` | `625` | 1,419,169.06 USD | -155,160.48 USD | `-10.93%` | -837,706,388.88 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `2330.22` | `2338.58` | `2325.76` | `2335.68` | `63,571` | 148,285,696.23 USD | -15,505,202.15 USD | `-10.46%` | -370,400,580.93 USD | `+0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `2335.68` | `2335.92` | `2230.20` | `2256.63` | `1,357,980` | 3,094,453,113.46 USD | -457,917,547.62 USD | `-14.80%` | -828,318,128.55 USD | `-3.95` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2256.63` | `2273.04` | `2245.02` | `2270.28` | `269,847` | 609,232,978.91 USD | -6,268,407.56 USD | `-1.03%` | -834,586,536.11 USD | `+0.27` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -163,611,405.07 USD | `+1.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -365,767,522.01 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2270.33` | `1,627,324` | 3,702,544,275.55 USD | -463,556,791.41 USD | `-12.52%` | -829,324,313.42 USD | `-1.83` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2308.03` | `2334.83` | `2303.75` | `2309.10` | `525,175` | 1,216,920,375.04 USD | -34,916,746.14 USD | `-2.87%` | -218,489,329.59 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2309.10` | `2330.05` | `2308.88` | `2324.26` | `409,016` | 949,400,649.22 USD | -49,162,247.72 USD | `-5.18%` | -267,651,577.31 USD | `+0.60` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -163,611,405.07 USD | `+1.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -365,767,522.01 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2270.33` | `1,627,324` | 3,702,544,275.55 USD | -463,556,791.41 USD | `-12.52%` | -829,324,313.42 USD | `-1.83` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`2282.90`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2282.90` | `118.6634` | 270,896.68 USD | 8,820,461.96 USD | `17 orders` | `-0.09%` | `-` |
| `BID` | `2283.00` | `157.4649` | 359,492.37 USD | 8,549,565.28 USD | `18 orders` | `-0.08%` | `-` |
| `BID` | `2283.10` | `87.5137` | 199,802.53 USD | 8,190,072.92 USD | `12 orders` | `-0.08%` | `-` |
| `BID` | `2283.20` | `330.2062` | 753,926.80 USD | 7,990,270.39 USD | `13 orders` | `-0.07%` | `-` |
| `BID` | `2283.30` | `299.7503` | 684,419.86 USD | 7,236,343.59 USD | `12 orders` | `-0.07%` | `-` |
| `BID` | `2283.40` | `143.9661` | 328,732.19 USD | 6,551,923.73 USD | `10 orders` | `-0.06%` | `-` |
| `BID` | `2283.50` | `183.7783` | 419,657.75 USD | 6,223,191.54 USD | `14 orders` | `-0.06%` | `-` |
| `BID` | `2283.60` | `95.6717` | 218,475.89 USD | 5,803,533.79 USD | `13 orders` | `-0.05%` | `-` |
| `BID` | `2283.70` | `507.7428` | 1,159,532.23 USD | 5,585,057.90 USD | `10 orders` | `-0.05%` | `-` |
| `BID` | `2283.80` | `280.4199` | 640,422.97 USD | 4,425,525.67 USD | `11 orders` | `-0.05%` | `-` |
| `BID` | `2283.90` | `251.2825` | 573,904.10 USD | 3,785,102.70 USD | `7 orders` | `-0.04%` | `-` |
| `BID` | `2284.00` | `232.7603` | 531,624.53 USD | 3,211,198.60 USD | `10 orders` | `-0.04%` | `-` |
| `BID` | `2284.10` | `267.7984` | 611,678.33 USD | 2,679,574.07 USD | `11 orders` | `-0.03%` | `-` |
| `BID` | `2284.20` | `82.6714` | 188,838.01 USD | 2,067,895.75 USD | `6 orders` | `-0.03%` | `-` |
| `BID` | `2284.30` | `117.0547` | 267,388.05 USD | 1,879,057.73 USD | `7 orders` | `-0.02%` | `-` |
| `BID` | `2284.40` | `240.2467` | 548,819.56 USD | 1,611,669.68 USD | `7 orders` | `-0.02%` | `-` |
| `BID` | `2284.50` | `45.3255` | 103,546.10 USD | 1,062,850.12 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `2284.60` | `51.1666` | 116,895.21 USD | 959,304.02 USD | `6 orders` | `-0.01%` | `-` |
| `BID` | `2284.70` | `193.4925` | 442,072.31 USD | 842,408.80 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `2284.80` | `175.2173` | 400,336.49 USD | 400,336.49 USD | `17 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2284.85` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,284.85` | `0.00%` | `-` |
| `ASK` | `2284.90` | `5.3852` | 12,304.64 USD | 12,304.64 USD | `6 orders` | `+0.00%` | `-` |
| `ASK` | `2285.00` | `37.8751` | 86,544.60 USD | 98,849.25 USD | `20 orders` | `+0.01%` | `-` |
| `ASK` | `2285.10` | `109.5626` | 250,361.50 USD | 349,210.74 USD | `7 orders` | `+0.01%` | `-` |
| `ASK` | `2285.20` | `71.1792` | 162,658.71 USD | 511,869.45 USD | `13 orders` | `+0.02%` | `-` |
| `ASK` | `2285.30` | `243.1316` | 555,628.65 USD | 1,067,498.10 USD | `13 orders` | `+0.02%` | `-` |
| `ASK` | `2285.40` | `49.3733` | 112,837.74 USD | 1,180,335.84 USD | `9 orders` | `+0.02%` | `-` |
| `ASK` | `2285.50` | `165.0270` | 377,169.21 USD | 1,557,505.05 USD | `11 orders` | `+0.03%` | `-` |
| `ASK` | `2285.60` | `241.0594` | 550,965.36 USD | 2,108,470.41 USD | `19 orders` | `+0.03%` | `-` |
| `ASK` | `2285.70` | `362.0157` | 827,459.29 USD | 2,935,929.70 USD | `10 orders` | `+0.04%` | `-` |
| `ASK` | `2285.80` | `211.4863` | 483,415.38 USD | 3,419,345.08 USD | `8 orders` | `+0.04%` | `-` |
| `ASK` | `2285.90` | `279.0917` | 637,975.72 USD | 4,057,320.80 USD | `10 orders` | `+0.05%` | `-` |
| `ASK` | `2286.00` | `280.3575` | 640,897.24 USD | 4,698,218.04 USD | `11 orders` | `+0.05%` | `-` |
| `ASK` | `2286.10` | `485.6893` | 1,110,334.31 USD | 5,808,552.35 USD | `19 orders` | `+0.05%` | `-` |
| `ASK` | `2286.20` | `447.7659` | 1,023,682.40 USD | 6,832,234.75 USD | `15 orders` | `+0.06%` | `-` |
| `ASK` | `2286.30` | `62.2814` | 142,393.96 USD | 6,974,628.72 USD | `8 orders` | `+0.06%` | `-` |
| `ASK` | `2286.40` | `204.2014` | 466,886.08 USD | 7,441,514.80 USD | `15 orders` | `+0.07%` | `-` |
| `ASK` | `2286.50` | `124.4911` | 284,648.90 USD | 7,726,163.70 USD | `11 orders` | `+0.07%` | `-` |
| `ASK` | `2286.60` | `119.9374` | 274,248.86 USD | 8,000,412.56 USD | `22 orders` | `+0.08%` | `-` |
| `ASK` | `2286.70` | `216.5096` | 495,092.50 USD | 8,495,505.06 USD | `17 orders` | `+0.08%` | `-` |
| `ASK` | `2286.80` | `580.5212` | 1,327,535.88 USD | 9,823,040.94 USD | `17 orders` | `+0.09%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:04:58 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 03:04:58 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1918.00` | `4,184.01` | 8,024,935.59 USD | `TRIGGER_STOP` | `0x6ea486a342` | `2026-10-30 03:04:58 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `8,500.00` | 16,371,850.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-30 03:04:58 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1926.37` | `8,092.45` | 15,589,061.68 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 03:04:58 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2040.74` | `7,964.66` | 16,253,781.36 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-30 03:04:58 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2148.53` | `6,615.35` | 14,213,296.10 USD | `AT_RISK_LIQ` | `0x0c4a3a7ac7` | `2026-10-30 03:04:58 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2171.20` | `48,499.51` | 105,302,149.66 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 03:04:58 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2180.26` | `44,734.81` | 97,533,620.73 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2244.10` | `2,091.26` | 4,692,990.06 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2256.30` | `3,379.38` | 7,624,898.48 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2260.20` | `1,408.90` | 3,184,391.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2262.50` | `653.09` | 1,477,625.18 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2264.20` | `354.04` | 801,627.56 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2264.20` | `339.07` | 767,714.60 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2268.30` | `976.84` | 2,215,768.89 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2270.00` | `471.36` | 1,069,982.66 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2271.00` | `1,743.05` | 3,958,464.73 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2271.40` | `653.24` | 1,483,767.06 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2274.50` | `688.89` | 1,566,870.07 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2275.40` | `1,760.54` | 4,005,921.34 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2276.00` | `653.27` | 1,486,840.24 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2276.10` | `343.23` | 781,235.82 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2277.80` | `1,319.06` | 3,004,556.69 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2278.70` | `889.31` | 2,026,472.98 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2278.70` | `486.13` | 1,107,747.39 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2278.90` | `471.54` | 1,074,583.39 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2280.00` | `878.50` | 2,002,983.65 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2281.50` | `658.44` | 1,502,241.81 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2281.60` | `435.82` | 994,376.04 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2282.90` | `353.42` | 806,824.80 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2283.10` | `438.66` | 1,001,494.37 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2283.90` | `342.08` | 781,270.12 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2289.50` | `328.09` | 751,158.16 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2290.60` | `437.24` | 1,001,535.07 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2291.30` | `353.48` | 809,919.56 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2292.20` | `655.40` | 1,502,301.92 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2292.50` | `435.47` | 998,310.39 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2292.80` | `478.69` | 1,097,539.51 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2292.90` | `343.25` | 787,030.13 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2293.80` | `873.19` | 2,002,926.89 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2294.10` | `890.37` | 2,042,591.62 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2295.70` | `471.30` | 1,081,970.30 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2296.20` | `1,308.49` | 3,004,552.67 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2296.60` | `672.01` | 1,543,348.27 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2297.50` | `653.74` | 1,501,958.46 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2298.40` | `1,742.91` | 4,005,899.75 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2300.20` | `342.14` | 786,995.49 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2301.80` | `1,745.12` | 4,016,916.07 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2303.40` | `653.23` | 1,504,643.07 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2304.00` | `471.52` | 1,086,382.08 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2305.30` | `971.90` | 2,240,532.60 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2309.20` | `654.22` | 1,510,720.21 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2309.70` | `332.39` | 767,714.48 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2310.30` | `346.98` | 801,627.66 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2310.70` | `498.66` | 1,152,248.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x7b7f72a28f` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2310.80` | `3,391.06` | 7,836,056.36 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2314.50` | `1,359.91` | 3,147,521.18 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:04:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2325.70` | `1,990.49` | 4,629,271.66 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:04:58 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2440.00` | `4,002.10` | 9,765,127.17 USD | `TRIGGER_STOP` | `0xfb941d2344` | `2026-10-30 03:04:58 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `3,045.71` | 7,656,616.15 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-30 03:04:58 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2585.96` | `6,224.05` | 16,095,121.81 USD | `AT_RISK_LIQ` | `0x08bf75d170` | `2026-10-30 03:04:58 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2589.92` | `4,845.89` | 12,550,494.06 USD | `AT_RISK_LIQ` | `0xfb1898bb59` | `2026-10-30 03:04:58 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2658.71` | `9,700.00` | 25,789,475.87 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-30 03:04:58 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2709.06` | `8,500.00` | 23,027,017.58 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-30 03:04:58 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 243,749,767.50 USD | `106,417.71` | `2322.74` | `2289.90` | `3908.91` | 3,431,244.65 USD | `+1.41%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 148,150,960.57 USD | `64,680.62` | `2375.30` | `2289.90` | `4527.27` | 5,485,336.93 USD | `+3.70%` | `5X Cross` |
| `6` | `0x77dd...e0e9` | `LONG` | 111,026,537.63 USD | `48,499.51` | `2610.31` | `2289.90` | `2171.18` | -15,572,346.24 USD | `-14.03%` | `10X Cross` |
| `8` | `0x0392...d7d9` | `LONG` | 102,205,628.17 USD | `44,734.81` | `2518.71` | `2289.90` | `2180.25` | -10,468,678.40 USD | `-10.24%` | `9X Cross` |
| `14` | `0xde8d...9524` | `LONG` | 69,186,207.28 USD | `30,282.40` | `2134.45` | `2289.90` | `1787.13` | 4,549,876.70 USD | `+6.58%` | `20X Cross` |
| `21` | `0x7fda...17d1` | `SHORT` | 54,491,774.77 USD | `23,800.73` | `2433.53` | `2289.90` | `3923.45` | 3,428,093.06 USD | `+6.29%` | `25X Cross` |
| `23` | `0xdf95...7d72` | `SHORT` | 51,846,250.15 USD | `22,632.38` | `2402.53` | `2289.90` | `4018.07` | 2,528,818.88 USD | `+4.88%` | `25X Cross` |
| `32` | `0xeced...6210` | `SHORT` | 40,409,036.81 USD | `17,687.58` | `2522.09` | `2289.90` | `3414.72` | 4,200,776.91 USD | `+10.40%` | `20X Cross` |
| `33` | `0xb695...a92d` | `SHORT` | 38,240,716.10 USD | `16,704.62` | `2557.74` | `2289.90` | `4111.31` | 4,485,448.95 USD | `+11.73%` | `20X Cross` |
| `34` | `0x6046...b21d` | `LONG` | 36,389,764.19 USD | `15,927.59` | `2410.19` | `2289.90` | `1656.12` | -1,998,855.46 USD | `-5.49%` | `6X Cross` |
| `38` | `0x45d2...4029` | `SHORT` | 31,930,155.00 USD | `13,950.00` | `2443.60` | `2289.90` | `5120.74` | 2,158,127.46 USD | `+6.76%` | `20X Cross` |
| `43` | `0xbd1c...ff0e` | `LONG` | 27,474,960.00 USD | `12,000.00` | `2419.91` | `2289.90` | `1521.01` | -1,564,072.39 USD | `-5.69%` | `20X Cross` |
| `45` | `0x2371...0883` | `LONG` | 27,412,800.00 USD | `12,000.00` | `2421.77` | `2289.90` | `1280.11` | -1,648,494.85 USD | `-6.01%` | `20X Cross` |
| `50` | `0x09dc...c094` | `LONG` | 25,485,900.00 USD | `11,000.00` | `2465.31` | `2289.90` | `1638.10` | -1,632,523.04 USD | `-6.41%` | `20X Cross` |
| `55` | `0x6c93...59a4` | `LONG` | 25,184,500.00 USD | `11,000.00` | `2441.15` | `2289.90` | `1603.04` | -1,668,172.73 USD | `-6.62%` | `20X Cross` |
| `56` | `0x0c5d...36b3` | `LONG` | 25,183,510.00 USD | `11,000.00` | `2482.20` | `2289.90` | `1645.08` | -2,120,743.24 USD | `-8.42%` | `20X Cross` |
| `57` | `0xa9de...e049` | `LONG` | 25,131,700.00 USD | `11,000.00` | `2481.81` | `2289.90` | `1644.75` | -2,168,279.46 USD | `-8.63%` | `20X Cross` |
| `58` | `0xa61c...66b9` | `LONG` | 24,944,408.00 USD | `10,888.00` | `2398.32` | `2289.90` | `1469.45` | -1,168,549.39 USD | `-4.68%` | `10X Cross` |
| `69` | `0xec7f...df39` | `LONG` | 23,165,000.00 USD | `10,000.00` | `2719.35` | `2289.90` | `1721.62` | -4,028,548.52 USD | `-17.39%` | `20X Cross` |
| `71` | `0xa2ce...3126` | `LONG` | 22,934,437.12 USD | `10,016.88` | `2162.83` | `2289.90` | `1487.14` | 1,269,635.07 USD | `+5.54%` | `10X Cross` |
| `73` | `0x15a4...dfdb` | `LONG` | 22,894,100.00 USD | `10,000.00` | `1761.94` | `2289.90` | `138.02` | 5,274,618.97 USD | `+23.04%` | `20X Cross` |
| `74` | `0x6646...6de5` | `LONG` | 22,865,000.00 USD | `10,000.00` | `1765.80` | `2289.90` | `1726.87` | 5,206,942.55 USD | `+22.77%` | `25X Cross` |
| `76` | `0xaeaa...2416` | `SHORT` | 22,162,560.00 USD | `9,700.00` | `2311.92` | `2289.90` | `2658.69` | 263,122.40 USD | `+1.19%` | `25X Cross` |
| `82` | `0xca49...53c8` | `SHORT` | 21,211,267.62 USD | `9,264.26` | `2549.47` | `2289.90` | `3806.43` | 2,407,757.12 USD | `+11.35%` | `25X Cross` |
| `83` | `0x4487...c92d` | `SHORT` | 21,190,578.52 USD | `9,257.97` | `2362.97` | `2289.90` | `2815.47` | 685,770.93 USD | `+3.24%` | `10X Cross` |
| `84` | `0xba5d...a352` | `SHORT` | 20,970,252.20 USD | `9,054.12` | `2493.89` | `2289.90` | `2940.24` | 1,609,755.06 USD | `+7.68%` | `20X Cross` |
| `86` | `0xea00...a918` | `LONG` | 20,571,041.95 USD | `9,003.83` | `2003.01` | `2289.90` | `1306.75` | 2,536,263.08 USD | `+12.33%` | `5X Cross` |
| `97` | `0xb37f...66ca` | `SHORT` | 19,459,050.00 USD | `8,500.00` | `2308.30` | `2289.90` | `2709.05` | 161,504.19 USD | `+0.83%` | `25X Cross` |
| `110` | `0x9eec...daab` | `LONG` | 18,526,050.59 USD | `8,092.45` | `1658.44` | `2289.90` | `1923.55` | 5,105,186.06 USD | `+27.56%` | `15X Cross` |
| `112` | `0x218a...7da2` | `SHORT` | 18,272,535.73 USD | `7,997.78` | `2208.16` | `2289.90` | `2815.97` | -612,140.52 USD | `-3.35%` | `10X Cross` |
| `114` | `0x5f91...65aa` | `LONG` | 18,196,849.33 USD | `7,964.66` | `1626.99` | `2289.90` | `2040.72` | 5,238,406.27 USD | `+28.79%` | `16X Cross` |
| `116` | `0xecb6...2b00` | `SHORT` | 17,597,275.47 USD | `7,681.72` | `2283.17` | `2289.90` | `5602.24` | -58,610.77 USD | `-0.33%` | `15X Cross` |
| `118` | `0xcf53...ee11` | `SHORT` | 17,359,842.86 USD | `7,603.63` | `1862.69` | `2289.90` | `4006.78` | -3,196,578.92 USD | `-18.41%` | `7X Cross` |
| `123` | `0x939f...04d2` | `LONG` | 16,504,245.33 USD | `7,223.81` | `2500.18` | `2289.90` | `1745.67` | -1,556,644.84 USD | `-9.43%` | `25X Cross` |
| `125` | `0xec0b...b078` | `LONG` | 16,052,064.16 USD | `7,007.80` | `2065.97` | `2289.90` | `1031.31` | 1,574,134.57 USD | `+9.81%` | `25X Cross` |
| `131` | `0x418a...8888` | `SHORT` | 15,352,774.59 USD | `6,724.38` | `2494.55` | `2289.90` | `2993.60` | 1,421,548.58 USD | `+9.26%` | `25X Cross` |
| `135` | `0x4ff9...38d3` | `LONG` | 14,931,486.59 USD | `6,564.10` | `2447.40` | `2289.90` | `1670.70` | -1,133,536.15 USD | `-7.59%` | `3X Isolated` |
| `136` | `0xf78c...c581` | `LONG` | 14,851,056.06 USD | `6,500.22` | `2521.53` | `2289.90` | `1914.18` | -1,539,484.89 USD | `-10.37%` | `20X Cross` |
| `140` | `0x799f...5f4c` | `LONG` | 14,455,755.10 USD | `6,310.90` | `2390.33` | `2289.90` | `1772.21` | -629,409.52 USD | `-4.35%` | `20X Cross` |
| `145` | `0x08bf...7872` | `SHORT` | 14,249,956.52 USD | `6,224.05` | `2258.00` | `2289.90` | `2585.94` | -196,040.42 USD | `-1.38%` | `20X Cross` |
| `151` | `0x0c4a...1b19` | `LONG` | 13,834,373.69 USD | `6,086.13` | `2373.06` | `2289.90` | `2135.33` | -608,376.88 USD | `-4.40%` | `25X Isolated` |
| `152` | `0xd9e7...4aff` | `LONG` | 13,708,200.00 USD | `6,000.00` | `2480.18` | `2289.90` | `1408.47` | -1,172,924.33 USD | `-8.56%` | `20X Cross` |
| `165` | `0x1ee7...edf5` | `LONG` | 12,591,755.00 USD | `5,500.00` | `2316.93` | `2289.90` | `2127.37` | -151,384.62 USD | `-1.20%` | `25X Cross` |
| `166` | `0x0622...8088` | `LONG` | 12,509,684.17 USD | `5,461.55` | `2280.44` | `2289.90` | `404.16` | 54,924.21 USD | `+0.44%` | `5X Cross` |
| `181` | `0x645b...87b8` | `SHORT` | 11,450,260.88 USD | `5,011.47` | `2421.64` | `2289.90` | `6316.27` | 685,748.88 USD | `+5.99%` | `10X Cross` |
| `186` | `0x45ab...6cbc` | `LONG` | 11,242,922.34 USD | `4,920.96` | `2727.66` | `2289.90` | `1377.13` | -2,179,821.46 USD | `-19.39%` | `7X Cross` |
| `188` | `0x64b7...9da9` | `LONG` | 11,127,018.61 USD | `4,856.84` | `2604.61` | `2289.90` | `1508.63` | -1,523,195.81 USD | `-13.69%` | `25X Cross` |
| `192` | `0xfb18...eb17` | `SHORT` | 11,095,055.12 USD | `4,845.89` | `2315.54` | `2289.90` | `2621.65` | 125,827.67 USD | `+1.13%` | `25X Cross` |
| `201` | `0x5559...d43b` | `SHORT` | 10,865,862.53 USD | `4,755.93` | `2262.69` | `2289.90` | `2831.52` | -104,656.66 USD | `-0.96%` | `25X Cross` |
| `204` | `0x12d2...f97f` | `LONG` | 10,758,632.20 USD | `4,708.79` | `2588.61` | `2289.90` | `1952.23` | -1,430,602.12 USD | `-13.30%` | `20X Cross` |
| `215` | `0xe091...6705` | `SHORT` | 10,281,150.46 USD | `4,500.00` | `2467.33` | `2289.90` | `2572.99` | 821,858.05 USD | `+7.99%` | `20X Cross` |
| `231` | `0xc179...e0c8` | `LONG` | 9,872,274.33 USD | `4,309.16` | `2342.89` | `2289.90` | `627.28` | -223,604.46 USD | `-2.26%` | `10X Cross` |
| `235` | `0x28bb...fca6` | `SHORT` | 9,644,226.13 USD | `4,209.61` | `1896.10` | `2289.90` | `3040.47` | -1,662,343.57 USD | `-17.24%` | `20X Cross` |
| `238` | `0x6ea4...0ea7` | `SHORT` | 9,551,681.68 USD | `4,184.01` | `2602.13` | `2289.90` | `3426.00` | 1,335,664.99 USD | `+13.98%` | `20X Cross` |
| `253` | `0x5e9e...35ee` | `SHORT` | 9,175,619.38 USD | `4,007.56` | `1796.39` | `2289.90` | `2586.50` | -1,976,469.29 USD | `-21.54%` | `20X Cross` |
| `255` | `0xfb94...0ddf` | `SHORT` | 9,162,450.74 USD | `4,002.10` | `2382.44` | `2289.90` | `5105.39` | 372,333.41 USD | `+4.06%` | `20X Cross` |
| `257` | `0x3dc9...54b0` | `SHORT` | 9,156,490.77 USD | `3,999.69` | `2480.32` | `2289.90` | `6232.84` | 764,045.78 USD | `+8.34%` | `20X Cross` |
| `258` | `0x8cc9...2b6a` | `SHORT` | 9,154,400.00 USD | `4,000.00` | `1791.18` | `2289.90` | `3778.21` | -1,989,653.33 USD | `-21.73%` | `25X Cross` |
| `269` | `0xf02d...5eb3` | `LONG` | 8,828,278.80 USD | `3,855.99` | `2513.67` | `2289.90` | `304.02` | -864,433.51 USD | `-9.79%` | `20X Cross` |
| `275` | `0x4b67...f4e7` | `LONG` | 8,729,477.49 USD | `3,820.84` | `2591.51` | `2289.90` | `1665.09` | -1,172,296.05 USD | `-13.43%` | `20X Cross` |
| `292` | `0xfe7c...b7ae` | `SHORT` | 8,247,464.40 USD | `3,602.58` | `2440.17` | `2289.90` | `4830.66` | 543,480.59 USD | `+6.59%` | `25X Cross` |
| `296` | `0x8ae4...3d60` | `LONG` | 8,095,612.77 USD | `3,558.20` | `2482.21` | `2289.90` | `473.56` | -736,585.26 USD | `-9.10%` | `10X Cross` |
| `334` | `0x9c2a...f6a8` | `SHORT` | 6,958,538.89 USD | `3,045.71` | `2543.83` | `2289.90` | `2608.03` | 789,247.66 USD | `+11.34%` | `20X Cross` |
| `338` | `0x4a20...3c26` | `LONG` | 6,867,900.00 USD | `3,000.00` | `2428.72` | `2289.90` | `456.85` | -418,260.28 USD | `-6.09%` | `20X Cross` |
| `340` | `0x007d...67a0` | `LONG` | 6,861,600.00 USD | `3,000.00` | `2400.00` | `2289.90` | `1476.20` | -338,400.00 USD | `-4.93%` | `25X Cross` |
| `346` | `0xbc76...417c` | `LONG` | 6,741,092.87 USD | `2,942.94` | `2261.84` | `2289.90` | `2204.78` | 84,627.97 USD | `+1.26%` | `25X Cross` |
| `350` | `0xfc66...ca06` | `SHORT` | 6,707,811.57 USD | `2,951.21` | `2275.19` | `2289.90` | `14471.46` | 6,787.14 USD | `+0.10%` | `20X Cross` |
| `381` | `0xf517...c032` | `SHORT` | 6,272,919.06 USD | `2,738.07` | `2053.90` | `2289.90` | `5621.20` | -649,177.15 USD | `-10.35%` | `25X Cross` |
| `400` | `0x8328...f54a` | `SHORT` | 5,898,552.91 USD | `2,576.45` | `2292.01` | `2289.90` | `3280.24` | 6,718.38 USD | `+0.11%` | `25X Cross` |
| `402` | `0xed48...7c9b` | `SHORT` | 5,840,303.05 USD | `2,551.13` | `2460.02` | `2289.90` | `3248.05` | 435,543.36 USD | `+7.46%` | `20X Cross` |
| `418` | `0xfbe2...c8ea` | `SHORT` | 5,503,653.02 USD | `2,404.08` | `2041.57` | `2289.90` | `2606.67` | -595,560.29 USD | `-10.82%` | `20X Cross` |
| `425` | `0x1c98...7fc7` | `LONG` | 5,391,813.09 USD | `2,358.00` | `2467.15` | `2289.90` | `1897.22` | -425,758.39 USD | `-7.90%` | `10X Cross` |
| `432` | `0x77ee...2902` | `SHORT` | 5,236,978.22 USD | `2,290.69` | `2476.53` | `2289.90` | `5840.11` | 435,994.01 USD | `+8.33%` | `25X Cross` |
| `442` | `0x023a...2355` | `LONG` | 5,114,320.26 USD | `2,232.35` | `2330.15` | `2289.90` | `0.000000` | -87,408.47 USD | `-1.71%` | `25X Cross` |
| `443` | `0x6859...7e1e` | `SHORT` | 5,095,620.66 USD | `2,224.58` | `2200.39` | `2289.90` | `3845.41` | -200,667.93 USD | `-3.94%` | `25X Cross` |
| `452` | `0xd507...c948` | `SHORT` | 4,975,182.97 USD | `2,172.00` | `2387.49` | `2289.90` | `2707.42` | 210,458.05 USD | `+4.23%` | `5X Isolated` |
| `462` | `0x382b...3e39` | `SHORT` | 4,877,927.99 USD | `2,129.54` | `2296.66` | `2289.90` | `4702.97` | 12,909.23 USD | `+0.26%` | `25X Cross` |
| `464` | `0xb829...3a81` | `LONG` | 4,862,454.08 USD | `2,153.91` | `2537.61` | `2289.90` | `708.30` | -603,342.65 USD | `-12.41%` | `20X Cross` |
| `493` | `0x3440...32c5` | `SHORT` | 4,582,494.65 USD | `2,000.57` | `2198.21` | `2289.90` | `3588.16` | -184,831.52 USD | `-4.03%` | `25X Cross` |
| `494` | `0xbb34...1696` | `LONG` | 4,578,820.00 USD | `2,000.00` | `2318.80` | `2289.90` | `1903.03` | -58,796.04 USD | `-1.28%` | `25X Cross` |
| `495` | `0xf929...d1f9` | `SHORT` | 4,578,820.00 USD | `2,000.00` | `2423.37` | `2289.90` | `2548.82` | 267,920.34 USD | `+5.85%` | `25X Cross` |
| `496` | `0x7a6d...f79c` | `SHORT` | 4,578,600.00 USD | `2,000.00` | `2418.41` | `2289.90` | `2649.56` | 258,232.11 USD | `+5.64%` | `25X Cross` |
| `498` | `0xc619...10f5` | `LONG` | 4,569,600.00 USD | `2,000.00` | `2318.40` | `2289.90` | `1755.69` | -67,206.86 USD | `-1.47%` | `25X Cross` |
| `510` | `0x0514...bdfe` | `SHORT` | 4,452,045.00 USD | `1,950.00` | `1988.74` | `2289.90` | `3015.22` | -573,985.37 USD | `-12.89%` | `25X Cross` |
| `516` | `0x8376...9a1e` | `SHORT` | 4,364,910.21 USD | `1,910.50` | `2477.72` | `2289.90` | `3173.62` | 368,777.96 USD | `+8.45%` | `20X Cross` |
| `524` | `0xfc27...9d9d` | `SHORT` | 4,273,683.16 USD | `1,867.36` | `2341.25` | `2289.90` | `11019.61` | 98,290.58 USD | `+2.30%` | `25X Cross` |
| `548` | `0x541e...071d` | `SHORT` | 4,132,186.50 USD | `1,805.00` | `2648.19` | `2289.90` | `3106.48` | 647,798.34 USD | `+15.68%` | `25X Cross` |
| `549` | `0x7265...91a5` | `LONG` | 4,125,217.82 USD | `1,801.87` | `2533.96` | `2289.90` | `1988.15` | -440,648.63 USD | `-10.68%` | `20X Cross` |
| `550` | `0x739c...cfb2` | `SHORT` | 4,117,860.00 USD | `1,800.00` | `2427.60` | `2289.90` | `2562.65` | 251,836.38 USD | `+6.12%` | `25X Cross` |
| `551` | `0xb15b...dbae` | `SHORT` | 4,114,880.36 USD | `1,797.68` | `2294.54` | `2289.90` | `2302.42` | 9,963.61 USD | `+0.24%` | `25X Cross` |
| `556` | `0xa445...329d` | `LONG` | 4,067,512.17 USD | `1,776.75` | `2398.85` | `2289.90` | `1876.81` | -194,657.18 USD | `-4.79%` | `25X Cross` |
| `559` | `0x91a9...3f70` | `SHORT` | 4,037,631.31 USD | `1,767.48` | `2156.23` | `2289.90` | `3628.23` | -226,527.23 USD | `-5.61%` | `4X Cross` |
| `563` | `0x2828...93a0` | `LONG` | 4,026,277.84 USD | `1,758.58` | `2314.00` | `2289.90` | `2241.75` | -43,089.02 USD | `-1.07%` | `25X Cross` |
| `569` | `0x3453...b323` | `SHORT` | 3,998,506.25 USD | `1,750.12` | `2328.82` | `2289.90` | `2427.63` | 77,225.89 USD | `+1.93%` | `25X Cross` |
| `587` | `0x39b4...5c34` | `SHORT` | 3,922,369.41 USD | `1,713.35` | `2329.97` | `2289.90` | `2446.11` | 69,687.60 USD | `+1.78%` | `25X Cross` |
| `595` | `0xfeec...4e9c` | `SHORT` | 3,875,257.24 USD | `1,691.81` | `2566.49` | `2289.90` | `2653.55` | 466,767.28 USD | `+12.04%` | `10X Cross` |
| `596` | `0x936c...bb0f` | `SHORT` | 3,867,935.28 USD | `1,688.69` | `2434.60` | `2289.90` | `6200.31` | 243,351.82 USD | `+6.29%` | `20X Cross` |
| `600` | `0x7b7f...dee2` | `LONG` | 3,843,456.74 USD | `1,677.63` | `2280.56` | `2289.90` | `875.53` | 17,498.14 USD | `+0.46%` | `20X Cross` |
| `614` | `0xeee0...0b53` | `LONG` | 3,740,336.97 USD | `1,637.12` | `2468.64` | `2289.90` | `171.60` | -301,139.09 USD | `-8.05%` | `7X Cross` |
| `621` | `0x27b8...12fc` | `LONG` | 3,716,835.38 USD | `1,628.12` | `2468.73` | `2289.90` | `553.59` | -302,559.26 USD | `-8.14%` | `10X Cross` |
| `622` | `0x982b...4606` | `LONG` | 3,716,789.49 USD | `1,626.82` | `2575.24` | `2289.90` | `1548.43` | -472,663.59 USD | `-12.72%` | `5X Isolated` |
| `634` | `0x73d7...8be1` | `LONG` | 3,661,270.43 USD | `1,601.47` | `2410.40` | `2289.90` | `2015.21` | -198,908.49 USD | `-5.43%` | `25X Cross` |
| `649` | `0xd7b8...9f55` | `LONG` | 3,559,468.44 USD | `1,554.75` | `2280.55` | `2289.90` | `821.00` | 13,761.96 USD | `+0.39%` | `15X Cross` |
| `659` | `0xe170...9300` | `SHORT` | 3,509,783.93 USD | `1,533.40` | `2076.39` | `2289.90` | `3125.41` | -325,834.43 USD | `-9.28%` | `25X Cross` |
| `672` | `0xad54...6203` | `LONG` | 3,457,672.57 USD | `1,510.29` | `2614.66` | `2289.90` | `2124.65` | -491,233.98 USD | `-14.21%` | `10X Isolated` |
| `675` | `0x2e2b...2fab` | `LONG` | 3,443,452.02 USD | `1,507.38` | `2245.53` | `2289.90` | `1167.15` | 58,578.92 USD | `+1.70%` | `25X Cross` |
| `677` | `0x251f...6e5d` | `LONG` | 3,436,500.00 USD | `1,500.00` | `2346.68` | `2289.90` | `1779.06` | -83,530.49 USD | `-2.43%` | `20X Cross` |
| `695` | `0xef70...a84c` | `SHORT` | 3,305,325.13 USD | `1,442.74` | `2424.73` | `2289.90` | `3347.51` | 192,945.70 USD | `+5.84%` | `25X Cross` |
| `706` | `0x4b5f...0dd8` | `LONG` | 3,271,162.11 USD | `1,431.96` | `2339.45` | `2289.90` | `2148.71` | -78,830.83 USD | `-2.41%` | `10X Cross` |
| `707` | `0xbadb...9ee6` | `LONG` | 3,269,643.79 USD | `1,428.16` | `1936.00` | `2289.90` | `1032.31` | 504,722.14 USD | `+15.44%` | `20X Cross` |
| `737` | `0xa0fb...96be` | `LONG` | 3,141,849.34 USD | `1,376.25` | `2293.96` | `2289.90` | `1549.95` | -15,225.54 USD | `-0.48%` | `3X Cross` |
| `751` | `0xd4c1...3d1d` | `SHORT` | 3,093,202.98 USD | `1,350.45` | `2334.28` | `2289.90` | `5766.28` | 59,124.04 USD | `+1.91%` | `12X Cross` |
| `770` | `0x880a...311c` | `SHORT` | 3,024,103.03 USD | `1,320.22` | `2425.76` | `2289.90` | `8108.38` | 178,446.12 USD | `+5.90%` | `9X Cross` |
| `774` | `0x0dd5...f6ee` | `LONG` | 3,010,574.15 USD | `1,315.00` | `2306.05` | `2289.90` | `1654.24` | -21,890.23 USD | `-0.73%` | `5X Cross` |
| `811` | `0xc435...c905` | `SHORT` | 2,857,071.36 USD | `1,248.00` | `2704.38` | `2289.90` | `5065.73` | 517,998.99 USD | `+18.13%` | `20X Cross` |
| `831` | `0x7178...0854` | `LONG` | 2,784,329.25 USD | `1,218.63` | `2461.81` | `2289.90` | `1134.21` | -215,717.15 USD | `-7.75%` | `10X Cross` |
| `862` | `0x2577...4897` | `LONG` | 2,678,965.59 USD | `1,169.60` | `2315.75` | `2289.90` | `0.000000` | -29,533.85 USD | `-1.10%` | `15X Cross` |
| `865` | `0x07fd...689d` | `LONG` | 2,671,271.72 USD | `1,166.49` | `2419.97` | `2289.90` | `0.000000` | -151,620.09 USD | `-5.68%` | `25X Cross` |
| `905` | `0xbef3...0d3e` | `LONG` | 2,527,492.61 USD | `1,103.99` | `2315.08` | `2289.90` | `2162.38` | -28,343.55 USD | `-1.12%` | `20X Cross` |
| `913` | `0x6a41...a3b9` | `LONG` | 2,511,130.92 USD | `1,099.06` | `2314.77` | `2289.90` | `2164.22` | -32,941.78 USD | `-1.31%` | `20X Cross` |
| `924` | `0x2f80...f203` | `SHORT` | 2,490,299.40 USD | `1,088.94` | `1984.00` | `2289.90` | `3065.56` | -329,832.21 USD | `-13.24%` | `20X Cross` |
| `931` | `0x6f11...0389` | `SHORT` | 2,470,154.70 USD | `1,079.00` | `2333.39` | `2289.90` | `3199.69` | 47,574.21 USD | `+1.93%` | `25X Cross` |
| `934` | `0x2b61...2f6c` | `SHORT` | 2,461,316.52 USD | `1,076.60` | `2681.75` | `2289.90` | `6321.93` | 425,856.22 USD | `+17.30%` | `10X Cross` |
| `976` | `0x1b2a...f7a6` | `LONG` | 2,342,658.27 USD | `1,025.37` | `2737.51` | `2289.90` | `883.09` | -464,301.67 USD | `-19.82%` | `10X Cross` |
| `990` | `0x02aa...1806` | `SHORT` | 2,307,266.33 USD | `1,007.10` | `2654.68` | `2289.90` | `3613.69` | 366,265.77 USD | `+15.87%` | `20X Cross` |
| `992` | `0x001a...fef6` | `SHORT` | 2,306,270.59 USD | `1,007.33` | `2022.19` | `2289.90` | `3058.75` | -269,262.63 USD | `-11.68%` | `10X Cross` |
| `997` | `0xdb3a...cf3b` | `LONG` | 2,298,365.79 USD | `1,003.22` | `2705.01` | `2289.90` | `0.000000` | -415,341.10 USD | `-18.07%` | `4X Cross` |
| `1000` | `0x5272...fcd9` | `SHORT` | 2,289,500.00 USD | `1,000.00` | `2241.82` | `2289.90` | `2880.76` | -47,675.51 USD | `-2.08%` | `5X Cross` |
| `1001` | `0x834c...dd93` | `SHORT` | 2,289,410.00 USD | `1,000.00` | `2249.68` | `2289.90` | `2310.91` | -39,724.58 USD | `-1.74%` | `25X Cross` |
| `1026` | `0xb002...ed8a` | `SHORT` | 2,204,207.32 USD | `962.78` | `2299.66` | `2289.90` | `4199.24` | 9,870.59 USD | `+0.45%` | `25X Cross` |
| `1050` | `0xc8fe...afa4` | `LONG` | 2,144,291.42 USD | `936.37` | `2331.34` | `2289.90` | `2145.82` | -38,712.81 USD | `-1.81%` | `10X Isolated` |
| `1075` | `0x9606...4e5d` | `SHORT` | 2,089,749.02 USD | `913.00` | `2478.70` | `2289.90` | `4165.53` | 173,304.59 USD | `+8.29%` | `20X Cross` |
| `1086` | `0x5238...54e5` | `SHORT` | 2,061,900.00 USD | `900.00` | `2289.53` | `2289.90` | `4617.95` | -1,317.58 USD | `-0.06%` | `25X Cross` |
| `1088` | `0x5f10...d49d` | `LONG` | 2,060,550.00 USD | `900.00` | `2249.83` | `2289.90` | `1790.46` | 35,696.53 USD | `+1.73%` | `25X Cross` |
| `1107` | `0x2e30...4cb5` | `SHORT` | 2,025,941.96 USD | `884.85` | `2340.07` | `2289.90` | `7722.58` | 44,676.86 USD | `+2.21%` | `2X Cross` |
| `1127` | `0x696d...8e28` | `SHORT` | 2,000,480.64 USD | `874.45` | `2287.00` | `2289.90` | `4008.27` | -609.09 USD | `-0.03%` | `20X Cross` |
| `1193` | `0xcd27...52a8` | `LONG` | 1,912,853.52 USD | `837.21` | `2553.56` | `2289.90` | `1404.24` | -225,011.25 USD | `-11.76%` | `2X Cross` |
| `1221` | `0xf83f...625f` | `SHORT` | 1,874,612.35 USD | `818.25` | `2595.19` | `2289.90` | `6008.24` | 248,904.69 USD | `+13.28%` | `20X Cross` |
| `1227` | `0x6ff1...8575` | `LONG` | 1,862,397.09 USD | `814.06` | `2272.53` | `2289.90` | `2227.12` | 12,427.33 USD | `+0.67%` | `25X Isolated` |
| `1239` | `0x3fc5...c0c1` | `SHORT` | 1,842,233.83 USD | `804.26` | `2702.11` | `2289.90` | `4721.57` | 330,967.70 USD | `+17.97%` | `25X Cross` |
| `1247` | `0x04a9...95aa` | `LONG` | 1,831,440.00 USD | `800.00` | `2595.13` | `2289.90` | `1884.99` | -244,666.74 USD | `-13.36%` | `5X Cross` |
| `1251` | `0x7737...bf66` | `SHORT` | 1,827,372.53 USD | `799.79` | `2494.83` | `2289.90` | `24131.79` | 167,973.50 USD | `+9.19%` | `15X Cross` |
| `1292` | `0x458d...ab3b` | `LONG` | 1,770,064.47 USD | `774.75` | `2740.41` | `2289.90` | `1887.99` | -353,064.71 USD | `-19.95%` | `3X Isolated` |
| `1317` | `0xe668...b5ca` | `LONG` | 1,715,775.00 USD | `750.00` | `2286.78` | `2289.90` | `2129.68` | 685.14 USD | `+0.04%` | `25X Cross` |
| `1349` | `0xaa53...9cb7` | `LONG` | 1,672,105.87 USD | `730.34` | `2389.70` | `2289.90` | `1985.68` | -73,183.76 USD | `-4.38%` | `20X Cross` |
| `1357` | `0xab81...c608` | `SHORT` | 1,664,943.79 USD | `727.27` | `2285.37` | `2289.90` | `5195.26` | -2,856.70 USD | `-0.17%` | `20X Cross` |
| `1358` | `0x621c...63ab` | `LONG` | 1,663,902.46 USD | `728.28` | `2281.90` | `2289.90` | `0.000000` | 2,032.16 USD | `+0.12%` | `20X Cross` |
| `1365` | `0x51a0...3543` | `SHORT` | 1,657,036.24 USD | `724.55` | `2627.71` | `2289.90` | `7463.51` | 246,860.51 USD | `+14.90%` | `20X Cross` |
| `1376` | `0xa189...94d7` | `SHORT` | 1,648,197.53 USD | `719.98` | `2691.84` | `2289.90` | `3051.94` | 289,875.14 USD | `+17.59%` | `25X Cross` |
| `1386` | `0x4b1c...bc38` | `SHORT` | 1,636,633.35 USD | `714.38` | `2528.62` | `2289.90` | `4256.86` | 169,750.55 USD | `+10.37%` | `10X Cross` |
| `1397` | `0x2f93...4404` | `LONG` | 1,612,822.78 USD | `707.47` | `1700.45` | `2289.90` | `1369.62` | 409,796.40 USD | `+25.41%` | `4X Isolated` |
| `1411` | `0x5605...fe0f` | `SHORT` | 1,602,923.62 USD | `702.14` | `2566.90` | `2289.90` | `3032.78` | 199,409.02 USD | `+12.44%` | `20X Cross` |
| `1412` | `0x0deb...0bc5` | `LONG` | 1,602,650.00 USD | `700.00` | `2071.05` | `2289.90` | `1598.21` | 152,914.21 USD | `+9.54%` | `20X Cross` |
| `1438` | `0x8b61...c0c2` | `LONG` | 1,575,727.71 USD | `688.30` | `2262.24` | `2289.90` | `2163.93` | 18,621.27 USD | `+1.18%` | `16X Isolated` |
| `1458` | `0xdbd1...29dd` | `SHORT` | 1,554,193.56 USD | `680.70` | `3030.57` | `2289.90` | `4064.58` | 508,727.56 USD | `+32.73%` | `6X Cross` |
| `1459` | `0x71e5...be04` | `LONG` | 1,551,518.14 USD | `677.67` | `2727.27` | `2289.90` | `1471.77` | -296,667.47 USD | `-19.12%` | `20X Cross` |
| `1468` | `0x0b23...f37b` | `LONG` | 1,543,185.00 USD | `675.00` | `2238.15` | `2289.90` | `591.89` | 32,428.36 USD | `+2.10%` | `5X Cross` |
| `1483` | `0x1f16...6d07` | `LONG` | 1,524,687.12 USD | `666.00` | `2287.38` | `2289.90` | `1326.71` | 1,287.83 USD | `+0.08%` | `7X Cross` |
| `1495` | `0x0cac...6170` | `SHORT` | 1,505,398.85 USD | `657.50` | `2146.55` | `2289.90` | `2840.19` | -94,036.65 USD | `-6.25%` | `20X Cross` |
| `1527` | `0xf00e...fe3d` | `SHORT` | 1,472,580.93 USD | `642.88` | `2333.21` | `2289.90` | `2517.65` | 27,397.04 USD | `+1.86%` | `20X Cross` |
| `1537` | `0xffb2...5ed6` | `SHORT` | 1,464,023.98 USD | `640.77` | `2672.96` | `2289.90` | `2509.95` | 248,724.36 USD | `+16.99%` | `20X Cross` |
| `1541` | `0xa522...2d0e` | `SHORT` | 1,455,107.64 USD | `636.36` | `2284.42` | `2289.90` | `4327.95` | -1,381.80 USD | `-0.09%` | `20X Cross` |
| `1566` | `0xfce0...f4c0` | `SHORT` | 1,424,738.92 USD | `623.60` | `3129.61` | `2289.90` | `2788.43` | 526,887.67 USD | `+36.98%` | `20X Cross` |
| `1585` | `0x7663...cb5a` | `SHORT` | 1,404,743.88 USD | `613.54` | `2342.35` | `2289.90` | `3739.53` | 32,376.61 USD | `+2.30%` | `3X Cross` |
| `1602` | `0x0999...c74b` | `LONG` | 1,382,541.96 USD | `605.10` | `2267.85` | `2289.90` | `2128.28` | 10,257.40 USD | `+0.74%` | `20X Cross` |
| `1608` | `0xad02...eb65` | `LONG` | 1,376,020.88 USD | `600.62` | `2460.69` | `2289.90` | `1079.69` | -101,919.68 USD | `-7.41%` | `5X Cross` |
| `1609` | `0x638f...f5f0` | `LONG` | 1,373,748.00 USD | `600.00` | `4011.50` | `2289.90` | `223.70` | -1,033,155.53 USD | `-75.21%` | `25X Cross` |
| `1612` | `0x26e6...6b28` | `LONG` | 1,372,620.00 USD | `600.00` | `1769.78` | `2289.90` | `2005.49` | 310,748.47 USD | `+22.64%` | `20X Cross` |
| `1614` | `0x67c3...609d` | `SHORT` | 1,369,740.00 USD | `600.00` | `2386.55` | `2289.90` | `2560.78` | 62,191.89 USD | `+4.54%` | `25X Cross` |
| `1650` | `0xca8e...507d` | `LONG` | 1,328,780.00 USD | `580.00` | `2253.46` | `2289.90` | `2069.74` | 21,769.65 USD | `+1.64%` | `10X Isolated` |
| `1677` | `0xfb99...37f3` | `LONG` | 1,294,297.57 USD | `565.34` | `2362.35` | `2289.90` | `1226.52` | -41,238.79 USD | `-3.19%` | `3X Cross` |
| `1688` | `0x844b...7f42` | `SHORT` | 1,281,772.80 USD | `561.00` | `2026.17` | `2289.90` | `3122.49` | -145,089.39 USD | `-11.32%` | `25X Cross` |
| `1694` | `0xabe6...1d99` | `SHORT` | 1,273,582.76 USD | `556.00` | `2484.68` | `2289.90` | `3073.12` | 107,913.13 USD | `+8.47%` | `20X Cross` |
| `1750` | `0xad21...fb6a` | `LONG` | 1,217,619.03 USD | `531.87` | `2574.89` | `2289.90` | `1697.96` | -151,886.47 USD | `-12.47%` | `7X Cross` |
| `1756` | `0x0082...1ae3` | `LONG` | 1,206,321.60 USD | `528.00` | `2448.58` | `2289.90` | `2234.25` | -86,533.31 USD | `-7.17%` | `25X Cross` |
| `1790` | `0x05b5...be75` | `LONG` | 1,175,102.39 USD | `513.39` | `2275.37` | `2289.90` | `1884.65` | 6,936.37 USD | `+0.59%` | `20X Cross` |
| `1800` | `0x0c7a...2f50` | `SHORT` | 1,165,825.45 USD | `509.25` | `2122.56` | `2289.90` | `4094.78` | -84,920.02 USD | `-7.28%` | `20X Cross` |
| `1821` | `0x7743...e4fe` | `SHORT` | 1,146,774.25 USD | `500.56` | `2326.87` | `2289.90` | `7720.54` | 17,959.91 USD | `+1.57%` | `25X Cross` |
| `1824` | `0x89b2...9ca6` | `LONG` | 1,144,650.00 USD | `500.00` | `2484.03` | `2289.90` | `1954.22` | -97,369.35 USD | `-8.51%` | `25X Cross` |
| `1829` | `0xa559...ff95` | `LONG` | 1,142,350.00 USD | `500.00` | `2260.68` | `2289.90` | `1137.00` | 12,005.64 USD | `+1.05%` | `20X Cross` |
| `1831` | `0x7298...7d6c` | `SHORT` | 1,140,467.99 USD | `498.15` | `3426.75` | `2289.90` | `5422.40` | 566,567.83 USD | `+49.68%` | `20X Cross` |
| `1842` | `0x536c...3e1f` | `LONG` | 1,133,655.30 USD | `494.83` | `2275.87` | `2289.90` | `2126.47` | 7,482.98 USD | `+0.66%` | `20X Cross` |
| `1845` | `0x9599...c60a` | `SHORT` | 1,130,714.61 USD | `493.91` | `2271.18` | `2289.90` | `10430.83` | -8,959.26 USD | `-0.79%` | `20X Cross` |
| `1849` | `0x9c68...7783` | `SHORT` | 1,129,295.01 USD | `493.31` | `2273.58` | `2289.90` | `3785.30` | -7,715.77 USD | `-0.68%` | `25X Cross` |
| `1855` | `0x404c...5f03` | `SHORT` | 1,122,098.12 USD | `489.79` | `2671.94` | `2289.90` | `4719.71` | 186,581.43 USD | `+16.63%` | `20X Cross` |
| `1859` | `0xc10f...23b3` | `LONG` | 1,117,543.00 USD | `490.00` | `2383.92` | `2289.90` | `2113.38` | -50,578.28 USD | `-4.53%` | `25X Cross` |
| `1863` | `0x321f...1c84` | `SHORT` | 1,115,017.59 USD | `488.02` | `2370.09` | `2289.90` | `3030.94` | 41,627.01 USD | `+3.73%` | `10X Cross` |
| `1925` | `0x82c6...fe42` | `LONG` | 1,058,801.25 USD | `462.50` | `2501.38` | `2289.90` | `2054.47` | -98,089.32 USD | `-9.26%` | `5X Isolated` |
| `1933` | `0x2de3...486d` | `LONG` | 1,054,085.80 USD | `460.40` | `2286.27` | `2289.90` | `1313.59` | 1,484.89 USD | `+0.14%` | `25X Cross` |
| `1944` | `0x617e...0f97` | `SHORT` | 1,048,257.65 USD | `457.85` | `2205.60` | `2289.90` | `3703.26` | -38,413.81 USD | `-3.66%` | `10X Cross` |
| `1965` | `0xae55...2236` | `LONG` | 1,030,005.00 USD | `450.00` | `2510.21` | `2289.90` | `0.000000` | -99,592.50 USD | `-9.67%` | `25X Cross` |
| `1984` | `0xac26...a9c7` | `SHORT` | 1,021,750.96 USD | `446.28` | `2192.58` | `2289.90` | `8715.23` | -43,251.26 USD | `-4.23%` | `20X Cross` |
| `1986` | `0x53f8...ceff` | `LONG` | 1,019,393.40 USD | `445.60` | `2399.81` | `2289.90` | `0.000000` | -49,957.20 USD | `-4.90%` | `20X Cross` |
| `1991` | `0xd6e1...f256` | `SHORT` | 1,015,640.93 USD | `443.66` | `2259.33` | `2289.90` | `3595.99` | -13,261.71 USD | `-1.31%` | `25X Cross` |
| `1996` | `0x051c...693c` | `LONG` | 1,012,801.10 USD | `442.39` | `2259.27` | `2289.90` | `0.000000` | 13,332.66 USD | `+1.32%` | `8X Cross` |
| `2003` | `0xd8a1...6687` | `LONG` | 1,010,801.50 USD | `441.53` | `2804.24` | `2289.90` | `2151.03` | -227,366.94 USD | `-22.49%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `2686.20` | 3,246.54 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 3.25K USD at 2686.2000 USD [API] | `2026-09-29 15:21:02` |
| `ANNOUNCEMENT` | `INFO` | `2686.20` | 44.05 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.04K USD at 2686.2000 USD [API] | `2026-09-29 15:21:02` |
| `ANNOUNCEMENT` | `INFO` | `2686.20` | 585.32 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.59K USD at 2686.2000 USD [API] | `2026-09-29 15:21:02` |
| `ANNOUNCEMENT` | `INFO` | `2686.30` | 18.80 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.02K USD at 2686.3000 USD [API] | `2026-09-29 15:21:02` |
| `ANNOUNCEMENT` | `INFO` | `2686.30` | 9,539.05 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 9.54K USD at 2686.3000 USD [API] | `2026-09-29 15:21:02` |
| `ANNOUNCEMENT` | `INFO` | `2686.30` | 15,905.58 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 15.91K USD at 2686.3000 USD [API] | `2026-09-29 15:21:02` |
| `ANNOUNCEMENT` | `INFO` | `2686.30` | 24.98 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.02K USD at 2686.3000 USD [API] | `2026-09-29 15:21:02` |
| `ANNOUNCEMENT` | `INFO` | `2686.40` | 18.80 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.02K USD at 2686.4000 USD [API] | `2026-09-29 15:21:02` |
| `ANNOUNCEMENT` | `INFO` | `2686.40` | 2,109.36 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 2.11K USD at 2686.4000 USD [API] | `2026-09-29 15:21:02` |
| `ANNOUNCEMENT` | `INFO` | `2686.40` | 406.45 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.41K USD at 2686.4000 USD [API] | `2026-09-29 15:21:02` |
| `ANNOUNCEMENT` | `INFO` | `2686.40` | 8,100.03 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 8.10K USD at 2686.4000 USD [API] | `2026-09-29 15:21:02` |
| `ANNOUNCEMENT` | `INFO` | `2686.50` | 18.81 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.02K USD at 2686.5000 USD [API] | `2026-09-29 15:21:02` |
| `ANNOUNCEMENT` | `INFO` | `2686.50` | 49.97 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.05K USD at 2686.5000 USD [API] | `2026-09-29 15:21:02` |
| `ANNOUNCEMENT` | `INFO` | `2686.60` | 24.99 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.02K USD at 2686.6000 USD [API] | `2026-09-29 15:21:02` |
| `ANNOUNCEMENT` | `INFO` | `2686.60` | 18.81 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.02K USD at 2686.6000 USD [API] | `2026-09-29 15:21:02` |
| `ANNOUNCEMENT` | `INFO` | `2686.60` | 148.57 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.15K USD at 2686.6000 USD [API] | `2026-09-29 15:21:02` |
| `ANNOUNCEMENT` | `INFO` | `2686.70` | 18.81 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.02K USD at 2686.7000 USD [API] | `2026-09-29 15:21:02` |
| `ANNOUNCEMENT` | `INFO` | `2686.70` | 136.22 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.14K USD at 2686.7000 USD [API] | `2026-09-29 15:21:02` |
| `ANNOUNCEMENT` | `INFO` | `2686.70` | 2,411.58 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 2.41K USD at 2686.7000 USD [API] | `2026-09-29 15:21:02` |
| `ANNOUNCEMENT` | `INFO` | `2686.80` | 18.81 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.02K USD at 2686.8000 USD [API] | `2026-09-29 15:21:02` |
| `ANNOUNCEMENT` | `INFO` | `2686.90` | 1,644.11 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.64K USD at 2686.9000 USD [API] | `2026-09-29 15:21:02` |
| `ANNOUNCEMENT` | `INFO` | `2686.90` | 18.81 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.02K USD at 2686.9000 USD [API] | `2026-09-29 15:21:02` |
| `ANNOUNCEMENT` | `INFO` | `2686.90` | 39,868.22 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 39.87K USD at 2686.9000 USD [API] | `2026-09-29 15:21:02` |
| `ANNOUNCEMENT` | `INFO` | `2686.90` | 11,013.60 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 11.01K USD at 2686.9000 USD [API] | `2026-09-29 15:20:13` |
| `ANNOUNCEMENT` | `INFO` | `2686.90` | 6,052.24 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 6.05K USD at 2686.9000 USD [API] | `2026-09-29 15:20:13` |
| `ANNOUNCEMENT` | `INFO` | `2686.90` | 4,030.35 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 4.03K USD at 2686.9000 USD [API] | `2026-09-29 15:20:13` |
| `ANNOUNCEMENT` | `INFO` | `2340.60` | 54,933.88 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 54.93K USD at 2340.6000 USD [API] | `2026-10-28 12:42:51` |
| `ANNOUNCEMENT` | `INFO` | `2340.60` | 55,554.84 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 55.55K USD at 2340.6000 USD [API] | `2026-10-28 12:42:51` |
| `ANNOUNCEMENT` | `INFO` | `2483.90` | 15,687.57 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 15.69K USD at 2483.9000 USD [API] | `2026-09-03 14:49:05` |
| `ANNOUNCEMENT` | `INFO` | `2228.60` | 21,865.46 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 21.87K USD at 2228.6000 USD [API] | `2026-08-19 20:51:18` |
| `ANNOUNCEMENT` | `INFO` | `2228.40` | 149,203.41 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 149.20K USD at 2228.4000 USD [API] | `2026-08-19 20:51:18` |
| `ANNOUNCEMENT` | `INFO` | `2228.40` | 61,153.54 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 61.15K USD at 2228.4000 USD [API] | `2026-08-19 20:51:18` |
| `ANNOUNCEMENT` | `INFO` | `2228.30` | 4,611.47 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 4.61K USD at 2228.3000 USD [API] | `2026-08-19 20:51:18` |
| `ANNOUNCEMENT` | `INFO` | `2228.30` | 222.61 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.22K USD at 2228.3000 USD [API] | `2026-08-19 20:51:18` |
| `ANNOUNCEMENT` | `INFO` | `2228.30` | 22.51 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2228.3000 USD [API] | `2026-08-19 20:51:18` |
| `ANNOUNCEMENT` | `INFO` | `2228.30` | 22.51 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2228.3000 USD [API] | `2026-08-19 20:51:18` |
| `ANNOUNCEMENT` | `INFO` | `2228.30` | 22.51 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2228.3000 USD [API] | `2026-08-19 20:51:18` |
| `ANNOUNCEMENT` | `INFO` | `2228.30` | 22.51 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2228.3000 USD [API] | `2026-08-19 20:51:18` |
| `ANNOUNCEMENT` | `INFO` | `2228.30` | 22.51 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2228.3000 USD [API] | `2026-08-19 20:51:18` |
| `ANNOUNCEMENT` | `INFO` | `2228.30` | 44.79 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.04K USD at 2228.3000 USD [API] | `2026-08-19 20:51:18` |
| `ANNOUNCEMENT` | `INFO` | `2228.30` | 44.79 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.04K USD at 2228.3000 USD [API] | `2026-08-19 20:51:18` |
| `ANNOUNCEMENT` | `INFO` | `2228.30` | 112.08 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.11K USD at 2228.3000 USD [API] | `2026-08-19 20:51:18` |
| `ANNOUNCEMENT` | `INFO` | `2228.30` | 224.17 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.22K USD at 2228.3000 USD [API] | `2026-08-19 20:51:18` |
| `ANNOUNCEMENT` | `INFO` | `2228.30` | 242.66 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.24K USD at 2228.3000 USD [API] | `2026-08-19 20:51:18` |
| `ANNOUNCEMENT` | `INFO` | `2258.10` | 38,931.00 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 38.93K USD at 2258.1000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2258.00` | 20.10 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2258.0000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2258.00` | 20.10 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2258.0000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2258.00` | 20.10 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2258.0000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2258.00` | 20.10 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2258.0000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2258.00` | 20.10 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2258.0000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2258.00` | 20.10 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2258.0000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2258.00` | 20.10 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2258.0000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2258.00` | 20.10 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2258.0000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2258.00` | 20.10 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2258.0000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2258.00` | 20.10 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2258.0000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2258.00` | 20.10 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2258.0000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2258.00` | 20.10 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2258.0000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2258.00` | 20.10 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2258.0000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2258.00` | 20.10 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2258.0000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2258.00` | 20.10 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2258.0000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2258.00` | 20.10 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2258.0000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2258.00` | 20.10 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2258.0000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2258.00` | 20.10 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2258.0000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2258.00` | 20.10 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2258.0000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2258.00` | 20.10 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2258.0000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2257.90` | 1,201.20 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.20K USD at 2257.9000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2257.80` | 2,596.47 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 2.60K USD at 2257.8000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2257.00` | 812.52 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.81K USD at 2257.0000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2256.70` | 304.65 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.30K USD at 2256.7000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2255.80` | 2,000.89 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 2.00K USD at 2255.8000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2255.80` | 13,985.28 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 13.99K USD at 2255.8000 USD [API] | `2026-08-19 20:51:15` |
| `ANNOUNCEMENT` | `INFO` | `2183.60` | 72,829.39 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 72.83K USD at 2183.6000 USD [API] | `2026-08-19 20:50:42` |
| `ANNOUNCEMENT` | `INFO` | `2338.60` | 42,678.05 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 42.68K USD at 2338.6000 USD [API] | `2026-10-28 12:49:54` |
| `ANNOUNCEMENT` | `INFO` | `2357.90` | 120,165.42 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 120.17K USD at 2357.9000 USD [API] | `2026-10-27 21:33:15` |
| `ANNOUNCEMENT` | `INFO` | `2346.30` | 120,189.45 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 120.19K USD at 2346.3000 USD [API] | `2026-10-27 15:21:36` |
| `ANNOUNCEMENT` | `INFO` | `2338.30` | 49,483.81 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 49.48K USD at 2338.3000 USD [API] | `2026-10-28 13:12:55` |
| `ANNOUNCEMENT` | `INFO` | `2346.60` | 47,825.35 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 47.83K USD at 2346.6000 USD [API] | `2026-10-18 19:30:44` |
| `ANNOUNCEMENT` | `INFO` | `2376.70` | 11,223.02 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 11.22K USD at 2376.7000 USD [API] | `2026-10-15 02:22:46` |
| `ANNOUNCEMENT` | `INFO` | `2323.80` | 28.58 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.03K USD at 2323.8000 USD [API] | `2026-10-28 13:48:33` |
| `ANNOUNCEMENT` | `INFO` | `2323.80` | 25.10 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.03K USD at 2323.8000 USD [API] | `2026-10-28 13:48:33` |
| `ANNOUNCEMENT` | `INFO` | `2323.80` | 14,458.68 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 14.46K USD at 2323.8000 USD [API] | `2026-10-28 13:48:33` |
| `ANNOUNCEMENT` | `INFO` | `2375.20` | 1,205.65 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.21K USD at 2375.2000 USD [API] | `2026-10-28 08:35:30` |
| `ANNOUNCEMENT` | `INFO` | `2331.30` | 61,479.41 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 61.48K USD at 2331.3000 USD [API] | `2026-10-28 14:52:07` |
| `ANNOUNCEMENT` | `INFO` | `2331.30` | 49,215.37 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 49.22K USD at 2331.3000 USD [API] | `2026-10-28 14:52:07` |
| `ANNOUNCEMENT` | `INFO` | `2330.20` | 49,530.96 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 49.53K USD at 2330.2000 USD [API] | `2026-10-28 14:54:21` |
| `ANNOUNCEMENT` | `INFO` | `2316.30` | 46,777.22 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 46.78K USD at 2316.3000 USD [API] | `2026-10-15 02:28:53` |
| `ANNOUNCEMENT` | `INFO` | `2335.70` | 40,057.49 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 40.06K USD at 2335.7000 USD [API] | `2026-10-28 15:19:10` |
| `ANNOUNCEMENT` | `INFO` | `2331.60` | 49,997.90 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 50.00K USD at 2331.6000 USD [API] | `2026-10-28 16:11:00` |
| `ANNOUNCEMENT` | `INFO` | `2326.60` | 42,131.24 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 42.13K USD at 2326.6000 USD [API] | `2026-10-28 16:47:56` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`2403.57` (Vol: 16,800,000.00 USD, Dist: `+3.87%`) | Long MP=`2294.75` (Vol: 27,100,000.00 USD, Dist: `--0.83%`)
  * 48H Horizon: Short MP=`2401.93` (Vol: 25,300,000.00 USD, Dist: `+3.80%`) | Long MP=`2284.33` (Vol: 30,000,000.00 USD, Dist: `--1.28%`)
  * 3D Horizon: Short MP=`2401.93` (Vol: 26,700,000.00 USD, Dist: `+3.80%`) | Long MP=`2286.29` (Vol: 37,900,000.00 USD, Dist: `--1.20%`)
  * 7D Horizon: Short MP=`2402.93` (Vol: 47,100,000.00 USD, Dist: `+3.84%`) | Long MP=`2284.60` (Vol: 72,300,000.00 USD, Dist: `--1.27%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `465.00` | 14,510.00 USD | 845,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `475.00` | 3,720.00 USD | 845,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.00` | 43,950.00 USD | 845,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `495.00` | 5,270.00 USD | 845,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.00` | 1,810,000.00 USD | 845,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.00` | 2,140.00 USD | 844,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.00` | 10,400.00 USD | 844,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.00` | 15,310.00 USD | 844,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.00` | 49,430.00 USD | 844,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.00` | 174,920.00 USD | 843,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `565.00` | 214.70 USD | 843,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `575.00` | 30,880.00 USD | 843,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.00` | 1,760,000.00 USD | 843,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.00` | 990,010.00 USD | 842,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `605.00` | 433,350.00 USD | 841,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.00` | 2,450.00 USD | 840,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.00` | 17,370.00 USD | 840,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.00` | 6,490.00 USD | 840,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `645.00` | 2,780,000.00 USD | 840,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `655.00` | 50,740.00 USD | 837,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `665.00` | 26,820.00 USD | 837,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `675.00` | 20,070.00 USD | 837,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `685.00` | 28,680.00 USD | 837,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `695.00` | 668.59 USD | 837,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `705.00` | 32,420.00 USD | 837,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `715.00` | 1,570,000.00 USD | 837,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `725.00` | 393,960.00 USD | 836,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `735.00` | 39,690.00 USD | 835,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `745.00` | 2,170.00 USD | 835,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `755.00` | 27,360.00 USD | 835,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `765.00` | 17,180.00 USD | 835,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `775.00` | 58,650.00 USD | 835,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `785.00` | 21,990.00 USD | 835,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `795.00` | 41,860.00 USD | 835,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `805.00` | 56,280.00 USD | 835,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `815.00` | 18,470.00 USD | 835,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `825.00` | 309,280.00 USD | 835,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `835.00` | 22,040.00 USD | 835,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `845.00` | 34,180.00 USD | 835,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `855.00` | 134,590.00 USD | 835,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `865.00` | 455,230.00 USD | 834,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `875.00` | 100,450.00 USD | 834,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `885.00` | 1,010,000.00 USD | 834,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `895.00` | 159,890.00 USD | 833,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `905.00` | 67,390.00 USD | 833,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `915.00` | 421,100.00 USD | 833,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `925.00` | 117,910.00 USD | 832,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `935.00` | 41,570.00 USD | 832,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `945.00` | 29,180.00 USD | 832,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `955.00` | 346,950.00 USD | 832,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `965.00` | 158,530.00 USD | 832,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `975.00` | 92,680.00 USD | 831,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `985.00` | 91,750.00 USD | 831,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `995.00` | 19,850.00 USD | 831,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1005.00` | 33,640.00 USD | 831,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1015.00` | 58,220.00 USD | 831,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1025.00` | 131,090.00 USD | 831,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1035.00` | 213,680.00 USD | 831,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1045.00` | 7,730,000.00 USD | 831,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1055.00` | 1,540,000.00 USD | 823,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1065.00` | 133,980.00 USD | 822,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1075.00` | 670,060.00 USD | 821,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1085.00` | 60,670.00 USD | 821,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1095.00` | 168,380.00 USD | 821,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1105.00` | 132,910.00 USD | 821,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1115.00` | 88,340.00 USD | 820,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1125.00` | 43,820.00 USD | 820,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1135.00` | 193,380.00 USD | 820,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1145.00` | 312,170.00 USD | 820,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1155.00` | 401,010.00 USD | 820,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1165.00` | 194,270.00 USD | 819,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1175.00` | 1,560,000.00 USD | 819,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1185.00` | 159,620.00 USD | 818,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1195.00` | 452,850.00 USD | 817,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1205.00` | 242,850.00 USD | 817,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1215.00` | 287,380.00 USD | 817,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1225.00` | 2,890,000.00 USD | 816,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1235.00` | 2,680,000.00 USD | 814,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1245.00` | 290,450.00 USD | 811,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1255.00` | 369,450.00 USD | 811,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1265.00` | 249,220.00 USD | 810,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1275.00` | 118,280.00 USD | 810,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1285.00` | 15,610,000.00 USD | 810,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1295.00` | 271,050.00 USD | 794,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1305.00` | 257,050.00 USD | 794,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1315.00` | 580,470.00 USD | 794,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1325.00` | 1,550,000.00 USD | 793,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1335.00` | 298,460.00 USD | 792,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1345.00` | 497,840.00 USD | 791,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1355.00` | 359,190.00 USD | 791,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1365.00` | 1,070,000.00 USD | 790,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1375.00` | 12,800,000.00 USD | 789,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1385.00` | 6,970,000.00 USD | 777,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1395.00` | 153,570.00 USD | 770,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1405.00` | 10,020,000.00 USD | 769,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1415.00` | 1,460,000.00 USD | 759,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1425.00` | 875,640.00 USD | 758,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1435.00` | 245,420.00 USD | 757,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1445.00` | 287,790.00 USD | 757,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1455.00` | 69,520.00 USD | 757,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1465.00` | 1,190,000.00 USD | 756,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1475.00` | 5,640,000.00 USD | 755,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1485.00` | 17,690,000.00 USD | 750,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1495.00` | 16,380,000.00 USD | 732,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1505.00` | 137,450.00 USD | 716,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1515.00` | 15,520,000.00 USD | 715,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1525.00` | 18,750,000.00 USD | 700,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1535.00` | 10,250,000.00 USD | 681,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1545.00` | 3,890,000.00 USD | 671,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1555.00` | 536,530.00 USD | 667,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1565.00` | 257,330.00 USD | 667,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1575.00` | 458,760.00 USD | 666,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1585.00` | 546,140.00 USD | 666,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1595.00` | 947,400.00 USD | 665,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1605.00` | 18,700,000.00 USD | 664,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1615.00` | 513,600.00 USD | 646,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1625.00` | 959,010.00 USD | 645,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1635.00` | 18,460,000.00 USD | 644,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1645.00` | 36,440,000.00 USD | 626,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1655.00` | 14,670,000.00 USD | 589,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1665.00` | 1,250,000.00 USD | 575,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1675.00` | 11,600,000.00 USD | 573,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1685.00` | 7,480,000.00 USD | 562,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1695.00` | 878,130.00 USD | 554,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1705.00` | 29,770,000.00 USD | 553,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1715.00` | 482,750.00 USD | 524,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1725.00` | 35,080,000.00 USD | 523,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1735.00` | 634,090.00 USD | 488,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1745.00` | 1,040,000.00 USD | 487,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1755.00` | 204,030.00 USD | 486,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1765.00` | 713,160.00 USD | 486,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1775.00` | 1,200,000.00 USD | 485,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1785.00` | 54,930,000.00 USD | 484,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1795.00` | 4,280,000.00 USD | 429,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1805.00` | 12,700,000.00 USD | 425,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1815.00` | 2,280,000.00 USD | 412,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1825.00` | 461,220.00 USD | 410,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1835.00` | 1,750,000.00 USD | 410,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1845.00` | 847,540.00 USD | 408,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1855.00` | 2,070,000.00 USD | 407,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1865.00` | 772,330.00 USD | 405,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1875.00` | 9,890,000.00 USD | 404,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1885.00` | 2,690,000.00 USD | 394,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1895.00` | 6,610,000.00 USD | 392,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1905.00` | 765,450.00 USD | 385,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1915.00` | 13,520,000.00 USD | 384,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1925.00` | 19,280,000.00 USD | 371,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1935.00` | 1,320,000.00 USD | 351,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1945.00` | 7,380,000.00 USD | 350,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1955.00` | 1,720,000.00 USD | 343,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1965.00` | 1,100,000.00 USD | 341,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1975.00` | 2,900,000.00 USD | 340,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1985.00` | 5,730,000.00 USD | 337,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1995.00` | 9,670,000.00 USD | 331,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2005.00` | 1,540,000.00 USD | 322,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2015.00` | 2,450,000.00 USD | 320,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2017.30` | 455,960,000.00 USD | 455,960,000.00 USD | 83,300.00 USD | 176,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2020.30` | 455,700,000.00 USD | 455,700,000.00 USD | 0.00 USD | 558,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2025.00` | 2,210,000.00 USD | 318,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2025.30` | 999,770,000.00 USD | 999,770,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2026.30` | 455,140,000.00 USD | 455,140,000.00 USD | 0.00 USD | 914,780.00 USD | 28,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2028.60` | 999,590,000.00 USD | 999,590,000.00 USD | 0.00 USD | 1,180,000.00 USD | 35,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2029.30` | 454,190,000.00 USD | 454,190,000.00 USD | 0.00 USD | 0.00 USD | 43,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2031.90` | 998,380,000.00 USD | 998,380,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2032.30` | 454,150,000.00 USD | 454,150,000.00 USD | 937,190.00 USD | 1,470,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2035.00` | 538,430.00 USD | 315,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2035.20` | 996,930,000.00 USD | 996,930,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2035.30` | 451,750,000.00 USD | 451,750,000.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2038.30` | 450,710,000.00 USD | 450,710,000.00 USD | 138,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2038.50` | 996,600,000.00 USD | 996,600,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2041.30` | 450,570,000.00 USD | 450,570,000.00 USD | 0.00 USD | 134,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2045.00` | 16,630,000.00 USD | 315,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2045.10` | 995,140,000.00 USD | 995,140,000.00 USD | 0.00 USD | 149,500.00 USD | 47,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2050.30` | 450,440,000.00 USD | 450,440,000.00 USD | 0.00 USD | 0.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2051.70` | 994,940,000.00 USD | 994,940,000.00 USD | 1,320,000.00 USD | 0.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2053.30` | 449,720,000.00 USD | 449,720,000.00 USD | 0.00 USD | 0.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2055.00` | 13,190,000.00 USD | 298,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2056.30` | 449,690,000.00 USD | 449,690,000.00 USD | 242,080.00 USD | 88,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2058.30` | 992,440,000.00 USD | 992,440,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2059.30` | 449,360,000.00 USD | 449,360,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2061.60` | 992,090,000.00 USD | 992,090,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2062.30` | 448,610,000.00 USD | 448,610,000.00 USD | 80,610.00 USD | 121,470.00 USD | 52,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2064.90` | 987,650,000.00 USD | 987,650,000.00 USD | 1,230,000.00 USD | 313,000.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2065.00` | 2,230,000.00 USD | 285,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2065.30` | 448,350,000.00 USD | 448,350,000.00 USD | 984,680.00 USD | 537,030.00 USD | 598,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2068.20` | 985,130,000.00 USD | 985,130,000.00 USD | 1,740,000.00 USD | 1,860,000.00 USD | 893,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2068.30` | 446,230,000.00 USD | 446,230,000.00 USD | 444,700.00 USD | 1,330,000.00 USD | 50,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2071.30` | 444,410,000.00 USD | 444,410,000.00 USD | 1,040,000.00 USD | 534,600.00 USD | 437,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2071.50` | 980,630,000.00 USD | 980,630,000.00 USD | 2,820,000.00 USD | 2,410,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2074.30` | 442,400,000.00 USD | 442,400,000.00 USD | 614,280.00 USD | 62,630.00 USD | 930,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2074.80` | 974,170,000.00 USD | 974,170,000.00 USD | 4,370,000.00 USD | 3,270,000.00 USD | 4,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 1,310,000.00 USD | 283,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2077.30` | 440,790,000.00 USD | 440,790,000.00 USD | 3,000,000.00 USD | 1,520,000.00 USD | 2,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2078.10` | 962,470,000.00 USD | 962,470,000.00 USD | 5,560,000.00 USD | 4,320,000.00 USD | 2,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2080.30` | 434,090,000.00 USD | 434,090,000.00 USD | 1,670,000.00 USD | 1,590,000.00 USD | 280,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2081.40` | 950,180,000.00 USD | 950,180,000.00 USD | 4,720,000.00 USD | 3,420,000.00 USD | 2,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2083.30` | 430,550,000.00 USD | 430,550,000.00 USD | 2,180,000.00 USD | 1,420,000.00 USD | 775,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2084.70` | 939,550,000.00 USD | 939,550,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 4,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 4,940,000.00 USD | 281,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2086.30` | 426,180,000.00 USD | 426,180,000.00 USD | 1,580,000.00 USD | 1,500,000.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2088.00` | 930,750,000.00 USD | 930,750,000.00 USD | 3,990,000.00 USD | 2,780,000.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2089.30` | 421,450,000.00 USD | 421,450,000.00 USD | 1,470,000.00 USD | 430,310.00 USD | 228,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2091.30` | 922,330,000.00 USD | 922,330,000.00 USD | 4,410,000.00 USD | 952,210.00 USD | 7,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2092.30` | 419,330,000.00 USD | 419,330,000.00 USD | 1,150,000.00 USD | 514,440.00 USD | 957,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2094.60` | 909,370,000.00 USD | 909,370,000.00 USD | 5,720,000.00 USD | 2,160,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 2,440,000.00 USD | 277,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2095.30` | 416,710,000.00 USD | 416,710,000.00 USD | 2,180,000.00 USD | 1,320,000.00 USD | 2,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2097.90` | 899,150,000.00 USD | 899,150,000.00 USD | 2,340,000.00 USD | 3,210,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2098.30` | 411,100,000.00 USD | 411,100,000.00 USD | 474,990.00 USD | 1,170,000.00 USD | 309,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2101.20` | 892,310,000.00 USD | 892,310,000.00 USD | 999,530.00 USD | 1,580,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2101.30` | 409,140,000.00 USD | 409,140,000.00 USD | 207,380.00 USD | 44,780.00 USD | 304,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2104.30` | 408,590,000.00 USD | 408,590,000.00 USD | 1,070,000.00 USD | 961,080.00 USD | 190,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2104.50` | 885,710,000.00 USD | 885,710,000.00 USD | 2,010,000.00 USD | 1,180,000.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 1,530,000.00 USD | 274,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2107.30` | 406,360,000.00 USD | 406,360,000.00 USD | 546,100.00 USD | 0.00 USD | 502,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2107.80` | 880,270,000.00 USD | 880,270,000.00 USD | 2,380,000.00 USD | 452,470.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2110.30` | 405,310,000.00 USD | 405,310,000.00 USD | 118,210.00 USD | 31,550.00 USD | 196,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2111.10` | 875,790,000.00 USD | 875,790,000.00 USD | 3,530,000.00 USD | 2,350,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2113.30` | 404,970,000.00 USD | 404,970,000.00 USD | 911,810.00 USD | 643,210.00 USD | 224,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2114.40` | 867,740,000.00 USD | 867,740,000.00 USD | 1,080,000.00 USD | 1,850,000.00 USD | 3,800,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 938,020.00 USD | 273,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2116.30` | 403,190,000.00 USD | 403,190,000.00 USD | 0.00 USD | 13,230.00 USD | 426,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2117.70` | 861,010,000.00 USD | 861,010,000.00 USD | 3,430,000.00 USD | 2,020,000.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2119.30` | 402,750,000.00 USD | 402,750,000.00 USD | 218,200.00 USD | 256,720.00 USD | 937,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2121.00` | 852,180,000.00 USD | 852,180,000.00 USD | 3,650,000.00 USD | 1,340,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2122.30` | 401,340,000.00 USD | 401,340,000.00 USD | 926,060.00 USD | 689,080.00 USD | 1,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2124.30` | 845,370,000.00 USD | 845,370,000.00 USD | 832,850.00 USD | 972,650.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 2,800,000.00 USD | 272,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2125.30` | 398,410,000.00 USD | 398,410,000.00 USD | 1,010,000.00 USD | 950,560.00 USD | 707,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2127.60` | 842,050,000.00 USD | 842,050,000.00 USD | 2,400,000.00 USD | 2,630,000.00 USD | 3,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2128.30` | 395,740,000.00 USD | 395,740,000.00 USD | 365,910.00 USD | 1,040,000.00 USD | 293,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2130.90` | 833,750,000.00 USD | 833,750,000.00 USD | 2,410,000.00 USD | 2,300,000.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2131.30` | 394,050,000.00 USD | 394,050,000.00 USD | 0.00 USD | 18,610.00 USD | 649,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2134.20` | 827,330,000.00 USD | 827,330,000.00 USD | 2,170,000.00 USD | 550,450.00 USD | 308,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 4,780,000.00 USD | 269,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2137.30` | 393,380,000.00 USD | 393,380,000.00 USD | 0.00 USD | 278,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2137.50` | 824,300,000.00 USD | 824,300,000.00 USD | 1,040,000.00 USD | 880,790.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2140.80` | 822,340,000.00 USD | 822,340,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2144.10` | 818,410,000.00 USD | 818,410,000.00 USD | 449,020.00 USD | 1,130,000.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 26,580,000.00 USD | 264,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2147.40` | 816,560,000.00 USD | 816,560,000.00 USD | 657,710.00 USD | 421,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2150.70` | 815,480,000.00 USD | 815,480,000.00 USD | 459,630.00 USD | 463,640.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2152.30` | 393,100,000.00 USD | 393,100,000.00 USD | 208,250.00 USD | 440,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2154.00` | 814,530,000.00 USD | 814,530,000.00 USD | 128,430.00 USD | 331,520.00 USD | 32,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 2,870,000.00 USD | 237,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2155.30` | 392,450,000.00 USD | 392,450,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2157.30` | 814,030,000.00 USD | 814,030,000.00 USD | 388,210.00 USD | 1,030,000.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2158.30` | 391,060,000.00 USD | 391,060,000.00 USD | 0.00 USD | 0.00 USD | 37,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2160.60` | 811,540,000.00 USD | 811,540,000.00 USD | 646,940.00 USD | 1,900,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2161.30` | 391,020,000.00 USD | 391,020,000.00 USD | 0.00 USD | 3,150,000.00 USD | 71,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2163.90` | 806,990,000.00 USD | 806,990,000.00 USD | 566,120.00 USD | 3,280,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2164.30` | 387,800,000.00 USD | 387,800,000.00 USD | 0.00 USD | 0.00 USD | 55,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 1,870,000.00 USD | 235,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2167.20` | 801,850,000.00 USD | 801,850,000.00 USD | 25,540.00 USD | 3,620,000.00 USD | 50,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2167.30` | 387,740,000.00 USD | 387,740,000.00 USD | 2,340,000.00 USD | 341,240.00 USD | 52,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2170.30` | 385,010,000.00 USD | 385,010,000.00 USD | 5,020,000.00 USD | 4,430,000.00 USD | 873,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2170.50` | 798,150,000.00 USD | 798,150,000.00 USD | 3,500,000.00 USD | 2,380,000.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2173.30` | 374,680,000.00 USD | 374,680,000.00 USD | 0.00 USD | 190,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2173.80` | 790,450,000.00 USD | 790,450,000.00 USD | 4,110,000.00 USD | 363,040.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 110,260,000.00 USD | 233,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2176.30` | 374,490,000.00 USD | 374,490,000.00 USD | 345,940.00 USD | 1,400,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2179.30` | 372,750,000.00 USD | 372,750,000.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2180.40` | 784,960,000.00 USD | 784,960,000.00 USD | 0.00 USD | 373,740.00 USD | 119,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2185.00` | 101,640,000.00 USD | 122,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2185.30` | 371,570,000.00 USD | 371,570,000.00 USD | 1,350,000.00 USD | 0.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2187.00` | 784,470,000.00 USD | 784,470,000.00 USD | 556,600.00 USD | 0.00 USD | 54,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2190.30` | 783,860,000.00 USD | 783,860,000.00 USD | 2,730,000.00 USD | 0.00 USD | 2,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2191.30` | 368,420,000.00 USD | 368,420,000.00 USD | 0.00 USD | 222,200.00 USD | 70,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2194.30` | 368,120,000.00 USD | 368,120,000.00 USD | 605,210.00 USD | 0.00 USD | 39,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 7,900,000.00 USD | 21,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2196.90` | 778,150,000.00 USD | 778,150,000.00 USD | 2,580,000.00 USD | 474,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2197.30` | 367,480,000.00 USD | 367,480,000.00 USD | 416,500.00 USD | 881,070.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2200.20` | 775,090,000.00 USD | 775,090,000.00 USD | 3,000,000.00 USD | 5,080,000.00 USD | 3,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2200.30` | 364,300,000.00 USD | 364,300,000.00 USD | 284,470.00 USD | 3,100,000.00 USD | 220,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2203.30` | 360,690,000.00 USD | 360,690,000.00 USD | 3,540,000.00 USD | 1,410,000.00 USD | 2,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2203.50` | 763,810,000.00 USD | 763,810,000.00 USD | 3,650,000.00 USD | 1,710,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 1,760,000.00 USD | 13,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2206.30` | 353,640,000.00 USD | 353,640,000.00 USD | 755,060.00 USD | 10,890,000.00 USD | 946,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2206.80` | 754,710,000.00 USD | 754,710,000.00 USD | 6,920,000.00 USD | 9,430,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2209.30` | 341,060,000.00 USD | 341,060,000.00 USD | 2,720,000.00 USD | 2,010,000.00 USD | 3,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2210.10` | 734,330,000.00 USD | 734,330,000.00 USD | 12,800,000.00 USD | 20,410,000.00 USD | 6,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2212.30` | 333,290,000.00 USD | 333,290,000.00 USD | 7,970,000.00 USD | 2,320,000.00 USD | 3,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2213.40` | 694,660,000.00 USD | 694,660,000.00 USD | 10,920,000.00 USD | 11,890,000.00 USD | 13,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 4,410,000.00 USD | 11,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2215.30` | 319,940,000.00 USD | 319,940,000.00 USD | 17,700,000.00 USD | 14,340,000.00 USD | 7,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2216.70` | 658,670,000.00 USD | 658,670,000.00 USD | 25,210,000.00 USD | 17,030,000.00 USD | 9,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2218.30` | 280,660,000.00 USD | 280,660,000.00 USD | 7,390,000.00 USD | 7,700,000.00 USD | 2,280,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2220.00` | 607,050,000.00 USD | 607,050,000.00 USD | 24,310,000.00 USD | 12,300,000.00 USD | 10,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2221.30` | 263,300,000.00 USD | 263,300,000.00 USD | 6,130,000.00 USD | 12,360,000.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2223.30` | 560,320,000.00 USD | 560,320,000.00 USD | 10,150,000.00 USD | 8,220,000.00 USD | 11,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2224.30` | 243,550,000.00 USD | 243,550,000.00 USD | 9,430,000.00 USD | 5,550,000.00 USD | 5,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2225.00` | 5,180,000.00 USD | 7,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2226.60` | 530,040,000.00 USD | 530,040,000.00 USD | 12,840,000.00 USD | 11,030,000.00 USD | 9,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2227.30` | 223,020,000.00 USD | 223,020,000.00 USD | 5,860,000.00 USD | 13,040,000.00 USD | 2,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2229.90` | 496,330,000.00 USD | 496,330,000.00 USD | 12,730,000.00 USD | 9,180,000.00 USD | 20,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2230.30` | 201,510,000.00 USD | 201,510,000.00 USD | 6,920,000.00 USD | 5,550,000.00 USD | 2,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2233.20` | 453,760,000.00 USD | 453,760,000.00 USD | 16,600,000.00 USD | 24,290,000.00 USD | 10,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2233.30` | 186,440,000.00 USD | 186,440,000.00 USD | 6,390,000.00 USD | 2,520,000.00 USD | 8,970,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2235.00` | 1,910,000.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2236.30` | 168,550,000.00 USD | 168,550,000.00 USD | 18,610,000.00 USD | 0.00 USD | 4,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2236.50` | 402,440,000.00 USD | 402,440,000.00 USD | 16,050,000.00 USD | 2,010,000.00 USD | 11,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2239.30` | 145,560,000.00 USD | 145,560,000.00 USD | 16,040,000.00 USD | 4,410,000.00 USD | 4,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2239.80` | 372,600,000.00 USD | 372,600,000.00 USD | 15,710,000.00 USD | 6,600,000.00 USD | 13,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2242.30` | 120,690,000.00 USD | 120,690,000.00 USD | 2,420,000.00 USD | 760,920.00 USD | 5,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2243.10` | 336,540,000.00 USD | 336,540,000.00 USD | 22,920,000.00 USD | 0.00 USD | 8,970,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2245.00` | 160,900.00 USD | 179,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2245.30` | 112,280,000.00 USD | 112,280,000.00 USD | 2,360,000.00 USD | 4,260,000.00 USD | 482,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2246.40` | 304,650,000.00 USD | 304,650,000.00 USD | 14,340,000.00 USD | 0.00 USD | 13,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2248.30` | 105,170,000.00 USD | 105,170,000.00 USD | 8,900,000.00 USD | 0.00 USD | 4,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2249.70` | 276,390,000.00 USD | 276,390,000.00 USD | 18,000,000.00 USD | 0.00 USD | 12,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2251.30` | 92,180,000.00 USD | 92,180,000.00 USD | 9,610,000.00 USD | 506,110.00 USD | 2,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2253.00` | 245,800,000.00 USD | 245,800,000.00 USD | 26,890,000.00 USD | 0.00 USD | 17,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2254.30` | 79,120,000.00 USD | 79,120,000.00 USD | 0.00 USD | 0.00 USD | 12,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2255.00` | 18,560.00 USD | 18,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2256.30` | 200,970,000.00 USD | 200,970,000.00 USD | 17,450,000.00 USD | 0.00 USD | 3,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2259.60` | 180,210,000.00 USD | 180,210,000.00 USD | 10,940,000.00 USD | 0.00 USD | 11,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2260.30` | 66,520,000.00 USD | 66,520,000.00 USD | 0.00 USD | 0.00 USD | 156,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2263.30` | 66,370,000.00 USD | 66,370,000.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2265.00` | 7,250.00 USD | 7,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2266.30` | 63,950,000.00 USD | 63,950,000.00 USD | 0.00 USD | 0.00 USD | 12,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2269.30` | 51,810,000.00 USD | 51,810,000.00 USD | 0.00 USD | 0.00 USD | 7,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2269.50` | 157,360,000.00 USD | 157,360,000.00 USD | 0.00 USD | 4,370,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2272.30` | 43,850,000.00 USD | 43,850,000.00 USD | 0.00 USD | 9,150,000.00 USD | 12,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2272.80` | 152,990,000.00 USD | 152,990,000.00 USD | 0.00 USD | 31,270,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2275.00` | 48,600.00 USD | 55,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2275.30` | 22,200,000.00 USD | 22,200,000.00 USD | 1,020,000.00 USD | 20,900,000.00 USD | 287,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2276.10` | 121,730,000.00 USD | 121,730,000.00 USD | 0.00 USD | 54,160,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2278.30` | 18,870,000.00 USD | 18,870,000.00 USD | 2,840,000.00 USD | 15,600,000.00 USD | 431,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2279.40` | 67,560,000.00 USD | 67,560,000.00 USD | 0.00 USD | 67,560,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2281.30` | 105,590,000.00 USD | 105,590,000.00 USD | 40,410,000.00 USD | 26,130,000.00 USD | 20,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2282.70` | 81,670,000.00 USD | 81,670,000.00 USD | 0.00 USD | 81,670,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2284.30` | 175,900,000.00 USD | 175,900,000.00 USD | 34,880,000.00 USD | 20,290,000.00 USD | 15,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2285.00` | 6,220,000.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2286.00` | 91,070,000.00 USD | 91,070,000.00 USD | 0.00 USD | 9,400,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2287.30` | 176,660,000.00 USD | 176,660,000.00 USD | 0.00 USD | 760,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2290.30` | 185,050,000.00 USD | 185,050,000.00 USD | 0.00 USD | 8,390,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2293.30` | 189,850,000.00 USD | 189,850,000.00 USD | 4,720,000.00 USD | 0.00 USD | 75,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2295.00` | 12,310.00 USD | 6,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2295.90` | 100,510,000.00 USD | 100,510,000.00 USD | 6,580,000.00 USD | 2,380,000.00 USD | 479,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2296.30` | 196,290,000.00 USD | 196,290,000.00 USD | 0.00 USD | 6,300,000.00 USD | 143,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2299.20` | 118,540,000.00 USD | 118,540,000.00 USD | 11,730,000.00 USD | 5,900,000.00 USD | 392,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2299.30` | 208,890,000.00 USD | 208,890,000.00 USD | 5,410,000.00 USD | 10,910.00 USD | 7,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2302.30` | 219,420,000.00 USD | 219,420,000.00 USD | 9,550,000.00 USD | 682,490.00 USD | 298,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2302.50` | 160,780,000.00 USD | 160,780,000.00 USD | 23,020,000.00 USD | 7,250,000.00 USD | 11,970,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2305.00` | 1,210,000.00 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2305.30` | 248,720,000.00 USD | 248,720,000.00 USD | 13,540,000.00 USD | 13,730,000.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2305.80` | 172,070,000.00 USD | 172,070,000.00 USD | 2,980,000.00 USD | 6,110,000.00 USD | 2,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2308.30` | 254,050,000.00 USD | 254,050,000.00 USD | 2,420,000.00 USD | 2,750,000.00 USD | 156,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2309.10` | 175,840,000.00 USD | 175,840,000.00 USD | 732,090.00 USD | 930,630.00 USD | 2,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2311.30` | 262,290,000.00 USD | 262,290,000.00 USD | 691,870.00 USD | 0.00 USD | 7,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2312.40` | 183,190,000.00 USD | 183,190,000.00 USD | 7,270,000.00 USD | 0.00 USD | 70,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2314.30` | 273,750,000.00 USD | 273,750,000.00 USD | 0.00 USD | 11,260,000.00 USD | 203,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2315.00` | 4,720,000.00 USD | 12,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2315.70` | 190,760,000.00 USD | 190,760,000.00 USD | 0.00 USD | 7,460,000.00 USD | 117,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2317.30` | 300,680,000.00 USD | 300,680,000.00 USD | 8,430,000.00 USD | 13,390,000.00 USD | 5,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2319.00` | 196,750,000.00 USD | 196,750,000.00 USD | 1,020,000.00 USD | 4,550,000.00 USD | 411,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2320.30` | 315,750,000.00 USD | 315,750,000.00 USD | 6,580,000.00 USD | 8,340,000.00 USD | 147,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2322.30` | 211,290,000.00 USD | 211,290,000.00 USD | 1,110,000.00 USD | 13,320,000.00 USD | 108,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2323.30` | 327,430,000.00 USD | 327,430,000.00 USD | 572,970.00 USD | 7,510,000.00 USD | 3,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2325.00` | 134,130.00 USD | 12,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2325.60` | 229,510,000.00 USD | 229,510,000.00 USD | 9,720,000.00 USD | 2,540,000.00 USD | 5,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2326.30` | 337,730,000.00 USD | 337,730,000.00 USD | 479,120.00 USD | 5,550,000.00 USD | 4,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2328.90` | 241,330,000.00 USD | 241,330,000.00 USD | 3,860,000.00 USD | 0.00 USD | 7,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2329.30` | 349,030,000.00 USD | 349,030,000.00 USD | 10,000,000.00 USD | 884,940.00 USD | 422,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2332.20` | 270,560,000.00 USD | 270,560,000.00 USD | 29,230,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2332.30` | 364,770,000.00 USD | 364,770,000.00 USD | 11,600,000.00 USD | 251,940.00 USD | 3,880,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2335.00` | 343,060.00 USD | 12,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2335.30` | 388,690,000.00 USD | 388,690,000.00 USD | 17,430,000.00 USD | 3,070,000.00 USD | 3,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2335.50` | 324,500,000.00 USD | 324,500,000.00 USD | 28,990,000.00 USD | 18,420,000.00 USD | 6,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2338.30` | 401,580,000.00 USD | 401,580,000.00 USD | 6,030,000.00 USD | 688,030.00 USD | 6,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2338.80` | 342,370,000.00 USD | 342,370,000.00 USD | 9,570,000.00 USD | 0.00 USD | 8,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2341.30` | 426,810,000.00 USD | 426,810,000.00 USD | 9,780,000.00 USD | 5,570,000.00 USD | 9,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2342.10` | 382,470,000.00 USD | 382,470,000.00 USD | 4,720,000.00 USD | 21,390,000.00 USD | 14,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2344.30` | 440,070,000.00 USD | 440,070,000.00 USD | 1,370,000.00 USD | 6,180,000.00 USD | 5,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2345.00` | 597,120.00 USD | 13,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2345.40` | 403,840,000.00 USD | 403,840,000.00 USD | 1,350,000.00 USD | 13,990,000.00 USD | 6,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2347.30` | 451,910,000.00 USD | 451,910,000.00 USD | 3,220,000.00 USD | 3,010,000.00 USD | 5,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2348.70` | 436,980,000.00 USD | 436,980,000.00 USD | 847,620.00 USD | 8,140,000.00 USD | 24,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2350.30` | 501,050,000.00 USD | 501,050,000.00 USD | 33,090,000.00 USD | 7,200,000.00 USD | 8,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2352.00` | 473,600,000.00 USD | 473,600,000.00 USD | 2,930,000.00 USD | 23,060,000.00 USD | 10,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2353.30` | 510,240,000.00 USD | 510,240,000.00 USD | 4,170,000.00 USD | 3,800,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 3,250,000.00 USD | 16,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2355.30` | 528,190,000.00 USD | 528,190,000.00 USD | 16,520,000.00 USD | 36,690,000.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2356.30` | 532,990,000.00 USD | 532,990,000.00 USD | 3,710,000.00 USD | 16,640,000.00 USD | 2,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2358.60` | 539,010,000.00 USD | 539,010,000.00 USD | 7,110,000.00 USD | 512,220.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2359.30` | 551,030,000.00 USD | 551,030,000.00 USD | 4,140,000.00 USD | 6,970,000.00 USD | 6,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2361.90` | 546,080,000.00 USD | 546,080,000.00 USD | 3,150,000.00 USD | 3,800,000.00 USD | 119,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2362.30` | 569,670,000.00 USD | 569,670,000.00 USD | 10,460,000.00 USD | 6,710,000.00 USD | 1,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 47,670.00 USD | 16,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2365.20` | 561,430,000.00 USD | 561,430,000.00 USD | 8,440,000.00 USD | 0.00 USD | 6,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2365.30` | 586,140,000.00 USD | 586,140,000.00 USD | 4,820,000.00 USD | 3,710,000.00 USD | 7,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2368.30` | 599,940,000.00 USD | 599,940,000.00 USD | 7,910,000.00 USD | 2,500,000.00 USD | 3,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2368.50` | 573,190,000.00 USD | 573,190,000.00 USD | 10,830,000.00 USD | 475,460.00 USD | 458,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2371.30` | 640,580,000.00 USD | 640,580,000.00 USD | 18,140,000.00 USD | 13,710,000.00 USD | 8,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2371.80` | 652,910,000.00 USD | 652,910,000.00 USD | 26,000,000.00 USD | 0.00 USD | 53,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2374.30` | 663,060,000.00 USD | 663,060,000.00 USD | 14,690,000.00 USD | 1,320,000.00 USD | 6,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 1,040,000.00 USD | 17,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2375.10` | 679,860,000.00 USD | 679,860,000.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2377.30` | 686,820,000.00 USD | 686,820,000.00 USD | 7,110,000.00 USD | 8,030,000.00 USD | 8,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2378.40` | 725,270,000.00 USD | 725,270,000.00 USD | 11,800,000.00 USD | 7,950,000.00 USD | 25,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2380.30` | 730,680,000.00 USD | 730,680,000.00 USD | 14,000,000.00 USD | 11,640,000.00 USD | 18,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2381.70` | 763,020,000.00 USD | 763,020,000.00 USD | 8,510,000.00 USD | 6,750,000.00 USD | 22,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2383.30` | 790,070,000.00 USD | 790,070,000.00 USD | 24,350,000.00 USD | 17,700,000.00 USD | 17,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2385.00` | 864,740,000.00 USD | 864,740,000.00 USD | 18,550,000.00 USD | 36,910,000.00 USD | 46,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 610,200.00 USD | 18,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2386.30` | 828,870,000.00 USD | 828,870,000.00 USD | 12,830,000.00 USD | 14,620,000.00 USD | 11,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2388.30` | 952,610,000.00 USD | 952,610,000.00 USD | 5,290,000.00 USD | 38,070,000.00 USD | 44,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2389.30` | 857,770,000.00 USD | 857,770,000.00 USD | 13,790,000.00 USD | 7,220,000.00 USD | 7,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2391.60` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 8,560,000.00 USD | 52,080,000.00 USD | 40,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2392.30` | 874,150,000.00 USD | 874,150,000.00 USD | 3,240,000.00 USD | 6,420,000.00 USD | 6,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2394.90` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 57,450,000.00 USD | 32,260,000.00 USD | 37,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 823,610.00 USD | 19,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2395.30` | 892,230,000.00 USD | 892,230,000.00 USD | 7,070,000.00 USD | 7,250,000.00 USD | 3,760,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2398.20` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 42,820,000.00 USD | 38,210,000.00 USD | 29,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2398.30` | 912,440,000.00 USD | 912,440,000.00 USD | 5,950,000.00 USD | 6,860,000.00 USD | 7,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2401.30` | 937,980,000.00 USD | 937,980,000.00 USD | 8,760,000.00 USD | 7,400,000.00 USD | 9,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2401.50` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 51,970,000.00 USD | 26,780,000.00 USD | 29,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2404.30` | 968,240,000.00 USD | 968,240,000.00 USD | 10,010,000.00 USD | 11,410,000.00 USD | 8,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2404.80` | 1,510,000,000.00 USD | 1,510,000,000.00 USD | 50,800,000.00 USD | 32,200,000.00 USD | 24,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 1,640,000.00 USD | 20,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2407.30` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 16,500,000.00 USD | 9,260,000.00 USD | 8,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2408.10` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 34,390,000.00 USD | 31,420,000.00 USD | 25,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2410.30` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 8,800,000.00 USD | 8,390,000.00 USD | 9,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2411.40` | 1,680,000,000.00 USD | 1,680,000,000.00 USD | 19,200,000.00 USD | 32,580,000.00 USD | 27,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2413.30` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 8,610,000.00 USD | 5,530,000.00 USD | 3,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2414.70` | 1,740,000,000.00 USD | 1,740,000,000.00 USD | 24,010,000.00 USD | 21,950,000.00 USD | 23,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 51,630.00 USD | 20,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2416.30` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 4,770,000.00 USD | 3,260,000.00 USD | 4,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2418.00` | 1,820,000,000.00 USD | 1,820,000,000.00 USD | 34,060,000.00 USD | 15,260,000.00 USD | 24,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2419.30` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 5,120,000.00 USD | 3,350,000.00 USD | 3,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2421.30` | 1,890,000,000.00 USD | 1,890,000,000.00 USD | 25,700,000.00 USD | 27,890,000.00 USD | 21,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2422.30` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 4,560,000.00 USD | 5,190,000.00 USD | 6,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.60` | 1,990,000,000.00 USD | 1,990,000,000.00 USD | 24,180,000.00 USD | 35,050,000.00 USD | 34,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 334,040.00 USD | 21,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2425.30` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 1,810,000.00 USD | 2,670,000.00 USD | 844,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2427.90` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 25,200,000.00 USD | 18,380,000.00 USD | 26,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2428.30` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 466,170.00 USD | 542,280.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2431.20` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 10,380,000.00 USD | 18,750,000.00 USD | 9,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2431.30` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 2,890,000.00 USD | 2,960,000.00 USD | 347,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2434.30` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 1,930,000.00 USD | 510,300.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2434.50` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 27,390,000.00 USD | 21,570,000.00 USD | 11,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 4,610,000.00 USD | 25,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2437.30` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 1,250,000.00 USD | 531,390.00 USD | 205,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2437.80` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 12,000,000.00 USD | 12,820,000.00 USD | 5,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2440.30` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 1,540,000.00 USD | 1,250,000.00 USD | 479,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2441.10` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 15,080,000.00 USD | 8,120,000.00 USD | 10,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2443.30` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 1,050,000.00 USD | 1,850,000.00 USD | 2,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2444.40` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 8,860,000.00 USD | 15,160,000.00 USD | 14,000,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 130,990.00 USD | 25,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2446.30` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 648,280.00 USD | 347,060.00 USD | 404,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2447.70` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 11,650,000.00 USD | 8,510,000.00 USD | 17,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2449.30` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 408,380.00 USD | 744,230.00 USD | 2,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2451.00` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 16,710,000.00 USD | 14,100,000.00 USD | 16,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2452.30` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 3,750,000.00 USD | 2,920,000.00 USD | 4,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2454.30` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 4,620,000.00 USD | 5,780,000.00 USD | 3,880,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 516,490.00 USD | 26,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2455.30` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 4,310,000.00 USD | 3,050,000.00 USD | 2,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2457.60` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 15,150,000.00 USD | 12,540,000.00 USD | 12,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2458.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 1,900,000.00 USD | 1,790,000.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2460.90` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 5,580,000.00 USD | 8,670,000.00 USD | 6,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2461.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 1,260,000.00 USD | 1,180,000.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2464.20` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 8,720,000.00 USD | 7,700,000.00 USD | 4,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2464.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 619,960.00 USD | 829,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 759,490.00 USD | 27,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2467.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 83,300.00 USD | 68,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2467.50` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 4,540,000.00 USD | 3,710,000.00 USD | 586,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2470.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 1,190,000.00 USD | 391,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2470.80` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 3,960,000.00 USD | 2,290,000.00 USD | 522,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2474.10` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 5,230,000.00 USD | 2,920,000.00 USD | 2,400,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 534,310.00 USD | 27,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2476.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 914,780.00 USD | 28,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2477.40` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 1,660,000.00 USD | 4,420,000.00 USD | 718,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2480.70` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 2,110,000.00 USD | 4,170,000.00 USD | 540,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2482.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 239,600.00 USD | 136,500.00 USD | 43,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2484.00` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 1,210,000.00 USD | 1,390,000.00 USD | 77,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 2,190,000.00 USD | 29,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2485.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 865,140.00 USD | 1,330,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2487.30` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 325,140.00 USD | 262,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2488.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 866,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2490.60` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 2,910,000.00 USD | 2,540,000.00 USD | 279,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2491.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 138,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2493.90` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 1,660,000.00 USD | 1,790,000.00 USD | 3,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2494.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 134,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 4,730,000.00 USD | 34,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2497.20` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 2,940,000.00 USD | 5,270,000.00 USD | 8,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2500.50` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 1,110,000.00 USD | 2,280,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2503.80` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 63,860.00 USD | 1,900,000.00 USD | 125,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 660,180.00 USD | 35,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2506.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 0.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2507.10` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 4,340,000.00 USD | 3,090,000.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2509.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 0.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2510.40` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 2,290,000.00 USD | 1,270,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2512.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 242,080.00 USD | 88,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2513.70` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 98,210.00 USD | 35,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2515.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2517.00` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 97,050.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2520.30` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2521.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 80,610.00 USD | 121,470.00 USD | 110,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2523.60` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2524.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 984,680.00 USD | 537,030.00 USD | 540,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 544,410.00 USD | 35,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2526.90` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2527.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 387,410.00 USD | 362,000.00 USD | 50,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2530.20` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 2,800,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2530.30` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 1,050,000.00 USD | 965,400.00 USD | 437,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2533.30` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 407,340.00 USD | 555,250.00 USD | 436,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2533.50` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 3,530,000.00 USD | 1,850,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2535.00` | 931,980.00 USD | 36,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2536.30` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 1,260,000.00 USD | 698,510.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2536.80` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 3,720,000.00 USD | 3,450,000.00 USD | 3,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2539.30` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 2,370,000.00 USD | 1,090,000.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2540.10` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 4,150,000.00 USD | 3,220,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2542.30` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 1,300,000.00 USD | 1,350,000.00 USD | 218,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2543.40` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 4,150,000.00 USD | 2,520,000.00 USD | 2,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2545.00` | 15,790,000.00 USD | 52,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2545.30` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 1,030,000.00 USD | 336,450.00 USD | 212,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2546.70` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 1,450,000.00 USD | 1,090,000.00 USD | 2,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2548.30` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 2,050,000.00 USD | 1,680,000.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2550.00` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 4,320,000.00 USD | 3,550,000.00 USD | 3,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2551.30` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 1,480,000.00 USD | 1,120,000.00 USD | 698,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2553.30` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 2,820,000.00 USD | 788,360.00 USD | 2,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2554.30` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 1,100,000.00 USD | 228,660.00 USD | 236,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2555.00` | 427,790.00 USD | 53,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2556.60` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 2,760,000.00 USD | 283,560.00 USD | 6,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2557.30` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 717,260.00 USD | 506,330.00 USD | 740,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2559.90` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 5,720,000.00 USD | 2,130,000.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2560.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 2,020,000.00 USD | 1,140,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2563.20` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 1,430,000.00 USD | 2,900,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2563.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 617,040.00 USD | 998,570.00 USD | 984,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2565.00` | 2,460,000.00 USD | 55,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2566.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 172,210.00 USD | 403,100.00 USD | 11,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2566.50` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 1,860,000.00 USD | 1,830,000.00 USD | 3,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2569.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 327,300.00 USD | 119,690.00 USD | 466,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2569.80` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 125,250.00 USD | 341,900.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2572.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 792,480.00 USD | 841,400.00 USD | 16,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2573.10` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2575.00` | 11,610,000.00 USD | 67,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2575.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 546,100.00 USD | 0.00 USD | 502,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2576.40` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 2,400,000.00 USD | 930,280.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2578.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 118,210.00 USD | 31,550.00 USD | 8,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2579.70` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 2,750,000.00 USD | 1,780,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2581.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 450,470.00 USD | 405,480.00 USD | 409,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2583.00` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 1,730,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2583.80` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 411,740.00 USD | 226,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2585.00` | 39,190,000.00 USD | 106,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2586.30` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 1,480,000.00 USD | 2,030,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2589.60` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 3,310,000.00 USD | 631,590.00 USD | 2,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2592.90` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 2,370,000.00 USD | 1,280,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2595.00` | 657,040.00 USD | 106,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2596.20` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 794,750.00 USD | 620,840.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2599.50` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 2,380,000.00 USD | 2,530,000.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2602.80` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 1,680,000.00 USD | 1,260,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2605.00` | 8,050,000.00 USD | 115,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2606.10` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 1,850,000.00 USD | 1,560,000.00 USD | 772,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2609.40` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2612.70` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 1,010,000.00 USD | 643,740.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2615.00` | 6,310,000.00 USD | 121,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2616.00` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2619.30` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 449,020.00 USD | 323,810.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2622.60` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 631,440.00 USD | 1,220,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2625.00` | 377,520.00 USD | 121,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2625.90` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 485,890.00 USD | 474,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2629.20` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 0.00 USD | 20,460.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2632.40` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 0.00 USD | 301,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2635.00` | 101,720.00 USD | 121,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2645.00` | 130,220.00 USD | 121,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2655.00` | 35,830,000.00 USD | 157,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2665.00` | 332,690.00 USD | 158,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2675.00` | 81,960.00 USD | 158,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2685.00` | 907,340.00 USD | 159,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2695.00` | 264,970.00 USD | 159,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2705.00` | 29,490,000.00 USD | 188,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2715.00` | 2,910,000.00 USD | 191,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2725.00` | 1,510,000.00 USD | 193,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2735.00` | 2,000,000.00 USD | 195,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2745.00` | 883,220.00 USD | 196,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2755.00` | 582,750.00 USD | 196,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2765.00` | 2,410,000.00 USD | 199,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2775.00` | 490,200.00 USD | 199,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2785.00` | 1,850,000.00 USD | 201,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2795.00` | 27,520,000.00 USD | 228,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2805.00` | 17,440,000.00 USD | 246,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2815.00` | 343,360.00 USD | 246,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2825.00` | 63,940.00 USD | 246,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2835.00` | 1,520,000.00 USD | 248,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2845.00` | 2,030,000.00 USD | 250,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2855.00` | 858,900.00 USD | 251,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2865.00` | 102,680.00 USD | 251,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2875.00` | 23,120,000.00 USD | 274,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2885.00` | 4,770,000.00 USD | 279,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2895.00` | 356,200.00 USD | 279,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2905.00` | 925,630.00 USD | 280,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2915.00` | 936,420.00 USD | 281,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2925.00` | 4,770.00 USD | 281,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2935.00` | 1,060,000.00 USD | 282,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2945.00` | 800,420.00 USD | 283,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2955.00` | 120,380.00 USD | 283,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2965.00` | 439,680.00 USD | 283,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2975.00` | 445,190.00 USD | 284,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2985.00` | 116,640.00 USD | 284,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2995.00` | 28,900,000.00 USD | 313,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3005.00` | 21,340,000.00 USD | 334,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3015.00` | 311,790.00 USD | 334,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3025.00` | 11,880,000.00 USD | 346,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3035.00` | 6,050,000.00 USD | 352,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3045.00` | 14,030,000.00 USD | 366,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3055.00` | 2,210,000.00 USD | 369,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3065.00` | 6,200,000.00 USD | 375,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3075.00` | 4,910,000.00 USD | 380,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3085.00` | 641,160.00 USD | 380,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3095.00` | 378,770.00 USD | 381,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3105.00` | 1,610,000.00 USD | 382,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3115.00` | 91,040.00 USD | 382,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3125.00` | 435,030.00 USD | 383,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3135.00` | 146,570.00 USD | 383,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3145.00` | 5,960,000.00 USD | 389,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3155.00` | 136,700.00 USD | 389,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3165.00` | 39,870.00 USD | 389,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3175.00` | 665,110.00 USD | 390,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3185.00` | 7,060,000.00 USD | 397,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3195.00` | 7,470,000.00 USD | 404,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3205.00` | 269,580.00 USD | 405,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3215.00` | 559,270.00 USD | 405,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3225.00` | 450,020.00 USD | 406,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3235.00` | 8,650,000.00 USD | 414,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3245.00` | 5,200,000.00 USD | 420,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3255.00` | 49,820.00 USD | 420,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3265.00` | 36,160.00 USD | 420,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3275.00` | 28,270.00 USD | 420,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3285.00` | 9,090,000.00 USD | 429,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3295.00` | 135,520.00 USD | 429,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3305.00` | 1,890,000.00 USD | 431,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3315.00` | 680,260.00 USD | 431,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3325.00` | 5,100,000.00 USD | 437,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3335.00` | 1,250.00 USD | 437,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3345.00` | 63,960,000.00 USD | 501,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3355.00` | 250,060.00 USD | 501,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3365.00` | 443,200.00 USD | 501,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3375.00` | 56,640.00 USD | 501,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3385.00` | 169,370.00 USD | 501,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3395.00` | 22,730.00 USD | 501,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3405.00` | 348,080.00 USD | 502,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3415.00` | 16,120.00 USD | 502,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3425.00` | 14,980,000.00 USD | 517,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3435.00` | 129,440.00 USD | 517,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3445.00` | 353,520.00 USD | 517,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3455.00` | 653,270.00 USD | 518,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3465.00` | 419,220.00 USD | 518,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3475.00` | 314,730.00 USD | 519,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3485.00` | 1,820,000.00 USD | 520,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3495.00` | 1,120,000.00 USD | 522,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3505.00` | 30,560.00 USD | 522,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3515.00` | 100,980.00 USD | 522,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3525.00` | 114,170.00 USD | 522,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3535.00` | 452,410.00 USD | 522,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3545.00` | 322,810.00 USD | 523,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3555.00` | 166,730.00 USD | 523,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3565.00` | 41,050.00 USD | 523,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3575.00` | 259,380.00 USD | 523,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3585.00` | 653,660.00 USD | 524,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3595.00` | 594,390.00 USD | 524,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3605.00` | 451,440.00 USD | 525,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3615.00` | 3,840,000.00 USD | 529,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3625.00` | 561,790.00 USD | 529,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3635.00` | 78,000.00 USD | 529,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3645.00` | 58,500.00 USD | 529,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3655.00` | 6,490,000.00 USD | 536,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3665.00` | 1,080.00 USD | 536,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3675.00` | 345,650.00 USD | 536,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3685.00` | 199,270.00 USD | 536,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3695.00` | 177,010.00 USD | 537,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3705.00` | 91,260.00 USD | 537,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3715.00` | 1,460.00 USD | 537,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3725.00` | 7,730,000.00 USD | 544,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3735.00` | 253,270.00 USD | 545,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3745.00` | 3,140,000.00 USD | 548,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3755.00` | 441,280.00 USD | 548,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3765.00` | 60,370.00 USD | 548,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3775.00` | 1,450,000.00 USD | 550,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3785.00` | 302.04 USD | 550,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3795.00` | 201,250.00 USD | 550,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3805.00` | 1,190,000.00 USD | 551,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3815.00` | 50,430.00 USD | 551,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3825.00` | 15,390,000.00 USD | 567,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3835.00` | 303,210.00 USD | 567,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3845.00` | 6,310.00 USD | 567,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3855.00` | 36,960,000.00 USD | 604,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3865.00` | 2,320,000.00 USD | 606,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3875.00` | 1,150,000.00 USD | 607,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3885.00` | 1,450,000.00 USD | 609,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3895.00` | 754,120.00 USD | 609,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3905.00` | 614,900.00 USD | 610,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3915.00` | 37,820.00 USD | 610,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3925.00` | 167,860.00 USD | 610,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3935.00` | 9,160,000.00 USD | 619,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3945.00` | 1,960,000.00 USD | 621,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3955.00` | 344,680.00 USD | 622,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3965.00` | 422,490,000.00 USD | 1,040,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3975.00` | 638,270.00 USD | 1,050,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3985.00` | 651,130.00 USD | 1,050,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3995.00` | 97,130,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4005.00` | 137,710.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4015.00` | 30,620,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4025.00` | 173,310.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4035.00` | 75,870.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4045.00` | 283,770.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4055.00` | 1,620,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4065.00` | 92,190,000.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4075.00` | 67,510.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4085.00` | 2,950.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4095.00` | 3,610.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4105.00` | 2,860,000.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4115.00` | 2,770,000.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4125.00` | 1,840,000.00 USD | 1,280,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4135.00` | 38,810.00 USD | 1,280,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4145.00` | 69,260,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4155.00` | 1,300,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4165.00` | 119,050.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4175.00` | 74,620.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4185.00` | 912,150.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4195.00` | 4,040,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4205.00` | 474,120.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4215.00` | 134,220.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4225.00` | 426,730.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4235.00` | 1,770.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4245.00` | 183,240.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4255.00` | 7,960.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4265.00` | 54,700.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4275.00` | 3,930,000.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4285.00` | 2,340.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4295.00` | 5,130.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4305.00` | 86,350.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4315.00` | 17,190,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4325.00` | 665,130.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4335.00` | 19,070.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4345.00` | 9,010.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4355.00` | 6,290.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4365.00` | 561,310.00 USD | 1,380,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4375.00` | 183,960.00 USD | 1,380,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4385.00` | 9,140.00 USD | 1,380,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4395.00` | 14,870.00 USD | 1,380,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4405.00` | 27,690.00 USD | 1,380,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4415.00` | 107,920.00 USD | 1,380,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4425.00` | 89,600.00 USD | 1,380,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4435.00` | 3,160,000.00 USD | 1,380,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4445.00` | 400,050.00 USD | 1,380,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4455.00` | 19,610,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4465.00` | 784,700.00 USD | 1,400,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4475.00` | 141,570.00 USD | 1,400,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4485.00` | 1,660,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4495.00` | 157,460.00 USD | 1,400,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4505.00` | 94,780.00 USD | 1,400,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4515.00` | 26,640.00 USD | 1,400,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `465.00` | 845,920,000.00 USD | 0.00 USD | 14,510.00 USD | `-79.39%` | `31.21` |
| `Live` | `Long` | `475.00` | 845,910,000.00 USD | 0.00 USD | 3,720.00 USD | `-78.94%` | `7.83` |
| `Live` | `Long` | `485.00` | 845,900,000.00 USD | 0.00 USD | 43,950.00 USD | `-78.50%` | `90.61` |
| `Live` | `Long` | `495.00` | 845,860,000.00 USD | 0.00 USD | 5,270.00 USD | `-78.06%` | `10.64` |
| `Live` | `Long` | `505.00` | 845,850,000.00 USD | 0.00 USD | 1,810,000.00 USD | `-77.61%` | `3,576.25` |
| `Live` | `Long` | `515.00` | 844,050,000.00 USD | 0.00 USD | 2,140.00 USD | `-77.17%` | `4.15` |
| `Live` | `Long` | `525.00` | 844,050,000.00 USD | 0.00 USD | 10,400.00 USD | `-76.73%` | `19.80` |
| `Live` | `Long` | `535.00` | 844,040,000.00 USD | 0.00 USD | 15,310.00 USD | `-76.28%` | `28.61` |
| `Live` | `Long` | `545.00` | 844,020,000.00 USD | 0.00 USD | 49,430.00 USD | `-75.84%` | `90.69` |
| `Live` | `Long` | `555.00` | 843,970,000.00 USD | 0.00 USD | 174,920.00 USD | `-75.40%` | `315.17` |
| `Live` | `Long` | `565.00` | 843,800,000.00 USD | 0.00 USD | 214.70 USD | `-74.95%` | `0.38` |
| `Live` | `Long` | `575.00` | 843,800,000.00 USD | 0.00 USD | 30,880.00 USD | `-74.51%` | `53.71` |
| `Live` | `Long` | `585.00` | 843,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | `-74.07%` | `3,012.88` |
| `Live` | `Long` | `595.00` | 842,000,000.00 USD | 0.00 USD | 990,010.00 USD | `-73.62%` | `1,663.88` |
| `Live` | `Long` | `605.00` | 841,010,000.00 USD | 0.00 USD | 433,350.00 USD | `-73.18%` | `716.28` |
| `Live` | `Long` | `615.00` | 840,580,000.00 USD | 0.00 USD | 2,450.00 USD | `-72.74%` | `3.98` |
| `Live` | `Long` | `625.00` | 840,580,000.00 USD | 0.00 USD | 17,370.00 USD | `-72.29%` | `27.80` |
| `Live` | `Long` | `635.00` | 840,560,000.00 USD | 0.00 USD | 6,490.00 USD | `-71.85%` | `10.22` |
| `Live` | `Long` | `645.00` | 840,550,000.00 USD | 0.00 USD | 2,780,000.00 USD | `-71.41%` | `4,314.07` |
| `Live` | `Long` | `655.00` | 837,770,000.00 USD | 0.00 USD | 50,740.00 USD | `-70.96%` | `77.46` |
| `Live` | `Long` | `665.00` | 837,720,000.00 USD | 0.00 USD | 26,820.00 USD | `-70.52%` | `40.33` |
| `Live` | `Long` | `675.00` | 837,690,000.00 USD | 0.00 USD | 20,070.00 USD | `-70.08%` | `29.74` |
| `Live` | `Long` | `685.00` | 837,670,000.00 USD | 0.00 USD | 28,680.00 USD | `-69.63%` | `41.87` |
| `Live` | `Long` | `695.00` | 837,640,000.00 USD | 0.00 USD | 668.59 USD | `-69.19%` | `0.96` |
| `Live` | `Long` | `705.00` | 837,640,000.00 USD | 0.00 USD | 32,420.00 USD | `-68.75%` | `45.98` |
| `Live` | `Long` | `715.00` | 837,610,000.00 USD | 0.00 USD | 1,570,000.00 USD | `-68.30%` | `2,194.63` |
| `Live` | `Long` | `725.00` | 836,040,000.00 USD | 0.00 USD | 393,960.00 USD | `-67.86%` | `543.39` |
| `Live` | `Long` | `735.00` | 835,650,000.00 USD | 0.00 USD | 39,690.00 USD | `-67.42%` | `54.01` |
| `Live` | `Long` | `745.00` | 835,610,000.00 USD | 0.00 USD | 2,170.00 USD | `-66.97%` | `2.91` |
| `Live` | `Long` | `755.00` | 835,610,000.00 USD | 0.00 USD | 27,360.00 USD | `-66.53%` | `36.24` |
| `Live` | `Long` | `765.00` | 835,580,000.00 USD | 0.00 USD | 17,180.00 USD | `-66.09%` | `22.46` |
| `Live` | `Long` | `775.00` | 835,560,000.00 USD | 0.00 USD | 58,650.00 USD | `-65.64%` | `75.68` |
| `Live` | `Long` | `785.00` | 835,500,000.00 USD | 0.00 USD | 21,990.00 USD | `-65.20%` | `28.01` |
| `Live` | `Long` | `795.00` | 835,480,000.00 USD | 0.00 USD | 41,860.00 USD | `-64.76%` | `52.66` |
| `Live` | `Long` | `805.00` | 835,440,000.00 USD | 0.00 USD | 56,280.00 USD | `-64.31%` | `69.92` |
| `Live` | `Long` | `815.00` | 835,380,000.00 USD | 0.00 USD | 18,470.00 USD | `-63.87%` | `22.66` |
| `Live` | `Long` | `825.00` | 835,360,000.00 USD | 0.00 USD | 309,280.00 USD | `-63.43%` | `374.89` |
| `Live` | `Long` | `835.00` | 835,050,000.00 USD | 0.00 USD | 22,040.00 USD | `-62.98%` | `26.40` |
| `Live` | `Long` | `845.00` | 835,030,000.00 USD | 0.00 USD | 34,180.00 USD | `-62.54%` | `40.46` |
| `Live` | `Long` | `855.00` | 835,000,000.00 USD | 0.00 USD | 134,590.00 USD | `-62.10%` | `157.42` |
| `Live` | `Long` | `865.00` | 834,860,000.00 USD | 0.00 USD | 455,230.00 USD | `-61.65%` | `526.28` |
| `Live` | `Long` | `875.00` | 834,410,000.00 USD | 0.00 USD | 100,450.00 USD | `-61.21%` | `114.80` |
| `Live` | `Long` | `885.00` | 834,310,000.00 USD | 0.00 USD | 1,010,000.00 USD | `-60.77%` | `1,137.36` |
| `Live` | `Long` | `895.00` | 833,300,000.00 USD | 0.00 USD | 159,890.00 USD | `-60.32%` | `178.65` |
| `Live` | `Long` | `905.00` | 833,140,000.00 USD | 0.00 USD | 67,390.00 USD | `-59.88%` | `74.47` |
| `Live` | `Long` | `915.00` | 833,070,000.00 USD | 0.00 USD | 421,100.00 USD | `-59.44%` | `460.21` |
| `Live` | `Long` | `925.00` | 832,650,000.00 USD | 0.00 USD | 117,910.00 USD | `-58.99%` | `127.47` |
| `Live` | `Long` | `935.00` | 832,530,000.00 USD | 0.00 USD | 41,570.00 USD | `-58.55%` | `44.46` |
| `Live` | `Long` | `945.00` | 832,490,000.00 USD | 0.00 USD | 29,180.00 USD | `-58.11%` | `30.88` |
| `Live` | `Long` | `955.00` | 832,460,000.00 USD | 0.00 USD | 346,950.00 USD | `-57.66%` | `363.30` |
| `Live` | `Long` | `965.00` | 832,120,000.00 USD | 0.00 USD | 158,530.00 USD | `-57.22%` | `164.28` |
| `Live` | `Long` | `975.00` | 831,960,000.00 USD | 0.00 USD | 92,680.00 USD | `-56.78%` | `95.05` |
| `Live` | `Long` | `985.00` | 831,870,000.00 USD | 0.00 USD | 91,750.00 USD | `-56.33%` | `93.15` |
| `Live` | `Long` | `995.00` | 831,770,000.00 USD | 0.00 USD | 19,850.00 USD | `-55.89%` | `19.94` |
| `Live` | `Long` | `1005.00` | 831,750,000.00 USD | 0.00 USD | 33,640.00 USD | `-55.45%` | `33.47` |
| `Live` | `Long` | `1015.00` | 831,720,000.00 USD | 0.00 USD | 58,220.00 USD | `-55.00%` | `57.36` |
| `Live` | `Long` | `1025.00` | 831,660,000.00 USD | 0.00 USD | 131,090.00 USD | `-54.56%` | `127.90` |
| `Live` | `Long` | `1035.00` | 831,530,000.00 USD | 0.00 USD | 213,680.00 USD | `-54.12%` | `206.46` |
| `Live` | `Long` | `1045.00` | 831,320,000.00 USD | 0.00 USD | 7,730,000.00 USD | `-53.67%` | `7,394.22` |
| `Live` | `Long` | `1055.00` | 823,590,000.00 USD | 0.00 USD | 1,540,000.00 USD | `-53.23%` | `1,455.85` |
| `Live` | `Long` | `1065.00` | 822,050,000.00 USD | 0.00 USD | 133,980.00 USD | `-52.79%` | `125.80` |
| `Live` | `Long` | `1075.00` | 821,920,000.00 USD | 0.00 USD | 670,060.00 USD | `-52.35%` | `623.31` |
| `Live` | `Long` | `1085.00` | 821,250,000.00 USD | 0.00 USD | 60,670.00 USD | `-51.90%` | `55.92` |
| `Live` | `Long` | `1095.00` | 821,190,000.00 USD | 0.00 USD | 168,380.00 USD | `-51.46%` | `153.77` |
| `Live` | `Long` | `1105.00` | 821,020,000.00 USD | 0.00 USD | 132,910.00 USD | `-51.02%` | `120.28` |
| `Live` | `Long` | `1115.00` | 820,890,000.00 USD | 0.00 USD | 88,340.00 USD | `-50.57%` | `79.23` |
| `Live` | `Long` | `1125.00` | 820,800,000.00 USD | 0.00 USD | 43,820.00 USD | `-50.13%` | `38.95` |
| `Live` | `Long` | `1135.00` | 820,760,000.00 USD | 0.00 USD | 193,380.00 USD | `-49.69%` | `170.38` |
| `Live` | `Long` | `1145.00` | 820,560,000.00 USD | 0.00 USD | 312,170.00 USD | `-49.24%` | `272.64` |
| `Live` | `Long` | `1155.00` | 820,250,000.00 USD | 0.00 USD | 401,010.00 USD | `-48.80%` | `347.19` |
| `Live` | `Long` | `1165.00` | 819,850,000.00 USD | 0.00 USD | 194,270.00 USD | `-48.36%` | `166.76` |
| `Live` | `Long` | `1175.00` | 819,660,000.00 USD | 0.00 USD | 1,560,000.00 USD | `-47.91%` | `1,324.68` |
| `Live` | `Long` | `1185.00` | 818,100,000.00 USD | 0.00 USD | 159,620.00 USD | `-47.47%` | `134.70` |
| `Live` | `Long` | `1195.00` | 817,940,000.00 USD | 0.00 USD | 452,850.00 USD | `-47.03%` | `378.95` |
| `Live` | `Long` | `1205.00` | 817,490,000.00 USD | 0.00 USD | 242,850.00 USD | `-46.58%` | `201.54` |
| `Live` | `Long` | `1215.00` | 817,240,000.00 USD | 0.00 USD | 287,380.00 USD | `-46.14%` | `236.53` |
| `Live` | `Long` | `1225.00` | 816,960,000.00 USD | 0.00 USD | 2,890,000.00 USD | `-45.70%` | `2,356.53` |
| `Live` | `Long` | `1235.00` | 814,070,000.00 USD | 0.00 USD | 2,680,000.00 USD | `-45.25%` | `2,172.86` |
| `Live` | `Long` | `1245.00` | 811,390,000.00 USD | 0.00 USD | 290,450.00 USD | `-44.81%` | `233.29` |
| `Live` | `Long` | `1255.00` | 811,100,000.00 USD | 0.00 USD | 369,450.00 USD | `-44.37%` | `294.39` |
| `Live` | `Long` | `1265.00` | 810,730,000.00 USD | 0.00 USD | 249,220.00 USD | `-43.92%` | `197.01` |
| `Live` | `Long` | `1275.00` | 810,480,000.00 USD | 0.00 USD | 118,280.00 USD | `-43.48%` | `92.77` |
| `Live` | `Long` | `1285.00` | 810,360,000.00 USD | 0.00 USD | 15,610,000.00 USD | `-43.04%` | `12,144.04` |
| `Live` | `Long` | `1295.00` | 794,750,000.00 USD | 0.00 USD | 271,050.00 USD | `-42.59%` | `209.30` |
| `Live` | `Long` | `1305.00` | 794,480,000.00 USD | 0.00 USD | 257,050.00 USD | `-42.15%` | `196.98` |
| `Live` | `Long` | `1315.00` | 794,230,000.00 USD | 0.00 USD | 580,470.00 USD | `-41.71%` | `441.42` |
| `Live` | `Long` | `1325.00` | 793,650,000.00 USD | 0.00 USD | 1,550,000.00 USD | `-41.26%` | `1,170.96` |
| `Live` | `Long` | `1335.00` | 792,090,000.00 USD | 0.00 USD | 298,460.00 USD | `-40.82%` | `223.57` |
| `Live` | `Long` | `1345.00` | 791,800,000.00 USD | 0.00 USD | 497,840.00 USD | `-40.38%` | `370.14` |
| `Live` | `Long` | `1355.00` | 791,300,000.00 USD | 0.00 USD | 359,190.00 USD | `-39.93%` | `265.09` |
| `Live` | `Long` | `1365.00` | 790,940,000.00 USD | 0.00 USD | 1,070,000.00 USD | `-39.49%` | `785.38` |
| `Live` | `Long` | `1375.00` | 789,870,000.00 USD | 0.00 USD | 12,800,000.00 USD | `-39.05%` | `9,311.32` |
| `Live` | `Long` | `1385.00` | 777,060,000.00 USD | 0.00 USD | 6,970,000.00 USD | `-38.60%` | `5,030.70` |
| `Live` | `Long` | `1395.00` | 770,100,000.00 USD | 0.00 USD | 153,570.00 USD | `-38.16%` | `110.08` |
| `Live` | `Long` | `1405.00` | 769,940,000.00 USD | 0.00 USD | 10,020,000.00 USD | `-37.72%` | `7,128.52` |
| `Live` | `Long` | `1415.00` | 759,930,000.00 USD | 0.00 USD | 1,460,000.00 USD | `-37.27%` | `1,031.29` |
| `Live` | `Long` | `1425.00` | 758,470,000.00 USD | 0.00 USD | 875,640.00 USD | `-36.83%` | `614.48` |
| `Live` | `Long` | `1435.00` | 757,590,000.00 USD | 0.00 USD | 245,420.00 USD | `-36.39%` | `171.03` |
| `Live` | `Long` | `1445.00` | 757,350,000.00 USD | 0.00 USD | 287,790.00 USD | `-35.94%` | `199.16` |
| `Live` | `Long` | `1455.00` | 757,060,000.00 USD | 0.00 USD | 69,520.00 USD | `-35.50%` | `47.78` |
| `Live` | `Long` | `1465.00` | 756,990,000.00 USD | 0.00 USD | 1,190,000.00 USD | `-35.06%` | `813.36` |
| `Live` | `Long` | `1475.00` | 755,800,000.00 USD | 0.00 USD | 5,640,000.00 USD | `-34.61%` | `3,820.96` |
| `Live` | `Long` | `1485.00` | 750,160,000.00 USD | 0.00 USD | 17,690,000.00 USD | `-34.17%` | `11,910.45` |
| `Live` | `Long` | `1495.00` | 732,470,000.00 USD | 0.00 USD | 16,380,000.00 USD | `-33.73%` | `10,956.05` |
| `Live` | `Long` | `1505.00` | 716,090,000.00 USD | 0.00 USD | 137,450.00 USD | `-33.28%` | `91.33` |
| `Live` | `Long` | `1515.00` | 715,960,000.00 USD | 0.00 USD | 15,520,000.00 USD | `-32.84%` | `10,241.44` |
| `Live` | `Long` | `1525.00` | 700,440,000.00 USD | 0.00 USD | 18,750,000.00 USD | `-32.40%` | `12,291.97` |
| `Live` | `Long` | `1535.00` | 681,700,000.00 USD | 0.00 USD | 10,250,000.00 USD | `-31.95%` | `6,677.74` |
| `Live` | `Long` | `1545.00` | 671,450,000.00 USD | 0.00 USD | 3,890,000.00 USD | `-31.51%` | `2,519.70` |
| `Live` | `Long` | `1555.00` | 667,550,000.00 USD | 0.00 USD | 536,530.00 USD | `-31.07%` | `345.03` |
| `Live` | `Long` | `1565.00` | 667,020,000.00 USD | 0.00 USD | 257,330.00 USD | `-30.62%` | `164.43` |
| `Live` | `Long` | `1575.00` | 666,760,000.00 USD | 0.00 USD | 458,760.00 USD | `-30.18%` | `291.28` |
| `Live` | `Long` | `1585.00` | 666,300,000.00 USD | 0.00 USD | 546,140.00 USD | `-29.74%` | `344.57` |
| `Live` | `Long` | `1595.00` | 665,750,000.00 USD | 0.00 USD | 947,400.00 USD | `-29.29%` | `593.98` |
| `Live` | `Long` | `1605.00` | 664,810,000.00 USD | 0.00 USD | 18,700,000.00 USD | `-28.85%` | `11,652.44` |
| `Live` | `Long` | `1615.00` | 646,100,000.00 USD | 0.00 USD | 513,600.00 USD | `-28.41%` | `318.02` |
| `Live` | `Long` | `1625.00` | 645,590,000.00 USD | 0.00 USD | 959,010.00 USD | `-27.96%` | `590.16` |
| `Live` | `Long` | `1635.00` | 644,630,000.00 USD | 0.00 USD | 18,460,000.00 USD | `-27.52%` | `11,292.26` |
| `Live` | `Long` | `1645.00` | 626,170,000.00 USD | 0.00 USD | 36,440,000.00 USD | `-27.08%` | `22,152.48` |
| `Live` | `Long` | `1655.00` | 589,730,000.00 USD | 0.00 USD | 14,670,000.00 USD | `-26.63%` | `8,865.13` |
| `Live` | `Long` | `1665.00` | 575,060,000.00 USD | 0.00 USD | 1,250,000.00 USD | `-26.19%` | `750.55` |
| `Live` | `Long` | `1675.00` | 573,810,000.00 USD | 0.00 USD | 11,600,000.00 USD | `-25.75%` | `6,922.70` |
| `Live` | `Long` | `1685.00` | 562,210,000.00 USD | 0.00 USD | 7,480,000.00 USD | `-25.30%` | `4,439.36` |
| `Live` | `Long` | `1695.00` | 554,730,000.00 USD | 0.00 USD | 878,130.00 USD | `-24.86%` | `518.07` |
| `Live` | `Long` | `1705.00` | 553,850,000.00 USD | 0.00 USD | 29,770,000.00 USD | `-24.42%` | `17,457.89` |
| `Live` | `Long` | `1715.00` | 524,090,000.00 USD | 0.00 USD | 482,750.00 USD | `-23.97%` | `281.49` |
| `Live` | `Long` | `1725.00` | 523,600,000.00 USD | 0.00 USD | 35,080,000.00 USD | `-23.53%` | `20,336.23` |
| `Live` | `Long` | `1735.00` | 488,520,000.00 USD | 0.00 USD | 634,090.00 USD | `-23.09%` | `365.47` |
| `Live` | `Long` | `1745.00` | 487,890,000.00 USD | 0.00 USD | 1,040,000.00 USD | `-22.64%` | `597.70` |
| `Live` | `Long` | `1755.00` | 486,850,000.00 USD | 0.00 USD | 204,030.00 USD | `-22.20%` | `116.25` |
| `Live` | `Long` | `1765.00` | 486,640,000.00 USD | 0.00 USD | 713,160.00 USD | `-21.76%` | `404.06` |
| `Live` | `Long` | `1775.00` | 485,930,000.00 USD | 0.00 USD | 1,200,000.00 USD | `-21.31%` | `674.68` |
| `Live` | `Long` | `1785.00` | 484,730,000.00 USD | 0.00 USD | 54,930,000.00 USD | `-20.87%` | `30,771.35` |
| `Live` | `Long` | `1795.00` | 429,810,000.00 USD | 0.00 USD | 4,280,000.00 USD | `-20.43%` | `2,383.92` |
| `Live` | `Long` | `1805.00` | 425,530,000.00 USD | 0.00 USD | 12,700,000.00 USD | `-19.98%` | `7,035.00` |
| `Live` | `Long` | `1815.00` | 412,830,000.00 USD | 0.00 USD | 2,280,000.00 USD | `-19.54%` | `1,256.57` |
| `Live` | `Long` | `1825.00` | 410,550,000.00 USD | 0.00 USD | 461,220.00 USD | `-19.10%` | `252.72` |
| `Live` | `Long` | `1835.00` | 410,090,000.00 USD | 0.00 USD | 1,750,000.00 USD | `-18.65%` | `954.91` |
| `Live` | `Long` | `1845.00` | 408,330,000.00 USD | 0.00 USD | 847,540.00 USD | `-18.21%` | `459.37` |
| `Live` | `Long` | `1855.00` | 407,490,000.00 USD | 0.00 USD | 2,070,000.00 USD | `-17.77%` | `1,115.41` |
| `Live` | `Long` | `1865.00` | 405,420,000.00 USD | 0.00 USD | 772,330.00 USD | `-17.32%` | `414.12` |
| `Live` | `Long` | `1875.00` | 404,650,000.00 USD | 0.00 USD | 9,890,000.00 USD | `-16.88%` | `5,275.80` |
| `Live` | `Long` | `1885.00` | 394,750,000.00 USD | 0.00 USD | 2,690,000.00 USD | `-16.44%` | `1,426.77` |
| `Live` | `Long` | `1895.00` | 392,060,000.00 USD | 0.00 USD | 6,610,000.00 USD | `-15.99%` | `3,485.52` |
| `Live` | `Long` | `1905.00` | 385,460,000.00 USD | 0.00 USD | 765,450.00 USD | `-15.55%` | `401.81` |
| `Live` | `Long` | `1915.00` | 384,690,000.00 USD | 0.00 USD | 13,520,000.00 USD | `-15.11%` | `7,061.29` |
| `Live` | `Long` | `1925.00` | 371,170,000.00 USD | 0.00 USD | 19,280,000.00 USD | `-14.66%` | `10,015.40` |
| `Live` | `Long` | `1935.00` | 351,890,000.00 USD | 0.00 USD | 1,320,000.00 USD | `-14.22%` | `680.01` |
| `Live` | `Long` | `1945.00` | 350,580,000.00 USD | 0.00 USD | 7,380,000.00 USD | `-13.78%` | `3,792.49` |
| `Live` | `Long` | `1955.00` | 343,200,000.00 USD | 0.00 USD | 1,720,000.00 USD | `-13.33%` | `878.33` |
| `Live` | `Long` | `1965.00` | 341,480,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-12.89%` | `558.81` |
| `Live` | `Long` | `1975.00` | 340,380,000.00 USD | 0.00 USD | 2,900,000.00 USD | `-12.45%` | `1,468.82` |
| `Live` | `Long` | `1985.00` | 337,480,000.00 USD | 0.00 USD | 5,730,000.00 USD | `-12.00%` | `2,888.18` |
| `Live` | `Long` | `1995.00` | 331,750,000.00 USD | 0.00 USD | 9,670,000.00 USD | `-11.56%` | `4,847.47` |
| `Live` | `Long` | `2005.00` | 322,080,000.00 USD | 0.00 USD | 1,540,000.00 USD | `-11.12%` | `767.36` |
| `Live` | `Long` | `2015.00` | 320,540,000.00 USD | 0.00 USD | 2,450,000.00 USD | `-10.67%` | `1,216.74` |
| `Live` | `Long` | `2025.00` | 318,090,000.00 USD | 0.00 USD | 2,210,000.00 USD | `-10.23%` | `1,093.32` |
| `Live` | `Long` | `2035.00` | 315,880,000.00 USD | 0.00 USD | 538,430.00 USD | `-9.79%` | `264.59` |
| `Live` | `Long` | `2045.00` | 315,340,000.00 USD | 0.00 USD | 16,630,000.00 USD | `-9.34%` | `8,133.37` |
| `Live` | `Long` | `2055.00` | 298,700,000.00 USD | 0.00 USD | 13,190,000.00 USD | `-8.90%` | `6,418.25` |
| `Live` | `Long` | `2065.00` | 285,510,000.00 USD | 0.00 USD | 2,230,000.00 USD | `-8.46%` | `1,078.92` |
| `Live` | `Long` | `2075.00` | 283,290,000.00 USD | 0.00 USD | 1,310,000.00 USD | `-8.01%` | `631.42` |
| `Live` | `Long` | `2085.00` | 281,980,000.00 USD | 0.00 USD | 4,940,000.00 USD | `-7.57%` | `2,370.40` |
| `Live` | `Long` | `2095.00` | 277,030,000.00 USD | 0.00 USD | 2,440,000.00 USD | `-7.13%` | `1,163.07` |
| `Live` | `Long` | `2105.00` | 274,600,000.00 USD | 0.00 USD | 1,530,000.00 USD | `-6.68%` | `726.92` |
| `Live` | `Long` | `2115.00` | 273,070,000.00 USD | 0.00 USD | 938,020.00 USD | `-6.24%` | `443.51` |
| `Live` | `Long` | `2125.00` | 272,130,000.00 USD | 0.00 USD | 2,800,000.00 USD | `-5.80%` | `1,315.35` |
| `Live` | `Long` | `2135.00` | 269,330,000.00 USD | 0.00 USD | 4,780,000.00 USD | `-5.36%` | `2,238.90` |
| `Live` | `Long` | `2145.00` | 264,550,000.00 USD | 0.00 USD | 26,580,000.00 USD | `-4.91%` | `12,393.69` |
| `Live` | `Long` | `2155.00` | 237,970,000.00 USD | 0.00 USD | 2,870,000.00 USD | `-4.47%` | `1,330.37` |
| `Live` | `Long` | `2165.00` | 235,100,000.00 USD | 0.00 USD | 1,870,000.00 USD | `-4.03%` | `864.18` |
| `Live` | `Long` | `2175.00` | 233,230,000.00 USD | 0.00 USD | 110,260,000.00 USD | `-3.58%` | `50,693.71` |
| `Live` | `Long` | `2185.00` | 122,970,000.00 USD | 0.00 USD | 101,640,000.00 USD | `-3.14%` | `46,515.50` |
| `Live` | `Long` | `2195.00` | 21,340,000.00 USD | 0.00 USD | 7,900,000.00 USD | `-2.70%` | `3,597.98` |
| `Live` | `Long` | `2205.00` | 13,440,000.00 USD | 0.00 USD | 1,760,000.00 USD | `-2.25%` | `798.27` |
| `Live` | `Long` | `2215.00` | 11,680,000.00 USD | 0.00 USD | 4,410,000.00 USD | `-1.81%` | `1,989.98` |
| `Live` | `Long` | `2225.00` | 7,270,000.00 USD | 0.00 USD | 5,180,000.00 USD | `-1.37%` | `2,328.80` |
| `Live` | `Long` | `2235.00` | 2,090,000.00 USD | 0.00 USD | 1,910,000.00 USD | `-0.92%` | `854.51` |
| `Live` | `Long` | `2245.00` | 179,470.00 USD | 0.00 USD | 160,900.00 USD | `-0.48%` | `71.67` |
| `Live` | `Long` | `2255.00` | 18,560.00 USD | 0.00 USD | 18,560.00 USD | `-0.04%` | `8.23` |
| `Live` | `Short` | `2265.00` | 7,250.00 USD | 7,250.00 USD | 0.00 USD | `+0.41%` | `3.20` |
| `Live` | `Short` | `2275.00` | 55,840.00 USD | 48,600.00 USD | 0.00 USD | `+0.85%` | `21.36` |
| `Live` | `Short` | `2285.00` | 6,280,000.00 USD | 6,220,000.00 USD | 0.00 USD | `+1.29%` | `2,721.88` |
| `Live` | `Short` | `2295.00` | 6,290,000.00 USD | 12,310.00 USD | 0.00 USD | `+1.74%` | `5.37` |
| `Live` | `Short` | `2305.00` | 7,500,000.00 USD | 1,210,000.00 USD | 0.00 USD | `+2.18%` | `524.92` |
| `Live` | `Short` | `2315.00` | 12,220,000.00 USD | 4,720,000.00 USD | 0.00 USD | `+2.62%` | `2,038.34` |
| `Live` | `Short` | `2325.00` | 12,350,000.00 USD | 134,130.00 USD | 0.00 USD | `+3.07%` | `57.69` |
| `Live` | `Short` | `2335.00` | 12,690,000.00 USD | 343,060.00 USD | 0.00 USD | `+3.51%` | `146.92` |
| `Live` | `Short` | `2345.00` | 13,290,000.00 USD | 597,120.00 USD | 0.00 USD | `+3.95%` | `254.63` |
| `Live` | `Short` | `2355.00` | 16,540,000.00 USD | 3,250,000.00 USD | 0.00 USD | `+4.40%` | `1,381.37` |
| `Live` | `Short` | `2365.00` | 16,590,000.00 USD | 47,670.00 USD | 0.00 USD | `+4.84%` | `20.16` |
| `Live` | `Short` | `2375.00` | 17,630,000.00 USD | 1,040,000.00 USD | 0.00 USD | `+5.28%` | `439.24` |
| `Live` | `Short` | `2385.00` | 18,240,000.00 USD | 610,200.00 USD | 0.00 USD | `+5.73%` | `255.85` |
| `Live` | `Short` | `2395.00` | 19,070,000.00 USD | 823,610.00 USD | 0.00 USD | `+6.17%` | `343.89` |
| `Live` | `Short` | `2405.00` | 20,710,000.00 USD | 1,640,000.00 USD | 0.00 USD | `+6.61%` | `683.61` |
| `Live` | `Short` | `2415.00` | 20,760,000.00 USD | 51,630.00 USD | 0.00 USD | `+7.06%` | `21.38` |
| `Live` | `Short` | `2425.00` | 21,100,000.00 USD | 334,040.00 USD | 0.00 USD | `+7.50%` | `137.75` |
| `Live` | `Short` | `2435.00` | 25,710,000.00 USD | 4,610,000.00 USD | 0.00 USD | `+7.94%` | `1,893.84` |
| `Live` | `Short` | `2445.00` | 25,840,000.00 USD | 130,990.00 USD | 0.00 USD | `+8.39%` | `53.57` |
| `Live` | `Short` | `2455.00` | 26,360,000.00 USD | 516,490.00 USD | 0.00 USD | `+8.83%` | `210.38` |
| `Live` | `Short` | `2465.00` | 27,120,000.00 USD | 759,490.00 USD | 0.00 USD | `+9.27%` | `308.11` |
| `Live` | `Short` | `2475.00` | 27,650,000.00 USD | 534,310.00 USD | 0.00 USD | `+9.72%` | `215.88` |
| `Live` | `Short` | `2485.00` | 29,840,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+10.16%` | `880.79` |
| `Live` | `Short` | `2495.00` | 34,570,000.00 USD | 4,730,000.00 USD | 0.00 USD | `+10.60%` | `1,896.93` |
| `Live` | `Short` | `2505.00` | 35,230,000.00 USD | 660,180.00 USD | 0.00 USD | `+11.05%` | `263.54` |
| `Live` | `Short` | `2515.00` | 35,330,000.00 USD | 98,210.00 USD | 0.00 USD | `+11.49%` | `39.05` |
| `Live` | `Short` | `2525.00` | 35,880,000.00 USD | 544,410.00 USD | 0.00 USD | `+11.93%` | `215.61` |
| `Live` | `Short` | `2535.00` | 36,810,000.00 USD | 931,980.00 USD | 0.00 USD | `+12.38%` | `367.64` |
| `Live` | `Short` | `2545.00` | 52,600,000.00 USD | 15,790,000.00 USD | 0.00 USD | `+12.82%` | `6,204.42` |
| `Live` | `Short` | `2555.00` | 53,030,000.00 USD | 427,790.00 USD | 0.00 USD | `+13.26%` | `167.43` |
| `Live` | `Short` | `2565.00` | 55,490,000.00 USD | 2,460,000.00 USD | 0.00 USD | `+13.71%` | `959.39` |
| `Live` | `Short` | `2575.00` | 67,100,000.00 USD | 11,610,000.00 USD | 0.00 USD | `+14.15%` | `4,508.33` |
| `Live` | `Short` | `2585.00` | 106,290,000.00 USD | 39,190,000.00 USD | 0.00 USD | `+14.59%` | `15,161.41` |
| `Live` | `Short` | `2595.00` | 106,940,000.00 USD | 657,040.00 USD | 0.00 USD | `+15.04%` | `253.20` |
| `Live` | `Short` | `2605.00` | 115,000,000.00 USD | 8,050,000.00 USD | 0.00 USD | `+15.48%` | `3,090.59` |
| `Live` | `Short` | `2615.00` | 121,310,000.00 USD | 6,310,000.00 USD | 0.00 USD | `+15.92%` | `2,414.20` |
| `Live` | `Short` | `2625.00` | 121,690,000.00 USD | 377,520.00 USD | 0.00 USD | `+16.37%` | `143.82` |
| `Live` | `Short` | `2635.00` | 121,790,000.00 USD | 101,720.00 USD | 0.00 USD | `+16.81%` | `38.60` |
| `Live` | `Short` | `2645.00` | 121,920,000.00 USD | 130,220.00 USD | 0.00 USD | `+17.25%` | `49.23` |
| `Live` | `Short` | `2655.00` | 157,750,000.00 USD | 35,830,000.00 USD | 0.00 USD | `+17.70%` | `13,494.24` |
| `Live` | `Short` | `2665.00` | 158,080,000.00 USD | 332,690.00 USD | 0.00 USD | `+18.14%` | `124.84` |
| `Live` | `Short` | `2675.00` | 158,160,000.00 USD | 81,960.00 USD | 0.00 USD | `+18.58%` | `30.64` |
| `Live` | `Short` | `2685.00` | 159,070,000.00 USD | 907,340.00 USD | 0.00 USD | `+19.03%` | `337.93` |
| `Live` | `Short` | `2695.00` | 159,330,000.00 USD | 264,970.00 USD | 0.00 USD | `+19.47%` | `98.32` |
| `Live` | `Short` | `2705.00` | 188,820,000.00 USD | 29,490,000.00 USD | 0.00 USD | `+19.91%` | `10,901.03` |
| `Live` | `Short` | `2715.00` | 191,730,000.00 USD | 2,910,000.00 USD | 0.00 USD | `+20.36%` | `1,073.34` |
| `Live` | `Short` | `2725.00` | 193,250,000.00 USD | 1,510,000.00 USD | 0.00 USD | `+20.80%` | `555.22` |
| `Live` | `Short` | `2735.00` | 195,250,000.00 USD | 2,000,000.00 USD | 0.00 USD | `+21.24%` | `731.52` |
| `Live` | `Short` | `2745.00` | 196,130,000.00 USD | 883,220.00 USD | 0.00 USD | `+21.69%` | `321.76` |
| `Live` | `Short` | `2755.00` | 196,710,000.00 USD | 582,750.00 USD | 0.00 USD | `+22.13%` | `211.52` |
| `Live` | `Short` | `2765.00` | 199,130,000.00 USD | 2,410,000.00 USD | 0.00 USD | `+22.57%` | `873.34` |
| `Live` | `Short` | `2775.00` | 199,620,000.00 USD | 490,200.00 USD | 0.00 USD | `+23.02%` | `176.65` |
| `Live` | `Short` | `2785.00` | 201,460,000.00 USD | 1,850,000.00 USD | 0.00 USD | `+23.46%` | `663.04` |
| `Live` | `Short` | `2795.00` | 228,980,000.00 USD | 27,520,000.00 USD | 0.00 USD | `+23.90%` | `9,845.03` |
| `Live` | `Short` | `2805.00` | 246,420,000.00 USD | 17,440,000.00 USD | 0.00 USD | `+24.35%` | `6,216.59` |
| `Live` | `Short` | `2815.00` | 246,760,000.00 USD | 343,360.00 USD | 0.00 USD | `+24.79%` | `121.97` |
| `Live` | `Short` | `2825.00` | 246,830,000.00 USD | 63,940.00 USD | 0.00 USD | `+25.23%` | `22.63` |
| `Live` | `Short` | `2835.00` | 248,350,000.00 USD | 1,520,000.00 USD | 0.00 USD | `+25.68%` | `537.76` |
| `Live` | `Short` | `2845.00` | 250,380,000.00 USD | 2,030,000.00 USD | 0.00 USD | `+26.12%` | `713.07` |
| `Live` | `Short` | `2855.00` | 251,240,000.00 USD | 858,900.00 USD | 0.00 USD | `+26.56%` | `300.84` |
| `Live` | `Short` | `2865.00` | 251,340,000.00 USD | 102,680.00 USD | 0.00 USD | `+27.01%` | `35.84` |
| `Live` | `Short` | `2875.00` | 274,460,000.00 USD | 23,120,000.00 USD | 0.00 USD | `+27.45%` | `8,040.72` |
| `Live` | `Short` | `2885.00` | 279,230,000.00 USD | 4,770,000.00 USD | 0.00 USD | `+27.89%` | `1,652.91` |
| `Live` | `Short` | `2895.00` | 279,580,000.00 USD | 356,200.00 USD | 0.00 USD | `+28.34%` | `123.04` |
| `Live` | `Short` | `2905.00` | 280,510,000.00 USD | 925,630.00 USD | 0.00 USD | `+28.78%` | `318.63` |
| `Live` | `Short` | `2915.00` | 281,450,000.00 USD | 936,420.00 USD | 0.00 USD | `+29.22%` | `321.24` |
| `Live` | `Short` | `2925.00` | 281,450,000.00 USD | 4,770.00 USD | 0.00 USD | `+29.67%` | `1.63` |
| `Live` | `Short` | `2935.00` | 282,510,000.00 USD | 1,060,000.00 USD | 0.00 USD | `+30.11%` | `360.71` |
| `Live` | `Short` | `2945.00` | 283,310,000.00 USD | 800,420.00 USD | 0.00 USD | `+30.55%` | `271.79` |
| `Live` | `Short` | `2955.00` | 283,430,000.00 USD | 120,380.00 USD | 0.00 USD | `+31.00%` | `40.74` |
| `Live` | `Short` | `2965.00` | 283,870,000.00 USD | 439,680.00 USD | 0.00 USD | `+31.44%` | `148.29` |
| `Live` | `Short` | `2975.00` | 284,310,000.00 USD | 445,190.00 USD | 0.00 USD | `+31.88%` | `149.64` |
| `Live` | `Short` | `2985.00` | 284,430,000.00 USD | 116,640.00 USD | 0.00 USD | `+32.33%` | `39.08` |
| `Live` | `Short` | `2995.00` | 313,330,000.00 USD | 28,900,000.00 USD | 0.00 USD | `+32.77%` | `9,648.62` |
| `Live` | `Short` | `3005.00` | 334,670,000.00 USD | 21,340,000.00 USD | 0.00 USD | `+33.21%` | `7,102.73` |
| `Live` | `Short` | `3015.00` | 334,980,000.00 USD | 311,790.00 USD | 0.00 USD | `+33.66%` | `103.41` |
| `Live` | `Short` | `3025.00` | 346,860,000.00 USD | 11,880,000.00 USD | 0.00 USD | `+34.10%` | `3,926.17` |
| `Live` | `Short` | `3035.00` | 352,910,000.00 USD | 6,050,000.00 USD | 0.00 USD | `+34.54%` | `1,993.91` |
| `Live` | `Short` | `3045.00` | 366,940,000.00 USD | 14,030,000.00 USD | 0.00 USD | `+34.99%` | `4,607.22` |
| `Live` | `Short` | `3055.00` | 369,150,000.00 USD | 2,210,000.00 USD | 0.00 USD | `+35.43%` | `723.11` |
| `Live` | `Short` | `3065.00` | 375,350,000.00 USD | 6,200,000.00 USD | 0.00 USD | `+35.87%` | `2,022.57` |
| `Live` | `Short` | `3075.00` | 380,260,000.00 USD | 4,910,000.00 USD | 0.00 USD | `+36.32%` | `1,595.66` |
| `Live` | `Short` | `3085.00` | 380,900,000.00 USD | 641,160.00 USD | 0.00 USD | `+36.76%` | `207.83` |
| `Live` | `Short` | `3095.00` | 381,280,000.00 USD | 378,770.00 USD | 0.00 USD | `+37.20%` | `122.38` |
| `Live` | `Short` | `3105.00` | 382,890,000.00 USD | 1,610,000.00 USD | 0.00 USD | `+37.65%` | `519.79` |
| `Live` | `Short` | `3115.00` | 382,980,000.00 USD | 91,040.00 USD | 0.00 USD | `+38.09%` | `29.23` |
| `Live` | `Short` | `3125.00` | 383,420,000.00 USD | 435,030.00 USD | 0.00 USD | `+38.53%` | `139.21` |
| `Live` | `Short` | `3135.00` | 383,560,000.00 USD | 146,570.00 USD | 0.00 USD | `+38.98%` | `46.75` |
| `Live` | `Short` | `3145.00` | 389,520,000.00 USD | 5,960,000.00 USD | 0.00 USD | `+39.42%` | `1,895.12` |
| `Live` | `Short` | `3155.00` | 389,660,000.00 USD | 136,700.00 USD | 0.00 USD | `+39.86%` | `43.33` |
| `Live` | `Short` | `3165.00` | 389,700,000.00 USD | 39,870.00 USD | 0.00 USD | `+40.30%` | `12.60` |
| `Live` | `Short` | `3175.00` | 390,360,000.00 USD | 665,110.00 USD | 0.00 USD | `+40.75%` | `209.48` |
| `Live` | `Short` | `3185.00` | 397,430,000.00 USD | 7,060,000.00 USD | 0.00 USD | `+41.19%` | `2,217.05` |
| `Live` | `Short` | `3195.00` | 404,900,000.00 USD | 7,470,000.00 USD | 0.00 USD | `+41.63%` | `2,338.12` |
| `Live` | `Short` | `3205.00` | 405,170,000.00 USD | 269,580.00 USD | 0.00 USD | `+42.08%` | `84.11` |
| `Live` | `Short` | `3215.00` | 405,720,000.00 USD | 559,270.00 USD | 0.00 USD | `+42.52%` | `173.96` |
| `Live` | `Short` | `3225.00` | 406,180,000.00 USD | 450,020.00 USD | 0.00 USD | `+42.96%` | `139.54` |
| `Live` | `Short` | `3235.00` | 414,830,000.00 USD | 8,650,000.00 USD | 0.00 USD | `+43.41%` | `2,674.68` |
| `Live` | `Short` | `3245.00` | 420,030,000.00 USD | 5,200,000.00 USD | 0.00 USD | `+43.85%` | `1,602.01` |
| `Live` | `Short` | `3255.00` | 420,080,000.00 USD | 49,820.00 USD | 0.00 USD | `+44.29%` | `15.31` |
| `Live` | `Short` | `3265.00` | 420,110,000.00 USD | 36,160.00 USD | 0.00 USD | `+44.74%` | `11.07` |
| `Live` | `Short` | `3275.00` | 420,140,000.00 USD | 28,270.00 USD | 0.00 USD | `+45.18%` | `8.63` |
| `Live` | `Short` | `3285.00` | 429,230,000.00 USD | 9,090,000.00 USD | 0.00 USD | `+45.62%` | `2,766.81` |
| `Live` | `Short` | `3295.00` | 429,360,000.00 USD | 135,520.00 USD | 0.00 USD | `+46.07%` | `41.13` |
| `Live` | `Short` | `3305.00` | 431,250,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+46.51%` | `571.69` |
| `Live` | `Short` | `3315.00` | 431,930,000.00 USD | 680,260.00 USD | 0.00 USD | `+46.95%` | `205.21` |
| `Live` | `Short` | `3325.00` | 437,040,000.00 USD | 5,100,000.00 USD | 0.00 USD | `+47.40%` | `1,535.33` |
| `Live` | `Short` | `3335.00` | 437,040,000.00 USD | 1,250.00 USD | 0.00 USD | `+47.84%` | `0.37` |
| `Live` | `Short` | `3345.00` | 501,000,000.00 USD | 63,960,000.00 USD | 0.00 USD | `+48.28%` | `19,119.85` |
| `Live` | `Short` | `3355.00` | 501,250,000.00 USD | 250,060.00 USD | 0.00 USD | `+48.73%` | `74.53` |
| `Live` | `Short` | `3365.00` | 501,690,000.00 USD | 443,200.00 USD | 0.00 USD | `+49.17%` | `131.71` |
| `Live` | `Short` | `3375.00` | 501,750,000.00 USD | 56,640.00 USD | 0.00 USD | `+49.61%` | `16.78` |
| `Live` | `Short` | `3385.00` | 501,920,000.00 USD | 169,370.00 USD | 0.00 USD | `+50.06%` | `50.04` |
| `Live` | `Short` | `3395.00` | 501,940,000.00 USD | 22,730.00 USD | 0.00 USD | `+50.50%` | `6.69` |
| `Live` | `Short` | `3405.00` | 502,290,000.00 USD | 348,080.00 USD | 0.00 USD | `+50.94%` | `102.23` |
| `Live` | `Short` | `3415.00` | 502,300,000.00 USD | 16,120.00 USD | 0.00 USD | `+51.39%` | `4.72` |
| `Live` | `Short` | `3425.00` | 517,280,000.00 USD | 14,980,000.00 USD | 0.00 USD | `+51.83%` | `4,374.35` |
| `Live` | `Short` | `3435.00` | 517,410,000.00 USD | 129,440.00 USD | 0.00 USD | `+52.27%` | `37.68` |
| `Live` | `Short` | `3445.00` | 517,770,000.00 USD | 353,520.00 USD | 0.00 USD | `+52.72%` | `102.62` |
| `Live` | `Short` | `3455.00` | 518,420,000.00 USD | 653,270.00 USD | 0.00 USD | `+53.16%` | `189.08` |
| `Live` | `Short` | `3465.00` | 518,840,000.00 USD | 419,220.00 USD | 0.00 USD | `+53.60%` | `120.99` |
| `Live` | `Short` | `3475.00` | 519,160,000.00 USD | 314,730.00 USD | 0.00 USD | `+54.05%` | `90.57` |
| `Live` | `Short` | `3485.00` | 520,980,000.00 USD | 1,820,000.00 USD | 0.00 USD | `+54.49%` | `522.47` |
| `Live` | `Short` | `3495.00` | 522,100,000.00 USD | 1,120,000.00 USD | 0.00 USD | `+54.93%` | `320.37` |
| `Live` | `Short` | `3505.00` | 522,130,000.00 USD | 30,560.00 USD | 0.00 USD | `+55.38%` | `8.72` |
| `Live` | `Short` | `3515.00` | 522,230,000.00 USD | 100,980.00 USD | 0.00 USD | `+55.82%` | `28.73` |
| `Live` | `Short` | `3525.00` | 522,340,000.00 USD | 114,170.00 USD | 0.00 USD | `+56.26%` | `32.39` |
| `Live` | `Short` | `3535.00` | 522,790,000.00 USD | 452,410.00 USD | 0.00 USD | `+56.71%` | `127.98` |
| `Live` | `Short` | `3545.00` | 523,120,000.00 USD | 322,810.00 USD | 0.00 USD | `+57.15%` | `91.06` |
| `Live` | `Short` | `3555.00` | 523,280,000.00 USD | 166,730.00 USD | 0.00 USD | `+57.59%` | `46.90` |
| `Live` | `Short` | `3565.00` | 523,320,000.00 USD | 41,050.00 USD | 0.00 USD | `+58.04%` | `11.51` |
| `Live` | `Short` | `3575.00` | 523,580,000.00 USD | 259,380.00 USD | 0.00 USD | `+58.48%` | `72.55` |
| `Live` | `Short` | `3585.00` | 524,240,000.00 USD | 653,660.00 USD | 0.00 USD | `+58.92%` | `182.33` |
| `Live` | `Short` | `3595.00` | 524,830,000.00 USD | 594,390.00 USD | 0.00 USD | `+59.37%` | `165.34` |
| `Live` | `Short` | `3605.00` | 525,280,000.00 USD | 451,440.00 USD | 0.00 USD | `+59.81%` | `125.23` |
| `Live` | `Short` | `3615.00` | 529,120,000.00 USD | 3,840,000.00 USD | 0.00 USD | `+60.25%` | `1,061.91` |
| `Live` | `Short` | `3625.00` | 529,680,000.00 USD | 561,790.00 USD | 0.00 USD | `+60.70%` | `154.98` |
| `Live` | `Short` | `3635.00` | 529,760,000.00 USD | 78,000.00 USD | 0.00 USD | `+61.14%` | `21.46` |
| `Live` | `Short` | `3645.00` | 529,820,000.00 USD | 58,500.00 USD | 0.00 USD | `+61.58%` | `16.05` |
| `Live` | `Short` | `3655.00` | 536,310,000.00 USD | 6,490,000.00 USD | 0.00 USD | `+62.03%` | `1,774.53` |
| `Live` | `Short` | `3665.00` | 536,310,000.00 USD | 1,080.00 USD | 0.00 USD | `+62.47%` | `0.30` |
| `Live` | `Short` | `3675.00` | 536,650,000.00 USD | 345,650.00 USD | 0.00 USD | `+62.91%` | `94.05` |
| `Live` | `Short` | `3685.00` | 536,850,000.00 USD | 199,270.00 USD | 0.00 USD | `+63.36%` | `54.08` |
| `Live` | `Short` | `3695.00` | 537,030,000.00 USD | 177,010.00 USD | 0.00 USD | `+63.80%` | `47.90` |
| `Live` | `Short` | `3705.00` | 537,120,000.00 USD | 91,260.00 USD | 0.00 USD | `+64.24%` | `24.63` |
| `Live` | `Short` | `3715.00` | 537,120,000.00 USD | 1,460.00 USD | 0.00 USD | `+64.69%` | `0.39` |
| `Live` | `Short` | `3725.00` | 544,860,000.00 USD | 7,730,000.00 USD | 0.00 USD | `+65.13%` | `2,076.21` |
| `Live` | `Short` | `3735.00` | 545,110,000.00 USD | 253,270.00 USD | 0.00 USD | `+65.57%` | `67.81` |
| `Live` | `Short` | `3745.00` | 548,250,000.00 USD | 3,140,000.00 USD | 0.00 USD | `+66.02%` | `838.14` |
| `Live` | `Short` | `3755.00` | 548,690,000.00 USD | 441,280.00 USD | 0.00 USD | `+66.46%` | `117.52` |
| `Live` | `Short` | `3765.00` | 548,750,000.00 USD | 60,370.00 USD | 0.00 USD | `+66.90%` | `16.03` |
| `Live` | `Short` | `3775.00` | 550,200,000.00 USD | 1,450,000.00 USD | 0.00 USD | `+67.35%` | `385.10` |
| `Live` | `Short` | `3785.00` | 550,200,000.00 USD | 302.04 USD | 0.00 USD | `+67.79%` | `0.08` |
| `Live` | `Short` | `3795.00` | 550,400,000.00 USD | 201,250.00 USD | 0.00 USD | `+68.23%` | `53.03` |
| `Live` | `Short` | `3805.00` | 551,600,000.00 USD | 1,190,000.00 USD | 0.00 USD | `+68.68%` | `313.97` |
| `Live` | `Short` | `3815.00` | 551,650,000.00 USD | 50,430.00 USD | 0.00 USD | `+69.12%` | `13.22` |
| `Live` | `Short` | `3825.00` | 567,040,000.00 USD | 15,390,000.00 USD | 0.00 USD | `+69.56%` | `4,023.96` |
| `Live` | `Short` | `3835.00` | 567,340,000.00 USD | 303,210.00 USD | 0.00 USD | `+70.01%` | `79.06` |
| `Live` | `Short` | `3845.00` | 567,350,000.00 USD | 6,310.00 USD | 0.00 USD | `+70.45%` | `1.64` |
| `Live` | `Short` | `3855.00` | 604,310,000.00 USD | 36,960,000.00 USD | 0.00 USD | `+70.89%` | `9,587.09` |
| `Live` | `Short` | `3865.00` | 606,630,000.00 USD | 2,320,000.00 USD | 0.00 USD | `+71.34%` | `599.82` |
| `Live` | `Short` | `3875.00` | 607,770,000.00 USD | 1,150,000.00 USD | 0.00 USD | `+71.78%` | `295.65` |
| `Live` | `Short` | `3885.00` | 609,220,000.00 USD | 1,450,000.00 USD | 0.00 USD | `+72.22%` | `371.95` |
| `Live` | `Short` | `3895.00` | 609,970,000.00 USD | 754,120.00 USD | 0.00 USD | `+72.67%` | `193.61` |
| `Live` | `Short` | `3905.00` | 610,590,000.00 USD | 614,900.00 USD | 0.00 USD | `+73.11%` | `157.46` |
| `Live` | `Short` | `3915.00` | 610,630,000.00 USD | 37,820.00 USD | 0.00 USD | `+73.55%` | `9.66` |
| `Live` | `Short` | `3925.00` | 610,790,000.00 USD | 167,860.00 USD | 0.00 USD | `+74.00%` | `42.77` |
| `Live` | `Short` | `3935.00` | 619,950,000.00 USD | 9,160,000.00 USD | 0.00 USD | `+74.44%` | `2,326.65` |
| `Live` | `Short` | `3945.00` | 621,910,000.00 USD | 1,960,000.00 USD | 0.00 USD | `+74.88%` | `497.84` |
| `Live` | `Short` | `3955.00` | 622,260,000.00 USD | 344,680.00 USD | 0.00 USD | `+75.33%` | `87.15` |
| `Live` | `Short` | `3965.00` | 1,040,000,000.00 USD | 422,490,000.00 USD | 0.00 USD | `+75.77%` | `106,554.48` |
| `Live` | `Short` | `3975.00` | 1,050,000,000.00 USD | 638,270.00 USD | 0.00 USD | `+76.21%` | `160.57` |
| `Live` | `Short` | `3985.00` | 1,050,000,000.00 USD | 651,130.00 USD | 0.00 USD | `+76.66%` | `163.39` |
| `Live` | `Short` | `3995.00` | 1,140,000,000.00 USD | 97,130,000.00 USD | 0.00 USD | `+77.10%` | `24,311.92` |
| `Live` | `Short` | `4005.00` | 1,140,000,000.00 USD | 137,710.00 USD | 0.00 USD | `+77.54%` | `34.38` |
| `Live` | `Short` | `4015.00` | 1,170,000,000.00 USD | 30,620,000.00 USD | 0.00 USD | `+77.99%` | `7,625.56` |
| `Live` | `Short` | `4025.00` | 1,170,000,000.00 USD | 173,310.00 USD | 0.00 USD | `+78.43%` | `43.06` |
| `Live` | `Short` | `4035.00` | 1,170,000,000.00 USD | 75,870.00 USD | 0.00 USD | `+78.87%` | `18.80` |
| `Live` | `Short` | `4045.00` | 1,170,000,000.00 USD | 283,770.00 USD | 0.00 USD | `+79.32%` | `70.15` |
| `Live` | `Short` | `4055.00` | 1,180,000,000.00 USD | 1,620,000.00 USD | 0.00 USD | `+79.76%` | `398.54` |
| `Live` | `Short` | `4065.00` | 1,270,000,000.00 USD | 92,190,000.00 USD | 0.00 USD | `+80.20%` | `22,679.74` |
| `Live` | `Short` | `4075.00` | 1,270,000,000.00 USD | 67,510.00 USD | 0.00 USD | `+80.65%` | `16.57` |
| `Live` | `Short` | `4085.00` | 1,270,000,000.00 USD | 2,950.00 USD | 0.00 USD | `+81.09%` | `0.72` |
| `Live` | `Short` | `4095.00` | 1,270,000,000.00 USD | 3,610.00 USD | 0.00 USD | `+81.53%` | `0.88` |
| `Live` | `Short` | `4105.00` | 1,270,000,000.00 USD | 2,860,000.00 USD | 0.00 USD | `+81.98%` | `696.12` |
| `Live` | `Short` | `4115.00` | 1,270,000,000.00 USD | 2,770,000.00 USD | 0.00 USD | `+82.42%` | `672.00` |
| `Live` | `Short` | `4125.00` | 1,280,000,000.00 USD | 1,840,000.00 USD | 0.00 USD | `+82.86%` | `446.26` |
| `Live` | `Short` | `4135.00` | 1,280,000,000.00 USD | 38,810.00 USD | 0.00 USD | `+83.31%` | `9.39` |
| `Live` | `Short` | `4145.00` | 1,350,000,000.00 USD | 69,260,000.00 USD | 0.00 USD | `+83.75%` | `16,709.46` |
| `Live` | `Short` | `4155.00` | 1,350,000,000.00 USD | 1,300,000.00 USD | 0.00 USD | `+84.19%` | `312.39` |
| `Live` | `Short` | `4165.00` | 1,350,000,000.00 USD | 119,050.00 USD | 0.00 USD | `+84.64%` | `28.58` |
| `Live` | `Short` | `4175.00` | 1,350,000,000.00 USD | 74,620.00 USD | 0.00 USD | `+85.08%` | `17.87` |
| `Live` | `Short` | `4185.00` | 1,350,000,000.00 USD | 912,150.00 USD | 0.00 USD | `+85.52%` | `217.96` |
| `Live` | `Short` | `4195.00` | 1,350,000,000.00 USD | 4,040,000.00 USD | 0.00 USD | `+85.97%` | `962.89` |
| `Live` | `Short` | `4205.00` | 1,350,000,000.00 USD | 474,120.00 USD | 0.00 USD | `+86.41%` | `112.75` |
| `Live` | `Short` | `4215.00` | 1,350,000,000.00 USD | 134,220.00 USD | 0.00 USD | `+86.85%` | `31.84` |
| `Live` | `Short` | `4225.00` | 1,350,000,000.00 USD | 426,730.00 USD | 0.00 USD | `+87.29%` | `101.00` |
| `Live` | `Short` | `4235.00` | 1,350,000,000.00 USD | 1,770.00 USD | 0.00 USD | `+87.74%` | `0.42` |
| `Live` | `Short` | `4245.00` | 1,350,000,000.00 USD | 183,240.00 USD | 0.00 USD | `+88.18%` | `43.16` |
| `Live` | `Short` | `4255.00` | 1,350,000,000.00 USD | 7,960.00 USD | 0.00 USD | `+88.62%` | `1.87` |
| `Live` | `Short` | `4265.00` | 1,350,000,000.00 USD | 54,700.00 USD | 0.00 USD | `+89.07%` | `12.83` |
| `Live` | `Short` | `4275.00` | 1,360,000,000.00 USD | 3,930,000.00 USD | 0.00 USD | `+89.51%` | `919.98` |
| `Live` | `Short` | `4285.00` | 1,360,000,000.00 USD | 2,340.00 USD | 0.00 USD | `+89.95%` | `0.55` |
| `Live` | `Short` | `4295.00` | 1,360,000,000.00 USD | 5,130.00 USD | 0.00 USD | `+90.40%` | `1.20` |
| `Live` | `Short` | `4305.00` | 1,360,000,000.00 USD | 86,350.00 USD | 0.00 USD | `+90.84%` | `20.06` |
| `Live` | `Short` | `4315.00` | 1,370,000,000.00 USD | 17,190,000.00 USD | 0.00 USD | `+91.28%` | `3,983.61` |
| `Live` | `Short` | `4325.00` | 1,370,000,000.00 USD | 665,130.00 USD | 0.00 USD | `+91.73%` | `153.79` |
| `Live` | `Short` | `4335.00` | 1,370,000,000.00 USD | 19,070.00 USD | 0.00 USD | `+92.17%` | `4.40` |
| `Live` | `Short` | `4345.00` | 1,370,000,000.00 USD | 9,010.00 USD | 0.00 USD | `+92.61%` | `2.07` |
| `Live` | `Short` | `4355.00` | 1,370,000,000.00 USD | 6,290.00 USD | 0.00 USD | `+93.06%` | `1.45` |
| `Live` | `Short` | `4365.00` | 1,380,000,000.00 USD | 561,310.00 USD | 0.00 USD | `+93.50%` | `128.59` |
| `Live` | `Short` | `4375.00` | 1,380,000,000.00 USD | 183,960.00 USD | 0.00 USD | `+93.94%` | `42.05` |
| `Live` | `Short` | `4385.00` | 1,380,000,000.00 USD | 9,140.00 USD | 0.00 USD | `+94.39%` | `2.08` |
| `Live` | `Short` | `4395.00` | 1,380,000,000.00 USD | 14,870.00 USD | 0.00 USD | `+94.83%` | `3.38` |
| `Live` | `Short` | `4405.00` | 1,380,000,000.00 USD | 27,690.00 USD | 0.00 USD | `+95.27%` | `6.29` |
| `Live` | `Short` | `4415.00` | 1,380,000,000.00 USD | 107,920.00 USD | 0.00 USD | `+95.72%` | `24.44` |
| `Live` | `Short` | `4425.00` | 1,380,000,000.00 USD | 89,600.00 USD | 0.00 USD | `+96.16%` | `20.25` |
| `Live` | `Short` | `4435.00` | 1,380,000,000.00 USD | 3,160,000.00 USD | 0.00 USD | `+96.60%` | `712.58` |
| `Live` | `Short` | `4445.00` | 1,380,000,000.00 USD | 400,050.00 USD | 0.00 USD | `+97.05%` | `90.00` |
| `Live` | `Short` | `4455.00` | 1,400,000,000.00 USD | 19,610,000.00 USD | 0.00 USD | `+97.49%` | `4,402.58` |
| `Live` | `Short` | `4465.00` | 1,400,000,000.00 USD | 784,700.00 USD | 0.00 USD | `+97.93%` | `175.74` |
| `Live` | `Short` | `4475.00` | 1,400,000,000.00 USD | 141,570.00 USD | 0.00 USD | `+98.38%` | `31.64` |
| `Live` | `Short` | `4485.00` | 1,400,000,000.00 USD | 1,660,000.00 USD | 0.00 USD | `+98.82%` | `370.90` |
| `Live` | `Short` | `4495.00` | 1,400,000,000.00 USD | 157,460.00 USD | 0.00 USD | `+99.26%` | `35.03` |
| `Live` | `Short` | `4505.00` | 1,400,000,000.00 USD | 94,780.00 USD | 0.00 USD | `+99.71%` | `21.04` |
| `Live` | `Short` | `4515.00` | 1,400,000,000.00 USD | 26,640.00 USD | 0.00 USD | `+100.15%` | `5.90` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `505.00` | 64,070,000.00 USD | 0.00 USD | 16,090.00 USD | `-77.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.00` | 64,050,000.00 USD | 0.00 USD | 563.16 USD | `-75.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.00` | 64,050,000.00 USD | 0.00 USD | 885.90 USD | `-68.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `755.00` | 64,050,000.00 USD | 0.00 USD | 177.27 USD | `-66.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `795.00` | 64,050,000.00 USD | 0.00 USD | 104.22 USD | `-64.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `805.00` | 64,050,000.00 USD | 0.00 USD | 2,090.00 USD | `-64.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `835.00` | 64,050,000.00 USD | 0.00 USD | 1,670.00 USD | `-62.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `865.00` | 64,050,000.00 USD | 0.00 USD | 139,280.00 USD | `-61.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `885.00` | 63,910,000.00 USD | 0.00 USD | 3,130.00 USD | `-60.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `905.00` | 63,900,000.00 USD | 0.00 USD | 2,780.00 USD | `-59.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `985.00` | 63,900,000.00 USD | 0.00 USD | 516.34 USD | `-56.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `995.00` | 63,900,000.00 USD | 0.00 USD | 100.50 USD | `-55.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1005.00` | 63,900,000.00 USD | 0.00 USD | 222,040.00 USD | `-55.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1015.00` | 63,680,000.00 USD | 0.00 USD | 438.28 USD | `-55.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1025.00` | 63,680,000.00 USD | 0.00 USD | 112.03 USD | `-54.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1065.00` | 63,680,000.00 USD | 0.00 USD | 1,060.00 USD | `-52.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1075.00` | 63,680,000.00 USD | 0.00 USD | 995.34 USD | `-52.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1105.00` | 63,680,000.00 USD | 0.00 USD | 1,610.00 USD | `-51.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1115.00` | 63,670,000.00 USD | 0.00 USD | 11,050.00 USD | `-50.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1125.00` | 63,660,000.00 USD | 0.00 USD | 1,320.00 USD | `-50.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1155.00` | 63,660,000.00 USD | 0.00 USD | 1,000.00 USD | `-48.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1175.00` | 63,660,000.00 USD | 0.00 USD | 203.98 USD | `-47.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1185.00` | 63,660,000.00 USD | 0.00 USD | 228.47 USD | `-47.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1205.00` | 63,660,000.00 USD | 0.00 USD | 3,110.00 USD | `-46.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1225.00` | 63,660,000.00 USD | 0.00 USD | 995.93 USD | `-45.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1245.00` | 63,660,000.00 USD | 0.00 USD | 951.93 USD | `-44.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1255.00` | 63,660,000.00 USD | 0.00 USD | 6,810.00 USD | `-44.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1285.00` | 63,650,000.00 USD | 0.00 USD | 9,050.00 USD | `-43.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1295.00` | 63,640,000.00 USD | 0.00 USD | 7,030.00 USD | `-42.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1305.00` | 63,630,000.00 USD | 0.00 USD | 23,030.00 USD | `-42.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1315.00` | 63,610,000.00 USD | 0.00 USD | 1,440.00 USD | `-41.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1345.00` | 63,610,000.00 USD | 0.00 USD | 141,950.00 USD | `-40.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1355.00` | 63,470,000.00 USD | 0.00 USD | 128.86 USD | `-39.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1365.00` | 63,470,000.00 USD | 0.00 USD | 1,270.00 USD | `-39.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1375.00` | 63,460,000.00 USD | 0.00 USD | 4,160.00 USD | `-39.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1395.00` | 63,460,000.00 USD | 0.00 USD | 535,600.00 USD | `-38.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1405.00` | 62,920,000.00 USD | 0.00 USD | 20,270.00 USD | `-37.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1425.00` | 62,900,000.00 USD | 0.00 USD | 6,450.00 USD | `-36.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1435.00` | 62,900,000.00 USD | 0.00 USD | 852.10 USD | `-36.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1445.00` | 62,900,000.00 USD | 0.00 USD | 1,490.00 USD | `-35.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1455.00` | 62,900,000.00 USD | 0.00 USD | 5,680.00 USD | `-35.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1465.00` | 62,890,000.00 USD | 0.00 USD | 19,460.00 USD | `-35.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1475.00` | 62,870,000.00 USD | 0.00 USD | 2,600.00 USD | `-34.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1485.00` | 62,870,000.00 USD | 0.00 USD | 18,710.00 USD | `-34.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1495.00` | 62,850,000.00 USD | 0.00 USD | 11,570.00 USD | `-33.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1505.00` | 62,840,000.00 USD | 0.00 USD | 89,400.00 USD | `-33.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1515.00` | 62,750,000.00 USD | 0.00 USD | 11,140.00 USD | `-32.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1525.00` | 62,740,000.00 USD | 0.00 USD | 32,310.00 USD | `-32.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1535.00` | 62,710,000.00 USD | 0.00 USD | 983.78 USD | `-31.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1545.00` | 62,700,000.00 USD | 0.00 USD | 17,470.00 USD | `-31.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1555.00` | 62,690,000.00 USD | 0.00 USD | 25,980.00 USD | `-31.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1565.00` | 62,660,000.00 USD | 0.00 USD | 6,260.00 USD | `-30.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1575.00` | 62,650,000.00 USD | 0.00 USD | 190,890.00 USD | `-30.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1585.00` | 62,460,000.00 USD | 0.00 USD | 3,390.00 USD | `-29.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1595.00` | 62,460,000.00 USD | 0.00 USD | 4,040.00 USD | `-29.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1605.00` | 62,460,000.00 USD | 0.00 USD | 437,510.00 USD | `-28.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1615.00` | 62,020,000.00 USD | 0.00 USD | 25,840.00 USD | `-28.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1625.00` | 61,990,000.00 USD | 0.00 USD | 13,590.00 USD | `-27.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1635.00` | 61,980,000.00 USD | 0.00 USD | 5,510.00 USD | `-27.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1645.00` | 61,970,000.00 USD | 0.00 USD | 328,140.00 USD | `-27.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1655.00` | 61,650,000.00 USD | 0.00 USD | 35,070.00 USD | `-26.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1665.00` | 61,610,000.00 USD | 0.00 USD | 3,110.00 USD | `-26.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1675.00` | 61,610,000.00 USD | 0.00 USD | 3,440.00 USD | `-25.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1685.00` | 61,600,000.00 USD | 0.00 USD | 35,300.00 USD | `-25.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1695.00` | 61,570,000.00 USD | 0.00 USD | 8,490.00 USD | `-24.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1705.00` | 61,560,000.00 USD | 0.00 USD | 81,450.00 USD | `-24.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1715.00` | 61,480,000.00 USD | 0.00 USD | 18,650.00 USD | `-23.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1725.00` | 61,460,000.00 USD | 0.00 USD | 47,500.00 USD | `-23.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1735.00` | 61,410,000.00 USD | 0.00 USD | 28,150.00 USD | `-23.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1745.00` | 61,380,000.00 USD | 0.00 USD | 3,180.00 USD | `-22.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1755.00` | 61,380,000.00 USD | 0.00 USD | 502,310.00 USD | `-22.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1765.00` | 60,880,000.00 USD | 0.00 USD | 76,460.00 USD | `-21.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1775.00` | 60,800,000.00 USD | 0.00 USD | 3,090.00 USD | `-21.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1785.00` | 60,800,000.00 USD | 0.00 USD | 8,500.00 USD | `-20.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1795.00` | 60,790,000.00 USD | 0.00 USD | 184,330.00 USD | `-20.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1805.00` | 60,610,000.00 USD | 0.00 USD | 318,970.00 USD | `-19.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1815.00` | 60,290,000.00 USD | 0.00 USD | 114,830.00 USD | `-19.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1825.00` | 60,170,000.00 USD | 0.00 USD | 26,810.00 USD | `-19.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1835.00` | 60,150,000.00 USD | 0.00 USD | 2,110.00 USD | `-18.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1845.00` | 60,140,000.00 USD | 0.00 USD | 14,290.00 USD | `-18.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1855.00` | 60,130,000.00 USD | 0.00 USD | 466,540.00 USD | `-17.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1865.00` | 59,660,000.00 USD | 0.00 USD | 33,750.00 USD | `-17.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1875.00` | 59,630,000.00 USD | 0.00 USD | 18,210,000.00 USD | `-16.88%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1885.00` | 41,420,000.00 USD | 0.00 USD | 2,500.00 USD | `-16.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1895.00` | 41,420,000.00 USD | 0.00 USD | 64,540.00 USD | `-15.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1905.00` | 41,350,000.00 USD | 0.00 USD | 151,500.00 USD | `-15.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1915.00` | 41,200,000.00 USD | 0.00 USD | 8,130,000.00 USD | `-15.11%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1925.00` | 33,070,000.00 USD | 0.00 USD | 16,410,000.00 USD | `-14.66%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1935.00` | 16,660,000.00 USD | 0.00 USD | 79,950.00 USD | `-14.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1945.00` | 16,580,000.00 USD | 0.00 USD | 46,890.00 USD | `-13.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1955.00` | 16,530,000.00 USD | 0.00 USD | 54,590.00 USD | `-13.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1965.00` | 16,480,000.00 USD | 0.00 USD | 17,890.00 USD | `-12.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1975.00` | 16,460,000.00 USD | 0.00 USD | 91,390.00 USD | `-12.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1985.00` | 16,370,000.00 USD | 0.00 USD | 112,950.00 USD | `-12.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1995.00` | 16,260,000.00 USD | 0.00 USD | 232,340.00 USD | `-11.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2005.00` | 16,020,000.00 USD | 0.00 USD | 1,410,000.00 USD | `-11.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2015.00` | 14,610,000.00 USD | 0.00 USD | 67,680.00 USD | `-10.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2025.00` | 14,540,000.00 USD | 0.00 USD | 535,570.00 USD | `-10.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2035.00` | 14,010,000.00 USD | 0.00 USD | 99,030.00 USD | `-9.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2045.00` | 13,910,000.00 USD | 0.00 USD | 96,580.00 USD | `-9.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2055.00` | 13,810,000.00 USD | 0.00 USD | 270,770.00 USD | `-8.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2065.00` | 13,540,000.00 USD | 0.00 USD | 48,870.00 USD | `-8.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2075.00` | 13,490,000.00 USD | 0.00 USD | 29,190.00 USD | `-8.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2085.00` | 13,460,000.00 USD | 0.00 USD | 65,010.00 USD | `-7.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2095.00` | 13,400,000.00 USD | 0.00 USD | 55,120.00 USD | `-7.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2105.00` | 13,340,000.00 USD | 0.00 USD | 208,210.00 USD | `-6.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2115.00` | 13,130,000.00 USD | 0.00 USD | 128,360.00 USD | `-6.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2125.00` | 13,000,000.00 USD | 0.00 USD | 203,330.00 USD | `-5.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2135.00` | 12,800,000.00 USD | 0.00 USD | 36,510.00 USD | `-5.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2145.00` | 12,760,000.00 USD | 0.00 USD | 60,600.00 USD | `-4.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2155.00` | 12,700,000.00 USD | 0.00 USD | 141,880.00 USD | `-4.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2165.00` | 12,560,000.00 USD | 0.00 USD | 925,420.00 USD | `-4.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2175.00` | 11,640,000.00 USD | 0.00 USD | 1,360,000.00 USD | `-3.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2185.00` | 10,270,000.00 USD | 0.00 USD | 401,770.00 USD | `-3.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2195.00` | 9,870,000.00 USD | 0.00 USD | 1,120,000.00 USD | `-2.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2205.00` | 8,750,000.00 USD | 0.00 USD | 3,990,000.00 USD | `-2.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2215.00` | 4,760,000.00 USD | 0.00 USD | 865,000.00 USD | `-1.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2225.00` | 3,890,000.00 USD | 0.00 USD | 2,270,000.00 USD | `-1.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2235.00` | 1,620,000.00 USD | 0.00 USD | 1,240,000.00 USD | `-0.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2245.00` | 385,420.00 USD | 0.00 USD | 359,100.00 USD | `-0.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2255.00` | 26,320.00 USD | 0.00 USD | 26,320.00 USD | `-0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2265.00` | 4,550.00 USD | 4,550.00 USD | 0.00 USD | `+0.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2275.00` | 2,000,000.00 USD | 1,990,000.00 USD | 0.00 USD | `+0.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2285.00` | 2,830,000.00 USD | 833,160.00 USD | 0.00 USD | `+1.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2295.00` | 5,290,000.00 USD | 2,460,000.00 USD | 0.00 USD | `+1.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2305.00` | 5,950,000.00 USD | 661,450.00 USD | 0.00 USD | `+2.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2315.00` | 7,220,000.00 USD | 1,280,000.00 USD | 0.00 USD | `+2.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2325.00` | 7,460,000.00 USD | 231,480.00 USD | 0.00 USD | `+3.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2335.00` | 7,480,000.00 USD | 25,140.00 USD | 0.00 USD | `+3.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2345.00` | 8,830,000.00 USD | 1,350,000.00 USD | 0.00 USD | `+3.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2355.00` | 11,950,000.00 USD | 3,120,000.00 USD | 0.00 USD | `+4.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2365.00` | 12,250,000.00 USD | 299,370.00 USD | 0.00 USD | `+4.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2375.00` | 12,450,000.00 USD | 205,540.00 USD | 0.00 USD | `+5.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2385.00` | 13,050,000.00 USD | 598,090.00 USD | 0.00 USD | `+5.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2395.00` | 14,500,000.00 USD | 1,450,000.00 USD | 0.00 USD | `+6.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2405.00` | 16,440,000.00 USD | 1,950,000.00 USD | 0.00 USD | `+6.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2415.00` | 16,840,000.00 USD | 393,820.00 USD | 0.00 USD | `+7.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2425.00` | 19,840,000.00 USD | 3,000,000.00 USD | 0.00 USD | `+7.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2435.00` | 20,060,000.00 USD | 222,810.00 USD | 0.00 USD | `+7.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2445.00` | 30,420,000.00 USD | 10,360,000.00 USD | 0.00 USD | `+8.39%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2455.00` | 30,600,000.00 USD | 176,000.00 USD | 0.00 USD | `+8.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2465.00` | 32,740,000.00 USD | 2,140,000.00 USD | 0.00 USD | `+9.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2475.00` | 32,930,000.00 USD | 190,740.00 USD | 0.00 USD | `+9.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2485.00` | 35,060,000.00 USD | 2,130,000.00 USD | 0.00 USD | `+10.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2495.00` | 35,500,000.00 USD | 439,220.00 USD | 0.00 USD | `+10.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2505.00` | 40,550,000.00 USD | 5,050,000.00 USD | 0.00 USD | `+11.05%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2515.00` | 48,280,000.00 USD | 7,740,000.00 USD | 0.00 USD | `+11.49%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2525.00` | 51,650,000.00 USD | 3,370,000.00 USD | 0.00 USD | `+11.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2535.00` | 51,720,000.00 USD | 73,340.00 USD | 0.00 USD | `+12.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2545.00` | 53,870,000.00 USD | 2,150,000.00 USD | 0.00 USD | `+12.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2555.00` | 54,180,000.00 USD | 303,910.00 USD | 0.00 USD | `+13.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2565.00` | 56,550,000.00 USD | 2,370,000.00 USD | 0.00 USD | `+13.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2575.00` | 56,670,000.00 USD | 123,300.00 USD | 0.00 USD | `+14.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2585.00` | 59,360,000.00 USD | 2,690,000.00 USD | 0.00 USD | `+14.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2595.00` | 59,370,000.00 USD | 14,370.00 USD | 0.00 USD | `+15.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2605.00` | 62,370,000.00 USD | 3,000,000.00 USD | 0.00 USD | `+15.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2615.00` | 62,510,000.00 USD | 144,740.00 USD | 0.00 USD | `+15.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2625.00` | 64,680,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+16.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2635.00` | 64,850,000.00 USD | 172,380.00 USD | 0.00 USD | `+16.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2645.00` | 67,000,000.00 USD | 2,140,000.00 USD | 0.00 USD | `+17.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2655.00` | 67,250,000.00 USD | 251,180.00 USD | 0.00 USD | `+17.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2665.00` | 69,390,000.00 USD | 2,150,000.00 USD | 0.00 USD | `+18.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2675.00` | 69,740,000.00 USD | 351,060.00 USD | 0.00 USD | `+18.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2685.00` | 71,930,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+19.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2695.00` | 72,020,000.00 USD | 95,970.00 USD | 0.00 USD | `+19.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2705.00` | 76,490,000.00 USD | 4,470,000.00 USD | 0.00 USD | `+19.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2715.00` | 76,570,000.00 USD | 76,590.00 USD | 0.00 USD | `+20.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2725.00` | 79,040,000.00 USD | 2,470,000.00 USD | 0.00 USD | `+20.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2735.00` | 79,090,000.00 USD | 55,230.00 USD | 0.00 USD | `+21.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2745.00` | 81,350,000.00 USD | 2,260,000.00 USD | 0.00 USD | `+21.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2755.00` | 82,030,000.00 USD | 681,740.00 USD | 0.00 USD | `+22.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2765.00` | 84,420,000.00 USD | 2,380,000.00 USD | 0.00 USD | `+22.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2775.00` | 84,990,000.00 USD | 577,690.00 USD | 0.00 USD | `+23.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2785.00` | 87,260,000.00 USD | 2,270,000.00 USD | 0.00 USD | `+23.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2795.00` | 87,280,000.00 USD | 17,550.00 USD | 0.00 USD | `+23.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2805.00` | 91,530,000.00 USD | 4,240,000.00 USD | 0.00 USD | `+24.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2815.00` | 91,580,000.00 USD | 52,670.00 USD | 0.00 USD | `+24.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2825.00` | 91,640,000.00 USD | 63,490.00 USD | 0.00 USD | `+25.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2835.00` | 91,930,000.00 USD | 289,000.00 USD | 0.00 USD | `+25.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2845.00` | 92,940,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+26.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2855.00` | 94,330,000.00 USD | 1,390,000.00 USD | 0.00 USD | `+26.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2865.00` | 94,340,000.00 USD | 10,290.00 USD | 0.00 USD | `+27.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2875.00` | 94,340,000.00 USD | 2,460.00 USD | 0.00 USD | `+27.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2885.00` | 94,650,000.00 USD | 303,660.00 USD | 0.00 USD | `+27.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2895.00` | 94,670,000.00 USD | 21,290.00 USD | 0.00 USD | `+28.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2905.00` | 96,140,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+28.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2915.00` | 96,160,000.00 USD | 10,340.00 USD | 0.00 USD | `+29.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2925.00` | 96,160,000.00 USD | 3,050.00 USD | 0.00 USD | `+29.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2935.00` | 96,210,000.00 USD | 52,910.00 USD | 0.00 USD | `+30.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2945.00` | 96,250,000.00 USD | 34,650.00 USD | 0.00 USD | `+30.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2955.00` | 96,320,000.00 USD | 74,770.00 USD | 0.00 USD | `+31.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2965.00` | 96,430,000.00 USD | 111,790.00 USD | 0.00 USD | `+31.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2975.00` | 96,580,000.00 USD | 147,920.00 USD | 0.00 USD | `+31.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2985.00` | 96,760,000.00 USD | 177,120.00 USD | 0.00 USD | `+32.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2995.00` | 98,670,000.00 USD | 1,910,000.00 USD | 0.00 USD | `+32.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3005.00` | 100,610,000.00 USD | 1,930,000.00 USD | 0.00 USD | `+33.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3015.00` | 100,610,000.00 USD | 6,950.00 USD | 0.00 USD | `+33.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3025.00` | 100,650,000.00 USD | 37,610.00 USD | 0.00 USD | `+34.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3035.00` | 100,720,000.00 USD | 73,700.00 USD | 0.00 USD | `+34.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3045.00` | 100,750,000.00 USD | 22,460.00 USD | 0.00 USD | `+34.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3055.00` | 101,530,000.00 USD | 783,940.00 USD | 0.00 USD | `+35.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3065.00` | 101,530,000.00 USD | 3,080.00 USD | 0.00 USD | `+35.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3075.00` | 101,580,000.00 USD | 49,330.00 USD | 0.00 USD | `+36.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3085.00` | 101,600,000.00 USD | 19,570.00 USD | 0.00 USD | `+36.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3095.00` | 101,600,000.00 USD | 928.50 USD | 0.00 USD | `+37.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3105.00` | 116,350,000.00 USD | 14,750,000.00 USD | 0.00 USD | `+37.65%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `3115.00` | 116,490,000.00 USD | 135,050.00 USD | 0.00 USD | `+38.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3125.00` | 116,900,000.00 USD | 414,660.00 USD | 0.00 USD | `+38.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3145.00` | 116,910,000.00 USD | 2,530.00 USD | 0.00 USD | `+39.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3155.00` | 116,980,000.00 USD | 68,940.00 USD | 0.00 USD | `+39.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3165.00` | 117,000,000.00 USD | 21,490.00 USD | 0.00 USD | `+40.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3175.00` | 117,010,000.00 USD | 17,040.00 USD | 0.00 USD | `+40.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3185.00` | 117,010,000.00 USD | 1,330.00 USD | 0.00 USD | `+41.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3195.00` | 117,040,000.00 USD | 29,450.00 USD | 0.00 USD | `+41.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3205.00` | 117,810,000.00 USD | 766,520.00 USD | 0.00 USD | `+42.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3215.00` | 117,810,000.00 USD | 1,290.00 USD | 0.00 USD | `+42.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3225.00` | 117,820,000.00 USD | 3,740.00 USD | 0.00 USD | `+42.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3235.00` | 117,850,000.00 USD | 30,790.00 USD | 0.00 USD | `+43.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3245.00` | 117,900,000.00 USD | 56,110.00 USD | 0.00 USD | `+43.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3255.00` | 118,140,000.00 USD | 236,580.00 USD | 0.00 USD | `+44.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3265.00` | 118,160,000.00 USD | 15,710.00 USD | 0.00 USD | `+44.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3275.00` | 118,160,000.00 USD | 1,630.00 USD | 0.00 USD | `+45.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3285.00` | 118,300,000.00 USD | 141,980.00 USD | 0.00 USD | `+45.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3295.00` | 118,310,000.00 USD | 15,350.00 USD | 0.00 USD | `+46.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3305.00` | 119,710,000.00 USD | 1,400,000.00 USD | 0.00 USD | `+46.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3315.00` | 120,100,000.00 USD | 385,510.00 USD | 0.00 USD | `+46.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3325.00` | 120,110,000.00 USD | 18,270.00 USD | 0.00 USD | `+47.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3335.00` | 120,130,000.00 USD | 18,080.00 USD | 0.00 USD | `+47.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3345.00` | 120,130,000.00 USD | 617.15 USD | 0.00 USD | `+48.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3355.00` | 120,140,000.00 USD | 2,520.00 USD | 0.00 USD | `+48.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3365.00` | 120,140,000.00 USD | 597.29 USD | 0.00 USD | `+49.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3375.00` | 120,160,000.00 USD | 21,260.00 USD | 0.00 USD | `+49.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3385.00` | 120,210,000.00 USD | 58,010.00 USD | 0.00 USD | `+50.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3395.00` | 120,570,000.00 USD | 355,050.00 USD | 0.00 USD | `+50.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3405.00` | 121,910,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+50.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3415.00` | 121,920,000.00 USD | 3,510.00 USD | 0.00 USD | `+51.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3425.00` | 121,930,000.00 USD | 16,310.00 USD | 0.00 USD | `+51.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3445.00` | 121,950,000.00 USD | 15,030.00 USD | 0.00 USD | `+52.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3455.00` | 121,970,000.00 USD | 18,600.00 USD | 0.00 USD | `+53.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3465.00` | 121,970,000.00 USD | 495.50 USD | 0.00 USD | `+53.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3475.00` | 121,970,000.00 USD | 2,980.00 USD | 0.00 USD | `+54.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3485.00` | 122,010,000.00 USD | 43,610.00 USD | 0.00 USD | `+54.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3495.00` | 122,010,000.00 USD | 158.32 USD | 0.00 USD | `+54.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3505.00` | 122,460,000.00 USD | 444,410.00 USD | 0.00 USD | `+55.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3515.00` | 122,500,000.00 USD | 43,460.00 USD | 0.00 USD | `+55.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3525.00` | 122,510,000.00 USD | 3,690.00 USD | 0.00 USD | `+56.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3535.00` | 122,520,000.00 USD | 9,810.00 USD | 0.00 USD | `+56.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3545.00` | 122,520,000.00 USD | 179.38 USD | 0.00 USD | `+57.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3555.00` | 122,610,000.00 USD | 90,810.00 USD | 0.00 USD | `+57.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3565.00` | 122,610,000.00 USD | 2,300.00 USD | 0.00 USD | `+58.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3585.00` | 122,610,000.00 USD | 354.92 USD | 0.00 USD | `+58.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3595.00` | 122,620,000.00 USD | 13,160.00 USD | 0.00 USD | `+59.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3605.00` | 122,730,000.00 USD | 105,860.00 USD | 0.00 USD | `+59.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3625.00` | 122,740,000.00 USD | 10,210.00 USD | 0.00 USD | `+60.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3635.00` | 122,750,000.00 USD | 7,790.00 USD | 0.00 USD | `+61.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3645.00` | 122,750,000.00 USD | 3,860.00 USD | 0.00 USD | `+61.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3655.00` | 122,760,000.00 USD | 7,740.00 USD | 0.00 USD | `+62.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3665.00` | 122,770,000.00 USD | 8,130.00 USD | 0.00 USD | `+62.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3675.00` | 122,820,000.00 USD | 55,120.00 USD | 0.00 USD | `+62.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3685.00` | 122,820,000.00 USD | 3,550.00 USD | 0.00 USD | `+63.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3705.00` | 122,830,000.00 USD | 819.92 USD | 0.00 USD | `+64.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3715.00` | 122,830,000.00 USD | 323.58 USD | 0.00 USD | `+64.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3725.00` | 122,830,000.00 USD | 1,400.00 USD | 0.00 USD | `+65.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3735.00` | 122,830,000.00 USD | 6,490.00 USD | 0.00 USD | `+65.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3755.00` | 122,830,000.00 USD | 751.00 USD | 0.00 USD | `+66.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3785.00` | 122,830,000.00 USD | 286.90 USD | 0.00 USD | `+67.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3795.00` | 122,840,000.00 USD | 1,560.00 USD | 0.00 USD | `+68.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3805.00` | 123,570,000.00 USD | 734,090.00 USD | 0.00 USD | `+68.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3815.00` | 123,590,000.00 USD | 20,930.00 USD | 0.00 USD | `+69.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3825.00` | 123,600,000.00 USD | 8,380.00 USD | 0.00 USD | `+69.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3835.00` | 123,600,000.00 USD | 711.78 USD | 0.00 USD | `+70.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3845.00` | 123,600,000.00 USD | 355.28 USD | 0.00 USD | `+70.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3855.00` | 123,610,000.00 USD | 5,170.00 USD | 0.00 USD | `+70.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3885.00` | 123,630,000.00 USD | 19,430.00 USD | 0.00 USD | `+72.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3905.00` | 123,640,000.00 USD | 12,120.00 USD | 0.00 USD | `+73.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3915.00` | 124,280,000.00 USD | 646,840.00 USD | 0.00 USD | `+73.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3925.00` | 124,290,000.00 USD | 3,260.00 USD | 0.00 USD | `+74.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3935.00` | 124,330,000.00 USD | 42,570.00 USD | 0.00 USD | `+74.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3945.00` | 124,390,000.00 USD | 59,170.00 USD | 0.00 USD | `+74.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3955.00` | 124,390,000.00 USD | 1,380.00 USD | 0.00 USD | `+75.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3965.00` | 124,390,000.00 USD | 323.54 USD | 0.00 USD | `+75.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3975.00` | 124,400,000.00 USD | 6,960.00 USD | 0.00 USD | `+76.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3985.00` | 124,410,000.00 USD | 14,610.00 USD | 0.00 USD | `+76.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3995.00` | 124,420,000.00 USD | 4,280.00 USD | 0.00 USD | `+77.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4005.00` | 127,070,000.00 USD | 2,660,000.00 USD | 0.00 USD | `+77.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4035.00` | 127,070,000.00 USD | 898.59 USD | 0.00 USD | `+78.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4055.00` | 127,080,000.00 USD | 811.00 USD | 0.00 USD | `+79.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4075.00` | 127,080,000.00 USD | 4,310.00 USD | 0.00 USD | `+80.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4085.00` | 127,080,000.00 USD | 2,800.00 USD | 0.00 USD | `+81.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4105.00` | 127,120,000.00 USD | 39,390.00 USD | 0.00 USD | `+81.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4115.00` | 127,130,000.00 USD | 5,990.00 USD | 0.00 USD | `+82.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4125.00` | 127,130,000.00 USD | 372.90 USD | 0.00 USD | `+82.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4145.00` | 127,130,000.00 USD | 395.43 USD | 0.00 USD | `+83.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4185.00` | 127,130,000.00 USD | 376.65 USD | 0.00 USD | `+85.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4205.00` | 127,170,000.00 USD | 41,200.00 USD | 0.00 USD | `+86.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4215.00` | 127,170,000.00 USD | 460.70 USD | 0.00 USD | `+86.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4225.00` | 127,170,000.00 USD | 1,270.00 USD | 0.00 USD | `+87.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4255.00` | 127,180,000.00 USD | 4,300.00 USD | 0.00 USD | `+88.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4265.00` | 127,180,000.00 USD | 437.16 USD | 0.00 USD | `+89.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4275.00` | 127,240,000.00 USD | 64,550.00 USD | 0.00 USD | `+89.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4285.00` | 127,240,000.00 USD | 1,610.00 USD | 0.00 USD | `+89.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4305.00` | 127,340,000.00 USD | 97,670.00 USD | 0.00 USD | `+90.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4315.00` | 127,340,000.00 USD | 1,070.00 USD | 0.00 USD | `+91.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4345.00` | 127,350,000.00 USD | 11,270.00 USD | 0.00 USD | `+92.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4355.00` | 127,360,000.00 USD | 3,250.00 USD | 0.00 USD | `+93.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4375.00` | 127,400,000.00 USD | 43,750.00 USD | 0.00 USD | `+93.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4385.00` | 127,460,000.00 USD | 64,570.00 USD | 0.00 USD | `+94.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4395.00` | 127,470,000.00 USD | 1,050.00 USD | 0.00 USD | `+94.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4405.00` | 127,510,000.00 USD | 44,050.00 USD | 0.00 USD | `+95.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4415.00` | 127,520,000.00 USD | 11,480.00 USD | 0.00 USD | `+95.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4425.00` | 127,520,000.00 USD | 2,510.00 USD | 0.00 USD | `+96.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4435.00` | 127,700,000.00 USD | 177,400.00 USD | 0.00 USD | `+96.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4455.00` | 127,700,000.00 USD | 641.97 USD | 0.00 USD | `+97.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4465.00` | 127,700,000.00 USD | 1,030.00 USD | 0.00 USD | `+97.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4505.00` | 128,080,000.00 USD | 376,800.00 USD | 0.00 USD | `+99.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4515.00` | 128,080,000.00 USD | 2,280.00 USD | 0.00 USD | `+100.15%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `2017.30` | 455,960,000.00 USD | 0.00 USD | 455,960,000.00 USD | 83,300.00 USD | 176,210.00 USD | 0.00 USD |
| `1D` | `2020.30` | 455,700,000.00 USD | 0.00 USD | 455,700,000.00 USD | 0.00 USD | 558,730.00 USD | 0.00 USD |
| `7D` | `2025.30` | 999,770,000.00 USD | 0.00 USD | 999,770,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD |
| `1D` | `2026.30` | 455,140,000.00 USD | 0.00 USD | 455,140,000.00 USD | 0.00 USD | 914,780.00 USD | 28,770.00 USD |
| `7D` | `2028.60` | 999,590,000.00 USD | 0.00 USD | 999,590,000.00 USD | 0.00 USD | 1,180,000.00 USD | 35,180.00 USD |
| `1D` | `2029.30` | 454,190,000.00 USD | 0.00 USD | 454,190,000.00 USD | 0.00 USD | 0.00 USD | 43,160.00 USD |
| `7D` | `2031.90` | 998,380,000.00 USD | 0.00 USD | 998,380,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD |
| `1D` | `2032.30` | 454,150,000.00 USD | 0.00 USD | 454,150,000.00 USD | 937,190.00 USD | 1,470,000.00 USD | 0.00 USD |
| `7D` | `2035.20` | 996,930,000.00 USD | 0.00 USD | 996,930,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD |
| `1D` | `2035.30` | 451,750,000.00 USD | 0.00 USD | 451,750,000.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2038.30` | 450,710,000.00 USD | 0.00 USD | 450,710,000.00 USD | 138,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2038.50` | 996,600,000.00 USD | 0.00 USD | 996,600,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2041.30` | 450,570,000.00 USD | 0.00 USD | 450,570,000.00 USD | 0.00 USD | 134,080.00 USD | 0.00 USD |
| `7D` | `2045.10` | 995,140,000.00 USD | 0.00 USD | 995,140,000.00 USD | 0.00 USD | 149,500.00 USD | 47,970.00 USD |
| `1D` | `2050.30` | 450,440,000.00 USD | 0.00 USD | 450,440,000.00 USD | 0.00 USD | 0.00 USD | 717,780.00 USD |
| `7D` | `2051.70` | 994,940,000.00 USD | 0.00 USD | 994,940,000.00 USD | 1,320,000.00 USD | 0.00 USD | 1,190,000.00 USD |
| `1D` | `2053.30` | 449,720,000.00 USD | 0.00 USD | 449,720,000.00 USD | 0.00 USD | 0.00 USD | 28,160.00 USD |
| `1D` | `2056.30` | 449,690,000.00 USD | 0.00 USD | 449,690,000.00 USD | 242,080.00 USD | 88,880.00 USD | 0.00 USD |
| `7D` | `2058.30` | 992,440,000.00 USD | 0.00 USD | 992,440,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD |
| `1D` | `2059.30` | 449,360,000.00 USD | 0.00 USD | 449,360,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `7D` | `2061.60` | 992,090,000.00 USD | 0.00 USD | 992,090,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD |
| `1D` | `2062.30` | 448,610,000.00 USD | 0.00 USD | 448,610,000.00 USD | 80,610.00 USD | 121,470.00 USD | 52,590.00 USD |
| `7D` | `2064.90` | 987,650,000.00 USD | 0.00 USD | 987,650,000.00 USD | 1,230,000.00 USD | 313,000.00 USD | 979,910.00 USD |
| `1D` | `2065.30` | 448,350,000.00 USD | 0.00 USD | 448,350,000.00 USD | 984,680.00 USD | 537,030.00 USD | 598,250.00 USD |
| `7D` | `2068.20` | 985,130,000.00 USD | 0.00 USD | 985,130,000.00 USD | 1,740,000.00 USD | 1,860,000.00 USD | 893,570.00 USD |
| `1D` | `2068.30` | 446,230,000.00 USD | 0.00 USD | 446,230,000.00 USD | 444,700.00 USD | 1,330,000.00 USD | 50,470.00 USD |
| `1D` | `2071.30` | 444,410,000.00 USD | 0.00 USD | 444,410,000.00 USD | 1,040,000.00 USD | 534,600.00 USD | 437,490.00 USD |
| `7D` | `2071.50` | 980,630,000.00 USD | 0.00 USD | 980,630,000.00 USD | 2,820,000.00 USD | 2,410,000.00 USD | 1,230,000.00 USD |
| `1D` | `2074.30` | 442,400,000.00 USD | 0.00 USD | 442,400,000.00 USD | 614,280.00 USD | 62,630.00 USD | 930,220.00 USD |
| `7D` | `2074.80` | 974,170,000.00 USD | 0.00 USD | 974,170,000.00 USD | 4,370,000.00 USD | 3,270,000.00 USD | 4,050,000.00 USD |
| `1D` | `2077.30` | 440,790,000.00 USD | 0.00 USD | 440,790,000.00 USD | 3,000,000.00 USD | 1,520,000.00 USD | 2,180,000.00 USD |
| `7D` | `2078.10` | 962,470,000.00 USD | 0.00 USD | 962,470,000.00 USD | 5,560,000.00 USD | 4,320,000.00 USD | 2,410,000.00 USD |
| `1D` | `2080.30` | 434,090,000.00 USD | 0.00 USD | 434,090,000.00 USD | 1,670,000.00 USD | 1,590,000.00 USD | 280,750.00 USD |
| `7D` | `2081.40` | 950,180,000.00 USD | 0.00 USD | 950,180,000.00 USD | 4,720,000.00 USD | 3,420,000.00 USD | 2,500,000.00 USD |
| `1D` | `2083.30` | 430,550,000.00 USD | 0.00 USD | 430,550,000.00 USD | 2,180,000.00 USD | 1,420,000.00 USD | 775,480.00 USD |
| `7D` | `2084.70` | 939,550,000.00 USD | 0.00 USD | 939,550,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 4,900,000.00 USD |
| `1D` | `2086.30` | 426,180,000.00 USD | 0.00 USD | 426,180,000.00 USD | 1,580,000.00 USD | 1,500,000.00 USD | 1,650,000.00 USD |
| `7D` | `2088.00` | 930,750,000.00 USD | 0.00 USD | 930,750,000.00 USD | 3,990,000.00 USD | 2,780,000.00 USD | 1,650,000.00 USD |
| `1D` | `2089.30` | 421,450,000.00 USD | 0.00 USD | 421,450,000.00 USD | 1,470,000.00 USD | 430,310.00 USD | 228,930.00 USD |
| `7D` | `2091.30` | 922,330,000.00 USD | 0.00 USD | 922,330,000.00 USD | 4,410,000.00 USD | 952,210.00 USD | 7,590,000.00 USD |
| `1D` | `2092.30` | 419,330,000.00 USD | 0.00 USD | 419,330,000.00 USD | 1,150,000.00 USD | 514,440.00 USD | 957,110.00 USD |
| `7D` | `2094.60` | 909,370,000.00 USD | 0.00 USD | 909,370,000.00 USD | 5,720,000.00 USD | 2,160,000.00 USD | 2,340,000.00 USD |
| `1D` | `2095.30` | 416,710,000.00 USD | 0.00 USD | 416,710,000.00 USD | 2,180,000.00 USD | 1,320,000.00 USD | 2,110,000.00 USD |
| `7D` | `2097.90` | 899,150,000.00 USD | 0.00 USD | 899,150,000.00 USD | 2,340,000.00 USD | 3,210,000.00 USD | 1,290,000.00 USD |
| `1D` | `2098.30` | 411,100,000.00 USD | 0.00 USD | 411,100,000.00 USD | 474,990.00 USD | 1,170,000.00 USD | 309,770.00 USD |
| `7D` | `2101.20` | 892,310,000.00 USD | 0.00 USD | 892,310,000.00 USD | 999,530.00 USD | 1,580,000.00 USD | 4,020,000.00 USD |
| `1D` | `2101.30` | 409,140,000.00 USD | 0.00 USD | 409,140,000.00 USD | 207,380.00 USD | 44,780.00 USD | 304,180.00 USD |
| `1D` | `2104.30` | 408,590,000.00 USD | 0.00 USD | 408,590,000.00 USD | 1,070,000.00 USD | 961,080.00 USD | 190,690.00 USD |
| `7D` | `2104.50` | 885,710,000.00 USD | 0.00 USD | 885,710,000.00 USD | 2,010,000.00 USD | 1,180,000.00 USD | 2,250,000.00 USD |
| `1D` | `2107.30` | 406,360,000.00 USD | 0.00 USD | 406,360,000.00 USD | 546,100.00 USD | 0.00 USD | 502,840.00 USD |
| `7D` | `2107.80` | 880,270,000.00 USD | 0.00 USD | 880,270,000.00 USD | 2,380,000.00 USD | 452,470.00 USD | 1,650,000.00 USD |
| `1D` | `2110.30` | 405,310,000.00 USD | 0.00 USD | 405,310,000.00 USD | 118,210.00 USD | 31,550.00 USD | 196,840.00 USD |
| `7D` | `2111.10` | 875,790,000.00 USD | 0.00 USD | 875,790,000.00 USD | 3,530,000.00 USD | 2,350,000.00 USD | 2,170,000.00 USD |
| `1D` | `2113.30` | 404,970,000.00 USD | 0.00 USD | 404,970,000.00 USD | 911,810.00 USD | 643,210.00 USD | 224,810.00 USD |
| `7D` | `2114.40` | 867,740,000.00 USD | 0.00 USD | 867,740,000.00 USD | 1,080,000.00 USD | 1,850,000.00 USD | 3,800,000.00 USD |
| `1D` | `2116.30` | 403,190,000.00 USD | 0.00 USD | 403,190,000.00 USD | 0.00 USD | 13,230.00 USD | 426,410.00 USD |
| `7D` | `2117.70` | 861,010,000.00 USD | 0.00 USD | 861,010,000.00 USD | 3,430,000.00 USD | 2,020,000.00 USD | 3,380,000.00 USD |
| `1D` | `2119.30` | 402,750,000.00 USD | 0.00 USD | 402,750,000.00 USD | 218,200.00 USD | 256,720.00 USD | 937,660.00 USD |
| `7D` | `2121.00` | 852,180,000.00 USD | 0.00 USD | 852,180,000.00 USD | 3,650,000.00 USD | 1,340,000.00 USD | 1,820,000.00 USD |
| `1D` | `2122.30` | 401,340,000.00 USD | 0.00 USD | 401,340,000.00 USD | 926,060.00 USD | 689,080.00 USD | 1,310,000.00 USD |
| `7D` | `2124.30` | 845,370,000.00 USD | 0.00 USD | 845,370,000.00 USD | 832,850.00 USD | 972,650.00 USD | 1,510,000.00 USD |
| `1D` | `2125.30` | 398,410,000.00 USD | 0.00 USD | 398,410,000.00 USD | 1,010,000.00 USD | 950,560.00 USD | 707,090.00 USD |
| `7D` | `2127.60` | 842,050,000.00 USD | 0.00 USD | 842,050,000.00 USD | 2,400,000.00 USD | 2,630,000.00 USD | 3,270,000.00 USD |
| `1D` | `2128.30` | 395,740,000.00 USD | 0.00 USD | 395,740,000.00 USD | 365,910.00 USD | 1,040,000.00 USD | 293,430.00 USD |
| `7D` | `2130.90` | 833,750,000.00 USD | 0.00 USD | 833,750,000.00 USD | 2,410,000.00 USD | 2,300,000.00 USD | 1,700,000.00 USD |
| `1D` | `2131.30` | 394,050,000.00 USD | 0.00 USD | 394,050,000.00 USD | 0.00 USD | 18,610.00 USD | 649,790.00 USD |
| `7D` | `2134.20` | 827,330,000.00 USD | 0.00 USD | 827,330,000.00 USD | 2,170,000.00 USD | 550,450.00 USD | 308,060.00 USD |
| `1D` | `2137.30` | 393,380,000.00 USD | 0.00 USD | 393,380,000.00 USD | 0.00 USD | 278,410.00 USD | 0.00 USD |
| `7D` | `2137.50` | 824,300,000.00 USD | 0.00 USD | 824,300,000.00 USD | 1,040,000.00 USD | 880,790.00 USD | 43,560.00 USD |
| `7D` | `2140.80` | 822,340,000.00 USD | 0.00 USD | 822,340,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD |
| `7D` | `2144.10` | 818,410,000.00 USD | 0.00 USD | 818,410,000.00 USD | 449,020.00 USD | 1,130,000.00 USD | 268,500.00 USD |
| `7D` | `2147.40` | 816,560,000.00 USD | 0.00 USD | 816,560,000.00 USD | 657,710.00 USD | 421,320.00 USD | 0.00 USD |
| `7D` | `2150.70` | 815,480,000.00 USD | 0.00 USD | 815,480,000.00 USD | 459,630.00 USD | 463,640.00 USD | 31,040.00 USD |
| `1D` | `2152.30` | 393,100,000.00 USD | 0.00 USD | 393,100,000.00 USD | 208,250.00 USD | 440,530.00 USD | 0.00 USD |
| `7D` | `2154.00` | 814,530,000.00 USD | 0.00 USD | 814,530,000.00 USD | 128,430.00 USD | 331,520.00 USD | 32,590.00 USD |
| `1D` | `2155.30` | 392,450,000.00 USD | 0.00 USD | 392,450,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD |
| `7D` | `2157.30` | 814,030,000.00 USD | 0.00 USD | 814,030,000.00 USD | 388,210.00 USD | 1,030,000.00 USD | 1,080,000.00 USD |
| `1D` | `2158.30` | 391,060,000.00 USD | 0.00 USD | 391,060,000.00 USD | 0.00 USD | 0.00 USD | 37,580.00 USD |
| `7D` | `2160.60` | 811,540,000.00 USD | 0.00 USD | 811,540,000.00 USD | 646,940.00 USD | 1,900,000.00 USD | 1,990,000.00 USD |
| `1D` | `2161.30` | 391,020,000.00 USD | 0.00 USD | 391,020,000.00 USD | 0.00 USD | 3,150,000.00 USD | 71,920.00 USD |
| `7D` | `2163.90` | 806,990,000.00 USD | 0.00 USD | 806,990,000.00 USD | 566,120.00 USD | 3,280,000.00 USD | 1,290,000.00 USD |
| `1D` | `2164.30` | 387,800,000.00 USD | 0.00 USD | 387,800,000.00 USD | 0.00 USD | 0.00 USD | 55,900.00 USD |
| `7D` | `2167.20` | 801,850,000.00 USD | 0.00 USD | 801,850,000.00 USD | 25,540.00 USD | 3,620,000.00 USD | 50,240.00 USD |
| `1D` | `2167.30` | 387,740,000.00 USD | 0.00 USD | 387,740,000.00 USD | 2,340,000.00 USD | 341,240.00 USD | 52,000.00 USD |
| `1D` | `2170.30` | 385,010,000.00 USD | 0.00 USD | 385,010,000.00 USD | 5,020,000.00 USD | 4,430,000.00 USD | 873,550.00 USD |
| `7D` | `2170.50` | 798,150,000.00 USD | 0.00 USD | 798,150,000.00 USD | 3,500,000.00 USD | 2,380,000.00 USD | 1,830,000.00 USD |
| `1D` | `2173.30` | 374,680,000.00 USD | 0.00 USD | 374,680,000.00 USD | 0.00 USD | 190,230.00 USD | 0.00 USD |
| `7D` | `2173.80` | 790,450,000.00 USD | 0.00 USD | 790,450,000.00 USD | 4,110,000.00 USD | 363,040.00 USD | 1,010,000.00 USD |
| `1D` | `2176.30` | 374,490,000.00 USD | 0.00 USD | 374,490,000.00 USD | 345,940.00 USD | 1,400,000.00 USD | 0.00 USD |
| `1D` | `2179.30` | 372,750,000.00 USD | 0.00 USD | 372,750,000.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2180.40` | 784,960,000.00 USD | 0.00 USD | 784,960,000.00 USD | 0.00 USD | 373,740.00 USD | 119,920.00 USD |
| `1D` | `2185.30` | 371,570,000.00 USD | 0.00 USD | 371,570,000.00 USD | 1,350,000.00 USD | 0.00 USD | 1,790,000.00 USD |
| `7D` | `2187.00` | 784,470,000.00 USD | 0.00 USD | 784,470,000.00 USD | 556,600.00 USD | 0.00 USD | 54,020.00 USD |
| `7D` | `2190.30` | 783,860,000.00 USD | 0.00 USD | 783,860,000.00 USD | 2,730,000.00 USD | 0.00 USD | 2,980,000.00 USD |
| `1D` | `2191.30` | 368,420,000.00 USD | 0.00 USD | 368,420,000.00 USD | 0.00 USD | 222,200.00 USD | 70,390.00 USD |
| `1D` | `2194.30` | 368,120,000.00 USD | 0.00 USD | 368,120,000.00 USD | 605,210.00 USD | 0.00 USD | 39,000.00 USD |
| `7D` | `2196.90` | 778,150,000.00 USD | 0.00 USD | 778,150,000.00 USD | 2,580,000.00 USD | 474,090.00 USD | 0.00 USD |
| `1D` | `2197.30` | 367,480,000.00 USD | 0.00 USD | 367,480,000.00 USD | 416,500.00 USD | 881,070.00 USD | 1,890,000.00 USD |
| `7D` | `2200.20` | 775,090,000.00 USD | 0.00 USD | 775,090,000.00 USD | 3,000,000.00 USD | 5,080,000.00 USD | 3,200,000.00 USD |
| `1D` | `2200.30` | 364,300,000.00 USD | 0.00 USD | 364,300,000.00 USD | 284,470.00 USD | 3,100,000.00 USD | 220,720.00 USD |
| `1D` | `2203.30` | 360,690,000.00 USD | 0.00 USD | 360,690,000.00 USD | 3,540,000.00 USD | 1,410,000.00 USD | 2,100,000.00 USD |
| `7D` | `2203.50` | 763,810,000.00 USD | 0.00 USD | 763,810,000.00 USD | 3,650,000.00 USD | 1,710,000.00 USD | 3,750,000.00 USD |
| `1D` | `2206.30` | 353,640,000.00 USD | 0.00 USD | 353,640,000.00 USD | 755,060.00 USD | 10,890,000.00 USD | 946,580.00 USD |
| `7D` | `2206.80` | 754,710,000.00 USD | 0.00 USD | 754,710,000.00 USD | 6,920,000.00 USD | 9,430,000.00 USD | 4,020,000.00 USD |
| `1D` | `2209.30` | 341,060,000.00 USD | 0.00 USD | 341,060,000.00 USD | 2,720,000.00 USD | 2,010,000.00 USD | 3,050,000.00 USD |
| `7D` | `2210.10` | 734,330,000.00 USD | 0.00 USD | 734,330,000.00 USD | 12,800,000.00 USD | 20,410,000.00 USD | 6,470,000.00 USD |
| `1D` | `2212.30` | 333,290,000.00 USD | 0.00 USD | 333,290,000.00 USD | 7,970,000.00 USD | 2,320,000.00 USD | 3,060,000.00 USD |
| `7D` | `2213.40` | 694,660,000.00 USD | 0.00 USD | 694,660,000.00 USD | 10,920,000.00 USD | 11,890,000.00 USD | 13,170,000.00 USD |
| `1D` | `2215.30` | 319,940,000.00 USD | 0.00 USD | 319,940,000.00 USD | 17,700,000.00 USD | 14,340,000.00 USD | 7,240,000.00 USD |
| `7D` | `2216.70` | 658,670,000.00 USD | 0.00 USD | 658,670,000.00 USD | 25,210,000.00 USD | 17,030,000.00 USD | 9,390,000.00 USD |
| `1D` | `2218.30` | 280,660,000.00 USD | 0.00 USD | 280,660,000.00 USD | 7,390,000.00 USD | 7,700,000.00 USD | 2,280,000.00 USD |
| `7D` | `2220.00` | 607,050,000.00 USD | 0.00 USD | 607,050,000.00 USD | 24,310,000.00 USD | 12,300,000.00 USD | 10,120,000.00 USD |
| `1D` | `2221.30` | 263,300,000.00 USD | 0.00 USD | 263,300,000.00 USD | 6,130,000.00 USD | 12,360,000.00 USD | 1,260,000.00 USD |
| `7D` | `2223.30` | 560,320,000.00 USD | 0.00 USD | 560,320,000.00 USD | 10,150,000.00 USD | 8,220,000.00 USD | 11,910,000.00 USD |
| `1D` | `2224.30` | 243,550,000.00 USD | 0.00 USD | 243,550,000.00 USD | 9,430,000.00 USD | 5,550,000.00 USD | 5,550,000.00 USD |
| `7D` | `2226.60` | 530,040,000.00 USD | 0.00 USD | 530,040,000.00 USD | 12,840,000.00 USD | 11,030,000.00 USD | 9,840,000.00 USD |
| `1D` | `2227.30` | 223,020,000.00 USD | 0.00 USD | 223,020,000.00 USD | 5,860,000.00 USD | 13,040,000.00 USD | 2,610,000.00 USD |
| `7D` | `2229.90` | 496,330,000.00 USD | 0.00 USD | 496,330,000.00 USD | 12,730,000.00 USD | 9,180,000.00 USD | 20,660,000.00 USD |
| `1D` | `2230.30` | 201,510,000.00 USD | 0.00 USD | 201,510,000.00 USD | 6,920,000.00 USD | 5,550,000.00 USD | 2,600,000.00 USD |
| `7D` | `2233.20` | 453,760,000.00 USD | 0.00 USD | 453,760,000.00 USD | 16,600,000.00 USD | 24,290,000.00 USD | 10,420,000.00 USD |
| `1D` | `2233.30` | 186,440,000.00 USD | 0.00 USD | 186,440,000.00 USD | 6,390,000.00 USD | 2,520,000.00 USD | 8,970,000.00 USD |
| `1D` | `2236.30` | 168,550,000.00 USD | 0.00 USD | 168,550,000.00 USD | 18,610,000.00 USD | 0.00 USD | 4,380,000.00 USD |
| `7D` | `2236.50` | 402,440,000.00 USD | 0.00 USD | 402,440,000.00 USD | 16,050,000.00 USD | 2,010,000.00 USD | 11,790,000.00 USD |
| `1D` | `2239.30` | 145,560,000.00 USD | 0.00 USD | 145,560,000.00 USD | 16,040,000.00 USD | 4,410,000.00 USD | 4,420,000.00 USD |
| `7D` | `2239.80` | 372,600,000.00 USD | 0.00 USD | 372,600,000.00 USD | 15,710,000.00 USD | 6,600,000.00 USD | 13,750,000.00 USD |
| `1D` | `2242.30` | 120,690,000.00 USD | 0.00 USD | 120,690,000.00 USD | 2,420,000.00 USD | 760,920.00 USD | 5,230,000.00 USD |
| `7D` | `2243.10` | 336,540,000.00 USD | 0.00 USD | 336,540,000.00 USD | 22,920,000.00 USD | 0.00 USD | 8,970,000.00 USD |
| `1D` | `2245.30` | 112,280,000.00 USD | 0.00 USD | 112,280,000.00 USD | 2,360,000.00 USD | 4,260,000.00 USD | 482,700.00 USD |
| `7D` | `2246.40` | 304,650,000.00 USD | 0.00 USD | 304,650,000.00 USD | 14,340,000.00 USD | 0.00 USD | 13,920,000.00 USD |
| `1D` | `2248.30` | 105,170,000.00 USD | 0.00 USD | 105,170,000.00 USD | 8,900,000.00 USD | 0.00 USD | 4,100,000.00 USD |
| `7D` | `2249.70` | 276,390,000.00 USD | 0.00 USD | 276,390,000.00 USD | 18,000,000.00 USD | 0.00 USD | 12,600,000.00 USD |
| `1D` | `2251.30` | 92,180,000.00 USD | 0.00 USD | 92,180,000.00 USD | 9,610,000.00 USD | 506,110.00 USD | 2,950,000.00 USD |
| `7D` | `2253.00` | 245,800,000.00 USD | 0.00 USD | 245,800,000.00 USD | 26,890,000.00 USD | 0.00 USD | 17,940,000.00 USD |
| `1D` | `2254.30` | 79,120,000.00 USD | 0.00 USD | 79,120,000.00 USD | 0.00 USD | 0.00 USD | 12,590,000.00 USD |
| `7D` | `2256.30` | 200,970,000.00 USD | 0.00 USD | 200,970,000.00 USD | 17,450,000.00 USD | 0.00 USD | 3,310,000.00 USD |
| `7D` | `2259.60` | 180,210,000.00 USD | 0.00 USD | 180,210,000.00 USD | 10,940,000.00 USD | 0.00 USD | 11,910,000.00 USD |
| `1D` | `2260.30` | 66,520,000.00 USD | 0.00 USD | 66,520,000.00 USD | 0.00 USD | 0.00 USD | 156,010.00 USD |
| `1D` | `2263.30` | 66,370,000.00 USD | 0.00 USD | 66,370,000.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2266.30` | 63,950,000.00 USD | 0.00 USD | 63,950,000.00 USD | 0.00 USD | 0.00 USD | 12,140,000.00 USD |
| `1D` | `2269.30` | 51,810,000.00 USD | 0.00 USD | 51,810,000.00 USD | 0.00 USD | 0.00 USD | 7,960,000.00 USD |
| `7D` | `2269.50` | 157,360,000.00 USD | 0.00 USD | 157,360,000.00 USD | 0.00 USD | 4,370,000.00 USD | 0.00 USD |
| `1D` | `2272.30` | 43,850,000.00 USD | 0.00 USD | 43,850,000.00 USD | 0.00 USD | 9,150,000.00 USD | 12,500,000.00 USD |
| `7D` | `2272.80` | 152,990,000.00 USD | 0.00 USD | 152,990,000.00 USD | 0.00 USD | 31,270,000.00 USD | 0.00 USD |
| `1D` | `2275.30` | 22,200,000.00 USD | 0.00 USD | 22,200,000.00 USD | 1,020,000.00 USD | 20,900,000.00 USD | 287,660.00 USD |
| `7D` | `2276.10` | 121,730,000.00 USD | 0.00 USD | 121,730,000.00 USD | 0.00 USD | 54,160,000.00 USD | 0.00 USD |
| `1D` | `2278.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2278.30` | 18,870,000.00 USD | 18,870,000.00 USD | 0.00 USD | 2,840,000.00 USD | 15,600,000.00 USD | 431,610.00 USD |
| `7D` | `2279.40` | 67,560,000.00 USD | 0.00 USD | 67,560,000.00 USD | 0.00 USD | 67,560,000.00 USD | 0.00 USD |
| `7D` | `2279.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2281.30` | 105,590,000.00 USD | 105,590,000.00 USD | 0.00 USD | 40,410,000.00 USD | 26,130,000.00 USD | 20,170,000.00 USD |
| `7D` | `2282.70` | 81,670,000.00 USD | 81,670,000.00 USD | 0.00 USD | 0.00 USD | 81,670,000.00 USD | 0.00 USD |
| `1D` | `2284.30` | 175,900,000.00 USD | 175,900,000.00 USD | 0.00 USD | 34,880,000.00 USD | 20,290,000.00 USD | 15,140,000.00 USD |
| `7D` | `2286.00` | 91,070,000.00 USD | 91,070,000.00 USD | 0.00 USD | 0.00 USD | 9,400,000.00 USD | 0.00 USD |
| `1D` | `2287.30` | 176,660,000.00 USD | 176,660,000.00 USD | 0.00 USD | 0.00 USD | 760,920.00 USD | 0.00 USD |
| `1D` | `2290.30` | 185,050,000.00 USD | 185,050,000.00 USD | 0.00 USD | 0.00 USD | 8,390,000.00 USD | 0.00 USD |
| `1D` | `2293.30` | 189,850,000.00 USD | 189,850,000.00 USD | 0.00 USD | 4,720,000.00 USD | 0.00 USD | 75,150.00 USD |
| `7D` | `2295.90` | 100,510,000.00 USD | 100,510,000.00 USD | 0.00 USD | 6,580,000.00 USD | 2,380,000.00 USD | 479,670.00 USD |
| `1D` | `2296.30` | 196,290,000.00 USD | 196,290,000.00 USD | 0.00 USD | 0.00 USD | 6,300,000.00 USD | 143,830.00 USD |
| `7D` | `2299.20` | 118,540,000.00 USD | 118,540,000.00 USD | 0.00 USD | 11,730,000.00 USD | 5,900,000.00 USD | 392,000.00 USD |
| `1D` | `2299.30` | 208,890,000.00 USD | 208,890,000.00 USD | 0.00 USD | 5,410,000.00 USD | 10,910.00 USD | 7,180,000.00 USD |
| `1D` | `2302.30` | 219,420,000.00 USD | 219,420,000.00 USD | 0.00 USD | 9,550,000.00 USD | 682,490.00 USD | 298,370.00 USD |
| `7D` | `2302.50` | 160,780,000.00 USD | 160,780,000.00 USD | 0.00 USD | 23,020,000.00 USD | 7,250,000.00 USD | 11,970,000.00 USD |
| `1D` | `2305.30` | 248,720,000.00 USD | 248,720,000.00 USD | 0.00 USD | 13,540,000.00 USD | 13,730,000.00 USD | 2,040,000.00 USD |
| `7D` | `2305.80` | 172,070,000.00 USD | 172,070,000.00 USD | 0.00 USD | 2,980,000.00 USD | 6,110,000.00 USD | 2,200,000.00 USD |
| `1D` | `2308.30` | 254,050,000.00 USD | 254,050,000.00 USD | 0.00 USD | 2,420,000.00 USD | 2,750,000.00 USD | 156,010.00 USD |
| `7D` | `2309.10` | 175,840,000.00 USD | 175,840,000.00 USD | 0.00 USD | 732,090.00 USD | 930,630.00 USD | 2,110,000.00 USD |
| `1D` | `2311.30` | 262,290,000.00 USD | 262,290,000.00 USD | 0.00 USD | 691,870.00 USD | 0.00 USD | 7,550,000.00 USD |
| `7D` | `2312.40` | 183,190,000.00 USD | 183,190,000.00 USD | 0.00 USD | 7,270,000.00 USD | 0.00 USD | 70,770.00 USD |
| `1D` | `2314.30` | 273,750,000.00 USD | 273,750,000.00 USD | 0.00 USD | 0.00 USD | 11,260,000.00 USD | 203,330.00 USD |
| `7D` | `2315.70` | 190,760,000.00 USD | 190,760,000.00 USD | 0.00 USD | 0.00 USD | 7,460,000.00 USD | 117,510.00 USD |
| `1D` | `2317.30` | 300,680,000.00 USD | 300,680,000.00 USD | 0.00 USD | 8,430,000.00 USD | 13,390,000.00 USD | 5,100,000.00 USD |
| `7D` | `2319.00` | 196,750,000.00 USD | 196,750,000.00 USD | 0.00 USD | 1,020,000.00 USD | 4,550,000.00 USD | 411,830.00 USD |
| `1D` | `2320.30` | 315,750,000.00 USD | 315,750,000.00 USD | 0.00 USD | 6,580,000.00 USD | 8,340,000.00 USD | 147,610.00 USD |
| `7D` | `2322.30` | 211,290,000.00 USD | 211,290,000.00 USD | 0.00 USD | 1,110,000.00 USD | 13,320,000.00 USD | 108,040.00 USD |
| `1D` | `2323.30` | 327,430,000.00 USD | 327,430,000.00 USD | 0.00 USD | 572,970.00 USD | 7,510,000.00 USD | 3,590,000.00 USD |
| `7D` | `2325.60` | 229,510,000.00 USD | 229,510,000.00 USD | 0.00 USD | 9,720,000.00 USD | 2,540,000.00 USD | 5,960,000.00 USD |
| `1D` | `2326.30` | 337,730,000.00 USD | 337,730,000.00 USD | 0.00 USD | 479,120.00 USD | 5,550,000.00 USD | 4,270,000.00 USD |
| `7D` | `2328.90` | 241,330,000.00 USD | 241,330,000.00 USD | 0.00 USD | 3,860,000.00 USD | 0.00 USD | 7,960,000.00 USD |
| `1D` | `2329.30` | 349,030,000.00 USD | 349,030,000.00 USD | 0.00 USD | 10,000,000.00 USD | 884,940.00 USD | 422,180.00 USD |
| `7D` | `2332.20` | 270,560,000.00 USD | 270,560,000.00 USD | 0.00 USD | 29,230,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2332.30` | 364,770,000.00 USD | 364,770,000.00 USD | 0.00 USD | 11,600,000.00 USD | 251,940.00 USD | 3,880,000.00 USD |
| `1D` | `2335.30` | 388,690,000.00 USD | 388,690,000.00 USD | 0.00 USD | 17,430,000.00 USD | 3,070,000.00 USD | 3,420,000.00 USD |
| `7D` | `2335.50` | 324,500,000.00 USD | 324,500,000.00 USD | 0.00 USD | 28,990,000.00 USD | 18,420,000.00 USD | 6,520,000.00 USD |
| `1D` | `2338.30` | 401,580,000.00 USD | 401,580,000.00 USD | 0.00 USD | 6,030,000.00 USD | 688,030.00 USD | 6,180,000.00 USD |
| `7D` | `2338.80` | 342,370,000.00 USD | 342,370,000.00 USD | 0.00 USD | 9,570,000.00 USD | 0.00 USD | 8,310,000.00 USD |
| `1D` | `2341.30` | 426,810,000.00 USD | 426,810,000.00 USD | 0.00 USD | 9,780,000.00 USD | 5,570,000.00 USD | 9,870,000.00 USD |
| `7D` | `2342.10` | 382,470,000.00 USD | 382,470,000.00 USD | 0.00 USD | 4,720,000.00 USD | 21,390,000.00 USD | 14,000,000.00 USD |
| `1D` | `2344.30` | 440,070,000.00 USD | 440,070,000.00 USD | 0.00 USD | 1,370,000.00 USD | 6,180,000.00 USD | 5,710,000.00 USD |
| `7D` | `2345.40` | 403,840,000.00 USD | 403,840,000.00 USD | 0.00 USD | 1,350,000.00 USD | 13,990,000.00 USD | 6,020,000.00 USD |
| `1D` | `2347.30` | 451,910,000.00 USD | 451,910,000.00 USD | 0.00 USD | 3,220,000.00 USD | 3,010,000.00 USD | 5,600,000.00 USD |
| `7D` | `2348.70` | 436,980,000.00 USD | 436,980,000.00 USD | 0.00 USD | 847,620.00 USD | 8,140,000.00 USD | 24,140,000.00 USD |
| `1D` | `2350.30` | 501,050,000.00 USD | 501,050,000.00 USD | 0.00 USD | 33,090,000.00 USD | 7,200,000.00 USD | 8,860,000.00 USD |
| `7D` | `2352.00` | 473,600,000.00 USD | 473,600,000.00 USD | 0.00 USD | 2,930,000.00 USD | 23,060,000.00 USD | 10,630,000.00 USD |
| `1D` | `2353.30` | 510,240,000.00 USD | 510,240,000.00 USD | 0.00 USD | 4,170,000.00 USD | 3,800,000.00 USD | 1,220,000.00 USD |
| `7D` | `2355.30` | 528,190,000.00 USD | 528,190,000.00 USD | 0.00 USD | 16,520,000.00 USD | 36,690,000.00 USD | 1,380,000.00 USD |
| `1D` | `2356.30` | 532,990,000.00 USD | 532,990,000.00 USD | 0.00 USD | 3,710,000.00 USD | 16,640,000.00 USD | 2,390,000.00 USD |
| `7D` | `2358.60` | 539,010,000.00 USD | 539,010,000.00 USD | 0.00 USD | 7,110,000.00 USD | 512,220.00 USD | 3,190,000.00 USD |
| `1D` | `2359.30` | 551,030,000.00 USD | 551,030,000.00 USD | 0.00 USD | 4,140,000.00 USD | 6,970,000.00 USD | 6,920,000.00 USD |
| `7D` | `2361.90` | 546,080,000.00 USD | 546,080,000.00 USD | 0.00 USD | 3,150,000.00 USD | 3,800,000.00 USD | 119,920.00 USD |
| `1D` | `2362.30` | 569,670,000.00 USD | 569,670,000.00 USD | 0.00 USD | 10,460,000.00 USD | 6,710,000.00 USD | 1,470,000.00 USD |
| `7D` | `2365.20` | 561,430,000.00 USD | 561,430,000.00 USD | 0.00 USD | 8,440,000.00 USD | 0.00 USD | 6,920,000.00 USD |
| `1D` | `2365.30` | 586,140,000.00 USD | 586,140,000.00 USD | 0.00 USD | 4,820,000.00 USD | 3,710,000.00 USD | 7,940,000.00 USD |
| `1D` | `2368.30` | 599,940,000.00 USD | 599,940,000.00 USD | 0.00 USD | 7,910,000.00 USD | 2,500,000.00 USD | 3,400,000.00 USD |
| `7D` | `2368.50` | 573,190,000.00 USD | 573,190,000.00 USD | 0.00 USD | 10,830,000.00 USD | 475,460.00 USD | 458,400.00 USD |
| `1D` | `2371.30` | 640,580,000.00 USD | 640,580,000.00 USD | 0.00 USD | 18,140,000.00 USD | 13,710,000.00 USD | 8,790,000.00 USD |
| `7D` | `2371.80` | 652,910,000.00 USD | 652,910,000.00 USD | 0.00 USD | 26,000,000.00 USD | 0.00 USD | 53,720,000.00 USD |
| `1D` | `2374.30` | 663,060,000.00 USD | 663,060,000.00 USD | 0.00 USD | 14,690,000.00 USD | 1,320,000.00 USD | 6,470,000.00 USD |
| `7D` | `2375.10` | 679,860,000.00 USD | 679,860,000.00 USD | 0.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD |
| `1D` | `2377.30` | 686,820,000.00 USD | 686,820,000.00 USD | 0.00 USD | 7,110,000.00 USD | 8,030,000.00 USD | 8,620,000.00 USD |
| `7D` | `2378.40` | 725,270,000.00 USD | 725,270,000.00 USD | 0.00 USD | 11,800,000.00 USD | 7,950,000.00 USD | 25,670,000.00 USD |
| `1D` | `2380.30` | 730,680,000.00 USD | 730,680,000.00 USD | 0.00 USD | 14,000,000.00 USD | 11,640,000.00 USD | 18,220,000.00 USD |
| `7D` | `2381.70` | 763,020,000.00 USD | 763,020,000.00 USD | 0.00 USD | 8,510,000.00 USD | 6,750,000.00 USD | 22,490,000.00 USD |
| `1D` | `2383.30` | 790,070,000.00 USD | 790,070,000.00 USD | 0.00 USD | 24,350,000.00 USD | 17,700,000.00 USD | 17,340,000.00 USD |
| `7D` | `2385.00` | 864,740,000.00 USD | 864,740,000.00 USD | 0.00 USD | 18,550,000.00 USD | 36,910,000.00 USD | 46,260,000.00 USD |
| `1D` | `2386.30` | 828,870,000.00 USD | 828,870,000.00 USD | 0.00 USD | 12,830,000.00 USD | 14,620,000.00 USD | 11,350,000.00 USD |
| `7D` | `2388.30` | 952,610,000.00 USD | 952,610,000.00 USD | 0.00 USD | 5,290,000.00 USD | 38,070,000.00 USD | 44,510,000.00 USD |
| `1D` | `2389.30` | 857,770,000.00 USD | 857,770,000.00 USD | 0.00 USD | 13,790,000.00 USD | 7,220,000.00 USD | 7,880,000.00 USD |
| `7D` | `2391.60` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 8,560,000.00 USD | 52,080,000.00 USD | 40,380,000.00 USD |
| `1D` | `2392.30` | 874,150,000.00 USD | 874,150,000.00 USD | 0.00 USD | 3,240,000.00 USD | 6,420,000.00 USD | 6,720,000.00 USD |
| `7D` | `2394.90` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 57,450,000.00 USD | 32,260,000.00 USD | 37,090,000.00 USD |
| `1D` | `2395.30` | 892,230,000.00 USD | 892,230,000.00 USD | 0.00 USD | 7,070,000.00 USD | 7,250,000.00 USD | 3,760,000.00 USD |
| `7D` | `2398.20` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 0.00 USD | 42,820,000.00 USD | 38,210,000.00 USD | 29,190,000.00 USD |
| `1D` | `2398.30` | 912,440,000.00 USD | 912,440,000.00 USD | 0.00 USD | 5,950,000.00 USD | 6,860,000.00 USD | 7,410,000.00 USD |
| `1D` | `2401.30` | 937,980,000.00 USD | 937,980,000.00 USD | 0.00 USD | 8,760,000.00 USD | 7,400,000.00 USD | 9,390,000.00 USD |
| `7D` | `2401.50` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 51,970,000.00 USD | 26,780,000.00 USD | 29,090,000.00 USD |
| `1D` | `2404.30` | 968,240,000.00 USD | 968,240,000.00 USD | 0.00 USD | 10,010,000.00 USD | 11,410,000.00 USD | 8,840,000.00 USD |
| `7D` | `2404.80` | 1,510,000,000.00 USD | 1,510,000,000.00 USD | 0.00 USD | 50,800,000.00 USD | 32,200,000.00 USD | 24,110,000.00 USD |
| `1D` | `2407.30` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 0.00 USD | 16,500,000.00 USD | 9,260,000.00 USD | 8,810,000.00 USD |
| `7D` | `2408.10` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 34,390,000.00 USD | 31,420,000.00 USD | 25,030,000.00 USD |
| `1D` | `2410.30` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 0.00 USD | 8,800,000.00 USD | 8,390,000.00 USD | 9,580,000.00 USD |
| `7D` | `2411.40` | 1,680,000,000.00 USD | 1,680,000,000.00 USD | 0.00 USD | 19,200,000.00 USD | 32,580,000.00 USD | 27,660,000.00 USD |
| `1D` | `2413.30` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 8,610,000.00 USD | 5,530,000.00 USD | 3,130,000.00 USD |
| `7D` | `2414.70` | 1,740,000,000.00 USD | 1,740,000,000.00 USD | 0.00 USD | 24,010,000.00 USD | 21,950,000.00 USD | 23,130,000.00 USD |
| `1D` | `2416.30` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 4,770,000.00 USD | 3,260,000.00 USD | 4,390,000.00 USD |
| `7D` | `2418.00` | 1,820,000,000.00 USD | 1,820,000,000.00 USD | 0.00 USD | 34,060,000.00 USD | 15,260,000.00 USD | 24,610,000.00 USD |
| `1D` | `2419.30` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 0.00 USD | 5,120,000.00 USD | 3,350,000.00 USD | 3,480,000.00 USD |
| `7D` | `2421.30` | 1,890,000,000.00 USD | 1,890,000,000.00 USD | 0.00 USD | 25,700,000.00 USD | 27,890,000.00 USD | 21,590,000.00 USD |
| `1D` | `2422.30` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 4,560,000.00 USD | 5,190,000.00 USD | 6,060,000.00 USD |
| `7D` | `2424.60` | 1,990,000,000.00 USD | 1,990,000,000.00 USD | 0.00 USD | 24,180,000.00 USD | 35,050,000.00 USD | 34,520,000.00 USD |
| `1D` | `2425.30` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 1,810,000.00 USD | 2,670,000.00 USD | 844,590.00 USD |
| `7D` | `2427.90` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 0.00 USD | 25,200,000.00 USD | 18,380,000.00 USD | 26,460,000.00 USD |
| `1D` | `2428.30` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 466,170.00 USD | 542,280.00 USD | 1,500,000.00 USD |
| `7D` | `2431.20` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 0.00 USD | 10,380,000.00 USD | 18,750,000.00 USD | 9,300,000.00 USD |
| `1D` | `2431.30` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 2,890,000.00 USD | 2,960,000.00 USD | 347,720.00 USD |
| `1D` | `2434.30` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 1,930,000.00 USD | 510,300.00 USD | 1,580,000.00 USD |
| `7D` | `2434.50` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 0.00 USD | 27,390,000.00 USD | 21,570,000.00 USD | 11,240,000.00 USD |
| `1D` | `2437.30` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 1,250,000.00 USD | 531,390.00 USD | 205,600.00 USD |
| `7D` | `2437.80` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 0.00 USD | 12,000,000.00 USD | 12,820,000.00 USD | 5,470,000.00 USD |
| `1D` | `2440.30` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 1,540,000.00 USD | 1,250,000.00 USD | 479,040.00 USD |
| `7D` | `2441.10` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 0.00 USD | 15,080,000.00 USD | 8,120,000.00 USD | 10,680,000.00 USD |
| `1D` | `2443.30` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 1,050,000.00 USD | 1,850,000.00 USD | 2,060,000.00 USD |
| `7D` | `2444.40` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 0.00 USD | 8,860,000.00 USD | 15,160,000.00 USD | 14,000,000.00 USD |
| `1D` | `2446.30` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 648,280.00 USD | 347,060.00 USD | 404,470.00 USD |
| `7D` | `2447.70` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 0.00 USD | 11,650,000.00 USD | 8,510,000.00 USD | 17,330,000.00 USD |
| `1D` | `2449.30` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 408,380.00 USD | 744,230.00 USD | 2,770,000.00 USD |
| `7D` | `2451.00` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 0.00 USD | 16,710,000.00 USD | 14,100,000.00 USD | 16,480,000.00 USD |
| `1D` | `2452.30` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 3,750,000.00 USD | 2,920,000.00 USD | 4,440,000.00 USD |
| `7D` | `2454.30` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 4,620,000.00 USD | 5,780,000.00 USD | 3,880,000.00 USD |
| `1D` | `2455.30` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 4,310,000.00 USD | 3,050,000.00 USD | 2,350,000.00 USD |
| `7D` | `2457.60` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 0.00 USD | 15,150,000.00 USD | 12,540,000.00 USD | 12,640,000.00 USD |
| `1D` | `2458.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 1,900,000.00 USD | 1,790,000.00 USD | 1,210,000.00 USD |
| `7D` | `2460.90` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 0.00 USD | 5,580,000.00 USD | 8,670,000.00 USD | 6,870,000.00 USD |
| `1D` | `2461.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 1,260,000.00 USD | 1,180,000.00 USD | 1,160,000.00 USD |
| `7D` | `2464.20` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 0.00 USD | 8,720,000.00 USD | 7,700,000.00 USD | 4,700,000.00 USD |
| `1D` | `2464.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 0.00 USD | 619,960.00 USD | 829,050.00 USD |
| `1D` | `2467.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 83,300.00 USD | 68,070.00 USD | 0.00 USD |
| `7D` | `2467.50` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 0.00 USD | 4,540,000.00 USD | 3,710,000.00 USD | 586,780.00 USD |
| `1D` | `2470.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 0.00 USD | 1,190,000.00 USD | 391,890.00 USD |
| `7D` | `2470.80` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 0.00 USD | 3,960,000.00 USD | 2,290,000.00 USD | 522,210.00 USD |
| `7D` | `2474.10` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 0.00 USD | 5,230,000.00 USD | 2,920,000.00 USD | 2,400,000.00 USD |
| `1D` | `2476.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 0.00 USD | 914,780.00 USD | 28,770.00 USD |
| `7D` | `2477.40` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 0.00 USD | 1,660,000.00 USD | 4,420,000.00 USD | 718,840.00 USD |
| `7D` | `2480.70` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 0.00 USD | 2,110,000.00 USD | 4,170,000.00 USD | 540,990.00 USD |
| `1D` | `2482.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 239,600.00 USD | 136,500.00 USD | 43,160.00 USD |
| `7D` | `2484.00` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 0.00 USD | 1,210,000.00 USD | 1,390,000.00 USD | 77,610.00 USD |
| `1D` | `2485.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 865,140.00 USD | 1,330,000.00 USD | 0.00 USD |
| `7D` | `2487.30` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 0.00 USD | 325,140.00 USD | 262,280.00 USD | 0.00 USD |
| `1D` | `2488.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 866,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2490.60` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 0.00 USD | 2,910,000.00 USD | 2,540,000.00 USD | 279,750.00 USD |
| `1D` | `2491.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 138,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2493.90` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 0.00 USD | 1,660,000.00 USD | 1,790,000.00 USD | 3,940,000.00 USD |
| `1D` | `2494.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 0.00 USD | 134,080.00 USD | 0.00 USD |
| `7D` | `2497.20` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 0.00 USD | 2,940,000.00 USD | 5,270,000.00 USD | 8,250,000.00 USD |
| `7D` | `2500.50` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 0.00 USD | 1,110,000.00 USD | 2,280,000.00 USD | 1,130,000.00 USD |
| `7D` | `2503.80` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 0.00 USD | 63,860.00 USD | 1,900,000.00 USD | 125,600.00 USD |
| `1D` | `2506.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 717,780.00 USD |
| `7D` | `2507.10` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 0.00 USD | 4,340,000.00 USD | 3,090,000.00 USD | 3,190,000.00 USD |
| `1D` | `2509.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,160.00 USD |
| `7D` | `2510.40` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 0.00 USD | 2,290,000.00 USD | 1,270,000.00 USD | 0.00 USD |
| `1D` | `2512.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 242,080.00 USD | 88,880.00 USD | 0.00 USD |
| `7D` | `2513.70` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 0.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2515.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `7D` | `2517.00` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 0.00 USD | 97,050.00 USD | 189,640.00 USD | 0.00 USD |
| `7D` | `2520.30` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD |
| `1D` | `2521.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 80,610.00 USD | 121,470.00 USD | 110,470.00 USD |
| `7D` | `2523.60` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 0.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD |
| `1D` | `2524.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 984,680.00 USD | 537,030.00 USD | 540,380.00 USD |
| `7D` | `2526.90` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 0.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD |
| `1D` | `2527.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 387,410.00 USD | 362,000.00 USD | 50,470.00 USD |
| `7D` | `2530.20` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 0.00 USD | 2,800,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD |
| `1D` | `2530.30` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 1,050,000.00 USD | 965,400.00 USD | 437,490.00 USD |
| `1D` | `2533.30` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 407,340.00 USD | 555,250.00 USD | 436,900.00 USD |
| `7D` | `2533.50` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 0.00 USD | 3,530,000.00 USD | 1,850,000.00 USD | 2,030,000.00 USD |
| `1D` | `2536.30` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 1,260,000.00 USD | 698,510.00 USD | 1,080,000.00 USD |
| `7D` | `2536.80` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 0.00 USD | 3,720,000.00 USD | 3,450,000.00 USD | 3,530,000.00 USD |
| `1D` | `2539.30` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 2,370,000.00 USD | 1,090,000.00 USD | 1,660,000.00 USD |
| `7D` | `2540.10` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 0.00 USD | 4,150,000.00 USD | 3,220,000.00 USD | 1,580,000.00 USD |
| `1D` | `2542.30` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 1,300,000.00 USD | 1,350,000.00 USD | 218,810.00 USD |
| `7D` | `2543.40` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 0.00 USD | 4,150,000.00 USD | 2,520,000.00 USD | 2,480,000.00 USD |
| `1D` | `2545.30` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 1,030,000.00 USD | 336,450.00 USD | 212,140.00 USD |
| `7D` | `2546.70` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 0.00 USD | 1,450,000.00 USD | 1,090,000.00 USD | 2,290,000.00 USD |
| `1D` | `2548.30` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 2,050,000.00 USD | 1,680,000.00 USD | 1,720,000.00 USD |
| `7D` | `2550.00` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 0.00 USD | 4,320,000.00 USD | 3,550,000.00 USD | 3,720,000.00 USD |
| `1D` | `2551.30` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 1,480,000.00 USD | 1,120,000.00 USD | 698,070.00 USD |
| `7D` | `2553.30` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 0.00 USD | 2,820,000.00 USD | 788,360.00 USD | 2,600,000.00 USD |
| `1D` | `2554.30` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 1,100,000.00 USD | 228,660.00 USD | 236,190.00 USD |
| `7D` | `2556.60` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 0.00 USD | 2,760,000.00 USD | 283,560.00 USD | 6,500,000.00 USD |
| `1D` | `2557.30` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 717,260.00 USD | 506,330.00 USD | 740,260.00 USD |
| `7D` | `2559.90` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 0.00 USD | 5,720,000.00 USD | 2,130,000.00 USD | 1,390,000.00 USD |
| `1D` | `2560.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 2,020,000.00 USD | 1,140,000.00 USD | 1,430,000.00 USD |
| `7D` | `2563.20` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 0.00 USD | 1,430,000.00 USD | 2,900,000.00 USD | 1,290,000.00 USD |
| `1D` | `2563.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 617,040.00 USD | 998,570.00 USD | 984,190.00 USD |
| `1D` | `2566.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 172,210.00 USD | 403,100.00 USD | 11,930.00 USD |
| `7D` | `2566.50` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 0.00 USD | 1,860,000.00 USD | 1,830,000.00 USD | 3,300,000.00 USD |
| `1D` | `2569.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 327,300.00 USD | 119,690.00 USD | 466,670.00 USD |
| `7D` | `2569.80` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 0.00 USD | 125,250.00 USD | 341,900.00 USD | 1,190,000.00 USD |
| `1D` | `2572.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 792,480.00 USD | 841,400.00 USD | 16,280.00 USD |
| `7D` | `2573.10` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,790,000.00 USD |
| `1D` | `2575.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 546,100.00 USD | 0.00 USD | 502,840.00 USD |
| `7D` | `2576.40` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 0.00 USD | 2,400,000.00 USD | 930,280.00 USD | 1,640,000.00 USD |
| `1D` | `2578.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 118,210.00 USD | 31,550.00 USD | 8,540.00 USD |
| `7D` | `2579.70` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 0.00 USD | 2,750,000.00 USD | 1,780,000.00 USD | 1,960,000.00 USD |
| `1D` | `2581.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 450,470.00 USD | 405,480.00 USD | 409,780.00 USD |
| `7D` | `2583.00` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 0.00 USD | 1,730,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD |
| `1D` | `2583.80` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 411,740.00 USD | 226,990.00 USD | 0.00 USD |
| `7D` | `2586.30` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 0.00 USD | 1,480,000.00 USD | 2,030,000.00 USD | 2,570,000.00 USD |
| `7D` | `2589.60` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 0.00 USD | 3,310,000.00 USD | 631,590.00 USD | 2,150,000.00 USD |
| `7D` | `2592.90` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 0.00 USD | 2,370,000.00 USD | 1,280,000.00 USD | 1,580,000.00 USD |
| `7D` | `2596.20` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 0.00 USD | 794,750.00 USD | 620,840.00 USD | 1,490,000.00 USD |
| `7D` | `2599.50` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,530,000.00 USD | 2,810,000.00 USD |
| `7D` | `2602.80` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 0.00 USD | 1,680,000.00 USD | 1,260,000.00 USD | 1,690,000.00 USD |
| `7D` | `2606.10` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 0.00 USD | 1,850,000.00 USD | 1,560,000.00 USD | 772,800.00 USD |
| `7D` | `2609.40` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 0.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD |
| `7D` | `2612.70` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 0.00 USD | 1,010,000.00 USD | 643,740.00 USD | 43,560.00 USD |
| `7D` | `2616.00` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 0.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD |
| `7D` | `2619.30` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 0.00 USD | 449,020.00 USD | 323,810.00 USD | 268,500.00 USD |
| `7D` | `2622.60` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 0.00 USD | 631,440.00 USD | 1,220,000.00 USD | 0.00 USD |
| `7D` | `2625.90` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 0.00 USD | 485,890.00 USD | 474,490.00 USD | 0.00 USD |
| `7D` | `2629.20` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 0.00 USD | 0.00 USD | 20,460.00 USD | 31,040.00 USD |
| `7D` | `2632.40` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 0.00 USD | 0.00 USD | 301,060.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `29.01B` | Total OI Tokens: `12,756,150.3 ETH`
  * 1h OI Change: `-1.81%` | 4h OI Change: `-4.01%` | 24h OI Change: `-3.26%`
  * Exchange Breakdown: Binance=`8.55B` | Bybit=`2.06B` | OKX=`1.75B` | Hyperliquid=`2.44B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `440.03K` | Last 24h: `2.27M` | Last 3d: `7.66M` | Last 7d: `13.85M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0035%` | **USDT OKX** | `0.0076%` |
| **USDT Bybit** | `0.0001%` | **USDT KuCoin** | `0.0019%` |
| **USDT MEXC** | `0.0039%` | **USDT BingX** | `0.0082%` |
| **USDT Gate** | `0.0051%` | **USDT Bitget** | `0.0056%` |
| **CoinM Binance** | `0.0062%` | **CoinM OKX** | `0.0034%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `59.36%` | `40.64%` | `1.46` | 1,810,000,000.00 USD |
| `15M` | `Binance` | `49.21%` | `50.79%` | `0.97` | 473,010,000.00 USD |
| `15M` | `OKX` | `54.88%` | `45.12%` | `1.22` | 187,730,000.00 USD |
| `15M` | `Bybit` | `52.21%` | `47.79%` | `1.09` | 229,110,000.00 USD |
| `15M` | `KuCoin` | `68.18%` | `31.82%` | `2.14` | 4,860,000.00 USD |
| `15M` | `Gate` | `53.11%` | `46.89%` | `1.13` | 218,380,000.00 USD |
| `15M` | `Bitget` | `62.97%` | `37.03%` | `1.70` | 87,830,000.00 USD |
| `15M` | `BingX` | `44.9%` | `55.1%` | `0.81` | 18,490,000.00 USD |
| `15M` | `MEXC` | `54.88%` | `45.12%` | `1.22` | 58,740,000.00 USD |
| `15M` | `Bitunix` | `50.52%` | `49.48%` | `1.02` | 61,340,000.00 USD |
| `15M` | `Hyperliquid` | `55.09%` | `44.91%` | `1.23` | 105,480,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `54.85%` | `45.15%` | `1.21` | 4,450,000.00 USD |
| `15M` | `Crypto.com` | `49.55%` | `50.45%` | `0.98` | 5,910,000.00 USD |
| `15M` | `WhiteBIT` | `98.55%` | `1.45%` | `67.97` | 266,420,000.00 USD |
| `15M` | `HTX` | `60.47%` | `39.53%` | `1.53` | 2,960,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `60.97%` | `39.03%` | `1.56` | 29,460,000.00 USD |
| `15M` | `Bitfinex` | `14.08%` | `85.92%` | `0.16` | 4,790,000.00 USD |
| `15M` | `Kraken` | `53.39%` | `46.61%` | `1.15` | 24,210,000.00 USD |
| `15M` | `Aster` | `50.57%` | `49.43%` | `1.02` | 9,140,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `50.31%` | `49.69%` | `1.01` | 17,270,000.00 USD |
| `15M` | `Whale Positions` | `49.21%` | `50.79%` | `0.97` | 473,010,000.00 USD |
| `15M` | `Global Accounts` | `59.36%` | `40.64%` | `1.46` | 1,810,000,000.00 USD |
| `1H` | `ETH` | `46.94%` | `53.06%` | `0.88` | 18,600,000,000.00 USD |
| `1H` | `Binance` | `45.51%` | `54.49%` | `0.84` | 5,080,000,000.00 USD |
| `1H` | `OKX` | `45.43%` | `54.57%` | `0.83` | 2,170,000,000.00 USD |
| `1H` | `Bybit` | `44.97%` | `55.03%` | `0.82` | 2,300,000,000.00 USD |
| `1H` | `KuCoin` | `51.44%` | `48.56%` | `1.06` | 96,100,000.00 USD |
| `1H` | `Gate` | `51.23%` | `48.77%` | `1.05` | 1,220,000,000.00 USD |
| `1H` | `Bitget` | `52.93%` | `47.07%` | `1.12` | 788,970,000.00 USD |
| `1H` | `BingX` | `51.95%` | `48.05%` | `1.08` | 232,980,000.00 USD |
| `1H` | `MEXC` | `49.16%` | `50.84%` | `0.97` | 706,680,000.00 USD |
| `1H` | `Bitunix` | `50%` | `50%` | `1.00` | 713,470,000.00 USD |
| `1H` | `Hyperliquid` | `46.98%` | `53.02%` | `0.89` | 1,210,000,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `53.65%` | `46.35%` | `1.16` | 79,880,000.00 USD |
| `1H` | `Crypto.com` | `50.19%` | `49.81%` | `1.01` | 88,430,000.00 USD |
| `1H` | `WhiteBIT` | `47.03%` | `52.97%` | `0.89` | 3,080,000,000.00 USD |
| `1H` | `HTX` | `43%` | `57%` | `0.75` | 54,370,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `48.54%` | `51.46%` | `0.94` | 283,150,000.00 USD |
| `1H` | `Bitfinex` | `13.8%` | `86.2%` | `0.16` | 25,980,000.00 USD |
| `1H` | `Kraken` | `44.03%` | `55.97%` | `0.79` | 160,120,000.00 USD |
| `1H` | `Aster` | `46.43%` | `53.57%` | `0.87` | 150,690,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `45.75%` | `54.25%` | `0.84` | 151,400,000.00 USD |
| `1H` | `Whale Positions` | `45.51%` | `54.49%` | `0.84` | 5,080,000,000.00 USD |
| `1H` | `Global Accounts` | `46.94%` | `53.06%` | `0.88` | 18,600,000,000.00 USD |
| `4H` | `ETH` | `46.82%` | `53.18%` | `0.88` | 26,670,000,000.00 USD |
| `4H` | `Binance` | `45.59%` | `54.41%` | `0.84` | 7,390,000,000.00 USD |
| `4H` | `OKX` | `45.1%` | `54.9%` | `0.82` | 3,280,000,000.00 USD |
| `4H` | `Bybit` | `44.3%` | `55.7%` | `0.80` | 3,160,000,000.00 USD |
| `4H` | `KuCoin` | `47.85%` | `52.15%` | `0.92` | 125,620,000.00 USD |
| `4H` | `Gate` | `51.57%` | `48.43%` | `1.06` | 2,150,000,000.00 USD |
| `4H` | `Bitget` | `51.58%` | `48.42%` | `1.07` | 1,180,000,000.00 USD |
| `4H` | `BingX` | `51.77%` | `48.23%` | `1.07` | 372,710,000.00 USD |
| `4H` | `MEXC` | `48.92%` | `51.08%` | `0.96` | 1,200,000,000.00 USD |
| `4H` | `Bitunix` | `50.71%` | `49.29%` | `1.03` | 1,190,000,000.00 USD |
| `4H` | `Hyperliquid` | `45.49%` | `54.51%` | `0.83` | 1,690,000,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `53.45%` | `46.55%` | `1.15` | 132,220,000.00 USD |
| `4H` | `Crypto.com` | `50.79%` | `49.21%` | `1.03` | 145,170,000.00 USD |
| `4H` | `WhiteBIT` | `46.51%` | `53.49%` | `0.87` | 3,250,000,000.00 USD |
| `4H` | `HTX` | `44.59%` | `55.41%` | `0.80` | 89,340,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `51.05%` | `48.95%` | `1.04` | 513,430,000.00 USD |
| `4H` | `Bitfinex` | `16.63%` | `83.37%` | `0.20` | 31,600,000.00 USD |
| `4H` | `Kraken` | `42.89%` | `57.11%` | `0.75` | 235,790,000.00 USD |
| `4H` | `Aster` | `45.25%` | `54.75%` | `0.83` | 235,130,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `46.39%` | `53.61%` | `0.87` | 298,240,000.00 USD |
| `4H` | `Whale Positions` | `45.59%` | `54.41%` | `0.84` | 7,390,000,000.00 USD |
| `4H` | `Global Accounts` | `46.82%` | `53.18%` | `0.88` | 26,670,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `2326.75` | `2328.61` | `2326.75` | `2331.75` | `2325.75` | 28,646,242.16 USD | 14,157,941.65 USD | 14,488,300.51 USD | -330,358.86 USD | `-1.15%` | `0B / 1S` |
| `0:00 UTC` | `2334.75` | `2334.23` | `2334.75` | `2336.25` | `2330.25` | 36,369,004.25 USD | 19,887,478.26 USD | 16,481,525.99 USD | 3,405,952.27 USD | `+9.36%` | `1B / 1S` |
| `5:00 UTC` | `2335.75` | `2336.07` | `2335.75` | `2338.75` | `2332.75` | 54,317,401.94 USD | 19,276,795.34 USD | 35,040,606.60 USD | -15,763,811.25 USD | `-29.02%` | `0B / 1S` |
| `0:00 UTC` | `2309.25` | `2313.87` | `2309.25` | `2335.75` | `2302.25` | 493,849,561.51 USD | 204,343,201.57 USD | 289,506,359.94 USD | -85,163,158.37 USD | `-17.24%` | `0B / 20S` |
| `5:00 UTC` | `2315.25` | `2315.75` | `2315.25` | `2318.75` | `2312.25` | 88,922,002.19 USD | 46,836,385.14 USD | 42,085,617.06 USD | 4,750,768.08 USD | `+5.34%` | `3B / 0S` |
| `0:00 UTC` | `2300.25` | `2278.61` | `2300.25` | `2319.25` | `2238.25` | 1,664,912,417.71 USD | 683,261,559.43 USD | 981,650,858.29 USD | -298,389,298.86 USD | `-17.92%` | `1B / 31S` |
| `5:00 UTC` | `2259.25` | `2255.66` | `2259.25` | `2277.25` | `2230.25` | 846,756,637.45 USD | 383,814,230.15 USD | 462,942,407.30 USD | -79,128,177.15 USD | `-9.34%` | `0B / 6S` |
| `0:00 UTC` | `2260.25` | `2257.68` | `2260.25` | `2273.25` | `2245.25` | 606,671,993.02 USD | 300,593,954.86 USD | 306,078,038.17 USD | -5,484,083.31 USD | `-0.90%` | `5B / 2S` |
| `5:00 UTC` | `2281.25` | `2281.90` | `2281.25` | `2293.75` | `2267.75` | 508,254,989.09 USD | 245,674,110.48 USD | 262,580,878.61 USD | -16,906,768.14 USD | `-3.33%` | `3B / 0S` |
| `0:00 UTC` | `2283.25` | `2282.53` | `2283.25` | `2284.25` | `2279.25` | 21,470,472.48 USD | 10,503,956.05 USD | 10,966,516.43 USD | -462,560.38 USD | `-2.15%` | `4B / 0S` |

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
| `5m` | 6,870,000.00 USD | 7,130,000.00 USD | **`ACCUMULATION`** |
| `15m` | 4,760,000.00 USD | -65,690,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 3,540,000.00 USD | -3,060,000.00 USD | **`ACCUMULATION`** |
| `1h` | -68,760,000.00 USD | -904,050,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -90,780,000.00 USD | -1,150,000,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -92,400,000.00 USD | -1,290,000,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -87,800,000.00 USD | -1,490,000,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -66,970,000.00 USD | -1,190,000,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -71,120,000.00 USD | -1,250,000,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -113,450,000.00 USD | -1,660,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -100,170,000.00 USD | -2,290,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,090,000,000.00 USD | -9,240,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+6.87M` | 15m=`+4.76M` | 1h=`-68.76M` | 24h=`-113.45M`
* Futures Capital Netflows: 5m=`+7.13M` | 15m=`-65.69M` | 1h=`-904.05M` | 24h=`-1.66B`
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
  * `2026-10-30 02:53:46 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:14:46 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:00:46 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:59:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:59:46 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:59:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:46 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:46 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:46 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:46 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:46 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:01:46 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:01:46 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `2263.20` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2234.56` (Risk Distance: `28.64` pts)
  * +2.5R Take Profit: `2334.79`
  * Mathematical Lot Sizing: **`0.34 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2288.67` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2317.31` (Risk Distance: `28.64` pts)
  * +2.5R Take Profit: `2217.08`
  * Mathematical Lot Sizing: **`0.34 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2301.16`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
