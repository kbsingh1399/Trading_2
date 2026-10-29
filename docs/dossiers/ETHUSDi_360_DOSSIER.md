# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 03:46:30 IST` (`2026-10-29 22:16:30 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2257.70` | **Live Ask Quote**: `2261.80` | **Mid Price**: `2259.75`
- **Spread Points**: `410.00` | **Spread BPS**: `18.14 bps` (Charter Threshold: `25.00 bps`)
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
  * Value Area High (VAH) = `2275.20` (Distance: `-0.66%`)
  * Point of Control (POC) = `2264.08` (Distance: `-0.18%`)
  * Value Area Low (VAL) = `2249.44` (Distance: `+0.47%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2339.52` | POC=`2321.58` | VAL=`2296.66`
  * Prior Day Extremes: PDH=`2374.90` | PDL=`2225.40` | PDC=`2252.70`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2342.87` | Weekly POC=`2310.39` | Weekly VAL=`2299.56`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2289.10` | Low=`2245.20`
  * London Session (08:00-16:00 UTC): High=`2268.79` | Low=`2250.71`
  * New York Session (13:00-21:00 UTC): High=`2273.31` | Low=`2246.19`
  * Initial Balance (First Hour): IB High=`2266.53` | IB Low=`2252.97`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2250.71` - `2268.79`
  * Optimal Trade Entry (OTE 0.705): `2264.27`
  * Structural Invalidation Anchor (0.786): `2277.83`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2258.40` | `2263.82` | `2251.12` | `2258.83` | `53,307` | 120,340,900.00 USD | -9,672,461.12 USD | `-8.04%` | -890,344,604.49 USD | `+0.26` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `2258.83` | `2272.20` | `2257.00` | `2265.46` | `36,173` | 81,979,385.73 USD | 10,270,837.76 USD | `+12.53%` | -880,073,766.72 USD | `+0.60` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `2265.46` | `2265.47` | `2262.65` | `2263.66` | `1,583` | 3,583,924.68 USD | -631,080.84 USD | `-17.61%` | -880,704,847.56 USD | `+0.35` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `2271.65` | `2279.09` | `2266.41` | `2272.46` | `72,186` | 164,039,523.36 USD | -3,654,259.77 USD | `-2.23%` | -864,470,970.34 USD | `+0.38` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `2272.47` | `2272.73` | `2251.12` | `2265.46` | `140,694` | 318,288,024.78 USD | -14,747,404.45 USD | `-4.63%` | -879,218,374.79 USD | `+0.21` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `2265.46` | `2265.47` | `2262.65` | `2263.67` | `1,578` | 3,572,493.19 USD | -622,379.33 USD | `-17.42%` | -879,840,754.12 USD | `+0.42` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `2335.68` | `2335.92` | `2230.20` | `2256.63` | `1,357,980` | 3,094,453,113.46 USD | -457,917,547.62 USD | `-14.80%` | -830,712,434.27 USD | `-3.95` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2256.63` | `2293.87` | `2245.02` | `2272.46` | `640,507` | 1,454,537,838.20 USD | -31,797,242.40 USD | `-2.19%` | -862,509,676.67 USD | `+0.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `2272.47` | `2272.73` | `2251.12` | `2263.67` | `142,272` | 321,860,517.97 USD | -15,369,783.78 USD | `-4.78%` | -877,879,460.45 USD | `+0.18` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -163,611,405.07 USD | `+1.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -365,767,522.01 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2263.66` | `2,140,764` | 4,870,862,901.12 USD | -505,093,275.30 USD | `-10.37%` | -870,860,797.31 USD | `-1.89` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2308.03` | `2334.83` | `2303.75` | `2309.10` | `525,175` | 1,216,920,375.04 USD | -34,916,746.14 USD | `-2.87%` | -218,489,329.59 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2309.10` | `2330.05` | `2308.88` | `2324.26` | `409,016` | 949,400,649.22 USD | -49,162,247.72 USD | `-5.18%` | -267,651,577.31 USD | `+0.60` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -163,611,405.07 USD | `+1.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -365,767,522.01 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2263.66` | `2,140,764` | 4,870,862,901.12 USD | -505,093,275.30 USD | `-10.37%` | -870,860,797.31 USD | `-1.89` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`2259.75`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

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
| `1` | `0x5b5d...c060` | `SHORT` | 242,164,143.61 USD | `106,417.71` | `2322.74` | `2253.72` | `3943.44` | 5,016,868.55 USD | `+2.07%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 147,174,283.20 USD | `64,680.62` | `2375.30` | `2253.72` | `4604.56` | 6,462,014.29 USD | `+4.39%` | `5X Cross` |
| `6` | `0x77dd...e0e9` | `LONG` | 109,511,897.87 USD | `48,499.51` | `2610.31` | `2253.72` | `2171.15` | -17,086,986.00 USD | `-15.60%` | `10X Cross` |
| `8` | `0x0392...d7d9` | `LONG` | 101,395,928.05 USD | `44,734.81` | `2518.71` | `2253.72` | `2180.21` | -11,278,378.52 USD | `-11.12%` | `9X Cross` |
| `14` | `0xde8d...9524` | `LONG` | 68,853,100.84 USD | `30,282.40` | `2134.45` | `2253.72` | `1787.13` | 4,216,770.26 USD | `+6.12%` | `20X Cross` |
| `23` | `0xdf95...7d72` | `SHORT` | 50,998,148.59 USD | `22,629.64` | `2402.53` | `2253.72` | `4067.22` | 3,370,335.09 USD | `+6.61%` | `25X Cross` |
| `24` | `0x8add...7d2c` | `SHORT` | 44,960,296.64 USD | `19,836.01` | `2272.36` | `2253.72` | `2361.26` | 114,282.64 USD | `+0.25%` | `25X Cross` |
| `27` | `0x7fda...17d1` | `SHORT` | 43,124,574.10 USD | `19,135.86` | `2433.53` | `2253.72` | `4501.43` | 3,443,174.55 USD | `+7.98%` | `25X Cross` |
| `33` | `0xeced...6210` | `SHORT` | 37,832,404.23 USD | `16,687.58` | `2522.09` | `2253.72` | `3478.35` | 4,255,310.77 USD | `+11.25%` | `20X Cross` |
| `34` | `0xb695...a92d` | `SHORT` | 37,719,030.83 USD | `16,704.62` | `2557.74` | `2253.72` | `3936.39` | 5,007,134.22 USD | `+13.27%` | `20X Cross` |
| `35` | `0x6046...b21d` | `LONG` | 36,197,040.35 USD | `15,927.59` | `2410.19` | `2253.72` | `1694.42` | -2,191,579.30 USD | `-6.05%` | `6X Cross` |
| `40` | `0x45d2...4029` | `SHORT` | 31,508,865.00 USD | `13,950.00` | `2443.60` | `2253.72` | `5309.64` | 2,579,417.46 USD | `+8.19%` | `20X Cross` |
| `44` | `0x2371...0883` | `LONG` | 27,304,800.00 USD | `12,000.00` | `2421.77` | `2253.72` | `1280.11` | -1,756,494.85 USD | `-6.43%` | `20X Cross` |
| `45` | `0xbd1c...ff0e` | `LONG` | 27,094,800.00 USD | `12,000.00` | `2419.91` | `2253.72` | `1520.98` | -1,944,232.39 USD | `-7.18%` | `20X Cross` |
| `55` | `0xa9de...e049` | `LONG` | 25,031,600.00 USD | `11,000.00` | `2481.81` | `2253.72` | `1644.75` | -2,268,379.46 USD | `-9.06%` | `20X Cross` |
| `57` | `0x09dc...c094` | `LONG` | 24,895,310.00 USD | `11,000.00` | `2465.31` | `2253.72` | `1638.04` | -2,223,113.04 USD | `-8.93%` | `20X Cross` |
| `58` | `0x0c5d...36b3` | `LONG` | 24,836,900.00 USD | `11,000.00` | `2482.20` | `2253.72` | `1645.05` | -2,467,353.24 USD | `-9.93%` | `20X Cross` |
| `59` | `0x6c93...59a4` | `LONG` | 24,834,700.00 USD | `11,000.00` | `2441.15` | `2253.72` | `1603.01` | -2,017,972.73 USD | `-8.13%` | `20X Cross` |
| `61` | `0xa61c...66b9` | `LONG` | 24,715,542.24 USD | `10,888.00` | `2398.32` | `2253.72` | `1499.10` | -1,397,415.15 USD | `-5.65%` | `10X Cross` |
| `62` | `0x0622...8088` | `LONG` | 24,434,995.89 USD | `10,822.96` | `2274.55` | `2253.72` | `1353.17` | -182,400.83 USD | `-0.75%` | `5X Cross` |
| `72` | `0xec7f...df39` | `LONG` | 22,632,100.00 USD | `10,000.00` | `2719.35` | `2253.72` | `1721.57` | -4,561,448.52 USD | `-20.15%` | `20X Cross` |
| `75` | `0x15a4...dfdb` | `LONG` | 22,579,000.00 USD | `10,000.00` | `1761.94` | `2253.72` | `221.82` | 4,959,518.97 USD | `+21.97%` | `20X Cross` |
| `76` | `0xa2ce...3126` | `LONG` | 22,571,024.89 USD | `10,016.88` | `2162.83` | `2253.72` | `1523.38` | 906,222.84 USD | `+4.01%` | `10X Cross` |
| `77` | `0x6646...6de5` | `LONG` | 22,533,000.00 USD | `10,000.00` | `1765.80` | `2253.72` | `1721.58` | 4,874,942.55 USD | `+21.63%` | `25X Cross` |
| `79` | `0xaeaa...2416` | `SHORT` | 22,071,380.00 USD | `9,700.00` | `2311.92` | `2253.72` | `2658.70` | 354,302.40 USD | `+1.61%` | `25X Cross` |
| `85` | `0xca49...53c8` | `SHORT` | 20,875,345.50 USD | `9,264.26` | `2549.47` | `2253.72` | `3856.45` | 2,743,679.24 USD | `+13.14%` | `25X Cross` |
| `87` | `0xba5d...a352` | `SHORT` | 20,526,600.21 USD | `9,054.12` | `2493.89` | `2253.72` | `2923.49` | 2,053,407.05 USD | `+10.00%` | `20X Cross` |
| `88` | `0xea00...a918` | `LONG` | 20,408,072.69 USD | `9,003.83` | `2003.01` | `2253.72` | `1372.54` | 2,373,293.83 USD | `+11.63%` | `5X Cross` |
| `99` | `0xb37f...66ca` | `SHORT` | 19,190,450.00 USD | `8,500.00` | `2308.30` | `2253.72` | `2709.01` | 430,104.19 USD | `+2.24%` | `25X Cross` |
| `113` | `0x9eec...daab` | `LONG` | 18,270,329.11 USD | `8,092.45` | `1658.44` | `2253.72` | `1926.80` | 4,849,464.58 USD | `+26.54%` | `15X Cross` |
| `115` | `0x218a...7da2` | `SHORT` | 18,202,955.02 USD | `7,997.78` | `2208.16` | `2253.72` | `2815.97` | -542,559.80 USD | `-2.98%` | `10X Cross` |
| `116` | `0x5f91...65aa` | `LONG` | 17,976,228.37 USD | `7,964.66` | `1626.99` | `2253.72` | `2040.68` | 5,017,785.30 USD | `+27.91%` | `16X Cross` |
| `119` | `0xcf53...ee11` | `SHORT` | 17,135,535.84 USD | `7,603.63` | `1862.69` | `2253.72` | `4018.36` | -2,972,271.89 USD | `-17.35%` | `7X Cross` |
| `124` | `0x939f...04d2` | `LONG` | 16,310,647.15 USD | `7,223.81` | `2500.18` | `2253.72` | `1628.62` | -1,750,243.03 USD | `-10.73%` | `25X Cross` |
| `126` | `0xec0b...b078` | `LONG` | 15,897,191.80 USD | `7,007.80` | `2065.97` | `2253.72` | `1038.06` | 1,419,262.22 USD | `+8.93%` | `25X Cross` |
| `132` | `0x4487...c92d` | `SHORT` | 15,451,772.21 USD | `6,857.40` | `2362.23` | `2253.72` | `2789.56` | 747,037.81 USD | `+4.83%` | `10X Cross` |
| `133` | `0x418a...8888` | `SHORT` | 15,175,587.10 USD | `6,724.38` | `2494.55` | `2253.72` | `3002.96` | 1,598,736.07 USD | `+10.53%` | `25X Cross` |
| `136` | `0x4ff9...38d3` | `LONG` | 14,815,170.77 USD | `6,564.10` | `2447.40` | `2253.72` | `1670.66` | -1,249,851.98 USD | `-8.44%` | `3X Isolated` |
| `137` | `0xf78c...c581` | `LONG` | 14,674,900.06 USD | `6,500.22` | `2521.53` | `2253.72` | `1914.14` | -1,715,640.89 USD | `-11.69%` | `20X Cross` |
| `142` | `0xefe4...194b` | `SHORT` | 14,370,604.51 USD | `6,367.13` | `2269.66` | `2253.72` | `4529.07` | 80,619.65 USD | `+0.56%` | `20X Cross` |
| `143` | `0x799f...5f4c` | `LONG` | 14,248,126.38 USD | `6,310.90` | `2390.33` | `2253.72` | `1813.41` | -837,038.24 USD | `-5.87%` | `20X Cross` |
| `147` | `0x08bf...7872` | `SHORT` | 14,073,193.58 USD | `6,224.05` | `2258.00` | `2253.72` | `2585.91` | -19,277.47 USD | `-0.14%` | `20X Cross` |
| `152` | `0xc179...e0c8` | `LONG` | 13,798,424.32 USD | `6,113.61` | `2322.20` | `2253.72` | `1182.76` | -398,626.17 USD | `-2.89%` | `10X Cross` |
| `153` | `0x0c4a...1b19` | `LONG` | 13,794,753.01 USD | `6,086.13` | `2373.06` | `2253.72` | `2135.30` | -647,997.56 USD | `-4.70%` | `25X Isolated` |
| `156` | `0xd9e7...4aff` | `LONG` | 13,547,400.00 USD | `6,000.00` | `2480.18` | `2253.72` | `1408.43` | -1,333,724.33 USD | `-9.84%` | `20X Cross` |
| `162` | `0xecb6...2b00` | `SHORT` | 12,953,848.07 USD | `5,748.07` | `2282.41` | `2253.72` | `7373.58` | 165,646.84 USD | `+1.28%` | `15X Cross` |
| `167` | `0x1ee7...edf5` | `LONG` | 12,512,500.00 USD | `5,500.00` | `2316.93` | `2253.72` | `2127.37` | -230,639.62 USD | `-1.84%` | `25X Cross` |
| `188` | `0x45ab...6cbc` | `LONG` | 11,106,611.69 USD | `4,920.96` | `2727.66` | `2253.72` | `1389.89` | -2,316,132.11 USD | `-20.85%` | `7X Cross` |
| `190` | `0x645b...87b8` | `SHORT` | 11,094,133.41 USD | `4,915.43` | `2421.64` | `2253.72` | `6639.69` | 809,305.60 USD | `+7.29%` | `10X Cross` |
| `191` | `0x64b7...9da9` | `LONG` | 11,051,251.92 USD | `4,856.84` | `2604.61` | `2253.72` | `1529.28` | -1,598,962.50 USD | `-14.47%` | `25X Cross` |
| `196` | `0xfb18...eb17` | `SHORT` | 10,920,699.96 USD | `4,845.89` | `2315.54` | `2253.72` | `2628.57` | 300,182.83 USD | `+2.75%` | `25X Cross` |
| `199` | `0x5559...d43b` | `SHORT` | 10,809,742.61 USD | `4,755.93` | `2262.69` | `2253.72` | `2810.07` | -48,536.74 USD | `-0.45%` | `25X Cross` |
| `203` | `0x12d2...f97f` | `LONG` | 10,688,848.00 USD | `4,708.79` | `2588.61` | `2253.72` | `1996.56` | -1,500,386.32 USD | `-14.04%` | `20X Cross` |
| `215` | `0xe091...6705` | `SHORT` | 10,226,700.45 USD | `4,500.00` | `2467.33` | `2253.72` | `2572.99` | 876,308.05 USD | `+8.57%` | `20X Cross` |
| `239` | `0x28bb...fca6` | `SHORT` | 9,555,740.04 USD | `4,209.61` | `1896.10` | `2253.72` | `3039.86` | -1,573,857.48 USD | `-16.47%` | `20X Cross` |
| `241` | `0x6ea4...0ea7` | `SHORT` | 9,483,440.44 USD | `4,184.01` | `2602.13` | `2253.72` | `3425.97` | 1,403,906.23 USD | `+14.80%` | `20X Cross` |
| `253` | `0x3dc9...54b0` | `SHORT` | 9,094,095.61 USD | `3,999.69` | `2480.32` | `2253.72` | `6410.07` | 826,440.94 USD | `+9.09%` | `20X Cross` |
| `257` | `0xfb94...0ddf` | `SHORT` | 9,032,742.63 USD | `4,002.10` | `2382.44` | `2253.72` | `5105.36` | 502,041.52 USD | `+5.56%` | `20X Cross` |
| `258` | `0x5e9e...35ee` | `SHORT` | 9,030,305.41 USD | `4,007.56` | `1796.39` | `2253.72` | `2586.46` | -1,831,155.32 USD | `-20.28%` | `20X Cross` |
| `260` | `0x8cc9...2b6a` | `SHORT` | 9,028,000.00 USD | `4,000.00` | `1791.18` | `2253.72` | `3857.05` | -1,863,253.33 USD | `-20.64%` | `25X Cross` |
| `270` | `0xf02d...5eb3` | `LONG` | 8,705,658.46 USD | `3,855.99` | `2513.67` | `2253.72` | `308.80` | -987,053.85 USD | `-11.34%` | `20X Cross` |
| `272` | `0x4b67...f4e7` | `LONG` | 8,683,245.30 USD | `3,820.84` | `2591.51` | `2253.72` | `1671.53` | -1,218,528.24 USD | `-14.03%` | `20X Cross` |
| `295` | `0x8ae4...3d60` | `LONG` | 8,064,976.68 USD | `3,558.20` | `2482.21` | `2253.72` | `480.71` | -767,221.35 USD | `-9.51%` | `10X Cross` |
| `317` | `0xfe7c...b7ae` | `SHORT` | 7,668,060.15 USD | `3,402.58` | `2440.17` | `2253.72` | `5179.18` | 634,849.12 USD | `+8.28%` | `25X Cross` |
| `335` | `0x9c2a...f6a8` | `SHORT` | 6,876,000.09 USD | `3,045.71` | `2543.83` | `2253.72` | `2602.91` | 871,786.46 USD | `+12.68%` | `20X Cross` |
| `341` | `0x007d...67a0` | `LONG` | 6,777,000.00 USD | `3,000.00` | `2400.00` | `2253.72` | `1472.46` | -423,000.00 USD | `-6.24%` | `25X Cross` |
| `342` | `0x4a20...3c26` | `LONG` | 6,774,000.00 USD | `3,000.00` | `2428.72` | `2253.72` | `560.96` | -512,160.28 USD | `-7.56%` | `20X Cross` |
| `384` | `0xf517...c032` | `SHORT` | 6,190,503.14 USD | `2,738.07` | `2053.90` | `2253.72` | `5350.86` | -566,761.23 USD | `-9.16%` | `25X Cross` |
| `387` | `0xd911...961e` | `LONG` | 6,126,611.87 USD | `2,714.25` | `2271.01` | `2253.72` | `1380.42` | -37,494.39 USD | `-0.61%` | `25X Cross` |
| `399` | `0x8328...f54a` | `SHORT` | 5,839,784.06 USD | `2,576.45` | `2292.01` | `2253.72` | `3280.20` | 65,487.22 USD | `+1.12%` | `25X Cross` |
| `400` | `0xb829...3a81` | `LONG` | 5,833,826.84 USD | `2,582.48` | `2492.52` | `2253.72` | `966.62` | -603,062.48 USD | `-10.34%` | `20X Cross` |
| `401` | `0xed48...7c9b` | `SHORT` | 5,759,687.33 USD | `2,551.13` | `2460.02` | `2253.72` | `3237.54` | 516,159.08 USD | `+8.96%` | `20X Cross` |
| `404` | `0xb8eb...1dd5` | `LONG` | 5,598,414.13 USD | `2,476.19` | `2271.46` | `2253.72` | `1427.89` | -26,172.18 USD | `-0.47%` | `25X Cross` |
| `414` | `0xfbe2...c8ea` | `SHORT` | 5,427,684.19 USD | `2,404.08` | `2041.57` | `2253.72` | `2608.36` | -519,591.46 USD | `-9.57%` | `20X Cross` |
| `422` | `0x1c98...7fc7` | `LONG` | 5,344,629.42 USD | `2,358.00` | `2467.15` | `2253.72` | `1897.18` | -472,942.06 USD | `-8.85%` | `10X Cross` |
| `426` | `0x77ee...2902` | `SHORT` | 5,192,057.77 USD | `2,290.69` | `2476.53` | `2253.72` | `5826.45` | 480,914.47 USD | `+9.26%` | `25X Cross` |
| `434` | `0x023a...2355` | `LONG` | 5,067,396.21 USD | `2,232.35` | `2330.15` | `2253.72` | `0.000000` | -134,332.52 USD | `-2.65%` | `25X Cross` |
| `439` | `0x6859...7e1e` | `SHORT` | 5,021,319.72 USD | `2,224.58` | `2200.39` | `2253.72` | `3536.92` | -126,366.99 USD | `-2.52%` | `25X Cross` |
| `450` | `0xd507...c948` | `SHORT` | 4,902,638.17 USD | `2,172.00` | `2387.49` | `2253.72` | `2707.39` | 283,002.85 USD | `+5.77%` | `5X Isolated` |
| `459` | `0x382b...3e39` | `SHORT` | 4,799,134.95 USD | `2,129.54` | `2296.66` | `2253.72` | `4642.15` | 91,702.27 USD | `+1.91%` | `25X Cross` |
| `485` | `0xbb34...1696` | `LONG` | 4,547,400.00 USD | `2,000.00` | `2318.80` | `2253.72` | `1941.48` | -90,216.04 USD | `-1.98%` | `25X Cross` |
| `487` | `0xc619...10f5` | `LONG` | 4,545,200.00 USD | `2,000.00` | `2318.40` | `2253.72` | `1791.15` | -91,606.86 USD | `-2.02%` | `25X Cross` |
| `488` | `0x3440...32c5` | `SHORT` | 4,539,082.38 USD | `2,000.57` | `2198.21` | `2253.72` | `3633.59` | -141,419.25 USD | `-3.12%` | `25X Cross` |
| `491` | `0xf929...d1f9` | `SHORT` | 4,514,000.00 USD | `2,000.00` | `2423.37` | `2253.72` | `2548.79` | 332,740.34 USD | `+7.37%` | `25X Cross` |
| `492` | `0x7a6d...f79c` | `SHORT` | 4,514,000.00 USD | `2,000.00` | `2418.41` | `2253.72` | `2656.98` | 322,832.11 USD | `+7.15%` | `25X Cross` |
| `503` | `0x0514...bdfe` | `SHORT` | 4,393,935.00 USD | `1,950.00` | `1988.74` | `2253.72` | `3062.49` | -515,875.37 USD | `-11.74%` | `25X Cross` |
| `505` | `0x7b7f...dee2` | `LONG` | 4,379,059.25 USD | `1,942.79` | `2274.63` | `2253.72` | `1027.10` | -40,091.86 USD | `-0.92%` | `20X Cross` |
| `509` | `0x8376...9a1e` | `SHORT` | 4,341,793.21 USD | `1,910.50` | `2477.72` | `2253.72` | `3178.76` | 391,894.96 USD | `+9.03%` | `20X Cross` |
| `518` | `0xfc27...9d9d` | `SHORT` | 4,217,811.68 USD | `1,867.36` | `2341.25` | `2253.72` | `11670.73` | 154,162.07 USD | `+3.66%` | `25X Cross` |
| `543` | `0x739c...cfb2` | `SHORT` | 4,095,000.00 USD | `1,800.00` | `2427.60` | `2253.72` | `2529.49` | 274,696.38 USD | `+6.71%` | `25X Cross` |
| `544` | `0xb15b...dbae` | `SHORT` | 4,085,937.78 USD | `1,797.68` | `2294.54` | `2253.72` | `2302.42` | 38,906.19 USD | `+0.95%` | `25X Cross` |
| `545` | `0x7265...91a5` | `LONG` | 4,084,117.18 USD | `1,801.87` | `2533.96` | `2253.72` | `1988.11` | -481,749.28 USD | `-11.80%` | `20X Cross` |
| `546` | `0x541e...071d` | `SHORT` | 4,073,885.00 USD | `1,805.00` | `2648.19` | `2253.72` | `3164.15` | 706,099.84 USD | `+17.33%` | `25X Cross` |
| `551` | `0x91a9...3f70` | `SHORT` | 4,021,723.99 USD | `1,767.48` | `2156.23` | `2253.72` | `3650.45` | -210,619.91 USD | `-5.24%` | `4X Cross` |
| `553` | `0xa445...329d` | `LONG` | 4,011,899.92 USD | `1,776.75` | `2398.85` | `2253.72` | `1942.33` | -250,269.43 USD | `-6.24%` | `25X Cross` |
| `561` | `0x3453...b323` | `SHORT` | 3,982,405.11 USD | `1,750.12` | `2328.82` | `2253.72` | `2433.77` | 93,327.02 USD | `+2.34%` | `25X Cross` |
| `566` | `0x2828...93a0` | `LONG` | 3,970,706.59 USD | `1,758.58` | `2314.00` | `2253.72` | `2241.71` | -98,660.27 USD | `-2.48%` | `25X Cross` |
| `591` | `0xfeec...4e9c` | `SHORT` | 3,837,529.90 USD | `1,691.81` | `2566.49` | `2253.72` | `2654.28` | 504,494.61 USD | `+13.15%` | `10X Cross` |
| `595` | `0x39b4...5c34` | `SHORT` | 3,820,767.41 USD | `1,692.70` | `2329.97` | `2253.72` | `2511.93` | 123,183.57 USD | `+3.22%` | `25X Cross` |
| `599` | `0x936c...bb0f` | `SHORT` | 3,805,622.77 USD | `1,688.69` | `2434.60` | `2253.72` | `4539.95` | 305,664.34 USD | `+8.03%` | `20X Cross` |
| `614` | `0x2577...4897` | `LONG` | 3,718,505.13 USD | `1,650.03` | `2298.42` | `2253.72` | `294.47` | -73,963.85 USD | `-1.99%` | `15X Cross` |
| `618` | `0x982b...4606` | `LONG` | 3,701,009.36 USD | `1,626.82` | `2575.24` | `2253.72` | `1548.43` | -488,443.72 USD | `-13.20%` | `5X Isolated` |
| `619` | `0xeee0...0b53` | `LONG` | 3,694,988.64 USD | `1,637.12` | `2468.64` | `2253.72` | `221.68` | -346,487.42 USD | `-9.38%` | `7X Cross` |
| `622` | `0x27b8...12fc` | `LONG` | 3,685,738.28 USD | `1,628.12` | `2468.73` | `2253.72` | `576.49` | -333,656.35 USD | `-9.05%` | `10X Cross` |
| `637` | `0x73d7...8be1` | `LONG` | 3,615,948.95 USD | `1,601.47` | `2410.40` | `2253.72` | `2021.57` | -244,229.97 USD | `-6.75%` | `25X Cross` |
| `652` | `0xf910...0a2d` | `LONG` | 3,492,335.93 USD | `1,546.72` | `2272.70` | `2253.72` | `0.000000` | -22,895.60 USD | `-0.66%` | `5X Cross` |
| `657` | `0xe170...9300` | `SHORT` | 3,475,037.08 USD | `1,533.40` | `2076.39` | `2253.72` | `3147.71` | -291,087.59 USD | `-8.38%` | `25X Cross` |
| `658` | `0x4b86...df9d` | `SHORT` | 3,468,014.40 USD | `1,524.00` | `2287.40` | `2253.72` | `2491.45` | 17,983.20 USD | `+0.52%` | `9X Isolated` |
| `672` | `0x2e2b...2fab` | `LONG` | 3,427,926.04 USD | `1,507.38` | `2245.53` | `2253.72` | `1200.16` | 43,052.94 USD | `+1.26%` | `25X Cross` |
| `676` | `0x251f...6e5d` | `LONG` | 3,413,700.00 USD | `1,500.00` | `2346.68` | `2253.72` | `1841.56` | -106,330.49 USD | `-3.11%` | `20X Cross` |
| `677` | `0xad54...6203` | `LONG` | 3,408,724.08 USD | `1,510.29` | `2614.66` | `2253.72` | `2124.61` | -540,182.47 USD | `-15.85%` | `10X Isolated` |
| `680` | `0xbc76...417c` | `LONG` | 3,405,387.93 USD | `1,500.90` | `2261.84` | `2253.72` | `2103.28` | 10,590.78 USD | `+0.31%` | `25X Cross` |
| `698` | `0xb885...3c54` | `LONG` | 3,267,318.96 USD | `1,450.00` | `2274.34` | `2253.72` | `19.81` | -30,489.18 USD | `-0.93%` | `20X Cross` |
| `703` | `0xef70...a84c` | `SHORT` | 3,258,291.69 USD | `1,442.74` | `2424.73` | `2253.72` | `3276.07` | 239,979.13 USD | `+7.37%` | `25X Cross` |
| `705` | `0x4b5f...0dd8` | `LONG` | 3,246,532.46 USD | `1,431.96` | `2339.45` | `2253.72` | `2148.67` | -103,460.49 USD | `-3.19%` | `10X Cross` |
| `707` | `0xbadb...9ee6` | `LONG` | 3,245,636.42 USD | `1,428.16` | `1936.00` | `2253.72` | `1060.18` | 480,714.77 USD | `+14.81%` | `20X Cross` |
| `742` | `0xa0fb...96be` | `LONG` | 3,114,750.91 USD | `1,376.25` | `2293.96` | `2253.72` | `1549.91` | -42,323.98 USD | `-1.36%` | `3X Cross` |
| `768` | `0x0dd5...f6ee` | `LONG` | 2,993,597.50 USD | `1,315.00` | `2306.05` | `2253.72` | `1654.21` | -38,866.88 USD | `-1.30%` | `5X Cross` |
| `769` | `0x880a...311c` | `SHORT` | 2,992,404.48 USD | `1,320.22` | `2425.76` | `2253.72` | `8326.12` | 210,144.68 USD | `+7.02%` | `9X Cross` |
| `814` | `0xc435...c905` | `SHORT` | 2,817,859.20 USD | `1,248.00` | `2704.38` | `2253.72` | `4237.21` | 557,211.15 USD | `+19.77%` | `20X Cross` |
| `835` | `0x7178...0854` | `LONG` | 2,750,451.30 USD | `1,218.63` | `2461.81` | `2253.72` | `1165.18` | -249,595.11 USD | `-9.07%` | `10X Cross` |
| `844` | `0xaaa1...ab8c` | `SHORT` | 2,708,400.00 USD | `1,200.00` | `2276.29` | `2253.72` | `2366.18` | 23,157.58 USD | `+0.86%` | `25X Isolated` |
| `865` | `0x07fd...689d` | `LONG` | 2,628,811.33 USD | `1,166.49` | `2419.97` | `2253.72` | `0.000000` | -194,080.48 USD | `-7.38%` | `25X Cross` |
| `907` | `0xbef3...0d3e` | `LONG` | 2,508,934.49 USD | `1,103.99` | `2315.08` | `2253.72` | `2162.38` | -46,901.67 USD | `-1.87%` | `20X Cross` |
| `917` | `0x6a41...a3b9` | `LONG` | 2,481,346.41 USD | `1,099.06` | `2314.77` | `2253.72` | `2164.18` | -62,726.29 USD | `-2.53%` | `20X Cross` |
| `922` | `0x2f80...f203` | `SHORT` | 2,465,144.86 USD | `1,088.94` | `1984.00` | `2253.72` | `3062.73` | -304,677.67 USD | `-12.36%` | `20X Cross` |
| `925` | `0x6f11...0389` | `SHORT` | 2,455,156.60 USD | `1,079.00` | `2333.39` | `2253.72` | `3199.69` | 62,572.31 USD | `+2.55%` | `25X Cross` |
| `936` | `0x2b61...2f6c` | `SHORT` | 2,429,879.88 USD | `1,076.60` | `2681.75` | `2253.72` | `6567.64` | 457,292.86 USD | `+18.82%` | `10X Cross` |
| `981` | `0x1b2a...f7a6` | `LONG` | 2,314,255.58 USD | `1,025.37` | `2737.51` | `2253.72` | `883.05` | -492,704.36 USD | `-21.29%` | `10X Cross` |
| `990` | `0x02aa...1806` | `SHORT` | 2,284,606.58 USD | `1,007.10` | `2654.68` | `2253.72` | `3613.65` | 388,925.53 USD | `+17.02%` | `20X Cross` |
| `991` | `0x31de...13f2` | `LONG` | 2,282,892.30 USD | `1,011.47` | `2274.31` | `2253.72` | `0.000000` | -17,518.56 USD | `-0.77%` | `20X Cross` |
| `994` | `0x001a...fef6` | `SHORT` | 2,273,331.06 USD | `1,007.33` | `2022.19` | `2253.72` | `3077.03` | -236,323.10 USD | `-10.40%` | `10X Cross` |
| `995` | `0x7743...e4fe` | `SHORT` | 2,271,762.85 USD | `1,000.56` | `2298.56` | `2253.72` | `4974.40` | 28,082.22 USD | `+1.24%` | `25X Cross` |
| `998` | `0x834c...dd93` | `SHORT` | 2,266,600.00 USD | `1,000.00` | `2249.68` | `2253.72` | `2310.88` | -16,914.58 USD | `-0.75%` | `25X Cross` |
| `1001` | `0xdb3a...cf3b` | `LONG` | 2,265,660.98 USD | `1,003.22` | `2705.01` | `2253.72` | `0.000000` | -448,045.91 USD | `-19.78%` | `4X Cross` |
| `1004` | `0x5272...fcd9` | `SHORT` | 2,256,800.00 USD | `1,000.00` | `2241.82` | `2253.72` | `2831.71` | -14,975.51 USD | `-0.66%` | `5X Cross` |
| `1033` | `0xb002...ed8a` | `SHORT` | 2,173,003.49 USD | `962.78` | `2299.66` | `2253.72` | `4199.87` | 41,074.42 USD | `+1.89%` | `25X Cross` |
| `1075` | `0x9606...4e5d` | `SHORT` | 2,060,633.55 USD | `913.00` | `2478.70` | `2253.72` | `4313.84` | 202,420.05 USD | `+9.82%` | `20X Cross` |
| `1084` | `0x5238...54e5` | `SHORT` | 2,047,860.00 USD | `900.00` | `2289.53` | `2253.72` | `4704.85` | 12,722.42 USD | `+0.62%` | `25X Cross` |
| `1093` | `0x5f10...d49d` | `LONG` | 2,031,120.00 USD | `900.00` | `2249.83` | `2253.72` | `1816.17` | 6,266.53 USD | `+0.31%` | `25X Cross` |
| `1096` | `0x9599...c60a` | `LONG` | 2,021,461.62 USD | `894.25` | `2271.44` | `2253.72` | `0.000000` | -9,785.05 USD | `-0.48%` | `20X Cross` |
| `1121` | `0x2e30...4cb5` | `SHORT` | 1,994,104.95 USD | `884.85` | `2340.07` | `2253.72` | `7869.54` | 76,513.87 USD | `+3.84%` | `2X Cross` |
| `1191` | `0xcd27...52a8` | `LONG` | 1,898,620.98 USD | `837.21` | `2553.56` | `2253.72` | `1404.20` | -239,243.79 USD | `-12.60%` | `2X Cross` |
| `1222` | `0x6ff1...8575` | `LONG` | 1,852,465.61 USD | `814.06` | `2272.53` | `2253.72` | `2227.12` | 2,495.85 USD | `+0.13%` | `25X Isolated` |
| `1246` | `0x7737...bf66` | `SHORT` | 1,820,726.26 USD | `799.79` | `2494.83` | `2253.72` | `23913.51` | 174,619.77 USD | `+9.59%` | `15X Cross` |
| `1248` | `0x04a9...95aa` | `LONG` | 1,820,320.00 USD | `800.00` | `2595.13` | `2253.72` | `1886.40` | -255,786.74 USD | `-14.05%` | `5X Cross` |
| `1252` | `0x3fc5...c0c1` | `SHORT` | 1,815,693.31 USD | `804.26` | `2702.11` | `2253.72` | `4987.67` | 357,508.22 USD | `+19.69%` | `25X Cross` |
| `1272` | `0xf83f...625f` | `SHORT` | 1,784,079.47 USD | `790.22` | `2595.19` | `2253.72` | `6191.75` | 266,692.29 USD | `+14.95%` | `20X Cross` |
| `1288` | `0x458d...ab3b` | `LONG` | 1,760,690.03 USD | `774.75` | `2740.41` | `2253.72` | `1887.99` | -362,439.15 USD | `-20.59%` | `3X Isolated` |
| `1316` | `0x6e6f...82a6` | `LONG` | 1,704,084.63 USD | `756.03` | `2267.81` | `2253.72` | `893.77` | -10,447.39 USD | `-0.61%` | `20X Cross` |
| `1355` | `0xaa53...9cb7` | `LONG` | 1,648,223.86 USD | `730.34` | `2389.70` | `2253.72` | `1938.15` | -97,065.77 USD | `-5.89%` | `20X Cross` |
| `1366` | `0xa70a...4be9` | `LONG` | 1,640,207.31 USD | `726.49` | `2269.64` | `2253.72` | `234.68` | -8,675.97 USD | `-0.53%` | `20X Cross` |
| `1369` | `0xab81...c608` | `SHORT` | 1,638,980.18 USD | `727.27` | `2285.37` | `2253.72` | `5223.02` | 23,106.91 USD | `+1.41%` | `20X Cross` |
| `1372` | `0x51a0...3543` | `SHORT` | 1,636,314.23 USD | `724.55` | `2627.71` | `2253.72` | `7460.22` | 267,582.52 USD | `+16.35%` | `20X Cross` |
| `1378` | `0xa189...94d7` | `SHORT` | 1,626,216.57 USD | `719.98` | `2691.84` | `2253.72` | `3051.91` | 311,856.09 USD | `+19.18%` | `25X Cross` |
| `1393` | `0x2f93...4404` | `LONG` | 1,594,145.53 USD | `707.47` | `1700.45` | `2253.72` | `1369.59` | 391,119.16 USD | `+24.53%` | `4X Isolated` |
| `1397` | `0x0a97...347d` | `LONG` | 1,585,386.74 USD | `702.21` | `2270.79` | `2253.72` | `1170.96` | -9,196.91 USD | `-0.58%` | `20X Cross` |
| `1399` | `0x5605...fe0f` | `SHORT` | 1,584,738.11 USD | `702.14` | `2566.90` | `2253.72` | `3070.92` | 217,594.54 USD | `+13.73%` | `20X Cross` |
| `1411` | `0x0deb...0bc5` | `LONG` | 1,580,390.00 USD | `700.00` | `2071.05` | `2253.72` | `1598.18` | 130,654.21 USD | `+8.27%` | `20X Cross` |
| `1458` | `0xb1ec...e86a` | `SHORT` | 1,536,205.49 USD | `679.30` | `2271.56` | `2253.72` | `16593.62` | 6,857.75 USD | `+0.45%` | `25X Cross` |
| `1459` | `0xdbd1...29dd` | `SHORT` | 1,533,826.94 USD | `680.70` | `3030.57` | `2253.72` | `4094.16` | 529,094.18 USD | `+34.50%` | `6X Cross` |
| `1464` | `0x71e5...be04` | `LONG` | 1,529,358.43 USD | `677.67` | `2727.27` | `2253.72` | `1471.73` | -318,827.17 USD | `-20.85%` | `20X Cross` |
| `1471` | `0x0b23...f37b` | `LONG` | 1,523,475.00 USD | `675.00` | `2238.15` | `2253.72` | `597.07` | 12,718.36 USD | `+0.83%` | `5X Cross` |
| `1480` | `0x1f16...6d07` | `LONG` | 1,503,295.20 USD | `666.00` | `2287.38` | `2253.72` | `1348.64` | -20,104.09 USD | `-1.34%` | `7X Cross` |
| `1485` | `0x696d...8e28` | `SHORT` | 1,498,118.47 USD | `660.46` | `2270.91` | `2253.72` | `4492.28` | 1,727.71 USD | `+0.12%` | `20X Cross` |
| `1489` | `0x4b1c...bc38` | `SHORT` | 1,490,992.52 USD | `660.34` | `2528.62` | `2253.72` | `4534.31` | 178,769.23 USD | `+11.99%` | `10X Cross` |
| `1492` | `0xc8fe...afa4` | `LONG` | 1,487,881.54 USD | `655.46` | `2331.34` | `2253.72` | `2146.94` | -40,221.28 USD | `-2.70%` | `10X Isolated` |
| `1494` | `0x0cac...6170` | `SHORT` | 1,481,742.00 USD | `657.50` | `2146.55` | `2253.72` | `2840.15` | -70,379.80 USD | `-4.75%` | `20X Cross` |
| `1518` | `0x7c90...d129` | `LONG` | 1,454,370.83 USD | `639.17` | `2286.01` | `2253.72` | `1874.22` | -6,782.57 USD | `-0.47%` | `20X Cross` |
| `1527` | `0xf00e...fe3d` | `SHORT` | 1,451,430.18 USD | `642.88` | `2333.21` | `2253.72` | `2564.89` | 48,547.79 USD | `+3.34%` | `20X Cross` |
| `1530` | `0x621c...63ab` | `LONG` | 1,449,020.85 USD | `642.98` | `2281.90` | `2253.72` | `0.000000` | -18,202.55 USD | `-1.26%` | `20X Cross` |
| `1535` | `0xffb2...5ed6` | `SHORT` | 1,446,210.67 USD | `640.77` | `2672.96` | `2253.72` | `2490.84` | 266,537.68 USD | `+18.43%` | `20X Cross` |
| `1540` | `0xa522...2d0e` | `SHORT` | 1,442,374.01 USD | `636.36` | `2284.42` | `2253.72` | `4351.66` | 11,351.83 USD | `+0.79%` | `20X Cross` |
| `1554` | `0x34fb...93de` | `LONG` | 1,426,558.64 USD | `633.09` | `2274.81` | `2253.72` | `0.000000` | -13,606.97 USD | `-0.95%` | `20X Cross` |
| `1562` | `0xfce0...f4c0` | `SHORT` | 1,419,001.80 USD | `623.60` | `3129.61` | `2253.72` | `2788.43` | 532,624.79 USD | `+37.54%` | `20X Cross` |
| `1566` | `0x871f...972b` | `SHORT` | 1,417,053.21 USD | `626.77` | `2279.80` | `2253.72` | `2586.28` | 11,848.61 USD | `+0.84%` | `20X Cross` |
| `1596` | `0x7663...cb5a` | `SHORT` | 1,382,497.00 USD | `613.54` | `2342.35` | `2253.72` | `3781.72` | 54,623.49 USD | `+3.95%` | `3X Cross` |
| `1607` | `0x26e6...6b28` | `LONG` | 1,364,220.00 USD | `600.00` | `1769.78` | `2253.72` | `2005.49` | 302,348.47 USD | `+22.16%` | `20X Cross` |
| `1608` | `0xad02...eb65` | `LONG` | 1,363,708.16 USD | `600.62` | `2460.69` | `2253.72` | `1079.65` | -114,232.39 USD | `-8.38%` | `5X Cross` |
| `1611` | `0x67c3...609d` | `SHORT` | 1,359,954.00 USD | `600.00` | `2386.55` | `2253.72` | `2560.74` | 71,977.89 USD | `+5.29%` | `25X Cross` |
| `1618` | `0x638f...f5f0` | `LONG` | 1,352,160.00 USD | `600.00` | `4011.50` | `2253.72` | `354.41` | -1,054,743.53 USD | `-78.00%` | `25X Cross` |
| `1653` | `0xca8e...507d` | `LONG` | 1,309,872.00 USD | `580.00` | `2253.46` | `2253.72` | `2069.71` | 2,861.65 USD | `+0.22%` | `10X Isolated` |
| `1659` | `0xfc66...ca06` | `SHORT` | 1,303,827.97 USD | `577.45` | `2275.19` | `2253.72` | `52082.08` | 9,989.79 USD | `+0.77%` | `20X Cross` |
| `1670` | `0xaa7a...af37` | `LONG` | 1,289,255.97 USD | `571.05` | `2273.28` | `2253.72` | `0.000000` | -8,901.87 USD | `-0.69%` | `20X Cross` |
| `1673` | `0xfb99...37f3` | `LONG` | 1,285,416.06 USD | `565.34` | `2362.35` | `2253.72` | `1235.11` | -50,120.30 USD | `-3.90%` | `3X Cross` |
| `1691` | `0x844b...7f42` | `SHORT` | 1,266,177.00 USD | `561.00` | `2026.17` | `2253.72` | `3224.45` | -129,493.59 USD | `-10.23%` | `25X Cross` |
| `1695` | `0xabe6...1d99` | `SHORT` | 1,261,517.48 USD | `556.00` | `2484.68` | `2253.72` | `3096.52` | 119,978.41 USD | `+9.51%` | `20X Cross` |
| `1754` | `0xad21...fb6a` | `LONG` | 1,200,535.38 USD | `531.87` | `2574.89` | `2253.72` | `1707.30` | -168,970.12 USD | `-14.07%` | `7X Cross` |
| `1768` | `0x0082...1ae3` | `LONG` | 1,192,012.80 USD | `528.00` | `2448.58` | `2253.72` | `2234.21` | -100,842.11 USD | `-8.46%` | `25X Cross` |
| `1785` | `0xd4c1...3d1d` | `SHORT` | 1,179,550.24 USD | `523.41` | `2334.28` | `2253.72` | `12260.55` | 42,229.02 USD | `+3.58%` | `12X Cross` |
| `1814` | `0x0c7a...2f50` | `SHORT` | 1,149,264.79 USD | `509.25` | `2122.56` | `2253.72` | `4110.36` | -68,359.36 USD | `-5.95%` | `20X Cross` |
| `1818` | `0x0089...2410` | `SHORT` | 1,147,159.14 USD | `507.35` | `2308.88` | `2253.72` | `3352.11` | 24,241.12 USD | `+2.11%` | `20X Cross` |
| `1826` | `0x3947...f3b1` | `LONG` | 1,138,635.72 USD | `505.31` | `2274.94` | `2253.72` | `0.000000` | -10,928.18 USD | `-0.96%` | `20X Cross` |
| `1829` | `0xa559...ff95` | `LONG` | 1,136,300.00 USD | `500.00` | `2260.68` | `2253.72` | `1149.36` | 5,955.64 USD | `+0.52%` | `20X Cross` |
| `1838` | `0xaf9f...a4fa` | `LONG` | 1,130,938.64 USD | `501.75` | `2269.89` | `2253.72` | `0.000000` | -7,972.99 USD | `-0.70%` | `20X Cross` |
| `1840` | `0x6936...9417` | `SHORT` | 1,130,550.00 USD | `500.00` | `2315.11` | `2253.72` | `2359.66` | 27,005.21 USD | `+2.39%` | `25X Isolated` |
| `1841` | `0x7298...7d6c` | `SHORT` | 1,129,105.20 USD | `498.15` | `3426.75` | `2253.72` | `5422.37` | 577,930.62 USD | `+51.18%` | `20X Cross` |
| `1842` | `0x89b2...9ca6` | `LONG` | 1,126,800.00 USD | `500.00` | `2484.03` | `2253.72` | `1954.18` | -115,219.35 USD | `-10.23%` | `25X Cross` |
| `1855` | `0xc10f...23b3` | `LONG` | 1,115,681.00 USD | `490.00` | `2383.92` | `2253.72` | `2084.59` | -52,440.28 USD | `-4.70%` | `25X Cross` |
| `1858` | `0x536c...3e1f` | `LONG` | 1,115,000.21 USD | `494.83` | `2275.87` | `2253.72` | `2129.50` | -11,172.11 USD | `-1.00%` | `20X Cross` |
| `1861` | `0x9c68...7783` | `SHORT` | 1,113,395.70 USD | `493.31` | `2273.58` | `2253.72` | `3897.25` | 8,183.54 USD | `+0.74%` | `25X Cross` |
| `1870` | `0x321f...1c84` | `SHORT` | 1,106,477.32 USD | `488.02` | `2370.09` | `2253.72` | `3028.24` | 50,167.28 USD | `+4.53%` | `10X Cross` |
| `1876` | `0x404c...5f03` | `SHORT` | 1,103,633.22 USD | `489.79` | `2671.94` | `2253.72` | `5073.97` | 205,046.34 USD | `+18.58%` | `20X Cross` |
| `1883` | `0x8923...1bac` | `SHORT` | 1,090,925.69 USD | `480.82` | `2277.43` | `2253.72` | `3097.17` | 4,102.35 USD | `+0.38%` | `25X Cross` |
| `1934` | `0x82c6...fe42` | `LONG` | 1,052,048.75 USD | `462.50` | `2501.38` | `2253.72` | `2054.47` | -104,841.82 USD | `-9.97%` | `5X Isolated` |
| `1943` | `0x2de3...486d` | `LONG` | 1,043,542.64 USD | `460.40` | `2286.27` | `2253.72` | `1281.84` | -9,058.27 USD | `-0.87%` | `25X Cross` |
| `1953` | `0x617e...0f97` | `SHORT` | 1,033,285.81 USD | `457.85` | `2205.60` | `2253.72` | `3798.10` | -23,441.97 USD | `-2.27%` | `10X Cross` |
| `1989` | `0xae55...2236` | `LONG` | 1,016,415.00 USD | `450.00` | `2510.21` | `2253.72` | `0.000000` | -113,182.50 USD | `-11.14%` | `25X Cross` |
| `1993` | `0x53f8...ceff` | `LONG` | 1,013,333.27 USD | `445.60` | `2399.81` | `2253.72` | `0.000000` | -56,017.32 USD | `-5.53%` | `20X Cross` |
| `2009` | `0xac26...a9c7` | `SHORT` | 1,007,693.24 USD | `446.28` | `2192.58` | `2253.72` | `8555.10` | -29,193.54 USD | `-2.90%` | `20X Cross` |
| `2023` | `0xd6e1...f256` | `SHORT` | 1,001,785.41 USD | `443.66` | `2259.33` | `2253.72` | `3560.04` | 593.81 USD | `+0.06%` | `25X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `ANNOUNCEMENT` | `INFO` | `2352.10` | 70,624.39 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 70.62K USD at 2352.1000 USD [API] | `2026-10-28 18:51:58` |
| `ANNOUNCEMENT` | `INFO` | `2452.70` | 2,224.84 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 2.22K USD at 2452.7000 USD [API] | `2026-09-17 20:15:01` |


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
| `1D` | `Long Liquidation` | `2015.70` | 443,670,000.00 USD | 443,670,000.00 USD | 0.00 USD | 176,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2018.60` | 443,490,000.00 USD | 443,490,000.00 USD | 83,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2021.50` | 443,410,000.00 USD | 443,410,000.00 USD | 0.00 USD | 558,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2025.00` | 1,710,000.00 USD | 322,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2025.30` | 876,790,000.00 USD | 876,790,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2027.30` | 442,850,000.00 USD | 442,850,000.00 USD | 0.00 USD | 970,290.00 USD | 40,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2028.60` | 876,620,000.00 USD | 876,620,000.00 USD | 0.00 USD | 1,180,000.00 USD | 35,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2030.20` | 441,840,000.00 USD | 441,840,000.00 USD | 87,180.00 USD | 136,500.00 USD | 43,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2031.90` | 875,400,000.00 USD | 875,400,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2033.10` | 441,570,000.00 USD | 441,570,000.00 USD | 1,460,000.00 USD | 1,330,000.00 USD | 408,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2035.00` | 1,790,000.00 USD | 320,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2035.20` | 873,950,000.00 USD | 873,950,000.00 USD | 146,420.00 USD | 186,130.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2036.00` | 438,380,000.00 USD | 438,380,000.00 USD | 866,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2038.50` | 872,260,000.00 USD | 872,260,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2038.90` | 437,510,000.00 USD | 437,510,000.00 USD | 138,370.00 USD | 0.00 USD | 13,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2041.80` | 437,360,000.00 USD | 437,360,000.00 USD | 0.00 USD | 178,560.00 USD | 14,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2045.00` | 17,480,000.00 USD | 319,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2045.10` | 870,800,000.00 USD | 870,800,000.00 USD | 0.00 USD | 149,500.00 USD | 47,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2050.50` | 437,170,000.00 USD | 437,170,000.00 USD | 0.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2051.70` | 870,610,000.00 USD | 870,610,000.00 USD | 1,320,000.00 USD | 0.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2053.40` | 436,110,000.00 USD | 436,110,000.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2055.00` | 5,010,000.00 USD | 301,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2056.30` | 435,990,000.00 USD | 435,990,000.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2058.30` | 868,100,000.00 USD | 868,100,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2059.20` | 435,750,000.00 USD | 435,750,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2061.60` | 867,750,000.00 USD | 867,750,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2062.10` | 435,000,000.00 USD | 435,000,000.00 USD | 80,610.00 USD | 121,470.00 USD | 52,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2064.90` | 862,500,000.00 USD | 862,500,000.00 USD | 1,230,000.00 USD | 313,000.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2065.00` | 434,740,000.00 USD | 434,740,000.00 USD | 984,680.00 USD | 537,030.00 USD | 598,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2065.00` | 2,650,000.00 USD | 296,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2067.90` | 432,620,000.00 USD | 432,620,000.00 USD | 387,410.00 USD | 1,010,000.00 USD | 50,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2068.20` | 859,970,000.00 USD | 859,970,000.00 USD | 1,740,000.00 USD | 1,860,000.00 USD | 893,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2070.80` | 431,180,000.00 USD | 431,180,000.00 USD | 1,100,000.00 USD | 854,090.00 USD | 437,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2071.50` | 855,480,000.00 USD | 855,480,000.00 USD | 2,820,000.00 USD | 2,410,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2073.70` | 428,780,000.00 USD | 428,780,000.00 USD | 419,970.00 USD | 62,630.00 USD | 926,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2074.80` | 849,010,000.00 USD | 849,010,000.00 USD | 4,370,000.00 USD | 3,270,000.00 USD | 4,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 3,470,000.00 USD | 294,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2076.60` | 427,370,000.00 USD | 427,370,000.00 USD | 2,580,000.00 USD | 1,020,000.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2078.10` | 837,320,000.00 USD | 837,320,000.00 USD | 5,560,000.00 USD | 4,320,000.00 USD | 2,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2079.50` | 421,770,000.00 USD | 421,770,000.00 USD | 1,700,000.00 USD | 1,270,000.00 USD | 443,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2081.40` | 825,030,000.00 USD | 825,030,000.00 USD | 4,720,000.00 USD | 3,420,000.00 USD | 2,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2082.40` | 418,360,000.00 USD | 418,360,000.00 USD | 1,610,000.00 USD | 1,140,000.00 USD | 224,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2084.70` | 814,390,000.00 USD | 814,390,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 4,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 1,850,000.00 USD | 290,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2085.30` | 415,370,000.00 USD | 415,370,000.00 USD | 2,180,000.00 USD | 1,820,000.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2088.00` | 805,590,000.00 USD | 805,590,000.00 USD | 3,990,000.00 USD | 2,780,000.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2088.20` | 409,550,000.00 USD | 409,550,000.00 USD | 1,730,000.00 USD | 1,000,000.00 USD | 605,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2091.10` | 406,210,000.00 USD | 406,210,000.00 USD | 1,250,000.00 USD | 423,330.00 USD | 520,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2091.30` | 797,170,000.00 USD | 797,170,000.00 USD | 4,410,000.00 USD | 952,210.00 USD | 7,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2094.00` | 404,020,000.00 USD | 404,020,000.00 USD | 1,800,000.00 USD | 1,330,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2094.60` | 784,220,000.00 USD | 784,220,000.00 USD | 5,720,000.00 USD | 2,160,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 2,410,000.00 USD | 288,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2096.90` | 399,540,000.00 USD | 399,540,000.00 USD | 1,010,000.00 USD | 797,210.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2097.90` | 773,990,000.00 USD | 773,990,000.00 USD | 2,340,000.00 USD | 3,210,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2099.80` | 396,220,000.00 USD | 396,220,000.00 USD | 194,900.00 USD | 700,850.00 USD | 11,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2101.20` | 767,150,000.00 USD | 767,150,000.00 USD | 999,530.00 USD | 1,580,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2102.70` | 395,320,000.00 USD | 395,320,000.00 USD | 530,980.00 USD | 289,160.00 USD | 466,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2104.50` | 760,560,000.00 USD | 760,560,000.00 USD | 2,010,000.00 USD | 1,180,000.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 1,670,000.00 USD | 286,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2105.60` | 394,030,000.00 USD | 394,030,000.00 USD | 652,720.00 USD | 671,930.00 USD | 422,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2107.80` | 755,120,000.00 USD | 755,120,000.00 USD | 2,380,000.00 USD | 452,470.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2108.50` | 392,280,000.00 USD | 392,280,000.00 USD | 600,390.00 USD | 21,400.00 USD | 102,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2111.10` | 750,630,000.00 USD | 750,630,000.00 USD | 3,530,000.00 USD | 2,350,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2111.40` | 391,560,000.00 USD | 391,560,000.00 USD | 490,860.00 USD | 146,050.00 USD | 193,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2114.30` | 390,730,000.00 USD | 390,730,000.00 USD | 420,950.00 USD | 507,320.00 USD | 389,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2114.40` | 742,590,000.00 USD | 742,590,000.00 USD | 1,080,000.00 USD | 1,850,000.00 USD | 3,800,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 1,430,000.00 USD | 284,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2117.20` | 389,410,000.00 USD | 389,410,000.00 USD | 202,840.00 USD | 15,250.00 USD | 635,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2117.70` | 735,860,000.00 USD | 735,860,000.00 USD | 3,430,000.00 USD | 2,020,000.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2120.10` | 388,550,000.00 USD | 388,550,000.00 USD | 198,890.00 USD | 431,090.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2121.00` | 727,020,000.00 USD | 727,020,000.00 USD | 3,650,000.00 USD | 1,340,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2123.00` | 386,820,000.00 USD | 386,820,000.00 USD | 1,320,000.00 USD | 683,920.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2124.30` | 720,210,000.00 USD | 720,210,000.00 USD | 832,850.00 USD | 972,650.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 17,940,000.00 USD | 283,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2125.90` | 383,670,000.00 USD | 383,670,000.00 USD | 179,030.00 USD | 1,330,000.00 USD | 486,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2127.60` | 716,890,000.00 USD | 716,890,000.00 USD | 2,400,000.00 USD | 2,630,000.00 USD | 3,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2128.80` | 381,670,000.00 USD | 381,670,000.00 USD | 116,180.00 USD | 475,750.00 USD | 318,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2130.90` | 708,600,000.00 USD | 708,600,000.00 USD | 2,410,000.00 USD | 2,300,000.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2131.70` | 380,760,000.00 USD | 380,760,000.00 USD | 0.00 USD | 18,610.00 USD | 331,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2134.20` | 702,180,000.00 USD | 702,180,000.00 USD | 2,170,000.00 USD | 550,450.00 USD | 308,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 14,630,000.00 USD | 265,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2137.50` | 380,410,000.00 USD | 380,410,000.00 USD | 0.00 USD | 278,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2137.50` | 699,150,000.00 USD | 699,150,000.00 USD | 1,040,000.00 USD | 880,790.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2140.80` | 697,190,000.00 USD | 697,190,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2144.10` | 693,250,000.00 USD | 693,250,000.00 USD | 449,020.00 USD | 1,130,000.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 7,440,000.00 USD | 250,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2147.40` | 691,400,000.00 USD | 691,400,000.00 USD | 657,710.00 USD | 421,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2150.70` | 690,330,000.00 USD | 690,330,000.00 USD | 459,630.00 USD | 463,640.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2152.00` | 380,130,000.00 USD | 380,130,000.00 USD | 208,250.00 USD | 440,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2154.00` | 689,370,000.00 USD | 689,370,000.00 USD | 128,430.00 USD | 331,520.00 USD | 32,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2154.90` | 379,490,000.00 USD | 379,490,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 2,180,000.00 USD | 243,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2157.30` | 688,880,000.00 USD | 688,880,000.00 USD | 388,210.00 USD | 1,030,000.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2157.80` | 378,090,000.00 USD | 378,090,000.00 USD | 0.00 USD | 0.00 USD | 37,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2160.60` | 686,380,000.00 USD | 686,380,000.00 USD | 646,940.00 USD | 1,900,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2160.70` | 378,050,000.00 USD | 378,050,000.00 USD | 0.00 USD | 2,290,000.00 USD | 71,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2163.60` | 375,690,000.00 USD | 375,690,000.00 USD | 0.00 USD | 999,490.00 USD | 28,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2163.90` | 681,840,000.00 USD | 681,840,000.00 USD | 566,120.00 USD | 3,280,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 6,820,000.00 USD | 241,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2166.50` | 374,660,000.00 USD | 374,660,000.00 USD | 1,690,000.00 USD | 341,240.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2167.20` | 676,690,000.00 USD | 676,690,000.00 USD | 25,540.00 USD | 3,620,000.00 USD | 50,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2169.40` | 371,500,000.00 USD | 371,500,000.00 USD | 6,770,000.00 USD | 4,810,000.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2170.50` | 673,000,000.00 USD | 673,000,000.00 USD | 3,500,000.00 USD | 3,730,000.00 USD | 5,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2173.80` | 660,530,000.00 USD | 660,530,000.00 USD | 4,110,000.00 USD | 363,040.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 109,290,000.00 USD | 234,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2175.20` | 357,800,000.00 USD | 357,800,000.00 USD | 345,940.00 USD | 301,420.00 USD | 33,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2177.10` | 655,050,000.00 USD | 655,050,000.00 USD | 0.00 USD | 0.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2178.10` | 357,120,000.00 USD | 357,120,000.00 USD | 0.00 USD | 1,400,000.00 USD | 49,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2180.40` | 653,730,000.00 USD | 653,730,000.00 USD | 0.00 USD | 373,740.00 USD | 176,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2181.00` | 355,670,000.00 USD | 355,670,000.00 USD | 2,080,000.00 USD | 478,110.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2183.70` | 653,180,000.00 USD | 653,180,000.00 USD | 0.00 USD | 1,310,000.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2183.90` | 351,740,000.00 USD | 351,740,000.00 USD | 1,350,000.00 USD | 509,320.00 USD | 13,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2185.00` | 100,000,000.00 USD | 124,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2186.80` | 349,870,000.00 USD | 349,870,000.00 USD | 0.00 USD | 1,450,000.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2187.00` | 649,330,000.00 USD | 649,330,000.00 USD | 556,600.00 USD | 0.00 USD | 54,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2189.70` | 346,620,000.00 USD | 346,620,000.00 USD | 0.00 USD | 0.00 USD | 693,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2190.30` | 648,720,000.00 USD | 648,720,000.00 USD | 2,730,000.00 USD | 0.00 USD | 4,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2192.60` | 345,930,000.00 USD | 345,930,000.00 USD | 605,210.00 USD | 222,200.00 USD | 109,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 2,280,000.00 USD | 24,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2195.50` | 344,990,000.00 USD | 344,990,000.00 USD | 0.00 USD | 881,070.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2196.90` | 641,790,000.00 USD | 641,790,000.00 USD | 2,580,000.00 USD | 474,090.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2198.40` | 342,220,000.00 USD | 342,220,000.00 USD | 416,500.00 USD | 149,110.00 USD | 50,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2200.20` | 636,690,000.00 USD | 636,690,000.00 USD | 3,000,000.00 USD | 5,080,000.00 USD | 3,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2201.30` | 341,610,000.00 USD | 341,610,000.00 USD | 1,690,000.00 USD | 4,250,000.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2203.50` | 625,420,000.00 USD | 625,420,000.00 USD | 3,650,000.00 USD | 1,710,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2204.20` | 334,170,000.00 USD | 334,170,000.00 USD | 2,130,000.00 USD | 314,310.00 USD | 867,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 8,120,000.00 USD | 22,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2206.80` | 616,310,000.00 USD | 616,310,000.00 USD | 6,920,000.00 USD | 9,430,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2207.10` | 330,850,000.00 USD | 330,850,000.00 USD | 2,210,000.00 USD | 10,880,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2210.00` | 315,730,000.00 USD | 315,730,000.00 USD | 3,190,000.00 USD | 3,380,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2210.10` | 595,940,000.00 USD | 595,940,000.00 USD | 12,800,000.00 USD | 20,410,000.00 USD | 6,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2212.90` | 306,470,000.00 USD | 306,470,000.00 USD | 9,500,000.00 USD | 8,670,000.00 USD | 4,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2213.40` | 556,260,000.00 USD | 556,260,000.00 USD | 10,920,000.00 USD | 14,600,000.00 USD | 19,980,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 4,660,000.00 USD | 14,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2215.80` | 283,910,000.00 USD | 283,910,000.00 USD | 18,430,000.00 USD | 9,030,000.00 USD | 10,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2216.70` | 510,760,000.00 USD | 510,760,000.00 USD | 25,210,000.00 USD | 17,030,000.00 USD | 9,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2218.70` | 246,280,000.00 USD | 246,280,000.00 USD | 6,790,000.00 USD | 7,780,000.00 USD | 1,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2220.00` | 459,130,000.00 USD | 459,130,000.00 USD | 24,310,000.00 USD | 12,300,000.00 USD | 12,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2221.60` | 229,840,000.00 USD | 229,840,000.00 USD | 6,200,000.00 USD | 12,240,000.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2223.30` | 409,770,000.00 USD | 409,770,000.00 USD | 10,150,000.00 USD | 8,220,000.00 USD | 11,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2224.50` | 210,060,000.00 USD | 210,060,000.00 USD | 9,730,000.00 USD | 5,030,000.00 USD | 5,660,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2225.00` | 5,380,000.00 USD | 9,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2226.60` | 379,490,000.00 USD | 379,490,000.00 USD | 12,840,000.00 USD | 11,030,000.00 USD | 9,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2227.40` | 189,640,000.00 USD | 189,640,000.00 USD | 5,940,000.00 USD | 13,200,000.00 USD | 5,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2229.90` | 345,660,000.00 USD | 345,660,000.00 USD | 12,730,000.00 USD | 11,790,000.00 USD | 25,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2230.30` | 164,890,000.00 USD | 164,890,000.00 USD | 6,830,000.00 USD | 8,320,000.00 USD | 2,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2233.20` | 147,320,000.00 USD | 147,320,000.00 USD | 5,060,000.00 USD | 4,220,000.00 USD | 8,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2233.20` | 295,390,000.00 USD | 295,390,000.00 USD | 16,600,000.00 USD | 24,290,000.00 USD | 10,420,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2235.00` | 878,090.00 USD | 878,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2236.10` | 130,000,000.00 USD | 130,000,000.00 USD | 22,420,000.00 USD | 0.00 USD | 10,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2236.50` | 244,070,000.00 USD | 244,070,000.00 USD | 16,050,000.00 USD | 7,430,000.00 USD | 27,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2239.00` | 96,790,000.00 USD | 96,790,000.00 USD | 17,940,000.00 USD | 5,930,000.00 USD | 9,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2239.80` | 192,770,000.00 USD | 192,770,000.00 USD | 15,710,000.00 USD | 6,600,000.00 USD | 13,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2241.90` | 63,500,000.00 USD | 63,500,000.00 USD | 619,130.00 USD | 760,920.00 USD | 5,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2243.10` | 156,710,000.00 USD | 156,710,000.00 USD | 22,920,000.00 USD | 0.00 USD | 18,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2244.80` | 56,750,000.00 USD | 56,750,000.00 USD | 3,850,000.00 USD | 4,700,000.00 USD | 463,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2245.00` | 4,430,000.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2246.40` | 115,460,000.00 USD | 115,460,000.00 USD | 14,340,000.00 USD | 0.00 USD | 13,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2247.70` | 47,740,000.00 USD | 47,740,000.00 USD | 12,800,000.00 USD | 0.00 USD | 7,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2249.70` | 87,200,000.00 USD | 87,200,000.00 USD | 18,000,000.00 USD | 0.00 USD | 12,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2250.60` | 27,860,000.00 USD | 27,860,000.00 USD | 4,190,000.00 USD | 1,910,000.00 USD | 3,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2253.00` | 56,380,000.00 USD | 56,380,000.00 USD | 26,890,000.00 USD | 0.00 USD | 12,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2253.50` | 17,790,000.00 USD | 17,790,000.00 USD | 5,410,000.00 USD | 4,440,000.00 USD | 4,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2255.00` | 68,250.00 USD | 68,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2256.30` | 17,450,000.00 USD | 17,450,000.00 USD | 17,450,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2256.40` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2259.60` | 10,940,000.00 USD | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2262.20` | 2,580,000.00 USD | 2,580,000.00 USD | 2,420,000.00 USD | 0.00 USD | 156,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2265.00` | 410.42 USD | 878,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2265.10` | 12,410,000.00 USD | 12,410,000.00 USD | 0.00 USD | 0.00 USD | 9,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2268.00` | 16,850,000.00 USD | 16,850,000.00 USD | 0.00 USD | 0.00 USD | 4,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2273.80` | 17,070,000.00 USD | 17,070,000.00 USD | 220,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2275.00` | 633.82 USD | 879,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2276.70` | 19,100,000.00 USD | 19,100,000.00 USD | 1,370,000.00 USD | 555,110.00 USD | 114,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2279.40` | 27,940,000.00 USD | 27,940,000.00 USD | 0.00 USD | 17,000,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2279.60` | 52,670,000.00 USD | 52,670,000.00 USD | 23,020,000.00 USD | 6,030,000.00 USD | 4,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2282.50` | 154,360,000.00 USD | 154,360,000.00 USD | 51,100,000.00 USD | 39,620,000.00 USD | 10,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2282.70` | 128,630,000.00 USD | 128,630,000.00 USD | 0.00 USD | 87,090,000.00 USD | 13,610,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2285.00` | 2,530.00 USD | 881,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2285.40` | 166,560,000.00 USD | 166,560,000.00 USD | 7,830,000.00 USD | 3,050,000.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2286.00` | 138,040,000.00 USD | 138,040,000.00 USD | 0.00 USD | 9,400,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2288.30` | 167,460,000.00 USD | 167,460,000.00 USD | 0.00 USD | 760,920.00 USD | 133,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2289.30` | 143,320,000.00 USD | 143,320,000.00 USD | 0.00 USD | 0.00 USD | 5,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2291.20` | 176,490,000.00 USD | 176,490,000.00 USD | 0.00 USD | 8,840,000.00 USD | 199,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2294.10` | 190,360,000.00 USD | 190,360,000.00 USD | 8,310,000.00 USD | 0.00 USD | 5,560,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2295.00` | 25,230.00 USD | 906,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2295.90` | 158,000,000.00 USD | 158,000,000.00 USD | 6,580,000.00 USD | 2,380,000.00 USD | 5,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2297.00` | 204,380,000.00 USD | 204,380,000.00 USD | 5,410,000.00 USD | 8,350,000.00 USD | 253,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2299.20` | 186,420,000.00 USD | 186,420,000.00 USD | 11,730,000.00 USD | 11,130,000.00 USD | 5,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2299.90` | 219,750,000.00 USD | 219,750,000.00 USD | 0.00 USD | 7,970,000.00 USD | 7,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2302.50` | 233,530,000.00 USD | 233,530,000.00 USD | 23,020,000.00 USD | 7,250,000.00 USD | 16,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2302.80` | 240,570,000.00 USD | 240,570,000.00 USD | 15,230,000.00 USD | 682,490.00 USD | 4,910,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2305.00` | 4,250,000.00 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2305.70` | 270,200,000.00 USD | 270,200,000.00 USD | 10,050,000.00 USD | 14,890,000.00 USD | 4,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2305.80` | 254,340,000.00 USD | 254,340,000.00 USD | 2,980,000.00 USD | 8,820,000.00 USD | 9,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2308.60` | 274,960,000.00 USD | 274,960,000.00 USD | 2,420,000.00 USD | 2,340,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2309.10` | 258,110,000.00 USD | 258,110,000.00 USD | 732,090.00 USD | 930,630.00 USD | 2,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2311.50` | 284,600,000.00 USD | 284,600,000.00 USD | 691,870.00 USD | 1,260,000.00 USD | 7,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2312.40` | 276,250,000.00 USD | 276,250,000.00 USD | 7,270,000.00 USD | 0.00 USD | 10,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2314.40` | 298,930,000.00 USD | 298,930,000.00 USD | 0.00 USD | 14,100,000.00 USD | 231,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2315.00` | 2,480,000.00 USD | 7,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2315.70` | 283,820,000.00 USD | 283,820,000.00 USD | 0.00 USD | 7,460,000.00 USD | 117,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2317.30` | 327,480,000.00 USD | 327,480,000.00 USD | 10,230,000.00 USD | 10,470,000.00 USD | 7,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2319.00` | 295,010,000.00 USD | 295,010,000.00 USD | 1,020,000.00 USD | 4,550,000.00 USD | 5,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2320.20` | 343,590,000.00 USD | 343,590,000.00 USD | 6,580,000.00 USD | 9,360,000.00 USD | 173,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2322.30` | 312,170,000.00 USD | 312,170,000.00 USD | 1,110,000.00 USD | 15,930,000.00 USD | 108,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2323.10` | 358,160,000.00 USD | 358,160,000.00 USD | 572,970.00 USD | 10,410,000.00 USD | 3,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2325.00` | 1,420,000.00 USD | 9,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2325.60` | 332,820,000.00 USD | 332,820,000.00 USD | 9,720,000.00 USD | 2,540,000.00 USD | 8,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2326.00` | 369,850,000.00 USD | 369,850,000.00 USD | 479,120.00 USD | 5,550,000.00 USD | 5,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2328.90` | 376,820,000.00 USD | 376,820,000.00 USD | 5,690,000.00 USD | 884,940.00 USD | 402,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2328.90` | 344,640,000.00 USD | 344,640,000.00 USD | 3,860,000.00 USD | 0.00 USD | 7,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2331.80` | 393,120,000.00 USD | 393,120,000.00 USD | 15,910,000.00 USD | 251,940.00 USD | 126,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2332.20` | 373,880,000.00 USD | 373,880,000.00 USD | 29,230,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2334.70` | 416,680,000.00 USD | 416,680,000.00 USD | 13,410,000.00 USD | 2,960,000.00 USD | 7,200,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2335.00` | 1,230,000.00 USD | 10,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2335.50` | 431,890,000.00 USD | 431,890,000.00 USD | 28,990,000.00 USD | 18,420,000.00 USD | 10,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2337.60` | 430,560,000.00 USD | 430,560,000.00 USD | 9,880,000.00 USD | 407,920.00 USD | 3,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2338.80` | 449,760,000.00 USD | 449,760,000.00 USD | 9,570,000.00 USD | 0.00 USD | 8,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2340.50` | 454,460,000.00 USD | 454,460,000.00 USD | 8,010,000.00 USD | 5,100,000.00 USD | 10,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2342.10` | 489,860,000.00 USD | 489,860,000.00 USD | 4,720,000.00 USD | 21,390,000.00 USD | 14,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2343.40` | 469,090,000.00 USD | 469,090,000.00 USD | 2,060,000.00 USD | 5,580,000.00 USD | 7,000,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2345.00` | 326,400.00 USD | 10,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2345.40` | 511,230,000.00 USD | 511,230,000.00 USD | 1,350,000.00 USD | 13,990,000.00 USD | 6,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2346.30` | 482,000,000.00 USD | 482,000,000.00 USD | 4,950,000.00 USD | 1,940,000.00 USD | 6,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2348.70` | 549,130,000.00 USD | 549,130,000.00 USD | 847,620.00 USD | 9,500,000.00 USD | 27,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2349.20` | 508,060,000.00 USD | 508,060,000.00 USD | 13,480,000.00 USD | 6,150,000.00 USD | 6,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2352.00` | 585,750,000.00 USD | 585,750,000.00 USD | 2,930,000.00 USD | 23,060,000.00 USD | 10,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2352.10` | 542,570,000.00 USD | 542,570,000.00 USD | 24,370,000.00 USD | 4,230,000.00 USD | 5,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2355.00` | 564,350,000.00 USD | 564,350,000.00 USD | 1,010,000.00 USD | 19,500,000.00 USD | 1,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 1,270,000.00 USD | 11,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2355.30` | 640,340,000.00 USD | 640,340,000.00 USD | 16,520,000.00 USD | 36,690,000.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2357.90` | 575,030,000.00 USD | 575,030,000.00 USD | 2,890,000.00 USD | 4,290,000.00 USD | 3,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2358.60` | 652,480,000.00 USD | 652,480,000.00 USD | 7,110,000.00 USD | 512,220.00 USD | 4,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2360.80` | 596,270,000.00 USD | 596,270,000.00 USD | 10,720,000.00 USD | 5,400,000.00 USD | 5,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2361.90` | 659,600,000.00 USD | 659,600,000.00 USD | 3,150,000.00 USD | 3,800,000.00 USD | 176,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2363.70` | 622,130,000.00 USD | 622,130,000.00 USD | 7,900,000.00 USD | 9,120,000.00 USD | 8,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 1,310,000.00 USD | 13,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2365.20` | 677,500,000.00 USD | 677,500,000.00 USD | 8,440,000.00 USD | 0.00 USD | 9,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2366.60` | 627,830,000.00 USD | 627,830,000.00 USD | 3,560,000.00 USD | 509,320.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2368.50` | 690,570,000.00 USD | 690,570,000.00 USD | 10,830,000.00 USD | 1,780,000.00 USD | 458,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2369.50` | 654,320,000.00 USD | 654,320,000.00 USD | 13,850,000.00 USD | 7,720,000.00 USD | 4,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2371.80` | 771,510,000.00 USD | 771,510,000.00 USD | 26,000,000.00 USD | 0.00 USD | 54,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2372.40` | 691,850,000.00 USD | 691,850,000.00 USD | 14,410,000.00 USD | 10,690,000.00 USD | 12,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 1,060,000.00 USD | 14,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2375.10` | 798,450,000.00 USD | 798,450,000.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2375.30` | 713,370,000.00 USD | 713,370,000.00 USD | 14,210,000.00 USD | 3,650,000.00 USD | 3,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2378.20` | 738,590,000.00 USD | 738,590,000.00 USD | 5,350,000.00 USD | 7,910,000.00 USD | 11,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2378.40` | 843,870,000.00 USD | 843,870,000.00 USD | 11,800,000.00 USD | 7,950,000.00 USD | 25,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2381.10` | 787,980,000.00 USD | 787,980,000.00 USD | 16,200,000.00 USD | 13,170,000.00 USD | 20,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2381.70` | 883,660,000.00 USD | 883,660,000.00 USD | 8,510,000.00 USD | 6,750,000.00 USD | 24,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2384.00` | 832,030,000.00 USD | 832,030,000.00 USD | 17,870,000.00 USD | 15,110,000.00 USD | 11,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2385.00` | 985,370,000.00 USD | 985,370,000.00 USD | 18,550,000.00 USD | 36,910,000.00 USD | 46,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 42,090,000.00 USD | 56,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2386.90` | 867,740,000.00 USD | 867,740,000.00 USD | 13,540,000.00 USD | 11,770,000.00 USD | 10,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2388.30` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 5,290,000.00 USD | 38,070,000.00 USD | 44,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2389.80` | 893,440,000.00 USD | 893,440,000.00 USD | 10,230,000.00 USD | 9,340,000.00 USD | 6,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2391.60` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 8,560,000.00 USD | 52,080,000.00 USD | 40,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2392.70` | 911,490,000.00 USD | 911,490,000.00 USD | 5,770,000.00 USD | 4,950,000.00 USD | 7,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2394.90` | 1,300,000,000.00 USD | 1,300,000,000.00 USD | 57,450,000.00 USD | 32,260,000.00 USD | 37,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 99,780.00 USD | 56,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2395.60` | 926,980,000.00 USD | 926,980,000.00 USD | 5,140,000.00 USD | 6,720,000.00 USD | 3,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2398.20` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 42,820,000.00 USD | 38,210,000.00 USD | 29,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2398.50` | 946,650,000.00 USD | 946,650,000.00 USD | 5,800,000.00 USD | 6,760,000.00 USD | 7,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2401.40` | 971,600,000.00 USD | 971,600,000.00 USD | 8,280,000.00 USD | 7,500,000.00 USD | 9,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2401.50` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 51,970,000.00 USD | 26,780,000.00 USD | 29,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2404.30` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 10,010,000.00 USD | 11,060,000.00 USD | 8,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2404.80` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 50,800,000.00 USD | 32,200,000.00 USD | 24,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 1,430,000.00 USD | 57,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2407.20` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 15,160,000.00 USD | 9,260,000.00 USD | 7,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2408.10` | 1,720,000,000.00 USD | 1,720,000,000.00 USD | 34,390,000.00 USD | 31,420,000.00 USD | 25,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2410.10` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 7,660,000.00 USD | 7,700,000.00 USD | 9,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2411.40` | 1,800,000,000.00 USD | 1,800,000,000.00 USD | 19,200,000.00 USD | 32,580,000.00 USD | 27,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2413.00` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 8,270,000.00 USD | 5,470,000.00 USD | 3,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2414.70` | 1,870,000,000.00 USD | 1,870,000,000.00 USD | 24,010,000.00 USD | 21,950,000.00 USD | 23,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 858,190.00 USD | 58,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2415.90` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 3,710,000.00 USD | 2,920,000.00 USD | 3,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2418.00` | 1,940,000,000.00 USD | 1,940,000,000.00 USD | 34,060,000.00 USD | 15,260,000.00 USD | 24,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2418.80` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 4,240,000.00 USD | 2,710,000.00 USD | 3,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2421.30` | 2,010,000,000.00 USD | 2,010,000,000.00 USD | 25,700,000.00 USD | 27,890,000.00 USD | 21,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2421.70` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 6,390,000.00 USD | 6,200,000.00 USD | 6,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2424.60` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 1,790,000.00 USD | 2,770,000.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.60` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 24,180,000.00 USD | 35,050,000.00 USD | 34,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 953,600.00 USD | 59,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2427.50` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 731,900.00 USD | 124,100.00 USD | 601,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2427.90` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 25,200,000.00 USD | 18,380,000.00 USD | 26,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2430.40` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 1,640,000.00 USD | 1,770,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2431.20` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 10,380,000.00 USD | 17,060,000.00 USD | 9,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2433.30` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 2,160,000.00 USD | 2,160,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2434.50` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 27,390,000.00 USD | 21,570,000.00 USD | 11,160,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 4,450,000.00 USD | 64,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2436.20` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 2,340,000.00 USD | 475,290.00 USD | 579,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2437.80` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 12,000,000.00 USD | 12,820,000.00 USD | 5,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2439.10` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 304,760.00 USD | 641,280.00 USD | 484,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2441.10` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 15,080,000.00 USD | 8,120,000.00 USD | 10,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2442.00` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 2,360,000.00 USD | 2,020,000.00 USD | 735,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2444.40` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 8,860,000.00 USD | 15,160,000.00 USD | 14,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2444.90` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 544,880.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 280,670.00 USD | 64,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2447.70` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 11,650,000.00 USD | 8,510,000.00 USD | 17,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2447.80` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 687,490.00 USD | 330,760.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2450.70` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 2,550,000.00 USD | 1,470,000.00 USD | 3,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2451.00` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 16,710,000.00 USD | 14,100,000.00 USD | 16,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2453.60` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 4,790,000.00 USD | 4,000,000.00 USD | 3,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2454.30` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 4,620,000.00 USD | 4,930,000.00 USD | 3,880,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 96,380.00 USD | 64,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2456.50` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 1,060,000.00 USD | 2,650,000.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2457.60` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 15,150,000.00 USD | 12,540,000.00 USD | 12,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2459.40` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 1,900,000.00 USD | 1,190,000.00 USD | 366,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2460.90` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 5,580,000.00 USD | 8,670,000.00 USD | 6,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2462.30` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 490,260.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2464.20` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 8,720,000.00 USD | 7,700,000.00 USD | 4,700,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 914,970.00 USD | 65,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2465.20` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 83,300.00 USD | 176,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2467.50` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 4,540,000.00 USD | 3,710,000.00 USD | 586,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2468.10` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 1,250,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2470.80` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 3,960,000.00 USD | 2,290,000.00 USD | 522,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2471.00` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 391,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2474.10` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 5,230,000.00 USD | 2,920,000.00 USD | 2,400,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 438,920.00 USD | 65,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2476.80` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 943,590.00 USD | 40,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2477.40` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 1,660,000.00 USD | 4,420,000.00 USD | 718,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2479.70` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 26,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2480.70` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 2,110,000.00 USD | 4,170,000.00 USD | 540,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2482.60` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 677,540.00 USD | 136,500.00 USD | 451,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2484.00` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 1,210,000.00 USD | 1,390,000.00 USD | 1,440,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 96,970.00 USD | 65,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2485.50` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 865,140.00 USD | 1,330,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2487.30` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 325,140.00 USD | 262,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2488.40` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 866,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2490.60` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 2,910,000.00 USD | 2,540,000.00 USD | 279,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2491.30` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 138,370.00 USD | 0.00 USD | 13,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2493.90` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 1,660,000.00 USD | 1,790,000.00 USD | 3,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2494.20` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 178,560.00 USD | 14,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 8,760,000.00 USD | 74,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2497.20` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 2,940,000.00 USD | 5,270,000.00 USD | 8,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2500.50` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 1,110,000.00 USD | 2,280,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2503.80` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 63,860.00 USD | 1,480,000.00 USD | 125,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 2,310,000.00 USD | 77,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2505.80` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2507.10` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 4,340,000.00 USD | 3,090,000.00 USD | 3,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2510.40` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 2,290,000.00 USD | 1,270,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2511.60` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 242,080.00 USD | 88,880.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2513.70` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 142,410.00 USD | 77,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2517.00` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 97,050.00 USD | 189,640.00 USD | 815,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2517.40` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2520.30` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 80,610.00 USD | 121,470.00 USD | 52,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2520.30` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2523.20` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 563,140.00 USD | 537,030.00 USD | 568,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2523.60` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 4,710,000.00 USD | 81,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2526.10` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 808,950.00 USD | 362,000.00 USD | 53,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2526.90` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2529.00` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 641,110.00 USD | 965,400.00 USD | 464,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2530.20` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 2,800,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2531.90` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 474,040.00 USD | 534,600.00 USD | 7,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2533.50` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 3,530,000.00 USD | 1,850,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2534.80` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 405,580.00 USD | 62,630.00 USD | 919,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2535.00` | 2,520,000.00 USD | 84,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2536.80` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 3,720,000.00 USD | 3,450,000.00 USD | 3,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2537.70` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 2,580,000.00 USD | 926,330.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2540.10` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 4,150,000.00 USD | 3,220,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2540.60` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 1,180,000.00 USD | 1,100,000.00 USD | 808,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2543.40` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 4,150,000.00 USD | 2,520,000.00 USD | 2,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2543.50` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 1,510,000.00 USD | 1,100,000.00 USD | 233,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2545.00` | 5,380,000.00 USD | 89,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2546.40` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 1,780,000.00 USD | 1,410,000.00 USD | 571,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2546.70` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 1,450,000.00 USD | 1,090,000.00 USD | 2,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2549.30` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 1,020,000.00 USD | 803,170.00 USD | 1,470,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2550.00` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 4,320,000.00 USD | 3,550,000.00 USD | 3,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2552.20` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 1,730,000.00 USD | 914,630.00 USD | 396,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2553.30` | 2,730,000,000.00 USD | 2,730,000,000.00 USD | 2,820,000.00 USD | 788,360.00 USD | 2,600,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2555.00` | 397,740.00 USD | 90,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2555.10` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 996,760.00 USD | 221,720.00 USD | 417,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2556.60` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 2,760,000.00 USD | 283,560.00 USD | 6,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2558.00` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 736,590.00 USD | 502,170.00 USD | 811,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2559.90` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 5,720,000.00 USD | 2,130,000.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2560.50` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 1,830,000.00 USD | 1,080,000.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2563.20` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 1,430,000.00 USD | 2,900,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2565.00` | 2,400,000.00 USD | 92,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2566.50` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 1,860,000.00 USD | 1,830,000.00 USD | 3,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2569.80` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 125,250.00 USD | 341,900.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2573.10` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2575.00` | 11,620,000.00 USD | 104,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2576.40` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 2,400,000.00 USD | 930,280.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2579.70` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 2,750,000.00 USD | 1,780,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2583.00` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 1,730,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2585.00` | 26,470,000.00 USD | 130,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2586.30` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 1,480,000.00 USD | 2,030,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2589.60` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 3,310,000.00 USD | 631,590.00 USD | 2,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2592.90` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 2,370,000.00 USD | 1,280,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2595.00` | 1,910,000.00 USD | 132,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2596.20` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 794,750.00 USD | 620,840.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2599.50` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 2,380,000.00 USD | 2,530,000.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2602.80` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 1,680,000.00 USD | 1,260,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2605.00` | 14,250,000.00 USD | 146,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2606.10` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 1,850,000.00 USD | 1,560,000.00 USD | 772,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2609.40` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2612.70` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 1,010,000.00 USD | 643,740.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2615.00` | 293,190.00 USD | 147,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2616.00` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2619.30` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 449,020.00 USD | 323,810.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2622.60` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 631,440.00 USD | 1,220,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2625.00` | 13,030,000.00 USD | 160,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2625.90` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 485,890.00 USD | 474,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2629.20` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 20,460.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2632.40` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 301,060.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `1D` | `2015.70` | 443,670,000.00 USD | 0.00 USD | 443,670,000.00 USD | 0.00 USD | 176,210.00 USD | 0.00 USD |
| `1D` | `2018.60` | 443,490,000.00 USD | 0.00 USD | 443,490,000.00 USD | 83,300.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2021.50` | 443,410,000.00 USD | 0.00 USD | 443,410,000.00 USD | 0.00 USD | 558,730.00 USD | 0.00 USD |
| `7D` | `2025.30` | 876,790,000.00 USD | 0.00 USD | 876,790,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD |
| `1D` | `2027.30` | 442,850,000.00 USD | 0.00 USD | 442,850,000.00 USD | 0.00 USD | 970,290.00 USD | 40,210.00 USD |
| `7D` | `2028.60` | 876,620,000.00 USD | 0.00 USD | 876,620,000.00 USD | 0.00 USD | 1,180,000.00 USD | 35,180.00 USD |
| `1D` | `2030.20` | 441,840,000.00 USD | 0.00 USD | 441,840,000.00 USD | 87,180.00 USD | 136,500.00 USD | 43,160.00 USD |
| `7D` | `2031.90` | 875,400,000.00 USD | 0.00 USD | 875,400,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD |
| `1D` | `2033.10` | 441,570,000.00 USD | 0.00 USD | 441,570,000.00 USD | 1,460,000.00 USD | 1,330,000.00 USD | 408,620.00 USD |
| `7D` | `2035.20` | 873,950,000.00 USD | 0.00 USD | 873,950,000.00 USD | 146,420.00 USD | 186,130.00 USD | 1,360,000.00 USD |
| `1D` | `2036.00` | 438,380,000.00 USD | 0.00 USD | 438,380,000.00 USD | 866,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2038.50` | 872,260,000.00 USD | 0.00 USD | 872,260,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2038.90` | 437,510,000.00 USD | 0.00 USD | 437,510,000.00 USD | 138,370.00 USD | 0.00 USD | 13,360.00 USD |
| `1D` | `2041.80` | 437,360,000.00 USD | 0.00 USD | 437,360,000.00 USD | 0.00 USD | 178,560.00 USD | 14,300.00 USD |
| `7D` | `2045.10` | 870,800,000.00 USD | 0.00 USD | 870,800,000.00 USD | 0.00 USD | 149,500.00 USD | 47,970.00 USD |
| `1D` | `2050.50` | 437,170,000.00 USD | 0.00 USD | 437,170,000.00 USD | 0.00 USD | 338,980.00 USD | 717,780.00 USD |
| `7D` | `2051.70` | 870,610,000.00 USD | 0.00 USD | 870,610,000.00 USD | 1,320,000.00 USD | 0.00 USD | 1,190,000.00 USD |
| `1D` | `2053.40` | 436,110,000.00 USD | 0.00 USD | 436,110,000.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD |
| `1D` | `2056.30` | 435,990,000.00 USD | 0.00 USD | 435,990,000.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2058.30` | 868,100,000.00 USD | 0.00 USD | 868,100,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD |
| `1D` | `2059.20` | 435,750,000.00 USD | 0.00 USD | 435,750,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `7D` | `2061.60` | 867,750,000.00 USD | 0.00 USD | 867,750,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD |
| `1D` | `2062.10` | 435,000,000.00 USD | 0.00 USD | 435,000,000.00 USD | 80,610.00 USD | 121,470.00 USD | 52,590.00 USD |
| `7D` | `2064.90` | 862,500,000.00 USD | 0.00 USD | 862,500,000.00 USD | 1,230,000.00 USD | 313,000.00 USD | 979,910.00 USD |
| `1D` | `2065.00` | 434,740,000.00 USD | 0.00 USD | 434,740,000.00 USD | 984,680.00 USD | 537,030.00 USD | 598,250.00 USD |
| `1D` | `2067.90` | 432,620,000.00 USD | 0.00 USD | 432,620,000.00 USD | 387,410.00 USD | 1,010,000.00 USD | 50,470.00 USD |
| `7D` | `2068.20` | 859,970,000.00 USD | 0.00 USD | 859,970,000.00 USD | 1,740,000.00 USD | 1,860,000.00 USD | 893,570.00 USD |
| `1D` | `2070.80` | 431,180,000.00 USD | 0.00 USD | 431,180,000.00 USD | 1,100,000.00 USD | 854,090.00 USD | 437,490.00 USD |
| `7D` | `2071.50` | 855,480,000.00 USD | 0.00 USD | 855,480,000.00 USD | 2,820,000.00 USD | 2,410,000.00 USD | 1,230,000.00 USD |
| `1D` | `2073.70` | 428,780,000.00 USD | 0.00 USD | 428,780,000.00 USD | 419,970.00 USD | 62,630.00 USD | 926,730.00 USD |
| `7D` | `2074.80` | 849,010,000.00 USD | 0.00 USD | 849,010,000.00 USD | 4,370,000.00 USD | 3,270,000.00 USD | 4,050,000.00 USD |
| `1D` | `2076.60` | 427,370,000.00 USD | 0.00 USD | 427,370,000.00 USD | 2,580,000.00 USD | 1,020,000.00 USD | 2,000,000.00 USD |
| `7D` | `2078.10` | 837,320,000.00 USD | 0.00 USD | 837,320,000.00 USD | 5,560,000.00 USD | 4,320,000.00 USD | 2,410,000.00 USD |
| `1D` | `2079.50` | 421,770,000.00 USD | 0.00 USD | 421,770,000.00 USD | 1,700,000.00 USD | 1,270,000.00 USD | 443,980.00 USD |
| `7D` | `2081.40` | 825,030,000.00 USD | 0.00 USD | 825,030,000.00 USD | 4,720,000.00 USD | 3,420,000.00 USD | 2,500,000.00 USD |
| `1D` | `2082.40` | 418,360,000.00 USD | 0.00 USD | 418,360,000.00 USD | 1,610,000.00 USD | 1,140,000.00 USD | 224,010.00 USD |
| `7D` | `2084.70` | 814,390,000.00 USD | 0.00 USD | 814,390,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 4,900,000.00 USD |
| `1D` | `2085.30` | 415,370,000.00 USD | 0.00 USD | 415,370,000.00 USD | 2,180,000.00 USD | 1,820,000.00 USD | 1,830,000.00 USD |
| `7D` | `2088.00` | 805,590,000.00 USD | 0.00 USD | 805,590,000.00 USD | 3,990,000.00 USD | 2,780,000.00 USD | 1,650,000.00 USD |
| `1D` | `2088.20` | 409,550,000.00 USD | 0.00 USD | 409,550,000.00 USD | 1,730,000.00 USD | 1,000,000.00 USD | 605,040.00 USD |
| `1D` | `2091.10` | 406,210,000.00 USD | 0.00 USD | 406,210,000.00 USD | 1,250,000.00 USD | 423,330.00 USD | 520,600.00 USD |
| `7D` | `2091.30` | 797,170,000.00 USD | 0.00 USD | 797,170,000.00 USD | 4,410,000.00 USD | 952,210.00 USD | 7,590,000.00 USD |
| `1D` | `2094.00` | 404,020,000.00 USD | 0.00 USD | 404,020,000.00 USD | 1,800,000.00 USD | 1,330,000.00 USD | 1,350,000.00 USD |
| `7D` | `2094.60` | 784,220,000.00 USD | 0.00 USD | 784,220,000.00 USD | 5,720,000.00 USD | 2,160,000.00 USD | 2,340,000.00 USD |
| `1D` | `2096.90` | 399,540,000.00 USD | 0.00 USD | 399,540,000.00 USD | 1,010,000.00 USD | 797,210.00 USD | 1,510,000.00 USD |
| `7D` | `2097.90` | 773,990,000.00 USD | 0.00 USD | 773,990,000.00 USD | 2,340,000.00 USD | 3,210,000.00 USD | 1,290,000.00 USD |
| `1D` | `2099.80` | 396,220,000.00 USD | 0.00 USD | 396,220,000.00 USD | 194,900.00 USD | 700,850.00 USD | 11,930.00 USD |
| `7D` | `2101.20` | 767,150,000.00 USD | 0.00 USD | 767,150,000.00 USD | 999,530.00 USD | 1,580,000.00 USD | 4,020,000.00 USD |
| `1D` | `2102.70` | 395,320,000.00 USD | 0.00 USD | 395,320,000.00 USD | 530,980.00 USD | 289,160.00 USD | 466,670.00 USD |
| `7D` | `2104.50` | 760,560,000.00 USD | 0.00 USD | 760,560,000.00 USD | 2,010,000.00 USD | 1,180,000.00 USD | 2,250,000.00 USD |
| `1D` | `2105.60` | 394,030,000.00 USD | 0.00 USD | 394,030,000.00 USD | 652,720.00 USD | 671,930.00 USD | 422,940.00 USD |
| `7D` | `2107.80` | 755,120,000.00 USD | 0.00 USD | 755,120,000.00 USD | 2,380,000.00 USD | 452,470.00 USD | 1,650,000.00 USD |
| `1D` | `2108.50` | 392,280,000.00 USD | 0.00 USD | 392,280,000.00 USD | 600,390.00 USD | 21,400.00 USD | 102,370.00 USD |
| `7D` | `2111.10` | 750,630,000.00 USD | 0.00 USD | 750,630,000.00 USD | 3,530,000.00 USD | 2,350,000.00 USD | 2,170,000.00 USD |
| `1D` | `2111.40` | 391,560,000.00 USD | 0.00 USD | 391,560,000.00 USD | 490,860.00 USD | 146,050.00 USD | 193,960.00 USD |
| `1D` | `2114.30` | 390,730,000.00 USD | 0.00 USD | 390,730,000.00 USD | 420,950.00 USD | 507,320.00 USD | 389,310.00 USD |
| `7D` | `2114.40` | 742,590,000.00 USD | 0.00 USD | 742,590,000.00 USD | 1,080,000.00 USD | 1,850,000.00 USD | 3,800,000.00 USD |
| `1D` | `2117.20` | 389,410,000.00 USD | 0.00 USD | 389,410,000.00 USD | 202,840.00 USD | 15,250.00 USD | 635,290.00 USD |
| `7D` | `2117.70` | 735,860,000.00 USD | 0.00 USD | 735,860,000.00 USD | 3,430,000.00 USD | 2,020,000.00 USD | 3,380,000.00 USD |
| `1D` | `2120.10` | 388,550,000.00 USD | 0.00 USD | 388,550,000.00 USD | 198,890.00 USD | 431,090.00 USD | 1,100,000.00 USD |
| `7D` | `2121.00` | 727,020,000.00 USD | 0.00 USD | 727,020,000.00 USD | 3,650,000.00 USD | 1,340,000.00 USD | 1,820,000.00 USD |
| `1D` | `2123.00` | 386,820,000.00 USD | 0.00 USD | 386,820,000.00 USD | 1,320,000.00 USD | 683,920.00 USD | 1,140,000.00 USD |
| `7D` | `2124.30` | 720,210,000.00 USD | 0.00 USD | 720,210,000.00 USD | 832,850.00 USD | 972,650.00 USD | 1,510,000.00 USD |
| `1D` | `2125.90` | 383,670,000.00 USD | 0.00 USD | 383,670,000.00 USD | 179,030.00 USD | 1,330,000.00 USD | 486,980.00 USD |
| `7D` | `2127.60` | 716,890,000.00 USD | 0.00 USD | 716,890,000.00 USD | 2,400,000.00 USD | 2,630,000.00 USD | 3,270,000.00 USD |
| `1D` | `2128.80` | 381,670,000.00 USD | 0.00 USD | 381,670,000.00 USD | 116,180.00 USD | 475,750.00 USD | 318,170.00 USD |
| `7D` | `2130.90` | 708,600,000.00 USD | 0.00 USD | 708,600,000.00 USD | 2,410,000.00 USD | 2,300,000.00 USD | 1,700,000.00 USD |
| `1D` | `2131.70` | 380,760,000.00 USD | 0.00 USD | 380,760,000.00 USD | 0.00 USD | 18,610.00 USD | 331,620.00 USD |
| `7D` | `2134.20` | 702,180,000.00 USD | 0.00 USD | 702,180,000.00 USD | 2,170,000.00 USD | 550,450.00 USD | 308,060.00 USD |
| `1D` | `2137.50` | 380,410,000.00 USD | 0.00 USD | 380,410,000.00 USD | 0.00 USD | 278,410.00 USD | 0.00 USD |
| `7D` | `2137.50` | 699,150,000.00 USD | 0.00 USD | 699,150,000.00 USD | 1,040,000.00 USD | 880,790.00 USD | 43,560.00 USD |
| `7D` | `2140.80` | 697,190,000.00 USD | 0.00 USD | 697,190,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD |
| `7D` | `2144.10` | 693,250,000.00 USD | 0.00 USD | 693,250,000.00 USD | 449,020.00 USD | 1,130,000.00 USD | 268,500.00 USD |
| `7D` | `2147.40` | 691,400,000.00 USD | 0.00 USD | 691,400,000.00 USD | 657,710.00 USD | 421,320.00 USD | 0.00 USD |
| `7D` | `2150.70` | 690,330,000.00 USD | 0.00 USD | 690,330,000.00 USD | 459,630.00 USD | 463,640.00 USD | 31,040.00 USD |
| `1D` | `2152.00` | 380,130,000.00 USD | 0.00 USD | 380,130,000.00 USD | 208,250.00 USD | 440,530.00 USD | 0.00 USD |
| `7D` | `2154.00` | 689,370,000.00 USD | 0.00 USD | 689,370,000.00 USD | 128,430.00 USD | 331,520.00 USD | 32,590.00 USD |
| `1D` | `2154.90` | 379,490,000.00 USD | 0.00 USD | 379,490,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD |
| `7D` | `2157.30` | 688,880,000.00 USD | 0.00 USD | 688,880,000.00 USD | 388,210.00 USD | 1,030,000.00 USD | 1,080,000.00 USD |
| `1D` | `2157.80` | 378,090,000.00 USD | 0.00 USD | 378,090,000.00 USD | 0.00 USD | 0.00 USD | 37,580.00 USD |
| `7D` | `2160.60` | 686,380,000.00 USD | 0.00 USD | 686,380,000.00 USD | 646,940.00 USD | 1,900,000.00 USD | 1,990,000.00 USD |
| `1D` | `2160.70` | 378,050,000.00 USD | 0.00 USD | 378,050,000.00 USD | 0.00 USD | 2,290,000.00 USD | 71,920.00 USD |
| `1D` | `2163.60` | 375,690,000.00 USD | 0.00 USD | 375,690,000.00 USD | 0.00 USD | 999,490.00 USD | 28,620.00 USD |
| `7D` | `2163.90` | 681,840,000.00 USD | 0.00 USD | 681,840,000.00 USD | 566,120.00 USD | 3,280,000.00 USD | 1,290,000.00 USD |
| `1D` | `2166.50` | 374,660,000.00 USD | 0.00 USD | 374,660,000.00 USD | 1,690,000.00 USD | 341,240.00 USD | 1,130,000.00 USD |
| `7D` | `2167.20` | 676,690,000.00 USD | 0.00 USD | 676,690,000.00 USD | 25,540.00 USD | 3,620,000.00 USD | 50,240.00 USD |
| `1D` | `2169.40` | 371,500,000.00 USD | 0.00 USD | 371,500,000.00 USD | 6,770,000.00 USD | 4,810,000.00 USD | 2,130,000.00 USD |
| `7D` | `2170.50` | 673,000,000.00 USD | 0.00 USD | 673,000,000.00 USD | 3,500,000.00 USD | 3,730,000.00 USD | 5,230,000.00 USD |
| `7D` | `2173.80` | 660,530,000.00 USD | 0.00 USD | 660,530,000.00 USD | 4,110,000.00 USD | 363,040.00 USD | 1,010,000.00 USD |
| `1D` | `2175.20` | 357,800,000.00 USD | 0.00 USD | 357,800,000.00 USD | 345,940.00 USD | 301,420.00 USD | 33,400.00 USD |
| `7D` | `2177.10` | 655,050,000.00 USD | 0.00 USD | 655,050,000.00 USD | 0.00 USD | 0.00 USD | 1,320,000.00 USD |
| `1D` | `2178.10` | 357,120,000.00 USD | 0.00 USD | 357,120,000.00 USD | 0.00 USD | 1,400,000.00 USD | 49,860.00 USD |
| `7D` | `2180.40` | 653,730,000.00 USD | 0.00 USD | 653,730,000.00 USD | 0.00 USD | 373,740.00 USD | 176,950.00 USD |
| `1D` | `2181.00` | 355,670,000.00 USD | 0.00 USD | 355,670,000.00 USD | 2,080,000.00 USD | 478,110.00 USD | 1,370,000.00 USD |
| `7D` | `2183.70` | 653,180,000.00 USD | 0.00 USD | 653,180,000.00 USD | 0.00 USD | 1,310,000.00 USD | 2,550,000.00 USD |
| `1D` | `2183.90` | 351,740,000.00 USD | 0.00 USD | 351,740,000.00 USD | 1,350,000.00 USD | 509,320.00 USD | 13,020.00 USD |
| `1D` | `2186.80` | 349,870,000.00 USD | 0.00 USD | 349,870,000.00 USD | 0.00 USD | 1,450,000.00 USD | 1,790,000.00 USD |
| `7D` | `2187.00` | 649,330,000.00 USD | 0.00 USD | 649,330,000.00 USD | 556,600.00 USD | 0.00 USD | 54,020.00 USD |
| `1D` | `2189.70` | 346,620,000.00 USD | 0.00 USD | 346,620,000.00 USD | 0.00 USD | 0.00 USD | 693,960.00 USD |
| `7D` | `2190.30` | 648,720,000.00 USD | 0.00 USD | 648,720,000.00 USD | 2,730,000.00 USD | 0.00 USD | 4,200,000.00 USD |
| `1D` | `2192.60` | 345,930,000.00 USD | 0.00 USD | 345,930,000.00 USD | 605,210.00 USD | 222,200.00 USD | 109,400.00 USD |
| `1D` | `2195.50` | 344,990,000.00 USD | 0.00 USD | 344,990,000.00 USD | 0.00 USD | 881,070.00 USD | 1,890,000.00 USD |
| `7D` | `2196.90` | 641,790,000.00 USD | 0.00 USD | 641,790,000.00 USD | 2,580,000.00 USD | 474,090.00 USD | 2,040,000.00 USD |
| `1D` | `2198.40` | 342,220,000.00 USD | 0.00 USD | 342,220,000.00 USD | 416,500.00 USD | 149,110.00 USD | 50,830.00 USD |
| `7D` | `2200.20` | 636,690,000.00 USD | 0.00 USD | 636,690,000.00 USD | 3,000,000.00 USD | 5,080,000.00 USD | 3,200,000.00 USD |
| `1D` | `2201.30` | 341,610,000.00 USD | 0.00 USD | 341,610,000.00 USD | 1,690,000.00 USD | 4,250,000.00 USD | 1,500,000.00 USD |
| `7D` | `2203.50` | 625,420,000.00 USD | 0.00 USD | 625,420,000.00 USD | 3,650,000.00 USD | 1,710,000.00 USD | 3,750,000.00 USD |
| `1D` | `2204.20` | 334,170,000.00 USD | 0.00 USD | 334,170,000.00 USD | 2,130,000.00 USD | 314,310.00 USD | 867,420.00 USD |
| `7D` | `2206.80` | 616,310,000.00 USD | 0.00 USD | 616,310,000.00 USD | 6,920,000.00 USD | 9,430,000.00 USD | 4,020,000.00 USD |
| `1D` | `2207.10` | 330,850,000.00 USD | 0.00 USD | 330,850,000.00 USD | 2,210,000.00 USD | 10,880,000.00 USD | 2,030,000.00 USD |
| `1D` | `2210.00` | 315,730,000.00 USD | 0.00 USD | 315,730,000.00 USD | 3,190,000.00 USD | 3,380,000.00 USD | 2,690,000.00 USD |
| `7D` | `2210.10` | 595,940,000.00 USD | 0.00 USD | 595,940,000.00 USD | 12,800,000.00 USD | 20,410,000.00 USD | 6,470,000.00 USD |
| `1D` | `2212.90` | 306,470,000.00 USD | 0.00 USD | 306,470,000.00 USD | 9,500,000.00 USD | 8,670,000.00 USD | 4,390,000.00 USD |
| `7D` | `2213.40` | 556,260,000.00 USD | 0.00 USD | 556,260,000.00 USD | 10,920,000.00 USD | 14,600,000.00 USD | 19,980,000.00 USD |
| `1D` | `2215.80` | 283,910,000.00 USD | 0.00 USD | 283,910,000.00 USD | 18,430,000.00 USD | 9,030,000.00 USD | 10,170,000.00 USD |
| `7D` | `2216.70` | 510,760,000.00 USD | 0.00 USD | 510,760,000.00 USD | 25,210,000.00 USD | 17,030,000.00 USD | 9,390,000.00 USD |
| `1D` | `2218.70` | 246,280,000.00 USD | 0.00 USD | 246,280,000.00 USD | 6,790,000.00 USD | 7,780,000.00 USD | 1,880,000.00 USD |
| `7D` | `2220.00` | 459,130,000.00 USD | 0.00 USD | 459,130,000.00 USD | 24,310,000.00 USD | 12,300,000.00 USD | 12,760,000.00 USD |
| `1D` | `2221.60` | 229,840,000.00 USD | 0.00 USD | 229,840,000.00 USD | 6,200,000.00 USD | 12,240,000.00 USD | 1,340,000.00 USD |
| `7D` | `2223.30` | 409,770,000.00 USD | 0.00 USD | 409,770,000.00 USD | 10,150,000.00 USD | 8,220,000.00 USD | 11,910,000.00 USD |
| `1D` | `2224.50` | 210,060,000.00 USD | 0.00 USD | 210,060,000.00 USD | 9,730,000.00 USD | 5,030,000.00 USD | 5,660,000.00 USD |
| `7D` | `2226.60` | 379,490,000.00 USD | 0.00 USD | 379,490,000.00 USD | 12,840,000.00 USD | 11,030,000.00 USD | 9,960,000.00 USD |
| `1D` | `2227.40` | 189,640,000.00 USD | 0.00 USD | 189,640,000.00 USD | 5,940,000.00 USD | 13,200,000.00 USD | 5,610,000.00 USD |
| `7D` | `2229.90` | 345,660,000.00 USD | 0.00 USD | 345,660,000.00 USD | 12,730,000.00 USD | 11,790,000.00 USD | 25,750,000.00 USD |
| `1D` | `2230.30` | 164,890,000.00 USD | 0.00 USD | 164,890,000.00 USD | 6,830,000.00 USD | 8,320,000.00 USD | 2,410,000.00 USD |
| `1D` | `2233.20` | 147,320,000.00 USD | 0.00 USD | 147,320,000.00 USD | 5,060,000.00 USD | 4,220,000.00 USD | 8,040,000.00 USD |
| `7D` | `2233.20` | 295,390,000.00 USD | 0.00 USD | 295,390,000.00 USD | 16,600,000.00 USD | 24,290,000.00 USD | 10,420,000.00 USD |
| `1D` | `2236.10` | 130,000,000.00 USD | 0.00 USD | 130,000,000.00 USD | 22,420,000.00 USD | 0.00 USD | 10,790,000.00 USD |
| `7D` | `2236.50` | 244,070,000.00 USD | 0.00 USD | 244,070,000.00 USD | 16,050,000.00 USD | 7,430,000.00 USD | 27,830,000.00 USD |
| `1D` | `2239.00` | 96,790,000.00 USD | 0.00 USD | 96,790,000.00 USD | 17,940,000.00 USD | 5,930,000.00 USD | 9,420,000.00 USD |
| `7D` | `2239.80` | 192,770,000.00 USD | 0.00 USD | 192,770,000.00 USD | 15,710,000.00 USD | 6,600,000.00 USD | 13,750,000.00 USD |
| `1D` | `2241.90` | 63,500,000.00 USD | 0.00 USD | 63,500,000.00 USD | 619,130.00 USD | 760,920.00 USD | 5,370,000.00 USD |
| `7D` | `2243.10` | 156,710,000.00 USD | 0.00 USD | 156,710,000.00 USD | 22,920,000.00 USD | 0.00 USD | 18,320,000.00 USD |
| `1D` | `2244.80` | 56,750,000.00 USD | 0.00 USD | 56,750,000.00 USD | 3,850,000.00 USD | 4,700,000.00 USD | 463,790.00 USD |
| `7D` | `2246.40` | 115,460,000.00 USD | 0.00 USD | 115,460,000.00 USD | 14,340,000.00 USD | 0.00 USD | 13,920,000.00 USD |
| `1D` | `2247.70` | 47,740,000.00 USD | 0.00 USD | 47,740,000.00 USD | 12,800,000.00 USD | 0.00 USD | 7,080,000.00 USD |
| `7D` | `2249.70` | 87,200,000.00 USD | 0.00 USD | 87,200,000.00 USD | 18,000,000.00 USD | 0.00 USD | 12,820,000.00 USD |
| `1D` | `2250.60` | 27,860,000.00 USD | 0.00 USD | 27,860,000.00 USD | 4,190,000.00 USD | 1,910,000.00 USD | 3,960,000.00 USD |
| `7D` | `2253.00` | 56,380,000.00 USD | 0.00 USD | 56,380,000.00 USD | 26,890,000.00 USD | 0.00 USD | 12,040,000.00 USD |
| `1D` | `2253.50` | 17,790,000.00 USD | 0.00 USD | 17,790,000.00 USD | 5,410,000.00 USD | 4,440,000.00 USD | 4,550,000.00 USD |
| `7D` | `2256.30` | 17,450,000.00 USD | 0.00 USD | 17,450,000.00 USD | 17,450,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2256.40` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 0.00 USD |
| `1D` | `2259.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2259.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2259.60` | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 10,940,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2262.20` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 2,420,000.00 USD | 0.00 USD | 156,010.00 USD |
| `1D` | `2265.10` | 12,410,000.00 USD | 12,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,830,000.00 USD |
| `1D` | `2268.00` | 16,850,000.00 USD | 16,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,440,000.00 USD |
| `1D` | `2273.80` | 17,070,000.00 USD | 17,070,000.00 USD | 0.00 USD | 220,250.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2276.70` | 19,100,000.00 USD | 19,100,000.00 USD | 0.00 USD | 1,370,000.00 USD | 555,110.00 USD | 114,460.00 USD |
| `7D` | `2279.40` | 27,940,000.00 USD | 27,940,000.00 USD | 0.00 USD | 0.00 USD | 17,000,000.00 USD | 0.00 USD |
| `1D` | `2279.60` | 52,670,000.00 USD | 52,670,000.00 USD | 0.00 USD | 23,020,000.00 USD | 6,030,000.00 USD | 4,520,000.00 USD |
| `1D` | `2282.50` | 154,360,000.00 USD | 154,360,000.00 USD | 0.00 USD | 51,100,000.00 USD | 39,620,000.00 USD | 10,980,000.00 USD |
| `7D` | `2282.70` | 128,630,000.00 USD | 128,630,000.00 USD | 0.00 USD | 0.00 USD | 87,090,000.00 USD | 13,610,000.00 USD |
| `1D` | `2285.40` | 166,560,000.00 USD | 166,560,000.00 USD | 0.00 USD | 7,830,000.00 USD | 3,050,000.00 USD | 1,320,000.00 USD |
| `7D` | `2286.00` | 138,040,000.00 USD | 138,040,000.00 USD | 0.00 USD | 0.00 USD | 9,400,000.00 USD | 0.00 USD |
| `1D` | `2288.30` | 167,460,000.00 USD | 167,460,000.00 USD | 0.00 USD | 0.00 USD | 760,920.00 USD | 133,600.00 USD |
| `7D` | `2289.30` | 143,320,000.00 USD | 143,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,280,000.00 USD |
| `1D` | `2291.20` | 176,490,000.00 USD | 176,490,000.00 USD | 0.00 USD | 0.00 USD | 8,840,000.00 USD | 199,420.00 USD |
| `1D` | `2294.10` | 190,360,000.00 USD | 190,360,000.00 USD | 0.00 USD | 8,310,000.00 USD | 0.00 USD | 5,560,000.00 USD |
| `7D` | `2295.90` | 158,000,000.00 USD | 158,000,000.00 USD | 0.00 USD | 6,580,000.00 USD | 2,380,000.00 USD | 5,720,000.00 USD |
| `1D` | `2297.00` | 204,380,000.00 USD | 204,380,000.00 USD | 0.00 USD | 5,410,000.00 USD | 8,350,000.00 USD | 253,130.00 USD |
| `7D` | `2299.20` | 186,420,000.00 USD | 186,420,000.00 USD | 0.00 USD | 11,730,000.00 USD | 11,130,000.00 USD | 5,560,000.00 USD |
| `1D` | `2299.90` | 219,750,000.00 USD | 219,750,000.00 USD | 0.00 USD | 0.00 USD | 7,970,000.00 USD | 7,390,000.00 USD |
| `7D` | `2302.50` | 233,530,000.00 USD | 233,530,000.00 USD | 0.00 USD | 23,020,000.00 USD | 7,250,000.00 USD | 16,850,000.00 USD |
| `1D` | `2302.80` | 240,570,000.00 USD | 240,570,000.00 USD | 0.00 USD | 15,230,000.00 USD | 682,490.00 USD | 4,910,000.00 USD |
| `1D` | `2305.70` | 270,200,000.00 USD | 270,200,000.00 USD | 0.00 USD | 10,050,000.00 USD | 14,890,000.00 USD | 4,690,000.00 USD |
| `7D` | `2305.80` | 254,340,000.00 USD | 254,340,000.00 USD | 0.00 USD | 2,980,000.00 USD | 8,820,000.00 USD | 9,000,000.00 USD |
| `1D` | `2308.60` | 274,960,000.00 USD | 274,960,000.00 USD | 0.00 USD | 2,420,000.00 USD | 2,340,000.00 USD | 0.00 USD |
| `7D` | `2309.10` | 258,110,000.00 USD | 258,110,000.00 USD | 0.00 USD | 732,090.00 USD | 930,630.00 USD | 2,110,000.00 USD |
| `1D` | `2311.50` | 284,600,000.00 USD | 284,600,000.00 USD | 0.00 USD | 691,870.00 USD | 1,260,000.00 USD | 7,690,000.00 USD |
| `7D` | `2312.40` | 276,250,000.00 USD | 276,250,000.00 USD | 0.00 USD | 7,270,000.00 USD | 0.00 USD | 10,870,000.00 USD |
| `1D` | `2314.40` | 298,930,000.00 USD | 298,930,000.00 USD | 0.00 USD | 0.00 USD | 14,100,000.00 USD | 231,520.00 USD |
| `7D` | `2315.70` | 283,820,000.00 USD | 283,820,000.00 USD | 0.00 USD | 0.00 USD | 7,460,000.00 USD | 117,510.00 USD |
| `1D` | `2317.30` | 327,480,000.00 USD | 327,480,000.00 USD | 0.00 USD | 10,230,000.00 USD | 10,470,000.00 USD | 7,850,000.00 USD |
| `7D` | `2319.00` | 295,010,000.00 USD | 295,010,000.00 USD | 0.00 USD | 1,020,000.00 USD | 4,550,000.00 USD | 5,620,000.00 USD |
| `1D` | `2320.20` | 343,590,000.00 USD | 343,590,000.00 USD | 0.00 USD | 6,580,000.00 USD | 9,360,000.00 USD | 173,650.00 USD |
| `7D` | `2322.30` | 312,170,000.00 USD | 312,170,000.00 USD | 0.00 USD | 1,110,000.00 USD | 15,930,000.00 USD | 108,040.00 USD |
| `1D` | `2323.10` | 358,160,000.00 USD | 358,160,000.00 USD | 0.00 USD | 572,970.00 USD | 10,410,000.00 USD | 3,590,000.00 USD |
| `7D` | `2325.60` | 332,820,000.00 USD | 332,820,000.00 USD | 0.00 USD | 9,720,000.00 USD | 2,540,000.00 USD | 8,390,000.00 USD |
| `1D` | `2326.00` | 369,850,000.00 USD | 369,850,000.00 USD | 0.00 USD | 479,120.00 USD | 5,550,000.00 USD | 5,660,000.00 USD |
| `1D` | `2328.90` | 376,820,000.00 USD | 376,820,000.00 USD | 0.00 USD | 5,690,000.00 USD | 884,940.00 USD | 402,280.00 USD |
| `7D` | `2328.90` | 344,640,000.00 USD | 344,640,000.00 USD | 0.00 USD | 3,860,000.00 USD | 0.00 USD | 7,960,000.00 USD |
| `1D` | `2331.80` | 393,120,000.00 USD | 393,120,000.00 USD | 0.00 USD | 15,910,000.00 USD | 251,940.00 USD | 126,990.00 USD |
| `7D` | `2332.20` | 373,880,000.00 USD | 373,880,000.00 USD | 0.00 USD | 29,230,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2334.70` | 416,680,000.00 USD | 416,680,000.00 USD | 0.00 USD | 13,410,000.00 USD | 2,960,000.00 USD | 7,200,000.00 USD |
| `7D` | `2335.50` | 431,890,000.00 USD | 431,890,000.00 USD | 0.00 USD | 28,990,000.00 USD | 18,420,000.00 USD | 10,600,000.00 USD |
| `1D` | `2337.60` | 430,560,000.00 USD | 430,560,000.00 USD | 0.00 USD | 9,880,000.00 USD | 407,920.00 USD | 3,600,000.00 USD |
| `7D` | `2338.80` | 449,760,000.00 USD | 449,760,000.00 USD | 0.00 USD | 9,570,000.00 USD | 0.00 USD | 8,310,000.00 USD |
| `1D` | `2340.50` | 454,460,000.00 USD | 454,460,000.00 USD | 0.00 USD | 8,010,000.00 USD | 5,100,000.00 USD | 10,780,000.00 USD |
| `7D` | `2342.10` | 489,860,000.00 USD | 489,860,000.00 USD | 0.00 USD | 4,720,000.00 USD | 21,390,000.00 USD | 14,000,000.00 USD |
| `1D` | `2343.40` | 469,090,000.00 USD | 469,090,000.00 USD | 0.00 USD | 2,060,000.00 USD | 5,580,000.00 USD | 7,000,000.00 USD |
| `7D` | `2345.40` | 511,230,000.00 USD | 511,230,000.00 USD | 0.00 USD | 1,350,000.00 USD | 13,990,000.00 USD | 6,020,000.00 USD |
| `1D` | `2346.30` | 482,000,000.00 USD | 482,000,000.00 USD | 0.00 USD | 4,950,000.00 USD | 1,940,000.00 USD | 6,020,000.00 USD |
| `7D` | `2348.70` | 549,130,000.00 USD | 549,130,000.00 USD | 0.00 USD | 847,620.00 USD | 9,500,000.00 USD | 27,550,000.00 USD |
| `1D` | `2349.20` | 508,060,000.00 USD | 508,060,000.00 USD | 0.00 USD | 13,480,000.00 USD | 6,150,000.00 USD | 6,430,000.00 USD |
| `7D` | `2352.00` | 585,750,000.00 USD | 585,750,000.00 USD | 0.00 USD | 2,930,000.00 USD | 23,060,000.00 USD | 10,630,000.00 USD |
| `1D` | `2352.10` | 542,570,000.00 USD | 542,570,000.00 USD | 0.00 USD | 24,370,000.00 USD | 4,230,000.00 USD | 5,920,000.00 USD |
| `1D` | `2355.00` | 564,350,000.00 USD | 564,350,000.00 USD | 0.00 USD | 1,010,000.00 USD | 19,500,000.00 USD | 1,280,000.00 USD |
| `7D` | `2355.30` | 640,340,000.00 USD | 640,340,000.00 USD | 0.00 USD | 16,520,000.00 USD | 36,690,000.00 USD | 1,380,000.00 USD |
| `1D` | `2357.90` | 575,030,000.00 USD | 575,030,000.00 USD | 0.00 USD | 2,890,000.00 USD | 4,290,000.00 USD | 3,500,000.00 USD |
| `7D` | `2358.60` | 652,480,000.00 USD | 652,480,000.00 USD | 0.00 USD | 7,110,000.00 USD | 512,220.00 USD | 4,510,000.00 USD |
| `1D` | `2360.80` | 596,270,000.00 USD | 596,270,000.00 USD | 0.00 USD | 10,720,000.00 USD | 5,400,000.00 USD | 5,130,000.00 USD |
| `7D` | `2361.90` | 659,600,000.00 USD | 659,600,000.00 USD | 0.00 USD | 3,150,000.00 USD | 3,800,000.00 USD | 176,950.00 USD |
| `1D` | `2363.70` | 622,130,000.00 USD | 622,130,000.00 USD | 0.00 USD | 7,900,000.00 USD | 9,120,000.00 USD | 8,830,000.00 USD |
| `7D` | `2365.20` | 677,500,000.00 USD | 677,500,000.00 USD | 0.00 USD | 8,440,000.00 USD | 0.00 USD | 9,460,000.00 USD |
| `1D` | `2366.60` | 627,830,000.00 USD | 627,830,000.00 USD | 0.00 USD | 3,560,000.00 USD | 509,320.00 USD | 1,620,000.00 USD |
| `7D` | `2368.50` | 690,570,000.00 USD | 690,570,000.00 USD | 0.00 USD | 10,830,000.00 USD | 1,780,000.00 USD | 458,400.00 USD |
| `1D` | `2369.50` | 654,320,000.00 USD | 654,320,000.00 USD | 0.00 USD | 13,850,000.00 USD | 7,720,000.00 USD | 4,920,000.00 USD |
| `7D` | `2371.80` | 771,510,000.00 USD | 771,510,000.00 USD | 0.00 USD | 26,000,000.00 USD | 0.00 USD | 54,940,000.00 USD |
| `1D` | `2372.40` | 691,850,000.00 USD | 691,850,000.00 USD | 0.00 USD | 14,410,000.00 USD | 10,690,000.00 USD | 12,430,000.00 USD |
| `7D` | `2375.10` | 798,450,000.00 USD | 798,450,000.00 USD | 0.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD |
| `1D` | `2375.30` | 713,370,000.00 USD | 713,370,000.00 USD | 0.00 USD | 14,210,000.00 USD | 3,650,000.00 USD | 3,660,000.00 USD |
| `1D` | `2378.20` | 738,590,000.00 USD | 738,590,000.00 USD | 0.00 USD | 5,350,000.00 USD | 7,910,000.00 USD | 11,950,000.00 USD |
| `7D` | `2378.40` | 843,870,000.00 USD | 843,870,000.00 USD | 0.00 USD | 11,800,000.00 USD | 7,950,000.00 USD | 25,670,000.00 USD |
| `1D` | `2381.10` | 787,980,000.00 USD | 787,980,000.00 USD | 0.00 USD | 16,200,000.00 USD | 13,170,000.00 USD | 20,030,000.00 USD |
| `7D` | `2381.70` | 883,660,000.00 USD | 883,660,000.00 USD | 0.00 USD | 8,510,000.00 USD | 6,750,000.00 USD | 24,530,000.00 USD |
| `1D` | `2384.00` | 832,030,000.00 USD | 832,030,000.00 USD | 0.00 USD | 17,870,000.00 USD | 15,110,000.00 USD | 11,070,000.00 USD |
| `7D` | `2385.00` | 985,370,000.00 USD | 985,370,000.00 USD | 0.00 USD | 18,550,000.00 USD | 36,910,000.00 USD | 46,260,000.00 USD |
| `1D` | `2386.90` | 867,740,000.00 USD | 867,740,000.00 USD | 0.00 USD | 13,540,000.00 USD | 11,770,000.00 USD | 10,400,000.00 USD |
| `7D` | `2388.30` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 0.00 USD | 5,290,000.00 USD | 38,070,000.00 USD | 44,510,000.00 USD |
| `1D` | `2389.80` | 893,440,000.00 USD | 893,440,000.00 USD | 0.00 USD | 10,230,000.00 USD | 9,340,000.00 USD | 6,130,000.00 USD |
| `7D` | `2391.60` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 8,560,000.00 USD | 52,080,000.00 USD | 40,380,000.00 USD |
| `1D` | `2392.70` | 911,490,000.00 USD | 911,490,000.00 USD | 0.00 USD | 5,770,000.00 USD | 4,950,000.00 USD | 7,340,000.00 USD |
| `7D` | `2394.90` | 1,300,000,000.00 USD | 1,300,000,000.00 USD | 0.00 USD | 57,450,000.00 USD | 32,260,000.00 USD | 37,090,000.00 USD |
| `1D` | `2395.60` | 926,980,000.00 USD | 926,980,000.00 USD | 0.00 USD | 5,140,000.00 USD | 6,720,000.00 USD | 3,630,000.00 USD |
| `7D` | `2398.20` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 42,820,000.00 USD | 38,210,000.00 USD | 29,190,000.00 USD |
| `1D` | `2398.50` | 946,650,000.00 USD | 946,650,000.00 USD | 0.00 USD | 5,800,000.00 USD | 6,760,000.00 USD | 7,120,000.00 USD |
| `1D` | `2401.40` | 971,600,000.00 USD | 971,600,000.00 USD | 0.00 USD | 8,280,000.00 USD | 7,500,000.00 USD | 9,170,000.00 USD |
| `7D` | `2401.50` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 0.00 USD | 51,970,000.00 USD | 26,780,000.00 USD | 29,090,000.00 USD |
| `1D` | `2404.30` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 0.00 USD | 10,010,000.00 USD | 11,060,000.00 USD | 8,510,000.00 USD |
| `7D` | `2404.80` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 0.00 USD | 50,800,000.00 USD | 32,200,000.00 USD | 24,110,000.00 USD |
| `1D` | `2407.20` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 0.00 USD | 15,160,000.00 USD | 9,260,000.00 USD | 7,920,000.00 USD |
| `7D` | `2408.10` | 1,720,000,000.00 USD | 1,720,000,000.00 USD | 0.00 USD | 34,390,000.00 USD | 31,420,000.00 USD | 25,030,000.00 USD |
| `1D` | `2410.10` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 7,660,000.00 USD | 7,700,000.00 USD | 9,120,000.00 USD |
| `7D` | `2411.40` | 1,800,000,000.00 USD | 1,800,000,000.00 USD | 0.00 USD | 19,200,000.00 USD | 32,580,000.00 USD | 27,660,000.00 USD |
| `1D` | `2413.00` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 0.00 USD | 8,270,000.00 USD | 5,470,000.00 USD | 3,790,000.00 USD |
| `7D` | `2414.70` | 1,870,000,000.00 USD | 1,870,000,000.00 USD | 0.00 USD | 24,010,000.00 USD | 21,950,000.00 USD | 23,130,000.00 USD |
| `1D` | `2415.90` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 3,710,000.00 USD | 2,920,000.00 USD | 3,620,000.00 USD |
| `7D` | `2418.00` | 1,940,000,000.00 USD | 1,940,000,000.00 USD | 0.00 USD | 34,060,000.00 USD | 15,260,000.00 USD | 24,610,000.00 USD |
| `1D` | `2418.80` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 4,240,000.00 USD | 2,710,000.00 USD | 3,900,000.00 USD |
| `7D` | `2421.30` | 2,010,000,000.00 USD | 2,010,000,000.00 USD | 0.00 USD | 25,700,000.00 USD | 27,890,000.00 USD | 21,590,000.00 USD |
| `1D` | `2421.70` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 6,390,000.00 USD | 6,200,000.00 USD | 6,250,000.00 USD |
| `1D` | `2424.60` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 1,790,000.00 USD | 2,770,000.00 USD | 1,020,000.00 USD |
| `7D` | `2424.60` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 0.00 USD | 24,180,000.00 USD | 35,050,000.00 USD | 34,520,000.00 USD |
| `1D` | `2427.50` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 731,900.00 USD | 124,100.00 USD | 601,200.00 USD |
| `7D` | `2427.90` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 0.00 USD | 25,200,000.00 USD | 18,380,000.00 USD | 26,460,000.00 USD |
| `1D` | `2430.40` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 1,640,000.00 USD | 1,770,000.00 USD | 1,230,000.00 USD |
| `7D` | `2431.20` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 0.00 USD | 10,380,000.00 USD | 17,060,000.00 USD | 9,300,000.00 USD |
| `1D` | `2433.30` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 2,160,000.00 USD | 2,160,000.00 USD | 1,220,000.00 USD |
| `7D` | `2434.50` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 0.00 USD | 27,390,000.00 USD | 21,570,000.00 USD | 11,160,000.00 USD |
| `1D` | `2436.20` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 2,340,000.00 USD | 475,290.00 USD | 579,580.00 USD |
| `7D` | `2437.80` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 0.00 USD | 12,000,000.00 USD | 12,820,000.00 USD | 5,470,000.00 USD |
| `1D` | `2439.10` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 304,760.00 USD | 641,280.00 USD | 484,910.00 USD |
| `7D` | `2441.10` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 0.00 USD | 15,080,000.00 USD | 8,120,000.00 USD | 10,680,000.00 USD |
| `1D` | `2442.00` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 2,360,000.00 USD | 2,020,000.00 USD | 735,530.00 USD |
| `7D` | `2444.40` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 0.00 USD | 8,860,000.00 USD | 15,160,000.00 USD | 14,000,000.00 USD |
| `1D` | `2444.90` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 544,880.00 USD | 1,480,000.00 USD |
| `7D` | `2447.70` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 0.00 USD | 11,650,000.00 USD | 8,510,000.00 USD | 17,330,000.00 USD |
| `1D` | `2447.80` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 687,490.00 USD | 330,760.00 USD | 1,530,000.00 USD |
| `1D` | `2450.70` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 2,550,000.00 USD | 1,470,000.00 USD | 3,400,000.00 USD |
| `7D` | `2451.00` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 0.00 USD | 16,710,000.00 USD | 14,100,000.00 USD | 16,480,000.00 USD |
| `1D` | `2453.60` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 4,790,000.00 USD | 4,000,000.00 USD | 3,570,000.00 USD |
| `7D` | `2454.30` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 0.00 USD | 4,620,000.00 USD | 4,930,000.00 USD | 3,880,000.00 USD |
| `1D` | `2456.50` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 1,060,000.00 USD | 2,650,000.00 USD | 2,020,000.00 USD |
| `7D` | `2457.60` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 0.00 USD | 15,150,000.00 USD | 12,540,000.00 USD | 12,600,000.00 USD |
| `1D` | `2459.40` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 1,900,000.00 USD | 1,190,000.00 USD | 366,800.00 USD |
| `7D` | `2460.90` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 0.00 USD | 5,580,000.00 USD | 8,670,000.00 USD | 6,870,000.00 USD |
| `1D` | `2462.30` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 490,260.00 USD | 1,620,000.00 USD |
| `7D` | `2464.20` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 0.00 USD | 8,720,000.00 USD | 7,700,000.00 USD | 4,700,000.00 USD |
| `1D` | `2465.20` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 83,300.00 USD | 176,210.00 USD | 0.00 USD |
| `7D` | `2467.50` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 0.00 USD | 4,540,000.00 USD | 3,710,000.00 USD | 586,780.00 USD |
| `1D` | `2468.10` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 1,250,000.00 USD | 0.00 USD |
| `7D` | `2470.80` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 0.00 USD | 3,960,000.00 USD | 2,290,000.00 USD | 522,210.00 USD |
| `1D` | `2471.00` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 391,890.00 USD |
| `7D` | `2474.10` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 0.00 USD | 5,230,000.00 USD | 2,920,000.00 USD | 2,400,000.00 USD |
| `1D` | `2476.80` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 943,590.00 USD | 40,210.00 USD |
| `7D` | `2477.40` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 0.00 USD | 1,660,000.00 USD | 4,420,000.00 USD | 718,840.00 USD |
| `1D` | `2479.70` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 26,700.00 USD | 0.00 USD |
| `7D` | `2480.70` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 0.00 USD | 2,110,000.00 USD | 4,170,000.00 USD | 540,990.00 USD |
| `1D` | `2482.60` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 677,540.00 USD | 136,500.00 USD | 451,780.00 USD |
| `7D` | `2484.00` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 0.00 USD | 1,210,000.00 USD | 1,390,000.00 USD | 1,440,000.00 USD |
| `1D` | `2485.50` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 865,140.00 USD | 1,330,000.00 USD | 0.00 USD |
| `7D` | `2487.30` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 0.00 USD | 325,140.00 USD | 262,280.00 USD | 0.00 USD |
| `1D` | `2488.40` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 866,230.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2490.60` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 0.00 USD | 2,910,000.00 USD | 2,540,000.00 USD | 279,750.00 USD |
| `1D` | `2491.30` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 138,370.00 USD | 0.00 USD | 13,360.00 USD |
| `7D` | `2493.90` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 0.00 USD | 1,660,000.00 USD | 1,790,000.00 USD | 3,940,000.00 USD |
| `1D` | `2494.20` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 178,560.00 USD | 14,300.00 USD |
| `7D` | `2497.20` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 0.00 USD | 2,940,000.00 USD | 5,270,000.00 USD | 8,250,000.00 USD |
| `7D` | `2500.50` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 0.00 USD | 1,110,000.00 USD | 2,280,000.00 USD | 1,130,000.00 USD |
| `7D` | `2503.80` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 0.00 USD | 63,860.00 USD | 1,480,000.00 USD | 125,600.00 USD |
| `1D` | `2505.80` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 338,980.00 USD | 717,780.00 USD |
| `7D` | `2507.10` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 0.00 USD | 4,340,000.00 USD | 3,090,000.00 USD | 3,180,000.00 USD |
| `7D` | `2510.40` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 0.00 USD | 2,290,000.00 USD | 1,270,000.00 USD | 0.00 USD |
| `1D` | `2511.60` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 242,080.00 USD | 88,880.00 USD | 28,160.00 USD |
| `7D` | `2513.70` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 0.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2517.00` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 0.00 USD | 97,050.00 USD | 189,640.00 USD | 815,620.00 USD |
| `1D` | `2517.40` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `1D` | `2520.30` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 80,610.00 USD | 121,470.00 USD | 52,590.00 USD |
| `7D` | `2520.30` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD |
| `1D` | `2523.20` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 563,140.00 USD | 537,030.00 USD | 568,070.00 USD |
| `7D` | `2523.60` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 0.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD |
| `1D` | `2526.10` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 808,950.00 USD | 362,000.00 USD | 53,680.00 USD |
| `7D` | `2526.90` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 0.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD |
| `1D` | `2529.00` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 641,110.00 USD | 965,400.00 USD | 464,460.00 USD |
| `7D` | `2530.20` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 0.00 USD | 2,800,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD |
| `1D` | `2531.90` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 474,040.00 USD | 534,600.00 USD | 7,120.00 USD |
| `7D` | `2533.50` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 0.00 USD | 3,530,000.00 USD | 1,850,000.00 USD | 2,030,000.00 USD |
| `1D` | `2534.80` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 405,580.00 USD | 62,630.00 USD | 919,610.00 USD |
| `7D` | `2536.80` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 0.00 USD | 3,720,000.00 USD | 3,450,000.00 USD | 3,530,000.00 USD |
| `1D` | `2537.70` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 2,580,000.00 USD | 926,330.00 USD | 1,620,000.00 USD |
| `7D` | `2540.10` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 0.00 USD | 4,150,000.00 USD | 3,220,000.00 USD | 1,580,000.00 USD |
| `1D` | `2540.60` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 1,180,000.00 USD | 1,100,000.00 USD | 808,470.00 USD |
| `7D` | `2543.40` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 0.00 USD | 4,150,000.00 USD | 2,520,000.00 USD | 2,480,000.00 USD |
| `1D` | `2543.50` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 1,510,000.00 USD | 1,100,000.00 USD | 233,890.00 USD |
| `1D` | `2546.40` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 1,780,000.00 USD | 1,410,000.00 USD | 571,260.00 USD |
| `7D` | `2546.70` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 0.00 USD | 1,450,000.00 USD | 1,090,000.00 USD | 2,290,000.00 USD |
| `1D` | `2549.30` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 1,020,000.00 USD | 803,170.00 USD | 1,470,000.00 USD |
| `7D` | `2550.00` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 0.00 USD | 4,320,000.00 USD | 3,550,000.00 USD | 3,720,000.00 USD |
| `1D` | `2552.20` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 1,730,000.00 USD | 914,630.00 USD | 396,670.00 USD |
| `7D` | `2553.30` | 2,730,000,000.00 USD | 2,730,000,000.00 USD | 0.00 USD | 2,820,000.00 USD | 788,360.00 USD | 2,600,000.00 USD |
| `1D` | `2555.10` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 996,760.00 USD | 221,720.00 USD | 417,580.00 USD |
| `7D` | `2556.60` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 0.00 USD | 2,760,000.00 USD | 283,560.00 USD | 6,500,000.00 USD |
| `1D` | `2558.00` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 736,590.00 USD | 502,170.00 USD | 811,030.00 USD |
| `7D` | `2559.90` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 0.00 USD | 5,720,000.00 USD | 2,130,000.00 USD | 1,390,000.00 USD |
| `1D` | `2560.50` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 1,830,000.00 USD | 1,080,000.00 USD | 1,160,000.00 USD |
| `7D` | `2563.20` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 0.00 USD | 1,430,000.00 USD | 2,900,000.00 USD | 1,290,000.00 USD |
| `7D` | `2566.50` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 0.00 USD | 1,860,000.00 USD | 1,830,000.00 USD | 3,300,000.00 USD |
| `7D` | `2569.80` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 0.00 USD | 125,250.00 USD | 341,900.00 USD | 1,190,000.00 USD |
| `7D` | `2573.10` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,790,000.00 USD |
| `7D` | `2576.40` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 2,400,000.00 USD | 930,280.00 USD | 1,640,000.00 USD |
| `7D` | `2579.70` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 0.00 USD | 2,750,000.00 USD | 1,780,000.00 USD | 1,960,000.00 USD |
| `7D` | `2583.00` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 0.00 USD | 1,730,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD |
| `7D` | `2586.30` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 0.00 USD | 1,480,000.00 USD | 2,030,000.00 USD | 2,570,000.00 USD |
| `7D` | `2589.60` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 0.00 USD | 3,310,000.00 USD | 631,590.00 USD | 2,150,000.00 USD |
| `7D` | `2592.90` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 0.00 USD | 2,370,000.00 USD | 1,280,000.00 USD | 1,580,000.00 USD |
| `7D` | `2596.20` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 0.00 USD | 794,750.00 USD | 620,840.00 USD | 1,490,000.00 USD |
| `7D` | `2599.50` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,530,000.00 USD | 2,810,000.00 USD |
| `7D` | `2602.80` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 1,680,000.00 USD | 1,260,000.00 USD | 1,690,000.00 USD |
| `7D` | `2606.10` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 1,850,000.00 USD | 1,560,000.00 USD | 772,800.00 USD |
| `7D` | `2609.40` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD |
| `7D` | `2612.70` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 1,010,000.00 USD | 643,740.00 USD | 43,560.00 USD |
| `7D` | `2616.00` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD |
| `7D` | `2619.30` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 449,020.00 USD | 323,810.00 USD | 268,500.00 USD |
| `7D` | `2622.60` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 631,440.00 USD | 1,220,000.00 USD | 0.00 USD |
| `7D` | `2625.90` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 485,890.00 USD | 474,490.00 USD | 0.00 USD |
| `7D` | `2629.20` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 0.00 USD | 20,460.00 USD | 31,040.00 USD |
| `7D` | `2632.40` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 0.00 USD | 301,060.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `28.99B` | Total OI Tokens: `12,859,091.6 ETH`
  * 1h OI Change: `+0.50%` | 4h OI Change: `-3.19%` | 24h OI Change: `-3.01%`
  * Exchange Breakdown: Binance=`8.47B` | Bybit=`2.09B` | OKX=`1.75B` | Hyperliquid=`2.49B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `23.40K` | Last 24h: `2.27M` | Last 3d: `7.66M` | Last 7d: `13.85M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0001%` | **USDT OKX** | `0.0039%` |
| **USDT Bybit** | `-0.0042%` | **USDT KuCoin** | `-0.0024%` |
| **USDT MEXC** | `0.0001%` | **USDT BingX** | `0.0043%` |
| **USDT Gate** | `0.0011%` | **USDT Bitget** | `0.0031%` |
| **CoinM Binance** | `0.0046%` | **CoinM OKX** | `-0.0012%` |

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
| `4H` | `ETH` | `47.23%` | `52.77%` | `0.90` | 28,580,000,000.00 USD |
| `4H` | `Binance` | `45.51%` | `54.49%` | `0.84` | 7,940,000,000.00 USD |
| `4H` | `OKX` | `46.28%` | `53.72%` | `0.86` | 3,500,000,000.00 USD |
| `4H` | `Bybit` | `44.88%` | `55.12%` | `0.81` | 3,470,000,000.00 USD |
| `4H` | `KuCoin` | `49.85%` | `50.15%` | `0.99` | 123,620,000.00 USD |
| `4H` | `Gate` | `51.21%` | `48.79%` | `1.05` | 2,280,000,000.00 USD |
| `4H` | `Bitget` | `52.34%` | `47.66%` | `1.10` | 1,260,000,000.00 USD |
| `4H` | `BingX` | `51.28%` | `48.72%` | `1.05` | 374,540,000.00 USD |
| `4H` | `MEXC` | `48.31%` | `51.69%` | `0.93` | 1,270,000,000.00 USD |
| `4H` | `Bitunix` | `49.9%` | `50.1%` | `1.00` | 1,240,000,000.00 USD |
| `4H` | `Hyperliquid` | `44.26%` | `55.74%` | `0.79` | 1,860,000,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.64%` | `47.36%` | `1.11` | 133,220,000.00 USD |
| `4H` | `Crypto.com` | `50.87%` | `49.13%` | `1.04` | 137,480,000.00 USD |
| `4H` | `WhiteBIT` | `49.71%` | `50.29%` | `0.99` | 3,520,000,000.00 USD |
| `4H` | `HTX` | `44.8%` | `55.2%` | `0.81` | 92,940,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `49.3%` | `50.7%` | `0.97` | 529,610,000.00 USD |
| `4H` | `Bitfinex` | `19.86%` | `80.14%` | `0.25` | 34,470,000.00 USD |
| `4H` | `Kraken` | `44.11%` | `55.89%` | `0.79` | 260,120,000.00 USD |
| `4H` | `Aster` | `44.85%` | `55.15%` | `0.81` | 232,590,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `47.96%` | `52.04%` | `0.92` | 328,380,000.00 USD |
| `4H` | `Whale Positions` | `45.51%` | `54.49%` | `0.84` | 7,940,000,000.00 USD |
| `4H` | `Global Accounts` | `47.23%` | `52.77%` | `0.90` | 28,580,000,000.00 USD |


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
| `0:00 UTC` | `2258.75` | `2261.21` | `2258.75` | `2272.75` | `2251.25` | 273,935,140.69 USD | 128,674,399.21 USD | 145,260,741.48 USD | -16,586,342.26 USD | `-6.05%` | `2B / 1S` |

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
| `5m` | 3,460,000.00 USD | -22,570,000.00 USD | **`DISTRIBUTION`** |
| `15m` | 377,300.00 USD | -27,580,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -4,230,000.00 USD | -57,100,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -12,100.00 USD | -35,380,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -75,770,000.00 USD | -971,760,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -87,170,000.00 USD | -1,270,000,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -109,100,000.00 USD | -1,550,000,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -64,430,000.00 USD | -1,250,000,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -72,010,000.00 USD | -1,300,000,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -116,800,000.00 USD | -1,710,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -107,590,000.00 USD | -2,310,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,100,000,000.00 USD | -9,310,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+3.46M` | 15m=`+377.30K` | 1h=`-12.10K` | 24h=`-116.80M`
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
  * `2026-10-30 03:29:57 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:53:57 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:40:57 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:57 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:57 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:57 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:41:57 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:41:57 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:57 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `2249.44` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2219.40` (Risk Distance: `30.04` pts)
  * +2.5R Take Profit: `2324.55`
  * Mathematical Lot Sizing: **`0.33 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2275.20` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2305.24` (Risk Distance: `30.04` pts)
  * +2.5R Take Profit: `2200.09`
  * Mathematical Lot Sizing: **`0.33 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2277.83`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
