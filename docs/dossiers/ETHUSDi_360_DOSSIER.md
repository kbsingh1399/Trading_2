# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 04:16:49 IST` (`2026-10-29 22:46:49 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2268.60` | **Live Ask Quote**: `2271.50` | **Mid Price**: `2270.05`
- **Spread Points**: `290.00` | **Spread BPS**: `12.78 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2313.68` | VWAP Z-Score: `-1.58` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `19.97` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `36.02` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2396.66` | Lower -3.00σ Band: `2230.70`
  * Upper +2.51σ Band: `2383.11` | Lower -2.51σ Band: `2244.26`
  * Upper +2.01σ Band: `2369.28` | Lower -2.01σ Band: `2258.09`
  * Upper +2.00σ Band: `2369.00` | Lower -2.00σ Band: `2258.36`
  * Upper +1.28σ Band: `2349.09` | Lower -1.28σ Band: `2278.28`
  * Upper +1.00σ Band: `2341.34` | Lower -1.00σ Band: `2286.02`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2273.87` | EMA-20=`2291.67` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2310.60` (Slope: `+0.0000`) | EMA-100=`2319.87`
  * Institutional Anchors: EMA-144=`2322.95` | EMA-200=`2324.18` (Slope: `-0.2572`) | EMA-233=`2325.55`
- **Range Boundaries**: 24H High=`2374.90` | 24H Low=`2225.40` | Weekly High=`2387.80` | Weekly Low=`2225.40`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2276.66` (Distance: `-0.40%`)
  * Point of Control (POC) = `2264.95` (Distance: `+0.11%`)
  * Value Area Low (VAL) = `2254.13` (Distance: `+0.60%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2339.52` | POC=`2321.58` | VAL=`2296.66`
  * Prior Day Extremes: PDH=`2374.90` | PDL=`2225.40` | PDC=`2252.70`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2343.95` | Weekly POC=`2310.39` | Weekly VAL=`2299.56`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2289.10` | Low=`2245.20`
  * London Session (08:00-16:00 UTC): High=`2279.13` | Low=`2260.97`
  * New York Session (13:00-21:00 UTC): High=`2283.67` | Low=`2256.43`
  * Initial Balance (First Hour): IB High=`2276.86` | IB Low=`2263.24`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2260.97` - `2279.13`
  * Optimal Trade Entry (OTE 0.705): `2274.59`
  * Structural Invalidation Anchor (0.786): `2288.21`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2268.21` | `2278.48` | `2264.28` | `2276.64` | `27,163` | 61,701,603.26 USD | 4,771,015.57 USD | `+7.73%` | -880,014,262.80 USD | `+0.60` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `2276.64` | `2280.20` | `2270.35` | `2270.35` | `18,018` | 41,019,349.79 USD | -1,382,092.95 USD | `-3.37%` | -881,396,355.75 USD | `+0.13` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `2270.35` | `2278.00` | `2269.00` | `2277.18` | `15,058` | 34,245,911.71 USD | 5,385,698.79 USD | `+15.73%` | -876,010,656.96 USD | `+0.65` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `2272.47` | `2272.73` | `2251.12` | `2265.46` | `140,694` | 318,288,024.78 USD | -14,747,404.45 USD | `-4.63%` | -879,608,401.16 USD | `+0.21` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `2265.46` | `2280.20` | `2256.82` | `2270.35` | `66,193` | 150,284,729.56 USD | 1,306,132.90 USD | `+0.87%` | -878,302,268.26 USD | `+0.45` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `2270.35` | `2278.00` | `2269.00` | `2276.39` | `14,766` | 33,581,580.14 USD | 5,088,196.89 USD | `+15.15%` | -873,214,071.37 USD | `+0.48` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `2335.68` | `2335.92` | `2230.20` | `2256.63` | `1,357,980` | 3,094,453,113.46 USD | -457,917,547.62 USD | `-14.80%` | -830,712,434.27 USD | `-3.95` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2256.63` | `2293.87` | `2245.02` | `2272.46` | `640,507` | 1,454,537,838.20 USD | -31,797,242.40 USD | `-2.19%` | -862,509,676.67 USD | `+0.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `2272.47` | `2280.20` | `2251.12` | `2277.45` | `221,882` | 502,676,594.83 USD | -7,966,174.94 USD | `-1.58%` | -870,475,851.61 USD | `+0.25` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -163,611,405.07 USD | `+1.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -365,767,522.01 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2277.69` | `2,220,464` | 5,051,883,318.23 USD | -497,717,336.52 USD | `-9.85%` | -863,484,858.53 USD | `-1.88` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2308.03` | `2334.83` | `2303.75` | `2309.10` | `525,175` | 1,216,920,375.04 USD | -34,916,746.14 USD | `-2.87%` | -218,489,329.59 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2309.10` | `2330.05` | `2308.88` | `2324.26` | `409,016` | 949,400,649.22 USD | -49,162,247.72 USD | `-5.18%` | -267,651,577.31 USD | `+0.60` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -163,611,405.07 USD | `+1.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -365,767,522.01 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2277.69` | `2,220,464` | 5,051,883,318.23 USD | -497,717,336.52 USD | `-9.85%` | -863,484,858.53 USD | `-1.88` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`2270.05`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2267.40` | `261.6928` | 593,362.25 USD | 6,935,148.15 USD | `12 orders` | `-0.09%` | `-` |
| `BID` | `2267.50` | `265.1450` | 601,216.29 USD | 6,341,785.89 USD | `18 orders` | `-0.08%` | `-` |
| `BID` | `2267.60` | `113.6611` | 257,737.91 USD | 5,740,569.61 USD | `19 orders` | `-0.08%` | `-` |
| `BID` | `2267.70` | `5.6217` | 12,748.33 USD | 5,482,831.70 USD | `12 orders` | `-0.07%` | `-` |
| `BID` | `2267.80` | `20.4305` | 46,332.29 USD | 5,470,083.37 USD | `5 orders` | `-0.07%` | `-` |
| `BID` | `2267.90` | `475.7531` | 1,078,960.46 USD | 5,423,751.08 USD | `12 orders` | `-0.06%` | `-` |
| `BID` | `2268.00` | `155.7106` | 353,151.64 USD | 4,344,790.62 USD | `13 orders` | `-0.06%` | `-` |
| `BID` | `2268.10` | `366.6554` | 831,611.11 USD | 3,991,638.98 USD | `13 orders` | `-0.06%` | `-` |
| `BID` | `2268.20` | `312.2748` | 708,301.70 USD | 3,160,027.87 USD | `11 orders` | `-0.05%` | `-` |
| `BID` | `2268.30` | `4.4817` | 10,165.84 USD | 2,451,726.17 USD | `7 orders` | `-0.05%` | `-` |
| `BID` | `2268.40` | `97.2992` | 220,713.51 USD | 2,441,560.33 USD | `9 orders` | `-0.04%` | `-` |
| `BID` | `2268.50` | `284.5287` | 645,453.36 USD | 2,220,846.82 USD | `12 orders` | `-0.04%` | `-` |
| `BID` | `2268.60` | `171.0399` | 388,021.12 USD | 1,575,393.47 USD | `6 orders` | `-0.03%` | `-` |
| `BID` | `2268.70` | `124.3363` | 282,081.76 USD | 1,187,372.35 USD | `9 orders` | `-0.03%` | `-` |
| `BID` | `2268.80` | `123.6001` | 280,423.91 USD | 905,290.59 USD | `10 orders` | `-0.02%` | `-` |
| `BID` | `2268.90` | `115.6220` | 262,334.76 USD | 624,866.68 USD | `5 orders` | `-0.02%` | `-` |
| `BID` | `2269.00` | `30.2640` | 68,669.02 USD | 362,531.92 USD | `6 orders` | `-0.02%` | `-` |
| `BID` | `2269.10` | `72.7234` | 165,016.67 USD | 293,862.91 USD | `10 orders` | `-0.01%` | `-` |
| `BID` | `2269.20` | `16.6382` | 37,755.40 USD | 128,846.24 USD | `6 orders` | `-0.01%` | `-` |
| `BID` | `2269.30` | `40.1405` | 91,090.84 USD | 91,090.84 USD | `16 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2269.35` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,269.35` | `0.00%` | `-` |
| `ASK` | `2269.40` | `125.0160` | 283,711.31 USD | 283,711.31 USD | `22 orders` | `+0.00%` | `-` |
| `ASK` | `2269.50` | `175.5605` | 398,434.55 USD | 682,145.87 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `2269.60` | `32.7510` | 74,331.67 USD | 756,477.53 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `2269.70` | `34.4380` | 78,163.93 USD | 834,641.46 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `2269.80` | `374.0959` | 849,122.87 USD | 1,683,764.34 USD | `15 orders` | `+0.02%` | `-` |
| `ASK` | `2269.90` | `87.4936` | 198,601.72 USD | 1,882,366.06 USD | `8 orders` | `+0.02%` | `-` |
| `ASK` | `2270.00` | `219.9394` | 499,262.44 USD | 2,381,628.50 USD | `7 orders` | `+0.03%` | `-` |
| `ASK` | `2270.10` | `174.9079` | 397,058.42 USD | 2,778,686.92 USD | `9 orders` | `+0.03%` | `-` |
| `ASK` | `2270.20` | `22.9670` | 52,139.68 USD | 2,830,826.60 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `2270.30` | `39.6548` | 90,028.29 USD | 2,920,854.90 USD | `7 orders` | `+0.04%` | `-` |
| `ASK` | `2270.40` | `90.9957` | 206,596.64 USD | 3,127,451.53 USD | `6 orders` | `+0.05%` | `-` |
| `ASK` | `2270.50` | `444.0780` | 1,008,279.10 USD | 4,135,730.63 USD | `11 orders` | `+0.05%` | `-` |
| `ASK` | `2270.60` | `66.0349` | 149,938.84 USD | 4,285,669.48 USD | `5 orders` | `+0.06%` | `-` |
| `ASK` | `2270.70` | `95.7334` | 217,381.83 USD | 4,503,051.31 USD | `11 orders` | `+0.06%` | `-` |
| `ASK` | `2270.80` | `206.8401` | 469,692.50 USD | 4,972,743.81 USD | `19 orders` | `+0.06%` | `-` |
| `ASK` | `2270.90` | `20.8383` | 47,321.70 USD | 5,020,065.50 USD | `11 orders` | `+0.07%` | `-` |
| `ASK` | `2271.00` | `110.3496` | 250,603.94 USD | 5,270,669.45 USD | `5 orders` | `+0.07%` | `-` |
| `ASK` | `2271.10` | `508.7034` | 1,155,316.29 USD | 6,425,985.74 USD | `8 orders` | `+0.08%` | `-` |
| `ASK` | `2271.20` | `83.3767` | 189,365.16 USD | 6,615,350.90 USD | `5 orders` | `+0.08%` | `-` |
| `ASK` | `2271.30` | `86.0325` | 195,405.62 USD | 6,810,756.52 USD | `6 orders` | `+0.09%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:16:04 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 04:16:04 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1914.18` | `6,500.22` | 12,442,605.92 USD | `AT_RISK_LIQ` | `0xf78c5d8d4b` | `2026-10-30 04:16:04 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1918.00` | `4,184.01` | 8,024,935.59 USD | `TRIGGER_STOP` | `0x6ea486a342` | `2026-10-30 04:16:04 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1925.99` | `8,092.45` | 15,586,021.29 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 04:16:04 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `8,500.00` | 16,371,850.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-30 04:16:04 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2040.72` | `7,964.66` | 16,253,646.32 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-30 04:16:04 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2171.18` | `48,499.51` | 105,301,316.03 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 04:16:04 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2180.25` | `44,734.81` | 97,532,862.28 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2234.20` | `497.80` | 1,112,186.99 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2240.60` | `2,139.93` | 4,794,722.23 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 04:16:04 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2245.00` | `1,758.58` | 3,948,020.86 USD | `TRIGGER_STOP` | `0x28280399d9` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2245.40` | `3,396.04` | 7,625,473.83 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2251.30` | `1,391.40` | 3,132,457.24 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2253.40` | `355.74` | 801,627.67 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2253.90` | `340.62` | 767,714.63 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2257.00` | `497.06` | 1,121,862.16 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2258.70` | `1,752.03` | 3,957,304.74 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2260.10` | `1,038.80` | 2,347,782.39 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2263.40` | `497.06` | 1,125,034.29 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2266.00` | `1,768.14` | 4,006,609.77 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2267.10` | `693.34` | 1,571,877.69 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2267.60` | `338.08` | 766,635.42 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2267.90` | `464.94` | 1,054,444.23 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2268.10` | `1,324.87` | 3,004,942.86 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2268.10` | `286.70` | 650,259.05 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x07fd7e702b` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2268.60` | `893.28` | 2,026,489.79 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2269.40` | `882.76` | 2,003,338.27 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2271.70` | `284.61` | 646,556.94 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x07fd7e702b` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2271.80` | `480.26` | 1,091,044.44 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2272.30` | `661.23` | 1,502,509.75 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2272.50` | `337.89` | 767,857.07 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2272.80` | `440.50` | 1,001,159.54 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2274.20` | `330.31` | 751,185.09 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2278.40` | `329.73` | 751,262.07 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2280.40` | `439.25` | 1,001,662.05 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2280.80` | `286.70` | 653,900.11 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x07fd7e702b` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2280.90` | `325.04` | 741,390.81 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2281.20` | `658.65` | 1,502,516.03 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2283.10` | `470.21` | 1,073,542.84 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2283.70` | `877.21` | 2,003,281.51 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2284.40` | `893.89` | 2,042,006.43 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2284.40` | `286.70` | 654,932.23 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x07fd7e702b` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2284.70` | `247.37` | 565,173.09 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2287.40` | `1,313.73` | 3,005,022.57 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2287.80` | `322.32` | 737,414.68 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2288.60` | `286.70` | 656,136.36 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x07fd7e702b` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2289.80` | `688.40` | 1,576,302.90 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2289.80` | `464.80` | 1,064,292.17 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2289.90` | `1,749.69` | 4,006,620.17 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2292.10` | `1,752.03` | 4,015,822.46 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2292.90` | `497.23` | 1,140,096.37 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2294.80` | `997.45` | 2,288,951.47 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2299.30` | `348.64` | 801,627.49 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2301.00` | `333.64` | 767,714.61 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2301.10` | `497.07` | 1,143,807.78 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2303.60` | `1,443.35` | 3,324,892.31 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 04:16:04 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2305.00` | `1,000.00` | 2,305,000.00 USD | `TRIGGER_STOP` | `0x834cae1ec1` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2312.10` | `3,391.07` | 7,840,496.65 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2316.90` | `497.68` | 1,153,063.21 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 04:16:04 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2317.90` | `2,034.87` | 4,716,629.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 04:16:04 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2389.41` | `17,632.57` | 42,131,523.40 USD | `AT_RISK_LIQ` | `0x8added25f8` | `2026-10-30 04:16:04 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `3,045.71` | 7,656,616.15 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-30 04:16:04 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2585.94` | `6,224.05` | 16,095,020.42 USD | `AT_RISK_LIQ` | `0x08bf75d170` | `2026-10-30 04:16:04 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2658.69` | `9,700.00` | 25,789,336.01 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-30 04:16:04 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2709.05` | `8,500.00` | 23,026,898.55 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-30 04:16:04 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 242,174,785.38 USD | `106,417.71` | `2322.74` | `2279.30` | `3961.03` | 5,006,226.78 USD | `+2.07%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 147,213,091.58 USD | `64,680.62` | `2375.30` | `2279.30` | `4636.22` | 6,423,205.92 USD | `+4.36%` | `5X Cross` |
| `6` | `0x77dd...e0e9` | `LONG` | 110,413,988.79 USD | `48,499.51` | `2610.31` | `2279.30` | `2171.15` | -16,184,895.07 USD | `-14.66%` | `10X Cross` |
| `8` | `0x0392...d7d9` | `LONG` | 101,776,173.97 USD | `44,734.81` | `2518.71` | `2279.30` | `2180.21` | -10,898,132.61 USD | `-10.71%` | `9X Cross` |
| `14` | `0xde8d...9524` | `LONG` | 68,904,580.92 USD | `30,282.40` | `2134.45` | `2279.30` | `1787.10` | 4,268,250.35 USD | `+6.19%` | `20X Cross` |
| `22` | `0xdf95...7d72` | `SHORT` | 51,279,009.23 USD | `22,530.32` | `2402.53` | `2279.30` | `4059.94` | 2,850,864.32 USD | `+5.56%` | `25X Cross` |
| `24` | `0x8add...7d2c` | `SHORT` | 50,178,946.51 USD | `22,046.99` | `2271.09` | `2279.30` | `2439.55` | -108,049.21 USD | `-0.22%` | `25X Cross` |
| `34` | `0xb695...a92d` | `SHORT` | 38,029,736.75 USD | `16,704.62` | `2557.74` | `2279.30` | `3836.15` | 4,696,428.30 USD | `+12.35%` | `20X Cross` |
| `35` | `0xeced...6210` | `SHORT` | 37,982,592.42 USD | `16,687.58` | `2522.09` | `2279.30` | `3477.18` | 4,105,122.58 USD | `+10.81%` | `20X Cross` |
| `36` | `0x7fda...17d1` | `SHORT` | 36,965,931.27 USD | `16,235.92` | `2433.32` | `2279.30` | `4584.44` | 2,541,343.94 USD | `+6.87%` | `25X Cross` |
| `37` | `0xe813...6d74` | `LONG` | 36,416,775.51 USD | `15,979.98` | `2253.24` | `2279.30` | `876.89` | 409,899.21 USD | `+1.13%` | `25X Cross` |
| `38` | `0x6046...b21d` | `LONG` | 36,236,859.33 USD | `15,927.59` | `2410.19` | `2279.30` | `1694.86` | -2,151,760.32 USD | `-5.94%` | `6X Cross` |
| `41` | `0x45d2...4029` | `SHORT` | 31,758,570.00 USD | `13,950.00` | `2443.60` | `2279.30` | `5300.95` | 2,329,712.46 USD | `+7.34%` | `20X Cross` |
| `45` | `0xbd1c...ff0e` | `LONG` | 27,346,800.00 USD | `12,000.00` | `2419.91` | `2279.30` | `1520.98` | -1,692,232.39 USD | `-6.19%` | `20X Cross` |
| `46` | `0x2371...0883` | `LONG` | 27,296,760.00 USD | `12,000.00` | `2421.77` | `2279.30` | `1280.07` | -1,764,534.85 USD | `-6.46%` | `20X Cross` |
| `57` | `0x6c93...59a4` | `LONG` | 25,058,000.00 USD | `11,000.00` | `2441.15` | `2279.30` | `1603.01` | -1,794,672.73 USD | `-7.16%` | `20X Cross` |
| `58` | `0x0c5d...36b3` | `LONG` | 25,033,800.00 USD | `11,000.00` | `2482.20` | `2279.30` | `1645.05` | -2,270,453.24 USD | `-9.07%` | `20X Cross` |
| `59` | `0xa9de...e049` | `LONG` | 25,028,300.00 USD | `11,000.00` | `2481.81` | `2279.30` | `1644.72` | -2,271,679.46 USD | `-9.08%` | `20X Cross` |
| `60` | `0x09dc...c094` | `LONG` | 25,026,100.00 USD | `11,000.00` | `2465.31` | `2279.30` | `1638.04` | -2,092,323.04 USD | `-8.36%` | `20X Cross` |
| `62` | `0xa61c...66b9` | `LONG` | 24,768,022.40 USD | `10,888.00` | `2398.32` | `2279.30` | `1501.62` | -1,344,934.99 USD | `-5.43%` | `10X Cross` |
| `72` | `0xa2ce...3126` | `LONG` | 22,781,379.27 USD | `10,016.88` | `2162.83` | `2279.30` | `1512.67` | 1,116,577.22 USD | `+4.90%` | `10X Cross` |
| `74` | `0x15a4...dfdb` | `LONG` | 22,758,000.00 USD | `10,000.00` | `1761.94` | `2279.30` | `200.36` | 5,138,518.97 USD | `+22.58%` | `20X Cross` |
| `75` | `0x6646...6de5` | `LONG` | 22,749,000.00 USD | `10,000.00` | `1765.80` | `2279.30` | `1721.13` | 5,090,942.55 USD | `+22.38%` | `25X Cross` |
| `76` | `0xec7f...df39` | `LONG` | 22,632,100.00 USD | `10,000.00` | `2719.35` | `2279.30` | `1721.57` | -4,561,448.52 USD | `-20.15%` | `20X Cross` |
| `79` | `0xaeaa...2416` | `SHORT` | 22,077,200.00 USD | `9,700.00` | `2311.92` | `2279.30` | `2658.66` | 348,482.40 USD | `+1.58%` | `25X Cross` |
| `84` | `0xca49...53c8` | `SHORT` | 21,115,420.96 USD | `9,265.62` | `2549.39` | `2279.30` | `3832.74` | 2,506,324.85 USD | `+11.87%` | `25X Cross` |
| `87` | `0xba5d...a352` | `SHORT` | 20,607,181.90 USD | `9,054.12` | `2493.89` | `2279.30` | `2926.14` | 1,972,825.36 USD | `+9.57%` | `20X Cross` |
| `88` | `0xea00...a918` | `LONG` | 20,487,306.36 USD | `9,003.83` | `2003.01` | `2279.30` | `1391.60` | 2,452,527.50 USD | `+11.97%` | `5X Cross` |
| `90` | `0xefe4...194b` | `SHORT` | 20,082,682.20 USD | `8,820.57` | `2267.42` | `2279.30` | `3899.33` | -82,667.81 USD | `-0.41%` | `20X Cross` |
| `97` | `0xb37f...66ca` | `SHORT` | 19,370,650.00 USD | `8,500.00` | `2308.30` | `2279.30` | `2709.01` | 249,904.19 USD | `+1.29%` | `25X Cross` |
| `108` | `0x9eec...daab` | `LONG` | 18,441,889.09 USD | `8,092.45` | `1658.44` | `2279.30` | `1925.67` | 5,021,024.56 USD | `+27.23%` | `15X Cross` |
| `114` | `0x5f91...65aa` | `LONG` | 18,120,388.64 USD | `7,964.66` | `1626.99` | `2279.30` | `2040.68` | 5,161,945.57 USD | `+28.49%` | `16X Cross` |
| `119` | `0xcf53...ee11` | `SHORT` | 17,292,930.93 USD | `7,603.63` | `1862.69` | `2279.30` | `4016.62` | -3,129,666.99 USD | `-18.10%` | `7X Cross` |
| `120` | `0x218a...7da2` | `SHORT` | 17,077,687.56 USD | `7,506.35` | `2208.16` | `2279.30` | `2854.64` | -502,465.57 USD | `-2.94%` | `10X Cross` |
| `124` | `0x939f...04d2` | `LONG` | 16,439,953.40 USD | `7,223.81` | `2500.18` | `2279.30` | `1637.87` | -1,620,936.78 USD | `-9.86%` | `25X Cross` |
| `126` | `0xec0b...b078` | `LONG` | 15,940,640.16 USD | `7,007.80` | `2065.97` | `2279.30` | `1040.92` | 1,462,710.57 USD | `+9.18%` | `25X Cross` |
| `130` | `0x4487...c92d` | `SHORT` | 15,734,559.31 USD | `6,904.45` | `2359.13` | `2279.30` | `2808.88` | 553,992.93 USD | `+3.52%` | `10X Cross` |
| `133` | `0x418a...8888` | `SHORT` | 15,309,402.32 USD | `6,724.38` | `2494.55` | `2279.30` | `2999.39` | 1,464,920.85 USD | `+9.57%` | `25X Cross` |
| `136` | `0x4ff9...38d3` | `LONG` | 14,939,888.64 USD | `6,564.10` | `2447.40` | `2279.30` | `1670.66` | -1,125,134.10 USD | `-7.53%` | `3X Isolated` |
| `138` | `0xf78c...c581` | `LONG` | 14,788,653.93 USD | `6,500.22` | `2521.53` | `2279.30` | `1914.14` | -1,601,887.01 USD | `-10.83%` | `20X Cross` |
| `143` | `0x799f...5f4c` | `LONG` | 14,353,518.47 USD | `6,310.90` | `2390.33` | `2279.30` | `1803.87` | -731,646.15 USD | `-5.10%` | `20X Cross` |
| `145` | `0xecb6...2b00` | `SHORT` | 14,183,964.93 USD | `6,229.78` | `2280.16` | `2279.30` | `6915.20` | 20,986.31 USD | `+0.15%` | `15X Cross` |
| `146` | `0x08bf...7872` | `SHORT` | 14,178,379.98 USD | `6,224.05` | `2258.00` | `2279.30` | `2585.91` | -124,463.87 USD | `-0.88%` | `20X Cross` |
| `150` | `0xc179...e0c8` | `LONG` | 13,917,028.41 USD | `6,113.61` | `2322.20` | `2279.30` | `1147.38` | -280,022.08 USD | `-2.01%` | `10X Cross` |
| `152` | `0x0c4a...1b19` | `LONG` | 13,852,632.07 USD | `6,086.13` | `2373.06` | `2279.30` | `2135.30` | -590,118.50 USD | `-4.26%` | `25X Isolated` |
| `154` | `0xd9e7...4aff` | `LONG` | 13,650,600.00 USD | `6,000.00` | `2480.18` | `2279.30` | `1408.43` | -1,230,524.33 USD | `-9.01%` | `20X Cross` |
| `160` | `0x0622...8088` | `LONG` | 13,124,095.17 USD | `5,764.27` | `2271.71` | `2279.30` | `516.93` | 29,287.05 USD | `+0.22%` | `5X Cross` |
| `167` | `0x1ee7...edf5` | `LONG` | 12,513,050.00 USD | `5,500.00` | `2316.93` | `2279.30` | `2127.33` | -230,089.62 USD | `-1.84%` | `25X Cross` |
| `187` | `0x45ab...6cbc` | `LONG` | 11,195,681.10 USD | `4,920.96` | `2727.66` | `2279.30` | `1384.32` | -2,227,062.70 USD | `-19.89%` | `7X Cross` |
| `189` | `0x645b...87b8` | `SHORT` | 11,142,741.11 USD | `4,895.76` | `2421.64` | `2279.30` | `6633.32` | 713,046.45 USD | `+6.40%` | `10X Cross` |
| `192` | `0x64b7...9da9` | `LONG` | 11,048,337.81 USD | `4,856.84` | `2604.61` | `2279.30` | `1541.01` | -1,601,876.60 USD | `-14.50%` | `25X Cross` |
| `193` | `0xfb18...eb17` | `SHORT` | 11,043,301.00 USD | `4,845.89` | `2315.54` | `2279.30` | `2625.89` | 177,581.79 USD | `+1.61%` | `25X Cross` |
| `198` | `0x5559...d43b` | `SHORT` | 10,823,534.80 USD | `4,755.93` | `2262.69` | `2279.30` | `2800.56` | -62,328.92 USD | `-0.58%` | `25X Cross` |
| `202` | `0x12d2...f97f` | `LONG` | 10,711,544.35 USD | `4,708.79` | `2588.61` | `2279.30` | `1996.81` | -1,477,689.97 USD | `-13.80%` | `20X Cross` |
| `213` | `0xe091...6705` | `SHORT` | 10,241,100.46 USD | `4,500.00` | `2467.33` | `2279.30` | `2572.96` | 861,908.05 USD | `+8.42%` | `20X Cross` |
| `229` | `0xb829...3a81` | `LONG` | 9,749,763.96 USD | `4,282.22` | `2401.77` | `2279.30` | `1502.28` | -535,162.19 USD | `-5.49%` | `20X Cross` |
| `237` | `0x28bb...fca6` | `SHORT` | 9,578,135.19 USD | `4,209.61` | `1896.10` | `2279.30` | `3039.02` | -1,596,252.63 USD | `-16.67%` | `20X Cross` |
| `239` | `0x6ea4...0ea7` | `SHORT` | 9,523,230.40 USD | `4,184.01` | `2602.13` | `2279.30` | `3425.97` | 1,364,116.27 USD | `+14.32%` | `20X Cross` |
| `252` | `0x5e9e...35ee` | `SHORT` | 9,116,788.46 USD | `4,007.56` | `1796.39` | `2279.30` | `2586.46` | -1,917,638.37 USD | `-21.03%` | `20X Cross` |
| `253` | `0xfb94...0ddf` | `SHORT` | 9,105,180.67 USD | `4,002.10` | `2382.44` | `2279.30` | `5105.36` | 429,603.48 USD | `+4.72%` | `20X Cross` |
| `254` | `0x3dc9...54b0` | `SHORT` | 9,099,695.17 USD | `3,999.69` | `2480.32` | `2279.30` | `6459.49` | 820,841.38 USD | `+9.02%` | `20X Cross` |
| `255` | `0x8cc9...2b6a` | `SHORT` | 9,097,600.00 USD | `4,000.00` | `1791.18` | `2279.30` | `3832.47` | -1,932,853.33 USD | `-21.25%` | `25X Cross` |
| `267` | `0xf02d...5eb3` | `LONG` | 8,770,053.42 USD | `3,855.99` | `2513.67` | `2279.30` | `318.85` | -922,658.89 USD | `-10.52%` | `20X Cross` |
| `271` | `0x4b67...f4e7` | `LONG` | 8,692,797.41 USD | `3,820.84` | `2591.51` | `2279.30` | `1646.90` | -1,208,976.14 USD | `-13.91%` | `20X Cross` |
| `292` | `0x8ae4...3d60` | `LONG` | 8,096,680.23 USD | `3,558.20` | `2482.21` | `2279.30` | `480.49` | -735,517.80 USD | `-9.08%` | `10X Cross` |
| `314` | `0xfe7c...b7ae` | `SHORT` | 7,746,319.55 USD | `3,402.58` | `2440.17` | `2279.30` | `5107.70` | 556,589.72 USD | `+7.19%` | `25X Cross` |
| `330` | `0xbc76...417c` | `LONG` | 7,071,331.58 USD | `3,109.10` | `2263.46` | `2279.30` | `2216.94` | 34,006.51 USD | `+0.48%` | `25X Cross` |
| `335` | `0x9c2a...f6a8` | `SHORT` | 6,929,300.05 USD | `3,045.71` | `2543.83` | `2279.30` | `2601.79` | 818,486.49 USD | `+11.81%` | `20X Cross` |
| `339` | `0x4a20...3c26` | `LONG` | 6,836,700.00 USD | `3,000.00` | `2428.72` | `2279.30` | `505.41` | -449,460.28 USD | `-6.57%` | `20X Cross` |
| `340` | `0x007d...67a0` | `LONG` | 6,827,700.00 USD | `3,000.00` | `2400.00` | `2279.30` | `1474.80` | -372,300.00 USD | `-5.45%` | `25X Cross` |
| `381` | `0xf517...c032` | `SHORT` | 6,233,490.84 USD | `2,738.07` | `2053.90` | `2279.30` | `5394.65` | -609,748.94 USD | `-9.78%` | `25X Cross` |
| `398` | `0x8328...f54a` | `SHORT` | 5,861,683.90 USD | `2,576.45` | `2292.01` | `2279.30` | `3280.20` | 43,587.39 USD | `+0.74%` | `25X Cross` |
| `400` | `0xed48...7c9b` | `SHORT` | 5,813,005.96 USD | `2,551.13` | `2460.02` | `2279.30` | `3238.39` | 462,840.45 USD | `+7.96%` | `20X Cross` |
| `415` | `0xfbe2...c8ea` | `SHORT` | 5,478,650.62 USD | `2,404.08` | `2041.57` | `2279.30` | `2609.03` | -570,557.89 USD | `-10.41%` | `20X Cross` |
| `420` | `0x1c98...7fc7` | `LONG` | 5,362,573.83 USD | `2,358.00` | `2467.15` | `2279.30` | `1897.18` | -454,997.65 USD | `-8.48%` | `10X Cross` |
| `425` | `0x77ee...2902` | `SHORT` | 5,213,842.24 USD | `2,290.69` | `2476.53` | `2279.30` | `5834.18` | 459,130.00 USD | `+8.81%` | `25X Cross` |
| `431` | `0x023a...2355` | `LONG` | 5,078,156.15 USD | `2,232.35` | `2330.15` | `2279.30` | `0.000000` | -123,572.58 USD | `-2.43%` | `25X Cross` |
| `433` | `0x6859...7e1e` | `SHORT` | 5,065,298.02 USD | `2,224.35` | `2200.39` | `2279.30` | `3517.62` | -170,841.26 USD | `-3.37%` | `25X Cross` |
| `443` | `0xd507...c948` | `SHORT` | 4,940,648.17 USD | `2,172.00` | `2387.49` | `2279.30` | `2707.39` | 244,992.85 USD | `+4.96%` | `5X Isolated` |
| `454` | `0x382b...3e39` | `SHORT` | 4,848,540.31 USD | `2,129.54` | `2296.66` | `2279.30` | `4636.83` | 42,296.90 USD | `+0.87%` | `25X Cross` |
| `483` | `0xf929...d1f9` | `SHORT` | 4,551,600.00 USD | `2,000.00` | `2423.37` | `2279.30` | `2548.79` | 295,140.34 USD | `+6.48%` | `25X Cross` |
| `484` | `0x7a6d...f79c` | `SHORT` | 4,551,600.00 USD | `2,000.00` | `2418.41` | `2279.30` | `2656.04` | 285,232.11 USD | `+6.27%` | `25X Cross` |
| `485` | `0xbb34...1696` | `LONG` | 4,550,200.00 USD | `2,000.00` | `2318.80` | `2279.30` | `1949.87` | -87,416.04 USD | `-1.92%` | `25X Cross` |
| `486` | `0x3440...32c5` | `SHORT` | 4,550,085.49 USD | `2,000.57` | `2198.21` | `2279.30` | `3631.20` | -152,422.36 USD | `-3.35%` | `25X Cross` |
| `487` | `0xc619...10f5` | `LONG` | 4,548,400.00 USD | `2,000.00` | `2318.40` | `2279.30` | `1793.07` | -88,406.86 USD | `-1.94%` | `25X Cross` |
| `500` | `0x0514...bdfe` | `SHORT` | 4,434,885.00 USD | `1,950.00` | `1988.74` | `2279.30` | `3055.15` | -556,825.37 USD | `-12.56%` | `25X Cross` |
| `509` | `0x8376...9a1e` | `SHORT` | 4,346,569.45 USD | `1,910.50` | `2477.72` | `2279.30` | `3179.62` | 387,118.72 USD | `+8.91%` | `20X Cross` |
| `515` | `0xfc27...9d9d` | `SHORT` | 4,251,237.47 USD | `1,867.36` | `2341.25` | `2279.30` | `11506.11` | 120,736.28 USD | `+2.84%` | `25X Cross` |
| `536` | `0x541e...071d` | `SHORT` | 4,108,360.50 USD | `1,805.00` | `2648.19` | `2279.30` | `3149.28` | 671,624.34 USD | `+16.35%` | `25X Cross` |
| `538` | `0x7265...91a5` | `LONG` | 4,100,694.38 USD | `1,801.87` | `2533.96` | `2279.30` | `1988.11` | -465,172.08 USD | `-11.34%` | `20X Cross` |
| `539` | `0x739c...cfb2` | `SHORT` | 4,095,180.00 USD | `1,800.00` | `2427.60` | `2279.30` | `2512.70` | 274,516.38 USD | `+6.70%` | `25X Cross` |
| `541` | `0xb15b...dbae` | `SHORT` | 4,092,049.88 USD | `1,797.68` | `2294.54` | `2279.30` | `2302.38` | 32,794.09 USD | `+0.80%` | `25X Cross` |
| `545` | `0xa445...329d` | `LONG` | 4,044,947.46 USD | `1,776.75` | `2398.85` | `2279.30` | `1944.48` | -217,221.90 USD | `-5.37%` | `25X Cross` |
| `550` | `0x91a9...3f70` | `SHORT` | 4,022,784.48 USD | `1,767.48` | `2156.23` | `2279.30` | `3659.58` | -211,680.40 USD | `-5.26%` | `4X Cross` |
| `555` | `0x2828...93a0` | `LONG` | 4,001,305.95 USD | `1,758.58` | `2314.00` | `2279.30` | `2241.71` | -68,060.91 USD | `-1.70%` | `25X Cross` |
| `557` | `0x3453...b323` | `SHORT` | 3,981,705.06 USD | `1,750.12` | `2328.82` | `2279.30` | `2434.62` | 94,027.07 USD | `+2.36%` | `25X Cross` |
| `587` | `0xfeec...4e9c` | `SHORT` | 3,847,849.93 USD | `1,691.81` | `2566.49` | `2279.30` | `2654.21` | 494,174.58 USD | `+12.84%` | `10X Cross` |
| `588` | `0x936c...bb0f` | `SHORT` | 3,847,839.92 USD | `1,688.69` | `2434.60` | `2279.30` | `4488.74` | 263,447.19 USD | `+6.85%` | `20X Cross` |
| `610` | `0xeee0...0b53` | `LONG` | 3,724,620.58 USD | `1,637.12` | `2468.64` | `2279.30` | `202.19` | -316,855.48 USD | `-8.51%` | `7X Cross` |
| `614` | `0x27b8...12fc` | `LONG` | 3,704,461.66 USD | `1,628.12` | `2468.73` | `2279.30` | `571.06` | -314,932.97 USD | `-8.50%` | `10X Cross` |
| `616` | `0x982b...4606` | `LONG` | 3,702,636.17 USD | `1,626.82` | `2575.24` | `2279.30` | `1548.39` | -486,816.90 USD | `-13.15%` | `5X Isolated` |
| `628` | `0x73d7...8be1` | `LONG` | 3,649,579.73 USD | `1,601.47` | `2410.40` | `2279.30` | `2015.95` | -210,599.19 USD | `-5.77%` | `25X Cross` |
| `648` | `0xe170...9300` | `SHORT` | 3,490,478.42 USD | `1,533.40` | `2076.39` | `2279.30` | `3150.74` | -306,528.92 USD | `-8.78%` | `25X Cross` |
| `651` | `0x4b86...df9d` | `SHORT` | 3,468,319.20 USD | `1,524.00` | `2287.40` | `2279.30` | `2760.56` | 17,678.40 USD | `+0.51%` | `9X Isolated` |
| `660` | `0xad54...6203` | `LONG` | 3,437,419.58 USD | `1,510.29` | `2614.66` | `2279.30` | `2124.61` | -511,486.96 USD | `-14.88%` | `10X Isolated` |
| `664` | `0x2e2b...2fab` | `LONG` | 3,429,433.41 USD | `1,507.38` | `2245.53` | `2279.30` | `1223.16` | 44,560.31 USD | `+1.30%` | `25X Cross` |
| `669` | `0x39b4...5c34` | `SHORT` | 3,412,575.00 USD | `1,500.00` | `2329.97` | `2279.30` | `2553.86` | 82,384.99 USD | `+2.41%` | `25X Cross` |
| `671` | `0x251f...6e5d` | `LONG` | 3,412,050.00 USD | `1,500.00` | `2346.68` | `2279.30` | `1855.76` | -107,980.49 USD | `-3.16%` | `20X Cross` |
| `683` | `0xb885...3c54` | `LONG` | 3,300,060.01 USD | `1,450.00` | `2274.34` | `2279.30` | `40.14` | 2,251.87 USD | `+0.07%` | `20X Cross` |
| `687` | `0xef70...a84c` | `SHORT` | 3,281,952.69 USD | `1,442.74` | `2424.73` | `2279.30` | `3292.63` | 216,318.14 USD | `+6.59%` | `25X Cross` |
| `694` | `0x4b5f...0dd8` | `LONG` | 3,257,844.92 USD | `1,431.96` | `2339.45` | `2279.30` | `2148.67` | -92,148.03 USD | `-2.83%` | `10X Cross` |
| `695` | `0xbadb...9ee6` | `LONG` | 3,250,206.53 USD | `1,428.16` | `1936.00` | `2279.30` | `1067.34` | 485,284.88 USD | `+14.93%` | `20X Cross` |
| `727` | `0xa0fb...96be` | `LONG` | 3,131,389.82 USD | `1,376.25` | `2293.96` | `2279.30` | `1549.91` | -25,685.07 USD | `-0.82%` | `3X Cross` |
| `757` | `0x880a...311c` | `SHORT` | 3,004,959.80 USD | `1,320.22` | `2425.76` | `2279.30` | `8357.41` | 197,589.36 USD | `+6.58%` | `9X Cross` |
| `760` | `0x0dd5...f6ee` | `LONG` | 2,993,334.50 USD | `1,315.00` | `2306.05` | `2279.30` | `1654.16` | -39,129.88 USD | `-1.31%` | `5X Cross` |
| `800` | `0xc435...c905` | `SHORT` | 2,840,448.00 USD | `1,248.00` | `2704.38` | `2279.30` | `4218.44` | 534,622.35 USD | `+18.82%` | `20X Cross` |
| `812` | `0x7178...0854` | `LONG` | 2,773,970.88 USD | `1,218.63` | `2461.81` | `2279.30` | `1146.71` | -226,075.52 USD | `-8.15%` | `10X Cross` |
| `829` | `0xaaa1...ab8c` | `SHORT` | 2,730,120.00 USD | `1,200.00` | `2276.29` | `2279.30` | `2366.18` | 1,437.58 USD | `+0.05%` | `25X Isolated` |
| `847` | `0x07fd...689d` | `LONG` | 2,653,890.95 USD | `1,166.49` | `2419.97` | `2279.30` | `0.000000` | -169,000.85 USD | `-6.37%` | `25X Cross` |
| `888` | `0xbef3...0d3e` | `LONG` | 2,511,694.47 USD | `1,103.99` | `2315.08` | `2279.30` | `2162.34` | -44,141.69 USD | `-1.76%` | `20X Cross` |
| `894` | `0x6a41...a3b9` | `LONG` | 2,503,657.31 USD | `1,099.06` | `2314.77` | `2279.30` | `2164.18` | -40,415.38 USD | `-1.61%` | `20X Cross` |
| `904` | `0x2f80...f203` | `SHORT` | 2,477,667.68 USD | `1,088.94` | `1984.00` | `2279.30` | `3063.20` | -317,200.50 USD | `-12.80%` | `20X Cross` |
| `914` | `0x6f11...0389` | `SHORT` | 2,454,832.90 USD | `1,079.00` | `2333.39` | `2279.30` | `3199.66` | 62,896.01 USD | `+2.56%` | `25X Cross` |
| `917` | `0x2b61...2f6c` | `SHORT` | 2,450,442.89 USD | `1,076.60` | `2681.75` | `2279.30` | `6450.60` | 436,729.85 USD | `+17.82%` | `10X Cross` |
| `952` | `0x30af...393e` | `SHORT` | 2,368,754.26 USD | `1,041.16` | `2252.26` | `2279.30` | `2297.87` | -23,771.94 USD | `-1.00%` | `25X Cross` |
| `962` | `0x1b2a...f7a6` | `LONG` | 2,333,532.49 USD | `1,025.37` | `2737.51` | `2279.30` | `883.05` | -473,427.44 USD | `-20.29%` | `10X Cross` |
| `976` | `0x001a...fef6` | `SHORT` | 2,294,686.35 USD | `1,007.33` | `2022.19` | `2279.30` | `3071.24` | -257,678.39 USD | `-11.23%` | `10X Cross` |
| `978` | `0x02aa...1806` | `SHORT` | 2,290,951.31 USD | `1,007.10` | `2654.68` | `2279.30` | `3613.65` | 382,580.79 USD | `+16.70%` | `20X Cross` |
| `979` | `0xdb3a...cf3b` | `LONG` | 2,282,515.00 USD | `1,003.22` | `2705.01` | `2279.30` | `0.000000` | -431,191.90 USD | `-18.89%` | `4X Cross` |
| `981` | `0x5272...fcd9` | `SHORT` | 2,278,000.00 USD | `1,000.00` | `2241.82` | `2279.30` | `2831.71` | -36,175.51 USD | `-1.59%` | `5X Cross` |
| `982` | `0x7743...e4fe` | `SHORT` | 2,276,365.41 USD | `1,000.56` | `2298.56` | `2279.30` | `4974.43` | 23,479.66 USD | `+1.03%` | `25X Cross` |
| `983` | `0x834c...dd93` | `SHORT` | 2,275,800.00 USD | `1,000.00` | `2249.68` | `2279.30` | `2310.88` | -26,114.58 USD | `-1.15%` | `25X Cross` |
| `1009` | `0x1f16...6d07` | `LONG` | 2,200,548.00 USD | `966.00` | `2278.41` | `2279.30` | `1645.01` | -401.14 USD | `-0.02%` | `7X Cross` |
| `1012` | `0xb002...ed8a` | `SHORT` | 2,190,429.88 USD | `962.78` | `2299.66` | `2279.30` | `4200.91` | 23,648.03 USD | `+1.08%` | `25X Cross` |
| `1057` | `0x9606...4e5d` | `SHORT` | 2,077,980.49 USD | `913.00` | `2478.70` | `2279.30` | `4301.21` | 185,073.12 USD | `+8.91%` | `20X Cross` |
| `1069` | `0x5f10...d49d` | `LONG` | 2,050,200.00 USD | `900.00` | `2249.83` | `2279.30` | `1799.10` | 25,346.53 USD | `+1.24%` | `25X Cross` |
| `1088` | `0x2e30...4cb5` | `SHORT` | 2,017,964.35 USD | `885.50` | `2340.00` | `2279.30` | `7853.59` | 54,107.49 USD | `+2.68%` | `2X Cross` |
| `1102` | `0xb1ec...e86a` | `SHORT` | 2,000,207.94 USD | `879.34` | `2273.00` | `2279.30` | `13346.92` | -1,454.00 USD | `-0.07%` | `25X Cross` |
| `1177` | `0xcd27...52a8` | `LONG` | 1,905,486.09 USD | `837.21` | `2553.56` | `2279.30` | `1404.20` | -232,378.68 USD | `-12.20%` | `2X Cross` |
| `1199` | `0x7b7f...dee2` | `LONG` | 1,853,884.63 USD | `814.25` | `2268.61` | `2279.30` | `0.000000` | 6,661.25 USD | `+0.36%` | `20X Cross` |
| `1200` | `0x6ff1...8575` | `LONG` | 1,852,791.23 USD | `814.06` | `2272.53` | `2279.30` | `2227.08` | 2,821.47 USD | `+0.15%` | `25X Isolated` |
| `1222` | `0x3fc5...c0c1` | `SHORT` | 1,831,215.50 USD | `804.26` | `2702.11` | `2279.30` | `4958.89` | 341,986.03 USD | `+18.68%` | `25X Cross` |
| `1228` | `0x6e6f...82a6` | `LONG` | 1,822,730.04 USD | `801.16` | `2267.14` | `2279.30` | `979.20` | 6,375.16 USD | `+0.35%` | `20X Cross` |
| `1230` | `0x7737...bf66` | `SHORT` | 1,820,566.30 USD | `799.79` | `2494.83` | `2279.30` | `23683.43` | 174,779.73 USD | `+9.60%` | `15X Cross` |
| `1232` | `0x04a9...95aa` | `LONG` | 1,820,080.00 USD | `800.00` | `2595.13` | `2279.30` | `1878.59` | -256,026.74 USD | `-14.07%` | `5X Cross` |
| `1234` | `0xa70a...4be9` | `LONG` | 1,817,143.15 USD | `798.39` | `2268.84` | `2279.30` | `419.84` | 5,714.87 USD | `+0.31%` | `20X Cross` |
| `1248` | `0x0a97...347d` | `LONG` | 1,798,941.46 USD | `790.95` | `2268.87` | `2279.30` | `1301.24` | 4,369.34 USD | `+0.24%` | `20X Cross` |
| `1249` | `0xf83f...625f` | `SHORT` | 1,797,210.81 USD | `790.02` | `2595.19` | `2279.30` | `6172.38` | 253,035.68 USD | `+14.08%` | `20X Cross` |
| `1266` | `0x31de...13f2` | `LONG` | 1,770,172.16 USD | `777.48` | `2273.48` | `2279.30` | `0.000000` | 2,580.26 USD | `+0.15%` | `20X Cross` |
| `1269` | `0x458d...ab3b` | `LONG` | 1,762,626.90 USD | `774.75` | `2740.41` | `2279.30` | `1887.95` | -360,502.28 USD | `-20.45%` | `3X Isolated` |
| `1327` | `0xaa53...9cb7` | `LONG` | 1,663,707.00 USD | `730.34` | `2389.70` | `2279.30` | `1940.75` | -81,582.63 USD | `-4.90%` | `20X Cross` |
| `1352` | `0xa189...94d7` | `SHORT` | 1,640,760.14 USD | `719.98` | `2691.84` | `2279.30` | `3051.91` | 297,312.52 USD | `+18.12%` | `25X Cross` |
| `1374` | `0x2f93...4404` | `LONG` | 1,612,256.80 USD | `707.47` | `1700.45` | `2279.30` | `1369.59` | 409,230.43 USD | `+25.38%` | `4X Isolated` |
| `1385` | `0x5605...fe0f` | `SHORT` | 1,597,446.90 USD | `702.14` | `2566.90` | `2279.30` | `3063.08` | 204,885.74 USD | `+12.83%` | `20X Cross` |
| `1387` | `0x0deb...0bc5` | `LONG` | 1,594,600.00 USD | `700.00` | `2071.05` | `2279.30` | `1598.18` | 144,864.21 USD | `+9.08%` | `20X Cross` |
| `1428` | `0xd911...961e` | `LONG` | 1,552,308.96 USD | `682.42` | `2268.00` | `2279.30` | `0.000000` | 4,566.58 USD | `+0.29%` | `25X Cross` |
| `1429` | `0xdbd1...29dd` | `SHORT` | 1,551,252.93 USD | `680.70` | `3030.57` | `2279.30` | `4104.60` | 511,668.20 USD | `+32.98%` | `6X Cross` |
| `1438` | `0x71e5...be04` | `LONG` | 1,543,724.97 USD | `677.67` | `2727.27` | `2279.30` | `1471.73` | -304,460.64 USD | `-19.72%` | `20X Cross` |
| `1446` | `0x0b23...f37b` | `LONG` | 1,535,962.50 USD | `675.00` | `2238.15` | `2279.30` | `596.34` | 25,205.86 USD | `+1.64%` | `5X Cross` |
| `1448` | `0xb8eb...1dd5` | `LONG` | 1,533,883.34 USD | `674.41` | `2267.05` | `2279.30` | `0.000000` | 4,954.84 USD | `+0.32%` | `25X Cross` |
| `1464` | `0x51a0...3543` | `SHORT` | 1,508,459.29 USD | `662.77` | `2627.71` | `2279.30` | `7940.99` | 233,102.49 USD | `+15.45%` | `20X Cross` |
| `1470` | `0x0cac...6170` | `SHORT` | 1,498,376.75 USD | `657.50` | `2146.55` | `2279.30` | `2840.15` | -87,014.55 USD | `-5.81%` | `20X Cross` |
| `1477` | `0x4b1c...bc38` | `SHORT` | 1,489,722.35 USD | `654.36` | `2528.62` | `2279.30` | `4514.22` | 164,913.19 USD | `+11.07%` | `10X Cross` |
| `1493` | `0x621c...63ab` | `LONG` | 1,462,844.94 USD | `642.98` | `2281.90` | `2279.30` | `0.000000` | -4,378.47 USD | `-0.30%` | `20X Cross` |
| `1494` | `0xf00e...fe3d` | `SHORT` | 1,462,166.27 USD | `642.88` | `2333.21` | `2279.30` | `2542.45` | 37,811.70 USD | `+2.59%` | `20X Cross` |
| `1499` | `0xffb2...5ed6` | `SHORT` | 1,458,385.24 USD | `640.77` | `2672.96` | `2279.30` | `2507.14` | 254,363.11 USD | `+17.44%` | `20X Cross` |
| `1533` | `0x871f...972b` | `SHORT` | 1,425,702.57 USD | `626.77` | `2279.80` | `2279.30` | `2581.94` | 3,199.25 USD | `+0.22%` | `20X Cross` |
| `1542` | `0xfce0...f4c0` | `SHORT` | 1,418,752.36 USD | `623.60` | `3129.61` | `2279.30` | `2788.40` | 532,874.22 USD | `+37.56%` | `20X Cross` |
| `1562` | `0x7663...cb5a` | `SHORT` | 1,398,191.29 USD | `613.54` | `2342.35` | `2279.30` | `3769.66` | 38,929.19 USD | `+2.78%` | `3X Cross` |
| `1594` | `0xad02...eb65` | `LONG` | 1,366,531.08 USD | `600.62` | `2460.69` | `2279.30` | `1079.65` | -111,409.48 USD | `-8.15%` | `5X Cross` |
| `1596` | `0x638f...f5f0` | `LONG` | 1,365,960.00 USD | `600.00` | `4011.50` | `2279.30` | `292.81` | -1,040,943.53 USD | `-76.21%` | `25X Cross` |
| `1597` | `0x67c3...609d` | `SHORT` | 1,365,660.00 USD | `600.00` | `2386.55` | `2279.30` | `2560.74` | 66,271.89 USD | `+4.85%` | `25X Cross` |
| `1598` | `0x26e6...6b28` | `LONG` | 1,365,060.00 USD | `600.00` | `1769.78` | `2279.30` | `2005.45` | 303,188.47 USD | `+22.21%` | `20X Cross` |
| `1603` | `0x7c90...d129` | `LONG` | 1,351,918.41 USD | `594.17` | `2286.01` | `2279.30` | `1844.84` | -6,364.47 USD | `-0.47%` | `20X Cross` |
| `1632` | `0x2577...4897` | `LONG` | 1,319,161.75 USD | `579.39` | `2298.03` | `2279.30` | `0.000000` | -12,305.25 USD | `-0.93%` | `15X Cross` |
| `1634` | `0xac48...3201` | `SHORT` | 1,316,423.68 USD | `578.19` | `2275.50` | `2279.30` | `5155.39` | -749.60 USD | `-0.06%` | `20X Cross` |
| `1635` | `0xab81...c608` | `SHORT` | 1,315,545.16 USD | `577.27` | `2285.37` | `2279.30` | `5998.20` | 3,736.13 USD | `+0.28%` | `20X Cross` |
| `1654` | `0xfc66...ca06` | `SHORT` | 1,290,058.70 USD | `567.43` | `2275.19` | `2279.30` | `9021.88` | 964.51 USD | `+0.07%` | `20X Cross` |
| `1657` | `0xfb99...37f3` | `LONG` | 1,286,207.54 USD | `565.34` | `2362.35` | `2279.30` | `1235.49` | -49,328.82 USD | `-3.84%` | `3X Cross` |
| `1665` | `0x844b...7f42` | `SHORT` | 1,275,826.20 USD | `561.00` | `2026.17` | `2279.30` | `3210.32` | -139,142.79 USD | `-10.91%` | `25X Cross` |
| `1677` | `0xabe6...1d99` | `SHORT` | 1,264,742.30 USD | `556.00` | `2484.68` | `2279.30` | `3095.41` | 116,753.59 USD | `+9.23%` | `20X Cross` |
| `1706` | `0xd6e1...f256` | `SHORT` | 1,242,086.55 USD | `545.59` | `2258.34` | `2279.30` | `3299.29` | -9,961.07 USD | `-0.80%` | `25X Cross` |
| `1731` | `0xad21...fb6a` | `LONG` | 1,211,917.39 USD | `531.87` | `2574.89` | `2279.30` | `1703.78` | -157,588.11 USD | `-13.00%` | `7X Cross` |
| `1735` | `0xf910...0a2d` | `LONG` | 1,208,886.54 USD | `530.96` | `2268.53` | `2279.30` | `0.000000` | 4,387.88 USD | `+0.36%` | `5X Cross` |
| `1747` | `0x0082...1ae3` | `LONG` | 1,201,252.80 USD | `528.00` | `2448.58` | `2279.30` | `2234.21` | -91,602.11 USD | `-7.63%` | `25X Cross` |
| `1793` | `0x0c7a...2f50` | `SHORT` | 1,160,060.79 USD | `509.25` | `2122.56` | `2279.30` | `4103.46` | -79,155.36 USD | `-6.82%` | `20X Cross` |
| `1798` | `0x0089...2410` | `SHORT` | 1,155,733.28 USD | `507.35` | `2308.88` | `2279.30` | `3341.05` | 15,666.98 USD | `+1.36%` | `20X Cross` |
| `1816` | `0xa559...ff95` | `LONG` | 1,137,550.00 USD | `500.00` | `2260.68` | `2279.30` | `1118.99` | 7,205.64 USD | `+0.63%` | `20X Cross` |
| `1817` | `0x6936...9417` | `SHORT` | 1,137,550.00 USD | `500.00` | `2315.11` | `2279.30` | `2359.66` | 20,005.21 USD | `+1.76%` | `25X Isolated` |
| `1818` | `0xb322...d51f` | `SHORT` | 1,137,400.00 USD | `500.00` | `2268.03` | `2279.30` | `3752.61` | -3,383.68 USD | `-0.30%` | `20X Cross` |
| `1819` | `0x89b2...9ca6` | `LONG` | 1,137,150.00 USD | `500.00` | `2484.03` | `2279.30` | `1954.18` | -104,869.35 USD | `-9.22%` | `25X Cross` |
| `1821` | `0x7298...7d6c` | `SHORT` | 1,133,339.47 USD | `498.15` | `3426.75` | `2279.30` | `5422.37` | 573,696.35 USD | `+50.62%` | `20X Cross` |
| `1830` | `0x536c...3e1f` | `LONG` | 1,125,688.54 USD | `494.83` | `2275.87` | `2279.30` | `2128.74` | -483.78 USD | `-0.04%` | `20X Cross` |
| `1835` | `0x9c68...7783` | `SHORT` | 1,122,965.88 USD | `493.31` | `2273.58` | `2279.30` | `3886.43` | -1,386.63 USD | `-0.12%` | `25X Cross` |
| `1846` | `0xc10f...23b3` | `LONG` | 1,115,093.00 USD | `490.00` | `2383.92` | `2279.30` | `2083.94` | -53,028.28 USD | `-4.76%` | `25X Cross` |
| `1848` | `0x404c...5f03` | `SHORT` | 1,113,918.71 USD | `489.79` | `2671.94` | `2279.30` | `4978.70` | 194,760.85 USD | `+17.48%` | `20X Cross` |
| `1851` | `0x321f...1c84` | `SHORT` | 1,110,869.46 USD | `488.02` | `2370.09` | `2279.30` | `3032.51` | 45,775.15 USD | `+4.12%` | `10X Cross` |
| `1855` | `0xa522...2d0e` | `SHORT` | 1,108,421.28 USD | `486.36` | `2284.42` | `2279.30` | `5004.81` | 2,640.27 USD | `+0.24%` | `20X Cross` |
| `1869` | `0x8923...1bac` | `SHORT` | 1,094,002.92 USD | `480.82` | `2277.43` | `2279.30` | `3130.66` | 1,025.12 USD | `+0.09%` | `25X Cross` |
| `1902` | `0xd4c1...3d1d` | `SHORT` | 1,065,564.26 USD | `468.01` | `2334.05` | `2279.30` | `13135.11` | 26,796.64 USD | `+2.51%` | `12X Cross` |
| `1911` | `0x94b6...e5b3` | `SHORT` | 1,055,694.42 USD | `463.86` | `2261.12` | `2279.30` | `2422.54` | -6,851.75 USD | `-0.65%` | `25X Cross` |
| `1917` | `0x82c6...fe42` | `LONG` | 1,052,233.75 USD | `462.50` | `2501.38` | `2279.30` | `2054.43` | -104,656.82 USD | `-9.95%` | `5X Isolated` |
| `1925` | `0x2de3...486d` | `LONG` | 1,048,791.20 USD | `460.40` | `2286.27` | `2279.30` | `1286.71` | -3,809.71 USD | `-0.36%` | `25X Cross` |
| `1933` | `0x617e...0f97` | `SHORT` | 1,042,992.32 USD | `457.85` | `2205.60` | `2279.30` | `3697.37` | -33,148.49 USD | `-3.18%` | `10X Cross` |
| `1957` | `0xae55...2236` | `LONG` | 1,024,470.00 USD | `450.00` | `2510.21` | `2279.30` | `0.000000` | -105,127.50 USD | `-10.26%` | `25X Cross` |
| `1971` | `0xac26...a9c7` | `SHORT` | 1,017,020.43 USD | `446.28` | `2192.58` | `2279.30` | `8553.70` | -38,520.73 USD | `-3.79%` | `20X Cross` |
| `1978` | `0x53f8...ceff` | `LONG` | 1,013,778.87 USD | `445.60` | `2399.81` | `2279.30` | `0.000000` | -55,571.73 USD | `-5.48%` | `20X Cross` |
| `1997` | `0xd8a1...6687` | `LONG` | 1,006,209.55 USD | `441.53` | `2804.24` | `2279.30` | `2150.99` | -231,958.88 USD | `-23.05%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `ANNOUNCEMENT` | `INFO` | `2362.30` | 10,820.99 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 10.82K USD at 2362.3000 USD [API] | `2026-10-27 21:33:37` |
| `ANNOUNCEMENT` | `INFO` | `2362.30` | 107.96 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.11K USD at 2362.3000 USD [API] | `2026-10-27 21:33:37` |
| `ANNOUNCEMENT` | `INFO` | `2362.30` | 3,244.86 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 3.24K USD at 2362.3000 USD [API] | `2026-10-27 21:33:37` |
| `ANNOUNCEMENT` | `INFO` | `2351.90` | 40,041.57 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 40.04K USD at 2351.9000 USD [API] | `2026-10-28 18:34:28` |
| `ANNOUNCEMENT` | `INFO` | `2351.90` | 110,984.75 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 110.98K USD at 2351.9000 USD [API] | `2026-10-28 18:34:28` |
| `ANNOUNCEMENT` | `INFO` | `2359.60` | 402,569.00 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 402.57K USD at 2359.6000 USD [API] | `2026-10-28 18:37:59` |
| `ANNOUNCEMENT` | `INFO` | `2359.50` | 40,039.54 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 40.04K USD at 2359.5000 USD [API] | `2026-10-28 18:37:59` |
| `ANNOUNCEMENT` | `INFO` | `2359.20` | 40,039.40 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 40.04K USD at 2359.2000 USD [API] | `2026-10-28 18:37:59` |
| `ANNOUNCEMENT` | `INFO` | `2352.10` | 70,624.39 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 70.62K USD at 2352.1000 USD [API] | `2026-10-28 18:51:58` |
| `ANNOUNCEMENT` | `INFO` | `2452.70` | 2,224.84 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 2.22K USD at 2452.7000 USD [API] | `2026-09-17 20:15:01` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`2303.89` (Vol: 21,900,000.00 USD, Dist: `+1.55%`) | Long MP=`2242.01` (Vol: 29,100,000.00 USD, Dist: `--1.18%`)
  * 48H Horizon: Short MP=`2402.77` (Vol: 36,200,000.00 USD, Dist: `+5.91%`) | Long MP=`2242.90` (Vol: 29,100,000.00 USD, Dist: `--1.14%`)
  * 3D Horizon: Short MP=`2402.77` (Vol: 36,700,000.00 USD, Dist: `+5.91%`) | Long MP=`2242.90` (Vol: 29,100,000.00 USD, Dist: `--1.14%`)
  * 7D Horizon: Short MP=`2393.80` (Vol: 49,300,000.00 USD, Dist: `+5.52%`) | Long MP=`2241.80` (Vol: 29,100,000.00 USD, Dist: `--1.18%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `455.00` | 166,430.00 USD | 860,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `465.00` | 11,670.00 USD | 860,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `475.00` | 1,690,000.00 USD | 860,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.00` | 765.91 USD | 858,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `495.00` | 18,200.00 USD | 858,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.00` | 16,180.00 USD | 858,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.00` | 1,560,000.00 USD | 858,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.00` | 40,180.00 USD | 856,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.00` | 2,560.00 USD | 856,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.00` | 224,160.00 USD | 856,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.00` | 4,450.00 USD | 856,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `565.00` | 57,600.00 USD | 856,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `575.00` | 948,790.00 USD | 856,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.00` | 3,440.00 USD | 855,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.00` | 408,980.00 USD | 855,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `605.00` | 71,270.00 USD | 855,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.00` | 23,190.00 USD | 855,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.00` | 13,830.00 USD | 855,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.00` | 29,140.00 USD | 855,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `645.00` | 3,760.00 USD | 855,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `655.00` | 41,860.00 USD | 855,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `665.00` | 62,980.00 USD | 855,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `675.00` | 3,470.00 USD | 854,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `685.00` | 26,760.00 USD | 854,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `695.00` | 907.04 USD | 854,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `705.00` | 1,530,000.00 USD | 854,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `715.00` | 27,410.00 USD | 853,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `725.00` | 1,530,000.00 USD | 853,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `735.00` | 64,390.00 USD | 851,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `745.00` | 3,040.00 USD | 851,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `755.00` | 33,350.00 USD | 851,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `765.00` | 4,100.00 USD | 851,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `775.00` | 86,110.00 USD | 851,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `785.00` | 75,350.00 USD | 851,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `795.00` | 581.70 USD | 851,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `805.00` | 21,700.00 USD | 851,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `815.00` | 107,710.00 USD | 851,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `825.00` | 72,460.00 USD | 851,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `835.00` | 123,880.00 USD | 851,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `845.00` | 598,570.00 USD | 851,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `855.00` | 16,080.00 USD | 850,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `865.00` | 161,460.00 USD | 850,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `875.00` | 469,610.00 USD | 850,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `885.00` | 1,000,000.00 USD | 850,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `895.00` | 283,040.00 USD | 849,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `905.00` | 10,330.00 USD | 848,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `915.00` | 170,200.00 USD | 848,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `925.00` | 151,920.00 USD | 848,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `935.00` | 29,070.00 USD | 848,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `945.00` | 42,930.00 USD | 848,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `955.00` | 405,980.00 USD | 848,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `965.00` | 26,630.00 USD | 847,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `975.00` | 125,730.00 USD | 847,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `985.00` | 92,350.00 USD | 847,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `995.00` | 30,870.00 USD | 847,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1005.00` | 1,770,000.00 USD | 847,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1015.00` | 46,850.00 USD | 845,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1025.00` | 309,600.00 USD | 845,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1035.00` | 25,540.00 USD | 845,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1045.00` | 7,720,000.00 USD | 845,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1055.00` | 1,570,000.00 USD | 837,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1065.00` | 212,530.00 USD | 836,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1075.00` | 657,920.00 USD | 835,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1085.00` | 54,410.00 USD | 835,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1095.00` | 137,290.00 USD | 835,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1105.00` | 2,480,000.00 USD | 835,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1115.00` | 182,280.00 USD | 832,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1125.00` | 31,010.00 USD | 832,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1135.00` | 189,070.00 USD | 832,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1145.00` | 2,270,000.00 USD | 832,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1155.00` | 396,310.00 USD | 829,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1165.00` | 125,610.00 USD | 829,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1175.00` | 81,870.00 USD | 829,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1185.00` | 307,540.00 USD | 829,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1195.00` | 466,020.00 USD | 829,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1205.00` | 9,430,000.00 USD | 828,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1215.00` | 11,660,000.00 USD | 819,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1225.00` | 289,940.00 USD | 807,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1235.00` | 782,060.00 USD | 807,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1245.00` | 266,630.00 USD | 806,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1255.00` | 410,370.00 USD | 806,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1265.00` | 189,820.00 USD | 805,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1275.00` | 381,930.00 USD | 805,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1285.00` | 16,180,000.00 USD | 805,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1295.00` | 231,640.00 USD | 789,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1305.00` | 408,190.00 USD | 788,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1315.00` | 91,070.00 USD | 788,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1325.00` | 783,520.00 USD | 788,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1335.00` | 623,930.00 USD | 787,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1345.00` | 1,360,000.00 USD | 786,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1355.00` | 388,240.00 USD | 785,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1365.00` | 13,380,000.00 USD | 785,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1375.00` | 331,630.00 USD | 771,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1385.00` | 6,940,000.00 USD | 771,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1395.00` | 227,160.00 USD | 764,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1405.00` | 9,990,000.00 USD | 764,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1415.00` | 74,340.00 USD | 754,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1425.00` | 693,990.00 USD | 754,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1435.00` | 901,280.00 USD | 753,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1445.00` | 980,830.00 USD | 752,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1455.00` | 76,810.00 USD | 751,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1465.00` | 490,660.00 USD | 751,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1475.00` | 5,700,000.00 USD | 751,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1485.00` | 106,380.00 USD | 745,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1495.00` | 16,370,000.00 USD | 745,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1505.00` | 80,160.00 USD | 728,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1515.00` | 15,690,000.00 USD | 728,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1525.00` | 25,840,000.00 USD | 713,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1535.00` | 1,140,000.00 USD | 687,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1545.00` | 4,930,000.00 USD | 686,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1555.00` | 562,470.00 USD | 681,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1565.00` | 250,640.00 USD | 680,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1575.00` | 736,930.00 USD | 680,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1585.00` | 579,830.00 USD | 679,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1595.00` | 2,130,000.00 USD | 679,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1605.00` | 18,890,000.00 USD | 676,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1615.00` | 307,010.00 USD | 658,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1625.00` | 214,610.00 USD | 657,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1635.00` | 19,010,000.00 USD | 657,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1645.00` | 36,430,000.00 USD | 638,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1655.00` | 2,610,000.00 USD | 602,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1665.00` | 19,150,000.00 USD | 599,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1675.00` | 11,640,000.00 USD | 580,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1685.00` | 1,610,000.00 USD | 568,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1695.00` | 27,870,000.00 USD | 567,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1705.00` | 2,100,000.00 USD | 539,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1715.00` | 335,300.00 USD | 537,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1725.00` | 35,100,000.00 USD | 536,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1735.00` | 490,830.00 USD | 501,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1745.00` | 883,670.00 USD | 501,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1755.00` | 372,910.00 USD | 500,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1765.00` | 815,120.00 USD | 499,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1775.00` | 1,200,000.00 USD | 499,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1785.00` | 58,810,000.00 USD | 497,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1795.00` | 451,160.00 USD | 439,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1805.00` | 14,610,000.00 USD | 438,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1815.00` | 823,030.00 USD | 424,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1825.00` | 602,550.00 USD | 423,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1835.00` | 1,240,000.00 USD | 422,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1845.00` | 1,560,000.00 USD | 421,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1855.00` | 5,030,000.00 USD | 419,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1865.00` | 531,380.00 USD | 414,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1875.00` | 7,010,000.00 USD | 414,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1885.00` | 4,040,000.00 USD | 407,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1895.00` | 5,640,000.00 USD | 403,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1905.00` | 791,000.00 USD | 397,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1915.00` | 14,710,000.00 USD | 396,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1925.00` | 19,870,000.00 USD | 382,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1935.00` | 5,410,000.00 USD | 362,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1945.00` | 1,530,000.00 USD | 356,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1955.00` | 4,410,000.00 USD | 355,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1965.00` | 810,350.00 USD | 350,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1975.00` | 2,680,000.00 USD | 350,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1985.00` | 5,240,000.00 USD | 347,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1995.00` | 10,940,000.00 USD | 342,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2005.00` | 1,820,000.00 USD | 331,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2015.00` | 6,680,000.00 USD | 329,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2016.30` | 487,320,000.00 USD | 487,320,000.00 USD | 0.00 USD | 176,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2019.00` | 487,140,000.00 USD | 487,140,000.00 USD | 83,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2021.70` | 487,060,000.00 USD | 487,060,000.00 USD | 0.00 USD | 558,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2025.00` | 1,710,000.00 USD | 322,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2025.30` | 910,320,000.00 USD | 910,320,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2027.10` | 486,500,000.00 USD | 486,500,000.00 USD | 0.00 USD | 943,590.00 USD | 40,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2028.60` | 910,140,000.00 USD | 910,140,000.00 USD | 0.00 USD | 1,180,000.00 USD | 35,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2029.80` | 485,520,000.00 USD | 485,520,000.00 USD | 87,180.00 USD | 163,200.00 USD | 43,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2031.90` | 908,930,000.00 USD | 908,930,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2032.50` | 485,220,000.00 USD | 485,220,000.00 USD | 1,360,000.00 USD | 1,330,000.00 USD | 408,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2035.00` | 1,790,000.00 USD | 320,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2035.20` | 482,120,000.00 USD | 482,120,000.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2035.20` | 907,480,000.00 USD | 907,480,000.00 USD | 146,420.00 USD | 186,130.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2037.90` | 481,090,000.00 USD | 481,090,000.00 USD | 0.00 USD | 0.00 USD | 13,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2038.50` | 905,790,000.00 USD | 905,790,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2040.60` | 481,070,000.00 USD | 481,070,000.00 USD | 138,370.00 USD | 178,560.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2043.30` | 480,740,000.00 USD | 480,740,000.00 USD | 0.00 USD | 0.00 USD | 8,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2045.00` | 17,480,000.00 USD | 319,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2045.10` | 904,330,000.00 USD | 904,330,000.00 USD | 0.00 USD | 149,500.00 USD | 108,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2046.00` | 480,730,000.00 USD | 480,730,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2048.70` | 480,700,000.00 USD | 480,700,000.00 USD | 467,370.00 USD | 0.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2051.40` | 479,510,000.00 USD | 479,510,000.00 USD | 0.00 USD | 338,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2051.70` | 904,080,000.00 USD | 904,080,000.00 USD | 1,320,000.00 USD | 0.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2054.10` | 479,180,000.00 USD | 479,180,000.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2055.00` | 5,010,000.00 USD | 301,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2056.80` | 479,060,000.00 USD | 479,060,000.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2058.30` | 901,570,000.00 USD | 901,570,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2059.50` | 478,820,000.00 USD | 478,820,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2061.60` | 901,230,000.00 USD | 901,230,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2062.20` | 478,060,000.00 USD | 478,060,000.00 USD | 80,610.00 USD | 121,470.00 USD | 52,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2064.90` | 477,810,000.00 USD | 477,810,000.00 USD | 563,140.00 USD | 537,030.00 USD | 598,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2064.90` | 895,970,000.00 USD | 895,970,000.00 USD | 1,230,000.00 USD | 313,000.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2065.00` | 2,650,000.00 USD | 296,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2067.60` | 476,110,000.00 USD | 476,110,000.00 USD | 808,950.00 USD | 362,000.00 USD | 23,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2068.20` | 893,440,000.00 USD | 893,440,000.00 USD | 1,740,000.00 USD | 1,860,000.00 USD | 893,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2070.30` | 474,910,000.00 USD | 474,910,000.00 USD | 1,050,000.00 USD | 965,400.00 USD | 464,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2071.50` | 888,950,000.00 USD | 888,950,000.00 USD | 2,820,000.00 USD | 2,410,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2073.00` | 472,430,000.00 USD | 472,430,000.00 USD | 442,230.00 USD | 597,240.00 USD | 436,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2074.80` | 882,480,000.00 USD | 882,480,000.00 USD | 4,370,000.00 USD | 3,270,000.00 USD | 4,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 3,470,000.00 USD | 294,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2075.70` | 470,950,000.00 USD | 470,950,000.00 USD | 2,040,000.00 USD | 901,140.00 USD | 2,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2078.10` | 870,790,000.00 USD | 870,790,000.00 USD | 5,560,000.00 USD | 4,320,000.00 USD | 2,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2078.40` | 465,920,000.00 USD | 465,920,000.00 USD | 1,700,000.00 USD | 1,130,000.00 USD | 632,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2081.10` | 462,450,000.00 USD | 462,450,000.00 USD | 1,560,000.00 USD | 1,100,000.00 USD | 424,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2081.40` | 858,500,000.00 USD | 858,500,000.00 USD | 4,720,000.00 USD | 3,420,000.00 USD | 2,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2083.80` | 459,380,000.00 USD | 459,380,000.00 USD | 2,130,000.00 USD | 1,420,000.00 USD | 755,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2084.70` | 847,860,000.00 USD | 847,860,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 4,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 1,850,000.00 USD | 290,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2086.50` | 455,070,000.00 USD | 455,070,000.00 USD | 1,230,000.00 USD | 1,630,000.00 USD | 1,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2088.00` | 839,070,000.00 USD | 839,070,000.00 USD | 3,990,000.00 USD | 2,780,000.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2089.20` | 450,750,000.00 USD | 450,750,000.00 USD | 1,200,000.00 USD | 274,650.00 USD | 228,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2091.30` | 830,640,000.00 USD | 830,640,000.00 USD | 4,410,000.00 USD | 952,210.00 USD | 7,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2091.90` | 449,050,000.00 USD | 449,050,000.00 USD | 1,400,000.00 USD | 514,440.00 USD | 957,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2094.60` | 446,170,000.00 USD | 446,170,000.00 USD | 2,040,000.00 USD | 1,120,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2094.60` | 817,690,000.00 USD | 817,690,000.00 USD | 5,720,000.00 USD | 2,160,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 2,410,000.00 USD | 288,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2097.30` | 441,580,000.00 USD | 441,580,000.00 USD | 617,040.00 USD | 1,010,000.00 USD | 984,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2097.90` | 807,460,000.00 USD | 807,460,000.00 USD | 2,340,000.00 USD | 3,210,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2100.00` | 438,970,000.00 USD | 438,970,000.00 USD | 172,210.00 USD | 403,100.00 USD | 15,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2101.20` | 800,630,000.00 USD | 800,630,000.00 USD | 999,530.00 USD | 1,580,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2102.70` | 438,380,000.00 USD | 438,380,000.00 USD | 530,980.00 USD | 289,160.00 USD | 462,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2104.50` | 794,030,000.00 USD | 794,030,000.00 USD | 2,010,000.00 USD | 1,180,000.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 1,670,000.00 USD | 286,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2105.40` | 437,090,000.00 USD | 437,090,000.00 USD | 588,810.00 USD | 671,930.00 USD | 172,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2107.80` | 788,590,000.00 USD | 788,590,000.00 USD | 2,380,000.00 USD | 452,470.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2108.10` | 435,660,000.00 USD | 435,660,000.00 USD | 664,310.00 USD | 9,120.00 USD | 347,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2110.80` | 434,640,000.00 USD | 434,640,000.00 USD | 36,110.00 USD | 22,440.00 USD | 200,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2111.10` | 784,100,000.00 USD | 784,100,000.00 USD | 3,530,000.00 USD | 2,350,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2113.50` | 434,380,000.00 USD | 434,380,000.00 USD | 875,700.00 USD | 643,210.00 USD | 226,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2114.40` | 776,060,000.00 USD | 776,060,000.00 USD | 1,080,000.00 USD | 1,850,000.00 USD | 3,800,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 1,430,000.00 USD | 284,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2116.20` | 432,640,000.00 USD | 432,640,000.00 USD | 0.00 USD | 13,230.00 USD | 421,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2117.70` | 769,330,000.00 USD | 769,330,000.00 USD | 3,430,000.00 USD | 2,020,000.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2118.90` | 432,200,000.00 USD | 432,200,000.00 USD | 218,200.00 USD | 99,440.00 USD | 856,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2121.00` | 760,490,000.00 USD | 760,490,000.00 USD | 3,650,000.00 USD | 1,340,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2121.60` | 431,030,000.00 USD | 431,030,000.00 USD | 926,060.00 USD | 647,730.00 USD | 672,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2124.30` | 428,780,000.00 USD | 428,780,000.00 USD | 702,090.00 USD | 844,410.00 USD | 919,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2124.30` | 753,680,000.00 USD | 753,680,000.00 USD | 832,850.00 USD | 972,650.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 17,940,000.00 USD | 283,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2127.00` | 426,310,000.00 USD | 426,310,000.00 USD | 49,690.00 USD | 682,190.00 USD | 320,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2127.60` | 750,360,000.00 USD | 750,360,000.00 USD | 2,400,000.00 USD | 2,630,000.00 USD | 3,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2129.70` | 425,260,000.00 USD | 425,260,000.00 USD | 107,010.00 USD | 453,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2130.90` | 742,070,000.00 USD | 742,070,000.00 USD | 2,410,000.00 USD | 2,300,000.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2132.40` | 424,700,000.00 USD | 424,700,000.00 USD | 0.00 USD | 18,610.00 USD | 331,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2134.20` | 735,650,000.00 USD | 735,650,000.00 USD | 2,170,000.00 USD | 550,450.00 USD | 308,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 14,630,000.00 USD | 265,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2135.10` | 424,350,000.00 USD | 424,350,000.00 USD | 0.00 USD | 27,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2137.50` | 732,620,000.00 USD | 732,620,000.00 USD | 1,040,000.00 USD | 880,790.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2137.80` | 424,320,000.00 USD | 424,320,000.00 USD | 0.00 USD | 251,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2140.80` | 730,660,000.00 USD | 730,660,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2144.10` | 726,720,000.00 USD | 726,720,000.00 USD | 449,020.00 USD | 1,130,000.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 7,440,000.00 USD | 250,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2147.40` | 724,880,000.00 USD | 724,880,000.00 USD | 657,710.00 USD | 421,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2150.70` | 723,800,000.00 USD | 723,800,000.00 USD | 459,630.00 USD | 463,640.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2151.30` | 424,070,000.00 USD | 424,070,000.00 USD | 208,250.00 USD | 440,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2154.00` | 423,420,000.00 USD | 423,420,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2154.00` | 722,840,000.00 USD | 722,840,000.00 USD | 128,430.00 USD | 311,060.00 USD | 32,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 2,180,000.00 USD | 243,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2157.30` | 722,370,000.00 USD | 722,370,000.00 USD | 388,210.00 USD | 1,030,000.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2159.40` | 422,030,000.00 USD | 422,030,000.00 USD | 0.00 USD | 0.00 USD | 37,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2160.60` | 719,870,000.00 USD | 719,870,000.00 USD | 613,630.00 USD | 1,900,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2162.10` | 421,990,000.00 USD | 421,990,000.00 USD | 0.00 USD | 3,220,000.00 USD | 100,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2163.90` | 715,360,000.00 USD | 715,360,000.00 USD | 566,120.00 USD | 3,280,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2164.80` | 418,670,000.00 USD | 418,670,000.00 USD | 217,960.00 USD | 408,000.00 USD | 107,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 6,820,000.00 USD | 241,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2167.20` | 710,220,000.00 USD | 710,220,000.00 USD | 25,540.00 USD | 3,620,000.00 USD | 50,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2167.50` | 417,940,000.00 USD | 417,940,000.00 USD | 3,410,000.00 USD | 1,360,000.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2170.20` | 412,150,000.00 USD | 412,150,000.00 USD | 5,020,000.00 USD | 3,820,000.00 USD | 2,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2170.50` | 706,520,000.00 USD | 706,520,000.00 USD | 3,500,000.00 USD | 3,730,000.00 USD | 5,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2172.90` | 400,560,000.00 USD | 400,560,000.00 USD | 0.00 USD | 190,230.00 USD | 497,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2173.80` | 694,080,000.00 USD | 694,080,000.00 USD | 4,370,000.00 USD | 363,040.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 109,290,000.00 USD | 234,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2175.60` | 399,880,000.00 USD | 399,880,000.00 USD | 345,940.00 USD | 630,790.00 USD | 69,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2177.10` | 688,340,000.00 USD | 688,340,000.00 USD | 0.00 USD | 0.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2178.30` | 398,830,000.00 USD | 398,830,000.00 USD | 445,430.00 USD | 1,250,000.00 USD | 33,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2180.40` | 687,020,000.00 USD | 687,020,000.00 USD | 0.00 USD | 373,740.00 USD | 328,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2181.00` | 397,100,000.00 USD | 397,100,000.00 USD | 2,080,000.00 USD | 478,110.00 USD | 1,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2183.70` | 393,100,000.00 USD | 393,100,000.00 USD | 2,590,000.00 USD | 509,320.00 USD | 37,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2183.70` | 686,320,000.00 USD | 686,320,000.00 USD | 1,760,000.00 USD | 1,310,000.00 USD | 3,950,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2185.00` | 100,000,000.00 USD | 124,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2186.40` | 389,970,000.00 USD | 389,970,000.00 USD | 438,350.00 USD | 1,450,000.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2187.00` | 679,310,000.00 USD | 679,310,000.00 USD | 556,600.00 USD | 0.00 USD | 54,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2189.10` | 386,290,000.00 USD | 386,290,000.00 USD | 0.00 USD | 42,550.00 USD | 693,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2190.30` | 678,700,000.00 USD | 678,700,000.00 USD | 2,730,000.00 USD | 0.00 USD | 4,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2191.80` | 385,550,000.00 USD | 385,550,000.00 USD | 0.00 USD | 222,200.00 USD | 109,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2194.50` | 385,220,000.00 USD | 385,220,000.00 USD | 605,210.00 USD | 881,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 2,280,000.00 USD | 24,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2196.90` | 671,770,000.00 USD | 671,770,000.00 USD | 2,580,000.00 USD | 474,090.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2197.20` | 383,730,000.00 USD | 383,730,000.00 USD | 416,500.00 USD | 0.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2199.90` | 381,430,000.00 USD | 381,430,000.00 USD | 201,540.00 USD | 3,100,000.00 USD | 220,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2200.20` | 666,680,000.00 USD | 666,680,000.00 USD | 3,000,000.00 USD | 5,080,000.00 USD | 3,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2202.60` | 377,910,000.00 USD | 377,910,000.00 USD | 2,660,000.00 USD | 1,410,000.00 USD | 2,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2203.50` | 655,400,000.00 USD | 655,400,000.00 USD | 3,650,000.00 USD | 1,710,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 8,120,000.00 USD | 22,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2205.30` | 371,750,000.00 USD | 371,750,000.00 USD | 968,520.00 USD | 6,090,000.00 USD | 879,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2206.80` | 646,290,000.00 USD | 646,290,000.00 USD | 6,920,000.00 USD | 9,430,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2208.00` | 363,810,000.00 USD | 363,810,000.00 USD | 3,240,000.00 USD | 5,170,000.00 USD | 2,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2210.10` | 625,920,000.00 USD | 625,920,000.00 USD | 12,800,000.00 USD | 20,410,000.00 USD | 6,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2210.70` | 352,860,000.00 USD | 352,860,000.00 USD | 2,630,000.00 USD | 3,720,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2213.40` | 345,080,000.00 USD | 345,080,000.00 USD | 13,740,000.00 USD | 9,500,000.00 USD | 5,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2213.40` | 586,240,000.00 USD | 586,240,000.00 USD | 10,920,000.00 USD | 14,590,000.00 USD | 19,950,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 4,660,000.00 USD | 14,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2216.10` | 316,060,000.00 USD | 316,060,000.00 USD | 15,030,000.00 USD | 9,200,000.00 USD | 11,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2216.70` | 540,770,000.00 USD | 540,770,000.00 USD | 25,710,000.00 USD | 17,030,000.00 USD | 9,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2218.80` | 280,700,000.00 USD | 280,700,000.00 USD | 6,090,000.00 USD | 7,230,000.00 USD | 1,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2220.00` | 488,640,000.00 USD | 488,640,000.00 USD | 24,310,000.00 USD | 12,300,000.00 USD | 12,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2221.50` | 265,630,000.00 USD | 265,630,000.00 USD | 5,390,000.00 USD | 11,940,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2223.30` | 439,270,000.00 USD | 439,270,000.00 USD | 10,150,000.00 USD | 8,220,000.00 USD | 11,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2224.20` | 246,950,000.00 USD | 246,950,000.00 USD | 10,770,000.00 USD | 5,040,000.00 USD | 5,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2225.00` | 5,380,000.00 USD | 9,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2226.60` | 408,990,000.00 USD | 408,990,000.00 USD | 16,350,000.00 USD | 11,030,000.00 USD | 10,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2226.90` | 225,770,000.00 USD | 225,770,000.00 USD | 5,400,000.00 USD | 4,420,000.00 USD | 5,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2229.60` | 210,210,000.00 USD | 210,210,000.00 USD | 9,510,000.00 USD | 15,930,000.00 USD | 1,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2229.90` | 371,350,000.00 USD | 371,350,000.00 USD | 12,730,000.00 USD | 11,790,000.00 USD | 28,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2232.30` | 182,990,000.00 USD | 182,990,000.00 USD | 4,360,000.00 USD | 4,830,000.00 USD | 7,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2233.20` | 318,280,000.00 USD | 318,280,000.00 USD | 16,600,000.00 USD | 24,290,000.00 USD | 10,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2235.00` | 166,310,000.00 USD | 166,310,000.00 USD | 19,080,000.00 USD | 1,450,000.00 USD | 11,770,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2235.00` | 878,090.00 USD | 878,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2236.50` | 266,960,000.00 USD | 266,960,000.00 USD | 16,050,000.00 USD | 7,430,000.00 USD | 27,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2237.70` | 134,000,000.00 USD | 134,000,000.00 USD | 23,860,000.00 USD | 7,390,000.00 USD | 12,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2239.80` | 215,720,000.00 USD | 215,720,000.00 USD | 16,720,000.00 USD | 6,600,000.00 USD | 13,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2240.40` | 90,310,000.00 USD | 90,310,000.00 USD | 846,550.00 USD | 760,920.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2243.10` | 86,150,000.00 USD | 86,150,000.00 USD | 2,540,000.00 USD | 444,750.00 USD | 5,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2243.10` | 178,660,000.00 USD | 178,660,000.00 USD | 22,920,000.00 USD | 0.00 USD | 18,320,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2245.00` | 4,430,000.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2245.80` | 78,040,000.00 USD | 78,040,000.00 USD | 3,700,000.00 USD | 5,740,000.00 USD | 790,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2246.40` | 137,410,000.00 USD | 137,410,000.00 USD | 14,340,000.00 USD | 0.00 USD | 13,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2248.50` | 67,810,000.00 USD | 67,810,000.00 USD | 15,010,000.00 USD | 0.00 USD | 10,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2249.70` | 109,150,000.00 USD | 109,150,000.00 USD | 25,030,000.00 USD | 0.00 USD | 19,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2251.20` | 42,130,000.00 USD | 42,130,000.00 USD | 12,010,000.00 USD | 1,910,000.00 USD | 661,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2253.00` | 65,090,000.00 USD | 65,090,000.00 USD | 26,890,000.00 USD | 0.00 USD | 12,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2253.90` | 27,540,000.00 USD | 27,540,000.00 USD | 1,750,000.00 USD | 7,830,000.00 USD | 4,080,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2255.00` | 68,250.00 USD | 68,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2256.30` | 26,160,000.00 USD | 26,160,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2256.60` | 13,880,000.00 USD | 13,880,000.00 USD | 0.00 USD | 170,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2259.60` | 10,940,000.00 USD | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2262.00` | 13,710,000.00 USD | 13,710,000.00 USD | 2,420,000.00 USD | 0.00 USD | 156,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2264.70` | 11,140,000.00 USD | 11,140,000.00 USD | 0.00 USD | 0.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2265.00` | 410.42 USD | 878,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2267.40` | 9,660,000.00 USD | 9,660,000.00 USD | 0.00 USD | 0.00 USD | 3,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2270.10` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2275.00` | 633.82 USD | 879,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2275.50` | 5,310,000.00 USD | 5,310,000.00 USD | 125,710.00 USD | 555,110.00 USD | 114,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2278.20` | 4,520,000.00 USD | 4,520,000.00 USD | 2,720,000.00 USD | 1,360,000.00 USD | 431,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2279.40` | 17,000,000.00 USD | 17,000,000.00 USD | 0.00 USD | 17,000,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2280.90` | 69,400,000.00 USD | 69,400,000.00 USD | 39,790,000.00 USD | 25,520,000.00 USD | 4,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2282.70` | 117,630,000.00 USD | 117,630,000.00 USD | 0.00 USD | 87,090,000.00 USD | 13,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2283.60` | 149,190,000.00 USD | 149,190,000.00 USD | 40,630,000.00 USD | 22,390,000.00 USD | 16,760,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2285.00` | 2,530.00 USD | 881,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2286.00` | 128,050,000.00 USD | 128,050,000.00 USD | 1,010,000.00 USD | 9,400,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2286.30` | 150,960,000.00 USD | 150,960,000.00 USD | 0.00 USD | 1,640,000.00 USD | 133,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2289.00` | 156,420,000.00 USD | 156,420,000.00 USD | 0.00 USD | 5,320,000.00 USD | 143,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2289.30` | 133,320,000.00 USD | 133,320,000.00 USD | 0.00 USD | 0.00 USD | 5,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2291.70` | 163,340,000.00 USD | 163,340,000.00 USD | 1,780,000.00 USD | 5,010,000.00 USD | 132,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2292.60` | 133,930,000.00 USD | 133,930,000.00 USD | 0.00 USD | 0.00 USD | 607,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2294.40` | 177,510,000.00 USD | 177,510,000.00 USD | 8,310,000.00 USD | 0.00 USD | 5,860,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2295.00` | 25,230.00 USD | 906,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2295.90` | 161,240,000.00 USD | 161,240,000.00 USD | 13,610,000.00 USD | 2,380,000.00 USD | 11,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2297.10` | 196,550,000.00 USD | 196,550,000.00 USD | 10,340,000.00 USD | 8,350,000.00 USD | 350,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2299.20` | 189,660,000.00 USD | 189,660,000.00 USD | 11,730,000.00 USD | 11,130,000.00 USD | 5,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2299.80` | 213,670,000.00 USD | 213,670,000.00 USD | 1,750,000.00 USD | 7,970,000.00 USD | 7,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2302.50` | 234,660,000.00 USD | 234,660,000.00 USD | 15,230,000.00 USD | 852,700.00 USD | 4,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2302.50` | 236,770,000.00 USD | 236,770,000.00 USD | 23,020,000.00 USD | 7,250,000.00 USD | 16,850,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2305.00` | 4,250,000.00 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2305.20` | 264,110,000.00 USD | 264,110,000.00 USD | 10,430,000.00 USD | 14,490,000.00 USD | 4,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2305.80` | 257,550,000.00 USD | 257,550,000.00 USD | 2,980,000.00 USD | 8,820,000.00 USD | 8,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2307.90` | 272,010,000.00 USD | 272,010,000.00 USD | 2,420,000.00 USD | 3,100,000.00 USD | 2,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2309.10` | 261,820,000.00 USD | 261,820,000.00 USD | 1,240,000.00 USD | 930,630.00 USD | 2,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2310.60` | 280,700,000.00 USD | 280,700,000.00 USD | 691,870.00 USD | 380,460.00 USD | 7,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2312.40` | 279,960,000.00 USD | 279,960,000.00 USD | 7,270,000.00 USD | 0.00 USD | 10,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2313.30` | 288,640,000.00 USD | 288,640,000.00 USD | 890,860.00 USD | 6,730,000.00 USD | 313,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2315.00` | 2,480,000.00 USD | 7,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2315.70` | 287,840,000.00 USD | 287,840,000.00 USD | 0.00 USD | 7,460,000.00 USD | 421,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2316.00` | 319,350,000.00 USD | 319,350,000.00 USD | 9,790,000.00 USD | 14,310,000.00 USD | 6,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2318.70` | 332,620,000.00 USD | 332,620,000.00 USD | 4,440,000.00 USD | 7,340,000.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2319.00` | 305,340,000.00 USD | 305,340,000.00 USD | 4,540,000.00 USD | 4,550,000.00 USD | 8,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2321.40` | 352,830,000.00 USD | 352,830,000.00 USD | 6,490,000.00 USD | 13,570,000.00 USD | 147,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2322.30` | 322,500,000.00 USD | 322,500,000.00 USD | 1,110,000.00 USD | 15,930,000.00 USD | 108,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2324.10` | 366,630,000.00 USD | 366,630,000.00 USD | 479,120.00 USD | 9,740,000.00 USD | 3,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2325.00` | 1,420,000.00 USD | 9,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2325.60` | 343,150,000.00 USD | 343,150,000.00 USD | 9,720,000.00 USD | 2,540,000.00 USD | 8,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2326.80` | 372,980,000.00 USD | 372,980,000.00 USD | 256,580.00 USD | 291,550.00 USD | 5,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2328.90` | 354,980,000.00 USD | 354,980,000.00 USD | 3,860,000.00 USD | 0.00 USD | 7,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2329.50` | 383,890,000.00 USD | 383,890,000.00 USD | 9,740,000.00 USD | 884,940.00 USD | 281,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2332.20` | 399,620,000.00 USD | 399,620,000.00 USD | 11,600,000.00 USD | 251,940.00 USD | 3,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2332.20` | 384,210,000.00 USD | 384,210,000.00 USD | 29,230,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2334.90` | 419,410,000.00 USD | 419,410,000.00 USD | 13,410,000.00 USD | 2,960,000.00 USD | 3,420,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2335.00` | 1,230,000.00 USD | 10,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2335.50` | 442,220,000.00 USD | 442,220,000.00 USD | 28,990,000.00 USD | 18,420,000.00 USD | 10,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2337.60` | 433,290,000.00 USD | 433,290,000.00 USD | 9,880,000.00 USD | 407,920.00 USD | 3,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2338.80` | 460,090,000.00 USD | 460,090,000.00 USD | 9,570,000.00 USD | 0.00 USD | 8,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2340.30` | 457,190,000.00 USD | 457,190,000.00 USD | 8,010,000.00 USD | 5,100,000.00 USD | 10,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2342.10` | 500,190,000.00 USD | 500,190,000.00 USD | 4,720,000.00 USD | 21,390,000.00 USD | 14,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2343.00` | 465,500,000.00 USD | 465,500,000.00 USD | 2,060,000.00 USD | 3,800,000.00 USD | 2,440,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2345.00` | 326,400.00 USD | 10,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2345.40` | 521,570,000.00 USD | 521,570,000.00 USD | 1,350,000.00 USD | 13,990,000.00 USD | 6,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2345.70` | 483,470,000.00 USD | 483,470,000.00 USD | 3,680,000.00 USD | 3,710,000.00 USD | 10,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2348.40` | 496,540,000.00 USD | 496,540,000.00 USD | 5,060,000.00 USD | 6,000,000.00 USD | 2,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2348.70` | 559,440,000.00 USD | 559,440,000.00 USD | 847,620.00 USD | 9,500,000.00 USD | 27,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2351.10` | 543,350,000.00 USD | 543,350,000.00 USD | 31,280,000.00 USD | 4,740,000.00 USD | 10,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2352.00` | 596,070,000.00 USD | 596,070,000.00 USD | 2,930,000.00 USD | 23,060,000.00 USD | 10,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2353.80` | 559,060,000.00 USD | 559,060,000.00 USD | 3,270,000.00 USD | 11,770,000.00 USD | 657,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 1,270,000.00 USD | 11,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2355.30` | 650,910,000.00 USD | 650,910,000.00 USD | 16,780,000.00 USD | 36,690,000.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2356.50` | 573,650,000.00 USD | 573,650,000.00 USD | 3,430,000.00 USD | 8,660,000.00 USD | 2,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2358.60` | 663,040,000.00 USD | 663,040,000.00 USD | 7,110,000.00 USD | 512,220.00 USD | 4,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2359.20` | 590,800,000.00 USD | 590,800,000.00 USD | 4,590,000.00 USD | 5,650,000.00 USD | 6,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2361.90` | 611,960,000.00 USD | 611,960,000.00 USD | 10,000,000.00 USD | 8,410,000.00 USD | 2,750,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2361.90` | 670,320,000.00 USD | 670,320,000.00 USD | 3,150,000.00 USD | 3,800,000.00 USD | 328,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2364.60` | 630,330,000.00 USD | 630,330,000.00 USD | 6,050,000.00 USD | 4,190,000.00 USD | 8,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 1,310,000.00 USD | 13,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2365.20` | 691,380,000.00 USD | 691,380,000.00 USD | 10,200,000.00 USD | 0.00 USD | 10,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2367.30` | 636,830,000.00 USD | 636,830,000.00 USD | 5,160,000.00 USD | 1,110,000.00 USD | 228,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2368.50` | 704,450,000.00 USD | 704,450,000.00 USD | 10,830,000.00 USD | 1,780,000.00 USD | 458,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2370.00` | 673,160,000.00 USD | 673,160,000.00 USD | 15,180,000.00 USD | 12,300,000.00 USD | 8,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2371.80` | 785,380,000.00 USD | 785,380,000.00 USD | 26,000,000.00 USD | 0.00 USD | 54,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2372.70` | 701,630,000.00 USD | 701,630,000.00 USD | 14,450,000.00 USD | 5,550,000.00 USD | 8,460,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 1,060,000.00 USD | 14,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2375.10` | 812,330,000.00 USD | 812,330,000.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2375.40` | 720,450,000.00 USD | 720,450,000.00 USD | 11,510,000.00 USD | 3,650,000.00 USD | 3,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2378.10` | 743,290,000.00 USD | 743,290,000.00 USD | 5,260,000.00 USD | 6,340,000.00 USD | 11,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2378.40` | 857,750,000.00 USD | 857,750,000.00 USD | 11,800,000.00 USD | 7,950,000.00 USD | 25,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2380.80` | 781,050,000.00 USD | 781,050,000.00 USD | 11,360,000.00 USD | 11,550,000.00 USD | 14,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2381.70` | 897,530,000.00 USD | 897,530,000.00 USD | 8,510,000.00 USD | 6,750,000.00 USD | 24,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2383.50` | 830,640,000.00 USD | 830,640,000.00 USD | 21,740,000.00 USD | 14,400,000.00 USD | 13,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2385.00` | 999,250,000.00 USD | 999,250,000.00 USD | 18,550,000.00 USD | 36,910,000.00 USD | 46,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 42,090,000.00 USD | 56,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2386.20` | 863,600,000.00 USD | 863,600,000.00 USD | 12,110,000.00 USD | 12,530,000.00 USD | 8,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2388.30` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 5,290,000.00 USD | 38,070,000.00 USD | 44,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2388.90` | 886,680,000.00 USD | 886,680,000.00 USD | 11,000,000.00 USD | 8,120,000.00 USD | 3,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2391.60` | 904,210,000.00 USD | 904,210,000.00 USD | 3,670,000.00 USD | 6,460,000.00 USD | 7,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2391.60` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 8,560,000.00 USD | 52,080,000.00 USD | 40,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2394.30` | 920,070,000.00 USD | 920,070,000.00 USD | 6,620,000.00 USD | 6,560,000.00 USD | 2,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2394.90` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 57,450,000.00 USD | 32,260,000.00 USD | 37,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 99,780.00 USD | 56,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2397.00` | 932,290,000.00 USD | 932,290,000.00 USD | 2,270,000.00 USD | 4,990,000.00 USD | 4,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2398.20` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 42,820,000.00 USD | 38,210,000.00 USD | 29,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2399.70` | 955,160,000.00 USD | 955,160,000.00 USD | 8,430,000.00 USD | 5,600,000.00 USD | 8,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2401.50` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 51,970,000.00 USD | 26,780,000.00 USD | 29,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2402.40` | 973,750,000.00 USD | 973,750,000.00 USD | 6,030,000.00 USD | 6,200,000.00 USD | 6,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2404.80` | 1,640,000,000.00 USD | 1,640,000,000.00 USD | 50,800,000.00 USD | 32,200,000.00 USD | 24,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 1,430,000.00 USD | 57,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2405.10` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 11,290,000.00 USD | 9,370,000.00 USD | 8,800,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2407.80` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 14,220,000.00 USD | 9,590,000.00 USD | 5,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2408.10` | 1,730,000,000.00 USD | 1,730,000,000.00 USD | 34,390,000.00 USD | 31,420,000.00 USD | 25,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2410.50` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 5,370,000.00 USD | 7,150,000.00 USD | 7,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2411.40` | 1,810,000,000.00 USD | 1,810,000,000.00 USD | 19,200,000.00 USD | 32,580,000.00 USD | 27,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2413.20` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 8,550,000.00 USD | 5,040,000.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2414.70` | 1,880,000,000.00 USD | 1,880,000,000.00 USD | 23,820,000.00 USD | 21,740,000.00 USD | 23,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 858,190.00 USD | 58,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2415.90` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 3,430,000.00 USD | 2,760,000.00 USD | 3,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2418.00` | 1,950,000,000.00 USD | 1,950,000,000.00 USD | 34,060,000.00 USD | 15,260,000.00 USD | 24,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2418.60` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 4,100,000.00 USD | 2,710,000.00 USD | 3,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2421.30` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 6,310,000.00 USD | 5,040,000.00 USD | 6,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2421.30` | 2,030,000,000.00 USD | 2,030,000,000.00 USD | 25,700,000.00 USD | 27,770,000.00 USD | 21,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2424.00` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 1,770,000.00 USD | 3,680,000.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.60` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 23,840,000.00 USD | 33,060,000.00 USD | 34,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 953,600.00 USD | 59,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2426.70` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 972,850.00 USD | 369,950.00 USD | 39,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2427.90` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 25,200,000.00 USD | 18,380,000.00 USD | 26,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2429.40` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 1,290,000.00 USD | 1,770,000.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2431.20` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 10,380,000.00 USD | 17,060,000.00 USD | 9,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2432.10` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 2,050,000.00 USD | 1,690,000.00 USD | 436,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2434.50` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 27,390,000.00 USD | 21,570,000.00 USD | 11,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2434.80` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 2,100,000.00 USD | 468,310.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 4,450,000.00 USD | 64,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2437.50` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 777,840.00 USD | 531,390.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2437.80` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 11,900,000.00 USD | 12,720,000.00 USD | 5,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2440.20` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 1,540,000.00 USD | 1,250,000.00 USD | 479,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2441.10` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 15,080,000.00 USD | 8,120,000.00 USD | 10,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2442.90` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 1,050,000.00 USD | 1,430,000.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2444.40` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 8,860,000.00 USD | 15,100,000.00 USD | 13,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 280,670.00 USD | 64,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2445.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 126,820.00 USD | 467,480.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2447.70` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 11,480,000.00 USD | 7,520,000.00 USD | 17,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2448.30` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 886,490.00 USD | 537,830.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2451.00` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 2,460,000.00 USD | 2,020,000.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2451.00` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 16,710,000.00 USD | 14,100,000.00 USD | 16,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2453.70` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 4,450,000.00 USD | 3,260,000.00 USD | 2,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2454.30` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 4,620,000.00 USD | 4,930,000.00 USD | 3,880,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 96,380.00 USD | 64,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2456.40` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 917,470.00 USD | 2,120,000.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2457.60` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 15,150,000.00 USD | 12,540,000.00 USD | 12,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2459.10` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 1,880,000.00 USD | 1,210,000.00 USD | 366,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2460.90` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 5,580,000.00 USD | 8,670,000.00 USD | 6,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2461.80` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 490,260.00 USD | 829,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2464.20` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 8,720,000.00 USD | 7,700,000.00 USD | 4,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2464.50` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 83,300.00 USD | 176,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 914,970.00 USD | 65,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2467.20` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 68,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2467.50` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 4,540,000.00 USD | 3,710,000.00 USD | 586,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2469.90` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 1,190,000.00 USD | 391,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2470.80` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 3,960,000.00 USD | 2,290,000.00 USD | 522,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2474.10` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 5,230,000.00 USD | 2,920,000.00 USD | 2,400,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 438,920.00 USD | 65,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2475.30` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 914,780.00 USD | 28,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2477.40` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 1,660,000.00 USD | 4,420,000.00 USD | 718,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2478.00` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 55,510.00 USD | 11,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2480.70` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 87,180.00 USD | 136,500.00 USD | 43,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2480.70` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 2,110,000.00 USD | 4,170,000.00 USD | 540,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2483.40` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 1,290,000.00 USD | 0.00 USD | 408,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2484.00` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 1,210,000.00 USD | 1,390,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 96,970.00 USD | 65,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2486.10` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 1,110,000.00 USD | 1,330,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2487.30` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 275,450.00 USD | 211,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2490.60` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 2,910,000.00 USD | 2,540,000.00 USD | 239,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2491.50` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 138,370.00 USD | 0.00 USD | 13,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2493.90` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 1,660,000.00 USD | 1,760,000.00 USD | 3,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2494.20` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 178,560.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 8,760,000.00 USD | 74,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2496.90` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 8,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2497.20` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 2,860,000.00 USD | 4,770,000.00 USD | 8,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2499.60` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2500.50` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 1,110,000.00 USD | 2,280,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2502.30` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 467,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2503.80` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 63,860.00 USD | 1,480,000.00 USD | 125,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2505.00` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 2,310,000.00 USD | 77,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2507.10` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 4,340,000.00 USD | 3,090,000.00 USD | 3,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2510.40` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2510.40` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 2,290,000.00 USD | 1,270,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2513.10` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2513.70` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 142,410.00 USD | 77,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2515.80` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2517.00` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 97,050.00 USD | 189,640.00 USD | 815,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2520.30` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2521.20` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 80,610.00 USD | 121,470.00 USD | 88,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2523.60` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2523.90` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 984,680.00 USD | 537,030.00 USD | 562,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 4,710,000.00 USD | 81,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2526.60` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 387,410.00 USD | 362,000.00 USD | 23,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2526.90` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2529.30` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 641,110.00 USD | 965,400.00 USD | 464,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2530.20` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 2,800,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2532.00` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 799,930.00 USD | 534,600.00 USD | 7,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2533.50` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 3,530,000.00 USD | 1,850,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2534.70` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 79,690.00 USD | 62,630.00 USD | 919,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2535.00` | 2,520,000.00 USD | 84,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2536.80` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 3,720,000.00 USD | 3,450,000.00 USD | 3,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2537.40` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 2,470,000.00 USD | 901,140.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2538.00` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 95,710.00 USD | 380,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2540.10` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 4,150,000.00 USD | 3,220,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2543.40` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 4,150,000.00 USD | 2,520,000.00 USD | 2,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2545.00` | 5,380,000.00 USD | 89,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2546.70` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 1,450,000.00 USD | 1,090,000.00 USD | 2,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2550.00` | 2,730,000,000.00 USD | 2,730,000,000.00 USD | 4,320,000.00 USD | 3,550,000.00 USD | 3,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2553.30` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 2,820,000.00 USD | 788,360.00 USD | 2,600,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2555.00` | 397,740.00 USD | 90,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2556.60` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 2,760,000.00 USD | 283,560.00 USD | 6,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2559.90` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 5,720,000.00 USD | 2,130,000.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2563.20` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 1,430,000.00 USD | 2,900,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2565.00` | 2,400,000.00 USD | 92,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2566.50` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 1,860,000.00 USD | 1,830,000.00 USD | 3,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2569.80` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 125,250.00 USD | 341,900.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2573.10` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2575.00` | 11,620,000.00 USD | 104,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2576.40` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 2,400,000.00 USD | 930,280.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2579.70` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 2,750,000.00 USD | 1,780,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2583.00` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 1,730,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2585.00` | 26,470,000.00 USD | 130,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2586.30` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 1,480,000.00 USD | 2,030,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2589.60` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 3,310,000.00 USD | 631,590.00 USD | 2,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2592.90` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 2,370,000.00 USD | 1,280,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2595.00` | 1,910,000.00 USD | 132,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2596.20` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 794,750.00 USD | 620,840.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2599.50` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 2,380,000.00 USD | 2,530,000.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2602.80` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 1,680,000.00 USD | 1,260,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2605.00` | 14,250,000.00 USD | 146,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2606.10` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 1,850,000.00 USD | 1,560,000.00 USD | 772,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2609.40` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2612.70` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 1,010,000.00 USD | 643,740.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2615.00` | 293,190.00 USD | 147,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2616.00` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2619.30` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 449,020.00 USD | 323,810.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2622.60` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 631,440.00 USD | 1,220,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2625.00` | 13,030,000.00 USD | 160,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2625.90` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 485,890.00 USD | 474,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2629.20` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 0.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2632.40` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 301,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2635.00` | 4,590,000.00 USD | 164,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2645.00` | 75,760.00 USD | 164,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2655.00` | 35,870,000.00 USD | 200,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2665.00` | 115,060.00 USD | 200,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2675.00` | 439,350.00 USD | 201,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2685.00` | 877,180.00 USD | 202,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2695.00` | 134,610.00 USD | 202,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2705.00` | 29,450,000.00 USD | 231,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2715.00` | 90,570.00 USD | 231,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2725.00` | 1,150,000.00 USD | 232,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2735.00` | 298,530.00 USD | 233,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2745.00` | 1,270,000.00 USD | 234,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2755.00` | 587,770.00 USD | 235,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2765.00` | 123,300.00 USD | 235,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2775.00` | 143,910.00 USD | 235,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2785.00` | 1,870,000.00 USD | 237,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2795.00` | 59,340.00 USD | 237,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2805.00` | 4,100,000.00 USD | 241,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2815.00` | 36,950,000.00 USD | 278,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2825.00` | 180,820.00 USD | 278,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2835.00` | 4,140,000.00 USD | 282,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2845.00` | 2,160,000.00 USD | 284,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2855.00` | 590,830.00 USD | 285,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2865.00` | 101,470.00 USD | 285,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2875.00` | 65,130.00 USD | 285,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2885.00` | 2,180,000.00 USD | 287,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2895.00` | 333,130.00 USD | 288,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2905.00` | 588,570.00 USD | 288,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2915.00` | 27,760,000.00 USD | 316,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2925.00` | 21,410,000.00 USD | 337,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2935.00` | 463,430.00 USD | 338,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2945.00` | 465,540.00 USD | 338,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2955.00` | 152,600.00 USD | 338,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2965.00` | 556,280.00 USD | 339,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2975.00` | 174,230.00 USD | 339,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2985.00` | 110,600.00 USD | 339,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2995.00` | 20,950,000.00 USD | 360,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3005.00` | 1,730,000.00 USD | 362,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3015.00` | 299,170.00 USD | 362,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3025.00` | 1,980,000.00 USD | 364,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3035.00` | 1,590,000.00 USD | 366,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3045.00` | 18,930,000.00 USD | 385,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3055.00` | 2,210,000.00 USD | 387,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3065.00` | 6,140,000.00 USD | 393,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3075.00` | 3,120,000.00 USD | 396,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3085.00` | 101,440.00 USD | 396,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3095.00` | 2,400,000.00 USD | 399,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3105.00` | 2,920,000.00 USD | 402,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3115.00` | 833,940.00 USD | 403,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3125.00` | 167,670.00 USD | 403,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3135.00` | 454,470.00 USD | 403,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3145.00` | 10,540,000.00 USD | 414,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3155.00` | 119,030.00 USD | 414,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3165.00` | 133,900.00 USD | 414,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3175.00` | 6,760,000.00 USD | 421,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3185.00` | 2,560,000.00 USD | 423,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3195.00` | 4,760,000.00 USD | 428,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3205.00` | 79,400.00 USD | 428,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3215.00` | 603,280.00 USD | 429,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3225.00` | 38,690.00 USD | 429,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3235.00` | 215,450.00 USD | 429,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3245.00` | 8,580,000.00 USD | 438,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3255.00` | 10,740.00 USD | 438,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3265.00` | 178,100.00 USD | 438,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3275.00` | 141,610.00 USD | 438,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3285.00` | 8,760,000.00 USD | 447,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3295.00` | 5,260,000.00 USD | 452,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3305.00` | 1,850,000.00 USD | 454,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3315.00` | 770,350.00 USD | 455,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3325.00` | 273,560.00 USD | 455,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3335.00` | 58,040.00 USD | 455,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3345.00` | 20,590.00 USD | 455,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3355.00` | 480,680.00 USD | 455,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3365.00` | 554,020.00 USD | 456,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3375.00` | 54,970.00 USD | 456,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3385.00` | 781,690.00 USD | 457,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3395.00` | 41,180.00 USD | 457,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3405.00` | 2,470,000.00 USD | 459,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3415.00` | 35,070.00 USD | 459,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3425.00` | 14,610,000.00 USD | 474,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3435.00` | 405,420.00 USD | 474,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3445.00` | 39,140.00 USD | 474,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3455.00` | 983,340.00 USD | 475,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3465.00` | 80,780.00 USD | 475,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3475.00` | 59,100,000.00 USD | 535,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3485.00` | 1,080,000.00 USD | 536,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3495.00` | 1,270,000.00 USD | 537,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3505.00` | 34,200.00 USD | 537,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3515.00` | 57,680.00 USD | 537,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3525.00` | 317,970.00 USD | 537,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3535.00` | 453,790.00 USD | 538,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3545.00` | 31,840.00 USD | 538,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3555.00` | 172,980.00 USD | 538,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3565.00` | 62,420.00 USD | 538,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3575.00` | 1,680,000.00 USD | 540,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3585.00` | 568,830.00 USD | 540,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3595.00` | 324,630.00 USD | 541,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3605.00` | 135,550.00 USD | 541,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3615.00` | 4,290,000.00 USD | 545,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3625.00` | 567,320.00 USD | 546,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3635.00` | 7,340,000.00 USD | 553,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3645.00` | 6,480,000.00 USD | 559,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3655.00` | 24,380.00 USD | 559,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3665.00` | 283,220.00 USD | 560,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3675.00` | 345,780.00 USD | 560,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3685.00` | 198,930.00 USD | 560,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3695.00` | 126,340.00 USD | 560,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3705.00` | 79,680.00 USD | 560,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3715.00` | 194,910.00 USD | 561,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3725.00` | 260,570.00 USD | 561,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3735.00` | 315,000.00 USD | 561,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3745.00` | 840,410.00 USD | 562,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3755.00` | 2,460,000.00 USD | 565,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3765.00` | 1,780,000.00 USD | 566,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3775.00` | 638,640.00 USD | 567,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3785.00` | 123,580.00 USD | 567,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3795.00` | 955.58 USD | 567,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3805.00` | 52,480.00 USD | 567,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3815.00` | 807,620.00 USD | 568,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3825.00` | 53,370.00 USD | 568,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3835.00` | 51,170,000.00 USD | 619,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3845.00` | 145,840.00 USD | 619,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3855.00` | 2,040,000.00 USD | 621,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3865.00` | 480,540.00 USD | 622,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3875.00` | 1,090,000.00 USD | 623,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3885.00` | 2,290,000.00 USD | 625,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3895.00` | 104,030.00 USD | 625,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3905.00` | 790,430.00 USD | 626,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3915.00` | 37,680.00 USD | 626,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3925.00` | 186,310.00 USD | 626,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3935.00` | 9,510,000.00 USD | 636,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3945.00` | 171,110.00 USD | 636,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3955.00` | 420,960,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3965.00` | 1,030.00 USD | 1,060,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3975.00` | 587,840.00 USD | 1,060,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3985.00` | 625,370.00 USD | 1,060,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3995.00` | 141,210.00 USD | 1,060,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4005.00` | 318,570.00 USD | 1,060,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4015.00` | 30,810,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4025.00` | 91,580.00 USD | 1,090,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4035.00` | 255,490.00 USD | 1,090,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4055.00` | 93,490,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4065.00` | 12,200.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4075.00` | 2,870,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4085.00` | 2,710.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4095.00` | 54,520.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4105.00` | 2,120,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4115.00` | 2,290,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4125.00` | 144,380.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4135.00` | 228,400.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4145.00` | 70,480,000.00 USD | 1,260,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4155.00` | 1,910,000.00 USD | 1,260,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4165.00` | 150,520.00 USD | 1,260,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4175.00` | 835,000.00 USD | 1,260,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4185.00` | 71,700.00 USD | 1,260,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4195.00` | 4,180,000.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4205.00` | 422,520.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4215.00` | 42,960.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4225.00` | 842.89 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4235.00` | 1,420.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4245.00` | 916.92 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4255.00` | 89,150,000.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4265.00` | 3,960,000.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4275.00` | 8,160.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4285.00` | 476,480.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4295.00` | 68,850.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4305.00` | 3,000.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4315.00` | 18,810.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4325.00` | 181,820.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4335.00` | 109,320.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4345.00` | 1,430,000.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4355.00` | 2,870,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4365.00` | 557,240.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4375.00` | 36,440.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4385.00` | 8,980.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4395.00` | 759,410.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4405.00` | 41,990.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4415.00` | 45,850.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4425.00` | 45,870.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4435.00` | 20,090.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4445.00` | 3,500,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4455.00` | 124,740.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4465.00` | 740,600.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4475.00` | 145,300.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4485.00` | 4,490.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4495.00` | 7,610.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4505.00` | 93,520.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4515.00` | 10,080.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4525.00` | 2,860.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4535.00` | 467,610.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4545.00` | 171,010.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `455.00` | 860,380,000.00 USD | 0.00 USD | 166,430.00 USD | `-79.98%` | `365.77` |
| `Live` | `Long` | `465.00` | 860,210,000.00 USD | 0.00 USD | 11,670.00 USD | `-79.54%` | `25.09` |
| `Live` | `Long` | `475.00` | 860,200,000.00 USD | 0.00 USD | 1,690,000.00 USD | `-79.10%` | `3,559.14` |
| `Live` | `Long` | `485.00` | 858,510,000.00 USD | 0.00 USD | 765.91 USD | `-78.66%` | `1.58` |
| `Live` | `Long` | `495.00` | 858,510,000.00 USD | 0.00 USD | 18,200.00 USD | `-78.21%` | `36.76` |
| `Live` | `Long` | `505.00` | 858,490,000.00 USD | 0.00 USD | 16,180.00 USD | `-77.77%` | `32.03` |
| `Live` | `Long` | `515.00` | 858,480,000.00 USD | 0.00 USD | 1,560,000.00 USD | `-77.33%` | `3,024.63` |
| `Live` | `Long` | `525.00` | 856,920,000.00 USD | 0.00 USD | 40,180.00 USD | `-76.89%` | `76.54` |
| `Live` | `Long` | `535.00` | 856,880,000.00 USD | 0.00 USD | 2,560.00 USD | `-76.45%` | `4.79` |
| `Live` | `Long` | `545.00` | 856,880,000.00 USD | 0.00 USD | 224,160.00 USD | `-76.01%` | `411.31` |
| `Live` | `Long` | `555.00` | 856,650,000.00 USD | 0.00 USD | 4,450.00 USD | `-75.57%` | `8.02` |
| `Live` | `Long` | `565.00` | 856,650,000.00 USD | 0.00 USD | 57,600.00 USD | `-75.13%` | `101.95` |
| `Live` | `Long` | `575.00` | 856,590,000.00 USD | 0.00 USD | 948,790.00 USD | `-74.69%` | `1,650.07` |
| `Live` | `Long` | `585.00` | 855,640,000.00 USD | 0.00 USD | 3,440.00 USD | `-74.25%` | `5.88` |
| `Live` | `Long` | `595.00` | 855,640,000.00 USD | 0.00 USD | 408,980.00 USD | `-73.81%` | `687.36` |
| `Live` | `Long` | `605.00` | 855,230,000.00 USD | 0.00 USD | 71,270.00 USD | `-73.37%` | `117.80` |
| `Live` | `Long` | `615.00` | 855,160,000.00 USD | 0.00 USD | 23,190.00 USD | `-72.93%` | `37.71` |
| `Live` | `Long` | `625.00` | 855,140,000.00 USD | 0.00 USD | 13,830.00 USD | `-72.49%` | `22.12` |
| `Live` | `Long` | `635.00` | 855,120,000.00 USD | 0.00 USD | 29,140.00 USD | `-72.05%` | `45.89` |
| `Live` | `Long` | `645.00` | 855,090,000.00 USD | 0.00 USD | 3,760.00 USD | `-71.61%` | `5.83` |
| `Live` | `Long` | `655.00` | 855,090,000.00 USD | 0.00 USD | 41,860.00 USD | `-71.17%` | `63.91` |
| `Live` | `Long` | `665.00` | 855,050,000.00 USD | 0.00 USD | 62,980.00 USD | `-70.73%` | `94.71` |
| `Live` | `Long` | `675.00` | 854,980,000.00 USD | 0.00 USD | 3,470.00 USD | `-70.29%` | `5.14` |
| `Live` | `Long` | `685.00` | 854,980,000.00 USD | 0.00 USD | 26,760.00 USD | `-69.85%` | `39.06` |
| `Live` | `Long` | `695.00` | 854,950,000.00 USD | 0.00 USD | 907.04 USD | `-69.41%` | `1.31` |
| `Live` | `Long` | `705.00` | 854,950,000.00 USD | 0.00 USD | 1,530,000.00 USD | `-68.97%` | `2,169.28` |
| `Live` | `Long` | `715.00` | 853,420,000.00 USD | 0.00 USD | 27,410.00 USD | `-68.53%` | `38.34` |
| `Live` | `Long` | `725.00` | 853,400,000.00 USD | 0.00 USD | 1,530,000.00 USD | `-68.09%` | `2,115.25` |
| `Live` | `Long` | `735.00` | 851,860,000.00 USD | 0.00 USD | 64,390.00 USD | `-67.65%` | `87.60` |
| `Live` | `Long` | `745.00` | 851,800,000.00 USD | 0.00 USD | 3,040.00 USD | `-67.21%` | `4.09` |
| `Live` | `Long` | `755.00` | 851,790,000.00 USD | 0.00 USD | 33,350.00 USD | `-66.77%` | `44.17` |
| `Live` | `Long` | `765.00` | 851,760,000.00 USD | 0.00 USD | 4,100.00 USD | `-66.33%` | `5.36` |
| `Live` | `Long` | `775.00` | 851,760,000.00 USD | 0.00 USD | 86,110.00 USD | `-65.89%` | `111.12` |
| `Live` | `Long` | `785.00` | 851,670,000.00 USD | 0.00 USD | 75,350.00 USD | `-65.45%` | `95.99` |
| `Live` | `Long` | `795.00` | 851,600,000.00 USD | 0.00 USD | 581.70 USD | `-65.01%` | `0.73` |
| `Live` | `Long` | `805.00` | 851,600,000.00 USD | 0.00 USD | 21,700.00 USD | `-64.57%` | `26.95` |
| `Live` | `Long` | `815.00` | 851,570,000.00 USD | 0.00 USD | 107,710.00 USD | `-64.13%` | `132.15` |
| `Live` | `Long` | `825.00` | 851,470,000.00 USD | 0.00 USD | 72,460.00 USD | `-63.69%` | `87.83` |
| `Live` | `Long` | `835.00` | 851,390,000.00 USD | 0.00 USD | 123,880.00 USD | `-63.25%` | `148.36` |
| `Live` | `Long` | `845.00` | 851,270,000.00 USD | 0.00 USD | 598,570.00 USD | `-62.81%` | `708.36` |
| `Live` | `Long` | `855.00` | 850,670,000.00 USD | 0.00 USD | 16,080.00 USD | `-62.37%` | `18.81` |
| `Live` | `Long` | `865.00` | 850,650,000.00 USD | 0.00 USD | 161,460.00 USD | `-61.93%` | `186.66` |
| `Live` | `Long` | `875.00` | 850,490,000.00 USD | 0.00 USD | 469,610.00 USD | `-61.49%` | `536.70` |
| `Live` | `Long` | `885.00` | 850,020,000.00 USD | 0.00 USD | 1,000,000.00 USD | `-61.05%` | `1,133.45` |
| `Live` | `Long` | `895.00` | 849,020,000.00 USD | 0.00 USD | 283,040.00 USD | `-60.61%` | `316.25` |
| `Live` | `Long` | `905.00` | 848,740,000.00 USD | 0.00 USD | 10,330.00 USD | `-60.17%` | `11.41` |
| `Live` | `Long` | `915.00` | 848,730,000.00 USD | 0.00 USD | 170,200.00 USD | `-59.73%` | `186.02` |
| `Live` | `Long` | `925.00` | 848,560,000.00 USD | 0.00 USD | 151,920.00 USD | `-59.29%` | `164.23` |
| `Live` | `Long` | `935.00` | 848,410,000.00 USD | 0.00 USD | 29,070.00 USD | `-58.85%` | `31.09` |
| `Live` | `Long` | `945.00` | 848,380,000.00 USD | 0.00 USD | 42,930.00 USD | `-58.41%` | `45.42` |
| `Live` | `Long` | `955.00` | 848,330,000.00 USD | 0.00 USD | 405,980.00 USD | `-57.97%` | `425.11` |
| `Live` | `Long` | `965.00` | 847,930,000.00 USD | 0.00 USD | 26,630.00 USD | `-57.53%` | `27.59` |
| `Live` | `Long` | `975.00` | 847,900,000.00 USD | 0.00 USD | 125,730.00 USD | `-57.09%` | `128.95` |
| `Live` | `Long` | `985.00` | 847,770,000.00 USD | 0.00 USD | 92,350.00 USD | `-56.65%` | `93.76` |
| `Live` | `Long` | `995.00` | 847,680,000.00 USD | 0.00 USD | 30,870.00 USD | `-56.21%` | `31.03` |
| `Live` | `Long` | `1005.00` | 847,650,000.00 USD | 0.00 USD | 1,770,000.00 USD | `-55.77%` | `1,762.46` |
| `Live` | `Long` | `1015.00` | 845,880,000.00 USD | 0.00 USD | 46,850.00 USD | `-55.33%` | `46.16` |
| `Live` | `Long` | `1025.00` | 845,830,000.00 USD | 0.00 USD | 309,600.00 USD | `-54.89%` | `302.05` |
| `Live` | `Long` | `1035.00` | 845,520,000.00 USD | 0.00 USD | 25,540.00 USD | `-54.45%` | `24.68` |
| `Live` | `Long` | `1045.00` | 845,500,000.00 USD | 0.00 USD | 7,720,000.00 USD | `-54.01%` | `7,390.32` |
| `Live` | `Long` | `1055.00` | 837,780,000.00 USD | 0.00 USD | 1,570,000.00 USD | `-53.57%` | `1,491.92` |
| `Live` | `Long` | `1065.00` | 836,200,000.00 USD | 0.00 USD | 212,530.00 USD | `-53.13%` | `199.55` |
| `Live` | `Long` | `1075.00` | 835,990,000.00 USD | 0.00 USD | 657,920.00 USD | `-52.69%` | `612.01` |
| `Live` | `Long` | `1085.00` | 835,330,000.00 USD | 0.00 USD | 54,410.00 USD | `-52.25%` | `50.15` |
| `Live` | `Long` | `1095.00` | 835,280,000.00 USD | 0.00 USD | 137,290.00 USD | `-51.81%` | `125.38` |
| `Live` | `Long` | `1105.00` | 835,140,000.00 USD | 0.00 USD | 2,480,000.00 USD | `-51.37%` | `2,240.94` |
| `Live` | `Long` | `1115.00` | 832,660,000.00 USD | 0.00 USD | 182,280.00 USD | `-50.93%` | `163.48` |
| `Live` | `Long` | `1125.00` | 832,480,000.00 USD | 0.00 USD | 31,010.00 USD | `-50.49%` | `27.56` |
| `Live` | `Long` | `1135.00` | 832,450,000.00 USD | 0.00 USD | 189,070.00 USD | `-50.05%` | `166.58` |
| `Live` | `Long` | `1145.00` | 832,260,000.00 USD | 0.00 USD | 2,270,000.00 USD | `-49.61%` | `1,986.51` |
| `Live` | `Long` | `1155.00` | 829,990,000.00 USD | 0.00 USD | 396,310.00 USD | `-49.17%` | `343.12` |
| `Live` | `Long` | `1165.00` | 829,590,000.00 USD | 0.00 USD | 125,610.00 USD | `-48.73%` | `107.82` |
| `Live` | `Long` | `1175.00` | 829,460,000.00 USD | 0.00 USD | 81,870.00 USD | `-48.29%` | `69.68` |
| `Live` | `Long` | `1185.00` | 829,380,000.00 USD | 0.00 USD | 307,540.00 USD | `-47.85%` | `259.53` |
| `Live` | `Long` | `1195.00` | 829,070,000.00 USD | 0.00 USD | 466,020.00 USD | `-47.41%` | `389.98` |
| `Live` | `Long` | `1205.00` | 828,610,000.00 USD | 0.00 USD | 9,430,000.00 USD | `-46.97%` | `7,826.83` |
| `Live` | `Long` | `1215.00` | 819,180,000.00 USD | 0.00 USD | 11,660,000.00 USD | `-46.53%` | `9,599.65` |
| `Live` | `Long` | `1225.00` | 807,510,000.00 USD | 0.00 USD | 289,940.00 USD | `-46.09%` | `236.69` |
| `Live` | `Long` | `1235.00` | 807,220,000.00 USD | 0.00 USD | 782,060.00 USD | `-45.65%` | `633.25` |
| `Live` | `Long` | `1245.00` | 806,440,000.00 USD | 0.00 USD | 266,630.00 USD | `-45.21%` | `214.16` |
| `Live` | `Long` | `1255.00` | 806,180,000.00 USD | 0.00 USD | 410,370.00 USD | `-44.77%` | `326.99` |
| `Live` | `Long` | `1265.00` | 805,760,000.00 USD | 0.00 USD | 189,820.00 USD | `-44.33%` | `150.05` |
| `Live` | `Long` | `1275.00` | 805,580,000.00 USD | 0.00 USD | 381,930.00 USD | `-43.89%` | `299.55` |
| `Live` | `Long` | `1285.00` | 805,190,000.00 USD | 0.00 USD | 16,180,000.00 USD | `-43.45%` | `12,592.60` |
| `Live` | `Long` | `1295.00` | 789,010,000.00 USD | 0.00 USD | 231,640.00 USD | `-43.01%` | `178.87` |
| `Live` | `Long` | `1305.00` | 788,780,000.00 USD | 0.00 USD | 408,190.00 USD | `-42.57%` | `312.79` |
| `Live` | `Long` | `1315.00` | 788,370,000.00 USD | 0.00 USD | 91,070.00 USD | `-42.13%` | `69.26` |
| `Live` | `Long` | `1325.00` | 788,280,000.00 USD | 0.00 USD | 783,520.00 USD | `-41.69%` | `591.34` |
| `Live` | `Long` | `1335.00` | 787,500,000.00 USD | 0.00 USD | 623,930.00 USD | `-41.25%` | `467.36` |
| `Live` | `Long` | `1345.00` | 786,870,000.00 USD | 0.00 USD | 1,360,000.00 USD | `-40.81%` | `1,011.65` |
| `Live` | `Long` | `1355.00` | 785,510,000.00 USD | 0.00 USD | 388,240.00 USD | `-40.37%` | `286.53` |
| `Live` | `Long` | `1365.00` | 785,120,000.00 USD | 0.00 USD | 13,380,000.00 USD | `-39.93%` | `9,802.11` |
| `Live` | `Long` | `1375.00` | 771,740,000.00 USD | 0.00 USD | 331,630.00 USD | `-39.49%` | `241.18` |
| `Live` | `Long` | `1385.00` | 771,410,000.00 USD | 0.00 USD | 6,940,000.00 USD | `-39.05%` | `5,011.98` |
| `Live` | `Long` | `1395.00` | 764,470,000.00 USD | 0.00 USD | 227,160.00 USD | `-38.61%` | `162.84` |
| `Live` | `Long` | `1405.00` | 764,240,000.00 USD | 0.00 USD | 9,990,000.00 USD | `-38.17%` | `7,107.94` |
| `Live` | `Long` | `1415.00` | 754,260,000.00 USD | 0.00 USD | 74,340.00 USD | `-37.73%` | `52.53` |
| `Live` | `Long` | `1425.00` | 754,180,000.00 USD | 0.00 USD | 693,990.00 USD | `-37.29%` | `487.01` |
| `Live` | `Long` | `1435.00` | 753,490,000.00 USD | 0.00 USD | 901,280.00 USD | `-36.85%` | `628.07` |
| `Live` | `Long` | `1445.00` | 752,590,000.00 USD | 0.00 USD | 980,830.00 USD | `-36.41%` | `678.78` |
| `Live` | `Long` | `1455.00` | 751,610,000.00 USD | 0.00 USD | 76,810.00 USD | `-35.97%` | `52.79` |
| `Live` | `Long` | `1465.00` | 751,530,000.00 USD | 0.00 USD | 490,660.00 USD | `-35.53%` | `334.92` |
| `Live` | `Long` | `1475.00` | 751,040,000.00 USD | 0.00 USD | 5,700,000.00 USD | `-35.08%` | `3,863.45` |
| `Live` | `Long` | `1485.00` | 745,340,000.00 USD | 0.00 USD | 106,380.00 USD | `-34.64%` | `71.64` |
| `Live` | `Long` | `1495.00` | 745,230,000.00 USD | 0.00 USD | 16,370,000.00 USD | `-34.20%` | `10,951.85` |
| `Live` | `Long` | `1505.00` | 728,860,000.00 USD | 0.00 USD | 80,160.00 USD | `-33.76%` | `53.26` |
| `Live` | `Long` | `1515.00` | 728,780,000.00 USD | 0.00 USD | 15,690,000.00 USD | `-33.32%` | `10,354.35` |
| `Live` | `Long` | `1525.00` | 713,090,000.00 USD | 0.00 USD | 25,840,000.00 USD | `-32.88%` | `16,941.61` |
| `Live` | `Long` | `1535.00` | 687,260,000.00 USD | 0.00 USD | 1,140,000.00 USD | `-32.44%` | `740.10` |
| `Live` | `Long` | `1545.00` | 686,120,000.00 USD | 0.00 USD | 4,930,000.00 USD | `-32.00%` | `3,189.92` |
| `Live` | `Long` | `1555.00` | 681,190,000.00 USD | 0.00 USD | 562,470.00 USD | `-31.56%` | `361.71` |
| `Live` | `Long` | `1565.00` | 680,630,000.00 USD | 0.00 USD | 250,640.00 USD | `-31.12%` | `160.15` |
| `Live` | `Long` | `1575.00` | 680,380,000.00 USD | 0.00 USD | 736,930.00 USD | `-30.68%` | `467.89` |
| `Live` | `Long` | `1585.00` | 679,640,000.00 USD | 0.00 USD | 579,830.00 USD | `-30.24%` | `365.82` |
| `Live` | `Long` | `1595.00` | 679,060,000.00 USD | 0.00 USD | 2,130,000.00 USD | `-29.80%` | `1,337.71` |
| `Live` | `Long` | `1605.00` | 676,930,000.00 USD | 0.00 USD | 18,890,000.00 USD | `-29.36%` | `11,768.62` |
| `Live` | `Long` | `1615.00` | 658,040,000.00 USD | 0.00 USD | 307,010.00 USD | `-28.92%` | `190.10` |
| `Live` | `Long` | `1625.00` | 657,730,000.00 USD | 0.00 USD | 214,610.00 USD | `-28.48%` | `132.07` |
| `Live` | `Long` | `1635.00` | 657,520,000.00 USD | 0.00 USD | 19,010,000.00 USD | `-28.04%` | `11,626.99` |
| `Live` | `Long` | `1645.00` | 638,510,000.00 USD | 0.00 USD | 36,430,000.00 USD | `-27.60%` | `22,143.53` |
| `Live` | `Long` | `1655.00` | 602,080,000.00 USD | 0.00 USD | 2,610,000.00 USD | `-27.16%` | `1,574.75` |
| `Live` | `Long` | `1665.00` | 599,480,000.00 USD | 0.00 USD | 19,150,000.00 USD | `-26.72%` | `11,501.81` |
| `Live` | `Long` | `1675.00` | 580,330,000.00 USD | 0.00 USD | 11,640,000.00 USD | `-26.28%` | `6,948.26` |
| `Live` | `Long` | `1685.00` | 568,690,000.00 USD | 0.00 USD | 1,610,000.00 USD | `-25.84%` | `954.97` |
| `Live` | `Long` | `1695.00` | 567,080,000.00 USD | 0.00 USD | 27,870,000.00 USD | `-25.40%` | `16,443.38` |
| `Live` | `Long` | `1705.00` | 539,210,000.00 USD | 0.00 USD | 2,100,000.00 USD | `-24.96%` | `1,233.89` |
| `Live` | `Long` | `1715.00` | 537,100,000.00 USD | 0.00 USD | 335,300.00 USD | `-24.52%` | `195.51` |
| `Live` | `Long` | `1725.00` | 536,770,000.00 USD | 0.00 USD | 35,100,000.00 USD | `-24.08%` | `20,350.72` |
| `Live` | `Long` | `1735.00` | 501,660,000.00 USD | 0.00 USD | 490,830.00 USD | `-23.64%` | `282.90` |
| `Live` | `Long` | `1745.00` | 501,170,000.00 USD | 0.00 USD | 883,670.00 USD | `-23.20%` | `506.40` |
| `Live` | `Long` | `1755.00` | 500,290,000.00 USD | 0.00 USD | 372,910.00 USD | `-22.76%` | `212.48` |
| `Live` | `Long` | `1765.00` | 499,920,000.00 USD | 0.00 USD | 815,120.00 USD | `-22.32%` | `461.83` |
| `Live` | `Long` | `1775.00` | 499,100,000.00 USD | 0.00 USD | 1,200,000.00 USD | `-21.88%` | `676.81` |
| `Live` | `Long` | `1785.00` | 497,900,000.00 USD | 0.00 USD | 58,810,000.00 USD | `-21.44%` | `32,946.49` |
| `Live` | `Long` | `1795.00` | 439,090,000.00 USD | 0.00 USD | 451,160.00 USD | `-21.00%` | `251.34` |
| `Live` | `Long` | `1805.00` | 438,640,000.00 USD | 0.00 USD | 14,610,000.00 USD | `-20.56%` | `8,093.60` |
| `Live` | `Long` | `1815.00` | 424,030,000.00 USD | 0.00 USD | 823,030.00 USD | `-20.12%` | `453.46` |
| `Live` | `Long` | `1825.00` | 423,210,000.00 USD | 0.00 USD | 602,550.00 USD | `-19.68%` | `330.17` |
| `Live` | `Long` | `1835.00` | 422,610,000.00 USD | 0.00 USD | 1,240,000.00 USD | `-19.24%` | `673.54` |
| `Live` | `Long` | `1845.00` | 421,370,000.00 USD | 0.00 USD | 1,560,000.00 USD | `-18.80%` | `846.81` |
| `Live` | `Long` | `1855.00` | 419,810,000.00 USD | 0.00 USD | 5,030,000.00 USD | `-18.36%` | `2,710.29` |
| `Live` | `Long` | `1865.00` | 414,780,000.00 USD | 0.00 USD | 531,380.00 USD | `-17.92%` | `284.92` |
| `Live` | `Long` | `1875.00` | 414,250,000.00 USD | 0.00 USD | 7,010,000.00 USD | `-17.48%` | `3,737.71` |
| `Live` | `Long` | `1885.00` | 407,240,000.00 USD | 0.00 USD | 4,040,000.00 USD | `-17.04%` | `2,141.05` |
| `Live` | `Long` | `1895.00` | 403,200,000.00 USD | 0.00 USD | 5,640,000.00 USD | `-16.60%` | `2,974.04` |
| `Live` | `Long` | `1905.00` | 397,570,000.00 USD | 0.00 USD | 791,000.00 USD | `-16.16%` | `415.22` |
| `Live` | `Long` | `1915.00` | 396,780,000.00 USD | 0.00 USD | 14,710,000.00 USD | `-15.72%` | `7,679.39` |
| `Live` | `Long` | `1925.00` | 382,070,000.00 USD | 0.00 USD | 19,870,000.00 USD | `-15.28%` | `10,319.99` |
| `Live` | `Long` | `1935.00` | 362,210,000.00 USD | 0.00 USD | 5,410,000.00 USD | `-14.84%` | `2,794.26` |
| `Live` | `Long` | `1945.00` | 356,800,000.00 USD | 0.00 USD | 1,530,000.00 USD | `-14.40%` | `787.76` |
| `Live` | `Long` | `1955.00` | 355,270,000.00 USD | 0.00 USD | 4,410,000.00 USD | `-13.96%` | `2,254.03` |
| `Live` | `Long` | `1965.00` | 350,860,000.00 USD | 0.00 USD | 810,350.00 USD | `-13.52%` | `412.39` |
| `Live` | `Long` | `1975.00` | 350,050,000.00 USD | 0.00 USD | 2,680,000.00 USD | `-13.08%` | `1,359.13` |
| `Live` | `Long` | `1985.00` | 347,360,000.00 USD | 0.00 USD | 5,240,000.00 USD | `-12.64%` | `2,639.02` |
| `Live` | `Long` | `1995.00` | 342,130,000.00 USD | 0.00 USD | 10,940,000.00 USD | `-12.20%` | `5,482.47` |
| `Live` | `Long` | `2005.00` | 331,190,000.00 USD | 0.00 USD | 1,820,000.00 USD | `-11.76%` | `907.74` |
| `Live` | `Long` | `2015.00` | 329,370,000.00 USD | 0.00 USD | 6,680,000.00 USD | `-11.32%` | `3,315.70` |
| `Live` | `Long` | `2025.00` | 322,690,000.00 USD | 0.00 USD | 1,710,000.00 USD | `-10.88%` | `845.26` |
| `Live` | `Long` | `2035.00` | 320,980,000.00 USD | 0.00 USD | 1,790,000.00 USD | `-10.44%` | `878.05` |
| `Live` | `Long` | `2045.00` | 319,190,000.00 USD | 0.00 USD | 17,480,000.00 USD | `-10.00%` | `8,546.11` |
| `Live` | `Long` | `2055.00` | 301,710,000.00 USD | 0.00 USD | 5,010,000.00 USD | `-9.56%` | `2,437.97` |
| `Live` | `Long` | `2065.00` | 296,700,000.00 USD | 0.00 USD | 2,650,000.00 USD | `-9.12%` | `1,282.56` |
| `Live` | `Long` | `2075.00` | 294,050,000.00 USD | 0.00 USD | 3,470,000.00 USD | `-8.68%` | `1,674.52` |
| `Live` | `Long` | `2085.00` | 290,580,000.00 USD | 0.00 USD | 1,850,000.00 USD | `-8.24%` | `886.41` |
| `Live` | `Long` | `2095.00` | 288,730,000.00 USD | 0.00 USD | 2,410,000.00 USD | `-7.80%` | `1,149.70` |
| `Live` | `Long` | `2105.00` | 286,320,000.00 USD | 0.00 USD | 1,670,000.00 USD | `-7.36%` | `795.67` |
| `Live` | `Long` | `2115.00` | 284,650,000.00 USD | 0.00 USD | 1,430,000.00 USD | `-6.92%` | `676.35` |
| `Live` | `Long` | `2125.00` | 283,220,000.00 USD | 0.00 USD | 17,940,000.00 USD | `-6.48%` | `8,440.83` |
| `Live` | `Long` | `2135.00` | 265,280,000.00 USD | 0.00 USD | 14,630,000.00 USD | `-6.04%` | `6,851.47` |
| `Live` | `Long` | `2145.00` | 250,650,000.00 USD | 0.00 USD | 7,440,000.00 USD | `-5.60%` | `3,469.58` |
| `Live` | `Long` | `2155.00` | 243,210,000.00 USD | 0.00 USD | 2,180,000.00 USD | `-5.16%` | `1,009.40` |
| `Live` | `Long` | `2165.00` | 241,030,000.00 USD | 0.00 USD | 6,820,000.00 USD | `-4.72%` | `3,151.79` |
| `Live` | `Long` | `2175.00` | 234,210,000.00 USD | 0.00 USD | 109,290,000.00 USD | `-4.28%` | `50,248.47` |
| `Live` | `Long` | `2185.00` | 124,920,000.00 USD | 0.00 USD | 100,000,000.00 USD | `-3.84%` | `45,764.34` |
| `Live` | `Long` | `2195.00` | 24,930,000.00 USD | 0.00 USD | 2,280,000.00 USD | `-3.40%` | `1,037.79` |
| `Live` | `Long` | `2205.00` | 22,650,000.00 USD | 0.00 USD | 8,120,000.00 USD | `-2.96%` | `3,681.16` |
| `Live` | `Long` | `2215.00` | 14,530,000.00 USD | 0.00 USD | 4,660,000.00 USD | `-2.52%` | `2,103.75` |
| `Live` | `Long` | `2225.00` | 9,870,000.00 USD | 0.00 USD | 5,380,000.00 USD | `-2.08%` | `2,416.19` |
| `Live` | `Short` | `2235.00` | 878,090.00 USD | 878,090.00 USD | 0.00 USD | `-1.64%` | `392.88` |
| `Live` | `Long` | `2245.00` | 4,500,000.00 USD | 0.00 USD | 4,430,000.00 USD | `-1.20%` | `1,971.86` |
| `Live` | `Long` | `2255.00` | 68,250.00 USD | 0.00 USD | 68,250.00 USD | `-0.76%` | `30.27` |
| `Live` | `Short` | `2265.00` | 878,500.00 USD | 410.42 USD | 0.00 USD | `-0.32%` | `0.18` |
| `Live` | `Short` | `2275.00` | 879,130.00 USD | 633.82 USD | 0.00 USD | `+0.12%` | `0.28` |
| `Live` | `Short` | `2285.00` | 881,660.00 USD | 2,530.00 USD | 0.00 USD | `+0.56%` | `1.11` |
| `Live` | `Short` | `2295.00` | 906,890.00 USD | 25,230.00 USD | 0.00 USD | `+1.00%` | `10.99` |
| `Live` | `Short` | `2305.00` | 5,150,000.00 USD | 4,250,000.00 USD | 0.00 USD | `+1.44%` | `1,842.89` |
| `Live` | `Short` | `2315.00` | 7,630,000.00 USD | 2,480,000.00 USD | 0.00 USD | `+1.88%` | `1,069.66` |
| `Live` | `Short` | `2325.00` | 9,060,000.00 USD | 1,420,000.00 USD | 0.00 USD | `+2.32%` | `612.90` |
| `Live` | `Short` | `2335.00` | 10,290,000.00 USD | 1,230,000.00 USD | 0.00 USD | `+2.76%` | `528.81` |
| `Live` | `Short` | `2345.00` | 10,620,000.00 USD | 326,400.00 USD | 0.00 USD | `+3.20%` | `139.19` |
| `Live` | `Short` | `2355.00` | 11,890,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+3.64%` | `541.25` |
| `Live` | `Short` | `2365.00` | 13,210,000.00 USD | 1,310,000.00 USD | 0.00 USD | `+4.08%` | `555.88` |
| `Live` | `Short` | `2375.00` | 14,270,000.00 USD | 1,060,000.00 USD | 0.00 USD | `+4.52%` | `447.33` |
| `Live` | `Short` | `2385.00` | 56,360,000.00 USD | 42,090,000.00 USD | 0.00 USD | `+4.96%` | `17,647.58` |
| `Live` | `Short` | `2395.00` | 56,460,000.00 USD | 99,780.00 USD | 0.00 USD | `+5.40%` | `41.66` |
| `Live` | `Short` | `2405.00` | 57,890,000.00 USD | 1,430,000.00 USD | 0.00 USD | `+5.84%` | `596.07` |
| `Live` | `Short` | `2415.00` | 58,750,000.00 USD | 858,190.00 USD | 0.00 USD | `+6.28%` | `355.36` |
| `Live` | `Short` | `2425.00` | 59,700,000.00 USD | 953,600.00 USD | 0.00 USD | `+6.72%` | `393.24` |
| `Live` | `Short` | `2435.00` | 64,150,000.00 USD | 4,450,000.00 USD | 0.00 USD | `+7.16%` | `1,827.05` |
| `Live` | `Short` | `2445.00` | 64,430,000.00 USD | 280,670.00 USD | 0.00 USD | `+7.60%` | `114.79` |
| `Live` | `Short` | `2455.00` | 64,530,000.00 USD | 96,380.00 USD | 0.00 USD | `+8.05%` | `39.26` |
| `Live` | `Short` | `2465.00` | 65,440,000.00 USD | 914,970.00 USD | 0.00 USD | `+8.49%` | `371.19` |
| `Live` | `Short` | `2475.00` | 65,880,000.00 USD | 438,920.00 USD | 0.00 USD | `+8.93%` | `177.34` |
| `Live` | `Short` | `2485.00` | 65,980,000.00 USD | 96,970.00 USD | 0.00 USD | `+9.37%` | `39.02` |
| `Live` | `Short` | `2495.00` | 74,740,000.00 USD | 8,760,000.00 USD | 0.00 USD | `+9.81%` | `3,510.88` |
| `Live` | `Short` | `2505.00` | 77,050,000.00 USD | 2,310,000.00 USD | 0.00 USD | `+10.25%` | `921.40` |
| `Live` | `Short` | `2515.00` | 77,190,000.00 USD | 142,410.00 USD | 0.00 USD | `+10.69%` | `56.62` |
| `Live` | `Short` | `2525.00` | 81,900,000.00 USD | 4,710,000.00 USD | 0.00 USD | `+11.13%` | `1,865.05` |
| `Live` | `Short` | `2535.00` | 84,420,000.00 USD | 2,520,000.00 USD | 0.00 USD | `+11.57%` | `995.66` |
| `Live` | `Short` | `2545.00` | 89,800,000.00 USD | 5,380,000.00 USD | 0.00 USD | `+12.01%` | `2,113.39` |
| `Live` | `Short` | `2555.00` | 90,200,000.00 USD | 397,740.00 USD | 0.00 USD | `+12.45%` | `155.67` |
| `Live` | `Short` | `2565.00` | 92,600,000.00 USD | 2,400,000.00 USD | 0.00 USD | `+12.89%` | `934.73` |
| `Live` | `Short` | `2575.00` | 104,220,000.00 USD | 11,620,000.00 USD | 0.00 USD | `+13.33%` | `4,513.94` |
| `Live` | `Short` | `2585.00` | 130,690,000.00 USD | 26,470,000.00 USD | 0.00 USD | `+13.77%` | `10,241.00` |
| `Live` | `Short` | `2595.00` | 132,600,000.00 USD | 1,910,000.00 USD | 0.00 USD | `+14.21%` | `735.54` |
| `Live` | `Short` | `2605.00` | 146,850,000.00 USD | 14,250,000.00 USD | 0.00 USD | `+14.65%` | `5,470.07` |
| `Live` | `Short` | `2615.00` | 147,150,000.00 USD | 293,190.00 USD | 0.00 USD | `+15.09%` | `112.12` |
| `Live` | `Short` | `2625.00` | 160,180,000.00 USD | 13,030,000.00 USD | 0.00 USD | `+15.53%` | `4,964.26` |
| `Live` | `Short` | `2635.00` | 164,770,000.00 USD | 4,590,000.00 USD | 0.00 USD | `+15.97%` | `1,743.53` |
| `Live` | `Short` | `2645.00` | 164,850,000.00 USD | 75,760.00 USD | 0.00 USD | `+16.41%` | `28.64` |
| `Live` | `Short` | `2655.00` | 200,720,000.00 USD | 35,870,000.00 USD | 0.00 USD | `+16.85%` | `13,509.88` |
| `Live` | `Short` | `2665.00` | 200,830,000.00 USD | 115,060.00 USD | 0.00 USD | `+17.29%` | `43.18` |
| `Live` | `Short` | `2675.00` | 201,270,000.00 USD | 439,350.00 USD | 0.00 USD | `+17.73%` | `164.24` |
| `Live` | `Short` | `2685.00` | 202,150,000.00 USD | 877,180.00 USD | 0.00 USD | `+18.17%` | `326.70` |
| `Live` | `Short` | `2695.00` | 202,280,000.00 USD | 134,610.00 USD | 0.00 USD | `+18.61%` | `49.95` |
| `Live` | `Short` | `2705.00` | 231,730,000.00 USD | 29,450,000.00 USD | 0.00 USD | `+19.05%` | `10,887.49` |
| `Live` | `Short` | `2715.00` | 231,820,000.00 USD | 90,570.00 USD | 0.00 USD | `+19.49%` | `33.36` |
| `Live` | `Short` | `2725.00` | 232,980,000.00 USD | 1,150,000.00 USD | 0.00 USD | `+19.93%` | `423.30` |
| `Live` | `Short` | `2735.00` | 233,270,000.00 USD | 298,530.00 USD | 0.00 USD | `+20.37%` | `109.15` |
| `Live` | `Short` | `2745.00` | 234,550,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+20.81%` | `463.07` |
| `Live` | `Short` | `2755.00` | 235,130,000.00 USD | 587,770.00 USD | 0.00 USD | `+21.25%` | `213.35` |
| `Live` | `Short` | `2765.00` | 235,260,000.00 USD | 123,300.00 USD | 0.00 USD | `+21.69%` | `44.59` |
| `Live` | `Short` | `2775.00` | 235,400,000.00 USD | 143,910.00 USD | 0.00 USD | `+22.13%` | `51.86` |
| `Live` | `Short` | `2785.00` | 237,280,000.00 USD | 1,870,000.00 USD | 0.00 USD | `+22.57%` | `673.19` |
| `Live` | `Short` | `2795.00` | 237,340,000.00 USD | 59,340.00 USD | 0.00 USD | `+23.01%` | `21.23` |
| `Live` | `Short` | `2805.00` | 241,440,000.00 USD | 4,100,000.00 USD | 0.00 USD | `+23.45%` | `1,462.14` |
| `Live` | `Short` | `2815.00` | 278,390,000.00 USD | 36,950,000.00 USD | 0.00 USD | `+23.89%` | `13,126.52` |
| `Live` | `Short` | `2825.00` | 278,570,000.00 USD | 180,820.00 USD | 0.00 USD | `+24.33%` | `64.01` |
| `Live` | `Short` | `2835.00` | 282,710,000.00 USD | 4,140,000.00 USD | 0.00 USD | `+24.77%` | `1,461.49` |
| `Live` | `Short` | `2845.00` | 284,870,000.00 USD | 2,160,000.00 USD | 0.00 USD | `+25.21%` | `760.27` |
| `Live` | `Short` | `2855.00` | 285,470,000.00 USD | 590,830.00 USD | 0.00 USD | `+25.65%` | `206.94` |
| `Live` | `Short` | `2865.00` | 285,570,000.00 USD | 101,470.00 USD | 0.00 USD | `+26.09%` | `35.42` |
| `Live` | `Short` | `2875.00` | 285,630,000.00 USD | 65,130.00 USD | 0.00 USD | `+26.53%` | `22.65` |
| `Live` | `Short` | `2885.00` | 287,810,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+26.97%` | `755.74` |
| `Live` | `Short` | `2895.00` | 288,150,000.00 USD | 333,130.00 USD | 0.00 USD | `+27.41%` | `115.07` |
| `Live` | `Short` | `2905.00` | 288,730,000.00 USD | 588,570.00 USD | 0.00 USD | `+27.85%` | `202.61` |
| `Live` | `Short` | `2915.00` | 316,490,000.00 USD | 27,760,000.00 USD | 0.00 USD | `+28.29%` | `9,522.69` |
| `Live` | `Short` | `2925.00` | 337,900,000.00 USD | 21,410,000.00 USD | 0.00 USD | `+28.73%` | `7,320.16` |
| `Live` | `Short` | `2935.00` | 338,370,000.00 USD | 463,430.00 USD | 0.00 USD | `+29.17%` | `157.90` |
| `Live` | `Short` | `2945.00` | 338,830,000.00 USD | 465,540.00 USD | 0.00 USD | `+29.61%` | `158.08` |
| `Live` | `Short` | `2955.00` | 338,990,000.00 USD | 152,600.00 USD | 0.00 USD | `+30.05%` | `51.64` |
| `Live` | `Short` | `2965.00` | 339,540,000.00 USD | 556,280.00 USD | 0.00 USD | `+30.49%` | `187.61` |
| `Live` | `Short` | `2975.00` | 339,720,000.00 USD | 174,230.00 USD | 0.00 USD | `+30.93%` | `58.57` |
| `Live` | `Short` | `2985.00` | 339,830,000.00 USD | 110,600.00 USD | 0.00 USD | `+31.37%` | `37.05` |
| `Live` | `Short` | `2995.00` | 360,770,000.00 USD | 20,950,000.00 USD | 0.00 USD | `+31.81%` | `6,993.35` |
| `Live` | `Short` | `3005.00` | 362,510,000.00 USD | 1,730,000.00 USD | 0.00 USD | `+32.25%` | `577.33` |
| `Live` | `Short` | `3015.00` | 362,810,000.00 USD | 299,170.00 USD | 0.00 USD | `+32.69%` | `99.23` |
| `Live` | `Short` | `3025.00` | 364,790,000.00 USD | 1,980,000.00 USD | 0.00 USD | `+33.13%` | `655.44` |
| `Live` | `Short` | `3035.00` | 366,380,000.00 USD | 1,590,000.00 USD | 0.00 USD | `+33.57%` | `524.18` |
| `Live` | `Short` | `3045.00` | 385,310,000.00 USD | 18,930,000.00 USD | 0.00 USD | `+34.01%` | `6,215.60` |
| `Live` | `Short` | `3055.00` | 387,510,000.00 USD | 2,210,000.00 USD | 0.00 USD | `+34.45%` | `722.97` |
| `Live` | `Short` | `3065.00` | 393,650,000.00 USD | 6,140,000.00 USD | 0.00 USD | `+34.89%` | `2,002.48` |
| `Live` | `Short` | `3075.00` | 396,770,000.00 USD | 3,120,000.00 USD | 0.00 USD | `+35.33%` | `1,014.47` |
| `Live` | `Short` | `3085.00` | 396,870,000.00 USD | 101,440.00 USD | 0.00 USD | `+35.77%` | `32.88` |
| `Live` | `Short` | `3095.00` | 399,270,000.00 USD | 2,400,000.00 USD | 0.00 USD | `+36.21%` | `775.11` |
| `Live` | `Short` | `3105.00` | 402,190,000.00 USD | 2,920,000.00 USD | 0.00 USD | `+36.65%` | `941.16` |
| `Live` | `Short` | `3115.00` | 403,030,000.00 USD | 833,940.00 USD | 0.00 USD | `+37.09%` | `267.72` |
| `Live` | `Short` | `3125.00` | 403,200,000.00 USD | 167,670.00 USD | 0.00 USD | `+37.53%` | `53.66` |
| `Live` | `Short` | `3135.00` | 403,650,000.00 USD | 454,470.00 USD | 0.00 USD | `+37.97%` | `144.97` |
| `Live` | `Short` | `3145.00` | 414,190,000.00 USD | 10,540,000.00 USD | 0.00 USD | `+38.41%` | `3,351.88` |
| `Live` | `Short` | `3155.00` | 414,310,000.00 USD | 119,030.00 USD | 0.00 USD | `+38.85%` | `37.73` |
| `Live` | `Short` | `3165.00` | 414,450,000.00 USD | 133,900.00 USD | 0.00 USD | `+39.29%` | `42.31` |
| `Live` | `Short` | `3175.00` | 421,200,000.00 USD | 6,760,000.00 USD | 0.00 USD | `+39.73%` | `2,128.45` |
| `Live` | `Short` | `3185.00` | 423,770,000.00 USD | 2,560,000.00 USD | 0.00 USD | `+40.17%` | `804.48` |
| `Live` | `Short` | `3195.00` | 428,520,000.00 USD | 4,760,000.00 USD | 0.00 USD | `+40.61%` | `1,488.44` |
| `Live` | `Short` | `3205.00` | 428,600,000.00 USD | 79,400.00 USD | 0.00 USD | `+41.05%` | `24.77` |
| `Live` | `Short` | `3215.00` | 429,200,000.00 USD | 603,280.00 USD | 0.00 USD | `+41.49%` | `187.65` |
| `Live` | `Short` | `3225.00` | 429,240,000.00 USD | 38,690.00 USD | 0.00 USD | `+41.93%` | `12.00` |
| `Live` | `Short` | `3235.00` | 429,460,000.00 USD | 215,450.00 USD | 0.00 USD | `+42.37%` | `66.60` |
| `Live` | `Short` | `3245.00` | 438,040,000.00 USD | 8,580,000.00 USD | 0.00 USD | `+42.81%` | `2,645.24` |
| `Live` | `Short` | `3255.00` | 438,050,000.00 USD | 10,740.00 USD | 0.00 USD | `+43.25%` | `3.30` |
| `Live` | `Short` | `3265.00` | 438,230,000.00 USD | 178,100.00 USD | 0.00 USD | `+43.69%` | `54.55` |
| `Live` | `Short` | `3275.00` | 438,370,000.00 USD | 141,610.00 USD | 0.00 USD | `+44.13%` | `43.24` |
| `Live` | `Short` | `3285.00` | 447,130,000.00 USD | 8,760,000.00 USD | 0.00 USD | `+44.57%` | `2,667.56` |
| `Live` | `Short` | `3295.00` | 452,390,000.00 USD | 5,260,000.00 USD | 0.00 USD | `+45.01%` | `1,595.82` |
| `Live` | `Short` | `3305.00` | 454,250,000.00 USD | 1,850,000.00 USD | 0.00 USD | `+45.45%` | `561.21` |
| `Live` | `Short` | `3315.00` | 455,020,000.00 USD | 770,350.00 USD | 0.00 USD | `+45.89%` | `232.38` |
| `Live` | `Short` | `3325.00` | 455,290,000.00 USD | 273,560.00 USD | 0.00 USD | `+46.33%` | `82.27` |
| `Live` | `Short` | `3335.00` | 455,350,000.00 USD | 58,040.00 USD | 0.00 USD | `+46.77%` | `17.40` |
| `Live` | `Short` | `3345.00` | 455,370,000.00 USD | 20,590.00 USD | 0.00 USD | `+47.21%` | `6.16` |
| `Live` | `Short` | `3355.00` | 455,850,000.00 USD | 480,680.00 USD | 0.00 USD | `+47.65%` | `143.27` |
| `Live` | `Short` | `3365.00` | 456,410,000.00 USD | 554,020.00 USD | 0.00 USD | `+48.09%` | `164.64` |
| `Live` | `Short` | `3375.00` | 456,460,000.00 USD | 54,970.00 USD | 0.00 USD | `+48.53%` | `16.29` |
| `Live` | `Short` | `3385.00` | 457,240,000.00 USD | 781,690.00 USD | 0.00 USD | `+48.97%` | `230.93` |
| `Live` | `Short` | `3395.00` | 457,280,000.00 USD | 41,180.00 USD | 0.00 USD | `+49.41%` | `12.13` |
| `Live` | `Short` | `3405.00` | 459,750,000.00 USD | 2,470,000.00 USD | 0.00 USD | `+49.85%` | `724.77` |
| `Live` | `Short` | `3415.00` | 459,790,000.00 USD | 35,070.00 USD | 0.00 USD | `+50.29%` | `10.27` |
| `Live` | `Short` | `3425.00` | 474,400,000.00 USD | 14,610,000.00 USD | 0.00 USD | `+50.73%` | `4,266.08` |
| `Live` | `Short` | `3435.00` | 474,800,000.00 USD | 405,420.00 USD | 0.00 USD | `+51.18%` | `118.03` |
| `Live` | `Short` | `3445.00` | 474,840,000.00 USD | 39,140.00 USD | 0.00 USD | `+51.62%` | `11.36` |
| `Live` | `Short` | `3455.00` | 475,830,000.00 USD | 983,340.00 USD | 0.00 USD | `+52.06%` | `284.61` |
| `Live` | `Short` | `3465.00` | 475,910,000.00 USD | 80,780.00 USD | 0.00 USD | `+52.50%` | `23.31` |
| `Live` | `Short` | `3475.00` | 535,010,000.00 USD | 59,100,000.00 USD | 0.00 USD | `+52.94%` | `17,007.94` |
| `Live` | `Short` | `3485.00` | 536,090,000.00 USD | 1,080,000.00 USD | 0.00 USD | `+53.38%` | `310.77` |
| `Live` | `Short` | `3495.00` | 537,360,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+53.82%` | `364.11` |
| `Live` | `Short` | `3505.00` | 537,400,000.00 USD | 34,200.00 USD | 0.00 USD | `+54.26%` | `9.76` |
| `Live` | `Short` | `3515.00` | 537,460,000.00 USD | 57,680.00 USD | 0.00 USD | `+54.70%` | `16.41` |
| `Live` | `Short` | `3525.00` | 537,770,000.00 USD | 317,970.00 USD | 0.00 USD | `+55.14%` | `90.21` |
| `Live` | `Short` | `3535.00` | 538,230,000.00 USD | 453,790.00 USD | 0.00 USD | `+55.58%` | `128.37` |
| `Live` | `Short` | `3545.00` | 538,260,000.00 USD | 31,840.00 USD | 0.00 USD | `+56.02%` | `8.98` |
| `Live` | `Short` | `3555.00` | 538,430,000.00 USD | 172,980.00 USD | 0.00 USD | `+56.46%` | `48.66` |
| `Live` | `Short` | `3565.00` | 538,500,000.00 USD | 62,420.00 USD | 0.00 USD | `+56.90%` | `17.51` |
| `Live` | `Short` | `3575.00` | 540,180,000.00 USD | 1,680,000.00 USD | 0.00 USD | `+57.34%` | `470.52` |
| `Live` | `Short` | `3585.00` | 540,750,000.00 USD | 568,830.00 USD | 0.00 USD | `+57.78%` | `158.67` |
| `Live` | `Short` | `3595.00` | 541,070,000.00 USD | 324,630.00 USD | 0.00 USD | `+58.22%` | `90.30` |
| `Live` | `Short` | `3605.00` | 541,210,000.00 USD | 135,550.00 USD | 0.00 USD | `+58.66%` | `37.60` |
| `Live` | `Short` | `3615.00` | 545,500,000.00 USD | 4,290,000.00 USD | 0.00 USD | `+59.10%` | `1,187.15` |
| `Live` | `Short` | `3625.00` | 546,070,000.00 USD | 567,320.00 USD | 0.00 USD | `+59.54%` | `156.50` |
| `Live` | `Short` | `3635.00` | 553,410,000.00 USD | 7,340,000.00 USD | 0.00 USD | `+59.98%` | `2,020.60` |
| `Live` | `Short` | `3645.00` | 559,890,000.00 USD | 6,480,000.00 USD | 0.00 USD | `+60.42%` | `1,778.87` |
| `Live` | `Short` | `3655.00` | 559,920,000.00 USD | 24,380.00 USD | 0.00 USD | `+60.86%` | `6.67` |
| `Live` | `Short` | `3665.00` | 560,200,000.00 USD | 283,220.00 USD | 0.00 USD | `+61.30%` | `77.28` |
| `Live` | `Short` | `3675.00` | 560,550,000.00 USD | 345,780.00 USD | 0.00 USD | `+61.74%` | `94.09` |
| `Live` | `Short` | `3685.00` | 560,750,000.00 USD | 198,930.00 USD | 0.00 USD | `+62.18%` | `53.98` |
| `Live` | `Short` | `3695.00` | 560,870,000.00 USD | 126,340.00 USD | 0.00 USD | `+62.62%` | `34.19` |
| `Live` | `Short` | `3705.00` | 560,950,000.00 USD | 79,680.00 USD | 0.00 USD | `+63.06%` | `21.51` |
| `Live` | `Short` | `3715.00` | 561,150,000.00 USD | 194,910.00 USD | 0.00 USD | `+63.50%` | `52.47` |
| `Live` | `Short` | `3725.00` | 561,410,000.00 USD | 260,570.00 USD | 0.00 USD | `+63.94%` | `69.95` |
| `Live` | `Short` | `3735.00` | 561,720,000.00 USD | 315,000.00 USD | 0.00 USD | `+64.38%` | `84.34` |
| `Live` | `Short` | `3745.00` | 562,560,000.00 USD | 840,410.00 USD | 0.00 USD | `+64.82%` | `224.41` |
| `Live` | `Short` | `3755.00` | 565,030,000.00 USD | 2,460,000.00 USD | 0.00 USD | `+65.26%` | `655.89` |
| `Live` | `Short` | `3765.00` | 566,810,000.00 USD | 1,780,000.00 USD | 0.00 USD | `+65.70%` | `473.97` |
| `Live` | `Short` | `3775.00` | 567,450,000.00 USD | 638,640.00 USD | 0.00 USD | `+66.14%` | `169.18` |
| `Live` | `Short` | `3785.00` | 567,570,000.00 USD | 123,580.00 USD | 0.00 USD | `+66.58%` | `32.65` |
| `Live` | `Short` | `3795.00` | 567,570,000.00 USD | 955.58 USD | 0.00 USD | `+67.02%` | `0.25` |
| `Live` | `Short` | `3805.00` | 567,630,000.00 USD | 52,480.00 USD | 0.00 USD | `+67.46%` | `13.79` |
| `Live` | `Short` | `3815.00` | 568,430,000.00 USD | 807,620.00 USD | 0.00 USD | `+67.90%` | `211.70` |
| `Live` | `Short` | `3825.00` | 568,490,000.00 USD | 53,370.00 USD | 0.00 USD | `+68.34%` | `13.95` |
| `Live` | `Short` | `3835.00` | 619,660,000.00 USD | 51,170,000.00 USD | 0.00 USD | `+68.78%` | `13,343.45` |
| `Live` | `Short` | `3845.00` | 619,810,000.00 USD | 145,840.00 USD | 0.00 USD | `+69.22%` | `37.93` |
| `Live` | `Short` | `3855.00` | 621,840,000.00 USD | 2,040,000.00 USD | 0.00 USD | `+69.66%` | `528.23` |
| `Live` | `Short` | `3865.00` | 622,320,000.00 USD | 480,540.00 USD | 0.00 USD | `+70.10%` | `124.33` |
| `Live` | `Short` | `3875.00` | 623,410,000.00 USD | 1,090,000.00 USD | 0.00 USD | `+70.54%` | `280.08` |
| `Live` | `Short` | `3885.00` | 625,700,000.00 USD | 2,290,000.00 USD | 0.00 USD | `+70.98%` | `590.29` |
| `Live` | `Short` | `3895.00` | 625,800,000.00 USD | 104,030.00 USD | 0.00 USD | `+71.42%` | `26.71` |
| `Live` | `Short` | `3905.00` | 626,590,000.00 USD | 790,430.00 USD | 0.00 USD | `+71.86%` | `202.42` |
| `Live` | `Short` | `3915.00` | 626,630,000.00 USD | 37,680.00 USD | 0.00 USD | `+72.30%` | `9.62` |
| `Live` | `Short` | `3925.00` | 626,820,000.00 USD | 186,310.00 USD | 0.00 USD | `+72.74%` | `47.47` |
| `Live` | `Short` | `3935.00` | 636,330,000.00 USD | 9,510,000.00 USD | 0.00 USD | `+73.18%` | `2,416.09` |
| `Live` | `Short` | `3945.00` | 636,500,000.00 USD | 171,110.00 USD | 0.00 USD | `+73.62%` | `43.37` |
| `Live` | `Short` | `3955.00` | 1,060,000,000.00 USD | 420,960,000.00 USD | 0.00 USD | `+74.06%` | `106,437.65` |
| `Live` | `Short` | `3965.00` | 1,060,000,000.00 USD | 1,030.00 USD | 0.00 USD | `+74.50%` | `0.26` |
| `Live` | `Short` | `3975.00` | 1,060,000,000.00 USD | 587,840.00 USD | 0.00 USD | `+74.94%` | `147.88` |
| `Live` | `Short` | `3985.00` | 1,060,000,000.00 USD | 625,370.00 USD | 0.00 USD | `+75.38%` | `156.93` |
| `Live` | `Short` | `3995.00` | 1,060,000,000.00 USD | 141,210.00 USD | 0.00 USD | `+75.82%` | `35.35` |
| `Live` | `Short` | `4005.00` | 1,060,000,000.00 USD | 318,570.00 USD | 0.00 USD | `+76.26%` | `79.54` |
| `Live` | `Short` | `4015.00` | 1,090,000,000.00 USD | 30,810,000.00 USD | 0.00 USD | `+76.70%` | `7,673.44` |
| `Live` | `Short` | `4025.00` | 1,090,000,000.00 USD | 91,580.00 USD | 0.00 USD | `+77.14%` | `22.75` |
| `Live` | `Short` | `4035.00` | 1,090,000,000.00 USD | 255,490.00 USD | 0.00 USD | `+77.58%` | `63.32` |
| `Live` | `Short` | `4055.00` | 1,180,000,000.00 USD | 93,490,000.00 USD | 0.00 USD | `+78.46%` | `23,055.10` |
| `Live` | `Short` | `4065.00` | 1,180,000,000.00 USD | 12,200.00 USD | 0.00 USD | `+78.90%` | `3.00` |
| `Live` | `Short` | `4075.00` | 1,190,000,000.00 USD | 2,870,000.00 USD | 0.00 USD | `+79.34%` | `703.07` |
| `Live` | `Short` | `4085.00` | 1,190,000,000.00 USD | 2,710.00 USD | 0.00 USD | `+79.78%` | `0.66` |
| `Live` | `Short` | `4095.00` | 1,190,000,000.00 USD | 54,520.00 USD | 0.00 USD | `+80.22%` | `13.31` |
| `Live` | `Short` | `4105.00` | 1,190,000,000.00 USD | 2,120,000.00 USD | 0.00 USD | `+80.66%` | `515.88` |
| `Live` | `Short` | `4115.00` | 1,190,000,000.00 USD | 2,290,000.00 USD | 0.00 USD | `+81.10%` | `557.02` |
| `Live` | `Short` | `4125.00` | 1,190,000,000.00 USD | 144,380.00 USD | 0.00 USD | `+81.54%` | `35.00` |
| `Live` | `Short` | `4135.00` | 1,190,000,000.00 USD | 228,400.00 USD | 0.00 USD | `+81.98%` | `55.23` |
| `Live` | `Short` | `4145.00` | 1,260,000,000.00 USD | 70,480,000.00 USD | 0.00 USD | `+82.42%` | `17,003.03` |
| `Live` | `Short` | `4155.00` | 1,260,000,000.00 USD | 1,910,000.00 USD | 0.00 USD | `+82.86%` | `459.37` |
| `Live` | `Short` | `4165.00` | 1,260,000,000.00 USD | 150,520.00 USD | 0.00 USD | `+83.30%` | `36.14` |
| `Live` | `Short` | `4175.00` | 1,260,000,000.00 USD | 835,000.00 USD | 0.00 USD | `+83.74%` | `200.00` |
| `Live` | `Short` | `4185.00` | 1,260,000,000.00 USD | 71,700.00 USD | 0.00 USD | `+84.18%` | `17.13` |
| `Live` | `Short` | `4195.00` | 1,270,000,000.00 USD | 4,180,000.00 USD | 0.00 USD | `+84.62%` | `996.43` |
| `Live` | `Short` | `4205.00` | 1,270,000,000.00 USD | 422,520.00 USD | 0.00 USD | `+85.06%` | `100.48` |
| `Live` | `Short` | `4215.00` | 1,270,000,000.00 USD | 42,960.00 USD | 0.00 USD | `+85.50%` | `10.19` |
| `Live` | `Short` | `4225.00` | 1,270,000,000.00 USD | 842.89 USD | 0.00 USD | `+85.94%` | `0.20` |
| `Live` | `Short` | `4235.00` | 1,270,000,000.00 USD | 1,420.00 USD | 0.00 USD | `+86.38%` | `0.33` |
| `Live` | `Short` | `4245.00` | 1,270,000,000.00 USD | 916.92 USD | 0.00 USD | `+86.82%` | `0.22` |
| `Live` | `Short` | `4255.00` | 1,360,000,000.00 USD | 89,150,000.00 USD | 0.00 USD | `+87.26%` | `20,951.14` |
| `Live` | `Short` | `4265.00` | 1,360,000,000.00 USD | 3,960,000.00 USD | 0.00 USD | `+87.70%` | `927.54` |
| `Live` | `Short` | `4275.00` | 1,360,000,000.00 USD | 8,160.00 USD | 0.00 USD | `+88.14%` | `1.91` |
| `Live` | `Short` | `4285.00` | 1,360,000,000.00 USD | 476,480.00 USD | 0.00 USD | `+88.58%` | `111.20` |
| `Live` | `Short` | `4295.00` | 1,360,000,000.00 USD | 68,850.00 USD | 0.00 USD | `+89.02%` | `16.03` |
| `Live` | `Short` | `4305.00` | 1,360,000,000.00 USD | 3,000.00 USD | 0.00 USD | `+89.46%` | `0.70` |
| `Live` | `Short` | `4315.00` | 1,360,000,000.00 USD | 18,810.00 USD | 0.00 USD | `+89.90%` | `4.36` |
| `Live` | `Short` | `4325.00` | 1,360,000,000.00 USD | 181,820.00 USD | 0.00 USD | `+90.34%` | `42.04` |
| `Live` | `Short` | `4335.00` | 1,360,000,000.00 USD | 109,320.00 USD | 0.00 USD | `+90.78%` | `25.22` |
| `Live` | `Short` | `4345.00` | 1,360,000,000.00 USD | 1,430,000.00 USD | 0.00 USD | `+91.22%` | `328.86` |
| `Live` | `Short` | `4355.00` | 1,370,000,000.00 USD | 2,870,000.00 USD | 0.00 USD | `+91.66%` | `659.61` |
| `Live` | `Short` | `4365.00` | 1,370,000,000.00 USD | 557,240.00 USD | 0.00 USD | `+92.10%` | `127.66` |
| `Live` | `Short` | `4375.00` | 1,370,000,000.00 USD | 36,440.00 USD | 0.00 USD | `+92.54%` | `8.33` |
| `Live` | `Short` | `4385.00` | 1,370,000,000.00 USD | 8,980.00 USD | 0.00 USD | `+92.98%` | `2.05` |
| `Live` | `Short` | `4395.00` | 1,370,000,000.00 USD | 759,410.00 USD | 0.00 USD | `+93.42%` | `172.79` |
| `Live` | `Short` | `4405.00` | 1,370,000,000.00 USD | 41,990.00 USD | 0.00 USD | `+93.86%` | `9.53` |
| `Live` | `Short` | `4415.00` | 1,370,000,000.00 USD | 45,850.00 USD | 0.00 USD | `+94.31%` | `10.38` |
| `Live` | `Short` | `4425.00` | 1,370,000,000.00 USD | 45,870.00 USD | 0.00 USD | `+94.75%` | `10.37` |
| `Live` | `Short` | `4435.00` | 1,370,000,000.00 USD | 20,090.00 USD | 0.00 USD | `+95.19%` | `4.53` |
| `Live` | `Short` | `4445.00` | 1,370,000,000.00 USD | 3,500,000.00 USD | 0.00 USD | `+95.63%` | `786.42` |
| `Live` | `Short` | `4455.00` | 1,370,000,000.00 USD | 124,740.00 USD | 0.00 USD | `+96.07%` | `28.00` |
| `Live` | `Short` | `4465.00` | 1,370,000,000.00 USD | 740,600.00 USD | 0.00 USD | `+96.51%` | `165.87` |
| `Live` | `Short` | `4475.00` | 1,370,000,000.00 USD | 145,300.00 USD | 0.00 USD | `+96.95%` | `32.47` |
| `Live` | `Short` | `4485.00` | 1,370,000,000.00 USD | 4,490.00 USD | 0.00 USD | `+97.39%` | `1.00` |
| `Live` | `Short` | `4495.00` | 1,370,000,000.00 USD | 7,610.00 USD | 0.00 USD | `+97.83%` | `1.69` |
| `Live` | `Short` | `4505.00` | 1,370,000,000.00 USD | 93,520.00 USD | 0.00 USD | `+98.27%` | `20.76` |
| `Live` | `Short` | `4515.00` | 1,370,000,000.00 USD | 10,080.00 USD | 0.00 USD | `+98.71%` | `2.23` |
| `Live` | `Short` | `4525.00` | 1,370,000,000.00 USD | 2,860.00 USD | 0.00 USD | `+99.15%` | `0.63` |
| `Live` | `Short` | `4535.00` | 1,370,000,000.00 USD | 467,610.00 USD | 0.00 USD | `+99.59%` | `103.11` |
| `Live` | `Short` | `4545.00` | 1,370,000,000.00 USD | 171,010.00 USD | 0.00 USD | `+100.03%` | `37.63` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `505.00` | 71,720,000.00 USD | 0.00 USD | 16,440.00 USD | `-77.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.00` | 71,700,000.00 USD | 0.00 USD | 563.16 USD | `-75.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.00` | 71,700,000.00 USD | 0.00 USD | 583.40 USD | `-71.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.00` | 71,700,000.00 USD | 0.00 USD | 885.90 USD | `-68.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `755.00` | 71,700,000.00 USD | 0.00 USD | 177.27 USD | `-66.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `795.00` | 71,700,000.00 USD | 0.00 USD | 104.22 USD | `-65.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `805.00` | 71,700,000.00 USD | 0.00 USD | 2,090.00 USD | `-64.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `835.00` | 71,700,000.00 USD | 0.00 USD | 1,670.00 USD | `-63.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `865.00` | 71,700,000.00 USD | 0.00 USD | 139,280.00 USD | `-61.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `885.00` | 71,560,000.00 USD | 0.00 USD | 3,130.00 USD | `-61.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `905.00` | 71,560,000.00 USD | 0.00 USD | 2,780.00 USD | `-60.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `985.00` | 71,550,000.00 USD | 0.00 USD | 516.34 USD | `-56.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `995.00` | 71,550,000.00 USD | 0.00 USD | 100.50 USD | `-56.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1005.00` | 71,550,000.00 USD | 0.00 USD | 223,740.00 USD | `-55.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1015.00` | 71,330,000.00 USD | 0.00 USD | 438.28 USD | `-55.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1025.00` | 71,330,000.00 USD | 0.00 USD | 112.03 USD | `-54.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1065.00` | 71,330,000.00 USD | 0.00 USD | 1,060.00 USD | `-53.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1075.00` | 71,330,000.00 USD | 0.00 USD | 995.34 USD | `-52.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1105.00` | 71,330,000.00 USD | 0.00 USD | 1,610.00 USD | `-51.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1115.00` | 71,320,000.00 USD | 0.00 USD | 11,050.00 USD | `-50.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1125.00` | 71,310,000.00 USD | 0.00 USD | 1,320.00 USD | `-50.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1155.00` | 71,310,000.00 USD | 0.00 USD | 1,000.00 USD | `-49.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1175.00` | 71,310,000.00 USD | 0.00 USD | 203.98 USD | `-48.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1185.00` | 71,310,000.00 USD | 0.00 USD | 228.47 USD | `-47.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1205.00` | 71,310,000.00 USD | 0.00 USD | 3,110.00 USD | `-46.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1225.00` | 71,310,000.00 USD | 0.00 USD | 995.93 USD | `-46.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1245.00` | 71,310,000.00 USD | 0.00 USD | 951.93 USD | `-45.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1255.00` | 71,310,000.00 USD | 0.00 USD | 6,810.00 USD | `-44.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1285.00` | 71,300,000.00 USD | 0.00 USD | 9,050.00 USD | `-43.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1295.00` | 71,290,000.00 USD | 0.00 USD | 7,030.00 USD | `-43.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1305.00` | 71,280,000.00 USD | 0.00 USD | 23,030.00 USD | `-42.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1315.00` | 71,260,000.00 USD | 0.00 USD | 1,440.00 USD | `-42.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1345.00` | 71,260,000.00 USD | 0.00 USD | 141,950.00 USD | `-40.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1355.00` | 71,120,000.00 USD | 0.00 USD | 128.86 USD | `-40.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1365.00` | 71,120,000.00 USD | 0.00 USD | 1,270.00 USD | `-39.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1375.00` | 71,110,000.00 USD | 0.00 USD | 4,160.00 USD | `-39.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1385.00` | 71,110,000.00 USD | 0.00 USD | 297.36 USD | `-39.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1395.00` | 71,110,000.00 USD | 0.00 USD | 535,600.00 USD | `-38.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1405.00` | 70,570,000.00 USD | 0.00 USD | 18,840.00 USD | `-38.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1425.00` | 70,560,000.00 USD | 0.00 USD | 6,450.00 USD | `-37.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1435.00` | 70,550,000.00 USD | 0.00 USD | 852.10 USD | `-36.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1445.00` | 70,550,000.00 USD | 0.00 USD | 1,490.00 USD | `-36.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1455.00` | 70,550,000.00 USD | 0.00 USD | 5,680.00 USD | `-35.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1465.00` | 70,540,000.00 USD | 0.00 USD | 19,460.00 USD | `-35.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1475.00` | 70,520,000.00 USD | 0.00 USD | 2,600.00 USD | `-35.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1485.00` | 70,520,000.00 USD | 0.00 USD | 18,710.00 USD | `-34.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1495.00` | 70,500,000.00 USD | 0.00 USD | 11,570.00 USD | `-34.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1505.00` | 70,490,000.00 USD | 0.00 USD | 89,400.00 USD | `-33.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1515.00` | 70,400,000.00 USD | 0.00 USD | 11,140.00 USD | `-33.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1525.00` | 70,390,000.00 USD | 0.00 USD | 31,900.00 USD | `-32.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1535.00` | 70,360,000.00 USD | 0.00 USD | 983.78 USD | `-32.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1545.00` | 70,360,000.00 USD | 0.00 USD | 960.99 USD | `-32.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1555.00` | 70,350,000.00 USD | 0.00 USD | 43,080.00 USD | `-31.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1565.00` | 70,310,000.00 USD | 0.00 USD | 6,260.00 USD | `-31.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1575.00` | 70,310,000.00 USD | 0.00 USD | 190,890.00 USD | `-30.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1585.00` | 70,110,000.00 USD | 0.00 USD | 3,390.00 USD | `-30.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1595.00` | 70,110,000.00 USD | 0.00 USD | 4,040.00 USD | `-29.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1605.00` | 70,110,000.00 USD | 0.00 USD | 435,540.00 USD | `-29.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1615.00` | 69,670,000.00 USD | 0.00 USD | 25,700.00 USD | `-28.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1625.00` | 69,650,000.00 USD | 0.00 USD | 13,590.00 USD | `-28.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1635.00` | 69,630,000.00 USD | 0.00 USD | 5,510.00 USD | `-28.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1645.00` | 69,630,000.00 USD | 0.00 USD | 330,340.00 USD | `-27.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1655.00` | 69,300,000.00 USD | 0.00 USD | 35,070.00 USD | `-27.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1665.00` | 69,260,000.00 USD | 0.00 USD | 3,110.00 USD | `-26.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1675.00` | 69,260,000.00 USD | 0.00 USD | 3,440.00 USD | `-26.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1685.00` | 69,250,000.00 USD | 0.00 USD | 35,300.00 USD | `-25.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1695.00` | 69,220,000.00 USD | 0.00 USD | 8,490.00 USD | `-25.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1705.00` | 69,210,000.00 USD | 0.00 USD | 83,330.00 USD | `-24.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1715.00` | 69,130,000.00 USD | 0.00 USD | 18,650.00 USD | `-24.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1725.00` | 69,110,000.00 USD | 0.00 USD | 47,500.00 USD | `-24.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1735.00` | 69,060,000.00 USD | 0.00 USD | 28,150.00 USD | `-23.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1745.00` | 69,030,000.00 USD | 0.00 USD | 3,180.00 USD | `-23.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1755.00` | 69,030,000.00 USD | 0.00 USD | 504,110.00 USD | `-22.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1765.00` | 68,530,000.00 USD | 0.00 USD | 76,460.00 USD | `-22.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1775.00` | 68,450,000.00 USD | 0.00 USD | 3,090.00 USD | `-21.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1785.00` | 68,450,000.00 USD | 0.00 USD | 8,500.00 USD | `-21.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1795.00` | 68,440,000.00 USD | 0.00 USD | 184,330.00 USD | `-21.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1805.00` | 68,250,000.00 USD | 0.00 USD | 636,880.00 USD | `-20.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1815.00` | 67,620,000.00 USD | 0.00 USD | 135,310.00 USD | `-20.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1825.00` | 67,480,000.00 USD | 0.00 USD | 33,370.00 USD | `-19.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1835.00` | 67,450,000.00 USD | 0.00 USD | 5,770.00 USD | `-19.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1845.00` | 67,440,000.00 USD | 0.00 USD | 14,290.00 USD | `-18.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1855.00` | 67,430,000.00 USD | 0.00 USD | 469,140.00 USD | `-18.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1865.00` | 66,960,000.00 USD | 0.00 USD | 33,750.00 USD | `-17.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1875.00` | 66,920,000.00 USD | 0.00 USD | 18,210,000.00 USD | `-17.48%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1885.00` | 48,720,000.00 USD | 0.00 USD | 4,390.00 USD | `-17.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1895.00` | 48,710,000.00 USD | 0.00 USD | 64,540.00 USD | `-16.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1905.00` | 48,650,000.00 USD | 0.00 USD | 145,330.00 USD | `-16.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1915.00` | 48,500,000.00 USD | 0.00 USD | 8,120,000.00 USD | `-15.72%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1925.00` | 40,380,000.00 USD | 0.00 USD | 16,420,000.00 USD | `-15.28%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1935.00` | 23,960,000.00 USD | 0.00 USD | 79,950.00 USD | `-14.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1945.00` | 23,880,000.00 USD | 0.00 USD | 47,270.00 USD | `-14.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1955.00` | 23,840,000.00 USD | 0.00 USD | 54,590.00 USD | `-13.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1965.00` | 23,780,000.00 USD | 0.00 USD | 19,290.00 USD | `-13.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1975.00` | 23,760,000.00 USD | 0.00 USD | 90,560.00 USD | `-13.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1985.00` | 23,670,000.00 USD | 0.00 USD | 96,120.00 USD | `-12.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1995.00` | 23,580,000.00 USD | 0.00 USD | 235,720.00 USD | `-12.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2005.00` | 23,340,000.00 USD | 0.00 USD | 1,030,000.00 USD | `-11.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2015.00` | 22,310,000.00 USD | 0.00 USD | 67,250.00 USD | `-11.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2025.00` | 22,240,000.00 USD | 0.00 USD | 536,580.00 USD | `-10.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2035.00` | 21,710,000.00 USD | 0.00 USD | 99,030.00 USD | `-10.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2045.00` | 21,610,000.00 USD | 0.00 USD | 12,590.00 USD | `-10.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2055.00` | 21,590,000.00 USD | 0.00 USD | 205,250.00 USD | `-9.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2065.00` | 21,390,000.00 USD | 0.00 USD | 43,800.00 USD | `-9.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2075.00` | 21,340,000.00 USD | 0.00 USD | 30,880.00 USD | `-8.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2085.00` | 21,310,000.00 USD | 0.00 USD | 52,260.00 USD | `-8.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2095.00` | 21,260,000.00 USD | 0.00 USD | 58,840.00 USD | `-7.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2105.00` | 21,200,000.00 USD | 0.00 USD | 309,270.00 USD | `-7.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2115.00` | 20,890,000.00 USD | 0.00 USD | 129,450.00 USD | `-6.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2125.00` | 20,760,000.00 USD | 0.00 USD | 214,920.00 USD | `-6.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2135.00` | 20,550,000.00 USD | 0.00 USD | 37,870.00 USD | `-6.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2145.00` | 20,510,000.00 USD | 0.00 USD | 70,710.00 USD | `-5.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2155.00` | 20,440,000.00 USD | 0.00 USD | 1,510,000.00 USD | `-5.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2165.00` | 18,930,000.00 USD | 0.00 USD | 1,080,000.00 USD | `-4.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2175.00` | 17,860,000.00 USD | 0.00 USD | 605,500.00 USD | `-4.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2185.00` | 17,250,000.00 USD | 0.00 USD | 319,250.00 USD | `-3.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2195.00` | 16,930,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-3.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2205.00` | 15,800,000.00 USD | 0.00 USD | 3,890,000.00 USD | `-2.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2215.00` | 11,910,000.00 USD | 0.00 USD | 1,040,000.00 USD | `-2.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2225.00` | 10,870,000.00 USD | 0.00 USD | 2,560,000.00 USD | `-2.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2235.00` | 8,320,000.00 USD | 0.00 USD | 1,930,000.00 USD | `-1.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2245.00` | 6,390,000.00 USD | 0.00 USD | 4,350,000.00 USD | `-1.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2255.00` | 2,040,000.00 USD | 0.00 USD | 371,710.00 USD | `-0.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2265.00` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | `-0.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2275.00` | 46,620.00 USD | 46,620.00 USD | 0.00 USD | `+0.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2285.00` | 126,170.00 USD | 79,550.00 USD | 0.00 USD | `+0.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2295.00` | 1,090,000.00 USD | 961,540.00 USD | 0.00 USD | `+1.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2305.00` | 4,410,000.00 USD | 3,320,000.00 USD | 0.00 USD | `+1.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2315.00` | 7,530,000.00 USD | 3,120,000.00 USD | 0.00 USD | `+1.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2325.00` | 8,700,000.00 USD | 1,170,000.00 USD | 0.00 USD | `+2.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2335.00` | 8,850,000.00 USD | 145,090.00 USD | 0.00 USD | `+2.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2345.00` | 10,130,000.00 USD | 1,280,000.00 USD | 0.00 USD | `+3.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2355.00` | 13,170,000.00 USD | 3,040,000.00 USD | 0.00 USD | `+3.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2365.00` | 13,600,000.00 USD | 425,610.00 USD | 0.00 USD | `+4.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2375.00` | 13,720,000.00 USD | 120,260.00 USD | 0.00 USD | `+4.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2385.00` | 13,840,000.00 USD | 120,230.00 USD | 0.00 USD | `+4.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2395.00` | 14,450,000.00 USD | 617,000.00 USD | 0.00 USD | `+5.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2405.00` | 16,390,000.00 USD | 1,940,000.00 USD | 0.00 USD | `+5.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2415.00` | 16,710,000.00 USD | 321,510.00 USD | 0.00 USD | `+6.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2425.00` | 19,700,000.00 USD | 2,990,000.00 USD | 0.00 USD | `+6.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2435.00` | 19,870,000.00 USD | 173,490.00 USD | 0.00 USD | `+7.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2445.00` | 20,440,000.00 USD | 571,480.00 USD | 0.00 USD | `+7.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2455.00` | 20,960,000.00 USD | 519,390.00 USD | 0.00 USD | `+8.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2465.00` | 23,110,000.00 USD | 2,140,000.00 USD | 0.00 USD | `+8.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2475.00` | 23,310,000.00 USD | 204,420.00 USD | 0.00 USD | `+8.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2485.00` | 25,450,000.00 USD | 2,140,000.00 USD | 0.00 USD | `+9.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2495.00` | 25,880,000.00 USD | 439,220.00 USD | 0.00 USD | `+9.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2505.00` | 31,040,000.00 USD | 5,150,000.00 USD | 0.00 USD | `+10.25%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2515.00` | 38,770,000.00 USD | 7,740,000.00 USD | 0.00 USD | `+10.69%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2525.00` | 42,000,000.00 USD | 3,220,000.00 USD | 0.00 USD | `+11.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2535.00` | 42,060,000.00 USD | 62,050.00 USD | 0.00 USD | `+11.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2545.00` | 44,240,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+12.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2555.00` | 44,520,000.00 USD | 282,650.00 USD | 0.00 USD | `+12.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2565.00` | 46,910,000.00 USD | 2,390,000.00 USD | 0.00 USD | `+12.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2575.00` | 47,040,000.00 USD | 128,450.00 USD | 0.00 USD | `+13.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2585.00` | 49,730,000.00 USD | 2,690,000.00 USD | 0.00 USD | `+13.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2595.00` | 49,740,000.00 USD | 13,760.00 USD | 0.00 USD | `+14.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2605.00` | 52,720,000.00 USD | 2,980,000.00 USD | 0.00 USD | `+14.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2615.00` | 52,870,000.00 USD | 147,350.00 USD | 0.00 USD | `+15.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2625.00` | 55,070,000.00 USD | 2,210,000.00 USD | 0.00 USD | `+15.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2635.00` | 55,230,000.00 USD | 155,950.00 USD | 0.00 USD | `+15.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2645.00` | 57,350,000.00 USD | 2,130,000.00 USD | 0.00 USD | `+16.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2655.00` | 57,610,000.00 USD | 251,180.00 USD | 0.00 USD | `+16.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2665.00` | 59,750,000.00 USD | 2,150,000.00 USD | 0.00 USD | `+17.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2675.00` | 60,100,000.00 USD | 351,060.00 USD | 0.00 USD | `+17.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2685.00` | 62,280,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+18.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2695.00` | 62,380,000.00 USD | 95,970.00 USD | 0.00 USD | `+18.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2705.00` | 66,840,000.00 USD | 4,470,000.00 USD | 0.00 USD | `+19.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2715.00` | 66,920,000.00 USD | 76,590.00 USD | 0.00 USD | `+19.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2725.00` | 69,390,000.00 USD | 2,470,000.00 USD | 0.00 USD | `+19.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2735.00` | 69,440,000.00 USD | 55,230.00 USD | 0.00 USD | `+20.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2745.00` | 71,700,000.00 USD | 2,260,000.00 USD | 0.00 USD | `+20.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2755.00` | 72,460,000.00 USD | 758,560.00 USD | 0.00 USD | `+21.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2765.00` | 74,840,000.00 USD | 2,380,000.00 USD | 0.00 USD | `+21.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2775.00` | 75,420,000.00 USD | 577,690.00 USD | 0.00 USD | `+22.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2785.00` | 77,690,000.00 USD | 2,270,000.00 USD | 0.00 USD | `+22.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2795.00` | 77,710,000.00 USD | 17,550.00 USD | 0.00 USD | `+23.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2805.00` | 81,950,000.00 USD | 4,240,000.00 USD | 0.00 USD | `+23.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2815.00` | 82,010,000.00 USD | 52,670.00 USD | 0.00 USD | `+23.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2825.00` | 82,070,000.00 USD | 63,490.00 USD | 0.00 USD | `+24.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2835.00` | 82,360,000.00 USD | 289,000.00 USD | 0.00 USD | `+24.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2845.00` | 83,370,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+25.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2855.00` | 84,780,000.00 USD | 1,410,000.00 USD | 0.00 USD | `+25.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2865.00` | 84,790,000.00 USD | 10,290.00 USD | 0.00 USD | `+26.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2875.00` | 84,790,000.00 USD | 2,460.00 USD | 0.00 USD | `+26.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2885.00` | 85,090,000.00 USD | 303,660.00 USD | 0.00 USD | `+26.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2895.00` | 85,110,000.00 USD | 21,290.00 USD | 0.00 USD | `+27.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2905.00` | 86,590,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+27.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2915.00` | 86,600,000.00 USD | 10,340.00 USD | 0.00 USD | `+28.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2925.00` | 86,600,000.00 USD | 3,050.00 USD | 0.00 USD | `+28.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2935.00` | 86,660,000.00 USD | 52,910.00 USD | 0.00 USD | `+29.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2945.00` | 86,690,000.00 USD | 34,650.00 USD | 0.00 USD | `+29.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2955.00` | 86,770,000.00 USD | 81,760.00 USD | 0.00 USD | `+30.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2965.00` | 86,890,000.00 USD | 113,340.00 USD | 0.00 USD | `+30.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2975.00` | 87,030,000.00 USD | 147,920.00 USD | 0.00 USD | `+30.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2985.00` | 87,210,000.00 USD | 177,120.00 USD | 0.00 USD | `+31.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2995.00` | 89,150,000.00 USD | 1,940,000.00 USD | 0.00 USD | `+31.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3005.00` | 96,330,000.00 USD | 7,170,000.00 USD | 0.00 USD | `+32.25%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `3015.00` | 96,330,000.00 USD | 6,950.00 USD | 0.00 USD | `+32.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3025.00` | 96,370,000.00 USD | 37,610.00 USD | 0.00 USD | `+33.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3035.00` | 96,440,000.00 USD | 73,700.00 USD | 0.00 USD | `+33.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3045.00` | 96,470,000.00 USD | 22,460.00 USD | 0.00 USD | `+34.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3055.00` | 97,250,000.00 USD | 783,940.00 USD | 0.00 USD | `+34.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3065.00` | 97,250,000.00 USD | 3,080.00 USD | 0.00 USD | `+34.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3075.00` | 97,300,000.00 USD | 49,330.00 USD | 0.00 USD | `+35.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3085.00` | 97,320,000.00 USD | 19,570.00 USD | 0.00 USD | `+35.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3095.00` | 97,320,000.00 USD | 928.50 USD | 0.00 USD | `+36.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3105.00` | 112,070,000.00 USD | 14,750,000.00 USD | 0.00 USD | `+36.65%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `3115.00` | 112,230,000.00 USD | 154,140.00 USD | 0.00 USD | `+37.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3125.00` | 112,640,000.00 USD | 414,660.00 USD | 0.00 USD | `+37.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3145.00` | 112,640,000.00 USD | 2,530.00 USD | 0.00 USD | `+38.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3155.00` | 112,710,000.00 USD | 68,940.00 USD | 0.00 USD | `+38.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3165.00` | 112,740,000.00 USD | 21,490.00 USD | 0.00 USD | `+39.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3175.00` | 112,750,000.00 USD | 17,040.00 USD | 0.00 USD | `+39.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3185.00` | 112,750,000.00 USD | 1,330.00 USD | 0.00 USD | `+40.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3195.00` | 112,780,000.00 USD | 29,450.00 USD | 0.00 USD | `+40.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3205.00` | 113,860,000.00 USD | 1,080,000.00 USD | 0.00 USD | `+41.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3215.00` | 113,860,000.00 USD | 1,290.00 USD | 0.00 USD | `+41.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3225.00` | 113,860,000.00 USD | 3,740.00 USD | 0.00 USD | `+41.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3235.00` | 113,890,000.00 USD | 30,790.00 USD | 0.00 USD | `+42.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3245.00` | 113,950,000.00 USD | 56,110.00 USD | 0.00 USD | `+42.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3255.00` | 114,190,000.00 USD | 236,580.00 USD | 0.00 USD | `+43.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3265.00` | 114,200,000.00 USD | 15,710.00 USD | 0.00 USD | `+43.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3275.00` | 114,200,000.00 USD | 1,630.00 USD | 0.00 USD | `+44.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3285.00` | 114,350,000.00 USD | 141,980.00 USD | 0.00 USD | `+44.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3295.00` | 114,360,000.00 USD | 15,350.00 USD | 0.00 USD | `+45.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3305.00` | 115,760,000.00 USD | 1,400,000.00 USD | 0.00 USD | `+45.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3315.00` | 116,140,000.00 USD | 385,510.00 USD | 0.00 USD | `+45.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3325.00` | 116,160,000.00 USD | 18,270.00 USD | 0.00 USD | `+46.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3335.00` | 116,180,000.00 USD | 18,080.00 USD | 0.00 USD | `+46.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3345.00` | 116,180,000.00 USD | 617.15 USD | 0.00 USD | `+47.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3355.00` | 116,180,000.00 USD | 837.74 USD | 0.00 USD | `+47.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3365.00` | 116,180,000.00 USD | 2,780.00 USD | 0.00 USD | `+48.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3375.00` | 116,200,000.00 USD | 21,260.00 USD | 0.00 USD | `+48.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3385.00` | 116,260,000.00 USD | 58,010.00 USD | 0.00 USD | `+48.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3395.00` | 116,620,000.00 USD | 355,050.00 USD | 0.00 USD | `+49.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3405.00` | 117,960,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+49.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3415.00` | 117,960,000.00 USD | 3,510.00 USD | 0.00 USD | `+50.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3425.00` | 117,980,000.00 USD | 16,310.00 USD | 0.00 USD | `+50.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3445.00` | 118,000,000.00 USD | 15,030.00 USD | 0.00 USD | `+51.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3455.00` | 118,010,000.00 USD | 18,600.00 USD | 0.00 USD | `+52.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3465.00` | 118,010,000.00 USD | 495.50 USD | 0.00 USD | `+52.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3475.00` | 118,020,000.00 USD | 2,980.00 USD | 0.00 USD | `+52.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3485.00` | 118,060,000.00 USD | 43,610.00 USD | 0.00 USD | `+53.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3495.00` | 118,060,000.00 USD | 158.32 USD | 0.00 USD | `+53.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3505.00` | 118,510,000.00 USD | 444,410.00 USD | 0.00 USD | `+54.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3515.00` | 118,550,000.00 USD | 43,410.00 USD | 0.00 USD | `+54.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3525.00` | 118,550,000.00 USD | 3,690.00 USD | 0.00 USD | `+55.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3535.00` | 118,560,000.00 USD | 9,810.00 USD | 0.00 USD | `+55.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3545.00` | 118,560,000.00 USD | 179.38 USD | 0.00 USD | `+56.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3555.00` | 118,650,000.00 USD | 90,810.00 USD | 0.00 USD | `+56.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3565.00` | 118,660,000.00 USD | 2,300.00 USD | 0.00 USD | `+56.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3585.00` | 118,660,000.00 USD | 354.92 USD | 0.00 USD | `+57.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3595.00` | 118,670,000.00 USD | 13,160.00 USD | 0.00 USD | `+58.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3605.00` | 118,780,000.00 USD | 105,860.00 USD | 0.00 USD | `+58.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3625.00` | 118,790,000.00 USD | 10,210.00 USD | 0.00 USD | `+59.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3635.00` | 118,790,000.00 USD | 7,790.00 USD | 0.00 USD | `+59.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3645.00` | 118,800,000.00 USD | 3,860.00 USD | 0.00 USD | `+60.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3655.00` | 118,810,000.00 USD | 7,740.00 USD | 0.00 USD | `+60.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3665.00` | 118,810,000.00 USD | 8,130.00 USD | 0.00 USD | `+61.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3675.00` | 118,870,000.00 USD | 55,120.00 USD | 0.00 USD | `+61.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3685.00` | 118,870,000.00 USD | 3,550.00 USD | 0.00 USD | `+62.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3705.00` | 118,870,000.00 USD | 819.92 USD | 0.00 USD | `+63.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3715.00` | 118,870,000.00 USD | 323.58 USD | 0.00 USD | `+63.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3725.00` | 118,870,000.00 USD | 1,400.00 USD | 0.00 USD | `+63.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3735.00` | 118,880,000.00 USD | 6,490.00 USD | 0.00 USD | `+64.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3755.00` | 118,880,000.00 USD | 751.00 USD | 0.00 USD | `+65.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3785.00` | 118,880,000.00 USD | 286.90 USD | 0.00 USD | `+66.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3795.00` | 118,880,000.00 USD | 1,560.00 USD | 0.00 USD | `+67.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3805.00` | 119,620,000.00 USD | 734,090.00 USD | 0.00 USD | `+67.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3815.00` | 119,640,000.00 USD | 20,930.00 USD | 0.00 USD | `+67.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3825.00` | 119,650,000.00 USD | 8,380.00 USD | 0.00 USD | `+68.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3835.00` | 119,650,000.00 USD | 711.78 USD | 0.00 USD | `+68.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3845.00` | 119,650,000.00 USD | 355.28 USD | 0.00 USD | `+69.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3855.00` | 119,650,000.00 USD | 5,170.00 USD | 0.00 USD | `+69.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3885.00` | 119,670,000.00 USD | 19,430.00 USD | 0.00 USD | `+70.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3905.00` | 119,680,000.00 USD | 12,120.00 USD | 0.00 USD | `+71.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3915.00` | 120,330,000.00 USD | 646,840.00 USD | 0.00 USD | `+72.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3925.00` | 120,330,000.00 USD | 3,260.00 USD | 0.00 USD | `+72.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3935.00` | 120,380,000.00 USD | 42,570.00 USD | 0.00 USD | `+73.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3945.00` | 120,440,000.00 USD | 59,170.00 USD | 0.00 USD | `+73.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3955.00` | 120,440,000.00 USD | 1,380.00 USD | 0.00 USD | `+74.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3965.00` | 120,440,000.00 USD | 323.54 USD | 0.00 USD | `+74.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3975.00` | 120,450,000.00 USD | 6,960.00 USD | 0.00 USD | `+74.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3985.00` | 120,460,000.00 USD | 14,610.00 USD | 0.00 USD | `+75.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3995.00` | 120,460,000.00 USD | 4,280.00 USD | 0.00 USD | `+75.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4005.00` | 123,100,000.00 USD | 2,640,000.00 USD | 0.00 USD | `+76.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4035.00` | 123,100,000.00 USD | 898.59 USD | 0.00 USD | `+77.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4055.00` | 123,100,000.00 USD | 811.00 USD | 0.00 USD | `+78.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4075.00` | 123,110,000.00 USD | 4,310.00 USD | 0.00 USD | `+79.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4085.00` | 123,110,000.00 USD | 2,800.00 USD | 0.00 USD | `+79.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4105.00` | 123,150,000.00 USD | 39,390.00 USD | 0.00 USD | `+80.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4115.00` | 123,150,000.00 USD | 5,990.00 USD | 0.00 USD | `+81.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4125.00` | 123,150,000.00 USD | 372.90 USD | 0.00 USD | `+81.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4145.00` | 123,150,000.00 USD | 395.43 USD | 0.00 USD | `+82.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4185.00` | 123,150,000.00 USD | 376.65 USD | 0.00 USD | `+84.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4205.00` | 123,200,000.00 USD | 41,200.00 USD | 0.00 USD | `+85.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4215.00` | 123,200,000.00 USD | 460.70 USD | 0.00 USD | `+85.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4225.00` | 123,200,000.00 USD | 1,270.00 USD | 0.00 USD | `+85.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4255.00` | 123,200,000.00 USD | 4,300.00 USD | 0.00 USD | `+87.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4265.00` | 123,200,000.00 USD | 437.16 USD | 0.00 USD | `+87.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4275.00` | 123,270,000.00 USD | 64,550.00 USD | 0.00 USD | `+88.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4285.00` | 123,270,000.00 USD | 1,610.00 USD | 0.00 USD | `+88.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4305.00` | 123,370,000.00 USD | 97,670.00 USD | 0.00 USD | `+89.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4315.00` | 123,370,000.00 USD | 1,070.00 USD | 0.00 USD | `+89.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4345.00` | 123,380,000.00 USD | 11,270.00 USD | 0.00 USD | `+91.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4355.00` | 123,380,000.00 USD | 3,250.00 USD | 0.00 USD | `+91.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4375.00` | 123,430,000.00 USD | 43,750.00 USD | 0.00 USD | `+92.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4385.00` | 123,490,000.00 USD | 64,570.00 USD | 0.00 USD | `+92.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4395.00` | 123,490,000.00 USD | 1,050.00 USD | 0.00 USD | `+93.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4405.00` | 123,540,000.00 USD | 44,050.00 USD | 0.00 USD | `+93.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4415.00` | 123,550,000.00 USD | 11,480.00 USD | 0.00 USD | `+94.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4425.00` | 123,550,000.00 USD | 2,510.00 USD | 0.00 USD | `+94.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4435.00` | 123,730,000.00 USD | 177,400.00 USD | 0.00 USD | `+95.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4455.00` | 123,730,000.00 USD | 641.97 USD | 0.00 USD | `+96.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4465.00` | 123,730,000.00 USD | 1,030.00 USD | 0.00 USD | `+96.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4505.00` | 124,110,000.00 USD | 376,800.00 USD | 0.00 USD | `+98.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4515.00` | 124,110,000.00 USD | 2,280.00 USD | 0.00 USD | `+98.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4525.00` | 124,110,000.00 USD | 6,560.00 USD | 0.00 USD | `+99.15%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `2016.30` | 487,320,000.00 USD | 0.00 USD | 487,320,000.00 USD | 0.00 USD | 176,210.00 USD | 0.00 USD |
| `1D` | `2019.00` | 487,140,000.00 USD | 0.00 USD | 487,140,000.00 USD | 83,300.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2021.70` | 487,060,000.00 USD | 0.00 USD | 487,060,000.00 USD | 0.00 USD | 558,730.00 USD | 0.00 USD |
| `7D` | `2025.30` | 910,320,000.00 USD | 0.00 USD | 910,320,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD |
| `1D` | `2027.10` | 486,500,000.00 USD | 0.00 USD | 486,500,000.00 USD | 0.00 USD | 943,590.00 USD | 40,210.00 USD |
| `7D` | `2028.60` | 910,140,000.00 USD | 0.00 USD | 910,140,000.00 USD | 0.00 USD | 1,180,000.00 USD | 35,180.00 USD |
| `1D` | `2029.80` | 485,520,000.00 USD | 0.00 USD | 485,520,000.00 USD | 87,180.00 USD | 163,200.00 USD | 43,160.00 USD |
| `7D` | `2031.90` | 908,930,000.00 USD | 0.00 USD | 908,930,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD |
| `1D` | `2032.50` | 485,220,000.00 USD | 0.00 USD | 485,220,000.00 USD | 1,360,000.00 USD | 1,330,000.00 USD | 408,620.00 USD |
| `1D` | `2035.20` | 482,120,000.00 USD | 0.00 USD | 482,120,000.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2035.20` | 907,480,000.00 USD | 0.00 USD | 907,480,000.00 USD | 146,420.00 USD | 186,130.00 USD | 1,350,000.00 USD |
| `1D` | `2037.90` | 481,090,000.00 USD | 0.00 USD | 481,090,000.00 USD | 0.00 USD | 0.00 USD | 13,360.00 USD |
| `7D` | `2038.50` | 905,790,000.00 USD | 0.00 USD | 905,790,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2040.60` | 481,070,000.00 USD | 0.00 USD | 481,070,000.00 USD | 138,370.00 USD | 178,560.00 USD | 21,940.00 USD |
| `1D` | `2043.30` | 480,740,000.00 USD | 0.00 USD | 480,740,000.00 USD | 0.00 USD | 0.00 USD | 8,270.00 USD |
| `7D` | `2045.10` | 904,330,000.00 USD | 0.00 USD | 904,330,000.00 USD | 0.00 USD | 149,500.00 USD | 108,710.00 USD |
| `1D` | `2046.00` | 480,730,000.00 USD | 0.00 USD | 480,730,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD |
| `1D` | `2048.70` | 480,700,000.00 USD | 0.00 USD | 480,700,000.00 USD | 467,370.00 USD | 0.00 USD | 717,780.00 USD |
| `1D` | `2051.40` | 479,510,000.00 USD | 0.00 USD | 479,510,000.00 USD | 0.00 USD | 338,980.00 USD | 0.00 USD |
| `7D` | `2051.70` | 904,080,000.00 USD | 0.00 USD | 904,080,000.00 USD | 1,320,000.00 USD | 0.00 USD | 1,190,000.00 USD |
| `1D` | `2054.10` | 479,180,000.00 USD | 0.00 USD | 479,180,000.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD |
| `1D` | `2056.80` | 479,060,000.00 USD | 0.00 USD | 479,060,000.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2058.30` | 901,570,000.00 USD | 0.00 USD | 901,570,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD |
| `1D` | `2059.50` | 478,820,000.00 USD | 0.00 USD | 478,820,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `7D` | `2061.60` | 901,230,000.00 USD | 0.00 USD | 901,230,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD |
| `1D` | `2062.20` | 478,060,000.00 USD | 0.00 USD | 478,060,000.00 USD | 80,610.00 USD | 121,470.00 USD | 52,590.00 USD |
| `1D` | `2064.90` | 477,810,000.00 USD | 0.00 USD | 477,810,000.00 USD | 563,140.00 USD | 537,030.00 USD | 598,250.00 USD |
| `7D` | `2064.90` | 895,970,000.00 USD | 0.00 USD | 895,970,000.00 USD | 1,230,000.00 USD | 313,000.00 USD | 979,910.00 USD |
| `1D` | `2067.60` | 476,110,000.00 USD | 0.00 USD | 476,110,000.00 USD | 808,950.00 USD | 362,000.00 USD | 23,500.00 USD |
| `7D` | `2068.20` | 893,440,000.00 USD | 0.00 USD | 893,440,000.00 USD | 1,740,000.00 USD | 1,860,000.00 USD | 893,570.00 USD |
| `1D` | `2070.30` | 474,910,000.00 USD | 0.00 USD | 474,910,000.00 USD | 1,050,000.00 USD | 965,400.00 USD | 464,460.00 USD |
| `7D` | `2071.50` | 888,950,000.00 USD | 0.00 USD | 888,950,000.00 USD | 2,820,000.00 USD | 2,410,000.00 USD | 1,230,000.00 USD |
| `1D` | `2073.00` | 472,430,000.00 USD | 0.00 USD | 472,430,000.00 USD | 442,230.00 USD | 597,240.00 USD | 436,900.00 USD |
| `7D` | `2074.80` | 882,480,000.00 USD | 0.00 USD | 882,480,000.00 USD | 4,370,000.00 USD | 3,270,000.00 USD | 4,050,000.00 USD |
| `1D` | `2075.70` | 470,950,000.00 USD | 0.00 USD | 470,950,000.00 USD | 2,040,000.00 USD | 901,140.00 USD | 2,100,000.00 USD |
| `7D` | `2078.10` | 870,790,000.00 USD | 0.00 USD | 870,790,000.00 USD | 5,560,000.00 USD | 4,320,000.00 USD | 2,410,000.00 USD |
| `1D` | `2078.40` | 465,920,000.00 USD | 0.00 USD | 465,920,000.00 USD | 1,700,000.00 USD | 1,130,000.00 USD | 632,440.00 USD |
| `1D` | `2081.10` | 462,450,000.00 USD | 0.00 USD | 462,450,000.00 USD | 1,560,000.00 USD | 1,100,000.00 USD | 424,820.00 USD |
| `7D` | `2081.40` | 858,500,000.00 USD | 0.00 USD | 858,500,000.00 USD | 4,720,000.00 USD | 3,420,000.00 USD | 2,500,000.00 USD |
| `1D` | `2083.80` | 459,380,000.00 USD | 0.00 USD | 459,380,000.00 USD | 2,130,000.00 USD | 1,420,000.00 USD | 755,170.00 USD |
| `7D` | `2084.70` | 847,860,000.00 USD | 0.00 USD | 847,860,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 4,900,000.00 USD |
| `1D` | `2086.50` | 455,070,000.00 USD | 0.00 USD | 455,070,000.00 USD | 1,230,000.00 USD | 1,630,000.00 USD | 1,460,000.00 USD |
| `7D` | `2088.00` | 839,070,000.00 USD | 0.00 USD | 839,070,000.00 USD | 3,990,000.00 USD | 2,780,000.00 USD | 1,650,000.00 USD |
| `1D` | `2089.20` | 450,750,000.00 USD | 0.00 USD | 450,750,000.00 USD | 1,200,000.00 USD | 274,650.00 USD | 228,450.00 USD |
| `7D` | `2091.30` | 830,640,000.00 USD | 0.00 USD | 830,640,000.00 USD | 4,410,000.00 USD | 952,210.00 USD | 7,590,000.00 USD |
| `1D` | `2091.90` | 449,050,000.00 USD | 0.00 USD | 449,050,000.00 USD | 1,400,000.00 USD | 514,440.00 USD | 957,110.00 USD |
| `1D` | `2094.60` | 446,170,000.00 USD | 0.00 USD | 446,170,000.00 USD | 2,040,000.00 USD | 1,120,000.00 USD | 1,430,000.00 USD |
| `7D` | `2094.60` | 817,690,000.00 USD | 0.00 USD | 817,690,000.00 USD | 5,720,000.00 USD | 2,160,000.00 USD | 2,340,000.00 USD |
| `1D` | `2097.30` | 441,580,000.00 USD | 0.00 USD | 441,580,000.00 USD | 617,040.00 USD | 1,010,000.00 USD | 984,190.00 USD |
| `7D` | `2097.90` | 807,460,000.00 USD | 0.00 USD | 807,460,000.00 USD | 2,340,000.00 USD | 3,210,000.00 USD | 1,290,000.00 USD |
| `1D` | `2100.00` | 438,970,000.00 USD | 0.00 USD | 438,970,000.00 USD | 172,210.00 USD | 403,100.00 USD | 15,650.00 USD |
| `7D` | `2101.20` | 800,630,000.00 USD | 0.00 USD | 800,630,000.00 USD | 999,530.00 USD | 1,580,000.00 USD | 4,020,000.00 USD |
| `1D` | `2102.70` | 438,380,000.00 USD | 0.00 USD | 438,380,000.00 USD | 530,980.00 USD | 289,160.00 USD | 462,940.00 USD |
| `7D` | `2104.50` | 794,030,000.00 USD | 0.00 USD | 794,030,000.00 USD | 2,010,000.00 USD | 1,180,000.00 USD | 2,250,000.00 USD |
| `1D` | `2105.40` | 437,090,000.00 USD | 0.00 USD | 437,090,000.00 USD | 588,810.00 USD | 671,930.00 USD | 172,100.00 USD |
| `7D` | `2107.80` | 788,590,000.00 USD | 0.00 USD | 788,590,000.00 USD | 2,380,000.00 USD | 452,470.00 USD | 1,650,000.00 USD |
| `1D` | `2108.10` | 435,660,000.00 USD | 0.00 USD | 435,660,000.00 USD | 664,310.00 USD | 9,120.00 USD | 347,020.00 USD |
| `1D` | `2110.80` | 434,640,000.00 USD | 0.00 USD | 434,640,000.00 USD | 36,110.00 USD | 22,440.00 USD | 200,160.00 USD |
| `7D` | `2111.10` | 784,100,000.00 USD | 0.00 USD | 784,100,000.00 USD | 3,530,000.00 USD | 2,350,000.00 USD | 2,170,000.00 USD |
| `1D` | `2113.50` | 434,380,000.00 USD | 0.00 USD | 434,380,000.00 USD | 875,700.00 USD | 643,210.00 USD | 226,360.00 USD |
| `7D` | `2114.40` | 776,060,000.00 USD | 0.00 USD | 776,060,000.00 USD | 1,080,000.00 USD | 1,850,000.00 USD | 3,800,000.00 USD |
| `1D` | `2116.20` | 432,640,000.00 USD | 0.00 USD | 432,640,000.00 USD | 0.00 USD | 13,230.00 USD | 421,530.00 USD |
| `7D` | `2117.70` | 769,330,000.00 USD | 0.00 USD | 769,330,000.00 USD | 3,430,000.00 USD | 2,020,000.00 USD | 3,380,000.00 USD |
| `1D` | `2118.90` | 432,200,000.00 USD | 0.00 USD | 432,200,000.00 USD | 218,200.00 USD | 99,440.00 USD | 856,150.00 USD |
| `7D` | `2121.00` | 760,490,000.00 USD | 0.00 USD | 760,490,000.00 USD | 3,650,000.00 USD | 1,340,000.00 USD | 1,820,000.00 USD |
| `1D` | `2121.60` | 431,030,000.00 USD | 0.00 USD | 431,030,000.00 USD | 926,060.00 USD | 647,730.00 USD | 672,270.00 USD |
| `1D` | `2124.30` | 428,780,000.00 USD | 0.00 USD | 428,780,000.00 USD | 702,090.00 USD | 844,410.00 USD | 919,980.00 USD |
| `7D` | `2124.30` | 753,680,000.00 USD | 0.00 USD | 753,680,000.00 USD | 832,850.00 USD | 972,650.00 USD | 1,510,000.00 USD |
| `1D` | `2127.00` | 426,310,000.00 USD | 0.00 USD | 426,310,000.00 USD | 49,690.00 USD | 682,190.00 USD | 320,060.00 USD |
| `7D` | `2127.60` | 750,360,000.00 USD | 0.00 USD | 750,360,000.00 USD | 2,400,000.00 USD | 2,630,000.00 USD | 3,270,000.00 USD |
| `1D` | `2129.70` | 425,260,000.00 USD | 0.00 USD | 425,260,000.00 USD | 107,010.00 USD | 453,880.00 USD | 0.00 USD |
| `7D` | `2130.90` | 742,070,000.00 USD | 0.00 USD | 742,070,000.00 USD | 2,410,000.00 USD | 2,300,000.00 USD | 1,700,000.00 USD |
| `1D` | `2132.40` | 424,700,000.00 USD | 0.00 USD | 424,700,000.00 USD | 0.00 USD | 18,610.00 USD | 331,620.00 USD |
| `7D` | `2134.20` | 735,650,000.00 USD | 0.00 USD | 735,650,000.00 USD | 2,170,000.00 USD | 550,450.00 USD | 308,060.00 USD |
| `1D` | `2135.10` | 424,350,000.00 USD | 0.00 USD | 424,350,000.00 USD | 0.00 USD | 27,230.00 USD | 0.00 USD |
| `7D` | `2137.50` | 732,620,000.00 USD | 0.00 USD | 732,620,000.00 USD | 1,040,000.00 USD | 880,790.00 USD | 43,560.00 USD |
| `1D` | `2137.80` | 424,320,000.00 USD | 0.00 USD | 424,320,000.00 USD | 0.00 USD | 251,180.00 USD | 0.00 USD |
| `7D` | `2140.80` | 730,660,000.00 USD | 0.00 USD | 730,660,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD |
| `7D` | `2144.10` | 726,720,000.00 USD | 0.00 USD | 726,720,000.00 USD | 449,020.00 USD | 1,130,000.00 USD | 268,500.00 USD |
| `7D` | `2147.40` | 724,880,000.00 USD | 0.00 USD | 724,880,000.00 USD | 657,710.00 USD | 421,320.00 USD | 0.00 USD |
| `7D` | `2150.70` | 723,800,000.00 USD | 0.00 USD | 723,800,000.00 USD | 459,630.00 USD | 463,640.00 USD | 31,040.00 USD |
| `1D` | `2151.30` | 424,070,000.00 USD | 0.00 USD | 424,070,000.00 USD | 208,250.00 USD | 440,530.00 USD | 0.00 USD |
| `1D` | `2154.00` | 423,420,000.00 USD | 0.00 USD | 423,420,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD |
| `7D` | `2154.00` | 722,840,000.00 USD | 0.00 USD | 722,840,000.00 USD | 128,430.00 USD | 311,060.00 USD | 32,590.00 USD |
| `7D` | `2157.30` | 722,370,000.00 USD | 0.00 USD | 722,370,000.00 USD | 388,210.00 USD | 1,030,000.00 USD | 1,080,000.00 USD |
| `1D` | `2159.40` | 422,030,000.00 USD | 0.00 USD | 422,030,000.00 USD | 0.00 USD | 0.00 USD | 37,580.00 USD |
| `7D` | `2160.60` | 719,870,000.00 USD | 0.00 USD | 719,870,000.00 USD | 613,630.00 USD | 1,900,000.00 USD | 1,990,000.00 USD |
| `1D` | `2162.10` | 421,990,000.00 USD | 0.00 USD | 421,990,000.00 USD | 0.00 USD | 3,220,000.00 USD | 100,530.00 USD |
| `7D` | `2163.90` | 715,360,000.00 USD | 0.00 USD | 715,360,000.00 USD | 566,120.00 USD | 3,280,000.00 USD | 1,290,000.00 USD |
| `1D` | `2164.80` | 418,670,000.00 USD | 0.00 USD | 418,670,000.00 USD | 217,960.00 USD | 408,000.00 USD | 107,900.00 USD |
| `7D` | `2167.20` | 710,220,000.00 USD | 0.00 USD | 710,220,000.00 USD | 25,540.00 USD | 3,620,000.00 USD | 50,240.00 USD |
| `1D` | `2167.50` | 417,940,000.00 USD | 0.00 USD | 417,940,000.00 USD | 3,410,000.00 USD | 1,360,000.00 USD | 1,020,000.00 USD |
| `1D` | `2170.20` | 412,150,000.00 USD | 0.00 USD | 412,150,000.00 USD | 5,020,000.00 USD | 3,820,000.00 USD | 2,740,000.00 USD |
| `7D` | `2170.50` | 706,520,000.00 USD | 0.00 USD | 706,520,000.00 USD | 3,500,000.00 USD | 3,730,000.00 USD | 5,210,000.00 USD |
| `1D` | `2172.90` | 400,560,000.00 USD | 0.00 USD | 400,560,000.00 USD | 0.00 USD | 190,230.00 USD | 497,070.00 USD |
| `7D` | `2173.80` | 694,080,000.00 USD | 0.00 USD | 694,080,000.00 USD | 4,370,000.00 USD | 363,040.00 USD | 1,010,000.00 USD |
| `1D` | `2175.60` | 399,880,000.00 USD | 0.00 USD | 399,880,000.00 USD | 345,940.00 USD | 630,790.00 USD | 69,160.00 USD |
| `7D` | `2177.10` | 688,340,000.00 USD | 0.00 USD | 688,340,000.00 USD | 0.00 USD | 0.00 USD | 1,320,000.00 USD |
| `1D` | `2178.30` | 398,830,000.00 USD | 0.00 USD | 398,830,000.00 USD | 445,430.00 USD | 1,250,000.00 USD | 33,190.00 USD |
| `7D` | `2180.40` | 687,020,000.00 USD | 0.00 USD | 687,020,000.00 USD | 0.00 USD | 373,740.00 USD | 328,810.00 USD |
| `1D` | `2181.00` | 397,100,000.00 USD | 0.00 USD | 397,100,000.00 USD | 2,080,000.00 USD | 478,110.00 USD | 1,450,000.00 USD |
| `1D` | `2183.70` | 393,100,000.00 USD | 0.00 USD | 393,100,000.00 USD | 2,590,000.00 USD | 509,320.00 USD | 37,260.00 USD |
| `7D` | `2183.70` | 686,320,000.00 USD | 0.00 USD | 686,320,000.00 USD | 1,760,000.00 USD | 1,310,000.00 USD | 3,950,000.00 USD |
| `1D` | `2186.40` | 389,970,000.00 USD | 0.00 USD | 389,970,000.00 USD | 438,350.00 USD | 1,450,000.00 USD | 1,790,000.00 USD |
| `7D` | `2187.00` | 679,310,000.00 USD | 0.00 USD | 679,310,000.00 USD | 556,600.00 USD | 0.00 USD | 54,020.00 USD |
| `1D` | `2189.10` | 386,290,000.00 USD | 0.00 USD | 386,290,000.00 USD | 0.00 USD | 42,550.00 USD | 693,960.00 USD |
| `7D` | `2190.30` | 678,700,000.00 USD | 0.00 USD | 678,700,000.00 USD | 2,730,000.00 USD | 0.00 USD | 4,200,000.00 USD |
| `1D` | `2191.80` | 385,550,000.00 USD | 0.00 USD | 385,550,000.00 USD | 0.00 USD | 222,200.00 USD | 109,400.00 USD |
| `1D` | `2194.50` | 385,220,000.00 USD | 0.00 USD | 385,220,000.00 USD | 605,210.00 USD | 881,070.00 USD | 0.00 USD |
| `7D` | `2196.90` | 671,770,000.00 USD | 0.00 USD | 671,770,000.00 USD | 2,580,000.00 USD | 474,090.00 USD | 2,040,000.00 USD |
| `1D` | `2197.20` | 383,730,000.00 USD | 0.00 USD | 383,730,000.00 USD | 416,500.00 USD | 0.00 USD | 1,890,000.00 USD |
| `1D` | `2199.90` | 381,430,000.00 USD | 0.00 USD | 381,430,000.00 USD | 201,540.00 USD | 3,100,000.00 USD | 220,720.00 USD |
| `7D` | `2200.20` | 666,680,000.00 USD | 0.00 USD | 666,680,000.00 USD | 3,000,000.00 USD | 5,080,000.00 USD | 3,200,000.00 USD |
| `1D` | `2202.60` | 377,910,000.00 USD | 0.00 USD | 377,910,000.00 USD | 2,660,000.00 USD | 1,410,000.00 USD | 2,100,000.00 USD |
| `7D` | `2203.50` | 655,400,000.00 USD | 0.00 USD | 655,400,000.00 USD | 3,650,000.00 USD | 1,710,000.00 USD | 3,750,000.00 USD |
| `1D` | `2205.30` | 371,750,000.00 USD | 0.00 USD | 371,750,000.00 USD | 968,520.00 USD | 6,090,000.00 USD | 879,150.00 USD |
| `7D` | `2206.80` | 646,290,000.00 USD | 0.00 USD | 646,290,000.00 USD | 6,920,000.00 USD | 9,430,000.00 USD | 4,020,000.00 USD |
| `1D` | `2208.00` | 363,810,000.00 USD | 0.00 USD | 363,810,000.00 USD | 3,240,000.00 USD | 5,170,000.00 USD | 2,530,000.00 USD |
| `7D` | `2210.10` | 625,920,000.00 USD | 0.00 USD | 625,920,000.00 USD | 12,800,000.00 USD | 20,410,000.00 USD | 6,470,000.00 USD |
| `1D` | `2210.70` | 352,860,000.00 USD | 0.00 USD | 352,860,000.00 USD | 2,630,000.00 USD | 3,720,000.00 USD | 1,430,000.00 USD |
| `1D` | `2213.40` | 345,080,000.00 USD | 0.00 USD | 345,080,000.00 USD | 13,740,000.00 USD | 9,500,000.00 USD | 5,780,000.00 USD |
| `7D` | `2213.40` | 586,240,000.00 USD | 0.00 USD | 586,240,000.00 USD | 10,920,000.00 USD | 14,590,000.00 USD | 19,950,000.00 USD |
| `1D` | `2216.10` | 316,060,000.00 USD | 0.00 USD | 316,060,000.00 USD | 15,030,000.00 USD | 9,200,000.00 USD | 11,130,000.00 USD |
| `7D` | `2216.70` | 540,770,000.00 USD | 0.00 USD | 540,770,000.00 USD | 25,710,000.00 USD | 17,030,000.00 USD | 9,390,000.00 USD |
| `1D` | `2218.80` | 280,700,000.00 USD | 0.00 USD | 280,700,000.00 USD | 6,090,000.00 USD | 7,230,000.00 USD | 1,740,000.00 USD |
| `7D` | `2220.00` | 488,640,000.00 USD | 0.00 USD | 488,640,000.00 USD | 24,310,000.00 USD | 12,300,000.00 USD | 12,760,000.00 USD |
| `1D` | `2221.50` | 265,630,000.00 USD | 0.00 USD | 265,630,000.00 USD | 5,390,000.00 USD | 11,940,000.00 USD | 1,360,000.00 USD |
| `7D` | `2223.30` | 439,270,000.00 USD | 0.00 USD | 439,270,000.00 USD | 10,150,000.00 USD | 8,220,000.00 USD | 11,910,000.00 USD |
| `1D` | `2224.20` | 246,950,000.00 USD | 0.00 USD | 246,950,000.00 USD | 10,770,000.00 USD | 5,040,000.00 USD | 5,360,000.00 USD |
| `7D` | `2226.60` | 408,990,000.00 USD | 0.00 USD | 408,990,000.00 USD | 16,350,000.00 USD | 11,030,000.00 USD | 10,260,000.00 USD |
| `1D` | `2226.90` | 225,770,000.00 USD | 0.00 USD | 225,770,000.00 USD | 5,400,000.00 USD | 4,420,000.00 USD | 5,750,000.00 USD |
| `1D` | `2229.60` | 210,210,000.00 USD | 0.00 USD | 210,210,000.00 USD | 9,510,000.00 USD | 15,930,000.00 USD | 1,780,000.00 USD |
| `7D` | `2229.90` | 371,350,000.00 USD | 0.00 USD | 371,350,000.00 USD | 12,730,000.00 USD | 11,790,000.00 USD | 28,550,000.00 USD |
| `1D` | `2232.30` | 182,990,000.00 USD | 0.00 USD | 182,990,000.00 USD | 4,360,000.00 USD | 4,830,000.00 USD | 7,490,000.00 USD |
| `7D` | `2233.20` | 318,280,000.00 USD | 0.00 USD | 318,280,000.00 USD | 16,600,000.00 USD | 24,290,000.00 USD | 10,420,000.00 USD |
| `1D` | `2235.00` | 166,310,000.00 USD | 0.00 USD | 166,310,000.00 USD | 19,080,000.00 USD | 1,450,000.00 USD | 11,770,000.00 USD |
| `7D` | `2236.50` | 266,960,000.00 USD | 0.00 USD | 266,960,000.00 USD | 16,050,000.00 USD | 7,430,000.00 USD | 27,770,000.00 USD |
| `1D` | `2237.70` | 134,000,000.00 USD | 0.00 USD | 134,000,000.00 USD | 23,860,000.00 USD | 7,390,000.00 USD | 12,450,000.00 USD |
| `7D` | `2239.80` | 215,720,000.00 USD | 0.00 USD | 215,720,000.00 USD | 16,720,000.00 USD | 6,600,000.00 USD | 13,750,000.00 USD |
| `1D` | `2240.40` | 90,310,000.00 USD | 0.00 USD | 90,310,000.00 USD | 846,550.00 USD | 760,920.00 USD | 2,550,000.00 USD |
| `1D` | `2243.10` | 86,150,000.00 USD | 0.00 USD | 86,150,000.00 USD | 2,540,000.00 USD | 444,750.00 USD | 5,130,000.00 USD |
| `7D` | `2243.10` | 178,660,000.00 USD | 0.00 USD | 178,660,000.00 USD | 22,920,000.00 USD | 0.00 USD | 18,320,000.00 USD |
| `1D` | `2245.80` | 78,040,000.00 USD | 0.00 USD | 78,040,000.00 USD | 3,700,000.00 USD | 5,740,000.00 USD | 790,870.00 USD |
| `7D` | `2246.40` | 137,410,000.00 USD | 0.00 USD | 137,410,000.00 USD | 14,340,000.00 USD | 0.00 USD | 13,920,000.00 USD |
| `1D` | `2248.50` | 67,810,000.00 USD | 0.00 USD | 67,810,000.00 USD | 15,010,000.00 USD | 0.00 USD | 10,670,000.00 USD |
| `7D` | `2249.70` | 109,150,000.00 USD | 0.00 USD | 109,150,000.00 USD | 25,030,000.00 USD | 0.00 USD | 19,030,000.00 USD |
| `1D` | `2251.20` | 42,130,000.00 USD | 0.00 USD | 42,130,000.00 USD | 12,010,000.00 USD | 1,910,000.00 USD | 661,130.00 USD |
| `7D` | `2253.00` | 65,090,000.00 USD | 0.00 USD | 65,090,000.00 USD | 26,890,000.00 USD | 0.00 USD | 12,040,000.00 USD |
| `1D` | `2253.90` | 27,540,000.00 USD | 0.00 USD | 27,540,000.00 USD | 1,750,000.00 USD | 7,830,000.00 USD | 4,080,000.00 USD |
| `7D` | `2256.30` | 26,160,000.00 USD | 0.00 USD | 26,160,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2256.60` | 13,880,000.00 USD | 0.00 USD | 13,880,000.00 USD | 0.00 USD | 170,210.00 USD | 0.00 USD |
| `7D` | `2259.60` | 10,940,000.00 USD | 0.00 USD | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2262.00` | 13,710,000.00 USD | 0.00 USD | 13,710,000.00 USD | 2,420,000.00 USD | 0.00 USD | 156,010.00 USD |
| `1D` | `2264.70` | 11,140,000.00 USD | 0.00 USD | 11,140,000.00 USD | 0.00 USD | 0.00 USD | 1,480,000.00 USD |
| `1D` | `2267.40` | 9,660,000.00 USD | 0.00 USD | 9,660,000.00 USD | 0.00 USD | 0.00 USD | 3,300,000.00 USD |
| `1D` | `2270.10` | 6,360,000.00 USD | 0.00 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 1,050,000.00 USD |
| `1D` | `2275.50` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 125,710.00 USD | 555,110.00 USD | 114,460.00 USD |
| `7D` | `2275.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2278.20` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 2,720,000.00 USD | 1,360,000.00 USD | 431,610.00 USD |
| `7D` | `2279.40` | 17,000,000.00 USD | 17,000,000.00 USD | 0.00 USD | 0.00 USD | 17,000,000.00 USD | 0.00 USD |
| `1D` | `2279.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2280.90` | 69,400,000.00 USD | 69,400,000.00 USD | 0.00 USD | 39,790,000.00 USD | 25,520,000.00 USD | 4,090,000.00 USD |
| `7D` | `2282.70` | 117,630,000.00 USD | 117,630,000.00 USD | 0.00 USD | 0.00 USD | 87,090,000.00 USD | 13,550,000.00 USD |
| `1D` | `2283.60` | 149,190,000.00 USD | 149,190,000.00 USD | 0.00 USD | 40,630,000.00 USD | 22,390,000.00 USD | 16,760,000.00 USD |
| `7D` | `2286.00` | 128,050,000.00 USD | 128,050,000.00 USD | 0.00 USD | 1,010,000.00 USD | 9,400,000.00 USD | 0.00 USD |
| `1D` | `2286.30` | 150,960,000.00 USD | 150,960,000.00 USD | 0.00 USD | 0.00 USD | 1,640,000.00 USD | 133,600.00 USD |
| `1D` | `2289.00` | 156,420,000.00 USD | 156,420,000.00 USD | 0.00 USD | 0.00 USD | 5,320,000.00 USD | 143,050.00 USD |
| `7D` | `2289.30` | 133,320,000.00 USD | 133,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,280,000.00 USD |
| `1D` | `2291.70` | 163,340,000.00 USD | 163,340,000.00 USD | 0.00 USD | 1,780,000.00 USD | 5,010,000.00 USD | 132,770.00 USD |
| `7D` | `2292.60` | 133,930,000.00 USD | 133,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 607,460.00 USD |
| `1D` | `2294.40` | 177,510,000.00 USD | 177,510,000.00 USD | 0.00 USD | 8,310,000.00 USD | 0.00 USD | 5,860,000.00 USD |
| `7D` | `2295.90` | 161,240,000.00 USD | 161,240,000.00 USD | 0.00 USD | 13,610,000.00 USD | 2,380,000.00 USD | 11,320,000.00 USD |
| `1D` | `2297.10` | 196,550,000.00 USD | 196,550,000.00 USD | 0.00 USD | 10,340,000.00 USD | 8,350,000.00 USD | 350,100.00 USD |
| `7D` | `2299.20` | 189,660,000.00 USD | 189,660,000.00 USD | 0.00 USD | 11,730,000.00 USD | 11,130,000.00 USD | 5,560,000.00 USD |
| `1D` | `2299.80` | 213,670,000.00 USD | 213,670,000.00 USD | 0.00 USD | 1,750,000.00 USD | 7,970,000.00 USD | 7,390,000.00 USD |
| `1D` | `2302.50` | 234,660,000.00 USD | 234,660,000.00 USD | 0.00 USD | 15,230,000.00 USD | 852,700.00 USD | 4,910,000.00 USD |
| `7D` | `2302.50` | 236,770,000.00 USD | 236,770,000.00 USD | 0.00 USD | 23,020,000.00 USD | 7,250,000.00 USD | 16,850,000.00 USD |
| `1D` | `2305.20` | 264,110,000.00 USD | 264,110,000.00 USD | 0.00 USD | 10,430,000.00 USD | 14,490,000.00 USD | 4,540,000.00 USD |
| `7D` | `2305.80` | 257,550,000.00 USD | 257,550,000.00 USD | 0.00 USD | 2,980,000.00 USD | 8,820,000.00 USD | 8,970,000.00 USD |
| `1D` | `2307.90` | 272,010,000.00 USD | 272,010,000.00 USD | 0.00 USD | 2,420,000.00 USD | 3,100,000.00 USD | 2,390,000.00 USD |
| `7D` | `2309.10` | 261,820,000.00 USD | 261,820,000.00 USD | 0.00 USD | 1,240,000.00 USD | 930,630.00 USD | 2,110,000.00 USD |
| `1D` | `2310.60` | 280,700,000.00 USD | 280,700,000.00 USD | 0.00 USD | 691,870.00 USD | 380,460.00 USD | 7,620,000.00 USD |
| `7D` | `2312.40` | 279,960,000.00 USD | 279,960,000.00 USD | 0.00 USD | 7,270,000.00 USD | 0.00 USD | 10,870,000.00 USD |
| `1D` | `2313.30` | 288,640,000.00 USD | 288,640,000.00 USD | 0.00 USD | 890,860.00 USD | 6,730,000.00 USD | 313,050.00 USD |
| `7D` | `2315.70` | 287,840,000.00 USD | 287,840,000.00 USD | 0.00 USD | 0.00 USD | 7,460,000.00 USD | 421,230.00 USD |
| `1D` | `2316.00` | 319,350,000.00 USD | 319,350,000.00 USD | 0.00 USD | 9,790,000.00 USD | 14,310,000.00 USD | 6,610,000.00 USD |
| `1D` | `2318.70` | 332,620,000.00 USD | 332,620,000.00 USD | 0.00 USD | 4,440,000.00 USD | 7,340,000.00 USD | 1,480,000.00 USD |
| `7D` | `2319.00` | 305,340,000.00 USD | 305,340,000.00 USD | 0.00 USD | 4,540,000.00 USD | 4,550,000.00 USD | 8,420,000.00 USD |
| `1D` | `2321.40` | 352,830,000.00 USD | 352,830,000.00 USD | 0.00 USD | 6,490,000.00 USD | 13,570,000.00 USD | 147,610.00 USD |
| `7D` | `2322.30` | 322,500,000.00 USD | 322,500,000.00 USD | 0.00 USD | 1,110,000.00 USD | 15,930,000.00 USD | 108,040.00 USD |
| `1D` | `2324.10` | 366,630,000.00 USD | 366,630,000.00 USD | 0.00 USD | 479,120.00 USD | 9,740,000.00 USD | 3,590,000.00 USD |
| `7D` | `2325.60` | 343,150,000.00 USD | 343,150,000.00 USD | 0.00 USD | 9,720,000.00 USD | 2,540,000.00 USD | 8,390,000.00 USD |
| `1D` | `2326.80` | 372,980,000.00 USD | 372,980,000.00 USD | 0.00 USD | 256,580.00 USD | 291,550.00 USD | 5,800,000.00 USD |
| `7D` | `2328.90` | 354,980,000.00 USD | 354,980,000.00 USD | 0.00 USD | 3,860,000.00 USD | 0.00 USD | 7,960,000.00 USD |
| `1D` | `2329.50` | 383,890,000.00 USD | 383,890,000.00 USD | 0.00 USD | 9,740,000.00 USD | 884,940.00 USD | 281,390.00 USD |
| `1D` | `2332.20` | 399,620,000.00 USD | 399,620,000.00 USD | 0.00 USD | 11,600,000.00 USD | 251,940.00 USD | 3,880,000.00 USD |
| `7D` | `2332.20` | 384,210,000.00 USD | 384,210,000.00 USD | 0.00 USD | 29,230,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2334.90` | 419,410,000.00 USD | 419,410,000.00 USD | 0.00 USD | 13,410,000.00 USD | 2,960,000.00 USD | 3,420,000.00 USD |
| `7D` | `2335.50` | 442,220,000.00 USD | 442,220,000.00 USD | 0.00 USD | 28,990,000.00 USD | 18,420,000.00 USD | 10,600,000.00 USD |
| `1D` | `2337.60` | 433,290,000.00 USD | 433,290,000.00 USD | 0.00 USD | 9,880,000.00 USD | 407,920.00 USD | 3,600,000.00 USD |
| `7D` | `2338.80` | 460,090,000.00 USD | 460,090,000.00 USD | 0.00 USD | 9,570,000.00 USD | 0.00 USD | 8,310,000.00 USD |
| `1D` | `2340.30` | 457,190,000.00 USD | 457,190,000.00 USD | 0.00 USD | 8,010,000.00 USD | 5,100,000.00 USD | 10,780,000.00 USD |
| `7D` | `2342.10` | 500,190,000.00 USD | 500,190,000.00 USD | 0.00 USD | 4,720,000.00 USD | 21,390,000.00 USD | 14,000,000.00 USD |
| `1D` | `2343.00` | 465,500,000.00 USD | 465,500,000.00 USD | 0.00 USD | 2,060,000.00 USD | 3,800,000.00 USD | 2,440,000.00 USD |
| `7D` | `2345.40` | 521,570,000.00 USD | 521,570,000.00 USD | 0.00 USD | 1,350,000.00 USD | 13,990,000.00 USD | 6,020,000.00 USD |
| `1D` | `2345.70` | 483,470,000.00 USD | 483,470,000.00 USD | 0.00 USD | 3,680,000.00 USD | 3,710,000.00 USD | 10,570,000.00 USD |
| `1D` | `2348.40` | 496,540,000.00 USD | 496,540,000.00 USD | 0.00 USD | 5,060,000.00 USD | 6,000,000.00 USD | 2,010,000.00 USD |
| `7D` | `2348.70` | 559,440,000.00 USD | 559,440,000.00 USD | 0.00 USD | 847,620.00 USD | 9,500,000.00 USD | 27,530,000.00 USD |
| `1D` | `2351.10` | 543,350,000.00 USD | 543,350,000.00 USD | 0.00 USD | 31,280,000.00 USD | 4,740,000.00 USD | 10,790,000.00 USD |
| `7D` | `2352.00` | 596,070,000.00 USD | 596,070,000.00 USD | 0.00 USD | 2,930,000.00 USD | 23,060,000.00 USD | 10,630,000.00 USD |
| `1D` | `2353.80` | 559,060,000.00 USD | 559,060,000.00 USD | 0.00 USD | 3,270,000.00 USD | 11,770,000.00 USD | 657,620.00 USD |
| `7D` | `2355.30` | 650,910,000.00 USD | 650,910,000.00 USD | 0.00 USD | 16,780,000.00 USD | 36,690,000.00 USD | 1,380,000.00 USD |
| `1D` | `2356.50` | 573,650,000.00 USD | 573,650,000.00 USD | 0.00 USD | 3,430,000.00 USD | 8,660,000.00 USD | 2,510,000.00 USD |
| `7D` | `2358.60` | 663,040,000.00 USD | 663,040,000.00 USD | 0.00 USD | 7,110,000.00 USD | 512,220.00 USD | 4,510,000.00 USD |
| `1D` | `2359.20` | 590,800,000.00 USD | 590,800,000.00 USD | 0.00 USD | 4,590,000.00 USD | 5,650,000.00 USD | 6,910,000.00 USD |
| `1D` | `2361.90` | 611,960,000.00 USD | 611,960,000.00 USD | 0.00 USD | 10,000,000.00 USD | 8,410,000.00 USD | 2,750,000.00 USD |
| `7D` | `2361.90` | 670,320,000.00 USD | 670,320,000.00 USD | 0.00 USD | 3,150,000.00 USD | 3,800,000.00 USD | 328,810.00 USD |
| `1D` | `2364.60` | 630,330,000.00 USD | 630,330,000.00 USD | 0.00 USD | 6,050,000.00 USD | 4,190,000.00 USD | 8,130,000.00 USD |
| `7D` | `2365.20` | 691,380,000.00 USD | 691,380,000.00 USD | 0.00 USD | 10,200,000.00 USD | 0.00 USD | 10,860,000.00 USD |
| `1D` | `2367.30` | 636,830,000.00 USD | 636,830,000.00 USD | 0.00 USD | 5,160,000.00 USD | 1,110,000.00 USD | 228,790.00 USD |
| `7D` | `2368.50` | 704,450,000.00 USD | 704,450,000.00 USD | 0.00 USD | 10,830,000.00 USD | 1,780,000.00 USD | 458,400.00 USD |
| `1D` | `2370.00` | 673,160,000.00 USD | 673,160,000.00 USD | 0.00 USD | 15,180,000.00 USD | 12,300,000.00 USD | 8,850,000.00 USD |
| `7D` | `2371.80` | 785,380,000.00 USD | 785,380,000.00 USD | 0.00 USD | 26,000,000.00 USD | 0.00 USD | 54,940,000.00 USD |
| `1D` | `2372.70` | 701,630,000.00 USD | 701,630,000.00 USD | 0.00 USD | 14,450,000.00 USD | 5,550,000.00 USD | 8,460,000.00 USD |
| `7D` | `2375.10` | 812,330,000.00 USD | 812,330,000.00 USD | 0.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD |
| `1D` | `2375.40` | 720,450,000.00 USD | 720,450,000.00 USD | 0.00 USD | 11,510,000.00 USD | 3,650,000.00 USD | 3,670,000.00 USD |
| `1D` | `2378.10` | 743,290,000.00 USD | 743,290,000.00 USD | 0.00 USD | 5,260,000.00 USD | 6,340,000.00 USD | 11,240,000.00 USD |
| `7D` | `2378.40` | 857,750,000.00 USD | 857,750,000.00 USD | 0.00 USD | 11,800,000.00 USD | 7,950,000.00 USD | 25,670,000.00 USD |
| `1D` | `2380.80` | 781,050,000.00 USD | 781,050,000.00 USD | 0.00 USD | 11,360,000.00 USD | 11,550,000.00 USD | 14,860,000.00 USD |
| `7D` | `2381.70` | 897,530,000.00 USD | 897,530,000.00 USD | 0.00 USD | 8,510,000.00 USD | 6,750,000.00 USD | 24,530,000.00 USD |
| `1D` | `2383.50` | 830,640,000.00 USD | 830,640,000.00 USD | 0.00 USD | 21,740,000.00 USD | 14,400,000.00 USD | 13,440,000.00 USD |
| `7D` | `2385.00` | 999,250,000.00 USD | 999,250,000.00 USD | 0.00 USD | 18,550,000.00 USD | 36,910,000.00 USD | 46,260,000.00 USD |
| `1D` | `2386.20` | 863,600,000.00 USD | 863,600,000.00 USD | 0.00 USD | 12,110,000.00 USD | 12,530,000.00 USD | 8,330,000.00 USD |
| `7D` | `2388.30` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 5,290,000.00 USD | 38,070,000.00 USD | 44,510,000.00 USD |
| `1D` | `2388.90` | 886,680,000.00 USD | 886,680,000.00 USD | 0.00 USD | 11,000,000.00 USD | 8,120,000.00 USD | 3,970,000.00 USD |
| `1D` | `2391.60` | 904,210,000.00 USD | 904,210,000.00 USD | 0.00 USD | 3,670,000.00 USD | 6,460,000.00 USD | 7,390,000.00 USD |
| `7D` | `2391.60` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 8,560,000.00 USD | 52,080,000.00 USD | 40,380,000.00 USD |
| `1D` | `2394.30` | 920,070,000.00 USD | 920,070,000.00 USD | 0.00 USD | 6,620,000.00 USD | 6,560,000.00 USD | 2,680,000.00 USD |
| `7D` | `2394.90` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 0.00 USD | 57,450,000.00 USD | 32,260,000.00 USD | 37,090,000.00 USD |
| `1D` | `2397.00` | 932,290,000.00 USD | 932,290,000.00 USD | 0.00 USD | 2,270,000.00 USD | 4,990,000.00 USD | 4,960,000.00 USD |
| `7D` | `2398.20` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 42,820,000.00 USD | 38,210,000.00 USD | 29,190,000.00 USD |
| `1D` | `2399.70` | 955,160,000.00 USD | 955,160,000.00 USD | 0.00 USD | 8,430,000.00 USD | 5,600,000.00 USD | 8,840,000.00 USD |
| `7D` | `2401.50` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 0.00 USD | 51,970,000.00 USD | 26,780,000.00 USD | 29,090,000.00 USD |
| `1D` | `2402.40` | 973,750,000.00 USD | 973,750,000.00 USD | 0.00 USD | 6,030,000.00 USD | 6,200,000.00 USD | 6,360,000.00 USD |
| `7D` | `2404.80` | 1,640,000,000.00 USD | 1,640,000,000.00 USD | 0.00 USD | 50,800,000.00 USD | 32,200,000.00 USD | 24,110,000.00 USD |
| `1D` | `2405.10` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 0.00 USD | 11,290,000.00 USD | 9,370,000.00 USD | 8,800,000.00 USD |
| `1D` | `2407.80` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 0.00 USD | 14,220,000.00 USD | 9,590,000.00 USD | 5,790,000.00 USD |
| `7D` | `2408.10` | 1,730,000,000.00 USD | 1,730,000,000.00 USD | 0.00 USD | 34,390,000.00 USD | 31,420,000.00 USD | 25,030,000.00 USD |
| `1D` | `2410.50` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 5,370,000.00 USD | 7,150,000.00 USD | 7,450,000.00 USD |
| `7D` | `2411.40` | 1,810,000,000.00 USD | 1,810,000,000.00 USD | 0.00 USD | 19,200,000.00 USD | 32,580,000.00 USD | 27,660,000.00 USD |
| `1D` | `2413.20` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 0.00 USD | 8,550,000.00 USD | 5,040,000.00 USD | 1,530,000.00 USD |
| `7D` | `2414.70` | 1,880,000,000.00 USD | 1,880,000,000.00 USD | 0.00 USD | 23,820,000.00 USD | 21,740,000.00 USD | 23,130,000.00 USD |
| `1D` | `2415.90` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 0.00 USD | 3,430,000.00 USD | 2,760,000.00 USD | 3,620,000.00 USD |
| `7D` | `2418.00` | 1,950,000,000.00 USD | 1,950,000,000.00 USD | 0.00 USD | 34,060,000.00 USD | 15,260,000.00 USD | 24,450,000.00 USD |
| `1D` | `2418.60` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 4,100,000.00 USD | 2,710,000.00 USD | 3,240,000.00 USD |
| `1D` | `2421.30` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 6,310,000.00 USD | 5,040,000.00 USD | 6,670,000.00 USD |
| `7D` | `2421.30` | 2,030,000,000.00 USD | 2,030,000,000.00 USD | 0.00 USD | 25,700,000.00 USD | 27,770,000.00 USD | 21,590,000.00 USD |
| `1D` | `2424.00` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 1,770,000.00 USD | 3,680,000.00 USD | 1,260,000.00 USD |
| `7D` | `2424.60` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 0.00 USD | 23,840,000.00 USD | 33,060,000.00 USD | 34,520,000.00 USD |
| `1D` | `2426.70` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 972,850.00 USD | 369,950.00 USD | 39,130.00 USD |
| `7D` | `2427.90` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 0.00 USD | 25,200,000.00 USD | 18,380,000.00 USD | 26,460,000.00 USD |
| `1D` | `2429.40` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 1,290,000.00 USD | 1,770,000.00 USD | 1,550,000.00 USD |
| `7D` | `2431.20` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 0.00 USD | 10,380,000.00 USD | 17,060,000.00 USD | 9,300,000.00 USD |
| `1D` | `2432.10` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 2,050,000.00 USD | 1,690,000.00 USD | 436,480.00 USD |
| `7D` | `2434.50` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 27,390,000.00 USD | 21,570,000.00 USD | 11,160,000.00 USD |
| `1D` | `2434.80` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 2,100,000.00 USD | 468,310.00 USD | 1,580,000.00 USD |
| `1D` | `2437.50` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 777,840.00 USD | 531,390.00 USD | 21,360.00 USD |
| `7D` | `2437.80` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 0.00 USD | 11,900,000.00 USD | 12,720,000.00 USD | 5,470,000.00 USD |
| `1D` | `2440.20` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 1,540,000.00 USD | 1,250,000.00 USD | 479,040.00 USD |
| `7D` | `2441.10` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 0.00 USD | 15,080,000.00 USD | 8,120,000.00 USD | 10,640,000.00 USD |
| `1D` | `2442.90` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 1,050,000.00 USD | 1,430,000.00 USD | 1,010,000.00 USD |
| `7D` | `2444.40` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 0.00 USD | 8,860,000.00 USD | 15,100,000.00 USD | 13,960,000.00 USD |
| `1D` | `2445.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 126,820.00 USD | 467,480.00 USD | 1,210,000.00 USD |
| `7D` | `2447.70` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 0.00 USD | 11,480,000.00 USD | 7,520,000.00 USD | 17,330,000.00 USD |
| `1D` | `2448.30` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 886,490.00 USD | 537,830.00 USD | 2,140,000.00 USD |
| `1D` | `2451.00` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 2,460,000.00 USD | 2,020,000.00 USD | 2,940,000.00 USD |
| `7D` | `2451.00` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 0.00 USD | 16,710,000.00 USD | 14,100,000.00 USD | 16,480,000.00 USD |
| `1D` | `2453.70` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 4,450,000.00 USD | 3,260,000.00 USD | 2,870,000.00 USD |
| `7D` | `2454.30` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 0.00 USD | 4,620,000.00 USD | 4,930,000.00 USD | 3,880,000.00 USD |
| `1D` | `2456.40` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 917,470.00 USD | 2,120,000.00 USD | 1,600,000.00 USD |
| `7D` | `2457.60` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 0.00 USD | 15,150,000.00 USD | 12,540,000.00 USD | 12,600,000.00 USD |
| `1D` | `2459.10` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 1,880,000.00 USD | 1,210,000.00 USD | 366,800.00 USD |
| `7D` | `2460.90` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 0.00 USD | 5,580,000.00 USD | 8,670,000.00 USD | 6,870,000.00 USD |
| `1D` | `2461.80` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 490,260.00 USD | 829,050.00 USD |
| `7D` | `2464.20` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 0.00 USD | 8,720,000.00 USD | 7,700,000.00 USD | 4,700,000.00 USD |
| `1D` | `2464.50` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 83,300.00 USD | 176,210.00 USD | 0.00 USD |
| `1D` | `2467.20` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 68,070.00 USD | 0.00 USD |
| `7D` | `2467.50` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 0.00 USD | 4,540,000.00 USD | 3,710,000.00 USD | 586,780.00 USD |
| `1D` | `2469.90` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 1,190,000.00 USD | 391,890.00 USD |
| `7D` | `2470.80` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 0.00 USD | 3,960,000.00 USD | 2,290,000.00 USD | 522,210.00 USD |
| `7D` | `2474.10` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 0.00 USD | 5,230,000.00 USD | 2,920,000.00 USD | 2,400,000.00 USD |
| `1D` | `2475.30` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 914,780.00 USD | 28,770.00 USD |
| `7D` | `2477.40` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 0.00 USD | 1,660,000.00 USD | 4,420,000.00 USD | 718,840.00 USD |
| `1D` | `2478.00` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 55,510.00 USD | 11,450.00 USD |
| `1D` | `2480.70` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 87,180.00 USD | 136,500.00 USD | 43,160.00 USD |
| `7D` | `2480.70` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 0.00 USD | 2,110,000.00 USD | 4,170,000.00 USD | 540,990.00 USD |
| `1D` | `2483.40` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 1,290,000.00 USD | 0.00 USD | 408,620.00 USD |
| `7D` | `2484.00` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 0.00 USD | 1,210,000.00 USD | 1,390,000.00 USD | 1,430,000.00 USD |
| `1D` | `2486.10` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 1,110,000.00 USD | 1,330,000.00 USD | 0.00 USD |
| `7D` | `2487.30` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 0.00 USD | 275,450.00 USD | 211,130.00 USD | 0.00 USD |
| `7D` | `2490.60` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 0.00 USD | 2,910,000.00 USD | 2,540,000.00 USD | 239,380.00 USD |
| `1D` | `2491.50` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 138,370.00 USD | 0.00 USD | 13,360.00 USD |
| `7D` | `2493.90` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 0.00 USD | 1,660,000.00 USD | 1,760,000.00 USD | 3,940,000.00 USD |
| `1D` | `2494.20` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 178,560.00 USD | 21,940.00 USD |
| `1D` | `2496.90` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,270.00 USD |
| `7D` | `2497.20` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 0.00 USD | 2,860,000.00 USD | 4,770,000.00 USD | 8,310,000.00 USD |
| `1D` | `2499.60` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD |
| `7D` | `2500.50` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 0.00 USD | 1,110,000.00 USD | 2,280,000.00 USD | 1,130,000.00 USD |
| `1D` | `2502.30` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 467,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2503.80` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 0.00 USD | 63,860.00 USD | 1,480,000.00 USD | 125,600.00 USD |
| `1D` | `2505.00` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 338,980.00 USD | 717,780.00 USD |
| `7D` | `2507.10` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 0.00 USD | 4,340,000.00 USD | 3,090,000.00 USD | 3,180,000.00 USD |
| `1D` | `2510.40` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD |
| `7D` | `2510.40` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 0.00 USD | 2,290,000.00 USD | 1,270,000.00 USD | 0.00 USD |
| `1D` | `2513.10` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2513.70` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 0.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2515.80` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `7D` | `2517.00` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 0.00 USD | 97,050.00 USD | 189,640.00 USD | 815,620.00 USD |
| `7D` | `2520.30` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD |
| `1D` | `2521.20` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 80,610.00 USD | 121,470.00 USD | 88,290.00 USD |
| `7D` | `2523.60` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 0.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD |
| `1D` | `2523.90` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 984,680.00 USD | 537,030.00 USD | 562,550.00 USD |
| `1D` | `2526.60` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 387,410.00 USD | 362,000.00 USD | 23,500.00 USD |
| `7D` | `2526.90` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 0.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD |
| `1D` | `2529.30` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 641,110.00 USD | 965,400.00 USD | 464,460.00 USD |
| `7D` | `2530.20` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 0.00 USD | 2,800,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD |
| `1D` | `2532.00` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 799,930.00 USD | 534,600.00 USD | 7,120.00 USD |
| `7D` | `2533.50` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 0.00 USD | 3,530,000.00 USD | 1,850,000.00 USD | 2,030,000.00 USD |
| `1D` | `2534.70` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 79,690.00 USD | 62,630.00 USD | 919,610.00 USD |
| `7D` | `2536.80` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 0.00 USD | 3,720,000.00 USD | 3,450,000.00 USD | 3,530,000.00 USD |
| `1D` | `2537.40` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 2,470,000.00 USD | 901,140.00 USD | 1,590,000.00 USD |
| `1D` | `2538.00` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 95,710.00 USD | 380,490.00 USD |
| `7D` | `2540.10` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 0.00 USD | 4,150,000.00 USD | 3,220,000.00 USD | 1,580,000.00 USD |
| `7D` | `2543.40` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 0.00 USD | 4,150,000.00 USD | 2,520,000.00 USD | 2,480,000.00 USD |
| `7D` | `2546.70` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 0.00 USD | 1,450,000.00 USD | 1,090,000.00 USD | 2,290,000.00 USD |
| `7D` | `2550.00` | 2,730,000,000.00 USD | 2,730,000,000.00 USD | 0.00 USD | 4,320,000.00 USD | 3,550,000.00 USD | 3,720,000.00 USD |
| `7D` | `2553.30` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 0.00 USD | 2,820,000.00 USD | 788,360.00 USD | 2,600,000.00 USD |
| `7D` | `2556.60` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 0.00 USD | 2,760,000.00 USD | 283,560.00 USD | 6,500,000.00 USD |
| `7D` | `2559.90` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 0.00 USD | 5,720,000.00 USD | 2,130,000.00 USD | 1,390,000.00 USD |
| `7D` | `2563.20` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 0.00 USD | 1,430,000.00 USD | 2,900,000.00 USD | 1,290,000.00 USD |
| `7D` | `2566.50` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 1,860,000.00 USD | 1,830,000.00 USD | 3,300,000.00 USD |
| `7D` | `2569.80` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 125,250.00 USD | 341,900.00 USD | 1,190,000.00 USD |
| `7D` | `2573.10` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,790,000.00 USD |
| `7D` | `2576.40` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 0.00 USD | 2,400,000.00 USD | 930,280.00 USD | 1,640,000.00 USD |
| `7D` | `2579.70` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 0.00 USD | 2,750,000.00 USD | 1,780,000.00 USD | 1,960,000.00 USD |
| `7D` | `2583.00` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 0.00 USD | 1,730,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD |
| `7D` | `2586.30` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 0.00 USD | 1,480,000.00 USD | 2,030,000.00 USD | 2,570,000.00 USD |
| `7D` | `2589.60` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 0.00 USD | 3,310,000.00 USD | 631,590.00 USD | 2,150,000.00 USD |
| `7D` | `2592.90` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 0.00 USD | 2,370,000.00 USD | 1,280,000.00 USD | 1,580,000.00 USD |
| `7D` | `2596.20` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 0.00 USD | 794,750.00 USD | 620,840.00 USD | 1,490,000.00 USD |
| `7D` | `2599.50` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,530,000.00 USD | 2,810,000.00 USD |
| `7D` | `2602.80` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 1,680,000.00 USD | 1,260,000.00 USD | 1,690,000.00 USD |
| `7D` | `2606.10` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 1,850,000.00 USD | 1,560,000.00 USD | 772,800.00 USD |
| `7D` | `2609.40` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD |
| `7D` | `2612.70` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 1,010,000.00 USD | 643,740.00 USD | 43,560.00 USD |
| `7D` | `2616.00` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD |
| `7D` | `2619.30` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 449,020.00 USD | 323,810.00 USD | 268,500.00 USD |
| `7D` | `2622.60` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 631,440.00 USD | 1,220,000.00 USD | 0.00 USD |
| `7D` | `2625.90` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 485,890.00 USD | 474,490.00 USD | 0.00 USD |
| `7D` | `2629.20` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31,040.00 USD |
| `7D` | `2632.40` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 0.00 USD | 301,060.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `29.38B` | Total OI Tokens: `12,891,067.7 ETH`
  * 1h OI Change: `+0.58%` | 4h OI Change: `-1.23%` | 24h OI Change: `-1.96%`
  * Exchange Breakdown: Binance=`8.56B` | Bybit=`2.13B` | OKX=`1.76B` | Hyperliquid=`2.52B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-74.78K` | Last 24h: `2.27M` | Last 3d: `7.66M` | Last 7d: `13.85M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0011%` | **USDT OKX** | `0.0026%` |
| **USDT Bybit** | `-0.0042%` | **USDT KuCoin** | `-0.0034%` |
| **USDT MEXC** | `-0.0010%` | **USDT BingX** | `0.0031%` |
| **USDT Gate** | `0.0008%` | **USDT Bitget** | `0.0031%` |
| **CoinM Binance** | `0.0077%` | **CoinM OKX** | `-0.0003%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `50.70%` | `49.30%` | `1.03` | 1,890,000,000.00 USD |
| `15M` | `Binance` | `53.37%` | `46.63%` | `1.14` | 416,770,000.00 USD |
| `15M` | `OKX` | `52.79%` | `47.21%` | `1.12` | 168,810,000.00 USD |
| `15M` | `Bybit` | `58.1%` | `41.9%` | `1.39` | 181,510,000.00 USD |
| `15M` | `KuCoin` | `59.16%` | `40.84%` | `1.45` | 4,850,000.00 USD |
| `15M` | `Gate` | `47.24%` | `52.76%` | `0.90` | 171,640,000.00 USD |
| `15M` | `Bitget` | `55.6%` | `44.4%` | `1.25` | 55,560,000.00 USD |
| `15M` | `BingX` | `52.39%` | `47.61%` | `1.10` | 12,080,000.00 USD |
| `15M` | `MEXC` | `53%` | `47%` | `1.13` | 53,980,000.00 USD |
| `15M` | `Bitunix` | `51.18%` | `48.82%` | `1.05` | 82,130,000.00 USD |
| `15M` | `Hyperliquid` | `46.95%` | `53.05%` | `0.89` | 67,590,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `45.67%` | `54.33%` | `0.84` | 4,460,000.00 USD |
| `15M` | `Crypto.com` | `56.66%` | `43.34%` | `1.31` | 9,660,000.00 USD |
| `15M` | `WhiteBIT` | `46.25%` | `53.75%` | `0.86` | 588,110,000.00 USD |
| `15M` | `HTX` | `55.59%` | `44.41%` | `1.25` | 3,860,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `48.41%` | `51.59%` | `0.94` | 32,720,000.00 USD |
| `15M` | `Bitfinex` | `41.21%` | `58.79%` | `0.70` | 1,750,000.00 USD |
| `15M` | `Kraken` | `61.34%` | `38.66%` | `1.59` | 11,250,000.00 USD |
| `15M` | `Aster` | `64.32%` | `35.68%` | `1.80` | 11,050,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `44.77%` | `55.23%` | `0.81` | 13,200,000.00 USD |
| `15M` | `Whale Positions` | `53.37%` | `46.63%` | `1.14` | 416,770,000.00 USD |
| `15M` | `Global Accounts` | `50.70%` | `49.30%` | `1.03` | 1,890,000,000.00 USD |
| `1H` | `ETH` | `50.92%` | `49.08%` | `1.04` | 7,500,000,000.00 USD |
| `1H` | `Binance` | `49.08%` | `50.92%` | `0.96` | 1,980,000,000.00 USD |
| `1H` | `OKX` | `53.54%` | `46.46%` | `1.15` | 865,990,000.00 USD |
| `1H` | `Bybit` | `53.31%` | `46.69%` | `1.14` | 843,210,000.00 USD |
| `1H` | `KuCoin` | `48.05%` | `51.95%` | `0.92` | 20,670,000.00 USD |
| `1H` | `Gate` | `50.44%` | `49.56%` | `1.02` | 697,280,000.00 USD |
| `1H` | `Bitget` | `54.63%` | `45.37%` | `1.20` | 311,980,000.00 USD |
| `1H` | `BingX` | `49.11%` | `50.89%` | `0.97` | 61,760,000.00 USD |
| `1H` | `MEXC` | `49.23%` | `50.77%` | `0.97` | 285,270,000.00 USD |
| `1H` | `Bitunix` | `50.41%` | `49.59%` | `1.02` | 303,420,000.00 USD |
| `1H` | `Hyperliquid` | `40.98%` | `59.02%` | `0.69` | 520,160,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.16%` | `52.84%` | `0.89` | 20,740,000.00 USD |
| `1H` | `Crypto.com` | `53.18%` | `46.82%` | `1.14` | 28,500,000.00 USD |
| `1H` | `WhiteBIT` | `54.54%` | `45.46%` | `1.20` | 1,170,000,000.00 USD |
| `1H` | `HTX` | `48.81%` | `51.19%` | `0.95` | 18,850,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `49.7%` | `50.3%` | `0.99` | 171,200,000.00 USD |
| `1H` | `Bitfinex` | `44.55%` | `55.45%` | `0.80` | 6,260,000.00 USD |
| `1H` | `Kraken` | `53.41%` | `46.59%` | `1.15` | 57,630,000.00 USD |
| `1H` | `Aster` | `54.7%` | `45.3%` | `1.21` | 39,600,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `54%` | `46%` | `1.17` | 86,860,000.00 USD |
| `1H` | `Whale Positions` | `49.08%` | `50.92%` | `0.96` | 1,980,000,000.00 USD |
| `1H` | `Global Accounts` | `50.92%` | `49.08%` | `1.04` | 7,500,000,000.00 USD |
| `4H` | `ETH` | `47.73%` | `52.27%` | `0.91` | 31,780,000,000.00 USD |
| `4H` | `Binance` | `46.49%` | `53.51%` | `0.87` | 8,760,000,000.00 USD |
| `4H` | `OKX` | `46.91%` | `53.09%` | `0.88` | 3,800,000,000.00 USD |
| `4H` | `Bybit` | `46.54%` | `53.46%` | `0.87` | 3,800,000,000.00 USD |
| `4H` | `KuCoin` | `50.01%` | `49.99%` | `1.00` | 130,930,000.00 USD |
| `4H` | `Gate` | `50.9%` | `49.1%` | `1.04` | 2,560,000,000.00 USD |
| `4H` | `Bitget` | `52.52%` | `47.48%` | `1.11` | 1,360,000,000.00 USD |
| `4H` | `BingX` | `51.39%` | `48.61%` | `1.06` | 379,080,000.00 USD |
| `4H` | `MEXC` | `48.79%` | `51.21%` | `0.95` | 1,330,000,000.00 USD |
| `4H` | `Bitunix` | `50.37%` | `49.63%` | `1.01` | 1,340,000,000.00 USD |
| `4H` | `Hyperliquid` | `44.31%` | `55.69%` | `0.80` | 2,050,000,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.7%` | `47.3%` | `1.11` | 135,720,000.00 USD |
| `4H` | `Crypto.com` | `51.12%` | `48.88%` | `1.05` | 148,280,000.00 USD |
| `4H` | `WhiteBIT` | `48.68%` | `51.32%` | `0.95` | 4,360,000,000.00 USD |
| `4H` | `HTX` | `45.38%` | `54.62%` | `0.83` | 98,280,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `49.45%` | `50.55%` | `0.98` | 592,690,000.00 USD |
| `4H` | `Bitfinex` | `21.03%` | `78.97%` | `0.27` | 36,630,000.00 USD |
| `4H` | `Kraken` | `45.38%` | `54.62%` | `0.83` | 282,810,000.00 USD |
| `4H` | `Aster` | `46.53%` | `53.47%` | `0.87` | 252,550,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.17%` | `51.83%` | `0.93` | 349,190,000.00 USD |
| `4H` | `Whale Positions` | `46.49%` | `53.51%` | `0.87` | 8,760,000,000.00 USD |
| `4H` | `Global Accounts` | `47.73%` | `52.27%` | `0.91` | 31,780,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `2315.25` | `2315.75` | `2315.25` | `2318.75` | `2312.25` | 88,922,002.19 USD | 46,836,385.14 USD | 42,085,617.06 USD | 4,750,768.08 USD | `+5.34%` | `3B / 0S` |
| `0:00 UTC` | `2300.25` | `2278.61` | `2300.25` | `2319.25` | `2238.25` | 1,664,912,417.71 USD | 683,261,559.43 USD | 981,650,858.29 USD | -298,389,298.86 USD | `-17.92%` | `1B / 31S` |
| `5:00 UTC` | `2259.25` | `2255.66` | `2259.25` | `2277.25` | `2230.25` | 846,756,637.45 USD | 383,814,230.15 USD | 462,942,407.30 USD | -79,128,177.15 USD | `-9.34%` | `0B / 6S` |
| `0:00 UTC` | `2260.25` | `2257.68` | `2260.25` | `2273.25` | `2245.25` | 606,671,993.02 USD | 300,593,954.86 USD | 306,078,038.17 USD | -5,484,083.31 USD | `-0.90%` | `5B / 2S` |
| `5:00 UTC` | `2281.25` | `2281.90` | `2281.25` | `2293.75` | `2267.75` | 508,254,989.09 USD | 245,674,110.48 USD | 262,580,878.61 USD | -16,906,768.14 USD | `-3.33%` | `3B / 0S` |
| `0:00 UTC` | `2287.25` | `2284.17` | `2287.25` | `2293.25` | `2271.25` | 175,571,332.73 USD | 84,909,600.78 USD | 90,661,731.96 USD | -5,752,131.18 USD | `-3.28%` | `0B / 2S` |
| `5:00 UTC` | `2272.25` | `2272.48` | `2272.25` | `2279.25` | `2266.25` | 164,039,523.36 USD | 80,192,631.79 USD | 83,846,891.57 USD | -3,654,259.77 USD | `-2.23%` | `1B / 3S` |
| `0:00 UTC` | `2258.75` | `2262.31` | `2258.75` | `2272.75` | `2251.25` | 318,288,167.50 USD | 151,770,310.17 USD | 166,517,857.34 USD | -14,747,547.17 USD | `-4.63%` | `1B / 1S` |
| `5:00 UTC` | `2278.25` | `2270.43` | `2278.25` | `2280.25` | `2256.75` | 150,284,586.83 USD | 75,795,431.23 USD | 74,489,155.60 USD | 1,306,275.62 USD | `+0.87%` | `2B / 0S` |
| `0:00 UTC` | `2282.25` | `2278.31` | `2282.25` | `2284.25` | `2269.25` | 121,928,069.49 USD | 59,857,876.55 USD | 62,070,192.94 USD | -2,212,316.39 USD | `-1.81%` | `4B / 2S` |

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
| `5m` | -3,200,000.00 USD | -10,620,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,670,000.00 USD | 12,850,000.00 USD | **`ACCUMULATION`** |
| `30m` | -8,930,000.00 USD | 5,130,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -12,650,000.00 USD | -27,300,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -36,370,000.00 USD | -923,820,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -98,630,000.00 USD | -1,230,000,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -103,400,000.00 USD | -1,420,000,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -88,470,000.00 USD | -1,220,000,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -81,770,000.00 USD | -1,270,000,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -129,740,000.00 USD | -1,700,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -112,920,000.00 USD | -2,280,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,100,000,000.00 USD | -9,280,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-3.20M` | 15m=`-1.67M` | 1h=`-12.65M` | 24h=`-129.74M`
* Futures Capital Netflows: 5m=`-10.62M` | 15m=`+12.85M` | 1h=`-27.30M` | 24h=`-1.70B`
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
  * `2026-10-30 03:30:16 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:11:16 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:11:16 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:10:16 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:12:17 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:12:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:12:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:12:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:12:17 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:12:17 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:12:17 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `2254.13` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2225.81` (Risk Distance: `28.32` pts)
  * +2.5R Take Profit: `2324.93`
  * Mathematical Lot Sizing: **`0.35 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2276.66` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2304.98` (Risk Distance: `28.32` pts)
  * +2.5R Take Profit: `2205.86`
  * Mathematical Lot Sizing: **`0.35 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2288.21`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
