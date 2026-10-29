# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 03:37:25 IST` (`2026-10-29 22:07:25 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2253.80` | **Live Ask Quote**: `2257.70` | **Mid Price**: `2255.75`
- **Spread Points**: `390.00` | **Spread BPS**: `17.29 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2316.39` | VWAP Z-Score: `-1.86` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `19.66` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `32.23` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2393.65` | Lower -3.00σ Band: `2239.13`
  * Upper +2.51σ Band: `2381.03` | Lower -2.51σ Band: `2251.75`
  * Upper +2.01σ Band: `2368.16` | Lower -2.01σ Band: `2264.63`
  * Upper +2.00σ Band: `2367.90` | Lower -2.00σ Band: `2264.89`
  * Upper +1.28σ Band: `2349.36` | Lower -1.28σ Band: `2283.43`
  * Upper +1.00σ Band: `2342.15` | Lower -1.00σ Band: `2290.64`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2281.16` | EMA-20=`2300.73` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2316.34` (Slope: `+0.0000`) | EMA-100=`2323.24`
  * Institutional Anchors: EMA-144=`2325.41` | EMA-200=`2325.99` (Slope: `-0.1847`) | EMA-233=`2326.89`
- **Range Boundaries**: 24H High=`2374.90` | 24H Low=`2225.40` | Weekly High=`2387.80` | Weekly Low=`2225.40`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2284.04` (Distance: `-1.17%`)
  * Point of Control (POC) = `2264.07` (Distance: `-0.29%`)
  * Value Area Low (VAL) = `2259.73` (Distance: `-0.10%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2339.52` | POC=`2321.58` | VAL=`2296.66`
  * Prior Day Extremes: PDH=`2374.90` | PDL=`2225.40` | PDC=`2252.70`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2342.87` | Weekly POC=`2310.39` | Weekly VAL=`2299.56`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2289.10` | Low=`2245.70`
  * London Session (08:00-16:00 UTC): High=`2264.77` | Low=`2246.73`
  * New York Session (13:00-21:00 UTC): High=`2269.28` | Low=`2242.22`
  * Initial Balance (First Hour): IB High=`2262.52` | IB Low=`2248.98`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2246.73` - `2264.77`
  * Optimal Trade Entry (OTE 0.705): `2260.26`
  * Structural Invalidation Anchor (0.786): `2273.80`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2274.31` | `2277.29` | `2269.54` | `2272.46` | `17,082` | 38,857,560.70 USD | 3,975,988.31 USD | `+10.23%` | -854,605,199.04 USD | `+0.52` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `2272.47` | `2272.73` | `2257.86` | `2258.39` | `51,213` | 115,967,739.05 USD | -15,345,781.09 USD | `-13.23%` | -869,950,980.13 USD | `+0.13` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `2258.40` | `2259.77` | `2257.52` | `2259.51` | `1,305` | 2,946,810.19 USD | -228,867.60 USD | `-7.77%` | -870,179,847.73 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `2279.62` | `2293.44` | `2271.00` | `2271.64` | `76,866` | 175,571,332.73 USD | -5,752,131.18 USD | `-3.28%` | -864,791,192.40 USD | `+0.36` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `2271.65` | `2279.09` | `2266.41` | `2272.46` | `72,186` | 164,039,523.36 USD | -3,654,259.77 USD | `-2.23%` | -868,445,452.18 USD | `+0.38` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `2272.47` | `2272.73` | `2257.52` | `2259.51` | `52,518` | 118,914,549.24 USD | -15,574,648.69 USD | `-13.10%` | -884,020,100.87 USD | `+0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2335.68` | `2335.92` | `2230.20` | `2256.63` | `1,357,980` | 3,094,453,113.46 USD | -457,917,547.62 USD | `-14.80%` | -830,712,434.27 USD | `-3.95` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2256.63` | `2293.87` | `2245.02` | `2272.46` | `640,507` | 1,454,537,838.20 USD | -31,797,242.40 USD | `-2.19%` | -862,509,676.67 USD | `+0.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `2272.47` | `2272.73` | `2257.52` | `2259.77` | `52,414` | 118,681,085.34 USD | -15,510,481.47 USD | `-13.07%` | -878,020,158.14 USD | `+0.18` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -163,611,405.07 USD | `+1.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -365,767,522.01 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2257.81` | `2,050,600` | 4,666,989,566.84 USD | -505,736,069.84 USD | `-10.84%` | -871,503,591.85 USD | `-1.89` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2308.03` | `2334.83` | `2303.75` | `2309.10` | `525,175` | 1,216,920,375.04 USD | -34,916,746.14 USD | `-2.87%` | -218,489,329.59 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2309.10` | `2330.05` | `2308.88` | `2324.26` | `409,016` | 949,400,649.22 USD | -49,162,247.72 USD | `-5.18%` | -267,651,577.31 USD | `+0.60` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -163,611,405.07 USD | `+1.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -365,767,522.01 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2257.81` | `2,050,600` | 4,666,989,566.84 USD | -505,736,069.84 USD | `-10.84%` | -871,503,591.85 USD | `-1.89` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`2255.75`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2257.00` | `161.8126` | 365,211.04 USD | 7,120,905.11 USD | `13 orders` | `-0.09%` | `-` |
| `BID` | `2257.10` | `57.9893` | 130,887.65 USD | 6,755,694.07 USD | `8 orders` | `-0.09%` | `-` |
| `BID` | `2257.20` | `255.5205` | 576,760.87 USD | 6,624,806.42 USD | `9 orders` | `-0.08%` | `-` |
| `BID` | `2257.30` | `177.7344` | 401,199.86 USD | 6,048,045.55 USD | `13 orders` | `-0.08%` | `-` |
| `BID` | `2257.40` | `24.5439` | 55,405.40 USD | 5,646,845.69 USD | `6 orders` | `-0.07%` | `-` |
| `BID` | `2257.50` | `349.0510` | 787,982.63 USD | 5,591,440.29 USD | `7 orders` | `-0.07%` | `-` |
| `BID` | `2257.60` | `404.7124` | 913,678.71 USD | 4,803,457.66 USD | `8 orders` | `-0.06%` | `-` |
| `BID` | `2257.70` | `157.6146` | 355,846.48 USD | 3,889,778.94 USD | `15 orders` | `-0.06%` | `-` |
| `BID` | `2257.80` | `264.6281` | 597,477.32 USD | 3,533,932.46 USD | `10 orders` | `-0.06%` | `-` |
| `BID` | `2257.90` | `143.5112` | 324,033.94 USD | 2,936,455.14 USD | `17 orders` | `-0.05%` | `-` |
| `BID` | `2258.00` | `326.9095` | 738,161.65 USD | 2,612,421.20 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `2258.10` | `324.0238` | 731,678.14 USD | 1,874,259.55 USD | `10 orders` | `-0.04%` | `-` |
| `BID` | `2258.20` | `114.4116` | 258,364.28 USD | 1,142,581.41 USD | `7 orders` | `-0.04%` | `-` |
| `BID` | `2258.30` | `137.8801` | 311,374.63 USD | 884,217.13 USD | `5 orders` | `-0.03%` | `-` |
| `BID` | `2258.40` | `78.4030` | 177,065.34 USD | 572,842.50 USD | `7 orders` | `-0.03%` | `-` |
| `BID` | `2258.50` | `57.6965` | 130,307.55 USD | 395,777.17 USD | `7 orders` | `-0.02%` | `-` |
| `BID` | `2258.60` | `70.8768` | 160,082.34 USD | 265,469.62 USD | `6 orders` | `-0.02%` | `-` |
| `BID` | `2258.70` | `3.1081` | 7,020.27 USD | 105,387.28 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `2258.80` | `0.0557` | 125.82 USD | 98,367.01 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `2259.00` | `43.4888` | 98,241.20 USD | 98,241.20 USD | `6 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2259.05` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,259.05` | `0.00%` | `-` |
| `ASK` | `2259.10` | `90.3995` | 204,221.51 USD | 204,221.51 USD | `9 orders` | `+0.00%` | `-` |
| `ASK` | `2259.20` | `2.4845` | 5,612.98 USD | 209,834.49 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `2259.30` | `73.7036` | 166,518.54 USD | 376,353.04 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `2259.40` | `45.4620` | 102,716.84 USD | 479,069.88 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `2259.50` | `44.4992` | 100,545.94 USD | 579,615.82 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `2259.60` | `170.9871` | 386,362.45 USD | 965,978.27 USD | `9 orders` | `+0.02%` | `-` |
| `ASK` | `2259.70` | `249.8299` | 564,540.63 USD | 1,530,518.90 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `2259.80` | `387.9589` | 876,709.52 USD | 2,407,228.42 USD | `12 orders` | `+0.03%` | `-` |
| `ASK` | `2259.90` | `251.8754` | 569,213.22 USD | 2,976,441.64 USD | `10 orders` | `+0.04%` | `-` |
| `ASK` | `2260.00` | `29.8740` | 67,515.24 USD | 3,043,956.88 USD | `7 orders` | `+0.04%` | `-` |
| `ASK` | `2260.10` | `11.4749` | 25,934.42 USD | 3,069,891.30 USD | `10 orders` | `+0.05%` | `-` |
| `ASK` | `2260.20` | `145.5725` | 329,022.96 USD | 3,398,914.26 USD | `19 orders` | `+0.05%` | `-` |
| `ASK` | `2260.30` | `322.1008` | 728,044.44 USD | 4,126,958.70 USD | `14 orders` | `+0.06%` | `-` |
| `ASK` | `2260.40` | `267.1105` | 603,776.57 USD | 4,730,735.27 USD | `13 orders` | `+0.06%` | `-` |
| `ASK` | `2260.50` | `381.6525` | 862,725.48 USD | 5,593,460.75 USD | `17 orders` | `+0.06%` | `-` |
| `ASK` | `2260.60` | `385.9003` | 872,366.22 USD | 6,465,826.97 USD | `17 orders` | `+0.07%` | `-` |
| `ASK` | `2260.70` | `257.2426` | 581,548.35 USD | 7,047,375.32 USD | `14 orders` | `+0.07%` | `-` |
| `ASK` | `2260.80` | `151.4294` | 342,351.59 USD | 7,389,726.90 USD | `14 orders` | `+0.08%` | `-` |
| `ASK` | `2260.90` | `428.6064` | 969,036.21 USD | 8,358,763.11 USD | `15 orders` | `+0.08%` | `-` |
| `ASK` | `2261.00` | `164.9424` | 372,934.77 USD | 8,731,697.88 USD | `5 orders` | `+0.09%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:35:39 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 03:35:39 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1914.18` | `6,500.22` | 12,442,605.92 USD | `AT_RISK_LIQ` | `0xf78c5d8d4b` | `2026-10-30 03:35:39 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1918.00` | `4,184.01` | 8,024,935.59 USD | `TRIGGER_STOP` | `0x6ea486a342` | `2026-10-30 03:35:39 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1925.99` | `8,092.45` | 15,586,021.29 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 03:35:39 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `8,500.00` | 16,371,850.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-30 03:35:39 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2040.72` | `7,964.66` | 16,253,646.32 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-30 03:35:39 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2171.18` | `48,499.51` | 105,301,316.03 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 03:35:39 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2180.25` | `44,734.81` | 97,532,862.28 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2216.30` | `5,376.25` | 11,915,385.98 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2221.90` | `2,185.00` | 4,854,860.17 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2224.70` | `499.11` | 1,110,363.34 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2227.00` | `734.73` | 1,636,235.69 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x646be0d5f9` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2232.60` | `3,413.98` | 7,622,042.15 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2235.70` | `1,528.71` | 3,417,741.64 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2235.70` | `343.39` | 767,714.56 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2238.50` | `500.15` | 1,119,583.54 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2240.20` | `357.84` | 801,627.57 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2242.20` | `994.62` | 2,230,141.90 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:35:39 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2245.00` | `1,758.58` | 3,948,020.86 USD | `TRIGGER_STOP` | `0x28280399d9` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2245.10` | `500.12` | 1,122,808.19 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2245.20` | `1,763.06` | 3,958,422.31 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2248.30` | `683.56` | 1,536,856.04 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2248.50` | `1,781.42` | 4,005,530.07 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2248.70` | `337.20` | 758,254.67 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2249.50` | `467.93` | 1,052,617.53 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2250.50` | `900.32` | 2,026,173.09 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2250.70` | `1,334.72` | 3,004,055.88 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2251.10` | `269.87` | 607,514.04 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x07fd7e702b` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2251.70` | `889.44` | 2,002,745.74 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2252.10` | `478.83` | 1,078,371.02 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2254.20` | `666.29` | 1,501,947.99 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2254.90` | `337.54` | 761,122.55 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2255.70` | `279.27` | 629,949.11 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x07fd7e702b` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2256.40` | `443.76` | 1,001,301.64 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2257.50` | `332.68` | 751,029.61 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2262.10` | `332.02` | 751,054.07 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2262.90` | `286.70` | 648,768.23 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x07fd7e702b` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2263.10` | `442.48` | 1,001,383.05 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2264.80` | `663.26` | 1,502,152.83 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2266.90` | `883.47` | 2,002,745.40 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2267.50` | `286.70` | 650,087.03 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x07fd7e702b` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2268.10` | `514.79` | 1,167,586.13 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2268.90` | `900.32` | 2,042,739.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2269.20` | `1,323.88` | 3,004,146.91 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2270.60` | `324.84` | 737,586.93 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2271.40` | `1,763.43` | 4,005,455.81 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2272.10` | `286.70` | 651,405.84 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x07fd7e702b` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2272.20` | `467.40` | 1,062,030.82 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2273.10` | `748.95` | 1,702,448.70 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2280.30` | `1,081.89` | 2,467,035.82 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2280.70` | `1,760.89` | 4,016,067.52 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2282.30` | `351.24` | 801,627.52 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2282.30` | `336.38` | 767,714.60 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2283.60` | `501.03` | 1,144,147.54 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2285.40` | `498.65` | 1,139,623.85 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2287.60` | `1,550.89` | 3,547,821.23 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2291.00` | `3,421.73` | 7,839,188.93 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2296.10` | `1,442.04` | 3,311,066.67 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xbc76170c8a` | `2026-10-30 03:35:39 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2300.70` | `501.01` | 1,152,669.11 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:35:39 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2305.00` | `1,000.00` | 2,305,000.00 USD | `TRIGGER_STOP` | `0x834cae1ec1` | `2026-10-30 03:35:39 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2389.41` | `17,632.57` | 42,131,523.40 USD | `AT_RISK_LIQ` | `0x8added25f8` | `2026-10-30 03:35:39 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `3,045.71` | 7,656,616.15 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-30 03:35:39 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2585.94` | `6,224.05` | 16,095,020.42 USD | `AT_RISK_LIQ` | `0x08bf75d170` | `2026-10-30 03:35:39 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2658.69` | `9,700.00` | 25,789,336.01 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-30 03:35:39 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2709.05` | `8,500.00` | 23,026,898.55 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-30 03:35:39 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 241,876,815.79 USD | `106,417.71` | `2322.74` | `2273.70` | `3953.23` | 5,304,196.37 USD | `+2.19%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 146,844,412.04 USD | `64,680.62` | `2375.30` | `2273.70` | `4609.28` | 6,791,885.46 USD | `+4.63%` | `5X Cross` |
| `6` | `0x77dd...e0e9` | `LONG` | 110,234,540.60 USD | `48,499.51` | `2610.31` | `2273.70` | `2171.18` | -16,364,343.27 USD | `-14.85%` | `10X Cross` |
| `8` | `0x0392...d7d9` | `LONG` | 101,758,280.04 USD | `44,734.81` | `2518.71` | `2273.70` | `2180.25` | -10,916,026.53 USD | `-10.73%` | `9X Cross` |
| `14` | `0xde8d...9524` | `LONG` | 68,868,242.04 USD | `30,282.40` | `2134.45` | `2273.70` | `1787.13` | 4,231,911.46 USD | `+6.14%` | `20X Cross` |
| `22` | `0xdf95...7d72` | `SHORT` | 51,436,898.45 USD | `22,630.52` | `2402.53` | `2273.70` | `4049.87` | 2,933,697.05 USD | `+5.70%` | `25X Cross` |
| `24` | `0x7fda...17d1` | `SHORT` | 47,761,759.16 USD | `21,013.58` | `2433.53` | `2273.70` | `4241.73` | 3,375,475.94 USD | `+7.07%` | `25X Cross` |
| `32` | `0x8add...7d2c` | `SHORT` | 40,057,669.80 USD | `17,632.57` | `2273.00` | `2273.70` | `2389.01` | 21,215.13 USD | `+0.05%` | `25X Cross` |
| `33` | `0xb695...a92d` | `SHORT` | 37,967,929.66 USD | `16,704.62` | `2557.74` | `2273.70` | `4042.34` | 4,758,235.39 USD | `+12.53%` | `20X Cross` |
| `34` | `0xeced...6210` | `SHORT` | 37,910,835.84 USD | `16,687.58` | `2522.09` | `2273.70` | `3477.74` | 4,176,879.16 USD | `+11.02%` | `20X Cross` |
| `35` | `0x6046...b21d` | `LONG` | 36,201,818.63 USD | `15,927.59` | `2410.19` | `2273.70` | `1691.43` | -2,186,801.02 USD | `-6.04%` | `6X Cross` |
| `40` | `0x45d2...4029` | `SHORT` | 31,706,955.00 USD | `13,950.00` | `2443.60` | `2273.70` | `5253.24` | 2,381,327.46 USD | `+7.51%` | `20X Cross` |
| `44` | `0x2371...0883` | `LONG` | 27,290,400.00 USD | `12,000.00` | `2421.77` | `2273.70` | `1280.11` | -1,770,894.85 USD | `-6.49%` | `20X Cross` |
| `45` | `0xbd1c...ff0e` | `LONG` | 27,272,400.00 USD | `12,000.00` | `2419.91` | `2273.70` | `1521.01` | -1,766,632.39 USD | `-6.48%` | `20X Cross` |
| `55` | `0x09dc...c094` | `LONG` | 25,022,800.00 USD | `11,000.00` | `2465.31` | `2273.70` | `1638.08` | -2,095,623.04 USD | `-8.37%` | `20X Cross` |
| `56` | `0x6c93...59a4` | `LONG` | 25,001,900.00 USD | `11,000.00` | `2441.15` | `2273.70` | `1603.04` | -1,850,772.73 USD | `-7.40%` | `20X Cross` |
| `57` | `0x0c5d...36b3` | `LONG` | 24,994,530.00 USD | `11,000.00` | `2482.20` | `2273.70` | `1645.08` | -2,309,723.24 USD | `-9.24%` | `20X Cross` |
| `58` | `0xa9de...e049` | `LONG` | 24,993,100.00 USD | `11,000.00` | `2481.81` | `2273.70` | `1644.75` | -2,306,879.46 USD | `-9.23%` | `20X Cross` |
| `59` | `0xa61c...66b9` | `LONG` | 24,773,466.40 USD | `10,888.00` | `2398.32` | `2273.70` | `1491.56` | -1,339,490.99 USD | `-5.41%` | `10X Cross` |
| `68` | `0x0622...8088` | `LONG` | 23,454,548.77 USD | `10,319.22` | `2276.95` | `2273.70` | `1307.65` | -41,877.73 USD | `-0.18%` | `5X Cross` |
| `71` | `0xa2ce...3126` | `LONG` | 22,758,340.45 USD | `10,016.88` | `2162.83` | `2273.70` | `1511.78` | 1,093,538.41 USD | `+4.81%` | `10X Cross` |
| `72` | `0x15a4...dfdb` | `LONG` | 22,729,000.00 USD | `10,000.00` | `1761.94` | `2273.70` | `197.55` | 5,109,518.97 USD | `+22.48%` | `20X Cross` |
| `74` | `0xec7f...df39` | `LONG` | 22,721,000.00 USD | `10,000.00` | `2719.35` | `2273.70` | `1721.60` | -4,472,548.52 USD | `-19.68%` | `20X Cross` |
| `75` | `0x6646...6de5` | `LONG` | 22,720,000.00 USD | `10,000.00` | `1765.80` | `2273.70` | `1724.65` | 5,061,942.55 USD | `+22.28%` | `25X Cross` |
| `78` | `0xaeaa...2416` | `SHORT` | 22,021,910.00 USD | `9,700.00` | `2311.92` | `2273.70` | `2658.69` | 403,772.40 USD | `+1.83%` | `25X Cross` |
| `84` | `0xca49...53c8` | `SHORT` | 21,054,886.88 USD | `9,264.26` | `2549.47` | `2273.70` | `3835.59` | 2,564,137.85 USD | `+12.18%` | `25X Cross` |
| `86` | `0xba5d...a352` | `SHORT` | 20,569,154.59 USD | `9,054.12` | `2493.89` | `2273.70` | `2919.82` | 2,010,852.67 USD | `+9.78%` | `20X Cross` |
| `87` | `0xea00...a918` | `LONG` | 20,476,501.77 USD | `9,003.83` | `2003.01` | `2273.70` | `1362.60` | 2,441,722.91 USD | `+11.92%` | `5X Cross` |
| `96` | `0xb37f...66ca` | `SHORT` | 19,319,650.00 USD | `8,500.00` | `2308.30` | `2273.70` | `2709.05` | 300,904.19 USD | `+1.56%` | `25X Cross` |
| `112` | `0x9eec...daab` | `LONG` | 18,393,334.38 USD | `8,092.45` | `1658.44` | `2273.70` | `1925.93` | 4,972,469.85 USD | `+27.03%` | `15X Cross` |
| `114` | `0x218a...7da2` | `SHORT` | 18,178,161.89 USD | `7,997.78` | `2208.16` | `2273.70` | `2815.97` | -517,766.67 USD | `-2.85%` | `10X Cross` |
| `115` | `0x5f91...65aa` | `LONG` | 18,113,220.45 USD | `7,964.66` | `1626.99` | `2273.70` | `2040.72` | 5,154,777.38 USD | `+28.46%` | `16X Cross` |
| `118` | `0xcf53...ee11` | `SHORT` | 17,277,723.68 USD | `7,603.63` | `1862.69` | `2273.70` | `4012.76` | -3,114,459.73 USD | `-18.03%` | `7X Cross` |
| `123` | `0x939f...04d2` | `LONG` | 16,419,004.34 USD | `7,223.81` | `2500.18` | `2273.70` | `1655.99` | -1,641,885.83 USD | `-10.00%` | `25X Cross` |
| `125` | `0x4487...c92d` | `SHORT` | 15,946,178.19 USD | `7,016.40` | `2362.23` | `2273.70` | `2801.80` | 628,241.53 USD | `+3.94%` | `10X Cross` |
| `126` | `0xec0b...b078` | `LONG` | 15,944,844.84 USD | `7,007.80` | `2065.97` | `2273.70` | `1038.73` | 1,466,915.25 USD | `+9.20%` | `25X Cross` |
| `132` | `0x418a...8888` | `SHORT` | 15,314,781.83 USD | `6,724.38` | `2494.55` | `2273.70` | `2995.89` | 1,459,541.35 USD | `+9.53%` | `25X Cross` |
| `135` | `0x4ff9...38d3` | `LONG` | 14,912,319.43 USD | `6,564.10` | `2447.40` | `2273.70` | `1670.70` | -1,152,703.32 USD | `-7.73%` | `3X Isolated` |
| `136` | `0xf78c...c581` | `LONG` | 14,830,905.37 USD | `6,500.22` | `2521.53` | `2273.70` | `1914.18` | -1,559,635.57 USD | `-10.52%` | `20X Cross` |
| `141` | `0x799f...5f4c` | `LONG` | 14,344,052.11 USD | `6,310.90` | `2390.33` | `2273.70` | `1802.00` | -741,112.51 USD | `-5.17%` | `20X Cross` |
| `144` | `0x08bf...7872` | `SHORT` | 14,146,637.34 USD | `6,224.05` | `2258.00` | `2273.70` | `2585.94` | -92,721.23 USD | `-0.66%` | `20X Cross` |
| `150` | `0xc179...e0c8` | `LONG` | 13,895,630.76 USD | `6,113.61` | `2322.20` | `2273.70` | `1196.12` | -301,419.72 USD | `-2.17%` | `10X Cross` |
| `151` | `0x0c4a...1b19` | `LONG` | 13,827,070.34 USD | `6,086.13` | `2373.06` | `2273.70` | `2135.33` | -615,680.23 USD | `-4.45%` | `25X Isolated` |
| `154` | `0xd9e7...4aff` | `LONG` | 13,637,400.00 USD | `6,000.00` | `2480.18` | `2273.70` | `1408.47` | -1,243,724.33 USD | `-9.12%` | `20X Cross` |
| `162` | `0xecb6...2b00` | `SHORT` | 12,965,718.88 USD | `5,706.49` | `2282.83` | `2273.70` | `7305.60` | 61,265.07 USD | `+0.47%` | `15X Cross` |
| `167` | `0x1ee7...edf5` | `LONG` | 12,486,650.00 USD | `5,500.00` | `2316.93` | `2273.70` | `2127.37` | -256,489.62 USD | `-2.05%` | `25X Cross` |
| `183` | `0x645b...87b8` | `SHORT` | 11,358,410.22 USD | `4,997.32` | `2421.64` | `2273.70` | `6496.39` | 743,330.59 USD | `+6.54%` | `10X Cross` |
| `189` | `0x45ab...6cbc` | `LONG` | 11,191,252.24 USD | `4,920.96` | `2727.66` | `2273.70` | `1387.01` | -2,231,491.56 USD | `-19.94%` | `7X Cross` |
| `193` | `0x64b7...9da9` | `LONG` | 11,021,625.20 USD | `4,856.84` | `2604.61` | `2273.70` | `1530.89` | -1,628,589.22 USD | `-14.78%` | `25X Cross` |
| `194` | `0xfb18...eb17` | `SHORT` | 11,010,348.94 USD | `4,845.89` | `2315.54` | `2273.70` | `2626.30` | 210,533.84 USD | `+1.91%` | `25X Cross` |
| `199` | `0x5559...d43b` | `SHORT` | 10,809,742.61 USD | `4,755.93` | `2262.69` | `2273.70` | `2810.07` | -48,536.74 USD | `-0.45%` | `25X Cross` |
| `204` | `0x12d2...f97f` | `LONG` | 10,708,719.07 USD | `4,708.79` | `2588.61` | `2273.70` | `1986.44` | -1,480,515.24 USD | `-13.83%` | `20X Cross` |
| `216` | `0xe091...6705` | `SHORT` | 10,228,050.45 USD | `4,500.00` | `2467.33` | `2273.70` | `2572.99` | 874,958.05 USD | `+8.55%` | `20X Cross` |
| `238` | `0x28bb...fca6` | `SHORT` | 9,548,667.89 USD | `4,209.61` | `1896.10` | `2273.70` | `3040.15` | -1,566,785.33 USD | `-16.41%` | `20X Cross` |
| `240` | `0x6ea4...0ea7` | `SHORT` | 9,505,239.14 USD | `4,184.01` | `2602.13` | `2273.70` | `3426.00` | 1,382,107.52 USD | `+14.54%` | `20X Cross` |
| `253` | `0x5e9e...35ee` | `SHORT` | 9,107,971.84 USD | `4,007.56` | `1796.39` | `2273.70` | `2586.50` | -1,908,821.75 USD | `-20.96%` | `20X Cross` |
| `254` | `0xfb94...0ddf` | `SHORT` | 9,103,179.62 USD | `4,002.10` | `2382.44` | `2273.70` | `5105.39` | 431,604.53 USD | `+4.74%` | `20X Cross` |
| `255` | `0x8cc9...2b6a` | `SHORT` | 9,100,400.00 USD | `4,000.00` | `1791.18` | `2273.70` | `3830.84` | -1,935,653.33 USD | `-21.27%` | `25X Cross` |
| `256` | `0x3dc9...54b0` | `SHORT` | 9,098,095.30 USD | `3,999.69` | `2480.32` | `2273.70` | `6412.03` | 822,441.25 USD | `+9.04%` | `20X Cross` |
| `268` | `0xf02d...5eb3` | `LONG` | 8,764,269.44 USD | `3,855.99` | `2513.67` | `2273.70` | `306.30` | -928,442.87 USD | `-10.59%` | `20X Cross` |
| `273` | `0x4b67...f4e7` | `LONG` | 8,680,188.63 USD | `3,820.84` | `2591.51` | `2273.70` | `1673.45` | -1,221,584.91 USD | `-14.07%` | `20X Cross` |
| `294` | `0x8ae4...3d60` | `LONG` | 8,087,428.92 USD | `3,558.20` | `2482.21` | `2273.70` | `482.98` | -744,769.12 USD | `-9.21%` | `10X Cross` |
| `315` | `0xfe7c...b7ae` | `SHORT` | 7,726,584.57 USD | `3,402.58` | `2440.17` | `2273.70` | `5114.19` | 576,324.70 USD | `+7.46%` | `25X Cross` |
| `320` | `0xefe4...194b` | `SHORT` | 7,508,640.68 USD | `3,304.71` | `2272.28` | `2273.70` | `6622.78` | 603.23 USD | `+0.01%` | `20X Cross` |
| `335` | `0x9c2a...f6a8` | `SHORT` | 6,919,249.20 USD | `3,045.71` | `2543.83` | `2273.70` | `2602.75` | 828,537.34 USD | `+11.97%` | `20X Cross` |
| `340` | `0x4a20...3c26` | `LONG` | 6,818,700.00 USD | `3,000.00` | `2428.72` | `2273.70` | `523.26` | -467,460.28 USD | `-6.86%` | `20X Cross` |
| `341` | `0x007d...67a0` | `LONG` | 6,816,300.00 USD | `3,000.00` | `2400.00` | `2273.70` | `1473.42` | -383,700.00 USD | `-5.63%` | `25X Cross` |
| `348` | `0xbc76...417c` | `LONG` | 6,689,002.87 USD | `2,942.94` | `2261.84` | `2273.70` | `2204.78` | 32,537.98 USD | `+0.49%` | `25X Cross` |
| `385` | `0xf517...c032` | `SHORT` | 6,213,502.93 USD | `2,738.07` | `2053.90` | `2273.70` | `5415.43` | -589,761.02 USD | `-9.49%` | `25X Cross` |
| `398` | `0xfc66...ca06` | `SHORT` | 5,876,588.86 USD | `2,585.50` | `2275.19` | `2273.70` | `12058.94` | 5,946.09 USD | `+0.10%` | `20X Cross` |
| `400` | `0x8328...f54a` | `SHORT` | 5,854,212.19 USD | `2,576.45` | `2292.01` | `2273.70` | `3280.24` | 51,059.10 USD | `+0.87%` | `25X Cross` |
| `401` | `0xed48...7c9b` | `SHORT` | 5,798,464.51 USD | `2,551.13` | `2460.02` | `2273.70` | `3240.51` | 477,381.90 USD | `+8.23%` | `20X Cross` |
| `414` | `0xfbe2...c8ea` | `SHORT` | 5,464,226.16 USD | `2,404.08` | `2041.57` | `2273.70` | `2609.31` | -556,133.43 USD | `-10.18%` | `20X Cross` |
| `423` | `0x1c98...7fc7` | `LONG` | 5,356,914.62 USD | `2,358.00` | `2467.15` | `2273.70` | `1897.22` | -460,656.86 USD | `-8.60%` | `10X Cross` |
| `427` | `0x77ee...2902` | `SHORT` | 5,203,992.27 USD | `2,290.69` | `2476.53` | `2273.70` | `5827.68` | 468,979.97 USD | `+9.01%` | `25X Cross` |
| `436` | `0x023a...2355` | `LONG` | 5,078,513.33 USD | `2,232.35` | `2330.15` | `2273.70` | `0.000000` | -123,215.41 USD | `-2.43%` | `25X Cross` |
| `440` | `0x6859...7e1e` | `SHORT` | 5,056,245.61 USD | `2,224.58` | `2200.39` | `2273.70` | `3937.73` | -161,292.88 USD | `-3.19%` | `25X Cross` |
| `446` | `0xd911...961e` | `LONG` | 4,939,188.48 USD | `2,170.79` | `2275.65` | `2273.70` | `1148.98` | -775.33 USD | `-0.02%` | `25X Cross` |
| `447` | `0xd507...c948` | `SHORT` | 4,936,738.57 USD | `2,172.00` | `2387.49` | `2273.70` | `2707.42` | 248,902.45 USD | `+5.04%` | `5X Isolated` |
| `452` | `0xb829...3a81` | `LONG` | 4,893,470.40 USD | `2,153.91` | `2537.61` | `2273.70` | `705.60` | -572,326.33 USD | `-11.70%` | `20X Cross` |
| `459` | `0x382b...3e39` | `SHORT` | 4,840,235.10 USD | `2,129.54` | `2296.66` | `2273.70` | `4687.27` | 50,602.11 USD | `+1.05%` | `25X Cross` |
| `489` | `0x3440...32c5` | `SHORT` | 4,547,084.64 USD | `2,000.57` | `2198.21` | `2273.70` | `3631.47` | -149,421.51 USD | `-3.29%` | `25X Cross` |
| `491` | `0xc619...10f5` | `LONG` | 4,545,800.00 USD | `2,000.00` | `2318.40` | `2273.70` | `1789.78` | -91,006.86 USD | `-2.00%` | `25X Cross` |
| `492` | `0xf929...d1f9` | `SHORT` | 4,545,800.00 USD | `2,000.00` | `2423.37` | `2273.70` | `2548.82` | 300,940.34 USD | `+6.62%` | `25X Cross` |
| `493` | `0x7a6d...f79c` | `SHORT` | 4,545,800.00 USD | `2,000.00` | `2418.41` | `2273.70` | `2656.18` | 291,032.11 USD | `+6.40%` | `25X Cross` |
| `494` | `0xbb34...1696` | `LONG` | 4,543,600.00 USD | `2,000.00` | `2318.80` | `2273.70` | `1940.20` | -94,016.04 USD | `-2.07%` | `25X Cross` |
| `505` | `0x0514...bdfe` | `SHORT` | 4,430,400.00 USD | `1,950.00` | `1988.74` | `2273.70` | `3044.86` | -552,340.37 USD | `-12.47%` | `25X Cross` |
| `511` | `0x8376...9a1e` | `SHORT` | 4,345,614.20 USD | `1,910.50` | `2477.72` | `2273.70` | `3177.07` | 388,073.97 USD | `+8.93%` | `20X Cross` |
| `520` | `0xfc27...9d9d` | `SHORT` | 4,244,328.23 USD | `1,867.36` | `2341.25` | `2273.70` | `11479.93` | 127,645.52 USD | `+3.01%` | `25X Cross` |
| `542` | `0x541e...071d` | `SHORT` | 4,102,584.50 USD | `1,805.00` | `2648.19` | `2273.70` | `3147.45` | 677,400.34 USD | `+16.51%` | `25X Cross` |
| `543` | `0x7265...91a5` | `LONG` | 4,094,027.46 USD | `1,801.87` | `2533.96` | `2273.70` | `1988.15` | -471,838.99 USD | `-11.53%` | `20X Cross` |
| `544` | `0x739c...cfb2` | `SHORT` | 4,089,780.00 USD | `1,800.00` | `2427.60` | `2273.70` | `2518.52` | 279,916.38 USD | `+6.84%` | `25X Cross` |
| `545` | `0xb15b...dbae` | `SHORT` | 4,085,937.78 USD | `1,797.68` | `2294.54` | `2273.70` | `2302.42` | 38,906.19 USD | `+0.95%` | `25X Cross` |
| `550` | `0xa445...329d` | `LONG` | 4,038,373.48 USD | `1,776.75` | `2398.85` | `2273.70` | `1923.75` | -223,795.87 USD | `-5.54%` | `25X Cross` |
| `556` | `0x91a9...3f70` | `SHORT` | 4,015,537.81 USD | `1,767.48` | `2156.23` | `2273.70` | `3652.73` | -204,433.73 USD | `-5.09%` | `4X Cross` |
| `562` | `0x2828...93a0` | `LONG` | 3,997,085.35 USD | `1,758.58` | `2314.00` | `2273.70` | `2241.75` | -72,281.51 USD | `-1.81%` | `25X Cross` |
| `568` | `0x3453...b323` | `SHORT` | 3,980,129.95 USD | `1,750.12` | `2328.82` | `2273.70` | `2433.37` | 95,602.18 USD | `+2.40%` | `25X Cross` |
| `586` | `0x39b4...5c34` | `SHORT` | 3,890,672.46 USD | `1,713.35` | `2329.97` | `2273.70` | `2495.10` | 101,384.55 USD | `+2.61%` | `25X Cross` |
| `592` | `0xfeec...4e9c` | `SHORT` | 3,845,312.22 USD | `1,691.81` | `2566.49` | `2273.70` | `2654.36` | 496,712.29 USD | `+12.92%` | `10X Cross` |
| `593` | `0x936c...bb0f` | `SHORT` | 3,838,214.41 USD | `1,688.69` | `2434.60` | `2273.70` | `4515.81` | 273,072.70 USD | `+7.11%` | `20X Cross` |
| `597` | `0x2577...4897` | `LONG` | 3,812,029.24 USD | `1,677.17` | `2298.42` | `2273.70` | `221.74` | -42,810.98 USD | `-1.12%` | `15X Cross` |
| `598` | `0xb8eb...1dd5` | `LONG` | 3,810,021.59 USD | `1,676.28` | `2275.16` | `2273.70` | `1006.83` | -3,798.06 USD | `-0.10%` | `25X Cross` |
| `615` | `0xeee0...0b53` | `LONG` | 3,719,218.08 USD | `1,637.12` | `2468.64` | `2273.70` | `213.26` | -322,257.98 USD | `-8.66%` | `7X Cross` |
| `619` | `0x982b...4606` | `LONG` | 3,699,707.90 USD | `1,626.82` | `2575.24` | `2273.70` | `1548.43` | -489,745.17 USD | `-13.24%` | `5X Isolated` |
| `620` | `0x27b8...12fc` | `LONG` | 3,698,926.06 USD | `1,628.12` | `2468.73` | `2273.70` | `572.51` | -320,468.58 USD | `-8.66%` | `10X Cross` |
| `633` | `0x73d7...8be1` | `LONG` | 3,639,650.64 USD | `1,601.47` | `2410.40` | `2273.70` | `2016.96` | -220,528.28 USD | `-6.06%` | `25X Cross` |
| `647` | `0x7b7f...dee2` | `LONG` | 3,534,498.75 USD | `1,555.61` | `2278.49` | `2273.70` | `720.25` | -9,943.02 USD | `-0.28%` | `20X Cross` |
| `659` | `0xe170...9300` | `SHORT` | 3,484,038.14 USD | `1,533.40` | `2076.39` | `2273.70` | `3152.43` | -300,088.64 USD | `-8.61%` | `25X Cross` |
| `663` | `0x4b86...df9d` | `SHORT` | 3,463,899.60 USD | `1,524.00` | `2287.40` | `2273.70` | `2491.45` | 22,098.00 USD | `+0.64%` | `9X Isolated` |
| `674` | `0xad54...6203` | `LONG` | 3,431,529.45 USD | `1,510.29` | `2614.66` | `2273.70` | `2124.65` | -517,377.09 USD | `-15.08%` | `10X Isolated` |
| `676` | `0x2e2b...2fab` | `LONG` | 3,428,076.77 USD | `1,507.38` | `2245.53` | `2273.70` | `1209.96` | 43,203.67 USD | `+1.26%` | `25X Cross` |
| `680` | `0x251f...6e5d` | `LONG` | 3,402,450.00 USD | `1,500.00` | `2346.68` | `2273.70` | `1853.44` | -117,580.49 USD | `-3.46%` | `20X Cross` |
| `696` | `0xef70...a84c` | `SHORT` | 3,273,180.81 USD | `1,442.74` | `2424.73` | `2273.70` | `3295.34` | 225,090.02 USD | `+6.88%` | `25X Cross` |
| `703` | `0x4b5f...0dd8` | `LONG` | 3,256,556.15 USD | `1,431.96` | `2339.45` | `2273.70` | `2148.71` | -93,436.79 USD | `-2.87%` | `10X Cross` |
| `708` | `0xbadb...9ee6` | `LONG` | 3,244,922.34 USD | `1,428.16` | `1936.00` | `2273.70` | `1064.82` | 480,000.69 USD | `+14.79%` | `20X Cross` |
| `726` | `0xf910...0a2d` | `LONG` | 3,161,804.14 USD | `1,391.09` | `2275.91` | `2273.70` | `0.000000` | -4,195.02 USD | `-0.13%` | `5X Cross` |
| `739` | `0xa0fb...96be` | `LONG` | 3,130,701.69 USD | `1,376.25` | `2293.96` | `2273.70` | `1549.95` | -26,373.20 USD | `-0.84%` | `3X Cross` |
| `771` | `0x880a...311c` | `SHORT` | 2,999,282.84 USD | `1,320.22` | `2425.76` | `2273.70` | `8334.42` | 203,266.32 USD | `+6.78%` | `9X Cross` |
| `774` | `0x0dd5...f6ee` | `LONG` | 2,988,863.50 USD | `1,315.00` | `2306.05` | `2273.70` | `1654.20` | -43,600.88 USD | `-1.46%` | `5X Cross` |
| `813` | `0xc435...c905` | `SHORT` | 2,836,579.20 USD | `1,248.00` | `2704.38` | `2273.70` | `5146.22` | 538,491.15 USD | `+18.98%` | `20X Cross` |
| `827` | `0x7178...0854` | `LONG` | 2,768,852.63 USD | `1,218.63` | `2461.81` | `2273.70` | `1150.58` | -231,193.77 USD | `-8.35%` | `10X Cross` |
| `842` | `0xaaa1...ab8c` | `SHORT` | 2,724,360.00 USD | `1,200.00` | `2276.29` | `2273.70` | `2366.21` | 7,197.58 USD | `+0.26%` | `25X Isolated` |
| `865` | `0x07fd...689d` | `LONG` | 2,648,875.03 USD | `1,166.49` | `2419.97` | `2273.70` | `0.000000` | -174,016.77 USD | `-6.57%` | `25X Cross` |
| `905` | `0xbef3...0d3e` | `LONG` | 2,508,051.30 USD | `1,103.99` | `2315.08` | `2273.70` | `2162.38` | -47,784.87 USD | `-1.91%` | `20X Cross` |
| `906` | `0x6a41...a3b9` | `LONG` | 2,498,052.11 USD | `1,099.06` | `2314.77` | `2273.70` | `2164.22` | -46,020.58 USD | `-1.84%` | `20X Cross` |
| `917` | `0x2f80...f203` | `SHORT` | 2,490,299.40 USD | `1,088.94` | `1984.00` | `2273.70` | `3065.56` | -329,832.21 USD | `-13.24%` | `20X Cross` |
| `932` | `0x6f11...0389` | `SHORT` | 2,450,624.80 USD | `1,079.00` | `2333.39` | `2273.70` | `3199.69` | 67,104.11 USD | `+2.74%` | `25X Cross` |
| `934` | `0x2b61...2f6c` | `SHORT` | 2,445,813.52 USD | `1,076.60` | `2681.75` | `2273.70` | `6460.09` | 441,359.22 USD | `+18.05%` | `10X Cross` |
| `975` | `0x1b2a...f7a6` | `LONG` | 2,331,891.91 USD | `1,025.37` | `2737.51` | `2273.70` | `883.09` | -475,068.03 USD | `-20.37%` | `10X Cross` |
| `988` | `0x001a...fef6` | `SHORT` | 2,289,548.99 USD | `1,007.33` | `2022.19` | `2273.70` | `3071.30` | -252,541.04 USD | `-11.03%` | `10X Cross` |
| `994` | `0x02aa...1806` | `SHORT` | 2,284,828.14 USD | `1,007.10` | `2654.68` | `2273.70` | `3613.69` | 388,703.96 USD | `+17.01%` | `20X Cross` |
| `996` | `0xdb3a...cf3b` | `LONG` | 2,280,207.60 USD | `1,003.22` | `2705.01` | `2273.70` | `0.000000` | -433,499.29 USD | `-19.01%` | `4X Cross` |
| `999` | `0x7743...e4fe` | `SHORT` | 2,274,164.19 USD | `1,000.56` | `2298.56` | `2273.70` | `4974.43` | 25,680.88 USD | `+1.13%` | `25X Cross` |
| `1001` | `0x5272...fcd9` | `SHORT` | 2,272,900.00 USD | `1,000.00` | `2241.82` | `2273.70` | `2831.74` | -31,075.51 USD | `-1.37%` | `5X Cross` |
| `1002` | `0xb885...3c54` | `LONG` | 2,272,705.00 USD | `1,000.00` | `2273.87` | `2273.70` | `0.000000` | -1,170.74 USD | `-0.05%` | `20X Cross` |
| `1003` | `0x834c...dd93` | `SHORT` | 2,272,230.00 USD | `1,000.00` | `2249.68` | `2273.70` | `2310.91` | -22,544.58 USD | `-0.99%` | `25X Cross` |
| `1027` | `0xb002...ed8a` | `SHORT` | 2,189,563.37 USD | `962.78` | `2299.66` | `2273.70` | `4200.00` | 24,514.54 USD | `+1.12%` | `25X Cross` |
| `1040` | `0xd4c1...3d1d` | `SHORT` | 2,148,680.38 USD | `945.72` | `2334.28` | `2273.70` | `7572.42` | 58,900.54 USD | `+2.74%` | `12X Cross` |
| `1047` | `0xc8fe...afa4` | `LONG` | 2,128,279.46 USD | `936.37` | `2331.34` | `2273.70` | `2145.82` | -54,724.77 USD | `-2.57%` | `10X Isolated` |
| `1064` | `0x31de...13f2` | `LONG` | 2,099,801.85 USD | `923.84` | `2275.50` | `2273.70` | `0.000000` | -2,408.58 USD | `-0.11%` | `20X Cross` |
| `1074` | `0x9606...4e5d` | `SHORT` | 2,075,150.20 USD | `913.00` | `2478.70` | `2273.70` | `4270.36` | 187,903.41 USD | `+9.05%` | `20X Cross` |
| `1087` | `0x5f10...d49d` | `LONG` | 2,045,610.00 USD | `900.00` | `2249.83` | `2273.70` | `1804.24` | 20,756.53 USD | `+1.01%` | `25X Cross` |
| `1088` | `0x5238...54e5` | `SHORT` | 2,045,610.00 USD | `900.00` | `2289.53` | `2273.70` | `4705.02` | 14,972.42 USD | `+0.73%` | `25X Cross` |
| `1111` | `0x2e30...4cb5` | `SHORT` | 2,010,474.73 USD | `884.85` | `2340.07` | `2273.70` | `7810.13` | 60,144.09 USD | `+2.99%` | `2X Cross` |
| `1195` | `0xcd27...52a8` | `LONG` | 1,903,979.12 USD | `837.21` | `2553.56` | `2273.70` | `1404.24` | -233,885.66 USD | `-12.28%` | `2X Cross` |
| `1231` | `0x6ff1...8575` | `LONG` | 1,849,616.41 USD | `814.06` | `2272.53` | `2273.70` | `2227.12` | -353.35 USD | `-0.02%` | `25X Isolated` |
| `1246` | `0x3fc5...c0c1` | `SHORT` | 1,827,113.78 USD | `804.26` | `2702.11` | `2273.70` | `4930.10` | 346,087.75 USD | `+18.94%` | `25X Cross` |
| `1252` | `0x04a9...95aa` | `LONG` | 1,819,360.00 USD | `800.00` | `2595.13` | `2273.70` | `1887.34` | -256,746.74 USD | `-14.11%` | `5X Cross` |
| `1255` | `0x7737...bf66` | `SHORT` | 1,817,207.18 USD | `799.79` | `2494.83` | `2273.70` | `23868.83` | 178,138.85 USD | `+9.80%` | `15X Cross` |
| `1268` | `0xf83f...625f` | `SHORT` | 1,795,379.61 USD | `790.22` | `2595.19` | `2273.70` | `6178.49` | 255,392.15 USD | `+14.22%` | `20X Cross` |
| `1293` | `0x458d...ab3b` | `LONG` | 1,760,380.13 USD | `774.75` | `2740.41` | `2273.70` | `1887.99` | -362,749.05 USD | `-20.61%` | `3X Isolated` |
| `1347` | `0xaa53...9cb7` | `LONG` | 1,659,982.29 USD | `730.34` | `2389.70` | `2273.70` | `1950.78` | -85,307.35 USD | `-5.14%` | `20X Cross` |
| `1356` | `0xab81...c608` | `SHORT` | 1,652,361.98 USD | `727.27` | `2285.37` | `2273.70` | `5219.36` | 9,725.11 USD | `+0.59%` | `20X Cross` |
| `1366` | `0x51a0...3543` | `SHORT` | 1,646,820.15 USD | `724.55` | `2627.71` | `2273.70` | `7451.90` | 257,076.61 USD | `+15.61%` | `20X Cross` |
| `1376` | `0xa189...94d7` | `SHORT` | 1,636,440.27 USD | `719.98` | `2691.84` | `2273.70` | `3051.94` | 301,632.39 USD | `+18.43%` | `25X Cross` |
| `1393` | `0x2f93...4404` | `LONG` | 1,607,375.25 USD | `707.47` | `1700.45` | `2273.70` | `1369.62` | 404,348.87 USD | `+25.16%` | `4X Isolated` |
| `1398` | `0x5605...fe0f` | `SHORT` | 1,595,200.04 USD | `702.14` | `2566.90` | `2273.70` | `3068.03` | 207,132.60 USD | `+12.98%` | `20X Cross` |
| `1401` | `0x0deb...0bc5` | `LONG` | 1,591,030.00 USD | `700.00` | `2071.05` | `2273.70` | `1598.21` | 141,294.21 USD | `+8.88%` | `20X Cross` |
| `1452` | `0xdbd1...29dd` | `SHORT` | 1,546,556.08 USD | `680.70` | `3030.57` | `2273.70` | `4075.15` | 516,365.04 USD | `+33.39%` | `6X Cross` |
| `1453` | `0xb1ec...e86a` | `SHORT` | 1,544,852.92 USD | `679.30` | `2271.56` | `2273.70` | `16735.61` | -1,789.68 USD | `-0.12%` | `25X Cross` |
| `1458` | `0x71e5...be04` | `LONG` | 1,540,268.87 USD | `677.67` | `2727.27` | `2273.70` | `1471.77` | -307,916.74 USD | `-19.99%` | `20X Cross` |
| `1464` | `0x0b23...f37b` | `LONG` | 1,533,465.00 USD | `675.00` | `2238.15` | `2273.70` | `593.17` | 22,708.36 USD | `+1.48%` | `5X Cross` |
| `1473` | `0x4b1c...bc38` | `SHORT` | 1,526,234.79 USD | `671.97` | `2528.62` | `2273.70` | `4444.93` | 172,910.81 USD | `+11.33%` | `10X Cross` |
| `1478` | `0x34fb...93de` | `LONG` | 1,517,651.84 USD | `667.70` | `2275.24` | `2273.70` | `0.000000` | -1,518.46 USD | `-0.10%` | `20X Cross` |
| `1482` | `0x1f16...6d07` | `LONG` | 1,513,751.40 USD | `666.00` | `2287.38` | `2273.70` | `1341.83` | -9,647.89 USD | `-0.64%` | `7X Cross` |
| `1488` | `0x696d...8e28` | `SHORT` | 1,502,015.18 USD | `660.46` | `2270.91` | `2273.70` | `4578.34` | -2,168.99 USD | `-0.14%` | `20X Cross` |
| `1494` | `0x0cac...6170` | `SHORT` | 1,493,905.75 USD | `657.50` | `2146.55` | `2273.70` | `2840.19` | -82,543.55 USD | `-5.53%` | `20X Cross` |
| `1518` | `0x621c...63ab` | `LONG` | 1,461,430.38 USD | `642.98` | `2281.90` | `2273.70` | `0.000000` | -5,793.03 USD | `-0.40%` | `20X Cross` |
| `1519` | `0xf00e...fe3d` | `SHORT` | 1,461,201.95 USD | `642.88` | `2333.21` | `2273.70` | `2532.78` | 38,776.02 USD | `+2.65%` | `20X Cross` |
| `1520` | `0xaa7a...af37` | `LONG` | 1,460,646.91 USD | `642.64` | `2273.28` | `2273.70` | `0.000000` | -249.76 USD | `-0.02%` | `20X Cross` |
| `1525` | `0xffb2...5ed6` | `SHORT` | 1,456,398.86 USD | `640.77` | `2672.96` | `2273.70` | `2500.23` | 256,349.49 USD | `+17.60%` | `20X Cross` |
| `1536` | `0x7c90...d129` | `LONG` | 1,450,101.17 USD | `639.17` | `2286.01` | `2273.70` | `1916.93` | -11,052.24 USD | `-0.76%` | `20X Cross` |
| `1543` | `0xa522...2d0e` | `SHORT` | 1,445,753.10 USD | `636.36` | `2284.42` | `2273.70` | `4350.76` | 7,972.74 USD | `+0.55%` | `20X Cross` |
| `1561` | `0x871f...972b` | `SHORT` | 1,424,574.40 USD | `626.77` | `2279.80` | `2273.70` | `2594.68` | 4,327.43 USD | `+0.30%` | `20X Cross` |
| `1568` | `0xfce0...f4c0` | `SHORT` | 1,418,191.12 USD | `623.60` | `3129.61` | `2273.70` | `2788.43` | 533,435.46 USD | `+37.61%` | `20X Cross` |
| `1586` | `0x7663...cb5a` | `SHORT` | 1,394,387.36 USD | `613.54` | `2342.35` | `2273.70` | `3759.70` | 42,733.13 USD | `+3.06%` | `3X Cross` |
| `1610` | `0x26e6...6b28` | `LONG` | 1,364,760.00 USD | `600.00` | `1769.78` | `2273.70` | `2005.49` | 302,888.47 USD | `+22.19%` | `20X Cross` |
| `1611` | `0xad02...eb65` | `LONG` | 1,364,128.60 USD | `600.62` | `2460.69` | `2273.70` | `1079.69` | -113,811.96 USD | `-8.34%` | `5X Cross` |
| `1612` | `0x638f...f5f0` | `LONG` | 1,363,260.00 USD | `600.00` | `4011.50` | `2273.70` | `296.75` | -1,043,643.53 USD | `-76.55%` | `25X Cross` |
| `1613` | `0x67c3...609d` | `SHORT` | 1,363,080.00 USD | `600.00` | `2386.55` | `2273.70` | `2560.78` | 68,851.89 USD | `+5.05%` | `25X Cross` |
| `1619` | `0x9599...c60a` | `LONG` | 1,355,348.68 USD | `596.31` | `2273.47` | `2273.70` | `0.000000` | -343.92 USD | `-0.03%` | `20X Cross` |
| `1653` | `0xca8e...507d` | `LONG` | 1,318,282.00 USD | `580.00` | `2253.46` | `2273.70` | `2069.74` | 11,271.65 USD | `+0.86%` | `10X Isolated` |
| `1680` | `0xfb99...37f3` | `LONG` | 1,284,511.51 USD | `565.34` | `2362.35` | `2273.70` | `1233.97` | -51,024.84 USD | `-3.97%` | `3X Cross` |
| `1689` | `0x844b...7f42` | `SHORT` | 1,274,479.80 USD | `561.00` | `2026.17` | `2273.70` | `3188.65` | -137,796.39 USD | `-10.81%` | `25X Cross` |
| `1702` | `0x3947...f3b1` | `LONG` | 1,265,301.38 USD | `556.69` | `2274.94` | `2273.70` | `0.000000` | -1,139.25 USD | `-0.09%` | `20X Cross` |
| `1704` | `0xabe6...1d99` | `SHORT` | 1,263,741.49 USD | `556.00` | `2484.68` | `2273.70` | `3094.80` | 117,754.40 USD | `+9.32%` | `20X Cross` |
| `1740` | `0x0a97...347d` | `LONG` | 1,223,804.59 USD | `538.43` | `2273.47` | `2273.70` | `844.56` | -309.13 USD | `-0.03%` | `20X Cross` |
| `1748` | `0xad21...fb6a` | `LONG` | 1,208,885.73 USD | `531.87` | `2574.89` | `2273.70` | `1704.93` | -160,619.77 USD | `-13.29%` | `7X Cross` |
| `1761` | `0x0082...1ae3` | `LONG` | 1,198,718.40 USD | `528.00` | `2448.58` | `2273.70` | `2234.25` | -94,136.51 USD | `-7.85%` | `25X Cross` |
| `1804` | `0x0c7a...2f50` | `SHORT` | 1,157,463.64 USD | `509.25` | `2122.56` | `2273.70` | `4105.15` | -76,558.21 USD | `-6.61%` | `20X Cross` |
| `1808` | `0x0089...2410` | `SHORT` | 1,153,145.81 USD | `507.35` | `2308.88` | `2273.70` | `3401.86` | 18,254.44 USD | `+1.58%` | `20X Cross` |
| `1831` | `0xa559...ff95` | `LONG` | 1,137,100.00 USD | `500.00` | `2260.68` | `2273.70` | `1150.23` | 6,755.64 USD | `+0.59%` | `20X Cross` |
| `1833` | `0x89b2...9ca6` | `LONG` | 1,136,000.00 USD | `500.00` | `2484.03` | `2273.70` | `1954.22` | -106,019.35 USD | `-9.33%` | `25X Cross` |
| `1835` | `0x7298...7d6c` | `SHORT` | 1,132,891.14 USD | `498.15` | `3426.75` | `2273.70` | `5422.40` | 574,144.68 USD | `+50.68%` | `20X Cross` |
| `1838` | `0xa70a...4be9` | `LONG` | 1,129,136.68 USD | `496.83` | `2272.13` | `2273.70` | `0.000000` | 279.13 USD | `+0.02%` | `20X Cross` |
| `1842` | `0x536c...3e1f` | `LONG` | 1,124,599.91 USD | `494.83` | `2275.87` | `2273.70` | `2128.57` | -1,572.41 USD | `-0.14%` | `20X Cross` |
| `1849` | `0x9c68...7783` | `SHORT` | 1,120,203.35 USD | `493.31` | `2273.58` | `2273.70` | `3866.27` | 1,375.90 USD | `+0.12%` | `25X Cross` |
| `1857` | `0x6e6f...82a6` | `LONG` | 1,115,002.92 USD | `490.56` | `2271.11` | `2273.70` | `149.50` | 876.75 USD | `+0.08%` | `20X Cross` |
| `1863` | `0xc10f...23b3` | `LONG` | 1,113,182.00 USD | `490.00` | `2383.92` | `2273.70` | `2084.50` | -54,939.28 USD | `-4.94%` | `25X Cross` |
| `1864` | `0x404c...5f03` | `SHORT` | 1,112,792.20 USD | `489.79` | `2671.94` | `2273.70` | `4950.70` | 195,887.36 USD | `+17.60%` | `20X Cross` |
| `1868` | `0x321f...1c84` | `SHORT` | 1,109,210.20 USD | `488.02` | `2370.09` | `2273.70` | `3031.66` | 47,434.40 USD | `+4.28%` | `10X Cross` |
| `1878` | `0x8923...1bac` | `SHORT` | 1,094,002.92 USD | `480.82` | `2277.43` | `2273.70` | `3113.69` | 1,025.12 USD | `+0.09%` | `25X Cross` |
| `1929` | `0x82c6...fe42` | `LONG` | 1,052,048.75 USD | `462.50` | `2501.38` | `2273.70` | `2054.47` | -104,841.82 USD | `-9.97%` | `5X Isolated` |
| `1938` | `0x2de3...486d` | `LONG` | 1,046,443.16 USD | `460.40` | `2286.27` | `2273.70` | `1278.49` | -6,157.75 USD | `-0.59%` | `25X Cross` |
| `1945` | `0x617e...0f97` | `SHORT` | 1,040,657.27 USD | `457.85` | `2205.60` | `2273.70` | `3767.14` | -30,813.43 USD | `-2.96%` | `10X Cross` |
| `1947` | `0x7717...bd7e` | `LONG` | 1,040,190.64 USD | `457.65` | `2277.03` | `2273.70` | `0.000000` | -1,891.14 USD | `-0.18%` | `20X Cross` |
| `1971` | `0xae55...2236` | `LONG` | 1,022,805.00 USD | `450.00` | `2510.21` | `2273.70` | `0.000000` | -106,792.50 USD | `-10.44%` | `25X Cross` |
| `1986` | `0xac26...a9c7` | `SHORT` | 1,014,342.77 USD | `446.28` | `2192.58` | `2273.70` | `8583.37` | -35,843.07 USD | `-3.53%` | `20X Cross` |
| `1987` | `0x53f8...ceff` | `LONG` | 1,012,308.40 USD | `445.60` | `2399.81` | `2273.70` | `0.000000` | -57,042.20 USD | `-5.63%` | `20X Cross` |
| `1999` | `0xd6e1...f256` | `SHORT` | 1,008,395.95 USD | `443.66` | `2259.33` | `2273.70` | `3573.90` | -6,016.73 USD | `-0.60%` | `25X Cross` |
| `2015` | `0xd8a1...6687` | `LONG` | 1,003,162.98 USD | `441.53` | `2804.24` | `2273.70` | `2151.03` | -235,005.46 USD | `-23.43%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `ANNOUNCEMENT` | `INFO` | `2362.30` | 10,820.99 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 10.82K USD at 2362.3000 USD [API] | `2026-10-27 21:33:37` |
| `ANNOUNCEMENT` | `INFO` | `2362.30` | 107.96 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.11K USD at 2362.3000 USD [API] | `2026-10-27 21:33:37` |
| `ANNOUNCEMENT` | `INFO` | `2362.30` | 3,244.86 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 3.24K USD at 2362.3000 USD [API] | `2026-10-27 21:33:37` |
| `ANNOUNCEMENT` | `INFO` | `2351.90` | 40,041.57 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 40.04K USD at 2351.9000 USD [API] | `2026-10-28 18:34:28` |
| `ANNOUNCEMENT` | `INFO` | `2351.90` | 110,984.75 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 110.98K USD at 2351.9000 USD [API] | `2026-10-28 18:34:28` |
| `ANNOUNCEMENT` | `INFO` | `2359.60` | 402,569.00 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 402.57K USD at 2359.6000 USD [API] | `2026-10-28 18:37:59` |
| `ANNOUNCEMENT` | `INFO` | `2359.50` | 40,039.54 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 40.04K USD at 2359.5000 USD [API] | `2026-10-28 18:37:59` |
| `ANNOUNCEMENT` | `INFO` | `2359.20` | 40,039.40 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 40.04K USD at 2359.2000 USD [API] | `2026-10-28 18:37:59` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`2303.89` (Vol: 21,900,000.00 USD, Dist: `+1.13%`) | Long MP=`2242.01` (Vol: 29,100,000.00 USD, Dist: `--1.59%`)
  * 48H Horizon: Short MP=`2402.77` (Vol: 36,200,000.00 USD, Dist: `+5.47%`) | Long MP=`2242.90` (Vol: 29,100,000.00 USD, Dist: `--1.55%`)
  * 3D Horizon: Short MP=`2402.77` (Vol: 36,700,000.00 USD, Dist: `+5.47%`) | Long MP=`2242.90` (Vol: 29,100,000.00 USD, Dist: `--1.55%`)
  * 7D Horizon: Short MP=`2393.80` (Vol: 49,300,000.00 USD, Dist: `+5.07%`) | Long MP=`2241.80` (Vol: 29,100,000.00 USD, Dist: `--1.60%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `455.00` | 80,200.00 USD | 846,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `1D` | `Long Liquidation` | `2017.60` | 446,740,000.00 USD | 446,740,000.00 USD | 83,300.00 USD | 176,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2020.60` | 446,480,000.00 USD | 446,480,000.00 USD | 0.00 USD | 558,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2025.00` | 2,210,000.00 USD | 318,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2025.30` | 893,380,000.00 USD | 893,380,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2026.60` | 445,920,000.00 USD | 445,920,000.00 USD | 0.00 USD | 914,780.00 USD | 28,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2028.60` | 893,210,000.00 USD | 893,210,000.00 USD | 0.00 USD | 1,180,000.00 USD | 35,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2029.60` | 444,980,000.00 USD | 444,980,000.00 USD | 87,180.00 USD | 136,500.00 USD | 43,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2031.90` | 891,990,000.00 USD | 891,990,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2032.60` | 444,710,000.00 USD | 444,710,000.00 USD | 850,010.00 USD | 1,330,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2035.00` | 538,430.00 USD | 315,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2035.20` | 890,540,000.00 USD | 890,540,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2035.60` | 442,530,000.00 USD | 442,530,000.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2038.50` | 890,210,000.00 USD | 890,210,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2038.60` | 441,500,000.00 USD | 441,500,000.00 USD | 138,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2041.60` | 441,360,000.00 USD | 441,360,000.00 USD | 0.00 USD | 178,560.00 USD | 14,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2045.00` | 16,630,000.00 USD | 315,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2045.10` | 888,750,000.00 USD | 888,750,000.00 USD | 0.00 USD | 149,500.00 USD | 47,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2050.60` | 441,160,000.00 USD | 441,160,000.00 USD | 0.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2051.70` | 888,560,000.00 USD | 888,560,000.00 USD | 1,320,000.00 USD | 0.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2053.60` | 440,110,000.00 USD | 440,110,000.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2055.00` | 13,190,000.00 USD | 298,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2056.60` | 439,990,000.00 USD | 439,990,000.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2058.30` | 886,050,000.00 USD | 886,050,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2059.60` | 439,750,000.00 USD | 439,750,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2061.60` | 885,710,000.00 USD | 885,710,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2062.60` | 438,990,000.00 USD | 438,990,000.00 USD | 80,610.00 USD | 121,470.00 USD | 88,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2064.90` | 880,450,000.00 USD | 880,450,000.00 USD | 1,230,000.00 USD | 313,000.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2065.00` | 2,230,000.00 USD | 285,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2065.60` | 438,700,000.00 USD | 438,700,000.00 USD | 1,370,000.00 USD | 537,030.00 USD | 562,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2068.20` | 877,920,000.00 USD | 877,920,000.00 USD | 1,740,000.00 USD | 1,860,000.00 USD | 893,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2068.60` | 436,230,000.00 USD | 436,230,000.00 USD | 57,300.00 USD | 1,330,000.00 USD | 50,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2071.50` | 873,430,000.00 USD | 873,430,000.00 USD | 2,820,000.00 USD | 2,410,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2071.60` | 434,800,000.00 USD | 434,800,000.00 USD | 1,380,000.00 USD | 534,600.00 USD | 444,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2074.60` | 432,430,000.00 USD | 432,430,000.00 USD | 476,310.00 USD | 379,210.00 USD | 937,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2074.80` | 866,960,000.00 USD | 866,960,000.00 USD | 4,370,000.00 USD | 3,270,000.00 USD | 4,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 1,310,000.00 USD | 283,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2077.60` | 430,640,000.00 USD | 430,640,000.00 USD | 3,170,000.00 USD | 1,430,000.00 USD | 2,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2078.10` | 855,270,000.00 USD | 855,270,000.00 USD | 5,560,000.00 USD | 4,320,000.00 USD | 2,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2080.60` | 423,820,000.00 USD | 423,820,000.00 USD | 1,300,000.00 USD | 1,380,000.00 USD | 218,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2081.40` | 842,980,000.00 USD | 842,980,000.00 USD | 4,720,000.00 USD | 3,420,000.00 USD | 2,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2083.60` | 420,910,000.00 USD | 420,910,000.00 USD | 2,480,000.00 USD | 1,420,000.00 USD | 961,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2084.70` | 832,340,000.00 USD | 832,340,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 4,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 4,940,000.00 USD | 281,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2086.60` | 416,060,000.00 USD | 416,060,000.00 USD | 1,670,000.00 USD | 1,680,000.00 USD | 1,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2088.00` | 823,550,000.00 USD | 823,550,000.00 USD | 3,990,000.00 USD | 2,780,000.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2089.60` | 411,250,000.00 USD | 411,250,000.00 USD | 1,320,000.00 USD | 233,840.00 USD | 443,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2091.30` | 815,120,000.00 USD | 815,120,000.00 USD | 4,410,000.00 USD | 952,210.00 USD | 7,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2092.60` | 409,260,000.00 USD | 409,260,000.00 USD | 991,170.00 USD | 527,120.00 USD | 876,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2094.60` | 802,170,000.00 USD | 802,170,000.00 USD | 5,720,000.00 USD | 2,160,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 2,440,000.00 USD | 277,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2095.60` | 406,860,000.00 USD | 406,860,000.00 USD | 2,100,000.00 USD | 1,300,000.00 USD | 1,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2097.90` | 791,950,000.00 USD | 791,950,000.00 USD | 2,340,000.00 USD | 3,210,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2098.60` | 401,490,000.00 USD | 401,490,000.00 USD | 513,870.00 USD | 1,190,000.00 USD | 309,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2101.20` | 785,110,000.00 USD | 785,110,000.00 USD | 999,530.00 USD | 1,580,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2101.60` | 399,480,000.00 USD | 399,480,000.00 USD | 283,960.00 USD | 31,040.00 USD | 478,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2104.50` | 778,510,000.00 USD | 778,510,000.00 USD | 2,010,000.00 USD | 1,180,000.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2104.60` | 398,680,000.00 USD | 398,680,000.00 USD | 957,520.00 USD | 961,080.00 USD | 16,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 1,530,000.00 USD | 274,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2107.60` | 396,750,000.00 USD | 396,750,000.00 USD | 603,300.00 USD | 0.00 USD | 502,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2107.80` | 773,070,000.00 USD | 773,070,000.00 USD | 2,380,000.00 USD | 452,470.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2110.60` | 395,640,000.00 USD | 395,640,000.00 USD | 97,120.00 USD | 31,550.00 USD | 196,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2111.10` | 768,580,000.00 USD | 768,580,000.00 USD | 3,530,000.00 USD | 2,350,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2113.60` | 395,320,000.00 USD | 395,320,000.00 USD | 875,700.00 USD | 643,210.00 USD | 229,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2114.40` | 760,540,000.00 USD | 760,540,000.00 USD | 1,080,000.00 USD | 1,850,000.00 USD | 3,800,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 938,020.00 USD | 273,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2116.60` | 393,570,000.00 USD | 393,570,000.00 USD | 202,840.00 USD | 13,230.00 USD | 521,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2117.70` | 753,810,000.00 USD | 753,810,000.00 USD | 3,430,000.00 USD | 2,020,000.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2119.60` | 392,830,000.00 USD | 392,830,000.00 USD | 15,360.00 USD | 256,720.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2121.00` | 744,970,000.00 USD | 744,970,000.00 USD | 3,650,000.00 USD | 1,340,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2122.60` | 391,450,000.00 USD | 391,450,000.00 USD | 1,220,000.00 USD | 689,080.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2124.30` | 738,160,000.00 USD | 738,160,000.00 USD | 832,850.00 USD | 972,650.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 2,800,000.00 USD | 272,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2125.60` | 388,420,000.00 USD | 388,420,000.00 USD | 714,970.00 USD | 1,500,000.00 USD | 778,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2127.60` | 734,840,000.00 USD | 734,840,000.00 USD | 2,400,000.00 USD | 2,630,000.00 USD | 3,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2128.60` | 385,420,000.00 USD | 385,420,000.00 USD | 116,180.00 USD | 475,750.00 USD | 318,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2130.90` | 726,550,000.00 USD | 726,550,000.00 USD | 2,410,000.00 USD | 2,300,000.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2131.60` | 384,510,000.00 USD | 384,510,000.00 USD | 0.00 USD | 18,610.00 USD | 331,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2134.20` | 720,130,000.00 USD | 720,130,000.00 USD | 2,170,000.00 USD | 550,450.00 USD | 308,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 4,780,000.00 USD | 269,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2137.50` | 717,100,000.00 USD | 717,100,000.00 USD | 1,040,000.00 USD | 880,790.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2137.60` | 384,160,000.00 USD | 384,160,000.00 USD | 0.00 USD | 278,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2140.80` | 715,140,000.00 USD | 715,140,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2144.10` | 711,200,000.00 USD | 711,200,000.00 USD | 449,020.00 USD | 1,130,000.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 26,580,000.00 USD | 264,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2147.40` | 709,360,000.00 USD | 709,360,000.00 USD | 657,710.00 USD | 421,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2150.70` | 708,280,000.00 USD | 708,280,000.00 USD | 459,630.00 USD | 463,640.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2152.60` | 383,880,000.00 USD | 383,880,000.00 USD | 208,250.00 USD | 440,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2154.00` | 707,320,000.00 USD | 707,320,000.00 USD | 128,430.00 USD | 331,520.00 USD | 32,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 2,870,000.00 USD | 237,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2155.60` | 383,230,000.00 USD | 383,230,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2157.30` | 706,830,000.00 USD | 706,830,000.00 USD | 388,210.00 USD | 1,030,000.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2158.60` | 381,840,000.00 USD | 381,840,000.00 USD | 0.00 USD | 0.00 USD | 37,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2160.60` | 704,330,000.00 USD | 704,330,000.00 USD | 646,940.00 USD | 1,900,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2161.60` | 381,800,000.00 USD | 381,800,000.00 USD | 0.00 USD | 3,150,000.00 USD | 71,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2163.90` | 699,790,000.00 USD | 699,790,000.00 USD | 566,120.00 USD | 3,280,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2164.60` | 378,580,000.00 USD | 378,580,000.00 USD | 0.00 USD | 0.00 USD | 107,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 1,870,000.00 USD | 235,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2167.20` | 694,650,000.00 USD | 694,650,000.00 USD | 25,540.00 USD | 3,620,000.00 USD | 50,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2167.60` | 378,470,000.00 USD | 378,470,000.00 USD | 2,340,000.00 USD | 1,700,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2170.50` | 690,950,000.00 USD | 690,950,000.00 USD | 3,500,000.00 USD | 2,380,000.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2170.60` | 374,430,000.00 USD | 374,430,000.00 USD | 5,020,000.00 USD | 3,070,000.00 USD | 873,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2173.60` | 365,460,000.00 USD | 365,460,000.00 USD | 0.00 USD | 190,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2173.80` | 683,240,000.00 USD | 683,240,000.00 USD | 4,110,000.00 USD | 363,040.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 110,260,000.00 USD | 233,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2176.60` | 365,270,000.00 USD | 365,270,000.00 USD | 345,940.00 USD | 1,510,000.00 USD | 35,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2179.60` | 363,380,000.00 USD | 363,380,000.00 USD | 2,080,000.00 USD | 0.00 USD | 706,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2180.40` | 677,760,000.00 USD | 677,760,000.00 USD | 0.00 USD | 373,740.00 USD | 176,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2182.60` | 360,600,000.00 USD | 360,600,000.00 USD | 0.00 USD | 478,110.00 USD | 679,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2183.70` | 677,210,000.00 USD | 677,210,000.00 USD | 0.00 USD | 1,310,000.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2185.00` | 101,640,000.00 USD | 122,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2185.60` | 359,440,000.00 USD | 359,440,000.00 USD | 1,350,000.00 USD | 1,960,000.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2187.00` | 673,360,000.00 USD | 673,360,000.00 USD | 556,600.00 USD | 0.00 USD | 54,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2188.60` | 354,330,000.00 USD | 354,330,000.00 USD | 0.00 USD | 0.00 USD | 693,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2190.30` | 672,750,000.00 USD | 672,750,000.00 USD | 2,730,000.00 USD | 0.00 USD | 4,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2191.60` | 353,640,000.00 USD | 353,640,000.00 USD | 0.00 USD | 222,200.00 USD | 109,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2194.60` | 353,310,000.00 USD | 353,310,000.00 USD | 605,210.00 USD | 881,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 7,900,000.00 USD | 21,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2196.90` | 665,820,000.00 USD | 665,820,000.00 USD | 2,580,000.00 USD | 474,090.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2197.60` | 351,820,000.00 USD | 351,820,000.00 USD | 416,500.00 USD | 0.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2200.20` | 660,720,000.00 USD | 660,720,000.00 USD | 3,000,000.00 USD | 5,080,000.00 USD | 3,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2200.60` | 349,520,000.00 USD | 349,520,000.00 USD | 284,470.00 USD | 3,230,000.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2203.50` | 649,450,000.00 USD | 649,450,000.00 USD | 3,650,000.00 USD | 1,710,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2203.60` | 344,450,000.00 USD | 344,450,000.00 USD | 3,540,000.00 USD | 1,280,000.00 USD | 830,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 1,760,000.00 USD | 13,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2206.60` | 338,810,000.00 USD | 338,810,000.00 USD | 2,210,000.00 USD | 10,890,000.00 USD | 1,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2206.80` | 640,340,000.00 USD | 640,340,000.00 USD | 6,920,000.00 USD | 9,430,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2209.60` | 323,740,000.00 USD | 323,740,000.00 USD | 1,890,000.00 USD | 2,010,000.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2210.10` | 619,960,000.00 USD | 619,960,000.00 USD | 12,800,000.00 USD | 20,410,000.00 USD | 6,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2212.60` | 317,640,000.00 USD | 317,640,000.00 USD | 7,820,000.00 USD | 5,240,000.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2213.40` | 580,290,000.00 USD | 580,290,000.00 USD | 10,920,000.00 USD | 11,890,000.00 USD | 13,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 4,410,000.00 USD | 11,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2215.60` | 301,750,000.00 USD | 301,750,000.00 USD | 18,260,000.00 USD | 11,500,000.00 USD | 7,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2216.70` | 544,310,000.00 USD | 544,310,000.00 USD | 25,210,000.00 USD | 17,030,000.00 USD | 9,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2218.60` | 264,430,000.00 USD | 264,430,000.00 USD | 7,700,000.00 USD | 8,360,000.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2220.00` | 492,680,000.00 USD | 492,680,000.00 USD | 24,310,000.00 USD | 12,300,000.00 USD | 10,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2221.60` | 246,420,000.00 USD | 246,420,000.00 USD | 6,250,000.00 USD | 13,160,000.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2223.30` | 445,950,000.00 USD | 445,950,000.00 USD | 10,150,000.00 USD | 8,220,000.00 USD | 11,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2224.60` | 225,670,000.00 USD | 225,670,000.00 USD | 9,730,000.00 USD | 5,030,000.00 USD | 6,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2225.00` | 5,180,000.00 USD | 7,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2226.60` | 415,670,000.00 USD | 415,670,000.00 USD | 12,840,000.00 USD | 11,030,000.00 USD | 9,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2227.60` | 204,800,000.00 USD | 204,800,000.00 USD | 6,230,000.00 USD | 13,340,000.00 USD | 5,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2229.90` | 381,850,000.00 USD | 381,850,000.00 USD | 12,730,000.00 USD | 11,790,000.00 USD | 25,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2230.60` | 180,090,000.00 USD | 180,090,000.00 USD | 7,100,000.00 USD | 8,290,000.00 USD | 2,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2233.20` | 331,570,000.00 USD | 331,570,000.00 USD | 16,600,000.00 USD | 24,290,000.00 USD | 10,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2233.60` | 161,860,000.00 USD | 161,860,000.00 USD | 6,140,000.00 USD | 3,540,000.00 USD | 8,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2235.00` | 1,910,000.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2236.50` | 280,250,000.00 USD | 280,250,000.00 USD | 16,050,000.00 USD | 2,010,000.00 USD | 14,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2236.60` | 143,660,000.00 USD | 143,660,000.00 USD | 18,680,000.00 USD | 0.00 USD | 5,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2239.60` | 119,070,000.00 USD | 119,070,000.00 USD | 16,010,000.00 USD | 4,410,000.00 USD | 4,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2239.80` | 247,980,000.00 USD | 247,980,000.00 USD | 15,710,000.00 USD | 6,600,000.00 USD | 13,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2242.60` | 94,460,000.00 USD | 94,460,000.00 USD | 2,540,000.00 USD | 760,920.00 USD | 5,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2243.10` | 211,920,000.00 USD | 211,920,000.00 USD | 22,920,000.00 USD | 0.00 USD | 13,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2245.00` | 160,900.00 USD | 179,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2245.60` | 85,840,000.00 USD | 85,840,000.00 USD | 1,910,000.00 USD | 4,700,000.00 USD | 940,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2246.40` | 175,950,000.00 USD | 175,950,000.00 USD | 14,340,000.00 USD | 0.00 USD | 13,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2248.60` | 78,280,000.00 USD | 78,280,000.00 USD | 15,010,000.00 USD | 22,790.00 USD | 10,470,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2249.70` | 147,690,000.00 USD | 147,690,000.00 USD | 18,000,000.00 USD | 0.00 USD | 12,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2251.60` | 52,770,000.00 USD | 52,770,000.00 USD | 7,080,000.00 USD | 2,400,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2253.00` | 116,870,000.00 USD | 116,870,000.00 USD | 26,890,000.00 USD | 5,220,000.00 USD | 28,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2254.60` | 41,590,000.00 USD | 41,590,000.00 USD | 0.00 USD | 7,830,000.00 USD | 12,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2255.00` | 18,560.00 USD | 18,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2256.30` | 56,630,000.00 USD | 56,630,000.00 USD | 17,450,000.00 USD | 0.00 USD | 8,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2257.60` | 21,170,000.00 USD | 21,170,000.00 USD | 0.00 USD | 0.00 USD | 2,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2259.60` | 31,000,000.00 USD | 31,000,000.00 USD | 10,940,000.00 USD | 0.00 USD | 11,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2260.60` | 18,390,000.00 USD | 18,390,000.00 USD | 2,420,000.00 USD | 0.00 USD | 156,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2263.60` | 15,820,000.00 USD | 15,820,000.00 USD | 0.00 USD | 0.00 USD | 7,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2265.00` | 7,250.00 USD | 7,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2266.20` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 0.00 USD | 8,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2266.60` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 0.00 USD | 4,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2269.60` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 1,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2272.60` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 287,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2275.00` | 48,600.00 USD | 55,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2275.60` | 1,150,000.00 USD | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2278.60` | 7,540,000.00 USD | 7,540,000.00 USD | 5,740,000.00 USD | 1,360,000.00 USD | 431,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2279.40` | 17,000,000.00 USD | 17,000,000.00 USD | 0.00 USD | 17,000,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2281.60` | 73,490,000.00 USD | 73,490,000.00 USD | 39,500,000.00 USD | 26,450,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2282.70` | 98,670,000.00 USD | 98,670,000.00 USD | 0.00 USD | 81,670,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2284.60` | 132,910,000.00 USD | 132,910,000.00 USD | 32,760,000.00 USD | 19,370,000.00 USD | 7,290,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2285.00` | 6,220,000.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2286.00` | 108,070,000.00 USD | 108,070,000.00 USD | 0.00 USD | 9,400,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2287.60` | 133,670,000.00 USD | 133,670,000.00 USD | 0.00 USD | 760,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2290.60` | 142,650,000.00 USD | 142,650,000.00 USD | 0.00 USD | 8,840,000.00 USD | 143,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2293.60` | 156,580,000.00 USD | 156,580,000.00 USD | 8,310,000.00 USD | 0.00 USD | 5,620,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2295.00` | 12,310.00 USD | 6,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2295.90` | 122,750,000.00 USD | 122,750,000.00 USD | 6,580,000.00 USD | 2,380,000.00 USD | 5,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2296.60` | 170,340,000.00 USD | 170,340,000.00 USD | 5,410,000.00 USD | 8,210,000.00 USD | 143,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2299.20` | 151,170,000.00 USD | 151,170,000.00 USD | 11,730,000.00 USD | 11,130,000.00 USD | 5,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2299.60` | 185,470,000.00 USD | 185,470,000.00 USD | 0.00 USD | 7,840,000.00 USD | 7,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2302.50` | 198,290,000.00 USD | 198,290,000.00 USD | 23,020,000.00 USD | 7,250,000.00 USD | 16,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2302.60` | 202,170,000.00 USD | 202,170,000.00 USD | 13,040,000.00 USD | 682,490.00 USD | 2,970,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2305.00` | 1,210,000.00 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2305.60` | 228,530,000.00 USD | 228,530,000.00 USD | 10,050,000.00 USD | 14,130,000.00 USD | 2,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2305.80` | 209,580,000.00 USD | 209,580,000.00 USD | 2,980,000.00 USD | 6,110,000.00 USD | 2,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2308.60` | 233,290,000.00 USD | 233,290,000.00 USD | 2,420,000.00 USD | 2,340,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2309.10` | 213,350,000.00 USD | 213,350,000.00 USD | 732,090.00 USD | 930,630.00 USD | 2,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2311.60` | 242,870,000.00 USD | 242,870,000.00 USD | 691,870.00 USD | 1,260,000.00 USD | 7,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2312.40` | 228,850,000.00 USD | 228,850,000.00 USD | 7,270,000.00 USD | 0.00 USD | 8,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2314.60` | 257,200,000.00 USD | 257,200,000.00 USD | 0.00 USD | 14,100,000.00 USD | 231,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2315.00` | 4,720,000.00 USD | 12,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2315.70` | 236,420,000.00 USD | 236,420,000.00 USD | 0.00 USD | 7,460,000.00 USD | 117,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2317.60` | 285,740,000.00 USD | 285,740,000.00 USD | 10,230,000.00 USD | 10,470,000.00 USD | 7,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2319.00` | 245,030,000.00 USD | 245,030,000.00 USD | 1,020,000.00 USD | 4,550,000.00 USD | 3,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2320.60` | 301,830,000.00 USD | 301,830,000.00 USD | 6,580,000.00 USD | 9,360,000.00 USD | 147,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2322.30` | 264,770,000.00 USD | 264,770,000.00 USD | 1,110,000.00 USD | 15,930,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2323.60` | 316,400,000.00 USD | 316,400,000.00 USD | 572,970.00 USD | 10,410,000.00 USD | 3,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2325.00` | 134,130.00 USD | 12,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2325.60` | 285,420,000.00 USD | 285,420,000.00 USD | 9,720,000.00 USD | 2,540,000.00 USD | 8,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2326.60` | 328,490,000.00 USD | 328,490,000.00 USD | 735,700.00 USD | 5,550,000.00 USD | 5,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2328.90` | 297,240,000.00 USD | 297,240,000.00 USD | 3,860,000.00 USD | 0.00 USD | 7,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2329.60` | 339,400,000.00 USD | 339,400,000.00 USD | 9,740,000.00 USD | 884,940.00 USD | 281,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2332.20` | 326,480,000.00 USD | 326,480,000.00 USD | 29,230,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2332.60` | 355,440,000.00 USD | 355,440,000.00 USD | 11,910,000.00 USD | 251,940.00 USD | 3,880,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2335.00` | 343,060.00 USD | 12,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2335.50` | 384,490,000.00 USD | 384,490,000.00 USD | 28,990,000.00 USD | 18,420,000.00 USD | 10,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2335.60` | 381,480,000.00 USD | 381,480,000.00 USD | 17,120,000.00 USD | 3,360,000.00 USD | 5,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2338.60` | 396,810,000.00 USD | 396,810,000.00 USD | 8,670,000.00 USD | 2,600,000.00 USD | 4,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2338.80` | 402,360,000.00 USD | 402,360,000.00 USD | 9,570,000.00 USD | 0.00 USD | 8,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2341.60` | 417,170,000.00 USD | 417,170,000.00 USD | 7,140,000.00 USD | 3,360,000.00 USD | 9,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2342.10` | 442,460,000.00 USD | 442,460,000.00 USD | 4,720,000.00 USD | 21,390,000.00 USD | 14,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2344.60` | 433,410,000.00 USD | 433,410,000.00 USD | 1,370,000.00 USD | 6,180,000.00 USD | 8,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2345.00` | 597,120.00 USD | 13,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2345.40` | 463,840,000.00 USD | 463,840,000.00 USD | 1,350,000.00 USD | 13,990,000.00 USD | 6,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2347.60` | 442,350,000.00 USD | 442,350,000.00 USD | 3,300,000.00 USD | 3,010,000.00 USD | 2,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2348.70` | 496,970,000.00 USD | 496,970,000.00 USD | 847,620.00 USD | 8,140,000.00 USD | 24,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2350.60` | 491,530,000.00 USD | 491,530,000.00 USD | 33,010,000.00 USD | 7,320,000.00 USD | 8,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2352.00` | 533,590,000.00 USD | 533,590,000.00 USD | 2,930,000.00 USD | 23,060,000.00 USD | 10,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2353.60` | 506,450,000.00 USD | 506,450,000.00 USD | 4,400,000.00 USD | 9,300,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 3,250,000.00 USD | 16,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2355.30` | 588,190,000.00 USD | 588,190,000.00 USD | 16,520,000.00 USD | 36,690,000.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2356.60` | 523,620,000.00 USD | 523,620,000.00 USD | 3,480,000.00 USD | 11,210,000.00 USD | 2,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2358.60` | 599,000,000.00 USD | 599,000,000.00 USD | 7,110,000.00 USD | 512,220.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2359.60` | 544,150,000.00 USD | 544,150,000.00 USD | 6,360,000.00 USD | 6,900,000.00 USD | 7,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2361.90` | 606,130,000.00 USD | 606,130,000.00 USD | 3,150,000.00 USD | 3,800,000.00 USD | 176,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2362.60` | 569,530,000.00 USD | 569,530,000.00 USD | 10,730,000.00 USD | 6,710,000.00 USD | 7,940,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 47,670.00 USD | 16,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2365.20` | 624,030,000.00 USD | 624,030,000.00 USD | 8,440,000.00 USD | 0.00 USD | 9,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2365.60` | 580,000,000.00 USD | 580,000,000.00 USD | 3,290,000.00 USD | 4,700,000.00 USD | 2,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2368.50` | 637,090,000.00 USD | 637,090,000.00 USD | 10,830,000.00 USD | 1,780,000.00 USD | 458,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2368.60` | 596,770,000.00 USD | 596,770,000.00 USD | 8,810,000.00 USD | 4,420,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2371.60` | 639,070,000.00 USD | 639,070,000.00 USD | 17,650,000.00 USD | 13,840,000.00 USD | 10,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2371.80` | 718,030,000.00 USD | 718,030,000.00 USD | 26,000,000.00 USD | 0.00 USD | 54,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2374.60` | 659,590,000.00 USD | 659,590,000.00 USD | 14,820,000.00 USD | 709,900.00 USD | 4,990,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 1,040,000.00 USD | 17,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2375.10` | 744,980,000.00 USD | 744,980,000.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2377.60` | 687,370,000.00 USD | 687,370,000.00 USD | 7,850,000.00 USD | 8,860,000.00 USD | 11,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2378.40` | 790,390,000.00 USD | 790,390,000.00 USD | 11,800,000.00 USD | 7,950,000.00 USD | 25,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2380.60` | 732,090,000.00 USD | 732,090,000.00 USD | 12,710,000.00 USD | 14,110,000.00 USD | 17,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2381.70` | 830,180,000.00 USD | 830,180,000.00 USD | 8,510,000.00 USD | 6,750,000.00 USD | 24,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2383.60` | 786,450,000.00 USD | 786,450,000.00 USD | 24,510,000.00 USD | 15,290,000.00 USD | 14,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2385.00` | 931,900,000.00 USD | 931,900,000.00 USD | 18,550,000.00 USD | 36,910,000.00 USD | 46,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 610,200.00 USD | 18,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2386.60` | 823,450,000.00 USD | 823,450,000.00 USD | 12,470,000.00 USD | 12,790,000.00 USD | 11,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2388.30` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 5,290,000.00 USD | 38,070,000.00 USD | 44,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2389.60` | 850,210,000.00 USD | 850,210,000.00 USD | 11,290,000.00 USD | 9,340,000.00 USD | 6,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2391.60` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 8,560,000.00 USD | 52,080,000.00 USD | 40,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2392.60` | 867,540,000.00 USD | 867,540,000.00 USD | 5,650,000.00 USD | 4,340,000.00 USD | 7,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2394.90` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 57,450,000.00 USD | 32,260,000.00 USD | 37,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 823,610.00 USD | 19,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2395.60` | 883,750,000.00 USD | 883,750,000.00 USD | 5,260,000.00 USD | 7,330,000.00 USD | 3,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2398.20` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 42,820,000.00 USD | 38,210,000.00 USD | 29,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2398.60` | 907,260,000.00 USD | 907,260,000.00 USD | 6,440,000.00 USD | 7,340,000.00 USD | 9,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2401.50` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 51,970,000.00 USD | 26,780,000.00 USD | 29,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2401.60` | 928,820,000.00 USD | 928,820,000.00 USD | 7,630,000.00 USD | 7,320,000.00 USD | 6,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2404.60` | 962,450,000.00 USD | 962,450,000.00 USD | 11,940,000.00 USD | 10,820,000.00 USD | 10,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2404.80` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 50,800,000.00 USD | 32,200,000.00 USD | 24,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 1,640,000.00 USD | 20,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2407.60` | 995,530,000.00 USD | 995,530,000.00 USD | 16,380,000.00 USD | 9,710,000.00 USD | 7,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2408.10` | 1,660,000,000.00 USD | 1,660,000,000.00 USD | 34,390,000.00 USD | 31,420,000.00 USD | 25,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2410.60` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 6,060,000.00 USD | 7,690,000.00 USD | 8,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2411.40` | 1,740,000,000.00 USD | 1,740,000,000.00 USD | 19,200,000.00 USD | 32,580,000.00 USD | 27,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2413.60` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 8,520,000.00 USD | 5,520,000.00 USD | 3,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2414.70` | 1,810,000,000.00 USD | 1,810,000,000.00 USD | 24,010,000.00 USD | 21,950,000.00 USD | 23,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 51,630.00 USD | 20,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2416.60` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 4,510,000.00 USD | 3,390,000.00 USD | 5,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2418.00` | 1,890,000,000.00 USD | 1,890,000,000.00 USD | 34,060,000.00 USD | 15,260,000.00 USD | 24,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2419.60` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 6,750,000.00 USD | 4,200,000.00 USD | 3,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2421.30` | 1,960,000,000.00 USD | 1,960,000,000.00 USD | 25,700,000.00 USD | 27,890,000.00 USD | 21,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2422.60` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 2,930,000.00 USD | 4,220,000.00 USD | 5,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.60` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 24,180,000.00 USD | 35,050,000.00 USD | 34,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 334,040.00 USD | 21,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2425.60` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 1,810,000.00 USD | 2,260,000.00 USD | 844,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2427.90` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 25,200,000.00 USD | 18,380,000.00 USD | 26,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2428.60` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 754,820.00 USD | 897,420.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2431.20` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 10,380,000.00 USD | 18,750,000.00 USD | 9,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2431.60` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 2,910,000.00 USD | 2,570,000.00 USD | 369,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2434.50` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 27,390,000.00 USD | 21,570,000.00 USD | 11,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2434.60` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 1,670,000.00 USD | 468,310.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 4,610,000.00 USD | 25,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2437.60` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 1,200,000.00 USD | 531,390.00 USD | 205,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2437.80` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 12,000,000.00 USD | 12,820,000.00 USD | 5,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2440.60` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 1,540,000.00 USD | 2,040,000.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2441.10` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 15,080,000.00 USD | 8,120,000.00 USD | 10,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2443.60` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 1,050,000.00 USD | 1,060,000.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2444.40` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 8,860,000.00 USD | 15,160,000.00 USD | 14,000,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 130,990.00 USD | 25,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2446.60` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 648,280.00 USD | 347,060.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2447.70` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 11,650,000.00 USD | 8,510,000.00 USD | 17,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2449.60` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 651,910.00 USD | 1,290,000.00 USD | 2,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2451.00` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 16,710,000.00 USD | 14,100,000.00 USD | 16,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2452.60` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 4,030,000.00 USD | 2,370,000.00 USD | 4,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2454.30` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 4,620,000.00 USD | 5,780,000.00 USD | 3,880,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 516,490.00 USD | 26,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2455.60` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 4,380,000.00 USD | 3,050,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2457.60` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 15,150,000.00 USD | 12,540,000.00 USD | 12,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2458.60` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 1,430,000.00 USD | 2,640,000.00 USD | 890,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2460.90` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 5,580,000.00 USD | 8,670,000.00 USD | 6,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2461.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 470,530.00 USD | 490,260.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2464.20` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 8,720,000.00 USD | 7,700,000.00 USD | 4,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2464.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 83,300.00 USD | 176,210.00 USD | 829,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 759,490.00 USD | 27,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2467.50` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 4,540,000.00 USD | 3,710,000.00 USD | 586,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2467.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 68,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2470.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 1,190,000.00 USD | 391,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2470.80` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 3,960,000.00 USD | 2,290,000.00 USD | 522,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2474.10` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 5,230,000.00 USD | 2,920,000.00 USD | 2,400,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 534,310.00 USD | 27,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2476.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 914,780.00 USD | 28,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2477.40` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 1,660,000.00 USD | 4,420,000.00 USD | 718,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2480.70` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 2,110,000.00 USD | 4,170,000.00 USD | 540,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2482.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 239,600.00 USD | 136,500.00 USD | 43,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2484.00` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 1,210,000.00 USD | 1,390,000.00 USD | 77,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 2,190,000.00 USD | 29,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2485.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 865,140.00 USD | 1,330,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2487.30` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 325,140.00 USD | 262,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2488.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 866,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2490.60` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 2,910,000.00 USD | 2,540,000.00 USD | 279,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2491.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 138,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2493.90` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 1,660,000.00 USD | 1,790,000.00 USD | 3,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2494.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 178,560.00 USD | 14,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 4,730,000.00 USD | 34,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2497.20` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 2,940,000.00 USD | 5,270,000.00 USD | 8,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2500.50` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 1,110,000.00 USD | 2,280,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2503.80` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 63,860.00 USD | 1,900,000.00 USD | 125,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 660,180.00 USD | 35,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2506.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2507.10` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 4,340,000.00 USD | 3,090,000.00 USD | 3,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2509.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2510.40` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 2,290,000.00 USD | 1,270,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2512.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 242,080.00 USD | 88,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2513.70` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 98,210.00 USD | 35,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2515.60` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2517.00` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 97,050.00 USD | 189,640.00 USD | 815,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2520.30` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2521.60` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 113,940.00 USD | 173,370.00 USD | 620,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2523.60` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2524.60` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 1,340,000.00 USD | 485,130.00 USD | 30,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 544,410.00 USD | 35,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2526.90` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2527.60` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 1,010,000.00 USD | 50,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2530.20` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 2,800,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2530.60` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 1,050,000.00 USD | 319,490.00 USD | 437,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2533.50` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 3,530,000.00 USD | 1,850,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2533.60` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 442,230.00 USD | 597,240.00 USD | 436,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2535.00` | 931,980.00 USD | 36,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2536.60` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 1,600,000.00 USD | 656,520.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2536.80` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 3,720,000.00 USD | 3,450,000.00 USD | 3,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2539.60` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 2,030,000.00 USD | 1,090,000.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2540.10` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 4,150,000.00 USD | 3,220,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2542.60` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 1,270,000.00 USD | 1,360,000.00 USD | 218,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2543.40` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 4,150,000.00 USD | 2,520,000.00 USD | 2,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2545.00` | 15,790,000.00 USD | 52,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2545.60` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 1,450,000.00 USD | 848,320.00 USD | 215,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2546.70` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 1,450,000.00 USD | 1,090,000.00 USD | 2,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2548.60` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 1,630,000.00 USD | 1,300,000.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2550.00` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 4,320,000.00 USD | 3,550,000.00 USD | 3,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2551.60` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 1,480,000.00 USD | 988,750.00 USD | 698,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2553.30` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 2,820,000.00 USD | 788,360.00 USD | 2,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2554.60` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 1,360,000.00 USD | 225,190.00 USD | 238,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2555.00` | 427,790.00 USD | 53,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2556.60` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 2,760,000.00 USD | 283,560.00 USD | 6,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2557.60` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 533,960.00 USD | 522,240.00 USD | 874,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2559.90` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 5,720,000.00 USD | 2,130,000.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2560.60` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 2,100,000.00 USD | 1,120,000.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2563.20` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 1,430,000.00 USD | 2,900,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2563.60` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 463,350.00 USD | 1,170,000.00 USD | 984,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2565.00` | 2,460,000.00 USD | 55,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2566.50` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 1,860,000.00 USD | 1,830,000.00 USD | 3,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2566.60` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 172,210.00 USD | 232,250.00 USD | 15,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2569.60` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 507,510.00 USD | 289,160.00 USD | 462,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2569.80` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 125,250.00 USD | 341,900.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2572.60` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 612,280.00 USD | 671,930.00 USD | 22,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2573.10` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2575.00` | 11,610,000.00 USD | 67,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2575.60` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 546,100.00 USD | 0.00 USD | 496,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2576.40` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 2,400,000.00 USD | 930,280.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2578.60` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 118,210.00 USD | 31,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2579.70` | 2,730,000,000.00 USD | 2,730,000,000.00 USD | 2,750,000.00 USD | 1,780,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2580.60` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 414,360.00 USD | 126,990.00 USD | 188,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2583.00` | 2,730,000,000.00 USD | 2,730,000,000.00 USD | 1,730,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2585.00` | 39,190,000.00 USD | 106,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2586.30` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 1,480,000.00 USD | 2,030,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2589.60` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 3,310,000.00 USD | 631,590.00 USD | 2,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2592.90` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 2,370,000.00 USD | 1,280,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2595.00` | 657,040.00 USD | 106,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2596.20` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 794,750.00 USD | 620,840.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2599.50` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 2,380,000.00 USD | 2,530,000.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2602.80` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 1,680,000.00 USD | 1,260,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2605.00` | 8,050,000.00 USD | 115,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2606.10` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 1,850,000.00 USD | 1,560,000.00 USD | 772,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2609.40` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2612.70` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 1,010,000.00 USD | 643,740.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2615.00` | 6,310,000.00 USD | 121,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2616.00` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2619.30` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 449,020.00 USD | 323,810.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2622.60` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 631,440.00 USD | 1,220,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2625.00` | 377,520.00 USD | 121,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2625.90` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 485,890.00 USD | 474,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2629.20` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 0.00 USD | 20,460.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2632.40` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 0.00 USD | 301,060.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `1D` | `2017.60` | 446,740,000.00 USD | 0.00 USD | 446,740,000.00 USD | 83,300.00 USD | 176,210.00 USD | 0.00 USD |
| `1D` | `2020.60` | 446,480,000.00 USD | 0.00 USD | 446,480,000.00 USD | 0.00 USD | 558,730.00 USD | 0.00 USD |
| `7D` | `2025.30` | 893,380,000.00 USD | 0.00 USD | 893,380,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD |
| `1D` | `2026.60` | 445,920,000.00 USD | 0.00 USD | 445,920,000.00 USD | 0.00 USD | 914,780.00 USD | 28,770.00 USD |
| `7D` | `2028.60` | 893,210,000.00 USD | 0.00 USD | 893,210,000.00 USD | 0.00 USD | 1,180,000.00 USD | 35,180.00 USD |
| `1D` | `2029.60` | 444,980,000.00 USD | 0.00 USD | 444,980,000.00 USD | 87,180.00 USD | 136,500.00 USD | 43,160.00 USD |
| `7D` | `2031.90` | 891,990,000.00 USD | 0.00 USD | 891,990,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD |
| `1D` | `2032.60` | 444,710,000.00 USD | 0.00 USD | 444,710,000.00 USD | 850,010.00 USD | 1,330,000.00 USD | 0.00 USD |
| `7D` | `2035.20` | 890,540,000.00 USD | 0.00 USD | 890,540,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD |
| `1D` | `2035.60` | 442,530,000.00 USD | 0.00 USD | 442,530,000.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2038.50` | 890,210,000.00 USD | 0.00 USD | 890,210,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2038.60` | 441,500,000.00 USD | 0.00 USD | 441,500,000.00 USD | 138,370.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2041.60` | 441,360,000.00 USD | 0.00 USD | 441,360,000.00 USD | 0.00 USD | 178,560.00 USD | 14,300.00 USD |
| `7D` | `2045.10` | 888,750,000.00 USD | 0.00 USD | 888,750,000.00 USD | 0.00 USD | 149,500.00 USD | 47,970.00 USD |
| `1D` | `2050.60` | 441,160,000.00 USD | 0.00 USD | 441,160,000.00 USD | 0.00 USD | 338,980.00 USD | 717,780.00 USD |
| `7D` | `2051.70` | 888,560,000.00 USD | 0.00 USD | 888,560,000.00 USD | 1,320,000.00 USD | 0.00 USD | 1,190,000.00 USD |
| `1D` | `2053.60` | 440,110,000.00 USD | 0.00 USD | 440,110,000.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD |
| `1D` | `2056.60` | 439,990,000.00 USD | 0.00 USD | 439,990,000.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2058.30` | 886,050,000.00 USD | 0.00 USD | 886,050,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD |
| `1D` | `2059.60` | 439,750,000.00 USD | 0.00 USD | 439,750,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `7D` | `2061.60` | 885,710,000.00 USD | 0.00 USD | 885,710,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD |
| `1D` | `2062.60` | 438,990,000.00 USD | 0.00 USD | 438,990,000.00 USD | 80,610.00 USD | 121,470.00 USD | 88,290.00 USD |
| `7D` | `2064.90` | 880,450,000.00 USD | 0.00 USD | 880,450,000.00 USD | 1,230,000.00 USD | 313,000.00 USD | 979,910.00 USD |
| `1D` | `2065.60` | 438,700,000.00 USD | 0.00 USD | 438,700,000.00 USD | 1,370,000.00 USD | 537,030.00 USD | 562,550.00 USD |
| `7D` | `2068.20` | 877,920,000.00 USD | 0.00 USD | 877,920,000.00 USD | 1,740,000.00 USD | 1,860,000.00 USD | 893,570.00 USD |
| `1D` | `2068.60` | 436,230,000.00 USD | 0.00 USD | 436,230,000.00 USD | 57,300.00 USD | 1,330,000.00 USD | 50,470.00 USD |
| `7D` | `2071.50` | 873,430,000.00 USD | 0.00 USD | 873,430,000.00 USD | 2,820,000.00 USD | 2,410,000.00 USD | 1,230,000.00 USD |
| `1D` | `2071.60` | 434,800,000.00 USD | 0.00 USD | 434,800,000.00 USD | 1,380,000.00 USD | 534,600.00 USD | 444,600.00 USD |
| `1D` | `2074.60` | 432,430,000.00 USD | 0.00 USD | 432,430,000.00 USD | 476,310.00 USD | 379,210.00 USD | 937,120.00 USD |
| `7D` | `2074.80` | 866,960,000.00 USD | 0.00 USD | 866,960,000.00 USD | 4,370,000.00 USD | 3,270,000.00 USD | 4,050,000.00 USD |
| `1D` | `2077.60` | 430,640,000.00 USD | 0.00 USD | 430,640,000.00 USD | 3,170,000.00 USD | 1,430,000.00 USD | 2,220,000.00 USD |
| `7D` | `2078.10` | 855,270,000.00 USD | 0.00 USD | 855,270,000.00 USD | 5,560,000.00 USD | 4,320,000.00 USD | 2,410,000.00 USD |
| `1D` | `2080.60` | 423,820,000.00 USD | 0.00 USD | 423,820,000.00 USD | 1,300,000.00 USD | 1,380,000.00 USD | 218,810.00 USD |
| `7D` | `2081.40` | 842,980,000.00 USD | 0.00 USD | 842,980,000.00 USD | 4,720,000.00 USD | 3,420,000.00 USD | 2,500,000.00 USD |
| `1D` | `2083.60` | 420,910,000.00 USD | 0.00 USD | 420,910,000.00 USD | 2,480,000.00 USD | 1,420,000.00 USD | 961,180.00 USD |
| `7D` | `2084.70` | 832,340,000.00 USD | 0.00 USD | 832,340,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 4,900,000.00 USD |
| `1D` | `2086.60` | 416,060,000.00 USD | 0.00 USD | 416,060,000.00 USD | 1,670,000.00 USD | 1,680,000.00 USD | 1,460,000.00 USD |
| `7D` | `2088.00` | 823,550,000.00 USD | 0.00 USD | 823,550,000.00 USD | 3,990,000.00 USD | 2,780,000.00 USD | 1,650,000.00 USD |
| `1D` | `2089.60` | 411,250,000.00 USD | 0.00 USD | 411,250,000.00 USD | 1,320,000.00 USD | 233,840.00 USD | 443,560.00 USD |
| `7D` | `2091.30` | 815,120,000.00 USD | 0.00 USD | 815,120,000.00 USD | 4,410,000.00 USD | 952,210.00 USD | 7,590,000.00 USD |
| `1D` | `2092.60` | 409,260,000.00 USD | 0.00 USD | 409,260,000.00 USD | 991,170.00 USD | 527,120.00 USD | 876,790.00 USD |
| `7D` | `2094.60` | 802,170,000.00 USD | 0.00 USD | 802,170,000.00 USD | 5,720,000.00 USD | 2,160,000.00 USD | 2,340,000.00 USD |
| `1D` | `2095.60` | 406,860,000.00 USD | 0.00 USD | 406,860,000.00 USD | 2,100,000.00 USD | 1,300,000.00 USD | 1,970,000.00 USD |
| `7D` | `2097.90` | 791,950,000.00 USD | 0.00 USD | 791,950,000.00 USD | 2,340,000.00 USD | 3,210,000.00 USD | 1,290,000.00 USD |
| `1D` | `2098.60` | 401,490,000.00 USD | 0.00 USD | 401,490,000.00 USD | 513,870.00 USD | 1,190,000.00 USD | 309,770.00 USD |
| `7D` | `2101.20` | 785,110,000.00 USD | 0.00 USD | 785,110,000.00 USD | 999,530.00 USD | 1,580,000.00 USD | 4,020,000.00 USD |
| `1D` | `2101.60` | 399,480,000.00 USD | 0.00 USD | 399,480,000.00 USD | 283,960.00 USD | 31,040.00 USD | 478,590.00 USD |
| `7D` | `2104.50` | 778,510,000.00 USD | 0.00 USD | 778,510,000.00 USD | 2,010,000.00 USD | 1,180,000.00 USD | 2,250,000.00 USD |
| `1D` | `2104.60` | 398,680,000.00 USD | 0.00 USD | 398,680,000.00 USD | 957,520.00 USD | 961,080.00 USD | 16,280.00 USD |
| `1D` | `2107.60` | 396,750,000.00 USD | 0.00 USD | 396,750,000.00 USD | 603,300.00 USD | 0.00 USD | 502,840.00 USD |
| `7D` | `2107.80` | 773,070,000.00 USD | 0.00 USD | 773,070,000.00 USD | 2,380,000.00 USD | 452,470.00 USD | 1,650,000.00 USD |
| `1D` | `2110.60` | 395,640,000.00 USD | 0.00 USD | 395,640,000.00 USD | 97,120.00 USD | 31,550.00 USD | 196,840.00 USD |
| `7D` | `2111.10` | 768,580,000.00 USD | 0.00 USD | 768,580,000.00 USD | 3,530,000.00 USD | 2,350,000.00 USD | 2,170,000.00 USD |
| `1D` | `2113.60` | 395,320,000.00 USD | 0.00 USD | 395,320,000.00 USD | 875,700.00 USD | 643,210.00 USD | 229,680.00 USD |
| `7D` | `2114.40` | 760,540,000.00 USD | 0.00 USD | 760,540,000.00 USD | 1,080,000.00 USD | 1,850,000.00 USD | 3,800,000.00 USD |
| `1D` | `2116.60` | 393,570,000.00 USD | 0.00 USD | 393,570,000.00 USD | 202,840.00 USD | 13,230.00 USD | 521,440.00 USD |
| `7D` | `2117.70` | 753,810,000.00 USD | 0.00 USD | 753,810,000.00 USD | 3,430,000.00 USD | 2,020,000.00 USD | 3,380,000.00 USD |
| `1D` | `2119.60` | 392,830,000.00 USD | 0.00 USD | 392,830,000.00 USD | 15,360.00 USD | 256,720.00 USD | 1,110,000.00 USD |
| `7D` | `2121.00` | 744,970,000.00 USD | 0.00 USD | 744,970,000.00 USD | 3,650,000.00 USD | 1,340,000.00 USD | 1,820,000.00 USD |
| `1D` | `2122.60` | 391,450,000.00 USD | 0.00 USD | 391,450,000.00 USD | 1,220,000.00 USD | 689,080.00 USD | 1,120,000.00 USD |
| `7D` | `2124.30` | 738,160,000.00 USD | 0.00 USD | 738,160,000.00 USD | 832,850.00 USD | 972,650.00 USD | 1,510,000.00 USD |
| `1D` | `2125.60` | 388,420,000.00 USD | 0.00 USD | 388,420,000.00 USD | 714,970.00 USD | 1,500,000.00 USD | 778,960.00 USD |
| `7D` | `2127.60` | 734,840,000.00 USD | 0.00 USD | 734,840,000.00 USD | 2,400,000.00 USD | 2,630,000.00 USD | 3,270,000.00 USD |
| `1D` | `2128.60` | 385,420,000.00 USD | 0.00 USD | 385,420,000.00 USD | 116,180.00 USD | 475,750.00 USD | 318,170.00 USD |
| `7D` | `2130.90` | 726,550,000.00 USD | 0.00 USD | 726,550,000.00 USD | 2,410,000.00 USD | 2,300,000.00 USD | 1,700,000.00 USD |
| `1D` | `2131.60` | 384,510,000.00 USD | 0.00 USD | 384,510,000.00 USD | 0.00 USD | 18,610.00 USD | 331,620.00 USD |
| `7D` | `2134.20` | 720,130,000.00 USD | 0.00 USD | 720,130,000.00 USD | 2,170,000.00 USD | 550,450.00 USD | 308,060.00 USD |
| `7D` | `2137.50` | 717,100,000.00 USD | 0.00 USD | 717,100,000.00 USD | 1,040,000.00 USD | 880,790.00 USD | 43,560.00 USD |
| `1D` | `2137.60` | 384,160,000.00 USD | 0.00 USD | 384,160,000.00 USD | 0.00 USD | 278,410.00 USD | 0.00 USD |
| `7D` | `2140.80` | 715,140,000.00 USD | 0.00 USD | 715,140,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD |
| `7D` | `2144.10` | 711,200,000.00 USD | 0.00 USD | 711,200,000.00 USD | 449,020.00 USD | 1,130,000.00 USD | 268,500.00 USD |
| `7D` | `2147.40` | 709,360,000.00 USD | 0.00 USD | 709,360,000.00 USD | 657,710.00 USD | 421,320.00 USD | 0.00 USD |
| `7D` | `2150.70` | 708,280,000.00 USD | 0.00 USD | 708,280,000.00 USD | 459,630.00 USD | 463,640.00 USD | 31,040.00 USD |
| `1D` | `2152.60` | 383,880,000.00 USD | 0.00 USD | 383,880,000.00 USD | 208,250.00 USD | 440,530.00 USD | 0.00 USD |
| `7D` | `2154.00` | 707,320,000.00 USD | 0.00 USD | 707,320,000.00 USD | 128,430.00 USD | 331,520.00 USD | 32,590.00 USD |
| `1D` | `2155.60` | 383,230,000.00 USD | 0.00 USD | 383,230,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD |
| `7D` | `2157.30` | 706,830,000.00 USD | 0.00 USD | 706,830,000.00 USD | 388,210.00 USD | 1,030,000.00 USD | 1,080,000.00 USD |
| `1D` | `2158.60` | 381,840,000.00 USD | 0.00 USD | 381,840,000.00 USD | 0.00 USD | 0.00 USD | 37,580.00 USD |
| `7D` | `2160.60` | 704,330,000.00 USD | 0.00 USD | 704,330,000.00 USD | 646,940.00 USD | 1,900,000.00 USD | 1,990,000.00 USD |
| `1D` | `2161.60` | 381,800,000.00 USD | 0.00 USD | 381,800,000.00 USD | 0.00 USD | 3,150,000.00 USD | 71,920.00 USD |
| `7D` | `2163.90` | 699,790,000.00 USD | 0.00 USD | 699,790,000.00 USD | 566,120.00 USD | 3,280,000.00 USD | 1,290,000.00 USD |
| `1D` | `2164.60` | 378,580,000.00 USD | 0.00 USD | 378,580,000.00 USD | 0.00 USD | 0.00 USD | 107,900.00 USD |
| `7D` | `2167.20` | 694,650,000.00 USD | 0.00 USD | 694,650,000.00 USD | 25,540.00 USD | 3,620,000.00 USD | 50,240.00 USD |
| `1D` | `2167.60` | 378,470,000.00 USD | 0.00 USD | 378,470,000.00 USD | 2,340,000.00 USD | 1,700,000.00 USD | 0.00 USD |
| `7D` | `2170.50` | 690,950,000.00 USD | 0.00 USD | 690,950,000.00 USD | 3,500,000.00 USD | 2,380,000.00 USD | 1,830,000.00 USD |
| `1D` | `2170.60` | 374,430,000.00 USD | 0.00 USD | 374,430,000.00 USD | 5,020,000.00 USD | 3,070,000.00 USD | 873,550.00 USD |
| `1D` | `2173.60` | 365,460,000.00 USD | 0.00 USD | 365,460,000.00 USD | 0.00 USD | 190,230.00 USD | 0.00 USD |
| `7D` | `2173.80` | 683,240,000.00 USD | 0.00 USD | 683,240,000.00 USD | 4,110,000.00 USD | 363,040.00 USD | 1,010,000.00 USD |
| `1D` | `2176.60` | 365,270,000.00 USD | 0.00 USD | 365,270,000.00 USD | 345,940.00 USD | 1,510,000.00 USD | 35,760.00 USD |
| `1D` | `2179.60` | 363,380,000.00 USD | 0.00 USD | 363,380,000.00 USD | 2,080,000.00 USD | 0.00 USD | 706,110.00 USD |
| `7D` | `2180.40` | 677,760,000.00 USD | 0.00 USD | 677,760,000.00 USD | 0.00 USD | 373,740.00 USD | 176,950.00 USD |
| `1D` | `2182.60` | 360,600,000.00 USD | 0.00 USD | 360,600,000.00 USD | 0.00 USD | 478,110.00 USD | 679,940.00 USD |
| `7D` | `2183.70` | 677,210,000.00 USD | 0.00 USD | 677,210,000.00 USD | 0.00 USD | 1,310,000.00 USD | 2,550,000.00 USD |
| `1D` | `2185.60` | 359,440,000.00 USD | 0.00 USD | 359,440,000.00 USD | 1,350,000.00 USD | 1,960,000.00 USD | 1,790,000.00 USD |
| `7D` | `2187.00` | 673,360,000.00 USD | 0.00 USD | 673,360,000.00 USD | 556,600.00 USD | 0.00 USD | 54,020.00 USD |
| `1D` | `2188.60` | 354,330,000.00 USD | 0.00 USD | 354,330,000.00 USD | 0.00 USD | 0.00 USD | 693,960.00 USD |
| `7D` | `2190.30` | 672,750,000.00 USD | 0.00 USD | 672,750,000.00 USD | 2,730,000.00 USD | 0.00 USD | 4,200,000.00 USD |
| `1D` | `2191.60` | 353,640,000.00 USD | 0.00 USD | 353,640,000.00 USD | 0.00 USD | 222,200.00 USD | 109,400.00 USD |
| `1D` | `2194.60` | 353,310,000.00 USD | 0.00 USD | 353,310,000.00 USD | 605,210.00 USD | 881,070.00 USD | 0.00 USD |
| `7D` | `2196.90` | 665,820,000.00 USD | 0.00 USD | 665,820,000.00 USD | 2,580,000.00 USD | 474,090.00 USD | 2,040,000.00 USD |
| `1D` | `2197.60` | 351,820,000.00 USD | 0.00 USD | 351,820,000.00 USD | 416,500.00 USD | 0.00 USD | 1,890,000.00 USD |
| `7D` | `2200.20` | 660,720,000.00 USD | 0.00 USD | 660,720,000.00 USD | 3,000,000.00 USD | 5,080,000.00 USD | 3,200,000.00 USD |
| `1D` | `2200.60` | 349,520,000.00 USD | 0.00 USD | 349,520,000.00 USD | 284,470.00 USD | 3,230,000.00 USD | 1,550,000.00 USD |
| `7D` | `2203.50` | 649,450,000.00 USD | 0.00 USD | 649,450,000.00 USD | 3,650,000.00 USD | 1,710,000.00 USD | 3,750,000.00 USD |
| `1D` | `2203.60` | 344,450,000.00 USD | 0.00 USD | 344,450,000.00 USD | 3,540,000.00 USD | 1,280,000.00 USD | 830,450.00 USD |
| `1D` | `2206.60` | 338,810,000.00 USD | 0.00 USD | 338,810,000.00 USD | 2,210,000.00 USD | 10,890,000.00 USD | 1,970,000.00 USD |
| `7D` | `2206.80` | 640,340,000.00 USD | 0.00 USD | 640,340,000.00 USD | 6,920,000.00 USD | 9,430,000.00 USD | 4,020,000.00 USD |
| `1D` | `2209.60` | 323,740,000.00 USD | 0.00 USD | 323,740,000.00 USD | 1,890,000.00 USD | 2,010,000.00 USD | 2,210,000.00 USD |
| `7D` | `2210.10` | 619,960,000.00 USD | 0.00 USD | 619,960,000.00 USD | 12,800,000.00 USD | 20,410,000.00 USD | 6,470,000.00 USD |
| `1D` | `2212.60` | 317,640,000.00 USD | 0.00 USD | 317,640,000.00 USD | 7,820,000.00 USD | 5,240,000.00 USD | 2,830,000.00 USD |
| `7D` | `2213.40` | 580,290,000.00 USD | 0.00 USD | 580,290,000.00 USD | 10,920,000.00 USD | 11,890,000.00 USD | 13,170,000.00 USD |
| `1D` | `2215.60` | 301,750,000.00 USD | 0.00 USD | 301,750,000.00 USD | 18,260,000.00 USD | 11,500,000.00 USD | 7,560,000.00 USD |
| `7D` | `2216.70` | 544,310,000.00 USD | 0.00 USD | 544,310,000.00 USD | 25,210,000.00 USD | 17,030,000.00 USD | 9,390,000.00 USD |
| `1D` | `2218.60` | 264,430,000.00 USD | 0.00 USD | 264,430,000.00 USD | 7,700,000.00 USD | 8,360,000.00 USD | 1,950,000.00 USD |
| `7D` | `2220.00` | 492,680,000.00 USD | 0.00 USD | 492,680,000.00 USD | 24,310,000.00 USD | 12,300,000.00 USD | 10,120,000.00 USD |
| `1D` | `2221.60` | 246,420,000.00 USD | 0.00 USD | 246,420,000.00 USD | 6,250,000.00 USD | 13,160,000.00 USD | 1,340,000.00 USD |
| `7D` | `2223.30` | 445,950,000.00 USD | 0.00 USD | 445,950,000.00 USD | 10,150,000.00 USD | 8,220,000.00 USD | 11,910,000.00 USD |
| `1D` | `2224.60` | 225,670,000.00 USD | 0.00 USD | 225,670,000.00 USD | 9,730,000.00 USD | 5,030,000.00 USD | 6,100,000.00 USD |
| `7D` | `2226.60` | 415,670,000.00 USD | 0.00 USD | 415,670,000.00 USD | 12,840,000.00 USD | 11,030,000.00 USD | 9,960,000.00 USD |
| `1D` | `2227.60` | 204,800,000.00 USD | 0.00 USD | 204,800,000.00 USD | 6,230,000.00 USD | 13,340,000.00 USD | 5,140,000.00 USD |
| `7D` | `2229.90` | 381,850,000.00 USD | 0.00 USD | 381,850,000.00 USD | 12,730,000.00 USD | 11,790,000.00 USD | 25,750,000.00 USD |
| `1D` | `2230.60` | 180,090,000.00 USD | 0.00 USD | 180,090,000.00 USD | 7,100,000.00 USD | 8,290,000.00 USD | 2,840,000.00 USD |
| `7D` | `2233.20` | 331,570,000.00 USD | 0.00 USD | 331,570,000.00 USD | 16,600,000.00 USD | 24,290,000.00 USD | 10,420,000.00 USD |
| `1D` | `2233.60` | 161,860,000.00 USD | 0.00 USD | 161,860,000.00 USD | 6,140,000.00 USD | 3,540,000.00 USD | 8,520,000.00 USD |
| `7D` | `2236.50` | 280,250,000.00 USD | 0.00 USD | 280,250,000.00 USD | 16,050,000.00 USD | 2,010,000.00 USD | 14,220,000.00 USD |
| `1D` | `2236.60` | 143,660,000.00 USD | 0.00 USD | 143,660,000.00 USD | 18,680,000.00 USD | 0.00 USD | 5,910,000.00 USD |
| `1D` | `2239.60` | 119,070,000.00 USD | 0.00 USD | 119,070,000.00 USD | 16,010,000.00 USD | 4,410,000.00 USD | 4,190,000.00 USD |
| `7D` | `2239.80` | 247,980,000.00 USD | 0.00 USD | 247,980,000.00 USD | 15,710,000.00 USD | 6,600,000.00 USD | 13,750,000.00 USD |
| `1D` | `2242.60` | 94,460,000.00 USD | 0.00 USD | 94,460,000.00 USD | 2,540,000.00 USD | 760,920.00 USD | 5,330,000.00 USD |
| `7D` | `2243.10` | 211,920,000.00 USD | 0.00 USD | 211,920,000.00 USD | 22,920,000.00 USD | 0.00 USD | 13,050,000.00 USD |
| `1D` | `2245.60` | 85,840,000.00 USD | 0.00 USD | 85,840,000.00 USD | 1,910,000.00 USD | 4,700,000.00 USD | 940,150.00 USD |
| `7D` | `2246.40` | 175,950,000.00 USD | 0.00 USD | 175,950,000.00 USD | 14,340,000.00 USD | 0.00 USD | 13,920,000.00 USD |
| `1D` | `2248.60` | 78,280,000.00 USD | 0.00 USD | 78,280,000.00 USD | 15,010,000.00 USD | 22,790.00 USD | 10,470,000.00 USD |
| `7D` | `2249.70` | 147,690,000.00 USD | 0.00 USD | 147,690,000.00 USD | 18,000,000.00 USD | 0.00 USD | 12,820,000.00 USD |
| `1D` | `2251.60` | 52,770,000.00 USD | 0.00 USD | 52,770,000.00 USD | 7,080,000.00 USD | 2,400,000.00 USD | 1,710,000.00 USD |
| `7D` | `2253.00` | 116,870,000.00 USD | 0.00 USD | 116,870,000.00 USD | 26,890,000.00 USD | 5,220,000.00 USD | 28,120,000.00 USD |
| `1D` | `2254.60` | 41,590,000.00 USD | 0.00 USD | 41,590,000.00 USD | 0.00 USD | 7,830,000.00 USD | 12,590,000.00 USD |
| `7D` | `2256.30` | 56,630,000.00 USD | 0.00 USD | 56,630,000.00 USD | 17,450,000.00 USD | 0.00 USD | 8,180,000.00 USD |
| `1D` | `2257.60` | 21,170,000.00 USD | 0.00 USD | 21,170,000.00 USD | 0.00 USD | 0.00 USD | 2,780,000.00 USD |
| `7D` | `2259.60` | 31,000,000.00 USD | 0.00 USD | 31,000,000.00 USD | 10,940,000.00 USD | 0.00 USD | 11,910,000.00 USD |
| `1D` | `2260.60` | 18,390,000.00 USD | 0.00 USD | 18,390,000.00 USD | 2,420,000.00 USD | 0.00 USD | 156,010.00 USD |
| `1D` | `2263.60` | 15,820,000.00 USD | 0.00 USD | 15,820,000.00 USD | 0.00 USD | 0.00 USD | 7,670,000.00 USD |
| `7D` | `2266.20` | 8,160,000.00 USD | 0.00 USD | 8,160,000.00 USD | 0.00 USD | 0.00 USD | 8,160,000.00 USD |
| `1D` | `2266.60` | 8,150,000.00 USD | 0.00 USD | 8,150,000.00 USD | 0.00 USD | 0.00 USD | 4,770,000.00 USD |
| `1D` | `2269.60` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 1,940,000.00 USD |
| `1D` | `2272.60` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 287,660.00 USD |
| `7D` | `2273.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2275.60` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2276.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2278.60` | 7,540,000.00 USD | 7,540,000.00 USD | 0.00 USD | 5,740,000.00 USD | 1,360,000.00 USD | 431,610.00 USD |
| `7D` | `2279.40` | 17,000,000.00 USD | 17,000,000.00 USD | 0.00 USD | 0.00 USD | 17,000,000.00 USD | 0.00 USD |
| `1D` | `2281.60` | 73,490,000.00 USD | 73,490,000.00 USD | 0.00 USD | 39,500,000.00 USD | 26,450,000.00 USD | 0.00 USD |
| `7D` | `2282.70` | 98,670,000.00 USD | 98,670,000.00 USD | 0.00 USD | 0.00 USD | 81,670,000.00 USD | 0.00 USD |
| `1D` | `2284.60` | 132,910,000.00 USD | 132,910,000.00 USD | 0.00 USD | 32,760,000.00 USD | 19,370,000.00 USD | 7,290,000.00 USD |
| `7D` | `2286.00` | 108,070,000.00 USD | 108,070,000.00 USD | 0.00 USD | 0.00 USD | 9,400,000.00 USD | 0.00 USD |
| `1D` | `2287.60` | 133,670,000.00 USD | 133,670,000.00 USD | 0.00 USD | 0.00 USD | 760,920.00 USD | 0.00 USD |
| `1D` | `2290.60` | 142,650,000.00 USD | 142,650,000.00 USD | 0.00 USD | 0.00 USD | 8,840,000.00 USD | 143,050.00 USD |
| `1D` | `2293.60` | 156,580,000.00 USD | 156,580,000.00 USD | 0.00 USD | 8,310,000.00 USD | 0.00 USD | 5,620,000.00 USD |
| `7D` | `2295.90` | 122,750,000.00 USD | 122,750,000.00 USD | 0.00 USD | 6,580,000.00 USD | 2,380,000.00 USD | 5,720,000.00 USD |
| `1D` | `2296.60` | 170,340,000.00 USD | 170,340,000.00 USD | 0.00 USD | 5,410,000.00 USD | 8,210,000.00 USD | 143,830.00 USD |
| `7D` | `2299.20` | 151,170,000.00 USD | 151,170,000.00 USD | 0.00 USD | 11,730,000.00 USD | 11,130,000.00 USD | 5,560,000.00 USD |
| `1D` | `2299.60` | 185,470,000.00 USD | 185,470,000.00 USD | 0.00 USD | 0.00 USD | 7,840,000.00 USD | 7,290,000.00 USD |
| `7D` | `2302.50` | 198,290,000.00 USD | 198,290,000.00 USD | 0.00 USD | 23,020,000.00 USD | 7,250,000.00 USD | 16,850,000.00 USD |
| `1D` | `2302.60` | 202,170,000.00 USD | 202,170,000.00 USD | 0.00 USD | 13,040,000.00 USD | 682,490.00 USD | 2,970,000.00 USD |
| `1D` | `2305.60` | 228,530,000.00 USD | 228,530,000.00 USD | 0.00 USD | 10,050,000.00 USD | 14,130,000.00 USD | 2,180,000.00 USD |
| `7D` | `2305.80` | 209,580,000.00 USD | 209,580,000.00 USD | 0.00 USD | 2,980,000.00 USD | 6,110,000.00 USD | 2,200,000.00 USD |
| `1D` | `2308.60` | 233,290,000.00 USD | 233,290,000.00 USD | 0.00 USD | 2,420,000.00 USD | 2,340,000.00 USD | 0.00 USD |
| `7D` | `2309.10` | 213,350,000.00 USD | 213,350,000.00 USD | 0.00 USD | 732,090.00 USD | 930,630.00 USD | 2,110,000.00 USD |
| `1D` | `2311.60` | 242,870,000.00 USD | 242,870,000.00 USD | 0.00 USD | 691,870.00 USD | 1,260,000.00 USD | 7,620,000.00 USD |
| `7D` | `2312.40` | 228,850,000.00 USD | 228,850,000.00 USD | 0.00 USD | 7,270,000.00 USD | 0.00 USD | 8,230,000.00 USD |
| `1D` | `2314.60` | 257,200,000.00 USD | 257,200,000.00 USD | 0.00 USD | 0.00 USD | 14,100,000.00 USD | 231,520.00 USD |
| `7D` | `2315.70` | 236,420,000.00 USD | 236,420,000.00 USD | 0.00 USD | 0.00 USD | 7,460,000.00 USD | 117,510.00 USD |
| `1D` | `2317.60` | 285,740,000.00 USD | 285,740,000.00 USD | 0.00 USD | 10,230,000.00 USD | 10,470,000.00 USD | 7,850,000.00 USD |
| `7D` | `2319.00` | 245,030,000.00 USD | 245,030,000.00 USD | 0.00 USD | 1,020,000.00 USD | 4,550,000.00 USD | 3,030,000.00 USD |
| `1D` | `2320.60` | 301,830,000.00 USD | 301,830,000.00 USD | 0.00 USD | 6,580,000.00 USD | 9,360,000.00 USD | 147,610.00 USD |
| `7D` | `2322.30` | 264,770,000.00 USD | 264,770,000.00 USD | 0.00 USD | 1,110,000.00 USD | 15,930,000.00 USD | 2,690,000.00 USD |
| `1D` | `2323.60` | 316,400,000.00 USD | 316,400,000.00 USD | 0.00 USD | 572,970.00 USD | 10,410,000.00 USD | 3,590,000.00 USD |
| `7D` | `2325.60` | 285,420,000.00 USD | 285,420,000.00 USD | 0.00 USD | 9,720,000.00 USD | 2,540,000.00 USD | 8,390,000.00 USD |
| `1D` | `2326.60` | 328,490,000.00 USD | 328,490,000.00 USD | 0.00 USD | 735,700.00 USD | 5,550,000.00 USD | 5,800,000.00 USD |
| `7D` | `2328.90` | 297,240,000.00 USD | 297,240,000.00 USD | 0.00 USD | 3,860,000.00 USD | 0.00 USD | 7,960,000.00 USD |
| `1D` | `2329.60` | 339,400,000.00 USD | 339,400,000.00 USD | 0.00 USD | 9,740,000.00 USD | 884,940.00 USD | 281,390.00 USD |
| `7D` | `2332.20` | 326,480,000.00 USD | 326,480,000.00 USD | 0.00 USD | 29,230,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2332.60` | 355,440,000.00 USD | 355,440,000.00 USD | 0.00 USD | 11,910,000.00 USD | 251,940.00 USD | 3,880,000.00 USD |
| `7D` | `2335.50` | 384,490,000.00 USD | 384,490,000.00 USD | 0.00 USD | 28,990,000.00 USD | 18,420,000.00 USD | 10,600,000.00 USD |
| `1D` | `2335.60` | 381,480,000.00 USD | 381,480,000.00 USD | 0.00 USD | 17,120,000.00 USD | 3,360,000.00 USD | 5,560,000.00 USD |
| `1D` | `2338.60` | 396,810,000.00 USD | 396,810,000.00 USD | 0.00 USD | 8,670,000.00 USD | 2,600,000.00 USD | 4,050,000.00 USD |
| `7D` | `2338.80` | 402,360,000.00 USD | 402,360,000.00 USD | 0.00 USD | 9,570,000.00 USD | 0.00 USD | 8,310,000.00 USD |
| `1D` | `2341.60` | 417,170,000.00 USD | 417,170,000.00 USD | 0.00 USD | 7,140,000.00 USD | 3,360,000.00 USD | 9,870,000.00 USD |
| `7D` | `2342.10` | 442,460,000.00 USD | 442,460,000.00 USD | 0.00 USD | 4,720,000.00 USD | 21,390,000.00 USD | 14,000,000.00 USD |
| `1D` | `2344.60` | 433,410,000.00 USD | 433,410,000.00 USD | 0.00 USD | 1,370,000.00 USD | 6,180,000.00 USD | 8,690,000.00 USD |
| `7D` | `2345.40` | 463,840,000.00 USD | 463,840,000.00 USD | 0.00 USD | 1,350,000.00 USD | 13,990,000.00 USD | 6,020,000.00 USD |
| `1D` | `2347.60` | 442,350,000.00 USD | 442,350,000.00 USD | 0.00 USD | 3,300,000.00 USD | 3,010,000.00 USD | 2,630,000.00 USD |
| `7D` | `2348.70` | 496,970,000.00 USD | 496,970,000.00 USD | 0.00 USD | 847,620.00 USD | 8,140,000.00 USD | 24,140,000.00 USD |
| `1D` | `2350.60` | 491,530,000.00 USD | 491,530,000.00 USD | 0.00 USD | 33,010,000.00 USD | 7,320,000.00 USD | 8,860,000.00 USD |
| `7D` | `2352.00` | 533,590,000.00 USD | 533,590,000.00 USD | 0.00 USD | 2,930,000.00 USD | 23,060,000.00 USD | 10,630,000.00 USD |
| `1D` | `2353.60` | 506,450,000.00 USD | 506,450,000.00 USD | 0.00 USD | 4,400,000.00 USD | 9,300,000.00 USD | 1,220,000.00 USD |
| `7D` | `2355.30` | 588,190,000.00 USD | 588,190,000.00 USD | 0.00 USD | 16,520,000.00 USD | 36,690,000.00 USD | 1,380,000.00 USD |
| `1D` | `2356.60` | 523,620,000.00 USD | 523,620,000.00 USD | 0.00 USD | 3,480,000.00 USD | 11,210,000.00 USD | 2,480,000.00 USD |
| `7D` | `2358.60` | 599,000,000.00 USD | 599,000,000.00 USD | 0.00 USD | 7,110,000.00 USD | 512,220.00 USD | 3,190,000.00 USD |
| `1D` | `2359.60` | 544,150,000.00 USD | 544,150,000.00 USD | 0.00 USD | 6,360,000.00 USD | 6,900,000.00 USD | 7,270,000.00 USD |
| `7D` | `2361.90` | 606,130,000.00 USD | 606,130,000.00 USD | 0.00 USD | 3,150,000.00 USD | 3,800,000.00 USD | 176,950.00 USD |
| `1D` | `2362.60` | 569,530,000.00 USD | 569,530,000.00 USD | 0.00 USD | 10,730,000.00 USD | 6,710,000.00 USD | 7,940,000.00 USD |
| `7D` | `2365.20` | 624,030,000.00 USD | 624,030,000.00 USD | 0.00 USD | 8,440,000.00 USD | 0.00 USD | 9,460,000.00 USD |
| `1D` | `2365.60` | 580,000,000.00 USD | 580,000,000.00 USD | 0.00 USD | 3,290,000.00 USD | 4,700,000.00 USD | 2,480,000.00 USD |
| `7D` | `2368.50` | 637,090,000.00 USD | 637,090,000.00 USD | 0.00 USD | 10,830,000.00 USD | 1,780,000.00 USD | 458,400.00 USD |
| `1D` | `2368.60` | 596,770,000.00 USD | 596,770,000.00 USD | 0.00 USD | 8,810,000.00 USD | 4,420,000.00 USD | 3,550,000.00 USD |
| `1D` | `2371.60` | 639,070,000.00 USD | 639,070,000.00 USD | 0.00 USD | 17,650,000.00 USD | 13,840,000.00 USD | 10,800,000.00 USD |
| `7D` | `2371.80` | 718,030,000.00 USD | 718,030,000.00 USD | 0.00 USD | 26,000,000.00 USD | 0.00 USD | 54,940,000.00 USD |
| `1D` | `2374.60` | 659,590,000.00 USD | 659,590,000.00 USD | 0.00 USD | 14,820,000.00 USD | 709,900.00 USD | 4,990,000.00 USD |
| `7D` | `2375.10` | 744,980,000.00 USD | 744,980,000.00 USD | 0.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD |
| `1D` | `2377.60` | 687,370,000.00 USD | 687,370,000.00 USD | 0.00 USD | 7,850,000.00 USD | 8,860,000.00 USD | 11,070,000.00 USD |
| `7D` | `2378.40` | 790,390,000.00 USD | 790,390,000.00 USD | 0.00 USD | 11,800,000.00 USD | 7,950,000.00 USD | 25,670,000.00 USD |
| `1D` | `2380.60` | 732,090,000.00 USD | 732,090,000.00 USD | 0.00 USD | 12,710,000.00 USD | 14,110,000.00 USD | 17,910,000.00 USD |
| `7D` | `2381.70` | 830,180,000.00 USD | 830,180,000.00 USD | 0.00 USD | 8,510,000.00 USD | 6,750,000.00 USD | 24,530,000.00 USD |
| `1D` | `2383.60` | 786,450,000.00 USD | 786,450,000.00 USD | 0.00 USD | 24,510,000.00 USD | 15,290,000.00 USD | 14,560,000.00 USD |
| `7D` | `2385.00` | 931,900,000.00 USD | 931,900,000.00 USD | 0.00 USD | 18,550,000.00 USD | 36,910,000.00 USD | 46,260,000.00 USD |
| `1D` | `2386.60` | 823,450,000.00 USD | 823,450,000.00 USD | 0.00 USD | 12,470,000.00 USD | 12,790,000.00 USD | 11,730,000.00 USD |
| `7D` | `2388.30` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 0.00 USD | 5,290,000.00 USD | 38,070,000.00 USD | 44,510,000.00 USD |
| `1D` | `2389.60` | 850,210,000.00 USD | 850,210,000.00 USD | 0.00 USD | 11,290,000.00 USD | 9,340,000.00 USD | 6,130,000.00 USD |
| `7D` | `2391.60` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 8,560,000.00 USD | 52,080,000.00 USD | 40,380,000.00 USD |
| `1D` | `2392.60` | 867,540,000.00 USD | 867,540,000.00 USD | 0.00 USD | 5,650,000.00 USD | 4,340,000.00 USD | 7,340,000.00 USD |
| `7D` | `2394.90` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 0.00 USD | 57,450,000.00 USD | 32,260,000.00 USD | 37,090,000.00 USD |
| `1D` | `2395.60` | 883,750,000.00 USD | 883,750,000.00 USD | 0.00 USD | 5,260,000.00 USD | 7,330,000.00 USD | 3,630,000.00 USD |
| `7D` | `2398.20` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 0.00 USD | 42,820,000.00 USD | 38,210,000.00 USD | 29,190,000.00 USD |
| `1D` | `2398.60` | 907,260,000.00 USD | 907,260,000.00 USD | 0.00 USD | 6,440,000.00 USD | 7,340,000.00 USD | 9,730,000.00 USD |
| `7D` | `2401.50` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 0.00 USD | 51,970,000.00 USD | 26,780,000.00 USD | 29,090,000.00 USD |
| `1D` | `2401.60` | 928,820,000.00 USD | 928,820,000.00 USD | 0.00 USD | 7,630,000.00 USD | 7,320,000.00 USD | 6,610,000.00 USD |
| `1D` | `2404.60` | 962,450,000.00 USD | 962,450,000.00 USD | 0.00 USD | 11,940,000.00 USD | 10,820,000.00 USD | 10,870,000.00 USD |
| `7D` | `2404.80` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 50,800,000.00 USD | 32,200,000.00 USD | 24,110,000.00 USD |
| `1D` | `2407.60` | 995,530,000.00 USD | 995,530,000.00 USD | 0.00 USD | 16,380,000.00 USD | 9,710,000.00 USD | 7,000,000.00 USD |
| `7D` | `2408.10` | 1,660,000,000.00 USD | 1,660,000,000.00 USD | 0.00 USD | 34,390,000.00 USD | 31,420,000.00 USD | 25,030,000.00 USD |
| `1D` | `2410.60` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 0.00 USD | 6,060,000.00 USD | 7,690,000.00 USD | 8,290,000.00 USD |
| `7D` | `2411.40` | 1,740,000,000.00 USD | 1,740,000,000.00 USD | 0.00 USD | 19,200,000.00 USD | 32,580,000.00 USD | 27,660,000.00 USD |
| `1D` | `2413.60` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 0.00 USD | 8,520,000.00 USD | 5,520,000.00 USD | 3,130,000.00 USD |
| `7D` | `2414.70` | 1,810,000,000.00 USD | 1,810,000,000.00 USD | 0.00 USD | 24,010,000.00 USD | 21,950,000.00 USD | 23,130,000.00 USD |
| `1D` | `2416.60` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 4,510,000.00 USD | 3,390,000.00 USD | 5,190,000.00 USD |
| `7D` | `2418.00` | 1,890,000,000.00 USD | 1,890,000,000.00 USD | 0.00 USD | 34,060,000.00 USD | 15,260,000.00 USD | 24,610,000.00 USD |
| `1D` | `2419.60` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 6,750,000.00 USD | 4,200,000.00 USD | 3,710,000.00 USD |
| `7D` | `2421.30` | 1,960,000,000.00 USD | 1,960,000,000.00 USD | 0.00 USD | 25,700,000.00 USD | 27,890,000.00 USD | 21,590,000.00 USD |
| `1D` | `2422.60` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 0.00 USD | 2,930,000.00 USD | 4,220,000.00 USD | 5,020,000.00 USD |
| `7D` | `2424.60` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 0.00 USD | 24,180,000.00 USD | 35,050,000.00 USD | 34,520,000.00 USD |
| `1D` | `2425.60` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 0.00 USD | 1,810,000.00 USD | 2,260,000.00 USD | 844,590.00 USD |
| `7D` | `2427.90` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 0.00 USD | 25,200,000.00 USD | 18,380,000.00 USD | 26,460,000.00 USD |
| `1D` | `2428.60` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 0.00 USD | 754,820.00 USD | 897,420.00 USD | 1,500,000.00 USD |
| `7D` | `2431.20` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 0.00 USD | 10,380,000.00 USD | 18,750,000.00 USD | 9,300,000.00 USD |
| `1D` | `2431.60` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 2,910,000.00 USD | 2,570,000.00 USD | 369,590.00 USD |
| `7D` | `2434.50` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 0.00 USD | 27,390,000.00 USD | 21,570,000.00 USD | 11,160,000.00 USD |
| `1D` | `2434.60` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 1,670,000.00 USD | 468,310.00 USD | 1,560,000.00 USD |
| `1D` | `2437.60` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 1,200,000.00 USD | 531,390.00 USD | 205,600.00 USD |
| `7D` | `2437.80` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 0.00 USD | 12,000,000.00 USD | 12,820,000.00 USD | 5,470,000.00 USD |
| `1D` | `2440.60` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 1,540,000.00 USD | 2,040,000.00 USD | 1,030,000.00 USD |
| `7D` | `2441.10` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 15,080,000.00 USD | 8,120,000.00 USD | 10,680,000.00 USD |
| `1D` | `2443.60` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 1,050,000.00 USD | 1,060,000.00 USD | 1,510,000.00 USD |
| `7D` | `2444.40` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 0.00 USD | 8,860,000.00 USD | 15,160,000.00 USD | 14,000,000.00 USD |
| `1D` | `2446.60` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 648,280.00 USD | 347,060.00 USD | 1,090,000.00 USD |
| `7D` | `2447.70` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 11,650,000.00 USD | 8,510,000.00 USD | 17,330,000.00 USD |
| `1D` | `2449.60` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 651,910.00 USD | 1,290,000.00 USD | 2,420,000.00 USD |
| `7D` | `2451.00` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 0.00 USD | 16,710,000.00 USD | 14,100,000.00 USD | 16,480,000.00 USD |
| `1D` | `2452.60` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 4,030,000.00 USD | 2,370,000.00 USD | 4,300,000.00 USD |
| `7D` | `2454.30` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 0.00 USD | 4,620,000.00 USD | 5,780,000.00 USD | 3,880,000.00 USD |
| `1D` | `2455.60` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 4,380,000.00 USD | 3,050,000.00 USD | 1,960,000.00 USD |
| `7D` | `2457.60` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 0.00 USD | 15,150,000.00 USD | 12,540,000.00 USD | 12,600,000.00 USD |
| `1D` | `2458.60` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 1,430,000.00 USD | 2,640,000.00 USD | 890,200.00 USD |
| `7D` | `2460.90` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 0.00 USD | 5,580,000.00 USD | 8,670,000.00 USD | 6,870,000.00 USD |
| `1D` | `2461.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 470,530.00 USD | 490,260.00 USD | 1,160,000.00 USD |
| `7D` | `2464.20` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 0.00 USD | 8,720,000.00 USD | 7,700,000.00 USD | 4,700,000.00 USD |
| `1D` | `2464.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 83,300.00 USD | 176,210.00 USD | 829,050.00 USD |
| `7D` | `2467.50` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 0.00 USD | 4,540,000.00 USD | 3,710,000.00 USD | 586,780.00 USD |
| `1D` | `2467.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 68,070.00 USD | 0.00 USD |
| `1D` | `2470.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 1,190,000.00 USD | 391,890.00 USD |
| `7D` | `2470.80` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 0.00 USD | 3,960,000.00 USD | 2,290,000.00 USD | 522,210.00 USD |
| `7D` | `2474.10` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 0.00 USD | 5,230,000.00 USD | 2,920,000.00 USD | 2,400,000.00 USD |
| `1D` | `2476.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 914,780.00 USD | 28,770.00 USD |
| `7D` | `2477.40` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 0.00 USD | 1,660,000.00 USD | 4,420,000.00 USD | 718,840.00 USD |
| `7D` | `2480.70` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 0.00 USD | 2,110,000.00 USD | 4,170,000.00 USD | 540,990.00 USD |
| `1D` | `2482.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 239,600.00 USD | 136,500.00 USD | 43,160.00 USD |
| `7D` | `2484.00` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 0.00 USD | 1,210,000.00 USD | 1,390,000.00 USD | 77,610.00 USD |
| `1D` | `2485.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 865,140.00 USD | 1,330,000.00 USD | 0.00 USD |
| `7D` | `2487.30` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 0.00 USD | 325,140.00 USD | 262,280.00 USD | 0.00 USD |
| `1D` | `2488.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 866,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2490.60` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 0.00 USD | 2,910,000.00 USD | 2,540,000.00 USD | 279,750.00 USD |
| `1D` | `2491.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 138,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2493.90` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 0.00 USD | 1,660,000.00 USD | 1,790,000.00 USD | 3,940,000.00 USD |
| `1D` | `2494.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 178,560.00 USD | 14,300.00 USD |
| `7D` | `2497.20` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 0.00 USD | 2,940,000.00 USD | 5,270,000.00 USD | 8,250,000.00 USD |
| `7D` | `2500.50` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 0.00 USD | 1,110,000.00 USD | 2,280,000.00 USD | 1,130,000.00 USD |
| `7D` | `2503.80` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 0.00 USD | 63,860.00 USD | 1,900,000.00 USD | 125,600.00 USD |
| `1D` | `2506.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 338,980.00 USD | 717,780.00 USD |
| `7D` | `2507.10` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 0.00 USD | 4,340,000.00 USD | 3,090,000.00 USD | 3,180,000.00 USD |
| `1D` | `2509.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,160.00 USD |
| `7D` | `2510.40` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 0.00 USD | 2,290,000.00 USD | 1,270,000.00 USD | 0.00 USD |
| `1D` | `2512.60` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 242,080.00 USD | 88,880.00 USD | 0.00 USD |
| `7D` | `2513.70` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 0.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2515.60` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `7D` | `2517.00` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 0.00 USD | 97,050.00 USD | 189,640.00 USD | 815,620.00 USD |
| `7D` | `2520.30` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD |
| `1D` | `2521.60` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 113,940.00 USD | 173,370.00 USD | 620,660.00 USD |
| `7D` | `2523.60` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 0.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD |
| `1D` | `2524.60` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 1,340,000.00 USD | 485,130.00 USD | 30,180.00 USD |
| `7D` | `2526.90` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 0.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD |
| `1D` | `2527.60` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 0.00 USD | 1,010,000.00 USD | 50,470.00 USD |
| `7D` | `2530.20` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 0.00 USD | 2,800,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD |
| `1D` | `2530.60` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 1,050,000.00 USD | 319,490.00 USD | 437,490.00 USD |
| `7D` | `2533.50` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 0.00 USD | 3,530,000.00 USD | 1,850,000.00 USD | 2,030,000.00 USD |
| `1D` | `2533.60` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 442,230.00 USD | 597,240.00 USD | 436,900.00 USD |
| `1D` | `2536.60` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 656,520.00 USD | 1,170,000.00 USD |
| `7D` | `2536.80` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 0.00 USD | 3,720,000.00 USD | 3,450,000.00 USD | 3,530,000.00 USD |
| `1D` | `2539.60` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 2,030,000.00 USD | 1,090,000.00 USD | 1,570,000.00 USD |
| `7D` | `2540.10` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 0.00 USD | 4,150,000.00 USD | 3,220,000.00 USD | 1,580,000.00 USD |
| `1D` | `2542.60` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 1,270,000.00 USD | 1,360,000.00 USD | 218,810.00 USD |
| `7D` | `2543.40` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 0.00 USD | 4,150,000.00 USD | 2,520,000.00 USD | 2,480,000.00 USD |
| `1D` | `2545.60` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 1,450,000.00 USD | 848,320.00 USD | 215,500.00 USD |
| `7D` | `2546.70` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 0.00 USD | 1,450,000.00 USD | 1,090,000.00 USD | 2,290,000.00 USD |
| `1D` | `2548.60` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 1,630,000.00 USD | 1,300,000.00 USD | 1,720,000.00 USD |
| `7D` | `2550.00` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 0.00 USD | 4,320,000.00 USD | 3,550,000.00 USD | 3,720,000.00 USD |
| `1D` | `2551.60` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 1,480,000.00 USD | 988,750.00 USD | 698,070.00 USD |
| `7D` | `2553.30` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 0.00 USD | 2,820,000.00 USD | 788,360.00 USD | 2,600,000.00 USD |
| `1D` | `2554.60` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 1,360,000.00 USD | 225,190.00 USD | 238,730.00 USD |
| `7D` | `2556.60` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 0.00 USD | 2,760,000.00 USD | 283,560.00 USD | 6,500,000.00 USD |
| `1D` | `2557.60` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 533,960.00 USD | 522,240.00 USD | 874,240.00 USD |
| `7D` | `2559.90` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 0.00 USD | 5,720,000.00 USD | 2,130,000.00 USD | 1,390,000.00 USD |
| `1D` | `2560.60` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 2,100,000.00 USD | 1,120,000.00 USD | 1,300,000.00 USD |
| `7D` | `2563.20` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 0.00 USD | 1,430,000.00 USD | 2,900,000.00 USD | 1,290,000.00 USD |
| `1D` | `2563.60` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 463,350.00 USD | 1,170,000.00 USD | 984,190.00 USD |
| `7D` | `2566.50` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 0.00 USD | 1,860,000.00 USD | 1,830,000.00 USD | 3,300,000.00 USD |
| `1D` | `2566.60` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 172,210.00 USD | 232,250.00 USD | 15,650.00 USD |
| `1D` | `2569.60` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 507,510.00 USD | 289,160.00 USD | 462,940.00 USD |
| `7D` | `2569.80` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 0.00 USD | 125,250.00 USD | 341,900.00 USD | 1,190,000.00 USD |
| `1D` | `2572.60` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 612,280.00 USD | 671,930.00 USD | 22,270.00 USD |
| `7D` | `2573.10` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,790,000.00 USD |
| `1D` | `2575.60` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 546,100.00 USD | 0.00 USD | 496,850.00 USD |
| `7D` | `2576.40` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 0.00 USD | 2,400,000.00 USD | 930,280.00 USD | 1,640,000.00 USD |
| `1D` | `2578.60` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 118,210.00 USD | 31,550.00 USD | 0.00 USD |
| `7D` | `2579.70` | 2,730,000,000.00 USD | 2,730,000,000.00 USD | 0.00 USD | 2,750,000.00 USD | 1,780,000.00 USD | 1,960,000.00 USD |
| `1D` | `2580.60` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 414,360.00 USD | 126,990.00 USD | 188,300.00 USD |
| `7D` | `2583.00` | 2,730,000,000.00 USD | 2,730,000,000.00 USD | 0.00 USD | 1,730,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD |
| `7D` | `2586.30` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 0.00 USD | 1,480,000.00 USD | 2,030,000.00 USD | 2,570,000.00 USD |
| `7D` | `2589.60` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 0.00 USD | 3,310,000.00 USD | 631,590.00 USD | 2,150,000.00 USD |
| `7D` | `2592.90` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 0.00 USD | 2,370,000.00 USD | 1,280,000.00 USD | 1,580,000.00 USD |
| `7D` | `2596.20` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 0.00 USD | 794,750.00 USD | 620,840.00 USD | 1,490,000.00 USD |
| `7D` | `2599.50` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,530,000.00 USD | 2,810,000.00 USD |
| `7D` | `2602.80` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 0.00 USD | 1,680,000.00 USD | 1,260,000.00 USD | 1,690,000.00 USD |
| `7D` | `2606.10` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 1,850,000.00 USD | 1,560,000.00 USD | 772,800.00 USD |
| `7D` | `2609.40` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD |
| `7D` | `2612.70` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 1,010,000.00 USD | 643,740.00 USD | 43,560.00 USD |
| `7D` | `2616.00` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 0.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD |
| `7D` | `2619.30` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 0.00 USD | 449,020.00 USD | 323,810.00 USD | 268,500.00 USD |
| `7D` | `2622.60` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 0.00 USD | 631,440.00 USD | 1,220,000.00 USD | 0.00 USD |
| `7D` | `2625.90` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 0.00 USD | 485,890.00 USD | 474,490.00 USD | 0.00 USD |
| `7D` | `2629.20` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 0.00 USD | 0.00 USD | 20,460.00 USD | 31,040.00 USD |
| `7D` | `2632.40` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 0.00 USD | 0.00 USD | 301,060.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `29.16B` | Total OI Tokens: `12,824,238.8 ETH`
  * 1h OI Change: `+1.28%` | 4h OI Change: `-2.53%` | 24h OI Change: `-2.65%`
  * Exchange Breakdown: Binance=`8.55B` | Bybit=`2.09B` | OKX=`1.77B` | Hyperliquid=`2.50B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `103.22K` | Last 24h: `2.27M` | Last 3d: `7.66M` | Last 7d: `13.85M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0012%` | **USDT OKX** | `0.0045%` |
| **USDT Bybit** | `-0.0039%` | **USDT KuCoin** | `-0.0016%` |
| **USDT MEXC** | `0.0012%` | **USDT BingX** | `0.0051%` |
| **USDT Gate** | `0.0013%` | **USDT Bitget** | `0.0035%` |
| **CoinM Binance** | `0.0046%` | **CoinM OKX** | `-0.0003%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `48.70%` | `51.30%` | `0.95` | 1,580,000,000.00 USD |
| `15M` | `Binance` | `49.02%` | `50.98%` | `0.96` | 495,600,000.00 USD |
| `15M` | `OKX` | `55.15%` | `44.85%` | `1.23` | 226,310,000.00 USD |
| `15M` | `Bybit` | `44.1%` | `55.9%` | `0.79` | 178,110,000.00 USD |
| `15M` | `KuCoin` | `40.8%` | `59.2%` | `0.69` | 4,710,000.00 USD |
| `15M` | `Gate` | `52.31%` | `47.69%` | `1.10` | 163,140,000.00 USD |
| `15M` | `Bitget` | `61.44%` | `38.56%` | `1.59` | 93,170,000.00 USD |
| `15M` | `BingX` | `42.22%` | `57.78%` | `0.73` | 14,040,000.00 USD |
| `15M` | `MEXC` | `42.46%` | `57.54%` | `0.74` | 87,290,000.00 USD |
| `15M` | `Bitunix` | `46.62%` | `53.38%` | `0.87` | 74,880,000.00 USD |
| `15M` | `Hyperliquid` | `30.26%` | `69.74%` | `0.43` | 113,610,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.83%` | `51.17%` | `0.95` | 4,090,000.00 USD |
| `15M` | `Crypto.com` | `53.41%` | `46.59%` | `1.15` | 5,730,000.00 USD |
| `15M` | `WhiteBIT` | `51.81%` | `48.19%` | `1.08` | 19,460,000.00 USD |
| `15M` | `HTX` | `46.48%` | `53.52%` | `0.87` | 5,310,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `47.16%` | `52.84%` | `0.89` | 43,530,000.00 USD |
| `15M` | `Bitfinex` | `35.28%` | `64.72%` | `0.55` | 1,390,000.00 USD |
| `15M` | `Kraken` | `54.81%` | `45.19%` | `1.21` | 15,670,000.00 USD |
| `15M` | `Aster` | `44.83%` | `55.17%` | `0.81` | 7,380,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `61.49%` | `38.51%` | `1.60` | 22,480,000.00 USD |
| `15M` | `Whale Positions` | `49.02%` | `50.98%` | `0.96` | 495,600,000.00 USD |
| `15M` | `Global Accounts` | `48.70%` | `51.30%` | `0.95` | 1,580,000,000.00 USD |
| `1H` | `ETH` | `54.78%` | `45.22%` | `1.21` | 8,830,000,000.00 USD |
| `1H` | `Binance` | `49.3%` | `50.7%` | `0.97` | 2,270,000,000.00 USD |
| `1H` | `OKX` | `57.01%` | `42.99%` | `1.33` | 992,180,000.00 USD |
| `1H` | `Bybit` | `52.9%` | `47.1%` | `1.12` | 1,140,000,000.00 USD |
| `1H` | `KuCoin` | `69.59%` | `30.41%` | `2.29` | 31,820,000.00 USD |
| `1H` | `Gate` | `52.34%` | `47.66%` | `1.10` | 892,290,000.00 USD |
| `1H` | `Bitget` | `55.67%` | `44.33%` | `1.26` | 404,230,000.00 USD |
| `1H` | `BingX` | `53.64%` | `46.36%` | `1.16` | 89,400,000.00 USD |
| `1H` | `MEXC` | `48.12%` | `51.88%` | `0.93` | 316,220,000.00 USD |
| `1H` | `Bitunix` | `48.52%` | `51.48%` | `0.94` | 313,050,000.00 USD |
| `1H` | `Hyperliquid` | `51.71%` | `48.29%` | `1.07` | 687,410,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.51%` | `49.49%` | `1.02` | 22,550,000.00 USD |
| `1H` | `Crypto.com` | `50.57%` | `49.43%` | `1.02` | 33,130,000.00 USD |
| `1H` | `WhiteBIT` | `73.07%` | `26.93%` | `2.71` | 1,210,000,000.00 USD |
| `1H` | `HTX` | `53.42%` | `46.58%` | `1.15` | 18,800,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `54.23%` | `45.77%` | `1.18` | 154,480,000.00 USD |
| `1H` | `Bitfinex` | `16.94%` | `83.06%` | `0.20` | 23,860,000.00 USD |
| `1H` | `Kraken` | `51.96%` | `48.04%` | `1.08` | 87,780,000.00 USD |
| `1H` | `Aster` | `50.97%` | `49.03%` | `1.04` | 46,310,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `49.72%` | `50.28%` | `0.99` | 97,050,000.00 USD |
| `1H` | `Whale Positions` | `49.3%` | `50.7%` | `0.97` | 2,270,000,000.00 USD |
| `1H` | `Global Accounts` | `54.78%` | `45.22%` | `1.21` | 8,830,000,000.00 USD |
| `4H` | `ETH` | `47.03%` | `52.97%` | `0.89` | 22,560,000,000.00 USD |
| `4H` | `Binance` | `45.06%` | `54.94%` | `0.82` | 6,810,000,000.00 USD |
| `4H` | `OKX` | `45.35%` | `54.65%` | `0.83` | 3,810,000,000.00 USD |
| `4H` | `Bybit` | `44.4%` | `55.6%` | `0.80` | 1,660,000,000.00 USD |
| `4H` | `KuCoin` | `53.64%` | `46.36%` | `1.16` | 209,110,000.00 USD |
| `4H` | `Gate` | `49.54%` | `50.46%` | `0.98` | 2,280,000,000.00 USD |
| `4H` | `Bitget` | `51.2%` | `48.8%` | `1.05` | 1,040,000,000.00 USD |
| `4H` | `BingX` | `50.4%` | `49.6%` | `1.02` | 238,390,000.00 USD |
| `4H` | `MEXC` | `48.51%` | `51.49%` | `0.94` | 666,570,000.00 USD |
| `4H` | `Bitunix` | `47.3%` | `52.7%` | `0.90` | 713,570,000.00 USD |
| `4H` | `Hyperliquid` | `45.09%` | `54.91%` | `0.82` | 1,180,000,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.32%` | `48.68%` | `1.05` | 53,540,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `51.7%` | `48.3%` | `1.07` | 2,980,000,000.00 USD |
| `4H` | `HTX` | `38.08%` | `61.92%` | `0.61` | 195,360,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `49%` | `51%` | `0.96` | 129,950,000.00 USD |
| `4H` | `Bitfinex` | `26.56%` | `73.44%` | `0.36` | 8,020,000.00 USD |
| `4H` | `Kraken` | `47.16%` | `52.84%` | `0.89` | 80,650,000.00 USD |
| `4H` | `Aster` | `46.69%` | `53.31%` | `0.88` | 189,670,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `49.09%` | `50.91%` | `0.96` | 312,130,000.00 USD |
| `4H` | `Whale Positions` | `45.06%` | `54.94%` | `0.82` | 6,810,000,000.00 USD |
| `4H` | `Global Accounts` | `47.03%` | `52.97%` | `0.89` | 22,560,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `2335.75` | `2336.07` | `2335.75` | `2338.75` | `2332.75` | 54,317,401.94 USD | 19,276,795.34 USD | 35,040,606.60 USD | -15,763,811.25 USD | `-29.02%` | `0B / 1S` |
| `0:00 UTC` | `2309.25` | `2313.87` | `2309.25` | `2335.75` | `2302.25` | 493,849,561.51 USD | 204,343,201.57 USD | 289,506,359.94 USD | -85,163,158.37 USD | `-17.24%` | `0B / 20S` |
| `5:00 UTC` | `2315.25` | `2315.75` | `2315.25` | `2318.75` | `2312.25` | 88,922,002.19 USD | 46,836,385.14 USD | 42,085,617.06 USD | 4,750,768.08 USD | `+5.34%` | `3B / 0S` |
| `0:00 UTC` | `2300.25` | `2278.61` | `2300.25` | `2319.25` | `2238.25` | 1,664,912,417.71 USD | 683,261,559.43 USD | 981,650,858.29 USD | -298,389,298.86 USD | `-17.92%` | `1B / 31S` |
| `5:00 UTC` | `2259.25` | `2255.66` | `2259.25` | `2277.25` | `2230.25` | 846,756,637.45 USD | 383,814,230.15 USD | 462,942,407.30 USD | -79,128,177.15 USD | `-9.34%` | `0B / 6S` |
| `0:00 UTC` | `2260.25` | `2257.68` | `2260.25` | `2273.25` | `2245.25` | 606,671,993.02 USD | 300,593,954.86 USD | 306,078,038.17 USD | -5,484,083.31 USD | `-0.90%` | `5B / 2S` |
| `5:00 UTC` | `2281.25` | `2281.90` | `2281.25` | `2293.75` | `2267.75` | 508,254,989.09 USD | 245,674,110.48 USD | 262,580,878.61 USD | -16,906,768.14 USD | `-3.33%` | `3B / 0S` |
| `0:00 UTC` | `2287.25` | `2284.17` | `2287.25` | `2293.25` | `2271.25` | 175,571,332.73 USD | 84,909,600.78 USD | 90,661,731.96 USD | -5,752,131.18 USD | `-3.28%` | `0B / 2S` |
| `5:00 UTC` | `2272.25` | `2272.48` | `2272.25` | `2279.25` | `2266.25` | 164,039,523.36 USD | 80,192,631.79 USD | 83,846,891.57 USD | -3,654,259.77 USD | `-2.23%` | `1B / 3S` |
| `0:00 UTC` | `2265.75` | `2268.13` | `2265.75` | `2272.75` | `2265.25` | 44,290,433.55 USD | 22,458,543.86 USD | 21,831,889.69 USD | 626,654.17 USD | `+1.41%` | `1B / 0S` |

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
| `5m` | 327,490.00 USD | -22,570,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -556,520.00 USD | -27,580,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -2,770,000.00 USD | -57,100,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 2,980,000.00 USD | -35,380,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -79,490,000.00 USD | -971,760,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -86,190,000.00 USD | -1,270,000,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -92,910,000.00 USD | -1,550,000,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -65,620,000.00 USD | -1,250,000,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -73,850,000.00 USD | -1,300,000,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -118,290,000.00 USD | -1,710,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -108,590,000.00 USD | -2,310,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,100,000,000.00 USD | -9,310,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+327.49K` | 15m=`-556.52K` | 1h=`+2.98M` | 24h=`-118.29M`
* Futures Capital Netflows: 5m=`-22.57M` | 15m=`-27.58M` | 1h=`-35.38M` | 24h=`-1.71B`
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
  * `2026-10-30 03:29:54 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:53:54 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:54 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:54 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:29:54 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:29:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:31:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:31:54 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:54 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `2259.73` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2230.29` (Risk Distance: `29.44` pts)
  * +2.5R Take Profit: `2333.33`
  * Mathematical Lot Sizing: **`0.33 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2284.04` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2313.48` (Risk Distance: `29.44` pts)
  * +2.5R Take Profit: `2210.44`
  * Mathematical Lot Sizing: **`0.33 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2273.80`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
