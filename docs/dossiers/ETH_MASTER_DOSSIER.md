# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 04:44:06 IST` (`2026-10-29 23:14:06 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2256.40` | **Live Ask Quote**: `2260.60` | **Mid Price**: `2258.50`
- **Spread Points**: `420.00` | **Spread BPS**: `18.60 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2313.22` | VWAP Z-Score: `-1.59` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `19.09` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `35.64` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2396.90` | Lower -3.00σ Band: `2229.54`
  * Upper +2.51σ Band: `2383.23` | Lower -2.51σ Band: `2243.20`
  * Upper +2.01σ Band: `2369.28` | Lower -2.01σ Band: `2257.15`
  * Upper +2.00σ Band: `2369.00` | Lower -2.00σ Band: `2257.43`
  * Upper +1.28σ Band: `2348.92` | Lower -1.28σ Band: `2277.51`
  * Upper +1.00σ Band: `2341.11` | Lower -1.00σ Band: `2285.32`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2272.87` | EMA-20=`2289.50` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2308.97` (Slope: `+0.0000`) | EMA-100=`2318.86`
  * Institutional Anchors: EMA-144=`2322.19` | EMA-200=`2323.62` (Slope: `-0.2816`) | EMA-233=`2325.16`
- **Range Boundaries**: 24H High=`2374.90` | 24H Low=`2225.40` | Weekly High=`2387.80` | Weekly Low=`2225.40`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2276.08` (Distance: `-0.66%`)
  * Point of Control (POC) = `2264.37` (Distance: `-0.15%`)
  * Value Area Low (VAL) = `2255.59` (Distance: `+0.24%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2339.52` | POC=`2321.58` | VAL=`2296.66`
  * Prior Day Extremes: PDH=`2374.90` | PDL=`2225.40` | PDC=`2252.70`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2343.95` | Weekly POC=`2310.39` | Weekly VAL=`2299.56`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2289.10` | Low=`2245.20`
  * London Session (08:00-16:00 UTC): High=`2267.53` | Low=`2249.47`
  * New York Session (13:00-21:00 UTC): High=`2272.05` | Low=`2244.95`
  * Initial Balance (First Hour): IB High=`2265.28` | IB Low=`2251.72`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2249.47` - `2267.53`
  * Optimal Trade Entry (OTE 0.705): `2263.02`
  * Structural Invalidation Anchor (0.786): `2276.57`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2274.07` | `2275.74` | `2271.14` | `2273.38` | `9,120` | 20,735,366.09 USD | 1,596,623.82 USD | `+7.70%` | -886,966,262.06 USD | `+0.57` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `2273.37` | `2273.37` | `2261.72` | `2261.74` | `21,282` | 48,237,296.34 USD | -4,228,531.36 USD | `-8.77%` | -891,194,793.42 USD | `-0.17` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `2261.73` | `2263.94` | `2260.69` | `2262.49` | `3,256` | 7,365,848.13 USD | 166,631.39 USD | `+2.26%` | -891,028,162.03 USD | `+0.28` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `2270.35` | `2284.38` | `2269.00` | `2273.92` | `65,473` | 149,129,529.31 USD | -12,399,553.39 USD | `-8.31%` | -888,525,096.45 USD | `+0.24` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `2273.92` | `2276.28` | `2269.62` | `2273.38` | `34,819` | 79,152,401.54 USD | 1,451,339.24 USD | `+1.83%` | -887,073,757.22 USD | `+0.44` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `2273.37` | `2273.37` | `2260.69` | `2262.99` | `24,603` | 55,751,896.18 USD | -4,135,705.11 USD | `-7.42%` | -891,209,462.33 USD | `+0.37` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2256.63` | `2293.87` | `2245.02` | `2272.46` | `640,507` | 1,454,537,838.20 USD | -31,797,242.40 USD | `-2.19%` | -855,482,312.03 USD | `+0.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `2272.47` | `2284.38` | `2251.12` | `2273.38` | `307,178` | 696,854,685.19 USD | -24,389,485.70 USD | `-3.50%` | -879,871,797.73 USD | `+0.10` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `2273.37` | `2273.37` | `2260.69` | `2262.49` | `24,537` | 55,603,144.47 USD | -4,061,899.98 USD | `-7.31%` | -883,933,697.71 USD | `+0.30` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -163,611,405.07 USD | `+1.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -365,767,522.01 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2262.99` | `2,330,269` | 5,301,597,533.04 USD | -518,239,980.83 USD | `-9.78%` | -884,007,502.84 USD | `-1.91` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2308.03` | `2334.83` | `2303.75` | `2309.10` | `525,175` | 1,216,920,375.04 USD | -34,916,746.14 USD | `-2.87%` | -218,489,329.59 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2309.10` | `2330.05` | `2308.88` | `2324.26` | `409,016` | 949,400,649.22 USD | -49,162,247.72 USD | `-5.18%` | -267,651,577.31 USD | `+0.60` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -163,611,405.07 USD | `+1.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -365,767,522.01 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2262.99` | `2,330,269` | 5,301,597,533.04 USD | -518,239,980.83 USD | `-9.78%` | -884,007,502.84 USD | `-1.91` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`2258.50`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2260.70` | `392.0831` | 886,382.26 USD | 5,043,404.14 USD | `8 orders` | `-0.09%` | `-` |
| `BID` | `2260.80` | `364.5735` | 824,227.77 USD | 4,157,021.87 USD | `6 orders` | `-0.08%` | `-` |
| `BID` | `2260.90` | `39.8039` | 89,992.64 USD | 3,332,794.10 USD | `6 orders` | `-0.08%` | `-` |
| `BID` | `2261.00` | `476.1858` | 1,076,656.09 USD | 3,242,801.47 USD | `5 orders` | `-0.07%` | `-` |
| `BID` | `2261.10` | `83.5373` | 188,886.19 USD | 2,166,145.37 USD | `6 orders` | `-0.07%` | `-` |
| `BID` | `2261.20` | `70.5100` | 159,437.21 USD | 1,977,259.18 USD | `5 orders` | `-0.06%` | `-` |
| `BID` | `2261.30` | `27.6254` | 62,469.32 USD | 1,817,821.97 USD | `7 orders` | `-0.06%` | `-` |
| `BID` | `2261.40` | `97.0173` | 219,394.92 USD | 1,755,352.65 USD | `7 orders` | `-0.06%` | `-` |
| `BID` | `2261.50` | `157.4344` | 356,037.90 USD | 1,535,957.73 USD | `6 orders` | `-0.05%` | `-` |
| `BID` | `2261.60` | `47.0720` | 106,458.04 USD | 1,179,919.84 USD | `7 orders` | `-0.05%` | `-` |
| `BID` | `2261.70` | `112.4083` | 254,233.85 USD | 1,073,461.80 USD | `7 orders` | `-0.04%` | `-` |
| `BID` | `2261.80` | `111.1171` | 251,324.66 USD | 819,227.95 USD | `10 orders` | `-0.04%` | `-` |
| `BID` | `2261.90` | `20.5401` | 46,459.65 USD | 567,903.29 USD | `6 orders` | `-0.03%` | `-` |
| `BID` | `2262.00` | `66.3347` | 150,049.09 USD | 521,443.64 USD | `10 orders` | `-0.03%` | `-` |
| `BID` | `2262.10` | `23.8912` | 54,044.28 USD | 371,394.55 USD | `8 orders` | `-0.02%` | `-` |
| `BID` | `2262.20` | `1.7681` | 3,999.80 USD | 317,350.26 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `2262.30` | `22.7489` | 51,464.84 USD | 313,350.47 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `2262.40` | `25.6703` | 58,076.49 USD | 261,885.63 USD | `5 orders` | `-0.01%` | `-` |
| `BID` | `2262.50` | `13.3753` | 30,261.62 USD | 203,809.15 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `2262.60` | `76.7027` | 173,547.53 USD | 173,547.53 USD | `20 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2262.65` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,262.65` | `0.00%` | `-` |
| `ASK` | `2262.70` | `419.6239` | 949,483.00 USD | 949,483.00 USD | `15 orders` | `+0.00%` | `-` |
| `ASK` | `2262.80` | `26.0260` | 58,891.63 USD | 1,008,374.63 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `2262.90` | `76.4454` | 172,988.30 USD | 1,181,362.93 USD | `7 orders` | `+0.01%` | `-` |
| `ASK` | `2263.00` | `243.1042` | 550,144.80 USD | 1,731,507.73 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `2263.10` | `208.8949` | 472,750.05 USD | 2,204,257.78 USD | `9 orders` | `+0.02%` | `-` |
| `ASK` | `2263.20` | `97.0034` | 219,538.09 USD | 2,423,795.87 USD | `9 orders` | `+0.02%` | `-` |
| `ASK` | `2263.30` | `265.6976` | 601,353.38 USD | 3,025,149.25 USD | `9 orders` | `+0.03%` | `-` |
| `ASK` | `2263.40` | `415.8776` | 941,297.36 USD | 3,966,446.61 USD | `17 orders` | `+0.03%` | `-` |
| `ASK` | `2263.50` | `115.9966` | 262,558.30 USD | 4,229,004.92 USD | `18 orders` | `+0.04%` | `-` |
| `ASK` | `2263.60` | `514.4327` | 1,164,469.86 USD | 5,393,474.78 USD | `14 orders` | `+0.04%` | `-` |
| `ASK` | `2263.70` | `190.5115` | 431,260.88 USD | 5,824,735.66 USD | `7 orders` | `+0.05%` | `-` |
| `ASK` | `2263.80` | `233.0397` | 527,555.27 USD | 6,352,290.93 USD | `9 orders` | `+0.05%` | `-` |
| `ASK` | `2263.90` | `432.9087` | 980,062.01 USD | 7,332,352.94 USD | `7 orders` | `+0.06%` | `-` |
| `ASK` | `2264.00` | `344.0895` | 779,018.63 USD | 8,111,371.57 USD | `10 orders` | `+0.06%` | `-` |
| `ASK` | `2264.10` | `198.5874` | 449,621.73 USD | 8,560,993.30 USD | `10 orders` | `+0.06%` | `-` |
| `ASK` | `2264.20` | `317.6032` | 719,117.17 USD | 9,280,110.46 USD | `7 orders` | `+0.07%` | `-` |
| `ASK` | `2264.30` | `80.5745` | 182,444.84 USD | 9,462,555.30 USD | `4 orders` | `+0.07%` | `-` |
| `ASK` | `2264.40` | `72.2618` | 163,629.62 USD | 9,626,184.92 USD | `5 orders` | `+0.08%` | `-` |
| `ASK` | `2264.50` | `363.0738` | 822,180.62 USD | 10,448,365.54 USD | `6 orders` | `+0.08%` | `-` |
| `ASK` | `2264.60` | `139.2450` | 315,334.23 USD | 10,763,699.77 USD | `8 orders` | `+0.09%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:36:18 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 04:36:18 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1914.14` | `6,500.22` | 12,442,365.30 USD | `AT_RISK_LIQ` | `0xf78c5d8d4b` | `2026-10-30 04:36:18 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1918.00` | `4,184.01` | 8,024,935.59 USD | `TRIGGER_STOP` | `0x6ea486a342` | `2026-10-30 04:36:18 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1926.10` | `8,092.45` | 15,586,857.75 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 04:36:18 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `8,500.00` | 16,371,850.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-30 04:36:18 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2040.68` | `7,964.66` | 16,253,351.49 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-30 04:36:18 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2171.15` | `48,499.51` | 105,299,495.95 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 04:36:18 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2180.21` | `44,734.81` | 97,531,206.32 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 04:36:18 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2200.00` | `1,000.00` | 2,200,000.00 USD | `TRIGGER_STOP` | `0x834cae1ec1` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2222.90` | `2,041.58` | 4,538,233.52 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2223.00` | `331.64` | 737,231.27 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2227.00` | `734.73` | 1,636,235.69 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x646be0d5f9` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2233.30` | `3,412.70` | 7,621,590.95 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2234.80` | `1,434.11` | 3,204,937.85 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2238.60` | `329.17` | 736,886.68 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2239.10` | `358.01` | 801,627.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2240.60` | `342.64` | 767,714.70 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2244.10` | `1,040.98` | 2,336,070.40 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 04:36:18 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2245.00` | `1,758.58` | 3,948,020.86 USD | `TRIGGER_STOP` | `0x28280399d9` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2247.90` | `1,760.24` | 3,956,835.18 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2247.90` | `331.84` | 745,947.63 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2248.80` | `1,781.70` | 4,006,684.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2250.60` | `686.42` | 1,544,855.28 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2251.00` | `259.25` | 583,572.20 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x07fd7e702b` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2251.30` | `348.83` | 785,325.26 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2251.60` | `310.75` | 699,680.20 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2253.40` | `889.06` | 2,003,412.99 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2255.40` | `470.10` | 1,060,256.77 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2255.80` | `898.38` | 2,026,567.86 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2258.00` | `339.84` | 767,369.78 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2259.10` | `276.62` | 624,906.59 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x07fd7e702b` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2260.00` | `332.43` | 751,285.02 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2263.70` | `286.70` | 648,997.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x07fd7e702b` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2264.30` | `331.82` | 751,345.23 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2265.40` | `442.20` | 1,001,749.69 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2265.70` | `327.34` | 741,654.69 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2265.90` | `663.11` | 1,502,537.32 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2267.60` | `286.70` | 650,115.70 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x07fd7e702b` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2268.70` | `883.09` | 2,003,465.38 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2268.70` | `483.33` | 1,096,533.27 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2271.40` | `326.37` | 741,327.95 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2271.60` | `468.18` | 1,063,508.60 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2271.60` | `286.70` | 651,262.50 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x07fd7e702b` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2271.70` | `899.26` | 2,042,842.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2272.10` | `1,763.48` | 4,006,792.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2272.20` | `2,200.51` | 4,999,999.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb1ec7febea` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2273.40` | `707.87` | 1,609,266.43 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2273.70` | `1,554.55` | 3,534,577.38 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xbc76170c8a` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2274.10` | `1,321.43` | 3,005,064.19 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2278.30` | `1,523.46` | 3,470,893.91 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xbc76170c8a` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2279.50` | `499.99` | 1,139,734.04 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2280.90` | `991.78` | 2,262,142.33 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2281.40` | `1,760.24` | 4,015,803.09 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2284.20` | `500.49` | 1,143,207.84 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2287.10` | `350.50` | 801,627.64 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2287.70` | `335.58` | 767,714.60 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2289.60` | `1,440.71` | 3,298,638.85 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2301.20` | `3,406.65` | 7,839,373.31 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2303.00` | `2,162.25` | 4,979,651.85 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 04:36:18 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2305.50` | `499.89` | 1,152,501.01 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 04:36:18 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2440.56` | `22,046.99` | 53,807,093.03 USD | `AT_RISK_LIQ` | `0x8added25f8` | `2026-10-30 04:36:18 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `3,045.71` | 7,656,616.15 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-30 04:36:18 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2585.91` | `6,224.05` | 16,094,799.06 USD | `AT_RISK_LIQ` | `0x08bf75d170` | `2026-10-30 04:36:18 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2658.66` | `9,700.00` | 25,789,022.95 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-30 04:36:18 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2709.02` | `8,500.00` | 23,026,630.41 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-30 04:36:18 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 240,695,579.19 USD | `106,417.71` | `2322.74` | `2264.65` | `3996.58` | 6,485,432.96 USD | `+2.69%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 146,288,158.71 USD | `64,680.62` | `2375.30` | `2264.65` | `4700.10` | 7,348,138.79 USD | `+5.02%` | `5X Cross` |
| `6` | `0x77dd...e0e9` | `LONG` | 109,686,496.11 USD | `48,499.51` | `2610.31` | `2264.65` | `2171.06` | -16,912,387.75 USD | `-15.42%` | `10X Cross` |
| `8` | `0x0392...d7d9` | `LONG` | 101,225,935.76 USD | `44,734.81` | `2518.71` | `2264.65` | `2180.12` | -11,448,370.81 USD | `-11.31%` | `9X Cross` |
| `14` | `0xde8d...9524` | `LONG` | 68,474,570.79 USD | `30,282.40` | `2134.45` | `2264.65` | `1787.01` | 3,838,240.22 USD | `+5.61%` | `20X Cross` |
| `22` | `0x8add...7d2c` | `SHORT` | 49,875,579.94 USD | `22,046.99` | `2271.09` | `2264.65` | `2445.50` | 195,317.36 USD | `+0.39%` | `25X Cross` |
| `23` | `0xdf95...7d72` | `SHORT` | 49,362,213.65 USD | `21,823.34` | `2402.53` | `2264.65` | `4137.27` | 3,069,116.02 USD | `+6.22%` | `25X Cross` |
| `34` | `0xeced...6210` | `SHORT` | 37,945,879.75 USD | `16,687.58` | `2522.09` | `2264.65` | `3474.50` | 4,141,835.25 USD | `+10.92%` | `20X Cross` |
| `35` | `0xb695...a92d` | `SHORT` | 37,779,167.46 USD | `16,704.62` | `2557.74` | `2264.65` | `3851.22` | 4,946,997.59 USD | `+13.09%` | `20X Cross` |
| `36` | `0x6046...b21d` | `LONG` | 36,025,022.38 USD | `15,927.59` | `2410.19` | `2264.65` | `1710.25` | -2,363,597.26 USD | `-6.56%` | `6X Cross` |
| `39` | `0x45d2...4029` | `SHORT` | 31,595,355.00 USD | `13,950.00` | `2443.60` | `2264.65` | `5392.63` | 2,492,927.46 USD | `+7.89%` | `20X Cross` |
| `41` | `0x7fda...17d1` | `SHORT` | 30,403,387.08 USD | `13,419.57` | `2433.32` | `2264.65` | `5202.76` | 2,250,812.40 USD | `+7.40%` | `25X Cross` |
| `44` | `0x0622...8088` | `LONG` | 27,762,887.37 USD | `12,254.64` | `2271.64` | `2264.65` | `1470.77` | -75,251.81 USD | `-0.27%` | `5X Cross` |
| `45` | `0xbd1c...ff0e` | `LONG` | 27,187,200.00 USD | `12,000.00` | `2419.91` | `2264.65` | `1520.89` | -1,851,832.39 USD | `-6.81%` | `20X Cross` |
| `46` | `0x2371...0883` | `LONG` | 27,150,000.00 USD | `12,000.00` | `2421.77` | `2264.65` | `1279.99` | -1,911,294.85 USD | `-7.04%` | `20X Cross` |
| `56` | `0xa9de...e049` | `LONG` | 25,000,800.00 USD | `11,000.00` | `2481.81` | `2264.65` | `1644.72` | -2,299,179.46 USD | `-9.20%` | `20X Cross` |
| `57` | `0x0c5d...36b3` | `LONG` | 24,995,300.00 USD | `11,000.00` | `2482.20` | `2264.65` | `1645.05` | -2,308,953.24 USD | `-9.24%` | `20X Cross` |
| `58` | `0x09dc...c094` | `LONG` | 24,992,000.00 USD | `11,000.00` | `2465.31` | `2264.65` | `1638.04` | -2,126,423.04 USD | `-8.51%` | `20X Cross` |
| `59` | `0x6c93...59a4` | `LONG` | 24,882,000.00 USD | `11,000.00` | `2441.15` | `2264.65` | `1602.92` | -1,970,672.73 USD | `-7.92%` | `20X Cross` |
| `61` | `0xa61c...66b9` | `LONG` | 24,692,895.20 USD | `10,888.00` | `2398.32` | `2264.65` | `1517.35` | -1,420,062.19 USD | `-5.75%` | `10X Cross` |
| `71` | `0x15a4...dfdb` | `LONG` | 22,723,000.00 USD | `10,000.00` | `1761.94` | `2264.65` | `205.60` | 5,103,518.97 USD | `+22.46%` | `20X Cross` |
| `72` | `0xa2ce...3126` | `LONG` | 22,694,232.45 USD | `10,016.88` | `2162.83` | `2264.65` | `1522.97` | 1,029,430.40 USD | `+4.54%` | `10X Cross` |
| `75` | `0x6646...6de5` | `LONG` | 22,660,000.00 USD | `10,000.00` | `1765.80` | `2264.65` | `1718.36` | 5,001,942.55 USD | `+22.07%` | `25X Cross` |
| `76` | `0xec7f...df39` | `LONG` | 22,622,400.00 USD | `10,000.00` | `2719.35` | `2264.65` | `1721.48` | -4,571,148.52 USD | `-20.21%` | `20X Cross` |
| `77` | `0xbf73...5d58` | `SHORT` | 22,609,000.00 USD | `10,000.00` | `2265.66` | `2264.65` | `2948.08` | 47,698.68 USD | `+0.21%` | `25X Cross` |
| `79` | `0xaeaa...2416` | `SHORT` | 21,989,900.00 USD | `9,700.00` | `2311.92` | `2264.65` | `2658.58` | 435,782.40 USD | `+1.98%` | `25X Cross` |
| `84` | `0xf517...c032` | `SHORT` | 21,181,200.50 USD | `9,363.51` | `2202.84` | `2264.65` | `3120.82` | -554,792.55 USD | `-2.62%` | `25X Cross` |
| `85` | `0xca49...53c8` | `SHORT` | 20,963,252.50 USD | `9,261.84` | `2549.39` | `2264.65` | `3860.48` | 2,648,861.43 USD | `+12.64%` | `25X Cross` |
| `89` | `0xba5d...a352` | `SHORT` | 20,578,208.71 USD | `9,054.12` | `2493.89` | `2264.65` | `2942.65` | 2,001,798.55 USD | `+9.73%` | `20X Cross` |
| `90` | `0xea00...a918` | `LONG` | 20,371,157.00 USD | `9,003.83` | `2003.01` | `2264.65` | `1439.79` | 2,336,378.14 USD | `+11.47%` | `5X Cross` |
| `92` | `0xefe4...194b` | `SHORT` | 19,983,009.72 USD | `8,820.57` | `2267.42` | `2264.65` | `3879.83` | 17,004.67 USD | `+0.09%` | `20X Cross` |
| `100` | `0xb37f...66ca` | `SHORT` | 19,216,800.00 USD | `8,500.00` | `2308.30` | `2264.65` | `2708.94` | 403,754.19 USD | `+2.10%` | `25X Cross` |
| `110` | `0x9eec...daab` | `LONG` | 18,301,889.67 USD | `8,092.45` | `1658.44` | `2264.65` | `1926.96` | 4,881,025.14 USD | `+26.67%` | `15X Cross` |
| `117` | `0x5f91...65aa` | `LONG` | 18,095,698.20 USD | `7,964.66` | `1626.99` | `2264.65` | `2040.68` | 5,137,255.14 USD | `+28.39%` | `16X Cross` |
| `120` | `0x939f...04d2` | `LONG` | 17,701,376.69 USD | `7,823.81` | `2482.77` | `2264.65` | `1636.66` | -1,723,374.96 USD | `-9.74%` | `25X Cross` |
| `122` | `0xcf53...ee11` | `SHORT` | 17,226,019.01 USD | `7,603.63` | `1862.69` | `2264.65` | `4021.18` | -3,062,755.06 USD | `-17.78%` | `7X Cross` |
| `124` | `0x218a...7da2` | `SHORT` | 16,983,107.60 USD | `7,506.35` | `2208.16` | `2264.65` | `2854.56` | -407,885.62 USD | `-2.40%` | `10X Cross` |
| `128` | `0xec0b...b078` | `LONG` | 15,850,940.33 USD | `7,007.80` | `2065.97` | `2264.65` | `1050.61` | 1,373,010.74 USD | `+8.66%` | `25X Cross` |
| `135` | `0x418a...8888` | `SHORT` | 15,211,226.33 USD | `6,724.38` | `2494.55` | `2264.65` | `3003.42` | 1,563,096.84 USD | `+10.28%` | `25X Cross` |
| `137` | `0x4ff9...38d3` | `LONG` | 14,849,566.64 USD | `6,564.10` | `2447.40` | `2264.65` | `1670.58` | -1,215,456.10 USD | `-8.19%` | `3X Isolated` |
| `139` | `0xf78c...c581` | `LONG` | 14,708,701.21 USD | `6,500.22` | `2521.53` | `2264.65` | `1914.06` | -1,681,839.74 USD | `-11.43%` | `20X Cross` |
| `144` | `0x799f...5f4c` | `LONG` | 14,274,632.17 USD | `6,310.90` | `2390.33` | `2264.65` | `1816.19` | -810,532.44 USD | `-5.68%` | `20X Cross` |
| `147` | `0x08bf...7872` | `SHORT` | 14,075,683.20 USD | `6,224.05` | `2258.00` | `2264.65` | `2585.83` | -21,767.09 USD | `-0.15%` | `20X Cross` |
| `152` | `0xc179...e0c8` | `LONG` | 13,828,381.02 USD | `6,113.61` | `2322.20` | `2264.65` | `1180.03` | -368,669.47 USD | `-2.67%` | `10X Cross` |
| `153` | `0x0c4a...1b19` | `LONG` | 13,768,278.36 USD | `6,086.13` | `2373.06` | `2264.65` | `2135.21` | -674,472.21 USD | `-4.90%` | `25X Isolated` |
| `155` | `0x4487...c92d` | `SHORT` | 13,576,121.58 USD | `5,992.29` | `2359.13` | `2264.65` | `2793.61` | 560,500.64 USD | `+4.13%` | `10X Cross` |
| `156` | `0xd9e7...4aff` | `LONG` | 13,575,000.00 USD | `6,000.00` | `2480.18` | `2264.65` | `1408.35` | -1,306,124.33 USD | `-9.62%` | `20X Cross` |
| `168` | `0x1ee7...edf5` | `LONG` | 12,436,600.00 USD | `5,500.00` | `2316.93` | `2264.65` | `2127.24` | -306,539.62 USD | `-2.46%` | `25X Cross` |
| `172` | `0xecb6...2b00` | `SHORT` | 12,155,283.69 USD | `5,364.44` | `2279.97` | `2264.65` | `7781.99` | 75,510.14 USD | `+0.62%` | `15X Cross` |
| `188` | `0x45ab...6cbc` | `LONG` | 11,132,692.79 USD | `4,920.96` | `2727.66` | `2264.65` | `1389.01` | -2,290,051.01 USD | `-20.57%` | `7X Cross` |
| `192` | `0x64b7...9da9` | `LONG` | 10,986,655.95 USD | `4,856.84` | `2604.61` | `2264.65` | `1534.69` | -1,663,558.46 USD | `-15.14%` | `25X Cross` |
| `194` | `0xfb18...eb17` | `SHORT` | 10,963,828.39 USD | `4,845.89` | `2315.54` | `2264.65` | `2628.03` | 257,054.40 USD | `+2.34%` | `25X Cross` |
| `196` | `0x5559...d43b` | `SHORT` | 10,759,329.81 USD | `4,755.93` | `2262.69` | `2264.65` | `2793.19` | 1,876.07 USD | `+0.02%` | `25X Cross` |
| `201` | `0x12d2...f97f` | `LONG` | 10,651,742.77 USD | `4,708.79` | `2588.61` | `2264.65` | `2026.59` | -1,537,491.54 USD | `-14.43%` | `20X Cross` |
| `210` | `0x645b...87b8` | `SHORT` | 10,275,664.37 USD | `4,535.72` | `2421.64` | `2264.65` | `7122.52` | 708,233.10 USD | `+6.89%` | `10X Cross` |
| `213` | `0xe091...6705` | `SHORT` | 10,178,100.45 USD | `4,500.00` | `2467.33` | `2264.65` | `2572.88` | 924,908.06 USD | `+9.09%` | `20X Cross` |
| `218` | `0xb829...3a81` | `LONG` | 9,994,467.11 USD | `4,394.91` | `2398.60` | `2264.65` | `1520.46` | -547,174.84 USD | `-5.47%` | `20X Cross` |
| `236` | `0x28bb...fca6` | `SHORT` | 9,522,568.28 USD | `4,209.61` | `1896.10` | `2264.65` | `3038.30` | -1,540,685.72 USD | `-16.18%` | `20X Cross` |
| `237` | `0x6ea4...0ea7` | `SHORT` | 9,514,025.57 USD | `4,184.01` | `2602.13` | `2264.65` | `3425.97` | 1,373,321.10 USD | `+14.43%` | `20X Cross` |
| `249` | `0xb8eb...1dd5` | `LONG` | 9,086,328.03 USD | `4,017.12` | `2271.48` | `2264.65` | `1778.20` | -38,514.62 USD | `-0.42%` | `25X Cross` |
| `251` | `0x5e9e...35ee` | `SHORT` | 9,081,121.22 USD | `4,007.56` | `1796.39` | `2264.65` | `2586.38` | -1,881,971.13 USD | `-20.72%` | `20X Cross` |
| `252` | `0x8cc9...2b6a` | `SHORT` | 9,062,000.00 USD | `4,000.00` | `1791.18` | `2264.65` | `3850.83` | -1,897,253.33 USD | `-20.94%` | `25X Cross` |
| `254` | `0x3dc9...54b0` | `SHORT` | 9,050,498.98 USD | `3,999.69` | `2480.32` | `2264.65` | `6640.08` | 870,037.57 USD | `+9.61%` | `20X Cross` |
| `255` | `0xfb94...0ddf` | `SHORT` | 9,049,551.46 USD | `4,002.10` | `2382.44` | `2264.65` | `5105.28` | 485,232.69 USD | `+5.36%` | `20X Cross` |
| `259` | `0xd911...961e` | `LONG` | 8,900,077.07 USD | `3,934.78` | `2272.80` | `2264.65` | `1680.87` | -42,924.32 USD | `-0.48%` | `25X Cross` |
| `267` | `0xf02d...5eb3` | `LONG` | 8,722,239.20 USD | `3,855.99` | `2513.67` | `2264.65` | `321.75` | -970,473.11 USD | `-11.13%` | `20X Cross` |
| `272` | `0x4b67...f4e7` | `LONG` | 8,643,890.63 USD | `3,820.84` | `2591.51` | `2264.65` | `1654.19` | -1,257,882.91 USD | `-14.55%` | `20X Cross` |
| `290` | `0x8ae4...3d60` | `LONG` | 8,090,987.11 USD | `3,558.20` | `2482.21` | `2264.65` | `488.10` | -741,210.92 USD | `-9.16%` | `10X Cross` |
| `329` | `0xbc76...417c` | `LONG` | 7,032,467.86 USD | `3,109.10` | `2263.46` | `2264.65` | `2216.85` | -4,857.21 USD | `-0.07%` | `25X Cross` |
| `332` | `0xb1ec...e86a` | `SHORT` | 6,969,094.08 USD | `3,079.85` | `2272.72` | `2264.65` | `5299.83` | 30,579.51 USD | `+0.44%` | `25X Cross` |
| `335` | `0x9c2a...f6a8` | `SHORT` | 6,919,858.35 USD | `3,045.71` | `2543.83` | `2264.65` | `2599.77` | 827,928.20 USD | `+11.96%` | `20X Cross` |
| `337` | `0xfe7c...b7ae` | `SHORT` | 6,836,038.58 USD | `3,023.19` | `2440.17` | `2264.65` | `5527.03` | 541,086.44 USD | `+7.92%` | `25X Cross` |
| `340` | `0x007d...67a0` | `LONG` | 6,787,500.00 USD | `3,000.00` | `2400.00` | `2264.65` | `1471.59` | -412,500.00 USD | `-6.08%` | `25X Cross` |
| `341` | `0x4a20...3c26` | `LONG` | 6,784,800.00 USD | `3,000.00` | `2428.72` | `2264.65` | `591.37` | -501,360.28 USD | `-7.39%` | `20X Cross` |
| `398` | `0x8328...f54a` | `SHORT` | 5,854,469.83 USD | `2,576.45` | `2292.01` | `2264.65` | `3280.20` | 50,801.45 USD | `+0.87%` | `25X Cross` |
| `400` | `0xed48...7c9b` | `SHORT` | 5,767,595.83 USD | `2,551.13` | `2460.02` | `2264.65` | `3237.82` | 508,250.58 USD | `+8.81%` | `20X Cross` |
| `412` | `0xfbe2...c8ea` | `SHORT` | 5,433,378.38 USD | `2,403.30` | `2041.57` | `2264.65` | `2615.82` | -526,873.58 USD | `-9.70%` | `20X Cross` |
| `416` | `0x1c98...7fc7` | `LONG` | 5,361,866.43 USD | `2,358.00` | `2467.15` | `2264.65` | `1897.18` | -455,705.05 USD | `-8.50%` | `10X Cross` |
| `420` | `0x9599...c60a` | `LONG` | 5,278,703.77 USD | `2,333.54` | `2271.64` | `2264.65` | `471.54` | -22,275.79 USD | `-0.42%` | `20X Cross` |
| `424` | `0x77ee...2902` | `SHORT` | 5,182,093.26 USD | `2,290.69` | `2476.53` | `2264.65` | `5814.31` | 490,878.98 USD | `+9.47%` | `25X Cross` |
| `433` | `0x023a...2355` | `LONG` | 5,049,805.27 USD | `2,232.35` | `2330.15` | `2264.65` | `0.000000` | -151,923.46 USD | `-3.01%` | `25X Cross` |
| `441` | `0xd507...c948` | `SHORT` | 4,912,846.57 USD | `2,172.00` | `2387.49` | `2264.65` | `2707.31` | 272,794.45 USD | `+5.55%` | `5X Isolated` |
| `450` | `0x382b...3e39` | `SHORT` | 4,824,476.49 USD | `2,129.54` | `2296.66` | `2264.65` | `4591.20` | 66,360.72 USD | `+1.38%` | `25X Cross` |
| `458` | `0xf910...0a2d` | `LONG` | 4,733,815.68 USD | `2,093.03` | `2270.43` | `2264.65` | `0.000000` | -18,274.46 USD | `-0.39%` | `5X Cross` |
| `481` | `0xc619...10f5` | `LONG` | 4,545,760.00 USD | `2,000.00` | `2318.40` | `2264.65` | `1809.58` | -91,046.86 USD | `-2.00%` | `25X Cross` |
| `482` | `0xf929...d1f9` | `SHORT` | 4,544,600.00 USD | `2,000.00` | `2423.37` | `2264.65` | `2548.79` | 302,140.34 USD | `+6.65%` | `25X Cross` |
| `484` | `0x3440...32c5` | `SHORT` | 4,538,282.16 USD | `2,000.57` | `2198.21` | `2264.65` | `3642.46` | -140,619.02 USD | `-3.10%` | `25X Cross` |
| `488` | `0x7a6d...f79c` | `SHORT` | 4,529,400.00 USD | `2,000.00` | `2418.41` | `2264.65` | `2656.86` | 307,432.11 USD | `+6.79%` | `25X Cross` |
| `489` | `0x3453...b323` | `SHORT` | 4,525,878.55 USD | `2,000.12` | `2322.47` | `2264.65` | `2411.78` | 119,357.29 USD | `+2.64%` | `25X Cross` |
| `490` | `0xbb34...1696` | `LONG` | 4,522,400.00 USD | `2,000.00` | `2318.80` | `2264.65` | `1970.84` | -115,216.04 USD | `-2.55%` | `25X Cross` |
| `501` | `0x0514...bdfe` | `SHORT` | 4,417,920.00 USD | `1,950.00` | `1988.74` | `2264.65` | `3124.75` | -539,860.37 USD | `-12.22%` | `25X Cross` |
| `513` | `0x8376...9a1e` | `SHORT` | 4,320,013.56 USD | `1,910.50` | `2477.72` | `2264.65` | `3183.57` | 413,674.62 USD | `+9.58%` | `20X Cross` |
| `533` | `0x7265...91a5` | `LONG` | 4,095,288.77 USD | `1,801.87` | `2533.96` | `2264.65` | `1988.11` | -470,577.68 USD | `-11.49%` | `20X Cross` |
| `536` | `0xb15b...dbae` | `SHORT` | 4,084,859.17 USD | `1,797.68` | `2294.54` | `2264.65` | `2302.38` | 39,984.80 USD | `+0.98%` | `25X Cross` |
| `539` | `0x541e...071d` | `SHORT` | 4,080,744.00 USD | `1,805.00` | `2648.19` | `2264.65` | `3173.35` | 699,240.84 USD | `+17.14%` | `25X Cross` |
| `542` | `0x739c...cfb2` | `SHORT` | 4,072,500.00 USD | `1,800.00` | `2427.60` | `2264.65` | `2484.66` | 297,196.38 USD | `+7.30%` | `25X Cross` |
| `548` | `0xa445...329d` | `LONG` | 4,018,296.22 USD | `1,776.75` | `2398.85` | `2264.65` | `1967.85` | -243,873.13 USD | `-6.07%` | `25X Cross` |
| `550` | `0x91a9...3f70` | `SHORT` | 3,999,100.25 USD | `1,767.48` | `2156.23` | `2264.65` | `3675.82` | -187,996.17 USD | `-4.70%` | `4X Cross` |
| `554` | `0x2828...93a0` | `LONG` | 3,977,565.06 USD | `1,758.58` | `2314.00` | `2264.65` | `2241.63` | -91,801.79 USD | `-2.31%` | `25X Cross` |
| `574` | `0xf3dc...1672` | `SHORT` | 3,901,866.01 USD | `1,725.12` | `2271.25` | `2264.65` | `2579.02` | 16,314.12 USD | `+0.42%` | `20X Cross` |
| `586` | `0xfeec...4e9c` | `SHORT` | 3,826,702.32 USD | `1,691.81` | `2566.49` | `2264.65` | `2654.76` | 515,322.19 USD | `+13.47%` | `10X Cross` |
| `587` | `0x936c...bb0f` | `SHORT` | 3,825,887.00 USD | `1,688.69` | `2434.60` | `2264.65` | `4562.53` | 285,400.10 USD | `+7.46%` | `20X Cross` |
| `602` | `0xeee0...0b53` | `LONG` | 3,720,036.64 USD | `1,637.12` | `2468.64` | `2264.65` | `212.24` | -321,439.42 USD | `-8.64%` | `7X Cross` |
| `605` | `0x27b8...12fc` | `LONG` | 3,702,507.92 USD | `1,628.12` | `2468.73` | `2264.65` | `580.01` | -316,886.72 USD | `-8.56%` | `10X Cross` |
| `611` | `0x982b...4606` | `LONG` | 3,680,674.14 USD | `1,626.82` | `2575.24` | `2264.65` | `1548.31` | -508,778.93 USD | `-13.82%` | `5X Isolated` |
| `625` | `0x73d7...8be1` | `LONG` | 3,628,920.82 USD | `1,601.47` | `2410.40` | `2264.65` | `2022.84` | -231,258.10 USD | `-6.37%` | `25X Cross` |
| `645` | `0xe170...9300` | `SHORT` | 3,468,244.12 USD | `1,533.40` | `2076.39` | `2264.65` | `3169.66` | -284,294.62 USD | `-8.20%` | `25X Cross` |
| `647` | `0x4b86...df9d` | `SHORT` | 3,462,985.20 USD | `1,524.00` | `2287.40` | `2264.65` | `2760.56` | 23,012.40 USD | `+0.66%` | `9X Isolated` |
| `654` | `0xad54...6203` | `LONG` | 3,415,973.47 USD | `1,510.29` | `2614.66` | `2264.65` | `2123.39` | -532,933.08 USD | `-15.60%` | `10X Isolated` |
| `657` | `0x2e2b...2fab` | `LONG` | 3,409,686.77 USD | `1,507.38` | `2245.53` | `2264.65` | `1275.06` | 24,813.67 USD | `+0.73%` | `25X Cross` |
| `663` | `0x251f...6e5d` | `LONG` | 3,393,150.00 USD | `1,500.00` | `2346.68` | `2264.65` | `1893.48` | -126,880.49 USD | `-3.74%` | `20X Cross` |
| `664` | `0x39b4...5c34` | `SHORT` | 3,392,700.00 USD | `1,500.00` | `2329.97` | `2264.65` | `2552.14` | 102,259.99 USD | `+3.01%` | `25X Cross` |
| `679` | `0xb885...3c54` | `LONG` | 3,280,629.98 USD | `1,450.00` | `2274.34` | `2264.65` | `9.25` | -17,178.16 USD | `-0.52%` | `20X Cross` |
| `681` | `0xef70...a84c` | `SHORT` | 3,263,629.85 USD | `1,442.74` | `2424.73` | `2264.65` | `3265.28` | 234,640.98 USD | `+7.19%` | `25X Cross` |
| `687` | `0x4b5f...0dd8` | `LONG` | 3,239,086.28 USD | `1,431.96` | `2339.45` | `2264.65` | `2148.59` | -110,906.66 USD | `-3.42%` | `10X Cross` |
| `690` | `0xbadb...9ee6` | `LONG` | 3,230,212.29 USD | `1,428.16` | `1936.00` | `2264.65` | `1084.58` | 465,290.64 USD | `+14.40%` | `20X Cross` |
| `704` | `0x2577...4897` | `LONG` | 3,174,377.71 USD | `1,400.93` | `2279.41` | `2264.65` | `0.000000` | -18,938.07 USD | `-0.60%` | `15X Cross` |
| `721` | `0xa0fb...96be` | `LONG` | 3,123,269.92 USD | `1,376.25` | `2293.96` | `2264.65` | `1549.82` | -33,804.97 USD | `-1.08%` | `3X Cross` |
| `735` | `0x6e6f...82a6` | `LONG` | 3,090,044.23 USD | `1,366.25` | `2267.28` | `2264.65` | `1521.37` | -7,632.69 USD | `-0.25%` | `20X Cross` |
| `750` | `0x0a97...347d` | `LONG` | 3,021,565.00 USD | `1,335.85` | `2268.49` | `2264.65` | `1705.22` | -8,811.56 USD | `-0.29%` | `20X Cross` |
| `755` | `0xa70a...4be9` | `LONG` | 3,004,666.27 USD | `1,326.27` | `2268.37` | `2264.65` | `1147.52` | -3,809.99 USD | `-0.13%` | `20X Cross` |
| `758` | `0x6859...7e1e` | `SHORT` | 2,996,065.24 USD | `1,324.58` | `2200.39` | `2264.65` | `4468.91` | -81,468.10 USD | `-2.72%` | `25X Cross` |
| `760` | `0x0dd5...f6ee` | `LONG` | 2,988,074.50 USD | `1,315.00` | `2306.05` | `2264.65` | `1654.16` | -44,389.88 USD | `-1.49%` | `5X Cross` |
| `761` | `0x880a...311c` | `SHORT` | 2,987,136.79 USD | `1,320.22` | `2425.76` | `2264.65` | `8521.94` | 215,412.37 USD | `+7.21%` | `9X Cross` |
| `763` | `0x71d0...8c26` | `LONG` | 2,973,165.17 USD | `1,312.37` | `2266.42` | `2264.65` | `0.000000` | -1,210.32 USD | `-0.04%` | `25X Cross` |
| `793` | `0x5b5f...c052` | `SHORT` | 2,866,539.08 USD | `1,266.98` | `2261.24` | `2264.65` | `2319.11` | -1,589.62 USD | `-0.06%` | `25X Cross` |
| `805` | `0xc435...c905` | `SHORT` | 2,835,830.40 USD | `1,248.00` | `2704.38` | `2264.65` | `4254.13` | 539,239.95 USD | `+19.02%` | `20X Cross` |
| `819` | `0x7178...0854` | `LONG` | 2,756,300.73 USD | `1,218.63` | `2461.81` | `2264.65` | `1171.20` | -243,745.67 USD | `-8.84%` | `10X Cross` |
| `827` | `0x34fb...93de` | `LONG` | 2,736,856.39 USD | `1,209.82` | `2272.67` | `2264.65` | `35.94` | -12,676.94 USD | `-0.46%` | `20X Cross` |
| `837` | `0xaaa1...ab8c` | `SHORT` | 2,713,440.00 USD | `1,200.00` | `2276.29` | `2264.65` | `2366.10` | 18,117.58 USD | `+0.67%` | `25X Isolated` |
| `856` | `0x07fd...689d` | `LONG` | 2,638,493.23 USD | `1,166.49` | `2419.97` | `2264.65` | `0.000000` | -184,398.57 USD | `-6.99%` | `25X Cross` |
| `860` | `0x31de...13f2` | `LONG` | 2,613,557.04 USD | `1,153.43` | `2272.38` | `2264.65` | `0.000000` | -7,481.03 USD | `-0.29%` | `20X Cross` |
| `901` | `0xaf9f...a4fa` | `LONG` | 2,506,697.87 USD | `1,106.27` | `2269.41` | `2264.65` | `0.000000` | -3,888.44 USD | `-0.16%` | `20X Cross` |
| `904` | `0xbef3...0d3e` | `LONG` | 2,496,348.97 USD | `1,103.99` | `2315.08` | `2264.65` | `2162.26` | -59,487.19 USD | `-2.38%` | `20X Cross` |
| `912` | `0x6a41...a3b9` | `LONG` | 2,486,072.36 USD | `1,099.06` | `2314.77` | `2264.65` | `2164.10` | -58,000.33 USD | `-2.33%` | `20X Cross` |
| `918` | `0x2f80...f203` | `SHORT` | 2,463,446.11 USD | `1,088.94` | `1984.00` | `2264.65` | `3061.65` | -302,978.93 USD | `-12.30%` | `20X Cross` |
| `924` | `0x2b61...2f6c` | `SHORT` | 2,448,074.37 USD | `1,076.60` | `2681.75` | `2264.65` | `6467.06` | 439,098.37 USD | `+17.94%` | `10X Cross` |
| `925` | `0xac48...3201` | `SHORT` | 2,445,852.42 USD | `1,081.23` | `2276.96` | `2264.65` | `3747.32` | 16,071.44 USD | `+0.66%` | `20X Cross` |
| `930` | `0x6f11...0389` | `SHORT` | 2,441,021.70 USD | `1,079.00` | `2333.39` | `2264.65` | `3199.58` | 76,707.21 USD | `+3.14%` | `25X Cross` |
| `966` | `0x30af...393e` | `SHORT` | 2,354,802.65 USD | `1,041.16` | `2252.26` | `2264.65` | `2297.78` | -9,820.33 USD | `-0.42%` | `25X Cross` |
| `980` | `0x1b2a...f7a6` | `LONG` | 2,318,562.12 USD | `1,025.37` | `2737.51` | `2264.65` | `882.97` | -488,397.82 USD | `-21.06%` | `10X Cross` |
| `988` | `0x02aa...1806` | `SHORT` | 2,278,161.14 USD | `1,007.10` | `2654.68` | `2264.65` | `3613.57` | 395,370.97 USD | `+17.35%` | `20X Cross` |
| `989` | `0x001a...fef6` | `SHORT` | 2,278,065.49 USD | `1,007.33` | `2022.19` | `2264.65` | `3082.09` | -241,057.53 USD | `-10.58%` | `10X Cross` |
| `994` | `0x834c...dd93` | `SHORT` | 2,272,300.00 USD | `1,000.00` | `2249.68` | `2264.65` | `2310.88` | -22,614.58 USD | `-1.00%` | `25X Cross` |
| `997` | `0xdb3a...cf3b` | `LONG` | 2,269,774.16 USD | `1,003.22` | `2705.01` | `2264.65` | `0.000000` | -443,932.73 USD | `-19.56%` | `4X Cross` |
| `999` | `0x7743...e4fe` | `SHORT` | 2,262,957.96 USD | `1,000.56` | `2298.56` | `2264.65` | `4974.37` | 36,887.11 USD | `+1.63%` | `25X Cross` |
| `1000` | `0x5272...fcd9` | `SHORT` | 2,262,000.00 USD | `1,000.00` | `2241.82` | `2264.65` | `2831.63` | -20,175.51 USD | `-0.89%` | `5X Cross` |
| `1018` | `0xfc27...9d9d` | `SHORT` | 2,197,640.12 USD | `970.05` | `2332.63` | `2264.65` | `20562.87` | 65,128.62 USD | `+2.96%` | `25X Cross` |
| `1023` | `0x1f16...6d07` | `LONG` | 2,184,145.32 USD | `966.00` | `2278.41` | `2264.65` | `1652.93` | -16,803.82 USD | `-0.77%` | `7X Cross` |
| `1026` | `0xb002...ed8a` | `SHORT` | 2,177,624.85 USD | `962.78` | `2299.66` | `2264.65` | `4202.26` | 36,453.06 USD | `+1.67%` | `25X Cross` |
| `1031` | `0xb812...b5e0` | `LONG` | 2,165,116.11 USD | `955.65` | `2264.26` | `2264.65` | `1521.15` | 1,276.25 USD | `+0.06%` | `25X Cross` |
| `1052` | `0x3947...f3b1` | `LONG` | 2,101,970.21 USD | `927.78` | `2270.90` | `2264.65` | `0.000000` | -4,924.37 USD | `-0.23%` | `20X Cross` |
| `1068` | `0x9606...4e5d` | `SHORT` | 2,074,693.70 USD | `913.00` | `2478.70` | `2264.65` | `4332.57` | 188,359.90 USD | `+9.08%` | `20X Cross` |
| `1070` | `0x2e30...4cb5` | `SHORT` | 2,070,350.17 USD | `915.07` | `2337.88` | `2264.65` | `7780.01` | 68,981.40 USD | `+3.33%` | `2X Cross` |
| `1081` | `0x5f10...d49d` | `LONG` | 2,035,350.00 USD | `900.00` | `2249.83` | `2264.65` | `1820.88` | 10,496.53 USD | `+0.52%` | `25X Cross` |
| `1185` | `0xcd27...52a8` | `LONG` | 1,897,951.22 USD | `837.21` | `2553.56` | `2264.65` | `1404.12` | -239,913.56 USD | `-12.64%` | `2X Cross` |
| `1212` | `0x6ff1...8575` | `LONG` | 1,841,801.47 USD | `814.06` | `2272.53` | `2264.65` | `2227.00` | -8,168.29 USD | `-0.44%` | `25X Isolated` |
| `1230` | `0x3fc5...c0c1` | `SHORT` | 1,819,875.46 USD | `804.26` | `2702.11` | `2264.65` | `5090.18` | 353,326.07 USD | `+19.41%` | `25X Cross` |
| `1242` | `0x7737...bf66` | `SHORT` | 1,815,047.74 USD | `799.79` | `2494.83` | `2264.65` | `23501.77` | 180,298.29 USD | `+9.93%` | `15X Cross` |
| `1248` | `0x04a9...95aa` | `LONG` | 1,809,360.00 USD | `800.00` | `2595.13` | `2264.65` | `1878.34` | -266,746.74 USD | `-14.74%` | `5X Cross` |
| `1276` | `0x458d...ab3b` | `LONG` | 1,752,865.09 USD | `774.75` | `2740.41` | `2264.65` | `1887.87` | -370,264.10 USD | `-21.12%` | `3X Isolated` |
| `1322` | `0xaa7a...af37` | `LONG` | 1,657,814.12 USD | `733.29` | `2273.62` | `2264.65` | `0.000000` | -9,404.09 USD | `-0.57%` | `20X Cross` |
| `1332` | `0xaa53...9cb7` | `LONG` | 1,651,656.45 USD | `730.34` | `2389.70` | `2264.65` | `1929.76` | -93,633.19 USD | `-5.67%` | `20X Cross` |
| `1354` | `0xa189...94d7` | `SHORT` | 1,628,304.51 USD | `719.98` | `2691.84` | `2264.65` | `3051.83` | 309,768.16 USD | `+19.02%` | `25X Cross` |
| `1355` | `0xf83f...625f` | `SHORT` | 1,625,699.86 USD | `717.56` | `2595.19` | `2264.65` | `6590.29` | 236,500.89 USD | `+14.55%` | `20X Cross` |
| `1376` | `0x2f93...4404` | `LONG` | 1,602,847.43 USD | `707.47` | `1700.45` | `2264.65` | `1369.50` | 399,821.06 USD | `+24.94%` | `4X Isolated` |
| `1383` | `0x5605...fe0f` | `SHORT` | 1,588,417.34 USD | `702.14` | `2566.90` | `2264.65` | `3094.64` | 213,915.31 USD | `+13.47%` | `20X Cross` |
| `1386` | `0x0deb...0bc5` | `LONG` | 1,583,400.00 USD | `700.00` | `2071.05` | `2264.65` | `1598.09` | 133,664.21 USD | `+8.44%` | `20X Cross` |
| `1429` | `0xdbd1...29dd` | `SHORT` | 1,540,565.90 USD | `680.70` | `3030.57` | `2264.65` | `4110.75` | 522,355.23 USD | `+33.91%` | `6X Cross` |
| `1432` | `0x7b7f...dee2` | `LONG` | 1,539,374.51 USD | `679.37` | `2268.61` | `2264.65` | `0.000000` | -1,847.30 USD | `-0.12%` | `20X Cross` |
| `1442` | `0x71e5...be04` | `LONG` | 1,532,882.30 USD | `677.67` | `2727.27` | `2264.65` | `1471.65` | -315,303.30 USD | `-20.57%` | `20X Cross` |
| `1443` | `0x0b23...f37b` | `LONG` | 1,531,845.00 USD | `675.00` | `2238.15` | `2264.65` | `599.74` | 21,088.36 USD | `+1.38%` | `5X Cross` |
| `1450` | `0x72d0...62ea` | `LONG` | 1,516,982.55 USD | `669.57` | `2269.07` | `2264.65` | `194.48` | -2,326.54 USD | `-0.15%` | `5X Cross` |
| `1466` | `0x823e...76c9` | `LONG` | 1,493,007.69 USD | `659.89` | `2263.69` | `2264.65` | `2218.68` | -791.79 USD | `-0.05%` | `25X Cross` |
| `1470` | `0x0cac...6170` | `SHORT` | 1,487,593.75 USD | `657.50` | `2146.55` | `2264.65` | `2840.07` | -76,231.55 USD | `-5.12%` | `20X Cross` |
| `1499` | `0x621c...63ab` | `LONG` | 1,456,672.32 USD | `642.98` | `2281.90` | `2264.65` | `0.000000` | -10,551.08 USD | `-0.72%` | `20X Cross` |
| `1500` | `0xffb2...5ed6` | `SHORT` | 1,456,014.40 USD | `640.77` | `2672.96` | `2264.65` | `2497.03` | 256,733.95 USD | `+17.63%` | `20X Cross` |
| `1503` | `0xf00e...fe3d` | `SHORT` | 1,454,130.27 USD | `642.88` | `2333.21` | `2264.65` | `2546.37` | 45,847.70 USD | `+3.15%` | `20X Cross` |
| `1536` | `0x871f...972b` | `SHORT` | 1,417,679.98 USD | `626.77` | `2279.80` | `2264.65` | `2570.83` | 11,221.85 USD | `+0.79%` | `20X Cross` |
| `1548` | `0xfce0...f4c0` | `SHORT` | 1,410,895.00 USD | `623.60` | `3129.61` | `2264.65` | `2788.32` | 540,731.58 USD | `+38.33%` | `20X Cross` |
| `1570` | `0x7663...cb5a` | `SHORT` | 1,388,129.27 USD | `613.54` | `2342.35` | `2264.65` | `3789.94` | 48,991.21 USD | `+3.53%` | `3X Cross` |
| `1591` | `0x67c3...609d` | `SHORT` | 1,364,340.00 USD | `600.00` | `2386.55` | `2264.65` | `2560.74` | 67,591.89 USD | `+4.95%` | `25X Cross` |
| `1598` | `0x638f...f5f0` | `LONG` | 1,358,940.00 USD | `600.00` | `4011.50` | `2264.65` | `339.89` | -1,047,963.53 USD | `-77.12%` | `25X Cross` |
| `1599` | `0xad02...eb65` | `LONG` | 1,358,422.71 USD | `600.62` | `2460.69` | `2264.65` | `1079.57` | -119,517.85 USD | `-8.80%` | `5X Cross` |
| `1601` | `0x26e6...6b28` | `LONG` | 1,357,680.00 USD | `600.00` | `1769.78` | `2264.65` | `2005.37` | 295,808.47 USD | `+21.79%` | `20X Cross` |
| `1603` | `0x51a0...3543` | `SHORT` | 1,353,140.56 USD | `597.28` | `2627.71` | `2264.65` | `8512.39` | 216,341.64 USD | `+15.99%` | `20X Cross` |
| `1608` | `0x7c90...d129` | `LONG` | 1,344,075.35 USD | `594.17` | `2286.01` | `2264.65` | `1856.53` | -14,207.53 USD | `-1.06%` | `20X Cross` |
| `1635` | `0xab81...c608` | `SHORT` | 1,307,809.72 USD | `577.27` | `2285.37` | `2264.65` | `6001.21` | 11,471.57 USD | `+0.88%` | `20X Cross` |
| `1650` | `0xfc66...ca06` | `SHORT` | 1,290,399.16 USD | `567.43` | `2275.19` | `2264.65` | `7283.65` | 624.05 USD | `+0.05%` | `20X Cross` |
| `1660` | `0xfb99...37f3` | `LONG` | 1,278,688.50 USD | `565.34` | `2362.35` | `2264.65` | `1238.88` | -56,847.86 USD | `-4.45%` | `3X Cross` |
| `1666` | `0x844b...7f42` | `SHORT` | 1,274,760.30 USD | `561.00` | `2026.17` | `2264.65` | `3098.03` | -138,076.89 USD | `-10.83%` | `25X Cross` |
| `1668` | `0x4b1c...bc38` | `SHORT` | 1,274,029.41 USD | `563.31` | `2528.62` | `2264.65` | `4930.13` | 150,358.25 USD | `+11.80%` | `10X Cross` |
| `1678` | `0xabe6...1d99` | `SHORT` | 1,261,295.07 USD | `556.00` | `2484.68` | `2264.65` | `3102.50` | 120,200.82 USD | `+9.53%` | `20X Cross` |
| `1743` | `0xad21...fb6a` | `LONG` | 1,202,567.12 USD | `531.87` | `2574.89` | `2264.65` | `1708.17` | -166,938.38 USD | `-13.88%` | `7X Cross` |
| `1750` | `0x0082...1ae3` | `LONG` | 1,194,758.40 USD | `528.00` | `2448.58` | `2264.65` | `2234.13` | -98,096.51 USD | `-8.21%` | `25X Cross` |
| `1801` | `0x0c7a...2f50` | `SHORT` | 1,151,413.81 USD | `509.25` | `2122.56` | `2264.65` | `4112.80` | -70,508.38 USD | `-6.12%` | `20X Cross` |
| `1805` | `0x0089...2410` | `SHORT` | 1,147,362.07 USD | `507.35` | `2308.88` | `2264.65` | `3294.37` | 24,038.18 USD | `+2.10%` | `20X Cross` |
| `1820` | `0xb322...d51f` | `SHORT` | 1,133,950.00 USD | `500.00` | `2268.03` | `2264.65` | `3760.87` | 66.32 USD | `+0.01%` | `20X Cross` |
| `1823` | `0x89b2...9ca6` | `LONG` | 1,131,250.00 USD | `500.00` | `2484.03` | `2264.65` | `1954.10` | -110,769.35 USD | `-9.79%` | `25X Cross` |
| `1824` | `0xa559...ff95` | `LONG` | 1,131,250.00 USD | `500.00` | `2260.68` | `2264.65` | `1126.58` | 905.64 USD | `+0.08%` | `20X Cross` |
| `1825` | `0x6936...9417` | `SHORT` | 1,131,250.00 USD | `500.00` | `2315.11` | `2264.65` | `2359.58` | 26,305.21 USD | `+2.33%` | `25X Isolated` |
| `1830` | `0x7298...7d6c` | `SHORT` | 1,126,415.20 USD | `498.15` | `3426.75` | `2264.65` | `5422.29` | 580,620.62 USD | `+51.55%` | `20X Cross` |
| `1837` | `0x9c68...7783` | `SHORT` | 1,115,812.91 USD | `493.31` | `2273.58` | `2264.65` | `3938.07` | 5,766.34 USD | `+0.52%` | `25X Cross` |
| `1849` | `0x7717...bd7e` | `LONG` | 1,110,064.86 USD | `489.90` | `2273.71` | `2264.65` | `0.000000` | -3,828.40 USD | `-0.34%` | `20X Cross` |
| `1850` | `0x404c...5f03` | `SHORT` | 1,110,000.43 USD | `489.79` | `2671.94` | `2264.65` | `5087.00` | 198,679.13 USD | `+17.90%` | `20X Cross` |
| `1851` | `0x321f...1c84` | `SHORT` | 1,109,200.44 USD | `488.02` | `2370.09` | `2264.65` | `3032.99` | 47,444.16 USD | `+4.28%` | `10X Cross` |
| `1856` | `0xa522...2d0e` | `SHORT` | 1,105,940.83 USD | `486.36` | `2284.42` | `2264.65` | `5008.29` | 5,120.72 USD | `+0.46%` | `20X Cross` |
| `1869` | `0xc10f...23b3` | `LONG` | 1,097,186.40 USD | `485.00` | `2383.92` | `2264.65` | `2073.72` | -59,015.27 USD | `-5.38%` | `25X Cross` |
| `1879` | `0x8923...1bac` | `SHORT` | 1,087,656.14 USD | `480.82` | `2277.43` | `2264.65` | `3145.65` | 7,371.90 USD | `+0.68%` | `25X Cross` |
| `1924` | `0x94b6...e5b3` | `SHORT` | 1,049,896.20 USD | `463.86` | `2261.12` | `2264.65` | `2395.43` | -1,053.53 USD | `-0.10%` | `25X Cross` |
| `1931` | `0x82c6...fe42` | `LONG` | 1,046,082.50 USD | `462.50` | `2501.38` | `2264.65` | `2054.35` | -110,808.07 USD | `-10.59%` | `5X Isolated` |
| `1940` | `0x2de3...486d` | `LONG` | 1,041,194.60 USD | `460.40` | `2286.27` | `2264.65` | `1265.06` | -11,406.31 USD | `-1.10%` | `25X Cross` |
| `1944` | `0x617e...0f97` | `SHORT` | 1,035,437.73 USD | `457.85` | `2205.60` | `2264.65` | `3696.43` | -25,593.89 USD | `-2.47%` | `10X Cross` |
| `1964` | `0xae55...2236` | `LONG` | 1,018,125.00 USD | `450.00` | `2510.21` | `2264.65` | `0.000000` | -111,472.50 USD | `-10.95%` | `25X Cross` |
| `1982` | `0xac26...a9c7` | `SHORT` | 1,009,299.84 USD | `446.28` | `2192.58` | `2264.65` | `8509.24` | -30,800.14 USD | `-3.05%` | `20X Cross` |
| `1983` | `0x53f8...ceff` | `LONG` | 1,008,298.02 USD | `445.60` | `2399.81` | `2264.65` | `0.000000` | -61,052.58 USD | `-6.06%` | `20X Cross` |
| `2002` | `0x8fb6...4667` | `LONG` | 1,001,017.87 USD | `442.56` | `2268.94` | `2264.65` | `88.48` | -3,119.92 USD | `-0.31%` | `20X Cross` |
| `2005` | `0x7df0...ceb3` | `SHORT` | 1,000,708.08 USD | `442.63` | `2259.20` | `2264.65` | `3533.57` | -708.22 USD | `-0.07%` | `10X Cross` |
| `2006` | `0xd8a1...6687` | `LONG` | 1,000,293.01 USD | `441.53` | `2804.24` | `2264.65` | `2150.91` | -237,875.42 USD | `-23.78%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `ANNOUNCEMENT` | `INFO` | `2354.00` | 70,620.00 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 70.62K USD at 2354.0000 USD [API] | `2026-10-28 19:17:34` |
| `ANNOUNCEMENT` | `INFO` | `2356.90` | 65,612.09 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 65.61K USD at 2356.9000 USD [API] | `2026-10-28 19:24:55` |
| `ANNOUNCEMENT` | `INFO` | `2363.20` | 40,034.50 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 40.03K USD at 2363.2000 USD [API] | `2026-10-28 19:45:20` |
| `ANNOUNCEMENT` | `INFO` | `2201.40` | 1,104.44 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.10K USD at 2201.4000 USD [API] | `2025-06-22 13:25:41` |
| `ANNOUNCEMENT` | `INFO` | `2457.00` | 1,228.50 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.23K USD at 2457.0000 USD [API] | `2025-06-20 17:20:32` |
| `ANNOUNCEMENT` | `INFO` | `2523.40` | 2,518.86 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 2.52K USD at 2523.4000 USD [API] | `2025-06-05 19:17:43` |
| `ANNOUNCEMENT` | `INFO` | `2524.60` | 3,564.74 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 3.56K USD at 2524.6000 USD [API] | `2025-05-30 22:44:53` |
| `ANNOUNCEMENT` | `INFO` | `2365.90` | 50,385.63 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 50.39K USD at 2365.9000 USD [API] | `2026-10-28 19:53:20` |
| `ANNOUNCEMENT` | `INFO` | `2365.90` | 49,871.52 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 49.87K USD at 2365.9000 USD [API] | `2026-10-28 19:53:20` |
| `ANNOUNCEMENT` | `INFO` | `2370.10` | 188,320.09 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 188.32K USD at 2370.1000 USD [API] | `2026-10-28 19:56:49` |
| `ANNOUNCEMENT` | `INFO` | `2370.10` | 135,860.77 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 135.86K USD at 2370.1000 USD [API] | `2026-10-28 19:56:49` |
| `ANNOUNCEMENT` | `INFO` | `2370.10` | 47,402.00 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 47.40K USD at 2370.1000 USD [API] | `2026-10-28 19:56:49` |
| `ANNOUNCEMENT` | `INFO` | `2368.80` | 68,619.16 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 68.62K USD at 2368.8000 USD [API] | `2026-10-28 19:59:31` |
| `ANNOUNCEMENT` | `INFO` | `2378.70` | 6.90 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.01K USD at 2378.7000 USD [API] | `2026-10-28 20:00:56` |
| `ANNOUNCEMENT` | `INFO` | `2377.10` | 627.79 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.63K USD at 2377.1000 USD [API] | `2026-10-28 20:00:18` |
| `ANNOUNCEMENT` | `INFO` | `2377.10` | 61.09 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.06K USD at 2377.1000 USD [API] | `2026-10-28 20:00:18` |
| `ANNOUNCEMENT` | `INFO` | `2371.00` | 4,789.42 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 4.79K USD at 2371.0000 USD [API] | `2026-10-28 19:57:32` |
| `ANNOUNCEMENT` | `INFO` | `2325.90` | 10,560.75 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 10.56K USD at 2325.9000 USD [API] | `2026-10-28 13:48:14` |
| `ANNOUNCEMENT` | `INFO` | `2325.90` | 23.26 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2325.9000 USD [API] | `2026-10-28 13:48:14` |
| `ANNOUNCEMENT` | `INFO` | `2325.90` | 23.26 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2325.9000 USD [API] | `2026-10-28 13:48:14` |
| `ANNOUNCEMENT` | `INFO` | `2325.90` | 43.49 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.04K USD at 2325.9000 USD [API] | `2026-10-28 13:48:14` |
| `ANNOUNCEMENT` | `INFO` | `2325.90` | 297.72 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.30K USD at 2325.9000 USD [API] | `2026-10-28 13:48:14` |
| `ANNOUNCEMENT` | `INFO` | `2325.90` | 128.16 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.13K USD at 2325.9000 USD [API] | `2026-10-28 13:48:14` |
| `ANNOUNCEMENT` | `INFO` | `2329.30` | 3,892.49 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 3.89K USD at 2329.3000 USD [API] | `2026-10-28 13:46:54` |
| `ANNOUNCEMENT` | `INFO` | `2329.30` | 23,953.59 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 23.95K USD at 2329.3000 USD [API] | `2026-10-28 13:46:54` |
| `ANNOUNCEMENT` | `INFO` | `2333.90` | 10.97 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.01K USD at 2333.9000 USD [API] | `2026-10-28 13:46:15` |
| `ANNOUNCEMENT` | `INFO` | `2388.00` | 118,053.41 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 118.05K USD at 2388.0000 USD [API] | `2026-10-28 20:01:45` |
| `ANNOUNCEMENT` | `INFO` | `2388.00` | 112,077.44 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 112.08K USD at 2388.0000 USD [API] | `2026-10-28 20:01:45` |
| `ANNOUNCEMENT` | `INFO` | `2386.00` | 4,029.00 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 4.03K USD at 2386.0000 USD [API] | `2026-10-28 20:01:41` |
| `ANNOUNCEMENT` | `INFO` | `2386.00` | 112.86 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.11K USD at 2386.0000 USD [API] | `2026-10-28 20:01:41` |
| `ANNOUNCEMENT` | `INFO` | `2386.00` | 68.48 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.07K USD at 2386.0000 USD [API] | `2026-10-28 20:01:41` |
| `ANNOUNCEMENT` | `INFO` | `2377.70` | 149,549.96 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 149.55K USD at 2377.7000 USD [API] | `2026-10-28 20:00:18` |
| `ANNOUNCEMENT` | `INFO` | `2388.00` | 13,348.92 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 13.35K USD at 2388.0000 USD [API] | `2026-10-28 20:01:45` |
| `ANNOUNCEMENT` | `INFO` | `2371.60` | 49,118.68 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 49.12K USD at 2371.6000 USD [API] | `2026-10-28 20:10:37` |
| `ANNOUNCEMENT` | `INFO` | `2376.00` | 135.43 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.14K USD at 2376.0000 USD [API] | `2026-10-28 20:00:14` |
| `ANNOUNCEMENT` | `INFO` | `2376.00` | 2,548.74 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 2.55K USD at 2376.0000 USD [API] | `2026-10-28 20:00:14` |
| `ANNOUNCEMENT` | `INFO` | `2375.80` | 5,230.80 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 5.23K USD at 2375.8000 USD [API] | `2026-10-28 20:00:13` |
| `ANNOUNCEMENT` | `INFO` | `2375.80` | 6,927.60 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 6.93K USD at 2375.8000 USD [API] | `2026-10-28 20:00:13` |
| `ANNOUNCEMENT` | `INFO` | `2375.80` | 13,316.60 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 13.32K USD at 2375.8000 USD [API] | `2026-10-28 20:00:13` |
| `ANNOUNCEMENT` | `INFO` | `2375.70` | 23,030.04 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 23.03K USD at 2375.7000 USD [API] | `2026-10-28 20:00:13` |
| `ANNOUNCEMENT` | `INFO` | `2375.60` | 12,319.15 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 12.32K USD at 2375.6000 USD [API] | `2026-10-28 20:00:13` |
| `ANNOUNCEMENT` | `INFO` | `2375.00` | 8,209.19 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 8.21K USD at 2375.0000 USD [API] | `2026-10-28 20:00:08` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`2303.89` (Vol: 21,900,000.00 USD, Dist: `+1.28%`) | Long MP=`2242.01` (Vol: 29,100,000.00 USD, Dist: `--1.44%`)
  * 48H Horizon: Short MP=`2402.77` (Vol: 36,200,000.00 USD, Dist: `+5.62%`) | Long MP=`2242.90` (Vol: 29,100,000.00 USD, Dist: `--1.40%`)
  * 3D Horizon: Short MP=`2402.77` (Vol: 36,700,000.00 USD, Dist: `+5.62%`) | Long MP=`2242.90` (Vol: 29,100,000.00 USD, Dist: `--1.40%`)
  * 7D Horizon: Short MP=`2393.80` (Vol: 49,300,000.00 USD, Dist: `+5.23%`) | Long MP=`2241.80` (Vol: 29,100,000.00 USD, Dist: `--1.45%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `455.00` | 160,750.00 USD | 865,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `465.00` | 11,230.00 USD | 865,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `475.00` | 10,340.00 USD | 865,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.00` | 1,930.00 USD | 865,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `495.00` | 1,770,000.00 USD | 865,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.00` | 23,450.00 USD | 863,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.00` | 5,850.00 USD | 863,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.00` | 992.04 USD | 863,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.00` | 1,900.00 USD | 863,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.00` | 1,650,000.00 USD | 863,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.00` | 73,450.00 USD | 862,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `565.00` | 25,410.00 USD | 861,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `575.00` | 712,960.00 USD | 861,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.00` | 954,130.00 USD | 861,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.00` | 407,770.00 USD | 860,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `605.00` | 30,250.00 USD | 859,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.00` | 17,690.00 USD | 859,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.00` | 5,400.00 USD | 859,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.00` | 5,170.00 USD | 859,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `645.00` | 7,490.00 USD | 859,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `655.00` | 31,090.00 USD | 859,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `665.00` | 49,240.00 USD | 859,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `675.00` | 55,300.00 USD | 859,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `685.00` | 54,590.00 USD | 859,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `695.00` | 6,870.00 USD | 859,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `705.00` | 24,470.00 USD | 859,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `715.00` | 1,440.00 USD | 859,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `725.00` | 390,570.00 USD | 859,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `735.00` | 56,790.00 USD | 859,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `745.00` | 15,300.00 USD | 859,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `755.00` | 39,840.00 USD | 859,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `765.00` | 66,870.00 USD | 859,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `775.00` | 33,450.00 USD | 859,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `785.00` | 93,970.00 USD | 858,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `795.00` | 1,620.00 USD | 858,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `805.00` | 60,820.00 USD | 858,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `815.00` | 16,590.00 USD | 858,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `825.00` | 149,370.00 USD | 858,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `835.00` | 43,440.00 USD | 858,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `845.00` | 466,890.00 USD | 858,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `855.00` | 25,890.00 USD | 858,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `865.00` | 164,020.00 USD | 858,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `875.00` | 45,750.00 USD | 857,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `885.00` | 945,020.00 USD | 857,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `895.00` | 302,490.00 USD | 856,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `905.00` | 47,080.00 USD | 856,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `915.00` | 161,630.00 USD | 856,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `925.00` | 144,890.00 USD | 856,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `935.00` | 377,130.00 USD | 856,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `945.00` | 86,300.00 USD | 855,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `955.00` | 17,370.00 USD | 855,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `965.00` | 317,920.00 USD | 855,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `975.00` | 367,230.00 USD | 855,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `985.00` | 12,830.00 USD | 855,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `995.00` | 112,050.00 USD | 855,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1005.00` | 109,480.00 USD | 855,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1015.00` | 63,030.00 USD | 854,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1025.00` | 120,320.00 USD | 854,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1035.00` | 36,820.00 USD | 854,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1045.00` | 7,730,000.00 USD | 854,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1055.00` | 14,950.00 USD | 846,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1065.00` | 134,880.00 USD | 846,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1075.00` | 2,650,000.00 USD | 846,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1085.00` | 976,670.00 USD | 844,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1095.00` | 74,990.00 USD | 843,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1105.00` | 178,170.00 USD | 843,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1115.00` | 346,470.00 USD | 842,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1125.00` | 10,360,000.00 USD | 842,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1135.00` | 186,700.00 USD | 832,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1145.00` | 275,100.00 USD | 832,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1155.00` | 1,860,000.00 USD | 831,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1165.00` | 131,750.00 USD | 829,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1175.00` | 7,370,000.00 USD | 829,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1185.00` | 143,160.00 USD | 822,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1195.00` | 335,690.00 USD | 822,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1205.00` | 362,060.00 USD | 821,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1215.00` | 255,010.00 USD | 821,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1225.00` | 292,720.00 USD | 821,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1235.00` | 935,800.00 USD | 821,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1245.00` | 222,700.00 USD | 820,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1255.00` | 2,300,000.00 USD | 819,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1265.00` | 263,070.00 USD | 817,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1275.00` | 966,910.00 USD | 817,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1285.00` | 15,630,000.00 USD | 816,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1295.00` | 181,060.00 USD | 800,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1305.00` | 439,590.00 USD | 800,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1315.00` | 118,750.00 USD | 800,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1325.00` | 522,200.00 USD | 799,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1335.00` | 376,840.00 USD | 799,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1345.00` | 749,590.00 USD | 799,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1355.00` | 202,460.00 USD | 798,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1365.00` | 1,090,000.00 USD | 798,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1375.00` | 337,380.00 USD | 797,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1385.00` | 6,950,000.00 USD | 796,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1395.00` | 167,840.00 USD | 789,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1405.00` | 10,150,000.00 USD | 789,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1415.00` | 13,100,000.00 USD | 779,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1425.00` | 425,740.00 USD | 766,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1435.00` | 1,730,000.00 USD | 765,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1445.00` | 1,090,000.00 USD | 764,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1455.00` | 96,230.00 USD | 763,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1465.00` | 4,900,000.00 USD | 762,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1475.00` | 5,700,000.00 USD | 758,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1485.00` | 120,280.00 USD | 752,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1495.00` | 4,010,000.00 USD | 752,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1505.00` | 16,550,000.00 USD | 748,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1515.00` | 22,140,000.00 USD | 731,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1525.00` | 18,600,000.00 USD | 709,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1535.00` | 8,600,000.00 USD | 690,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1545.00` | 4,980,000.00 USD | 682,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1555.00` | 374,830.00 USD | 677,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1565.00` | 282,150.00 USD | 677,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1575.00` | 318,000.00 USD | 676,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1585.00` | 962,940.00 USD | 676,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1595.00` | 2,570,000.00 USD | 675,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1605.00` | 18,310,000.00 USD | 672,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1615.00` | 485,170.00 USD | 654,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1625.00` | 634,930.00 USD | 654,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1635.00` | 18,550,000.00 USD | 653,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1645.00` | 49,240,000.00 USD | 634,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1655.00` | 10,740,000.00 USD | 585,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1665.00` | 710,320.00 USD | 574,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1675.00` | 11,660,000.00 USD | 574,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1685.00` | 1,070,000.00 USD | 562,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1695.00` | 27,830,000.00 USD | 561,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1705.00` | 2,200,000.00 USD | 533,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1715.00` | 17,350,000.00 USD | 531,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1725.00` | 17,790,000.00 USD | 514,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1735.00` | 375,500.00 USD | 496,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1745.00` | 885,560.00 USD | 495,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1755.00` | 491,240.00 USD | 495,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1765.00` | 460,750.00 USD | 494,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1775.00` | 1,110,000.00 USD | 494,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1785.00` | 54,900,000.00 USD | 492,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1795.00` | 386,030.00 USD | 438,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1805.00` | 16,360,000.00 USD | 437,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1815.00` | 2,470,000.00 USD | 421,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1825.00` | 1,430,000.00 USD | 418,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1835.00` | 892,470.00 USD | 417,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1845.00` | 394,260.00 USD | 416,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1855.00` | 2,930,000.00 USD | 416,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1865.00` | 5,380,000.00 USD | 413,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1875.00` | 7,600,000.00 USD | 407,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1885.00` | 2,590,000.00 USD | 400,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1895.00` | 5,400,000.00 USD | 397,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1905.00` | 903,170.00 USD | 392,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1915.00` | 13,210,000.00 USD | 391,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1925.00` | 16,400,000.00 USD | 378,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1935.00` | 2,790,000.00 USD | 361,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1945.00` | 1,640,000.00 USD | 358,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1955.00` | 5,430,000.00 USD | 357,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1965.00` | 4,950,000.00 USD | 351,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1975.00` | 1,180,000.00 USD | 346,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1985.00` | 5,600,000.00 USD | 345,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1995.00` | 1,340,000.00 USD | 340,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2005.00` | 2,120,000.00 USD | 338,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2015.00` | 11,980,000.00 USD | 336,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2025.00` | 5,030,000.00 USD | 324,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2025.30` | 942,070,000.00 USD | 942,070,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2026.90` | 513,860,000.00 USD | 513,860,000.00 USD | 0.00 USD | 943,590.00 USD | 40,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2028.60` | 941,890,000.00 USD | 941,890,000.00 USD | 0.00 USD | 1,180,000.00 USD | 35,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2029.50` | 512,870,000.00 USD | 512,870,000.00 USD | 87,180.00 USD | 163,200.00 USD | 43,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2031.90` | 940,670,000.00 USD | 940,670,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2032.10` | 512,580,000.00 USD | 512,580,000.00 USD | 1,360,000.00 USD | 542,800.00 USD | 408,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2034.70` | 510,260,000.00 USD | 510,260,000.00 USD | 1,030,000.00 USD | 787,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2035.00` | 906,040.00 USD | 319,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2035.20` | 939,220,000.00 USD | 939,220,000.00 USD | 146,420.00 USD | 186,130.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2037.30` | 508,440,000.00 USD | 508,440,000.00 USD | 202,200.00 USD | 300,240.00 USD | 348,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2038.50` | 937,540,000.00 USD | 937,540,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2039.90` | 507,590,000.00 USD | 507,590,000.00 USD | 138,370.00 USD | 178,560.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2042.50` | 507,250,000.00 USD | 507,250,000.00 USD | 0.00 USD | 0.00 USD | 12,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2045.00` | 18,320,000.00 USD | 318,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2045.10` | 507,240,000.00 USD | 507,240,000.00 USD | 0.00 USD | 0.00 USD | 35,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2045.10` | 936,080,000.00 USD | 936,080,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2047.70` | 507,200,000.00 USD | 507,200,000.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2050.30` | 506,380,000.00 USD | 506,380,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2051.70` | 935,780,000.00 USD | 935,780,000.00 USD | 1,320,000.00 USD | 0.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2052.90` | 505,270,000.00 USD | 505,270,000.00 USD | 0.00 USD | 0.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2055.00` | 5,060,000.00 USD | 300,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2055.50` | 505,240,000.00 USD | 505,240,000.00 USD | 242,080.00 USD | 88,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2058.10` | 504,910,000.00 USD | 504,910,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2058.30` | 933,280,000.00 USD | 933,280,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2061.60` | 932,930,000.00 USD | 932,930,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2063.30` | 504,160,000.00 USD | 504,160,000.00 USD | 643,750.00 USD | 173,370.00 USD | 620,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2064.90` | 927,680,000.00 USD | 927,680,000.00 USD | 1,230,000.00 USD | 313,000.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2065.00` | 1,460,000.00 USD | 295,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2065.90` | 502,720,000.00 USD | 502,720,000.00 USD | 808,950.00 USD | 485,130.00 USD | 53,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2068.20` | 925,150,000.00 USD | 925,150,000.00 USD | 1,740,000.00 USD | 1,860,000.00 USD | 893,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2068.50` | 501,370,000.00 USD | 501,370,000.00 USD | 57,300.00 USD | 1,330,000.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2071.10` | 499,960,000.00 USD | 499,960,000.00 USD | 1,040,000.00 USD | 534,600.00 USD | 437,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2071.50` | 920,650,000.00 USD | 920,650,000.00 USD | 2,820,000.00 USD | 2,410,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2073.70` | 497,940,000.00 USD | 497,940,000.00 USD | 419,970.00 USD | 62,630.00 USD | 926,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2074.80` | 914,190,000.00 USD | 914,190,000.00 USD | 4,370,000.00 USD | 3,270,000.00 USD | 4,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 3,300,000.00 USD | 293,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2076.30` | 496,530,000.00 USD | 496,530,000.00 USD | 2,580,000.00 USD | 926,330.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2078.10` | 902,490,000.00 USD | 902,490,000.00 USD | 5,560,000.00 USD | 4,320,000.00 USD | 2,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2078.90` | 491,410,000.00 USD | 491,410,000.00 USD | 1,320,000.00 USD | 1,100,000.00 USD | 816,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2081.40` | 890,210,000.00 USD | 890,210,000.00 USD | 4,720,000.00 USD | 3,420,000.00 USD | 2,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2081.50` | 488,160,000.00 USD | 488,160,000.00 USD | 1,430,000.00 USD | 1,260,000.00 USD | 227,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2084.10` | 485,250,000.00 USD | 485,250,000.00 USD | 2,090,000.00 USD | 1,290,000.00 USD | 753,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2084.70` | 879,570,000.00 USD | 879,570,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 4,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 974,560.00 USD | 290,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2086.70` | 481,120,000.00 USD | 481,120,000.00 USD | 1,600,000.00 USD | 1,650,000.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2088.00` | 870,770,000.00 USD | 870,770,000.00 USD | 3,990,000.00 USD | 2,780,000.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2089.30` | 476,270,000.00 USD | 476,270,000.00 USD | 1,080,000.00 USD | 220,540.00 USD | 90,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2091.30` | 862,350,000.00 USD | 862,350,000.00 USD | 4,410,000.00 USD | 952,210.00 USD | 7,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2091.90` | 474,880,000.00 USD | 474,880,000.00 USD | 1,130,000.00 USD | 514,440.00 USD | 957,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2094.50` | 472,270,000.00 USD | 472,270,000.00 USD | 2,040,000.00 USD | 1,120,000.00 USD | 1,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2094.60` | 849,390,000.00 USD | 849,390,000.00 USD | 5,720,000.00 USD | 2,160,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 2,220,000.00 USD | 289,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2097.10` | 467,800,000.00 USD | 467,800,000.00 USD | 617,040.00 USD | 712,710.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2097.90` | 839,170,000.00 USD | 839,170,000.00 USD | 2,340,000.00 USD | 3,210,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2099.70` | 465,360,000.00 USD | 465,360,000.00 USD | 172,210.00 USD | 700,850.00 USD | 11,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2101.20` | 832,330,000.00 USD | 832,330,000.00 USD | 999,530.00 USD | 1,580,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2102.30` | 464,480,000.00 USD | 464,480,000.00 USD | 507,510.00 USD | 289,160.00 USD | 466,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2104.50` | 825,730,000.00 USD | 825,730,000.00 USD | 2,010,000.00 USD | 1,180,000.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2104.90` | 463,210,000.00 USD | 463,210,000.00 USD | 612,280.00 USD | 671,930.00 USD | 30,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 1,740,000.00 USD | 287,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2107.50` | 461,900,000.00 USD | 461,900,000.00 USD | 546,100.00 USD | 0.00 USD | 488,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2107.80` | 820,290,000.00 USD | 820,290,000.00 USD | 2,380,000.00 USD | 452,470.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2110.10` | 460,860,000.00 USD | 460,860,000.00 USD | 118,210.00 USD | 31,550.00 USD | 196,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2111.10` | 815,810,000.00 USD | 815,810,000.00 USD | 3,530,000.00 USD | 2,350,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2112.70` | 460,520,000.00 USD | 460,520,000.00 USD | 911,810.00 USD | 643,210.00 USD | 224,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2114.40` | 807,760,000.00 USD | 807,760,000.00 USD | 1,080,000.00 USD | 1,850,000.00 USD | 3,800,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 1,360,000.00 USD | 285,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2115.30` | 458,740,000.00 USD | 458,740,000.00 USD | 0.00 USD | 13,230.00 USD | 426,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2117.70` | 801,030,000.00 USD | 801,030,000.00 USD | 3,430,000.00 USD | 2,020,000.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2117.90` | 458,300,000.00 USD | 458,300,000.00 USD | 202,840.00 USD | 2,100.00 USD | 472,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2120.50` | 457,620,000.00 USD | 457,620,000.00 USD | 744,340.00 USD | 230,360.00 USD | 997,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2121.00` | 792,200,000.00 USD | 792,200,000.00 USD | 3,650,000.00 USD | 1,340,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2123.10` | 455,650,000.00 USD | 455,650,000.00 USD | 766,550.00 USD | 1,210,000.00 USD | 976,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2124.30` | 785,390,000.00 USD | 785,390,000.00 USD | 832,850.00 USD | 972,650.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 18,610,000.00 USD | 284,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2125.70` | 452,700,000.00 USD | 452,700,000.00 USD | 173,130.00 USD | 636,520.00 USD | 320,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2127.60` | 782,070,000.00 USD | 782,070,000.00 USD | 2,400,000.00 USD | 2,630,000.00 USD | 3,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2128.30` | 451,570,000.00 USD | 451,570,000.00 USD | 107,010.00 USD | 475,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2130.90` | 450,990,000.00 USD | 450,990,000.00 USD | 0.00 USD | 18,610.00 USD | 331,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2130.90` | 773,770,000.00 USD | 773,770,000.00 USD | 2,410,000.00 USD | 2,300,000.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2134.20` | 767,360,000.00 USD | 767,360,000.00 USD | 2,170,000.00 USD | 550,450.00 USD | 308,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 14,450,000.00 USD | 265,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2136.10` | 450,640,000.00 USD | 450,640,000.00 USD | 0.00 USD | 278,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2137.50` | 764,330,000.00 USD | 764,330,000.00 USD | 1,040,000.00 USD | 880,790.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2140.80` | 762,360,000.00 USD | 762,360,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2144.10` | 758,430,000.00 USD | 758,430,000.00 USD | 449,020.00 USD | 1,130,000.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 5,830,000.00 USD | 251,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2147.40` | 756,580,000.00 USD | 756,580,000.00 USD | 657,710.00 USD | 421,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2150.70` | 755,500,000.00 USD | 755,500,000.00 USD | 459,630.00 USD | 463,640.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2151.70` | 450,360,000.00 USD | 450,360,000.00 USD | 208,250.00 USD | 440,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2154.00` | 754,550,000.00 USD | 754,550,000.00 USD | 128,430.00 USD | 311,060.00 USD | 32,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2154.30` | 449,710,000.00 USD | 449,710,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 2,520,000.00 USD | 245,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2157.30` | 754,080,000.00 USD | 754,080,000.00 USD | 388,210.00 USD | 1,030,000.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2159.50` | 448,310,000.00 USD | 448,310,000.00 USD | 0.00 USD | 0.00 USD | 37,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2160.60` | 751,580,000.00 USD | 751,580,000.00 USD | 613,630.00 USD | 1,900,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2162.10` | 448,270,000.00 USD | 448,270,000.00 USD | 0.00 USD | 3,220,000.00 USD | 100,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2163.90` | 747,070,000.00 USD | 747,070,000.00 USD | 566,120.00 USD | 2,950,000.00 USD | 540,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2164.70` | 444,950,000.00 USD | 444,950,000.00 USD | 217,960.00 USD | 408,000.00 USD | 107,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 6,850,000.00 USD | 242,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2167.20` | 743,010,000.00 USD | 743,010,000.00 USD | 25,540.00 USD | 3,620,000.00 USD | 50,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2167.30` | 444,220,000.00 USD | 444,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2169.90` | 439,980,000.00 USD | 439,980,000.00 USD | 5,210,000.00 USD | 5,170,000.00 USD | 2,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2170.50` | 739,310,000.00 USD | 739,310,000.00 USD | 3,500,000.00 USD | 3,730,000.00 USD | 5,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2172.50` | 426,850,000.00 USD | 426,850,000.00 USD | 0.00 USD | 1,230,000.00 USD | 497,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2173.80` | 726,860,000.00 USD | 726,860,000.00 USD | 4,370,000.00 USD | 363,040.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 108,060,000.00 USD | 236,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2175.10` | 425,120,000.00 USD | 425,120,000.00 USD | 1,150,000.00 USD | 111,190.00 USD | 870,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2177.10` | 721,130,000.00 USD | 721,130,000.00 USD | 1,750,000.00 USD | 1,330,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2177.70` | 423,000,000.00 USD | 423,000,000.00 USD | 445,430.00 USD | 1,770,000.00 USD | 99,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2180.30` | 420,680,000.00 USD | 420,680,000.00 USD | 2,080,000.00 USD | 0.00 USD | 1,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2180.40` | 715,230,000.00 USD | 715,230,000.00 USD | 0.00 USD | 373,740.00 USD | 431,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2182.90` | 417,180,000.00 USD | 417,180,000.00 USD | 2,960,000.00 USD | 1,140,000.00 USD | 425,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2183.70` | 714,420,000.00 USD | 714,420,000.00 USD | 1,760,000.00 USD | 1,310,000.00 USD | 3,950,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2185.00` | 100,190,000.00 USD | 128,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2185.50` | 412,660,000.00 USD | 412,660,000.00 USD | 566,020.00 USD | 1,110,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2187.00` | 707,410,000.00 USD | 707,410,000.00 USD | 556,600.00 USD | 0.00 USD | 54,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2188.10` | 408,300,000.00 USD | 408,300,000.00 USD | 0.00 USD | 890,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2190.30` | 706,800,000.00 USD | 706,800,000.00 USD | 2,730,000.00 USD | 0.00 USD | 4,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2190.70` | 407,410,000.00 USD | 407,410,000.00 USD | 0.00 USD | 222,200.00 USD | 764,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2193.30` | 406,420,000.00 USD | 406,420,000.00 USD | 605,210.00 USD | 0.00 USD | 39,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 1,810,000.00 USD | 27,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2195.90` | 405,780,000.00 USD | 405,780,000.00 USD | 416,500.00 USD | 881,070.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2196.90` | 699,870,000.00 USD | 699,870,000.00 USD | 2,580,000.00 USD | 474,090.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2198.50` | 402,590,000.00 USD | 402,590,000.00 USD | 0.00 USD | 149,110.00 USD | 50,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2200.20` | 694,780,000.00 USD | 694,780,000.00 USD | 3,000,000.00 USD | 5,080,000.00 USD | 3,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2201.10` | 402,390,000.00 USD | 402,390,000.00 USD | 1,690,000.00 USD | 4,250,000.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2203.50` | 683,500,000.00 USD | 683,500,000.00 USD | 3,650,000.00 USD | 1,710,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2203.70` | 394,950,000.00 USD | 394,950,000.00 USD | 2,130,000.00 USD | 107,200.00 USD | 830,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 2,440,000.00 USD | 26,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2206.30` | 391,880,000.00 USD | 391,880,000.00 USD | 755,060.00 USD | 10,890,000.00 USD | 887,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2206.80` | 674,390,000.00 USD | 674,390,000.00 USD | 6,920,000.00 USD | 9,430,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2208.90` | 379,350,000.00 USD | 379,350,000.00 USD | 2,680,000.00 USD | 2,280,000.00 USD | 3,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2210.10` | 654,020,000.00 USD | 654,020,000.00 USD | 12,800,000.00 USD | 20,410,000.00 USD | 6,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2211.50` | 371,280,000.00 USD | 371,280,000.00 USD | 6,150,000.00 USD | 2,320,000.00 USD | 3,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2213.40` | 614,340,000.00 USD | 614,340,000.00 USD | 10,920,000.00 USD | 14,590,000.00 USD | 19,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2214.10` | 358,930,000.00 USD | 358,930,000.00 USD | 14,080,000.00 USD | 10,880,000.00 USD | 6,490,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 11,410,000.00 USD | 23,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2216.70` | 327,480,000.00 USD | 327,480,000.00 USD | 11,870,000.00 USD | 8,780,000.00 USD | 8,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2216.70` | 568,880,000.00 USD | 568,880,000.00 USD | 25,710,000.00 USD | 17,030,000.00 USD | 9,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2219.30` | 298,830,000.00 USD | 298,830,000.00 USD | 6,980,000.00 USD | 8,590,000.00 USD | 2,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2220.00` | 516,750,000.00 USD | 516,750,000.00 USD | 27,820,000.00 USD | 14,950,000.00 USD | 15,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2221.90` | 280,410,000.00 USD | 280,410,000.00 USD | 6,400,000.00 USD | 12,880,000.00 USD | 2,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2223.30` | 458,220,000.00 USD | 458,220,000.00 USD | 10,150,000.00 USD | 8,220,000.00 USD | 11,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2224.50` | 259,050,000.00 USD | 259,050,000.00 USD | 10,020,000.00 USD | 4,140,000.00 USD | 4,940,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2225.00` | 5,130,000.00 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2226.60` | 427,940,000.00 USD | 427,940,000.00 USD | 16,350,000.00 USD | 11,030,000.00 USD | 10,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2227.10` | 239,950,000.00 USD | 239,950,000.00 USD | 5,090,000.00 USD | 13,450,000.00 USD | 6,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2229.70` | 215,260,000.00 USD | 215,260,000.00 USD | 10,130,000.00 USD | 7,410,000.00 USD | 4,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2229.90` | 390,090,000.00 USD | 390,090,000.00 USD | 12,730,000.00 USD | 11,790,000.00 USD | 28,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2232.30` | 193,630,000.00 USD | 193,630,000.00 USD | 4,620,000.00 USD | 4,830,000.00 USD | 6,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2233.20` | 337,020,000.00 USD | 337,020,000.00 USD | 16,600,000.00 USD | 24,290,000.00 USD | 10,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2234.90` | 177,230,000.00 USD | 177,230,000.00 USD | 19,080,000.00 USD | 1,450,000.00 USD | 11,000,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2235.00` | 2,700,000.00 USD | 7,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2236.50` | 285,700,000.00 USD | 285,700,000.00 USD | 16,050,000.00 USD | 7,430,000.00 USD | 27,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2237.50` | 145,690,000.00 USD | 145,690,000.00 USD | 22,650,000.00 USD | 5,930,000.00 USD | 13,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2239.80` | 234,460,000.00 USD | 234,460,000.00 USD | 16,720,000.00 USD | 6,600,000.00 USD | 13,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2240.10` | 103,890,000.00 USD | 103,890,000.00 USD | 2,060,000.00 USD | 2,600,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2242.70` | 97,250,000.00 USD | 97,250,000.00 USD | 5,750,000.00 USD | 3,760,000.00 USD | 9,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2243.10` | 197,390,000.00 USD | 197,390,000.00 USD | 29,940,000.00 USD | 5,310,000.00 USD | 24,330,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2245.00` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2245.30` | 78,700,000.00 USD | 78,700,000.00 USD | 3,700,000.00 USD | 6,190,000.00 USD | 381,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2246.40` | 137,820,000.00 USD | 137,820,000.00 USD | 14,340,000.00 USD | 0.00 USD | 13,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2247.90` | 68,440,000.00 USD | 68,440,000.00 USD | 12,490,000.00 USD | 0.00 USD | 7,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2249.70` | 109,560,000.00 USD | 109,560,000.00 USD | 25,030,000.00 USD | 0.00 USD | 19,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2250.50` | 48,710,000.00 USD | 48,710,000.00 USD | 4,450,000.00 USD | 4,540,000.00 USD | 5,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2253.00` | 65,090,000.00 USD | 65,090,000.00 USD | 26,890,000.00 USD | 0.00 USD | 12,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2253.10` | 34,100,000.00 USD | 34,100,000.00 USD | 13,840,000.00 USD | 4,440,000.00 USD | 8,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2255.70` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 3,390,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2256.30` | 26,160,000.00 USD | 26,160,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2258.30` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 170,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2259.60` | 10,940,000.00 USD | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2260.90` | 4,140,000.00 USD | 4,140,000.00 USD | 2,420,000.00 USD | 0.00 USD | 156,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2265.00` | 866.59 USD | 866.59 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2266.10` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2268.70` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 2,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2273.90` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 288,080.00 USD | 114,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2275.00` | 3,220.00 USD | 3,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2276.50` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 267,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2279.10` | 23,520,000.00 USD | 23,520,000.00 USD | 11,600,000.00 USD | 3,950,000.00 USD | 4,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2279.40` | 17,000,000.00 USD | 17,000,000.00 USD | 0.00 USD | 17,000,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2281.70` | 84,770,000.00 USD | 84,770,000.00 USD | 33,480,000.00 USD | 25,270,000.00 USD | 2,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2282.70` | 117,630,000.00 USD | 117,630,000.00 USD | 0.00 USD | 87,090,000.00 USD | 13,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2284.30` | 152,740,000.00 USD | 152,740,000.00 USD | 32,760,000.00 USD | 20,940,000.00 USD | 14,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2285.00` | 20,390.00 USD | 23,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2286.00` | 128,050,000.00 USD | 128,050,000.00 USD | 1,010,000.00 USD | 9,400,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2286.90` | 164,340,000.00 USD | 164,340,000.00 USD | 3,210,000.00 USD | 4,900,000.00 USD | 3,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2289.30` | 151,650,000.00 USD | 151,650,000.00 USD | 7,010,000.00 USD | 5,310,000.00 USD | 11,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2289.50` | 173,390,000.00 USD | 173,390,000.00 USD | 0.00 USD | 8,840,000.00 USD | 219,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2292.10` | 181,560,000.00 USD | 181,560,000.00 USD | 6,500,000.00 USD | 1,490,000.00 USD | 176,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2292.60` | 152,670,000.00 USD | 152,670,000.00 USD | 0.00 USD | 0.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2294.70` | 197,490,000.00 USD | 197,490,000.00 USD | 3,590,000.00 USD | 6,490,000.00 USD | 5,860,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2295.00` | 2,620,000.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2295.90` | 179,980,000.00 USD | 179,980,000.00 USD | 13,610,000.00 USD | 2,380,000.00 USD | 11,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2297.30` | 221,250,000.00 USD | 221,250,000.00 USD | 11,830,000.00 USD | 6,530,000.00 USD | 5,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2299.20` | 208,390,000.00 USD | 208,390,000.00 USD | 11,730,000.00 USD | 11,130,000.00 USD | 5,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2299.90` | 236,840,000.00 USD | 236,840,000.00 USD | 2,260,000.00 USD | 5,930,000.00 USD | 7,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2302.50` | 257,830,000.00 USD | 257,830,000.00 USD | 15,230,000.00 USD | 852,700.00 USD | 4,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2302.50` | 255,510,000.00 USD | 255,510,000.00 USD | 23,020,000.00 USD | 7,250,000.00 USD | 16,850,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2305.00` | 4,350,000.00 USD | 6,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2305.10` | 286,870,000.00 USD | 286,870,000.00 USD | 10,430,000.00 USD | 14,090,000.00 USD | 4,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2305.80` | 276,280,000.00 USD | 276,280,000.00 USD | 2,980,000.00 USD | 8,820,000.00 USD | 8,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2307.70` | 295,180,000.00 USD | 295,180,000.00 USD | 2,420,000.00 USD | 3,500,000.00 USD | 2,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2309.10` | 280,560,000.00 USD | 280,560,000.00 USD | 1,240,000.00 USD | 930,630.00 USD | 2,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2310.30` | 309,220,000.00 USD | 309,220,000.00 USD | 2,300,000.00 USD | 2,450,000.00 USD | 9,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2312.40` | 307,860,000.00 USD | 307,860,000.00 USD | 10,780,000.00 USD | 2,650,000.00 USD | 13,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2312.90` | 317,160,000.00 USD | 317,160,000.00 USD | 890,860.00 USD | 6,730,000.00 USD | 313,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2315.00` | 2,780,000.00 USD | 9,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2315.50` | 343,460,000.00 USD | 343,460,000.00 USD | 9,790,000.00 USD | 9,890,000.00 USD | 6,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2315.70` | 315,940,000.00 USD | 315,940,000.00 USD | 0.00 USD | 7,460,000.00 USD | 627,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2318.10` | 360,870,000.00 USD | 360,870,000.00 USD | 4,440,000.00 USD | 10,740,000.00 USD | 2,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2319.00` | 333,450,000.00 USD | 333,450,000.00 USD | 4,540,000.00 USD | 4,550,000.00 USD | 8,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2320.70` | 378,520,000.00 USD | 378,520,000.00 USD | 5,790,000.00 USD | 9,890,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2322.30` | 350,600,000.00 USD | 350,600,000.00 USD | 1,110,000.00 USD | 15,930,000.00 USD | 108,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2323.30` | 394,220,000.00 USD | 394,220,000.00 USD | 1,710,000.00 USD | 10,410,000.00 USD | 3,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2325.00` | 1,180,000.00 USD | 10,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2325.60` | 371,260,000.00 USD | 371,260,000.00 USD | 9,720,000.00 USD | 2,540,000.00 USD | 8,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2325.90` | 405,990,000.00 USD | 405,990,000.00 USD | 479,120.00 USD | 5,640,000.00 USD | 5,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2328.50` | 408,980,000.00 USD | 408,980,000.00 USD | 2,140,000.00 USD | 444,400.00 USD | 402,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2328.90` | 383,080,000.00 USD | 383,080,000.00 USD | 3,860,000.00 USD | 0.00 USD | 7,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2331.10` | 427,150,000.00 USD | 427,150,000.00 USD | 17,350,000.00 USD | 692,470.00 USD | 126,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2332.20` | 412,310,000.00 USD | 412,310,000.00 USD | 29,230,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2333.70` | 443,360,000.00 USD | 443,360,000.00 USD | 6,250,000.00 USD | 2,820,000.00 USD | 7,150,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2335.00` | 762,050.00 USD | 11,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2335.50` | 470,320,000.00 USD | 470,320,000.00 USD | 28,990,000.00 USD | 18,420,000.00 USD | 10,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2336.30` | 463,500,000.00 USD | 463,500,000.00 USD | 17,400,000.00 USD | 547,950.00 USD | 2,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2338.80` | 488,200,000.00 USD | 488,200,000.00 USD | 9,570,000.00 USD | 0.00 USD | 8,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2338.90` | 476,510,000.00 USD | 476,510,000.00 USD | 6,360,000.00 USD | 2,600,000.00 USD | 4,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2341.50` | 495,170,000.00 USD | 495,170,000.00 USD | 5,340,000.00 USD | 3,430,000.00 USD | 9,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2342.10` | 528,300,000.00 USD | 528,300,000.00 USD | 4,720,000.00 USD | 21,390,000.00 USD | 14,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2344.10` | 508,500,000.00 USD | 508,500,000.00 USD | 1,370,000.00 USD | 6,240,000.00 USD | 5,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2345.00` | 1,210,000.00 USD | 12,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2345.40` | 549,670,000.00 USD | 549,670,000.00 USD | 1,350,000.00 USD | 13,990,000.00 USD | 6,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2346.70` | 519,400,000.00 USD | 519,400,000.00 USD | 3,930,000.00 USD | 341,240.00 USD | 6,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2348.70` | 587,550,000.00 USD | 587,550,000.00 USD | 847,620.00 USD | 9,500,000.00 USD | 27,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2349.30` | 550,410,000.00 USD | 550,410,000.00 USD | 19,450,000.00 USD | 6,150,000.00 USD | 5,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2351.90` | 579,570,000.00 USD | 579,570,000.00 USD | 17,620,000.00 USD | 4,590,000.00 USD | 6,940,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2352.00` | 624,170,000.00 USD | 624,170,000.00 USD | 2,930,000.00 USD | 23,060,000.00 USD | 10,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2354.50` | 602,430,000.00 USD | 602,430,000.00 USD | 1,710,000.00 USD | 18,970,000.00 USD | 2,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 1,320,000.00 USD | 14,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2355.30` | 683,600,000.00 USD | 683,600,000.00 USD | 18,530,000.00 USD | 38,020,000.00 USD | 2,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2357.10` | 612,610,000.00 USD | 612,610,000.00 USD | 3,570,000.00 USD | 3,100,000.00 USD | 3,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2358.60` | 695,730,000.00 USD | 695,730,000.00 USD | 7,110,000.00 USD | 512,220.00 USD | 4,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2359.70` | 631,440,000.00 USD | 631,440,000.00 USD | 7,040,000.00 USD | 6,750,000.00 USD | 5,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2361.90` | 703,110,000.00 USD | 703,110,000.00 USD | 3,150,000.00 USD | 3,800,000.00 USD | 431,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2362.30` | 649,600,000.00 USD | 649,600,000.00 USD | 8,900,000.00 USD | 6,710,000.00 USD | 2,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2364.90` | 669,200,000.00 USD | 669,200,000.00 USD | 6,420,000.00 USD | 4,850,000.00 USD | 8,330,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 2,990,000.00 USD | 17,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2365.20` | 724,170,000.00 USD | 724,170,000.00 USD | 10,200,000.00 USD | 0.00 USD | 10,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2367.50` | 677,980,000.00 USD | 677,980,000.00 USD | 4,770,000.00 USD | 1,110,000.00 USD | 2,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2368.50` | 737,240,000.00 USD | 737,240,000.00 USD | 10,830,000.00 USD | 1,780,000.00 USD | 458,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2370.10` | 711,700,000.00 USD | 711,700,000.00 USD | 14,350,000.00 USD | 12,300,000.00 USD | 7,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2371.80` | 818,170,000.00 USD | 818,170,000.00 USD | 26,000,000.00 USD | 0.00 USD | 54,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2372.70` | 740,160,000.00 USD | 740,160,000.00 USD | 14,450,000.00 USD | 5,550,000.00 USD | 8,460,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 1,510,000.00 USD | 18,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2375.10` | 845,120,000.00 USD | 845,120,000.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2375.30` | 758,950,000.00 USD | 758,950,000.00 USD | 11,490,000.00 USD | 3,650,000.00 USD | 3,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2377.90` | 779,510,000.00 USD | 779,510,000.00 USD | 5,060,000.00 USD | 6,270,000.00 USD | 9,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2378.40` | 890,530,000.00 USD | 890,530,000.00 USD | 11,800,000.00 USD | 7,950,000.00 USD | 25,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2380.50` | 818,190,000.00 USD | 818,190,000.00 USD | 11,350,000.00 USD | 10,470,000.00 USD | 16,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2381.70` | 930,320,000.00 USD | 930,320,000.00 USD | 8,510,000.00 USD | 6,750,000.00 USD | 24,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2383.10` | 866,090,000.00 USD | 866,090,000.00 USD | 20,500,000.00 USD | 14,070,000.00 USD | 13,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2385.00` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 18,550,000.00 USD | 36,910,000.00 USD | 46,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 10,960.00 USD | 18,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2385.70` | 894,380,000.00 USD | 894,380,000.00 USD | 9,780,000.00 USD | 11,460,000.00 USD | 7,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2388.30` | 919,560,000.00 USD | 919,560,000.00 USD | 13,100,000.00 USD | 6,720,000.00 USD | 5,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2388.30` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 5,290,000.00 USD | 38,070,000.00 USD | 44,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2390.90` | 935,170,000.00 USD | 935,170,000.00 USD | 3,770,000.00 USD | 6,670,000.00 USD | 5,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2391.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 8,560,000.00 USD | 52,080,000.00 USD | 40,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2393.50` | 949,510,000.00 USD | 949,510,000.00 USD | 4,350,000.00 USD | 6,000,000.00 USD | 4,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2394.90` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 57,450,000.00 USD | 32,260,000.00 USD | 37,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 255,130.00 USD | 19,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2396.10` | 962,660,000.00 USD | 962,660,000.00 USD | 5,380,000.00 USD | 3,200,000.00 USD | 4,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2398.20` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 42,820,000.00 USD | 38,210,000.00 USD | 29,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2398.70` | 984,780,000.00 USD | 984,780,000.00 USD | 7,520,000.00 USD | 6,910,000.00 USD | 7,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2401.30` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 5,960,000.00 USD | 6,570,000.00 USD | 6,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2401.50` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 51,970,000.00 USD | 26,780,000.00 USD | 29,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2403.90` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 9,280,000.00 USD | 8,450,000.00 USD | 6,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2404.80` | 1,670,000,000.00 USD | 1,670,000,000.00 USD | 50,800,000.00 USD | 32,200,000.00 USD | 24,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 5,500,000.00 USD | 24,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2406.50` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 12,590,000.00 USD | 7,420,000.00 USD | 6,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2408.10` | 1,760,000,000.00 USD | 1,760,000,000.00 USD | 34,390,000.00 USD | 31,420,000.00 USD | 25,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2409.10` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 8,470,000.00 USD | 8,000,000.00 USD | 8,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2411.40` | 1,840,000,000.00 USD | 1,840,000,000.00 USD | 19,200,000.00 USD | 32,580,000.00 USD | 27,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2411.70` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 7,650,000.00 USD | 7,200,000.00 USD | 2,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2414.30` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 4,160,000.00 USD | 2,340,000.00 USD | 2,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2414.70` | 1,910,000,000.00 USD | 1,910,000,000.00 USD | 23,820,000.00 USD | 21,740,000.00 USD | 23,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 2,180,000.00 USD | 26,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2416.90` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 3,500,000.00 USD | 2,390,000.00 USD | 3,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2418.00` | 1,990,000,000.00 USD | 1,990,000,000.00 USD | 34,060,000.00 USD | 15,260,000.00 USD | 24,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2419.50` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 6,320,000.00 USD | 4,000,000.00 USD | 3,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2421.30` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 25,700,000.00 USD | 27,770,000.00 USD | 21,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2422.10` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 3,230,000.00 USD | 3,700,000.00 USD | 5,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.60` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 23,650,000.00 USD | 33,060,000.00 USD | 34,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2424.70` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 1,400,000.00 USD | 2,670,000.00 USD | 844,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 282,030.00 USD | 26,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2427.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 731,900.00 USD | 124,100.00 USD | 601,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2427.90` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 25,200,000.00 USD | 15,090,000.00 USD | 18,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2429.90` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 1,390,000.00 USD | 1,770,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2431.20` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 10,380,000.00 USD | 17,060,000.00 USD | 9,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2432.50` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 2,260,000.00 USD | 1,690,000.00 USD | 247,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2434.50` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 27,390,000.00 USD | 21,570,000.00 USD | 11,160,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 669,590.00 USD | 27,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2435.10` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 1,790,000.00 USD | 482,360.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2437.70` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 777,840.00 USD | 530,330.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2437.80` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 11,900,000.00 USD | 12,720,000.00 USD | 5,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2440.30` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 1,540,000.00 USD | 1,240,000.00 USD | 479,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2441.10` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 15,080,000.00 USD | 8,120,000.00 USD | 10,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2442.90` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 1,050,000.00 USD | 1,430,000.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2444.40` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 8,860,000.00 USD | 15,100,000.00 USD | 13,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 54,880,000.00 USD | 82,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2445.50` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 126,820.00 USD | 467,480.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2447.70` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 11,380,000.00 USD | 7,520,000.00 USD | 17,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2448.10` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 864,380.00 USD | 325,700.00 USD | 1,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2450.70` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 2,020,000.00 USD | 877,190.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2451.00` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 16,710,000.00 USD | 12,450,000.00 USD | 12,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2453.30` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 4,710,000.00 USD | 2,600,000.00 USD | 3,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2454.30` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 4,620,000.00 USD | 4,930,000.00 USD | 3,880,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 97,340.00 USD | 82,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2455.90` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 1,050,000.00 USD | 2,090,000.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2457.60` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 15,150,000.00 USD | 12,540,000.00 USD | 12,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2458.50` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 1,400,000.00 USD | 2,620,000.00 USD | 479,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2460.90` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 5,580,000.00 USD | 8,670,000.00 USD | 6,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2461.10` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 470,530.00 USD | 46,520.00 USD | 366,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2463.70` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 619,960.00 USD | 829,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2464.20` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 8,720,000.00 USD | 7,700,000.00 USD | 4,700,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 873,000.00 USD | 83,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2466.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 83,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2467.50` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 4,540,000.00 USD | 3,710,000.00 USD | 586,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2468.90` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 1,250,000.00 USD | 391,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2470.80` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 3,960,000.00 USD | 2,290,000.00 USD | 522,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2474.10` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 5,230,000.00 USD | 2,920,000.00 USD | 2,400,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 494,020.00 USD | 84,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2476.70` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 943,590.00 USD | 40,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2477.40` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 1,660,000.00 USD | 4,420,000.00 USD | 718,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2479.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 26,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2480.70` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 2,110,000.00 USD | 4,170,000.00 USD | 540,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2481.90` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 525,130.00 USD | 136,500.00 USD | 451,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2484.00` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 1,210,000.00 USD | 1,390,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2484.50` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 925,970.00 USD | 1,330,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 47,980.00 USD | 84,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2487.10` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2487.30` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 275,450.00 USD | 211,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2489.70` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 300,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2490.60` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 2,910,000.00 USD | 2,540,000.00 USD | 239,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2492.30` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 340,580.00 USD | 44,470.00 USD | 348,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2493.90` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 1,610,000.00 USD | 1,760,000.00 USD | 3,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2494.90` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 134,080.00 USD | 33,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 2,280,000.00 USD | 86,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2497.20` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 2,860,000.00 USD | 4,770,000.00 USD | 6,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2497.50` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 8,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2500.10` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2500.50` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 1,110,000.00 USD | 1,450,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2502.70` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2503.80` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 63,860.00 USD | 1,480,000.00 USD | 125,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 4,960,000.00 USD | 91,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2505.30` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2507.10` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 4,340,000.00 USD | 3,090,000.00 USD | 3,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2510.40` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 2,290,000.00 USD | 1,270,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2510.50` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2513.10` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2513.70` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 149,030.00 USD | 91,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2515.70` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2517.00` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 97,050.00 USD | 189,640.00 USD | 815,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2520.30` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2520.90` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 80,610.00 USD | 121,470.00 USD | 88,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2523.50` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 563,140.00 USD | 537,030.00 USD | 532,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2523.60` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 146,750.00 USD | 91,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2526.10` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 754,970.00 USD | 304,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2526.90` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2530.20` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 2,800,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2533.50` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 3,530,000.00 USD | 1,850,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2535.00` | 911,950.00 USD | 92,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2536.80` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 3,720,000.00 USD | 3,450,000.00 USD | 3,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2540.10` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 4,150,000.00 USD | 3,220,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2543.40` | 2,730,000,000.00 USD | 2,730,000,000.00 USD | 4,150,000.00 USD | 2,520,000.00 USD | 2,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2545.00` | 10,820,000.00 USD | 103,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2546.70` | 2,730,000,000.00 USD | 2,730,000,000.00 USD | 1,450,000.00 USD | 1,090,000.00 USD | 2,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2550.00` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 4,320,000.00 USD | 3,550,000.00 USD | 3,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2553.30` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 2,820,000.00 USD | 788,360.00 USD | 2,600,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2555.00` | 916,380.00 USD | 104,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2556.60` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 2,760,000.00 USD | 283,560.00 USD | 6,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2559.90` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 5,720,000.00 USD | 2,130,000.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2563.20` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 1,430,000.00 USD | 2,900,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2565.00` | 3,050,000.00 USD | 107,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2566.50` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 1,860,000.00 USD | 1,830,000.00 USD | 3,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2569.80` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 125,250.00 USD | 341,900.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2573.10` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2575.00` | 13,240,000.00 USD | 120,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2576.40` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 2,400,000.00 USD | 930,280.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2579.70` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 2,750,000.00 USD | 1,780,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2583.00` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 1,730,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2585.00` | 26,480,000.00 USD | 146,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2586.30` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 1,480,000.00 USD | 2,030,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2589.60` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 3,310,000.00 USD | 631,590.00 USD | 2,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2592.90` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 2,370,000.00 USD | 1,280,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2595.00` | 8,190,000.00 USD | 155,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2596.20` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 794,750.00 USD | 620,840.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2599.50` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 2,380,000.00 USD | 2,530,000.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2602.80` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 1,680,000.00 USD | 1,260,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2605.00` | 56,520.00 USD | 155,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2606.10` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 1,850,000.00 USD | 1,560,000.00 USD | 772,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2609.40` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2612.70` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 1,010,000.00 USD | 643,740.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2615.00` | 6,310,000.00 USD | 161,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2616.00` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2619.30` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 449,020.00 USD | 323,810.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2622.60` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 631,440.00 USD | 1,220,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2625.00` | 13,030,000.00 USD | 174,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2625.90` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 485,890.00 USD | 474,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2629.20` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 0.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2632.40` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 301,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2635.00` | 4,030,000.00 USD | 178,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2645.00` | 278,920.00 USD | 178,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2655.00` | 35,910,000.00 USD | 214,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2665.00` | 56,390.00 USD | 214,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2675.00` | 418,850.00 USD | 215,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2685.00` | 1,320,000.00 USD | 216,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2695.00` | 155,350.00 USD | 216,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2705.00` | 29,540,000.00 USD | 246,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2715.00` | 189,530.00 USD | 246,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2725.00` | 313,150.00 USD | 246,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2735.00` | 195,790.00 USD | 246,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2745.00` | 1,230,000.00 USD | 248,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2755.00` | 1,200,000.00 USD | 249,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2765.00` | 4,420,000.00 USD | 253,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2775.00` | 68,390.00 USD | 253,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2785.00` | 1,850,000.00 USD | 255,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2795.00` | 44,950.00 USD | 255,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2805.00` | 16,920,000.00 USD | 272,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2815.00` | 1,050,000.00 USD | 273,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2825.00` | 137,300.00 USD | 273,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2835.00` | 4,660,000.00 USD | 278,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2845.00` | 2,040,000.00 USD | 280,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2855.00` | 21,590,000.00 USD | 302,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2865.00` | 18,280,000.00 USD | 320,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2875.00` | 773,940.00 USD | 321,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2885.00` | 1,200,000.00 USD | 322,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2895.00` | 617,890.00 USD | 323,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2905.00` | 2,050,000.00 USD | 325,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2915.00` | 1,820,000.00 USD | 326,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2925.00` | 1,170,000.00 USD | 328,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2935.00` | 40,300.00 USD | 328,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2945.00` | 27,050,000.00 USD | 355,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2955.00` | 160,000.00 USD | 355,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2965.00` | 546,120.00 USD | 355,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2975.00` | 170,870.00 USD | 356,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2985.00` | 382,320.00 USD | 356,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2995.00` | 1,430,000.00 USD | 357,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3005.00` | 21,340,000.00 USD | 379,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3015.00` | 321,930.00 USD | 379,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3025.00` | 774,330.00 USD | 380,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3035.00` | 14,360,000.00 USD | 394,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3045.00` | 462,170.00 USD | 395,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3055.00` | 2,520,000.00 USD | 397,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3065.00` | 3,990,000.00 USD | 401,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3075.00` | 3,120,000.00 USD | 404,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3085.00` | 2,190,000.00 USD | 406,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3095.00` | 378,770.00 USD | 407,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3105.00` | 9,360,000.00 USD | 416,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3115.00` | 2,080,000.00 USD | 418,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3125.00` | 136,240.00 USD | 418,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3135.00` | 111,600.00 USD | 419,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3145.00` | 34,810.00 USD | 419,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3155.00` | 5,820,000.00 USD | 424,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3165.00` | 5,120,000.00 USD | 430,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3175.00` | 692,710.00 USD | 430,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3185.00` | 7,450,000.00 USD | 438,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3195.00` | 3,910,000.00 USD | 442,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3205.00` | 312,360.00 USD | 442,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3215.00` | 178,880.00 USD | 442,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3225.00` | 171,100.00 USD | 442,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3235.00` | 8,500,000.00 USD | 451,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3245.00` | 2,060,000.00 USD | 453,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3255.00` | 321,440.00 USD | 453,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3265.00` | 137,500.00 USD | 453,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3275.00` | 4,770,000.00 USD | 458,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3285.00` | 8,520,000.00 USD | 467,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3295.00` | 1,810,000.00 USD | 468,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3305.00` | 2,150,000.00 USD | 471,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3315.00` | 672,890.00 USD | 471,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3325.00` | 36,290.00 USD | 471,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3335.00` | 4,880.00 USD | 471,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3345.00` | 581,730.00 USD | 472,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3355.00` | 361,600.00 USD | 472,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3365.00` | 444,550.00 USD | 473,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3375.00` | 12,390.00 USD | 473,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3385.00` | 144,330.00 USD | 473,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3395.00` | 109,840.00 USD | 473,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3405.00` | 234,160.00 USD | 473,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3415.00` | 171,840.00 USD | 473,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3425.00` | 14,630,000.00 USD | 488,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3435.00` | 400,900.00 USD | 488,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3445.00` | 21,230.00 USD | 488,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3455.00` | 961,150.00 USD | 489,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3465.00` | 636,050.00 USD | 490,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3475.00` | 59,190,000.00 USD | 549,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3485.00` | 929,200.00 USD | 550,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3495.00` | 1,160,000.00 USD | 551,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3505.00` | 76,670.00 USD | 551,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3515.00` | 338,550.00 USD | 552,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3525.00` | 95,940.00 USD | 552,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3535.00` | 453,980.00 USD | 552,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3545.00` | 7,670.00 USD | 552,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3555.00` | 101,490.00 USD | 552,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3565.00` | 135,970.00 USD | 552,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3575.00` | 213,290.00 USD | 553,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3585.00` | 474,410.00 USD | 553,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3595.00` | 325,710.00 USD | 553,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3605.00` | 19,770.00 USD | 553,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3615.00` | 4,050,000.00 USD | 558,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3625.00` | 469,000.00 USD | 558,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3635.00` | 7,350,000.00 USD | 565,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3645.00` | 44,640.00 USD | 565,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3655.00` | 161,510.00 USD | 566,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3665.00` | 264,890.00 USD | 566,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3675.00` | 6,940,000.00 USD | 573,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3685.00` | 197,070.00 USD | 573,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3695.00` | 753,490.00 USD | 574,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3705.00` | 16,570.00 USD | 574,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3715.00` | 1,700,000.00 USD | 575,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3725.00` | 379,690.00 USD | 576,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3735.00` | 1,070,000.00 USD | 577,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3745.00` | 840,410.00 USD | 578,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3755.00` | 17,520.00 USD | 578,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3765.00` | 1,940,000.00 USD | 580,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3775.00` | 862,520.00 USD | 581,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3785.00` | 2,370,000.00 USD | 583,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3795.00` | 4,140,000.00 USD | 587,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3805.00` | 3,490.00 USD | 587,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3815.00` | 812,690.00 USD | 588,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3825.00` | 2,190,000.00 USD | 590,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3835.00` | 79,710,000.00 USD | 670,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3845.00` | 35,800,000.00 USD | 706,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3855.00` | 169,550.00 USD | 706,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3865.00` | 1,800,000.00 USD | 708,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3875.00` | 928,140.00 USD | 708,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3885.00` | 2,860,000.00 USD | 711,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3895.00` | 34,440,000.00 USD | 746,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3905.00` | 2,420,000.00 USD | 748,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3915.00` | 7,060.00 USD | 748,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3925.00` | 385,990.00 USD | 749,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3935.00` | 6,960.00 USD | 749,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3945.00` | 2,300.00 USD | 749,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3955.00` | 198,760.00 USD | 749,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3965.00` | 776,400.00 USD | 750,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3975.00` | 423,630,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3985.00` | 816,840.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3995.00` | 235,910.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4005.00` | 58,240.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4015.00` | 31,070,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4025.00` | 378,560.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4035.00` | 123,170.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4045.00` | 477,480.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4055.00` | 1,710,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4065.00` | 19,210.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4075.00` | 126,010.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4085.00` | 3,320.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4095.00` | 36,480.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4105.00` | 6,850,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4115.00` | 139,550.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4125.00` | 92,410,000.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4135.00` | 95,240.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4145.00` | 1,210,000.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4155.00` | 113,950.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4165.00` | 116,140.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4175.00` | 975,990.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4185.00` | 428,230.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4195.00` | 258,150.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4205.00` | 4,050,000.00 USD | 1,320,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4215.00` | 47,330.00 USD | 1,320,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4225.00` | 71,560.00 USD | 1,320,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4235.00` | 433,220.00 USD | 1,320,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4245.00` | 7,520.00 USD | 1,320,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4255.00` | 5,310,000.00 USD | 1,320,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4265.00` | 54,480.00 USD | 1,320,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4275.00` | 50,950.00 USD | 1,320,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4285.00` | 480,150.00 USD | 1,320,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4295.00` | 169,410.00 USD | 1,320,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4305.00` | 239.36 USD | 1,320,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4315.00` | 9,540.00 USD | 1,320,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4325.00` | 18,220.00 USD | 1,320,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4335.00` | 4,160,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4345.00` | 53,810.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4365.00` | 1,310,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4375.00` | 19,610.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4395.00` | 451,490.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4405.00` | 23,060.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4415.00` | 5,890,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4425.00` | 3,120.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4435.00` | 19,840.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4445.00` | 1,920.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4455.00` | 66,260.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4465.00` | 1,170,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4475.00` | 49,510.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4485.00` | 166,140.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4495.00` | 1,550,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4505.00` | 427.52 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4515.00` | 23,420.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4525.00` | 7,660,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4535.00` | 55,010.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4545.00` | 12,730.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `455.00` | 865,700,000.00 USD | 0.00 USD | 160,750.00 USD | `-79.97%` | `353.29` |
| `Live` | `Long` | `465.00` | 865,540,000.00 USD | 0.00 USD | 11,230.00 USD | `-79.53%` | `24.15` |
| `Live` | `Long` | `475.00` | 865,530,000.00 USD | 0.00 USD | 10,340.00 USD | `-79.09%` | `21.76` |
| `Live` | `Long` | `485.00` | 865,520,000.00 USD | 0.00 USD | 1,930.00 USD | `-78.64%` | `3.98` |
| `Live` | `Long` | `495.00` | 865,510,000.00 USD | 0.00 USD | 1,770,000.00 USD | `-78.20%` | `3,578.80` |
| `Live` | `Long` | `505.00` | 863,740,000.00 USD | 0.00 USD | 23,450.00 USD | `-77.76%` | `46.43` |
| `Live` | `Long` | `515.00` | 863,720,000.00 USD | 0.00 USD | 5,850.00 USD | `-77.32%` | `11.35` |
| `Live` | `Long` | `525.00` | 863,710,000.00 USD | 0.00 USD | 992.04 USD | `-76.88%` | `1.89` |
| `Live` | `Long` | `535.00` | 863,710,000.00 USD | 0.00 USD | 1,900.00 USD | `-76.44%` | `3.54` |
| `Live` | `Long` | `545.00` | 863,710,000.00 USD | 0.00 USD | 1,650,000.00 USD | `-76.00%` | `3,029.38` |
| `Live` | `Long` | `555.00` | 862,060,000.00 USD | 0.00 USD | 73,450.00 USD | `-75.56%` | `132.35` |
| `Live` | `Long` | `565.00` | 861,990,000.00 USD | 0.00 USD | 25,410.00 USD | `-75.12%` | `44.97` |
| `Live` | `Long` | `575.00` | 861,960,000.00 USD | 0.00 USD | 712,960.00 USD | `-74.68%` | `1,239.93` |
| `Live` | `Long` | `585.00` | 861,250,000.00 USD | 0.00 USD | 954,130.00 USD | `-74.24%` | `1,631.00` |
| `Live` | `Long` | `595.00` | 860,290,000.00 USD | 0.00 USD | 407,770.00 USD | `-73.80%` | `685.32` |
| `Live` | `Long` | `605.00` | 859,890,000.00 USD | 0.00 USD | 30,250.00 USD | `-73.36%` | `50.00` |
| `Live` | `Long` | `615.00` | 859,860,000.00 USD | 0.00 USD | 17,690.00 USD | `-72.92%` | `28.76` |
| `Live` | `Long` | `625.00` | 859,840,000.00 USD | 0.00 USD | 5,400.00 USD | `-72.48%` | `8.64` |
| `Live` | `Long` | `635.00` | 859,830,000.00 USD | 0.00 USD | 5,170.00 USD | `-72.04%` | `8.14` |
| `Live` | `Long` | `645.00` | 859,830,000.00 USD | 0.00 USD | 7,490.00 USD | `-71.60%` | `11.61` |
| `Live` | `Long` | `655.00` | 859,820,000.00 USD | 0.00 USD | 31,090.00 USD | `-71.16%` | `47.46` |
| `Live` | `Long` | `665.00` | 859,790,000.00 USD | 0.00 USD | 49,240.00 USD | `-70.72%` | `74.04` |
| `Live` | `Long` | `675.00` | 859,740,000.00 USD | 0.00 USD | 55,300.00 USD | `-70.28%` | `81.92` |
| `Live` | `Long` | `685.00` | 859,680,000.00 USD | 0.00 USD | 54,590.00 USD | `-69.84%` | `79.70` |
| `Live` | `Long` | `695.00` | 859,630,000.00 USD | 0.00 USD | 6,870.00 USD | `-69.40%` | `9.88` |
| `Live` | `Long` | `705.00` | 859,620,000.00 USD | 0.00 USD | 24,470.00 USD | `-68.96%` | `34.71` |
| `Live` | `Long` | `715.00` | 859,600,000.00 USD | 0.00 USD | 1,440.00 USD | `-68.52%` | `2.01` |
| `Live` | `Long` | `725.00` | 859,600,000.00 USD | 0.00 USD | 390,570.00 USD | `-68.08%` | `538.72` |
| `Live` | `Long` | `735.00` | 859,210,000.00 USD | 0.00 USD | 56,790.00 USD | `-67.64%` | `77.27` |
| `Live` | `Long` | `745.00` | 859,150,000.00 USD | 0.00 USD | 15,300.00 USD | `-67.20%` | `20.53` |
| `Live` | `Long` | `755.00` | 859,130,000.00 USD | 0.00 USD | 39,840.00 USD | `-66.76%` | `52.76` |
| `Live` | `Long` | `765.00` | 859,090,000.00 USD | 0.00 USD | 66,870.00 USD | `-66.32%` | `87.41` |
| `Live` | `Long` | `775.00` | 859,030,000.00 USD | 0.00 USD | 33,450.00 USD | `-65.88%` | `43.16` |
| `Live` | `Long` | `785.00` | 858,990,000.00 USD | 0.00 USD | 93,970.00 USD | `-65.44%` | `119.71` |
| `Live` | `Long` | `795.00` | 858,900,000.00 USD | 0.00 USD | 1,620.00 USD | `-64.99%` | `2.03` |
| `Live` | `Long` | `805.00` | 858,900,000.00 USD | 0.00 USD | 60,820.00 USD | `-64.55%` | `75.55` |
| `Live` | `Long` | `815.00` | 858,840,000.00 USD | 0.00 USD | 16,590.00 USD | `-64.11%` | `20.35` |
| `Live` | `Long` | `825.00` | 858,820,000.00 USD | 0.00 USD | 149,370.00 USD | `-63.67%` | `181.06` |
| `Live` | `Long` | `835.00` | 858,670,000.00 USD | 0.00 USD | 43,440.00 USD | `-63.23%` | `52.03` |
| `Live` | `Long` | `845.00` | 858,630,000.00 USD | 0.00 USD | 466,890.00 USD | `-62.79%` | `552.53` |
| `Live` | `Long` | `855.00` | 858,160,000.00 USD | 0.00 USD | 25,890.00 USD | `-62.35%` | `30.29` |
| `Live` | `Long` | `865.00` | 858,140,000.00 USD | 0.00 USD | 164,020.00 USD | `-61.91%` | `189.62` |
| `Live` | `Long` | `875.00` | 857,970,000.00 USD | 0.00 USD | 45,750.00 USD | `-61.47%` | `52.29` |
| `Live` | `Long` | `885.00` | 857,930,000.00 USD | 0.00 USD | 945,020.00 USD | `-61.03%` | `1,067.82` |
| `Live` | `Long` | `895.00` | 856,980,000.00 USD | 0.00 USD | 302,490.00 USD | `-60.59%` | `337.98` |
| `Live` | `Long` | `905.00` | 856,680,000.00 USD | 0.00 USD | 47,080.00 USD | `-60.15%` | `52.02` |
| `Live` | `Long` | `915.00` | 856,630,000.00 USD | 0.00 USD | 161,630.00 USD | `-59.71%` | `176.64` |
| `Live` | `Long` | `925.00` | 856,470,000.00 USD | 0.00 USD | 144,890.00 USD | `-59.27%` | `156.64` |
| `Live` | `Long` | `935.00` | 856,320,000.00 USD | 0.00 USD | 377,130.00 USD | `-58.83%` | `403.35` |
| `Live` | `Long` | `945.00` | 855,950,000.00 USD | 0.00 USD | 86,300.00 USD | `-58.39%` | `91.33` |
| `Live` | `Long` | `955.00` | 855,860,000.00 USD | 0.00 USD | 17,370.00 USD | `-57.95%` | `18.18` |
| `Live` | `Long` | `965.00` | 855,840,000.00 USD | 0.00 USD | 317,920.00 USD | `-57.51%` | `329.45` |
| `Live` | `Long` | `975.00` | 855,530,000.00 USD | 0.00 USD | 367,230.00 USD | `-57.07%` | `376.65` |
| `Live` | `Long` | `985.00` | 855,160,000.00 USD | 0.00 USD | 12,830.00 USD | `-56.63%` | `13.02` |
| `Live` | `Long` | `995.00` | 855,150,000.00 USD | 0.00 USD | 112,050.00 USD | `-56.19%` | `112.62` |
| `Live` | `Long` | `1005.00` | 855,030,000.00 USD | 0.00 USD | 109,480.00 USD | `-55.75%` | `108.93` |
| `Live` | `Long` | `1015.00` | 854,920,000.00 USD | 0.00 USD | 63,030.00 USD | `-55.31%` | `62.10` |
| `Live` | `Long` | `1025.00` | 854,860,000.00 USD | 0.00 USD | 120,320.00 USD | `-54.87%` | `117.38` |
| `Live` | `Long` | `1035.00` | 854,740,000.00 USD | 0.00 USD | 36,820.00 USD | `-54.43%` | `35.57` |
| `Live` | `Long` | `1045.00` | 854,700,000.00 USD | 0.00 USD | 7,730,000.00 USD | `-53.99%` | `7,400.97` |
| `Live` | `Long` | `1055.00` | 846,970,000.00 USD | 0.00 USD | 14,950.00 USD | `-53.55%` | `14.17` |
| `Live` | `Long` | `1065.00` | 846,950,000.00 USD | 0.00 USD | 134,880.00 USD | `-53.11%` | `126.65` |
| `Live` | `Long` | `1075.00` | 846,820,000.00 USD | 0.00 USD | 2,650,000.00 USD | `-52.67%` | `2,465.40` |
| `Live` | `Long` | `1085.00` | 844,170,000.00 USD | 0.00 USD | 976,670.00 USD | `-52.23%` | `900.16` |
| `Live` | `Long` | `1095.00` | 843,190,000.00 USD | 0.00 USD | 74,990.00 USD | `-51.79%` | `68.48` |
| `Live` | `Long` | `1105.00` | 843,120,000.00 USD | 0.00 USD | 178,170.00 USD | `-51.35%` | `161.24` |
| `Live` | `Long` | `1115.00` | 842,940,000.00 USD | 0.00 USD | 346,470.00 USD | `-50.90%` | `310.74` |
| `Live` | `Long` | `1125.00` | 842,590,000.00 USD | 0.00 USD | 10,360,000.00 USD | `-50.46%` | `9,205.41` |
| `Live` | `Long` | `1135.00` | 832,240,000.00 USD | 0.00 USD | 186,700.00 USD | `-50.02%` | `164.49` |
| `Live` | `Long` | `1145.00` | 832,050,000.00 USD | 0.00 USD | 275,100.00 USD | `-49.58%` | `240.27` |
| `Live` | `Long` | `1155.00` | 831,780,000.00 USD | 0.00 USD | 1,860,000.00 USD | `-49.14%` | `1,612.57` |
| `Live` | `Long` | `1165.00` | 829,910,000.00 USD | 0.00 USD | 131,750.00 USD | `-48.70%` | `113.09` |
| `Live` | `Long` | `1175.00` | 829,780,000.00 USD | 0.00 USD | 7,370,000.00 USD | `-48.26%` | `6,271.03` |
| `Live` | `Long` | `1185.00` | 822,410,000.00 USD | 0.00 USD | 143,160.00 USD | `-47.82%` | `120.81` |
| `Live` | `Long` | `1195.00` | 822,270,000.00 USD | 0.00 USD | 335,690.00 USD | `-47.38%` | `280.91` |
| `Live` | `Long` | `1205.00` | 821,930,000.00 USD | 0.00 USD | 362,060.00 USD | `-46.94%` | `300.46` |
| `Live` | `Long` | `1215.00` | 821,570,000.00 USD | 0.00 USD | 255,010.00 USD | `-46.50%` | `209.88` |
| `Live` | `Long` | `1225.00` | 821,320,000.00 USD | 0.00 USD | 292,720.00 USD | `-46.06%` | `238.96` |
| `Live` | `Long` | `1235.00` | 821,020,000.00 USD | 0.00 USD | 935,800.00 USD | `-45.62%` | `757.73` |
| `Live` | `Long` | `1245.00` | 820,090,000.00 USD | 0.00 USD | 222,700.00 USD | `-45.18%` | `178.88` |
| `Live` | `Long` | `1255.00` | 819,870,000.00 USD | 0.00 USD | 2,300,000.00 USD | `-44.74%` | `1,832.97` |
| `Live` | `Long` | `1265.00` | 817,570,000.00 USD | 0.00 USD | 263,070.00 USD | `-44.30%` | `207.96` |
| `Live` | `Long` | `1275.00` | 817,300,000.00 USD | 0.00 USD | 966,910.00 USD | `-43.86%` | `758.36` |
| `Live` | `Long` | `1285.00` | 816,340,000.00 USD | 0.00 USD | 15,630,000.00 USD | `-43.42%` | `12,164.13` |
| `Live` | `Long` | `1295.00` | 800,700,000.00 USD | 0.00 USD | 181,060.00 USD | `-42.98%` | `139.82` |
| `Live` | `Long` | `1305.00` | 800,520,000.00 USD | 0.00 USD | 439,590.00 USD | `-42.54%` | `336.85` |
| `Live` | `Long` | `1315.00` | 800,080,000.00 USD | 0.00 USD | 118,750.00 USD | `-42.10%` | `90.30` |
| `Live` | `Long` | `1325.00` | 799,960,000.00 USD | 0.00 USD | 522,200.00 USD | `-41.66%` | `394.11` |
| `Live` | `Long` | `1335.00` | 799,440,000.00 USD | 0.00 USD | 376,840.00 USD | `-41.22%` | `282.28` |
| `Live` | `Long` | `1345.00` | 799,070,000.00 USD | 0.00 USD | 749,590.00 USD | `-40.78%` | `557.32` |
| `Live` | `Long` | `1355.00` | 798,320,000.00 USD | 0.00 USD | 202,460.00 USD | `-40.34%` | `149.42` |
| `Live` | `Long` | `1365.00` | 798,110,000.00 USD | 0.00 USD | 1,090,000.00 USD | `-39.90%` | `800.75` |
| `Live` | `Long` | `1375.00` | 797,020,000.00 USD | 0.00 USD | 337,380.00 USD | `-39.46%` | `245.37` |
| `Live` | `Long` | `1385.00` | 796,680,000.00 USD | 0.00 USD | 6,950,000.00 USD | `-39.02%` | `5,014.91` |
| `Live` | `Long` | `1395.00` | 789,740,000.00 USD | 0.00 USD | 167,840.00 USD | `-38.58%` | `120.32` |
| `Live` | `Long` | `1405.00` | 789,570,000.00 USD | 0.00 USD | 10,150,000.00 USD | `-38.14%` | `7,225.34` |
| `Live` | `Long` | `1415.00` | 779,420,000.00 USD | 0.00 USD | 13,100,000.00 USD | `-37.70%` | `9,259.48` |
| `Live` | `Long` | `1425.00` | 766,320,000.00 USD | 0.00 USD | 425,740.00 USD | `-37.26%` | `298.77` |
| `Live` | `Long` | `1435.00` | 765,890,000.00 USD | 0.00 USD | 1,730,000.00 USD | `-36.81%` | `1,202.49` |
| `Live` | `Long` | `1445.00` | 764,160,000.00 USD | 0.00 USD | 1,090,000.00 USD | `-36.37%` | `751.19` |
| `Live` | `Long` | `1455.00` | 763,080,000.00 USD | 0.00 USD | 96,230.00 USD | `-35.93%` | `66.14` |
| `Live` | `Long` | `1465.00` | 762,980,000.00 USD | 0.00 USD | 4,900,000.00 USD | `-35.49%` | `3,344.49` |
| `Live` | `Long` | `1475.00` | 758,080,000.00 USD | 0.00 USD | 5,700,000.00 USD | `-35.05%` | `3,866.64` |
| `Live` | `Long` | `1485.00` | 752,380,000.00 USD | 0.00 USD | 120,280.00 USD | `-34.61%` | `80.99` |
| `Live` | `Long` | `1495.00` | 752,260,000.00 USD | 0.00 USD | 4,010,000.00 USD | `-34.17%` | `2,682.05` |
| `Live` | `Long` | `1505.00` | 748,250,000.00 USD | 0.00 USD | 16,550,000.00 USD | `-33.73%` | `10,998.21` |
| `Live` | `Long` | `1515.00` | 731,700,000.00 USD | 0.00 USD | 22,140,000.00 USD | `-33.29%` | `14,611.46` |
| `Live` | `Long` | `1525.00` | 709,560,000.00 USD | 0.00 USD | 18,600,000.00 USD | `-32.85%` | `12,197.27` |
| `Live` | `Long` | `1535.00` | 690,960,000.00 USD | 0.00 USD | 8,600,000.00 USD | `-32.41%` | `5,600.37` |
| `Live` | `Long` | `1545.00` | 682,360,000.00 USD | 0.00 USD | 4,980,000.00 USD | `-31.97%` | `3,224.87` |
| `Live` | `Long` | `1555.00` | 677,380,000.00 USD | 0.00 USD | 374,830.00 USD | `-31.53%` | `241.05` |
| `Live` | `Long` | `1565.00` | 677,010,000.00 USD | 0.00 USD | 282,150.00 USD | `-31.09%` | `180.29` |
| `Live` | `Long` | `1575.00` | 676,720,000.00 USD | 0.00 USD | 318,000.00 USD | `-30.65%` | `201.91` |
| `Live` | `Long` | `1585.00` | 676,410,000.00 USD | 0.00 USD | 962,940.00 USD | `-30.21%` | `607.53` |
| `Live` | `Long` | `1595.00` | 675,440,000.00 USD | 0.00 USD | 2,570,000.00 USD | `-29.77%` | `1,609.88` |
| `Live` | `Long` | `1605.00` | 672,880,000.00 USD | 0.00 USD | 18,310,000.00 USD | `-29.33%` | `11,407.14` |
| `Live` | `Long` | `1615.00` | 654,570,000.00 USD | 0.00 USD | 485,170.00 USD | `-28.89%` | `300.41` |
| `Live` | `Long` | `1625.00` | 654,080,000.00 USD | 0.00 USD | 634,930.00 USD | `-28.45%` | `390.72` |
| `Live` | `Long` | `1635.00` | 653,450,000.00 USD | 0.00 USD | 18,550,000.00 USD | `-28.01%` | `11,344.79` |
| `Live` | `Long` | `1645.00` | 634,900,000.00 USD | 0.00 USD | 49,240,000.00 USD | `-27.57%` | `29,933.91` |
| `Live` | `Long` | `1655.00` | 585,660,000.00 USD | 0.00 USD | 10,740,000.00 USD | `-27.13%` | `6,491.40` |
| `Live` | `Long` | `1665.00` | 574,910,000.00 USD | 0.00 USD | 710,320.00 USD | `-26.69%` | `426.62` |
| `Live` | `Long` | `1675.00` | 574,200,000.00 USD | 0.00 USD | 11,660,000.00 USD | `-26.25%` | `6,963.52` |
| `Live` | `Long` | `1685.00` | 562,540,000.00 USD | 0.00 USD | 1,070,000.00 USD | `-25.81%` | `634.77` |
| `Live` | `Long` | `1695.00` | 561,470,000.00 USD | 0.00 USD | 27,830,000.00 USD | `-25.37%` | `16,416.81` |
| `Live` | `Long` | `1705.00` | 533,640,000.00 USD | 0.00 USD | 2,200,000.00 USD | `-24.93%` | `1,289.47` |
| `Live` | `Long` | `1715.00` | 531,450,000.00 USD | 0.00 USD | 17,350,000.00 USD | `-24.49%` | `10,114.65` |
| `Live` | `Long` | `1725.00` | 514,100,000.00 USD | 0.00 USD | 17,790,000.00 USD | `-24.05%` | `10,311.14` |
| `Live` | `Long` | `1735.00` | 496,310,000.00 USD | 0.00 USD | 375,500.00 USD | `-23.61%` | `216.43` |
| `Live` | `Long` | `1745.00` | 495,940,000.00 USD | 0.00 USD | 885,560.00 USD | `-23.16%` | `507.48` |
| `Live` | `Long` | `1755.00` | 495,050,000.00 USD | 0.00 USD | 491,240.00 USD | `-22.72%` | `279.91` |
| `Live` | `Long` | `1765.00` | 494,560,000.00 USD | 0.00 USD | 460,750.00 USD | `-22.28%` | `261.05` |
| `Live` | `Long` | `1775.00` | 494,100,000.00 USD | 0.00 USD | 1,110,000.00 USD | `-21.84%` | `626.17` |
| `Live` | `Long` | `1785.00` | 492,990,000.00 USD | 0.00 USD | 54,900,000.00 USD | `-21.40%` | `30,757.84` |
| `Live` | `Long` | `1795.00` | 438,080,000.00 USD | 0.00 USD | 386,030.00 USD | `-20.96%` | `215.06` |
| `Live` | `Long` | `1805.00` | 437,700,000.00 USD | 0.00 USD | 16,360,000.00 USD | `-20.52%` | `9,063.40` |
| `Live` | `Long` | `1815.00` | 421,340,000.00 USD | 0.00 USD | 2,470,000.00 USD | `-20.08%` | `1,363.23` |
| `Live` | `Long` | `1825.00` | 418,860,000.00 USD | 0.00 USD | 1,430,000.00 USD | `-19.64%` | `784.15` |
| `Live` | `Long` | `1835.00` | 417,430,000.00 USD | 0.00 USD | 892,470.00 USD | `-19.20%` | `486.36` |
| `Live` | `Long` | `1845.00` | 416,540,000.00 USD | 0.00 USD | 394,260.00 USD | `-18.76%` | `213.69` |
| `Live` | `Long` | `1855.00` | 416,150,000.00 USD | 0.00 USD | 2,930,000.00 USD | `-18.32%` | `1,577.56` |
| `Live` | `Long` | `1865.00` | 413,220,000.00 USD | 0.00 USD | 5,380,000.00 USD | `-17.88%` | `2,885.04` |
| `Live` | `Long` | `1875.00` | 407,840,000.00 USD | 0.00 USD | 7,600,000.00 USD | `-17.44%` | `4,053.61` |
| `Live` | `Long` | `1885.00` | 400,240,000.00 USD | 0.00 USD | 2,590,000.00 USD | `-17.00%` | `1,373.91` |
| `Live` | `Long` | `1895.00` | 397,650,000.00 USD | 0.00 USD | 5,400,000.00 USD | `-16.56%` | `2,849.16` |
| `Live` | `Long` | `1905.00` | 392,250,000.00 USD | 0.00 USD | 903,170.00 USD | `-16.12%` | `474.10` |
| `Live` | `Long` | `1915.00` | 391,350,000.00 USD | 0.00 USD | 13,210,000.00 USD | `-15.68%` | `6,898.78` |
| `Live` | `Long` | `1925.00` | 378,140,000.00 USD | 0.00 USD | 16,400,000.00 USD | `-15.24%` | `8,519.68` |
| `Live` | `Long` | `1935.00` | 361,740,000.00 USD | 0.00 USD | 2,790,000.00 USD | `-14.80%` | `1,440.92` |
| `Live` | `Long` | `1945.00` | 358,950,000.00 USD | 0.00 USD | 1,640,000.00 USD | `-14.36%` | `843.98` |
| `Live` | `Long` | `1955.00` | 357,310,000.00 USD | 0.00 USD | 5,430,000.00 USD | `-13.92%` | `2,778.59` |
| `Live` | `Long` | `1965.00` | 351,870,000.00 USD | 0.00 USD | 4,950,000.00 USD | `-13.48%` | `2,517.03` |
| `Live` | `Long` | `1975.00` | 346,930,000.00 USD | 0.00 USD | 1,180,000.00 USD | `-13.04%` | `596.15` |
| `Live` | `Long` | `1985.00` | 345,750,000.00 USD | 0.00 USD | 5,600,000.00 USD | `-12.60%` | `2,820.54` |
| `Live` | `Long` | `1995.00` | 340,150,000.00 USD | 0.00 USD | 1,340,000.00 USD | `-12.16%` | `674.07` |
| `Live` | `Long` | `2005.00` | 338,810,000.00 USD | 0.00 USD | 2,120,000.00 USD | `-11.72%` | `1,055.48` |
| `Live` | `Long` | `2015.00` | 336,690,000.00 USD | 0.00 USD | 11,980,000.00 USD | `-11.28%` | `5,943.77` |
| `Live` | `Long` | `2025.00` | 324,710,000.00 USD | 0.00 USD | 5,030,000.00 USD | `-10.84%` | `2,485.34` |
| `Live` | `Long` | `2035.00` | 319,680,000.00 USD | 0.00 USD | 906,040.00 USD | `-10.40%` | `445.23` |
| `Live` | `Long` | `2045.00` | 318,780,000.00 USD | 0.00 USD | 18,320,000.00 USD | `-9.96%` | `8,960.03` |
| `Live` | `Long` | `2055.00` | 300,450,000.00 USD | 0.00 USD | 5,060,000.00 USD | `-9.52%` | `2,464.17` |
| `Live` | `Long` | `2065.00` | 295,390,000.00 USD | 0.00 USD | 1,460,000.00 USD | `-9.07%` | `704.73` |
| `Live` | `Long` | `2075.00` | 293,930,000.00 USD | 0.00 USD | 3,300,000.00 USD | `-8.63%` | `1,590.39` |
| `Live` | `Long` | `2085.00` | 290,630,000.00 USD | 0.00 USD | 974,560.00 USD | `-8.19%` | `467.41` |
| `Live` | `Long` | `2095.00` | 289,660,000.00 USD | 0.00 USD | 2,220,000.00 USD | `-7.75%` | `1,057.53` |
| `Live` | `Long` | `2105.00` | 287,440,000.00 USD | 0.00 USD | 1,740,000.00 USD | `-7.31%` | `824.37` |
| `Live` | `Long` | `2115.00` | 285,710,000.00 USD | 0.00 USD | 1,360,000.00 USD | `-6.87%` | `641.89` |
| `Live` | `Long` | `2125.00` | 284,350,000.00 USD | 0.00 USD | 18,610,000.00 USD | `-6.43%` | `8,756.06` |
| `Live` | `Long` | `2135.00` | 265,740,000.00 USD | 0.00 USD | 14,450,000.00 USD | `-5.99%` | `6,769.94` |
| `Live` | `Long` | `2145.00` | 251,290,000.00 USD | 0.00 USD | 5,830,000.00 USD | `-5.55%` | `2,719.40` |
| `Live` | `Long` | `2155.00` | 245,460,000.00 USD | 0.00 USD | 2,520,000.00 USD | `-5.11%` | `1,170.00` |
| `Live` | `Long` | `2165.00` | 242,940,000.00 USD | 0.00 USD | 6,850,000.00 USD | `-4.67%` | `3,162.57` |
| `Live` | `Long` | `2175.00` | 236,090,000.00 USD | 0.00 USD | 108,060,000.00 USD | `-4.23%` | `49,683.51` |
| `Live` | `Long` | `2185.00` | 128,030,000.00 USD | 0.00 USD | 100,190,000.00 USD | `-3.79%` | `45,853.89` |
| `Live` | `Long` | `2195.00` | 27,840,000.00 USD | 0.00 USD | 1,810,000.00 USD | `-3.35%` | `822.92` |
| `Live` | `Long` | `2205.00` | 26,030,000.00 USD | 0.00 USD | 2,440,000.00 USD | `-2.91%` | `1,108.19` |
| `Live` | `Long` | `2215.00` | 23,590,000.00 USD | 0.00 USD | 11,410,000.00 USD | `-2.47%` | `5,151.71` |
| `Live` | `Long` | `2225.00` | 12,170,000.00 USD | 0.00 USD | 5,130,000.00 USD | `-2.03%` | `2,307.50` |
| `Live` | `Long` | `2235.00` | 7,040,000.00 USD | 0.00 USD | 2,700,000.00 USD | `-1.59%` | `1,209.42` |
| `Live` | `Long` | `2245.00` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | `-1.15%` | `1,931.76` |
| `Live` | `Long` | `2265.00` | 866.59 USD | 0.00 USD | 866.59 USD | `-0.27%` | `0.38` |
| `Live` | `Short` | `2275.00` | 3,220.00 USD | 3,220.00 USD | 0.00 USD | `+0.17%` | `1.41` |
| `Live` | `Short` | `2285.00` | 23,600.00 USD | 20,390.00 USD | 0.00 USD | `+0.61%` | `8.92` |
| `Live` | `Short` | `2295.00` | 2,640,000.00 USD | 2,620,000.00 USD | 0.00 USD | `+1.05%` | `1,141.69` |
| `Live` | `Short` | `2305.00` | 6,990,000.00 USD | 4,350,000.00 USD | 0.00 USD | `+1.49%` | `1,885.39` |
| `Live` | `Short` | `2315.00` | 9,770,000.00 USD | 2,780,000.00 USD | 0.00 USD | `+1.93%` | `1,202.79` |
| `Live` | `Short` | `2325.00` | 10,960,000.00 USD | 1,180,000.00 USD | 0.00 USD | `+2.37%` | `509.37` |
| `Live` | `Short` | `2335.00` | 11,720,000.00 USD | 762,050.00 USD | 0.00 USD | `+2.81%` | `326.36` |
| `Live` | `Short` | `2345.00` | 12,930,000.00 USD | 1,210,000.00 USD | 0.00 USD | `+3.25%` | `514.75` |
| `Live` | `Short` | `2355.00` | 14,240,000.00 USD | 1,320,000.00 USD | 0.00 USD | `+3.69%` | `558.57` |
| `Live` | `Short` | `2365.00` | 17,240,000.00 USD | 2,990,000.00 USD | 0.00 USD | `+4.13%` | `1,266.03` |
| `Live` | `Short` | `2375.00` | 18,750,000.00 USD | 1,510,000.00 USD | 0.00 USD | `+4.57%` | `636.79` |
| `Live` | `Short` | `2385.00` | 18,760,000.00 USD | 10,960.00 USD | 0.00 USD | `+5.02%` | `4.60` |
| `Live` | `Short` | `2395.00` | 19,020,000.00 USD | 255,130.00 USD | 0.00 USD | `+5.46%` | `106.53` |
| `Live` | `Short` | `2405.00` | 24,510,000.00 USD | 5,500,000.00 USD | 0.00 USD | `+5.90%` | `2,286.39` |
| `Live` | `Short` | `2415.00` | 26,700,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+6.34%` | `904.76` |
| `Live` | `Short` | `2425.00` | 26,980,000.00 USD | 282,030.00 USD | 0.00 USD | `+6.78%` | `116.30` |
| `Live` | `Short` | `2435.00` | 27,650,000.00 USD | 669,590.00 USD | 0.00 USD | `+7.22%` | `274.98` |
| `Live` | `Short` | `2445.00` | 82,530,000.00 USD | 54,880,000.00 USD | 0.00 USD | `+7.66%` | `22,445.79` |
| `Live` | `Short` | `2455.00` | 82,630,000.00 USD | 97,340.00 USD | 0.00 USD | `+8.10%` | `39.65` |
| `Live` | `Short` | `2465.00` | 83,500,000.00 USD | 873,000.00 USD | 0.00 USD | `+8.54%` | `354.16` |
| `Live` | `Short` | `2475.00` | 84,000,000.00 USD | 494,020.00 USD | 0.00 USD | `+8.98%` | `199.61` |
| `Live` | `Short` | `2485.00` | 84,040,000.00 USD | 47,980.00 USD | 0.00 USD | `+9.42%` | `19.31` |
| `Live` | `Short` | `2495.00` | 86,330,000.00 USD | 2,280,000.00 USD | 0.00 USD | `+9.86%` | `914.60` |
| `Live` | `Short` | `2505.00` | 91,280,000.00 USD | 4,960,000.00 USD | 0.00 USD | `+10.30%` | `1,978.75` |
| `Live` | `Short` | `2515.00` | 91,430,000.00 USD | 149,030.00 USD | 0.00 USD | `+10.74%` | `59.25` |
| `Live` | `Short` | `2525.00` | 91,580,000.00 USD | 146,750.00 USD | 0.00 USD | `+11.18%` | `58.12` |
| `Live` | `Short` | `2535.00` | 92,490,000.00 USD | 911,950.00 USD | 0.00 USD | `+11.62%` | `359.74` |
| `Live` | `Short` | `2545.00` | 103,310,000.00 USD | 10,820,000.00 USD | 0.00 USD | `+12.06%` | `4,249.87` |
| `Live` | `Short` | `2555.00` | 104,220,000.00 USD | 916,380.00 USD | 0.00 USD | `+12.50%` | `358.66` |
| `Live` | `Short` | `2565.00` | 107,270,000.00 USD | 3,050,000.00 USD | 0.00 USD | `+12.94%` | `1,189.55` |
| `Live` | `Short` | `2575.00` | 120,520,000.00 USD | 13,240,000.00 USD | 0.00 USD | `+13.38%` | `5,142.79` |
| `Live` | `Short` | `2585.00` | 146,990,000.00 USD | 26,480,000.00 USD | 0.00 USD | `+13.82%` | `10,242.78` |
| `Live` | `Short` | `2595.00` | 155,180,000.00 USD | 8,190,000.00 USD | 0.00 USD | `+14.26%` | `3,154.40` |
| `Live` | `Short` | `2605.00` | 155,240,000.00 USD | 56,520.00 USD | 0.00 USD | `+14.70%` | `21.70` |
| `Live` | `Short` | `2615.00` | 161,550,000.00 USD | 6,310,000.00 USD | 0.00 USD | `+15.14%` | `2,413.46` |
| `Live` | `Short` | `2625.00` | 174,570,000.00 USD | 13,030,000.00 USD | 0.00 USD | `+15.58%` | `4,962.87` |
| `Live` | `Short` | `2635.00` | 178,610,000.00 USD | 4,030,000.00 USD | 0.00 USD | `+16.02%` | `1,529.99` |
| `Live` | `Short` | `2645.00` | 178,880,000.00 USD | 278,920.00 USD | 0.00 USD | `+16.46%` | `105.45` |
| `Live` | `Short` | `2655.00` | 214,800,000.00 USD | 35,910,000.00 USD | 0.00 USD | `+16.90%` | `13,526.47` |
| `Live` | `Short` | `2665.00` | 214,850,000.00 USD | 56,390.00 USD | 0.00 USD | `+17.34%` | `21.16` |
| `Live` | `Short` | `2675.00` | 215,270,000.00 USD | 418,850.00 USD | 0.00 USD | `+17.78%` | `156.58` |
| `Live` | `Short` | `2685.00` | 216,600,000.00 USD | 1,320,000.00 USD | 0.00 USD | `+18.22%` | `492.66` |
| `Live` | `Short` | `2695.00` | 216,750,000.00 USD | 155,350.00 USD | 0.00 USD | `+18.66%` | `57.64` |
| `Live` | `Short` | `2705.00` | 246,290,000.00 USD | 29,540,000.00 USD | 0.00 USD | `+19.11%` | `10,920.25` |
| `Live` | `Short` | `2715.00` | 246,480,000.00 USD | 189,530.00 USD | 0.00 USD | `+19.55%` | `69.81` |
| `Live` | `Short` | `2725.00` | 246,790,000.00 USD | 313,150.00 USD | 0.00 USD | `+19.99%` | `114.92` |
| `Live` | `Short` | `2735.00` | 246,990,000.00 USD | 195,790.00 USD | 0.00 USD | `+20.43%` | `71.59` |
| `Live` | `Short` | `2745.00` | 248,220,000.00 USD | 1,230,000.00 USD | 0.00 USD | `+20.87%` | `447.10` |
| `Live` | `Short` | `2755.00` | 249,420,000.00 USD | 1,200,000.00 USD | 0.00 USD | `+21.31%` | `436.72` |
| `Live` | `Short` | `2765.00` | 253,840,000.00 USD | 4,420,000.00 USD | 0.00 USD | `+21.75%` | `1,597.91` |
| `Live` | `Short` | `2775.00` | 253,910,000.00 USD | 68,390.00 USD | 0.00 USD | `+22.19%` | `24.64` |
| `Live` | `Short` | `2785.00` | 255,760,000.00 USD | 1,850,000.00 USD | 0.00 USD | `+22.63%` | `664.11` |
| `Live` | `Short` | `2795.00` | 255,800,000.00 USD | 44,950.00 USD | 0.00 USD | `+23.07%` | `16.08` |
| `Live` | `Short` | `2805.00` | 272,720,000.00 USD | 16,920,000.00 USD | 0.00 USD | `+23.51%` | `6,032.80` |
| `Live` | `Short` | `2815.00` | 273,770,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+23.95%` | `371.43` |
| `Live` | `Short` | `2825.00` | 273,910,000.00 USD | 137,300.00 USD | 0.00 USD | `+24.39%` | `48.60` |
| `Live` | `Short` | `2835.00` | 278,570,000.00 USD | 4,660,000.00 USD | 0.00 USD | `+24.83%` | `1,645.02` |
| `Live` | `Short` | `2845.00` | 280,610,000.00 USD | 2,040,000.00 USD | 0.00 USD | `+25.27%` | `718.16` |
| `Live` | `Short` | `2855.00` | 302,210,000.00 USD | 21,590,000.00 USD | 0.00 USD | `+25.71%` | `7,563.79` |
| `Live` | `Short` | `2865.00` | 320,480,000.00 USD | 18,280,000.00 USD | 0.00 USD | `+26.15%` | `6,379.00` |
| `Live` | `Short` | `2875.00` | 321,260,000.00 USD | 773,940.00 USD | 0.00 USD | `+26.59%` | `269.20` |
| `Live` | `Short` | `2885.00` | 322,460,000.00 USD | 1,200,000.00 USD | 0.00 USD | `+27.03%` | `417.30` |
| `Live` | `Short` | `2895.00` | 323,080,000.00 USD | 617,890.00 USD | 0.00 USD | `+27.47%` | `213.43` |
| `Live` | `Short` | `2905.00` | 325,130,000.00 USD | 2,050,000.00 USD | 0.00 USD | `+27.91%` | `705.10` |
| `Live` | `Short` | `2915.00` | 326,950,000.00 USD | 1,820,000.00 USD | 0.00 USD | `+28.35%` | `625.44` |
| `Live` | `Short` | `2925.00` | 328,120,000.00 USD | 1,170,000.00 USD | 0.00 USD | `+28.79%` | `401.36` |
| `Live` | `Short` | `2935.00` | 328,160,000.00 USD | 40,300.00 USD | 0.00 USD | `+29.23%` | `13.73` |
| `Live` | `Short` | `2945.00` | 355,220,000.00 USD | 27,050,000.00 USD | 0.00 USD | `+29.67%` | `9,186.17` |
| `Live` | `Short` | `2955.00` | 355,380,000.00 USD | 160,000.00 USD | 0.00 USD | `+30.11%` | `54.15` |
| `Live` | `Short` | `2965.00` | 355,920,000.00 USD | 546,120.00 USD | 0.00 USD | `+30.55%` | `184.19` |
| `Live` | `Short` | `2975.00` | 356,090,000.00 USD | 170,870.00 USD | 0.00 USD | `+30.99%` | `57.43` |
| `Live` | `Short` | `2985.00` | 356,480,000.00 USD | 382,320.00 USD | 0.00 USD | `+31.43%` | `128.08` |
| `Live` | `Short` | `2995.00` | 357,910,000.00 USD | 1,430,000.00 USD | 0.00 USD | `+31.87%` | `478.57` |
| `Live` | `Short` | `3005.00` | 379,250,000.00 USD | 21,340,000.00 USD | 0.00 USD | `+32.31%` | `7,102.96` |
| `Live` | `Short` | `3015.00` | 379,580,000.00 USD | 321,930.00 USD | 0.00 USD | `+32.76%` | `106.78` |
| `Live` | `Short` | `3025.00` | 380,350,000.00 USD | 774,330.00 USD | 0.00 USD | `+33.20%` | `255.98` |
| `Live` | `Short` | `3035.00` | 394,720,000.00 USD | 14,360,000.00 USD | 0.00 USD | `+33.64%` | `4,733.03` |
| `Live` | `Short` | `3045.00` | 395,180,000.00 USD | 462,170.00 USD | 0.00 USD | `+34.08%` | `151.78` |
| `Live` | `Short` | `3055.00` | 397,690,000.00 USD | 2,520,000.00 USD | 0.00 USD | `+34.52%` | `823.67` |
| `Live` | `Short` | `3065.00` | 401,680,000.00 USD | 3,990,000.00 USD | 0.00 USD | `+34.96%` | `1,300.21` |
| `Live` | `Short` | `3075.00` | 404,800,000.00 USD | 3,120,000.00 USD | 0.00 USD | `+35.40%` | `1,014.60` |
| `Live` | `Short` | `3085.00` | 406,990,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+35.84%` | `710.78` |
| `Live` | `Short` | `3095.00` | 407,370,000.00 USD | 378,770.00 USD | 0.00 USD | `+36.28%` | `122.38` |
| `Live` | `Short` | `3105.00` | 416,730,000.00 USD | 9,360,000.00 USD | 0.00 USD | `+36.72%` | `3,013.02` |
| `Live` | `Short` | `3115.00` | 418,800,000.00 USD | 2,080,000.00 USD | 0.00 USD | `+37.16%` | `667.40` |
| `Live` | `Short` | `3125.00` | 418,940,000.00 USD | 136,240.00 USD | 0.00 USD | `+37.60%` | `43.60` |
| `Live` | `Short` | `3135.00` | 419,050,000.00 USD | 111,600.00 USD | 0.00 USD | `+38.04%` | `35.60` |
| `Live` | `Short` | `3145.00` | 419,090,000.00 USD | 34,810.00 USD | 0.00 USD | `+38.48%` | `11.07` |
| `Live` | `Short` | `3155.00` | 424,900,000.00 USD | 5,820,000.00 USD | 0.00 USD | `+38.92%` | `1,843.95` |
| `Live` | `Short` | `3165.00` | 430,020,000.00 USD | 5,120,000.00 USD | 0.00 USD | `+39.36%` | `1,616.67` |
| `Live` | `Short` | `3175.00` | 430,710,000.00 USD | 692,710.00 USD | 0.00 USD | `+39.80%` | `218.18` |
| `Live` | `Short` | `3185.00` | 438,160,000.00 USD | 7,450,000.00 USD | 0.00 USD | `+40.24%` | `2,338.42` |
| `Live` | `Short` | `3195.00` | 442,070,000.00 USD | 3,910,000.00 USD | 0.00 USD | `+40.68%` | `1,224.51` |
| `Live` | `Short` | `3205.00` | 442,390,000.00 USD | 312,360.00 USD | 0.00 USD | `+41.12%` | `97.46` |
| `Live` | `Short` | `3215.00` | 442,570,000.00 USD | 178,880.00 USD | 0.00 USD | `+41.56%` | `55.64` |
| `Live` | `Short` | `3225.00` | 442,740,000.00 USD | 171,100.00 USD | 0.00 USD | `+42.00%` | `53.05` |
| `Live` | `Short` | `3235.00` | 451,240,000.00 USD | 8,500,000.00 USD | 0.00 USD | `+42.44%` | `2,628.89` |
| `Live` | `Short` | `3245.00` | 453,300,000.00 USD | 2,060,000.00 USD | 0.00 USD | `+42.88%` | `634.93` |
| `Live` | `Short` | `3255.00` | 453,620,000.00 USD | 321,440.00 USD | 0.00 USD | `+43.32%` | `98.75` |
| `Live` | `Short` | `3265.00` | 453,760,000.00 USD | 137,500.00 USD | 0.00 USD | `+43.76%` | `42.11` |
| `Live` | `Short` | `3275.00` | 458,530,000.00 USD | 4,770,000.00 USD | 0.00 USD | `+44.20%` | `1,457.39` |
| `Live` | `Short` | `3285.00` | 467,050,000.00 USD | 8,520,000.00 USD | 0.00 USD | `+44.64%` | `2,593.86` |
| `Live` | `Short` | `3295.00` | 468,860,000.00 USD | 1,810,000.00 USD | 0.00 USD | `+45.08%` | `547.82` |
| `Live` | `Short` | `3305.00` | 471,010,000.00 USD | 2,150,000.00 USD | 0.00 USD | `+45.52%` | `650.25` |
| `Live` | `Short` | `3315.00` | 471,680,000.00 USD | 672,890.00 USD | 0.00 USD | `+45.96%` | `202.98` |
| `Live` | `Short` | `3325.00` | 471,720,000.00 USD | 36,290.00 USD | 0.00 USD | `+46.40%` | `10.91` |
| `Live` | `Short` | `3335.00` | 471,720,000.00 USD | 4,880.00 USD | 0.00 USD | `+46.85%` | `1.46` |
| `Live` | `Short` | `3345.00` | 472,300,000.00 USD | 581,730.00 USD | 0.00 USD | `+47.29%` | `173.91` |
| `Live` | `Short` | `3355.00` | 472,670,000.00 USD | 361,600.00 USD | 0.00 USD | `+47.73%` | `107.78` |
| `Live` | `Short` | `3365.00` | 473,110,000.00 USD | 444,550.00 USD | 0.00 USD | `+48.17%` | `132.11` |
| `Live` | `Short` | `3375.00` | 473,120,000.00 USD | 12,390.00 USD | 0.00 USD | `+48.61%` | `3.67` |
| `Live` | `Short` | `3385.00` | 473,270,000.00 USD | 144,330.00 USD | 0.00 USD | `+49.05%` | `42.64` |
| `Live` | `Short` | `3395.00` | 473,380,000.00 USD | 109,840.00 USD | 0.00 USD | `+49.49%` | `32.35` |
| `Live` | `Short` | `3405.00` | 473,610,000.00 USD | 234,160.00 USD | 0.00 USD | `+49.93%` | `68.77` |
| `Live` | `Short` | `3415.00` | 473,780,000.00 USD | 171,840.00 USD | 0.00 USD | `+50.37%` | `50.32` |
| `Live` | `Short` | `3425.00` | 488,410,000.00 USD | 14,630,000.00 USD | 0.00 USD | `+50.81%` | `4,271.63` |
| `Live` | `Short` | `3435.00` | 488,810,000.00 USD | 400,900.00 USD | 0.00 USD | `+51.25%` | `116.71` |
| `Live` | `Short` | `3445.00` | 488,840,000.00 USD | 21,230.00 USD | 0.00 USD | `+51.69%` | `6.16` |
| `Live` | `Short` | `3455.00` | 489,800,000.00 USD | 961,150.00 USD | 0.00 USD | `+52.13%` | `278.19` |
| `Live` | `Short` | `3465.00` | 490,430,000.00 USD | 636,050.00 USD | 0.00 USD | `+52.57%` | `183.57` |
| `Live` | `Short` | `3475.00` | 549,620,000.00 USD | 59,190,000.00 USD | 0.00 USD | `+53.01%` | `17,032.59` |
| `Live` | `Short` | `3485.00` | 550,550,000.00 USD | 929,200.00 USD | 0.00 USD | `+53.45%` | `266.63` |
| `Live` | `Short` | `3495.00` | 551,710,000.00 USD | 1,160,000.00 USD | 0.00 USD | `+53.89%` | `333.26` |
| `Live` | `Short` | `3505.00` | 551,790,000.00 USD | 76,670.00 USD | 0.00 USD | `+54.33%` | `21.87` |
| `Live` | `Short` | `3515.00` | 552,130,000.00 USD | 338,550.00 USD | 0.00 USD | `+54.77%` | `96.32` |
| `Live` | `Short` | `3525.00` | 552,230,000.00 USD | 95,940.00 USD | 0.00 USD | `+55.21%` | `27.22` |
| `Live` | `Short` | `3535.00` | 552,680,000.00 USD | 453,980.00 USD | 0.00 USD | `+55.65%` | `128.43` |
| `Live` | `Short` | `3545.00` | 552,690,000.00 USD | 7,670.00 USD | 0.00 USD | `+56.09%` | `2.16` |
| `Live` | `Short` | `3555.00` | 552,790,000.00 USD | 101,490.00 USD | 0.00 USD | `+56.53%` | `28.55` |
| `Live` | `Short` | `3565.00` | 552,930,000.00 USD | 135,970.00 USD | 0.00 USD | `+56.97%` | `38.14` |
| `Live` | `Short` | `3575.00` | 553,140,000.00 USD | 213,290.00 USD | 0.00 USD | `+57.41%` | `59.66` |
| `Live` | `Short` | `3585.00` | 553,610,000.00 USD | 474,410.00 USD | 0.00 USD | `+57.85%` | `132.33` |
| `Live` | `Short` | `3595.00` | 553,940,000.00 USD | 325,710.00 USD | 0.00 USD | `+58.29%` | `90.60` |
| `Live` | `Short` | `3605.00` | 553,960,000.00 USD | 19,770.00 USD | 0.00 USD | `+58.73%` | `5.48` |
| `Live` | `Short` | `3615.00` | 558,000,000.00 USD | 4,050,000.00 USD | 0.00 USD | `+59.17%` | `1,119.14` |
| `Live` | `Short` | `3625.00` | 558,470,000.00 USD | 469,000.00 USD | 0.00 USD | `+59.61%` | `129.38` |
| `Live` | `Short` | `3635.00` | 565,820,000.00 USD | 7,350,000.00 USD | 0.00 USD | `+60.05%` | `2,020.80` |
| `Live` | `Short` | `3645.00` | 565,860,000.00 USD | 44,640.00 USD | 0.00 USD | `+60.49%` | `12.25` |
| `Live` | `Short` | `3655.00` | 566,020,000.00 USD | 161,510.00 USD | 0.00 USD | `+60.94%` | `44.19` |
| `Live` | `Short` | `3665.00` | 566,290,000.00 USD | 264,890.00 USD | 0.00 USD | `+61.38%` | `72.28` |
| `Live` | `Short` | `3675.00` | 573,230,000.00 USD | 6,940,000.00 USD | 0.00 USD | `+61.82%` | `1,889.55` |
| `Live` | `Short` | `3685.00` | 573,430,000.00 USD | 197,070.00 USD | 0.00 USD | `+62.26%` | `53.48` |
| `Live` | `Short` | `3695.00` | 574,180,000.00 USD | 753,490.00 USD | 0.00 USD | `+62.70%` | `203.92` |
| `Live` | `Short` | `3705.00` | 574,200,000.00 USD | 16,570.00 USD | 0.00 USD | `+63.14%` | `4.47` |
| `Live` | `Short` | `3715.00` | 575,900,000.00 USD | 1,700,000.00 USD | 0.00 USD | `+63.58%` | `458.22` |
| `Live` | `Short` | `3725.00` | 576,280,000.00 USD | 379,690.00 USD | 0.00 USD | `+64.02%` | `101.93` |
| `Live` | `Short` | `3735.00` | 577,360,000.00 USD | 1,070,000.00 USD | 0.00 USD | `+64.46%` | `287.21` |
| `Live` | `Short` | `3745.00` | 578,200,000.00 USD | 840,410.00 USD | 0.00 USD | `+64.90%` | `224.41` |
| `Live` | `Short` | `3755.00` | 578,210,000.00 USD | 17,520.00 USD | 0.00 USD | `+65.34%` | `4.67` |
| `Live` | `Short` | `3765.00` | 580,160,000.00 USD | 1,940,000.00 USD | 0.00 USD | `+65.78%` | `516.13` |
| `Live` | `Short` | `3775.00` | 581,020,000.00 USD | 862,520.00 USD | 0.00 USD | `+66.22%` | `228.48` |
| `Live` | `Short` | `3785.00` | 583,390,000.00 USD | 2,370,000.00 USD | 0.00 USD | `+66.66%` | `627.18` |
| `Live` | `Short` | `3795.00` | 587,530,000.00 USD | 4,140,000.00 USD | 0.00 USD | `+67.10%` | `1,090.31` |
| `Live` | `Short` | `3805.00` | 587,530,000.00 USD | 3,490.00 USD | 0.00 USD | `+67.54%` | `0.92` |
| `Live` | `Short` | `3815.00` | 588,350,000.00 USD | 812,690.00 USD | 0.00 USD | `+67.98%` | `213.03` |
| `Live` | `Short` | `3825.00` | 590,540,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+68.42%` | `573.33` |
| `Live` | `Short` | `3835.00` | 670,250,000.00 USD | 79,710,000.00 USD | 0.00 USD | `+68.86%` | `20,783.80` |
| `Live` | `Short` | `3845.00` | 706,050,000.00 USD | 35,800,000.00 USD | 0.00 USD | `+69.30%` | `9,310.86` |
| `Live` | `Short` | `3855.00` | 706,220,000.00 USD | 169,550.00 USD | 0.00 USD | `+69.74%` | `43.98` |
| `Live` | `Short` | `3865.00` | 708,020,000.00 USD | 1,800,000.00 USD | 0.00 USD | `+70.18%` | `465.74` |
| `Live` | `Short` | `3875.00` | 708,940,000.00 USD | 928,140.00 USD | 0.00 USD | `+70.62%` | `239.52` |
| `Live` | `Short` | `3885.00` | 711,810,000.00 USD | 2,860,000.00 USD | 0.00 USD | `+71.06%` | `737.30` |
| `Live` | `Short` | `3895.00` | 746,250,000.00 USD | 34,440,000.00 USD | 0.00 USD | `+71.50%` | `8,842.62` |
| `Live` | `Short` | `3905.00` | 748,670,000.00 USD | 2,420,000.00 USD | 0.00 USD | `+71.94%` | `618.47` |
| `Live` | `Short` | `3915.00` | 748,670,000.00 USD | 7,060.00 USD | 0.00 USD | `+72.38%` | `1.80` |
| `Live` | `Short` | `3925.00` | 749,060,000.00 USD | 385,990.00 USD | 0.00 USD | `+72.82%` | `98.34` |
| `Live` | `Short` | `3935.00` | 749,070,000.00 USD | 6,960.00 USD | 0.00 USD | `+73.26%` | `1.77` |
| `Live` | `Short` | `3945.00` | 749,070,000.00 USD | 2,300.00 USD | 0.00 USD | `+73.70%` | `0.58` |
| `Live` | `Short` | `3955.00` | 749,270,000.00 USD | 198,760.00 USD | 0.00 USD | `+74.14%` | `50.26` |
| `Live` | `Short` | `3965.00` | 750,040,000.00 USD | 776,400.00 USD | 0.00 USD | `+74.59%` | `195.81` |
| `Live` | `Short` | `3975.00` | 1,170,000,000.00 USD | 423,630,000.00 USD | 0.00 USD | `+75.03%` | `106,574.37` |
| `Live` | `Short` | `3985.00` | 1,170,000,000.00 USD | 816,840.00 USD | 0.00 USD | `+75.47%` | `204.98` |
| `Live` | `Short` | `3995.00` | 1,170,000,000.00 USD | 235,910.00 USD | 0.00 USD | `+75.91%` | `59.05` |
| `Live` | `Short` | `4005.00` | 1,170,000,000.00 USD | 58,240.00 USD | 0.00 USD | `+76.35%` | `14.54` |
| `Live` | `Short` | `4015.00` | 1,210,000,000.00 USD | 31,070,000.00 USD | 0.00 USD | `+76.79%` | `7,738.27` |
| `Live` | `Short` | `4025.00` | 1,210,000,000.00 USD | 378,560.00 USD | 0.00 USD | `+77.23%` | `94.05` |
| `Live` | `Short` | `4035.00` | 1,210,000,000.00 USD | 123,170.00 USD | 0.00 USD | `+77.67%` | `30.53` |
| `Live` | `Short` | `4045.00` | 1,210,000,000.00 USD | 477,480.00 USD | 0.00 USD | `+78.11%` | `118.04` |
| `Live` | `Short` | `4055.00` | 1,210,000,000.00 USD | 1,710,000.00 USD | 0.00 USD | `+78.55%` | `421.81` |
| `Live` | `Short` | `4065.00` | 1,210,000,000.00 USD | 19,210.00 USD | 0.00 USD | `+78.99%` | `4.73` |
| `Live` | `Short` | `4075.00` | 1,210,000,000.00 USD | 126,010.00 USD | 0.00 USD | `+79.43%` | `30.92` |
| `Live` | `Short` | `4085.00` | 1,210,000,000.00 USD | 3,320.00 USD | 0.00 USD | `+79.87%` | `0.81` |
| `Live` | `Short` | `4095.00` | 1,210,000,000.00 USD | 36,480.00 USD | 0.00 USD | `+80.31%` | `8.91` |
| `Live` | `Short` | `4105.00` | 1,220,000,000.00 USD | 6,850,000.00 USD | 0.00 USD | `+80.75%` | `1,668.23` |
| `Live` | `Short` | `4115.00` | 1,220,000,000.00 USD | 139,550.00 USD | 0.00 USD | `+81.19%` | `33.91` |
| `Live` | `Short` | `4125.00` | 1,310,000,000.00 USD | 92,410,000.00 USD | 0.00 USD | `+81.63%` | `22,401.95` |
| `Live` | `Short` | `4135.00` | 1,310,000,000.00 USD | 95,240.00 USD | 0.00 USD | `+82.07%` | `23.03` |
| `Live` | `Short` | `4145.00` | 1,310,000,000.00 USD | 1,210,000.00 USD | 0.00 USD | `+82.51%` | `292.07` |
| `Live` | `Short` | `4155.00` | 1,310,000,000.00 USD | 113,950.00 USD | 0.00 USD | `+82.95%` | `27.43` |
| `Live` | `Short` | `4165.00` | 1,310,000,000.00 USD | 116,140.00 USD | 0.00 USD | `+83.39%` | `27.89` |
| `Live` | `Short` | `4175.00` | 1,310,000,000.00 USD | 975,990.00 USD | 0.00 USD | `+83.83%` | `233.77` |
| `Live` | `Short` | `4185.00` | 1,310,000,000.00 USD | 428,230.00 USD | 0.00 USD | `+84.27%` | `102.32` |
| `Live` | `Short` | `4195.00` | 1,310,000,000.00 USD | 258,150.00 USD | 0.00 USD | `+84.71%` | `61.54` |
| `Live` | `Short` | `4205.00` | 1,320,000,000.00 USD | 4,050,000.00 USD | 0.00 USD | `+85.15%` | `963.96` |
| `Live` | `Short` | `4215.00` | 1,320,000,000.00 USD | 47,330.00 USD | 0.00 USD | `+85.59%` | `11.23` |
| `Live` | `Short` | `4225.00` | 1,320,000,000.00 USD | 71,560.00 USD | 0.00 USD | `+86.03%` | `16.94` |
| `Live` | `Short` | `4235.00` | 1,320,000,000.00 USD | 433,220.00 USD | 0.00 USD | `+86.47%` | `102.30` |
| `Live` | `Short` | `4245.00` | 1,320,000,000.00 USD | 7,520.00 USD | 0.00 USD | `+86.91%` | `1.77` |
| `Live` | `Short` | `4255.00` | 1,320,000,000.00 USD | 5,310,000.00 USD | 0.00 USD | `+87.35%` | `1,248.15` |
| `Live` | `Short` | `4265.00` | 1,320,000,000.00 USD | 54,480.00 USD | 0.00 USD | `+87.79%` | `12.77` |
| `Live` | `Short` | `4275.00` | 1,320,000,000.00 USD | 50,950.00 USD | 0.00 USD | `+88.23%` | `11.92` |
| `Live` | `Short` | `4285.00` | 1,320,000,000.00 USD | 480,150.00 USD | 0.00 USD | `+88.68%` | `112.05` |
| `Live` | `Short` | `4295.00` | 1,320,000,000.00 USD | 169,410.00 USD | 0.00 USD | `+89.12%` | `39.44` |
| `Live` | `Short` | `4305.00` | 1,320,000,000.00 USD | 239.36 USD | 0.00 USD | `+89.56%` | `0.06` |
| `Live` | `Short` | `4315.00` | 1,320,000,000.00 USD | 9,540.00 USD | 0.00 USD | `+90.00%` | `2.21` |
| `Live` | `Short` | `4325.00` | 1,320,000,000.00 USD | 18,220.00 USD | 0.00 USD | `+90.44%` | `4.21` |
| `Live` | `Short` | `4335.00` | 1,330,000,000.00 USD | 4,160,000.00 USD | 0.00 USD | `+90.88%` | `959.43` |
| `Live` | `Short` | `4345.00` | 1,330,000,000.00 USD | 53,810.00 USD | 0.00 USD | `+91.32%` | `12.38` |
| `Live` | `Short` | `4365.00` | 1,330,000,000.00 USD | 1,310,000.00 USD | 0.00 USD | `+92.20%` | `301.20` |
| `Live` | `Short` | `4375.00` | 1,330,000,000.00 USD | 19,610.00 USD | 0.00 USD | `+92.64%` | `4.48` |
| `Live` | `Short` | `4395.00` | 1,330,000,000.00 USD | 451,490.00 USD | 0.00 USD | `+93.52%` | `102.73` |
| `Live` | `Short` | `4405.00` | 1,330,000,000.00 USD | 23,060.00 USD | 0.00 USD | `+93.96%` | `5.24` |
| `Live` | `Short` | `4415.00` | 1,330,000,000.00 USD | 5,890,000.00 USD | 0.00 USD | `+94.40%` | `1,334.60` |
| `Live` | `Short` | `4425.00` | 1,330,000,000.00 USD | 3,120.00 USD | 0.00 USD | `+94.84%` | `0.71` |
| `Live` | `Short` | `4435.00` | 1,330,000,000.00 USD | 19,840.00 USD | 0.00 USD | `+95.28%` | `4.47` |
| `Live` | `Short` | `4445.00` | 1,330,000,000.00 USD | 1,920.00 USD | 0.00 USD | `+95.72%` | `0.43` |
| `Live` | `Short` | `4455.00` | 1,330,000,000.00 USD | 66,260.00 USD | 0.00 USD | `+96.16%` | `14.87` |
| `Live` | `Short` | `4465.00` | 1,340,000,000.00 USD | 1,170,000.00 USD | 0.00 USD | `+96.60%` | `261.49` |
| `Live` | `Short` | `4475.00` | 1,340,000,000.00 USD | 49,510.00 USD | 0.00 USD | `+97.04%` | `11.06` |
| `Live` | `Short` | `4485.00` | 1,340,000,000.00 USD | 166,140.00 USD | 0.00 USD | `+97.48%` | `37.04` |
| `Live` | `Short` | `4495.00` | 1,340,000,000.00 USD | 1,550,000.00 USD | 0.00 USD | `+97.92%` | `344.04` |
| `Live` | `Short` | `4505.00` | 1,340,000,000.00 USD | 427.52 USD | 0.00 USD | `+98.36%` | `0.09` |
| `Live` | `Short` | `4515.00` | 1,340,000,000.00 USD | 23,420.00 USD | 0.00 USD | `+98.80%` | `5.19` |
| `Live` | `Short` | `4525.00` | 1,340,000,000.00 USD | 7,660,000.00 USD | 0.00 USD | `+99.24%` | `1,692.75` |
| `Live` | `Short` | `4535.00` | 1,340,000,000.00 USD | 55,010.00 USD | 0.00 USD | `+99.68%` | `12.13` |
| `Live` | `Short` | `4545.00` | 1,340,000,000.00 USD | 12,730.00 USD | 0.00 USD | `+100.12%` | `2.80` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `505.00` | 73,760,000.00 USD | 0.00 USD | 16,270.00 USD | `-77.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.00` | 73,740,000.00 USD | 0.00 USD | 563.16 USD | `-75.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.00` | 73,740,000.00 USD | 0.00 USD | 583.40 USD | `-71.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.00` | 73,740,000.00 USD | 0.00 USD | 242.21 USD | `-69.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.00` | 73,740,000.00 USD | 0.00 USD | 885.90 USD | `-68.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `755.00` | 73,740,000.00 USD | 0.00 USD | 177.27 USD | `-66.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `795.00` | 73,740,000.00 USD | 0.00 USD | 104.22 USD | `-64.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `805.00` | 73,740,000.00 USD | 0.00 USD | 2,090.00 USD | `-64.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `835.00` | 73,740,000.00 USD | 0.00 USD | 1,670.00 USD | `-63.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `865.00` | 73,740,000.00 USD | 0.00 USD | 139,280.00 USD | `-61.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `875.00` | 73,600,000.00 USD | 0.00 USD | 918.49 USD | `-61.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `885.00` | 73,590,000.00 USD | 0.00 USD | 3,130.00 USD | `-61.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `905.00` | 73,590,000.00 USD | 0.00 USD | 2,780.00 USD | `-60.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `985.00` | 73,590,000.00 USD | 0.00 USD | 516.34 USD | `-56.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `995.00` | 73,590,000.00 USD | 0.00 USD | 100.50 USD | `-56.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1005.00` | 73,590,000.00 USD | 0.00 USD | 223,740.00 USD | `-55.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1015.00` | 73,360,000.00 USD | 0.00 USD | 438.28 USD | `-55.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1025.00` | 73,360,000.00 USD | 0.00 USD | 112.03 USD | `-54.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1065.00` | 73,360,000.00 USD | 0.00 USD | 1,060.00 USD | `-53.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1075.00` | 73,360,000.00 USD | 0.00 USD | 995.34 USD | `-52.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1105.00` | 73,360,000.00 USD | 0.00 USD | 1,610.00 USD | `-51.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1115.00` | 73,360,000.00 USD | 0.00 USD | 11,050.00 USD | `-50.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1125.00` | 73,350,000.00 USD | 0.00 USD | 1,320.00 USD | `-50.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1155.00` | 73,350,000.00 USD | 0.00 USD | 1,000.00 USD | `-49.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1175.00` | 73,350,000.00 USD | 0.00 USD | 189.53 USD | `-48.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1185.00` | 73,350,000.00 USD | 0.00 USD | 228.47 USD | `-47.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1205.00` | 73,350,000.00 USD | 0.00 USD | 3,110.00 USD | `-46.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1225.00` | 73,340,000.00 USD | 0.00 USD | 995.93 USD | `-46.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1245.00` | 73,340,000.00 USD | 0.00 USD | 951.93 USD | `-45.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1255.00` | 73,340,000.00 USD | 0.00 USD | 6,810.00 USD | `-44.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1285.00` | 73,330,000.00 USD | 0.00 USD | 9,050.00 USD | `-43.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1295.00` | 73,330,000.00 USD | 0.00 USD | 7,030.00 USD | `-42.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1305.00` | 73,320,000.00 USD | 0.00 USD | 23,030.00 USD | `-42.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1315.00` | 73,300,000.00 USD | 0.00 USD | 1,440.00 USD | `-42.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1345.00` | 73,290,000.00 USD | 0.00 USD | 141,950.00 USD | `-40.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1355.00` | 73,150,000.00 USD | 0.00 USD | 128.86 USD | `-40.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1365.00` | 73,150,000.00 USD | 0.00 USD | 1,270.00 USD | `-39.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1375.00` | 73,150,000.00 USD | 0.00 USD | 4,160.00 USD | `-39.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1385.00` | 73,150,000.00 USD | 0.00 USD | 297.36 USD | `-39.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1395.00` | 73,150,000.00 USD | 0.00 USD | 535,600.00 USD | `-38.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1405.00` | 72,610,000.00 USD | 0.00 USD | 18,840.00 USD | `-38.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1425.00` | 72,590,000.00 USD | 0.00 USD | 6,450.00 USD | `-37.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1435.00` | 72,590,000.00 USD | 0.00 USD | 852.10 USD | `-36.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1445.00` | 72,580,000.00 USD | 0.00 USD | 1,490.00 USD | `-36.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1455.00` | 72,580,000.00 USD | 0.00 USD | 5,680.00 USD | `-35.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1465.00` | 72,580,000.00 USD | 0.00 USD | 19,460.00 USD | `-35.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1475.00` | 72,560,000.00 USD | 0.00 USD | 2,600.00 USD | `-35.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1485.00` | 72,560,000.00 USD | 0.00 USD | 18,710.00 USD | `-34.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1495.00` | 72,540,000.00 USD | 0.00 USD | 11,570.00 USD | `-34.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1505.00` | 72,530,000.00 USD | 0.00 USD | 80,620.00 USD | `-33.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1515.00` | 72,440,000.00 USD | 0.00 USD | 11,140.00 USD | `-33.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1525.00` | 72,430,000.00 USD | 0.00 USD | 31,900.00 USD | `-32.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1535.00` | 72,400,000.00 USD | 0.00 USD | 983.78 USD | `-32.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1545.00` | 72,400,000.00 USD | 0.00 USD | 960.99 USD | `-31.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1555.00` | 72,400,000.00 USD | 0.00 USD | 58,630.00 USD | `-31.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1565.00` | 72,340,000.00 USD | 0.00 USD | 6,260.00 USD | `-31.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1575.00` | 72,330,000.00 USD | 0.00 USD | 190,890.00 USD | `-30.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1585.00` | 72,140,000.00 USD | 0.00 USD | 7,750.00 USD | `-30.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1595.00` | 72,140,000.00 USD | 0.00 USD | 4,040.00 USD | `-29.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1605.00` | 72,130,000.00 USD | 0.00 USD | 432,330.00 USD | `-29.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1615.00` | 71,700,000.00 USD | 0.00 USD | 28,870.00 USD | `-28.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1625.00` | 71,670,000.00 USD | 0.00 USD | 13,590.00 USD | `-28.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1635.00` | 71,660,000.00 USD | 0.00 USD | 5,510.00 USD | `-28.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1645.00` | 71,650,000.00 USD | 0.00 USD | 326,130.00 USD | `-27.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1655.00` | 71,330,000.00 USD | 0.00 USD | 35,070.00 USD | `-27.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1665.00` | 71,290,000.00 USD | 0.00 USD | 3,110.00 USD | `-26.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1675.00` | 71,290,000.00 USD | 0.00 USD | 289.27 USD | `-26.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1685.00` | 71,290,000.00 USD | 0.00 USD | 35,300.00 USD | `-25.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1695.00` | 71,250,000.00 USD | 0.00 USD | 8,490.00 USD | `-25.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1705.00` | 71,240,000.00 USD | 0.00 USD | 83,330.00 USD | `-24.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1715.00` | 71,160,000.00 USD | 0.00 USD | 16,350.00 USD | `-24.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1725.00` | 71,140,000.00 USD | 0.00 USD | 50,170.00 USD | `-24.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1735.00` | 71,090,000.00 USD | 0.00 USD | 28,150.00 USD | `-23.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1745.00` | 71,070,000.00 USD | 0.00 USD | 3,180.00 USD | `-23.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1755.00` | 71,060,000.00 USD | 0.00 USD | 504,110.00 USD | `-22.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1765.00` | 70,560,000.00 USD | 0.00 USD | 76,460.00 USD | `-22.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1775.00` | 70,480,000.00 USD | 0.00 USD | 3,090.00 USD | `-21.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1785.00` | 70,480,000.00 USD | 0.00 USD | 8,500.00 USD | `-21.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1795.00` | 70,470,000.00 USD | 0.00 USD | 184,330.00 USD | `-20.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1805.00` | 70,290,000.00 USD | 0.00 USD | 655,290.00 USD | `-20.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1815.00` | 69,630,000.00 USD | 0.00 USD | 135,310.00 USD | `-20.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1825.00` | 69,500,000.00 USD | 0.00 USD | 27,250.00 USD | `-19.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1835.00` | 69,470,000.00 USD | 0.00 USD | 18,240.00 USD | `-19.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1845.00` | 69,450,000.00 USD | 0.00 USD | 14,290.00 USD | `-18.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1855.00` | 69,440,000.00 USD | 0.00 USD | 477,550.00 USD | `-18.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1865.00` | 68,960,000.00 USD | 0.00 USD | 33,750.00 USD | `-17.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1875.00` | 68,920,000.00 USD | 0.00 USD | 18,190,000.00 USD | `-17.44%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1885.00` | 50,730,000.00 USD | 0.00 USD | 4,390.00 USD | `-17.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1895.00` | 50,730,000.00 USD | 0.00 USD | 56,040.00 USD | `-16.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1905.00` | 50,670,000.00 USD | 0.00 USD | 145,330.00 USD | `-16.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1915.00` | 50,520,000.00 USD | 0.00 USD | 8,120,000.00 USD | `-15.68%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1925.00` | 42,400,000.00 USD | 0.00 USD | 16,410,000.00 USD | `-15.24%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1935.00` | 25,990,000.00 USD | 0.00 USD | 79,950.00 USD | `-14.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1945.00` | 25,910,000.00 USD | 0.00 USD | 43,390.00 USD | `-14.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1955.00` | 25,870,000.00 USD | 0.00 USD | 54,590.00 USD | `-13.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1965.00` | 25,810,000.00 USD | 0.00 USD | 19,500.00 USD | `-13.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1975.00` | 25,790,000.00 USD | 0.00 USD | 70,060.00 USD | `-13.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1985.00` | 25,720,000.00 USD | 0.00 USD | 96,910.00 USD | `-12.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1995.00` | 25,630,000.00 USD | 0.00 USD | 233,160.00 USD | `-12.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2005.00` | 25,390,000.00 USD | 0.00 USD | 1,040,000.00 USD | `-11.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2015.00` | 24,350,000.00 USD | 0.00 USD | 505,510.00 USD | `-11.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2025.00` | 23,850,000.00 USD | 0.00 USD | 536,580.00 USD | `-10.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2035.00` | 23,310,000.00 USD | 0.00 USD | 99,030.00 USD | `-10.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2045.00` | 23,210,000.00 USD | 0.00 USD | 17,890.00 USD | `-9.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2055.00` | 23,190,000.00 USD | 0.00 USD | 226,270.00 USD | `-9.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2065.00` | 22,970,000.00 USD | 0.00 USD | 42,200.00 USD | `-9.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2075.00` | 22,920,000.00 USD | 0.00 USD | 34,010.00 USD | `-8.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2085.00` | 22,890,000.00 USD | 0.00 USD | 59,460.00 USD | `-8.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2095.00` | 22,830,000.00 USD | 0.00 USD | 50,460.00 USD | `-7.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2105.00` | 22,780,000.00 USD | 0.00 USD | 227,370.00 USD | `-7.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2115.00` | 22,550,000.00 USD | 0.00 USD | 124,450.00 USD | `-6.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2125.00` | 22,430,000.00 USD | 0.00 USD | 207,440.00 USD | `-6.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2135.00` | 22,220,000.00 USD | 0.00 USD | 44,240.00 USD | `-5.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2145.00` | 22,180,000.00 USD | 0.00 USD | 81,080.00 USD | `-5.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2155.00` | 22,100,000.00 USD | 0.00 USD | 1,490,000.00 USD | `-5.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2165.00` | 20,610,000.00 USD | 0.00 USD | 1,400,000.00 USD | `-4.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2175.00` | 19,210,000.00 USD | 0.00 USD | 607,100.00 USD | `-4.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2185.00` | 18,600,000.00 USD | 0.00 USD | 418,060.00 USD | `-3.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2195.00` | 18,190,000.00 USD | 0.00 USD | 2,040,000.00 USD | `-3.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2205.00` | 16,140,000.00 USD | 0.00 USD | 3,550,000.00 USD | `-2.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2215.00` | 12,600,000.00 USD | 0.00 USD | 1,060,000.00 USD | `-2.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2225.00` | 11,530,000.00 USD | 0.00 USD | 3,860,000.00 USD | `-2.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2235.00` | 7,670,000.00 USD | 0.00 USD | 1,580,000.00 USD | `-1.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2245.00` | 6,090,000.00 USD | 0.00 USD | 5,410,000.00 USD | `-1.15%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2255.00` | 681,600.00 USD | 0.00 USD | 624,280.00 USD | `-0.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2265.00` | 57,320.00 USD | 0.00 USD | 57,320.00 USD | `-0.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2275.00` | 1,660.00 USD | 1,660.00 USD | 0.00 USD | `+0.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2285.00` | 370,770.00 USD | 369,110.00 USD | 0.00 USD | `+0.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2295.00` | 1,110,000.00 USD | 734,690.00 USD | 0.00 USD | `+1.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2305.00` | 4,440,000.00 USD | 3,330,000.00 USD | 0.00 USD | `+1.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2315.00` | 8,100,000.00 USD | 3,660,000.00 USD | 0.00 USD | `+1.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2325.00` | 9,950,000.00 USD | 1,850,000.00 USD | 0.00 USD | `+2.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2335.00` | 10,090,000.00 USD | 142,880.00 USD | 0.00 USD | `+2.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2345.00` | 11,370,000.00 USD | 1,280,000.00 USD | 0.00 USD | `+3.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2355.00` | 14,430,000.00 USD | 3,070,000.00 USD | 0.00 USD | `+3.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2365.00` | 14,860,000.00 USD | 429,010.00 USD | 0.00 USD | `+4.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2375.00` | 15,000,000.00 USD | 133,570.00 USD | 0.00 USD | `+4.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2385.00` | 15,110,000.00 USD | 116,900.00 USD | 0.00 USD | `+5.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2395.00` | 16,280,000.00 USD | 1,160,000.00 USD | 0.00 USD | `+5.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2405.00` | 18,250,000.00 USD | 1,980,000.00 USD | 0.00 USD | `+5.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2415.00` | 18,560,000.00 USD | 313,270.00 USD | 0.00 USD | `+6.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2425.00` | 21,550,000.00 USD | 2,980,000.00 USD | 0.00 USD | `+6.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2435.00` | 21,720,000.00 USD | 173,490.00 USD | 0.00 USD | `+7.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2445.00` | 22,290,000.00 USD | 572,240.00 USD | 0.00 USD | `+7.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2455.00` | 22,810,000.00 USD | 519,390.00 USD | 0.00 USD | `+8.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2465.00` | 24,950,000.00 USD | 2,140,000.00 USD | 0.00 USD | `+8.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2475.00` | 25,160,000.00 USD | 204,200.00 USD | 0.00 USD | `+8.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2485.00` | 27,290,000.00 USD | 2,130,000.00 USD | 0.00 USD | `+9.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2495.00` | 27,730,000.00 USD | 439,530.00 USD | 0.00 USD | `+9.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2505.00` | 32,780,000.00 USD | 5,050,000.00 USD | 0.00 USD | `+10.30%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2515.00` | 40,530,000.00 USD | 7,750,000.00 USD | 0.00 USD | `+10.74%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2525.00` | 43,740,000.00 USD | 3,200,000.00 USD | 0.00 USD | `+11.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2535.00` | 43,800,000.00 USD | 62,050.00 USD | 0.00 USD | `+11.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2545.00` | 45,980,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+12.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2555.00` | 46,260,000.00 USD | 282,650.00 USD | 0.00 USD | `+12.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2565.00` | 48,650,000.00 USD | 2,390,000.00 USD | 0.00 USD | `+12.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2575.00` | 48,780,000.00 USD | 128,450.00 USD | 0.00 USD | `+13.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2585.00` | 51,460,000.00 USD | 2,680,000.00 USD | 0.00 USD | `+13.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2595.00` | 51,470,000.00 USD | 13,760.00 USD | 0.00 USD | `+14.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2605.00` | 54,450,000.00 USD | 2,980,000.00 USD | 0.00 USD | `+14.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2615.00` | 54,600,000.00 USD | 148,690.00 USD | 0.00 USD | `+15.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2625.00` | 56,810,000.00 USD | 2,210,000.00 USD | 0.00 USD | `+15.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2635.00` | 56,960,000.00 USD | 155,950.00 USD | 0.00 USD | `+16.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2645.00` | 59,090,000.00 USD | 2,130,000.00 USD | 0.00 USD | `+16.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2655.00` | 59,390,000.00 USD | 305,400.00 USD | 0.00 USD | `+16.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2665.00` | 61,540,000.00 USD | 2,150,000.00 USD | 0.00 USD | `+17.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2675.00` | 61,890,000.00 USD | 351,060.00 USD | 0.00 USD | `+17.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2685.00` | 64,070,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+18.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2695.00` | 64,160,000.00 USD | 95,970.00 USD | 0.00 USD | `+18.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2705.00` | 69,210,000.00 USD | 5,050,000.00 USD | 0.00 USD | `+19.11%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2715.00` | 69,290,000.00 USD | 76,590.00 USD | 0.00 USD | `+19.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2725.00` | 71,760,000.00 USD | 2,470,000.00 USD | 0.00 USD | `+19.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2735.00` | 71,810,000.00 USD | 55,230.00 USD | 0.00 USD | `+20.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2745.00` | 74,070,000.00 USD | 2,260,000.00 USD | 0.00 USD | `+20.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2755.00` | 74,830,000.00 USD | 761,370.00 USD | 0.00 USD | `+21.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2765.00` | 77,220,000.00 USD | 2,390,000.00 USD | 0.00 USD | `+21.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2775.00` | 77,800,000.00 USD | 577,690.00 USD | 0.00 USD | `+22.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2785.00` | 80,070,000.00 USD | 2,270,000.00 USD | 0.00 USD | `+22.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2795.00` | 80,080,000.00 USD | 17,550.00 USD | 0.00 USD | `+23.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2805.00` | 83,210,000.00 USD | 3,120,000.00 USD | 0.00 USD | `+23.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2815.00` | 83,260,000.00 USD | 52,670.00 USD | 0.00 USD | `+23.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2825.00` | 83,320,000.00 USD | 63,490.00 USD | 0.00 USD | `+24.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2835.00` | 83,610,000.00 USD | 289,000.00 USD | 0.00 USD | `+24.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2845.00` | 84,620,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+25.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2855.00` | 86,030,000.00 USD | 1,410,000.00 USD | 0.00 USD | `+25.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2865.00` | 86,040,000.00 USD | 10,290.00 USD | 0.00 USD | `+26.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2875.00` | 86,040,000.00 USD | 2,460.00 USD | 0.00 USD | `+26.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2885.00` | 86,350,000.00 USD | 303,660.00 USD | 0.00 USD | `+27.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2895.00` | 86,370,000.00 USD | 21,290.00 USD | 0.00 USD | `+27.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2905.00` | 87,860,000.00 USD | 1,490,000.00 USD | 0.00 USD | `+27.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2915.00` | 87,870,000.00 USD | 10,340.00 USD | 0.00 USD | `+28.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2925.00` | 87,870,000.00 USD | 3,050.00 USD | 0.00 USD | `+28.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2935.00` | 87,920,000.00 USD | 53,040.00 USD | 0.00 USD | `+29.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2945.00` | 87,960,000.00 USD | 34,650.00 USD | 0.00 USD | `+29.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2955.00` | 88,040,000.00 USD | 85,030.00 USD | 0.00 USD | `+30.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2965.00` | 88,160,000.00 USD | 113,340.00 USD | 0.00 USD | `+30.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2975.00` | 88,300,000.00 USD | 147,920.00 USD | 0.00 USD | `+30.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2985.00` | 88,480,000.00 USD | 177,120.00 USD | 0.00 USD | `+31.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2995.00` | 90,420,000.00 USD | 1,940,000.00 USD | 0.00 USD | `+31.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3005.00` | 98,930,000.00 USD | 8,510,000.00 USD | 0.00 USD | `+32.31%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `3015.00` | 98,940,000.00 USD | 6,950.00 USD | 0.00 USD | `+32.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3025.00` | 98,970,000.00 USD | 37,610.00 USD | 0.00 USD | `+33.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3035.00` | 99,050,000.00 USD | 73,700.00 USD | 0.00 USD | `+33.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3045.00` | 99,070,000.00 USD | 22,460.00 USD | 0.00 USD | `+34.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3055.00` | 99,850,000.00 USD | 783,940.00 USD | 0.00 USD | `+34.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3065.00` | 99,860,000.00 USD | 3,080.00 USD | 0.00 USD | `+34.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3075.00` | 99,910,000.00 USD | 49,330.00 USD | 0.00 USD | `+35.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3085.00` | 99,930,000.00 USD | 23,940.00 USD | 0.00 USD | `+35.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3095.00` | 99,930,000.00 USD | 928.50 USD | 0.00 USD | `+36.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3105.00` | 114,680,000.00 USD | 14,750,000.00 USD | 0.00 USD | `+36.72%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `3115.00` | 114,840,000.00 USD | 154,140.00 USD | 0.00 USD | `+37.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3125.00` | 115,250,000.00 USD | 414,660.00 USD | 0.00 USD | `+37.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3145.00` | 115,250,000.00 USD | 2,530.00 USD | 0.00 USD | `+38.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3155.00` | 115,320,000.00 USD | 68,940.00 USD | 0.00 USD | `+38.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3165.00` | 115,340,000.00 USD | 21,490.00 USD | 0.00 USD | `+39.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3175.00` | 115,360,000.00 USD | 17,040.00 USD | 0.00 USD | `+39.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3185.00` | 115,360,000.00 USD | 1,330.00 USD | 0.00 USD | `+40.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3195.00` | 115,390,000.00 USD | 29,450.00 USD | 0.00 USD | `+40.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3205.00` | 116,600,000.00 USD | 1,210,000.00 USD | 0.00 USD | `+41.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3215.00` | 116,600,000.00 USD | 1,290.00 USD | 0.00 USD | `+41.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3225.00` | 116,610,000.00 USD | 3,740.00 USD | 0.00 USD | `+42.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3235.00` | 116,640,000.00 USD | 30,790.00 USD | 0.00 USD | `+42.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3245.00` | 116,700,000.00 USD | 56,110.00 USD | 0.00 USD | `+42.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3255.00` | 116,930,000.00 USD | 236,580.00 USD | 0.00 USD | `+43.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3265.00` | 116,950,000.00 USD | 15,710.00 USD | 0.00 USD | `+43.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3275.00` | 116,950,000.00 USD | 1,630.00 USD | 0.00 USD | `+44.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3285.00` | 117,090,000.00 USD | 141,980.00 USD | 0.00 USD | `+44.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3295.00` | 117,110,000.00 USD | 15,350.00 USD | 0.00 USD | `+45.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3305.00` | 118,500,000.00 USD | 1,400,000.00 USD | 0.00 USD | `+45.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3315.00` | 118,890,000.00 USD | 385,510.00 USD | 0.00 USD | `+45.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3325.00` | 118,910,000.00 USD | 18,270.00 USD | 0.00 USD | `+46.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3335.00` | 118,920,000.00 USD | 18,080.00 USD | 0.00 USD | `+46.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3345.00` | 118,930,000.00 USD | 617.15 USD | 0.00 USD | `+47.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3355.00` | 118,930,000.00 USD | 837.74 USD | 0.00 USD | `+47.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3365.00` | 118,930,000.00 USD | 2,780.00 USD | 0.00 USD | `+48.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3375.00` | 118,950,000.00 USD | 21,260.00 USD | 0.00 USD | `+48.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3385.00` | 119,010,000.00 USD | 58,010.00 USD | 0.00 USD | `+49.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3395.00` | 119,360,000.00 USD | 355,050.00 USD | 0.00 USD | `+49.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3405.00` | 120,710,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+49.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3415.00` | 120,710,000.00 USD | 3,510.00 USD | 0.00 USD | `+50.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3425.00` | 120,730,000.00 USD | 16,310.00 USD | 0.00 USD | `+50.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3445.00` | 120,740,000.00 USD | 15,030.00 USD | 0.00 USD | `+51.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3455.00` | 120,760,000.00 USD | 18,600.00 USD | 0.00 USD | `+52.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3465.00` | 120,760,000.00 USD | 495.50 USD | 0.00 USD | `+52.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3475.00` | 120,760,000.00 USD | 3,190.00 USD | 0.00 USD | `+53.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3485.00` | 120,810,000.00 USD | 43,610.00 USD | 0.00 USD | `+53.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3495.00` | 120,810,000.00 USD | 158.32 USD | 0.00 USD | `+53.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3505.00` | 121,250,000.00 USD | 444,410.00 USD | 0.00 USD | `+54.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3515.00` | 121,300,000.00 USD | 43,410.00 USD | 0.00 USD | `+54.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3525.00` | 121,300,000.00 USD | 3,690.00 USD | 0.00 USD | `+55.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3535.00` | 121,310,000.00 USD | 9,810.00 USD | 0.00 USD | `+55.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3545.00` | 121,310,000.00 USD | 179.38 USD | 0.00 USD | `+56.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3555.00` | 121,400,000.00 USD | 90,810.00 USD | 0.00 USD | `+56.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3565.00` | 121,400,000.00 USD | 2,300.00 USD | 0.00 USD | `+56.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3585.00` | 121,400,000.00 USD | 354.92 USD | 0.00 USD | `+57.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3595.00` | 121,420,000.00 USD | 13,160.00 USD | 0.00 USD | `+58.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3605.00` | 121,520,000.00 USD | 106,490.00 USD | 0.00 USD | `+58.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3625.00` | 121,530,000.00 USD | 10,210.00 USD | 0.00 USD | `+59.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3635.00` | 121,540,000.00 USD | 7,790.00 USD | 0.00 USD | `+60.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3645.00` | 121,540,000.00 USD | 3,860.00 USD | 0.00 USD | `+60.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3655.00` | 121,550,000.00 USD | 7,740.00 USD | 0.00 USD | `+60.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3665.00` | 121,560,000.00 USD | 8,130.00 USD | 0.00 USD | `+61.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3675.00` | 121,610,000.00 USD | 55,120.00 USD | 0.00 USD | `+61.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3685.00` | 121,620,000.00 USD | 3,550.00 USD | 0.00 USD | `+62.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3705.00` | 121,620,000.00 USD | 819.92 USD | 0.00 USD | `+63.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3715.00` | 121,620,000.00 USD | 323.58 USD | 0.00 USD | `+63.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3725.00` | 121,620,000.00 USD | 1,400.00 USD | 0.00 USD | `+64.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3735.00` | 121,630,000.00 USD | 6,490.00 USD | 0.00 USD | `+64.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3755.00` | 121,630,000.00 USD | 751.00 USD | 0.00 USD | `+65.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3785.00` | 121,630,000.00 USD | 286.90 USD | 0.00 USD | `+66.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3795.00` | 121,630,000.00 USD | 1,560.00 USD | 0.00 USD | `+67.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3805.00` | 122,360,000.00 USD | 734,090.00 USD | 0.00 USD | `+67.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3815.00` | 122,390,000.00 USD | 20,930.00 USD | 0.00 USD | `+67.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3825.00` | 122,390,000.00 USD | 8,380.00 USD | 0.00 USD | `+68.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3835.00` | 122,390,000.00 USD | 711.78 USD | 0.00 USD | `+68.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3845.00` | 122,390,000.00 USD | 355.28 USD | 0.00 USD | `+69.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3855.00` | 122,400,000.00 USD | 5,170.00 USD | 0.00 USD | `+69.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3885.00` | 122,420,000.00 USD | 19,430.00 USD | 0.00 USD | `+71.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3905.00` | 122,430,000.00 USD | 12,120.00 USD | 0.00 USD | `+71.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3915.00` | 123,080,000.00 USD | 646,840.00 USD | 0.00 USD | `+72.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3925.00` | 123,080,000.00 USD | 3,260.00 USD | 0.00 USD | `+72.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3935.00` | 123,120,000.00 USD | 42,570.00 USD | 0.00 USD | `+73.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3945.00` | 123,180,000.00 USD | 59,170.00 USD | 0.00 USD | `+73.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3955.00` | 123,180,000.00 USD | 1,380.00 USD | 0.00 USD | `+74.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3965.00` | 123,180,000.00 USD | 323.54 USD | 0.00 USD | `+74.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3975.00` | 123,190,000.00 USD | 6,960.00 USD | 0.00 USD | `+75.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3985.00` | 123,210,000.00 USD | 14,610.00 USD | 0.00 USD | `+75.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3995.00` | 123,210,000.00 USD | 4,280.00 USD | 0.00 USD | `+75.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4005.00` | 125,850,000.00 USD | 2,640,000.00 USD | 0.00 USD | `+76.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4035.00` | 125,850,000.00 USD | 898.59 USD | 0.00 USD | `+77.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4055.00` | 125,850,000.00 USD | 811.00 USD | 0.00 USD | `+78.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4075.00` | 125,850,000.00 USD | 4,310.00 USD | 0.00 USD | `+79.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4085.00` | 125,850,000.00 USD | 2,800.00 USD | 0.00 USD | `+79.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4105.00` | 125,890,000.00 USD | 39,390.00 USD | 0.00 USD | `+80.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4115.00` | 125,900,000.00 USD | 5,990.00 USD | 0.00 USD | `+81.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4125.00` | 125,900,000.00 USD | 372.90 USD | 0.00 USD | `+81.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4145.00` | 125,900,000.00 USD | 395.43 USD | 0.00 USD | `+82.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4185.00` | 125,900,000.00 USD | 376.65 USD | 0.00 USD | `+84.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4205.00` | 125,940,000.00 USD | 41,200.00 USD | 0.00 USD | `+85.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4215.00` | 125,940,000.00 USD | 460.70 USD | 0.00 USD | `+85.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4225.00` | 125,940,000.00 USD | 1,270.00 USD | 0.00 USD | `+86.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4255.00` | 125,950,000.00 USD | 4,300.00 USD | 0.00 USD | `+87.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4265.00` | 125,950,000.00 USD | 437.16 USD | 0.00 USD | `+87.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4275.00` | 126,010,000.00 USD | 64,550.00 USD | 0.00 USD | `+88.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4285.00` | 126,010,000.00 USD | 1,610.00 USD | 0.00 USD | `+88.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4305.00` | 126,110,000.00 USD | 97,670.00 USD | 0.00 USD | `+89.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4315.00` | 126,110,000.00 USD | 1,070.00 USD | 0.00 USD | `+90.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4345.00` | 126,120,000.00 USD | 11,270.00 USD | 0.00 USD | `+91.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4355.00` | 126,130,000.00 USD | 3,250.00 USD | 0.00 USD | `+91.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4375.00` | 126,170,000.00 USD | 43,750.00 USD | 0.00 USD | `+92.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4385.00` | 126,240,000.00 USD | 64,570.00 USD | 0.00 USD | `+93.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4395.00` | 126,240,000.00 USD | 1,050.00 USD | 0.00 USD | `+93.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4405.00` | 126,280,000.00 USD | 44,050.00 USD | 0.00 USD | `+93.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4415.00` | 126,290,000.00 USD | 11,480.00 USD | 0.00 USD | `+94.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4425.00` | 126,300,000.00 USD | 2,510.00 USD | 0.00 USD | `+94.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4435.00` | 126,470,000.00 USD | 177,400.00 USD | 0.00 USD | `+95.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4455.00` | 126,470,000.00 USD | 641.97 USD | 0.00 USD | `+96.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4465.00` | 126,470,000.00 USD | 1,030.00 USD | 0.00 USD | `+96.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4505.00` | 126,850,000.00 USD | 376,800.00 USD | 0.00 USD | `+98.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4515.00` | 126,850,000.00 USD | 2,280.00 USD | 0.00 USD | `+98.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4525.00` | 126,860,000.00 USD | 6,560.00 USD | 0.00 USD | `+99.24%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `2025.30` | 942,070,000.00 USD | 0.00 USD | 942,070,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD |
| `1D` | `2026.90` | 513,860,000.00 USD | 0.00 USD | 513,860,000.00 USD | 0.00 USD | 943,590.00 USD | 40,210.00 USD |
| `7D` | `2028.60` | 941,890,000.00 USD | 0.00 USD | 941,890,000.00 USD | 0.00 USD | 1,180,000.00 USD | 35,180.00 USD |
| `1D` | `2029.50` | 512,870,000.00 USD | 0.00 USD | 512,870,000.00 USD | 87,180.00 USD | 163,200.00 USD | 43,160.00 USD |
| `7D` | `2031.90` | 940,670,000.00 USD | 0.00 USD | 940,670,000.00 USD | 0.00 USD | 1,450,000.00 USD | 0.00 USD |
| `1D` | `2032.10` | 512,580,000.00 USD | 0.00 USD | 512,580,000.00 USD | 1,360,000.00 USD | 542,800.00 USD | 408,620.00 USD |
| `1D` | `2034.70` | 510,260,000.00 USD | 0.00 USD | 510,260,000.00 USD | 1,030,000.00 USD | 787,650.00 USD | 0.00 USD |
| `7D` | `2035.20` | 939,220,000.00 USD | 0.00 USD | 939,220,000.00 USD | 146,420.00 USD | 186,130.00 USD | 1,350,000.00 USD |
| `1D` | `2037.30` | 508,440,000.00 USD | 0.00 USD | 508,440,000.00 USD | 202,200.00 USD | 300,240.00 USD | 348,110.00 USD |
| `7D` | `2038.50` | 937,540,000.00 USD | 0.00 USD | 937,540,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2039.90` | 507,590,000.00 USD | 0.00 USD | 507,590,000.00 USD | 138,370.00 USD | 178,560.00 USD | 21,940.00 USD |
| `1D` | `2042.50` | 507,250,000.00 USD | 0.00 USD | 507,250,000.00 USD | 0.00 USD | 0.00 USD | 12,020.00 USD |
| `1D` | `2045.10` | 507,240,000.00 USD | 0.00 USD | 507,240,000.00 USD | 0.00 USD | 0.00 USD | 35,980.00 USD |
| `7D` | `2045.10` | 936,080,000.00 USD | 0.00 USD | 936,080,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD |
| `1D` | `2047.70` | 507,200,000.00 USD | 0.00 USD | 507,200,000.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD |
| `1D` | `2050.30` | 506,380,000.00 USD | 0.00 USD | 506,380,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD |
| `7D` | `2051.70` | 935,780,000.00 USD | 0.00 USD | 935,780,000.00 USD | 1,320,000.00 USD | 0.00 USD | 1,190,000.00 USD |
| `1D` | `2052.90` | 505,270,000.00 USD | 0.00 USD | 505,270,000.00 USD | 0.00 USD | 0.00 USD | 28,160.00 USD |
| `1D` | `2055.50` | 505,240,000.00 USD | 0.00 USD | 505,240,000.00 USD | 242,080.00 USD | 88,880.00 USD | 0.00 USD |
| `1D` | `2058.10` | 504,910,000.00 USD | 0.00 USD | 504,910,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `7D` | `2058.30` | 933,280,000.00 USD | 0.00 USD | 933,280,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD |
| `7D` | `2061.60` | 932,930,000.00 USD | 0.00 USD | 932,930,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD |
| `1D` | `2063.30` | 504,160,000.00 USD | 0.00 USD | 504,160,000.00 USD | 643,750.00 USD | 173,370.00 USD | 620,660.00 USD |
| `7D` | `2064.90` | 927,680,000.00 USD | 0.00 USD | 927,680,000.00 USD | 1,230,000.00 USD | 313,000.00 USD | 979,910.00 USD |
| `1D` | `2065.90` | 502,720,000.00 USD | 0.00 USD | 502,720,000.00 USD | 808,950.00 USD | 485,130.00 USD | 53,680.00 USD |
| `7D` | `2068.20` | 925,150,000.00 USD | 0.00 USD | 925,150,000.00 USD | 1,740,000.00 USD | 1,860,000.00 USD | 893,570.00 USD |
| `1D` | `2068.50` | 501,370,000.00 USD | 0.00 USD | 501,370,000.00 USD | 57,300.00 USD | 1,330,000.00 USD | 26,970.00 USD |
| `1D` | `2071.10` | 499,960,000.00 USD | 0.00 USD | 499,960,000.00 USD | 1,040,000.00 USD | 534,600.00 USD | 437,490.00 USD |
| `7D` | `2071.50` | 920,650,000.00 USD | 0.00 USD | 920,650,000.00 USD | 2,820,000.00 USD | 2,410,000.00 USD | 1,230,000.00 USD |
| `1D` | `2073.70` | 497,940,000.00 USD | 0.00 USD | 497,940,000.00 USD | 419,970.00 USD | 62,630.00 USD | 926,730.00 USD |
| `7D` | `2074.80` | 914,190,000.00 USD | 0.00 USD | 914,190,000.00 USD | 4,370,000.00 USD | 3,270,000.00 USD | 4,050,000.00 USD |
| `1D` | `2076.30` | 496,530,000.00 USD | 0.00 USD | 496,530,000.00 USD | 2,580,000.00 USD | 926,330.00 USD | 1,620,000.00 USD |
| `7D` | `2078.10` | 902,490,000.00 USD | 0.00 USD | 902,490,000.00 USD | 5,560,000.00 USD | 4,320,000.00 USD | 2,410,000.00 USD |
| `1D` | `2078.90` | 491,410,000.00 USD | 0.00 USD | 491,410,000.00 USD | 1,320,000.00 USD | 1,100,000.00 USD | 816,960.00 USD |
| `7D` | `2081.40` | 890,210,000.00 USD | 0.00 USD | 890,210,000.00 USD | 4,720,000.00 USD | 3,420,000.00 USD | 2,500,000.00 USD |
| `1D` | `2081.50` | 488,160,000.00 USD | 0.00 USD | 488,160,000.00 USD | 1,430,000.00 USD | 1,260,000.00 USD | 227,550.00 USD |
| `1D` | `2084.10` | 485,250,000.00 USD | 0.00 USD | 485,250,000.00 USD | 2,090,000.00 USD | 1,290,000.00 USD | 753,020.00 USD |
| `7D` | `2084.70` | 879,570,000.00 USD | 0.00 USD | 879,570,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 4,900,000.00 USD |
| `1D` | `2086.70` | 481,120,000.00 USD | 0.00 USD | 481,120,000.00 USD | 1,600,000.00 USD | 1,650,000.00 USD | 1,600,000.00 USD |
| `7D` | `2088.00` | 870,770,000.00 USD | 0.00 USD | 870,770,000.00 USD | 3,990,000.00 USD | 2,780,000.00 USD | 1,650,000.00 USD |
| `1D` | `2089.30` | 476,270,000.00 USD | 0.00 USD | 476,270,000.00 USD | 1,080,000.00 USD | 220,540.00 USD | 90,660.00 USD |
| `7D` | `2091.30` | 862,350,000.00 USD | 0.00 USD | 862,350,000.00 USD | 4,410,000.00 USD | 952,210.00 USD | 7,590,000.00 USD |
| `1D` | `2091.90` | 474,880,000.00 USD | 0.00 USD | 474,880,000.00 USD | 1,130,000.00 USD | 514,440.00 USD | 957,110.00 USD |
| `1D` | `2094.50` | 472,270,000.00 USD | 0.00 USD | 472,270,000.00 USD | 2,040,000.00 USD | 1,120,000.00 USD | 1,310,000.00 USD |
| `7D` | `2094.60` | 849,390,000.00 USD | 0.00 USD | 849,390,000.00 USD | 5,720,000.00 USD | 2,160,000.00 USD | 2,340,000.00 USD |
| `1D` | `2097.10` | 467,800,000.00 USD | 0.00 USD | 467,800,000.00 USD | 617,040.00 USD | 712,710.00 USD | 1,110,000.00 USD |
| `7D` | `2097.90` | 839,170,000.00 USD | 0.00 USD | 839,170,000.00 USD | 2,340,000.00 USD | 3,210,000.00 USD | 1,290,000.00 USD |
| `1D` | `2099.70` | 465,360,000.00 USD | 0.00 USD | 465,360,000.00 USD | 172,210.00 USD | 700,850.00 USD | 11,930.00 USD |
| `7D` | `2101.20` | 832,330,000.00 USD | 0.00 USD | 832,330,000.00 USD | 999,530.00 USD | 1,580,000.00 USD | 4,020,000.00 USD |
| `1D` | `2102.30` | 464,480,000.00 USD | 0.00 USD | 464,480,000.00 USD | 507,510.00 USD | 289,160.00 USD | 466,670.00 USD |
| `7D` | `2104.50` | 825,730,000.00 USD | 0.00 USD | 825,730,000.00 USD | 2,010,000.00 USD | 1,180,000.00 USD | 2,250,000.00 USD |
| `1D` | `2104.90` | 463,210,000.00 USD | 0.00 USD | 463,210,000.00 USD | 612,280.00 USD | 671,930.00 USD | 30,860.00 USD |
| `1D` | `2107.50` | 461,900,000.00 USD | 0.00 USD | 461,900,000.00 USD | 546,100.00 USD | 0.00 USD | 488,260.00 USD |
| `7D` | `2107.80` | 820,290,000.00 USD | 0.00 USD | 820,290,000.00 USD | 2,380,000.00 USD | 452,470.00 USD | 1,650,000.00 USD |
| `1D` | `2110.10` | 460,860,000.00 USD | 0.00 USD | 460,860,000.00 USD | 118,210.00 USD | 31,550.00 USD | 196,840.00 USD |
| `7D` | `2111.10` | 815,810,000.00 USD | 0.00 USD | 815,810,000.00 USD | 3,530,000.00 USD | 2,350,000.00 USD | 2,170,000.00 USD |
| `1D` | `2112.70` | 460,520,000.00 USD | 0.00 USD | 460,520,000.00 USD | 911,810.00 USD | 643,210.00 USD | 224,810.00 USD |
| `7D` | `2114.40` | 807,760,000.00 USD | 0.00 USD | 807,760,000.00 USD | 1,080,000.00 USD | 1,850,000.00 USD | 3,800,000.00 USD |
| `1D` | `2115.30` | 458,740,000.00 USD | 0.00 USD | 458,740,000.00 USD | 0.00 USD | 13,230.00 USD | 426,410.00 USD |
| `7D` | `2117.70` | 801,030,000.00 USD | 0.00 USD | 801,030,000.00 USD | 3,430,000.00 USD | 2,020,000.00 USD | 3,380,000.00 USD |
| `1D` | `2117.90` | 458,300,000.00 USD | 0.00 USD | 458,300,000.00 USD | 202,840.00 USD | 2,100.00 USD | 472,930.00 USD |
| `1D` | `2120.50` | 457,620,000.00 USD | 0.00 USD | 457,620,000.00 USD | 744,340.00 USD | 230,360.00 USD | 997,350.00 USD |
| `7D` | `2121.00` | 792,200,000.00 USD | 0.00 USD | 792,200,000.00 USD | 3,650,000.00 USD | 1,340,000.00 USD | 1,820,000.00 USD |
| `1D` | `2123.10` | 455,650,000.00 USD | 0.00 USD | 455,650,000.00 USD | 766,550.00 USD | 1,210,000.00 USD | 976,300.00 USD |
| `7D` | `2124.30` | 785,390,000.00 USD | 0.00 USD | 785,390,000.00 USD | 832,850.00 USD | 972,650.00 USD | 1,510,000.00 USD |
| `1D` | `2125.70` | 452,700,000.00 USD | 0.00 USD | 452,700,000.00 USD | 173,130.00 USD | 636,520.00 USD | 320,060.00 USD |
| `7D` | `2127.60` | 782,070,000.00 USD | 0.00 USD | 782,070,000.00 USD | 2,400,000.00 USD | 2,630,000.00 USD | 3,270,000.00 USD |
| `1D` | `2128.30` | 451,570,000.00 USD | 0.00 USD | 451,570,000.00 USD | 107,010.00 USD | 475,750.00 USD | 0.00 USD |
| `1D` | `2130.90` | 450,990,000.00 USD | 0.00 USD | 450,990,000.00 USD | 0.00 USD | 18,610.00 USD | 331,620.00 USD |
| `7D` | `2130.90` | 773,770,000.00 USD | 0.00 USD | 773,770,000.00 USD | 2,410,000.00 USD | 2,300,000.00 USD | 1,700,000.00 USD |
| `7D` | `2134.20` | 767,360,000.00 USD | 0.00 USD | 767,360,000.00 USD | 2,170,000.00 USD | 550,450.00 USD | 308,060.00 USD |
| `1D` | `2136.10` | 450,640,000.00 USD | 0.00 USD | 450,640,000.00 USD | 0.00 USD | 278,410.00 USD | 0.00 USD |
| `7D` | `2137.50` | 764,330,000.00 USD | 0.00 USD | 764,330,000.00 USD | 1,040,000.00 USD | 880,790.00 USD | 43,560.00 USD |
| `7D` | `2140.80` | 762,360,000.00 USD | 0.00 USD | 762,360,000.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD |
| `7D` | `2144.10` | 758,430,000.00 USD | 0.00 USD | 758,430,000.00 USD | 449,020.00 USD | 1,130,000.00 USD | 268,500.00 USD |
| `7D` | `2147.40` | 756,580,000.00 USD | 0.00 USD | 756,580,000.00 USD | 657,710.00 USD | 421,320.00 USD | 0.00 USD |
| `7D` | `2150.70` | 755,500,000.00 USD | 0.00 USD | 755,500,000.00 USD | 459,630.00 USD | 463,640.00 USD | 31,040.00 USD |
| `1D` | `2151.70` | 450,360,000.00 USD | 0.00 USD | 450,360,000.00 USD | 208,250.00 USD | 440,530.00 USD | 0.00 USD |
| `7D` | `2154.00` | 754,550,000.00 USD | 0.00 USD | 754,550,000.00 USD | 128,430.00 USD | 311,060.00 USD | 32,590.00 USD |
| `1D` | `2154.30` | 449,710,000.00 USD | 0.00 USD | 449,710,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD |
| `7D` | `2157.30` | 754,080,000.00 USD | 0.00 USD | 754,080,000.00 USD | 388,210.00 USD | 1,030,000.00 USD | 1,080,000.00 USD |
| `1D` | `2159.50` | 448,310,000.00 USD | 0.00 USD | 448,310,000.00 USD | 0.00 USD | 0.00 USD | 37,580.00 USD |
| `7D` | `2160.60` | 751,580,000.00 USD | 0.00 USD | 751,580,000.00 USD | 613,630.00 USD | 1,900,000.00 USD | 1,990,000.00 USD |
| `1D` | `2162.10` | 448,270,000.00 USD | 0.00 USD | 448,270,000.00 USD | 0.00 USD | 3,220,000.00 USD | 100,530.00 USD |
| `7D` | `2163.90` | 747,070,000.00 USD | 0.00 USD | 747,070,000.00 USD | 566,120.00 USD | 2,950,000.00 USD | 540,130.00 USD |
| `1D` | `2164.70` | 444,950,000.00 USD | 0.00 USD | 444,950,000.00 USD | 217,960.00 USD | 408,000.00 USD | 107,900.00 USD |
| `7D` | `2167.20` | 743,010,000.00 USD | 0.00 USD | 743,010,000.00 USD | 25,540.00 USD | 3,620,000.00 USD | 50,240.00 USD |
| `1D` | `2167.30` | 444,220,000.00 USD | 0.00 USD | 444,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 1,020,000.00 USD |
| `1D` | `2169.90` | 439,980,000.00 USD | 0.00 USD | 439,980,000.00 USD | 5,210,000.00 USD | 5,170,000.00 USD | 2,740,000.00 USD |
| `7D` | `2170.50` | 739,310,000.00 USD | 0.00 USD | 739,310,000.00 USD | 3,500,000.00 USD | 3,730,000.00 USD | 5,210,000.00 USD |
| `1D` | `2172.50` | 426,850,000.00 USD | 0.00 USD | 426,850,000.00 USD | 0.00 USD | 1,230,000.00 USD | 497,070.00 USD |
| `7D` | `2173.80` | 726,860,000.00 USD | 0.00 USD | 726,860,000.00 USD | 4,370,000.00 USD | 363,040.00 USD | 1,010,000.00 USD |
| `1D` | `2175.10` | 425,120,000.00 USD | 0.00 USD | 425,120,000.00 USD | 1,150,000.00 USD | 111,190.00 USD | 870,280.00 USD |
| `7D` | `2177.10` | 721,130,000.00 USD | 0.00 USD | 721,130,000.00 USD | 1,750,000.00 USD | 1,330,000.00 USD | 2,820,000.00 USD |
| `1D` | `2177.70` | 423,000,000.00 USD | 0.00 USD | 423,000,000.00 USD | 445,430.00 USD | 1,770,000.00 USD | 99,000.00 USD |
| `1D` | `2180.30` | 420,680,000.00 USD | 0.00 USD | 420,680,000.00 USD | 2,080,000.00 USD | 0.00 USD | 1,420,000.00 USD |
| `7D` | `2180.40` | 715,230,000.00 USD | 0.00 USD | 715,230,000.00 USD | 0.00 USD | 373,740.00 USD | 431,800.00 USD |
| `1D` | `2182.90` | 417,180,000.00 USD | 0.00 USD | 417,180,000.00 USD | 2,960,000.00 USD | 1,140,000.00 USD | 425,980.00 USD |
| `7D` | `2183.70` | 714,420,000.00 USD | 0.00 USD | 714,420,000.00 USD | 1,760,000.00 USD | 1,310,000.00 USD | 3,950,000.00 USD |
| `1D` | `2185.50` | 412,660,000.00 USD | 0.00 USD | 412,660,000.00 USD | 566,020.00 USD | 1,110,000.00 USD | 2,690,000.00 USD |
| `7D` | `2187.00` | 707,410,000.00 USD | 0.00 USD | 707,410,000.00 USD | 556,600.00 USD | 0.00 USD | 54,020.00 USD |
| `1D` | `2188.10` | 408,300,000.00 USD | 0.00 USD | 408,300,000.00 USD | 0.00 USD | 890,000.00 USD | 0.00 USD |
| `7D` | `2190.30` | 706,800,000.00 USD | 0.00 USD | 706,800,000.00 USD | 2,730,000.00 USD | 0.00 USD | 4,200,000.00 USD |
| `1D` | `2190.70` | 407,410,000.00 USD | 0.00 USD | 407,410,000.00 USD | 0.00 USD | 222,200.00 USD | 764,360.00 USD |
| `1D` | `2193.30` | 406,420,000.00 USD | 0.00 USD | 406,420,000.00 USD | 605,210.00 USD | 0.00 USD | 39,000.00 USD |
| `1D` | `2195.90` | 405,780,000.00 USD | 0.00 USD | 405,780,000.00 USD | 416,500.00 USD | 881,070.00 USD | 1,890,000.00 USD |
| `7D` | `2196.90` | 699,870,000.00 USD | 0.00 USD | 699,870,000.00 USD | 2,580,000.00 USD | 474,090.00 USD | 2,040,000.00 USD |
| `1D` | `2198.50` | 402,590,000.00 USD | 0.00 USD | 402,590,000.00 USD | 0.00 USD | 149,110.00 USD | 50,830.00 USD |
| `7D` | `2200.20` | 694,780,000.00 USD | 0.00 USD | 694,780,000.00 USD | 3,000,000.00 USD | 5,080,000.00 USD | 3,200,000.00 USD |
| `1D` | `2201.10` | 402,390,000.00 USD | 0.00 USD | 402,390,000.00 USD | 1,690,000.00 USD | 4,250,000.00 USD | 1,500,000.00 USD |
| `7D` | `2203.50` | 683,500,000.00 USD | 0.00 USD | 683,500,000.00 USD | 3,650,000.00 USD | 1,710,000.00 USD | 3,750,000.00 USD |
| `1D` | `2203.70` | 394,950,000.00 USD | 0.00 USD | 394,950,000.00 USD | 2,130,000.00 USD | 107,200.00 USD | 830,450.00 USD |
| `1D` | `2206.30` | 391,880,000.00 USD | 0.00 USD | 391,880,000.00 USD | 755,060.00 USD | 10,890,000.00 USD | 887,820.00 USD |
| `7D` | `2206.80` | 674,390,000.00 USD | 0.00 USD | 674,390,000.00 USD | 6,920,000.00 USD | 9,430,000.00 USD | 4,020,000.00 USD |
| `1D` | `2208.90` | 379,350,000.00 USD | 0.00 USD | 379,350,000.00 USD | 2,680,000.00 USD | 2,280,000.00 USD | 3,110,000.00 USD |
| `7D` | `2210.10` | 654,020,000.00 USD | 0.00 USD | 654,020,000.00 USD | 12,800,000.00 USD | 20,410,000.00 USD | 6,470,000.00 USD |
| `1D` | `2211.50` | 371,280,000.00 USD | 0.00 USD | 371,280,000.00 USD | 6,150,000.00 USD | 2,320,000.00 USD | 3,880,000.00 USD |
| `7D` | `2213.40` | 614,340,000.00 USD | 0.00 USD | 614,340,000.00 USD | 10,920,000.00 USD | 14,590,000.00 USD | 19,950,000.00 USD |
| `1D` | `2214.10` | 358,930,000.00 USD | 0.00 USD | 358,930,000.00 USD | 14,080,000.00 USD | 10,880,000.00 USD | 6,490,000.00 USD |
| `1D` | `2216.70` | 327,480,000.00 USD | 0.00 USD | 327,480,000.00 USD | 11,870,000.00 USD | 8,780,000.00 USD | 8,010,000.00 USD |
| `7D` | `2216.70` | 568,880,000.00 USD | 0.00 USD | 568,880,000.00 USD | 25,710,000.00 USD | 17,030,000.00 USD | 9,390,000.00 USD |
| `1D` | `2219.30` | 298,830,000.00 USD | 0.00 USD | 298,830,000.00 USD | 6,980,000.00 USD | 8,590,000.00 USD | 2,840,000.00 USD |
| `7D` | `2220.00` | 516,750,000.00 USD | 0.00 USD | 516,750,000.00 USD | 27,820,000.00 USD | 14,950,000.00 USD | 15,760,000.00 USD |
| `1D` | `2221.90` | 280,410,000.00 USD | 0.00 USD | 280,410,000.00 USD | 6,400,000.00 USD | 12,880,000.00 USD | 2,080,000.00 USD |
| `7D` | `2223.30` | 458,220,000.00 USD | 0.00 USD | 458,220,000.00 USD | 10,150,000.00 USD | 8,220,000.00 USD | 11,910,000.00 USD |
| `1D` | `2224.50` | 259,050,000.00 USD | 0.00 USD | 259,050,000.00 USD | 10,020,000.00 USD | 4,140,000.00 USD | 4,940,000.00 USD |
| `7D` | `2226.60` | 427,940,000.00 USD | 0.00 USD | 427,940,000.00 USD | 16,350,000.00 USD | 11,030,000.00 USD | 10,460,000.00 USD |
| `1D` | `2227.10` | 239,950,000.00 USD | 0.00 USD | 239,950,000.00 USD | 5,090,000.00 USD | 13,450,000.00 USD | 6,140,000.00 USD |
| `1D` | `2229.70` | 215,260,000.00 USD | 0.00 USD | 215,260,000.00 USD | 10,130,000.00 USD | 7,410,000.00 USD | 4,090,000.00 USD |
| `7D` | `2229.90` | 390,090,000.00 USD | 0.00 USD | 390,090,000.00 USD | 12,730,000.00 USD | 11,790,000.00 USD | 28,550,000.00 USD |
| `1D` | `2232.30` | 193,630,000.00 USD | 0.00 USD | 193,630,000.00 USD | 4,620,000.00 USD | 4,830,000.00 USD | 6,950,000.00 USD |
| `7D` | `2233.20` | 337,020,000.00 USD | 0.00 USD | 337,020,000.00 USD | 16,600,000.00 USD | 24,290,000.00 USD | 10,420,000.00 USD |
| `1D` | `2234.90` | 177,230,000.00 USD | 0.00 USD | 177,230,000.00 USD | 19,080,000.00 USD | 1,450,000.00 USD | 11,000,000.00 USD |
| `7D` | `2236.50` | 285,700,000.00 USD | 0.00 USD | 285,700,000.00 USD | 16,050,000.00 USD | 7,430,000.00 USD | 27,770,000.00 USD |
| `1D` | `2237.50` | 145,690,000.00 USD | 0.00 USD | 145,690,000.00 USD | 22,650,000.00 USD | 5,930,000.00 USD | 13,220,000.00 USD |
| `7D` | `2239.80` | 234,460,000.00 USD | 0.00 USD | 234,460,000.00 USD | 16,720,000.00 USD | 6,600,000.00 USD | 13,750,000.00 USD |
| `1D` | `2240.10` | 103,890,000.00 USD | 0.00 USD | 103,890,000.00 USD | 2,060,000.00 USD | 2,600,000.00 USD | 1,990,000.00 USD |
| `1D` | `2242.70` | 97,250,000.00 USD | 0.00 USD | 97,250,000.00 USD | 5,750,000.00 USD | 3,760,000.00 USD | 9,040,000.00 USD |
| `7D` | `2243.10` | 197,390,000.00 USD | 0.00 USD | 197,390,000.00 USD | 29,940,000.00 USD | 5,310,000.00 USD | 24,330,000.00 USD |
| `1D` | `2245.30` | 78,700,000.00 USD | 0.00 USD | 78,700,000.00 USD | 3,700,000.00 USD | 6,190,000.00 USD | 381,400.00 USD |
| `7D` | `2246.40` | 137,820,000.00 USD | 0.00 USD | 137,820,000.00 USD | 14,340,000.00 USD | 0.00 USD | 13,920,000.00 USD |
| `1D` | `2247.90` | 68,440,000.00 USD | 0.00 USD | 68,440,000.00 USD | 12,490,000.00 USD | 0.00 USD | 7,240,000.00 USD |
| `7D` | `2249.70` | 109,560,000.00 USD | 0.00 USD | 109,560,000.00 USD | 25,030,000.00 USD | 0.00 USD | 19,440,000.00 USD |
| `1D` | `2250.50` | 48,710,000.00 USD | 0.00 USD | 48,710,000.00 USD | 4,450,000.00 USD | 4,540,000.00 USD | 5,610,000.00 USD |
| `7D` | `2253.00` | 65,090,000.00 USD | 0.00 USD | 65,090,000.00 USD | 26,890,000.00 USD | 0.00 USD | 12,040,000.00 USD |
| `1D` | `2253.10` | 34,100,000.00 USD | 0.00 USD | 34,100,000.00 USD | 13,840,000.00 USD | 4,440,000.00 USD | 8,130,000.00 USD |
| `1D` | `2255.70` | 7,700,000.00 USD | 0.00 USD | 7,700,000.00 USD | 0.00 USD | 3,390,000.00 USD | 0.00 USD |
| `7D` | `2256.30` | 26,160,000.00 USD | 0.00 USD | 26,160,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2258.30` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 0.00 USD | 170,210.00 USD | 0.00 USD |
| `7D` | `2259.60` | 10,940,000.00 USD | 0.00 USD | 10,940,000.00 USD | 10,940,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2260.90` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 2,420,000.00 USD | 0.00 USD | 156,010.00 USD |
| `1D` | `2266.10` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 1,560,000.00 USD |
| `1D` | `2267.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2267.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2268.70` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,780,000.00 USD |
| `1D` | `2273.90` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 288,080.00 USD | 114,460.00 USD |
| `1D` | `2276.50` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 267,040.00 USD | 0.00 USD |
| `1D` | `2279.10` | 23,520,000.00 USD | 23,520,000.00 USD | 0.00 USD | 11,600,000.00 USD | 3,950,000.00 USD | 4,520,000.00 USD |
| `7D` | `2279.40` | 17,000,000.00 USD | 17,000,000.00 USD | 0.00 USD | 0.00 USD | 17,000,000.00 USD | 0.00 USD |
| `1D` | `2281.70` | 84,770,000.00 USD | 84,770,000.00 USD | 0.00 USD | 33,480,000.00 USD | 25,270,000.00 USD | 2,500,000.00 USD |
| `7D` | `2282.70` | 117,630,000.00 USD | 117,630,000.00 USD | 0.00 USD | 0.00 USD | 87,090,000.00 USD | 13,550,000.00 USD |
| `1D` | `2284.30` | 152,740,000.00 USD | 152,740,000.00 USD | 0.00 USD | 32,760,000.00 USD | 20,940,000.00 USD | 14,270,000.00 USD |
| `7D` | `2286.00` | 128,050,000.00 USD | 128,050,000.00 USD | 0.00 USD | 1,010,000.00 USD | 9,400,000.00 USD | 0.00 USD |
| `1D` | `2286.90` | 164,340,000.00 USD | 164,340,000.00 USD | 0.00 USD | 3,210,000.00 USD | 4,900,000.00 USD | 3,480,000.00 USD |
| `7D` | `2289.30` | 151,650,000.00 USD | 151,650,000.00 USD | 0.00 USD | 7,010,000.00 USD | 5,310,000.00 USD | 11,280,000.00 USD |
| `1D` | `2289.50` | 173,390,000.00 USD | 173,390,000.00 USD | 0.00 USD | 0.00 USD | 8,840,000.00 USD | 219,440.00 USD |
| `1D` | `2292.10` | 181,560,000.00 USD | 181,560,000.00 USD | 0.00 USD | 6,500,000.00 USD | 1,490,000.00 USD | 176,580.00 USD |
| `7D` | `2292.60` | 152,670,000.00 USD | 152,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,020,000.00 USD |
| `1D` | `2294.70` | 197,490,000.00 USD | 197,490,000.00 USD | 0.00 USD | 3,590,000.00 USD | 6,490,000.00 USD | 5,860,000.00 USD |
| `7D` | `2295.90` | 179,980,000.00 USD | 179,980,000.00 USD | 0.00 USD | 13,610,000.00 USD | 2,380,000.00 USD | 11,320,000.00 USD |
| `1D` | `2297.30` | 221,250,000.00 USD | 221,250,000.00 USD | 0.00 USD | 11,830,000.00 USD | 6,530,000.00 USD | 5,390,000.00 USD |
| `7D` | `2299.20` | 208,390,000.00 USD | 208,390,000.00 USD | 0.00 USD | 11,730,000.00 USD | 11,130,000.00 USD | 5,560,000.00 USD |
| `1D` | `2299.90` | 236,840,000.00 USD | 236,840,000.00 USD | 0.00 USD | 2,260,000.00 USD | 5,930,000.00 USD | 7,390,000.00 USD |
| `1D` | `2302.50` | 257,830,000.00 USD | 257,830,000.00 USD | 0.00 USD | 15,230,000.00 USD | 852,700.00 USD | 4,910,000.00 USD |
| `7D` | `2302.50` | 255,510,000.00 USD | 255,510,000.00 USD | 0.00 USD | 23,020,000.00 USD | 7,250,000.00 USD | 16,850,000.00 USD |
| `1D` | `2305.10` | 286,870,000.00 USD | 286,870,000.00 USD | 0.00 USD | 10,430,000.00 USD | 14,090,000.00 USD | 4,540,000.00 USD |
| `7D` | `2305.80` | 276,280,000.00 USD | 276,280,000.00 USD | 0.00 USD | 2,980,000.00 USD | 8,820,000.00 USD | 8,970,000.00 USD |
| `1D` | `2307.70` | 295,180,000.00 USD | 295,180,000.00 USD | 0.00 USD | 2,420,000.00 USD | 3,500,000.00 USD | 2,390,000.00 USD |
| `7D` | `2309.10` | 280,560,000.00 USD | 280,560,000.00 USD | 0.00 USD | 1,240,000.00 USD | 930,630.00 USD | 2,110,000.00 USD |
| `1D` | `2310.30` | 309,220,000.00 USD | 309,220,000.00 USD | 0.00 USD | 2,300,000.00 USD | 2,450,000.00 USD | 9,290,000.00 USD |
| `7D` | `2312.40` | 307,860,000.00 USD | 307,860,000.00 USD | 0.00 USD | 10,780,000.00 USD | 2,650,000.00 USD | 13,870,000.00 USD |
| `1D` | `2312.90` | 317,160,000.00 USD | 317,160,000.00 USD | 0.00 USD | 890,860.00 USD | 6,730,000.00 USD | 313,050.00 USD |
| `1D` | `2315.50` | 343,460,000.00 USD | 343,460,000.00 USD | 0.00 USD | 9,790,000.00 USD | 9,890,000.00 USD | 6,630,000.00 USD |
| `7D` | `2315.70` | 315,940,000.00 USD | 315,940,000.00 USD | 0.00 USD | 0.00 USD | 7,460,000.00 USD | 627,210.00 USD |
| `1D` | `2318.10` | 360,870,000.00 USD | 360,870,000.00 USD | 0.00 USD | 4,440,000.00 USD | 10,740,000.00 USD | 2,230,000.00 USD |
| `7D` | `2319.00` | 333,450,000.00 USD | 333,450,000.00 USD | 0.00 USD | 4,540,000.00 USD | 4,550,000.00 USD | 8,420,000.00 USD |
| `1D` | `2320.70` | 378,520,000.00 USD | 378,520,000.00 USD | 0.00 USD | 5,790,000.00 USD | 9,890,000.00 USD | 1,960,000.00 USD |
| `7D` | `2322.30` | 350,600,000.00 USD | 350,600,000.00 USD | 0.00 USD | 1,110,000.00 USD | 15,930,000.00 USD | 108,040.00 USD |
| `1D` | `2323.30` | 394,220,000.00 USD | 394,220,000.00 USD | 0.00 USD | 1,710,000.00 USD | 10,410,000.00 USD | 3,590,000.00 USD |
| `7D` | `2325.60` | 371,260,000.00 USD | 371,260,000.00 USD | 0.00 USD | 9,720,000.00 USD | 2,540,000.00 USD | 8,390,000.00 USD |
| `1D` | `2325.90` | 405,990,000.00 USD | 405,990,000.00 USD | 0.00 USD | 479,120.00 USD | 5,640,000.00 USD | 5,660,000.00 USD |
| `1D` | `2328.50` | 408,980,000.00 USD | 408,980,000.00 USD | 0.00 USD | 2,140,000.00 USD | 444,400.00 USD | 402,280.00 USD |
| `7D` | `2328.90` | 383,080,000.00 USD | 383,080,000.00 USD | 0.00 USD | 3,860,000.00 USD | 0.00 USD | 7,960,000.00 USD |
| `1D` | `2331.10` | 427,150,000.00 USD | 427,150,000.00 USD | 0.00 USD | 17,350,000.00 USD | 692,470.00 USD | 126,990.00 USD |
| `7D` | `2332.20` | 412,310,000.00 USD | 412,310,000.00 USD | 0.00 USD | 29,230,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2333.70` | 443,360,000.00 USD | 443,360,000.00 USD | 0.00 USD | 6,250,000.00 USD | 2,820,000.00 USD | 7,150,000.00 USD |
| `7D` | `2335.50` | 470,320,000.00 USD | 470,320,000.00 USD | 0.00 USD | 28,990,000.00 USD | 18,420,000.00 USD | 10,600,000.00 USD |
| `1D` | `2336.30` | 463,500,000.00 USD | 463,500,000.00 USD | 0.00 USD | 17,400,000.00 USD | 547,950.00 USD | 2,190,000.00 USD |
| `7D` | `2338.80` | 488,200,000.00 USD | 488,200,000.00 USD | 0.00 USD | 9,570,000.00 USD | 0.00 USD | 8,310,000.00 USD |
| `1D` | `2338.90` | 476,510,000.00 USD | 476,510,000.00 USD | 0.00 USD | 6,360,000.00 USD | 2,600,000.00 USD | 4,050,000.00 USD |
| `1D` | `2341.50` | 495,170,000.00 USD | 495,170,000.00 USD | 0.00 USD | 5,340,000.00 USD | 3,430,000.00 USD | 9,900,000.00 USD |
| `7D` | `2342.10` | 528,300,000.00 USD | 528,300,000.00 USD | 0.00 USD | 4,720,000.00 USD | 21,390,000.00 USD | 14,000,000.00 USD |
| `1D` | `2344.10` | 508,500,000.00 USD | 508,500,000.00 USD | 0.00 USD | 1,370,000.00 USD | 6,240,000.00 USD | 5,710,000.00 USD |
| `7D` | `2345.40` | 549,670,000.00 USD | 549,670,000.00 USD | 0.00 USD | 1,350,000.00 USD | 13,990,000.00 USD | 6,020,000.00 USD |
| `1D` | `2346.70` | 519,400,000.00 USD | 519,400,000.00 USD | 0.00 USD | 3,930,000.00 USD | 341,240.00 USD | 6,620,000.00 USD |
| `7D` | `2348.70` | 587,550,000.00 USD | 587,550,000.00 USD | 0.00 USD | 847,620.00 USD | 9,500,000.00 USD | 27,530,000.00 USD |
| `1D` | `2349.30` | 550,410,000.00 USD | 550,410,000.00 USD | 0.00 USD | 19,450,000.00 USD | 6,150,000.00 USD | 5,420,000.00 USD |
| `1D` | `2351.90` | 579,570,000.00 USD | 579,570,000.00 USD | 0.00 USD | 17,620,000.00 USD | 4,590,000.00 USD | 6,940,000.00 USD |
| `7D` | `2352.00` | 624,170,000.00 USD | 624,170,000.00 USD | 0.00 USD | 2,930,000.00 USD | 23,060,000.00 USD | 10,630,000.00 USD |
| `1D` | `2354.50` | 602,430,000.00 USD | 602,430,000.00 USD | 0.00 USD | 1,710,000.00 USD | 18,970,000.00 USD | 2,190,000.00 USD |
| `7D` | `2355.30` | 683,600,000.00 USD | 683,600,000.00 USD | 0.00 USD | 18,530,000.00 USD | 38,020,000.00 USD | 2,880,000.00 USD |
| `1D` | `2357.10` | 612,610,000.00 USD | 612,610,000.00 USD | 0.00 USD | 3,570,000.00 USD | 3,100,000.00 USD | 3,500,000.00 USD |
| `7D` | `2358.60` | 695,730,000.00 USD | 695,730,000.00 USD | 0.00 USD | 7,110,000.00 USD | 512,220.00 USD | 4,510,000.00 USD |
| `1D` | `2359.70` | 631,440,000.00 USD | 631,440,000.00 USD | 0.00 USD | 7,040,000.00 USD | 6,750,000.00 USD | 5,050,000.00 USD |
| `7D` | `2361.90` | 703,110,000.00 USD | 703,110,000.00 USD | 0.00 USD | 3,150,000.00 USD | 3,800,000.00 USD | 431,800.00 USD |
| `1D` | `2362.30` | 649,600,000.00 USD | 649,600,000.00 USD | 0.00 USD | 8,900,000.00 USD | 6,710,000.00 USD | 2,540,000.00 USD |
| `1D` | `2364.90` | 669,200,000.00 USD | 669,200,000.00 USD | 0.00 USD | 6,420,000.00 USD | 4,850,000.00 USD | 8,330,000.00 USD |
| `7D` | `2365.20` | 724,170,000.00 USD | 724,170,000.00 USD | 0.00 USD | 10,200,000.00 USD | 0.00 USD | 10,860,000.00 USD |
| `1D` | `2367.50` | 677,980,000.00 USD | 677,980,000.00 USD | 0.00 USD | 4,770,000.00 USD | 1,110,000.00 USD | 2,910,000.00 USD |
| `7D` | `2368.50` | 737,240,000.00 USD | 737,240,000.00 USD | 0.00 USD | 10,830,000.00 USD | 1,780,000.00 USD | 458,400.00 USD |
| `1D` | `2370.10` | 711,700,000.00 USD | 711,700,000.00 USD | 0.00 USD | 14,350,000.00 USD | 12,300,000.00 USD | 7,060,000.00 USD |
| `7D` | `2371.80` | 818,170,000.00 USD | 818,170,000.00 USD | 0.00 USD | 26,000,000.00 USD | 0.00 USD | 54,940,000.00 USD |
| `1D` | `2372.70` | 740,160,000.00 USD | 740,160,000.00 USD | 0.00 USD | 14,450,000.00 USD | 5,550,000.00 USD | 8,460,000.00 USD |
| `7D` | `2375.10` | 845,120,000.00 USD | 845,120,000.00 USD | 0.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD |
| `1D` | `2375.30` | 758,950,000.00 USD | 758,950,000.00 USD | 0.00 USD | 11,490,000.00 USD | 3,650,000.00 USD | 3,660,000.00 USD |
| `1D` | `2377.90` | 779,510,000.00 USD | 779,510,000.00 USD | 0.00 USD | 5,060,000.00 USD | 6,270,000.00 USD | 9,230,000.00 USD |
| `7D` | `2378.40` | 890,530,000.00 USD | 890,530,000.00 USD | 0.00 USD | 11,800,000.00 USD | 7,950,000.00 USD | 25,670,000.00 USD |
| `1D` | `2380.50` | 818,190,000.00 USD | 818,190,000.00 USD | 0.00 USD | 11,350,000.00 USD | 10,470,000.00 USD | 16,850,000.00 USD |
| `7D` | `2381.70` | 930,320,000.00 USD | 930,320,000.00 USD | 0.00 USD | 8,510,000.00 USD | 6,750,000.00 USD | 24,530,000.00 USD |
| `1D` | `2383.10` | 866,090,000.00 USD | 866,090,000.00 USD | 0.00 USD | 20,500,000.00 USD | 14,070,000.00 USD | 13,340,000.00 USD |
| `7D` | `2385.00` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 0.00 USD | 18,550,000.00 USD | 36,910,000.00 USD | 46,260,000.00 USD |
| `1D` | `2385.70` | 894,380,000.00 USD | 894,380,000.00 USD | 0.00 USD | 9,780,000.00 USD | 11,460,000.00 USD | 7,030,000.00 USD |
| `1D` | `2388.30` | 919,560,000.00 USD | 919,560,000.00 USD | 0.00 USD | 13,100,000.00 USD | 6,720,000.00 USD | 5,370,000.00 USD |
| `7D` | `2388.30` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 5,290,000.00 USD | 38,070,000.00 USD | 44,510,000.00 USD |
| `1D` | `2390.90` | 935,170,000.00 USD | 935,170,000.00 USD | 0.00 USD | 3,770,000.00 USD | 6,670,000.00 USD | 5,160,000.00 USD |
| `7D` | `2391.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 8,560,000.00 USD | 52,080,000.00 USD | 40,380,000.00 USD |
| `1D` | `2393.50` | 949,510,000.00 USD | 949,510,000.00 USD | 0.00 USD | 4,350,000.00 USD | 6,000,000.00 USD | 4,000,000.00 USD |
| `7D` | `2394.90` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 57,450,000.00 USD | 32,260,000.00 USD | 37,090,000.00 USD |
| `1D` | `2396.10` | 962,660,000.00 USD | 962,660,000.00 USD | 0.00 USD | 5,380,000.00 USD | 3,200,000.00 USD | 4,560,000.00 USD |
| `7D` | `2398.20` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 0.00 USD | 42,820,000.00 USD | 38,210,000.00 USD | 29,190,000.00 USD |
| `1D` | `2398.70` | 984,780,000.00 USD | 984,780,000.00 USD | 0.00 USD | 7,520,000.00 USD | 6,910,000.00 USD | 7,690,000.00 USD |
| `1D` | `2401.30` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 0.00 USD | 5,960,000.00 USD | 6,570,000.00 USD | 6,540,000.00 USD |
| `7D` | `2401.50` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 51,970,000.00 USD | 26,780,000.00 USD | 29,090,000.00 USD |
| `1D` | `2403.90` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 0.00 USD | 9,280,000.00 USD | 8,450,000.00 USD | 6,870,000.00 USD |
| `7D` | `2404.80` | 1,670,000,000.00 USD | 1,670,000,000.00 USD | 0.00 USD | 50,800,000.00 USD | 32,200,000.00 USD | 24,110,000.00 USD |
| `1D` | `2406.50` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 12,590,000.00 USD | 7,420,000.00 USD | 6,990,000.00 USD |
| `7D` | `2408.10` | 1,760,000,000.00 USD | 1,760,000,000.00 USD | 0.00 USD | 34,390,000.00 USD | 31,420,000.00 USD | 25,030,000.00 USD |
| `1D` | `2409.10` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 0.00 USD | 8,470,000.00 USD | 8,000,000.00 USD | 8,010,000.00 USD |
| `7D` | `2411.40` | 1,840,000,000.00 USD | 1,840,000,000.00 USD | 0.00 USD | 19,200,000.00 USD | 32,580,000.00 USD | 27,660,000.00 USD |
| `1D` | `2411.70` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 7,650,000.00 USD | 7,200,000.00 USD | 2,990,000.00 USD |
| `1D` | `2414.30` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 4,160,000.00 USD | 2,340,000.00 USD | 2,950,000.00 USD |
| `7D` | `2414.70` | 1,910,000,000.00 USD | 1,910,000,000.00 USD | 0.00 USD | 23,820,000.00 USD | 21,740,000.00 USD | 23,130,000.00 USD |
| `1D` | `2416.90` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 3,500,000.00 USD | 2,390,000.00 USD | 3,260,000.00 USD |
| `7D` | `2418.00` | 1,990,000,000.00 USD | 1,990,000,000.00 USD | 0.00 USD | 34,060,000.00 USD | 15,260,000.00 USD | 24,450,000.00 USD |
| `1D` | `2419.50` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 6,320,000.00 USD | 4,000,000.00 USD | 3,660,000.00 USD |
| `7D` | `2421.30` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 0.00 USD | 25,700,000.00 USD | 27,770,000.00 USD | 21,590,000.00 USD |
| `1D` | `2422.10` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 3,230,000.00 USD | 3,700,000.00 USD | 5,020,000.00 USD |
| `7D` | `2424.60` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 0.00 USD | 23,650,000.00 USD | 33,060,000.00 USD | 34,520,000.00 USD |
| `1D` | `2424.70` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 1,400,000.00 USD | 2,670,000.00 USD | 844,590.00 USD |
| `1D` | `2427.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 731,900.00 USD | 124,100.00 USD | 601,200.00 USD |
| `7D` | `2427.90` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 0.00 USD | 25,200,000.00 USD | 15,090,000.00 USD | 18,920,000.00 USD |
| `1D` | `2429.90` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 1,390,000.00 USD | 1,770,000.00 USD | 1,220,000.00 USD |
| `7D` | `2431.20` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 0.00 USD | 10,380,000.00 USD | 17,060,000.00 USD | 9,300,000.00 USD |
| `1D` | `2432.50` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 2,260,000.00 USD | 1,690,000.00 USD | 247,270.00 USD |
| `7D` | `2434.50` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 0.00 USD | 27,390,000.00 USD | 21,570,000.00 USD | 11,160,000.00 USD |
| `1D` | `2435.10` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 1,790,000.00 USD | 482,360.00 USD | 1,540,000.00 USD |
| `1D` | `2437.70` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 777,840.00 USD | 530,330.00 USD | 21,360.00 USD |
| `7D` | `2437.80` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 0.00 USD | 11,900,000.00 USD | 12,720,000.00 USD | 5,470,000.00 USD |
| `1D` | `2440.30` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 1,540,000.00 USD | 1,240,000.00 USD | 479,040.00 USD |
| `7D` | `2441.10` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 0.00 USD | 15,080,000.00 USD | 8,120,000.00 USD | 10,640,000.00 USD |
| `1D` | `2442.90` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 1,050,000.00 USD | 1,430,000.00 USD | 1,010,000.00 USD |
| `7D` | `2444.40` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 0.00 USD | 8,860,000.00 USD | 15,100,000.00 USD | 13,960,000.00 USD |
| `1D` | `2445.50` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 126,820.00 USD | 467,480.00 USD | 1,210,000.00 USD |
| `7D` | `2447.70` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 0.00 USD | 11,380,000.00 USD | 7,520,000.00 USD | 17,330,000.00 USD |
| `1D` | `2448.10` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 864,380.00 USD | 325,700.00 USD | 1,840,000.00 USD |
| `1D` | `2450.70` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 2,020,000.00 USD | 877,190.00 USD | 2,820,000.00 USD |
| `7D` | `2451.00` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 0.00 USD | 16,710,000.00 USD | 12,450,000.00 USD | 12,710,000.00 USD |
| `1D` | `2453.30` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 4,710,000.00 USD | 2,600,000.00 USD | 3,290,000.00 USD |
| `7D` | `2454.30` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 0.00 USD | 4,620,000.00 USD | 4,930,000.00 USD | 3,880,000.00 USD |
| `1D` | `2455.90` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 1,050,000.00 USD | 2,090,000.00 USD | 1,120,000.00 USD |
| `7D` | `2457.60` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 0.00 USD | 15,150,000.00 USD | 12,540,000.00 USD | 12,600,000.00 USD |
| `1D` | `2458.50` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 1,400,000.00 USD | 2,620,000.00 USD | 479,530.00 USD |
| `7D` | `2460.90` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 0.00 USD | 5,580,000.00 USD | 8,670,000.00 USD | 6,870,000.00 USD |
| `1D` | `2461.10` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 470,530.00 USD | 46,520.00 USD | 366,800.00 USD |
| `1D` | `2463.70` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 619,960.00 USD | 829,050.00 USD |
| `7D` | `2464.20` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 0.00 USD | 8,720,000.00 USD | 7,700,000.00 USD | 4,700,000.00 USD |
| `1D` | `2466.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 83,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2467.50` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 0.00 USD | 4,540,000.00 USD | 3,710,000.00 USD | 586,780.00 USD |
| `1D` | `2468.90` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 1,250,000.00 USD | 391,890.00 USD |
| `7D` | `2470.80` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 0.00 USD | 3,960,000.00 USD | 2,290,000.00 USD | 522,210.00 USD |
| `7D` | `2474.10` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 0.00 USD | 5,230,000.00 USD | 2,920,000.00 USD | 2,400,000.00 USD |
| `1D` | `2476.70` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 943,590.00 USD | 40,210.00 USD |
| `7D` | `2477.40` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 0.00 USD | 1,660,000.00 USD | 4,420,000.00 USD | 718,840.00 USD |
| `1D` | `2479.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 0.00 USD | 26,700.00 USD | 0.00 USD |
| `7D` | `2480.70` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 0.00 USD | 2,110,000.00 USD | 4,170,000.00 USD | 540,990.00 USD |
| `1D` | `2481.90` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 525,130.00 USD | 136,500.00 USD | 451,780.00 USD |
| `7D` | `2484.00` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 0.00 USD | 1,210,000.00 USD | 1,390,000.00 USD | 1,430,000.00 USD |
| `1D` | `2484.50` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 925,970.00 USD | 1,330,000.00 USD | 0.00 USD |
| `1D` | `2487.10` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2487.30` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 0.00 USD | 275,450.00 USD | 211,130.00 USD | 0.00 USD |
| `1D` | `2489.70` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 300,240.00 USD | 0.00 USD |
| `7D` | `2490.60` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 0.00 USD | 2,910,000.00 USD | 2,540,000.00 USD | 239,380.00 USD |
| `1D` | `2492.30` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 340,580.00 USD | 44,470.00 USD | 348,110.00 USD |
| `7D` | `2493.90` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 0.00 USD | 1,610,000.00 USD | 1,760,000.00 USD | 3,940,000.00 USD |
| `1D` | `2494.90` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 134,080.00 USD | 33,960.00 USD |
| `7D` | `2497.20` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 0.00 USD | 2,860,000.00 USD | 4,770,000.00 USD | 6,460,000.00 USD |
| `1D` | `2497.50` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,270.00 USD |
| `1D` | `2500.10` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD |
| `7D` | `2500.50` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 0.00 USD | 1,110,000.00 USD | 1,450,000.00 USD | 1,130,000.00 USD |
| `1D` | `2502.70` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD |
| `7D` | `2503.80` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 0.00 USD | 63,860.00 USD | 1,480,000.00 USD | 125,600.00 USD |
| `1D` | `2505.30` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD |
| `7D` | `2507.10` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 0.00 USD | 4,340,000.00 USD | 3,090,000.00 USD | 3,180,000.00 USD |
| `7D` | `2510.40` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 0.00 USD | 2,290,000.00 USD | 1,270,000.00 USD | 0.00 USD |
| `1D` | `2510.50` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD |
| `1D` | `2513.10` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2513.70` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 0.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2515.70` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `7D` | `2517.00` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 0.00 USD | 97,050.00 USD | 189,640.00 USD | 815,620.00 USD |
| `7D` | `2520.30` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD |
| `1D` | `2520.90` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 80,610.00 USD | 121,470.00 USD | 88,290.00 USD |
| `1D` | `2523.50` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 563,140.00 USD | 537,030.00 USD | 532,370.00 USD |
| `7D` | `2523.60` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 0.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD |
| `1D` | `2526.10` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 754,970.00 USD | 304,560.00 USD | 0.00 USD |
| `7D` | `2526.90` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 0.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD |
| `7D` | `2530.20` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 0.00 USD | 2,800,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD |
| `7D` | `2533.50` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 0.00 USD | 3,530,000.00 USD | 1,850,000.00 USD | 2,030,000.00 USD |
| `7D` | `2536.80` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 0.00 USD | 3,720,000.00 USD | 3,450,000.00 USD | 3,530,000.00 USD |
| `7D` | `2540.10` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 0.00 USD | 4,150,000.00 USD | 3,220,000.00 USD | 1,580,000.00 USD |
| `7D` | `2543.40` | 2,730,000,000.00 USD | 2,730,000,000.00 USD | 0.00 USD | 4,150,000.00 USD | 2,520,000.00 USD | 2,480,000.00 USD |
| `7D` | `2546.70` | 2,730,000,000.00 USD | 2,730,000,000.00 USD | 0.00 USD | 1,450,000.00 USD | 1,090,000.00 USD | 2,290,000.00 USD |
| `7D` | `2550.00` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 0.00 USD | 4,320,000.00 USD | 3,550,000.00 USD | 3,720,000.00 USD |
| `7D` | `2553.30` | 2,750,000,000.00 USD | 2,750,000,000.00 USD | 0.00 USD | 2,820,000.00 USD | 788,360.00 USD | 2,600,000.00 USD |
| `7D` | `2556.60` | 2,760,000,000.00 USD | 2,760,000,000.00 USD | 0.00 USD | 2,760,000.00 USD | 283,560.00 USD | 6,500,000.00 USD |
| `7D` | `2559.90` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 5,720,000.00 USD | 2,130,000.00 USD | 1,390,000.00 USD |
| `7D` | `2563.20` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 1,430,000.00 USD | 2,900,000.00 USD | 1,290,000.00 USD |
| `7D` | `2566.50` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 0.00 USD | 1,860,000.00 USD | 1,830,000.00 USD | 3,300,000.00 USD |
| `7D` | `2569.80` | 2,780,000,000.00 USD | 2,780,000,000.00 USD | 0.00 USD | 125,250.00 USD | 341,900.00 USD | 1,190,000.00 USD |
| `7D` | `2573.10` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,790,000.00 USD |
| `7D` | `2576.40` | 2,790,000,000.00 USD | 2,790,000,000.00 USD | 0.00 USD | 2,400,000.00 USD | 930,280.00 USD | 1,640,000.00 USD |
| `7D` | `2579.70` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 0.00 USD | 2,750,000.00 USD | 1,780,000.00 USD | 1,960,000.00 USD |
| `7D` | `2583.00` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 0.00 USD | 1,730,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD |
| `7D` | `2586.30` | 2,810,000,000.00 USD | 2,810,000,000.00 USD | 0.00 USD | 1,480,000.00 USD | 2,030,000.00 USD | 2,570,000.00 USD |
| `7D` | `2589.60` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 3,310,000.00 USD | 631,590.00 USD | 2,150,000.00 USD |
| `7D` | `2592.90` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 2,370,000.00 USD | 1,280,000.00 USD | 1,580,000.00 USD |
| `7D` | `2596.20` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 794,750.00 USD | 620,840.00 USD | 1,490,000.00 USD |
| `7D` | `2599.50` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,530,000.00 USD | 2,810,000.00 USD |
| `7D` | `2602.80` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 1,680,000.00 USD | 1,260,000.00 USD | 1,690,000.00 USD |
| `7D` | `2606.10` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 1,850,000.00 USD | 1,560,000.00 USD | 772,800.00 USD |
| `7D` | `2609.40` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD |
| `7D` | `2612.70` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 1,010,000.00 USD | 643,740.00 USD | 43,560.00 USD |
| `7D` | `2616.00` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 1,970,000.00 USD | 1,170,000.00 USD | 801,910.00 USD |
| `7D` | `2619.30` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 449,020.00 USD | 323,810.00 USD | 268,500.00 USD |
| `7D` | `2622.60` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 631,440.00 USD | 1,220,000.00 USD | 0.00 USD |
| `7D` | `2625.90` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 485,890.00 USD | 474,490.00 USD | 0.00 USD |
| `7D` | `2629.20` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31,040.00 USD |
| `7D` | `2632.40` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 0.00 USD | 301,060.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `29.32B` | Total OI Tokens: `12,940,739.2 ETH`
  * 1h OI Change: `+1.11%` | 4h OI Change: `-1.27%` | 24h OI Change: `-1.91%`
  * Exchange Breakdown: Binance=`8.51B` | Bybit=`2.12B` | OKX=`1.76B` | Hyperliquid=`2.57B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-216.57K` | Last 24h: `2.27M` | Last 3d: `7.66M` | Last 7d: `13.85M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0027%` | **USDT OKX** | `0.0002%` |
| **USDT Bybit** | `-0.0048%` | **USDT KuCoin** | `-0.0050%` |
| **USDT MEXC** | `-0.0026%` | **USDT BingX** | `0.0026%` |
| **USDT Gate** | `-0.0008%` | **USDT Bitget** | `0.0025%` |
| **CoinM Binance** | `0.0088%` | **CoinM OKX** | `-0.0012%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `39.40%` | `60.60%` | `0.65` | 714,240,000.00 USD |
| `15M` | `Binance` | `40.46%` | `59.54%` | `0.68` | 218,570,000.00 USD |
| `15M` | `OKX` | `45.35%` | `54.65%` | `0.83` | 75,420,000.00 USD |
| `15M` | `Bybit` | `38.09%` | `61.91%` | `0.62` | 83,910,000.00 USD |
| `15M` | `KuCoin` | `48.8%` | `51.2%` | `0.95` | 2,670,000.00 USD |
| `15M` | `Gate` | `46.25%` | `53.75%` | `0.86` | 69,820,000.00 USD |
| `15M` | `Bitget` | `45.56%` | `54.44%` | `0.84` | 36,280,000.00 USD |
| `15M` | `BingX` | `36.33%` | `63.67%` | `0.57` | 9,720,000.00 USD |
| `15M` | `MEXC` | `27.11%` | `72.89%` | `0.37` | 38,590,000.00 USD |
| `15M` | `Bitunix` | `54.81%` | `45.19%` | `1.21` | 38,660,000.00 USD |
| `15M` | `Hyperliquid` | `24.62%` | `75.38%` | `0.33` | 55,520,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `45.55%` | `54.45%` | `0.84` | 2,750,000.00 USD |
| `15M` | `Crypto.com` | `49.49%` | `50.51%` | `0.98` | 4,100,000.00 USD |
| `15M` | `WhiteBIT` | `0.05%` | `99.95%` | `0.00` | 17,110,000.00 USD |
| `15M` | `HTX` | `44.56%` | `55.44%` | `0.80` | 2,690,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `37.46%` | `62.54%` | `0.60` | 35,030,000.00 USD |
| `15M` | `Bitfinex` | `29.38%` | `70.62%` | `0.42` | 1,840,000.00 USD |
| `15M` | `Kraken` | `39.72%` | `60.28%` | `0.66` | 7,400,000.00 USD |
| `15M` | `Aster` | `44.05%` | `55.95%` | `0.79` | 6,130,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `50.1%` | `49.9%` | `1.00` | 8,020,000.00 USD |
| `15M` | `Whale Positions` | `40.46%` | `59.54%` | `0.68` | 218,570,000.00 USD |
| `15M` | `Global Accounts` | `39.40%` | `60.60%` | `0.65` | 714,240,000.00 USD |
| `1H` | `ETH` | `50.24%` | `49.76%` | `1.01` | 5,570,000,000.00 USD |
| `1H` | `Binance` | `50.94%` | `49.06%` | `1.04` | 1,510,000,000.00 USD |
| `1H` | `OKX` | `53.01%` | `46.99%` | `1.13` | 594,190,000.00 USD |
| `1H` | `Bybit` | `56.38%` | `43.62%` | `1.29` | 565,200,000.00 USD |
| `1H` | `KuCoin` | `50.76%` | `49.24%` | `1.03` | 16,590,000.00 USD |
| `1H` | `Gate` | `49.19%` | `50.81%` | `0.97` | 537,350,000.00 USD |
| `1H` | `Bitget` | `52.77%` | `47.23%` | `1.12` | 213,220,000.00 USD |
| `1H` | `BingX` | `48.25%` | `51.75%` | `0.93` | 46,630,000.00 USD |
| `1H` | `MEXC` | `50.86%` | `49.14%` | `1.04` | 194,870,000.00 USD |
| `1H` | `Bitunix` | `53.39%` | `46.61%` | `1.15` | 231,730,000.00 USD |
| `1H` | `Hyperliquid` | `42.1%` | `57.9%` | `0.73` | 332,500,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.89%` | `48.11%` | `1.08` | 16,190,000.00 USD |
| `1H` | `Crypto.com` | `50.79%` | `49.21%` | `1.03` | 30,320,000.00 USD |
| `1H` | `WhiteBIT` | `46.39%` | `53.61%` | `0.87` | 965,660,000.00 USD |
| `1H` | `HTX` | `49.98%` | `50.02%` | `1.00` | 13,730,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `44.65%` | `55.35%` | `0.81` | 160,460,000.00 USD |
| `1H` | `Bitfinex` | `33.98%` | `66.02%` | `0.51` | 6,590,000.00 USD |
| `1H` | `Kraken` | `54.83%` | `45.17%` | `1.21` | 42,100,000.00 USD |
| `1H` | `Aster` | `57.57%` | `42.43%` | `1.36` | 37,780,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `50.5%` | `49.5%` | `1.02` | 52,810,000.00 USD |
| `1H` | `Whale Positions` | `50.94%` | `49.06%` | `1.04` | 1,510,000,000.00 USD |
| `1H` | `Global Accounts` | `50.24%` | `49.76%` | `1.01` | 5,570,000,000.00 USD |
| `4H` | `ETH` | `47.43%` | `52.57%` | `0.90` | 32,510,000,000.00 USD |
| `4H` | `Binance` | `45.96%` | `54.04%` | `0.85` | 9,000,000,000.00 USD |
| `4H` | `OKX` | `46.84%` | `53.16%` | `0.88` | 3,870,000,000.00 USD |
| `4H` | `Bybit` | `46.34%` | `53.66%` | `0.86` | 3,890,000,000.00 USD |
| `4H` | `KuCoin` | `49.9%` | `50.1%` | `1.00` | 135,040,000.00 USD |
| `4H` | `Gate` | `50.36%` | `49.64%` | `1.01` | 2,620,000,000.00 USD |
| `4H` | `Bitget` | `51.95%` | `48.05%` | `1.08` | 1,390,000,000.00 USD |
| `4H` | `BingX` | `50.06%` | `49.94%` | `1.00` | 383,190,000.00 USD |
| `4H` | `MEXC` | `48%` | `52%` | `0.92` | 1,340,000,000.00 USD |
| `4H` | `Bitunix` | `49.82%` | `50.18%` | `0.99` | 1,370,000,000.00 USD |
| `4H` | `Hyperliquid` | `43.78%` | `56.22%` | `0.78` | 2,110,000,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.55%` | `47.45%` | `1.11` | 133,230,000.00 USD |
| `4H` | `Crypto.com` | `50.66%` | `49.34%` | `1.03` | 153,390,000.00 USD |
| `4H` | `WhiteBIT` | `49.23%` | `50.77%` | `0.97` | 4,450,000,000.00 USD |
| `4H` | `HTX` | `44.36%` | `55.64%` | `0.80` | 99,300,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `48.19%` | `51.81%` | `0.93` | 640,010,000.00 USD |
| `4H` | `Bitfinex` | `21.88%` | `78.12%` | `0.28` | 39,620,000.00 USD |
| `4H` | `Kraken` | `45.7%` | `54.3%` | `0.84` | 292,020,000.00 USD |
| `4H` | `Aster` | `46.37%` | `53.63%` | `0.86` | 256,910,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.6%` | `51.4%` | `0.95` | 342,650,000.00 USD |
| `4H` | `Whale Positions` | `45.96%` | `54.04%` | `0.85` | 9,000,000,000.00 USD |
| `4H` | `Global Accounts` | `47.43%` | `52.57%` | `0.90` | 32,510,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `2259.25` | `2255.66` | `2259.25` | `2277.25` | `2230.25` | 846,756,637.45 USD | 383,814,230.15 USD | 462,942,407.30 USD | -79,128,177.15 USD | `-9.34%` | `0B / 6S` |
| `0:00 UTC` | `2260.25` | `2257.68` | `2260.25` | `2273.25` | `2245.25` | 606,671,993.02 USD | 300,593,954.86 USD | 306,078,038.17 USD | -5,484,083.31 USD | `-0.90%` | `5B / 2S` |
| `5:00 UTC` | `2281.25` | `2281.90` | `2281.25` | `2293.75` | `2267.75` | 508,254,989.09 USD | 245,674,110.48 USD | 262,580,878.61 USD | -16,906,768.14 USD | `-3.33%` | `3B / 0S` |
| `0:00 UTC` | `2287.25` | `2284.17` | `2287.25` | `2293.25` | `2271.25` | 175,571,332.73 USD | 84,909,600.78 USD | 90,661,731.96 USD | -5,752,131.18 USD | `-3.28%` | `0B / 2S` |
| `5:00 UTC` | `2272.25` | `2272.48` | `2272.25` | `2279.25` | `2266.25` | 164,039,523.36 USD | 80,192,631.79 USD | 83,846,891.57 USD | -3,654,259.77 USD | `-2.23%` | `1B / 3S` |
| `0:00 UTC` | `2258.75` | `2262.31` | `2258.75` | `2272.75` | `2251.25` | 318,288,167.50 USD | 151,770,310.17 USD | 166,517,857.34 USD | -14,747,547.17 USD | `-4.63%` | `1B / 1S` |
| `5:00 UTC` | `2278.25` | `2270.43` | `2278.25` | `2280.25` | `2256.75` | 150,284,586.83 USD | 75,795,431.23 USD | 74,489,155.60 USD | 1,306,275.62 USD | `+0.87%` | `2B / 0S` |
| `0:00 UTC` | `2282.25` | `2277.79` | `2282.25` | `2284.25` | `2269.25` | 149,129,529.31 USD | 68,364,987.96 USD | 80,764,541.35 USD | -12,399,553.39 USD | `-8.31%` | `3B / 4S` |
| `5:00 UTC` | `2273.25` | `2273.28` | `2273.25` | `2276.25` | `2269.75` | 79,152,401.54 USD | 40,301,870.39 USD | 38,850,531.15 USD | 1,451,339.24 USD | `+1.83%` | `0B / 0S` |
| `0:00 UTC` | `2266.75` | `2265.59` | `2266.75` | `2273.25` | `2260.75` | 114,607,437.43 USD | 55,510,584.11 USD | 59,096,853.32 USD | -3,586,269.21 USD | `-3.13%` | `0B / 4S` |

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
| `5m` | -5,450,000.00 USD | -6,440,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -12,680,000.00 USD | 6,710,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -15,840,000.00 USD | -15,230,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -20,100,000.00 USD | 25,740,000.00 USD | **`ACCUMULATION`** |
| `2h` | -20,820,000.00 USD | -29,640,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -106,560,000.00 USD | -1,160,000,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -113,760,000.00 USD | -1,360,000,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -98,010,000.00 USD | -1,220,000,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -95,020,000.00 USD | -1,260,000,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -142,990,000.00 USD | -1,730,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -125,720,000.00 USD | -2,280,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,110,000,000.00 USD | -9,280,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-5.45M` | 15m=`-12.68M` | 1h=`-20.10M` | 24h=`-142.99M`
* Futures Capital Netflows: 5m=`-6.44M` | 15m=`+6.71M` | 1h=`+25.74M` | 24h=`-1.73B`
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
  * `2026-10-30 04:15:34 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:40:34 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:42:34 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `2255.59` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2226.38` (Risk Distance: `29.21` pts)
  * +2.5R Take Profit: `2328.61`
  * Mathematical Lot Sizing: **`0.34 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2276.08` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2305.29` (Risk Distance: `29.21` pts)
  * +2.5R Take Profit: `2203.06`
  * Mathematical Lot Sizing: **`0.34 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2276.57`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
