# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 03:55:34 IST` (`2026-10-29 22:25:34 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2272.40` | **Live Ask Quote**: `2275.40` | **Mid Price**: `2273.90`
- **Spread Points**: `300.00` | **Spread BPS**: `13.19 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2315.31` | VWAP Z-Score: `-2.08` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `19.91` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `29.85` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2395.43` | Lower -3.00σ Band: `2235.19`
  * Upper +2.51σ Band: `2382.34` | Lower -2.51σ Band: `2248.27`
  * Upper +2.01σ Band: `2368.99` | Lower -2.01σ Band: `2261.63`
  * Upper +2.00σ Band: `2368.72` | Lower -2.00σ Band: `2261.89`
  * Upper +1.28σ Band: `2349.49` | Lower -1.28σ Band: `2281.12`
  * Upper +1.00σ Band: `2342.02` | Lower -1.00σ Band: `2288.60`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2276.86` | EMA-20=`2296.82` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2314.12` (Slope: `+0.0000`) | EMA-100=`2321.98`
  * Institutional Anchors: EMA-144=`2324.50` | EMA-200=`2325.32` (Slope: `-0.2100`) | EMA-233=`2326.38`
- **Range Boundaries**: 24H High=`2374.90` | 24H Low=`2225.40` | Weekly High=`2387.80` | Weekly Low=`2225.40`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2275.20` (Distance: `-0.03%`)
  * Point of Control (POC) = `2264.08` (Distance: `+0.46%`)
  * Value Area Low (VAL) = `2251.78` (Distance: `+1.01%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2339.52` | POC=`2321.58` | VAL=`2296.66`
  * Prior Day Extremes: PDH=`2374.90` | PDL=`2225.40` | PDC=`2252.70`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2342.87` | Weekly POC=`2310.39` | Weekly VAL=`2299.56`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2289.10` | Low=`2245.20`
  * London Session (08:00-16:00 UTC): High=`2283.00` | Low=`2264.80`
  * New York Session (13:00-21:00 UTC): High=`2287.54` | Low=`2260.26`
  * Initial Balance (First Hour): IB High=`2280.72` | IB Low=`2267.08`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2264.80` - `2283.00`
  * Optimal Trade Entry (OTE 0.705): `2278.45`
  * Structural Invalidation Anchor (0.786): `2292.09`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2265.46` | `2270.64` | `2256.82` | `2268.20` | `21,012` | 47,563,776.50 USD | -2,082,789.72 USD | `-4.38%` | -881,301,164.51 USD | `+0.32` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `2268.21` | `2278.48` | `2264.28` | `2276.64` | `27,163` | 61,701,603.26 USD | 4,771,015.57 USD | `+7.73%` | -876,530,148.94 USD | `+0.60` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `2276.64` | `2276.64` | `2275.73` | `2276.10` | `474` | 1,079,150.37 USD | 129,715.63 USD | `+12.02%` | -876,400,433.30 USD | `+0.25` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `2271.65` | `2279.09` | `2266.41` | `2272.46` | `72,186` | 164,039,523.36 USD | -3,654,259.77 USD | `-2.23%` | -864,470,970.34 USD | `+0.38` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `2272.47` | `2272.73` | `2251.12` | `2265.46` | `140,694` | 318,288,024.78 USD | -14,747,404.45 USD | `-4.63%` | -879,218,374.79 USD | `+0.21` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `2265.46` | `2278.48` | `2256.82` | `2276.78` | `48,734` | 110,537,049.35 USD | 2,974,879.77 USD | `+2.69%` | -876,243,495.01 USD | `+0.47` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `2335.68` | `2335.92` | `2230.20` | `2256.63` | `1,357,980` | 3,094,453,113.46 USD | -457,917,547.62 USD | `-14.80%` | -830,712,434.27 USD | `-3.95` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2256.63` | `2293.87` | `2245.02` | `2272.46` | `640,507` | 1,454,537,838.20 USD | -31,797,242.40 USD | `-2.19%` | -862,509,676.67 USD | `+0.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `2272.47` | `2278.48` | `2251.12` | `2276.10` | `189,343` | 428,632,554.92 USD | -11,929,462.96 USD | `-2.78%` | -874,439,139.63 USD | `+0.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -163,611,405.07 USD | `+1.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -365,767,522.01 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2276.10` | `2,187,830` | 4,977,623,506.58 USD | -501,644,252.98 USD | `-10.08%` | -867,411,774.99 USD | `-1.89` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2308.03` | `2334.83` | `2303.75` | `2309.10` | `525,175` | 1,216,920,375.04 USD | -34,916,746.14 USD | `-2.87%` | -218,489,329.59 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2309.10` | `2330.05` | `2308.88` | `2324.26` | `409,016` | 949,400,649.22 USD | -49,162,247.72 USD | `-5.18%` | -267,651,577.31 USD | `+0.60` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -163,611,405.07 USD | `+1.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -365,767,522.01 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2276.10` | `2,187,830` | 4,977,623,506.58 USD | -501,644,252.98 USD | `-10.08%` | -867,411,774.99 USD | `-1.89` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`2273.90`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2261.10` | `104.0151` | 235,188.54 USD | 9,978,070.80 USD | `7 orders` | `-0.09%` | `-` |
| `BID` | `2261.20` | `428.1068` | 968,035.10 USD | 9,742,882.26 USD | `12 orders` | `-0.08%` | `-` |
| `BID` | `2261.30` | `339.0535` | 766,701.68 USD | 8,774,847.16 USD | `15 orders` | `-0.08%` | `-` |
| `BID` | `2261.40` | `126.5299` | 286,134.72 USD | 8,008,145.49 USD | `12 orders` | `-0.07%` | `-` |
| `BID` | `2261.50` | `162.7279` | 368,009.15 USD | 7,722,010.77 USD | `13 orders` | `-0.07%` | `-` |
| `BID` | `2261.60` | `291.3116` | 658,830.31 USD | 7,354,001.62 USD | `8 orders` | `-0.06%` | `-` |
| `BID` | `2261.70` | `253.3736` | 573,055.07 USD | 6,695,171.31 USD | `9 orders` | `-0.06%` | `-` |
| `BID` | `2261.80` | `345.4315` | 781,296.97 USD | 6,122,116.24 USD | `9 orders` | `-0.06%` | `-` |
| `BID` | `2261.90` | `113.7743` | 257,346.09 USD | 5,340,819.27 USD | `11 orders` | `-0.05%` | `-` |
| `BID` | `2262.00` | `435.9553` | 986,130.89 USD | 5,083,473.18 USD | `11 orders` | `-0.05%` | `-` |
| `BID` | `2262.10` | `583.2282` | 1,319,320.51 USD | 4,097,342.29 USD | `11 orders` | `-0.04%` | `-` |
| `BID` | `2262.20` | `410.8815` | 929,496.13 USD | 2,778,021.78 USD | `13 orders` | `-0.04%` | `-` |
| `BID` | `2262.30` | `82.4631` | 186,556.27 USD | 1,848,525.65 USD | `10 orders` | `-0.03%` | `-` |
| `BID` | `2262.40` | `460.6335` | 1,042,137.23 USD | 1,661,969.38 USD | `16 orders` | `-0.03%` | `-` |
| `BID` | `2262.50` | `30.9893` | 70,113.29 USD | 619,832.15 USD | `8 orders` | `-0.02%` | `-` |
| `BID` | `2262.60` | `123.6596` | 279,792.21 USD | 549,718.86 USD | `15 orders` | `-0.02%` | `-` |
| `BID` | `2262.70` | `30.3865` | 68,755.53 USD | 269,926.65 USD | `14 orders` | `-0.02%` | `-` |
| `BID` | `2262.80` | `62.8425` | 142,200.01 USD | 201,171.12 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `2262.90` | `19.9457` | 45,135.12 USD | 58,971.11 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `2263.00` | `6.1140` | 13,835.98 USD | 13,835.98 USD | `1 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2263.05` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,263.05` | `0.00%` | `-` |
| `ASK` | `2263.10` | `8.5452` | 19,338.64 USD | 19,338.64 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `2263.20` | `39.9282` | 90,365.50 USD | 109,704.14 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `2263.30` | `219.9262` | 497,758.97 USD | 607,463.11 USD | `34 orders` | `+0.01%` | `-` |
| `ASK` | `2263.40` | `85.3111` | 193,093.14 USD | 800,556.26 USD | `35 orders` | `+0.02%` | `-` |
| `ASK` | `2263.50` | `190.3201` | 430,789.55 USD | 1,231,345.80 USD | `12 orders` | `+0.02%` | `-` |
| `ASK` | `2263.60` | `27.4439` | 62,122.01 USD | 1,293,467.81 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `2263.70` | `70.2711` | 159,072.69 USD | 1,452,540.50 USD | `9 orders` | `+0.03%` | `-` |
| `ASK` | `2263.80` | `565.3473` | 1,279,833.22 USD | 2,732,373.72 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `2263.90` | `280.8532` | 635,823.56 USD | 3,368,197.28 USD | `9 orders` | `+0.04%` | `-` |
| `ASK` | `2264.00` | `87.3066` | 197,662.14 USD | 3,565,859.42 USD | `7 orders` | `+0.04%` | `-` |
| `ASK` | `2264.10` | `227.7367` | 515,618.66 USD | 4,081,478.09 USD | `6 orders` | `+0.05%` | `-` |
| `ASK` | `2264.20` | `432.8612` | 980,084.33 USD | 5,061,562.42 USD | `7 orders` | `+0.05%` | `-` |
| `ASK` | `2264.30` | `198.3256` | 449,068.66 USD | 5,510,631.07 USD | `4 orders` | `+0.06%` | `-` |
| `ASK` | `2264.40` | `363.0130` | 822,006.64 USD | 6,332,637.71 USD | `11 orders` | `+0.06%` | `-` |
| `ASK` | `2264.50` | `267.5484` | 605,863.35 USD | 6,938,501.06 USD | `7 orders` | `+0.06%` | `-` |
| `ASK` | `2264.60` | `150.0148` | 339,723.52 USD | 7,278,224.58 USD | `8 orders` | `+0.07%` | `-` |
| `ASK` | `2264.70` | `487.3692` | 1,103,745.03 USD | 8,381,969.60 USD | `5 orders` | `+0.07%` | `-` |
| `ASK` | `2264.80` | `259.1285` | 586,874.23 USD | 8,968,843.83 USD | `6 orders` | `+0.08%` | `-` |
| `ASK` | `2264.90` | `10.3233` | 23,381.24 USD | 8,992,225.07 USD | `3 orders` | `+0.08%` | `-` |
| `ASK` | `2265.00` | `191.5790` | 433,926.43 USD | 9,426,151.51 USD | `10 orders` | `+0.09%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:45:41 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 03:45:41 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1914.18` | `6,500.22` | 12,442,605.92 USD | `AT_RISK_LIQ` | `0xf78c5d8d4b` | `2026-10-30 03:45:41 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1918.00` | `4,184.01` | 8,024,935.59 USD | `TRIGGER_STOP` | `0x6ea486a342` | `2026-10-30 03:45:41 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1925.99` | `8,092.45` | 15,586,021.29 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 03:45:41 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `8,500.00` | 16,371,850.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-30 03:45:41 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2040.72` | `7,964.66` | 16,253,646.32 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-30 03:45:41 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2171.18` | `48,499.51` | 105,301,316.03 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 03:45:41 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2180.25` | `44,734.81` | 97,532,862.28 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2226.80` | `499.60` | 1,112,498.15 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2227.00` | `734.73` | 1,636,235.69 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x646be0d5f9` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2231.60` | `2,042.13` | 4,557,207.94 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2234.10` | `3,412.99` | 7,624,961.18 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2242.30` | `1,469.60` | 3,295,286.99 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:45:41 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2245.00` | `1,758.58` | 3,948,020.86 USD | `TRIGGER_STOP` | `0x28280399d9` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2246.10` | `356.90` | 801,627.47 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2246.60` | `499.31` | 1,121,761.08 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2247.70` | `341.56` | 767,714.52 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2247.90` | `985.82` | 2,216,029.50 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2251.10` | `1,758.61` | 3,958,817.78 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2252.10` | `498.80` | 1,123,338.47 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2253.80` | `1,777.56` | 4,006,269.91 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2254.40` | `339.65` | 765,705.38 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2254.70` | `681.55` | 1,536,700.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2255.30` | `286.70` | 646,589.32 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x07fd7e702b` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2255.40` | `1,332.26` | 3,004,788.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2255.80` | `466.81` | 1,053,025.49 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2257.60` | `887.29` | 2,003,143.19 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2258.00` | `897.42` | 2,026,373.46 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2259.40` | `491.41` | 1,110,293.56 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2259.80` | `664.83` | 1,502,374.02 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2259.90` | `286.70` | 647,908.13 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x07fd7e702b` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2261.00` | `338.58` | 765,536.16 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2261.30` | `442.92` | 1,001,578.39 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2262.20` | `332.03` | 751,113.29 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2267.10` | `331.35` | 751,202.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2268.70` | `441.50` | 1,001,637.86 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2269.70` | `329.10` | 746,952.60 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2271.00` | `270.00` | 613,168.41 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x07fd7e702b` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2271.10` | `882.02` | 2,003,147.67 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2271.50` | `661.42` | 1,502,408.26 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2272.80` | `248.28` | 564,302.15 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2274.30` | `481.83` | 1,095,818.92 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2276.00` | `1,320.20` | 3,004,772.01 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2276.60` | `1,759.82` | 4,006,405.98 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2277.30` | `686.81` | 1,564,069.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2277.30` | `328.03` | 747,018.85 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2277.50` | `467.04` | 1,063,685.88 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2280.20` | `267.26` | 609,406.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x07fd7e702b` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2281.20` | `499.86` | 1,140,282.91 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2285.20` | `1,758.61` | 4,018,786.54 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2286.00` | `1,016.56` | 2,323,846.56 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2288.60` | `499.64` | 1,143,485.26 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2290.20` | `350.03` | 801,627.48 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2290.90` | `335.11` | 767,714.50 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2297.10` | `1,475.84` | 3,390,147.01 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2302.80` | `3,405.12` | 7,841,314.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2306.10` | `2,125.61` | 4,901,867.38 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2306.50` | `1,554.55` | 3,585,566.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xbc76170c8a` | `2026-10-30 03:45:41 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2306.50` | `1,492.37` | 3,442,144.02 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xbc76170c8a` | `2026-10-30 03:45:41 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2389.41` | `17,632.57` | 42,131,523.40 USD | `AT_RISK_LIQ` | `0x8added25f8` | `2026-10-30 03:45:41 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2500.10` | `1,000.00` | 2,500,100.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 03:45:41 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `3,045.71` | 7,656,616.15 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-30 03:45:41 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2585.94` | `6,224.05` | 16,095,020.42 USD | `AT_RISK_LIQ` | `0x08bf75d170` | `2026-10-30 03:45:41 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2658.69` | `9,700.00` | 25,789,336.01 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-30 03:45:41 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2709.05` | `8,500.00` | 23,026,898.55 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-30 03:45:41 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 242,164,143.61 USD | `106,417.71` | `2322.74` | `2258.60` | `3943.44` | 5,016,868.55 USD | `+2.07%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 146,307,562.89 USD | `64,680.62` | `2375.30` | `2258.60` | `4657.28` | 7,328,734.60 USD | `+5.01%` | `5X Cross` |
| `6` | `0x77dd...e0e9` | `LONG` | 109,671,946.26 USD | `48,499.51` | `2610.31` | `2258.60` | `2171.15` | -16,926,937.61 USD | `-15.43%` | `10X Cross` |
| `8` | `0x0392...d7d9` | `LONG` | 101,190,147.91 USD | `44,734.81` | `2518.71` | `2258.60` | `2180.21` | -11,484,158.66 USD | `-11.35%` | `9X Cross` |
| `14` | `0xde8d...9524` | `LONG` | 68,853,100.84 USD | `30,282.40` | `2134.45` | `2258.60` | `1787.13` | 4,216,770.26 USD | `+6.12%` | `20X Cross` |
| `23` | `0xdf95...7d72` | `SHORT` | 50,941,551.84 USD | `22,530.54` | `2402.53` | `2258.60` | `4072.46` | 3,188,850.27 USD | `+6.26%` | `25X Cross` |
| `24` | `0x8add...7d2c` | `SHORT` | 49,956,271.92 USD | `22,046.99` | `2271.09` | `2258.60` | `2333.57` | 114,625.38 USD | `+0.23%` | `25X Cross` |
| `32` | `0x7fda...17d1` | `SHORT` | 39,902,584.95 USD | `17,648.20` | `2433.32` | `2258.60` | `4696.77` | 3,041,245.28 USD | `+7.62%` | `25X Cross` |
| `35` | `0xeced...6210` | `SHORT` | 37,832,404.23 USD | `16,687.58` | `2522.09` | `2258.60` | `3478.35` | 4,255,310.77 USD | `+11.25%` | `20X Cross` |
| `36` | `0xb695...a92d` | `SHORT` | 37,774,156.08 USD | `16,704.62` | `2557.74` | `2258.60` | `3854.56` | 4,952,008.97 USD | `+13.11%` | `20X Cross` |
| `37` | `0xe813...6d74` | `LONG` | 36,164,291.83 USD | `15,979.98` | `2253.24` | `2258.60` | `876.89` | 157,415.53 USD | `+0.44%` | `25X Cross` |
| `38` | `0x6046...b21d` | `LONG` | 36,004,316.52 USD | `15,927.59` | `2410.19` | `2258.60` | `1714.32` | -2,384,303.13 USD | `-6.62%` | `6X Cross` |
| `42` | `0x45d2...4029` | `SHORT` | 31,545,135.00 USD | `13,950.00` | `2443.60` | `2258.60` | `5332.57` | 2,543,147.46 USD | `+8.06%` | `20X Cross` |
| `46` | `0x2371...0883` | `LONG` | 27,144,000.00 USD | `12,000.00` | `2421.77` | `2258.60` | `1280.07` | -1,917,294.85 USD | `-7.06%` | `20X Cross` |
| `47` | `0xbd1c...ff0e` | `LONG` | 27,136,800.00 USD | `12,000.00` | `2419.91` | `2258.60` | `1520.98` | -1,902,232.39 USD | `-7.01%` | `20X Cross` |
| `57` | `0xa9de...e049` | `LONG` | 24,924,900.00 USD | `11,000.00` | `2481.81` | `2258.60` | `1644.72` | -2,375,079.46 USD | `-9.53%` | `20X Cross` |
| `58` | `0x09dc...c094` | `LONG` | 24,895,310.00 USD | `11,000.00` | `2465.31` | `2258.60` | `1638.04` | -2,223,113.04 USD | `-8.93%` | `20X Cross` |
| `59` | `0x6c93...59a4` | `LONG` | 24,875,400.00 USD | `11,000.00` | `2441.15` | `2258.60` | `1603.01` | -1,977,272.73 USD | `-7.95%` | `20X Cross` |
| `60` | `0x0c5d...36b3` | `LONG` | 24,865,500.00 USD | `11,000.00` | `2482.20` | `2258.60` | `1645.05` | -2,438,753.24 USD | `-9.81%` | `20X Cross` |
| `62` | `0xa61c...66b9` | `LONG` | 24,622,123.20 USD | `10,888.00` | `2398.32` | `2258.60` | `1511.74` | -1,490,834.19 USD | `-6.05%` | `10X Cross` |
| `72` | `0xa2ce...3126` | `LONG` | 22,653,163.26 USD | `10,016.88` | `2162.83` | `2258.60` | `1522.36` | 988,361.22 USD | `+4.36%` | `10X Cross` |
| `73` | `0xec7f...df39` | `LONG` | 22,632,100.00 USD | `10,000.00` | `2719.35` | `2258.60` | `1721.57` | -4,561,448.52 USD | `-20.15%` | `20X Cross` |
| `75` | `0x6646...6de5` | `LONG` | 22,614,000.00 USD | `10,000.00` | `1765.80` | `2258.60` | `1720.62` | 4,955,942.55 USD | `+21.92%` | `25X Cross` |
| `76` | `0x15a4...dfdb` | `LONG` | 22,514,000.00 USD | `10,000.00` | `1761.94` | `2258.60` | `234.62` | 4,894,518.97 USD | `+21.74%` | `20X Cross` |
| `79` | `0xaeaa...2416` | `SHORT` | 21,936,550.00 USD | `9,700.00` | `2311.92` | `2258.60` | `2658.66` | 489,132.40 USD | `+2.23%` | `25X Cross` |
| `85` | `0xca49...53c8` | `SHORT` | 20,943,715.75 USD | `9,264.26` | `2549.47` | `2258.60` | `3853.52` | 2,675,308.99 USD | `+12.77%` | `25X Cross` |
| `87` | `0xba5d...a352` | `SHORT` | 20,526,600.21 USD | `9,054.12` | `2493.89` | `2258.60` | `2923.49` | 2,053,407.05 USD | `+10.00%` | `20X Cross` |
| `88` | `0xea00...a918` | `LONG` | 20,366,655.09 USD | `9,003.83` | `2003.01` | `2258.60` | `1399.34` | 2,331,876.23 USD | `+11.45%` | `5X Cross` |
| `92` | `0xefe4...194b` | `SHORT` | 19,951,255.65 USD | `8,820.57` | `2267.42` | `2258.60` | `3882.16` | 48,758.74 USD | `+0.24%` | `20X Cross` |
| `100` | `0xb37f...66ca` | `SHORT` | 19,221,050.00 USD | `8,500.00` | `2308.30` | `2258.60` | `2709.01` | 399,504.19 USD | `+2.08%` | `25X Cross` |
| `113` | `0x9eec...daab` | `LONG` | 18,299,461.93 USD | `8,092.45` | `1658.44` | `2258.60` | `1927.31` | 4,878,597.41 USD | `+26.66%` | `15X Cross` |
| `116` | `0x5f91...65aa` | `LONG` | 18,014,458.71 USD | `7,964.66` | `1626.99` | `2258.60` | `2040.68` | 5,056,015.65 USD | `+28.07%` | `16X Cross` |
| `118` | `0x218a...7da2` | `SHORT` | 17,829,334.51 USD | `7,877.58` | `2208.16` | `2258.60` | `2824.98` | -434,360.27 USD | `-2.44%` | `10X Cross` |
| `120` | `0xcf53...ee11` | `SHORT` | 17,202,447.76 USD | `7,603.63` | `1862.69` | `2258.60` | `4017.32` | -3,039,183.82 USD | `-17.67%` | `7X Cross` |
| `125` | `0x939f...04d2` | `LONG` | 16,310,647.15 USD | `7,223.81` | `2500.18` | `2258.60` | `1628.62` | -1,750,243.03 USD | `-10.73%` | `25X Cross` |
| `127` | `0xec0b...b078` | `LONG` | 15,847,436.43 USD | `7,007.80` | `2065.97` | `2258.60` | `1043.12` | 1,369,506.84 USD | `+8.64%` | `25X Cross` |
| `131` | `0x4487...c92d` | `SHORT` | 15,693,880.39 USD | `6,937.44` | `2359.13` | `2258.60` | `2792.41` | 672,495.07 USD | `+4.29%` | `10X Cross` |
| `134` | `0x418a...8888` | `SHORT` | 15,219,295.59 USD | `6,724.38` | `2494.55` | `2258.60` | `3003.81` | 1,555,027.58 USD | `+10.22%` | `25X Cross` |
| `136` | `0x0622...8088` | `LONG` | 14,943,149.85 USD | `6,598.29` | `2272.20` | `2258.60` | `744.46` | -49,491.81 USD | `-0.33%` | `5X Cross` |
| `137` | `0x4ff9...38d3` | `LONG` | 14,851,273.31 USD | `6,564.10` | `2447.40` | `2258.60` | `1670.66` | -1,213,749.44 USD | `-8.17%` | `3X Isolated` |
| `139` | `0xf78c...c581` | `LONG` | 14,702,851.01 USD | `6,500.22` | `2521.53` | `2258.60` | `1914.14` | -1,687,689.94 USD | `-11.48%` | `20X Cross` |
| `144` | `0x799f...5f4c` | `LONG` | 14,271,476.72 USD | `6,310.90` | `2390.33` | `2258.60` | `1819.48` | -813,687.89 USD | `-5.70%` | `20X Cross` |
| `146` | `0xecb6...2b00` | `SHORT` | 14,189,891.60 USD | `6,282.05` | `2280.21` | `2258.60` | `6919.43` | 134,551.54 USD | `+0.95%` | `15X Cross` |
| `149` | `0x08bf...7872` | `SHORT` | 14,073,815.98 USD | `6,224.05` | `2258.00` | `2258.60` | `2585.91` | -19,899.87 USD | `-0.14%` | `20X Cross` |
| `153` | `0xc179...e0c8` | `LONG` | 13,822,878.77 USD | `6,113.61` | `2322.20` | `2258.60` | `1150.79` | -374,171.72 USD | `-2.71%` | `10X Cross` |
| `154` | `0x0c4a...1b19` | `LONG` | 13,794,753.01 USD | `6,086.13` | `2373.06` | `2258.60` | `2135.30` | -647,997.56 USD | `-4.70%` | `25X Isolated` |
| `158` | `0xd9e7...4aff` | `LONG` | 13,595,400.00 USD | `6,000.00` | `2480.18` | `2258.60` | `1408.43` | -1,285,724.33 USD | `-9.46%` | `20X Cross` |
| `168` | `0x1ee7...edf5` | `LONG` | 12,439,900.00 USD | `5,500.00` | `2316.93` | `2258.60` | `2127.33` | -303,239.62 USD | `-2.44%` | `25X Cross` |
| `189` | `0x45ab...6cbc` | `LONG` | 11,130,232.30 USD | `4,920.96` | `2727.66` | `2258.60` | `1387.52` | -2,292,511.49 USD | `-20.60%` | `7X Cross` |
| `191` | `0x645b...87b8` | `SHORT` | 11,069,304.77 USD | `4,895.76` | `2421.64` | `2258.60` | `6676.99` | 786,482.79 USD | `+7.11%` | `10X Cross` |
| `193` | `0x64b7...9da9` | `LONG` | 10,983,256.17 USD | `4,856.84` | `2604.61` | `2258.60` | `1530.35` | -1,666,958.25 USD | `-15.18%` | `25X Cross` |
| `195` | `0xfb18...eb17` | `SHORT` | 10,959,467.09 USD | `4,845.89` | `2315.54` | `2258.60` | `2628.79` | 261,415.70 USD | `+2.39%` | `25X Cross` |
| `201` | `0x5559...d43b` | `SHORT` | 10,750,769.14 USD | `4,755.93` | `2262.69` | `2258.60` | `2805.93` | 10,436.74 USD | `+0.10%` | `25X Cross` |
| `204` | `0x12d2...f97f` | `LONG` | 10,648,917.50 USD | `4,708.79` | `2588.61` | `2258.60` | `2010.48` | -1,540,316.81 USD | `-14.46%` | `20X Cross` |
| `214` | `0xe091...6705` | `SHORT` | 10,226,700.45 USD | `4,500.00` | `2467.33` | `2258.60` | `2572.99` | 876,308.05 USD | `+8.57%` | `20X Cross` |
| `238` | `0x28bb...fca6` | `SHORT` | 9,520,042.51 USD | `4,209.61` | `1896.10` | `2258.60` | `3039.84` | -1,538,159.95 USD | `-16.16%` | `20X Cross` |
| `240` | `0x6ea4...0ea7` | `SHORT` | 9,480,553.47 USD | `4,184.01` | `2602.13` | `2258.60` | `3425.97` | 1,406,793.20 USD | `+14.84%` | `20X Cross` |
| `253` | `0x5e9e...35ee` | `SHORT` | 9,059,881.17 USD | `4,007.56` | `1796.39` | `2258.60` | `2586.46` | -1,860,731.08 USD | `-20.54%` | `20X Cross` |
| `254` | `0xfb94...0ddf` | `SHORT` | 9,052,352.93 USD | `4,002.10` | `2382.44` | `2258.60` | `5105.36` | 482,431.22 USD | `+5.33%` | `20X Cross` |
| `255` | `0x3dc9...54b0` | `SHORT` | 9,047,299.23 USD | `3,999.69` | `2480.32` | `2258.60` | `6527.53` | 873,237.32 USD | `+9.65%` | `20X Cross` |
| `257` | `0x8cc9...2b6a` | `SHORT` | 9,037,200.00 USD | `4,000.00` | `1791.18` | `2258.60` | `3853.05` | -1,872,453.33 USD | `-20.72%` | `25X Cross` |
| `268` | `0xf02d...5eb3` | `LONG` | 8,719,925.61 USD | `3,855.99` | `2513.67` | `2258.60` | `313.37` | -972,786.70 USD | `-11.16%` | `20X Cross` |
| `274` | `0x4b67...f4e7` | `LONG` | 8,642,362.29 USD | `3,820.84` | `2591.51` | `2258.60` | `1662.11` | -1,259,411.25 USD | `-14.57%` | `20X Cross` |
| `286` | `0xb829...3a81` | `LONG` | 8,282,813.16 USD | `3,661.88` | `2424.26` | `2258.60` | `1358.46` | -594,571.85 USD | `-7.18%` | `20X Cross` |
| `296` | `0x8ae4...3d60` | `LONG` | 8,050,423.65 USD | `3,558.20` | `2482.21` | `2258.60` | `489.92` | -781,774.38 USD | `-9.71%` | `10X Cross` |
| `317` | `0xfe7c...b7ae` | `SHORT` | 7,696,301.58 USD | `3,402.58` | `2440.17` | `2258.60` | `5161.09` | 606,607.68 USD | `+7.88%` | `25X Cross` |
| `331` | `0xbc76...417c` | `LONG` | 7,030,913.31 USD | `3,109.10` | `2263.46` | `2258.60` | `2216.94` | -6,411.76 USD | `-0.09%` | `25X Cross` |
| `337` | `0x9c2a...f6a8` | `SHORT` | 6,889,096.65 USD | `3,045.71` | `2543.83` | `2258.60` | `2602.21` | 858,689.90 USD | `+12.46%` | `20X Cross` |
| `342` | `0x007d...67a0` | `LONG` | 6,784,800.00 USD | `3,000.00` | `2400.00` | `2258.60` | `1472.15` | -415,200.00 USD | `-6.12%` | `25X Cross` |
| `343` | `0x4a20...3c26` | `LONG` | 6,783,900.00 USD | `3,000.00` | `2428.72` | `2258.60` | `566.60` | -502,260.28 USD | `-7.40%` | `20X Cross` |
| `383` | `0xf517...c032` | `SHORT` | 6,191,872.18 USD | `2,738.07` | `2053.90` | `2258.60` | `5326.29` | -568,130.27 USD | `-9.18%` | `25X Cross` |
| `399` | `0x8328...f54a` | `SHORT` | 5,839,784.06 USD | `2,576.45` | `2292.01` | `2258.60` | `3280.20` | 65,487.22 USD | `+1.12%` | `25X Cross` |
| `400` | `0xed48...7c9b` | `SHORT` | 5,768,616.29 USD | `2,551.13` | `2460.02` | `2258.60` | `3236.23` | 507,230.12 USD | `+8.79%` | `20X Cross` |
| `414` | `0xfbe2...c8ea` | `SHORT` | 5,436,338.87 USD | `2,404.08` | `2041.57` | `2258.60` | `2608.90` | -528,246.14 USD | `-9.72%` | `20X Cross` |
| `422` | `0x1c98...7fc7` | `LONG` | 5,344,629.42 USD | `2,358.00` | `2467.15` | `2258.60` | `1897.18` | -472,942.06 USD | `-8.85%` | `10X Cross` |
| `427` | `0x77ee...2902` | `SHORT` | 5,182,688.84 USD | `2,290.69` | `2476.53` | `2258.60` | `5815.66` | 490,283.40 USD | `+9.46%` | `25X Cross` |
| `437` | `0x023a...2355` | `LONG` | 5,048,465.86 USD | `2,232.35` | `2330.15` | `2258.60` | `0.000000` | -153,262.88 USD | `-3.04%` | `25X Cross` |
| `439` | `0x6859...7e1e` | `SHORT` | 5,030,662.95 USD | `2,224.58` | `2200.39` | `2258.60` | `3539.04` | -135,710.22 USD | `-2.70%` | `25X Cross` |
| `448` | `0xd507...c948` | `SHORT` | 4,911,760.57 USD | `2,172.00` | `2387.49` | `2258.60` | `2707.39` | 273,880.45 USD | `+5.58%` | `5X Isolated` |
| `456` | `0x382b...3e39` | `SHORT` | 4,816,810.14 USD | `2,129.54` | `2296.66` | `2258.60` | `4621.68` | 74,027.07 USD | `+1.54%` | `25X Cross` |
| `484` | `0xc619...10f5` | `LONG` | 4,531,800.00 USD | `2,000.00` | `2318.40` | `2258.60` | `1799.22` | -105,006.86 USD | `-2.32%` | `25X Cross` |
| `486` | `0x7a6d...f79c` | `SHORT` | 4,525,800.00 USD | `2,000.00` | `2418.41` | `2258.60` | `2655.85` | 311,032.11 USD | `+6.87%` | `25X Cross` |
| `487` | `0xf929...d1f9` | `SHORT` | 4,525,000.00 USD | `2,000.00` | `2423.37` | `2258.60` | `2548.79` | 321,740.34 USD | `+7.11%` | `25X Cross` |
| `489` | `0x3440...32c5` | `SHORT` | 4,524,078.14 USD | `2,000.57` | `2198.21` | `2258.60` | `3659.75` | -126,415.01 USD | `-2.79%` | `25X Cross` |
| `490` | `0xbb34...1696` | `LONG` | 4,523,600.00 USD | `2,000.00` | `2318.80` | `2258.60` | `1959.76` | -114,016.04 USD | `-2.52%` | `25X Cross` |
| `503` | `0x0514...bdfe` | `SHORT` | 4,409,925.00 USD | `1,950.00` | `1988.74` | `2258.60` | `3066.41` | -531,865.37 USD | `-12.06%` | `25X Cross` |
| `510` | `0x8376...9a1e` | `SHORT` | 4,321,159.85 USD | `1,910.50` | `2477.72` | `2258.60` | `3182.24` | 412,528.32 USD | `+9.55%` | `20X Cross` |
| `518` | `0xfc27...9d9d` | `SHORT` | 4,229,762.80 USD | `1,867.36` | `2341.25` | `2258.60` | `11690.58` | 142,210.95 USD | `+3.36%` | `25X Cross` |
| `540` | `0x541e...071d` | `SHORT` | 4,082,729.50 USD | `1,805.00` | `2648.19` | `2258.60` | `3174.61` | 697,255.34 USD | `+17.08%` | `25X Cross` |
| `541` | `0x7265...91a5` | `LONG` | 4,076,729.52 USD | `1,801.87` | `2533.96` | `2258.60` | `1988.11` | -489,136.94 USD | `-12.00%` | `20X Cross` |
| `542` | `0x739c...cfb2` | `SHORT` | 4,071,420.00 USD | `1,800.00` | `2427.60` | `2258.60` | `2496.32` | 298,276.38 USD | `+7.33%` | `25X Cross` |
| `543` | `0xb15b...dbae` | `SHORT` | 4,067,241.95 USD | `1,797.68` | `2294.54` | `2258.60` | `2302.38` | 57,602.02 USD | `+1.42%` | `25X Cross` |
| `551` | `0xa445...329d` | `LONG` | 4,017,763.19 USD | `1,776.75` | `2398.85` | `2258.60` | `1949.44` | -244,406.16 USD | `-6.08%` | `25X Cross` |
| `554` | `0x91a9...3f70` | `SHORT` | 3,998,039.76 USD | `1,767.48` | `2156.23` | `2258.60` | `3661.12` | -186,935.68 USD | `-4.68%` | `4X Cross` |
| `558` | `0x2828...93a0` | `LONG` | 3,984,775.26 USD | `1,758.58` | `2314.00` | `2258.60` | `2241.71` | -84,591.60 USD | `-2.12%` | `25X Cross` |
| `566` | `0x3453...b323` | `SHORT` | 3,958,778.45 USD | `1,750.12` | `2328.82` | `2258.60` | `2438.85` | 116,953.68 USD | `+2.95%` | `25X Cross` |
| `592` | `0xfeec...4e9c` | `SHORT` | 3,825,856.42 USD | `1,691.81` | `2566.49` | `2258.60` | `2654.41` | 516,168.09 USD | `+13.49%` | `10X Cross` |
| `593` | `0x936c...bb0f` | `SHORT` | 3,819,638.86 USD | `1,688.69` | `2434.60` | `2258.60` | `4530.07` | 291,648.24 USD | `+7.64%` | `20X Cross` |
| `614` | `0xeee0...0b53` | `LONG` | 3,703,010.55 USD | `1,637.12` | `2468.64` | `2258.60` | `214.37` | -338,465.51 USD | `-9.14%` | `7X Cross` |
| `619` | `0x27b8...12fc` | `LONG` | 3,685,738.28 USD | `1,628.12` | `2468.73` | `2258.60` | `576.49` | -333,656.35 USD | `-9.05%` | `10X Cross` |
| `621` | `0x982b...4606` | `LONG` | 3,679,535.37 USD | `1,626.82` | `2575.24` | `2258.60` | `1548.39` | -509,917.71 USD | `-13.86%` | `5X Isolated` |
| `631` | `0x73d7...8be1` | `LONG` | 3,620,433.06 USD | `1,601.47` | `2410.40` | `2258.60` | `2021.76` | -239,745.87 USD | `-6.62%` | `25X Cross` |
| `643` | `0x39b4...5c34` | `SHORT` | 3,517,385.24 USD | `1,555.06` | `2329.97` | `2258.60` | `2536.05` | 105,857.96 USD | `+3.01%` | `25X Cross` |
| `654` | `0xe170...9300` | `SHORT` | 3,466,250.70 USD | `1,533.40` | `2076.39` | `2258.60` | `3153.38` | -282,301.20 USD | `-8.14%` | `25X Cross` |
| `657` | `0x4b86...df9d` | `SHORT` | 3,453,231.60 USD | `1,524.00` | `2287.40` | `2258.60` | `2760.56` | 32,766.00 USD | `+0.95%` | `9X Isolated` |
| `669` | `0xad54...6203` | `LONG` | 3,417,030.67 USD | `1,510.29` | `2614.66` | `2258.60` | `2124.61` | -531,875.87 USD | `-15.57%` | `10X Isolated` |
| `670` | `0x2e2b...2fab` | `LONG` | 3,409,536.04 USD | `1,507.38` | `2245.53` | `2258.60` | `1238.50` | 24,662.94 USD | `+0.72%` | `25X Cross` |
| `674` | `0x251f...6e5d` | `LONG` | 3,392,100.00 USD | `1,500.00` | `2346.68` | `2258.60` | `1884.51` | -127,930.49 USD | `-3.77%` | `20X Cross` |
| `688` | `0xb885...3c54` | `LONG` | 3,278,019.97 USD | `1,450.00` | `2274.34` | `2258.60` | `39.04` | -19,788.16 USD | `-0.60%` | `20X Cross` |
| `694` | `0xef70...a84c` | `SHORT` | 3,262,764.20 USD | `1,442.74` | `2424.73` | `2258.60` | `3266.33` | 235,506.63 USD | `+7.22%` | `25X Cross` |
| `699` | `0x4b5f...0dd8` | `LONG` | 3,239,086.28 USD | `1,431.96` | `2339.45` | `2258.60` | `2148.67` | -110,906.66 USD | `-3.42%` | `10X Cross` |
| `701` | `0xbadb...9ee6` | `LONG` | 3,228,355.68 USD | `1,428.16` | `1936.00` | `2258.60` | `1065.82` | 463,434.03 USD | `+14.36%` | `20X Cross` |
| `741` | `0xa0fb...96be` | `LONG` | 3,098,910.23 USD | `1,376.25` | `2293.96` | `2258.60` | `1549.91` | -58,164.66 USD | `-1.88%` | `3X Cross` |
| `763` | `0x880a...311c` | `SHORT` | 2,986,080.61 USD | `1,320.22` | `2425.76` | `2258.60` | `8368.59` | 216,468.55 USD | `+7.25%` | `9X Cross` |
| `771` | `0x0dd5...f6ee` | `LONG` | 2,960,591.00 USD | `1,315.00` | `2306.05` | `2258.60` | `1654.14` | -71,873.38 USD | `-2.43%` | `5X Cross` |
| `804` | `0xc435...c905` | `SHORT` | 2,817,859.20 USD | `1,248.00` | `2704.38` | `2258.60` | `4237.21` | 557,211.15 USD | `+19.77%` | `20X Cross` |
| `825` | `0x7178...0854` | `LONG` | 2,750,451.30 USD | `1,218.63` | `2461.81` | `2258.60` | `1165.18` | -249,595.11 USD | `-9.07%` | `10X Cross` |
| `834` | `0xaaa1...ab8c` | `SHORT` | 2,714,160.00 USD | `1,200.00` | `2276.29` | `2258.60` | `2366.18` | 17,397.58 USD | `+0.64%` | `25X Isolated` |
| `851` | `0x07fd...689d` | `LONG` | 2,638,026.63 USD | `1,166.49` | `2419.97` | `2258.60` | `0.000000` | -184,865.17 USD | `-7.01%` | `25X Cross` |
| `894` | `0xbef3...0d3e` | `LONG` | 2,508,934.49 USD | `1,103.99` | `2315.08` | `2258.60` | `2162.38` | -46,901.67 USD | `-1.87%` | `20X Cross` |
| `906` | `0x6a41...a3b9` | `LONG` | 2,485,193.12 USD | `1,099.06` | `2314.77` | `2258.60` | `2164.18` | -58,879.58 USD | `-2.37%` | `20X Cross` |
| `914` | `0x2f80...f203` | `SHORT` | 2,465,144.86 USD | `1,088.94` | `1984.00` | `2258.60` | `3062.73` | -304,677.67 USD | `-12.36%` | `20X Cross` |
| `924` | `0x6f11...0389` | `SHORT` | 2,440,158.50 USD | `1,079.00` | `2333.39` | `2258.60` | `3199.66` | 77,570.41 USD | `+3.18%` | `25X Cross` |
| `928` | `0x2b61...2f6c` | `SHORT` | 2,434,078.61 USD | `1,076.60` | `2681.75` | `2258.60` | `6503.21` | 453,094.13 USD | `+18.61%` | `10X Cross` |
| `963` | `0x30af...393e` | `SHORT` | 2,354,594.42 USD | `1,041.16` | `2252.26` | `2258.60` | `2297.87` | -9,612.09 USD | `-0.41%` | `25X Cross` |
| `972` | `0x1b2a...f7a6` | `LONG` | 2,319,279.88 USD | `1,025.37` | `2737.51` | `2258.60` | `883.05` | -487,680.06 USD | `-21.03%` | `10X Cross` |
| `984` | `0x001a...fef6` | `SHORT` | 2,277,763.29 USD | `1,007.33` | `2022.19` | `2258.60` | `3078.49` | -240,755.33 USD | `-10.57%` | `10X Cross` |
| `985` | `0x02aa...1806` | `SHORT` | 2,277,556.88 USD | `1,007.10` | `2654.68` | `2258.60` | `3613.65` | 395,975.23 USD | `+17.39%` | `20X Cross` |
| `988` | `0xdb3a...cf3b` | `LONG` | 2,268,770.95 USD | `1,003.22` | `2705.01` | `2258.60` | `0.000000` | -444,935.95 USD | `-19.61%` | `4X Cross` |
| `989` | `0x834c...dd93` | `SHORT` | 2,266,600.00 USD | `1,000.00` | `2249.68` | `2258.60` | `2310.88` | -16,914.58 USD | `-0.75%` | `25X Cross` |
| `992` | `0x7743...e4fe` | `SHORT` | 2,262,757.85 USD | `1,000.56` | `2298.56` | `2258.60` | `4974.41` | 37,087.23 USD | `+1.64%` | `25X Cross` |
| `993` | `0x5272...fcd9` | `SHORT` | 2,261,200.00 USD | `1,000.00` | `2241.82` | `2258.60` | `2831.71` | -19,375.51 USD | `-0.86%` | `5X Cross` |
| `1018` | `0x1f16...6d07` | `LONG` | 2,184,319.20 USD | `966.00` | `2278.41` | `2258.60` | `1647.23` | -16,629.94 USD | `-0.76%` | `7X Cross` |
| `1024` | `0xb002...ed8a` | `SHORT` | 2,173,003.49 USD | `962.78` | `2299.66` | `2258.60` | `4199.87` | 41,074.42 USD | `+1.89%` | `25X Cross` |
| `1066` | `0x9606...4e5d` | `SHORT` | 2,060,633.55 USD | `913.00` | `2478.70` | `2258.60` | `4313.84` | 202,420.05 USD | `+9.82%` | `20X Cross` |
| `1078` | `0x5f10...d49d` | `LONG` | 2,035,080.00 USD | `900.00` | `2249.83` | `2258.60` | `1813.09` | 10,226.53 USD | `+0.50%` | `25X Cross` |
| `1104` | `0x2e30...4cb5` | `SHORT` | 2,000,387.40 USD | `884.85` | `2340.07` | `2258.60` | `7886.28` | 70,231.42 USD | `+3.51%` | `2X Cross` |
| `1117` | `0x31de...13f2` | `LONG` | 1,987,681.08 USD | `879.78` | `2273.48` | `2258.60` | `0.000000` | -12,476.35 USD | `-0.63%` | `20X Cross` |
| `1163` | `0x7b7f...dee2` | `LONG` | 1,922,264.32 USD | `850.52` | `2268.61` | `2258.60` | `0.000000` | -7,245.73 USD | `-0.38%` | `20X Cross` |
| `1183` | `0xcd27...52a8` | `LONG` | 1,893,346.57 USD | `837.21` | `2553.56` | `2258.60` | `1404.20` | -244,518.20 USD | `-12.91%` | `2X Cross` |
| `1200` | `0x6ff1...8575` | `LONG` | 1,852,465.61 USD | `814.06` | `2272.53` | `2258.60` | `2227.12` | 2,495.85 USD | `+0.13%` | `25X Isolated` |
| `1229` | `0x7737...bf66` | `SHORT` | 1,820,726.26 USD | `799.79` | `2494.83` | `2258.60` | `23913.51` | 174,619.77 USD | `+9.59%` | `15X Cross` |
| `1231` | `0x3fc5...c0c1` | `SHORT` | 1,819,151.62 USD | `804.26` | `2702.11` | `2258.60` | `5012.93` | 354,049.91 USD | `+19.46%` | `25X Cross` |
| `1236` | `0xd911...961e` | `LONG` | 1,812,498.63 USD | `801.35` | `2268.25` | `2258.60` | `0.000000` | -5,176.22 USD | `-0.29%` | `25X Cross` |
| `1240` | `0x04a9...95aa` | `LONG` | 1,809,200.00 USD | `800.00` | `2595.13` | `2258.60` | `1883.95` | -266,906.74 USD | `-14.75%` | `5X Cross` |
| `1254` | `0x0a97...347d` | `LONG` | 1,788,659.08 USD | `790.95` | `2268.87` | `2258.60` | `1291.50` | -5,913.04 USD | `-0.33%` | `20X Cross` |
| `1256` | `0xf83f...625f` | `SHORT` | 1,787,003.28 USD | `790.22` | `2595.19` | `2258.60` | `6196.75` | 263,768.48 USD | `+14.76%` | `20X Cross` |
| `1257` | `0xa70a...4be9` | `LONG` | 1,785,612.29 USD | `789.60` | `2268.76` | `2258.60` | `386.16` | -5,816.00 USD | `-0.33%` | `20X Cross` |
| `1258` | `0x2577...4897` | `LONG` | 1,784,000.00 USD | `789.03` | `2298.10` | `2258.60` | `0.000000` | -29,279.37 USD | `-1.64%` | `15X Cross` |
| `1273` | `0x6e6f...82a6` | `LONG` | 1,772,264.28 USD | `783.67` | `2267.17` | `2258.60` | `939.75` | -4,447.42 USD | `-0.25%` | `20X Cross` |
| `1286` | `0x458d...ab3b` | `LONG` | 1,745,350.04 USD | `774.75` | `2740.41` | `2258.60` | `1887.95` | -377,779.14 USD | `-21.64%` | `3X Isolated` |
| `1340` | `0xaa53...9cb7` | `LONG` | 1,651,437.35 USD | `730.34` | `2389.70` | `2258.60` | `1934.83` | -93,852.29 USD | `-5.68%` | `20X Cross` |
| `1365` | `0xa189...94d7` | `SHORT` | 1,628,088.51 USD | `719.98` | `2691.84` | `2258.60` | `3051.91` | 309,984.15 USD | `+19.04%` | `25X Cross` |
| `1381` | `0x2f93...4404` | `LONG` | 1,599,946.80 USD | `707.47` | `1700.45` | `2258.60` | `1369.59` | 396,920.42 USD | `+24.81%` | `4X Isolated` |
| `1389` | `0x5605...fe0f` | `SHORT` | 1,584,738.11 USD | `702.14` | `2566.90` | `2258.60` | `3070.92` | 217,594.54 USD | `+13.73%` | `20X Cross` |
| `1391` | `0x0deb...0bc5` | `LONG` | 1,582,840.00 USD | `700.00` | `2071.05` | `2258.60` | `1598.18` | 133,104.21 USD | `+8.41%` | `20X Cross` |
| `1446` | `0xdbd1...29dd` | `SHORT` | 1,539,885.20 USD | `680.70` | `3030.57` | `2258.60` | `4093.39` | 523,035.93 USD | `+33.97%` | `6X Cross` |
| `1449` | `0xb1ec...e86a` | `SHORT` | 1,536,497.59 USD | `679.30` | `2271.56` | `2258.60` | `16463.61` | 6,565.65 USD | `+0.43%` | `25X Cross` |
| `1453` | `0x71e5...be04` | `LONG` | 1,532,340.17 USD | `677.67` | `2727.27` | `2258.60` | `1471.73` | -315,845.44 USD | `-20.61%` | `20X Cross` |
| `1455` | `0x51a0...3543` | `SHORT` | 1,531,038.72 USD | `676.88` | `2627.71` | `2258.60` | `7827.12` | 247,610.57 USD | `+16.17%` | `20X Cross` |
| `1457` | `0xb8eb...1dd5` | `LONG` | 1,525,115.98 USD | `674.41` | `2267.05` | `2258.60` | `0.000000` | -3,812.52 USD | `-0.25%` | `25X Cross` |
| `1460` | `0x0b23...f37b` | `LONG` | 1,523,475.00 USD | `675.00` | `2238.15` | `2258.60` | `597.07` | 12,718.36 USD | `+0.83%` | `5X Cross` |
| `1479` | `0x0cac...6170` | `SHORT` | 1,486,673.25 USD | `657.50` | `2146.55` | `2258.60` | `2840.15` | -75,311.05 USD | `-5.07%` | `20X Cross` |
| `1485` | `0x4b1c...bc38` | `SHORT` | 1,480,103.22 USD | `654.36` | `2528.62` | `2258.60` | `4533.90` | 174,532.32 USD | `+11.79%` | `10X Cross` |
| `1502` | `0x621c...63ab` | `LONG` | 1,456,543.73 USD | `642.98` | `2281.90` | `2258.60` | `0.000000` | -10,679.68 USD | `-0.73%` | `20X Cross` |
| `1506` | `0xf00e...fe3d` | `SHORT` | 1,453,808.83 USD | `642.88` | `2333.21` | `2258.60` | `2556.84` | 46,169.14 USD | `+3.18%` | `20X Cross` |
| `1511` | `0xffb2...5ed6` | `SHORT` | 1,451,913.49 USD | `640.77` | `2672.96` | `2258.60` | `2499.02` | 260,834.86 USD | `+17.96%` | `20X Cross` |
| `1541` | `0x871f...972b` | `SHORT` | 1,417,366.60 USD | `626.77` | `2279.80` | `2258.60` | `2581.68` | 11,535.23 USD | `+0.81%` | `20X Cross` |
| `1554` | `0xfce0...f4c0` | `SHORT` | 1,410,583.20 USD | `623.60` | `3129.61` | `2258.60` | `2788.40` | 541,043.39 USD | `+38.36%` | `20X Cross` |
| `1570` | `0x7663...cb5a` | `SHORT` | 1,387,945.21 USD | `613.54` | `2342.35` | `2258.60` | `3775.90` | 49,175.28 USD | `+3.54%` | `3X Cross` |
| `1592` | `0x67c3...609d` | `SHORT` | 1,359,954.00 USD | `600.00` | `2386.55` | `2258.60` | `2560.74` | 71,977.89 USD | `+5.29%` | `25X Cross` |
| `1593` | `0xad02...eb65` | `LONG` | 1,358,302.58 USD | `600.62` | `2460.69` | `2258.60` | `1079.65` | -119,637.98 USD | `-8.81%` | `5X Cross` |
| `1595` | `0x26e6...6b28` | `LONG` | 1,357,080.00 USD | `600.00` | `1769.78` | `2258.60` | `2005.45` | 295,208.47 USD | `+21.75%` | `20X Cross` |
| `1596` | `0x638f...f5f0` | `LONG` | 1,356,060.00 USD | `600.00` | `4011.50` | `2258.60` | `344.13` | -1,050,843.53 USD | `-77.49%` | `25X Cross` |
| `1607` | `0x7c90...d129` | `LONG` | 1,343,718.85 USD | `594.17` | `2286.01` | `2258.60` | `1839.21` | -14,564.04 USD | `-1.08%` | `20X Cross` |
| `1637` | `0xab81...c608` | `SHORT` | 1,305,500.63 USD | `577.27` | `2285.37` | `2258.60` | `6004.29` | 13,780.66 USD | `+1.06%` | `20X Cross` |
| `1656` | `0xfc66...ca06` | `SHORT` | 1,283,476.48 USD | `567.43` | `2275.19` | `2258.60` | `30966.24` | 7,546.73 USD | `+0.59%` | `20X Cross` |
| `1659` | `0xfb99...37f3` | `LONG` | 1,278,688.50 USD | `565.34` | `2362.35` | `2258.60` | `1240.03` | -56,847.86 USD | `-4.45%` | `3X Cross` |
| `1673` | `0x844b...7f42` | `SHORT` | 1,263,035.40 USD | `561.00` | `2026.17` | `2258.60` | `3237.19` | -126,351.99 USD | `-10.00%` | `25X Cross` |
| `1682` | `0xabe6...1d99` | `SHORT` | 1,257,347.45 USD | `556.00` | `2484.68` | `2258.60` | `3105.57` | 124,148.44 USD | `+9.87%` | `20X Cross` |
| `1700` | `0xf910...0a2d` | `LONG` | 1,244,677.56 USD | `550.50` | `2269.31` | `2258.60` | `0.000000` | -4,575.99 USD | `-0.37%` | `5X Cross` |
| `1710` | `0xd6e1...f256` | `SHORT` | 1,233,739.05 USD | `545.59` | `2258.34` | `2258.60` | `3301.73` | -1,613.57 USD | `-0.13%` | `25X Cross` |
| `1732` | `0xad21...fb6a` | `LONG` | 1,202,662.86 USD | `531.87` | `2574.89` | `2258.60` | `1708.63` | -166,842.64 USD | `-13.87%` | `7X Cross` |
| `1742` | `0x0082...1ae3` | `LONG` | 1,194,336.00 USD | `528.00` | `2448.58` | `2258.60` | `2234.21` | -98,518.91 USD | `-8.25%` | `25X Cross` |
| `1790` | `0x0c7a...2f50` | `SHORT` | 1,151,505.47 USD | `509.25` | `2122.56` | `2258.60` | `4111.46` | -70,600.04 USD | `-6.13%` | `20X Cross` |
| `1800` | `0x0089...2410` | `SHORT` | 1,147,209.87 USD | `507.35` | `2308.88` | `2258.60` | `3328.05` | 24,190.39 USD | `+2.11%` | `20X Cross` |
| `1814` | `0x6936...9417` | `SHORT` | 1,130,950.00 USD | `500.00` | `2315.11` | `2258.60` | `2359.66` | 26,605.21 USD | `+2.35%` | `25X Isolated` |
| `1815` | `0x89b2...9ca6` | `LONG` | 1,130,750.00 USD | `500.00` | `2484.03` | `2258.60` | `1954.18` | -111,269.35 USD | `-9.84%` | `25X Cross` |
| `1821` | `0x7298...7d6c` | `SHORT` | 1,126,714.09 USD | `498.15` | `3426.75` | `2258.60` | `5422.37` | 580,321.74 USD | `+51.51%` | `20X Cross` |
| `1822` | `0xa559...ff95` | `LONG` | 1,126,400.00 USD | `500.00` | `2260.68` | `2258.60` | `1146.71` | -3,944.36 USD | `-0.35%` | `20X Cross` |
| `1831` | `0x536c...3e1f` | `LONG` | 1,119,008.34 USD | `494.83` | `2275.87` | `2258.60` | `2129.64` | -7,163.98 USD | `-0.64%` | `20X Cross` |
| `1836` | `0x9c68...7783` | `SHORT` | 1,115,516.93 USD | `493.31` | `2273.58` | `2258.60` | `3904.19` | 6,062.32 USD | `+0.54%` | `25X Cross` |
| `1847` | `0xc10f...23b3` | `LONG` | 1,108,625.00 USD | `490.00` | `2383.92` | `2258.60` | `2085.43` | -59,496.28 USD | `-5.37%` | `25X Cross` |
| `1849` | `0x404c...5f03` | `SHORT` | 1,107,649.46 USD | `489.79` | `2671.94` | `2258.60` | `5034.58` | 201,030.10 USD | `+18.15%` | `20X Cross` |
| `1854` | `0x321f...1c84` | `SHORT` | 1,103,158.81 USD | `488.02` | `2370.09` | `2258.60` | `3027.76` | 53,485.79 USD | `+4.85%` | `10X Cross` |
| `1862` | `0xa522...2d0e` | `SHORT` | 1,099,618.11 USD | `486.36` | `2284.42` | `2258.60` | `5014.26` | 11,443.44 USD | `+1.04%` | `20X Cross` |
| `1865` | `0xd4c1...3d1d` | `SHORT` | 1,096,481.44 USD | `485.32` | `2334.28` | `2258.60` | `13095.62` | 36,389.73 USD | `+3.32%` | `12X Cross` |
| `1873` | `0x8923...1bac` | `SHORT` | 1,087,319.56 USD | `480.82` | `2277.43` | `2258.60` | `3127.05` | 7,708.47 USD | `+0.71%` | `25X Cross` |
| `1921` | `0x82c6...fe42` | `LONG` | 1,046,175.00 USD | `462.50` | `2501.38` | `2258.60` | `2054.43` | -110,715.57 USD | `-10.58%` | `5X Isolated` |
| `1927` | `0x2de3...486d` | `LONG` | 1,041,056.48 USD | `460.40` | `2286.27` | `2258.60` | `1275.80` | -11,544.43 USD | `-1.11%` | `25X Cross` |
| `1932` | `0x617e...0f97` | `SHORT` | 1,035,300.37 USD | `457.85` | `2205.60` | `2258.60` | `3773.12` | -25,456.53 USD | `-2.46%` | `10X Cross` |
| `1964` | `0xae55...2236` | `LONG` | 1,017,495.00 USD | `450.00` | `2510.21` | `2258.60` | `0.000000` | -112,102.50 USD | `-11.02%` | `25X Cross` |
| `1982` | `0xac26...a9c7` | `SHORT` | 1,009,165.95 USD | `446.28` | `2192.58` | `2258.60` | `8548.73` | -30,666.25 USD | `-3.04%` | `20X Cross` |
| `1986` | `0x53f8...ceff` | `LONG` | 1,007,896.99 USD | `445.60` | `2399.81` | `2258.60` | `0.000000` | -61,453.61 USD | `-6.10%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `1D` | `Long Liquidation` | `2015.70` | 464,260,000.00 USD | 464,260,000.00 USD | 0.00 USD | 176,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2018.60` | 464,080,000.00 USD | 464,080,000.00 USD | 83,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2021.50` | 464,000,000.00 USD | 464,000,000.00 USD | 0.00 USD | 558,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2025.00` | 1,710,000.00 USD | 322,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2025.30` | 887,120,000.00 USD | 887,120,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2027.30` | 463,440,000.00 USD | 463,440,000.00 USD | 0.00 USD | 970,290.00 USD | 40,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2028.60` | 886,940,000.00 USD | 886,940,000.00 USD | 0.00 USD | 1,180,000.00 USD | 35,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2030.20` | 462,430,000.00 USD | 462,430,000.00 USD | 87,180.00 USD | 136,500.00 USD | 43,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2031.90` | 885,730,000.00 USD | 885,730,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2033.10` | 462,160,000.00 USD | 462,160,000.00 USD | 1,530,000.00 USD | 1,330,000.00 USD | 408,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2035.00` | 1,790,000.00 USD | 320,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2035.20` | 884,280,000.00 USD | 884,280,000.00 USD | 146,420.00 USD | 186,130.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2036.00` | 458,890,000.00 USD | 458,890,000.00 USD | 866,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2038.50` | 882,590,000.00 USD | 882,590,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2038.90` | 458,030,000.00 USD | 458,030,000.00 USD | 138,370.00 USD | 0.00 USD | 13,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2041.80` | 457,880,000.00 USD | 457,880,000.00 USD | 0.00 USD | 178,560.00 USD | 14,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2045.00` | 17,480,000.00 USD | 319,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2045.10` | 881,140,000.00 USD | 881,140,000.00 USD | 0.00 USD | 149,500.00 USD | 47,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2050.50` | 457,680,000.00 USD | 457,680,000.00 USD | 0.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2051.70` | 880,940,000.00 USD | 880,940,000.00 USD | 1,320,000.00 USD | 0.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2053.40` | 456,630,000.00 USD | 456,630,000.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2055.00` | 5,010,000.00 USD | 301,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2056.30` | 456,510,000.00 USD | 456,510,000.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2058.30` | 878,430,000.00 USD | 878,430,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2059.20` | 456,270,000.00 USD | 456,270,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2061.60` | 878,090,000.00 USD | 878,090,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2062.10` | 455,510,000.00 USD | 455,510,000.00 USD | 80,610.00 USD | 121,470.00 USD | 52,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2064.90` | 872,830,000.00 USD | 872,830,000.00 USD | 1,230,000.00 USD | 313,000.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2065.00` | 455,260,000.00 USD | 455,260,000.00 USD | 984,680.00 USD | 537,030.00 USD | 598,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2065.00` | 2,650,000.00 USD | 296,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2067.90` | 453,140,000.00 USD | 453,140,000.00 USD | 387,410.00 USD | 1,010,000.00 USD | 50,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2068.20` | 870,310,000.00 USD | 870,310,000.00 USD | 1,740,000.00 USD | 1,860,000.00 USD | 893,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2070.80` | 451,690,000.00 USD | 451,690,000.00 USD | 1,100,000.00 USD | 854,090.00 USD | 437,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2071.50` | 865,810,000.00 USD | 865,810,000.00 USD | 2,820,000.00 USD | 2,410,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2073.70` | 449,300,000.00 USD | 449,300,000.00 USD | 419,970.00 USD | 62,630.00 USD | 926,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2074.80` | 859,350,000.00 USD | 859,350,000.00 USD | 4,370,000.00 USD | 3,270,000.00 USD | 4,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 3,470,000.00 USD | 294,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2076.60` | 447,890,000.00 USD | 447,890,000.00 USD | 2,580,000.00 USD | 1,020,000.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2078.10` | 847,650,000.00 USD | 847,650,000.00 USD | 5,560,000.00 USD | 4,320,000.00 USD | 2,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2079.50` | 442,290,000.00 USD | 442,290,000.00 USD | 1,700,000.00 USD | 1,270,000.00 USD | 443,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2081.40` | 835,360,000.00 USD | 835,360,000.00 USD | 4,720,000.00 USD | 3,420,000.00 USD | 2,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2082.40` | 438,870,000.00 USD | 438,870,000.00 USD | 1,610,000.00 USD | 1,140,000.00 USD | 224,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2084.70` | 824,730,000.00 USD | 824,730,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 4,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 1,850,000.00 USD | 290,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2085.30` | 435,890,000.00 USD | 435,890,000.00 USD | 2,180,000.00 USD | 1,820,000.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2088.00` | 815,930,000.00 USD | 815,930,000.00 USD | 3,990,000.00 USD | 2,780,000.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2088.20` | 430,070,000.00 USD | 430,070,000.00 USD | 1,730,000.00 USD | 1,000,000.00 USD | 605,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2091.10` | 426,720,000.00 USD | 426,720,000.00 USD | 1,250,000.00 USD | 423,330.00 USD | 520,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2091.30` | 807,510,000.00 USD | 807,510,000.00 USD | 4,410,000.00 USD | 952,210.00 USD | 7,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2094.00` | 424,530,000.00 USD | 424,530,000.00 USD | 1,800,000.00 USD | 1,330,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2094.60` | 794,550,000.00 USD | 794,550,000.00 USD | 5,720,000.00 USD | 2,160,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 2,410,000.00 USD | 288,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2096.90` | 420,050,000.00 USD | 420,050,000.00 USD | 1,010,000.00 USD | 797,210.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2097.90` | 784,330,000.00 USD | 784,330,000.00 USD | 2,340,000.00 USD | 3,210,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2099.80` | 416,740,000.00 USD | 416,740,000.00 USD | 194,900.00 USD | 700,850.00 USD | 11,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2101.20` | 777,490,000.00 USD | 777,490,000.00 USD | 999,530.00 USD | 1,580,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2102.70` | 415,830,000.00 USD | 415,830,000.00 USD | 530,980.00 USD | 289,160.00 USD | 466,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2104.50` | 770,890,000.00 USD | 770,890,000.00 USD | 2,010,000.00 USD | 1,180,000.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 1,670,000.00 USD | 286,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2105.60` | 414,540,000.00 USD | 414,540,000.00 USD | 652,720.00 USD | 671,930.00 USD | 422,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2107.80` | 765,450,000.00 USD | 765,450,000.00 USD | 2,380,000.00 USD | 452,470.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2108.50` | 412,800,000.00 USD | 412,800,000.00 USD | 600,390.00 USD | 21,400.00 USD | 102,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2111.10` | 760,970,000.00 USD | 760,970,000.00 USD | 3,530,000.00 USD | 2,350,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2111.40` | 412,070,000.00 USD | 412,070,000.00 USD | 490,860.00 USD | 146,050.00 USD | 193,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2114.30` | 411,240,000.00 USD | 411,240,000.00 USD | 420,950.00 USD | 507,320.00 USD | 389,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2114.40` | 752,920,000.00 USD | 752,920,000.00 USD | 1,080,000.00 USD | 1,850,000.00 USD | 3,800,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 1,430,000.00 USD | 284,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2117.20` | 409,920,000.00 USD | 409,920,000.00 USD | 202,840.00 USD | 15,250.00 USD | 635,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2117.70` | 746,190,000.00 USD | 746,190,000.00 USD | 3,430,000.00 USD | 2,020,000.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2120.10` | 409,070,000.00 USD | 409,070,000.00 USD | 198,890.00 USD | 431,090.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2121.00` | 737,360,000.00 USD | 737,360,000.00 USD | 3,650,000.00 USD | 1,340,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2123.00` | 407,340,000.00 USD | 407,340,000.00 USD | 1,320,000.00 USD | 683,920.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2124.30` | 730,550,000.00 USD | 730,550,000.00 USD | 832,850.00 USD | 972,650.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 17,940,000.00 USD | 283,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2125.90` | 404,190,000.00 USD | 404,190,000.00 USD | 179,030.00 USD | 1,330,000.00 USD | 486,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2127.60` | 727,230,000.00 USD | 727,230,000.00 USD | 2,400,000.00 USD | 2,630,000.00 USD | 3,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2128.80` | 402,190,000.00 USD | 402,190,000.00 USD | 116,180.00 USD | 475,750.00 USD | 318,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2130.90` | 718,930,000.00 USD | 718,930,000.00 USD | 2,410,000.00 USD | 2,300,000.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2131.70` | 401,280,000.00 USD | 401,280,000.00 USD | 0.00 USD | 18,610.00 USD | 331,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2134.20` | 712,510,000.00 USD | 712,510,000.00 USD | 2,170,000.00 USD | 550,450.00 USD | 308,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 14,630,000.00 USD | 265,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2137.50` | 400,930,000.00 USD | 400,930,000.00 USD | 0.00 USD | 278,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2137.50` | 709,480,000.00 USD | 709,480,000.00 USD | 1,040,000.00 USD | 880,790.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2140.80` | 707,520,000.00 USD | 707,520,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2144.10` | 703,590,000.00 USD | 703,590,000.00 USD | 449,020.00 USD | 1,130,000.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 7,440,000.00 USD | 250,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2147.40` | 701,740,000.00 USD | 701,740,000.00 USD | 657,710.00 USD | 421,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2150.70` | 700,660,000.00 USD | 700,660,000.00 USD | 459,630.00 USD | 463,640.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2152.00` | 400,650,000.00 USD | 400,650,000.00 USD | 208,250.00 USD | 440,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2154.00` | 699,710,000.00 USD | 699,710,000.00 USD | 128,430.00 USD | 331,520.00 USD | 32,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2154.90` | 400,000,000.00 USD | 400,000,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 2,180,000.00 USD | 243,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2157.30` | 699,210,000.00 USD | 699,210,000.00 USD | 388,210.00 USD | 1,030,000.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2157.80` | 398,600,000.00 USD | 398,600,000.00 USD | 0.00 USD | 0.00 USD | 37,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2160.60` | 696,720,000.00 USD | 696,720,000.00 USD | 613,630.00 USD | 1,900,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2160.70` | 398,570,000.00 USD | 398,570,000.00 USD | 0.00 USD | 2,290,000.00 USD | 71,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2163.60` | 396,210,000.00 USD | 396,210,000.00 USD | 0.00 USD | 999,490.00 USD | 28,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2163.90` | 692,200,000.00 USD | 692,200,000.00 USD | 566,120.00 USD | 3,280,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 6,820,000.00 USD | 241,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2166.50` | 395,180,000.00 USD | 395,180,000.00 USD | 1,690,000.00 USD | 341,240.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2167.20` | 687,060,000.00 USD | 687,060,000.00 USD | 25,540.00 USD | 3,620,000.00 USD | 50,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2169.40` | 392,020,000.00 USD | 392,020,000.00 USD | 6,960,000.00 USD | 4,810,000.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2170.50` | 683,360,000.00 USD | 683,360,000.00 USD | 3,500,000.00 USD | 3,730,000.00 USD | 5,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2172.30` | 378,120,000.00 USD | 378,120,000.00 USD | 0.00 USD | 365,630.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2173.80` | 670,920,000.00 USD | 670,920,000.00 USD | 4,370,000.00 USD | 363,040.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 109,290,000.00 USD | 234,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2175.20` | 376,640,000.00 USD | 376,640,000.00 USD | 345,940.00 USD | 301,420.00 USD | 33,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2177.10` | 665,180,000.00 USD | 665,180,000.00 USD | 0.00 USD | 0.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2178.10` | 375,960,000.00 USD | 375,960,000.00 USD | 0.00 USD | 1,400,000.00 USD | 49,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2180.40` | 663,860,000.00 USD | 663,860,000.00 USD | 0.00 USD | 373,740.00 USD | 176,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2181.00` | 374,510,000.00 USD | 374,510,000.00 USD | 2,080,000.00 USD | 478,110.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2183.70` | 663,310,000.00 USD | 663,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2183.90` | 370,590,000.00 USD | 370,590,000.00 USD | 1,350,000.00 USD | 509,320.00 USD | 13,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2185.00` | 100,000,000.00 USD | 124,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2186.80` | 368,710,000.00 USD | 368,710,000.00 USD | 0.00 USD | 1,450,000.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2187.00` | 659,460,000.00 USD | 659,460,000.00 USD | 556,600.00 USD | 0.00 USD | 54,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2189.70` | 365,470,000.00 USD | 365,470,000.00 USD | 0.00 USD | 0.00 USD | 693,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2190.30` | 658,850,000.00 USD | 658,850,000.00 USD | 2,730,000.00 USD | 0.00 USD | 4,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2192.60` | 364,770,000.00 USD | 364,770,000.00 USD | 605,210.00 USD | 222,200.00 USD | 109,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 2,280,000.00 USD | 24,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2195.50` | 363,840,000.00 USD | 363,840,000.00 USD | 0.00 USD | 881,070.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2196.90` | 651,920,000.00 USD | 651,920,000.00 USD | 2,580,000.00 USD | 474,090.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2198.40` | 361,070,000.00 USD | 361,070,000.00 USD | 416,500.00 USD | 149,110.00 USD | 50,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2200.20` | 646,830,000.00 USD | 646,830,000.00 USD | 3,000,000.00 USD | 5,080,000.00 USD | 3,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2201.30` | 360,450,000.00 USD | 360,450,000.00 USD | 1,690,000.00 USD | 4,250,000.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2203.50` | 635,550,000.00 USD | 635,550,000.00 USD | 3,650,000.00 USD | 1,710,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2204.20` | 353,010,000.00 USD | 353,010,000.00 USD | 2,130,000.00 USD | 314,310.00 USD | 867,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 8,120,000.00 USD | 22,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2206.80` | 626,440,000.00 USD | 626,440,000.00 USD | 6,920,000.00 USD | 9,430,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2207.10` | 349,700,000.00 USD | 349,700,000.00 USD | 2,210,000.00 USD | 10,880,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2210.00` | 334,580,000.00 USD | 334,580,000.00 USD | 3,190,000.00 USD | 3,380,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2210.10` | 606,070,000.00 USD | 606,070,000.00 USD | 12,800,000.00 USD | 20,410,000.00 USD | 6,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2212.90` | 325,320,000.00 USD | 325,320,000.00 USD | 9,880,000.00 USD | 8,670,000.00 USD | 4,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2213.40` | 566,390,000.00 USD | 566,390,000.00 USD | 10,920,000.00 USD | 14,590,000.00 USD | 19,950,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 4,660,000.00 USD | 14,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2215.80` | 302,380,000.00 USD | 302,380,000.00 USD | 18,430,000.00 USD | 9,760,000.00 USD | 12,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2216.70` | 520,920,000.00 USD | 520,920,000.00 USD | 25,710,000.00 USD | 17,030,000.00 USD | 9,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2218.70` | 261,780,000.00 USD | 261,780,000.00 USD | 6,790,000.00 USD | 7,780,000.00 USD | 1,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2220.00` | 468,790,000.00 USD | 468,790,000.00 USD | 24,310,000.00 USD | 12,300,000.00 USD | 12,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2221.60` | 245,340,000.00 USD | 245,340,000.00 USD | 6,200,000.00 USD | 12,240,000.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2223.30` | 419,420,000.00 USD | 419,420,000.00 USD | 10,150,000.00 USD | 8,220,000.00 USD | 11,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2224.50` | 225,560,000.00 USD | 225,560,000.00 USD | 9,730,000.00 USD | 5,030,000.00 USD | 5,660,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2225.00` | 5,380,000.00 USD | 9,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2226.60` | 389,140,000.00 USD | 389,140,000.00 USD | 12,840,000.00 USD | 11,030,000.00 USD | 9,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2227.40` | 205,150,000.00 USD | 205,150,000.00 USD | 5,940,000.00 USD | 13,200,000.00 USD | 5,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2229.90` | 355,320,000.00 USD | 355,320,000.00 USD | 12,730,000.00 USD | 11,790,000.00 USD | 25,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2230.30` | 180,390,000.00 USD | 180,390,000.00 USD | 6,830,000.00 USD | 8,320,000.00 USD | 2,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2233.20` | 162,820,000.00 USD | 162,820,000.00 USD | 5,060,000.00 USD | 4,220,000.00 USD | 8,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2233.20` | 305,050,000.00 USD | 305,050,000.00 USD | 16,600,000.00 USD | 24,290,000.00 USD | 10,420,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2235.00` | 878,090.00 USD | 878,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2236.10` | 145,500,000.00 USD | 145,500,000.00 USD | 23,180,000.00 USD | 0.00 USD | 10,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2236.50` | 253,730,000.00 USD | 253,730,000.00 USD | 16,050,000.00 USD | 7,430,000.00 USD | 27,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2239.00` | 111,530,000.00 USD | 111,530,000.00 USD | 17,940,000.00 USD | 7,390,000.00 USD | 13,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2239.80` | 202,490,000.00 USD | 202,490,000.00 USD | 16,720,000.00 USD | 6,600,000.00 USD | 13,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2241.90` | 72,320,000.00 USD | 72,320,000.00 USD | 619,130.00 USD | 760,920.00 USD | 5,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2243.10` | 165,420,000.00 USD | 165,420,000.00 USD | 22,920,000.00 USD | 0.00 USD | 18,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2244.80` | 65,570,000.00 USD | 65,570,000.00 USD | 3,850,000.00 USD | 4,700,000.00 USD | 463,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2245.00` | 4,430,000.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2246.40` | 124,170,000.00 USD | 124,170,000.00 USD | 14,340,000.00 USD | 0.00 USD | 13,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2247.70` | 56,550,000.00 USD | 56,550,000.00 USD | 12,800,000.00 USD | 0.00 USD | 7,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2249.70` | 95,910,000.00 USD | 95,910,000.00 USD | 18,000,000.00 USD | 0.00 USD | 12,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2250.60` | 36,670,000.00 USD | 36,670,000.00 USD | 4,190,000.00 USD | 1,910,000.00 USD | 3,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2253.00` | 65,090,000.00 USD | 65,090,000.00 USD | 26,890,000.00 USD | 0.00 USD | 12,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2253.50` | 26,600,000.00 USD | 26,600,000.00 USD | 5,410,000.00 USD | 4,440,000.00 USD | 4,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2255.00` | 68,250.00 USD | 68,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2256.30` | 26,160,000.00 USD | 26,160,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2256.40` | 12,200,000.00 USD | 12,200,000.00 USD | 0.00 USD | 3,390,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2259.60` | 10,940,000.00 USD | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2262.20` | 8,810,000.00 USD | 8,810,000.00 USD | 2,420,000.00 USD | 0.00 USD | 156,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2265.00` | 410.42 USD | 878,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2265.10` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 1,800,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2268.00` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 4,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2273.80` | 220,250.00 USD | 220,250.00 USD | 220,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2275.00` | 633.82 USD | 879,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2276.70` | 2,260,000.00 USD | 2,260,000.00 USD | 1,370,000.00 USD | 555,110.00 USD | 114,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2279.40` | 17,000,000.00 USD | 17,000,000.00 USD | 0.00 USD | 17,000,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2279.60` | 35,820,000.00 USD | 35,820,000.00 USD | 23,020,000.00 USD | 6,030,000.00 USD | 4,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2282.50` | 138,270,000.00 USD | 138,270,000.00 USD | 51,860,000.00 USD | 39,620,000.00 USD | 10,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2282.70` | 117,630,000.00 USD | 117,630,000.00 USD | 0.00 USD | 87,090,000.00 USD | 13,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2285.00` | 2,530.00 USD | 881,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2285.40` | 156,400,000.00 USD | 156,400,000.00 USD | 7,830,000.00 USD | 4,510,000.00 USD | 5,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2286.00` | 128,050,000.00 USD | 128,050,000.00 USD | 1,010,000.00 USD | 9,400,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2288.30` | 157,300,000.00 USD | 157,300,000.00 USD | 0.00 USD | 760,920.00 USD | 133,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2289.30` | 133,330,000.00 USD | 133,330,000.00 USD | 0.00 USD | 0.00 USD | 5,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2291.20` | 166,330,000.00 USD | 166,330,000.00 USD | 0.00 USD | 8,840,000.00 USD | 199,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2294.10` | 180,200,000.00 USD | 180,200,000.00 USD | 8,310,000.00 USD | 0.00 USD | 5,560,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2295.00` | 25,230.00 USD | 906,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2295.90` | 148,010,000.00 USD | 148,010,000.00 USD | 6,580,000.00 USD | 2,380,000.00 USD | 5,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2297.00` | 194,220,000.00 USD | 194,220,000.00 USD | 5,410,000.00 USD | 8,350,000.00 USD | 253,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2299.20` | 176,420,000.00 USD | 176,420,000.00 USD | 11,730,000.00 USD | 11,130,000.00 USD | 5,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2299.90` | 209,590,000.00 USD | 209,590,000.00 USD | 0.00 USD | 7,970,000.00 USD | 7,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2302.50` | 223,540,000.00 USD | 223,540,000.00 USD | 23,020,000.00 USD | 7,250,000.00 USD | 16,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2302.80` | 230,410,000.00 USD | 230,410,000.00 USD | 15,230,000.00 USD | 682,490.00 USD | 4,910,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2305.00` | 4,250,000.00 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2305.70` | 262,380,000.00 USD | 262,380,000.00 USD | 10,430,000.00 USD | 15,620,000.00 USD | 5,930,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2305.80` | 244,310,000.00 USD | 244,310,000.00 USD | 2,980,000.00 USD | 8,820,000.00 USD | 8,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2308.60` | 268,140,000.00 USD | 268,140,000.00 USD | 2,420,000.00 USD | 2,340,000.00 USD | 994,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2309.10` | 248,590,000.00 USD | 248,590,000.00 USD | 1,240,000.00 USD | 930,630.00 USD | 2,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2311.50` | 277,780,000.00 USD | 277,780,000.00 USD | 691,870.00 USD | 1,260,000.00 USD | 7,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2312.40` | 266,730,000.00 USD | 266,730,000.00 USD | 7,270,000.00 USD | 0.00 USD | 10,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2314.40` | 292,120,000.00 USD | 292,120,000.00 USD | 0.00 USD | 14,100,000.00 USD | 231,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2315.00` | 2,480,000.00 USD | 7,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2315.70` | 274,300,000.00 USD | 274,300,000.00 USD | 0.00 USD | 7,460,000.00 USD | 117,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2317.30` | 320,660,000.00 USD | 320,660,000.00 USD | 10,230,000.00 USD | 10,470,000.00 USD | 7,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2319.00` | 285,490,000.00 USD | 285,490,000.00 USD | 1,020,000.00 USD | 4,550,000.00 USD | 5,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2320.20` | 336,780,000.00 USD | 336,780,000.00 USD | 6,580,000.00 USD | 9,360,000.00 USD | 173,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2322.30` | 302,650,000.00 USD | 302,650,000.00 USD | 1,110,000.00 USD | 15,930,000.00 USD | 108,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2323.10` | 351,350,000.00 USD | 351,350,000.00 USD | 572,970.00 USD | 10,410,000.00 USD | 3,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2325.00` | 1,420,000.00 USD | 9,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2325.60` | 323,300,000.00 USD | 323,300,000.00 USD | 9,720,000.00 USD | 2,540,000.00 USD | 8,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2326.00` | 363,030,000.00 USD | 363,030,000.00 USD | 479,120.00 USD | 5,550,000.00 USD | 5,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2328.90` | 370,010,000.00 USD | 370,010,000.00 USD | 5,690,000.00 USD | 884,940.00 USD | 402,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2328.90` | 335,130,000.00 USD | 335,130,000.00 USD | 3,860,000.00 USD | 0.00 USD | 7,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2331.80` | 386,300,000.00 USD | 386,300,000.00 USD | 15,910,000.00 USD | 251,940.00 USD | 126,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2332.20` | 364,360,000.00 USD | 364,360,000.00 USD | 29,230,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2334.70` | 409,870,000.00 USD | 409,870,000.00 USD | 13,410,000.00 USD | 2,960,000.00 USD | 7,200,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2335.00` | 1,230,000.00 USD | 10,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2335.50` | 422,370,000.00 USD | 422,370,000.00 USD | 28,990,000.00 USD | 18,420,000.00 USD | 10,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2337.60` | 423,750,000.00 USD | 423,750,000.00 USD | 9,880,000.00 USD | 407,920.00 USD | 3,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2338.80` | 440,240,000.00 USD | 440,240,000.00 USD | 9,570,000.00 USD | 0.00 USD | 8,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2340.50` | 447,640,000.00 USD | 447,640,000.00 USD | 8,010,000.00 USD | 5,100,000.00 USD | 10,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2342.10` | 480,350,000.00 USD | 480,350,000.00 USD | 4,720,000.00 USD | 21,390,000.00 USD | 14,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2343.40` | 462,280,000.00 USD | 462,280,000.00 USD | 2,060,000.00 USD | 5,580,000.00 USD | 7,000,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2345.00` | 326,400.00 USD | 10,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2345.40` | 501,720,000.00 USD | 501,720,000.00 USD | 1,350,000.00 USD | 13,990,000.00 USD | 6,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2346.30` | 475,180,000.00 USD | 475,180,000.00 USD | 4,950,000.00 USD | 1,940,000.00 USD | 6,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2348.70` | 539,590,000.00 USD | 539,590,000.00 USD | 847,620.00 USD | 9,500,000.00 USD | 27,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2349.20` | 501,430,000.00 USD | 501,430,000.00 USD | 13,670,000.00 USD | 6,150,000.00 USD | 6,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2352.00` | 576,470,000.00 USD | 576,470,000.00 USD | 3,190,000.00 USD | 23,060,000.00 USD | 10,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2352.10` | 537,420,000.00 USD | 537,420,000.00 USD | 24,370,000.00 USD | 4,590,000.00 USD | 7,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2355.00` | 559,200,000.00 USD | 559,200,000.00 USD | 1,010,000.00 USD | 19,500,000.00 USD | 1,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 1,270,000.00 USD | 11,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2355.30` | 631,060,000.00 USD | 631,060,000.00 USD | 16,520,000.00 USD | 36,690,000.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2357.90` | 569,890,000.00 USD | 569,890,000.00 USD | 2,890,000.00 USD | 4,290,000.00 USD | 3,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2358.60` | 643,200,000.00 USD | 643,200,000.00 USD | 7,110,000.00 USD | 512,220.00 USD | 4,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2360.80` | 591,130,000.00 USD | 591,130,000.00 USD | 10,720,000.00 USD | 5,400,000.00 USD | 5,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2361.90` | 650,320,000.00 USD | 650,320,000.00 USD | 3,150,000.00 USD | 3,800,000.00 USD | 176,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2363.70` | 616,990,000.00 USD | 616,990,000.00 USD | 7,900,000.00 USD | 9,120,000.00 USD | 8,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 1,310,000.00 USD | 13,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2365.20` | 668,220,000.00 USD | 668,220,000.00 USD | 8,440,000.00 USD | 0.00 USD | 9,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2366.60` | 622,680,000.00 USD | 622,680,000.00 USD | 3,560,000.00 USD | 509,320.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2368.50` | 681,290,000.00 USD | 681,290,000.00 USD | 10,830,000.00 USD | 1,780,000.00 USD | 458,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2369.50` | 649,180,000.00 USD | 649,180,000.00 USD | 13,850,000.00 USD | 7,720,000.00 USD | 4,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2371.80` | 762,230,000.00 USD | 762,230,000.00 USD | 26,000,000.00 USD | 0.00 USD | 54,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2372.40` | 686,700,000.00 USD | 686,700,000.00 USD | 14,410,000.00 USD | 10,690,000.00 USD | 12,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 1,060,000.00 USD | 14,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2375.10` | 789,170,000.00 USD | 789,170,000.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2375.30` | 708,220,000.00 USD | 708,220,000.00 USD | 14,210,000.00 USD | 3,650,000.00 USD | 3,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2378.20` | 733,440,000.00 USD | 733,440,000.00 USD | 5,350,000.00 USD | 7,910,000.00 USD | 11,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2378.40` | 834,590,000.00 USD | 834,590,000.00 USD | 11,800,000.00 USD | 7,950,000.00 USD | 25,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2381.10` | 782,790,000.00 USD | 782,790,000.00 USD | 16,150,000.00 USD | 13,170,000.00 USD | 20,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2381.70` | 874,370,000.00 USD | 874,370,000.00 USD | 8,510,000.00 USD | 6,750,000.00 USD | 24,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2384.00` | 826,420,000.00 USD | 826,420,000.00 USD | 17,870,000.00 USD | 15,110,000.00 USD | 10,650,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2385.00` | 976,090,000.00 USD | 976,090,000.00 USD | 18,550,000.00 USD | 36,910,000.00 USD | 46,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 42,090,000.00 USD | 56,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2386.90` | 862,130,000.00 USD | 862,130,000.00 USD | 13,540,000.00 USD | 11,770,000.00 USD | 10,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2388.30` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 5,290,000.00 USD | 38,070,000.00 USD | 44,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2389.80` | 887,830,000.00 USD | 887,830,000.00 USD | 10,230,000.00 USD | 9,340,000.00 USD | 6,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2391.60` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 8,560,000.00 USD | 52,080,000.00 USD | 40,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2392.70` | 905,880,000.00 USD | 905,880,000.00 USD | 5,770,000.00 USD | 4,950,000.00 USD | 7,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2394.90` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 57,450,000.00 USD | 32,260,000.00 USD | 37,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 99,780.00 USD | 56,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2395.60` | 921,360,000.00 USD | 921,360,000.00 USD | 5,140,000.00 USD | 6,720,000.00 USD | 3,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2398.20` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 42,820,000.00 USD | 38,210,000.00 USD | 29,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2398.50` | 941,040,000.00 USD | 941,040,000.00 USD | 5,800,000.00 USD | 6,760,000.00 USD | 7,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2401.40` | 965,980,000.00 USD | 965,980,000.00 USD | 8,280,000.00 USD | 7,500,000.00 USD | 9,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2401.50` | 1,510,000,000.00 USD | 1,510,000,000.00 USD | 51,970,000.00 USD | 26,780,000.00 USD | 29,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2404.30` | 995,550,000.00 USD | 995,550,000.00 USD | 9,990,000.00 USD | 11,060,000.00 USD | 8,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2404.80` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 50,800,000.00 USD | 32,200,000.00 USD | 24,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 1,430,000.00 USD | 57,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2407.20` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 15,160,000.00 USD | 9,260,000.00 USD | 7,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2408.10` | 1,710,000,000.00 USD | 1,710,000,000.00 USD | 34,390,000.00 USD | 31,420,000.00 USD | 25,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2410.10` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 7,660,000.00 USD | 7,700,000.00 USD | 9,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2411.40` | 1,790,000,000.00 USD | 1,790,000,000.00 USD | 19,200,000.00 USD | 32,580,000.00 USD | 27,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2413.00` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 8,270,000.00 USD | 5,470,000.00 USD | 3,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2414.70` | 1,860,000,000.00 USD | 1,860,000,000.00 USD | 24,010,000.00 USD | 21,950,000.00 USD | 23,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 858,190.00 USD | 58,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2415.90` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 3,710,000.00 USD | 2,920,000.00 USD | 3,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2418.00` | 1,930,000,000.00 USD | 1,930,000,000.00 USD | 34,060,000.00 USD | 15,260,000.00 USD | 24,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2418.80` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 4,240,000.00 USD | 2,710,000.00 USD | 3,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2421.30` | 2,010,000,000.00 USD | 2,010,000,000.00 USD | 25,700,000.00 USD | 27,770,000.00 USD | 21,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2421.70` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 6,390,000.00 USD | 6,200,000.00 USD | 6,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2424.60` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 1,790,000.00 USD | 2,770,000.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.60` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 23,840,000.00 USD | 34,930,000.00 USD | 34,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 953,600.00 USD | 59,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2427.50` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 731,900.00 USD | 124,100.00 USD | 601,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2427.90` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 25,200,000.00 USD | 18,380,000.00 USD | 26,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2430.40` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 1,640,000.00 USD | 1,770,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2431.20` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 10,380,000.00 USD | 17,060,000.00 USD | 9,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2433.30` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 2,160,000.00 USD | 2,160,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2434.50` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 27,390,000.00 USD | 21,570,000.00 USD | 11,160,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 4,450,000.00 USD | 64,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2436.20` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 2,340,000.00 USD | 475,290.00 USD | 579,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2437.80` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 12,000,000.00 USD | 12,820,000.00 USD | 5,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2439.10` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 304,760.00 USD | 641,280.00 USD | 484,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2441.10` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 15,080,000.00 USD | 8,120,000.00 USD | 10,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2442.00` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 2,360,000.00 USD | 2,020,000.00 USD | 735,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2444.40` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 8,860,000.00 USD | 15,100,000.00 USD | 14,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2444.90` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 544,880.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 280,670.00 USD | 64,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2447.70` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 11,480,000.00 USD | 8,450,000.00 USD | 17,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2447.80` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 687,490.00 USD | 330,760.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2450.70` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 2,540,000.00 USD | 1,470,000.00 USD | 3,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2451.00` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 16,710,000.00 USD | 14,100,000.00 USD | 16,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2453.60` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 4,790,000.00 USD | 4,000,000.00 USD | 3,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2454.30` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 4,620,000.00 USD | 4,930,000.00 USD | 3,880,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 96,380.00 USD | 64,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2456.50` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 1,060,000.00 USD | 2,650,000.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2457.60` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 15,150,000.00 USD | 12,540,000.00 USD | 12,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2459.40` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 1,900,000.00 USD | 1,190,000.00 USD | 366,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2460.90` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 5,580,000.00 USD | 8,670,000.00 USD | 6,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2462.30` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 490,260.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2464.20` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 8,720,000.00 USD | 7,700,000.00 USD | 4,700,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 914,970.00 USD | 65,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2465.20` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 83,300.00 USD | 176,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2467.50` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 4,540,000.00 USD | 3,710,000.00 USD | 586,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2468.10` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 1,250,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2470.80` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 3,960,000.00 USD | 2,290,000.00 USD | 522,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2471.00` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 391,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2474.10` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 5,230,000.00 USD | 2,920,000.00 USD | 2,400,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 438,920.00 USD | 65,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2476.80` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 943,590.00 USD | 40,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2477.40` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 1,660,000.00 USD | 4,420,000.00 USD | 718,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2479.70` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 26,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2480.70` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 2,110,000.00 USD | 4,170,000.00 USD | 540,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2482.60` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 677,540.00 USD | 136,500.00 USD | 451,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2484.00` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 1,210,000.00 USD | 1,390,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 96,970.00 USD | 65,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2485.50` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 941,100.00 USD | 1,330,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2487.30` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 325,140.00 USD | 262,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2488.40` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 866,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2490.60` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 2,910,000.00 USD | 2,540,000.00 USD | 279,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2491.30` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 138,370.00 USD | 0.00 USD | 13,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2493.90` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 1,660,000.00 USD | 1,760,000.00 USD | 3,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2494.20` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 178,560.00 USD | 14,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 8,760,000.00 USD | 74,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2497.20` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 2,860,000.00 USD | 5,240,000.00 USD | 8,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2500.50` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 1,110,000.00 USD | 2,280,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2503.80` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 63,860.00 USD | 1,480,000.00 USD | 125,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 2,310,000.00 USD | 77,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2505.80` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2507.10` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 4,340,000.00 USD | 3,090,000.00 USD | 3,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2510.40` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 2,290,000.00 USD | 1,270,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2511.60` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 242,080.00 USD | 88,880.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2513.70` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 142,410.00 USD | 77,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2517.00` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 97,050.00 USD | 189,640.00 USD | 815,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2517.40` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2520.30` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 80,610.00 USD | 121,470.00 USD | 52,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2520.30` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2523.20` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 563,140.00 USD | 537,030.00 USD | 568,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2523.60` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 4,710,000.00 USD | 81,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2526.10` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 808,950.00 USD | 362,000.00 USD | 53,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2526.90` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2529.00` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 641,110.00 USD | 965,400.00 USD | 464,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2530.20` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 2,800,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2531.90` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 474,040.00 USD | 534,600.00 USD | 7,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2533.50` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 3,530,000.00 USD | 1,850,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2534.80` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 405,580.00 USD | 62,630.00 USD | 919,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2535.00` | 2,520,000.00 USD | 84,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2536.80` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 3,720,000.00 USD | 3,450,000.00 USD | 3,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2537.70` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 2,580,000.00 USD | 926,330.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2540.10` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 4,150,000.00 USD | 3,220,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2540.60` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 1,180,000.00 USD | 1,100,000.00 USD | 808,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2543.40` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 4,150,000.00 USD | 2,520,000.00 USD | 2,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2543.50` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 1,510,000.00 USD | 1,100,000.00 USD | 233,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2545.00` | 5,380,000.00 USD | 89,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2546.40` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 1,780,000.00 USD | 1,410,000.00 USD | 571,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2546.70` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 1,450,000.00 USD | 1,090,000.00 USD | 2,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2549.30` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 1,020,000.00 USD | 803,170.00 USD | 1,470,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2550.00` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 4,320,000.00 USD | 3,550,000.00 USD | 3,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2552.20` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 1,730,000.00 USD | 914,630.00 USD | 396,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2553.30` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 2,820,000.00 USD | 788,360.00 USD | 2,600,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2555.00` | 397,740.00 USD | 90,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2555.10` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 996,760.00 USD | 221,720.00 USD | 417,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2556.60` | 2,730,000,000.00 USD | 2,730,000,000.00 USD | 2,760,000.00 USD | 283,560.00 USD | 6,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2558.00` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 736,590.00 USD | 502,170.00 USD | 811,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2559.90` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 5,720,000.00 USD | 2,130,000.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2560.50` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 1,830,000.00 USD | 1,080,000.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2563.20` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 1,430,000.00 USD | 2,900,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2565.00` | 2,400,000.00 USD | 92,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2566.50` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 1,860,000.00 USD | 1,830,000.00 USD | 3,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2569.80` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 125,250.00 USD | 341,900.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2573.10` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2575.00` | 11,620,000.00 USD | 104,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2576.40` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 2,400,000.00 USD | 930,280.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2579.70` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 2,750,000.00 USD | 1,780,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2583.00` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 1,730,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2585.00` | 26,470,000.00 USD | 130,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2586.30` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 1,480,000.00 USD | 2,030,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2589.60` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 3,310,000.00 USD | 631,590.00 USD | 2,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2592.90` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 2,370,000.00 USD | 1,280,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2595.00` | 1,910,000.00 USD | 132,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2596.20` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 794,750.00 USD | 620,840.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2599.50` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 2,380,000.00 USD | 2,530,000.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2602.80` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 1,680,000.00 USD | 1,260,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2605.00` | 14,250,000.00 USD | 146,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2606.10` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 1,850,000.00 USD | 1,560,000.00 USD | 772,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2609.40` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2612.70` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 1,010,000.00 USD | 643,740.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2615.00` | 293,190.00 USD | 147,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2616.00` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2619.30` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 449,020.00 USD | 323,810.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2622.60` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 631,440.00 USD | 1,220,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2625.00` | 13,030,000.00 USD | 160,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2625.90` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 485,890.00 USD | 474,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2629.20` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 20,460.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2632.40` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 301,060.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `1D` | `2015.70` | 464,260,000.00 USD | 0.00 USD | 464,260,000.00 USD | 0.00 USD | 176,210.00 USD | 0.00 USD |
| `1D` | `2018.60` | 464,080,000.00 USD | 0.00 USD | 464,080,000.00 USD | 83,300.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2021.50` | 464,000,000.00 USD | 0.00 USD | 464,000,000.00 USD | 0.00 USD | 558,730.00 USD | 0.00 USD |
| `7D` | `2025.30` | 887,120,000.00 USD | 0.00 USD | 887,120,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD |
| `1D` | `2027.30` | 463,440,000.00 USD | 0.00 USD | 463,440,000.00 USD | 0.00 USD | 970,290.00 USD | 40,210.00 USD |
| `7D` | `2028.60` | 886,940,000.00 USD | 0.00 USD | 886,940,000.00 USD | 0.00 USD | 1,180,000.00 USD | 35,180.00 USD |
| `1D` | `2030.20` | 462,430,000.00 USD | 0.00 USD | 462,430,000.00 USD | 87,180.00 USD | 136,500.00 USD | 43,160.00 USD |
| `7D` | `2031.90` | 885,730,000.00 USD | 0.00 USD | 885,730,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD |
| `1D` | `2033.10` | 462,160,000.00 USD | 0.00 USD | 462,160,000.00 USD | 1,530,000.00 USD | 1,330,000.00 USD | 408,620.00 USD |
| `7D` | `2035.20` | 884,280,000.00 USD | 0.00 USD | 884,280,000.00 USD | 146,420.00 USD | 186,130.00 USD | 1,350,000.00 USD |
| `1D` | `2036.00` | 458,890,000.00 USD | 0.00 USD | 458,890,000.00 USD | 866,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2038.50` | 882,590,000.00 USD | 0.00 USD | 882,590,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2038.90` | 458,030,000.00 USD | 0.00 USD | 458,030,000.00 USD | 138,370.00 USD | 0.00 USD | 13,360.00 USD |
| `1D` | `2041.80` | 457,880,000.00 USD | 0.00 USD | 457,880,000.00 USD | 0.00 USD | 178,560.00 USD | 14,300.00 USD |
| `7D` | `2045.10` | 881,140,000.00 USD | 0.00 USD | 881,140,000.00 USD | 0.00 USD | 149,500.00 USD | 47,970.00 USD |
| `1D` | `2050.50` | 457,680,000.00 USD | 0.00 USD | 457,680,000.00 USD | 0.00 USD | 338,980.00 USD | 717,780.00 USD |
| `7D` | `2051.70` | 880,940,000.00 USD | 0.00 USD | 880,940,000.00 USD | 1,320,000.00 USD | 0.00 USD | 1,190,000.00 USD |
| `1D` | `2053.40` | 456,630,000.00 USD | 0.00 USD | 456,630,000.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD |
| `1D` | `2056.30` | 456,510,000.00 USD | 0.00 USD | 456,510,000.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2058.30` | 878,430,000.00 USD | 0.00 USD | 878,430,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD |
| `1D` | `2059.20` | 456,270,000.00 USD | 0.00 USD | 456,270,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `7D` | `2061.60` | 878,090,000.00 USD | 0.00 USD | 878,090,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD |
| `1D` | `2062.10` | 455,510,000.00 USD | 0.00 USD | 455,510,000.00 USD | 80,610.00 USD | 121,470.00 USD | 52,590.00 USD |
| `7D` | `2064.90` | 872,830,000.00 USD | 0.00 USD | 872,830,000.00 USD | 1,230,000.00 USD | 313,000.00 USD | 979,910.00 USD |
| `1D` | `2065.00` | 455,260,000.00 USD | 0.00 USD | 455,260,000.00 USD | 984,680.00 USD | 537,030.00 USD | 598,250.00 USD |
| `1D` | `2067.90` | 453,140,000.00 USD | 0.00 USD | 453,140,000.00 USD | 387,410.00 USD | 1,010,000.00 USD | 50,470.00 USD |
| `7D` | `2068.20` | 870,310,000.00 USD | 0.00 USD | 870,310,000.00 USD | 1,740,000.00 USD | 1,860,000.00 USD | 893,570.00 USD |
| `1D` | `2070.80` | 451,690,000.00 USD | 0.00 USD | 451,690,000.00 USD | 1,100,000.00 USD | 854,090.00 USD | 437,490.00 USD |
| `7D` | `2071.50` | 865,810,000.00 USD | 0.00 USD | 865,810,000.00 USD | 2,820,000.00 USD | 2,410,000.00 USD | 1,230,000.00 USD |
| `1D` | `2073.70` | 449,300,000.00 USD | 0.00 USD | 449,300,000.00 USD | 419,970.00 USD | 62,630.00 USD | 926,730.00 USD |
| `7D` | `2074.80` | 859,350,000.00 USD | 0.00 USD | 859,350,000.00 USD | 4,370,000.00 USD | 3,270,000.00 USD | 4,050,000.00 USD |
| `1D` | `2076.60` | 447,890,000.00 USD | 0.00 USD | 447,890,000.00 USD | 2,580,000.00 USD | 1,020,000.00 USD | 2,000,000.00 USD |
| `7D` | `2078.10` | 847,650,000.00 USD | 0.00 USD | 847,650,000.00 USD | 5,560,000.00 USD | 4,320,000.00 USD | 2,410,000.00 USD |
| `1D` | `2079.50` | 442,290,000.00 USD | 0.00 USD | 442,290,000.00 USD | 1,700,000.00 USD | 1,270,000.00 USD | 443,980.00 USD |
| `7D` | `2081.40` | 835,360,000.00 USD | 0.00 USD | 835,360,000.00 USD | 4,720,000.00 USD | 3,420,000.00 USD | 2,500,000.00 USD |
| `1D` | `2082.40` | 438,870,000.00 USD | 0.00 USD | 438,870,000.00 USD | 1,610,000.00 USD | 1,140,000.00 USD | 224,010.00 USD |
| `7D` | `2084.70` | 824,730,000.00 USD | 0.00 USD | 824,730,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 4,900,000.00 USD |
| `1D` | `2085.30` | 435,890,000.00 USD | 0.00 USD | 435,890,000.00 USD | 2,180,000.00 USD | 1,820,000.00 USD | 1,830,000.00 USD |
| `7D` | `2088.00` | 815,930,000.00 USD | 0.00 USD | 815,930,000.00 USD | 3,990,000.00 USD | 2,780,000.00 USD | 1,650,000.00 USD |
| `1D` | `2088.20` | 430,070,000.00 USD | 0.00 USD | 430,070,000.00 USD | 1,730,000.00 USD | 1,000,000.00 USD | 605,040.00 USD |
| `1D` | `2091.10` | 426,720,000.00 USD | 0.00 USD | 426,720,000.00 USD | 1,250,000.00 USD | 423,330.00 USD | 520,600.00 USD |
| `7D` | `2091.30` | 807,510,000.00 USD | 0.00 USD | 807,510,000.00 USD | 4,410,000.00 USD | 952,210.00 USD | 7,590,000.00 USD |
| `1D` | `2094.00` | 424,530,000.00 USD | 0.00 USD | 424,530,000.00 USD | 1,800,000.00 USD | 1,330,000.00 USD | 1,350,000.00 USD |
| `7D` | `2094.60` | 794,550,000.00 USD | 0.00 USD | 794,550,000.00 USD | 5,720,000.00 USD | 2,160,000.00 USD | 2,340,000.00 USD |
| `1D` | `2096.90` | 420,050,000.00 USD | 0.00 USD | 420,050,000.00 USD | 1,010,000.00 USD | 797,210.00 USD | 1,510,000.00 USD |
| `7D` | `2097.90` | 784,330,000.00 USD | 0.00 USD | 784,330,000.00 USD | 2,340,000.00 USD | 3,210,000.00 USD | 1,290,000.00 USD |
| `1D` | `2099.80` | 416,740,000.00 USD | 0.00 USD | 416,740,000.00 USD | 194,900.00 USD | 700,850.00 USD | 11,930.00 USD |
| `7D` | `2101.20` | 777,490,000.00 USD | 0.00 USD | 777,490,000.00 USD | 999,530.00 USD | 1,580,000.00 USD | 4,020,000.00 USD |
| `1D` | `2102.70` | 415,830,000.00 USD | 0.00 USD | 415,830,000.00 USD | 530,980.00 USD | 289,160.00 USD | 466,670.00 USD |
| `7D` | `2104.50` | 770,890,000.00 USD | 0.00 USD | 770,890,000.00 USD | 2,010,000.00 USD | 1,180,000.00 USD | 2,250,000.00 USD |
| `1D` | `2105.60` | 414,540,000.00 USD | 0.00 USD | 414,540,000.00 USD | 652,720.00 USD | 671,930.00 USD | 422,940.00 USD |
| `7D` | `2107.80` | 765,450,000.00 USD | 0.00 USD | 765,450,000.00 USD | 2,380,000.00 USD | 452,470.00 USD | 1,650,000.00 USD |
| `1D` | `2108.50` | 412,800,000.00 USD | 0.00 USD | 412,800,000.00 USD | 600,390.00 USD | 21,400.00 USD | 102,370.00 USD |
| `7D` | `2111.10` | 760,970,000.00 USD | 0.00 USD | 760,970,000.00 USD | 3,530,000.00 USD | 2,350,000.00 USD | 2,170,000.00 USD |
| `1D` | `2111.40` | 412,070,000.00 USD | 0.00 USD | 412,070,000.00 USD | 490,860.00 USD | 146,050.00 USD | 193,960.00 USD |
| `1D` | `2114.30` | 411,240,000.00 USD | 0.00 USD | 411,240,000.00 USD | 420,950.00 USD | 507,320.00 USD | 389,310.00 USD |
| `7D` | `2114.40` | 752,920,000.00 USD | 0.00 USD | 752,920,000.00 USD | 1,080,000.00 USD | 1,850,000.00 USD | 3,800,000.00 USD |
| `1D` | `2117.20` | 409,920,000.00 USD | 0.00 USD | 409,920,000.00 USD | 202,840.00 USD | 15,250.00 USD | 635,290.00 USD |
| `7D` | `2117.70` | 746,190,000.00 USD | 0.00 USD | 746,190,000.00 USD | 3,430,000.00 USD | 2,020,000.00 USD | 3,380,000.00 USD |
| `1D` | `2120.10` | 409,070,000.00 USD | 0.00 USD | 409,070,000.00 USD | 198,890.00 USD | 431,090.00 USD | 1,100,000.00 USD |
| `7D` | `2121.00` | 737,360,000.00 USD | 0.00 USD | 737,360,000.00 USD | 3,650,000.00 USD | 1,340,000.00 USD | 1,820,000.00 USD |
| `1D` | `2123.00` | 407,340,000.00 USD | 0.00 USD | 407,340,000.00 USD | 1,320,000.00 USD | 683,920.00 USD | 1,140,000.00 USD |
| `7D` | `2124.30` | 730,550,000.00 USD | 0.00 USD | 730,550,000.00 USD | 832,850.00 USD | 972,650.00 USD | 1,510,000.00 USD |
| `1D` | `2125.90` | 404,190,000.00 USD | 0.00 USD | 404,190,000.00 USD | 179,030.00 USD | 1,330,000.00 USD | 486,980.00 USD |
| `7D` | `2127.60` | 727,230,000.00 USD | 0.00 USD | 727,230,000.00 USD | 2,400,000.00 USD | 2,630,000.00 USD | 3,270,000.00 USD |
| `1D` | `2128.80` | 402,190,000.00 USD | 0.00 USD | 402,190,000.00 USD | 116,180.00 USD | 475,750.00 USD | 318,170.00 USD |
| `7D` | `2130.90` | 718,930,000.00 USD | 0.00 USD | 718,930,000.00 USD | 2,410,000.00 USD | 2,300,000.00 USD | 1,700,000.00 USD |
| `1D` | `2131.70` | 401,280,000.00 USD | 0.00 USD | 401,280,000.00 USD | 0.00 USD | 18,610.00 USD | 331,620.00 USD |
| `7D` | `2134.20` | 712,510,000.00 USD | 0.00 USD | 712,510,000.00 USD | 2,170,000.00 USD | 550,450.00 USD | 308,060.00 USD |
| `1D` | `2137.50` | 400,930,000.00 USD | 0.00 USD | 400,930,000.00 USD | 0.00 USD | 278,410.00 USD | 0.00 USD |
| `7D` | `2137.50` | 709,480,000.00 USD | 0.00 USD | 709,480,000.00 USD | 1,040,000.00 USD | 880,790.00 USD | 43,560.00 USD |
| `7D` | `2140.80` | 707,520,000.00 USD | 0.00 USD | 707,520,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD |
| `7D` | `2144.10` | 703,590,000.00 USD | 0.00 USD | 703,590,000.00 USD | 449,020.00 USD | 1,130,000.00 USD | 268,500.00 USD |
| `7D` | `2147.40` | 701,740,000.00 USD | 0.00 USD | 701,740,000.00 USD | 657,710.00 USD | 421,320.00 USD | 0.00 USD |
| `7D` | `2150.70` | 700,660,000.00 USD | 0.00 USD | 700,660,000.00 USD | 459,630.00 USD | 463,640.00 USD | 31,040.00 USD |
| `1D` | `2152.00` | 400,650,000.00 USD | 0.00 USD | 400,650,000.00 USD | 208,250.00 USD | 440,530.00 USD | 0.00 USD |
| `7D` | `2154.00` | 699,710,000.00 USD | 0.00 USD | 699,710,000.00 USD | 128,430.00 USD | 331,520.00 USD | 32,590.00 USD |
| `1D` | `2154.90` | 400,000,000.00 USD | 0.00 USD | 400,000,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD |
| `7D` | `2157.30` | 699,210,000.00 USD | 0.00 USD | 699,210,000.00 USD | 388,210.00 USD | 1,030,000.00 USD | 1,080,000.00 USD |
| `1D` | `2157.80` | 398,600,000.00 USD | 0.00 USD | 398,600,000.00 USD | 0.00 USD | 0.00 USD | 37,580.00 USD |
| `7D` | `2160.60` | 696,720,000.00 USD | 0.00 USD | 696,720,000.00 USD | 613,630.00 USD | 1,900,000.00 USD | 1,990,000.00 USD |
| `1D` | `2160.70` | 398,570,000.00 USD | 0.00 USD | 398,570,000.00 USD | 0.00 USD | 2,290,000.00 USD | 71,920.00 USD |
| `1D` | `2163.60` | 396,210,000.00 USD | 0.00 USD | 396,210,000.00 USD | 0.00 USD | 999,490.00 USD | 28,620.00 USD |
| `7D` | `2163.90` | 692,200,000.00 USD | 0.00 USD | 692,200,000.00 USD | 566,120.00 USD | 3,280,000.00 USD | 1,290,000.00 USD |
| `1D` | `2166.50` | 395,180,000.00 USD | 0.00 USD | 395,180,000.00 USD | 1,690,000.00 USD | 341,240.00 USD | 1,130,000.00 USD |
| `7D` | `2167.20` | 687,060,000.00 USD | 0.00 USD | 687,060,000.00 USD | 25,540.00 USD | 3,620,000.00 USD | 50,240.00 USD |
| `1D` | `2169.40` | 392,020,000.00 USD | 0.00 USD | 392,020,000.00 USD | 6,960,000.00 USD | 4,810,000.00 USD | 2,130,000.00 USD |
| `7D` | `2170.50` | 683,360,000.00 USD | 0.00 USD | 683,360,000.00 USD | 3,500,000.00 USD | 3,730,000.00 USD | 5,210,000.00 USD |
| `1D` | `2172.30` | 378,120,000.00 USD | 0.00 USD | 378,120,000.00 USD | 0.00 USD | 365,630.00 USD | 1,120,000.00 USD |
| `7D` | `2173.80` | 670,920,000.00 USD | 0.00 USD | 670,920,000.00 USD | 4,370,000.00 USD | 363,040.00 USD | 1,010,000.00 USD |
| `1D` | `2175.20` | 376,640,000.00 USD | 0.00 USD | 376,640,000.00 USD | 345,940.00 USD | 301,420.00 USD | 33,400.00 USD |
| `7D` | `2177.10` | 665,180,000.00 USD | 0.00 USD | 665,180,000.00 USD | 0.00 USD | 0.00 USD | 1,320,000.00 USD |
| `1D` | `2178.10` | 375,960,000.00 USD | 0.00 USD | 375,960,000.00 USD | 0.00 USD | 1,400,000.00 USD | 49,860.00 USD |
| `7D` | `2180.40` | 663,860,000.00 USD | 0.00 USD | 663,860,000.00 USD | 0.00 USD | 373,740.00 USD | 176,950.00 USD |
| `1D` | `2181.00` | 374,510,000.00 USD | 0.00 USD | 374,510,000.00 USD | 2,080,000.00 USD | 478,110.00 USD | 1,370,000.00 USD |
| `7D` | `2183.70` | 663,310,000.00 USD | 0.00 USD | 663,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 2,550,000.00 USD |
| `1D` | `2183.90` | 370,590,000.00 USD | 0.00 USD | 370,590,000.00 USD | 1,350,000.00 USD | 509,320.00 USD | 13,020.00 USD |
| `1D` | `2186.80` | 368,710,000.00 USD | 0.00 USD | 368,710,000.00 USD | 0.00 USD | 1,450,000.00 USD | 1,790,000.00 USD |
| `7D` | `2187.00` | 659,460,000.00 USD | 0.00 USD | 659,460,000.00 USD | 556,600.00 USD | 0.00 USD | 54,020.00 USD |
| `1D` | `2189.70` | 365,470,000.00 USD | 0.00 USD | 365,470,000.00 USD | 0.00 USD | 0.00 USD | 693,960.00 USD |
| `7D` | `2190.30` | 658,850,000.00 USD | 0.00 USD | 658,850,000.00 USD | 2,730,000.00 USD | 0.00 USD | 4,200,000.00 USD |
| `1D` | `2192.60` | 364,770,000.00 USD | 0.00 USD | 364,770,000.00 USD | 605,210.00 USD | 222,200.00 USD | 109,400.00 USD |
| `1D` | `2195.50` | 363,840,000.00 USD | 0.00 USD | 363,840,000.00 USD | 0.00 USD | 881,070.00 USD | 1,890,000.00 USD |
| `7D` | `2196.90` | 651,920,000.00 USD | 0.00 USD | 651,920,000.00 USD | 2,580,000.00 USD | 474,090.00 USD | 2,040,000.00 USD |
| `1D` | `2198.40` | 361,070,000.00 USD | 0.00 USD | 361,070,000.00 USD | 416,500.00 USD | 149,110.00 USD | 50,830.00 USD |
| `7D` | `2200.20` | 646,830,000.00 USD | 0.00 USD | 646,830,000.00 USD | 3,000,000.00 USD | 5,080,000.00 USD | 3,200,000.00 USD |
| `1D` | `2201.30` | 360,450,000.00 USD | 0.00 USD | 360,450,000.00 USD | 1,690,000.00 USD | 4,250,000.00 USD | 1,500,000.00 USD |
| `7D` | `2203.50` | 635,550,000.00 USD | 0.00 USD | 635,550,000.00 USD | 3,650,000.00 USD | 1,710,000.00 USD | 3,750,000.00 USD |
| `1D` | `2204.20` | 353,010,000.00 USD | 0.00 USD | 353,010,000.00 USD | 2,130,000.00 USD | 314,310.00 USD | 867,420.00 USD |
| `7D` | `2206.80` | 626,440,000.00 USD | 0.00 USD | 626,440,000.00 USD | 6,920,000.00 USD | 9,430,000.00 USD | 4,020,000.00 USD |
| `1D` | `2207.10` | 349,700,000.00 USD | 0.00 USD | 349,700,000.00 USD | 2,210,000.00 USD | 10,880,000.00 USD | 2,030,000.00 USD |
| `1D` | `2210.00` | 334,580,000.00 USD | 0.00 USD | 334,580,000.00 USD | 3,190,000.00 USD | 3,380,000.00 USD | 2,690,000.00 USD |
| `7D` | `2210.10` | 606,070,000.00 USD | 0.00 USD | 606,070,000.00 USD | 12,800,000.00 USD | 20,410,000.00 USD | 6,470,000.00 USD |
| `1D` | `2212.90` | 325,320,000.00 USD | 0.00 USD | 325,320,000.00 USD | 9,880,000.00 USD | 8,670,000.00 USD | 4,390,000.00 USD |
| `7D` | `2213.40` | 566,390,000.00 USD | 0.00 USD | 566,390,000.00 USD | 10,920,000.00 USD | 14,590,000.00 USD | 19,950,000.00 USD |
| `1D` | `2215.80` | 302,380,000.00 USD | 0.00 USD | 302,380,000.00 USD | 18,430,000.00 USD | 9,760,000.00 USD | 12,400,000.00 USD |
| `7D` | `2216.70` | 520,920,000.00 USD | 0.00 USD | 520,920,000.00 USD | 25,710,000.00 USD | 17,030,000.00 USD | 9,390,000.00 USD |
| `1D` | `2218.70` | 261,780,000.00 USD | 0.00 USD | 261,780,000.00 USD | 6,790,000.00 USD | 7,780,000.00 USD | 1,880,000.00 USD |
| `7D` | `2220.00` | 468,790,000.00 USD | 0.00 USD | 468,790,000.00 USD | 24,310,000.00 USD | 12,300,000.00 USD | 12,760,000.00 USD |
| `1D` | `2221.60` | 245,340,000.00 USD | 0.00 USD | 245,340,000.00 USD | 6,200,000.00 USD | 12,240,000.00 USD | 1,340,000.00 USD |
| `7D` | `2223.30` | 419,420,000.00 USD | 0.00 USD | 419,420,000.00 USD | 10,150,000.00 USD | 8,220,000.00 USD | 11,910,000.00 USD |
| `1D` | `2224.50` | 225,560,000.00 USD | 0.00 USD | 225,560,000.00 USD | 9,730,000.00 USD | 5,030,000.00 USD | 5,660,000.00 USD |
| `7D` | `2226.60` | 389,140,000.00 USD | 0.00 USD | 389,140,000.00 USD | 12,840,000.00 USD | 11,030,000.00 USD | 9,960,000.00 USD |
| `1D` | `2227.40` | 205,150,000.00 USD | 0.00 USD | 205,150,000.00 USD | 5,940,000.00 USD | 13,200,000.00 USD | 5,610,000.00 USD |
| `7D` | `2229.90` | 355,320,000.00 USD | 0.00 USD | 355,320,000.00 USD | 12,730,000.00 USD | 11,790,000.00 USD | 25,750,000.00 USD |
| `1D` | `2230.30` | 180,390,000.00 USD | 0.00 USD | 180,390,000.00 USD | 6,830,000.00 USD | 8,320,000.00 USD | 2,410,000.00 USD |
| `1D` | `2233.20` | 162,820,000.00 USD | 0.00 USD | 162,820,000.00 USD | 5,060,000.00 USD | 4,220,000.00 USD | 8,040,000.00 USD |
| `7D` | `2233.20` | 305,050,000.00 USD | 0.00 USD | 305,050,000.00 USD | 16,600,000.00 USD | 24,290,000.00 USD | 10,420,000.00 USD |
| `1D` | `2236.10` | 145,500,000.00 USD | 0.00 USD | 145,500,000.00 USD | 23,180,000.00 USD | 0.00 USD | 10,790,000.00 USD |
| `7D` | `2236.50` | 253,730,000.00 USD | 0.00 USD | 253,730,000.00 USD | 16,050,000.00 USD | 7,430,000.00 USD | 27,770,000.00 USD |
| `1D` | `2239.00` | 111,530,000.00 USD | 0.00 USD | 111,530,000.00 USD | 17,940,000.00 USD | 7,390,000.00 USD | 13,890,000.00 USD |
| `7D` | `2239.80` | 202,490,000.00 USD | 0.00 USD | 202,490,000.00 USD | 16,720,000.00 USD | 6,600,000.00 USD | 13,750,000.00 USD |
| `1D` | `2241.90` | 72,320,000.00 USD | 0.00 USD | 72,320,000.00 USD | 619,130.00 USD | 760,920.00 USD | 5,370,000.00 USD |
| `7D` | `2243.10` | 165,420,000.00 USD | 0.00 USD | 165,420,000.00 USD | 22,920,000.00 USD | 0.00 USD | 18,320,000.00 USD |
| `1D` | `2244.80` | 65,570,000.00 USD | 0.00 USD | 65,570,000.00 USD | 3,850,000.00 USD | 4,700,000.00 USD | 463,790.00 USD |
| `7D` | `2246.40` | 124,170,000.00 USD | 0.00 USD | 124,170,000.00 USD | 14,340,000.00 USD | 0.00 USD | 13,920,000.00 USD |
| `1D` | `2247.70` | 56,550,000.00 USD | 0.00 USD | 56,550,000.00 USD | 12,800,000.00 USD | 0.00 USD | 7,080,000.00 USD |
| `7D` | `2249.70` | 95,910,000.00 USD | 0.00 USD | 95,910,000.00 USD | 18,000,000.00 USD | 0.00 USD | 12,820,000.00 USD |
| `1D` | `2250.60` | 36,670,000.00 USD | 0.00 USD | 36,670,000.00 USD | 4,190,000.00 USD | 1,910,000.00 USD | 3,960,000.00 USD |
| `7D` | `2253.00` | 65,090,000.00 USD | 0.00 USD | 65,090,000.00 USD | 26,890,000.00 USD | 0.00 USD | 12,040,000.00 USD |
| `1D` | `2253.50` | 26,600,000.00 USD | 0.00 USD | 26,600,000.00 USD | 5,410,000.00 USD | 4,440,000.00 USD | 4,550,000.00 USD |
| `7D` | `2256.30` | 26,160,000.00 USD | 0.00 USD | 26,160,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2256.40` | 12,200,000.00 USD | 0.00 USD | 12,200,000.00 USD | 0.00 USD | 3,390,000.00 USD | 0.00 USD |
| `7D` | `2259.60` | 10,940,000.00 USD | 0.00 USD | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2262.20` | 8,810,000.00 USD | 0.00 USD | 8,810,000.00 USD | 2,420,000.00 USD | 0.00 USD | 156,010.00 USD |
| `1D` | `2265.10` | 6,240,000.00 USD | 0.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 1,800,000.00 USD |
| `7D` | `2266.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2268.00` | 4,440,000.00 USD | 0.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 4,440,000.00 USD |
| `1D` | `2270.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2273.80` | 220,250.00 USD | 220,250.00 USD | 0.00 USD | 220,250.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2276.70` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 1,370,000.00 USD | 555,110.00 USD | 114,460.00 USD |
| `7D` | `2279.40` | 17,000,000.00 USD | 17,000,000.00 USD | 0.00 USD | 0.00 USD | 17,000,000.00 USD | 0.00 USD |
| `1D` | `2279.60` | 35,820,000.00 USD | 35,820,000.00 USD | 0.00 USD | 23,020,000.00 USD | 6,030,000.00 USD | 4,520,000.00 USD |
| `1D` | `2282.50` | 138,270,000.00 USD | 138,270,000.00 USD | 0.00 USD | 51,860,000.00 USD | 39,620,000.00 USD | 10,980,000.00 USD |
| `7D` | `2282.70` | 117,630,000.00 USD | 117,630,000.00 USD | 0.00 USD | 0.00 USD | 87,090,000.00 USD | 13,550,000.00 USD |
| `1D` | `2285.40` | 156,400,000.00 USD | 156,400,000.00 USD | 0.00 USD | 7,830,000.00 USD | 4,510,000.00 USD | 5,790,000.00 USD |
| `7D` | `2286.00` | 128,050,000.00 USD | 128,050,000.00 USD | 0.00 USD | 1,010,000.00 USD | 9,400,000.00 USD | 0.00 USD |
| `1D` | `2288.30` | 157,300,000.00 USD | 157,300,000.00 USD | 0.00 USD | 0.00 USD | 760,920.00 USD | 133,600.00 USD |
| `7D` | `2289.30` | 133,330,000.00 USD | 133,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,280,000.00 USD |
| `1D` | `2291.20` | 166,330,000.00 USD | 166,330,000.00 USD | 0.00 USD | 0.00 USD | 8,840,000.00 USD | 199,420.00 USD |
| `1D` | `2294.10` | 180,200,000.00 USD | 180,200,000.00 USD | 0.00 USD | 8,310,000.00 USD | 0.00 USD | 5,560,000.00 USD |
| `7D` | `2295.90` | 148,010,000.00 USD | 148,010,000.00 USD | 0.00 USD | 6,580,000.00 USD | 2,380,000.00 USD | 5,720,000.00 USD |
| `1D` | `2297.00` | 194,220,000.00 USD | 194,220,000.00 USD | 0.00 USD | 5,410,000.00 USD | 8,350,000.00 USD | 253,130.00 USD |
| `7D` | `2299.20` | 176,420,000.00 USD | 176,420,000.00 USD | 0.00 USD | 11,730,000.00 USD | 11,130,000.00 USD | 5,560,000.00 USD |
| `1D` | `2299.90` | 209,590,000.00 USD | 209,590,000.00 USD | 0.00 USD | 0.00 USD | 7,970,000.00 USD | 7,390,000.00 USD |
| `7D` | `2302.50` | 223,540,000.00 USD | 223,540,000.00 USD | 0.00 USD | 23,020,000.00 USD | 7,250,000.00 USD | 16,850,000.00 USD |
| `1D` | `2302.80` | 230,410,000.00 USD | 230,410,000.00 USD | 0.00 USD | 15,230,000.00 USD | 682,490.00 USD | 4,910,000.00 USD |
| `1D` | `2305.70` | 262,380,000.00 USD | 262,380,000.00 USD | 0.00 USD | 10,430,000.00 USD | 15,620,000.00 USD | 5,930,000.00 USD |
| `7D` | `2305.80` | 244,310,000.00 USD | 244,310,000.00 USD | 0.00 USD | 2,980,000.00 USD | 8,820,000.00 USD | 8,970,000.00 USD |
| `1D` | `2308.60` | 268,140,000.00 USD | 268,140,000.00 USD | 0.00 USD | 2,420,000.00 USD | 2,340,000.00 USD | 994,140.00 USD |
| `7D` | `2309.10` | 248,590,000.00 USD | 248,590,000.00 USD | 0.00 USD | 1,240,000.00 USD | 930,630.00 USD | 2,110,000.00 USD |
| `1D` | `2311.50` | 277,780,000.00 USD | 277,780,000.00 USD | 0.00 USD | 691,870.00 USD | 1,260,000.00 USD | 7,690,000.00 USD |
| `7D` | `2312.40` | 266,730,000.00 USD | 266,730,000.00 USD | 0.00 USD | 7,270,000.00 USD | 0.00 USD | 10,870,000.00 USD |
| `1D` | `2314.40` | 292,120,000.00 USD | 292,120,000.00 USD | 0.00 USD | 0.00 USD | 14,100,000.00 USD | 231,520.00 USD |
| `7D` | `2315.70` | 274,300,000.00 USD | 274,300,000.00 USD | 0.00 USD | 0.00 USD | 7,460,000.00 USD | 117,510.00 USD |
| `1D` | `2317.30` | 320,660,000.00 USD | 320,660,000.00 USD | 0.00 USD | 10,230,000.00 USD | 10,470,000.00 USD | 7,850,000.00 USD |
| `7D` | `2319.00` | 285,490,000.00 USD | 285,490,000.00 USD | 0.00 USD | 1,020,000.00 USD | 4,550,000.00 USD | 5,620,000.00 USD |
| `1D` | `2320.20` | 336,780,000.00 USD | 336,780,000.00 USD | 0.00 USD | 6,580,000.00 USD | 9,360,000.00 USD | 173,650.00 USD |
| `7D` | `2322.30` | 302,650,000.00 USD | 302,650,000.00 USD | 0.00 USD | 1,110,000.00 USD | 15,930,000.00 USD | 108,040.00 USD |
| `1D` | `2323.10` | 351,350,000.00 USD | 351,350,000.00 USD | 0.00 USD | 572,970.00 USD | 10,410,000.00 USD | 3,590,000.00 USD |
| `7D` | `2325.60` | 323,300,000.00 USD | 323,300,000.00 USD | 0.00 USD | 9,720,000.00 USD | 2,540,000.00 USD | 8,390,000.00 USD |
| `1D` | `2326.00` | 363,030,000.00 USD | 363,030,000.00 USD | 0.00 USD | 479,120.00 USD | 5,550,000.00 USD | 5,660,000.00 USD |
| `1D` | `2328.90` | 370,010,000.00 USD | 370,010,000.00 USD | 0.00 USD | 5,690,000.00 USD | 884,940.00 USD | 402,280.00 USD |
| `7D` | `2328.90` | 335,130,000.00 USD | 335,130,000.00 USD | 0.00 USD | 3,860,000.00 USD | 0.00 USD | 7,960,000.00 USD |
| `1D` | `2331.80` | 386,300,000.00 USD | 386,300,000.00 USD | 0.00 USD | 15,910,000.00 USD | 251,940.00 USD | 126,990.00 USD |
| `7D` | `2332.20` | 364,360,000.00 USD | 364,360,000.00 USD | 0.00 USD | 29,230,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2334.70` | 409,870,000.00 USD | 409,870,000.00 USD | 0.00 USD | 13,410,000.00 USD | 2,960,000.00 USD | 7,200,000.00 USD |
| `7D` | `2335.50` | 422,370,000.00 USD | 422,370,000.00 USD | 0.00 USD | 28,990,000.00 USD | 18,420,000.00 USD | 10,600,000.00 USD |
| `1D` | `2337.60` | 423,750,000.00 USD | 423,750,000.00 USD | 0.00 USD | 9,880,000.00 USD | 407,920.00 USD | 3,600,000.00 USD |
| `7D` | `2338.80` | 440,240,000.00 USD | 440,240,000.00 USD | 0.00 USD | 9,570,000.00 USD | 0.00 USD | 8,310,000.00 USD |
| `1D` | `2340.50` | 447,640,000.00 USD | 447,640,000.00 USD | 0.00 USD | 8,010,000.00 USD | 5,100,000.00 USD | 10,780,000.00 USD |
| `7D` | `2342.10` | 480,350,000.00 USD | 480,350,000.00 USD | 0.00 USD | 4,720,000.00 USD | 21,390,000.00 USD | 14,000,000.00 USD |
| `1D` | `2343.40` | 462,280,000.00 USD | 462,280,000.00 USD | 0.00 USD | 2,060,000.00 USD | 5,580,000.00 USD | 7,000,000.00 USD |
| `7D` | `2345.40` | 501,720,000.00 USD | 501,720,000.00 USD | 0.00 USD | 1,350,000.00 USD | 13,990,000.00 USD | 6,020,000.00 USD |
| `1D` | `2346.30` | 475,180,000.00 USD | 475,180,000.00 USD | 0.00 USD | 4,950,000.00 USD | 1,940,000.00 USD | 6,020,000.00 USD |
| `7D` | `2348.70` | 539,590,000.00 USD | 539,590,000.00 USD | 0.00 USD | 847,620.00 USD | 9,500,000.00 USD | 27,530,000.00 USD |
| `1D` | `2349.20` | 501,430,000.00 USD | 501,430,000.00 USD | 0.00 USD | 13,670,000.00 USD | 6,150,000.00 USD | 6,430,000.00 USD |
| `7D` | `2352.00` | 576,470,000.00 USD | 576,470,000.00 USD | 0.00 USD | 3,190,000.00 USD | 23,060,000.00 USD | 10,630,000.00 USD |
| `1D` | `2352.10` | 537,420,000.00 USD | 537,420,000.00 USD | 0.00 USD | 24,370,000.00 USD | 4,590,000.00 USD | 7,030,000.00 USD |
| `1D` | `2355.00` | 559,200,000.00 USD | 559,200,000.00 USD | 0.00 USD | 1,010,000.00 USD | 19,500,000.00 USD | 1,280,000.00 USD |
| `7D` | `2355.30` | 631,060,000.00 USD | 631,060,000.00 USD | 0.00 USD | 16,520,000.00 USD | 36,690,000.00 USD | 1,380,000.00 USD |
| `1D` | `2357.90` | 569,890,000.00 USD | 569,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 4,290,000.00 USD | 3,500,000.00 USD |
| `7D` | `2358.60` | 643,200,000.00 USD | 643,200,000.00 USD | 0.00 USD | 7,110,000.00 USD | 512,220.00 USD | 4,510,000.00 USD |
| `1D` | `2360.80` | 591,130,000.00 USD | 591,130,000.00 USD | 0.00 USD | 10,720,000.00 USD | 5,400,000.00 USD | 5,130,000.00 USD |
| `7D` | `2361.90` | 650,320,000.00 USD | 650,320,000.00 USD | 0.00 USD | 3,150,000.00 USD | 3,800,000.00 USD | 176,950.00 USD |
| `1D` | `2363.70` | 616,990,000.00 USD | 616,990,000.00 USD | 0.00 USD | 7,900,000.00 USD | 9,120,000.00 USD | 8,830,000.00 USD |
| `7D` | `2365.20` | 668,220,000.00 USD | 668,220,000.00 USD | 0.00 USD | 8,440,000.00 USD | 0.00 USD | 9,460,000.00 USD |
| `1D` | `2366.60` | 622,680,000.00 USD | 622,680,000.00 USD | 0.00 USD | 3,560,000.00 USD | 509,320.00 USD | 1,620,000.00 USD |
| `7D` | `2368.50` | 681,290,000.00 USD | 681,290,000.00 USD | 0.00 USD | 10,830,000.00 USD | 1,780,000.00 USD | 458,400.00 USD |
| `1D` | `2369.50` | 649,180,000.00 USD | 649,180,000.00 USD | 0.00 USD | 13,850,000.00 USD | 7,720,000.00 USD | 4,920,000.00 USD |
| `7D` | `2371.80` | 762,230,000.00 USD | 762,230,000.00 USD | 0.00 USD | 26,000,000.00 USD | 0.00 USD | 54,940,000.00 USD |
| `1D` | `2372.40` | 686,700,000.00 USD | 686,700,000.00 USD | 0.00 USD | 14,410,000.00 USD | 10,690,000.00 USD | 12,430,000.00 USD |
| `7D` | `2375.10` | 789,170,000.00 USD | 789,170,000.00 USD | 0.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD |
| `1D` | `2375.30` | 708,220,000.00 USD | 708,220,000.00 USD | 0.00 USD | 14,210,000.00 USD | 3,650,000.00 USD | 3,660,000.00 USD |
| `1D` | `2378.20` | 733,440,000.00 USD | 733,440,000.00 USD | 0.00 USD | 5,350,000.00 USD | 7,910,000.00 USD | 11,950,000.00 USD |
| `7D` | `2378.40` | 834,590,000.00 USD | 834,590,000.00 USD | 0.00 USD | 11,800,000.00 USD | 7,950,000.00 USD | 25,670,000.00 USD |
| `1D` | `2381.10` | 782,790,000.00 USD | 782,790,000.00 USD | 0.00 USD | 16,150,000.00 USD | 13,170,000.00 USD | 20,030,000.00 USD |
| `7D` | `2381.70` | 874,370,000.00 USD | 874,370,000.00 USD | 0.00 USD | 8,510,000.00 USD | 6,750,000.00 USD | 24,530,000.00 USD |
| `1D` | `2384.00` | 826,420,000.00 USD | 826,420,000.00 USD | 0.00 USD | 17,870,000.00 USD | 15,110,000.00 USD | 10,650,000.00 USD |
| `7D` | `2385.00` | 976,090,000.00 USD | 976,090,000.00 USD | 0.00 USD | 18,550,000.00 USD | 36,910,000.00 USD | 46,260,000.00 USD |
| `1D` | `2386.90` | 862,130,000.00 USD | 862,130,000.00 USD | 0.00 USD | 13,540,000.00 USD | 11,770,000.00 USD | 10,400,000.00 USD |
| `7D` | `2388.30` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 5,290,000.00 USD | 38,070,000.00 USD | 44,510,000.00 USD |
| `1D` | `2389.80` | 887,830,000.00 USD | 887,830,000.00 USD | 0.00 USD | 10,230,000.00 USD | 9,340,000.00 USD | 6,130,000.00 USD |
| `7D` | `2391.60` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 8,560,000.00 USD | 52,080,000.00 USD | 40,380,000.00 USD |
| `1D` | `2392.70` | 905,880,000.00 USD | 905,880,000.00 USD | 0.00 USD | 5,770,000.00 USD | 4,950,000.00 USD | 7,340,000.00 USD |
| `7D` | `2394.90` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 0.00 USD | 57,450,000.00 USD | 32,260,000.00 USD | 37,090,000.00 USD |
| `1D` | `2395.60` | 921,360,000.00 USD | 921,360,000.00 USD | 0.00 USD | 5,140,000.00 USD | 6,720,000.00 USD | 3,630,000.00 USD |
| `7D` | `2398.20` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 42,820,000.00 USD | 38,210,000.00 USD | 29,190,000.00 USD |
| `1D` | `2398.50` | 941,040,000.00 USD | 941,040,000.00 USD | 0.00 USD | 5,800,000.00 USD | 6,760,000.00 USD | 7,120,000.00 USD |
| `1D` | `2401.40` | 965,980,000.00 USD | 965,980,000.00 USD | 0.00 USD | 8,280,000.00 USD | 7,500,000.00 USD | 9,170,000.00 USD |
| `7D` | `2401.50` | 1,510,000,000.00 USD | 1,510,000,000.00 USD | 0.00 USD | 51,970,000.00 USD | 26,780,000.00 USD | 29,090,000.00 USD |
| `1D` | `2404.30` | 995,550,000.00 USD | 995,550,000.00 USD | 0.00 USD | 9,990,000.00 USD | 11,060,000.00 USD | 8,510,000.00 USD |
| `7D` | `2404.80` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 50,800,000.00 USD | 32,200,000.00 USD | 24,110,000.00 USD |
| `1D` | `2407.20` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 0.00 USD | 15,160,000.00 USD | 9,260,000.00 USD | 7,710,000.00 USD |
| `7D` | `2408.10` | 1,710,000,000.00 USD | 1,710,000,000.00 USD | 0.00 USD | 34,390,000.00 USD | 31,420,000.00 USD | 25,030,000.00 USD |
| `1D` | `2410.10` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 7,660,000.00 USD | 7,700,000.00 USD | 9,120,000.00 USD |
| `7D` | `2411.40` | 1,790,000,000.00 USD | 1,790,000,000.00 USD | 0.00 USD | 19,200,000.00 USD | 32,580,000.00 USD | 27,660,000.00 USD |
| `1D` | `2413.00` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 0.00 USD | 8,270,000.00 USD | 5,470,000.00 USD | 3,790,000.00 USD |
| `7D` | `2414.70` | 1,860,000,000.00 USD | 1,860,000,000.00 USD | 0.00 USD | 24,010,000.00 USD | 21,950,000.00 USD | 23,130,000.00 USD |
| `1D` | `2415.90` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 0.00 USD | 3,710,000.00 USD | 2,920,000.00 USD | 3,620,000.00 USD |
| `7D` | `2418.00` | 1,930,000,000.00 USD | 1,930,000,000.00 USD | 0.00 USD | 34,060,000.00 USD | 15,260,000.00 USD | 24,610,000.00 USD |
| `1D` | `2418.80` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 4,240,000.00 USD | 2,710,000.00 USD | 3,900,000.00 USD |
| `7D` | `2421.30` | 2,010,000,000.00 USD | 2,010,000,000.00 USD | 0.00 USD | 25,700,000.00 USD | 27,770,000.00 USD | 21,590,000.00 USD |
| `1D` | `2421.70` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 6,390,000.00 USD | 6,200,000.00 USD | 6,250,000.00 USD |
| `1D` | `2424.60` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 1,790,000.00 USD | 2,770,000.00 USD | 1,020,000.00 USD |
| `7D` | `2424.60` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 0.00 USD | 23,840,000.00 USD | 34,930,000.00 USD | 34,520,000.00 USD |
| `1D` | `2427.50` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 731,900.00 USD | 124,100.00 USD | 601,200.00 USD |
| `7D` | `2427.90` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 0.00 USD | 25,200,000.00 USD | 18,380,000.00 USD | 26,460,000.00 USD |
| `1D` | `2430.40` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 1,640,000.00 USD | 1,770,000.00 USD | 1,230,000.00 USD |
| `7D` | `2431.20` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 0.00 USD | 10,380,000.00 USD | 17,060,000.00 USD | 9,300,000.00 USD |
| `1D` | `2433.30` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 2,160,000.00 USD | 2,160,000.00 USD | 1,220,000.00 USD |
| `7D` | `2434.50` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 0.00 USD | 27,390,000.00 USD | 21,570,000.00 USD | 11,160,000.00 USD |
| `1D` | `2436.20` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 2,340,000.00 USD | 475,290.00 USD | 579,580.00 USD |
| `7D` | `2437.80` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 0.00 USD | 12,000,000.00 USD | 12,820,000.00 USD | 5,470,000.00 USD |
| `1D` | `2439.10` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 304,760.00 USD | 641,280.00 USD | 484,910.00 USD |
| `7D` | `2441.10` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 0.00 USD | 15,080,000.00 USD | 8,120,000.00 USD | 10,680,000.00 USD |
| `1D` | `2442.00` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 2,360,000.00 USD | 2,020,000.00 USD | 735,530.00 USD |
| `7D` | `2444.40` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 0.00 USD | 8,860,000.00 USD | 15,100,000.00 USD | 14,000,000.00 USD |
| `1D` | `2444.90` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 544,880.00 USD | 1,480,000.00 USD |
| `7D` | `2447.70` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 0.00 USD | 11,480,000.00 USD | 8,450,000.00 USD | 17,330,000.00 USD |
| `1D` | `2447.80` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 687,490.00 USD | 330,760.00 USD | 1,530,000.00 USD |
| `1D` | `2450.70` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 2,540,000.00 USD | 1,470,000.00 USD | 3,400,000.00 USD |
| `7D` | `2451.00` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 0.00 USD | 16,710,000.00 USD | 14,100,000.00 USD | 16,480,000.00 USD |
| `1D` | `2453.60` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 4,790,000.00 USD | 4,000,000.00 USD | 3,460,000.00 USD |
| `7D` | `2454.30` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 0.00 USD | 4,620,000.00 USD | 4,930,000.00 USD | 3,880,000.00 USD |
| `1D` | `2456.50` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 1,060,000.00 USD | 2,650,000.00 USD | 2,020,000.00 USD |
| `7D` | `2457.60` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 0.00 USD | 15,150,000.00 USD | 12,540,000.00 USD | 12,600,000.00 USD |
| `1D` | `2459.40` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 1,900,000.00 USD | 1,190,000.00 USD | 366,800.00 USD |
| `7D` | `2460.90` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 0.00 USD | 5,580,000.00 USD | 8,670,000.00 USD | 6,870,000.00 USD |
| `1D` | `2462.30` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 490,260.00 USD | 1,620,000.00 USD |
| `7D` | `2464.20` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 0.00 USD | 8,720,000.00 USD | 7,700,000.00 USD | 4,700,000.00 USD |
| `1D` | `2465.20` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 83,300.00 USD | 176,210.00 USD | 0.00 USD |
| `7D` | `2467.50` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 0.00 USD | 4,540,000.00 USD | 3,710,000.00 USD | 586,780.00 USD |
| `1D` | `2468.10` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 1,250,000.00 USD | 0.00 USD |
| `7D` | `2470.80` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 0.00 USD | 3,960,000.00 USD | 2,290,000.00 USD | 522,210.00 USD |
| `1D` | `2471.00` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 391,890.00 USD |
| `7D` | `2474.10` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 0.00 USD | 5,230,000.00 USD | 2,920,000.00 USD | 2,400,000.00 USD |
| `1D` | `2476.80` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 943,590.00 USD | 40,210.00 USD |
| `7D` | `2477.40` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 0.00 USD | 1,660,000.00 USD | 4,420,000.00 USD | 718,840.00 USD |
| `1D` | `2479.70` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 26,700.00 USD | 0.00 USD |
| `7D` | `2480.70` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 0.00 USD | 2,110,000.00 USD | 4,170,000.00 USD | 540,990.00 USD |
| `1D` | `2482.60` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 677,540.00 USD | 136,500.00 USD | 451,780.00 USD |
| `7D` | `2484.00` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 0.00 USD | 1,210,000.00 USD | 1,390,000.00 USD | 1,430,000.00 USD |
| `1D` | `2485.50` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 941,100.00 USD | 1,330,000.00 USD | 0.00 USD |
| `7D` | `2487.30` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 0.00 USD | 325,140.00 USD | 262,280.00 USD | 0.00 USD |
| `1D` | `2488.40` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 866,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2490.60` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 0.00 USD | 2,910,000.00 USD | 2,540,000.00 USD | 279,750.00 USD |
| `1D` | `2491.30` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 138,370.00 USD | 0.00 USD | 13,360.00 USD |
| `7D` | `2493.90` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 0.00 USD | 1,660,000.00 USD | 1,760,000.00 USD | 3,940,000.00 USD |
| `1D` | `2494.20` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 178,560.00 USD | 14,300.00 USD |
| `7D` | `2497.20` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 0.00 USD | 2,860,000.00 USD | 5,240,000.00 USD | 8,250,000.00 USD |
| `7D` | `2500.50` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 0.00 USD | 1,110,000.00 USD | 2,280,000.00 USD | 1,130,000.00 USD |
| `7D` | `2503.80` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 0.00 USD | 63,860.00 USD | 1,480,000.00 USD | 125,600.00 USD |
| `1D` | `2505.80` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 338,980.00 USD | 717,780.00 USD |
| `7D` | `2507.10` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 0.00 USD | 4,340,000.00 USD | 3,090,000.00 USD | 3,180,000.00 USD |
| `7D` | `2510.40` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 0.00 USD | 2,290,000.00 USD | 1,270,000.00 USD | 0.00 USD |
| `1D` | `2511.60` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 242,080.00 USD | 88,880.00 USD | 28,160.00 USD |
| `7D` | `2513.70` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 0.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2517.00` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 0.00 USD | 97,050.00 USD | 189,640.00 USD | 815,620.00 USD |
| `1D` | `2517.40` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `1D` | `2520.30` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 80,610.00 USD | 121,470.00 USD | 52,590.00 USD |
| `7D` | `2520.30` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD |
| `1D` | `2523.20` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 563,140.00 USD | 537,030.00 USD | 568,070.00 USD |
| `7D` | `2523.60` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 0.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD |
| `1D` | `2526.10` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 808,950.00 USD | 362,000.00 USD | 53,680.00 USD |
| `7D` | `2526.90` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 0.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD |
| `1D` | `2529.00` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 641,110.00 USD | 965,400.00 USD | 464,460.00 USD |
| `7D` | `2530.20` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 0.00 USD | 2,800,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD |
| `1D` | `2531.90` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 474,040.00 USD | 534,600.00 USD | 7,120.00 USD |
| `7D` | `2533.50` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 0.00 USD | 3,530,000.00 USD | 1,850,000.00 USD | 2,030,000.00 USD |
| `1D` | `2534.80` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 405,580.00 USD | 62,630.00 USD | 919,610.00 USD |
| `7D` | `2536.80` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 0.00 USD | 3,720,000.00 USD | 3,450,000.00 USD | 3,530,000.00 USD |
| `1D` | `2537.70` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 2,580,000.00 USD | 926,330.00 USD | 1,620,000.00 USD |
| `7D` | `2540.10` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 0.00 USD | 4,150,000.00 USD | 3,220,000.00 USD | 1,580,000.00 USD |
| `1D` | `2540.60` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 1,180,000.00 USD | 1,100,000.00 USD | 808,470.00 USD |
| `7D` | `2543.40` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 0.00 USD | 4,150,000.00 USD | 2,520,000.00 USD | 2,480,000.00 USD |
| `1D` | `2543.50` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 1,510,000.00 USD | 1,100,000.00 USD | 233,890.00 USD |
| `1D` | `2546.40` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 1,780,000.00 USD | 1,410,000.00 USD | 571,260.00 USD |
| `7D` | `2546.70` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 0.00 USD | 1,450,000.00 USD | 1,090,000.00 USD | 2,290,000.00 USD |
| `1D` | `2549.30` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 1,020,000.00 USD | 803,170.00 USD | 1,470,000.00 USD |
| `7D` | `2550.00` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 0.00 USD | 4,320,000.00 USD | 3,550,000.00 USD | 3,720,000.00 USD |
| `1D` | `2552.20` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 1,730,000.00 USD | 914,630.00 USD | 396,670.00 USD |
| `7D` | `2553.30` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 0.00 USD | 2,820,000.00 USD | 788,360.00 USD | 2,600,000.00 USD |
| `1D` | `2555.10` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 996,760.00 USD | 221,720.00 USD | 417,580.00 USD |
| `7D` | `2556.60` | 2,730,000,000.00 USD | 2,730,000,000.00 USD | 0.00 USD | 2,760,000.00 USD | 283,560.00 USD | 6,500,000.00 USD |
| `1D` | `2558.00` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 736,590.00 USD | 502,170.00 USD | 811,030.00 USD |
| `7D` | `2559.90` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 0.00 USD | 5,720,000.00 USD | 2,130,000.00 USD | 1,390,000.00 USD |
| `1D` | `2560.50` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 1,830,000.00 USD | 1,080,000.00 USD | 1,160,000.00 USD |
| `7D` | `2563.20` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 0.00 USD | 1,430,000.00 USD | 2,900,000.00 USD | 1,290,000.00 USD |
| `7D` | `2566.50` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 0.00 USD | 1,860,000.00 USD | 1,830,000.00 USD | 3,300,000.00 USD |
| `7D` | `2569.80` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 0.00 USD | 125,250.00 USD | 341,900.00 USD | 1,190,000.00 USD |
| `7D` | `2573.10` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,790,000.00 USD |
| `7D` | `2576.40` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 0.00 USD | 2,400,000.00 USD | 930,280.00 USD | 1,640,000.00 USD |
| `7D` | `2579.70` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 2,750,000.00 USD | 1,780,000.00 USD | 1,960,000.00 USD |
| `7D` | `2583.00` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 1,730,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD |
| `7D` | `2586.30` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 0.00 USD | 1,480,000.00 USD | 2,030,000.00 USD | 2,570,000.00 USD |
| `7D` | `2589.60` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 0.00 USD | 3,310,000.00 USD | 631,590.00 USD | 2,150,000.00 USD |
| `7D` | `2592.90` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 0.00 USD | 2,370,000.00 USD | 1,280,000.00 USD | 1,580,000.00 USD |
| `7D` | `2596.20` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 0.00 USD | 794,750.00 USD | 620,840.00 USD | 1,490,000.00 USD |
| `7D` | `2599.50` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,530,000.00 USD | 2,810,000.00 USD |
| `7D` | `2602.80` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 0.00 USD | 1,680,000.00 USD | 1,260,000.00 USD | 1,690,000.00 USD |
| `7D` | `2606.10` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 0.00 USD | 1,850,000.00 USD | 1,560,000.00 USD | 772,800.00 USD |
| `7D` | `2609.40` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 0.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD |
| `7D` | `2612.70` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 0.00 USD | 1,010,000.00 USD | 643,740.00 USD | 43,560.00 USD |
| `7D` | `2616.00` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD |
| `7D` | `2619.30` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 449,020.00 USD | 323,810.00 USD | 268,500.00 USD |
| `7D` | `2622.60` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 631,440.00 USD | 1,220,000.00 USD | 0.00 USD |
| `7D` | `2625.90` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 485,890.00 USD | 474,490.00 USD | 0.00 USD |
| `7D` | `2629.20` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 0.00 USD | 20,460.00 USD | 31,040.00 USD |
| `7D` | `2632.40` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 0.00 USD | 301,060.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `29.11B` | Total OI Tokens: `12,887,156.6 ETH`
  * 1h OI Change: `+0.16%` | 4h OI Change: `-2.73%` | 24h OI Change: `-2.57%`
  * Exchange Breakdown: Binance=`8.48B` | Bybit=`2.10B` | OKX=`1.75B` | Hyperliquid=`2.50B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `28.87K` | Last 24h: `2.27M` | Last 3d: `7.66M` | Last 7d: `13.85M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0002%` | **USDT OKX** | `0.0038%` |
| **USDT Bybit** | `-0.0038%` | **USDT KuCoin** | `-0.0026%` |
| **USDT MEXC** | `0.0001%` | **USDT BingX** | `0.0040%` |
| **USDT Gate** | `0.0020%` | **USDT Bitget** | `0.0031%` |
| **CoinM Binance** | `0.0060%` | **CoinM OKX** | `-0.0012%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `50.17%` | `49.83%` | `1.01` | 2,310,000,000.00 USD |
| `15M` | `Binance` | `50.31%` | `49.69%` | `1.01` | 728,930,000.00 USD |
| `15M` | `OKX` | `54.72%` | `45.28%` | `1.21` | 339,760,000.00 USD |
| `15M` | `Bybit` | `57.05%` | `42.95%` | `1.33` | 268,810,000.00 USD |
| `15M` | `KuCoin` | `36.18%` | `63.82%` | `0.57` | 6,250,000.00 USD |
| `15M` | `Gate` | `50.87%` | `49.13%` | `1.04` | 250,010,000.00 USD |
| `15M` | `Bitget` | `58.75%` | `41.25%` | `1.42` | 125,740,000.00 USD |
| `15M` | `BingX` | `47.88%` | `52.12%` | `0.92` | 20,240,000.00 USD |
| `15M` | `MEXC` | `50.05%` | `49.95%` | `1.00` | 87,630,000.00 USD |
| `15M` | `Bitunix` | `53.43%` | `46.57%` | `1.15` | 97,510,000.00 USD |
| `15M` | `Hyperliquid` | `31.67%` | `68.33%` | `0.46` | 195,220,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `62.56%` | `37.44%` | `1.67` | 6,780,000.00 USD |
| `15M` | `Crypto.com` | `53.4%` | `46.6%` | `1.15` | 11,890,000.00 USD |
| `15M` | `WhiteBIT` | `22.51%` | `77.49%` | `0.29` | 43,990,000.00 USD |
| `15M` | `HTX` | `45.35%` | `54.65%` | `0.83` | 6,080,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `47.85%` | `52.15%` | `0.92` | 65,330,000.00 USD |
| `15M` | `Bitfinex` | `25.44%` | `74.56%` | `0.34` | 1,330,000.00 USD |
| `15M` | `Kraken` | `43.59%` | `56.41%` | `0.77` | 18,670,000.00 USD |
| `15M` | `Aster` | `48.23%` | `51.77%` | `0.93` | 12,590,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `54.94%` | `45.06%` | `1.22` | 28,140,000.00 USD |
| `15M` | `Whale Positions` | `50.31%` | `49.69%` | `1.01` | 728,930,000.00 USD |
| `15M` | `Global Accounts` | `50.17%` | `49.83%` | `1.01` | 2,310,000,000.00 USD |
| `1H` | `ETH` | `48.74%` | `51.26%` | `0.95` | 4,950,000,000.00 USD |
| `1H` | `Binance` | `47.44%` | `52.56%` | `0.90` | 1,500,000,000.00 USD |
| `1H` | `OKX` | `49.41%` | `50.59%` | `0.98` | 835,070,000.00 USD |
| `1H` | `Bybit` | `47.28%` | `52.72%` | `0.90` | 374,480,000.00 USD |
| `1H` | `KuCoin` | `56.35%` | `43.65%` | `1.29` | 31,270,000.00 USD |
| `1H` | `Gate` | `50.05%` | `49.95%` | `1.00` | 730,110,000.00 USD |
| `1H` | `Bitget` | `51.87%` | `48.13%` | `1.08` | 204,720,000.00 USD |
| `1H` | `BingX` | `51.38%` | `48.62%` | `1.06` | 46,940,000.00 USD |
| `1H` | `MEXC` | `49.47%` | `50.53%` | `0.98` | 218,510,000.00 USD |
| `1H` | `Bitunix` | `50.94%` | `49.06%` | `1.04` | 162,300,000.00 USD |
| `1H` | `Hyperliquid` | `39.73%` | `60.27%` | `0.66` | 399,130,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `46.93%` | `53.07%` | `0.88` | 11,010,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `77.9%` | `22.1%` | `3.52` | 175,140,000.00 USD |
| `1H` | `HTX` | `21.73%` | `78.27%` | `0.28` | 83,300,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `56.88%` | `43.12%` | `1.32` | 42,230,000.00 USD |
| `1H` | `Bitfinex` | `25.27%` | `74.73%` | `0.34` | 940,750.00 USD |
| `1H` | `Kraken` | `47.86%` | `52.14%` | `0.92` | 21,900,000.00 USD |
| `1H` | `Aster` | `45.9%` | `54.1%` | `0.85` | 35,770,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `49.28%` | `50.72%` | `0.97` | 75,850,000.00 USD |
| `1H` | `Whale Positions` | `47.44%` | `52.56%` | `0.90` | 1,500,000,000.00 USD |
| `1H` | `Global Accounts` | `48.74%` | `51.26%` | `0.95` | 4,950,000,000.00 USD |
| `4H` | `ETH` | `47.47%` | `52.53%` | `0.90` | 29,870,000,000.00 USD |
| `4H` | `Binance` | `45.84%` | `54.16%` | `0.85` | 8,370,000,000.00 USD |
| `4H` | `OKX` | `46.83%` | `53.17%` | `0.88` | 3,680,000,000.00 USD |
| `4H` | `Bybit` | `45.79%` | `54.21%` | `0.84` | 3,640,000,000.00 USD |
| `4H` | `KuCoin` | `49.18%` | `50.82%` | `0.97` | 127,660,000.00 USD |
| `4H` | `Gate` | `51.22%` | `48.78%` | `1.05` | 2,420,000,000.00 USD |
| `4H` | `Bitget` | `52.59%` | `47.41%` | `1.11` | 1,320,000,000.00 USD |
| `4H` | `BingX` | `51.22%` | `48.78%` | `1.05` | 381,500,000.00 USD |
| `4H` | `MEXC` | `48.6%` | `51.4%` | `0.95` | 1,310,000,000.00 USD |
| `4H` | `Bitunix` | `50.3%` | `49.7%` | `1.01` | 1,290,000,000.00 USD |
| `4H` | `Hyperliquid` | `43.43%` | `56.57%` | `0.77` | 1,980,000,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `53.19%` | `46.81%` | `1.14` | 136,160,000.00 USD |
| `4H` | `Crypto.com` | `51%` | `49%` | `1.04` | 141,780,000.00 USD |
| `4H` | `WhiteBIT` | `49.55%` | `50.45%` | `0.98` | 3,530,000,000.00 USD |
| `4H` | `HTX` | `44.87%` | `55.13%` | `0.81` | 96,040,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `49.41%` | `50.59%` | `0.98` | 568,790,000.00 USD |
| `4H` | `Bitfinex` | `19.95%` | `80.05%` | `0.25` | 35,200,000.00 USD |
| `4H` | `Kraken` | `44.42%` | `55.58%` | `0.80` | 270,200,000.00 USD |
| `4H` | `Aster` | `45.22%` | `54.78%` | `0.83` | 240,170,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.31%` | `51.69%` | `0.93` | 342,020,000.00 USD |
| `4H` | `Whale Positions` | `45.84%` | `54.16%` | `0.85` | 8,370,000,000.00 USD |
| `4H` | `Global Accounts` | `47.47%` | `52.53%` | `0.90` | 29,870,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `2309.25` | `2313.87` | `2309.25` | `2335.75` | `2302.25` | 493,849,561.51 USD | 204,343,201.57 USD | 289,506,359.94 USD | -85,163,158.37 USD | `-17.24%` | `0B / 20S` |
| `5:00 UTC` | `2315.25` | `2315.75` | `2315.25` | `2318.75` | `2312.25` | 88,922,002.19 USD | 46,836,385.14 USD | 42,085,617.06 USD | 4,750,768.08 USD | `+5.34%` | `3B / 0S` |
| `0:00 UTC` | `2300.25` | `2278.61` | `2300.25` | `2319.25` | `2238.25` | 1,664,912,417.71 USD | 683,261,559.43 USD | 981,650,858.29 USD | -298,389,298.86 USD | `-17.92%` | `1B / 31S` |
| `5:00 UTC` | `2259.25` | `2255.66` | `2259.25` | `2277.25` | `2230.25` | 846,756,637.45 USD | 383,814,230.15 USD | 462,942,407.30 USD | -79,128,177.15 USD | `-9.34%` | `0B / 6S` |
| `0:00 UTC` | `2260.25` | `2257.68` | `2260.25` | `2273.25` | `2245.25` | 606,671,993.02 USD | 300,593,954.86 USD | 306,078,038.17 USD | -5,484,083.31 USD | `-0.90%` | `5B / 2S` |
| `5:00 UTC` | `2281.25` | `2281.90` | `2281.25` | `2293.75` | `2267.75` | 508,254,989.09 USD | 245,674,110.48 USD | 262,580,878.61 USD | -16,906,768.14 USD | `-3.33%` | `3B / 0S` |
| `0:00 UTC` | `2287.25` | `2284.17` | `2287.25` | `2293.25` | `2271.25` | 175,571,332.73 USD | 84,909,600.78 USD | 90,661,731.96 USD | -5,752,131.18 USD | `-3.28%` | `0B / 2S` |
| `5:00 UTC` | `2272.25` | `2272.48` | `2272.25` | `2279.25` | `2266.25` | 164,039,523.36 USD | 80,192,631.79 USD | 83,846,891.57 USD | -3,654,259.77 USD | `-2.23%` | `1B / 3S` |
| `0:00 UTC` | `2258.75` | `2262.31` | `2258.75` | `2272.75` | `2251.25` | 318,288,167.50 USD | 151,770,310.17 USD | 166,517,857.34 USD | -14,747,547.17 USD | `-4.63%` | `1B / 1S` |
| `5:00 UTC` | `2265.25` | `2264.80` | `2265.25` | `2270.75` | `2256.75` | 69,120,880.09 USD | 32,158,226.13 USD | 36,962,653.96 USD | -4,804,427.83 USD | `-6.95%` | `1B / 0S` |

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
| `5m` | 3,460,000.00 USD | 41,320,000.00 USD | **`ACCUMULATION`** |
| `15m` | 377,300.00 USD | -1,600,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -4,230,000.00 USD | -20,520,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -12,100.00 USD | -71,360,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -75,770,000.00 USD | -941,270,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -87,170,000.00 USD | -1,250,000,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -109,100,000.00 USD | -1,570,000,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -64,430,000.00 USD | -1,220,000,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -72,010,000.00 USD | -1,270,000,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -116,800,000.00 USD | -1,700,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -107,590,000.00 USD | -2,290,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,100,000,000.00 USD | -9,290,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+3.46M` | 15m=`+377.30K` | 1h=`-12.10K` | 24h=`-116.80M`
* Futures Capital Netflows: 5m=`+41.32M` | 15m=`-1.60M` | 1h=`-71.36M` | 24h=`-1.70B`
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
  * `2026-10-30 03:30:02 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:54:02 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:51:02 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:50:02 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:50:02 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:52:02 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:52:02 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:02 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:02 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:02 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:02 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:02 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:52:02 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:52:02 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:52:02 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `2251.78` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2223.39` (Risk Distance: `28.39` pts)
  * +2.5R Take Profit: `2322.76`
  * Mathematical Lot Sizing: **`0.35 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2275.20` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2303.59` (Risk Distance: `28.39` pts)
  * +2.5R Take Profit: `2204.22`
  * Mathematical Lot Sizing: **`0.35 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2292.09`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
