# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-29 22:55:03 IST` (`2026-10-29 17:25:03 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2347.60` | **Live Ask Quote**: `2350.60` | **Mid Price**: `2349.10`
- **Spread Points**: `300.00` | **Spread BPS**: `12.77 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2323.01` | VWAP Z-Score: `+1.20` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `11.48` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `55.56` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2379.86` | Lower -3.00σ Band: `2266.16`
  * Upper +2.51σ Band: `2370.58` | Lower -2.51σ Band: `2275.44`
  * Upper +2.01σ Band: `2361.10` | Lower -2.01σ Band: `2284.92`
  * Upper +2.00σ Band: `2360.91` | Lower -2.00σ Band: `2285.11`
  * Upper +1.28σ Band: `2347.27` | Lower -1.28σ Band: `2298.75`
  * Upper +1.00σ Band: `2341.96` | Lower -1.00σ Band: `2304.06`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2350.51` | EMA-20=`2342.46` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2332.53` (Slope: `+0.0000`) | EMA-100=`2331.74`
  * Institutional Anchors: EMA-144=`2331.61` | EMA-200=`2330.16` (Slope: `+0.1177`) | EMA-233=`2328.89`
- **Range Boundaries**: 24H High=`2387.80` | 24H Low=`2288.80` | Weekly High=`2387.80` | Weekly Low=`2288.80`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2337.88` (Distance: `+0.48%`)
  * Point of Control (POC) = `2318.94` (Distance: `+1.30%`)
  * Value Area Low (VAL) = `2293.68` (Distance: `+2.42%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2367.21` | POC=`2350.17` | VAL=`2335.02`
  * Prior Day Extremes: PDH=`2387.80` | PDL=`2316.80` | PDC=`2356.60`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2341.03` | Weekly POC=`2309.86` | Weekly VAL=`2299.24`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2367.70` | Low=`2288.80`
  * London Session (08:00-16:00 UTC): High=`2331.00` | Low=`2299.00`
  * New York Session (13:00-21:00 UTC): High=`2374.90` | Low=`2307.50`
  * Initial Balance (First Hour): IB High=`2331.00` | IB Low=`2299.30`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2339.70` - `2358.50`
  * Optimal Trade Entry (OTE 0.705): `2353.80`
  * Structural Invalidation Anchor (0.786): `2367.89`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2351.72` | `2353.50` | `2348.93` | `2348.93` | `11,533` | 27,122,245.49 USD | -7,594,665.97 USD | `-28.00%` | -205,661,282.12 USD | `-0.02` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `2348.93` | `2350.87` | `2346.54` | `2349.32` | `22,365` | 52,524,745.05 USD | -3,806,542.39 USD | `-7.25%` | -209,467,824.51 USD | `+0.24` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `2349.31` | `2352.81` | `2348.91` | `2350.67` | `5,758` | 13,538,155.55 USD | 3,467,694.13 USD | `+25.61%` | -206,000,130.38 USD | `+0.81` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `2357.71` | `2358.31` | `2350.50` | `2352.18` | `30,135` | 70,925,128.95 USD | -17,709,135.06 USD | `-24.97%` | -188,566,462.45 USD | `-0.60` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `2352.18` | `2353.79` | `2348.93` | `2348.93` | `39,101` | 91,943,279.10 USD | -19,199,964.77 USD | `-20.88%` | -207,766,427.22 USD | `-0.62` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `2348.93` | `2352.81` | `2346.54` | `2350.67` | `28,122` | 66,060,190.28 USD | -341,473.95 USD | `-0.52%` | -208,107,901.17 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `2343.79` | `2372.42` | `2343.64` | `2368.02` | `352,713` | 832,609,165.45 USD | 75,422,863.20 USD | `+9.06%` | -132,463,849.43 USD | `+2.09` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `2368.02` | `2378.69` | `2350.25` | `2352.18` | `255,135` | 602,581,670.57 USD | -105,228,527.95 USD | `-17.46%` | -237,692,377.38 USD | `-2.06` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `2352.18` | `2353.79` | `2346.54` | `2350.67` | `67,224` | 158,006,179.70 USD | -19,538,813.03 USD | `-12.37%` | -257,231,190.40 USD | `-0.11` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2309.10` | `2330.05` | `2308.88` | `2324.26` | `409,016` | 949,400,649.22 USD | -49,162,247.72 USD | `-5.18%` | -277,081,181.03 USD | `+0.30` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -173,041,008.80 USD | `+1.51` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2346.54` | `2350.66` | `322,353` | 760,572,596.80 USD | -124,771,160.84 USD | `-16.40%` | -297,812,169.64 USD | `-0.83` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `2358.56` | `2360.38` | `2292.20` | `2308.04` | `812,683` | 1,883,052,517.85 USD | -183,572,583.45 USD | `-9.75%` | -193,002,187.18 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2308.03` | `2334.83` | `2303.75` | `2309.10` | `525,175` | 1,216,920,375.04 USD | -34,916,746.14 USD | `-2.87%` | -227,918,933.31 USD | `+0.53` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2309.10` | `2330.05` | `2308.88` | `2324.26` | `409,016` | 949,400,649.22 USD | -49,162,247.72 USD | `-5.18%` | -277,081,181.03 USD | `+0.30` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -173,041,008.80 USD | `+1.51` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2346.54` | `2350.66` | `322,353` | 760,572,596.80 USD | -124,771,160.84 USD | `-16.40%` | -297,812,169.64 USD | `-0.83` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`2349.10`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2348.70` | `616.2313` | 1,447,342.45 USD | 13,307,906.07 USD | `17 orders` | `-0.08%` | `-` |
| `BID` | `2348.80` | `466.5755` | 1,095,892.53 USD | 11,860,563.62 USD | `24 orders` | `-0.08%` | `-` |
| `BID` | `2348.90` | `193.6126` | 454,776.64 USD | 10,764,671.08 USD | `24 orders` | `-0.07%` | `-` |
| `BID` | `2349.00` | `173.4402` | 407,411.03 USD | 10,309,894.45 USD | `12 orders` | `-0.07%` | `-` |
| `BID` | `2349.10` | `529.4508` | 1,243,732.87 USD | 9,902,483.42 USD | `21 orders` | `-0.07%` | `-` |
| `BID` | `2349.20` | `154.1472` | 362,122.60 USD | 8,658,750.54 USD | `16 orders` | `-0.06%` | `-` |
| `BID` | `2349.30` | `357.8456` | 840,686.67 USD | 8,296,627.94 USD | `21 orders` | `-0.06%` | `-` |
| `BID` | `2349.40` | `136.8434` | 321,499.88 USD | 7,455,941.27 USD | `15 orders` | `-0.05%` | `-` |
| `BID` | `2349.50` | `431.8768` | 1,014,694.54 USD | 7,134,441.39 USD | `13 orders` | `-0.05%` | `-` |
| `BID` | `2349.60` | `333.4713` | 783,524.17 USD | 6,119,746.85 USD | `24 orders` | `-0.04%` | `-` |
| `BID` | `2349.70` | `179.9942` | 422,932.37 USD | 5,336,222.68 USD | `22 orders` | `-0.04%` | `-` |
| `BID` | `2349.80` | `253.4712` | 595,606.63 USD | 4,913,290.31 USD | `24 orders` | `-0.04%` | `-` |
| `BID` | `2349.90` | `197.8537` | 464,936.41 USD | 4,317,683.68 USD | `24 orders` | `-0.03%` | `-` |
| `BID` | `2350.00` | `201.4294` | 473,359.09 USD | 3,852,747.27 USD | `27 orders` | `-0.03%` | `-` |
| `BID` | `2350.10` | `326.9827` | 768,442.04 USD | 3,379,388.18 USD | `24 orders` | `-0.02%` | `-` |
| `BID` | `2350.20` | `359.7100` | 845,390.44 USD | 2,610,946.14 USD | `24 orders` | `-0.02%` | `-` |
| `BID` | `2350.30` | `173.7092` | 408,268.73 USD | 1,765,555.70 USD | `20 orders` | `-0.01%` | `-` |
| `BID` | `2350.40` | `129.2330` | 303,749.24 USD | 1,357,286.96 USD | `17 orders` | `-0.01%` | `-` |
| `BID` | `2350.50` | `169.4834` | 398,370.73 USD | 1,053,537.72 USD | `16 orders` | `-0.01%` | `-` |
| `BID` | `2350.60` | `278.7233` | 655,166.99 USD | 655,166.99 USD | `36 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2350.65` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,350.65` | `0.00%` | `-` |
| `ASK` | `2350.70` | `0.0297` | 69.82 USD | 69.82 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `2350.80` | `0.0571` | 134.23 USD | 204.05 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `2350.90` | `27.2142` | 63,977.86 USD | 64,181.91 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `2351.00` | `54.4165` | 127,933.19 USD | 192,115.10 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `2351.10` | `50.8267` | 119,498.65 USD | 311,613.76 USD | `9 orders` | `+0.02%` | `-` |
| `ASK` | `2351.20` | `50.4643` | 118,651.66 USD | 430,265.42 USD | `18 orders` | `+0.02%` | `-` |
| `ASK` | `2351.30` | `202.3387` | 475,758.99 USD | 906,024.40 USD | `22 orders` | `+0.03%` | `-` |
| `ASK` | `2351.40` | `180.0751` | 423,428.59 USD | 1,329,452.99 USD | `16 orders` | `+0.03%` | `-` |
| `ASK` | `2351.50` | `188.8023` | 443,968.61 USD | 1,773,421.60 USD | `15 orders` | `+0.04%` | `-` |
| `ASK` | `2351.60` | `303.0664` | 712,690.95 USD | 2,486,112.55 USD | `19 orders` | `+0.04%` | `-` |
| `ASK` | `2351.70` | `265.9413` | 625,414.16 USD | 3,111,526.70 USD | `23 orders` | `+0.04%` | `-` |
| `ASK` | `2351.80` | `414.6599` | 975,197.15 USD | 4,086,723.86 USD | `22 orders` | `+0.05%` | `-` |
| `ASK` | `2351.90` | `268.1197` | 630,590.72 USD | 4,717,314.58 USD | `14 orders` | `+0.05%` | `-` |
| `ASK` | `2352.00` | `432.0127` | 1,016,093.87 USD | 5,733,408.45 USD | `23 orders` | `+0.06%` | `-` |
| `ASK` | `2352.10` | `300.6328` | 707,118.41 USD | 6,440,526.86 USD | `17 orders` | `+0.06%` | `-` |
| `ASK` | `2352.20` | `173.9921` | 409,264.22 USD | 6,849,791.07 USD | `16 orders` | `+0.07%` | `-` |
| `ASK` | `2352.30` | `230.4617` | 542,115.06 USD | 7,391,906.13 USD | `23 orders` | `+0.07%` | `-` |
| `ASK` | `2352.40` | `463.1198` | 1,089,443.02 USD | 8,481,349.15 USD | `18 orders` | `+0.07%` | `-` |
| `ASK` | `2352.50` | `199.8163` | 470,067.85 USD | 8,951,416.99 USD | `27 orders` | `+0.08%` | `-` |
| `ASK` | `2352.60` | `226.8320` | 533,644.96 USD | 9,485,061.96 USD | `23 orders` | `+0.08%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:54:46 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1892.00` | `8,092.45` | 15,310,914.71 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-29 22:54:46 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1918.00` | `4,184.01` | 8,024,935.59 USD | `TRIGGER_STOP` | `0x6ea486a342` | `2026-10-29 22:54:46 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `8,500.00` | 16,371,850.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-29 22:54:46 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2040.65` | `7,964.66` | 16,253,082.08 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-29 22:54:46 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2101.66` | `10,000.00` | 21,016,620.86 USD | `AT_RISK_LIQ` | `0x469e9a7f62` | `2026-10-29 22:54:46 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2171.11` | `48,499.51` | 105,297,832.78 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-29 22:54:46 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2180.17` | `44,734.81` | 97,529,693.12 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-29 22:54:46 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2250.00` | `6,500.00` | 14,625,000.00 USD | `TRIGGER_STOP` | `0x6eae4120a8` | `2026-10-29 22:54:46 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2292.00` | `2,500.00` | 5,730,000.00 USD | `TRIGGER_STOP` | `0x934de82f50` | `2026-10-29 22:54:46 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2307.20` | `599,999.99` | 1,384,319,976.93 USD | `TRIGGER_STOP` | `0x069604ebfb` | `2026-10-29 22:54:46 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2310.00` | `2,000.00` | 4,620,000.00 USD | `TRIGGER_STOP` | `0x524ed67d71` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2311.00` | `1,015.35` | 2,346,465.99 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x674982e841` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2313.70` | `1,964.55` | 4,545,369.39 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2315.00` | `5,430.46` | 12,571,509.81 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-29 22:54:46 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2319.00` | `2,500.00` | 5,797,500.00 USD | `TRIGGER_STOP` | `0x524ed67d71` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2324.20` | `1,342.94` | 3,121,267.19 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2329.00` | `343.53` | 800,091.38 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2329.20` | `600.63` | 1,398,994.38 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2334.10` | `925.39` | 2,159,962.84 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2334.80` | `2,794.82` | 6,525,348.07 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2334.90` | `405.95` | 947,848.22 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x7b7f72a28f` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2338.00` | `600.49` | 1,403,952.63 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2338.00` | `433.02` | 1,012,396.08 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2340.20` | `332.56` | 778,259.49 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2340.40` | `1,711.02` | 4,004,461.38 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2341.00` | `692.47` | 1,621,071.10 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2342.70` | `1,281.97` | 3,003,269.24 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2342.90` | `1,426.13` | 3,341,284.19 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2343.20` | `600.16` | 1,406,304.28 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2345.60` | `853.61` | 2,002,228.32 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2345.70` | `433.02` | 1,015,739.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2345.80` | `454.32` | 1,065,743.39 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2347.30` | `639.73` | 1,501,637.52 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2347.80` | `400.07` | 939,284.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2348.10` | `332.30` | 780,280.91 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2348.30` | `380.26` | 892,968.55 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x76bf72092b` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2349.40` | `426.10` | 1,001,075.82 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2355.40` | `328.00` | 772,578.74 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2355.70` | `424.97` | 1,001,096.65 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2356.70` | `378.92` | 893,011.84 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x76bf72092b` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2356.90` | `400.07` | 942,936.77 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2357.40` | `637.01` | 1,501,678.89 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2358.10` | `433.21` | 1,021,550.14 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2358.80` | `1,427.73` | 3,367,734.24 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2358.80` | `470.53` | 1,109,878.14 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2359.60` | `848.54` | 2,002,218.52 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2360.50` | `327.35` | 772,708.97 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2361.10` | `600.33` | 1,417,429.72 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2361.60` | `1,271.72` | 3,003,295.37 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2363.70` | `676.26` | 1,598,465.83 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2364.80` | `1,693.35` | 4,004,445.67 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2365.60` | `600.10` | 1,419,584.73 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2366.80` | `407.74` | 965,032.17 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x7b7f72a28f` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2366.90` | `2,797.90` | 6,622,353.06 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2366.90` | `432.96` | 1,024,782.49 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2370.40` | `953.03` | 2,259,055.20 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2372.50` | `600.47` | 1,424,605.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2375.00` | `336.88` | 800,091.43 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2379.90` | `1,363.97` | 3,246,119.82 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2388.70` | `5,408.95` | 12,920,349.79 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2391.50` | `1,943.68` | 4,648,309.76 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 22:54:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2396.00` | `500.00` | 1,198,000.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xaa53f4044a` | `2026-10-29 22:54:46 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2440.00` | `4,002.10` | 9,765,127.17 USD | `TRIGGER_STOP` | `0xfb941d2344` | `2026-10-29 22:54:46 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `3,058.48` | 7,688,708.10 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-29 22:54:46 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2658.62` | `9,700.00` | 25,788,617.00 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-29 22:54:46 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2708.97` | `8,500.00` | 23,026,257.07 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-29 22:54:46 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 250,039,054.24 USD | `106,417.71` | `2322.74` | `2349.90` | `3788.49` | -2,858,042.08 USD | `-1.14%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 153,082,176.67 USD | `65,205.17` | `2375.30` | `2349.90` | `4312.22` | 1,800,086.43 USD | `+1.18%` | `5X Cross` |
| `6` | `0x77dd...e0e9` | `LONG` | 113,876,853.94 USD | `48,499.51` | `2610.31` | `2349.90` | `2171.14` | -12,722,029.92 USD | `-11.17%` | `10X Cross` |
| `7` | `0x0392...d7d9` | `LONG` | 105,140,231.93 USD | `44,734.81` | `2518.71` | `2349.90` | `2180.20` | -7,534,074.64 USD | `-7.17%` | `9X Cross` |
| `15` | `0xde8d...9524` | `LONG` | 71,227,846.92 USD | `30,282.40` | `2134.45` | `2349.90` | `1787.09` | 6,591,516.34 USD | `+9.25%` | `20X Cross` |
| `17` | `0x7fda...17d1` | `SHORT` | 65,990,923.64 USD | `28,082.44` | `2437.87` | `2349.90` | `3714.62` | 2,470,517.70 USD | `+3.74%` | `25X Cross` |
| `25` | `0xdf95...7d72` | `SHORT` | 53,223,924.91 USD | `22,652.33` | `2402.54` | `2349.90` | `3948.61` | 1,199,248.05 USD | `+2.25%` | `25X Cross` |
| `29` | `0xeced...6210` | `SHORT` | 43,958,785.73 USD | `18,687.58` | `2522.09` | `2349.90` | `3356.74` | 3,173,126.73 USD | `+7.22%` | `20X Cross` |
| `34` | `0xb695...a92d` | `SHORT` | 39,222,446.59 USD | `16,704.62` | `2557.74` | `2349.90` | `4012.51` | 3,503,718.46 USD | `+8.93%` | `20X Cross` |
| `35` | `0x6046...b21d` | `LONG` | 37,463,602.29 USD | `15,927.59` | `2410.19` | `2349.90` | `1536.48` | -925,017.36 USD | `-2.47%` | `6X Cross` |
| `39` | `0x45d2...4029` | `SHORT` | 32,758,785.00 USD | `13,950.00` | `2443.60` | `2349.90` | `4886.44` | 1,329,497.46 USD | `+4.06%` | `20X Cross` |
| `45` | `0xbd1c...ff0e` | `LONG` | 28,198,800.00 USD | `12,000.00` | `2419.91` | `2349.90` | `1520.97` | -840,232.39 USD | `-2.98%` | `20X Cross` |
| `46` | `0x2371...0883` | `LONG` | 28,172,400.00 USD | `12,000.00` | `2421.77` | `2349.90` | `1280.07` | -888,894.85 USD | `-3.16%` | `20X Cross` |
| `50` | `0x09dc...c094` | `LONG` | 25,839,000.00 USD | `11,000.00` | `2465.31` | `2349.90` | `1638.04` | -1,279,423.04 USD | `-4.95%` | `20X Cross` |
| `51` | `0xa9de...e049` | `LONG` | 25,829,100.00 USD | `11,000.00` | `2481.81` | `2349.90` | `1644.71` | -1,470,879.46 USD | `-5.69%` | `20X Cross` |
| `52` | `0x0c5d...36b3` | `LONG` | 25,824,150.00 USD | `11,000.00` | `2482.20` | `2349.90` | `1645.04` | -1,480,103.24 USD | `-5.73%` | `20X Cross` |
| `53` | `0x6c93...59a4` | `LONG` | 25,823,600.00 USD | `11,000.00` | `2441.15` | `2349.90` | `1603.00` | -1,029,072.73 USD | `-3.99%` | `20X Cross` |
| `57` | `0xa61c...66b9` | `LONG` | 25,561,757.60 USD | `10,888.00` | `2398.32` | `2349.90` | `1386.90` | -551,199.79 USD | `-2.16%` | `10X Cross` |
| `60` | `0x4487...c92d` | `SHORT` | 25,146,599.96 USD | `10,701.14` | `2374.04` | `2349.90` | `2880.35` | 258,365.52 USD | `+1.03%` | `10X Cross` |
| `61` | `0xecb6...2b00` | `SHORT` | 24,615,939.19 USD | `10,475.31` | `2327.62` | `2349.90` | `5516.34` | -233,318.11 USD | `-0.95%` | `15X Cross` |
| `70` | `0xa2ce...3126` | `LONG` | 23,535,649.97 USD | `10,016.88` | `2162.83` | `2349.90` | `1448.84` | 1,870,847.92 USD | `+7.95%` | `10X Cross` |
| `71` | `0x15a4...dfdb` | `LONG` | 23,527,000.00 USD | `10,000.00` | `1761.94` | `2349.90` | `0.000000` | 5,907,518.97 USD | `+25.11%` | `20X Cross` |
| `72` | `0x6646...6de5` | `LONG` | 23,499,000.00 USD | `10,000.00` | `1765.80` | `2349.90` | `1737.38` | 5,840,942.55 USD | `+24.86%` | `25X Cross` |
| `73` | `0x469e...58a5` | `LONG` | 23,494,000.00 USD | `10,000.00` | `2463.91` | `2349.90` | `2107.35` | -1,145,141.54 USD | `-4.87%` | `25X Cross` |
| `74` | `0xec7f...df39` | `LONG` | 23,490,000.00 USD | `10,000.00` | `2719.35` | `2349.90` | `1721.56` | -3,703,548.52 USD | `-15.77%` | `20X Cross` |
| `80` | `0xaeaa...2416` | `SHORT` | 22,772,690.00 USD | `9,700.00` | `2311.92` | `2349.90` | `2658.65` | -347,007.60 USD | `-1.52%` | `25X Cross` |
| `85` | `0xca49...53c8` | `SHORT` | 21,770,087.86 USD | `9,264.26` | `2549.47` | `2349.90` | `3704.44` | 1,848,936.87 USD | `+8.49%` | `25X Cross` |
| `87` | `0xba5d...a352` | `SHORT` | 21,259,984.10 USD | `9,054.12` | `2493.89` | `2349.90` | `2894.95` | 1,320,023.16 USD | `+6.21%` | `20X Cross` |
| `88` | `0xea00...a918` | `LONG` | 21,137,832.81 USD | `9,003.83` | `2003.01` | `2349.90` | `1168.46` | 3,103,053.95 USD | `+14.68%` | `5X Cross` |
| `95` | `0xb37f...66ca` | `SHORT` | 19,958,000.00 USD | `8,500.00` | `2308.30` | `2349.90` | `2709.00` | -337,445.81 USD | `-1.69%` | `25X Cross` |
| `108` | `0x9eec...daab` | `LONG` | 19,001,077.53 USD | `8,092.45` | `1658.44` | `2349.90` | `1893.09` | 5,580,213.00 USD | `+29.37%` | `15X Cross` |
| `109` | `0x218a...7da2` | `SHORT` | 18,790,792.10 USD | `7,997.78` | `2208.16` | `2349.90` | `2877.22` | -1,130,396.88 USD | `-6.02%` | `10X Cross` |
| `110` | `0x5f91...65aa` | `LONG` | 18,738,445.94 USD | `7,964.66` | `1626.99` | `2349.90` | `2040.68` | 5,780,002.87 USD | `+30.85%` | `16X Cross` |
| `115` | `0xcf53...ee11` | `SHORT` | 17,865,484.11 USD | `7,603.63` | `1862.69` | `2349.90` | `3978.29` | -3,702,220.17 USD | `-20.72%` | `7X Cross` |
| `116` | `0x524e...0de0` | `LONG` | 17,607,750.00 USD | `7,500.00` | `2320.35` | `2349.90` | `2115.20` | 205,063.78 USD | `+1.16%` | `10X Cross` |
| `121` | `0x939f...04d2` | `LONG` | 16,958,984.35 USD | `7,223.81` | `2500.18` | `2349.90` | `1837.70` | -1,101,905.82 USD | `-6.50%` | `25X Cross` |
| `124` | `0xec0b...b078` | `LONG` | 16,466,925.86 USD | `7,007.80` | `2065.97` | `2349.90` | `989.53` | 1,988,996.27 USD | `+12.08%` | `25X Cross` |
| `130` | `0x418a...8888` | `SHORT` | 15,793,557.88 USD | `6,724.38` | `2494.55` | `2349.90` | `2955.32` | 980,765.29 USD | `+6.21%` | `25X Cross` |
| `132` | `0x4ff9...38d3` | `LONG` | 15,419,067.85 USD | `6,564.10` | `2447.40` | `2349.90` | `1670.66` | -645,954.90 USD | `-4.19%` | `3X Isolated` |
| `134` | `0xf78c...c581` | `LONG` | 15,277,470.59 USD | `6,500.22` | `2521.53` | `2349.90` | `1914.14` | -1,113,070.35 USD | `-7.29%` | `20X Cross` |
| `135` | `0x1ee7...edf5` | `LONG` | 15,276,950.00 USD | `6,500.00` | `2328.85` | `2349.90` | `2135.22` | 139,403.34 USD | `+0.91%` | `25X Cross` |
| `141` | `0x799f...5f4c` | `LONG` | 14,816,107.68 USD | `6,310.90` | `2390.33` | `2349.90` | `1708.17` | -269,056.94 USD | `-1.82%` | `20X Cross` |
| `143` | `0x08bf...7872` | `SHORT` | 14,611,573.68 USD | `6,224.05` | `2258.00` | `2349.90` | `2585.90` | -557,657.57 USD | `-3.82%` | `20X Cross` |
| `145` | `0x0c4a...1b19` | `LONG` | 14,411,086.52 USD | `6,135.77` | `2382.15` | `2349.90` | `2186.42` | -205,244.84 USD | `-1.42%` | `25X Isolated` |
| `151` | `0xec4a...cf62` | `LONG` | 14,114,400.00 USD | `6,000.00` | `2318.70` | `2349.90` | `2081.14` | 202,154.88 USD | `+1.43%` | `25X Cross` |
| `153` | `0xd9e7...4aff` | `LONG` | 14,097,000.00 USD | `6,000.00` | `2480.18` | `2349.90` | `1408.43` | -784,124.33 USD | `-5.56%` | `20X Cross` |
| `180` | `0x645b...87b8` | `SHORT` | 11,913,180.92 USD | `5,073.54` | `2421.68` | `2349.90` | `6056.09` | 373,325.04 USD | `+3.13%` | `10X Cross` |
| `188` | `0x45ab...6cbc` | `LONG` | 11,574,103.09 USD | `4,920.96` | `2727.66` | `2349.90` | `1350.46` | -1,848,640.70 USD | `-15.97%` | `7X Cross` |
| `190` | `0xfb18...eb17` | `SHORT` | 11,441,965.88 USD | `4,872.45` | `2315.54` | `2349.90` | `2707.70` | -159,592.85 USD | `-1.39%` | `25X Cross` |
| `191` | `0x64b7...9da9` | `LONG` | 11,402,401.39 USD | `4,856.84` | `2604.61` | `2349.90` | `1382.02` | -1,247,813.02 USD | `-10.94%` | `25X Cross` |
| `200` | `0x5559...d43b` | `SHORT` | 11,174,046.49 USD | `4,755.93` | `2262.69` | `2349.90` | `2873.20` | -412,840.61 USD | `-3.69%` | `25X Cross` |
| `215` | `0xe091...6705` | `SHORT` | 10,572,750.47 USD | `4,500.00` | `2467.33` | `2349.90` | `2572.95` | 530,258.04 USD | `+5.02%` | `20X Cross` |
| `223` | `0xfe7c...b7ae` | `SHORT` | 10,347,389.88 USD | `4,402.58` | `2440.17` | `2349.90` | `4130.73` | 395,697.99 USD | `+3.82%` | `25X Cross` |
| `232` | `0xc179...e0c8` | `LONG` | 10,117,034.34 USD | `4,309.16` | `2342.89` | `2349.90` | `900.22` | 21,155.55 USD | `+0.21%` | `10X Cross` |
| `233` | `0x0622...8088` | `LONG` | 10,114,315.60 USD | `4,304.70` | `2357.55` | `2349.90` | `0.000000` | -34,235.67 USD | `-0.34%` | `5X Cross` |
| `238` | `0x12d2...f97f` | `LONG` | 10,020,347.78 USD | `4,264.34` | `2623.90` | `2349.90` | `1820.76` | -1,168,886.64 USD | `-11.67%` | `20X Cross` |
| `243` | `0x28bb...fca6` | `SHORT` | 9,891,751.45 USD | `4,209.61` | `1896.10` | `2349.90` | `3046.65` | -1,909,868.88 USD | `-19.31%` | `20X Cross` |
| `245` | `0x6ea4...0ea7` | `SHORT` | 9,842,888.94 USD | `4,184.01` | `2602.13` | `2349.90` | `3425.97` | 1,044,457.73 USD | `+10.61%` | `20X Cross` |
| `257` | `0x5e9e...35ee` | `SHORT` | 9,417,355.14 USD | `4,007.56` | `1796.39` | `2349.90` | `2586.46` | -2,218,205.05 USD | `-23.55%` | `20X Cross` |
| `258` | `0x3dc9...54b0` | `SHORT` | 9,410,071.13 USD | `3,999.69` | `2480.32` | `2349.90` | `5726.00` | 510,465.42 USD | `+5.42%` | `20X Cross` |
| `259` | `0xfb94...0ddf` | `SHORT` | 9,406,138.69 USD | `4,002.10` | `2382.44` | `2349.90` | `5105.36` | 128,645.46 USD | `+1.37%` | `20X Cross` |
| `260` | `0x95fe...f8fa` | `LONG` | 9,399,200.00 USD | `4,000.00` | `2341.35` | `2349.90` | `2258.96` | 33,783.49 USD | `+0.36%` | `20X Isolated` |
| `261` | `0x8cc9...2b6a` | `SHORT` | 9,389,200.00 USD | `4,000.00` | `1791.18` | `2349.90` | `3814.60` | -2,224,453.33 USD | `-23.69%` | `25X Cross` |
| `262` | `0x77ee...2902` | `SHORT` | 9,353,459.71 USD | `3,982.23` | `2476.53` | `2349.90` | `4337.33` | 508,661.87 USD | `+5.44%` | `25X Cross` |
| `272` | `0xf02d...5eb3` | `LONG` | 9,052,697.16 USD | `3,855.99` | `2513.67` | `2349.90` | `312.33` | -640,015.16 USD | `-7.07%` | `20X Cross` |
| `274` | `0x4b67...f4e7` | `LONG` | 8,980,124.72 USD | `3,820.84` | `2591.51` | `2349.90` | `1573.79` | -921,648.83 USD | `-10.26%` | `20X Cross` |
| `291` | `0x382b...3e39` | `SHORT` | 8,521,644.70 USD | `3,626.39` | `2299.42` | `2349.90` | `3748.37` | -183,034.15 USD | `-2.15%` | `25X Cross` |
| `298` | `0x8ae4...3d60` | `LONG` | 8,357,496.17 USD | `3,558.20` | `2482.21` | `2349.90` | `312.92` | -474,701.87 USD | `-5.68%` | `10X Cross` |
| `326` | `0x9c06...0560` | `SHORT` | 7,761,761.21 USD | `3,303.58` | `2270.55` | `2349.90` | `3274.16` | -260,797.26 USD | `-3.36%` | `25X Cross` |
| `334` | `0x984e...14c2` | `SHORT` | 7,312,859.19 USD | `3,111.99` | `2357.50` | `2349.90` | `2434.93` | 23,663.57 USD | `+0.32%` | `20X Cross` |
| `338` | `0x9c2a...f6a8` | `SHORT` | 7,180,389.04 USD | `3,058.48` | `2543.83` | `2349.90` | `2590.45` | 599,871.59 USD | `+8.35%` | `20X Cross` |
| `341` | `0x007d...67a0` | `LONG` | 7,049,700.00 USD | `3,000.00` | `2400.00` | `2349.90` | `1493.21` | -150,300.00 USD | `-2.13%` | `25X Cross` |
| `342` | `0x39b4...5c34` | `SHORT` | 7,045,239.93 USD | `3,000.91` | `2329.97` | `2349.90` | `2405.85` | -53,196.18 USD | `-0.76%` | `25X Cross` |
| `343` | `0x4a20...3c26` | `LONG` | 7,044,000.00 USD | `3,000.00` | `2428.72` | `2349.90` | `173.61` | -242,160.28 USD | `-3.44%` | `20X Cross` |
| `384` | `0xf517...c032` | `SHORT` | 6,428,989.06 USD | `2,738.07` | `2053.90` | `2349.90` | `5638.15` | -805,247.16 USD | `-12.53%` | `25X Cross` |
| `398` | `0xc619...10f5` | `LONG` | 6,116,500.00 USD | `2,600.00` | `2318.40` | `2349.90` | `1841.90` | 88,651.09 USD | `+1.45%` | `25X Cross` |
| `399` | `0xbb34...1696` | `LONG` | 6,103,890.00 USD | `2,600.00` | `2318.80` | `2349.90` | `1961.27` | 74,989.15 USD | `+1.23%` | `25X Cross` |
| `405` | `0x8328...f54a` | `SHORT` | 6,048,605.42 USD | `2,576.45` | `2292.01` | `2349.90` | `3280.20` | -143,334.14 USD | `-2.37%` | `25X Cross` |
| `407` | `0xed48...7c9b` | `SHORT` | 5,990,054.41 USD | `2,551.13` | `2460.02` | `2349.90` | `3240.94` | 285,792.00 USD | `+4.77%` | `20X Cross` |
| `411` | `0x934d...92c9` | `LONG` | 5,869,000.00 USD | `2,500.00` | `2343.98` | `2349.90` | `2152.13` | 9,035.49 USD | `+0.15%` | `25X Cross` |
| `432` | `0xfbe2...c8ea` | `SHORT` | 5,644,772.33 USD | `2,404.08` | `2041.57` | `2349.90` | `2712.52` | -736,679.60 USD | `-13.05%` | `20X Cross` |
| `441` | `0x1c98...7fc7` | `LONG` | 5,538,245.17 USD | `2,358.00` | `2467.15` | `2349.90` | `1897.18` | -279,326.31 USD | `-5.04%` | `10X Cross` |
| `460` | `0x6859...7e1e` | `SHORT` | 5,233,099.64 USD | `2,224.58` | `2200.39` | `2349.90` | `3600.75` | -338,146.91 USD | `-6.46%` | `25X Cross` |
| `469` | `0xd507...c948` | `SHORT` | 5,099,855.77 USD | `2,172.00` | `2387.49` | `2349.90` | `2707.38` | 85,785.26 USD | `+1.68%` | `5X Isolated` |
| `474` | `0xb829...3a81` | `LONG` | 5,058,890.77 USD | `2,153.91` | `2537.61` | `2349.90` | `794.11` | -406,905.97 USD | `-8.04%` | `20X Cross` |
| `507` | `0xd4c1...3d1d` | `SHORT` | 4,707,672.17 USD | `2,003.35` | `2336.05` | `2349.90` | `4561.96` | -27,731.49 USD | `-0.59%` | `12X Cross` |
| `509` | `0xf929...d1f9` | `SHORT` | 4,699,000.00 USD | `2,000.00` | `2423.37` | `2349.90` | `2548.78` | 147,740.34 USD | `+3.14%` | `25X Cross` |
| `510` | `0x3440...32c5` | `SHORT` | 4,697,327.09 USD | `2,000.57` | `2198.21` | `2349.90` | `3510.29` | -299,663.96 USD | `-6.38%` | `25X Cross` |
| `521` | `0x0514...bdfe` | `SHORT` | 4,581,720.00 USD | `1,950.00` | `1988.74` | `2349.90` | `2928.52` | -703,660.37 USD | `-15.36%` | `25X Cross` |
| `530` | `0x8376...9a1e` | `SHORT` | 4,493,486.59 USD | `1,910.50` | `2477.72` | `2349.90` | `3152.64` | 240,201.58 USD | `+5.35%` | `20X Cross` |
| `550` | `0x7a6d...f79c` | `SHORT` | 4,288,189.17 USD | `1,825.07` | `2433.80` | `2349.90` | `2776.77` | 153,679.71 USD | `+3.58%` | `25X Cross` |
| `558` | `0x7265...91a5` | `LONG` | 4,239,258.14 USD | `1,801.87` | `2533.96` | `2349.90` | `1988.11` | -326,608.32 USD | `-7.70%` | `20X Cross` |
| `559` | `0x541e...071d` | `SHORT` | 4,238,140.00 USD | `1,805.00` | `2648.19` | `2349.90` | `2989.61` | 541,844.84 USD | `+12.78%` | `25X Cross` |
| `561` | `0x739c...cfb2` | `SHORT` | 4,230,540.00 USD | `1,800.00` | `2427.60` | `2349.90` | `2691.13` | 139,156.38 USD | `+3.29%` | `25X Cross` |
| `567` | `0xa445...329d` | `LONG` | 4,171,807.36 USD | `1,776.75` | `2398.85` | `2349.90` | `1783.02` | -90,362.00 USD | `-2.17%` | `25X Cross` |
| `571` | `0x91a9...3f70` | `SHORT` | 4,153,224.50 USD | `1,767.48` | `2156.23` | `2349.90` | `3620.61` | -342,120.42 USD | `-8.24%` | `4X Cross` |
| `578` | `0x3453...b323` | `SHORT` | 4,117,514.62 USD | `1,750.12` | `2328.82` | `2349.90` | `2400.80` | -41,782.48 USD | `-1.01%` | `25X Cross` |
| `603` | `0xfeec...4e9c` | `SHORT` | 3,971,859.52 USD | `1,691.81` | `2566.49` | `2349.90` | `2649.84` | 370,164.99 USD | `+9.32%` | `10X Cross` |
| `604` | `0x936c...bb0f` | `SHORT` | 3,968,243.23 USD | `1,688.69` | `2434.60` | `2349.90` | `8410.99` | 143,043.88 USD | `+3.60%` | `20X Cross` |
| `622` | `0xeee0...0b53` | `LONG` | 3,851,661.40 USD | `1,637.12` | `2468.64` | `2349.90` | `75.96` | -189,814.66 USD | `-4.93%` | `7X Cross` |
| `624` | `0xfc27...9d9d` | `SHORT` | 3,833,685.84 USD | `1,631.63` | `2402.17` | `2349.90` | `10928.76` | 85,777.15 USD | `+2.24%` | `25X Cross` |
| `625` | `0x982b...4606` | `LONG` | 3,827,413.06 USD | `1,626.82` | `2575.24` | `2349.90` | `1548.38` | -362,040.01 USD | `-9.46%` | `5X Isolated` |
| `627` | `0x27b8...12fc` | `LONG` | 3,824,421.55 USD | `1,628.12` | `2468.73` | `2349.90` | `404.16` | -194,973.08 USD | `-5.10%` | `10X Cross` |
| `632` | `0x73d7...8be1` | `LONG` | 3,763,283.78 USD | `1,601.47` | `2410.40` | `2349.90` | `2032.51` | -96,895.14 USD | `-2.57%` | `25X Cross` |
| `663` | `0xe170...9300` | `SHORT` | 3,600,576.54 USD | `1,533.40` | `2076.39` | `2349.90` | `3203.40` | -416,627.04 USD | `-11.57%` | `25X Cross` |
| `672` | `0x2e2b...2fab` | `LONG` | 3,544,898.49 USD | `1,507.38` | `2245.53` | `2349.90` | `1047.81` | 160,025.39 USD | `+4.51%` | `25X Cross` |
| `675` | `0x251f...6e5d` | `LONG` | 3,522,000.00 USD | `1,500.00` | `2346.68` | `2349.90` | `1567.89` | 1,969.51 USD | `+0.06%` | `20X Cross` |
| `691` | `0xad54...6203` | `LONG` | 3,423,953.16 USD | `1,458.18` | `2627.45` | `2349.90` | `2146.44` | -407,353.52 USD | `-11.90%` | `10X Isolated` |
| `698` | `0xef70...a84c` | `SHORT` | 3,387,128.68 USD | `1,442.74` | `2424.73` | `2349.90` | `3494.02` | 111,142.14 USD | `+3.28%` | `25X Cross` |
| `704` | `0x4b5f...0dd8` | `LONG` | 3,361,804.98 USD | `1,431.96` | `2339.45` | `2349.90` | `2148.67` | 11,812.03 USD | `+0.35%` | `10X Cross` |
| `705` | `0xbadb...9ee6` | `LONG` | 3,360,032.03 USD | `1,428.16` | `1936.00` | `2349.90` | `1023.01` | 595,110.39 USD | `+17.71%` | `20X Cross` |
| `764` | `0x880a...311c` | `SHORT` | 3,101,864.17 USD | `1,320.22` | `2425.76` | `2349.90` | `8032.74` | 100,684.98 USD | `+3.25%` | `9X Cross` |
| `774` | `0x29de...3e93` | `LONG` | 3,078,238.00 USD | `1,310.00` | `2352.60` | `2349.90` | `1922.20` | -3,670.82 USD | `-0.12%` | `5X Isolated` |
| `785` | `0x023a...2355` | `LONG` | 3,050,954.83 USD | `1,298.33` | `2341.05` | `2349.90` | `0.000000` | 11,486.29 USD | `+0.38%` | `25X Cross` |
| `816` | `0xc435...c905` | `SHORT` | 2,929,867.20 USD | `1,248.00` | `2704.38` | `2349.90` | `4757.06` | 445,203.15 USD | `+15.20%` | `20X Cross` |
| `823` | `0x4202...aaf5` | `SHORT` | 2,895,322.13 USD | `1,232.10` | `2321.73` | `2349.90` | `2733.52` | -34,697.83 USD | `-1.20%` | `5X Isolated` |
| `833` | `0x7178...0854` | `LONG` | 2,861,468.63 USD | `1,218.63` | `2461.81` | `2349.90` | `1029.11` | -138,577.78 USD | `-4.84%` | `10X Cross` |
| `880` | `0x07fd...689d` | `LONG` | 2,667,433.03 USD | `1,135.90` | `2423.84` | `2349.90` | `0.000000` | -85,810.17 USD | `-3.22%` | `25X Cross` |
| `913` | `0x2f80...f203` | `SHORT` | 2,557,595.96 USD | `1,088.94` | `1984.00` | `2349.90` | `3075.18` | -397,128.77 USD | `-15.53%` | `20X Cross` |
| `924` | `0x6f11...0389` | `SHORT` | 2,533,168.30 USD | `1,079.00` | `2333.39` | `2349.90` | `3199.65` | -15,439.39 USD | `-0.61%` | `25X Cross` |
| `925` | `0x2b61...2f6c` | `SHORT` | 2,528,711.50 USD | `1,076.60` | `2681.75` | `2349.90` | `6431.06` | 358,461.24 USD | `+14.18%` | `10X Cross` |
| `963` | `0x1b2a...f7a6` | `LONG` | 2,412,383.29 USD | `1,025.37` | `2737.51` | `2349.90` | `922.99` | -394,576.64 USD | `-16.36%` | `10X Cross` |
| `964` | `0xb15b...dbae` | `SHORT` | 2,408,471.43 USD | `1,025.14` | `2338.37` | `2349.90` | `2381.04` | -11,297.72 USD | `-0.47%` | `25X Cross` |
| `971` | `0x6749...ce07` | `SHORT` | 2,383,627.68 USD | `1,015.35` | `2318.56` | `2349.90` | `5884.21` | -29,484.32 USD | `-1.24%` | `20X Cross` |
| `975` | `0x02aa...1806` | `SHORT` | 2,366,483.81 USD | `1,007.10` | `2654.68` | `2349.90` | `3613.65` | 307,048.29 USD | `+12.97%` | `20X Cross` |
| `976` | `0x001a...fef6` | `SHORT` | 2,364,796.17 USD | `1,007.33` | `2022.19` | `2349.90` | `3028.04` | -327,788.21 USD | `-13.86%` | `10X Cross` |
| `981` | `0xdb3a...cf3b` | `LONG` | 2,357,354.84 USD | `1,003.22` | `2705.01` | `2349.90` | `0.000000` | -356,352.05 USD | `-15.12%` | `4X Cross` |
| `984` | `0xdf60...d3c7` | `LONG` | 2,351,700.00 USD | `1,000.00` | `2736.24` | `2349.90` | `2246.05` | -384,542.88 USD | `-16.35%` | `10X Isolated` |
| `986` | `0x004e...1bb8` | `SHORT` | 2,349,800.00 USD | `1,000.00` | `2363.71` | `2349.90` | `2423.03` | 13,910.06 USD | `+0.59%` | `25X Cross` |
| `987` | `0x5986...89d9` | `LONG` | 2,348,700.00 USD | `1,000.00` | `2346.34` | `2349.90` | `1198.30` | 2,350.46 USD | `+0.10%` | `25X Cross` |
| `990` | `0x2828...93a0` | `LONG` | 2,348,100.00 USD | `1,000.00` | `2393.30` | `2349.90` | `2261.77` | -45,209.16 USD | `-1.93%` | `25X Cross` |
| `991` | `0xfe82...ce65` | `SHORT` | 2,347,700.00 USD | `1,000.00` | `2300.50` | `2349.90` | `2718.39` | -47,192.07 USD | `-2.01%` | `25X Cross` |
| `992` | `0x4044...794c` | `LONG` | 2,347,650.00 USD | `1,000.00` | `2332.68` | `2349.90` | `0.000000` | 14,960.16 USD | `+0.64%` | `25X Cross` |
| `993` | `0x5272...fcd9` | `SHORT` | 2,347,600.00 USD | `1,000.00` | `2241.82` | `2349.90` | `2880.72` | -105,775.51 USD | `-4.51%` | `5X Cross` |
| `1024` | `0xb002...ed8a` | `SHORT` | 2,262,061.01 USD | `962.78` | `2299.66` | `2349.90` | `4192.08` | -47,983.10 USD | `-2.12%` | `25X Cross` |
| `1027` | `0x2e30...4cb5` | `SHORT` | 2,254,544.58 USD | `959.54` | `2340.09` | `2349.90` | `7121.13` | -9,117.50 USD | `-0.40%` | `2X Cross` |
| `1043` | `0xc8fe...afa4` | `LONG` | 2,200,286.46 USD | `936.37` | `2331.34` | `2349.90` | `2145.78` | 17,282.22 USD | `+0.79%` | `10X Isolated` |
| `1057` | `0x9606...4e5d` | `SHORT` | 2,143,807.55 USD | `913.00` | `2478.70` | `2349.90` | `3857.94` | 119,246.05 USD | `+5.56%` | `20X Cross` |
| `1063` | `0xaeea...bfa7` | `LONG` | 2,133,372.81 USD | `908.75` | `2339.31` | `2349.90` | `2286.69` | 7,530.71 USD | `+0.35%` | `23X Isolated` |
| `1093` | `0x60f7...d1ee` | `LONG` | 2,089,987.00 USD | `890.00` | `2343.49` | `2349.90` | `2266.03` | 4,277.04 USD | `+0.20%` | `25X Cross` |
| `1172` | `0x2577...4897` | `LONG` | 1,973,798.40 USD | `840.06` | `2357.55` | `2349.90` | `0.000000` | -6,684.88 USD | `-0.34%` | `15X Cross` |
| `1175` | `0xcd27...52a8` | `LONG` | 1,967,272.06 USD | `837.21` | `2553.56` | `2349.90` | `1404.20` | -170,592.71 USD | `-8.67%` | `2X Cross` |
| `1230` | `0x3fc5...c0c1` | `SHORT` | 1,890,248.05 USD | `804.26` | `2702.11` | `2349.90` | `4748.51` | 282,953.48 USD | `+14.97%` | `25X Cross` |
| `1235` | `0xf83f...625f` | `SHORT` | 1,887,085.55 USD | `803.05` | `2601.00` | `2349.90` | `6021.47` | 201,650.90 USD | `+10.69%` | `20X Cross` |
| `1238` | `0x04a9...95aa` | `LONG` | 1,879,840.00 USD | `800.00` | `2595.13` | `2349.90` | `1855.31` | -196,266.74 USD | `-10.44%` | `5X Cross` |
| `1239` | `0x7737...bf66` | `SHORT` | 1,877,991.36 USD | `799.79` | `2494.83` | `2349.90` | `25734.58` | 117,354.67 USD | `+6.25%` | `15X Cross` |
| `1259` | `0xbef3...0d3e` | `LONG` | 1,837,442.23 USD | `780.99` | `2332.46` | `2349.90` | `2092.90` | 15,800.98 USD | `+0.86%` | `20X Cross` |
| `1270` | `0x6a41...a3b9` | `LONG` | 1,821,877.05 USD | `776.06` | `2332.17` | `2349.90` | `2095.12` | 11,972.19 USD | `+0.66%` | `20X Cross` |
| `1274` | `0x458d...ab3b` | `LONG` | 1,818,834.79 USD | `774.75` | `2740.41` | `2349.90` | `1887.95` | -304,294.39 USD | `-16.73%` | `3X Isolated` |
| `1316` | `0x4b1c...bc38` | `SHORT` | 1,743,164.64 USD | `742.51` | `2529.31` | `2349.90` | `4405.99` | 134,890.91 USD | `+7.74%` | `10X Cross` |
| `1347` | `0x51a0...3543` | `SHORT` | 1,701,016.17 USD | `724.55` | `2627.71` | `2349.90` | `7721.37` | 202,880.58 USD | `+11.93%` | `20X Cross` |
| `1358` | `0xa189...94d7` | `SHORT` | 1,690,726.69 USD | `719.98` | `2691.84` | `2349.90` | `3051.90` | 247,345.98 USD | `+14.63%` | `25X Cross` |
| `1365` | `0x3ee5...4fab` | `SHORT` | 1,679,912.74 USD | `715.17` | `2759.35` | `2349.90` | `3531.89` | 293,487.22 USD | `+17.47%` | `20X Cross` |
| `1373` | `0x2f93...4404` | `LONG` | 1,662,275.04 USD | `707.47` | `1700.45` | `2349.90` | `1369.58` | 459,248.66 USD | `+27.63%` | `4X Isolated` |
| `1386` | `0x5605...fe0f` | `SHORT` | 1,649,335.32 USD | `702.14` | `2566.90` | `2349.90` | `3032.03` | 152,997.33 USD | `+9.28%` | `20X Cross` |
| `1390` | `0xaa53...9cb7` | `LONG` | 1,643,320.00 USD | `700.00` | `2394.46` | `2349.90` | `1960.34` | -32,802.07 USD | `-2.00%` | `20X Cross` |
| `1439` | `0xdbd1...29dd` | `SHORT` | 1,599,582.80 USD | `680.70` | `3030.57` | `2349.90` | `4068.87` | 463,338.32 USD | `+28.97%` | `6X Cross` |
| `1446` | `0x71e5...be04` | `LONG` | 1,590,890.58 USD | `677.67` | `2727.27` | `2349.90` | `1471.73` | -257,295.03 USD | `-16.17%` | `20X Cross` |
| `1450` | `0x0b23...f37b` | `LONG` | 1,585,440.00 USD | `675.00` | `2238.15` | `2349.90` | `576.06` | 74,683.36 USD | `+4.71%` | `5X Cross` |
| `1476` | `0x0cac...6170` | `SHORT` | 1,555,748.75 USD | `662.50` | `2146.55` | `2349.90` | `2835.36` | -133,653.76 USD | `-8.59%` | `20X Cross` |
| `1478` | `0x0082...1ae3` | `LONG` | 1,552,782.00 USD | `660.00` | `2448.58` | `2349.90` | `2244.93` | -63,286.64 USD | `-4.08%` | `25X Cross` |
| `1506` | `0x7743...e4fe` | `SHORT` | 1,527,310.79 USD | `650.56` | `2325.23` | `2349.90` | `6449.04` | -14,616.66 USD | `-0.96%` | `25X Cross` |
| `1515` | `0xffb2...5ed6` | `SHORT` | 1,505,225.29 USD | `640.77` | `2672.96` | `2349.90` | `2595.20` | 207,523.06 USD | `+13.79%` | `20X Cross` |
| `1523` | `0xb1ec...e86a` | `SHORT` | 1,494,018.29 USD | `636.38` | `2357.26` | `2349.90` | `18358.55` | 6,086.41 USD | `+0.41%` | `25X Cross` |
| `1556` | `0xfce0...f4c0` | `SHORT` | 1,463,994.54 USD | `623.60` | `3129.61` | `2349.90` | `2788.39` | 487,632.04 USD | `+33.31%` | `20X Cross` |
| `1577` | `0x7663...cb5a` | `SHORT` | 1,441,752.48 USD | `613.54` | `2342.35` | `2349.90` | `3618.80` | -4,631.99 USD | `-0.32%` | `3X Cross` |
| `1598` | `0xa0fb...96be` | `SHORT` | 1,416,314.08 USD | `602.82` | `2334.83` | `2349.90` | `3862.74` | -8,841.12 USD | `-0.62%` | `3X Cross` |
| `1606` | `0x26e6...6b28` | `LONG` | 1,410,180.00 USD | `600.00` | `1769.78` | `2349.90` | `2005.45` | 348,308.47 USD | `+24.70%` | `20X Cross` |
| `1607` | `0xad02...eb65` | `LONG` | 1,410,076.04 USD | `600.62` | `2460.69` | `2349.90` | `1079.65` | -67,864.52 USD | `-4.81%` | `5X Cross` |
| `1609` | `0x638f...f5f0` | `LONG` | 1,408,980.00 USD | `600.00` | `4011.50` | `2349.90` | `0.000000` | -997,923.53 USD | `-70.83%` | `25X Cross` |
| `1610` | `0x67c3...609d` | `SHORT` | 1,408,860.00 USD | `600.00` | `2386.55` | `2349.90` | `2560.74` | 23,071.89 USD | `+1.64%` | `25X Cross` |
| `1611` | `0x0deb...0bc5` | `LONG` | 1,408,560.00 USD | `600.00` | `2038.23` | `2349.90` | `1478.66` | 185,621.36 USD | `+13.18%` | `20X Cross` |
| `1612` | `0x0a84...6ddd` | `LONG` | 1,408,560.00 USD | `600.00` | `2222.36` | `2349.90` | `1774.77` | 75,141.66 USD | `+5.33%` | `25X Cross` |
| `1634` | `0x3bca...66f3` | `SHORT` | 1,379,623.56 USD | `587.17` | `2348.07` | `2349.90` | `15435.60` | -894.40 USD | `-0.06%` | `25X Cross` |
| `1635` | `0x94b6...e5b3` | `SHORT` | 1,378,709.83 USD | `586.71` | `2377.90` | `2349.90` | `2509.54` | 16,428.41 USD | `+1.19%` | `25X Cross` |
| `1674` | `0xfb99...37f3` | `LONG` | 1,327,223.03 USD | `565.34` | `2362.35` | `2349.90` | `1205.63` | -8,313.32 USD | `-0.63%` | `3X Cross` |
| `1687` | `0x844b...7f42` | `SHORT` | 1,318,854.90 USD | `561.00` | `2026.17` | `2349.90` | `2947.36` | -182,171.49 USD | `-13.81%` | `25X Cross` |
| `1704` | `0xabe6...1d99` | `SHORT` | 1,305,497.39 USD | `556.00` | `2484.68` | `2349.90` | `2931.95` | 75,998.50 USD | `+5.82%` | `20X Cross` |
| `1751` | `0xad21...fb6a` | `LONG` | 1,248,616.37 USD | `531.87` | `2574.89` | `2349.90` | `1681.05` | -120,889.13 USD | `-9.68%` | `7X Cross` |
| `1793` | `0x8923...1bac` | `SHORT` | 1,214,191.70 USD | `517.18` | `2348.15` | `2349.90` | `3224.56` | 233.40 USD | `+0.02%` | `25X Cross` |
| `1814` | `0x0c7a...2f50` | `SHORT` | 1,195,504.27 USD | `509.25` | `2122.56` | `2349.90` | `4062.52` | -114,598.84 USD | `-9.59%` | `20X Cross` |
| `1834` | `0x89b2...9ca6` | `LONG` | 1,174,800.00 USD | `500.00` | `2484.03` | `2349.90` | `1954.18` | -67,219.35 USD | `-5.72%` | `25X Cross` |
| `1837` | `0x0e1c...ce6d` | `LONG` | 1,173,850.00 USD | `500.00` | `2329.15` | `2349.90` | `1997.70` | 9,273.27 USD | `+0.79%` | `15X Cross` |
| `1840` | `0x7298...7d6c` | `SHORT` | 1,169,480.20 USD | `498.15` | `3426.75` | `2349.90` | `5422.36` | 537,555.62 USD | `+45.97%` | `20X Cross` |
| `1863` | `0x404c...5f03` | `SHORT` | 1,150,799.54 USD | `489.79` | `2671.94` | `2349.90` | `4148.23` | 157,880.02 USD | `+13.72%` | `20X Cross` |
| `1864` | `0xc10f...23b3` | `LONG` | 1,150,569.00 USD | `490.00` | `2402.16` | `2349.90` | `2082.02` | -26,493.83 USD | `-2.30%` | `25X Cross` |
| `1867` | `0x321f...1c84` | `SHORT` | 1,148,056.23 USD | `488.02` | `2370.09` | `2349.90` | `3011.35` | 8,588.37 USD | `+0.75%` | `10X Cross` |
| `1934` | `0x82c6...fe42` | `LONG` | 1,087,013.75 USD | `462.50` | `2501.38` | `2349.90` | `2054.43` | -69,876.82 USD | `-6.43%` | `5X Isolated` |
| `1949` | `0x617e...0f97` | `SHORT` | 1,074,858.99 USD | `457.85` | `2205.60` | `2349.90` | `3604.34` | -65,015.15 USD | `-6.05%` | `10X Cross` |
| `1980` | `0xae55...2236` | `LONG` | 1,056,735.00 USD | `450.00` | `2510.21` | `2349.90` | `0.000000` | -72,862.50 USD | `-6.90%` | `25X Cross` |
| `1989` | `0xac26...a9c7` | `SHORT` | 1,047,858.16 USD | `446.28` | `2192.58` | `2349.90` | `8655.92` | -69,358.46 USD | `-6.62%` | `20X Cross` |
| `1995` | `0x53f8...ceff` | `LONG` | 1,046,129.25 USD | `445.60` | `2399.81` | `2349.90` | `0.000000` | -23,221.35 USD | `-2.22%` | `20X Cross` |
| `1997` | `0xd8a1...6687` | `LONG` | 1,037,425.94 USD | `441.53` | `2804.24` | `2349.90` | `2150.99` | -200,742.50 USD | `-19.35%` | `20X Cross` |
| `2015` | `0x248e...6be2` | `SHORT` | 1,025,094.44 USD | `436.40` | `2314.49` | `2349.90` | `4355.81` | -15,059.72 USD | `-1.47%` | `20X Cross` |
| `2020` | `0x80f2...0c3a` | `LONG` | 1,020,312.13 USD | `434.55` | `2564.17` | `2349.90` | `905.26` | -93,936.75 USD | `-9.21%` | `5X Cross` |
| `2048` | `0x15c8...045f` | `SHORT` | 1,006,923.60 USD | `428.90` | `1903.23` | `2349.90` | `3081.78` | -190,630.55 USD | `-18.93%` | `25X Cross` |
| `2054` | `0x4e6b...b7d4` | `LONG` | 1,005,181.47 USD | `427.77` | `2744.83` | `2349.90` | `70.81` | -168,983.56 USD | `-16.81%` | `25X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `2347.90` | 95,925.80 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 95.93K USD at 2347.9000 USD [API] | `2026-10-27 19:42:43` |
| `ANNOUNCEMENT` | `INFO` | `2350.40` | 65,403.88 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 65.40K USD at 2350.4000 USD [API] | `2026-10-27 19:45:02` |
| `ANNOUNCEMENT` | `INFO` | `2346.40` | 123,113.26 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 123.11K USD at 2346.4000 USD [API] | `2026-10-27 15:21:36` |
| `ANNOUNCEMENT` | `INFO` | `2346.30` | 195,447.73 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 195.45K USD at 2346.3000 USD [API] | `2026-10-27 15:21:36` |
| `ANNOUNCEMENT` | `INFO` | `2346.90` | 154,024.23 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 154.02K USD at 2346.9000 USD [API] | `2026-10-27 15:21:33` |
| `ANNOUNCEMENT` | `INFO` | `2346.80` | 87,619.19 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 87.62K USD at 2346.8000 USD [API] | `2026-10-27 15:21:33` |
| `ANNOUNCEMENT` | `INFO` | `2346.70` | 18,067.24 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 18.07K USD at 2346.7000 USD [API] | `2026-10-27 15:21:33` |
| `ANNOUNCEMENT` | `INFO` | `2346.70` | 19,043.47 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 19.04K USD at 2346.7000 USD [API] | `2026-10-27 15:21:33` |
| `ANNOUNCEMENT` | `INFO` | `2340.40` | 61,587.86 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 61.59K USD at 2340.4000 USD [API] | `2026-10-27 20:41:16` |
| `ANNOUNCEMENT` | `INFO` | `2340.50` | 58,665.57 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 58.67K USD at 2340.5000 USD [API] | `2026-10-27 20:41:16` |
| `ANNOUNCEMENT` | `INFO` | `2346.30` | 58,810.95 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 58.81K USD at 2346.3000 USD [API] | `2026-10-27 15:21:36` |
| `ANNOUNCEMENT` | `INFO` | `2346.40` | 44,237.38 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 44.24K USD at 2346.4000 USD [API] | `2026-10-27 15:21:36` |
| `ANNOUNCEMENT` | `INFO` | `2346.90` | 111,487.61 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 111.49K USD at 2346.9000 USD [API] | `2026-10-27 15:21:33` |
| `ANNOUNCEMENT` | `INFO` | `2344.10` | 119,932.36 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 119.93K USD at 2344.1000 USD [API] | `2026-10-27 20:56:13` |
| `ANNOUNCEMENT` | `INFO` | `2343.50` | 58,830.52 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 58.83K USD at 2343.5000 USD [API] | `2026-10-27 20:58:00` |
| `ANNOUNCEMENT` | `INFO` | `2343.50` | 40,058.15 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 40.06K USD at 2343.5000 USD [API] | `2026-10-27 20:58:17` |
| `ANNOUNCEMENT` | `INFO` | `2360.00` | 40,054.63 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 40.05K USD at 2360.0000 USD [API] | `2026-10-27 21:35:10` |
| `ANNOUNCEMENT` | `INFO` | `2363.80` | 1,243.36 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.24K USD at 2363.8000 USD [API] | `2026-10-27 21:33:40` |
| `ANNOUNCEMENT` | `INFO` | `2363.80` | 364.50 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.36K USD at 2363.8000 USD [API] | `2026-10-27 21:33:40` |
| `ANNOUNCEMENT` | `INFO` | `2354.60` | 47,096.24 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 47.10K USD at 2354.6000 USD [API] | `2026-10-27 21:41:06` |
| `ANNOUNCEMENT` | `INFO` | `2346.30` | 406,136.08 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 406.14K USD at 2346.3000 USD [API] | `2026-10-27 15:21:36` |
| `ANNOUNCEMENT` | `INFO` | `2355.20` | 40,978.60 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 40.98K USD at 2355.2000 USD [API] | `2026-10-27 21:52:05` |
| `ANNOUNCEMENT` | `INFO` | `2362.30` | 10,820.99 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 10.82K USD at 2362.3000 USD [API] | `2026-10-27 21:33:37` |
| `ANNOUNCEMENT` | `INFO` | `2357.80` | 212,571.94 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 212.57K USD at 2357.8000 USD [API] | `2026-10-27 21:33:15` |
| `ANNOUNCEMENT` | `INFO` | `2357.60` | 133,550.02 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 133.55K USD at 2357.6000 USD [API] | `2026-10-27 21:33:15` |
| `ANNOUNCEMENT` | `INFO` | `2357.60` | 212,553.91 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 212.55K USD at 2357.6000 USD [API] | `2026-10-27 21:33:15` |
| `ANNOUNCEMENT` | `INFO` | `2357.80` | 13,323.46 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 13.32K USD at 2357.8000 USD [API] | `2026-10-27 21:33:15` |
| `ANNOUNCEMENT` | `INFO` | `2346.40` | 24,840.87 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 24.84K USD at 2346.4000 USD [API] | `2026-10-27 15:21:36` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`2401.93` (Vol: 17,300,000.00 USD, Dist: `+2.22%`) | Long MP=`2284.33` (Vol: 27,300,000.00 USD, Dist: `--2.79%`)
  * 48H Horizon: Short MP=`2401.93` (Vol: 25,300,000.00 USD, Dist: `+2.22%`) | Long MP=`2284.33` (Vol: 30,000,000.00 USD, Dist: `--2.79%`)
  * 3D Horizon: Short MP=`2401.93` (Vol: 26,700,000.00 USD, Dist: `+2.22%`) | Long MP=`2286.29` (Vol: 37,900,000.00 USD, Dist: `--2.71%`)
  * 7D Horizon: Short MP=`2402.93` (Vol: 47,100,000.00 USD, Dist: `+2.26%`) | Long MP=`2284.60` (Vol: 72,300,000.00 USD, Dist: `--2.78%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `475.00` | 8,640.00 USD | 882,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.00` | 25,130.00 USD | 882,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `495.00` | 9,510.00 USD | 882,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.00` | 28,840.00 USD | 882,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.00` | 3,560.00 USD | 882,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.00` | 131,920.00 USD | 882,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.00` | 13,230.00 USD | 882,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.00` | 11,150.00 USD | 882,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.00` | 6,170.00 USD | 882,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `565.00` | 37,290.00 USD | 882,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `575.00` | 389,040.00 USD | 882,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.00` | 38,780.00 USD | 882,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.00` | 242.82 USD | 882,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `605.00` | 8,760.00 USD | 882,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.00` | 149,310.00 USD | 882,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.00` | 10,570.00 USD | 881,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.00` | 44,080.00 USD | 881,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `645.00` | 3,870.00 USD | 881,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `655.00` | 27,600.00 USD | 881,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `665.00` | 109,500.00 USD | 881,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `675.00` | 14,570.00 USD | 881,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `685.00` | 26,520.00 USD | 881,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `695.00` | 429,090.00 USD | 881,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `705.00` | 79,880.00 USD | 881,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `715.00` | 722.15 USD | 881,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `725.00` | 470,870.00 USD | 881,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `735.00` | 58,800.00 USD | 880,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `745.00` | 73,890.00 USD | 880,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `755.00` | 66,360.00 USD | 880,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `765.00` | 451,170.00 USD | 880,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `775.00` | 14,600.00 USD | 880,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `785.00` | 33,390.00 USD | 880,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `795.00` | 674.16 USD | 879,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `805.00` | 1,800,000.00 USD | 879,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `815.00` | 80,080.00 USD | 878,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `825.00` | 3,630,000.00 USD | 878,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `835.00` | 19,570.00 USD | 874,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `845.00` | 8,950.00 USD | 874,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `855.00` | 12,910.00 USD | 874,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `865.00` | 70,390.00 USD | 874,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `875.00` | 177,240.00 USD | 874,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `885.00` | 6,380.00 USD | 874,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `895.00` | 946,640.00 USD | 874,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `905.00` | 402,930.00 USD | 873,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `915.00` | 166,450.00 USD | 872,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `925.00` | 1,100,000.00 USD | 872,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `935.00` | 201,350.00 USD | 871,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `945.00` | 12,960.00 USD | 871,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `955.00` | 60,890.00 USD | 871,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `965.00` | 22,700.00 USD | 871,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `975.00` | 165,100.00 USD | 871,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `985.00` | 8,010.00 USD | 871,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `995.00` | 6,990,000.00 USD | 871,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1005.00` | 34,900.00 USD | 864,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1015.00` | 1,260,000.00 USD | 864,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1025.00` | 1,640,000.00 USD | 862,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1035.00` | 66,460.00 USD | 861,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1045.00` | 1,980,000.00 USD | 861,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1055.00` | 227,570.00 USD | 859,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1065.00` | 196,890.00 USD | 858,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1075.00` | 663,910.00 USD | 858,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1085.00` | 148,710.00 USD | 858,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1095.00` | 74,350.00 USD | 857,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1105.00` | 188,810.00 USD | 857,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1115.00` | 110,610.00 USD | 857,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1125.00` | 80,330.00 USD | 857,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1135.00` | 202,010.00 USD | 857,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1145.00` | 379,510.00 USD | 857,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1155.00` | 10,750,000.00 USD | 856,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1165.00` | 61,630.00 USD | 846,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1175.00` | 124,720.00 USD | 846,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1185.00` | 1,500,000.00 USD | 845,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1195.00` | 293,100.00 USD | 844,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1205.00` | 981,950.00 USD | 844,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1215.00` | 119,890.00 USD | 843,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1225.00` | 943,680.00 USD | 843,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1235.00` | 263,310.00 USD | 842,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1245.00` | 520,710.00 USD | 841,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1255.00` | 342,100.00 USD | 841,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1265.00` | 361,680.00 USD | 840,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1275.00` | 73,580.00 USD | 840,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1285.00` | 15,600,000.00 USD | 840,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1295.00` | 281,140.00 USD | 824,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1305.00` | 248,940.00 USD | 824,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1315.00` | 211,340.00 USD | 824,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1325.00` | 449,550.00 USD | 824,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1335.00` | 458,220.00 USD | 823,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1345.00` | 432,360.00 USD | 823,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1355.00` | 6,750,000.00 USD | 822,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1365.00` | 1,110,000.00 USD | 816,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1375.00` | 22,060,000.00 USD | 814,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1385.00` | 290,680.00 USD | 792,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1395.00` | 166,060.00 USD | 792,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1405.00` | 10,170,000.00 USD | 792,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1415.00` | 64,340.00 USD | 782,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1425.00` | 1,480,000.00 USD | 782,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1435.00` | 245,940.00 USD | 780,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1445.00` | 15,020,000.00 USD | 780,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1455.00` | 110,950.00 USD | 765,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1465.00` | 442,100.00 USD | 765,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1475.00` | 2,320,000.00 USD | 764,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1485.00` | 299,770.00 USD | 762,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1495.00` | 4,610,000.00 USD | 762,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1505.00` | 95,120.00 USD | 757,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1515.00` | 25,280,000.00 USD | 757,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1525.00` | 18,440,000.00 USD | 732,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1535.00` | 726,900.00 USD | 713,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1545.00` | 4,940,000.00 USD | 713,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1555.00` | 388,160.00 USD | 708,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1565.00` | 142,630.00 USD | 707,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1575.00` | 6,160,000.00 USD | 707,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1585.00` | 307,140.00 USD | 701,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1595.00` | 1,550,000.00 USD | 701,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1605.00` | 18,410,000.00 USD | 699,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1615.00` | 768,060.00 USD | 681,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1625.00` | 207,400.00 USD | 680,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1635.00` | 18,750,000.00 USD | 680,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1645.00` | 36,560,000.00 USD | 661,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1655.00` | 1,390,000.00 USD | 624,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1665.00` | 738,370.00 USD | 623,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1675.00` | 12,750,000.00 USD | 622,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1685.00` | 1,930,000.00 USD | 610,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1695.00` | 11,130,000.00 USD | 608,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1705.00` | 1,660,000.00 USD | 597,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1715.00` | 319,600.00 USD | 595,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1725.00` | 18,430,000.00 USD | 595,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1735.00` | 18,400,000.00 USD | 576,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1745.00` | 1,050,000.00 USD | 558,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1755.00` | 709,580.00 USD | 557,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1765.00` | 4,190,000.00 USD | 556,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1775.00` | 1,460,000.00 USD | 552,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1785.00` | 54,280,000.00 USD | 550,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1795.00` | 1,150,000.00 USD | 496,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1805.00` | 9,830,000.00 USD | 495,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1815.00` | 1,840,000.00 USD | 485,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1825.00` | 531,360.00 USD | 483,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1835.00` | 5,740,000.00 USD | 483,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1845.00` | 13,680,000.00 USD | 477,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1855.00` | 2,470,000.00 USD | 463,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1865.00` | 966,690.00 USD | 461,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1875.00` | 5,580,000.00 USD | 460,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1885.00` | 2,940,000.00 USD | 454,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1895.00` | 20,370,000.00 USD | 451,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1905.00` | 941,710.00 USD | 431,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1915.00` | 13,210,000.00 USD | 430,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1925.00` | 2,910,000.00 USD | 417,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1935.00` | 1,360,000.00 USD | 414,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1945.00` | 1,750,000.00 USD | 413,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1955.00` | 8,060,000.00 USD | 411,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1965.00` | 900,710.00 USD | 403,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1975.00` | 1,250,000.00 USD | 402,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1985.00` | 4,420,000.00 USD | 401,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1995.00` | 2,050,000.00 USD | 396,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2005.00` | 1,820,000.00 USD | 394,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2015.00` | 2,640,000.00 USD | 392,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2025.00` | 1,760,000.00 USD | 390,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2035.00` | 3,700,000.00 USD | 388,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2045.00` | 16,870,000.00 USD | 384,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2055.00` | 4,130,000.00 USD | 367,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2065.00` | 1,390,000.00 USD | 363,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2068.70` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 1,890,000.00 USD | 1,910,000.00 USD | 939,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2071.50` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 2,760,000.00 USD | 1,510,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2074.30` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 3,850,000.00 USD | 2,610,000.00 USD | 2,930,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 13,750,000.00 USD | 362,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2077.10` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 4,430,000.00 USD | 4,120,000.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2079.90` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 3,400,000.00 USD | 3,020,000.00 USD | 2,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2082.70` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 2,420,000.00 USD | 1,860,000.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 1,810,000.00 USD | 348,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2085.50` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 3,840,000.00 USD | 1,860,000.00 USD | 3,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2088.30` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 2,280,000.00 USD | 1,820,000.00 USD | 907,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2091.10` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 4,280,000.00 USD | 952,210.00 USD | 6,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2093.90` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 5,200,000.00 USD | 1,640,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 4,620,000.00 USD | 346,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2096.70` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 1,940,000.00 USD | 3,330,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2099.50` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 1,880,000.00 USD | 1,520,000.00 USD | 2,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2102.30` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 125,250.00 USD | 688,260.00 USD | 2,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 23,040,000.00 USD | 342,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2105.10` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2107.90` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 2,320,000.00 USD | 356,360.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2110.70` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 2,830,000.00 USD | 2,300,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2111.30` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 1,250,000.00 USD | 343,530.00 USD | 525,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2113.50` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 1,730,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2113.90` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 1,090,000.00 USD | 1,080,000.00 USD | 363,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 16,720,000.00 USD | 319,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2116.30` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 1,480,000.00 USD | 2,030,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2116.50` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 1,240,000.00 USD | 335,670.00 USD | 859,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2119.10` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 507,030.00 USD | 201,150.00 USD | 917,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2119.10` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 3,390,000.00 USD | 935,590.00 USD | 2,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2121.70` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 982,960.00 USD | 759,970.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2121.90` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 2,300,000.00 USD | 973,690.00 USD | 1,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2124.30` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 957,510.00 USD | 1,040,000.00 USD | 525,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2124.70` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 2,110,000.00 USD | 983,790.00 USD | 989,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 1,140,000.00 USD | 302,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2126.90` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 308,590.00 USD | 840,990.00 USD | 629,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2127.50` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 1,080,000.00 USD | 2,620,000.00 USD | 3,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2129.50` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 107,010.00 USD | 453,880.00 USD | 318,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2130.30` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 2,040,000.00 USD | 2,130,000.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2132.10` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 956,330.00 USD | 336,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2133.10` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 1,930,000.00 USD | 715,940.00 USD | 330,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2134.70` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 187,520.00 USD | 185,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 15,440,000.00 USD | 301,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2135.90` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 1,370,000.00 USD | 596,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2137.30` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 236,290.00 USD | 544,840.00 USD | 208,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2138.70` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 909,440.00 USD | 1,250,000.00 USD | 78,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2139.90` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 319,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2141.50` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 1,750,000.00 USD | 199,980.00 USD | 776,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2142.50` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 295,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2144.30` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 465,960.00 USD | 1,540,000.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 16,180,000.00 USD | 285,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2145.10` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 16,700.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2147.10` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 311,920.00 USD | 32,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2147.70` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 251,250.00 USD | 11,090.00 USD | 207,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2149.90` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 459,630.00 USD | 482,820.00 USD | 537,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2152.70` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 58,340.00 USD | 681,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 2,580,000.00 USD | 269,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2155.50` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 191,860.00 USD | 454,940.00 USD | 866,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2158.30` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 738,850.00 USD | 717,210.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2161.10` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 1,490,000.00 USD | 1,350,000.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2163.90` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 36,870.00 USD | 329,690.00 USD | 409,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 1,660,000.00 USD | 266,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2166.70` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 25,540.00 USD | 0.00 USD | 68,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2169.50` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 1,700,000.00 USD | 726,240.00 USD | 810,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2172.30` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 479,540.00 USD | 1,150,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 109,510,000.00 USD | 265,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2185.00` | 113,580,000.00 USD | 155,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2194.70` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 141,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 1,210,000.00 USD | 42,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2197.50` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 2,440,000.00 USD | 3,270,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2199.70` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 201,540.00 USD | 154,560.00 USD | 80,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2200.30` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 3,000,000.00 USD | 3,140,000.00 USD | 3,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2202.30` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 82,940.00 USD | 62,930.00 USD | 220,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2203.10` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 3,240,000.00 USD | 624,500.00 USD | 2,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2204.90` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 1,050,000.00 USD | 207,110.00 USD | 716,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 1,160,000.00 USD | 41,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2205.90` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 6,050,000.00 USD | 4,010,000.00 USD | 3,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2207.50` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 3,100,000.00 USD | 2,380,000.00 USD | 3,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2208.70` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 10,060,000.00 USD | 6,100,000.00 USD | 4,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2210.10` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 1,610,000.00 USD | 1,180,000.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2211.50` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 7,320,000.00 USD | 7,940,000.00 USD | 7,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2212.70` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 2,200,000.00 USD | 1,180,000.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2214.30` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 13,980,000.00 USD | 12,380,000.00 USD | 9,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 2,240,000.00 USD | 39,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2215.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 5,950,000.00 USD | 5,220,000.00 USD | 5,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2217.10` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 16,020,000.00 USD | 10,300,000.00 USD | 8,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2217.90` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 4,610,000.00 USD | 4,240,000.00 USD | 1,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2219.90` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 12,620,000.00 USD | 10,310,000.00 USD | 3,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2220.50` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 3,450,000.00 USD | 4,220,000.00 USD | 680,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2222.70` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 5,480,000.00 USD | 5,400,000.00 USD | 8,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2223.10` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 5,770,000.00 USD | 3,810,000.00 USD | 2,870,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2225.00` | 1,560,000.00 USD | 37,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2225.50` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 12,980,000.00 USD | 13,620,000.00 USD | 9,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2225.70` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 3,700,000.00 USD | 5,870,000.00 USD | 2,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2228.30` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 4,150,000.00 USD | 1,310,000.00 USD | 766,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2228.30` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 7,790,000.00 USD | 5,070,000.00 USD | 7,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2230.90` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 3,630,000.00 USD | 2,460,000.00 USD | 3,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2231.10` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 9,590,000.00 USD | 3,450,000.00 USD | 17,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2233.50` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 6,590,000.00 USD | 3,820,000.00 USD | 2,280,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2233.90` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 18,230,000.00 USD | 10,390,000.00 USD | 6,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2235.00` | 789,970.00 USD | 36,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2236.10` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 2,630,000.00 USD | 2,440,000.00 USD | 3,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2236.70` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 7,440,000.00 USD | 11,700,000.00 USD | 5,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2238.70` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 1,620,000.00 USD | 2,160,000.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2239.50` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 6,630,000.00 USD | 6,820,000.00 USD | 6,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2241.30` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 321,680.00 USD | 220,800.00 USD | 39,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2242.30` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 3,580,000.00 USD | 2,780,000.00 USD | 7,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2243.90` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 2,480,000.00 USD | 423,680.00 USD | 483,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2245.00` | 4,680,000.00 USD | 35,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2245.10` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 16,710,000.00 USD | 13,060,000.00 USD | 11,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2246.50` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 883,930.00 USD | 788,500.00 USD | 1,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2247.90` | 2,090,000,000.00 USD | 2,090,000,000.00 USD | 13,600,000.00 USD | 6,160,000.00 USD | 9,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2249.10` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 4,190,000.00 USD | 1,420,000.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2250.70` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 10,570,000.00 USD | 10,360,000.00 USD | 8,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2251.70` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 4,500,000.00 USD | 6,550,000.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2253.50` | 2,030,000,000.00 USD | 2,030,000,000.00 USD | 24,760,000.00 USD | 21,020,000.00 USD | 19,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2254.30` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 7,670,000.00 USD | 3,590,000.00 USD | 5,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2255.00` | 13,270,000.00 USD | 30,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2256.30` | 1,970,000,000.00 USD | 1,970,000,000.00 USD | 31,260,000.00 USD | 19,100,000.00 USD | 18,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2256.90` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 5,660,000.00 USD | 5,380,000.00 USD | 4,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2259.10` | 1,900,000,000.00 USD | 1,900,000,000.00 USD | 22,390,000.00 USD | 19,400,000.00 USD | 22,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2259.50` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 13,310,000.00 USD | 6,270,000.00 USD | 8,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2261.90` | 1,840,000,000.00 USD | 1,840,000,000.00 USD | 48,180,000.00 USD | 29,390,000.00 USD | 21,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2262.10` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 15,090,000.00 USD | 12,940,000.00 USD | 13,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2264.70` | 965,430,000.00 USD | 965,430,000.00 USD | 15,200,000.00 USD | 12,030,000.00 USD | 6,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2264.70` | 1,740,000,000.00 USD | 1,740,000,000.00 USD | 30,320,000.00 USD | 28,050,000.00 USD | 19,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2265.00` | 3,530,000.00 USD | 17,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2267.30` | 931,600,000.00 USD | 931,600,000.00 USD | 5,460,000.00 USD | 10,030,000.00 USD | 3,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2267.50` | 1,660,000,000.00 USD | 1,660,000,000.00 USD | 40,120,000.00 USD | 40,100,000.00 USD | 31,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2269.90` | 912,990,000.00 USD | 912,990,000.00 USD | 14,410,000.00 USD | 11,130,000.00 USD | 8,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2270.30` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 39,480,000.00 USD | 27,490,000.00 USD | 39,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2272.50` | 879,220,000.00 USD | 879,220,000.00 USD | 14,080,000.00 USD | 10,950,000.00 USD | 10,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2273.10` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 33,160,000.00 USD | 25,760,000.00 USD | 19,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2275.00` | 4,430,000.00 USD | 13,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2275.10` | 844,130,000.00 USD | 844,130,000.00 USD | 9,170,000.00 USD | 15,450,000.00 USD | 4,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2275.90` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 48,240,000.00 USD | 42,710,000.00 USD | 44,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2277.70` | 815,280,000.00 USD | 815,280,000.00 USD | 16,430,000.00 USD | 8,710,000.00 USD | 18,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2278.70` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 74,310,000.00 USD | 34,750,000.00 USD | 42,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2280.30` | 772,080,000.00 USD | 772,080,000.00 USD | 24,350,000.00 USD | 14,020,000.00 USD | 8,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2281.50` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 56,100,000.00 USD | 59,940,000.00 USD | 49,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2282.90` | 725,680,000.00 USD | 725,680,000.00 USD | 22,370,000.00 USD | 16,300,000.00 USD | 19,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2284.30` | 911,260,000.00 USD | 911,260,000.00 USD | 89,220,000.00 USD | 69,840,000.00 USD | 44,200,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2285.00` | 5,990,000.00 USD | 9,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2285.50` | 667,930,000.00 USD | 667,930,000.00 USD | 28,040,000.00 USD | 29,600,000.00 USD | 19,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2287.10` | 708,000,000.00 USD | 708,000,000.00 USD | 58,910,000.00 USD | 53,380,000.00 USD | 45,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2288.10` | 590,420,000.00 USD | 590,420,000.00 USD | 19,180,000.00 USD | 14,490,000.00 USD | 4,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2289.90` | 550,520,000.00 USD | 550,520,000.00 USD | 48,430,000.00 USD | 34,490,000.00 USD | 22,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2290.70` | 552,030,000.00 USD | 552,030,000.00 USD | 12,440,000.00 USD | 7,760,000.00 USD | 2,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2292.70` | 445,420,000.00 USD | 445,420,000.00 USD | 38,110,000.00 USD | 20,900,000.00 USD | 44,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2293.30` | 528,890,000.00 USD | 528,890,000.00 USD | 18,860,000.00 USD | 18,460,000.00 USD | 15,490,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2295.00` | 1,460,000.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2295.50` | 342,350,000.00 USD | 342,350,000.00 USD | 17,510,000.00 USD | 8,110,000.00 USD | 7,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2295.90` | 476,090,000.00 USD | 476,090,000.00 USD | 23,870,000.00 USD | 15,930,000.00 USD | 7,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2298.30` | 309,500,000.00 USD | 309,500,000.00 USD | 2,090,000.00 USD | 5,410,000.00 USD | 301,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2298.50` | 429,080,000.00 USD | 429,080,000.00 USD | 8,010,000.00 USD | 7,220,000.00 USD | 3,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2301.10` | 410,610,000.00 USD | 410,610,000.00 USD | 17,170,000.00 USD | 11,820,000.00 USD | 13,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2301.10` | 301,700,000.00 USD | 301,700,000.00 USD | 11,790,000.00 USD | 2,200,000.00 USD | 7,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2303.70` | 368,300,000.00 USD | 368,300,000.00 USD | 29,770,000.00 USD | 15,890,000.00 USD | 10,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2303.90` | 280,130,000.00 USD | 280,130,000.00 USD | 32,960,000.00 USD | 17,020,000.00 USD | 13,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2305.00` | 280,710.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2306.30` | 311,960,000.00 USD | 311,960,000.00 USD | 4,970,000.00 USD | 5,530,000.00 USD | 15,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2306.70` | 216,870,000.00 USD | 216,870,000.00 USD | 0.00 USD | 3,740,000.00 USD | 10,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2308.90` | 286,120,000.00 USD | 286,120,000.00 USD | 642,440.00 USD | 1,990,000.00 USD | 2,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2309.50` | 202,240,000.00 USD | 202,240,000.00 USD | 282,530.00 USD | 300,580.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2311.50` | 280,950,000.00 USD | 280,950,000.00 USD | 7,190,000.00 USD | 3,230,000.00 USD | 5,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2312.30` | 200,160,000.00 USD | 200,160,000.00 USD | 1,740,000.00 USD | 128,300.00 USD | 2,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2314.10` | 264,760,000.00 USD | 264,760,000.00 USD | 10,080,000.00 USD | 3,280,000.00 USD | 688,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2315.00` | 267,770.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2315.10` | 195,780,000.00 USD | 195,780,000.00 USD | 4,300,000.00 USD | 4,100,000.00 USD | 117,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2316.70` | 250,710,000.00 USD | 250,710,000.00 USD | 3,450,000.00 USD | 5,270,000.00 USD | 3,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2317.90` | 187,260,000.00 USD | 187,260,000.00 USD | 817,040.00 USD | 3,010,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2319.30` | 238,290,000.00 USD | 238,290,000.00 USD | 8,240,000.00 USD | 2,120,000.00 USD | 795,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2320.70` | 183,440,000.00 USD | 183,440,000.00 USD | 0.00 USD | 2,790,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2321.90` | 227,140,000.00 USD | 227,140,000.00 USD | 616,250.00 USD | 2,660,000.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2323.50` | 180,650,000.00 USD | 180,650,000.00 USD | 4,070,000.00 USD | 1,900,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2324.50` | 222,200,000.00 USD | 222,200,000.00 USD | 8,660,000.00 USD | 2,780,000.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2325.00` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2326.30` | 174,670,000.00 USD | 174,670,000.00 USD | 0.00 USD | 0.00 USD | 126,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2327.10` | 208,540,000.00 USD | 208,540,000.00 USD | 0.00 USD | 3,260,000.00 USD | 4,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2329.10` | 174,550,000.00 USD | 174,550,000.00 USD | 3,860,000.00 USD | 0.00 USD | 4,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2329.70` | 200,830,000.00 USD | 200,830,000.00 USD | 5,520,000.00 USD | 1,150,000.00 USD | 3,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2331.90` | 165,800,000.00 USD | 165,800,000.00 USD | 29,230,000.00 USD | 1,090,000.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2332.30` | 191,120,000.00 USD | 191,120,000.00 USD | 17,970,000.00 USD | 2,290,000.00 USD | 107,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2334.70` | 132,670,000.00 USD | 132,670,000.00 USD | 7,260,000.00 USD | 18,420,000.00 USD | 8,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2334.90` | 170,750,000.00 USD | 170,750,000.00 USD | 28,290,000.00 USD | 25,090,000.00 USD | 16,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2337.50` | 101,280,000.00 USD | 101,280,000.00 USD | 6,570,000.00 USD | 22,000,000.00 USD | 10,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2337.50` | 98,050,000.00 USD | 98,050,000.00 USD | 20,380,000.00 USD | 18,560,000.00 USD | 13,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2340.10` | 62,550,000.00 USD | 62,550,000.00 USD | 4,960,000.00 USD | 21,890,000.00 USD | 7,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2340.30` | 45,550,000.00 USD | 45,550,000.00 USD | 1,630,000.00 USD | 10,010,000.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2342.70` | 28,630,000.00 USD | 28,630,000.00 USD | 5,030,000.00 USD | 8,490,000.00 USD | 2,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2343.10` | 30,520,000.00 USD | 30,520,000.00 USD | 0.00 USD | 5,540,000.00 USD | 3,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2345.30` | 12,940,000.00 USD | 12,940,000.00 USD | 963,370.00 USD | 1,770,000.00 USD | 9,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2345.90` | 21,140,000.00 USD | 21,140,000.00 USD | 0.00 USD | 8,310,000.00 USD | 12,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2347.90` | 215,860.00 USD | 215,860.00 USD | 215,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2348.70` | 18,370,000.00 USD | 18,370,000.00 USD | 285,680.00 USD | 7,340,000.00 USD | 10,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2350.50` | 28,430,000.00 USD | 28,430,000.00 USD | 25,900,000.00 USD | 2,510,000.00 USD | 23,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2351.50` | 42,270,000.00 USD | 42,270,000.00 USD | 782,590.00 USD | 17,440,000.00 USD | 5,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2353.10` | 30,230,000.00 USD | 30,230,000.00 USD | 576,450.00 USD | 1,110,000.00 USD | 107,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2354.30` | 83,490,000.00 USD | 83,490,000.00 USD | 5,960,000.00 USD | 35,020,000.00 USD | 237,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 35,020.00 USD | 35,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2355.70` | 47,760,000.00 USD | 47,760,000.00 USD | 318,080.00 USD | 15,970,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2357.10` | 96,790,000.00 USD | 96,790,000.00 USD | 7,900,000.00 USD | 5,400,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2358.30` | 47,960,000.00 USD | 47,960,000.00 USD | 0.00 USD | 0.00 USD | 198,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2359.90` | 99,010,000.00 USD | 99,010,000.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2360.90` | 49,910,000.00 USD | 49,910,000.00 USD | 1,850,000.00 USD | 0.00 USD | 93,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2362.70` | 101,160,000.00 USD | 101,160,000.00 USD | 467,570.00 USD | 0.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2363.50` | 53,020,000.00 USD | 53,020,000.00 USD | 929,610.00 USD | 1,840,000.00 USD | 341,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 153.25 USD | 35,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2365.50` | 109,160,000.00 USD | 109,160,000.00 USD | 6,340,000.00 USD | 0.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2366.10` | 53,250,000.00 USD | 53,250,000.00 USD | 61,300.00 USD | 0.00 USD | 170,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2368.30` | 119,130,000.00 USD | 119,130,000.00 USD | 9,590,000.00 USD | 0.00 USD | 370,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2368.70` | 65,730,000.00 USD | 65,730,000.00 USD | 8,060,000.00 USD | 3,260,000.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2371.10` | 180,920,000.00 USD | 180,920,000.00 USD | 16,760,000.00 USD | 0.00 USD | 45,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2371.30` | 104,120,000.00 USD | 104,120,000.00 USD | 17,050,000.00 USD | 12,840,000.00 USD | 8,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2373.90` | 121,660,000.00 USD | 121,660,000.00 USD | 13,630,000.00 USD | 955,690.00 USD | 2,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2373.90` | 203,490,000.00 USD | 203,490,000.00 USD | 15,830,000.00 USD | 0.00 USD | 6,730,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 14,790.00 USD | 49,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2376.50` | 147,560,000.00 USD | 147,560,000.00 USD | 12,130,000.00 USD | 3,180,000.00 USD | 10,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2376.70` | 243,630,000.00 USD | 243,630,000.00 USD | 12,140,000.00 USD | 5,950,000.00 USD | 22,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2379.10` | 178,930,000.00 USD | 178,930,000.00 USD | 5,850,000.00 USD | 13,800,000.00 USD | 11,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2379.50` | 270,940,000.00 USD | 270,940,000.00 USD | 7,180,000.00 USD | 2,580,000.00 USD | 17,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2381.70` | 220,730,000.00 USD | 220,730,000.00 USD | 15,410,000.00 USD | 10,970,000.00 USD | 15,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2382.30` | 312,290,000.00 USD | 312,290,000.00 USD | 7,910,000.00 USD | 12,120,000.00 USD | 21,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2384.30` | 269,950,000.00 USD | 269,950,000.00 USD | 21,040,000.00 USD | 17,560,000.00 USD | 10,610,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 3,380,000.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2385.10` | 399,030,000.00 USD | 399,030,000.00 USD | 14,990,000.00 USD | 28,990,000.00 USD | 42,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2386.90` | 300,220,000.00 USD | 300,220,000.00 USD | 12,200,000.00 USD | 11,050,000.00 USD | 7,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2387.90` | 479,170,000.00 USD | 479,170,000.00 USD | 4,870,000.00 USD | 32,720,000.00 USD | 42,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2389.50` | 324,160,000.00 USD | 324,160,000.00 USD | 9,590,000.00 USD | 8,400,000.00 USD | 5,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2390.70` | 578,860,000.00 USD | 578,860,000.00 USD | 5,470,000.00 USD | 45,700,000.00 USD | 48,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2392.10` | 351,900,000.00 USD | 351,900,000.00 USD | 5,340,000.00 USD | 13,820,000.00 USD | 8,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2393.50` | 677,320,000.00 USD | 677,320,000.00 USD | 43,890,000.00 USD | 22,890,000.00 USD | 31,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2394.70` | 382,860,000.00 USD | 382,860,000.00 USD | 14,780,000.00 USD | 13,450,000.00 USD | 2,740,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 4,430,000.00 USD | 7,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2396.30` | 761,370,000.00 USD | 761,370,000.00 USD | 29,820,000.00 USD | 32,850,000.00 USD | 21,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2397.30` | 402,050,000.00 USD | 402,050,000.00 USD | 5,540,000.00 USD | 8,740,000.00 USD | 4,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2399.10` | 850,890,000.00 USD | 850,890,000.00 USD | 39,350,000.00 USD | 31,200,000.00 USD | 18,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2399.90` | 443,360,000.00 USD | 443,360,000.00 USD | 17,930,000.00 USD | 9,240,000.00 USD | 14,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2401.90` | 961,680,000.00 USD | 961,680,000.00 USD | 53,530,000.00 USD | 24,490,000.00 USD | 32,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2402.50` | 469,850,000.00 USD | 469,850,000.00 USD | 8,820,000.00 USD | 9,710,000.00 USD | 7,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2404.70` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 36,370,000.00 USD | 25,840,000.00 USD | 15,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 11,200,000.00 USD | 19,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2405.10` | 503,290,000.00 USD | 503,290,000.00 USD | 13,880,000.00 USD | 10,580,000.00 USD | 8,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2407.50` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 22,760,000.00 USD | 29,510,000.00 USD | 18,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2407.70` | 538,430,000.00 USD | 538,430,000.00 USD | 14,050,000.00 USD | 11,560,000.00 USD | 9,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2410.30` | 563,070,000.00 USD | 563,070,000.00 USD | 9,390,000.00 USD | 8,300,000.00 USD | 6,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2410.30` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 26,620,000.00 USD | 26,620,000.00 USD | 23,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2412.90` | 582,600,000.00 USD | 582,600,000.00 USD | 9,190,000.00 USD | 6,900,000.00 USD | 3,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2413.10` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 13,360,000.00 USD | 15,180,000.00 USD | 13,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 666,630.00 USD | 19,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2415.50` | 595,630,000.00 USD | 595,630,000.00 USD | 3,550,000.00 USD | 5,790,000.00 USD | 3,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2415.90` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 28,030,000.00 USD | 17,450,000.00 USD | 32,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2418.10` | 608,540,000.00 USD | 608,540,000.00 USD | 4,840,000.00 USD | 5,370,000.00 USD | 2,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2418.70` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 28,840,000.00 USD | 18,500,000.00 USD | 12,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2420.70` | 623,470,000.00 USD | 623,470,000.00 USD | 6,810,000.00 USD | 5,220,000.00 USD | 2,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2421.50` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 23,440,000.00 USD | 25,120,000.00 USD | 18,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2423.30` | 637,320,000.00 USD | 637,320,000.00 USD | 4,570,000.00 USD | 3,780,000.00 USD | 5,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.30` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 25,250,000.00 USD | 29,620,000.00 USD | 33,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 3,250,000.00 USD | 22,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2425.90` | 640,670,000.00 USD | 640,670,000.00 USD | 516,070.00 USD | 2,570,000.00 USD | 261,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2427.10` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 24,580,000.00 USD | 22,020,000.00 USD | 23,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2428.50` | 643,030,000.00 USD | 643,030,000.00 USD | 2,090,000.00 USD | 12,140.00 USD | 264,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2429.90` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 6,160,000.00 USD | 14,060,000.00 USD | 8,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2431.10` | 645,990,000.00 USD | 645,990,000.00 USD | 2,190,000.00 USD | 507,190.00 USD | 254,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2432.70` | 1,660,000,000.00 USD | 1,660,000,000.00 USD | 17,740,000.00 USD | 13,220,000.00 USD | 6,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2433.70` | 648,840,000.00 USD | 648,840,000.00 USD | 314,980.00 USD | 534,830.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 8,030,000.00 USD | 31,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2435.50` | 1,710,000,000.00 USD | 1,710,000,000.00 USD | 22,360,000.00 USD | 14,140,000.00 USD | 15,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2436.30` | 653,700,000.00 USD | 653,700,000.00 USD | 3,340,000.00 USD | 1,270,000.00 USD | 261,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2438.30` | 1,770,000,000.00 USD | 1,770,000,000.00 USD | 17,900,000.00 USD | 23,900,000.00 USD | 15,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2438.90` | 658,290,000.00 USD | 658,290,000.00 USD | 1,260,000.00 USD | 1,610,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2441.10` | 1,810,000,000.00 USD | 1,810,000,000.00 USD | 17,250,000.00 USD | 6,990,000.00 USD | 14,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2441.50` | 667,150,000.00 USD | 667,150,000.00 USD | 4,710,000.00 USD | 3,380,000.00 USD | 767,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2443.90` | 1,840,000,000.00 USD | 1,840,000,000.00 USD | 6,650,000.00 USD | 13,590,000.00 USD | 7,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2444.10` | 670,380,000.00 USD | 670,380,000.00 USD | 791,730.00 USD | 798,660.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 748,180.00 USD | 31,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2446.70` | 678,140,000.00 USD | 678,140,000.00 USD | 4,320,000.00 USD | 1,500,000.00 USD | 1,940,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2446.70` | 1,870,000,000.00 USD | 1,870,000,000.00 USD | 11,870,000.00 USD | 7,020,000.00 USD | 18,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2449.30` | 684,680,000.00 USD | 684,680,000.00 USD | 2,040,000.00 USD | 1,740,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2449.50` | 1,910,000,000.00 USD | 1,910,000,000.00 USD | 15,780,000.00 USD | 9,650,000.00 USD | 14,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2451.90` | 696,950,000.00 USD | 696,950,000.00 USD | 3,860,000.00 USD | 3,720,000.00 USD | 4,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2452.30` | 1,940,000,000.00 USD | 1,940,000,000.00 USD | 10,050,000.00 USD | 9,630,000.00 USD | 7,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2454.50` | 707,120,000.00 USD | 707,120,000.00 USD | 4,200,000.00 USD | 3,460,000.00 USD | 2,510,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 108,990.00 USD | 31,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2455.10` | 1,960,000,000.00 USD | 1,960,000,000.00 USD | 5,550,000.00 USD | 5,830,000.00 USD | 3,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2457.10` | 714,270,000.00 USD | 714,270,000.00 USD | 2,160,000.00 USD | 2,720,000.00 USD | 2,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2457.90` | 1,990,000,000.00 USD | 1,990,000,000.00 USD | 12,470,000.00 USD | 11,200,000.00 USD | 13,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2459.70` | 719,950,000.00 USD | 719,950,000.00 USD | 2,370,000.00 USD | 1,970,000.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2460.70` | 2,020,000,000.00 USD | 2,020,000,000.00 USD | 7,010,000.00 USD | 10,640,000.00 USD | 5,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2462.30` | 723,270,000.00 USD | 723,270,000.00 USD | 174,920.00 USD | 2,050,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2463.50` | 2,040,000,000.00 USD | 2,040,000,000.00 USD | 9,490,000.00 USD | 9,600,000.00 USD | 8,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2464.90` | 725,340,000.00 USD | 725,340,000.00 USD | 820,990.00 USD | 1,240,000.00 USD | 5,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 296,600.00 USD | 32,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2466.30` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 5,400,000.00 USD | 2,080,000.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2467.50` | 725,720,000.00 USD | 725,720,000.00 USD | 0.00 USD | 370,410.00 USD | 7,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2469.10` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 2,770,000.00 USD | 3,570,000.00 USD | 408,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2470.10` | 729,770,000.00 USD | 729,770,000.00 USD | 1,390,000.00 USD | 1,510,000.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2471.90` | 2,070,000,000.00 USD | 2,070,000,000.00 USD | 3,090,000.00 USD | 2,760,000.00 USD | 814,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2472.70` | 730,010,000.00 USD | 730,010,000.00 USD | 0.00 USD | 232,740.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2474.70` | 2,070,000,000.00 USD | 2,070,000,000.00 USD | 5,400,000.00 USD | 866,790.00 USD | 1,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 444,190.00 USD | 32,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2475.30` | 730,750,000.00 USD | 730,750,000.00 USD | 738,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2477.50` | 2,080,000,000.00 USD | 2,080,000,000.00 USD | 790,860.00 USD | 3,880,000.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2477.90` | 730,800,000.00 USD | 730,800,000.00 USD | 0.00 USD | 41,760.00 USD | 7,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2480.30` | 2,080,000,000.00 USD | 2,080,000,000.00 USD | 2,300,000.00 USD | 1,740,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2480.50` | 731,350,000.00 USD | 731,350,000.00 USD | 0.00 USD | 27,720.00 USD | 518,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2483.10` | 731,970,000.00 USD | 731,970,000.00 USD | 628,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2483.10` | 2,090,000,000.00 USD | 2,090,000,000.00 USD | 2,010,000.00 USD | 1,330,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 528,130.00 USD | 33,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2485.90` | 2,090,000,000.00 USD | 2,090,000,000.00 USD | 586,480.00 USD | 1,560,000.00 USD | 77,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2488.70` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 1,710,000.00 USD | 842,740.00 USD | 2,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2491.50` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 1,660,000.00 USD | 2,550,000.00 USD | 672,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2494.30` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 2,380,000.00 USD | 2,730,000.00 USD | 5,000,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 939,880.00 USD | 34,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2497.10` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 3,640,000.00 USD | 3,570,000.00 USD | 6,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2499.90` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 1,110,000.00 USD | 2,430,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2502.70` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 110,450.00 USD | 1,430,000.00 USD | 170,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 217,400.00 USD | 34,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2505.50` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 3,200,000.00 USD | 2,320,000.00 USD | 59,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2508.30` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 1,150,000.00 USD | 1,270,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2511.10` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 2,560,000.00 USD | 3,230,000.00 USD | 2,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2513.90` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 776,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 1,670,000.00 USD | 35,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2516.70` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 97,050.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2519.50` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2522.10` | 732,210,000.00 USD | 732,210,000.00 USD | 80,610.00 USD | 61,830.00 USD | 90,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2522.30` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 1,050,000.00 USD | 0.00 USD | 945,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2524.70` | 732,660,000.00 USD | 732,660,000.00 USD | 421,540.00 USD | 0.00 USD | 30,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 1,000,000.00 USD | 36,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2525.10` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 307,040.00 USD | 224,130.00 USD | 178,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2527.30` | 732,770,000.00 USD | 732,770,000.00 USD | 0.00 USD | 57,450.00 USD | 50,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2527.90` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 1,520,000.00 USD | 871,200.00 USD | 749,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2529.90` | 734,840,000.00 USD | 734,840,000.00 USD | 995,550.00 USD | 645,910.00 USD | 437,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2530.70` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 2,140,000.00 USD | 1,930,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2532.50` | 735,210,000.00 USD | 735,210,000.00 USD | 359,430.00 USD | 0.00 USD | 7,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2533.50` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 2,620,000.00 USD | 1,770,000.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2535.00` | 941,310.00 USD | 37,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2535.10` | 735,980,000.00 USD | 735,980,000.00 USD | 229,190.00 USD | 41,990.00 USD | 499,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2536.30` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 2,810,000.00 USD | 2,460,000.00 USD | 2,740,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2537.70` | 740,530,000.00 USD | 740,530,000.00 USD | 2,030,000.00 USD | 901,140.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2539.10` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 3,530,000.00 USD | 3,180,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2540.30` | 743,390,000.00 USD | 743,390,000.00 USD | 1,140,000.00 USD | 1,100,000.00 USD | 617,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2541.90` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 3,400,000.00 USD | 2,740,000.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2542.90` | 745,580,000.00 USD | 745,580,000.00 USD | 1,100,000.00 USD | 1,070,000.00 USD | 19,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2544.70` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 2,170,000.00 USD | 1,830,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2545.00` | 6,810,000.00 USD | 44,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2545.50` | 746,990,000.00 USD | 746,990,000.00 USD | 590,640.00 USD | 800,740.00 USD | 12,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2547.50` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 2,380,000.00 USD | 938,680.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2548.10` | 749,930,000.00 USD | 749,930,000.00 USD | 1,370,000.00 USD | 832,850.00 USD | 743,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2550.30` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 2,860,000.00 USD | 2,690,000.00 USD | 1,800,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2550.70` | 753,390,000.00 USD | 753,390,000.00 USD | 1,380,000.00 USD | 1,460,000.00 USD | 618,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2553.10` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 2,120,000.00 USD | 788,360.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2553.30` | 754,170,000.00 USD | 754,170,000.00 USD | 468,780.00 USD | 220,540.00 USD | 90,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2555.00` | 316,850.00 USD | 45,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2555.90` | 755,940,000.00 USD | 755,940,000.00 USD | 1,010,000.00 USD | 398,720.00 USD | 366,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2555.90` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 3,290,000.00 USD | 255,750.00 USD | 5,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2558.50` | 757,550,000.00 USD | 757,550,000.00 USD | 722,170.00 USD | 141,030.00 USD | 745,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2558.70` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 3,850,000.00 USD | 1,200,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2561.10` | 761,790,000.00 USD | 761,790,000.00 USD | 1,640,000.00 USD | 1,270,000.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2561.50` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 2,780,000.00 USD | 2,030,000.00 USD | 426,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2563.70` | 763,510,000.00 USD | 763,510,000.00 USD | 440,660.00 USD | 975,880.00 USD | 309,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2564.30` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 1,800,000.00 USD | 2,150,000.00 USD | 1,460,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2565.00` | 1,770,000.00 USD | 46,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2566.30` | 763,760,000.00 USD | 763,760,000.00 USD | 121,690.00 USD | 17,120.00 USD | 105,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2567.10` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 575,630.00 USD | 1,510,000.00 USD | 2,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2568.90` | 764,020,000.00 USD | 764,020,000.00 USD | 162,270.00 USD | 0.00 USD | 101,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2569.90` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 125,250.00 USD | 290,680.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2571.50` | 764,970,000.00 USD | 764,970,000.00 USD | 770,210.00 USD | 169,470.00 USD | 5,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2572.70` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 2,000,000.00 USD | 890,480.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2574.10` | 765,660,000.00 USD | 765,660,000.00 USD | 121,300.00 USD | 191,750.00 USD | 381,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2575.00` | 11,780,000.00 USD | 58,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2575.50` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 2,180,000.00 USD | 440,740.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2576.70` | 766,310,000.00 USD | 766,310,000.00 USD | 439,020.00 USD | 209,570.00 USD | 3,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2578.30` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 734,040.00 USD | 1,480,000.00 USD | 1,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2579.30` | 767,650,000.00 USD | 767,650,000.00 USD | 308,690.00 USD | 314,010.00 USD | 710,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2581.10` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 3,270,000.00 USD | 864,580.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2581.90` | 770,400,000.00 USD | 770,400,000.00 USD | 1,580,000.00 USD | 935,910.00 USD | 234,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2583.90` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 740,840.00 USD | 1,260,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2584.50` | 771,400,000.00 USD | 771,400,000.00 USD | 287,140.00 USD | 153,810.00 USD | 554,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2585.00` | 34,400,000.00 USD | 92,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2586.70` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 1,900,000.00 USD | 2,190,000.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2587.10` | 773,430,000.00 USD | 773,430,000.00 USD | 1,260,000.00 USD | 335,670.00 USD | 439,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2589.50` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 2,840,000.00 USD | 446,810.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2589.70` | 774,740,000.00 USD | 774,740,000.00 USD | 445,920.00 USD | 99,440.00 USD | 763,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2592.30` | 776,980,000.00 USD | 776,980,000.00 USD | 971,410.00 USD | 349,000.00 USD | 919,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2592.30` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 2,340,000.00 USD | 1,280,000.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2594.90` | 780,080,000.00 USD | 780,080,000.00 USD | 886,830.00 USD | 1,220,000.00 USD | 995,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2595.00` | 526,600.00 USD | 93,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2595.10` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 452,020.00 USD | 569,790.00 USD | 752,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2597.50` | 781,040,000.00 USD | 781,040,000.00 USD | 179,030.00 USD | 442,330.00 USD | 339,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2597.90` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 2,280,000.00 USD | 1,630,000.00 USD | 2,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2600.10` | 782,330,000.00 USD | 782,330,000.00 USD | 258,900.00 USD | 724,120.00 USD | 303,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2600.70` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 496,060.00 USD | 1,960,000.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2602.70` | 783,210,000.00 USD | 783,210,000.00 USD | 107,010.00 USD | 453,880.00 USD | 318,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2603.50` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 2,040,000.00 USD | 1,580,000.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2605.00` | 2,280,000.00 USD | 95,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2605.30` | 784,190,000.00 USD | 784,190,000.00 USD | 0.00 USD | 644,330.00 USD | 336,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2606.30` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 1,480,000.00 USD | 229,360.00 USD | 342,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2607.90` | 784,870,000.00 USD | 784,870,000.00 USD | 187,520.00 USD | 497,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2609.10` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2610.50` | 785,170,000.00 USD | 785,170,000.00 USD | 0.00 USD | 294,600.00 USD | 2,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2611.90` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 724,220.00 USD | 608,060.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2613.10` | 786,180,000.00 USD | 786,180,000.00 USD | 555,320.00 USD | 250,240.00 USD | 205,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2614.70` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 1,110,000.00 USD | 1,000,000.00 USD | 409,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2615.00` | 1,400,000.00 USD | 97,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2617.50` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 1,550,000.00 USD | 209,240.00 USD | 402,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2618.30` | 786,480,000.00 USD | 786,480,000.00 USD | 295,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2620.30` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 47,360.00 USD | 1,120,000.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2623.10` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 631,440.00 USD | 410,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2625.00` | 415,110.00 USD | 97,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2635.00` | 285,480.00 USD | 97,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2645.00` | 4,570,000.00 USD | 102,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2655.00` | 26,040,000.00 USD | 128,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2665.00` | 308,530.00 USD | 128,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2675.00` | 129,060.00 USD | 128,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2685.00` | 863,190.00 USD | 129,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2695.00` | 127,350.00 USD | 129,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2705.00` | 34,620,000.00 USD | 164,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2715.00` | 9,400,000.00 USD | 173,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2725.00` | 252,980.00 USD | 174,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2735.00` | 3,680,000.00 USD | 177,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2745.00` | 14,130,000.00 USD | 192,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2755.00` | 781,510.00 USD | 192,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2765.00` | 133,660.00 USD | 192,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2775.00` | 5,300,000.00 USD | 198,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2785.00` | 1,840,000.00 USD | 200,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2795.00` | 215,540.00 USD | 200,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2805.00` | 614,490.00 USD | 200,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2815.00` | 317,080.00 USD | 201,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2825.00` | 73,550.00 USD | 201,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2835.00` | 3,400,000.00 USD | 204,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2845.00` | 561,940.00 USD | 205,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2855.00` | 142,800.00 USD | 205,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2865.00` | 891,760.00 USD | 206,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2875.00` | 54,180,000.00 USD | 260,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2885.00` | 17,520,000.00 USD | 277,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2895.00` | 26,860,000.00 USD | 304,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2905.00` | 482,750.00 USD | 305,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2915.00` | 6,630,000.00 USD | 311,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2925.00` | 1,630,000.00 USD | 313,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2935.00` | 338,370.00 USD | 313,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2945.00` | 1,840,000.00 USD | 315,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2955.00` | 20,280,000.00 USD | 336,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2965.00` | 1,340,000.00 USD | 337,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2975.00` | 5,760,000.00 USD | 343,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2985.00` | 793,760.00 USD | 343,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2995.00` | 905,120.00 USD | 344,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3005.00` | 4,160,000.00 USD | 349,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3015.00` | 483,050.00 USD | 349,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3025.00` | 4,050,000.00 USD | 353,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3035.00` | 2,670,000.00 USD | 356,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3045.00` | 13,140,000.00 USD | 369,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3055.00` | 2,250,000.00 USD | 371,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3065.00` | 627,050.00 USD | 372,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3075.00` | 3,710,000.00 USD | 375,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3085.00` | 2,000,000.00 USD | 377,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3095.00` | 793,480.00 USD | 378,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3105.00` | 188,840.00 USD | 378,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3115.00` | 256,410.00 USD | 379,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3125.00` | 150,350.00 USD | 379,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3135.00` | 57,540.00 USD | 379,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3145.00` | 1,260,000.00 USD | 380,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3155.00` | 7,240,000.00 USD | 387,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3165.00` | 145,340.00 USD | 388,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3175.00` | 723,430.00 USD | 388,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3185.00` | 772,400.00 USD | 389,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3195.00` | 3,500,000.00 USD | 393,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3205.00` | 5,070,000.00 USD | 398,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3215.00` | 1,830,000.00 USD | 399,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3225.00` | 492,170.00 USD | 400,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3235.00` | 83,440.00 USD | 400,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3245.00` | 8,290,000.00 USD | 408,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3255.00` | 18,180.00 USD | 408,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3265.00` | 226,090.00 USD | 409,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3275.00` | 10,860,000.00 USD | 419,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3285.00` | 8,550,000.00 USD | 428,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3295.00` | 1,260,000.00 USD | 429,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3305.00` | 373,660.00 USD | 430,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3315.00` | 962,150.00 USD | 431,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3325.00` | 185,310.00 USD | 431,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3335.00` | 101.38 USD | 431,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3345.00` | 526,380.00 USD | 431,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3355.00` | 63,100,000.00 USD | 494,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3365.00` | 681,010.00 USD | 495,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3375.00` | 151,280.00 USD | 495,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3385.00` | 156,290.00 USD | 495,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3395.00` | 51,790.00 USD | 495,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3405.00` | 758,050.00 USD | 496,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3415.00` | 296,330.00 USD | 496,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3425.00` | 14,570,000.00 USD | 511,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3435.00` | 355,230.00 USD | 511,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3445.00` | 27,180.00 USD | 511,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3455.00` | 353,230.00 USD | 512,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3465.00` | 1,360,000.00 USD | 513,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3475.00` | 291,150.00 USD | 513,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3485.00` | 7,030,000.00 USD | 520,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3495.00` | 6,150,000.00 USD | 527,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3505.00` | 18,140.00 USD | 527,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3515.00` | 36,050.00 USD | 527,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3525.00` | 140,630.00 USD | 527,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3535.00` | 69,700.00 USD | 527,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3545.00` | 17,420.00 USD | 527,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3555.00` | 97,800.00 USD | 527,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3565.00` | 559,850.00 USD | 528,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3575.00` | 3,060,000.00 USD | 531,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3585.00` | 474,410.00 USD | 531,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3595.00` | 291,170.00 USD | 531,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3605.00` | 8,020,000.00 USD | 539,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3615.00` | 8,720,000.00 USD | 548,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3625.00` | 6,900,000.00 USD | 555,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3635.00` | 365,530.00 USD | 555,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3645.00` | 85,260.00 USD | 555,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3655.00` | 40,200.00 USD | 555,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3665.00` | 292.47 USD | 555,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3675.00` | 1,240,000.00 USD | 557,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3685.00` | 387,210.00 USD | 557,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3695.00` | 34,630,000.00 USD | 592,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3705.00` | 17,450.00 USD | 592,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3715.00` | 104,740,000.00 USD | 697,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3725.00` | 13,820,000.00 USD | 710,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3735.00` | 146,060.00 USD | 710,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3745.00` | 1,100,000.00 USD | 712,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3755.00` | 207,740.00 USD | 712,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3765.00` | 77,170.00 USD | 712,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3775.00` | 412,690.00 USD | 712,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3785.00` | 403,030,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3795.00` | 15,200,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3805.00` | 508,180.00 USD | 1,130,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3815.00` | 7,140.00 USD | 1,130,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3825.00` | 19,580.00 USD | 1,130,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3835.00` | 4,800,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3845.00` | 1,660,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3855.00` | 667,630.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3865.00` | 666,280.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3875.00` | 1,610.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3885.00` | 1,430,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3895.00` | 2,090,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3905.00` | 616,790.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3915.00` | 88,830,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3925.00` | 154,500.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3935.00` | 258,650.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3945.00` | 55,720.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3955.00` | 272,590.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3965.00` | 622,310.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3975.00` | 30,240,000.00 USD | 1,260,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3985.00` | 115,680.00 USD | 1,260,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3995.00` | 67,290,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4005.00` | 872,190.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4015.00` | 204,990.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4025.00` | 76,530.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4035.00` | 1,170,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4045.00` | 3,310,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4055.00` | 2,150,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4065.00` | 85,690.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4075.00` | 10,100.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4085.00` | 4,810,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4095.00` | 592,770.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4105.00` | 3,100.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4115.00` | 877,120.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4125.00` | 36,990.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4135.00` | 23,360.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4145.00` | 2,120,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4155.00` | 58,670.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4165.00` | 939,410.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4175.00` | 71,340.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4185.00` | 879,160.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4195.00` | 4,120,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4205.00` | 42,840.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4215.00` | 7,630.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4225.00` | 89,150.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4235.00` | 1,310,000.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4245.00` | 26,390.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4255.00` | 14,280.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4265.00` | 198,440.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4275.00` | 118,730.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4285.00` | 216,590.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4295.00` | 132,720.00 USD | 1,360,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4305.00` | 280,900,000.00 USD | 1,640,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4315.00` | 1,740.00 USD | 1,640,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4325.00` | 106,060.00 USD | 1,640,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4335.00` | 17,340,000.00 USD | 1,650,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4345.00` | 19,600,000.00 USD | 1,670,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4355.00` | 2,000,000.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4365.00` | 568,450.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4375.00` | 122,120.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4385.00` | 3,270,000.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4395.00` | 2,190,000.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4405.00` | 262,700.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4415.00` | 83,180.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4425.00` | 584.54 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4435.00` | 16,720.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4445.00` | 357,280.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4455.00` | 28,260.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4465.00` | 1,180,000.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4475.00` | 91,960.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4485.00` | 24,480.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4495.00` | 1,310,000.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4505.00` | 6,750.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4525.00` | 54,810.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4535.00` | 34,730.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4545.00` | 10,260,000.00 USD | 1,700,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4555.00` | 288,340.00 USD | 1,700,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4565.00` | 30,130.00 USD | 1,700,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4575.00` | 416,350.00 USD | 1,700,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4585.00` | 168,330.00 USD | 1,700,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4595.00` | 40,880.00 USD | 1,700,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4605.00` | 498,430.00 USD | 1,700,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4615.00` | 258,140.00 USD | 1,700,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4625.00` | 776,590.00 USD | 1,700,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4635.00` | 70,800.00 USD | 1,700,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4645.00` | 2,110,000.00 USD | 1,700,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4655.00` | 443,600.00 USD | 1,700,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4665.00` | 398.86 USD | 1,700,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4675.00` | 5,710.00 USD | 1,700,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4685.00` | 990,380.00 USD | 1,700,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4695.00` | 32,300.00 USD | 1,700,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4705.00` | 2,730.00 USD | 1,700,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `475.00` | 882,750,000.00 USD | 0.00 USD | 8,640.00 USD | `-79.80%` | `18.19` |
| `Live` | `Long` | `485.00` | 882,740,000.00 USD | 0.00 USD | 25,130.00 USD | `-79.38%` | `51.82` |
| `Live` | `Long` | `495.00` | 882,720,000.00 USD | 0.00 USD | 9,510.00 USD | `-78.95%` | `19.22` |
| `Live` | `Long` | `505.00` | 882,710,000.00 USD | 0.00 USD | 28,840.00 USD | `-78.53%` | `57.11` |
| `Live` | `Long` | `515.00` | 882,680,000.00 USD | 0.00 USD | 3,560.00 USD | `-78.10%` | `6.91` |
| `Live` | `Long` | `525.00` | 882,680,000.00 USD | 0.00 USD | 131,920.00 USD | `-77.68%` | `251.27` |
| `Live` | `Long` | `535.00` | 882,540,000.00 USD | 0.00 USD | 13,230.00 USD | `-77.25%` | `24.72` |
| `Live` | `Long` | `545.00` | 882,530,000.00 USD | 0.00 USD | 11,150.00 USD | `-76.83%` | `20.46` |
| `Live` | `Long` | `555.00` | 882,520,000.00 USD | 0.00 USD | 6,170.00 USD | `-76.40%` | `11.12` |
| `Live` | `Long` | `565.00` | 882,510,000.00 USD | 0.00 USD | 37,290.00 USD | `-75.97%` | `65.99` |
| `Live` | `Long` | `575.00` | 882,480,000.00 USD | 0.00 USD | 389,040.00 USD | `-75.55%` | `676.59` |
| `Live` | `Long` | `585.00` | 882,090,000.00 USD | 0.00 USD | 38,780.00 USD | `-75.12%` | `66.29` |
| `Live` | `Long` | `595.00` | 882,050,000.00 USD | 0.00 USD | 242.82 USD | `-74.70%` | `0.41` |
| `Live` | `Long` | `605.00` | 882,050,000.00 USD | 0.00 USD | 8,760.00 USD | `-74.27%` | `14.48` |
| `Live` | `Long` | `615.00` | 882,040,000.00 USD | 0.00 USD | 149,310.00 USD | `-73.85%` | `242.79` |
| `Live` | `Long` | `625.00` | 881,890,000.00 USD | 0.00 USD | 10,570.00 USD | `-73.42%` | `16.92` |
| `Live` | `Long` | `635.00` | 881,880,000.00 USD | 0.00 USD | 44,080.00 USD | `-73.00%` | `69.42` |
| `Live` | `Long` | `645.00` | 881,840,000.00 USD | 0.00 USD | 3,870.00 USD | `-72.57%` | `6.00` |
| `Live` | `Long` | `655.00` | 881,830,000.00 USD | 0.00 USD | 27,600.00 USD | `-72.15%` | `42.13` |
| `Live` | `Long` | `665.00` | 881,800,000.00 USD | 0.00 USD | 109,500.00 USD | `-71.72%` | `164.66` |
| `Live` | `Long` | `675.00` | 881,700,000.00 USD | 0.00 USD | 14,570.00 USD | `-71.30%` | `21.58` |
| `Live` | `Long` | `685.00` | 881,680,000.00 USD | 0.00 USD | 26,520.00 USD | `-70.87%` | `38.71` |
| `Live` | `Long` | `695.00` | 881,650,000.00 USD | 0.00 USD | 429,090.00 USD | `-70.45%` | `617.39` |
| `Live` | `Long` | `705.00` | 881,220,000.00 USD | 0.00 USD | 79,880.00 USD | `-70.02%` | `113.31` |
| `Live` | `Long` | `715.00` | 881,140,000.00 USD | 0.00 USD | 722.15 USD | `-69.60%` | `1.01` |
| `Live` | `Long` | `725.00` | 881,140,000.00 USD | 0.00 USD | 470,870.00 USD | `-69.17%` | `649.48` |
| `Live` | `Long` | `735.00` | 880,670,000.00 USD | 0.00 USD | 58,800.00 USD | `-68.75%` | `80.00` |
| `Live` | `Long` | `745.00` | 880,610,000.00 USD | 0.00 USD | 73,890.00 USD | `-68.32%` | `99.19` |
| `Live` | `Long` | `755.00` | 880,540,000.00 USD | 0.00 USD | 66,360.00 USD | `-67.90%` | `87.90` |
| `Live` | `Long` | `765.00` | 880,470,000.00 USD | 0.00 USD | 451,170.00 USD | `-67.47%` | `589.77` |
| `Live` | `Long` | `775.00` | 880,020,000.00 USD | 0.00 USD | 14,600.00 USD | `-67.05%` | `18.84` |
| `Live` | `Long` | `785.00` | 880,010,000.00 USD | 0.00 USD | 33,390.00 USD | `-66.62%` | `42.53` |
| `Live` | `Long` | `795.00` | 879,980,000.00 USD | 0.00 USD | 674.16 USD | `-66.19%` | `0.85` |
| `Live` | `Long` | `805.00` | 879,970,000.00 USD | 0.00 USD | 1,800,000.00 USD | `-65.77%` | `2,236.73` |
| `Live` | `Long` | `815.00` | 878,170,000.00 USD | 0.00 USD | 80,080.00 USD | `-65.34%` | `98.25` |
| `Live` | `Long` | `825.00` | 878,090,000.00 USD | 0.00 USD | 3,630,000.00 USD | `-64.92%` | `4,398.17` |
| `Live` | `Long` | `835.00` | 874,470,000.00 USD | 0.00 USD | 19,570.00 USD | `-64.49%` | `23.44` |
| `Live` | `Long` | `845.00` | 874,450,000.00 USD | 0.00 USD | 8,950.00 USD | `-64.07%` | `10.59` |
| `Live` | `Long` | `855.00` | 874,440,000.00 USD | 0.00 USD | 12,910.00 USD | `-63.64%` | `15.10` |
| `Live` | `Long` | `865.00` | 874,420,000.00 USD | 0.00 USD | 70,390.00 USD | `-63.22%` | `81.38` |
| `Live` | `Long` | `875.00` | 874,350,000.00 USD | 0.00 USD | 177,240.00 USD | `-62.79%` | `202.56` |
| `Live` | `Long` | `885.00` | 874,180,000.00 USD | 0.00 USD | 6,380.00 USD | `-62.37%` | `7.21` |
| `Live` | `Long` | `895.00` | 874,170,000.00 USD | 0.00 USD | 946,640.00 USD | `-61.94%` | `1,057.70` |
| `Live` | `Long` | `905.00` | 873,220,000.00 USD | 0.00 USD | 402,930.00 USD | `-61.52%` | `445.23` |
| `Live` | `Long` | `915.00` | 872,820,000.00 USD | 0.00 USD | 166,450.00 USD | `-61.09%` | `181.91` |
| `Live` | `Long` | `925.00` | 872,650,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-60.67%` | `1,186.50` |
| `Live` | `Long` | `935.00` | 871,560,000.00 USD | 0.00 USD | 201,350.00 USD | `-60.24%` | `215.35` |
| `Live` | `Long` | `945.00` | 871,360,000.00 USD | 0.00 USD | 12,960.00 USD | `-59.82%` | `13.71` |
| `Live` | `Long` | `955.00` | 871,340,000.00 USD | 0.00 USD | 60,890.00 USD | `-59.39%` | `63.76` |
| `Live` | `Long` | `965.00` | 871,280,000.00 USD | 0.00 USD | 22,700.00 USD | `-58.97%` | `23.52` |
| `Live` | `Long` | `975.00` | 871,260,000.00 USD | 0.00 USD | 165,100.00 USD | `-58.54%` | `169.33` |
| `Live` | `Long` | `985.00` | 871,090,000.00 USD | 0.00 USD | 8,010.00 USD | `-58.12%` | `8.13` |
| `Live` | `Long` | `995.00` | 871,090,000.00 USD | 0.00 USD | 6,990,000.00 USD | `-57.69%` | `7,026.36` |
| `Live` | `Long` | `1005.00` | 864,090,000.00 USD | 0.00 USD | 34,900.00 USD | `-57.26%` | `34.73` |
| `Live` | `Long` | `1015.00` | 864,060,000.00 USD | 0.00 USD | 1,260,000.00 USD | `-56.84%` | `1,241.50` |
| `Live` | `Long` | `1025.00` | 862,800,000.00 USD | 0.00 USD | 1,640,000.00 USD | `-56.41%` | `1,603.12` |
| `Live` | `Long` | `1035.00` | 861,160,000.00 USD | 0.00 USD | 66,460.00 USD | `-55.99%` | `64.21` |
| `Live` | `Long` | `1045.00` | 861,090,000.00 USD | 0.00 USD | 1,980,000.00 USD | `-55.56%` | `1,891.40` |
| `Live` | `Long` | `1055.00` | 859,110,000.00 USD | 0.00 USD | 227,570.00 USD | `-55.14%` | `215.70` |
| `Live` | `Long` | `1065.00` | 858,890,000.00 USD | 0.00 USD | 196,890.00 USD | `-54.71%` | `184.87` |
| `Live` | `Long` | `1075.00` | 858,690,000.00 USD | 0.00 USD | 663,910.00 USD | `-54.29%` | `617.59` |
| `Live` | `Long` | `1085.00` | 858,020,000.00 USD | 0.00 USD | 148,710.00 USD | `-53.86%` | `137.06` |
| `Live` | `Long` | `1095.00` | 857,880,000.00 USD | 0.00 USD | 74,350.00 USD | `-53.44%` | `67.90` |
| `Live` | `Long` | `1105.00` | 857,800,000.00 USD | 0.00 USD | 188,810.00 USD | `-53.01%` | `170.87` |
| `Live` | `Long` | `1115.00` | 857,610,000.00 USD | 0.00 USD | 110,610.00 USD | `-52.59%` | `99.20` |
| `Live` | `Long` | `1125.00` | 857,500,000.00 USD | 0.00 USD | 80,330.00 USD | `-52.16%` | `71.40` |
| `Live` | `Long` | `1135.00` | 857,420,000.00 USD | 0.00 USD | 202,010.00 USD | `-51.74%` | `177.98` |
| `Live` | `Long` | `1145.00` | 857,220,000.00 USD | 0.00 USD | 379,510.00 USD | `-51.31%` | `331.45` |
| `Live` | `Long` | `1155.00` | 856,840,000.00 USD | 0.00 USD | 10,750,000.00 USD | `-50.89%` | `9,310.55` |
| `Live` | `Long` | `1165.00` | 846,090,000.00 USD | 0.00 USD | 61,630.00 USD | `-50.46%` | `52.90` |
| `Live` | `Long` | `1175.00` | 846,020,000.00 USD | 0.00 USD | 124,720.00 USD | `-50.04%` | `106.14` |
| `Live` | `Long` | `1185.00` | 845,900,000.00 USD | 0.00 USD | 1,500,000.00 USD | `-49.61%` | `1,265.49` |
| `Live` | `Long` | `1195.00` | 844,400,000.00 USD | 0.00 USD | 293,100.00 USD | `-49.19%` | `245.27` |
| `Live` | `Long` | `1205.00` | 844,110,000.00 USD | 0.00 USD | 981,950.00 USD | `-48.76%` | `814.90` |
| `Live` | `Long` | `1215.00` | 843,130,000.00 USD | 0.00 USD | 119,890.00 USD | `-48.34%` | `98.68` |
| `Live` | `Long` | `1225.00` | 843,010,000.00 USD | 0.00 USD | 943,680.00 USD | `-47.91%` | `770.35` |
| `Live` | `Long` | `1235.00` | 842,060,000.00 USD | 0.00 USD | 263,310.00 USD | `-47.48%` | `213.21` |
| `Live` | `Long` | `1245.00` | 841,800,000.00 USD | 0.00 USD | 520,710.00 USD | `-47.06%` | `418.24` |
| `Live` | `Long` | `1255.00` | 841,280,000.00 USD | 0.00 USD | 342,100.00 USD | `-46.63%` | `272.59` |
| `Live` | `Long` | `1265.00` | 840,940,000.00 USD | 0.00 USD | 361,680.00 USD | `-46.21%` | `285.91` |
| `Live` | `Long` | `1275.00` | 840,570,000.00 USD | 0.00 USD | 73,580.00 USD | `-45.78%` | `57.71` |
| `Live` | `Long` | `1285.00` | 840,500,000.00 USD | 0.00 USD | 15,600,000.00 USD | `-45.36%` | `12,139.96` |
| `Live` | `Long` | `1295.00` | 824,900,000.00 USD | 0.00 USD | 281,140.00 USD | `-44.93%` | `217.10` |
| `Live` | `Long` | `1305.00` | 824,620,000.00 USD | 0.00 USD | 248,940.00 USD | `-44.51%` | `190.76` |
| `Live` | `Long` | `1315.00` | 824,370,000.00 USD | 0.00 USD | 211,340.00 USD | `-44.08%` | `160.71` |
| `Live` | `Long` | `1325.00` | 824,160,000.00 USD | 0.00 USD | 449,550.00 USD | `-43.66%` | `339.28` |
| `Live` | `Long` | `1335.00` | 823,710,000.00 USD | 0.00 USD | 458,220.00 USD | `-43.23%` | `343.24` |
| `Live` | `Long` | `1345.00` | 823,250,000.00 USD | 0.00 USD | 432,360.00 USD | `-42.81%` | `321.46` |
| `Live` | `Long` | `1355.00` | 822,820,000.00 USD | 0.00 USD | 6,750,000.00 USD | `-42.38%` | `4,978.01` |
| `Live` | `Long` | `1365.00` | 816,070,000.00 USD | 0.00 USD | 1,110,000.00 USD | `-41.96%` | `812.48` |
| `Live` | `Long` | `1375.00` | 814,960,000.00 USD | 0.00 USD | 22,060,000.00 USD | `-41.53%` | `16,040.66` |
| `Live` | `Long` | `1385.00` | 792,910,000.00 USD | 0.00 USD | 290,680.00 USD | `-41.11%` | `209.88` |
| `Live` | `Long` | `1395.00` | 792,620,000.00 USD | 0.00 USD | 166,060.00 USD | `-40.68%` | `119.04` |
| `Live` | `Long` | `1405.00` | 792,450,000.00 USD | 0.00 USD | 10,170,000.00 USD | `-40.26%` | `7,239.83` |
| `Live` | `Long` | `1415.00` | 782,280,000.00 USD | 0.00 USD | 64,340.00 USD | `-39.83%` | `45.47` |
| `Live` | `Long` | `1425.00` | 782,220,000.00 USD | 0.00 USD | 1,480,000.00 USD | `-39.41%` | `1,036.03` |
| `Live` | `Long` | `1435.00` | 780,740,000.00 USD | 0.00 USD | 245,940.00 USD | `-38.98%` | `171.39` |
| `Live` | `Long` | `1445.00` | 780,490,000.00 USD | 0.00 USD | 15,020,000.00 USD | `-38.56%` | `10,392.90` |
| `Live` | `Long` | `1455.00` | 765,480,000.00 USD | 0.00 USD | 110,950.00 USD | `-38.13%` | `76.25` |
| `Live` | `Long` | `1465.00` | 765,370,000.00 USD | 0.00 USD | 442,100.00 USD | `-37.70%` | `301.78` |
| `Live` | `Long` | `1475.00` | 764,920,000.00 USD | 0.00 USD | 2,320,000.00 USD | `-37.28%` | `1,572.89` |
| `Live` | `Long` | `1485.00` | 762,600,000.00 USD | 0.00 USD | 299,770.00 USD | `-36.85%` | `201.87` |
| `Live` | `Long` | `1495.00` | 762,300,000.00 USD | 0.00 USD | 4,610,000.00 USD | `-36.43%` | `3,084.81` |
| `Live` | `Long` | `1505.00` | 757,690,000.00 USD | 0.00 USD | 95,120.00 USD | `-36.00%` | `63.20` |
| `Live` | `Long` | `1515.00` | 757,600,000.00 USD | 0.00 USD | 25,280,000.00 USD | `-35.58%` | `16,689.42` |
| `Live` | `Long` | `1525.00` | 732,310,000.00 USD | 0.00 USD | 18,440,000.00 USD | `-35.15%` | `12,088.97` |
| `Live` | `Long` | `1535.00` | 713,880,000.00 USD | 0.00 USD | 726,900.00 USD | `-34.73%` | `473.55` |
| `Live` | `Long` | `1545.00` | 713,150,000.00 USD | 0.00 USD | 4,940,000.00 USD | `-34.30%` | `3,197.34` |
| `Live` | `Long` | `1555.00` | 708,210,000.00 USD | 0.00 USD | 388,160.00 USD | `-33.88%` | `249.62` |
| `Live` | `Long` | `1565.00` | 707,820,000.00 USD | 0.00 USD | 142,630.00 USD | `-33.45%` | `91.14` |
| `Live` | `Long` | `1575.00` | 707,680,000.00 USD | 0.00 USD | 6,160,000.00 USD | `-33.03%` | `3,912.06` |
| `Live` | `Long` | `1585.00` | 701,520,000.00 USD | 0.00 USD | 307,140.00 USD | `-32.60%` | `193.78` |
| `Live` | `Long` | `1595.00` | 701,210,000.00 USD | 0.00 USD | 1,550,000.00 USD | `-32.18%` | `971.58` |
| `Live` | `Long` | `1605.00` | 699,660,000.00 USD | 0.00 USD | 18,410,000.00 USD | `-31.75%` | `11,470.06` |
| `Live` | `Long` | `1615.00` | 681,250,000.00 USD | 0.00 USD | 768,060.00 USD | `-31.33%` | `475.58` |
| `Live` | `Long` | `1625.00` | 680,480,000.00 USD | 0.00 USD | 207,400.00 USD | `-30.90%` | `127.63` |
| `Live` | `Long` | `1635.00` | 680,280,000.00 USD | 0.00 USD | 18,750,000.00 USD | `-30.48%` | `11,465.69` |
| `Live` | `Long` | `1645.00` | 661,530,000.00 USD | 0.00 USD | 36,560,000.00 USD | `-30.05%` | `22,222.58` |
| `Live` | `Long` | `1655.00` | 624,970,000.00 USD | 0.00 USD | 1,390,000.00 USD | `-29.63%` | `842.39` |
| `Live` | `Long` | `1665.00` | 623,580,000.00 USD | 0.00 USD | 738,370.00 USD | `-29.20%` | `443.47` |
| `Live` | `Long` | `1675.00` | 622,840,000.00 USD | 0.00 USD | 12,750,000.00 USD | `-28.77%` | `7,613.33` |
| `Live` | `Long` | `1685.00` | 610,090,000.00 USD | 0.00 USD | 1,930,000.00 USD | `-28.35%` | `1,145.24` |
| `Live` | `Long` | `1695.00` | 608,160,000.00 USD | 0.00 USD | 11,130,000.00 USD | `-27.92%` | `6,568.93` |
| `Live` | `Long` | `1705.00` | 597,020,000.00 USD | 0.00 USD | 1,660,000.00 USD | `-27.50%` | `972.01` |
| `Live` | `Long` | `1715.00` | 595,370,000.00 USD | 0.00 USD | 319,600.00 USD | `-27.07%` | `186.36` |
| `Live` | `Long` | `1725.00` | 595,050,000.00 USD | 0.00 USD | 18,430,000.00 USD | `-26.65%` | `10,683.92` |
| `Live` | `Long` | `1735.00` | 576,620,000.00 USD | 0.00 USD | 18,400,000.00 USD | `-26.22%` | `10,603.74` |
| `Live` | `Long` | `1745.00` | 558,220,000.00 USD | 0.00 USD | 1,050,000.00 USD | `-25.80%` | `602.85` |
| `Live` | `Long` | `1755.00` | 557,170,000.00 USD | 0.00 USD | 709,580.00 USD | `-25.37%` | `404.32` |
| `Live` | `Long` | `1765.00` | 556,460,000.00 USD | 0.00 USD | 4,190,000.00 USD | `-24.95%` | `2,371.18` |
| `Live` | `Long` | `1775.00` | 552,270,000.00 USD | 0.00 USD | 1,460,000.00 USD | `-24.52%` | `822.90` |
| `Live` | `Long` | `1785.00` | 550,810,000.00 USD | 0.00 USD | 54,280,000.00 USD | `-24.10%` | `30,410.36` |
| `Live` | `Long` | `1795.00` | 496,530,000.00 USD | 0.00 USD | 1,150,000.00 USD | `-23.67%` | `639.37` |
| `Live` | `Long` | `1805.00` | 495,380,000.00 USD | 0.00 USD | 9,830,000.00 USD | `-23.25%` | `5,446.91` |
| `Live` | `Long` | `1815.00` | 485,550,000.00 USD | 0.00 USD | 1,840,000.00 USD | `-22.82%` | `1,014.98` |
| `Live` | `Long` | `1825.00` | 483,710,000.00 USD | 0.00 USD | 531,360.00 USD | `-22.40%` | `291.15` |
| `Live` | `Long` | `1835.00` | 483,180,000.00 USD | 0.00 USD | 5,740,000.00 USD | `-21.97%` | `3,126.02` |
| `Live` | `Long` | `1845.00` | 477,440,000.00 USD | 0.00 USD | 13,680,000.00 USD | `-21.55%` | `7,412.36` |
| `Live` | `Long` | `1855.00` | 463,760,000.00 USD | 0.00 USD | 2,470,000.00 USD | `-21.12%` | `1,334.18` |
| `Live` | `Long` | `1865.00` | 461,290,000.00 USD | 0.00 USD | 966,690.00 USD | `-20.70%` | `518.33` |
| `Live` | `Long` | `1875.00` | 460,320,000.00 USD | 0.00 USD | 5,580,000.00 USD | `-20.27%` | `2,975.09` |
| `Live` | `Long` | `1885.00` | 454,750,000.00 USD | 0.00 USD | 2,940,000.00 USD | `-19.85%` | `1,562.12` |
| `Live` | `Long` | `1895.00` | 451,800,000.00 USD | 0.00 USD | 20,370,000.00 USD | `-19.42%` | `10,749.19` |
| `Live` | `Long` | `1905.00` | 431,430,000.00 USD | 0.00 USD | 941,710.00 USD | `-18.99%` | `494.34` |
| `Live` | `Long` | `1915.00` | 430,490,000.00 USD | 0.00 USD | 13,210,000.00 USD | `-18.57%` | `6,896.19` |
| `Live` | `Long` | `1925.00` | 417,280,000.00 USD | 0.00 USD | 2,910,000.00 USD | `-18.14%` | `1,510.00` |
| `Live` | `Long` | `1935.00` | 414,380,000.00 USD | 0.00 USD | 1,360,000.00 USD | `-17.72%` | `703.05` |
| `Live` | `Long` | `1945.00` | 413,020,000.00 USD | 0.00 USD | 1,750,000.00 USD | `-17.29%` | `900.53` |
| `Live` | `Long` | `1955.00` | 411,260,000.00 USD | 0.00 USD | 8,060,000.00 USD | `-16.87%` | `4,125.31` |
| `Live` | `Long` | `1965.00` | 403,200,000.00 USD | 0.00 USD | 900,710.00 USD | `-16.44%` | `458.38` |
| `Live` | `Long` | `1975.00` | 402,300,000.00 USD | 0.00 USD | 1,250,000.00 USD | `-16.02%` | `632.94` |
| `Live` | `Long` | `1985.00` | 401,050,000.00 USD | 0.00 USD | 4,420,000.00 USD | `-15.59%` | `2,225.20` |
| `Live` | `Long` | `1995.00` | 396,630,000.00 USD | 0.00 USD | 2,050,000.00 USD | `-15.17%` | `1,028.19` |
| `Live` | `Long` | `2005.00` | 394,580,000.00 USD | 0.00 USD | 1,820,000.00 USD | `-14.74%` | `908.71` |
| `Live` | `Long` | `2015.00` | 392,760,000.00 USD | 0.00 USD | 2,640,000.00 USD | `-14.32%` | `1,312.54` |
| `Live` | `Long` | `2025.00` | 390,110,000.00 USD | 0.00 USD | 1,760,000.00 USD | `-13.89%` | `869.54` |
| `Live` | `Long` | `2035.00` | 388,350,000.00 USD | 0.00 USD | 3,700,000.00 USD | `-13.47%` | `1,819.00` |
| `Live` | `Long` | `2045.00` | 384,650,000.00 USD | 0.00 USD | 16,870,000.00 USD | `-13.04%` | `8,251.70` |
| `Live` | `Long` | `2055.00` | 367,780,000.00 USD | 0.00 USD | 4,130,000.00 USD | `-12.62%` | `2,008.63` |
| `Live` | `Long` | `2065.00` | 363,650,000.00 USD | 0.00 USD | 1,390,000.00 USD | `-12.19%` | `674.69` |
| `Live` | `Long` | `2075.00` | 362,260,000.00 USD | 0.00 USD | 13,750,000.00 USD | `-11.77%` | `6,628.16` |
| `Live` | `Long` | `2085.00` | 348,500,000.00 USD | 0.00 USD | 1,810,000.00 USD | `-11.34%` | `865.86` |
| `Live` | `Long` | `2095.00` | 346,700,000.00 USD | 0.00 USD | 4,620,000.00 USD | `-10.92%` | `2,203.89` |
| `Live` | `Long` | `2105.00` | 342,080,000.00 USD | 0.00 USD | 23,040,000.00 USD | `-10.49%` | `10,945.91` |
| `Live` | `Long` | `2115.00` | 319,040,000.00 USD | 0.00 USD | 16,720,000.00 USD | `-10.07%` | `7,904.90` |
| `Live` | `Long` | `2125.00` | 302,320,000.00 USD | 0.00 USD | 1,140,000.00 USD | `-9.64%` | `537.38` |
| `Live` | `Long` | `2135.00` | 301,180,000.00 USD | 0.00 USD | 15,440,000.00 USD | `-9.21%` | `7,234.18` |
| `Live` | `Long` | `2145.00` | 285,730,000.00 USD | 0.00 USD | 16,180,000.00 USD | `-8.79%` | `7,545.32` |
| `Live` | `Long` | `2155.00` | 269,550,000.00 USD | 0.00 USD | 2,580,000.00 USD | `-8.36%` | `1,195.40` |
| `Live` | `Long` | `2165.00` | 266,970,000.00 USD | 0.00 USD | 1,660,000.00 USD | `-7.94%` | `764.93` |
| `Live` | `Long` | `2175.00` | 265,320,000.00 USD | 0.00 USD | 109,510,000.00 USD | `-7.51%` | `50,348.41` |
| `Live` | `Long` | `2185.00` | 155,810,000.00 USD | 0.00 USD | 113,580,000.00 USD | `-7.09%` | `51,982.01` |
| `Live` | `Long` | `2195.00` | 42,230,000.00 USD | 0.00 USD | 1,210,000.00 USD | `-6.66%` | `552.17` |
| `Live` | `Long` | `2205.00` | 41,020,000.00 USD | 0.00 USD | 1,160,000.00 USD | `-6.24%` | `527.51` |
| `Live` | `Long` | `2215.00` | 39,850,000.00 USD | 0.00 USD | 2,240,000.00 USD | `-5.81%` | `1,009.85` |
| `Live` | `Long` | `2225.00` | 37,620,000.00 USD | 0.00 USD | 1,560,000.00 USD | `-5.39%` | `701.25` |
| `Live` | `Long` | `2235.00` | 36,050,000.00 USD | 0.00 USD | 789,970.00 USD | `-4.96%` | `353.45` |
| `Live` | `Long` | `2245.00` | 35,260,000.00 USD | 0.00 USD | 4,680,000.00 USD | `-4.54%` | `2,082.52` |
| `Live` | `Long` | `2255.00` | 30,590,000.00 USD | 0.00 USD | 13,270,000.00 USD | `-4.11%` | `5,884.41` |
| `Live` | `Long` | `2265.00` | 17,320,000.00 USD | 0.00 USD | 3,530,000.00 USD | `-3.69%` | `1,560.41` |
| `Live` | `Long` | `2275.00` | 13,790,000.00 USD | 0.00 USD | 4,430,000.00 USD | `-3.26%` | `1,948.74` |
| `Live` | `Long` | `2285.00` | 9,350,000.00 USD | 0.00 USD | 5,990,000.00 USD | `-2.84%` | `2,623.26` |
| `Live` | `Long` | `2295.00` | 3,360,000.00 USD | 0.00 USD | 1,460,000.00 USD | `-2.41%` | `634.36` |
| `Live` | `Long` | `2305.00` | 1,900,000.00 USD | 0.00 USD | 280,710.00 USD | `-1.99%` | `121.78` |
| `Live` | `Long` | `2315.00` | 1,620,000.00 USD | 0.00 USD | 267,770.00 USD | `-1.56%` | `115.67` |
| `Live` | `Long` | `2325.00` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | `-1.14%` | `582.39` |
| `Live` | `Short` | `2355.00` | 35,020.00 USD | 35,020.00 USD | 0.00 USD | `+0.14%` | `14.87` |
| `Live` | `Short` | `2365.00` | 35,170.00 USD | 153.25 USD | 0.00 USD | `+0.57%` | `0.06` |
| `Live` | `Short` | `2375.00` | 49,960.00 USD | 14,790.00 USD | 0.00 USD | `+0.99%` | `6.23` |
| `Live` | `Short` | `2385.00` | 3,430,000.00 USD | 3,380,000.00 USD | 0.00 USD | `+1.42%` | `1,415.30` |
| `Live` | `Short` | `2395.00` | 7,860,000.00 USD | 4,430,000.00 USD | 0.00 USD | `+1.84%` | `1,850.93` |
| `Live` | `Short` | `2405.00` | 19,050,000.00 USD | 11,200,000.00 USD | 0.00 USD | `+2.27%` | `4,655.31` |
| `Live` | `Short` | `2415.00` | 19,720,000.00 USD | 666,630.00 USD | 0.00 USD | `+2.69%` | `276.04` |
| `Live` | `Short` | `2425.00` | 22,970,000.00 USD | 3,250,000.00 USD | 0.00 USD | `+3.12%` | `1,341.50` |
| `Live` | `Short` | `2435.00` | 31,000,000.00 USD | 8,030,000.00 USD | 0.00 USD | `+3.54%` | `3,295.85` |
| `Live` | `Short` | `2445.00` | 31,750,000.00 USD | 748,180.00 USD | 0.00 USD | `+3.97%` | `306.00` |
| `Live` | `Short` | `2455.00` | 31,860,000.00 USD | 108,990.00 USD | 0.00 USD | `+4.39%` | `44.39` |
| `Live` | `Short` | `2465.00` | 32,150,000.00 USD | 296,600.00 USD | 0.00 USD | `+4.82%` | `120.32` |
| `Live` | `Short` | `2475.00` | 32,600,000.00 USD | 444,190.00 USD | 0.00 USD | `+5.24%` | `179.47` |
| `Live` | `Short` | `2485.00` | 33,130,000.00 USD | 528,130.00 USD | 0.00 USD | `+5.67%` | `212.53` |
| `Live` | `Short` | `2495.00` | 34,070,000.00 USD | 939,880.00 USD | 0.00 USD | `+6.09%` | `376.71` |
| `Live` | `Short` | `2505.00` | 34,280,000.00 USD | 217,400.00 USD | 0.00 USD | `+6.52%` | `86.79` |
| `Live` | `Short` | `2515.00` | 35,950,000.00 USD | 1,670,000.00 USD | 0.00 USD | `+6.94%` | `662.97` |
| `Live` | `Short` | `2525.00` | 36,950,000.00 USD | 1,000,000.00 USD | 0.00 USD | `+7.37%` | `396.46` |
| `Live` | `Short` | `2535.00` | 37,890,000.00 USD | 941,310.00 USD | 0.00 USD | `+7.79%` | `371.33` |
| `Live` | `Short` | `2545.00` | 44,700,000.00 USD | 6,810,000.00 USD | 0.00 USD | `+8.22%` | `2,675.33` |
| `Live` | `Short` | `2555.00` | 45,020,000.00 USD | 316,850.00 USD | 0.00 USD | `+8.64%` | `124.01` |
| `Live` | `Short` | `2565.00` | 46,790,000.00 USD | 1,770,000.00 USD | 0.00 USD | `+9.07%` | `689.84` |
| `Live` | `Short` | `2575.00` | 58,570,000.00 USD | 11,780,000.00 USD | 0.00 USD | `+9.50%` | `4,575.52` |
| `Live` | `Short` | `2585.00` | 92,970,000.00 USD | 34,400,000.00 USD | 0.00 USD | `+9.92%` | `13,308.95` |
| `Live` | `Short` | `2595.00` | 93,500,000.00 USD | 526,600.00 USD | 0.00 USD | `+10.35%` | `202.93` |
| `Live` | `Short` | `2605.00` | 95,780,000.00 USD | 2,280,000.00 USD | 0.00 USD | `+10.77%` | `874.64` |
| `Live` | `Short` | `2615.00` | 97,180,000.00 USD | 1,400,000.00 USD | 0.00 USD | `+11.20%` | `536.15` |
| `Live` | `Short` | `2625.00` | 97,600,000.00 USD | 415,110.00 USD | 0.00 USD | `+11.62%` | `158.14` |
| `Live` | `Short` | `2635.00` | 97,880,000.00 USD | 285,480.00 USD | 0.00 USD | `+12.05%` | `108.34` |
| `Live` | `Short` | `2645.00` | 102,450,000.00 USD | 4,570,000.00 USD | 0.00 USD | `+12.47%` | `1,728.96` |
| `Live` | `Short` | `2655.00` | 128,500,000.00 USD | 26,040,000.00 USD | 0.00 USD | `+12.90%` | `9,809.12` |
| `Live` | `Short` | `2665.00` | 128,810,000.00 USD | 308,530.00 USD | 0.00 USD | `+13.32%` | `115.77` |
| `Live` | `Short` | `2675.00` | 128,930,000.00 USD | 129,060.00 USD | 0.00 USD | `+13.75%` | `48.25` |
| `Live` | `Short` | `2685.00` | 129,800,000.00 USD | 863,190.00 USD | 0.00 USD | `+14.17%` | `321.49` |
| `Live` | `Short` | `2695.00` | 129,930,000.00 USD | 127,350.00 USD | 0.00 USD | `+14.60%` | `47.25` |
| `Live` | `Short` | `2705.00` | 164,540,000.00 USD | 34,620,000.00 USD | 0.00 USD | `+15.02%` | `12,796.76` |
| `Live` | `Short` | `2715.00` | 173,950,000.00 USD | 9,400,000.00 USD | 0.00 USD | `+15.45%` | `3,464.02` |
| `Live` | `Short` | `2725.00` | 174,200,000.00 USD | 252,980.00 USD | 0.00 USD | `+15.87%` | `92.84` |
| `Live` | `Short` | `2735.00` | 177,880,000.00 USD | 3,680,000.00 USD | 0.00 USD | `+16.30%` | `1,346.58` |
| `Live` | `Short` | `2745.00` | 192,010,000.00 USD | 14,130,000.00 USD | 0.00 USD | `+16.72%` | `5,147.13` |
| `Live` | `Short` | `2755.00` | 192,790,000.00 USD | 781,510.00 USD | 0.00 USD | `+17.15%` | `283.67` |
| `Live` | `Short` | `2765.00` | 192,930,000.00 USD | 133,660.00 USD | 0.00 USD | `+17.57%` | `48.34` |
| `Live` | `Short` | `2775.00` | 198,220,000.00 USD | 5,300,000.00 USD | 0.00 USD | `+18.00%` | `1,909.49` |
| `Live` | `Short` | `2785.00` | 200,060,000.00 USD | 1,840,000.00 USD | 0.00 USD | `+18.42%` | `659.16` |
| `Live` | `Short` | `2795.00` | 200,280,000.00 USD | 215,540.00 USD | 0.00 USD | `+18.85%` | `77.12` |
| `Live` | `Short` | `2805.00` | 200,890,000.00 USD | 614,490.00 USD | 0.00 USD | `+19.28%` | `219.07` |
| `Live` | `Short` | `2815.00` | 201,210,000.00 USD | 317,080.00 USD | 0.00 USD | `+19.70%` | `112.64` |
| `Live` | `Short` | `2825.00` | 201,280,000.00 USD | 73,550.00 USD | 0.00 USD | `+20.13%` | `26.03` |
| `Live` | `Short` | `2835.00` | 204,680,000.00 USD | 3,400,000.00 USD | 0.00 USD | `+20.55%` | `1,197.54` |
| `Live` | `Short` | `2845.00` | 205,240,000.00 USD | 561,940.00 USD | 0.00 USD | `+20.98%` | `197.52` |
| `Live` | `Short` | `2855.00` | 205,380,000.00 USD | 142,800.00 USD | 0.00 USD | `+21.40%` | `50.02` |
| `Live` | `Short` | `2865.00` | 206,270,000.00 USD | 891,760.00 USD | 0.00 USD | `+21.83%` | `311.26` |
| `Live` | `Short` | `2875.00` | 260,450,000.00 USD | 54,180,000.00 USD | 0.00 USD | `+22.25%` | `18,845.87` |
| `Live` | `Short` | `2885.00` | 277,970,000.00 USD | 17,520,000.00 USD | 0.00 USD | `+22.68%` | `6,072.19` |
| `Live` | `Short` | `2895.00` | 304,830,000.00 USD | 26,860,000.00 USD | 0.00 USD | `+23.10%` | `9,277.11` |
| `Live` | `Short` | `2905.00` | 305,310,000.00 USD | 482,750.00 USD | 0.00 USD | `+23.53%` | `166.18` |
| `Live` | `Short` | `2915.00` | 311,940,000.00 USD | 6,630,000.00 USD | 0.00 USD | `+23.95%` | `2,273.43` |
| `Live` | `Short` | `2925.00` | 313,570,000.00 USD | 1,630,000.00 USD | 0.00 USD | `+24.38%` | `557.75` |
| `Live` | `Short` | `2935.00` | 313,910,000.00 USD | 338,370.00 USD | 0.00 USD | `+24.80%` | `115.29` |
| `Live` | `Short` | `2945.00` | 315,750,000.00 USD | 1,840,000.00 USD | 0.00 USD | `+25.23%` | `625.74` |
| `Live` | `Short` | `2955.00` | 336,040,000.00 USD | 20,280,000.00 USD | 0.00 USD | `+25.65%` | `6,864.22` |
| `Live` | `Short` | `2965.00` | 337,380,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+26.08%` | `453.05` |
| `Live` | `Short` | `2975.00` | 343,140,000.00 USD | 5,760,000.00 USD | 0.00 USD | `+26.50%` | `1,937.25` |
| `Live` | `Short` | `2985.00` | 343,940,000.00 USD | 793,760.00 USD | 0.00 USD | `+26.93%` | `265.92` |
| `Live` | `Short` | `2995.00` | 344,840,000.00 USD | 905,120.00 USD | 0.00 USD | `+27.35%` | `302.21` |
| `Live` | `Short` | `3005.00` | 349,000,000.00 USD | 4,160,000.00 USD | 0.00 USD | `+27.78%` | `1,384.99` |
| `Live` | `Short` | `3015.00` | 349,490,000.00 USD | 483,050.00 USD | 0.00 USD | `+28.21%` | `160.22` |
| `Live` | `Short` | `3025.00` | 353,540,000.00 USD | 4,050,000.00 USD | 0.00 USD | `+28.63%` | `1,338.88` |
| `Live` | `Short` | `3035.00` | 356,210,000.00 USD | 2,670,000.00 USD | 0.00 USD | `+29.06%` | `881.27` |
| `Live` | `Short` | `3045.00` | 369,350,000.00 USD | 13,140,000.00 USD | 0.00 USD | `+29.48%` | `4,316.48` |
| `Live` | `Short` | `3055.00` | 371,600,000.00 USD | 2,250,000.00 USD | 0.00 USD | `+29.91%` | `734.91` |
| `Live` | `Short` | `3065.00` | 372,230,000.00 USD | 627,050.00 USD | 0.00 USD | `+30.33%` | `204.58` |
| `Live` | `Short` | `3075.00` | 375,940,000.00 USD | 3,710,000.00 USD | 0.00 USD | `+30.76%` | `1,206.99` |
| `Live` | `Short` | `3085.00` | 377,930,000.00 USD | 2,000,000.00 USD | 0.00 USD | `+31.18%` | `646.83` |
| `Live` | `Short` | `3095.00` | 378,730,000.00 USD | 793,480.00 USD | 0.00 USD | `+31.61%` | `256.38` |
| `Live` | `Short` | `3105.00` | 378,920,000.00 USD | 188,840.00 USD | 0.00 USD | `+32.03%` | `60.82` |
| `Live` | `Short` | `3115.00` | 379,170,000.00 USD | 256,410.00 USD | 0.00 USD | `+32.46%` | `82.31` |
| `Live` | `Short` | `3125.00` | 379,320,000.00 USD | 150,350.00 USD | 0.00 USD | `+32.88%` | `48.11` |
| `Live` | `Short` | `3135.00` | 379,380,000.00 USD | 57,540.00 USD | 0.00 USD | `+33.31%` | `18.35` |
| `Live` | `Short` | `3145.00` | 380,640,000.00 USD | 1,260,000.00 USD | 0.00 USD | `+33.73%` | `399.41` |
| `Live` | `Short` | `3155.00` | 387,870,000.00 USD | 7,240,000.00 USD | 0.00 USD | `+34.16%` | `2,293.60` |
| `Live` | `Short` | `3165.00` | 388,020,000.00 USD | 145,340.00 USD | 0.00 USD | `+34.58%` | `45.92` |
| `Live` | `Short` | `3175.00` | 388,740,000.00 USD | 723,430.00 USD | 0.00 USD | `+35.01%` | `227.85` |
| `Live` | `Short` | `3185.00` | 389,510,000.00 USD | 772,400.00 USD | 0.00 USD | `+35.43%` | `242.51` |
| `Live` | `Short` | `3195.00` | 393,010,000.00 USD | 3,500,000.00 USD | 0.00 USD | `+35.86%` | `1,094.39` |
| `Live` | `Short` | `3205.00` | 398,080,000.00 USD | 5,070,000.00 USD | 0.00 USD | `+36.28%` | `1,581.26` |
| `Live` | `Short` | `3215.00` | 399,910,000.00 USD | 1,830,000.00 USD | 0.00 USD | `+36.71%` | `568.22` |
| `Live` | `Short` | `3225.00` | 400,400,000.00 USD | 492,170.00 USD | 0.00 USD | `+37.13%` | `152.61` |
| `Live` | `Short` | `3235.00` | 400,480,000.00 USD | 83,440.00 USD | 0.00 USD | `+37.56%` | `25.79` |
| `Live` | `Short` | `3245.00` | 408,770,000.00 USD | 8,290,000.00 USD | 0.00 USD | `+37.99%` | `2,554.80` |
| `Live` | `Short` | `3255.00` | 408,790,000.00 USD | 18,180.00 USD | 0.00 USD | `+38.41%` | `5.58` |
| `Live` | `Short` | `3265.00` | 409,020,000.00 USD | 226,090.00 USD | 0.00 USD | `+38.84%` | `69.25` |
| `Live` | `Short` | `3275.00` | 419,880,000.00 USD | 10,860,000.00 USD | 0.00 USD | `+39.26%` | `3,317.17` |
| `Live` | `Short` | `3285.00` | 428,430,000.00 USD | 8,550,000.00 USD | 0.00 USD | `+39.69%` | `2,604.14` |
| `Live` | `Short` | `3295.00` | 429,700,000.00 USD | 1,260,000.00 USD | 0.00 USD | `+40.11%` | `383.35` |
| `Live` | `Short` | `3305.00` | 430,070,000.00 USD | 373,660.00 USD | 0.00 USD | `+40.54%` | `113.06` |
| `Live` | `Short` | `3315.00` | 431,030,000.00 USD | 962,150.00 USD | 0.00 USD | `+40.96%` | `290.24` |
| `Live` | `Short` | `3325.00` | 431,220,000.00 USD | 185,310.00 USD | 0.00 USD | `+41.39%` | `55.73` |
| `Live` | `Short` | `3335.00` | 431,220,000.00 USD | 101.38 USD | 0.00 USD | `+41.81%` | `0.03` |
| `Live` | `Short` | `3345.00` | 431,740,000.00 USD | 526,380.00 USD | 0.00 USD | `+42.24%` | `157.36` |
| `Live` | `Short` | `3355.00` | 494,850,000.00 USD | 63,100,000.00 USD | 0.00 USD | `+42.66%` | `18,808.63` |
| `Live` | `Short` | `3365.00` | 495,530,000.00 USD | 681,010.00 USD | 0.00 USD | `+43.09%` | `202.38` |
| `Live` | `Short` | `3375.00` | 495,680,000.00 USD | 151,280.00 USD | 0.00 USD | `+43.51%` | `44.82` |
| `Live` | `Short` | `3385.00` | 495,840,000.00 USD | 156,290.00 USD | 0.00 USD | `+43.94%` | `46.17` |
| `Live` | `Short` | `3395.00` | 495,890,000.00 USD | 51,790.00 USD | 0.00 USD | `+44.36%` | `15.25` |
| `Live` | `Short` | `3405.00` | 496,650,000.00 USD | 758,050.00 USD | 0.00 USD | `+44.79%` | `222.63` |
| `Live` | `Short` | `3415.00` | 496,940,000.00 USD | 296,330.00 USD | 0.00 USD | `+45.21%` | `86.77` |
| `Live` | `Short` | `3425.00` | 511,510,000.00 USD | 14,570,000.00 USD | 0.00 USD | `+45.64%` | `4,253.58` |
| `Live` | `Short` | `3435.00` | 511,870,000.00 USD | 355,230.00 USD | 0.00 USD | `+46.06%` | `103.42` |
| `Live` | `Short` | `3445.00` | 511,890,000.00 USD | 27,180.00 USD | 0.00 USD | `+46.49%` | `7.89` |
| `Live` | `Short` | `3455.00` | 512,250,000.00 USD | 353,230.00 USD | 0.00 USD | `+46.91%` | `102.24` |
| `Live` | `Short` | `3465.00` | 513,610,000.00 USD | 1,360,000.00 USD | 0.00 USD | `+47.34%` | `393.61` |
| `Live` | `Short` | `3475.00` | 513,900,000.00 USD | 291,150.00 USD | 0.00 USD | `+47.77%` | `83.78` |
| `Live` | `Short` | `3485.00` | 520,940,000.00 USD | 7,030,000.00 USD | 0.00 USD | `+48.19%` | `2,018.30` |
| `Live` | `Short` | `3495.00` | 527,090,000.00 USD | 6,150,000.00 USD | 0.00 USD | `+48.62%` | `1,760.95` |
| `Live` | `Short` | `3505.00` | 527,110,000.00 USD | 18,140.00 USD | 0.00 USD | `+49.04%` | `5.17` |
| `Live` | `Short` | `3515.00` | 527,140,000.00 USD | 36,050.00 USD | 0.00 USD | `+49.47%` | `10.26` |
| `Live` | `Short` | `3525.00` | 527,280,000.00 USD | 140,630.00 USD | 0.00 USD | `+49.89%` | `39.90` |
| `Live` | `Short` | `3535.00` | 527,350,000.00 USD | 69,700.00 USD | 0.00 USD | `+50.32%` | `19.72` |
| `Live` | `Short` | `3545.00` | 527,370,000.00 USD | 17,420.00 USD | 0.00 USD | `+50.74%` | `4.91` |
| `Live` | `Short` | `3555.00` | 527,470,000.00 USD | 97,800.00 USD | 0.00 USD | `+51.17%` | `27.51` |
| `Live` | `Short` | `3565.00` | 528,030,000.00 USD | 559,850.00 USD | 0.00 USD | `+51.59%` | `157.04` |
| `Live` | `Short` | `3575.00` | 531,090,000.00 USD | 3,060,000.00 USD | 0.00 USD | `+52.02%` | `854.92` |
| `Live` | `Short` | `3585.00` | 531,560,000.00 USD | 474,410.00 USD | 0.00 USD | `+52.44%` | `132.33` |
| `Live` | `Short` | `3595.00` | 531,850,000.00 USD | 291,170.00 USD | 0.00 USD | `+52.87%` | `80.99` |
| `Live` | `Short` | `3605.00` | 539,870,000.00 USD | 8,020,000.00 USD | 0.00 USD | `+53.29%` | `2,225.02` |
| `Live` | `Short` | `3615.00` | 548,590,000.00 USD | 8,720,000.00 USD | 0.00 USD | `+53.72%` | `2,412.09` |
| `Live` | `Short` | `3625.00` | 555,490,000.00 USD | 6,900,000.00 USD | 0.00 USD | `+54.14%` | `1,903.35` |
| `Live` | `Short` | `3635.00` | 555,860,000.00 USD | 365,530.00 USD | 0.00 USD | `+54.57%` | `100.56` |
| `Live` | `Short` | `3645.00` | 555,940,000.00 USD | 85,260.00 USD | 0.00 USD | `+54.99%` | `23.39` |
| `Live` | `Short` | `3655.00` | 555,980,000.00 USD | 40,200.00 USD | 0.00 USD | `+55.42%` | `11.00` |
| `Live` | `Short` | `3665.00` | 555,980,000.00 USD | 292.47 USD | 0.00 USD | `+55.84%` | `0.08` |
| `Live` | `Short` | `3675.00` | 557,220,000.00 USD | 1,240,000.00 USD | 0.00 USD | `+56.27%` | `337.10` |
| `Live` | `Short` | `3685.00` | 557,610,000.00 USD | 387,210.00 USD | 0.00 USD | `+56.70%` | `105.08` |
| `Live` | `Short` | `3695.00` | 592,240,000.00 USD | 34,630,000.00 USD | 0.00 USD | `+57.12%` | `9,372.80` |
| `Live` | `Short` | `3705.00` | 592,260,000.00 USD | 17,450.00 USD | 0.00 USD | `+57.55%` | `4.71` |
| `Live` | `Short` | `3715.00` | 697,000,000.00 USD | 104,740,000.00 USD | 0.00 USD | `+57.97%` | `28,194.41` |
| `Live` | `Short` | `3725.00` | 710,820,000.00 USD | 13,820,000.00 USD | 0.00 USD | `+58.40%` | `3,710.15` |
| `Live` | `Short` | `3735.00` | 710,970,000.00 USD | 146,060.00 USD | 0.00 USD | `+58.82%` | `39.11` |
| `Live` | `Short` | `3745.00` | 712,070,000.00 USD | 1,100,000.00 USD | 0.00 USD | `+59.25%` | `294.96` |
| `Live` | `Short` | `3755.00` | 712,280,000.00 USD | 207,740.00 USD | 0.00 USD | `+59.67%` | `55.32` |
| `Live` | `Short` | `3765.00` | 712,360,000.00 USD | 77,170.00 USD | 0.00 USD | `+60.10%` | `20.50` |
| `Live` | `Short` | `3775.00` | 712,770,000.00 USD | 412,690.00 USD | 0.00 USD | `+60.52%` | `109.32` |
| `Live` | `Short` | `3785.00` | 1,120,000,000.00 USD | 403,030,000.00 USD | 0.00 USD | `+60.95%` | `106,479.96` |
| `Live` | `Short` | `3795.00` | 1,130,000,000.00 USD | 15,200,000.00 USD | 0.00 USD | `+61.37%` | `4,005.21` |
| `Live` | `Short` | `3805.00` | 1,130,000,000.00 USD | 508,180.00 USD | 0.00 USD | `+61.80%` | `133.56` |
| `Live` | `Short` | `3815.00` | 1,130,000,000.00 USD | 7,140.00 USD | 0.00 USD | `+62.22%` | `1.87` |
| `Live` | `Short` | `3825.00` | 1,130,000,000.00 USD | 19,580.00 USD | 0.00 USD | `+62.65%` | `5.12` |
| `Live` | `Short` | `3835.00` | 1,140,000,000.00 USD | 4,800,000.00 USD | 0.00 USD | `+63.07%` | `1,252.17` |
| `Live` | `Short` | `3845.00` | 1,140,000,000.00 USD | 1,660,000.00 USD | 0.00 USD | `+63.50%` | `431.02` |
| `Live` | `Short` | `3855.00` | 1,140,000,000.00 USD | 667,630.00 USD | 0.00 USD | `+63.92%` | `173.19` |
| `Live` | `Short` | `3865.00` | 1,140,000,000.00 USD | 666,280.00 USD | 0.00 USD | `+64.35%` | `172.39` |
| `Live` | `Short` | `3875.00` | 1,140,000,000.00 USD | 1,610.00 USD | 0.00 USD | `+64.77%` | `0.41` |
| `Live` | `Short` | `3885.00` | 1,140,000,000.00 USD | 1,430,000.00 USD | 0.00 USD | `+65.20%` | `369.06` |
| `Live` | `Short` | `3895.00` | 1,140,000,000.00 USD | 2,090,000.00 USD | 0.00 USD | `+65.62%` | `537.56` |
| `Live` | `Short` | `3905.00` | 1,140,000,000.00 USD | 616,790.00 USD | 0.00 USD | `+66.05%` | `157.95` |
| `Live` | `Short` | `3915.00` | 1,230,000,000.00 USD | 88,830,000.00 USD | 0.00 USD | `+66.48%` | `22,689.90` |
| `Live` | `Short` | `3925.00` | 1,230,000,000.00 USD | 154,500.00 USD | 0.00 USD | `+66.90%` | `39.36` |
| `Live` | `Short` | `3935.00` | 1,230,000,000.00 USD | 258,650.00 USD | 0.00 USD | `+67.33%` | `65.73` |
| `Live` | `Short` | `3945.00` | 1,230,000,000.00 USD | 55,720.00 USD | 0.00 USD | `+67.75%` | `14.12` |
| `Live` | `Short` | `3955.00` | 1,230,000,000.00 USD | 272,590.00 USD | 0.00 USD | `+68.18%` | `68.92` |
| `Live` | `Short` | `3965.00` | 1,230,000,000.00 USD | 622,310.00 USD | 0.00 USD | `+68.60%` | `156.95` |
| `Live` | `Short` | `3975.00` | 1,260,000,000.00 USD | 30,240,000.00 USD | 0.00 USD | `+69.03%` | `7,607.29` |
| `Live` | `Short` | `3985.00` | 1,260,000,000.00 USD | 115,680.00 USD | 0.00 USD | `+69.45%` | `29.03` |
| `Live` | `Short` | `3995.00` | 1,330,000,000.00 USD | 67,290,000.00 USD | 0.00 USD | `+69.88%` | `16,843.31` |
| `Live` | `Short` | `4005.00` | 1,330,000,000.00 USD | 872,190.00 USD | 0.00 USD | `+70.30%` | `217.78` |
| `Live` | `Short` | `4015.00` | 1,330,000,000.00 USD | 204,990.00 USD | 0.00 USD | `+70.73%` | `51.06` |
| `Live` | `Short` | `4025.00` | 1,330,000,000.00 USD | 76,530.00 USD | 0.00 USD | `+71.15%` | `19.01` |
| `Live` | `Short` | `4035.00` | 1,330,000,000.00 USD | 1,170,000.00 USD | 0.00 USD | `+71.58%` | `290.83` |
| `Live` | `Short` | `4045.00` | 1,340,000,000.00 USD | 3,310,000.00 USD | 0.00 USD | `+72.00%` | `817.18` |
| `Live` | `Short` | `4055.00` | 1,340,000,000.00 USD | 2,150,000.00 USD | 0.00 USD | `+72.43%` | `530.60` |
| `Live` | `Short` | `4065.00` | 1,340,000,000.00 USD | 85,690.00 USD | 0.00 USD | `+72.85%` | `21.08` |
| `Live` | `Short` | `4075.00` | 1,340,000,000.00 USD | 10,100.00 USD | 0.00 USD | `+73.28%` | `2.48` |
| `Live` | `Short` | `4085.00` | 1,340,000,000.00 USD | 4,810,000.00 USD | 0.00 USD | `+73.70%` | `1,176.46` |
| `Live` | `Short` | `4095.00` | 1,340,000,000.00 USD | 592,770.00 USD | 0.00 USD | `+74.13%` | `144.75` |
| `Live` | `Short` | `4105.00` | 1,340,000,000.00 USD | 3,100.00 USD | 0.00 USD | `+74.55%` | `0.76` |
| `Live` | `Short` | `4115.00` | 1,350,000,000.00 USD | 877,120.00 USD | 0.00 USD | `+74.98%` | `213.15` |
| `Live` | `Short` | `4125.00` | 1,350,000,000.00 USD | 36,990.00 USD | 0.00 USD | `+75.41%` | `8.97` |
| `Live` | `Short` | `4135.00` | 1,350,000,000.00 USD | 23,360.00 USD | 0.00 USD | `+75.83%` | `5.65` |
| `Live` | `Short` | `4145.00` | 1,350,000,000.00 USD | 2,120,000.00 USD | 0.00 USD | `+76.26%` | `511.85` |
| `Live` | `Short` | `4155.00` | 1,350,000,000.00 USD | 58,670.00 USD | 0.00 USD | `+76.68%` | `14.12` |
| `Live` | `Short` | `4165.00` | 1,350,000,000.00 USD | 939,410.00 USD | 0.00 USD | `+77.11%` | `225.55` |
| `Live` | `Short` | `4175.00` | 1,350,000,000.00 USD | 71,340.00 USD | 0.00 USD | `+77.53%` | `17.09` |
| `Live` | `Short` | `4185.00` | 1,350,000,000.00 USD | 879,160.00 USD | 0.00 USD | `+77.96%` | `210.07` |
| `Live` | `Short` | `4195.00` | 1,350,000,000.00 USD | 4,120,000.00 USD | 0.00 USD | `+78.38%` | `983.01` |
| `Live` | `Short` | `4205.00` | 1,350,000,000.00 USD | 42,840.00 USD | 0.00 USD | `+78.81%` | `10.19` |
| `Live` | `Short` | `4215.00` | 1,350,000,000.00 USD | 7,630.00 USD | 0.00 USD | `+79.23%` | `1.81` |
| `Live` | `Short` | `4225.00` | 1,350,000,000.00 USD | 89,150.00 USD | 0.00 USD | `+79.66%` | `21.10` |
| `Live` | `Short` | `4235.00` | 1,360,000,000.00 USD | 1,310,000.00 USD | 0.00 USD | `+80.08%` | `310.00` |
| `Live` | `Short` | `4245.00` | 1,360,000,000.00 USD | 26,390.00 USD | 0.00 USD | `+80.51%` | `6.22` |
| `Live` | `Short` | `4255.00` | 1,360,000,000.00 USD | 14,280.00 USD | 0.00 USD | `+80.93%` | `3.36` |
| `Live` | `Short` | `4265.00` | 1,360,000,000.00 USD | 198,440.00 USD | 0.00 USD | `+81.36%` | `46.53` |
| `Live` | `Short` | `4275.00` | 1,360,000,000.00 USD | 118,730.00 USD | 0.00 USD | `+81.78%` | `27.77` |
| `Live` | `Short` | `4285.00` | 1,360,000,000.00 USD | 216,590.00 USD | 0.00 USD | `+82.21%` | `50.55` |
| `Live` | `Short` | `4295.00` | 1,360,000,000.00 USD | 132,720.00 USD | 0.00 USD | `+82.63%` | `30.90` |
| `Live` | `Short` | `4305.00` | 1,640,000,000.00 USD | 280,900,000.00 USD | 0.00 USD | `+83.06%` | `65,248.74` |
| `Live` | `Short` | `4315.00` | 1,640,000,000.00 USD | 1,740.00 USD | 0.00 USD | `+83.48%` | `0.40` |
| `Live` | `Short` | `4325.00` | 1,640,000,000.00 USD | 106,060.00 USD | 0.00 USD | `+83.91%` | `24.52` |
| `Live` | `Short` | `4335.00` | 1,650,000,000.00 USD | 17,340,000.00 USD | 0.00 USD | `+84.33%` | `3,999.53` |
| `Live` | `Short` | `4345.00` | 1,670,000,000.00 USD | 19,600,000.00 USD | 0.00 USD | `+84.76%` | `4,510.58` |
| `Live` | `Short` | `4355.00` | 1,680,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | `+85.19%` | `459.85` |
| `Live` | `Short` | `4365.00` | 1,680,000,000.00 USD | 568,450.00 USD | 0.00 USD | `+85.61%` | `130.23` |
| `Live` | `Short` | `4375.00` | 1,680,000,000.00 USD | 122,120.00 USD | 0.00 USD | `+86.04%` | `27.91` |
| `Live` | `Short` | `4385.00` | 1,680,000,000.00 USD | 3,270,000.00 USD | 0.00 USD | `+86.46%` | `746.47` |
| `Live` | `Short` | `4395.00` | 1,680,000,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+86.89%` | `498.24` |
| `Live` | `Short` | `4405.00` | 1,680,000,000.00 USD | 262,700.00 USD | 0.00 USD | `+87.31%` | `59.64` |
| `Live` | `Short` | `4415.00` | 1,680,000,000.00 USD | 83,180.00 USD | 0.00 USD | `+87.74%` | `18.84` |
| `Live` | `Short` | `4425.00` | 1,680,000,000.00 USD | 584.54 USD | 0.00 USD | `+88.16%` | `0.13` |
| `Live` | `Short` | `4435.00` | 1,680,000,000.00 USD | 16,720.00 USD | 0.00 USD | `+88.59%` | `3.77` |
| `Live` | `Short` | `4445.00` | 1,680,000,000.00 USD | 357,280.00 USD | 0.00 USD | `+89.01%` | `80.38` |
| `Live` | `Short` | `4455.00` | 1,680,000,000.00 USD | 28,260.00 USD | 0.00 USD | `+89.44%` | `6.34` |
| `Live` | `Short` | `4465.00` | 1,680,000,000.00 USD | 1,180,000.00 USD | 0.00 USD | `+89.86%` | `264.99` |
| `Live` | `Short` | `4475.00` | 1,680,000,000.00 USD | 91,960.00 USD | 0.00 USD | `+90.29%` | `20.55` |
| `Live` | `Short` | `4485.00` | 1,680,000,000.00 USD | 24,480.00 USD | 0.00 USD | `+90.71%` | `5.46` |
| `Live` | `Short` | `4495.00` | 1,690,000,000.00 USD | 1,310,000.00 USD | 0.00 USD | `+91.14%` | `292.02` |
| `Live` | `Short` | `4505.00` | 1,690,000,000.00 USD | 6,750.00 USD | 0.00 USD | `+91.56%` | `1.50` |
| `Live` | `Short` | `4525.00` | 1,690,000,000.00 USD | 54,810.00 USD | 0.00 USD | `+92.41%` | `12.11` |
| `Live` | `Short` | `4535.00` | 1,690,000,000.00 USD | 34,730.00 USD | 0.00 USD | `+92.84%` | `7.66` |
| `Live` | `Short` | `4545.00` | 1,700,000,000.00 USD | 10,260,000.00 USD | 0.00 USD | `+93.26%` | `2,258.38` |
| `Live` | `Short` | `4555.00` | 1,700,000,000.00 USD | 288,340.00 USD | 0.00 USD | `+93.69%` | `63.30` |
| `Live` | `Short` | `4565.00` | 1,700,000,000.00 USD | 30,130.00 USD | 0.00 USD | `+94.11%` | `6.60` |
| `Live` | `Short` | `4575.00` | 1,700,000,000.00 USD | 416,350.00 USD | 0.00 USD | `+94.54%` | `91.00` |
| `Live` | `Short` | `4585.00` | 1,700,000,000.00 USD | 168,330.00 USD | 0.00 USD | `+94.97%` | `36.71` |
| `Live` | `Short` | `4595.00` | 1,700,000,000.00 USD | 40,880.00 USD | 0.00 USD | `+95.39%` | `8.90` |
| `Live` | `Short` | `4605.00` | 1,700,000,000.00 USD | 498,430.00 USD | 0.00 USD | `+95.82%` | `108.24` |
| `Live` | `Short` | `4615.00` | 1,700,000,000.00 USD | 258,140.00 USD | 0.00 USD | `+96.24%` | `55.93` |
| `Live` | `Short` | `4625.00` | 1,700,000,000.00 USD | 776,590.00 USD | 0.00 USD | `+96.67%` | `167.91` |
| `Live` | `Short` | `4635.00` | 1,700,000,000.00 USD | 70,800.00 USD | 0.00 USD | `+97.09%` | `15.28` |
| `Live` | `Short` | `4645.00` | 1,700,000,000.00 USD | 2,110,000.00 USD | 0.00 USD | `+97.52%` | `454.35` |
| `Live` | `Short` | `4655.00` | 1,700,000,000.00 USD | 443,600.00 USD | 0.00 USD | `+97.94%` | `95.29` |
| `Live` | `Short` | `4665.00` | 1,700,000,000.00 USD | 398.86 USD | 0.00 USD | `+98.37%` | `0.09` |
| `Live` | `Short` | `4675.00` | 1,700,000,000.00 USD | 5,710.00 USD | 0.00 USD | `+98.79%` | `1.22` |
| `Live` | `Short` | `4685.00` | 1,700,000,000.00 USD | 990,380.00 USD | 0.00 USD | `+99.22%` | `211.39` |
| `Live` | `Short` | `4695.00` | 1,700,000,000.00 USD | 32,300.00 USD | 0.00 USD | `+99.64%` | `6.88` |
| `Live` | `Short` | `4705.00` | 1,700,000,000.00 USD | 2,730.00 USD | 0.00 USD | `+100.07%` | `0.58` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `505.00` | 1,500,000,000.00 USD | 0.00 USD | 16,940.00 USD | `-78.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.00` | 1,500,000,000.00 USD | 0.00 USD | 563.16 USD | `-76.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.00` | 1,500,000,000.00 USD | 0.00 USD | 383.31 USD | `-70.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `755.00` | 1,500,000,000.00 USD | 0.00 USD | 177.27 USD | `-67.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `795.00` | 1,500,000,000.00 USD | 0.00 USD | 104.22 USD | `-66.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `805.00` | 1,500,000,000.00 USD | 0.00 USD | 2,090.00 USD | `-65.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `835.00` | 1,500,000,000.00 USD | 0.00 USD | 1,670.00 USD | `-64.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `865.00` | 1,500,000,000.00 USD | 0.00 USD | 139,280.00 USD | `-63.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `885.00` | 1,500,000,000.00 USD | 0.00 USD | 3,130.00 USD | `-62.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `905.00` | 1,500,000,000.00 USD | 0.00 USD | 2,780.00 USD | `-61.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `985.00` | 1,500,000,000.00 USD | 0.00 USD | 516.34 USD | `-58.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `995.00` | 1,500,000,000.00 USD | 0.00 USD | 100.50 USD | `-57.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1005.00` | 1,500,000,000.00 USD | 0.00 USD | 222,040.00 USD | `-57.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1025.00` | 1,500,000,000.00 USD | 0.00 USD | 112.03 USD | `-56.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1065.00` | 1,500,000,000.00 USD | 0.00 USD | 1,060.00 USD | `-54.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1075.00` | 1,500,000,000.00 USD | 0.00 USD | 995.34 USD | `-54.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1105.00` | 1,500,000,000.00 USD | 0.00 USD | 1,610.00 USD | `-53.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1115.00` | 1,500,000,000.00 USD | 0.00 USD | 11,050.00 USD | `-52.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1125.00` | 1,500,000,000.00 USD | 0.00 USD | 1,320.00 USD | `-52.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1155.00` | 1,500,000,000.00 USD | 0.00 USD | 1,000.00 USD | `-50.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1175.00` | 1,500,000,000.00 USD | 0.00 USD | 203.98 USD | `-50.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1185.00` | 1,500,000,000.00 USD | 0.00 USD | 228.47 USD | `-49.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1205.00` | 1,500,000,000.00 USD | 0.00 USD | 27,760.00 USD | `-48.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1225.00` | 1,500,000,000.00 USD | 0.00 USD | 995.93 USD | `-47.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1245.00` | 1,500,000,000.00 USD | 0.00 USD | 951.93 USD | `-47.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1255.00` | 1,500,000,000.00 USD | 0.00 USD | 6,810.00 USD | `-46.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1285.00` | 1,500,000,000.00 USD | 0.00 USD | 9,050.00 USD | `-45.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1295.00` | 1,500,000,000.00 USD | 0.00 USD | 7,030.00 USD | `-44.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1305.00` | 1,500,000,000.00 USD | 0.00 USD | 23,030.00 USD | `-44.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1315.00` | 1,500,000,000.00 USD | 0.00 USD | 1,440.00 USD | `-44.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1345.00` | 1,500,000,000.00 USD | 0.00 USD | 141,950.00 USD | `-42.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1355.00` | 1,500,000,000.00 USD | 0.00 USD | 128.86 USD | `-42.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1375.00` | 1,500,000,000.00 USD | 0.00 USD | 4,160.00 USD | `-41.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1395.00` | 1,500,000,000.00 USD | 0.00 USD | 535,600.00 USD | `-40.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1405.00` | 1,500,000,000.00 USD | 0.00 USD | 20,270.00 USD | `-40.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1425.00` | 1,500,000,000.00 USD | 0.00 USD | 6,450.00 USD | `-39.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1435.00` | 1,500,000,000.00 USD | 0.00 USD | 852.10 USD | `-38.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1445.00` | 1,500,000,000.00 USD | 0.00 USD | 1,490.00 USD | `-38.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1455.00` | 1,500,000,000.00 USD | 0.00 USD | 5,680.00 USD | `-38.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1465.00` | 1,500,000,000.00 USD | 0.00 USD | 19,350.00 USD | `-37.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1475.00` | 1,500,000,000.00 USD | 0.00 USD | 2,600.00 USD | `-37.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1485.00` | 1,500,000,000.00 USD | 0.00 USD | 18,710.00 USD | `-36.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1495.00` | 1,500,000,000.00 USD | 0.00 USD | 11,460.00 USD | `-36.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1505.00` | 1,500,000,000.00 USD | 0.00 USD | 78,910.00 USD | `-36.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1515.00` | 1,500,000,000.00 USD | 0.00 USD | 11,140.00 USD | `-35.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1525.00` | 1,500,000,000.00 USD | 0.00 USD | 32,310.00 USD | `-35.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1535.00` | 1,500,000,000.00 USD | 0.00 USD | 983.78 USD | `-34.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1545.00` | 1,500,000,000.00 USD | 0.00 USD | 17,470.00 USD | `-34.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1555.00` | 1,500,000,000.00 USD | 0.00 USD | 4,210.00 USD | `-33.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1565.00` | 1,500,000,000.00 USD | 0.00 USD | 6,260.00 USD | `-33.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1575.00` | 1,500,000,000.00 USD | 0.00 USD | 190,890.00 USD | `-33.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1585.00` | 1,500,000,000.00 USD | 0.00 USD | 3,390.00 USD | `-32.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1595.00` | 1,500,000,000.00 USD | 0.00 USD | 4,040.00 USD | `-32.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1605.00` | 1,500,000,000.00 USD | 0.00 USD | 435,900.00 USD | `-31.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1615.00` | 1,500,000,000.00 USD | 0.00 USD | 25,840.00 USD | `-31.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1625.00` | 1,500,000,000.00 USD | 0.00 USD | 13,590.00 USD | `-30.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1635.00` | 1,500,000,000.00 USD | 0.00 USD | 5,510.00 USD | `-30.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1645.00` | 1,500,000,000.00 USD | 0.00 USD | 328,140.00 USD | `-30.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1655.00` | 1,500,000,000.00 USD | 0.00 USD | 22,220.00 USD | `-29.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1665.00` | 1,500,000,000.00 USD | 0.00 USD | 3,110.00 USD | `-29.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1675.00` | 1,500,000,000.00 USD | 0.00 USD | 3,440.00 USD | `-28.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1685.00` | 1,500,000,000.00 USD | 0.00 USD | 58,890.00 USD | `-28.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1695.00` | 1,500,000,000.00 USD | 0.00 USD | 6,800.00 USD | `-27.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1705.00` | 1,500,000,000.00 USD | 0.00 USD | 81,190.00 USD | `-27.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1715.00` | 1,500,000,000.00 USD | 0.00 USD | 28,180.00 USD | `-27.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1725.00` | 1,500,000,000.00 USD | 0.00 USD | 47,500.00 USD | `-26.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1735.00` | 1,500,000,000.00 USD | 0.00 USD | 28,150.00 USD | `-26.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1745.00` | 1,500,000,000.00 USD | 0.00 USD | 3,180.00 USD | `-25.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1755.00` | 1,500,000,000.00 USD | 0.00 USD | 498,120.00 USD | `-25.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1765.00` | 1,500,000,000.00 USD | 0.00 USD | 75,630.00 USD | `-24.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1775.00` | 1,500,000,000.00 USD | 0.00 USD | 3,090.00 USD | `-24.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1785.00` | 1,500,000,000.00 USD | 0.00 USD | 4,930.00 USD | `-24.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1795.00` | 1,500,000,000.00 USD | 0.00 USD | 184,330.00 USD | `-23.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1805.00` | 1,500,000,000.00 USD | 0.00 USD | 238,740.00 USD | `-23.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1815.00` | 1,500,000,000.00 USD | 0.00 USD | 114,830.00 USD | `-22.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1825.00` | 1,500,000,000.00 USD | 0.00 USD | 26,790.00 USD | `-22.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1835.00` | 1,500,000,000.00 USD | 0.00 USD | 2,500.00 USD | `-21.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1845.00` | 1,500,000,000.00 USD | 0.00 USD | 9,040.00 USD | `-21.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1855.00` | 1,500,000,000.00 USD | 0.00 USD | 467,010.00 USD | `-21.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1865.00` | 1,500,000,000.00 USD | 0.00 USD | 32,910.00 USD | `-20.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1875.00` | 1,500,000,000.00 USD | 0.00 USD | 18,210,000.00 USD | `-20.27%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1885.00` | 1,480,000,000.00 USD | 0.00 USD | 2,390.00 USD | `-19.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1895.00` | 1,480,000,000.00 USD | 0.00 USD | 61,700.00 USD | `-19.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1905.00` | 1,480,000,000.00 USD | 0.00 USD | 162,190.00 USD | `-18.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1915.00` | 1,480,000,000.00 USD | 0.00 USD | 8,110,000.00 USD | `-18.57%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1925.00` | 1,470,000,000.00 USD | 0.00 USD | 16,410,000.00 USD | `-18.14%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1935.00` | 1,460,000,000.00 USD | 0.00 USD | 79,950.00 USD | `-17.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1945.00` | 1,460,000,000.00 USD | 0.00 USD | 44,850.00 USD | `-17.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1955.00` | 1,460,000,000.00 USD | 0.00 USD | 52,220.00 USD | `-16.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1965.00` | 1,460,000,000.00 USD | 0.00 USD | 510.51 USD | `-16.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1975.00` | 1,460,000,000.00 USD | 0.00 USD | 59,770.00 USD | `-16.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1985.00` | 1,460,000,000.00 USD | 0.00 USD | 95,270.00 USD | `-15.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1995.00` | 1,460,000,000.00 USD | 0.00 USD | 164,110.00 USD | `-15.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2005.00` | 1,460,000,000.00 USD | 0.00 USD | 1,320,000.00 USD | `-14.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2015.00` | 1,460,000,000.00 USD | 0.00 USD | 69,640.00 USD | `-14.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2025.00` | 1,460,000,000.00 USD | 0.00 USD | 5,040.00 USD | `-13.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2035.00` | 1,460,000,000.00 USD | 0.00 USD | 103,890.00 USD | `-13.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2045.00` | 1,450,000,000.00 USD | 0.00 USD | 15,220.00 USD | `-13.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2055.00` | 1,450,000,000.00 USD | 0.00 USD | 140,840.00 USD | `-12.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2065.00` | 1,450,000,000.00 USD | 0.00 USD | 47,480.00 USD | `-12.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2075.00` | 1,450,000,000.00 USD | 0.00 USD | 76,450.00 USD | `-11.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2085.00` | 1,450,000,000.00 USD | 0.00 USD | 52,030.00 USD | `-11.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2095.00` | 1,450,000,000.00 USD | 0.00 USD | 29,710.00 USD | `-10.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2105.00` | 1,450,000,000.00 USD | 0.00 USD | 330,470.00 USD | `-10.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2115.00` | 1,450,000,000.00 USD | 0.00 USD | 119,630.00 USD | `-10.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2125.00` | 1,450,000,000.00 USD | 0.00 USD | 81,460.00 USD | `-9.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2135.00` | 1,450,000,000.00 USD | 0.00 USD | 19,470.00 USD | `-9.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2145.00` | 1,450,000,000.00 USD | 0.00 USD | 217,830.00 USD | `-8.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2155.00` | 1,450,000,000.00 USD | 0.00 USD | 104,580.00 USD | `-8.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2165.00` | 1,450,000,000.00 USD | 0.00 USD | 871,350.00 USD | `-7.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2175.00` | 1,450,000,000.00 USD | 0.00 USD | 1,360,000.00 USD | `-7.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2185.00` | 1,450,000,000.00 USD | 0.00 USD | 92,000.00 USD | `-7.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2195.00` | 1,450,000,000.00 USD | 0.00 USD | 438,560.00 USD | `-6.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2205.00` | 1,450,000,000.00 USD | 0.00 USD | 2,140,000.00 USD | `-6.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2215.00` | 1,450,000,000.00 USD | 0.00 USD | 1,020,000.00 USD | `-5.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2225.00` | 1,450,000,000.00 USD | 0.00 USD | 992,450.00 USD | `-5.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2235.00` | 1,450,000,000.00 USD | 0.00 USD | 125,690.00 USD | `-4.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2245.00` | 1,450,000,000.00 USD | 0.00 USD | 1,590,000.00 USD | `-4.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2255.00` | 1,450,000,000.00 USD | 0.00 USD | 23,250,000.00 USD | `-4.11%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2265.00` | 1,420,000,000.00 USD | 0.00 USD | 653,600.00 USD | `-3.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2275.00` | 1,420,000,000.00 USD | 0.00 USD | 4,680,000.00 USD | `-3.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2285.00` | 1,420,000,000.00 USD | 0.00 USD | 4,200,000.00 USD | `-2.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2295.00` | 1,410,000,000.00 USD | 0.00 USD | 10,550,000.00 USD | `-2.41%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2305.00` | 1,400,000,000.00 USD | 0.00 USD | 1,390,000,000.00 USD | `-1.99%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2315.00` | 15,990,000.00 USD | 0.00 USD | 11,460,000.00 USD | `-1.56%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2325.00` | 4,520,000.00 USD | 0.00 USD | 1,610,000.00 USD | `-1.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2335.00` | 2,910,000.00 USD | 0.00 USD | 1,900,000.00 USD | `-0.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2345.00` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | `-0.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2355.00` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | `+0.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2365.00` | 1,120,000.00 USD | 102,380.00 USD | 0.00 USD | `+0.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2375.00` | 2,190,000.00 USD | 1,070,000.00 USD | 0.00 USD | `+0.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2385.00` | 4,190,000.00 USD | 2,000,000.00 USD | 0.00 USD | `+1.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2395.00` | 15,070,000.00 USD | 10,880,000.00 USD | 0.00 USD | `+1.84%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2405.00` | 17,390,000.00 USD | 2,320,000.00 USD | 0.00 USD | `+2.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2415.00` | 18,550,000.00 USD | 1,160,000.00 USD | 0.00 USD | `+2.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2425.00` | 22,060,000.00 USD | 3,510,000.00 USD | 0.00 USD | `+3.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2435.00` | 22,540,000.00 USD | 482,650.00 USD | 0.00 USD | `+3.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2445.00` | 33,060,000.00 USD | 10,520,000.00 USD | 0.00 USD | `+3.97%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2455.00` | 33,290,000.00 USD | 233,060.00 USD | 0.00 USD | `+4.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2465.00` | 35,470,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+4.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2475.00` | 35,790,000.00 USD | 327,070.00 USD | 0.00 USD | `+5.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2485.00` | 37,950,000.00 USD | 2,150,000.00 USD | 0.00 USD | `+5.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2495.00` | 38,430,000.00 USD | 486,690.00 USD | 0.00 USD | `+6.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2505.00` | 43,740,000.00 USD | 5,300,000.00 USD | 0.00 USD | `+6.52%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2515.00` | 51,510,000.00 USD | 7,780,000.00 USD | 0.00 USD | `+6.94%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2525.00` | 54,720,000.00 USD | 3,200,000.00 USD | 0.00 USD | `+7.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2535.00` | 54,790,000.00 USD | 72,580.00 USD | 0.00 USD | `+7.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2545.00` | 56,960,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+8.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2555.00` | 57,290,000.00 USD | 332,460.00 USD | 0.00 USD | `+8.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2565.00` | 59,630,000.00 USD | 2,330,000.00 USD | 0.00 USD | `+9.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2575.00` | 59,780,000.00 USD | 154,870.00 USD | 0.00 USD | `+9.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2585.00` | 62,240,000.00 USD | 2,450,000.00 USD | 0.00 USD | `+9.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2595.00` | 62,250,000.00 USD | 14,590.00 USD | 0.00 USD | `+10.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2605.00` | 65,350,000.00 USD | 3,100,000.00 USD | 0.00 USD | `+10.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2615.00` | 65,570,000.00 USD | 218,380.00 USD | 0.00 USD | `+11.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2625.00` | 67,760,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+11.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2635.00` | 68,060,000.00 USD | 303,700.00 USD | 0.00 USD | `+12.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2645.00` | 70,230,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+12.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2655.00` | 70,520,000.00 USD | 285,850.00 USD | 0.00 USD | `+12.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2665.00` | 72,670,000.00 USD | 2,160,000.00 USD | 0.00 USD | `+13.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2675.00` | 73,070,000.00 USD | 393,350.00 USD | 0.00 USD | `+13.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2685.00` | 75,250,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+14.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2695.00` | 75,430,000.00 USD | 175,980.00 USD | 0.00 USD | `+14.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2705.00` | 80,060,000.00 USD | 4,630,000.00 USD | 0.00 USD | `+15.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2715.00` | 80,140,000.00 USD | 76,900.00 USD | 0.00 USD | `+15.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2725.00` | 82,600,000.00 USD | 2,470,000.00 USD | 0.00 USD | `+15.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2735.00` | 82,660,000.00 USD | 55,720.00 USD | 0.00 USD | `+16.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2745.00` | 84,960,000.00 USD | 2,300,000.00 USD | 0.00 USD | `+16.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2755.00` | 86,480,000.00 USD | 1,510,000.00 USD | 0.00 USD | `+17.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2765.00` | 88,860,000.00 USD | 2,380,000.00 USD | 0.00 USD | `+17.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2775.00` | 89,480,000.00 USD | 620,300.00 USD | 0.00 USD | `+18.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2785.00` | 91,780,000.00 USD | 2,300,000.00 USD | 0.00 USD | `+18.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2795.00` | 91,810,000.00 USD | 36,990.00 USD | 0.00 USD | `+18.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2805.00` | 94,960,000.00 USD | 3,140,000.00 USD | 0.00 USD | `+19.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2815.00` | 95,010,000.00 USD | 53,260.00 USD | 0.00 USD | `+19.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2825.00` | 95,070,000.00 USD | 62,020.00 USD | 0.00 USD | `+20.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2835.00` | 95,360,000.00 USD | 289,110.00 USD | 0.00 USD | `+20.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2845.00` | 96,370,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+20.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2855.00` | 97,650,000.00 USD | 1,280,000.00 USD | 0.00 USD | `+21.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2865.00` | 97,660,000.00 USD | 10,290.00 USD | 0.00 USD | `+21.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2875.00` | 97,670,000.00 USD | 3,630.00 USD | 0.00 USD | `+22.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2885.00` | 97,960,000.00 USD | 290,880.00 USD | 0.00 USD | `+22.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2895.00` | 97,980,000.00 USD | 23,020.00 USD | 0.00 USD | `+23.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2905.00` | 99,940,000.00 USD | 1,960,000.00 USD | 0.00 USD | `+23.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2915.00` | 99,950,000.00 USD | 10,340.00 USD | 0.00 USD | `+23.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2925.00` | 99,950,000.00 USD | 3,040.00 USD | 0.00 USD | `+24.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2935.00` | 100,010,000.00 USD | 54,540.00 USD | 0.00 USD | `+24.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2945.00` | 100,040,000.00 USD | 34,650.00 USD | 0.00 USD | `+25.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2955.00` | 100,120,000.00 USD | 74,770.00 USD | 0.00 USD | `+25.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2965.00` | 100,230,000.00 USD | 111,790.00 USD | 0.00 USD | `+26.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2975.00` | 100,380,000.00 USD | 148,070.00 USD | 0.00 USD | `+26.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2985.00` | 104,460,000.00 USD | 4,090,000.00 USD | 0.00 USD | `+26.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2995.00` | 106,380,000.00 USD | 1,920,000.00 USD | 0.00 USD | `+27.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3005.00` | 108,370,000.00 USD | 1,990,000.00 USD | 0.00 USD | `+27.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3015.00` | 108,380,000.00 USD | 6,950.00 USD | 0.00 USD | `+28.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3025.00` | 108,420,000.00 USD | 37,410.00 USD | 0.00 USD | `+28.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3035.00` | 108,490,000.00 USD | 70,360.00 USD | 0.00 USD | `+29.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3045.00` | 108,510,000.00 USD | 22,460.00 USD | 0.00 USD | `+29.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3055.00` | 109,300,000.00 USD | 786,100.00 USD | 0.00 USD | `+29.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3065.00` | 109,300,000.00 USD | 3,080.00 USD | 0.00 USD | `+30.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3075.00` | 109,350,000.00 USD | 50,370.00 USD | 0.00 USD | `+30.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3085.00` | 109,370,000.00 USD | 19,860.00 USD | 0.00 USD | `+31.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3095.00` | 109,400,000.00 USD | 34,020.00 USD | 0.00 USD | `+31.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3105.00` | 122,810,000.00 USD | 13,410,000.00 USD | 0.00 USD | `+32.03%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `3115.00` | 122,930,000.00 USD | 118,040.00 USD | 0.00 USD | `+32.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3125.00` | 123,280,000.00 USD | 352,160.00 USD | 0.00 USD | `+32.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3145.00` | 123,290,000.00 USD | 1,860.00 USD | 0.00 USD | `+33.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3155.00` | 123,350,000.00 USD | 68,940.00 USD | 0.00 USD | `+34.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3165.00` | 123,360,000.00 USD | 9,860.00 USD | 0.00 USD | `+34.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3175.00` | 123,380,000.00 USD | 16,410.00 USD | 0.00 USD | `+35.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3185.00` | 123,380,000.00 USD | 1,330.00 USD | 0.00 USD | `+35.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3195.00` | 123,410,000.00 USD | 29,580.00 USD | 0.00 USD | `+35.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3205.00` | 124,320,000.00 USD | 910,780.00 USD | 0.00 USD | `+36.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3215.00` | 124,320,000.00 USD | 1,290.00 USD | 0.00 USD | `+36.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3225.00` | 124,330,000.00 USD | 3,740.00 USD | 0.00 USD | `+37.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3235.00` | 124,360,000.00 USD | 31,330.00 USD | 0.00 USD | `+37.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3245.00` | 124,410,000.00 USD | 56,110.00 USD | 0.00 USD | `+37.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3255.00` | 124,620,000.00 USD | 204,030.00 USD | 0.00 USD | `+38.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3265.00` | 124,630,000.00 USD | 15,710.00 USD | 0.00 USD | `+38.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3275.00` | 124,640,000.00 USD | 1,630.00 USD | 0.00 USD | `+39.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3285.00` | 124,780,000.00 USD | 142,210.00 USD | 0.00 USD | `+39.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3295.00` | 124,790,000.00 USD | 16,780.00 USD | 0.00 USD | `+40.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3305.00` | 126,060,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+40.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3315.00` | 126,450,000.00 USD | 385,510.00 USD | 0.00 USD | `+40.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3325.00` | 126,470,000.00 USD | 18,270.00 USD | 0.00 USD | `+41.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3335.00` | 126,480,000.00 USD | 14,190.00 USD | 0.00 USD | `+41.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3345.00` | 126,480,000.00 USD | 617.15 USD | 0.00 USD | `+42.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3355.00` | 126,480,000.00 USD | 334.49 USD | 0.00 USD | `+42.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3365.00` | 126,480,000.00 USD | 597.29 USD | 0.00 USD | `+43.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3375.00` | 126,510,000.00 USD | 23,460.00 USD | 0.00 USD | `+43.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3385.00` | 126,570,000.00 USD | 58,010.00 USD | 0.00 USD | `+43.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3395.00` | 126,920,000.00 USD | 355,050.00 USD | 0.00 USD | `+44.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3405.00` | 128,520,000.00 USD | 1,600,000.00 USD | 0.00 USD | `+44.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3415.00` | 128,530,000.00 USD | 3,510.00 USD | 0.00 USD | `+45.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3425.00` | 128,540,000.00 USD | 16,310.00 USD | 0.00 USD | `+45.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3445.00` | 128,560,000.00 USD | 15,030.00 USD | 0.00 USD | `+46.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3455.00` | 128,580,000.00 USD | 18,600.00 USD | 0.00 USD | `+46.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3465.00` | 128,890,000.00 USD | 311,800.00 USD | 0.00 USD | `+47.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3475.00` | 128,890,000.00 USD | 2,980.00 USD | 0.00 USD | `+47.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3485.00` | 128,930,000.00 USD | 43,610.00 USD | 0.00 USD | `+48.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3495.00` | 128,930,000.00 USD | 158.32 USD | 0.00 USD | `+48.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3505.00` | 129,480,000.00 USD | 550,300.00 USD | 0.00 USD | `+49.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3515.00` | 129,530,000.00 USD | 43,200.00 USD | 0.00 USD | `+49.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3525.00` | 129,530,000.00 USD | 3,690.00 USD | 0.00 USD | `+49.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3535.00` | 129,540,000.00 USD | 9,810.00 USD | 0.00 USD | `+50.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3545.00` | 129,540,000.00 USD | 179.38 USD | 0.00 USD | `+50.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3555.00` | 129,630,000.00 USD | 90,810.00 USD | 0.00 USD | `+51.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3565.00` | 129,630,000.00 USD | 2,300.00 USD | 0.00 USD | `+51.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3585.00` | 129,630,000.00 USD | 354.92 USD | 0.00 USD | `+52.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3595.00` | 129,650,000.00 USD | 13,160.00 USD | 0.00 USD | `+52.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3605.00` | 129,750,000.00 USD | 105,860.00 USD | 0.00 USD | `+53.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3625.00` | 129,760,000.00 USD | 10,210.00 USD | 0.00 USD | `+54.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3635.00` | 129,770,000.00 USD | 7,790.00 USD | 0.00 USD | `+54.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3645.00` | 129,780,000.00 USD | 3,860.00 USD | 0.00 USD | `+54.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3655.00` | 129,780,000.00 USD | 7,740.00 USD | 0.00 USD | `+55.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3665.00` | 129,790,000.00 USD | 8,130.00 USD | 0.00 USD | `+55.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3675.00` | 129,850,000.00 USD | 55,120.00 USD | 0.00 USD | `+56.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3685.00` | 129,850,000.00 USD | 3,550.00 USD | 0.00 USD | `+56.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3705.00` | 129,850,000.00 USD | 819.92 USD | 0.00 USD | `+57.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3715.00` | 129,850,000.00 USD | 323.58 USD | 0.00 USD | `+57.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3725.00` | 129,850,000.00 USD | 1,400.00 USD | 0.00 USD | `+58.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3735.00` | 129,860,000.00 USD | 6,490.00 USD | 0.00 USD | `+58.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3755.00` | 129,860,000.00 USD | 751.00 USD | 0.00 USD | `+59.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3785.00` | 129,860,000.00 USD | 286.90 USD | 0.00 USD | `+60.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3795.00` | 129,860,000.00 USD | 1,560.00 USD | 0.00 USD | `+61.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3805.00` | 130,600,000.00 USD | 734,090.00 USD | 0.00 USD | `+61.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3815.00` | 130,620,000.00 USD | 20,930.00 USD | 0.00 USD | `+62.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3825.00` | 130,620,000.00 USD | 8,380.00 USD | 0.00 USD | `+62.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3835.00` | 130,630,000.00 USD | 711.78 USD | 0.00 USD | `+63.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3845.00` | 130,630,000.00 USD | 932.03 USD | 0.00 USD | `+63.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3855.00` | 130,830,000.00 USD | 203,880.00 USD | 0.00 USD | `+63.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3875.00` | 130,870,000.00 USD | 41,200.00 USD | 0.00 USD | `+64.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3885.00` | 130,890,000.00 USD | 21,210.00 USD | 0.00 USD | `+65.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3905.00` | 131,070,000.00 USD | 180,010.00 USD | 0.00 USD | `+66.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3915.00` | 131,720,000.00 USD | 646,840.00 USD | 0.00 USD | `+66.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3925.00` | 131,720,000.00 USD | 3,260.00 USD | 0.00 USD | `+66.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3935.00` | 131,770,000.00 USD | 42,570.00 USD | 0.00 USD | `+67.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3945.00` | 131,790,000.00 USD | 19,730.00 USD | 0.00 USD | `+67.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3955.00` | 131,790,000.00 USD | 1,380.00 USD | 0.00 USD | `+68.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3965.00` | 131,790,000.00 USD | 323.54 USD | 0.00 USD | `+68.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3975.00` | 131,790,000.00 USD | 6,960.00 USD | 0.00 USD | `+69.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3985.00` | 131,810,000.00 USD | 14,610.00 USD | 0.00 USD | `+69.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3995.00` | 131,810,000.00 USD | 4,280.00 USD | 0.00 USD | `+69.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4005.00` | 134,490,000.00 USD | 2,680,000.00 USD | 0.00 USD | `+70.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4035.00` | 134,490,000.00 USD | 898.59 USD | 0.00 USD | `+71.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4055.00` | 134,490,000.00 USD | 811.00 USD | 0.00 USD | `+72.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4075.00` | 134,500,000.00 USD | 4,310.00 USD | 0.00 USD | `+73.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4085.00` | 134,500,000.00 USD | 2,800.00 USD | 0.00 USD | `+73.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4095.00` | 134,500,000.00 USD | 2,750.00 USD | 0.00 USD | `+74.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4105.00` | 134,550,000.00 USD | 43,660.00 USD | 0.00 USD | `+74.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4115.00` | 134,550,000.00 USD | 5,990.00 USD | 0.00 USD | `+74.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4125.00` | 134,550,000.00 USD | 372.90 USD | 0.00 USD | `+75.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4145.00` | 134,550,000.00 USD | 395.43 USD | 0.00 USD | `+76.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4175.00` | 134,560,000.00 USD | 2,890.00 USD | 0.00 USD | `+77.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4185.00` | 134,560,000.00 USD | 376.65 USD | 0.00 USD | `+77.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4205.00` | 134,590,000.00 USD | 28,760.00 USD | 0.00 USD | `+78.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4215.00` | 134,590,000.00 USD | 460.70 USD | 0.00 USD | `+79.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4225.00` | 134,590,000.00 USD | 1,270.00 USD | 0.00 USD | `+79.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4255.00` | 134,590,000.00 USD | 4,300.00 USD | 0.00 USD | `+80.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4265.00` | 134,600,000.00 USD | 4,010.00 USD | 0.00 USD | `+81.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4275.00` | 134,660,000.00 USD | 64,550.00 USD | 0.00 USD | `+81.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4285.00` | 134,660,000.00 USD | 1,610.00 USD | 0.00 USD | `+82.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4305.00` | 134,760,000.00 USD | 97,670.00 USD | 0.00 USD | `+83.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4315.00` | 134,760,000.00 USD | 1,070.00 USD | 0.00 USD | `+83.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4345.00` | 134,770,000.00 USD | 11,270.00 USD | 0.00 USD | `+84.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4355.00` | 134,770,000.00 USD | 3,250.00 USD | 0.00 USD | `+85.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4375.00` | 134,820,000.00 USD | 43,750.00 USD | 0.00 USD | `+86.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4385.00` | 134,880,000.00 USD | 64,570.00 USD | 0.00 USD | `+86.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4395.00` | 134,880,000.00 USD | 1,050.00 USD | 0.00 USD | `+86.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4405.00` | 136,110,000.00 USD | 1,230,000.00 USD | 0.00 USD | `+87.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4415.00` | 136,120,000.00 USD | 11,480.00 USD | 0.00 USD | `+87.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4425.00` | 136,120,000.00 USD | 2,510.00 USD | 0.00 USD | `+88.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4435.00` | 136,300,000.00 USD | 177,400.00 USD | 0.00 USD | `+88.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4455.00` | 136,300,000.00 USD | 641.97 USD | 0.00 USD | `+89.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4505.00` | 136,650,000.00 USD | 343,680.00 USD | 0.00 USD | `+91.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4515.00` | 136,650,000.00 USD | 2,280.00 USD | 0.00 USD | `+91.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4525.00` | 136,650,000.00 USD | 6,560.00 USD | 0.00 USD | `+92.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4545.00` | 136,850,000.00 USD | 197,950.00 USD | 0.00 USD | `+93.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4565.00` | 136,950,000.00 USD | 97,750.00 USD | 0.00 USD | `+94.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4585.00` | 136,950,000.00 USD | 1,420.00 USD | 0.00 USD | `+94.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4595.00` | 136,950,000.00 USD | 2,610.00 USD | 0.00 USD | `+95.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4605.00` | 137,020,000.00 USD | 64,120.00 USD | 0.00 USD | `+95.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4645.00` | 137,050,000.00 USD | 27,410.00 USD | 0.00 USD | `+97.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4655.00` | 137,220,000.00 USD | 174,790.00 USD | 0.00 USD | `+97.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4695.00` | 137,280,000.00 USD | 56,760.00 USD | 0.00 USD | `+99.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4705.00` | 137,280,000.00 USD | 4,740.00 USD | 0.00 USD | `+100.07%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `2068.70` | 2,690,000,000.00 USD | 0.00 USD | 2,690,000,000.00 USD | 1,890,000.00 USD | 1,910,000.00 USD | 939,150.00 USD |
| `7D` | `2071.50` | 2,690,000,000.00 USD | 0.00 USD | 2,690,000,000.00 USD | 2,760,000.00 USD | 1,510,000.00 USD | 1,220,000.00 USD |
| `7D` | `2074.30` | 2,680,000,000.00 USD | 0.00 USD | 2,680,000,000.00 USD | 3,850,000.00 USD | 2,610,000.00 USD | 2,930,000.00 USD |
| `7D` | `2077.10` | 2,670,000,000.00 USD | 0.00 USD | 2,670,000,000.00 USD | 4,430,000.00 USD | 4,120,000.00 USD | 2,000,000.00 USD |
| `7D` | `2079.90` | 2,660,000,000.00 USD | 0.00 USD | 2,660,000,000.00 USD | 3,400,000.00 USD | 3,020,000.00 USD | 2,510,000.00 USD |
| `7D` | `2082.70` | 2,650,000,000.00 USD | 0.00 USD | 2,650,000,000.00 USD | 2,420,000.00 USD | 1,860,000.00 USD | 1,910,000.00 USD |
| `7D` | `2085.50` | 2,650,000,000.00 USD | 0.00 USD | 2,650,000,000.00 USD | 3,840,000.00 USD | 1,860,000.00 USD | 3,120,000.00 USD |
| `7D` | `2088.30` | 2,640,000,000.00 USD | 0.00 USD | 2,640,000,000.00 USD | 2,280,000.00 USD | 1,820,000.00 USD | 907,940.00 USD |
| `7D` | `2091.10` | 2,630,000,000.00 USD | 0.00 USD | 2,630,000,000.00 USD | 4,280,000.00 USD | 952,210.00 USD | 6,980,000.00 USD |
| `7D` | `2093.90` | 2,620,000,000.00 USD | 0.00 USD | 2,620,000,000.00 USD | 5,200,000.00 USD | 1,640,000.00 USD | 2,340,000.00 USD |
| `7D` | `2096.70` | 2,610,000,000.00 USD | 0.00 USD | 2,610,000,000.00 USD | 1,940,000.00 USD | 3,330,000.00 USD | 1,290,000.00 USD |
| `7D` | `2099.50` | 2,600,000,000.00 USD | 0.00 USD | 2,600,000,000.00 USD | 1,880,000.00 USD | 1,520,000.00 USD | 2,070,000.00 USD |
| `7D` | `2102.30` | 2,600,000,000.00 USD | 0.00 USD | 2,600,000,000.00 USD | 125,250.00 USD | 688,260.00 USD | 2,010,000.00 USD |
| `7D` | `2105.10` | 2,600,000,000.00 USD | 0.00 USD | 2,600,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 2,210,000.00 USD |
| `7D` | `2107.90` | 2,590,000,000.00 USD | 0.00 USD | 2,590,000,000.00 USD | 2,320,000.00 USD | 356,360.00 USD | 1,640,000.00 USD |
| `7D` | `2110.70` | 2,590,000,000.00 USD | 0.00 USD | 2,590,000,000.00 USD | 2,830,000.00 USD | 2,300,000.00 USD | 1,960,000.00 USD |
| `1D` | `2111.30` | 1,240,000,000.00 USD | 0.00 USD | 1,240,000,000.00 USD | 1,250,000.00 USD | 343,530.00 USD | 525,670.00 USD |
| `7D` | `2113.50` | 2,580,000,000.00 USD | 0.00 USD | 2,580,000,000.00 USD | 1,730,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD |
| `1D` | `2113.90` | 1,240,000,000.00 USD | 0.00 USD | 1,240,000,000.00 USD | 1,090,000.00 USD | 1,080,000.00 USD | 363,830.00 USD |
| `7D` | `2116.30` | 2,570,000,000.00 USD | 0.00 USD | 2,570,000,000.00 USD | 1,480,000.00 USD | 2,030,000.00 USD | 2,570,000.00 USD |
| `1D` | `2116.50` | 1,230,000,000.00 USD | 0.00 USD | 1,230,000,000.00 USD | 1,240,000.00 USD | 335,670.00 USD | 859,760.00 USD |
| `1D` | `2119.10` | 1,230,000,000.00 USD | 0.00 USD | 1,230,000,000.00 USD | 507,030.00 USD | 201,150.00 USD | 917,320.00 USD |
| `7D` | `2119.10` | 2,570,000,000.00 USD | 0.00 USD | 2,570,000,000.00 USD | 3,390,000.00 USD | 935,590.00 USD | 2,590,000.00 USD |
| `1D` | `2121.70` | 1,230,000,000.00 USD | 0.00 USD | 1,230,000,000.00 USD | 982,960.00 USD | 759,970.00 USD | 1,250,000.00 USD |
| `7D` | `2121.90` | 2,560,000,000.00 USD | 0.00 USD | 2,560,000,000.00 USD | 2,300,000.00 USD | 973,690.00 USD | 1,630,000.00 USD |
| `1D` | `2124.30` | 1,230,000,000.00 USD | 0.00 USD | 1,230,000,000.00 USD | 957,510.00 USD | 1,040,000.00 USD | 525,500.00 USD |
| `7D` | `2124.70` | 2,560,000,000.00 USD | 0.00 USD | 2,560,000,000.00 USD | 2,110,000.00 USD | 983,790.00 USD | 989,650.00 USD |
| `1D` | `2126.90` | 1,220,000,000.00 USD | 0.00 USD | 1,220,000,000.00 USD | 308,590.00 USD | 840,990.00 USD | 629,970.00 USD |
| `7D` | `2127.50` | 2,550,000,000.00 USD | 0.00 USD | 2,550,000,000.00 USD | 1,080,000.00 USD | 2,620,000.00 USD | 3,270,000.00 USD |
| `1D` | `2129.50` | 1,220,000,000.00 USD | 0.00 USD | 1,220,000,000.00 USD | 107,010.00 USD | 453,880.00 USD | 318,170.00 USD |
| `7D` | `2130.30` | 2,540,000,000.00 USD | 0.00 USD | 2,540,000,000.00 USD | 2,040,000.00 USD | 2,130,000.00 USD | 1,680,000.00 USD |
| `1D` | `2132.10` | 1,220,000,000.00 USD | 0.00 USD | 1,220,000,000.00 USD | 0.00 USD | 956,330.00 USD | 336,530.00 USD |
| `7D` | `2133.10` | 2,540,000,000.00 USD | 0.00 USD | 2,540,000,000.00 USD | 1,930,000.00 USD | 715,940.00 USD | 330,780.00 USD |
| `1D` | `2134.70` | 1,220,000,000.00 USD | 0.00 USD | 1,220,000,000.00 USD | 187,520.00 USD | 185,320.00 USD | 0.00 USD |
| `7D` | `2135.90` | 2,540,000,000.00 USD | 0.00 USD | 2,540,000,000.00 USD | 1,370,000.00 USD | 596,290.00 USD | 0.00 USD |
| `1D` | `2137.30` | 1,220,000,000.00 USD | 0.00 USD | 1,220,000,000.00 USD | 236,290.00 USD | 544,840.00 USD | 208,060.00 USD |
| `7D` | `2138.70` | 2,530,000,000.00 USD | 0.00 USD | 2,530,000,000.00 USD | 909,440.00 USD | 1,250,000.00 USD | 78,760.00 USD |
| `1D` | `2139.90` | 1,220,000,000.00 USD | 0.00 USD | 1,220,000,000.00 USD | 319,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2141.50` | 2,530,000,000.00 USD | 0.00 USD | 2,530,000,000.00 USD | 1,750,000.00 USD | 199,980.00 USD | 776,560.00 USD |
| `1D` | `2142.50` | 1,220,000,000.00 USD | 0.00 USD | 1,220,000,000.00 USD | 295,510.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2144.30` | 2,530,000,000.00 USD | 0.00 USD | 2,530,000,000.00 USD | 465,960.00 USD | 1,540,000.00 USD | 268,500.00 USD |
| `1D` | `2145.10` | 1,220,000,000.00 USD | 0.00 USD | 1,220,000,000.00 USD | 0.00 USD | 16,700.00 USD | 3,100.00 USD |
| `7D` | `2147.10` | 2,530,000,000.00 USD | 0.00 USD | 2,530,000,000.00 USD | 311,920.00 USD | 32,210.00 USD | 0.00 USD |
| `1D` | `2147.70` | 1,220,000,000.00 USD | 0.00 USD | 1,220,000,000.00 USD | 251,250.00 USD | 11,090.00 USD | 207,420.00 USD |
| `7D` | `2149.90` | 2,530,000,000.00 USD | 0.00 USD | 2,530,000,000.00 USD | 459,630.00 USD | 482,820.00 USD | 537,180.00 USD |
| `7D` | `2152.70` | 2,520,000,000.00 USD | 0.00 USD | 2,520,000,000.00 USD | 58,340.00 USD | 681,070.00 USD | 0.00 USD |
| `7D` | `2155.50` | 2,520,000,000.00 USD | 0.00 USD | 2,520,000,000.00 USD | 191,860.00 USD | 454,940.00 USD | 866,760.00 USD |
| `7D` | `2158.30` | 2,520,000,000.00 USD | 0.00 USD | 2,520,000,000.00 USD | 738,850.00 USD | 717,210.00 USD | 1,590,000.00 USD |
| `7D` | `2161.10` | 2,520,000,000.00 USD | 0.00 USD | 2,520,000,000.00 USD | 1,490,000.00 USD | 1,350,000.00 USD | 2,240,000.00 USD |
| `7D` | `2163.90` | 2,510,000,000.00 USD | 0.00 USD | 2,510,000,000.00 USD | 36,870.00 USD | 329,690.00 USD | 409,110.00 USD |
| `7D` | `2166.70` | 2,510,000,000.00 USD | 0.00 USD | 2,510,000,000.00 USD | 25,540.00 USD | 0.00 USD | 68,110.00 USD |
| `7D` | `2169.50` | 2,510,000,000.00 USD | 0.00 USD | 2,510,000,000.00 USD | 1,700,000.00 USD | 726,240.00 USD | 810,540.00 USD |
| `7D` | `2172.30` | 2,510,000,000.00 USD | 0.00 USD | 2,510,000,000.00 USD | 479,540.00 USD | 1,150,000.00 USD | 0.00 USD |
| `7D` | `2194.70` | 2,510,000,000.00 USD | 0.00 USD | 2,510,000,000.00 USD | 141,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2197.50` | 2,510,000,000.00 USD | 0.00 USD | 2,510,000,000.00 USD | 2,440,000.00 USD | 3,270,000.00 USD | 0.00 USD |
| `1D` | `2199.70` | 1,220,000,000.00 USD | 0.00 USD | 1,220,000,000.00 USD | 201,540.00 USD | 154,560.00 USD | 80,640.00 USD |
| `7D` | `2200.30` | 2,500,000,000.00 USD | 0.00 USD | 2,500,000,000.00 USD | 3,000,000.00 USD | 3,140,000.00 USD | 3,200,000.00 USD |
| `1D` | `2202.30` | 1,220,000,000.00 USD | 0.00 USD | 1,220,000,000.00 USD | 82,940.00 USD | 62,930.00 USD | 220,140.00 USD |
| `7D` | `2203.10` | 2,490,000,000.00 USD | 0.00 USD | 2,490,000,000.00 USD | 3,240,000.00 USD | 624,500.00 USD | 2,720,000.00 USD |
| `1D` | `2204.90` | 1,220,000,000.00 USD | 0.00 USD | 1,220,000,000.00 USD | 1,050,000.00 USD | 207,110.00 USD | 716,810.00 USD |
| `7D` | `2205.90` | 2,490,000,000.00 USD | 0.00 USD | 2,490,000,000.00 USD | 6,050,000.00 USD | 4,010,000.00 USD | 3,950,000.00 USD |
| `1D` | `2207.50` | 1,210,000,000.00 USD | 0.00 USD | 1,210,000,000.00 USD | 3,100,000.00 USD | 2,380,000.00 USD | 3,090,000.00 USD |
| `7D` | `2208.70` | 2,470,000,000.00 USD | 0.00 USD | 2,470,000,000.00 USD | 10,060,000.00 USD | 6,100,000.00 USD | 4,070,000.00 USD |
| `1D` | `2210.10` | 1,210,000,000.00 USD | 0.00 USD | 1,210,000,000.00 USD | 1,610,000.00 USD | 1,180,000.00 USD | 1,190,000.00 USD |
| `7D` | `2211.50` | 2,450,000,000.00 USD | 0.00 USD | 2,450,000,000.00 USD | 7,320,000.00 USD | 7,940,000.00 USD | 7,060,000.00 USD |
| `1D` | `2212.70` | 1,200,000,000.00 USD | 0.00 USD | 1,200,000,000.00 USD | 2,200,000.00 USD | 1,180,000.00 USD | 1,260,000.00 USD |
| `7D` | `2214.30` | 2,430,000,000.00 USD | 0.00 USD | 2,430,000,000.00 USD | 13,980,000.00 USD | 12,380,000.00 USD | 9,960,000.00 USD |
| `1D` | `2215.30` | 1,200,000,000.00 USD | 0.00 USD | 1,200,000,000.00 USD | 5,950,000.00 USD | 5,220,000.00 USD | 5,490,000.00 USD |
| `7D` | `2217.10` | 2,390,000,000.00 USD | 0.00 USD | 2,390,000,000.00 USD | 16,020,000.00 USD | 10,300,000.00 USD | 8,280,000.00 USD |
| `1D` | `2217.90` | 1,180,000,000.00 USD | 0.00 USD | 1,180,000,000.00 USD | 4,610,000.00 USD | 4,240,000.00 USD | 1,460,000.00 USD |
| `7D` | `2219.90` | 2,360,000,000.00 USD | 0.00 USD | 2,360,000,000.00 USD | 12,620,000.00 USD | 10,310,000.00 USD | 3,040,000.00 USD |
| `1D` | `2220.50` | 1,170,000,000.00 USD | 0.00 USD | 1,170,000,000.00 USD | 3,450,000.00 USD | 4,220,000.00 USD | 680,790.00 USD |
| `7D` | `2222.70` | 2,330,000,000.00 USD | 0.00 USD | 2,330,000,000.00 USD | 5,480,000.00 USD | 5,400,000.00 USD | 8,890,000.00 USD |
| `1D` | `2223.10` | 1,160,000,000.00 USD | 0.00 USD | 1,160,000,000.00 USD | 5,770,000.00 USD | 3,810,000.00 USD | 2,870,000.00 USD |
| `7D` | `2225.50` | 2,310,000,000.00 USD | 0.00 USD | 2,310,000,000.00 USD | 12,980,000.00 USD | 13,620,000.00 USD | 9,460,000.00 USD |
| `1D` | `2225.70` | 1,150,000,000.00 USD | 0.00 USD | 1,150,000,000.00 USD | 3,700,000.00 USD | 5,870,000.00 USD | 2,430,000.00 USD |
| `1D` | `2228.30` | 1,140,000,000.00 USD | 0.00 USD | 1,140,000,000.00 USD | 4,150,000.00 USD | 1,310,000.00 USD | 766,720.00 USD |
| `7D` | `2228.30` | 2,280,000,000.00 USD | 0.00 USD | 2,280,000,000.00 USD | 7,790,000.00 USD | 5,070,000.00 USD | 7,280,000.00 USD |
| `1D` | `2230.90` | 1,130,000,000.00 USD | 0.00 USD | 1,130,000,000.00 USD | 3,630,000.00 USD | 2,460,000.00 USD | 3,100,000.00 USD |
| `7D` | `2231.10` | 2,260,000,000.00 USD | 0.00 USD | 2,260,000,000.00 USD | 9,590,000.00 USD | 3,450,000.00 USD | 17,130,000.00 USD |
| `1D` | `2233.50` | 1,120,000,000.00 USD | 0.00 USD | 1,120,000,000.00 USD | 6,590,000.00 USD | 3,820,000.00 USD | 2,280,000.00 USD |
| `7D` | `2233.90` | 2,230,000,000.00 USD | 0.00 USD | 2,230,000,000.00 USD | 18,230,000.00 USD | 10,390,000.00 USD | 6,100,000.00 USD |
| `1D` | `2236.10` | 1,110,000,000.00 USD | 0.00 USD | 1,110,000,000.00 USD | 2,630,000.00 USD | 2,440,000.00 USD | 3,890,000.00 USD |
| `7D` | `2236.70` | 2,190,000,000.00 USD | 0.00 USD | 2,190,000,000.00 USD | 7,440,000.00 USD | 11,700,000.00 USD | 5,850,000.00 USD |
| `1D` | `2238.70` | 1,100,000,000.00 USD | 0.00 USD | 1,100,000,000.00 USD | 1,620,000.00 USD | 2,160,000.00 USD | 1,080,000.00 USD |
| `7D` | `2239.50` | 2,170,000,000.00 USD | 0.00 USD | 2,170,000,000.00 USD | 6,630,000.00 USD | 6,820,000.00 USD | 6,100,000.00 USD |
| `1D` | `2241.30` | 1,100,000,000.00 USD | 0.00 USD | 1,100,000,000.00 USD | 321,680.00 USD | 220,800.00 USD | 39,130.00 USD |
| `7D` | `2242.30` | 2,150,000,000.00 USD | 0.00 USD | 2,150,000,000.00 USD | 3,580,000.00 USD | 2,780,000.00 USD | 7,090,000.00 USD |
| `1D` | `2243.90` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 2,480,000.00 USD | 423,680.00 USD | 483,930.00 USD |
| `7D` | `2245.10` | 2,130,000,000.00 USD | 0.00 USD | 2,130,000,000.00 USD | 16,710,000.00 USD | 13,060,000.00 USD | 11,660,000.00 USD |
| `1D` | `2246.50` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 883,930.00 USD | 788,500.00 USD | 1,410,000.00 USD |
| `7D` | `2247.90` | 2,090,000,000.00 USD | 0.00 USD | 2,090,000,000.00 USD | 13,600,000.00 USD | 6,160,000.00 USD | 9,920,000.00 USD |
| `1D` | `2249.10` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 4,190,000.00 USD | 1,420,000.00 USD | 2,130,000.00 USD |
| `7D` | `2250.70` | 2,060,000,000.00 USD | 0.00 USD | 2,060,000,000.00 USD | 10,570,000.00 USD | 10,360,000.00 USD | 8,310,000.00 USD |
| `1D` | `2251.70` | 1,080,000,000.00 USD | 0.00 USD | 1,080,000,000.00 USD | 4,500,000.00 USD | 6,550,000.00 USD | 2,810,000.00 USD |
| `7D` | `2253.50` | 2,030,000,000.00 USD | 0.00 USD | 2,030,000,000.00 USD | 24,760,000.00 USD | 21,020,000.00 USD | 19,300,000.00 USD |
| `1D` | `2254.30` | 1,070,000,000.00 USD | 0.00 USD | 1,070,000,000.00 USD | 7,670,000.00 USD | 3,590,000.00 USD | 5,580,000.00 USD |
| `7D` | `2256.30` | 1,970,000,000.00 USD | 0.00 USD | 1,970,000,000.00 USD | 31,260,000.00 USD | 19,100,000.00 USD | 18,030,000.00 USD |
| `1D` | `2256.90` | 1,050,000,000.00 USD | 0.00 USD | 1,050,000,000.00 USD | 5,660,000.00 USD | 5,380,000.00 USD | 4,210,000.00 USD |
| `7D` | `2259.10` | 1,900,000,000.00 USD | 0.00 USD | 1,900,000,000.00 USD | 22,390,000.00 USD | 19,400,000.00 USD | 22,950,000.00 USD |
| `1D` | `2259.50` | 1,030,000,000.00 USD | 0.00 USD | 1,030,000,000.00 USD | 13,310,000.00 USD | 6,270,000.00 USD | 8,070,000.00 USD |
| `7D` | `2261.90` | 1,840,000,000.00 USD | 0.00 USD | 1,840,000,000.00 USD | 48,180,000.00 USD | 29,390,000.00 USD | 21,430,000.00 USD |
| `1D` | `2262.10` | 1,010,000,000.00 USD | 0.00 USD | 1,010,000,000.00 USD | 15,090,000.00 USD | 12,940,000.00 USD | 13,450,000.00 USD |
| `1D` | `2264.70` | 965,430,000.00 USD | 0.00 USD | 965,430,000.00 USD | 15,200,000.00 USD | 12,030,000.00 USD | 6,600,000.00 USD |
| `7D` | `2264.70` | 1,740,000,000.00 USD | 0.00 USD | 1,740,000,000.00 USD | 30,320,000.00 USD | 28,050,000.00 USD | 19,360,000.00 USD |
| `1D` | `2267.30` | 931,600,000.00 USD | 0.00 USD | 931,600,000.00 USD | 5,460,000.00 USD | 10,030,000.00 USD | 3,120,000.00 USD |
| `7D` | `2267.50` | 1,660,000,000.00 USD | 0.00 USD | 1,660,000,000.00 USD | 40,120,000.00 USD | 40,100,000.00 USD | 31,060,000.00 USD |
| `1D` | `2269.90` | 912,990,000.00 USD | 0.00 USD | 912,990,000.00 USD | 14,410,000.00 USD | 11,130,000.00 USD | 8,240,000.00 USD |
| `7D` | `2270.30` | 1,550,000,000.00 USD | 0.00 USD | 1,550,000,000.00 USD | 39,480,000.00 USD | 27,490,000.00 USD | 39,210,000.00 USD |
| `1D` | `2272.50` | 879,220,000.00 USD | 0.00 USD | 879,220,000.00 USD | 14,080,000.00 USD | 10,950,000.00 USD | 10,060,000.00 USD |
| `7D` | `2273.10` | 1,440,000,000.00 USD | 0.00 USD | 1,440,000,000.00 USD | 33,160,000.00 USD | 25,760,000.00 USD | 19,780,000.00 USD |
| `1D` | `2275.10` | 844,130,000.00 USD | 0.00 USD | 844,130,000.00 USD | 9,170,000.00 USD | 15,450,000.00 USD | 4,220,000.00 USD |
| `7D` | `2275.90` | 1,360,000,000.00 USD | 0.00 USD | 1,360,000,000.00 USD | 48,240,000.00 USD | 42,710,000.00 USD | 44,210,000.00 USD |
| `1D` | `2277.70` | 815,280,000.00 USD | 0.00 USD | 815,280,000.00 USD | 16,430,000.00 USD | 8,710,000.00 USD | 18,070,000.00 USD |
| `7D` | `2278.70` | 1,230,000,000.00 USD | 0.00 USD | 1,230,000,000.00 USD | 74,310,000.00 USD | 34,750,000.00 USD | 42,010,000.00 USD |
| `1D` | `2280.30` | 772,080,000.00 USD | 0.00 USD | 772,080,000.00 USD | 24,350,000.00 USD | 14,020,000.00 USD | 8,040,000.00 USD |
| `7D` | `2281.50` | 1,080,000,000.00 USD | 0.00 USD | 1,080,000,000.00 USD | 56,100,000.00 USD | 59,940,000.00 USD | 49,270,000.00 USD |
| `1D` | `2282.90` | 725,680,000.00 USD | 0.00 USD | 725,680,000.00 USD | 22,370,000.00 USD | 16,300,000.00 USD | 19,080,000.00 USD |
| `7D` | `2284.30` | 911,260,000.00 USD | 0.00 USD | 911,260,000.00 USD | 89,220,000.00 USD | 69,840,000.00 USD | 44,200,000.00 USD |
| `1D` | `2285.50` | 667,930,000.00 USD | 0.00 USD | 667,930,000.00 USD | 28,040,000.00 USD | 29,600,000.00 USD | 19,870,000.00 USD |
| `7D` | `2287.10` | 708,000,000.00 USD | 0.00 USD | 708,000,000.00 USD | 58,910,000.00 USD | 53,380,000.00 USD | 45,180,000.00 USD |
| `1D` | `2288.10` | 590,420,000.00 USD | 0.00 USD | 590,420,000.00 USD | 19,180,000.00 USD | 14,490,000.00 USD | 4,720,000.00 USD |
| `7D` | `2289.90` | 550,520,000.00 USD | 0.00 USD | 550,520,000.00 USD | 48,430,000.00 USD | 34,490,000.00 USD | 22,190,000.00 USD |
| `1D` | `2290.70` | 552,030,000.00 USD | 0.00 USD | 552,030,000.00 USD | 12,440,000.00 USD | 7,760,000.00 USD | 2,950,000.00 USD |
| `7D` | `2292.70` | 445,420,000.00 USD | 0.00 USD | 445,420,000.00 USD | 38,110,000.00 USD | 20,900,000.00 USD | 44,070,000.00 USD |
| `1D` | `2293.30` | 528,890,000.00 USD | 0.00 USD | 528,890,000.00 USD | 18,860,000.00 USD | 18,460,000.00 USD | 15,490,000.00 USD |
| `7D` | `2295.50` | 342,350,000.00 USD | 0.00 USD | 342,350,000.00 USD | 17,510,000.00 USD | 8,110,000.00 USD | 7,220,000.00 USD |
| `1D` | `2295.90` | 476,090,000.00 USD | 0.00 USD | 476,090,000.00 USD | 23,870,000.00 USD | 15,930,000.00 USD | 7,210,000.00 USD |
| `7D` | `2298.30` | 309,500,000.00 USD | 0.00 USD | 309,500,000.00 USD | 2,090,000.00 USD | 5,410,000.00 USD | 301,550.00 USD |
| `1D` | `2298.50` | 429,080,000.00 USD | 0.00 USD | 429,080,000.00 USD | 8,010,000.00 USD | 7,220,000.00 USD | 3,250,000.00 USD |
| `1D` | `2301.10` | 410,610,000.00 USD | 0.00 USD | 410,610,000.00 USD | 17,170,000.00 USD | 11,820,000.00 USD | 13,320,000.00 USD |
| `7D` | `2301.10` | 301,700,000.00 USD | 0.00 USD | 301,700,000.00 USD | 11,790,000.00 USD | 2,200,000.00 USD | 7,590,000.00 USD |
| `1D` | `2303.70` | 368,300,000.00 USD | 0.00 USD | 368,300,000.00 USD | 29,770,000.00 USD | 15,890,000.00 USD | 10,680,000.00 USD |
| `7D` | `2303.90` | 280,130,000.00 USD | 0.00 USD | 280,130,000.00 USD | 32,960,000.00 USD | 17,020,000.00 USD | 13,270,000.00 USD |
| `1D` | `2306.30` | 311,960,000.00 USD | 0.00 USD | 311,960,000.00 USD | 4,970,000.00 USD | 5,530,000.00 USD | 15,350,000.00 USD |
| `7D` | `2306.70` | 216,870,000.00 USD | 0.00 USD | 216,870,000.00 USD | 0.00 USD | 3,740,000.00 USD | 10,890,000.00 USD |
| `1D` | `2308.90` | 286,120,000.00 USD | 0.00 USD | 286,120,000.00 USD | 642,440.00 USD | 1,990,000.00 USD | 2,540,000.00 USD |
| `7D` | `2309.50` | 202,240,000.00 USD | 0.00 USD | 202,240,000.00 USD | 282,530.00 USD | 300,580.00 USD | 1,500,000.00 USD |
| `1D` | `2311.50` | 280,950,000.00 USD | 0.00 USD | 280,950,000.00 USD | 7,190,000.00 USD | 3,230,000.00 USD | 5,780,000.00 USD |
| `7D` | `2312.30` | 200,160,000.00 USD | 0.00 USD | 200,160,000.00 USD | 1,740,000.00 USD | 128,300.00 USD | 2,500,000.00 USD |
| `1D` | `2314.10` | 264,760,000.00 USD | 0.00 USD | 264,760,000.00 USD | 10,080,000.00 USD | 3,280,000.00 USD | 688,260.00 USD |
| `7D` | `2315.10` | 195,780,000.00 USD | 0.00 USD | 195,780,000.00 USD | 4,300,000.00 USD | 4,100,000.00 USD | 117,510.00 USD |
| `1D` | `2316.70` | 250,710,000.00 USD | 0.00 USD | 250,710,000.00 USD | 3,450,000.00 USD | 5,270,000.00 USD | 3,700,000.00 USD |
| `7D` | `2317.90` | 187,260,000.00 USD | 0.00 USD | 187,260,000.00 USD | 817,040.00 USD | 3,010,000.00 USD | 0.00 USD |
| `1D` | `2319.30` | 238,290,000.00 USD | 0.00 USD | 238,290,000.00 USD | 8,240,000.00 USD | 2,120,000.00 USD | 795,520.00 USD |
| `7D` | `2320.70` | 183,440,000.00 USD | 0.00 USD | 183,440,000.00 USD | 0.00 USD | 2,790,000.00 USD | 0.00 USD |
| `1D` | `2321.90` | 227,140,000.00 USD | 0.00 USD | 227,140,000.00 USD | 616,250.00 USD | 2,660,000.00 USD | 1,660,000.00 USD |
| `7D` | `2323.50` | 180,650,000.00 USD | 0.00 USD | 180,650,000.00 USD | 4,070,000.00 USD | 1,900,000.00 USD | 0.00 USD |
| `1D` | `2324.50` | 222,200,000.00 USD | 0.00 USD | 222,200,000.00 USD | 8,660,000.00 USD | 2,780,000.00 USD | 2,210,000.00 USD |
| `7D` | `2326.30` | 174,670,000.00 USD | 0.00 USD | 174,670,000.00 USD | 0.00 USD | 0.00 USD | 126,530.00 USD |
| `1D` | `2327.10` | 208,540,000.00 USD | 0.00 USD | 208,540,000.00 USD | 0.00 USD | 3,260,000.00 USD | 4,450,000.00 USD |
| `7D` | `2329.10` | 174,550,000.00 USD | 0.00 USD | 174,550,000.00 USD | 3,860,000.00 USD | 0.00 USD | 4,880,000.00 USD |
| `1D` | `2329.70` | 200,830,000.00 USD | 0.00 USD | 200,830,000.00 USD | 5,520,000.00 USD | 1,150,000.00 USD | 3,040,000.00 USD |
| `7D` | `2331.90` | 165,800,000.00 USD | 0.00 USD | 165,800,000.00 USD | 29,230,000.00 USD | 1,090,000.00 USD | 2,810,000.00 USD |
| `1D` | `2332.30` | 191,120,000.00 USD | 0.00 USD | 191,120,000.00 USD | 17,970,000.00 USD | 2,290,000.00 USD | 107,090.00 USD |
| `7D` | `2334.70` | 132,670,000.00 USD | 0.00 USD | 132,670,000.00 USD | 7,260,000.00 USD | 18,420,000.00 USD | 8,930,000.00 USD |
| `1D` | `2334.90` | 170,750,000.00 USD | 0.00 USD | 170,750,000.00 USD | 28,290,000.00 USD | 25,090,000.00 USD | 16,090,000.00 USD |
| `1D` | `2337.50` | 101,280,000.00 USD | 0.00 USD | 101,280,000.00 USD | 6,570,000.00 USD | 22,000,000.00 USD | 10,170,000.00 USD |
| `7D` | `2337.50` | 98,050,000.00 USD | 0.00 USD | 98,050,000.00 USD | 20,380,000.00 USD | 18,560,000.00 USD | 13,560,000.00 USD |
| `1D` | `2340.10` | 62,550,000.00 USD | 0.00 USD | 62,550,000.00 USD | 4,960,000.00 USD | 21,890,000.00 USD | 7,070,000.00 USD |
| `7D` | `2340.30` | 45,550,000.00 USD | 0.00 USD | 45,550,000.00 USD | 1,630,000.00 USD | 10,010,000.00 USD | 3,380,000.00 USD |
| `1D` | `2342.70` | 28,630,000.00 USD | 0.00 USD | 28,630,000.00 USD | 5,030,000.00 USD | 8,490,000.00 USD | 2,160,000.00 USD |
| `7D` | `2343.10` | 30,520,000.00 USD | 0.00 USD | 30,520,000.00 USD | 0.00 USD | 5,540,000.00 USD | 3,840,000.00 USD |
| `1D` | `2345.30` | 12,940,000.00 USD | 0.00 USD | 12,940,000.00 USD | 963,370.00 USD | 1,770,000.00 USD | 9,990,000.00 USD |
| `7D` | `2345.90` | 21,140,000.00 USD | 0.00 USD | 21,140,000.00 USD | 0.00 USD | 8,310,000.00 USD | 12,830,000.00 USD |
| `1D` | `2347.90` | 215,860.00 USD | 0.00 USD | 215,860.00 USD | 215,860.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2348.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2348.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2348.70` | 18,370,000.00 USD | 18,370,000.00 USD | 0.00 USD | 285,680.00 USD | 7,340,000.00 USD | 10,750,000.00 USD |
| `1D` | `2350.50` | 28,430,000.00 USD | 28,430,000.00 USD | 0.00 USD | 25,900,000.00 USD | 2,510,000.00 USD | 23,220.00 USD |
| `7D` | `2351.50` | 42,270,000.00 USD | 42,270,000.00 USD | 0.00 USD | 782,590.00 USD | 17,440,000.00 USD | 5,680,000.00 USD |
| `1D` | `2353.10` | 30,230,000.00 USD | 30,230,000.00 USD | 0.00 USD | 576,450.00 USD | 1,110,000.00 USD | 107,380.00 USD |
| `7D` | `2354.30` | 83,490,000.00 USD | 83,490,000.00 USD | 0.00 USD | 5,960,000.00 USD | 35,020,000.00 USD | 237,340.00 USD |
| `1D` | `2355.70` | 47,760,000.00 USD | 47,760,000.00 USD | 0.00 USD | 318,080.00 USD | 15,970,000.00 USD | 1,240,000.00 USD |
| `7D` | `2357.10` | 96,790,000.00 USD | 96,790,000.00 USD | 0.00 USD | 7,900,000.00 USD | 5,400,000.00 USD | 0.00 USD |
| `1D` | `2358.30` | 47,960,000.00 USD | 47,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 198,570.00 USD |
| `7D` | `2359.90` | 99,010,000.00 USD | 99,010,000.00 USD | 0.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2360.90` | 49,910,000.00 USD | 49,910,000.00 USD | 0.00 USD | 1,850,000.00 USD | 0.00 USD | 93,130.00 USD |
| `7D` | `2362.70` | 101,160,000.00 USD | 101,160,000.00 USD | 0.00 USD | 467,570.00 USD | 0.00 USD | 1,690,000.00 USD |
| `1D` | `2363.50` | 53,020,000.00 USD | 53,020,000.00 USD | 0.00 USD | 929,610.00 USD | 1,840,000.00 USD | 341,510.00 USD |
| `7D` | `2365.50` | 109,160,000.00 USD | 109,160,000.00 USD | 0.00 USD | 6,340,000.00 USD | 0.00 USD | 1,660,000.00 USD |
| `1D` | `2366.10` | 53,250,000.00 USD | 53,250,000.00 USD | 0.00 USD | 61,300.00 USD | 0.00 USD | 170,870.00 USD |
| `7D` | `2368.30` | 119,130,000.00 USD | 119,130,000.00 USD | 0.00 USD | 9,590,000.00 USD | 0.00 USD | 370,810.00 USD |
| `1D` | `2368.70` | 65,730,000.00 USD | 65,730,000.00 USD | 0.00 USD | 8,060,000.00 USD | 3,260,000.00 USD | 1,170,000.00 USD |
| `7D` | `2371.10` | 180,920,000.00 USD | 180,920,000.00 USD | 0.00 USD | 16,760,000.00 USD | 0.00 USD | 45,040,000.00 USD |
| `1D` | `2371.30` | 104,120,000.00 USD | 104,120,000.00 USD | 0.00 USD | 17,050,000.00 USD | 12,840,000.00 USD | 8,490,000.00 USD |
| `1D` | `2373.90` | 121,660,000.00 USD | 121,660,000.00 USD | 0.00 USD | 13,630,000.00 USD | 955,690.00 USD | 2,970,000.00 USD |
| `7D` | `2373.90` | 203,490,000.00 USD | 203,490,000.00 USD | 0.00 USD | 15,830,000.00 USD | 0.00 USD | 6,730,000.00 USD |
| `1D` | `2376.50` | 147,560,000.00 USD | 147,560,000.00 USD | 0.00 USD | 12,130,000.00 USD | 3,180,000.00 USD | 10,590,000.00 USD |
| `7D` | `2376.70` | 243,630,000.00 USD | 243,630,000.00 USD | 0.00 USD | 12,140,000.00 USD | 5,950,000.00 USD | 22,050,000.00 USD |
| `1D` | `2379.10` | 178,930,000.00 USD | 178,930,000.00 USD | 0.00 USD | 5,850,000.00 USD | 13,800,000.00 USD | 11,720,000.00 USD |
| `7D` | `2379.50` | 270,940,000.00 USD | 270,940,000.00 USD | 0.00 USD | 7,180,000.00 USD | 2,580,000.00 USD | 17,560,000.00 USD |
| `1D` | `2381.70` | 220,730,000.00 USD | 220,730,000.00 USD | 0.00 USD | 15,410,000.00 USD | 10,970,000.00 USD | 15,420,000.00 USD |
| `7D` | `2382.30` | 312,290,000.00 USD | 312,290,000.00 USD | 0.00 USD | 7,910,000.00 USD | 12,120,000.00 USD | 21,320,000.00 USD |
| `1D` | `2384.30` | 269,950,000.00 USD | 269,950,000.00 USD | 0.00 USD | 21,040,000.00 USD | 17,560,000.00 USD | 10,610,000.00 USD |
| `7D` | `2385.10` | 399,030,000.00 USD | 399,030,000.00 USD | 0.00 USD | 14,990,000.00 USD | 28,990,000.00 USD | 42,760,000.00 USD |
| `1D` | `2386.90` | 300,220,000.00 USD | 300,220,000.00 USD | 0.00 USD | 12,200,000.00 USD | 11,050,000.00 USD | 7,020,000.00 USD |
| `7D` | `2387.90` | 479,170,000.00 USD | 479,170,000.00 USD | 0.00 USD | 4,870,000.00 USD | 32,720,000.00 USD | 42,550,000.00 USD |
| `1D` | `2389.50` | 324,160,000.00 USD | 324,160,000.00 USD | 0.00 USD | 9,590,000.00 USD | 8,400,000.00 USD | 5,950,000.00 USD |
| `7D` | `2390.70` | 578,860,000.00 USD | 578,860,000.00 USD | 0.00 USD | 5,470,000.00 USD | 45,700,000.00 USD | 48,520,000.00 USD |
| `1D` | `2392.10` | 351,900,000.00 USD | 351,900,000.00 USD | 0.00 USD | 5,340,000.00 USD | 13,820,000.00 USD | 8,570,000.00 USD |
| `7D` | `2393.50` | 677,320,000.00 USD | 677,320,000.00 USD | 0.00 USD | 43,890,000.00 USD | 22,890,000.00 USD | 31,690,000.00 USD |
| `1D` | `2394.70` | 382,860,000.00 USD | 382,860,000.00 USD | 0.00 USD | 14,780,000.00 USD | 13,450,000.00 USD | 2,740,000.00 USD |
| `7D` | `2396.30` | 761,370,000.00 USD | 761,370,000.00 USD | 0.00 USD | 29,820,000.00 USD | 32,850,000.00 USD | 21,360,000.00 USD |
| `1D` | `2397.30` | 402,050,000.00 USD | 402,050,000.00 USD | 0.00 USD | 5,540,000.00 USD | 8,740,000.00 USD | 4,910,000.00 USD |
| `7D` | `2399.10` | 850,890,000.00 USD | 850,890,000.00 USD | 0.00 USD | 39,350,000.00 USD | 31,200,000.00 USD | 18,980,000.00 USD |
| `1D` | `2399.90` | 443,360,000.00 USD | 443,360,000.00 USD | 0.00 USD | 17,930,000.00 USD | 9,240,000.00 USD | 14,130,000.00 USD |
| `7D` | `2401.90` | 961,680,000.00 USD | 961,680,000.00 USD | 0.00 USD | 53,530,000.00 USD | 24,490,000.00 USD | 32,780,000.00 USD |
| `1D` | `2402.50` | 469,850,000.00 USD | 469,850,000.00 USD | 0.00 USD | 8,820,000.00 USD | 9,710,000.00 USD | 7,970,000.00 USD |
| `7D` | `2404.70` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 0.00 USD | 36,370,000.00 USD | 25,840,000.00 USD | 15,520,000.00 USD |
| `1D` | `2405.10` | 503,290,000.00 USD | 503,290,000.00 USD | 0.00 USD | 13,880,000.00 USD | 10,580,000.00 USD | 8,970,000.00 USD |
| `7D` | `2407.50` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 22,760,000.00 USD | 29,510,000.00 USD | 18,930,000.00 USD |
| `1D` | `2407.70` | 538,430,000.00 USD | 538,430,000.00 USD | 0.00 USD | 14,050,000.00 USD | 11,560,000.00 USD | 9,530,000.00 USD |
| `1D` | `2410.30` | 563,070,000.00 USD | 563,070,000.00 USD | 0.00 USD | 9,390,000.00 USD | 8,300,000.00 USD | 6,950,000.00 USD |
| `7D` | `2410.30` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 26,620,000.00 USD | 26,620,000.00 USD | 23,370,000.00 USD |
| `1D` | `2412.90` | 582,600,000.00 USD | 582,600,000.00 USD | 0.00 USD | 9,190,000.00 USD | 6,900,000.00 USD | 3,440,000.00 USD |
| `7D` | `2413.10` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 13,360,000.00 USD | 15,180,000.00 USD | 13,360,000.00 USD |
| `1D` | `2415.50` | 595,630,000.00 USD | 595,630,000.00 USD | 0.00 USD | 3,550,000.00 USD | 5,790,000.00 USD | 3,690,000.00 USD |
| `7D` | `2415.90` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 0.00 USD | 28,030,000.00 USD | 17,450,000.00 USD | 32,370,000.00 USD |
| `1D` | `2418.10` | 608,540,000.00 USD | 608,540,000.00 USD | 0.00 USD | 4,840,000.00 USD | 5,370,000.00 USD | 2,700,000.00 USD |
| `7D` | `2418.70` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 28,840,000.00 USD | 18,500,000.00 USD | 12,150,000.00 USD |
| `1D` | `2420.70` | 623,470,000.00 USD | 623,470,000.00 USD | 0.00 USD | 6,810,000.00 USD | 5,220,000.00 USD | 2,900,000.00 USD |
| `7D` | `2421.50` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 23,440,000.00 USD | 25,120,000.00 USD | 18,550,000.00 USD |
| `1D` | `2423.30` | 637,320,000.00 USD | 637,320,000.00 USD | 0.00 USD | 4,570,000.00 USD | 3,780,000.00 USD | 5,500,000.00 USD |
| `7D` | `2424.30` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 0.00 USD | 25,250,000.00 USD | 29,620,000.00 USD | 33,670,000.00 USD |
| `1D` | `2425.90` | 640,670,000.00 USD | 640,670,000.00 USD | 0.00 USD | 516,070.00 USD | 2,570,000.00 USD | 261,350.00 USD |
| `7D` | `2427.10` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 24,580,000.00 USD | 22,020,000.00 USD | 23,680,000.00 USD |
| `1D` | `2428.50` | 643,030,000.00 USD | 643,030,000.00 USD | 0.00 USD | 2,090,000.00 USD | 12,140.00 USD | 264,480.00 USD |
| `7D` | `2429.90` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 6,160,000.00 USD | 14,060,000.00 USD | 8,450,000.00 USD |
| `1D` | `2431.10` | 645,990,000.00 USD | 645,990,000.00 USD | 0.00 USD | 2,190,000.00 USD | 507,190.00 USD | 254,180.00 USD |
| `7D` | `2432.70` | 1,660,000,000.00 USD | 1,660,000,000.00 USD | 0.00 USD | 17,740,000.00 USD | 13,220,000.00 USD | 6,540,000.00 USD |
| `1D` | `2433.70` | 648,840,000.00 USD | 648,840,000.00 USD | 0.00 USD | 314,980.00 USD | 534,830.00 USD | 2,000,000.00 USD |
| `7D` | `2435.50` | 1,710,000,000.00 USD | 1,710,000,000.00 USD | 0.00 USD | 22,360,000.00 USD | 14,140,000.00 USD | 15,430,000.00 USD |
| `1D` | `2436.30` | 653,700,000.00 USD | 653,700,000.00 USD | 0.00 USD | 3,340,000.00 USD | 1,270,000.00 USD | 261,300.00 USD |
| `7D` | `2438.30` | 1,770,000,000.00 USD | 1,770,000,000.00 USD | 0.00 USD | 17,900,000.00 USD | 23,900,000.00 USD | 15,750,000.00 USD |
| `1D` | `2438.90` | 658,290,000.00 USD | 658,290,000.00 USD | 0.00 USD | 1,260,000.00 USD | 1,610,000.00 USD | 1,710,000.00 USD |
| `7D` | `2441.10` | 1,810,000,000.00 USD | 1,810,000,000.00 USD | 0.00 USD | 17,250,000.00 USD | 6,990,000.00 USD | 14,660,000.00 USD |
| `1D` | `2441.50` | 667,150,000.00 USD | 667,150,000.00 USD | 0.00 USD | 4,710,000.00 USD | 3,380,000.00 USD | 767,510.00 USD |
| `7D` | `2443.90` | 1,840,000,000.00 USD | 1,840,000,000.00 USD | 0.00 USD | 6,650,000.00 USD | 13,590,000.00 USD | 7,960,000.00 USD |
| `1D` | `2444.10` | 670,380,000.00 USD | 670,380,000.00 USD | 0.00 USD | 791,730.00 USD | 798,660.00 USD | 1,640,000.00 USD |
| `1D` | `2446.70` | 678,140,000.00 USD | 678,140,000.00 USD | 0.00 USD | 4,320,000.00 USD | 1,500,000.00 USD | 1,940,000.00 USD |
| `7D` | `2446.70` | 1,870,000,000.00 USD | 1,870,000,000.00 USD | 0.00 USD | 11,870,000.00 USD | 7,020,000.00 USD | 18,970,000.00 USD |
| `1D` | `2449.30` | 684,680,000.00 USD | 684,680,000.00 USD | 0.00 USD | 2,040,000.00 USD | 1,740,000.00 USD | 2,760,000.00 USD |
| `7D` | `2449.50` | 1,910,000,000.00 USD | 1,910,000,000.00 USD | 0.00 USD | 15,780,000.00 USD | 9,650,000.00 USD | 14,870,000.00 USD |
| `1D` | `2451.90` | 696,950,000.00 USD | 696,950,000.00 USD | 0.00 USD | 3,860,000.00 USD | 3,720,000.00 USD | 4,690,000.00 USD |
| `7D` | `2452.30` | 1,940,000,000.00 USD | 1,940,000,000.00 USD | 0.00 USD | 10,050,000.00 USD | 9,630,000.00 USD | 7,330,000.00 USD |
| `1D` | `2454.50` | 707,120,000.00 USD | 707,120,000.00 USD | 0.00 USD | 4,200,000.00 USD | 3,460,000.00 USD | 2,510,000.00 USD |
| `7D` | `2455.10` | 1,960,000,000.00 USD | 1,960,000,000.00 USD | 0.00 USD | 5,550,000.00 USD | 5,830,000.00 USD | 3,620,000.00 USD |
| `1D` | `2457.10` | 714,270,000.00 USD | 714,270,000.00 USD | 0.00 USD | 2,160,000.00 USD | 2,720,000.00 USD | 2,270,000.00 USD |
| `7D` | `2457.90` | 1,990,000,000.00 USD | 1,990,000,000.00 USD | 0.00 USD | 12,470,000.00 USD | 11,200,000.00 USD | 13,240,000.00 USD |
| `1D` | `2459.70` | 719,950,000.00 USD | 719,950,000.00 USD | 0.00 USD | 2,370,000.00 USD | 1,970,000.00 USD | 1,340,000.00 USD |
| `7D` | `2460.70` | 2,020,000,000.00 USD | 2,020,000,000.00 USD | 0.00 USD | 7,010,000.00 USD | 10,640,000.00 USD | 5,770,000.00 USD |
| `1D` | `2462.30` | 723,270,000.00 USD | 723,270,000.00 USD | 0.00 USD | 174,920.00 USD | 2,050,000.00 USD | 1,100,000.00 USD |
| `7D` | `2463.50` | 2,040,000,000.00 USD | 2,040,000,000.00 USD | 0.00 USD | 9,490,000.00 USD | 9,600,000.00 USD | 8,830,000.00 USD |
| `1D` | `2464.90` | 725,340,000.00 USD | 725,340,000.00 USD | 0.00 USD | 820,990.00 USD | 1,240,000.00 USD | 5,650.00 USD |
| `7D` | `2466.30` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 0.00 USD | 5,400,000.00 USD | 2,080,000.00 USD | 1,330,000.00 USD |
| `1D` | `2467.50` | 725,720,000.00 USD | 725,720,000.00 USD | 0.00 USD | 0.00 USD | 370,410.00 USD | 7,190.00 USD |
| `7D` | `2469.10` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 0.00 USD | 2,770,000.00 USD | 3,570,000.00 USD | 408,300.00 USD |
| `1D` | `2470.10` | 729,770,000.00 USD | 729,770,000.00 USD | 0.00 USD | 1,390,000.00 USD | 1,510,000.00 USD | 1,160,000.00 USD |
| `7D` | `2471.90` | 2,070,000,000.00 USD | 2,070,000,000.00 USD | 0.00 USD | 3,090,000.00 USD | 2,760,000.00 USD | 814,440.00 USD |
| `1D` | `2472.70` | 730,010,000.00 USD | 730,010,000.00 USD | 0.00 USD | 0.00 USD | 232,740.00 USD | 3,820.00 USD |
| `7D` | `2474.70` | 2,070,000,000.00 USD | 2,070,000,000.00 USD | 0.00 USD | 5,400,000.00 USD | 866,790.00 USD | 1,750,000.00 USD |
| `1D` | `2475.30` | 730,750,000.00 USD | 730,750,000.00 USD | 0.00 USD | 738,780.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2477.50` | 2,080,000,000.00 USD | 2,080,000,000.00 USD | 0.00 USD | 790,860.00 USD | 3,880,000.00 USD | 2,000,000.00 USD |
| `1D` | `2477.90` | 730,800,000.00 USD | 730,800,000.00 USD | 0.00 USD | 0.00 USD | 41,760.00 USD | 7,750.00 USD |
| `7D` | `2480.30` | 2,080,000,000.00 USD | 2,080,000,000.00 USD | 0.00 USD | 2,300,000.00 USD | 1,740,000.00 USD | 0.00 USD |
| `1D` | `2480.50` | 731,350,000.00 USD | 731,350,000.00 USD | 0.00 USD | 0.00 USD | 27,720.00 USD | 518,550.00 USD |
| `1D` | `2483.10` | 731,970,000.00 USD | 731,970,000.00 USD | 0.00 USD | 628,130.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2483.10` | 2,090,000,000.00 USD | 2,090,000,000.00 USD | 0.00 USD | 2,010,000.00 USD | 1,330,000.00 USD | 1,990,000.00 USD |
| `7D` | `2485.90` | 2,090,000,000.00 USD | 2,090,000,000.00 USD | 0.00 USD | 586,480.00 USD | 1,560,000.00 USD | 77,610.00 USD |
| `7D` | `2488.70` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 0.00 USD | 1,710,000.00 USD | 842,740.00 USD | 2,100,000.00 USD |
| `7D` | `2491.50` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 0.00 USD | 1,660,000.00 USD | 2,550,000.00 USD | 672,990.00 USD |
| `7D` | `2494.30` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,730,000.00 USD | 5,000,000.00 USD |
| `7D` | `2497.10` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 0.00 USD | 3,640,000.00 USD | 3,570,000.00 USD | 6,690,000.00 USD |
| `7D` | `2499.90` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 0.00 USD | 1,110,000.00 USD | 2,430,000.00 USD | 1,090,000.00 USD |
| `7D` | `2502.70` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 0.00 USD | 110,450.00 USD | 1,430,000.00 USD | 170,270.00 USD |
| `7D` | `2505.50` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 0.00 USD | 3,200,000.00 USD | 2,320,000.00 USD | 59,220.00 USD |
| `7D` | `2508.30` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 0.00 USD | 1,150,000.00 USD | 1,270,000.00 USD | 1,990,000.00 USD |
| `7D` | `2511.10` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 0.00 USD | 2,560,000.00 USD | 3,230,000.00 USD | 2,640,000.00 USD |
| `7D` | `2513.90` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 0.00 USD | 776,920.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2516.70` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 0.00 USD | 97,050.00 USD | 189,640.00 USD | 0.00 USD |
| `7D` | `2519.50` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD |
| `1D` | `2522.10` | 732,210,000.00 USD | 732,210,000.00 USD | 0.00 USD | 80,610.00 USD | 61,830.00 USD | 90,130.00 USD |
| `7D` | `2522.30` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 0.00 USD | 1,050,000.00 USD | 0.00 USD | 945,860.00 USD |
| `1D` | `2524.70` | 732,660,000.00 USD | 732,660,000.00 USD | 0.00 USD | 421,540.00 USD | 0.00 USD | 30,180.00 USD |
| `7D` | `2525.10` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 0.00 USD | 307,040.00 USD | 224,130.00 USD | 178,180.00 USD |
| `1D` | `2527.30` | 732,770,000.00 USD | 732,770,000.00 USD | 0.00 USD | 0.00 USD | 57,450.00 USD | 50,470.00 USD |
| `7D` | `2527.90` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 0.00 USD | 1,520,000.00 USD | 871,200.00 USD | 749,440.00 USD |
| `1D` | `2529.90` | 734,840,000.00 USD | 734,840,000.00 USD | 0.00 USD | 995,550.00 USD | 645,910.00 USD | 437,490.00 USD |
| `7D` | `2530.70` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 0.00 USD | 2,140,000.00 USD | 1,930,000.00 USD | 1,220,000.00 USD |
| `1D` | `2532.50` | 735,210,000.00 USD | 735,210,000.00 USD | 0.00 USD | 359,430.00 USD | 0.00 USD | 7,120.00 USD |
| `7D` | `2533.50` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 0.00 USD | 2,620,000.00 USD | 1,770,000.00 USD | 1,390,000.00 USD |
| `1D` | `2535.10` | 735,980,000.00 USD | 735,980,000.00 USD | 0.00 USD | 229,190.00 USD | 41,990.00 USD | 499,440.00 USD |
| `7D` | `2536.30` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 0.00 USD | 2,810,000.00 USD | 2,460,000.00 USD | 2,740,000.00 USD |
| `1D` | `2537.70` | 740,530,000.00 USD | 740,530,000.00 USD | 0.00 USD | 2,030,000.00 USD | 901,140.00 USD | 1,620,000.00 USD |
| `7D` | `2539.10` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 0.00 USD | 3,530,000.00 USD | 3,180,000.00 USD | 1,090,000.00 USD |
| `1D` | `2540.30` | 743,390,000.00 USD | 743,390,000.00 USD | 0.00 USD | 1,140,000.00 USD | 1,100,000.00 USD | 617,540.00 USD |
| `7D` | `2541.90` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 0.00 USD | 3,400,000.00 USD | 2,740,000.00 USD | 2,240,000.00 USD |
| `1D` | `2542.90` | 745,580,000.00 USD | 745,580,000.00 USD | 0.00 USD | 1,100,000.00 USD | 1,070,000.00 USD | 19,390.00 USD |
| `7D` | `2544.70` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 0.00 USD | 2,170,000.00 USD | 1,830,000.00 USD | 1,350,000.00 USD |
| `1D` | `2545.50` | 746,990,000.00 USD | 746,990,000.00 USD | 0.00 USD | 590,640.00 USD | 800,740.00 USD | 12,050.00 USD |
| `7D` | `2547.50` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 938,680.00 USD | 2,240,000.00 USD |
| `1D` | `2548.10` | 749,930,000.00 USD | 749,930,000.00 USD | 0.00 USD | 1,370,000.00 USD | 832,850.00 USD | 743,470.00 USD |
| `7D` | `2550.30` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 0.00 USD | 2,860,000.00 USD | 2,690,000.00 USD | 1,800,000.00 USD |
| `1D` | `2550.70` | 753,390,000.00 USD | 753,390,000.00 USD | 0.00 USD | 1,380,000.00 USD | 1,460,000.00 USD | 618,500.00 USD |
| `7D` | `2553.10` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 0.00 USD | 2,120,000.00 USD | 788,360.00 USD | 1,670,000.00 USD |
| `1D` | `2553.30` | 754,170,000.00 USD | 754,170,000.00 USD | 0.00 USD | 468,780.00 USD | 220,540.00 USD | 90,660.00 USD |
| `1D` | `2555.90` | 755,940,000.00 USD | 755,940,000.00 USD | 0.00 USD | 1,010,000.00 USD | 398,720.00 USD | 366,540.00 USD |
| `7D` | `2555.90` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 0.00 USD | 3,290,000.00 USD | 255,750.00 USD | 5,860,000.00 USD |
| `1D` | `2558.50` | 757,550,000.00 USD | 757,550,000.00 USD | 0.00 USD | 722,170.00 USD | 141,030.00 USD | 745,190.00 USD |
| `7D` | `2558.70` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 0.00 USD | 3,850,000.00 USD | 1,200,000.00 USD | 2,340,000.00 USD |
| `1D` | `2561.10` | 761,790,000.00 USD | 761,790,000.00 USD | 0.00 USD | 1,640,000.00 USD | 1,270,000.00 USD | 1,320,000.00 USD |
| `7D` | `2561.50` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 0.00 USD | 2,780,000.00 USD | 2,030,000.00 USD | 426,110.00 USD |
| `1D` | `2563.70` | 763,510,000.00 USD | 763,510,000.00 USD | 0.00 USD | 440,660.00 USD | 975,880.00 USD | 309,770.00 USD |
| `7D` | `2564.30` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 0.00 USD | 1,800,000.00 USD | 2,150,000.00 USD | 1,460,000.00 USD |
| `1D` | `2566.30` | 763,760,000.00 USD | 763,760,000.00 USD | 0.00 USD | 121,690.00 USD | 17,120.00 USD | 105,450.00 USD |
| `7D` | `2567.10` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 0.00 USD | 575,630.00 USD | 1,510,000.00 USD | 2,700,000.00 USD |
| `1D` | `2568.90` | 764,020,000.00 USD | 764,020,000.00 USD | 0.00 USD | 162,270.00 USD | 0.00 USD | 101,820.00 USD |
| `7D` | `2569.90` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 0.00 USD | 125,250.00 USD | 290,680.00 USD | 1,180,000.00 USD |
| `1D` | `2571.50` | 764,970,000.00 USD | 764,970,000.00 USD | 0.00 USD | 770,210.00 USD | 169,470.00 USD | 5,200.00 USD |
| `7D` | `2572.70` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 890,480.00 USD | 1,790,000.00 USD |
| `1D` | `2574.10` | 765,660,000.00 USD | 765,660,000.00 USD | 0.00 USD | 121,300.00 USD | 191,750.00 USD | 381,370.00 USD |
| `7D` | `2575.50` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 0.00 USD | 2,180,000.00 USD | 440,740.00 USD | 1,060,000.00 USD |
| `1D` | `2576.70` | 766,310,000.00 USD | 766,310,000.00 USD | 0.00 USD | 439,020.00 USD | 209,570.00 USD | 3,450.00 USD |
| `7D` | `2578.30` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 0.00 USD | 734,040.00 USD | 1,480,000.00 USD | 1,750,000.00 USD |
| `1D` | `2579.30` | 767,650,000.00 USD | 767,650,000.00 USD | 0.00 USD | 308,690.00 USD | 314,010.00 USD | 710,940.00 USD |
| `7D` | `2581.10` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 0.00 USD | 3,270,000.00 USD | 864,580.00 USD | 1,220,000.00 USD |
| `1D` | `2581.90` | 770,400,000.00 USD | 770,400,000.00 USD | 0.00 USD | 1,580,000.00 USD | 935,910.00 USD | 234,280.00 USD |
| `7D` | `2583.90` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 0.00 USD | 740,840.00 USD | 1,260,000.00 USD | 3,550,000.00 USD |
| `1D` | `2584.50` | 771,400,000.00 USD | 771,400,000.00 USD | 0.00 USD | 287,140.00 USD | 153,810.00 USD | 554,400.00 USD |
| `7D` | `2586.70` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 0.00 USD | 1,900,000.00 USD | 2,190,000.00 USD | 1,530,000.00 USD |
| `1D` | `2587.10` | 773,430,000.00 USD | 773,430,000.00 USD | 0.00 USD | 1,260,000.00 USD | 335,670.00 USD | 439,060.00 USD |
| `7D` | `2589.50` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 2,840,000.00 USD | 446,810.00 USD | 2,140,000.00 USD |
| `1D` | `2589.70` | 774,740,000.00 USD | 774,740,000.00 USD | 0.00 USD | 445,920.00 USD | 99,440.00 USD | 763,970.00 USD |
| `1D` | `2592.30` | 776,980,000.00 USD | 776,980,000.00 USD | 0.00 USD | 971,410.00 USD | 349,000.00 USD | 919,490.00 USD |
| `7D` | `2592.30` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 2,340,000.00 USD | 1,280,000.00 USD | 1,550,000.00 USD |
| `1D` | `2594.90` | 780,080,000.00 USD | 780,080,000.00 USD | 0.00 USD | 886,830.00 USD | 1,220,000.00 USD | 995,020.00 USD |
| `7D` | `2595.10` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 452,020.00 USD | 569,790.00 USD | 752,870.00 USD |
| `1D` | `2597.50` | 781,040,000.00 USD | 781,040,000.00 USD | 0.00 USD | 179,030.00 USD | 442,330.00 USD | 339,490.00 USD |
| `7D` | `2597.90` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 0.00 USD | 2,280,000.00 USD | 1,630,000.00 USD | 2,420,000.00 USD |
| `1D` | `2600.10` | 782,330,000.00 USD | 782,330,000.00 USD | 0.00 USD | 258,900.00 USD | 724,120.00 USD | 303,400.00 USD |
| `7D` | `2600.70` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 0.00 USD | 496,060.00 USD | 1,960,000.00 USD | 1,610,000.00 USD |
| `1D` | `2602.70` | 783,210,000.00 USD | 783,210,000.00 USD | 0.00 USD | 107,010.00 USD | 453,880.00 USD | 318,170.00 USD |
| `7D` | `2603.50` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 0.00 USD | 2,040,000.00 USD | 1,580,000.00 USD | 1,660,000.00 USD |
| `1D` | `2605.30` | 784,190,000.00 USD | 784,190,000.00 USD | 0.00 USD | 0.00 USD | 644,330.00 USD | 336,530.00 USD |
| `7D` | `2606.30` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 0.00 USD | 1,480,000.00 USD | 229,360.00 USD | 342,240.00 USD |
| `1D` | `2607.90` | 784,870,000.00 USD | 784,870,000.00 USD | 0.00 USD | 187,520.00 USD | 497,320.00 USD | 0.00 USD |
| `7D` | `2609.10` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 0.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD |
| `1D` | `2610.50` | 785,170,000.00 USD | 785,170,000.00 USD | 0.00 USD | 0.00 USD | 294,600.00 USD | 2,870.00 USD |
| `7D` | `2611.90` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 0.00 USD | 724,220.00 USD | 608,060.00 USD | 43,560.00 USD |
| `1D` | `2613.10` | 786,180,000.00 USD | 786,180,000.00 USD | 0.00 USD | 555,320.00 USD | 250,240.00 USD | 205,180.00 USD |
| `7D` | `2614.70` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 0.00 USD | 1,110,000.00 USD | 1,000,000.00 USD | 409,160.00 USD |
| `7D` | `2617.50` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 0.00 USD | 1,550,000.00 USD | 209,240.00 USD | 402,600.00 USD |
| `1D` | `2618.30` | 786,480,000.00 USD | 786,480,000.00 USD | 0.00 USD | 295,510.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2620.30` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 0.00 USD | 47,360.00 USD | 1,120,000.00 USD | 268,500.00 USD |
| `7D` | `2623.10` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 0.00 USD | 631,440.00 USD | 410,460.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `30.21B` | Total OI Tokens: `12,859,093.5 ETH`
  * 1h OI Change: `-1.06%` | 4h OI Change: `-0.08%` | 24h OI Change: `+1.32%`
  * Exchange Breakdown: Binance=`8.98B` | Bybit=`2.13B` | OKX=`1.83B` | Hyperliquid=`2.58B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `1.16M` | Last 24h: `2.27M` | Last 3d: `7.66M` | Last 7d: `13.85M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0098%` | **USDT OKX** | `0.0092%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0073%` |
| **USDT MEXC** | `0.0098%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0073%` | **USDT Bitget** | `0.0034%` |
| **CoinM Binance** | `0.0099%` | **CoinM OKX** | `0.0063%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `38.24%` | `61.76%` | `0.62` | 1,290,000,000.00 USD |
| `15M` | `Binance` | `29.94%` | `70.06%` | `0.43` | 497,640,000.00 USD |
| `15M` | `OKX` | `40.27%` | `59.73%` | `0.67` | 175,820,000.00 USD |
| `15M` | `Bybit` | `35.88%` | `64.12%` | `0.56` | 121,370,000.00 USD |
| `15M` | `KuCoin` | `39.01%` | `60.99%` | `0.64` | 3,380,000.00 USD |
| `15M` | `Gate` | `47.04%` | `52.96%` | `0.89` | 133,550,000.00 USD |
| `15M` | `Bitget` | `38.91%` | `61.09%` | `0.64` | 70,710,000.00 USD |
| `15M` | `BingX` | `44.45%` | `55.55%` | `0.80` | 16,400,000.00 USD |
| `15M` | `MEXC` | `50.1%` | `49.9%` | `1.00` | 60,780,000.00 USD |
| `15M` | `Bitunix` | `45.35%` | `54.65%` | `0.83` | 48,830,000.00 USD |
| `15M` | `Hyperliquid` | `47.68%` | `52.32%` | `0.91` | 31,080,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `70.39%` | `29.61%` | `2.38` | 5,240,000.00 USD |
| `15M` | `Crypto.com` | `45.63%` | `54.37%` | `0.84` | 12,250,000.00 USD |
| `15M` | `WhiteBIT` | `65.74%` | `34.26%` | `1.92` | 37,220,000.00 USD |
| `15M` | `HTX` | `30.37%` | `69.63%` | `0.44` | 4,870,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `51.19%` | `48.81%` | `1.05` | 19,950,000.00 USD |
| `15M` | `Bitfinex` | `26.79%` | `73.21%` | `0.37` | 1,030,000.00 USD |
| `15M` | `Kraken` | `31.69%` | `68.31%` | `0.46` | 14,060,000.00 USD |
| `15M` | `Aster` | `28.52%` | `71.48%` | `0.40` | 21,430,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `49.12%` | `50.88%` | `0.97` | 16,370,000.00 USD |
| `15M` | `Whale Positions` | `29.94%` | `70.06%` | `0.43` | 497,640,000.00 USD |
| `15M` | `Global Accounts` | `38.24%` | `61.76%` | `0.62` | 1,290,000,000.00 USD |
| `1H` | `ETH` | `44.79%` | `55.21%` | `0.81` | 4,130,000,000.00 USD |
| `1H` | `Binance` | `40.25%` | `59.75%` | `0.67` | 1,430,000,000.00 USD |
| `1H` | `OKX` | `44.89%` | `55.11%` | `0.81` | 531,620,000.00 USD |
| `1H` | `Bybit` | `44.39%` | `55.61%` | `0.80` | 375,700,000.00 USD |
| `1H` | `KuCoin` | `24.12%` | `75.88%` | `0.32` | 16,250,000.00 USD |
| `1H` | `Gate` | `48.41%` | `51.59%` | `0.94` | 486,840,000.00 USD |
| `1H` | `Bitget` | `41.3%` | `58.7%` | `0.70` | 228,690,000.00 USD |
| `1H` | `BingX` | `50.46%` | `49.54%` | `1.02` | 73,830,000.00 USD |
| `1H` | `MEXC` | `52.13%` | `47.87%` | `1.09` | 211,200,000.00 USD |
| `1H` | `Bitunix` | `48.56%` | `51.44%` | `0.94` | 180,280,000.00 USD |
| `1H` | `Hyperliquid` | `44.87%` | `55.13%` | `0.81` | 168,690,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `61.29%` | `38.71%` | `1.58` | 31,860,000.00 USD |
| `1H` | `Crypto.com` | `47.38%` | `52.62%` | `0.90` | 28,910,000.00 USD |
| `1H` | `WhiteBIT` | `67.43%` | `32.57%` | `2.07` | 82,400,000.00 USD |
| `1H` | `HTX` | `44.96%` | `55.04%` | `0.82` | 16,390,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `55.76%` | `44.24%` | `1.26` | 90,350,000.00 USD |
| `1H` | `Bitfinex` | `37.96%` | `62.04%` | `0.61` | 2,740,000.00 USD |
| `1H` | `Kraken` | `41.97%` | `58.03%` | `0.72` | 35,310,000.00 USD |
| `1H` | `Aster` | `38.07%` | `61.93%` | `0.61` | 57,680,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `49.47%` | `50.53%` | `0.98` | 70,030,000.00 USD |
| `1H` | `Whale Positions` | `40.25%` | `59.75%` | `0.67` | 1,430,000,000.00 USD |
| `1H` | `Global Accounts` | `44.79%` | `55.21%` | `0.81` | 4,130,000,000.00 USD |
| `4H` | `ETH` | `50.27%` | `49.73%` | `1.01` | 21,200,000,000.00 USD |
| `4H` | `Binance` | `49.92%` | `50.08%` | `1.00` | 6,780,000,000.00 USD |
| `4H` | `OKX` | `49.95%` | `50.05%` | `1.00` | 3,060,000,000.00 USD |
| `4H` | `Bybit` | `49.68%` | `50.32%` | `0.99` | 2,100,000,000.00 USD |
| `4H` | `KuCoin` | `47.16%` | `52.84%` | `0.89` | 84,120,000.00 USD |
| `4H` | `Gate` | `50.1%` | `49.9%` | `1.00` | 2,510,000,000.00 USD |
| `4H` | `Bitget` | `49.48%` | `50.52%` | `0.98` | 1,270,000,000.00 USD |
| `4H` | `BingX` | `49.43%` | `50.57%` | `0.98` | 382,470,000.00 USD |
| `4H` | `MEXC` | `54.42%` | `45.58%` | `1.19` | 1,150,000,000.00 USD |
| `4H` | `Bitunix` | `47.79%` | `52.21%` | `0.92` | 1,080,000,000.00 USD |
| `4H` | `Hyperliquid` | `53.02%` | `46.98%` | `1.13` | 951,000,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.17%` | `50.83%` | `0.97` | 133,310,000.00 USD |
| `4H` | `Crypto.com` | `47.9%` | `52.1%` | `0.92` | 137,930,000.00 USD |
| `4H` | `WhiteBIT` | `55.74%` | `44.26%` | `1.26` | 367,250,000.00 USD |
| `4H` | `HTX` | `47.04%` | `52.96%` | `0.89` | 85,180,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `51.18%` | `48.82%` | `1.05` | 424,330,000.00 USD |
| `4H` | `Bitfinex` | `65.7%` | `34.3%` | `1.92` | 29,280,000.00 USD |
| `4H` | `Kraken` | `52.8%` | `47.2%` | `1.12` | 162,910,000.00 USD |
| `4H` | `Aster` | `47.93%` | `52.07%` | `0.92` | 228,690,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.33%` | `49.67%` | `1.01` | 266,050,000.00 USD |
| `4H` | `Whale Positions` | `49.92%` | `50.08%` | `1.00` | 6,780,000,000.00 USD |
| `4H` | `Global Accounts` | `50.27%` | `49.73%` | `1.01` | 21,200,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `2361.25` | `2356.05` | `2361.25` | `2364.75` | `2343.75` | 331,920,007.02 USD | 204,886,521.51 USD | 127,033,485.50 USD | 77,853,036.01 USD | `+23.46%` | `11B / 0S` |
| `5:00 UTC` | `2357.75` | `2358.45` | `2357.75` | `2365.75` | `2355.25` | 136,642,531.53 USD | 60,568,643.70 USD | 76,073,887.82 USD | -15,505,244.12 USD | `-11.35%` | `1B / 5S` |
| `0:00 UTC` | `2364.75` | `2364.47` | `2364.75` | `2369.25` | `2356.75` | 211,703,599.24 USD | 122,647,689.31 USD | 89,055,909.93 USD | 33,591,779.37 USD | `+15.87%` | `9B / 0S` |
| `5:00 UTC` | `2370.25` | `2367.30` | `2370.25` | `2372.25` | `2362.75` | 152,368,912.49 USD | 65,939,044.63 USD | 86,429,867.86 USD | -20,490,823.24 USD | `-13.45%` | `0B / 0S` |
| `0:00 UTC` | `2367.25` | `2370.68` | `2367.25` | `2378.75` | `2362.25` | 227,963,041.65 USD | 108,724,843.75 USD | 119,238,197.91 USD | -10,513,354.16 USD | `-4.61%` | `6B / 3S` |
| `5:00 UTC` | `2360.25` | `2359.15` | `2360.25` | `2367.25` | `2354.75` | 178,447,053.53 USD | 59,723,171.00 USD | 118,723,882.53 USD | -59,000,711.54 USD | `-33.06%` | `0B / 9S` |
| `0:00 UTC` | `2358.25` | `2354.41` | `2358.25` | `2359.25` | `2350.25` | 125,220,561.61 USD | 53,594,674.80 USD | 71,625,886.81 USD | -18,031,212.02 USD | `-14.40%` | `0B / 1S` |
| `5:00 UTC` | `2353.75` | `2353.63` | `2353.75` | `2358.25` | `2350.75` | 70,925,128.95 USD | 26,607,996.94 USD | 44,317,132.01 USD | -17,709,135.06 USD | `-24.97%` | `0B / 2S` |
| `0:00 UTC` | `2350.75` | `2351.46` | `2350.75` | `2353.75` | `2348.75` | 91,943,279.10 USD | 36,371,657.16 USD | 55,571,621.93 USD | -19,199,964.77 USD | `-20.88%` | `0B / 3S` |
| `5:00 UTC` | `2348.75` | `2348.71` | `2348.75` | `2351.75` | `2346.75` | 58,565,811.02 USD | 28,811,133.49 USD | 29,754,677.53 USD | -943,544.04 USD | `-1.61%` | `2B / 1S` |

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
| `5m` | -370,890.00 USD | -14,760,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -477,700.00 USD | -34,650,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -887,860.00 USD | -64,200,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -6,390,000.00 USD | -225,600,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 7,150,000.00 USD | -211,440,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 24,800,000.00 USD | 115,760,000.00 USD | **`ACCUMULATION`** |
| `6h` | 21,540,000.00 USD | 83,800,000.00 USD | **`ACCUMULATION`** |
| `8h` | 17,520,000.00 USD | 70,570,000.00 USD | **`ACCUMULATION`** |
| `12h` | 28,190,000.00 USD | -99,880,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,850,000.00 USD | -139,300,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -7,240,000.00 USD | -821,450,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,000,000,000.00 USD | -7,950,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-370.89K` | 15m=`-477.70K` | 1h=`-6.39M` | 24h=`-2.85M`
* Futures Capital Netflows: 5m=`-14.76M` | 15m=`-34.65M` | 1h=`-225.60M` | 24h=`-139.30M`
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
  * `2026-10-29 22:45:14 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:14 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [dol.gov] - (Sentiment: `Neutral`)


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
  * Execution Entry: `2293.68` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2275.41` (Risk Distance: `18.27` pts)
  * +2.5R Take Profit: `2339.36`
  * Mathematical Lot Sizing: **`0.54 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2337.88` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2356.15` (Risk Distance: `18.27` pts)
  * +2.5R Take Profit: `2292.20`
  * Mathematical Lot Sizing: **`0.54 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2367.89`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
