# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-29 23:10:16 IST` (`2026-10-29 17:40:16 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2345.00` | **Live Ask Quote**: `2348.10` | **Mid Price**: `2346.55`
- **Spread Points**: `310.00` | **Spread BPS**: `13.21 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2323.30` | VWAP Z-Score: `+1.21` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `11.14` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `55.97` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2380.33` | Lower -3.00σ Band: `2266.27`
  * Upper +2.51σ Band: `2371.01` | Lower -2.51σ Band: `2275.59`
  * Upper +2.01σ Band: `2361.51` | Lower -2.01σ Band: `2285.09`
  * Upper +2.00σ Band: `2361.32` | Lower -2.00σ Band: `2285.28`
  * Upper +1.28σ Band: `2347.63` | Lower -1.28σ Band: `2298.97`
  * Upper +1.00σ Band: `2342.31` | Lower -1.00σ Band: `2304.29`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2349.66` | EMA-20=`2342.83` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2333.07` (Slope: `+0.0000`) | EMA-100=`2332.02`
  * Institutional Anchors: EMA-144=`2331.80` | EMA-200=`2330.36` (Slope: `+0.1253`) | EMA-233=`2329.05`
- **Range Boundaries**: 24H High=`2387.80` | 24H Low=`2288.80` | Weekly High=`2387.80` | Weekly Low=`2288.80`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2339.60` (Distance: `+0.33%`)
  * Point of Control (POC) = `2318.94` (Distance: `+1.23%`)
  * Value Area Low (VAL) = `2293.68` (Distance: `+2.34%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `2337.16` - `2355.94`
  * Optimal Trade Entry (OTE 0.705): `2351.24`
  * Structural Invalidation Anchor (0.786): `2365.32`

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
| --- | **`2346.55`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2346.10` | `513.0280` | 1,203,614.99 USD | 11,335,102.86 USD | `15 orders` | `-0.08%` | `-` |
| `BID` | `2346.20` | `232.9388` | 546,521.01 USD | 10,131,487.86 USD | `15 orders` | `-0.08%` | `-` |
| `BID` | `2346.30` | `193.1318` | 453,145.14 USD | 9,584,966.85 USD | `17 orders` | `-0.07%` | `-` |
| `BID` | `2346.40` | `210.9101` | 494,879.46 USD | 9,131,821.71 USD | `17 orders` | `-0.07%` | `-` |
| `BID` | `2346.50` | `109.1558` | 256,134.08 USD | 8,636,942.25 USD | `19 orders` | `-0.07%` | `-` |
| `BID` | `2346.60` | `307.7871` | 722,253.21 USD | 8,380,808.17 USD | `21 orders` | `-0.06%` | `-` |
| `BID` | `2346.70` | `368.4170` | 864,564.17 USD | 7,658,554.96 USD | `15 orders` | `-0.06%` | `-` |
| `BID` | `2346.80` | `184.4757` | 432,927.57 USD | 6,793,990.78 USD | `20 orders` | `-0.05%` | `-` |
| `BID` | `2346.90` | `151.0796` | 354,568.71 USD | 6,361,063.21 USD | `11 orders` | `-0.05%` | `-` |
| `BID` | `2347.00` | `354.8943` | 832,936.92 USD | 6,006,494.50 USD | `20 orders` | `-0.04%` | `-` |
| `BID` | `2347.10` | `284.8915` | 668,668.84 USD | 5,173,557.58 USD | `20 orders` | `-0.04%` | `-` |
| `BID` | `2347.20` | `334.7294` | 785,676.85 USD | 4,504,888.74 USD | `27 orders` | `-0.04%` | `-` |
| `BID` | `2347.30` | `312.6965` | 733,992.49 USD | 3,719,211.89 USD | `24 orders` | `-0.03%` | `-` |
| `BID` | `2347.40` | `222.9865` | 523,438.51 USD | 2,985,219.39 USD | `20 orders` | `-0.03%` | `-` |
| `BID` | `2347.50` | `179.7520` | 421,967.82 USD | 2,461,780.88 USD | `20 orders` | `-0.02%` | `-` |
| `BID` | `2347.60` | `214.5153` | 503,596.12 USD | 2,039,813.06 USD | `23 orders` | `-0.02%` | `-` |
| `BID` | `2347.70` | `351.7533` | 825,811.22 USD | 1,536,216.95 USD | `31 orders` | `-0.01%` | `-` |
| `BID` | `2347.80` | `152.2248` | 357,393.39 USD | 710,405.72 USD | `11 orders` | `-0.01%` | `-` |
| `BID` | `2347.90` | `7.7519` | 18,200.69 USD | 353,012.34 USD | `5 orders` | `-0.01%` | `-` |
| `BID` | `2348.00` | `142.5944` | 334,811.65 USD | 334,811.65 USD | `45 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2348.05` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,348.05` | `0.00%` | `-` |
| `ASK` | `2348.10` | `37.4266` | 87,881.40 USD | 87,881.40 USD | `9 orders` | `+0.00%` | `-` |
| `ASK` | `2348.20` | `12.7659` | 29,976.89 USD | 117,858.29 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `2348.30` | `112.8144` | 264,922.06 USD | 382,780.34 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `2348.40` | `137.7139` | 323,407.32 USD | 706,187.66 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `2348.50` | `256.9372` | 603,417.01 USD | 1,309,604.68 USD | `11 orders` | `+0.02%` | `-` |
| `ASK` | `2348.60` | `233.9973` | 549,566.06 USD | 1,859,170.74 USD | `18 orders` | `+0.02%` | `-` |
| `ASK` | `2348.70` | `302.9560` | 711,552.76 USD | 2,570,723.49 USD | `20 orders` | `+0.03%` | `-` |
| `ASK` | `2348.80` | `261.8863` | 615,118.54 USD | 3,185,842.04 USD | `20 orders` | `+0.03%` | `-` |
| `ASK` | `2348.90` | `388.2165` | 911,881.74 USD | 4,097,723.77 USD | `13 orders` | `+0.04%` | `-` |
| `ASK` | `2349.00` | `386.2536` | 907,309.71 USD | 5,005,033.48 USD | `27 orders` | `+0.04%` | `-` |
| `ASK` | `2349.10` | `220.4987` | 517,973.50 USD | 5,523,006.98 USD | `16 orders` | `+0.04%` | `-` |
| `ASK` | `2349.20` | `198.8753` | 467,197.85 USD | 5,990,204.83 USD | `22 orders` | `+0.05%` | `-` |
| `ASK` | `2349.30` | `317.6998` | 746,372.14 USD | 6,736,576.97 USD | `16 orders` | `+0.05%` | `-` |
| `ASK` | `2349.40` | `240.9304` | 566,041.88 USD | 7,302,618.85 USD | `16 orders` | `+0.06%` | `-` |
| `ASK` | `2349.50` | `303.3544` | 712,731.16 USD | 8,015,350.01 USD | `20 orders` | `+0.06%` | `-` |
| `ASK` | `2349.60` | `296.7845` | 697,324.86 USD | 8,712,674.88 USD | `17 orders` | `+0.07%` | `-` |
| `ASK` | `2349.70` | `389.0617` | 914,178.28 USD | 9,626,853.15 USD | `21 orders` | `+0.07%` | `-` |
| `ASK` | `2349.80` | `324.6115` | 762,772.10 USD | 10,389,625.26 USD | `20 orders` | `+0.07%` | `-` |
| `ASK` | `2349.90` | `111.6830` | 262,443.88 USD | 10,652,069.14 USD | `8 orders` | `+0.08%` | `-` |
| `ASK` | `2350.00` | `200.8128` | 471,910.08 USD | 11,123,979.22 USD | `14 orders` | `+0.08%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:06:38 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1892.00` | `8,092.45` | 15,310,914.71 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-29 23:06:38 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1918.00` | `4,184.01` | 8,024,935.59 USD | `TRIGGER_STOP` | `0x6ea486a342` | `2026-10-29 23:06:38 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `8,500.00` | 16,371,850.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-29 23:06:38 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2040.65` | `7,964.66` | 16,253,082.08 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-29 23:06:38 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2101.66` | `10,000.00` | 21,016,620.86 USD | `AT_RISK_LIQ` | `0x469e9a7f62` | `2026-10-29 23:06:38 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2171.11` | `48,499.51` | 105,297,832.78 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-29 23:06:38 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2180.17` | `44,734.81` | 97,529,693.12 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-29 23:06:38 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2250.00` | `6,500.00` | 14,625,000.00 USD | `TRIGGER_STOP` | `0x6eae4120a8` | `2026-10-29 23:06:38 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2292.00` | `2,500.00` | 5,730,000.00 USD | `TRIGGER_STOP` | `0x934de82f50` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2303.00` | `908.97` | 2,093,354.23 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x0c4a3a7ac7` | `2026-10-29 23:06:38 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2307.20` | `599,999.99` | 1,384,319,976.93 USD | `TRIGGER_STOP` | `0x069604ebfb` | `2026-10-29 23:06:38 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2310.00` | `2,000.00` | 4,620,000.00 USD | `TRIGGER_STOP` | `0x524ed67d71` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2310.20` | `1,960.39` | 4,528,897.14 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2311.00` | `1,015.35` | 2,346,465.99 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x674982e841` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2315.00` | `5,430.46` | 12,571,509.81 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-29 23:06:38 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2319.00` | `2,500.00` | 5,797,500.00 USD | `TRIGGER_STOP` | `0x524ed67d71` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2322.80` | `1,372.64` | 3,188,370.28 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2329.00` | `343.53` | 800,091.38 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2329.20` | `600.63` | 1,398,994.38 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2331.70` | `929.33` | 2,166,915.73 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2334.80` | `2,794.82` | 6,525,348.07 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2334.90` | `406.95` | 950,177.51 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x7b7f72a28f` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2336.30` | `433.30` | 1,012,314.12 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2338.10` | `639.03` | 1,494,114.64 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2338.20` | `1,712.54` | 4,004,268.28 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2338.50` | `600.35` | 1,403,920.81 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2340.20` | `332.56` | 778,259.49 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2340.40` | `1,283.21` | 3,003,220.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2341.10` | `600.63` | 1,406,132.55 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2341.80` | `854.96` | 2,002,141.11 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2343.50` | `468.50` | 1,097,928.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2343.80` | `433.07` | 1,015,029.47 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2344.40` | `385.64` | 904,088.09 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x76bf72092b` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2345.10` | `640.31` | 1,501,593.80 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2345.10` | `331.32` | 776,975.25 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2345.70` | `426.76` | 1,001,046.24 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2345.70` | `400.45` | 939,340.26 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2352.70` | `327.92` | 771,490.09 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2353.10` | `425.45` | 1,001,121.69 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2353.80` | `384.11` | 904,122.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x76bf72092b` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2354.40` | `400.48` | 942,883.05 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2355.40` | `637.52` | 1,501,612.72 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2356.80` | `433.28` | 1,021,154.30 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2357.10` | `466.10` | 1,098,636.30 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2357.70` | `849.19` | 2,002,131.73 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2358.80` | `1,427.73` | 3,367,734.24 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2359.10` | `600.60` | 1,416,866.02 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2360.70` | `327.00` | 771,953.86 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2360.90` | `662.26` | 1,563,523.02 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2361.60` | `1,271.72` | 3,003,295.37 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2361.90` | `1,695.37` | 4,004,297.47 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2363.80` | `600.48` | 1,419,424.08 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2365.10` | `433.25` | 1,024,677.21 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2366.80` | `391.11` | 925,682.70 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x7b7f72a28f` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2366.90` | `2,797.90` | 6,622,353.06 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2367.80` | `958.39` | 2,269,272.53 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2372.50` | `600.47` | 1,424,605.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2375.00` | `336.88` | 800,091.43 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2377.80` | `1,380.91` | 3,283,532.32 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2388.70` | `5,408.95` | 12,920,349.79 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2389.40` | `1,947.85` | 4,654,188.25 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 23:06:38 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2396.00` | `500.00` | 1,198,000.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xaa53f4044a` | `2026-10-29 23:06:38 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2440.00` | `4,002.10` | 9,765,127.17 USD | `TRIGGER_STOP` | `0xfb941d2344` | `2026-10-29 23:06:38 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `3,058.48` | 7,688,708.10 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-29 23:06:38 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2658.62` | `9,700.00` | 25,788,617.00 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-29 23:06:38 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2708.97` | `8,500.00` | 23,026,257.07 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-29 23:06:38 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 250,039,054.24 USD | `106,417.71` | `2322.74` | `2348.54` | `3788.91` | -2,858,042.08 USD | `-1.14%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 153,160,422.87 USD | `65,205.17` | `2375.30` | `2348.54` | `4310.21` | 1,721,840.22 USD | `+1.12%` | `5X Cross` |
| `6` | `0x77dd...e0e9` | `LONG` | 113,954,453.16 USD | `48,499.51` | `2610.31` | `2348.54` | `2171.14` | -12,644,430.71 USD | `-11.10%` | `10X Cross` |
| `7` | `0x0392...d7d9` | `LONG` | 105,077,603.20 USD | `44,734.81` | `2518.71` | `2348.54` | `2180.20` | -7,596,703.38 USD | `-7.23%` | `9X Cross` |
| `15` | `0xde8d...9524` | `LONG` | 71,136,394.06 USD | `30,282.40` | `2134.45` | `2348.54` | `1787.09` | 6,500,063.49 USD | `+9.14%` | `20X Cross` |
| `17` | `0x7fda...17d1` | `SHORT` | 65,928,811.77 USD | `28,069.15` | `2437.87` | `2348.54` | `3663.49` | 2,500,224.38 USD | `+3.79%` | `25X Cross` |
| `25` | `0xdf95...7d72` | `SHORT` | 53,205,803.04 USD | `22,652.33` | `2402.54` | `2348.54` | `3947.68` | 1,217,369.92 USD | `+2.29%` | `25X Cross` |
| `29` | `0xeced...6210` | `SHORT` | 43,912,066.79 USD | `18,687.58` | `2522.09` | `2348.54` | `3355.26` | 3,219,845.67 USD | `+7.33%` | `20X Cross` |
| `34` | `0xb695...a92d` | `SHORT` | 39,249,173.98 USD | `16,704.62` | `2557.74` | `2348.54` | `4007.77` | 3,476,991.07 USD | `+8.86%` | `20X Cross` |
| `35` | `0x6046...b21d` | `LONG` | 37,415,500.96 USD | `15,927.59` | `2410.19` | `2348.54` | `1529.59` | -973,118.68 USD | `-2.60%` | `6X Cross` |
| `39` | `0x45d2...4029` | `SHORT` | 32,776,920.00 USD | `13,950.00` | `2443.60` | `2348.54` | `4889.33` | 1,311,362.46 USD | `+4.00%` | `20X Cross` |
| `44` | `0xbd1c...ff0e` | `LONG` | 28,197,600.00 USD | `12,000.00` | `2419.91` | `2348.54` | `1520.97` | -841,432.39 USD | `-2.98%` | `20X Cross` |
| `45` | `0x2371...0883` | `LONG` | 28,186,800.00 USD | `12,000.00` | `2421.77` | `2348.54` | `1280.07` | -874,494.85 USD | `-3.10%` | `20X Cross` |
| `50` | `0x09dc...c094` | `LONG` | 25,850,000.00 USD | `11,000.00` | `2465.31` | `2348.54` | `1638.04` | -1,268,423.04 USD | `-4.91%` | `20X Cross` |
| `51` | `0x6c93...59a4` | `LONG` | 25,842,300.00 USD | `11,000.00` | `2441.15` | `2348.54` | `1603.00` | -1,010,372.73 USD | `-3.91%` | `20X Cross` |
| `52` | `0xa9de...e049` | `LONG` | 25,841,200.00 USD | `11,000.00` | `2481.81` | `2348.54` | `1644.71` | -1,458,779.46 USD | `-5.65%` | `20X Cross` |
| `53` | `0x0c5d...36b3` | `LONG` | 25,840,100.00 USD | `11,000.00` | `2482.20` | `2348.54` | `1645.04` | -1,464,153.24 USD | `-5.67%` | `20X Cross` |
| `56` | `0xa61c...66b9` | `LONG` | 25,573,734.40 USD | `10,888.00` | `2398.32` | `2348.54` | `1385.61` | -539,222.99 USD | `-2.11%` | `10X Cross` |
| `58` | `0x4487...c92d` | `SHORT` | 25,179,186.03 USD | `10,715.46` | `2373.98` | `2348.54` | `2879.57` | 259,198.66 USD | `+1.03%` | `10X Cross` |
| `63` | `0xecb6...2b00` | `SHORT` | 24,170,779.73 USD | `10,290.25` | `2327.63` | `2348.54` | `5240.90` | -218,812.23 USD | `-0.91%` | `15X Cross` |
| `66` | `0xa2ce...3126` | `LONG` | 23,535,649.97 USD | `10,016.88` | `2162.83` | `2348.54` | `1442.45` | 1,870,847.92 USD | `+7.95%` | `10X Cross` |
| `67` | `0xec7f...df39` | `LONG` | 23,500,000.00 USD | `10,000.00` | `2719.35` | `2348.54` | `1721.56` | -3,693,548.52 USD | `-15.72%` | `20X Cross` |
| `68` | `0x6646...6de5` | `LONG` | 23,498,000.00 USD | `10,000.00` | `1765.80` | `2348.54` | `1737.32` | 5,839,942.55 USD | `+24.85%` | `25X Cross` |
| `69` | `0x469e...58a5` | `LONG` | 23,494,000.00 USD | `10,000.00` | `2463.91` | `2348.54` | `2101.75` | -1,145,141.54 USD | `-4.87%` | `25X Cross` |
| `70` | `0x15a4...dfdb` | `LONG` | 23,492,000.00 USD | `10,000.00` | `1761.94` | `2348.54` | `0.000000` | 5,872,518.97 USD | `+25.00%` | `20X Cross` |
| `78` | `0xaeaa...2416` | `SHORT` | 22,783,360.00 USD | `9,700.00` | `2311.92` | `2348.54` | `2658.65` | -357,677.60 USD | `-1.57%` | `25X Cross` |
| `83` | `0xca49...53c8` | `SHORT` | 21,767,308.59 USD | `9,264.26` | `2549.47` | `2348.54` | `3702.77` | 1,851,716.15 USD | `+8.51%` | `25X Cross` |
| `85` | `0xba5d...a352` | `SHORT` | 21,271,754.46 USD | `9,054.12` | `2493.89` | `2348.54` | `2897.62` | 1,308,252.80 USD | `+6.15%` | `20X Cross` |
| `86` | `0xea00...a918` | `LONG` | 21,149,087.60 USD | `9,003.83` | `2003.01` | `2348.54` | `1174.17` | 3,114,308.73 USD | `+14.73%` | `5X Cross` |
| `93` | `0xb37f...66ca` | `SHORT` | 19,971,600.00 USD | `8,500.00` | `2308.30` | `2348.54` | `2709.00` | -351,045.81 USD | `-1.76%` | `25X Cross` |
| `105` | `0x9eec...daab` | `LONG` | 19,014,025.45 USD | `8,092.45` | `1658.44` | `2348.54` | `1917.76` | 5,593,160.93 USD | `+29.42%` | `15X Cross` |
| `107` | `0x218a...7da2` | `SHORT` | 18,787,592.98 USD | `7,997.78` | `2208.16` | `2348.54` | `2877.22` | -1,127,197.77 USD | `-6.00%` | `10X Cross` |
| `108` | `0x5f91...65aa` | `LONG` | 18,708,180.24 USD | `7,964.66` | `1626.99` | `2348.54` | `2040.68` | 5,749,737.18 USD | `+30.73%` | `16X Cross` |
| `113` | `0xcf53...ee11` | `SHORT` | 17,867,004.84 USD | `7,603.63` | `1862.69` | `2348.54` | `3979.39` | -3,703,740.90 USD | `-20.73%` | `7X Cross` |
| `114` | `0x524e...0de0` | `LONG` | 17,616,000.00 USD | `7,500.00` | `2320.35` | `2348.54` | `2115.20` | 213,313.78 USD | `+1.21%` | `10X Cross` |
| `119` | `0x939f...04d2` | `LONG` | 16,969,458.88 USD | `7,223.81` | `2500.18` | `2348.54` | `1824.71` | -1,091,431.29 USD | `-6.43%` | `25X Cross` |
| `121` | `0xec0b...b078` | `LONG` | 16,463,421.96 USD | `7,007.80` | `2065.97` | `2348.54` | `992.48` | 1,985,492.37 USD | `+12.06%` | `25X Cross` |
| `122` | `0x1ee7...edf5` | `LONG` | 16,442,300.00 USD | `7,000.00` | `2330.22` | `2348.54` | `2153.90` | 130,737.80 USD | `+0.80%` | `25X Cross` |
| `130` | `0x418a...8888` | `SHORT` | 15,802,299.58 USD | `6,724.38` | `2494.55` | `2348.54` | `2953.46` | 972,023.59 USD | `+6.15%` | `25X Cross` |
| `132` | `0x4ff9...38d3` | `LONG` | 15,421,693.49 USD | `6,564.10` | `2447.40` | `2348.54` | `1670.66` | -643,329.26 USD | `-4.17%` | `3X Isolated` |
| `134` | `0xf78c...c581` | `LONG` | 15,268,370.28 USD | `6,500.22` | `2521.53` | `2348.54` | `1914.14` | -1,122,170.67 USD | `-7.35%` | `20X Cross` |
| `140` | `0x799f...5f4c` | `LONG` | 14,826,205.12 USD | `6,310.90` | `2390.33` | `2348.54` | `1700.89` | -258,959.49 USD | `-1.75%` | `20X Cross` |
| `142` | `0x08bf...7872` | `SHORT` | 14,624,021.77 USD | `6,224.05` | `2258.00` | `2348.54` | `2585.90` | -570,105.66 USD | `-3.90%` | `20X Cross` |
| `146` | `0x0622...8088` | `LONG` | 14,235,623.85 USD | `6,058.85` | `2353.89` | `2348.54` | `653.24` | -26,257.53 USD | `-0.18%` | `5X Cross` |
| `151` | `0xd9e7...4aff` | `LONG` | 14,095,200.00 USD | `6,000.00` | `2480.18` | `2348.54` | `1408.43` | -785,924.33 USD | `-5.58%` | `20X Cross` |
| `159` | `0x0c4a...1b19` | `LONG` | 13,408,866.53 USD | `5,706.39` | `2382.15` | `2348.54` | `2185.19` | -184,604.65 USD | `-1.38%` | `25X Isolated` |
| `177` | `0x645b...87b8` | `SHORT` | 11,920,283.87 USD | `5,073.54` | `2421.68` | `2348.54` | `6084.79` | 366,222.08 USD | `+3.07%` | `10X Cross` |
| `185` | `0x45ab...6cbc` | `LONG` | 11,558,356.02 USD | `4,920.96` | `2727.66` | `2348.54` | `1353.08` | -1,864,387.78 USD | `-16.13%` | `7X Cross` |
| `188` | `0xfb18...eb17` | `SHORT` | 11,448,300.06 USD | `4,872.45` | `2315.54` | `2348.54` | `2706.65` | -165,927.03 USD | `-1.45%` | `25X Cross` |
| `190` | `0x64b7...9da9` | `LONG` | 11,407,743.91 USD | `4,856.84` | `2604.61` | `2348.54` | `1385.58` | -1,242,470.50 USD | `-10.89%` | `25X Cross` |
| `197` | `0x5559...d43b` | `SHORT` | 11,172,619.71 USD | `4,755.93` | `2262.69` | `2348.54` | `2878.32` | -411,413.84 USD | `-3.68%` | `25X Cross` |
| `212` | `0xe091...6705` | `SHORT` | 10,570,950.47 USD | `4,500.00` | `2467.33` | `2348.54` | `2572.95` | 532,058.04 USD | `+5.03%` | `20X Cross` |
| `219` | `0xfe7c...b7ae` | `SHORT` | 10,341,226.27 USD | `4,402.58` | `2440.17` | `2348.54` | `4140.72` | 401,861.60 USD | `+3.89%` | `25X Cross` |
| `230` | `0xc179...e0c8` | `LONG` | 10,121,343.50 USD | `4,309.16` | `2342.89` | `2348.54` | `922.09` | 25,464.70 USD | `+0.25%` | `10X Cross` |
| `234` | `0x12d2...f97f` | `LONG` | 10,016,083.44 USD | `4,264.34` | `2623.90` | `2348.54` | `1817.79` | -1,173,150.98 USD | `-11.71%` | `20X Cross` |
| `241` | `0x28bb...fca6` | `SHORT` | 9,887,541.83 USD | `4,209.61` | `1896.10` | `2348.54` | `3046.91` | -1,905,659.27 USD | `-19.27%` | `20X Cross` |
| `242` | `0x6ea4...0ea7` | `SHORT` | 9,831,592.10 USD | `4,184.01` | `2602.13` | `2348.54` | `3425.97` | 1,055,754.56 USD | `+10.74%` | `20X Cross` |
| `253` | `0x5e9e...35ee` | `SHORT` | 9,411,744.56 USD | `4,007.56` | `1796.39` | `2348.54` | `2586.46` | -2,212,594.47 USD | `-23.51%` | `20X Cross` |
| `254` | `0xfb94...0ddf` | `SHORT` | 9,401,336.16 USD | `4,002.10` | `2382.44` | `2348.54` | `5105.36` | 133,447.99 USD | `+1.42%` | `20X Cross` |
| `255` | `0x8cc9...2b6a` | `SHORT` | 9,399,600.00 USD | `4,000.00` | `1791.18` | `2348.54` | `3817.71` | -2,234,853.33 USD | `-23.78%` | `25X Cross` |
| `256` | `0xec4a...cf62` | `LONG` | 9,397,200.00 USD | `4,000.00` | `2318.70` | `2348.54` | `1894.59` | 122,369.92 USD | `+1.30%` | `25X Cross` |
| `257` | `0x95fe...f8fa` | `LONG` | 9,395,600.00 USD | `4,000.00` | `2341.35` | `2348.54` | `2258.96` | 30,183.49 USD | `+0.32%` | `20X Isolated` |
| `258` | `0x3dc9...54b0` | `SHORT` | 9,394,872.31 USD | `3,999.69` | `2480.32` | `2348.54` | `5785.73` | 525,664.24 USD | `+5.60%` | `20X Cross` |
| `260` | `0x77ee...2902` | `SHORT` | 9,357,441.94 USD | `3,982.23` | `2476.53` | `2348.54` | `4321.53` | 504,679.64 USD | `+5.39%` | `25X Cross` |
| `271` | `0xf02d...5eb3` | `LONG` | 9,058,866.74 USD | `3,855.99` | `2513.67` | `2348.54` | `317.29` | -633,845.58 USD | `-7.00%` | `20X Cross` |
| `273` | `0x4b67...f4e7` | `LONG` | 8,975,539.71 USD | `3,820.84` | `2591.51` | `2348.54` | `1579.77` | -926,233.84 USD | `-10.32%` | `20X Cross` |
| `290` | `0x382b...3e39` | `SHORT` | 8,509,309.45 USD | `3,622.83` | `2299.47` | `2348.54` | `3750.78` | -178,710.82 USD | `-2.10%` | `25X Cross` |
| `295` | `0x8ae4...3d60` | `LONG` | 8,361,054.37 USD | `3,558.20` | `2482.21` | `2348.54` | `308.94` | -471,143.67 USD | `-5.63%` | `10X Cross` |
| `323` | `0x9c06...0560` | `SHORT` | 7,761,100.49 USD | `3,303.58` | `2270.55` | `2348.54` | `3270.74` | -260,136.55 USD | `-3.35%` | `25X Cross` |
| `332` | `0x984e...14c2` | `SHORT` | 7,312,547.99 USD | `3,111.99` | `2357.50` | `2348.54` | `2434.93` | 23,974.77 USD | `+0.33%` | `20X Cross` |
| `335` | `0x9c2a...f6a8` | `SHORT` | 7,184,059.21 USD | `3,058.48` | `2543.83` | `2348.54` | `2590.74` | 596,201.41 USD | `+8.30%` | `20X Cross` |
| `340` | `0x39b4...5c34` | `SHORT` | 7,048,841.02 USD | `3,000.91` | `2329.97` | `2348.54` | `2405.85` | -56,797.27 USD | `-0.81%` | `25X Cross` |
| `341` | `0x4a20...3c26` | `LONG` | 7,048,800.00 USD | `3,000.00` | `2428.72` | `2348.54` | `171.12` | -237,360.28 USD | `-3.37%` | `20X Cross` |
| `342` | `0x007d...67a0` | `LONG` | 7,048,800.00 USD | `3,000.00` | `2400.00` | `2348.54` | `1492.88` | -151,200.00 USD | `-2.15%` | `25X Cross` |
| `381` | `0xf517...c032` | `SHORT` | 6,432,548.56 USD | `2,738.07` | `2053.90` | `2348.54` | `5640.96` | -808,806.65 USD | `-12.57%` | `25X Cross` |
| `395` | `0xc619...10f5` | `LONG` | 6,108,180.00 USD | `2,600.00` | `2318.40` | `2348.54` | `1844.90` | 80,331.09 USD | `+1.32%` | `25X Cross` |
| `396` | `0xbb34...1696` | `LONG` | 6,106,880.00 USD | `2,600.00` | `2318.80` | `2348.54` | `1959.94` | 77,979.15 USD | `+1.28%` | `25X Cross` |
| `404` | `0x8328...f54a` | `SHORT` | 6,052,341.28 USD | `2,576.45` | `2292.01` | `2348.54` | `3280.20` | -147,069.99 USD | `-2.43%` | `25X Cross` |
| `405` | `0xed48...7c9b` | `SHORT` | 5,994,136.22 USD | `2,551.13` | `2460.02` | `2348.54` | `3239.40` | 281,710.19 USD | `+4.70%` | `20X Cross` |
| `408` | `0x934d...92c9` | `LONG` | 5,873,250.00 USD | `2,500.00` | `2343.98` | `2348.54` | `2146.08` | 13,285.49 USD | `+0.23%` | `25X Cross` |
| `426` | `0xfbe2...c8ea` | `SHORT` | 5,648,618.85 USD | `2,404.08` | `2041.57` | `2348.54` | `2705.14` | -740,526.12 USD | `-13.11%` | `20X Cross` |
| `435` | `0x1c98...7fc7` | `LONG` | 5,540,838.97 USD | `2,358.00` | `2467.15` | `2348.54` | `1897.18` | -276,732.51 USD | `-4.99%` | `10X Cross` |
| `455` | `0x6859...7e1e` | `SHORT` | 5,226,203.44 USD | `2,224.58` | `2200.39` | `2348.54` | `3605.50` | -331,250.72 USD | `-6.34%` | `25X Cross` |
| `463` | `0xd507...c948` | `SHORT` | 5,102,679.37 USD | `2,172.00` | `2387.49` | `2348.54` | `2707.38` | 82,961.66 USD | `+1.63%` | `5X Isolated` |
| `469` | `0xb829...3a81` | `LONG` | 5,061,690.85 USD | `2,153.91` | `2537.61` | `2348.54` | `795.37` | -404,105.88 USD | `-7.98%` | `20X Cross` |
| `505` | `0x3440...32c5` | `SHORT` | 4,699,927.82 USD | `2,000.57` | `2198.21` | `2348.54` | `3501.88` | -302,264.69 USD | `-6.43%` | `25X Cross` |
| `506` | `0xd4c1...3d1d` | `SHORT` | 4,698,854.26 USD | `2,000.53` | `2336.05` | `2348.54` | `4556.68` | -25,491.92 USD | `-0.54%` | `12X Cross` |
| `507` | `0xf929...d1f9` | `SHORT` | 4,698,400.00 USD | `2,000.00` | `2423.37` | `2348.54` | `2548.78` | 148,340.34 USD | `+3.16%` | `25X Cross` |
| `518` | `0x0514...bdfe` | `SHORT` | 4,582,110.00 USD | `1,950.00` | `1988.74` | `2348.54` | `2920.86` | -704,050.37 USD | `-15.37%` | `25X Cross` |
| `527` | `0x8376...9a1e` | `SHORT` | 4,487,946.15 USD | `1,910.50` | `2477.72` | `2348.54` | `3152.59` | 245,742.02 USD | `+5.48%` | `20X Cross` |
| `547` | `0x7a6d...f79c` | `SHORT` | 4,287,459.14 USD | `1,825.07` | `2433.80` | `2348.54` | `2778.75` | 154,409.74 USD | `+3.60%` | `25X Cross` |
| `555` | `0x541e...071d` | `SHORT` | 4,241,028.00 USD | `1,805.00` | `2648.19` | `2348.54` | `2986.61` | 538,956.84 USD | `+12.71%` | `25X Cross` |
| `557` | `0x7265...91a5` | `LONG` | 4,232,951.59 USD | `1,801.87` | `2533.96` | `2348.54` | `1988.11` | -332,914.86 USD | `-7.86%` | `20X Cross` |
| `558` | `0x739c...cfb2` | `SHORT` | 4,228,020.00 USD | `1,800.00` | `2427.60` | `2348.54` | `2693.52` | 141,676.38 USD | `+3.35%` | `25X Cross` |
| `564` | `0xa445...329d` | `LONG` | 4,174,650.16 USD | `1,776.75` | `2398.85` | `2348.54` | `1776.07` | -87,519.20 USD | `-2.10%` | `25X Cross` |
| `569` | `0x91a9...3f70` | `SHORT` | 4,151,633.77 USD | `1,767.48` | `2156.23` | `2348.54` | `3622.43` | -340,529.69 USD | `-8.20%` | `4X Cross` |
| `576` | `0x3453...b323` | `SHORT` | 4,110,864.15 USD | `1,750.12` | `2328.82` | `2348.54` | `2400.24` | -35,132.02 USD | `-0.85%` | `25X Cross` |
| `598` | `0xfeec...4e9c` | `SHORT` | 3,974,566.41 USD | `1,691.81` | `2566.49` | `2348.54` | `2649.93` | 367,458.10 USD | `+9.25%` | `10X Cross` |
| `600` | `0x936c...bb0f` | `SHORT` | 3,966,554.55 USD | `1,688.69` | `2434.60` | `2348.54` | `8479.24` | 144,732.56 USD | `+3.65%` | `20X Cross` |
| `621` | `0xeee0...0b53` | `LONG` | 3,845,767.75 USD | `1,637.12` | `2468.64` | `2348.54` | `86.47` | -195,708.31 USD | `-5.09%` | `7X Cross` |
| `623` | `0xfc27...9d9d` | `SHORT` | 3,833,685.84 USD | `1,631.63` | `2402.17` | `2348.54` | `10863.71` | 85,777.15 USD | `+2.24%` | `25X Cross` |
| `624` | `0x27b8...12fc` | `LONG` | 3,826,082.23 USD | `1,628.12` | `2468.73` | `2348.54` | `398.13` | -193,312.40 USD | `-5.05%` | `10X Cross` |
| `626` | `0x982b...4606` | `LONG` | 3,821,231.16 USD | `1,626.82` | `2575.24` | `2348.54` | `1548.38` | -368,221.92 USD | `-9.64%` | `5X Isolated` |
| `631` | `0x73d7...8be1` | `LONG` | 3,762,963.49 USD | `1,601.47` | `2410.40` | `2348.54` | `2033.48` | -97,215.44 USD | `-2.58%` | `25X Cross` |
| `659` | `0xe170...9300` | `SHORT` | 3,602,416.62 USD | `1,533.40` | `2076.39` | `2348.54` | `3208.59` | -418,467.12 USD | `-11.62%` | `25X Cross` |
| `673` | `0x2e2b...2fab` | `LONG` | 3,540,677.84 USD | `1,507.38` | `2245.53` | `2348.54` | `1053.16` | 155,804.74 USD | `+4.40%` | `25X Cross` |
| `677` | `0x251f...6e5d` | `LONG` | 3,523,950.00 USD | `1,500.00` | `2346.68` | `2348.54` | `1563.69` | 3,919.51 USD | `+0.11%` | `20X Cross` |
| `691` | `0xad54...6203` | `LONG` | 3,425,557.16 USD | `1,458.18` | `2627.45` | `2348.54` | `2146.44` | -405,749.52 USD | `-11.84%` | `10X Isolated` |
| `696` | `0xef70...a84c` | `SHORT` | 3,388,715.70 USD | `1,442.74` | `2424.73` | `2348.54` | `3473.10` | 109,555.13 USD | `+3.23%` | `25X Cross` |
| `703` | `0x4b5f...0dd8` | `LONG` | 3,363,523.33 USD | `1,431.96` | `2339.45` | `2348.54` | `2148.67` | 13,530.38 USD | `+0.40%` | `10X Cross` |
| `704` | `0xbadb...9ee6` | `LONG` | 3,355,033.47 USD | `1,428.16` | `1936.00` | `2348.54` | `1029.35` | 590,111.83 USD | `+17.59%` | `20X Cross` |
| `766` | `0x880a...311c` | `SHORT` | 3,101,864.17 USD | `1,320.22` | `2425.76` | `2348.54` | `8080.11` | 100,684.98 USD | `+3.25%` | `9X Cross` |
| `775` | `0x29de...3e93` | `LONG` | 3,076,928.00 USD | `1,310.00` | `2352.60` | `2348.54` | `1922.20` | -4,980.82 USD | `-0.16%` | `5X Isolated` |
| `780` | `0x023a...2355` | `LONG` | 3,058,224.27 USD | `1,302.04` | `2341.07` | `2348.54` | `0.000000` | 10,053.12 USD | `+0.33%` | `25X Cross` |
| `813` | `0xc435...c905` | `SHORT` | 2,931,676.80 USD | `1,248.00` | `2704.38` | `2348.54` | `4779.29` | 443,393.55 USD | `+15.12%` | `20X Cross` |
| `820` | `0x4202...aaf5` | `SHORT` | 2,895,198.92 USD | `1,232.10` | `2321.73` | `2348.54` | `2733.52` | -34,574.62 USD | `-1.19%` | `5X Isolated` |
| `826` | `0x7178...0854` | `LONG` | 2,862,930.98 USD | `1,218.63` | `2461.81` | `2348.54` | `1027.50` | -137,115.42 USD | `-4.79%` | `10X Cross` |
| `874` | `0x3bca...66f3` | `SHORT` | 2,669,497.84 USD | `1,136.30` | `2347.84` | `2348.54` | `9094.07` | -1,648.99 USD | `-0.06%` | `25X Cross` |
| `876` | `0x07fd...689d` | `LONG` | 2,668,000.98 USD | `1,135.90` | `2423.84` | `2348.54` | `0.000000` | -85,242.22 USD | `-3.19%` | `25X Cross` |
| `910` | `0x2f80...f203` | `SHORT` | 2,559,011.58 USD | `1,088.94` | `1984.00` | `2348.54` | `3076.05` | -398,544.40 USD | `-15.57%` | `20X Cross` |
| `921` | `0x6f11...0389` | `SHORT` | 2,534,463.10 USD | `1,079.00` | `2333.39` | `2348.54` | `3199.65` | -16,734.19 USD | `-0.66%` | `25X Cross` |
| `922` | `0x2b61...2f6c` | `SHORT` | 2,529,788.10 USD | `1,076.60` | `2681.75` | `2348.54` | `6431.20` | 357,384.64 USD | `+14.13%` | `10X Cross` |
| `962` | `0x1b2a...f7a6` | `LONG` | 2,408,691.97 USD | `1,025.37` | `2737.51` | `2348.54` | `931.52` | -398,267.97 USD | `-16.53%` | `10X Cross` |
| `963` | `0xb15b...dbae` | `SHORT` | 2,408,368.92 USD | `1,025.14` | `2338.37` | `2348.54` | `2381.04` | -11,195.20 USD | `-0.46%` | `25X Cross` |
| `967` | `0x6749...ce07` | `SHORT` | 2,385,353.77 USD | `1,015.35` | `2318.56` | `2348.54` | `5890.13` | -31,210.41 USD | `-1.31%` | `20X Cross` |
| `974` | `0x001a...fef6` | `SHORT` | 2,366,810.82 USD | `1,007.33` | `2022.19` | `2348.54` | `3026.49` | -329,802.86 USD | `-13.93%` | `10X Cross` |
| `976` | `0x02aa...1806` | `SHORT` | 2,365,476.71 USD | `1,007.10` | `2654.68` | `2348.54` | `3613.65` | 308,055.39 USD | `+13.02%` | `20X Cross` |
| `980` | `0xdb3a...cf3b` | `LONG` | 2,356,351.63 USD | `1,003.22` | `2705.01` | `2348.54` | `0.000000` | -357,355.27 USD | `-15.17%` | `4X Cross` |
| `983` | `0x5986...89d9` | `LONG` | 2,350,000.00 USD | `1,000.00` | `2346.34` | `2348.54` | `1195.05` | 3,650.46 USD | `+0.16%` | `25X Cross` |
| `986` | `0x5272...fcd9` | `SHORT` | 2,349,300.00 USD | `1,000.00` | `2241.82` | `2348.54` | `2880.72` | -107,475.51 USD | `-4.57%` | `5X Cross` |
| `987` | `0x2828...93a0` | `LONG` | 2,349,200.00 USD | `1,000.00` | `2393.30` | `2348.54` | `2261.32` | -44,109.16 USD | `-1.88%` | `25X Cross` |
| `988` | `0xdf60...d3c7` | `LONG` | 2,348,900.00 USD | `1,000.00` | `2736.24` | `2348.54` | `2246.05` | -387,342.88 USD | `-16.49%` | `10X Isolated` |
| `989` | `0xfe82...ce65` | `SHORT` | 2,348,900.00 USD | `1,000.00` | `2300.50` | `2348.54` | `2718.39` | -48,392.07 USD | `-2.06%` | `25X Cross` |
| `990` | `0x4044...794c` | `LONG` | 2,348,800.00 USD | `1,000.00` | `2332.68` | `2348.54` | `0.000000` | 16,110.16 USD | `+0.69%` | `25X Cross` |
| `1019` | `0xb002...ed8a` | `SHORT` | 2,261,675.89 USD | `962.78` | `2299.66` | `2348.54` | `4191.71` | -47,597.99 USD | `-2.10%` | `25X Cross` |
| `1028` | `0x2e30...4cb5` | `SHORT` | 2,253,206.02 USD | `958.97` | `2340.09` | `2348.54` | `7122.95` | -9,111.81 USD | `-0.40%` | `2X Cross` |
| `1043` | `0xc8fe...afa4` | `LONG` | 2,199,350.08 USD | `936.37` | `2331.34` | `2348.54` | `2145.78` | 16,345.85 USD | `+0.74%` | `10X Isolated` |
| `1058` | `0x9606...4e5d` | `SHORT` | 2,144,903.15 USD | `913.00` | `2478.70` | `2348.54` | `3876.18` | 118,150.46 USD | `+5.51%` | `20X Cross` |
| `1064` | `0xaeea...bfa7` | `LONG` | 2,134,917.68 USD | `908.75` | `2339.31` | `2348.54` | `2286.69` | 9,075.58 USD | `+0.43%` | `23X Isolated` |
| `1088` | `0x60f7...d1ee` | `LONG` | 2,091,144.00 USD | `890.00` | `2343.49` | `2348.54` | `2263.99` | 5,434.04 USD | `+0.26%` | `25X Cross` |
| `1178` | `0xcd27...52a8` | `LONG` | 1,966,518.58 USD | `837.21` | `2553.56` | `2348.54` | `1404.20` | -171,346.20 USD | `-8.71%` | `2X Cross` |
| `1207` | `0x2577...4897` | `LONG` | 1,910,076.81 USD | `813.21` | `2357.51` | `2348.54` | `0.000000` | -7,088.28 USD | `-0.37%` | `15X Cross` |
| `1232` | `0x3fc5...c0c1` | `SHORT` | 1,889,122.09 USD | `804.26` | `2702.11` | `2348.54` | `4756.47` | 284,079.44 USD | `+15.04%` | `25X Cross` |
| `1233` | `0xf83f...625f` | `SHORT` | 1,887,005.25 USD | `803.05` | `2601.00` | `2348.54` | `6018.12` | 201,731.21 USD | `+10.69%` | `20X Cross` |
| `1237` | `0x04a9...95aa` | `LONG` | 1,879,040.00 USD | `800.00` | `2595.13` | `2348.54` | `1857.48` | -197,066.74 USD | `-10.49%` | `5X Cross` |
| `1238` | `0x7737...bf66` | `SHORT` | 1,878,951.11 USD | `799.79` | `2494.83` | `2348.54` | `25624.01` | 116,394.92 USD | `+6.19%` | `15X Cross` |
| `1259` | `0xbef3...0d3e` | `LONG` | 1,834,630.66 USD | `780.99` | `2332.46` | `2348.54` | `2092.90` | 12,989.41 USD | `+0.71%` | `20X Cross` |
| `1266` | `0x6a41...a3b9` | `LONG` | 1,823,196.35 USD | `776.06` | `2332.17` | `2348.54` | `2095.12` | 13,291.49 USD | `+0.73%` | `20X Cross` |
| `1271` | `0x458d...ab3b` | `LONG` | 1,819,958.18 USD | `774.75` | `2740.41` | `2348.54` | `1887.95` | -303,171.01 USD | `-16.66%` | `3X Isolated` |
| `1308` | `0x5f10...d49d` | `SHORT` | 1,762,200.00 USD | `750.00` | `2350.92` | `2348.54` | `2842.49` | 996.61 USD | `+0.06%` | `25X Cross` |
| `1320` | `0x4b1c...bc38` | `SHORT` | 1,740,413.66 USD | `740.89` | `2529.31` | `2348.54` | `4410.48` | 133,520.62 USD | `+7.67%` | `10X Cross` |
| `1352` | `0x51a0...3543` | `SHORT` | 1,701,813.18 USD | `724.55` | `2627.71` | `2348.54` | `7727.17` | 202,083.58 USD | `+11.87%` | `20X Cross` |
| `1359` | `0xa189...94d7` | `SHORT` | 1,691,662.66 USD | `719.98` | `2691.84` | `2348.54` | `3051.90` | 246,410.00 USD | `+14.57%` | `25X Cross` |
| `1364` | `0x3ee5...4fab` | `SHORT` | 1,680,642.22 USD | `715.17` | `2759.35` | `2348.54` | `3555.35` | 292,757.75 USD | `+17.42%` | `20X Cross` |
| `1375` | `0x2f93...4404` | `LONG` | 1,662,416.53 USD | `707.47` | `1700.45` | `2348.54` | `1369.58` | 459,390.16 USD | `+27.63%` | `4X Isolated` |
| `1383` | `0x5605...fe0f` | `SHORT` | 1,650,037.46 USD | `702.14` | `2566.90` | `2348.54` | `3041.25` | 152,295.19 USD | `+9.23%` | `20X Cross` |
| `1388` | `0xaa53...9cb7` | `LONG` | 1,644,720.00 USD | `700.00` | `2394.46` | `2348.54` | `1956.21` | -31,402.07 USD | `-1.91%` | `20X Cross` |
| `1442` | `0xdbd1...29dd` | `SHORT` | 1,599,514.73 USD | `680.70` | `3030.57` | `2348.54` | `4067.51` | 463,406.39 USD | `+28.97%` | `6X Cross` |
| `1449` | `0x71e5...be04` | `LONG` | 1,592,042.61 USD | `677.67` | `2727.27` | `2348.54` | `1471.73` | -256,142.99 USD | `-16.09%` | `20X Cross` |
| `1456` | `0x0b23...f37b` | `LONG` | 1,586,115.00 USD | `675.00` | `2238.15` | `2348.54` | `575.83` | 75,358.36 USD | `+4.75%` | `5X Cross` |
| `1476` | `0x0cac...6170` | `SHORT` | 1,556,610.00 USD | `662.50` | `2146.55` | `2348.54` | `2835.36` | -134,515.01 USD | `-8.64%` | `20X Cross` |
| `1485` | `0x0082...1ae3` | `LONG` | 1,550,274.00 USD | `660.00` | `2448.58` | `2348.54` | `2244.93` | -65,794.64 USD | `-4.24%` | `25X Cross` |
| `1502` | `0x7743...e4fe` | `SHORT` | 1,528,026.40 USD | `650.56` | `2325.23` | `2348.54` | `6449.05` | -15,332.27 USD | `-1.00%` | `25X Cross` |
| `1518` | `0xffb2...5ed6` | `SHORT` | 1,505,417.52 USD | `640.77` | `2672.96` | `2348.54` | `2594.34` | 207,330.83 USD | `+13.77%` | `20X Cross` |
| `1526` | `0xb1ec...e86a` | `SHORT` | 1,494,781.94 USD | `636.38` | `2357.26` | `2348.54` | `18276.43` | 5,322.76 USD | `+0.36%` | `25X Cross` |
| `1533` | `0xa0fb...96be` | `SHORT` | 1,485,742.85 USD | `632.23` | `2335.52` | `2348.54` | `3790.20` | -9,148.41 USD | `-0.62%` | `3X Cross` |
| `1553` | `0xfce0...f4c0` | `SHORT` | 1,464,774.04 USD | `623.60` | `3129.61` | `2348.54` | `2788.39` | 486,852.54 USD | `+33.24%` | `20X Cross` |
| `1576` | `0x7663...cb5a` | `SHORT` | 1,441,629.77 USD | `613.54` | `2342.35` | `2348.54` | `3617.22` | -4,509.28 USD | `-0.31%` | `3X Cross` |
| `1607` | `0xad02...eb65` | `LONG` | 1,410,736.73 USD | `600.62` | `2460.69` | `2348.54` | `1079.65` | -67,203.83 USD | `-4.76%` | `5X Cross` |
| `1608` | `0x67c3...609d` | `SHORT` | 1,409,880.00 USD | `600.00` | `2386.55` | `2348.54` | `2560.74` | 22,051.89 USD | `+1.56%` | `25X Cross` |
| `1609` | `0x638f...f5f0` | `LONG` | 1,409,760.00 USD | `600.00` | `4011.50` | `2348.54` | `0.000000` | -997,143.53 USD | `-70.73%` | `25X Cross` |
| `1610` | `0x0deb...0bc5` | `LONG` | 1,409,580.00 USD | `600.00` | `2038.23` | `2348.54` | `1478.66` | 186,641.36 USD | `+13.24%` | `20X Cross` |
| `1611` | `0x0a84...6ddd` | `LONG` | 1,409,580.00 USD | `600.00` | `2222.36` | `2348.54` | `1774.77` | 76,161.66 USD | `+5.40%` | `25X Cross` |
| `1612` | `0x26e6...6b28` | `LONG` | 1,409,340.00 USD | `600.00` | `1769.78` | `2348.54` | `2005.45` | 347,468.47 USD | `+24.65%` | `20X Cross` |
| `1630` | `0x94b6...e5b3` | `SHORT` | 1,378,592.49 USD | `586.71` | `2377.90` | `2348.54` | `2511.43` | 16,545.75 USD | `+1.20%` | `25X Cross` |
| `1674` | `0xfb99...37f3` | `LONG` | 1,327,929.71 USD | `565.34` | `2362.35` | `2348.54` | `1203.67` | -7,606.65 USD | `-0.57%` | `3X Cross` |
| `1686` | `0x844b...7f42` | `SHORT` | 1,318,013.40 USD | `561.00` | `2026.17` | `2348.54` | `2960.03` | -181,329.99 USD | `-13.76%` | `25X Cross` |
| `1704` | `0xabe6...1d99` | `SHORT` | 1,306,220.20 USD | `556.00` | `2484.68` | `2348.54` | `2928.75` | 75,275.69 USD | `+5.76%` | `20X Cross` |
| `1751` | `0xad21...fb6a` | `LONG` | 1,249,680.11 USD | `531.87` | `2574.89` | `2348.54` | `1679.75` | -119,825.39 USD | `-9.59%` | `7X Cross` |
| `1787` | `0x8923...1bac` | `SHORT` | 1,215,019.20 USD | `517.18` | `2348.15` | `2348.54` | `3221.62` | -594.10 USD | `-0.05%` | `25X Cross` |
| `1806` | `0x0c7a...2f50` | `SHORT` | 1,196,522.76 USD | `509.25` | `2122.56` | `2348.54` | `4060.68` | -115,617.33 USD | `-9.66%` | `20X Cross` |
| `1831` | `0x89b2...9ca6` | `LONG` | 1,174,900.00 USD | `500.00` | `2484.03` | `2348.54` | `1954.18` | -67,119.35 USD | `-5.71%` | `25X Cross` |
| `1832` | `0x0e1c...ce6d` | `LONG` | 1,174,450.00 USD | `500.00` | `2329.15` | `2348.54` | `1996.65` | 9,873.27 USD | `+0.84%` | `15X Cross` |
| `1837` | `0x7298...7d6c` | `SHORT` | 1,170,202.52 USD | `498.15` | `3426.75` | `2348.54` | `5422.36` | 536,833.30 USD | `+45.88%` | `20X Cross` |
| `1857` | `0xc10f...23b3` | `LONG` | 1,151,206.00 USD | `490.00` | `2402.16` | `2348.54` | `2082.02` | -25,856.83 USD | `-2.25%` | `25X Cross` |
| `1858` | `0x404c...5f03` | `SHORT` | 1,150,897.50 USD | `489.79` | `2671.94` | `2348.54` | `4155.25` | 157,782.06 USD | `+13.71%` | `20X Cross` |
| `1864` | `0x321f...1c84` | `SHORT` | 1,146,494.58 USD | `488.02` | `2370.09` | `2348.54` | `3014.45` | 10,150.02 USD | `+0.89%` | `10X Cross` |
| `1927` | `0x82c6...fe42` | `LONG` | 1,086,366.25 USD | `462.50` | `2501.38` | `2348.54` | `2054.43` | -70,524.32 USD | `-6.49%` | `5X Isolated` |
| `1942` | `0x617e...0f97` | `SHORT` | 1,075,774.70 USD | `457.85` | `2205.60` | `2348.54` | `3603.81` | -65,930.86 USD | `-6.13%` | `10X Cross` |
| `1970` | `0xae55...2236` | `LONG` | 1,057,320.00 USD | `450.00` | `2510.21` | `2348.54` | `0.000000` | -72,277.50 USD | `-6.84%` | `25X Cross` |
| `1982` | `0xac26...a9c7` | `SHORT` | 1,048,572.20 USD | `446.28` | `2192.58` | `2348.54` | `8654.84` | -70,072.50 USD | `-6.68%` | `20X Cross` |
| `1988` | `0x53f8...ceff` | `LONG` | 1,046,663.97 USD | `445.60` | `2399.81` | `2348.54` | `0.000000` | -22,686.63 USD | `-2.17%` | `20X Cross` |
| `1997` | `0xd8a1...6687` | `LONG` | 1,037,514.24 USD | `441.53` | `2804.24` | `2348.54` | `2150.99` | -200,654.19 USD | `-19.34%` | `20X Cross` |
| `2014` | `0x248e...6be2` | `SHORT` | 1,025,530.83 USD | `436.40` | `2314.49` | `2348.54` | `4359.21` | -15,496.12 USD | `-1.51%` | `20X Cross` |
| `2018` | `0x80f2...0c3a` | `LONG` | 1,020,877.04 USD | `434.55` | `2564.17` | `2348.54` | `904.88` | -93,371.84 USD | `-9.15%` | `5X Cross` |
| `2043` | `0x15c8...045f` | `SHORT` | 1,007,609.84 USD | `428.90` | `1903.23` | `2348.54` | `3081.76` | -191,316.79 USD | `-18.99%` | `25X Cross` |
| `2052` | `0x4e6b...b7d4` | `LONG` | 1,004,753.69 USD | `427.77` | `2744.83` | `2348.54` | `67.92` | -169,411.34 USD | `-16.86%` | `25X Cross` |
| `2062` | `0x92cb...859c` | `LONG` | 1,001,377.90 USD | `426.19` | `2338.54` | `2348.54` | `0.000000` | 4,712.28 USD | `+0.47%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `ANNOUNCEMENT` | `INFO` | `2357.90` | 70,001.57 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 70.00K USD at 2357.9000 USD [API] | `2026-10-27 21:33:15` |
| `ANNOUNCEMENT` | `INFO` | `2346.30` | 70,001.39 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 70.00K USD at 2346.3000 USD [API] | `2026-10-27 15:21:36` |
| `ANNOUNCEMENT` | `INFO` | `2348.60` | 40,055.14 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 40.06K USD at 2348.6000 USD [API] | `2026-10-27 22:31:05` |
| `ANNOUNCEMENT` | `INFO` | `2348.60` | 56,673.13 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 56.67K USD at 2348.6000 USD [API] | `2026-10-27 22:31:05` |
| `ANNOUNCEMENT` | `INFO` | `2357.60` | 56,270.96 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 56.27K USD at 2357.6000 USD [API] | `2026-10-27 21:33:15` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`2401.93` (Vol: 17,300,000.00 USD, Dist: `+2.21%`) | Long MP=`2284.33` (Vol: 27,300,000.00 USD, Dist: `--2.79%`)
  * 48H Horizon: Short MP=`2401.93` (Vol: 25,300,000.00 USD, Dist: `+2.21%`) | Long MP=`2284.33` (Vol: 30,000,000.00 USD, Dist: `--2.79%`)
  * 3D Horizon: Short MP=`2401.93` (Vol: 26,700,000.00 USD, Dist: `+2.21%`) | Long MP=`2286.29` (Vol: 37,900,000.00 USD, Dist: `--2.71%`)
  * 7D Horizon: Short MP=`2402.93` (Vol: 47,100,000.00 USD, Dist: `+2.25%`) | Long MP=`2284.60` (Vol: 72,300,000.00 USD, Dist: `--2.78%`)
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
| `7D` | `Long Liquidation` | `2068.70` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 1,890,000.00 USD | 1,910,000.00 USD | 939,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2071.50` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 2,760,000.00 USD | 1,510,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2074.30` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 3,850,000.00 USD | 2,610,000.00 USD | 2,930,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 13,750,000.00 USD | 362,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2077.10` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 4,430,000.00 USD | 4,120,000.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2079.90` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 3,400,000.00 USD | 3,020,000.00 USD | 2,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2082.70` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 2,420,000.00 USD | 1,860,000.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 1,810,000.00 USD | 348,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2085.50` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 3,840,000.00 USD | 1,860,000.00 USD | 3,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2088.30` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 2,280,000.00 USD | 1,820,000.00 USD | 907,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2091.10` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 4,280,000.00 USD | 952,210.00 USD | 6,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2093.90` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 5,200,000.00 USD | 1,640,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 4,620,000.00 USD | 346,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2096.70` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 1,940,000.00 USD | 3,330,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2099.50` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 1,880,000.00 USD | 1,520,000.00 USD | 2,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2102.30` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 125,250.00 USD | 688,260.00 USD | 2,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 23,040,000.00 USD | 342,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2105.10` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2107.90` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 2,320,000.00 USD | 356,360.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2110.70` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 2,830,000.00 USD | 2,300,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2111.30` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 1,250,000.00 USD | 343,530.00 USD | 525,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2113.50` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 1,730,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2113.90` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 1,090,000.00 USD | 1,080,000.00 USD | 363,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 16,720,000.00 USD | 319,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2116.30` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 1,480,000.00 USD | 2,030,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2116.50` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 1,240,000.00 USD | 335,670.00 USD | 859,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2119.10` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 507,030.00 USD | 201,150.00 USD | 917,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2119.10` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 3,390,000.00 USD | 935,590.00 USD | 2,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2121.70` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 982,960.00 USD | 759,970.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2121.90` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 2,300,000.00 USD | 973,690.00 USD | 1,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2124.30` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 957,510.00 USD | 1,040,000.00 USD | 525,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2124.70` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 2,110,000.00 USD | 983,790.00 USD | 989,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 1,140,000.00 USD | 302,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2126.90` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 308,590.00 USD | 840,990.00 USD | 629,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2127.50` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 1,080,000.00 USD | 2,620,000.00 USD | 3,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2129.50` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 107,010.00 USD | 453,880.00 USD | 318,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2130.30` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 2,040,000.00 USD | 2,130,000.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2132.10` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 0.00 USD | 956,330.00 USD | 336,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2133.10` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 1,930,000.00 USD | 715,940.00 USD | 330,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2134.70` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 187,520.00 USD | 185,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 15,440,000.00 USD | 301,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2135.90` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 1,370,000.00 USD | 596,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2137.30` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 236,290.00 USD | 544,840.00 USD | 208,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2138.70` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 909,440.00 USD | 1,250,000.00 USD | 78,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2139.90` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 319,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2141.50` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 1,750,000.00 USD | 199,980.00 USD | 766,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2142.50` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 295,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2144.30` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 465,960.00 USD | 1,540,000.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 16,180,000.00 USD | 285,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2145.10` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 16,700.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2147.10` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 311,920.00 USD | 32,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2147.70` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 251,250.00 USD | 11,090.00 USD | 207,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2149.90` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 459,630.00 USD | 482,820.00 USD | 537,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2152.70` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 58,340.00 USD | 681,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 2,580,000.00 USD | 269,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2155.50` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 191,860.00 USD | 454,940.00 USD | 866,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2158.30` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 738,850.00 USD | 717,210.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2161.10` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 1,490,000.00 USD | 1,350,000.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2163.90` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 36,870.00 USD | 329,690.00 USD | 409,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 1,660,000.00 USD | 266,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2166.70` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 25,540.00 USD | 0.00 USD | 68,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2169.50` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 1,700,000.00 USD | 726,240.00 USD | 810,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2172.30` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 479,540.00 USD | 1,150,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 109,510,000.00 USD | 265,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2185.00` | 113,580,000.00 USD | 155,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2194.70` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 141,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 1,210,000.00 USD | 42,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2197.50` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 2,440,000.00 USD | 3,270,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2199.70` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 201,540.00 USD | 154,560.00 USD | 80,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2200.30` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 3,000,000.00 USD | 3,140,000.00 USD | 3,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2202.30` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 82,940.00 USD | 62,930.00 USD | 220,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2203.10` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 3,240,000.00 USD | 624,500.00 USD | 2,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2204.90` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 1,050,000.00 USD | 207,110.00 USD | 716,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 1,160,000.00 USD | 41,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2205.90` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 6,050,000.00 USD | 4,010,000.00 USD | 3,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2207.50` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 3,100,000.00 USD | 2,380,000.00 USD | 3,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2208.70` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 10,060,000.00 USD | 6,100,000.00 USD | 4,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2210.10` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 1,610,000.00 USD | 1,180,000.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2211.50` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 7,320,000.00 USD | 7,940,000.00 USD | 7,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2212.70` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 2,200,000.00 USD | 1,180,000.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2214.30` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 13,980,000.00 USD | 12,380,000.00 USD | 9,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 2,240,000.00 USD | 39,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2215.30` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 5,950,000.00 USD | 5,220,000.00 USD | 5,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2217.10` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 16,020,000.00 USD | 10,300,000.00 USD | 8,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2217.90` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 4,610,000.00 USD | 4,240,000.00 USD | 1,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2219.90` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 12,620,000.00 USD | 10,310,000.00 USD | 3,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2220.50` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 3,450,000.00 USD | 4,220,000.00 USD | 680,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2222.70` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 5,480,000.00 USD | 5,400,000.00 USD | 8,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2223.10` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 5,770,000.00 USD | 3,810,000.00 USD | 2,870,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2225.00` | 1,560,000.00 USD | 37,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2225.50` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 12,980,000.00 USD | 13,620,000.00 USD | 9,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2225.70` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 3,700,000.00 USD | 5,870,000.00 USD | 2,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2228.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 4,150,000.00 USD | 1,310,000.00 USD | 766,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2228.30` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 7,790,000.00 USD | 5,070,000.00 USD | 7,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2230.90` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 3,630,000.00 USD | 2,460,000.00 USD | 3,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2231.10` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 9,590,000.00 USD | 3,450,000.00 USD | 17,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2233.50` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 6,590,000.00 USD | 3,820,000.00 USD | 2,280,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2233.90` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 18,230,000.00 USD | 10,390,000.00 USD | 6,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2235.00` | 789,970.00 USD | 36,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2236.10` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 2,630,000.00 USD | 2,440,000.00 USD | 3,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2236.70` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 7,440,000.00 USD | 11,700,000.00 USD | 5,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2238.70` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 1,620,000.00 USD | 2,150,000.00 USD | 844,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2239.50` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 6,630,000.00 USD | 6,820,000.00 USD | 6,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2241.30` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 321,680.00 USD | 216,600.00 USD | 39,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2242.30` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 3,580,000.00 USD | 2,780,000.00 USD | 7,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2243.90` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 2,380,000.00 USD | 423,680.00 USD | 238,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2245.00` | 4,680,000.00 USD | 35,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2245.10` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 16,710,000.00 USD | 13,060,000.00 USD | 11,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2246.50` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 883,930.00 USD | 788,500.00 USD | 1,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2247.90` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 13,600,000.00 USD | 6,160,000.00 USD | 9,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2249.10` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 4,190,000.00 USD | 1,420,000.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2250.70` | 2,080,000,000.00 USD | 2,080,000,000.00 USD | 10,570,000.00 USD | 10,360,000.00 USD | 8,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2251.70` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 4,500,000.00 USD | 6,550,000.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2253.50` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 24,760,000.00 USD | 21,020,000.00 USD | 19,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2254.30` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 7,670,000.00 USD | 3,590,000.00 USD | 5,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2255.00` | 13,270,000.00 USD | 30,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2256.30` | 1,990,000,000.00 USD | 1,990,000,000.00 USD | 31,260,000.00 USD | 19,100,000.00 USD | 18,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2256.90` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 5,660,000.00 USD | 5,380,000.00 USD | 4,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2259.10` | 1,920,000,000.00 USD | 1,920,000,000.00 USD | 22,390,000.00 USD | 19,400,000.00 USD | 22,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2259.50` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 13,310,000.00 USD | 6,270,000.00 USD | 8,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2261.90` | 1,850,000,000.00 USD | 1,850,000,000.00 USD | 48,180,000.00 USD | 29,390,000.00 USD | 21,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2262.10` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 15,090,000.00 USD | 12,940,000.00 USD | 13,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2264.70` | 992,660,000.00 USD | 992,660,000.00 USD | 15,200,000.00 USD | 12,030,000.00 USD | 6,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2264.70` | 1,760,000,000.00 USD | 1,760,000,000.00 USD | 30,320,000.00 USD | 28,050,000.00 USD | 19,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2265.00` | 3,530,000.00 USD | 17,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2267.30` | 958,830,000.00 USD | 958,830,000.00 USD | 5,460,000.00 USD | 10,030,000.00 USD | 3,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2267.50` | 1,680,000,000.00 USD | 1,680,000,000.00 USD | 40,120,000.00 USD | 40,100,000.00 USD | 31,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2269.90` | 940,220,000.00 USD | 940,220,000.00 USD | 14,410,000.00 USD | 11,130,000.00 USD | 8,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2270.30` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 39,480,000.00 USD | 27,490,000.00 USD | 39,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2272.50` | 906,440,000.00 USD | 906,440,000.00 USD | 14,080,000.00 USD | 10,950,000.00 USD | 10,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2273.10` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 33,160,000.00 USD | 25,760,000.00 USD | 19,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2275.00` | 4,430,000.00 USD | 13,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2275.10` | 871,350,000.00 USD | 871,350,000.00 USD | 9,170,000.00 USD | 15,450,000.00 USD | 4,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2275.90` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 48,240,000.00 USD | 42,710,000.00 USD | 44,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2277.70` | 842,510,000.00 USD | 842,510,000.00 USD | 16,430,000.00 USD | 8,710,000.00 USD | 18,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2278.70` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 74,310,000.00 USD | 34,750,000.00 USD | 42,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2280.30` | 799,300,000.00 USD | 799,300,000.00 USD | 24,350,000.00 USD | 14,020,000.00 USD | 8,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2281.50` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 56,100,000.00 USD | 59,940,000.00 USD | 49,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2282.90` | 752,900,000.00 USD | 752,900,000.00 USD | 22,370,000.00 USD | 16,300,000.00 USD | 19,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2284.30` | 929,630,000.00 USD | 929,630,000.00 USD | 89,220,000.00 USD | 69,840,000.00 USD | 44,200,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2285.00` | 5,990,000.00 USD | 9,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2285.50` | 695,170,000.00 USD | 695,170,000.00 USD | 28,040,000.00 USD | 29,580,000.00 USD | 19,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2287.10` | 726,370,000.00 USD | 726,370,000.00 USD | 58,910,000.00 USD | 53,380,000.00 USD | 45,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2288.10` | 618,150,000.00 USD | 618,150,000.00 USD | 19,180,000.00 USD | 14,480,000.00 USD | 4,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2289.90` | 568,900,000.00 USD | 568,900,000.00 USD | 48,430,000.00 USD | 34,490,000.00 USD | 22,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2290.70` | 579,780,000.00 USD | 579,780,000.00 USD | 12,240,000.00 USD | 7,760,000.00 USD | 2,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2292.70` | 463,800,000.00 USD | 463,800,000.00 USD | 38,110,000.00 USD | 20,900,000.00 USD | 44,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2293.30` | 557,320,000.00 USD | 557,320,000.00 USD | 18,860,000.00 USD | 18,460,000.00 USD | 15,490,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2295.00` | 1,460,000.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2295.50` | 360,720,000.00 USD | 360,720,000.00 USD | 17,510,000.00 USD | 8,110,000.00 USD | 7,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2295.90` | 504,520,000.00 USD | 504,520,000.00 USD | 23,870,000.00 USD | 15,930,000.00 USD | 7,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2298.30` | 327,880,000.00 USD | 327,880,000.00 USD | 2,090,000.00 USD | 5,410,000.00 USD | 301,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2298.50` | 457,510,000.00 USD | 457,510,000.00 USD | 8,010,000.00 USD | 7,220,000.00 USD | 3,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2301.10` | 439,040,000.00 USD | 439,040,000.00 USD | 17,170,000.00 USD | 11,820,000.00 USD | 13,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2301.10` | 320,070,000.00 USD | 320,070,000.00 USD | 11,790,000.00 USD | 2,200,000.00 USD | 7,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2303.70` | 396,730,000.00 USD | 396,730,000.00 USD | 29,770,000.00 USD | 15,890,000.00 USD | 10,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2303.90` | 298,500,000.00 USD | 298,500,000.00 USD | 32,960,000.00 USD | 17,020,000.00 USD | 13,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2305.00` | 280,710.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2306.30` | 340,400,000.00 USD | 340,400,000.00 USD | 4,970,000.00 USD | 5,530,000.00 USD | 15,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2306.70` | 235,250,000.00 USD | 235,250,000.00 USD | 0.00 USD | 3,740,000.00 USD | 10,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2308.90` | 314,550,000.00 USD | 314,550,000.00 USD | 642,440.00 USD | 1,990,000.00 USD | 2,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2309.50` | 220,620,000.00 USD | 220,620,000.00 USD | 282,530.00 USD | 300,580.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2311.50` | 309,380,000.00 USD | 309,380,000.00 USD | 7,190,000.00 USD | 3,230,000.00 USD | 5,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2312.30` | 218,530,000.00 USD | 218,530,000.00 USD | 1,740,000.00 USD | 128,300.00 USD | 2,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2314.10` | 293,190,000.00 USD | 293,190,000.00 USD | 10,080,000.00 USD | 3,280,000.00 USD | 688,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2315.00` | 267,770.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2315.10` | 214,150,000.00 USD | 214,150,000.00 USD | 4,300,000.00 USD | 4,100,000.00 USD | 117,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2316.70` | 279,140,000.00 USD | 279,140,000.00 USD | 3,450,000.00 USD | 5,270,000.00 USD | 3,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2317.90` | 205,640,000.00 USD | 205,640,000.00 USD | 817,040.00 USD | 3,010,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2319.30` | 266,720,000.00 USD | 266,720,000.00 USD | 8,240,000.00 USD | 2,120,000.00 USD | 795,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2320.70` | 201,810,000.00 USD | 201,810,000.00 USD | 0.00 USD | 2,790,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2321.90` | 255,570,000.00 USD | 255,570,000.00 USD | 616,250.00 USD | 2,660,000.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2323.50` | 199,020,000.00 USD | 199,020,000.00 USD | 4,070,000.00 USD | 1,900,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2324.50` | 250,630,000.00 USD | 250,630,000.00 USD | 8,660,000.00 USD | 2,780,000.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2325.00` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2326.30` | 193,050,000.00 USD | 193,050,000.00 USD | 0.00 USD | 0.00 USD | 126,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2327.10` | 236,970,000.00 USD | 236,970,000.00 USD | 0.00 USD | 3,260,000.00 USD | 4,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2329.10` | 192,920,000.00 USD | 192,920,000.00 USD | 3,860,000.00 USD | 0.00 USD | 4,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2329.70` | 229,260,000.00 USD | 229,260,000.00 USD | 5,520,000.00 USD | 1,150,000.00 USD | 3,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2331.90` | 184,180,000.00 USD | 184,180,000.00 USD | 29,230,000.00 USD | 1,090,000.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2332.30` | 219,550,000.00 USD | 219,550,000.00 USD | 17,970,000.00 USD | 2,290,000.00 USD | 107,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2334.70` | 151,040,000.00 USD | 151,040,000.00 USD | 7,260,000.00 USD | 18,420,000.00 USD | 8,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2334.90` | 199,180,000.00 USD | 199,180,000.00 USD | 28,290,000.00 USD | 25,090,000.00 USD | 16,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2337.50` | 129,720,000.00 USD | 129,720,000.00 USD | 6,570,000.00 USD | 22,000,000.00 USD | 10,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2337.50` | 116,430,000.00 USD | 116,430,000.00 USD | 20,380,000.00 USD | 18,560,000.00 USD | 13,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2340.10` | 90,980,000.00 USD | 90,980,000.00 USD | 4,960,000.00 USD | 21,890,000.00 USD | 7,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2340.30` | 63,920,000.00 USD | 63,920,000.00 USD | 1,630,000.00 USD | 10,010,000.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2342.70` | 57,060,000.00 USD | 57,060,000.00 USD | 5,030,000.00 USD | 8,490,000.00 USD | 2,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2343.10` | 48,890,000.00 USD | 48,890,000.00 USD | 0.00 USD | 5,540,000.00 USD | 3,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2345.30` | 41,380,000.00 USD | 41,380,000.00 USD | 963,370.00 USD | 1,770,000.00 USD | 9,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2345.90` | 39,510,000.00 USD | 39,510,000.00 USD | 0.00 USD | 8,310,000.00 USD | 12,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2347.90` | 28,650,000.00 USD | 28,650,000.00 USD | 215,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2348.70` | 18,370,000.00 USD | 18,370,000.00 USD | 285,680.00 USD | 7,340,000.00 USD | 10,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2350.50` | 28,430,000.00 USD | 28,430,000.00 USD | 25,900,000.00 USD | 2,510,000.00 USD | 23,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2351.50` | 23,900,000.00 USD | 23,900,000.00 USD | 782,590.00 USD | 17,440,000.00 USD | 5,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2353.10` | 1,790,000.00 USD | 1,790,000.00 USD | 576,450.00 USD | 1,110,000.00 USD | 107,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2354.30` | 65,110,000.00 USD | 65,110,000.00 USD | 5,960,000.00 USD | 35,020,000.00 USD | 237,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 35,020.00 USD | 35,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2355.70` | 19,330,000.00 USD | 19,330,000.00 USD | 318,080.00 USD | 15,970,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2357.10` | 78,410,000.00 USD | 78,410,000.00 USD | 7,900,000.00 USD | 5,400,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2358.30` | 19,520,000.00 USD | 19,520,000.00 USD | 0.00 USD | 0.00 USD | 198,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2359.90` | 80,630,000.00 USD | 80,630,000.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2360.90` | 21,470,000.00 USD | 21,470,000.00 USD | 1,850,000.00 USD | 0.00 USD | 93,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2362.70` | 82,790,000.00 USD | 82,790,000.00 USD | 467,570.00 USD | 0.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2363.50` | 24,580,000.00 USD | 24,580,000.00 USD | 929,610.00 USD | 1,840,000.00 USD | 341,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 153.25 USD | 35,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2365.50` | 90,790,000.00 USD | 90,790,000.00 USD | 6,340,000.00 USD | 0.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2366.10` | 24,820,000.00 USD | 24,820,000.00 USD | 61,300.00 USD | 0.00 USD | 170,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2368.30` | 100,760,000.00 USD | 100,760,000.00 USD | 9,590,000.00 USD | 0.00 USD | 370,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2368.70` | 37,300,000.00 USD | 37,300,000.00 USD | 8,060,000.00 USD | 3,260,000.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2371.10` | 162,550,000.00 USD | 162,550,000.00 USD | 16,760,000.00 USD | 0.00 USD | 45,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2371.30` | 75,680,000.00 USD | 75,680,000.00 USD | 17,050,000.00 USD | 12,840,000.00 USD | 8,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2373.90` | 93,230,000.00 USD | 93,230,000.00 USD | 13,630,000.00 USD | 955,690.00 USD | 2,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2373.90` | 185,110,000.00 USD | 185,110,000.00 USD | 15,830,000.00 USD | 0.00 USD | 6,730,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 14,790.00 USD | 49,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2376.50` | 119,130,000.00 USD | 119,130,000.00 USD | 12,130,000.00 USD | 3,180,000.00 USD | 10,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2376.70` | 225,250,000.00 USD | 225,250,000.00 USD | 12,140,000.00 USD | 5,950,000.00 USD | 22,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2379.10` | 150,490,000.00 USD | 150,490,000.00 USD | 5,850,000.00 USD | 13,800,000.00 USD | 11,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2379.50` | 252,570,000.00 USD | 252,570,000.00 USD | 7,180,000.00 USD | 2,580,000.00 USD | 17,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2381.70` | 192,290,000.00 USD | 192,290,000.00 USD | 15,410,000.00 USD | 10,970,000.00 USD | 15,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2382.30` | 293,920,000.00 USD | 293,920,000.00 USD | 7,910,000.00 USD | 12,120,000.00 USD | 21,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2384.30` | 241,320,000.00 USD | 241,320,000.00 USD | 20,840,000.00 USD | 17,560,000.00 USD | 10,610,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 3,380,000.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2385.10` | 380,660,000.00 USD | 380,660,000.00 USD | 14,990,000.00 USD | 28,990,000.00 USD | 42,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2386.90` | 271,590,000.00 USD | 271,590,000.00 USD | 12,200,000.00 USD | 11,050,000.00 USD | 7,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2387.90` | 460,800,000.00 USD | 460,800,000.00 USD | 4,870,000.00 USD | 32,720,000.00 USD | 42,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2389.50` | 295,530,000.00 USD | 295,530,000.00 USD | 9,590,000.00 USD | 8,400,000.00 USD | 5,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2390.70` | 560,480,000.00 USD | 560,480,000.00 USD | 5,470,000.00 USD | 45,700,000.00 USD | 48,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2392.10` | 323,270,000.00 USD | 323,270,000.00 USD | 5,340,000.00 USD | 13,820,000.00 USD | 8,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2393.50` | 658,950,000.00 USD | 658,950,000.00 USD | 43,890,000.00 USD | 22,890,000.00 USD | 31,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2394.70` | 354,220,000.00 USD | 354,220,000.00 USD | 14,780,000.00 USD | 13,450,000.00 USD | 2,740,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 4,430,000.00 USD | 7,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2396.30` | 742,990,000.00 USD | 742,990,000.00 USD | 29,820,000.00 USD | 32,850,000.00 USD | 21,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2397.30` | 373,410,000.00 USD | 373,410,000.00 USD | 5,540,000.00 USD | 8,740,000.00 USD | 4,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2399.10` | 832,520,000.00 USD | 832,520,000.00 USD | 39,350,000.00 USD | 31,200,000.00 USD | 18,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2399.90` | 414,720,000.00 USD | 414,720,000.00 USD | 17,930,000.00 USD | 9,240,000.00 USD | 14,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2401.90` | 943,310,000.00 USD | 943,310,000.00 USD | 53,530,000.00 USD | 24,490,000.00 USD | 32,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2402.50` | 441,220,000.00 USD | 441,220,000.00 USD | 8,820,000.00 USD | 9,710,000.00 USD | 7,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2404.70` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 36,370,000.00 USD | 25,840,000.00 USD | 15,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 11,200,000.00 USD | 19,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2405.10` | 474,650,000.00 USD | 474,650,000.00 USD | 13,880,000.00 USD | 10,580,000.00 USD | 8,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2407.50` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 22,760,000.00 USD | 29,510,000.00 USD | 18,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2407.70` | 509,790,000.00 USD | 509,790,000.00 USD | 14,050,000.00 USD | 11,560,000.00 USD | 9,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2410.30` | 534,440,000.00 USD | 534,440,000.00 USD | 9,390,000.00 USD | 8,300,000.00 USD | 6,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2410.30` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 26,620,000.00 USD | 26,620,000.00 USD | 23,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2412.90` | 553,970,000.00 USD | 553,970,000.00 USD | 9,190,000.00 USD | 6,900,000.00 USD | 3,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2413.10` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 13,360,000.00 USD | 15,180,000.00 USD | 13,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 666,630.00 USD | 19,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2415.50` | 566,990,000.00 USD | 566,990,000.00 USD | 3,550,000.00 USD | 5,790,000.00 USD | 3,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2415.90` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 28,030,000.00 USD | 17,450,000.00 USD | 32,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2418.10` | 579,910,000.00 USD | 579,910,000.00 USD | 4,840,000.00 USD | 5,370,000.00 USD | 2,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2418.70` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 28,840,000.00 USD | 18,500,000.00 USD | 12,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2420.70` | 594,840,000.00 USD | 594,840,000.00 USD | 6,810,000.00 USD | 5,220,000.00 USD | 2,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2421.50` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 23,440,000.00 USD | 25,120,000.00 USD | 18,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2423.30` | 608,680,000.00 USD | 608,680,000.00 USD | 4,570,000.00 USD | 3,780,000.00 USD | 5,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.30` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 25,250,000.00 USD | 29,620,000.00 USD | 33,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 3,250,000.00 USD | 22,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2425.90` | 611,780,000.00 USD | 611,780,000.00 USD | 516,070.00 USD | 2,560,000.00 USD | 27,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2427.10` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 24,580,000.00 USD | 22,020,000.00 USD | 23,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2428.50` | 613,900,000.00 USD | 613,900,000.00 USD | 2,090,000.00 USD | 12,140.00 USD | 19,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2429.90` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 6,160,000.00 USD | 14,060,000.00 USD | 6,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2431.10` | 616,750,000.00 USD | 616,750,000.00 USD | 2,090,000.00 USD | 507,190.00 USD | 254,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2432.70` | 1,640,000,000.00 USD | 1,640,000,000.00 USD | 17,740,000.00 USD | 13,220,000.00 USD | 6,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2433.70` | 619,600,000.00 USD | 619,600,000.00 USD | 314,980.00 USD | 534,830.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 8,030,000.00 USD | 31,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2435.50` | 1,690,000,000.00 USD | 1,690,000,000.00 USD | 22,360,000.00 USD | 14,140,000.00 USD | 15,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2436.30` | 624,470,000.00 USD | 624,470,000.00 USD | 3,340,000.00 USD | 1,270,000.00 USD | 261,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2438.30` | 1,750,000,000.00 USD | 1,750,000,000.00 USD | 17,900,000.00 USD | 23,900,000.00 USD | 15,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2438.90` | 629,050,000.00 USD | 629,050,000.00 USD | 1,260,000.00 USD | 1,610,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2441.10` | 1,790,000,000.00 USD | 1,790,000,000.00 USD | 17,250,000.00 USD | 6,990,000.00 USD | 14,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2441.50` | 637,910,000.00 USD | 637,910,000.00 USD | 4,710,000.00 USD | 3,380,000.00 USD | 767,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2443.90` | 1,820,000,000.00 USD | 1,820,000,000.00 USD | 6,650,000.00 USD | 13,590,000.00 USD | 7,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2444.10` | 641,140,000.00 USD | 641,140,000.00 USD | 791,730.00 USD | 798,660.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 748,180.00 USD | 31,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2446.70` | 648,900,000.00 USD | 648,900,000.00 USD | 4,320,000.00 USD | 1,500,000.00 USD | 1,940,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2446.70` | 1,850,000,000.00 USD | 1,850,000,000.00 USD | 11,870,000.00 USD | 7,020,000.00 USD | 18,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2449.30` | 655,440,000.00 USD | 655,440,000.00 USD | 2,040,000.00 USD | 1,740,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2449.50` | 1,890,000,000.00 USD | 1,890,000,000.00 USD | 15,780,000.00 USD | 9,650,000.00 USD | 14,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2451.90` | 667,710,000.00 USD | 667,710,000.00 USD | 3,860,000.00 USD | 3,720,000.00 USD | 4,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2452.30` | 1,920,000,000.00 USD | 1,920,000,000.00 USD | 10,050,000.00 USD | 9,630,000.00 USD | 7,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2454.50` | 677,880,000.00 USD | 677,880,000.00 USD | 4,200,000.00 USD | 3,460,000.00 USD | 2,510,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 108,990.00 USD | 31,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2455.10` | 1,940,000,000.00 USD | 1,940,000,000.00 USD | 5,550,000.00 USD | 5,830,000.00 USD | 3,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2457.10` | 685,030,000.00 USD | 685,030,000.00 USD | 2,160,000.00 USD | 2,720,000.00 USD | 2,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2457.90` | 1,970,000,000.00 USD | 1,970,000,000.00 USD | 12,470,000.00 USD | 11,200,000.00 USD | 13,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2459.70` | 690,710,000.00 USD | 690,710,000.00 USD | 2,370,000.00 USD | 1,970,000.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2460.70` | 2,000,000,000.00 USD | 2,000,000,000.00 USD | 7,010,000.00 USD | 10,640,000.00 USD | 5,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2462.30` | 694,030,000.00 USD | 694,030,000.00 USD | 174,920.00 USD | 2,050,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2463.50` | 2,020,000,000.00 USD | 2,020,000,000.00 USD | 9,490,000.00 USD | 9,600,000.00 USD | 8,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2464.90` | 696,100,000.00 USD | 696,100,000.00 USD | 820,990.00 USD | 1,240,000.00 USD | 5,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 296,600.00 USD | 32,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2466.30` | 2,030,000,000.00 USD | 2,030,000,000.00 USD | 5,400,000.00 USD | 2,080,000.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2467.50` | 696,480,000.00 USD | 696,480,000.00 USD | 0.00 USD | 370,410.00 USD | 7,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2469.10` | 2,040,000,000.00 USD | 2,040,000,000.00 USD | 2,770,000.00 USD | 3,570,000.00 USD | 408,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2470.10` | 700,530,000.00 USD | 700,530,000.00 USD | 1,390,000.00 USD | 1,510,000.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2471.90` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 3,090,000.00 USD | 2,760,000.00 USD | 814,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2472.70` | 700,770,000.00 USD | 700,770,000.00 USD | 0.00 USD | 232,740.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2474.70` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 5,400,000.00 USD | 866,790.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 444,190.00 USD | 32,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2475.30` | 701,510,000.00 USD | 701,510,000.00 USD | 738,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2477.50` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 790,860.00 USD | 3,880,000.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2477.90` | 701,560,000.00 USD | 701,560,000.00 USD | 0.00 USD | 41,760.00 USD | 7,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2480.30` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 2,300,000.00 USD | 1,740,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2480.50` | 702,110,000.00 USD | 702,110,000.00 USD | 0.00 USD | 27,720.00 USD | 518,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2483.10` | 702,730,000.00 USD | 702,730,000.00 USD | 628,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2483.10` | 2,070,000,000.00 USD | 2,070,000,000.00 USD | 2,010,000.00 USD | 1,330,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 528,130.00 USD | 33,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2485.90` | 2,070,000,000.00 USD | 2,070,000,000.00 USD | 586,480.00 USD | 1,560,000.00 USD | 77,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2488.70` | 2,080,000,000.00 USD | 2,080,000,000.00 USD | 1,710,000.00 USD | 842,740.00 USD | 2,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2491.50` | 2,080,000,000.00 USD | 2,080,000,000.00 USD | 1,660,000.00 USD | 2,550,000.00 USD | 672,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2494.30` | 2,090,000,000.00 USD | 2,090,000,000.00 USD | 2,380,000.00 USD | 2,730,000.00 USD | 5,000,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 939,880.00 USD | 34,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2497.10` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 3,640,000.00 USD | 3,570,000.00 USD | 6,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2499.90` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 1,110,000.00 USD | 2,430,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2502.70` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 110,450.00 USD | 1,430,000.00 USD | 170,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 217,400.00 USD | 34,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2505.50` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 3,200,000.00 USD | 2,320,000.00 USD | 59,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2508.30` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 1,150,000.00 USD | 1,270,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2511.10` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 2,560,000.00 USD | 3,230,000.00 USD | 2,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2513.90` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 776,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 1,670,000.00 USD | 35,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2516.70` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 97,050.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2519.50` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2522.10` | 702,970,000.00 USD | 702,970,000.00 USD | 80,610.00 USD | 61,830.00 USD | 90,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2522.30` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 1,050,000.00 USD | 0.00 USD | 945,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2524.70` | 703,420,000.00 USD | 703,420,000.00 USD | 421,540.00 USD | 0.00 USD | 30,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 1,000,000.00 USD | 36,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2525.10` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 307,040.00 USD | 224,130.00 USD | 178,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2527.30` | 703,530,000.00 USD | 703,530,000.00 USD | 0.00 USD | 57,450.00 USD | 50,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2527.90` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 1,520,000.00 USD | 871,200.00 USD | 749,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2529.90` | 705,610,000.00 USD | 705,610,000.00 USD | 995,550.00 USD | 645,910.00 USD | 437,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2530.70` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 2,140,000.00 USD | 1,930,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2532.50` | 705,970,000.00 USD | 705,970,000.00 USD | 359,430.00 USD | 0.00 USD | 7,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2533.50` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 2,620,000.00 USD | 1,770,000.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2535.00` | 941,310.00 USD | 37,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2535.10` | 706,740,000.00 USD | 706,740,000.00 USD | 229,190.00 USD | 41,990.00 USD | 499,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2536.30` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 2,810,000.00 USD | 2,460,000.00 USD | 2,740,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2537.70` | 711,300,000.00 USD | 711,300,000.00 USD | 2,030,000.00 USD | 901,140.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2539.10` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 3,530,000.00 USD | 3,180,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2540.30` | 714,150,000.00 USD | 714,150,000.00 USD | 1,140,000.00 USD | 1,100,000.00 USD | 617,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2541.90` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 3,400,000.00 USD | 2,740,000.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2542.90` | 716,340,000.00 USD | 716,340,000.00 USD | 1,100,000.00 USD | 1,070,000.00 USD | 19,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2544.70` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 2,170,000.00 USD | 1,830,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2545.00` | 6,810,000.00 USD | 44,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2545.50` | 717,750,000.00 USD | 717,750,000.00 USD | 590,640.00 USD | 800,740.00 USD | 12,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2547.50` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 2,380,000.00 USD | 938,680.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2548.10` | 720,690,000.00 USD | 720,690,000.00 USD | 1,370,000.00 USD | 832,850.00 USD | 743,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2550.30` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 2,860,000.00 USD | 2,690,000.00 USD | 1,800,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2550.70` | 724,150,000.00 USD | 724,150,000.00 USD | 1,380,000.00 USD | 1,460,000.00 USD | 618,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2553.10` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 2,120,000.00 USD | 788,360.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2553.30` | 724,930,000.00 USD | 724,930,000.00 USD | 468,780.00 USD | 220,540.00 USD | 90,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2555.00` | 316,850.00 USD | 45,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2555.90` | 726,700,000.00 USD | 726,700,000.00 USD | 1,010,000.00 USD | 398,720.00 USD | 366,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2555.90` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 3,290,000.00 USD | 255,750.00 USD | 5,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2558.50` | 728,310,000.00 USD | 728,310,000.00 USD | 722,170.00 USD | 141,030.00 USD | 745,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2558.70` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 3,850,000.00 USD | 1,200,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2561.10` | 732,550,000.00 USD | 732,550,000.00 USD | 1,640,000.00 USD | 1,270,000.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2561.50` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 2,780,000.00 USD | 2,030,000.00 USD | 426,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2563.70` | 734,270,000.00 USD | 734,270,000.00 USD | 440,660.00 USD | 975,880.00 USD | 309,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2564.30` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 1,800,000.00 USD | 2,150,000.00 USD | 1,460,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2565.00` | 1,770,000.00 USD | 46,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2566.30` | 734,420,000.00 USD | 734,420,000.00 USD | 121,690.00 USD | 11,860.00 USD | 11,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2567.10` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 575,630.00 USD | 1,510,000.00 USD | 2,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2568.90` | 734,580,000.00 USD | 734,580,000.00 USD | 162,270.00 USD | 0.00 USD | 3,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2569.90` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 125,250.00 USD | 290,680.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2571.50` | 735,530,000.00 USD | 735,530,000.00 USD | 770,210.00 USD | 169,470.00 USD | 5,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2572.70` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 2,000,000.00 USD | 890,480.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2574.10` | 736,220,000.00 USD | 736,220,000.00 USD | 121,300.00 USD | 191,750.00 USD | 381,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2575.00` | 11,780,000.00 USD | 58,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2575.50` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 2,180,000.00 USD | 440,740.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2576.70` | 736,870,000.00 USD | 736,870,000.00 USD | 439,020.00 USD | 209,570.00 USD | 3,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2578.30` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 734,040.00 USD | 1,480,000.00 USD | 1,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2579.30` | 738,210,000.00 USD | 738,210,000.00 USD | 308,690.00 USD | 314,010.00 USD | 710,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2581.10` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 3,270,000.00 USD | 864,580.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2581.90` | 740,960,000.00 USD | 740,960,000.00 USD | 1,580,000.00 USD | 935,910.00 USD | 234,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2583.90` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 740,840.00 USD | 1,260,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2584.50` | 741,960,000.00 USD | 741,960,000.00 USD | 287,140.00 USD | 153,810.00 USD | 554,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2585.00` | 34,400,000.00 USD | 92,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2586.70` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 1,900,000.00 USD | 2,190,000.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2587.10` | 743,990,000.00 USD | 743,990,000.00 USD | 1,260,000.00 USD | 335,670.00 USD | 439,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2589.50` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 2,840,000.00 USD | 446,810.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2589.70` | 745,300,000.00 USD | 745,300,000.00 USD | 445,920.00 USD | 99,440.00 USD | 763,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2592.30` | 747,540,000.00 USD | 747,540,000.00 USD | 971,410.00 USD | 349,000.00 USD | 919,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2592.30` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 2,340,000.00 USD | 1,280,000.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2594.90` | 750,640,000.00 USD | 750,640,000.00 USD | 886,830.00 USD | 1,220,000.00 USD | 995,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2595.00` | 526,600.00 USD | 93,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2595.10` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 452,020.00 USD | 569,790.00 USD | 752,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2597.50` | 751,600,000.00 USD | 751,600,000.00 USD | 179,030.00 USD | 442,330.00 USD | 339,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2597.90` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 2,280,000.00 USD | 1,630,000.00 USD | 2,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2600.10` | 752,890,000.00 USD | 752,890,000.00 USD | 258,900.00 USD | 724,120.00 USD | 303,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2600.70` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 496,060.00 USD | 1,960,000.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2602.70` | 753,770,000.00 USD | 753,770,000.00 USD | 107,010.00 USD | 453,880.00 USD | 318,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2603.50` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 2,040,000.00 USD | 1,580,000.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2605.00` | 2,280,000.00 USD | 95,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2605.30` | 754,750,000.00 USD | 754,750,000.00 USD | 0.00 USD | 644,330.00 USD | 336,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2606.30` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 1,480,000.00 USD | 229,360.00 USD | 342,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2607.90` | 755,430,000.00 USD | 755,430,000.00 USD | 187,520.00 USD | 497,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2609.10` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2610.50` | 755,730,000.00 USD | 755,730,000.00 USD | 0.00 USD | 294,600.00 USD | 2,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2611.90` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 724,220.00 USD | 608,060.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2613.10` | 756,740,000.00 USD | 756,740,000.00 USD | 555,320.00 USD | 250,240.00 USD | 205,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2614.70` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 1,110,000.00 USD | 1,000,000.00 USD | 409,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2615.00` | 1,400,000.00 USD | 97,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2617.50` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 1,550,000.00 USD | 209,240.00 USD | 392,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2618.30` | 757,040,000.00 USD | 757,040,000.00 USD | 295,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2620.30` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 47,360.00 USD | 1,120,000.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2623.10` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 631,440.00 USD | 410,460.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `7D` | `2068.70` | 2,710,000,000.00 USD | 0.00 USD | 2,710,000,000.00 USD | 1,890,000.00 USD | 1,910,000.00 USD | 939,150.00 USD |
| `7D` | `2071.50` | 2,700,000,000.00 USD | 0.00 USD | 2,700,000,000.00 USD | 2,760,000.00 USD | 1,510,000.00 USD | 1,220,000.00 USD |
| `7D` | `2074.30` | 2,700,000,000.00 USD | 0.00 USD | 2,700,000,000.00 USD | 3,850,000.00 USD | 2,610,000.00 USD | 2,930,000.00 USD |
| `7D` | `2077.10` | 2,690,000,000.00 USD | 0.00 USD | 2,690,000,000.00 USD | 4,430,000.00 USD | 4,120,000.00 USD | 2,000,000.00 USD |
| `7D` | `2079.90` | 2,680,000,000.00 USD | 0.00 USD | 2,680,000,000.00 USD | 3,400,000.00 USD | 3,020,000.00 USD | 2,510,000.00 USD |
| `7D` | `2082.70` | 2,670,000,000.00 USD | 0.00 USD | 2,670,000,000.00 USD | 2,420,000.00 USD | 1,860,000.00 USD | 1,910,000.00 USD |
| `7D` | `2085.50` | 2,660,000,000.00 USD | 0.00 USD | 2,660,000,000.00 USD | 3,840,000.00 USD | 1,860,000.00 USD | 3,120,000.00 USD |
| `7D` | `2088.30` | 2,660,000,000.00 USD | 0.00 USD | 2,660,000,000.00 USD | 2,280,000.00 USD | 1,820,000.00 USD | 907,940.00 USD |
| `7D` | `2091.10` | 2,650,000,000.00 USD | 0.00 USD | 2,650,000,000.00 USD | 4,280,000.00 USD | 952,210.00 USD | 6,980,000.00 USD |
| `7D` | `2093.90` | 2,640,000,000.00 USD | 0.00 USD | 2,640,000,000.00 USD | 5,200,000.00 USD | 1,640,000.00 USD | 2,340,000.00 USD |
| `7D` | `2096.70` | 2,630,000,000.00 USD | 0.00 USD | 2,630,000,000.00 USD | 1,940,000.00 USD | 3,330,000.00 USD | 1,290,000.00 USD |
| `7D` | `2099.50` | 2,620,000,000.00 USD | 0.00 USD | 2,620,000,000.00 USD | 1,880,000.00 USD | 1,520,000.00 USD | 2,070,000.00 USD |
| `7D` | `2102.30` | 2,620,000,000.00 USD | 0.00 USD | 2,620,000,000.00 USD | 125,250.00 USD | 688,260.00 USD | 2,010,000.00 USD |
| `7D` | `2105.10` | 2,610,000,000.00 USD | 0.00 USD | 2,610,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 2,210,000.00 USD |
| `7D` | `2107.90` | 2,610,000,000.00 USD | 0.00 USD | 2,610,000,000.00 USD | 2,320,000.00 USD | 356,360.00 USD | 1,640,000.00 USD |
| `7D` | `2110.70` | 2,600,000,000.00 USD | 0.00 USD | 2,600,000,000.00 USD | 2,830,000.00 USD | 2,300,000.00 USD | 1,960,000.00 USD |
| `1D` | `2111.30` | 1,260,000,000.00 USD | 0.00 USD | 1,260,000,000.00 USD | 1,250,000.00 USD | 343,530.00 USD | 525,670.00 USD |
| `7D` | `2113.50` | 2,600,000,000.00 USD | 0.00 USD | 2,600,000,000.00 USD | 1,730,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD |
| `1D` | `2113.90` | 1,260,000,000.00 USD | 0.00 USD | 1,260,000,000.00 USD | 1,090,000.00 USD | 1,080,000.00 USD | 363,830.00 USD |
| `7D` | `2116.30` | 2,590,000,000.00 USD | 0.00 USD | 2,590,000,000.00 USD | 1,480,000.00 USD | 2,030,000.00 USD | 2,570,000.00 USD |
| `1D` | `2116.50` | 1,260,000,000.00 USD | 0.00 USD | 1,260,000,000.00 USD | 1,240,000.00 USD | 335,670.00 USD | 859,760.00 USD |
| `1D` | `2119.10` | 1,260,000,000.00 USD | 0.00 USD | 1,260,000,000.00 USD | 507,030.00 USD | 201,150.00 USD | 917,320.00 USD |
| `7D` | `2119.10` | 2,590,000,000.00 USD | 0.00 USD | 2,590,000,000.00 USD | 3,390,000.00 USD | 935,590.00 USD | 2,590,000.00 USD |
| `1D` | `2121.70` | 1,260,000,000.00 USD | 0.00 USD | 1,260,000,000.00 USD | 982,960.00 USD | 759,970.00 USD | 1,250,000.00 USD |
| `7D` | `2121.90` | 2,580,000,000.00 USD | 0.00 USD | 2,580,000,000.00 USD | 2,300,000.00 USD | 973,690.00 USD | 1,630,000.00 USD |
| `1D` | `2124.30` | 1,250,000,000.00 USD | 0.00 USD | 1,250,000,000.00 USD | 957,510.00 USD | 1,040,000.00 USD | 525,500.00 USD |
| `7D` | `2124.70` | 2,570,000,000.00 USD | 0.00 USD | 2,570,000,000.00 USD | 2,110,000.00 USD | 983,790.00 USD | 989,650.00 USD |
| `1D` | `2126.90` | 1,250,000,000.00 USD | 0.00 USD | 1,250,000,000.00 USD | 308,590.00 USD | 840,990.00 USD | 629,970.00 USD |
| `7D` | `2127.50` | 2,570,000,000.00 USD | 0.00 USD | 2,570,000,000.00 USD | 1,080,000.00 USD | 2,620,000.00 USD | 3,270,000.00 USD |
| `1D` | `2129.50` | 1,250,000,000.00 USD | 0.00 USD | 1,250,000,000.00 USD | 107,010.00 USD | 453,880.00 USD | 318,170.00 USD |
| `7D` | `2130.30` | 2,560,000,000.00 USD | 0.00 USD | 2,560,000,000.00 USD | 2,040,000.00 USD | 2,130,000.00 USD | 1,680,000.00 USD |
| `1D` | `2132.10` | 1,250,000,000.00 USD | 0.00 USD | 1,250,000,000.00 USD | 0.00 USD | 956,330.00 USD | 336,530.00 USD |
| `7D` | `2133.10` | 2,560,000,000.00 USD | 0.00 USD | 2,560,000,000.00 USD | 1,930,000.00 USD | 715,940.00 USD | 330,780.00 USD |
| `1D` | `2134.70` | 1,250,000,000.00 USD | 0.00 USD | 1,250,000,000.00 USD | 187,520.00 USD | 185,320.00 USD | 0.00 USD |
| `7D` | `2135.90` | 2,550,000,000.00 USD | 0.00 USD | 2,550,000,000.00 USD | 1,370,000.00 USD | 596,290.00 USD | 0.00 USD |
| `1D` | `2137.30` | 1,250,000,000.00 USD | 0.00 USD | 1,250,000,000.00 USD | 236,290.00 USD | 544,840.00 USD | 208,060.00 USD |
| `7D` | `2138.70` | 2,550,000,000.00 USD | 0.00 USD | 2,550,000,000.00 USD | 909,440.00 USD | 1,250,000.00 USD | 78,760.00 USD |
| `1D` | `2139.90` | 1,240,000,000.00 USD | 0.00 USD | 1,240,000,000.00 USD | 319,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2141.50` | 2,550,000,000.00 USD | 0.00 USD | 2,550,000,000.00 USD | 1,750,000.00 USD | 199,980.00 USD | 766,720.00 USD |
| `1D` | `2142.50` | 1,240,000,000.00 USD | 0.00 USD | 1,240,000,000.00 USD | 295,510.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2144.30` | 2,550,000,000.00 USD | 0.00 USD | 2,550,000,000.00 USD | 465,960.00 USD | 1,540,000.00 USD | 268,500.00 USD |
| `1D` | `2145.10` | 1,240,000,000.00 USD | 0.00 USD | 1,240,000,000.00 USD | 0.00 USD | 16,700.00 USD | 3,100.00 USD |
| `7D` | `2147.10` | 2,540,000,000.00 USD | 0.00 USD | 2,540,000,000.00 USD | 311,920.00 USD | 32,210.00 USD | 0.00 USD |
| `1D` | `2147.70` | 1,240,000,000.00 USD | 0.00 USD | 1,240,000,000.00 USD | 251,250.00 USD | 11,090.00 USD | 207,420.00 USD |
| `7D` | `2149.90` | 2,540,000,000.00 USD | 0.00 USD | 2,540,000,000.00 USD | 459,630.00 USD | 482,820.00 USD | 537,180.00 USD |
| `7D` | `2152.70` | 2,540,000,000.00 USD | 0.00 USD | 2,540,000,000.00 USD | 58,340.00 USD | 681,070.00 USD | 0.00 USD |
| `7D` | `2155.50` | 2,540,000,000.00 USD | 0.00 USD | 2,540,000,000.00 USD | 191,860.00 USD | 454,940.00 USD | 866,760.00 USD |
| `7D` | `2158.30` | 2,540,000,000.00 USD | 0.00 USD | 2,540,000,000.00 USD | 738,850.00 USD | 717,210.00 USD | 1,590,000.00 USD |
| `7D` | `2161.10` | 2,540,000,000.00 USD | 0.00 USD | 2,540,000,000.00 USD | 1,490,000.00 USD | 1,350,000.00 USD | 2,240,000.00 USD |
| `7D` | `2163.90` | 2,530,000,000.00 USD | 0.00 USD | 2,530,000,000.00 USD | 36,870.00 USD | 329,690.00 USD | 409,110.00 USD |
| `7D` | `2166.70` | 2,530,000,000.00 USD | 0.00 USD | 2,530,000,000.00 USD | 25,540.00 USD | 0.00 USD | 68,110.00 USD |
| `7D` | `2169.50` | 2,530,000,000.00 USD | 0.00 USD | 2,530,000,000.00 USD | 1,700,000.00 USD | 726,240.00 USD | 810,540.00 USD |
| `7D` | `2172.30` | 2,530,000,000.00 USD | 0.00 USD | 2,530,000,000.00 USD | 479,540.00 USD | 1,150,000.00 USD | 0.00 USD |
| `7D` | `2194.70` | 2,530,000,000.00 USD | 0.00 USD | 2,530,000,000.00 USD | 141,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2197.50` | 2,530,000,000.00 USD | 0.00 USD | 2,530,000,000.00 USD | 2,440,000.00 USD | 3,270,000.00 USD | 0.00 USD |
| `1D` | `2199.70` | 1,240,000,000.00 USD | 0.00 USD | 1,240,000,000.00 USD | 201,540.00 USD | 154,560.00 USD | 80,640.00 USD |
| `7D` | `2200.30` | 2,520,000,000.00 USD | 0.00 USD | 2,520,000,000.00 USD | 3,000,000.00 USD | 3,140,000.00 USD | 3,200,000.00 USD |
| `1D` | `2202.30` | 1,240,000,000.00 USD | 0.00 USD | 1,240,000,000.00 USD | 82,940.00 USD | 62,930.00 USD | 220,140.00 USD |
| `7D` | `2203.10` | 2,510,000,000.00 USD | 0.00 USD | 2,510,000,000.00 USD | 3,240,000.00 USD | 624,500.00 USD | 2,720,000.00 USD |
| `1D` | `2204.90` | 1,240,000,000.00 USD | 0.00 USD | 1,240,000,000.00 USD | 1,050,000.00 USD | 207,110.00 USD | 716,810.00 USD |
| `7D` | `2205.90` | 2,500,000,000.00 USD | 0.00 USD | 2,500,000,000.00 USD | 6,050,000.00 USD | 4,010,000.00 USD | 3,950,000.00 USD |
| `1D` | `2207.50` | 1,240,000,000.00 USD | 0.00 USD | 1,240,000,000.00 USD | 3,100,000.00 USD | 2,380,000.00 USD | 3,090,000.00 USD |
| `7D` | `2208.70` | 2,490,000,000.00 USD | 0.00 USD | 2,490,000,000.00 USD | 10,060,000.00 USD | 6,100,000.00 USD | 4,070,000.00 USD |
| `1D` | `2210.10` | 1,230,000,000.00 USD | 0.00 USD | 1,230,000,000.00 USD | 1,610,000.00 USD | 1,180,000.00 USD | 1,190,000.00 USD |
| `7D` | `2211.50` | 2,470,000,000.00 USD | 0.00 USD | 2,470,000,000.00 USD | 7,320,000.00 USD | 7,940,000.00 USD | 7,060,000.00 USD |
| `1D` | `2212.70` | 1,230,000,000.00 USD | 0.00 USD | 1,230,000,000.00 USD | 2,200,000.00 USD | 1,180,000.00 USD | 1,260,000.00 USD |
| `7D` | `2214.30` | 2,450,000,000.00 USD | 0.00 USD | 2,450,000,000.00 USD | 13,980,000.00 USD | 12,380,000.00 USD | 9,960,000.00 USD |
| `1D` | `2215.30` | 1,220,000,000.00 USD | 0.00 USD | 1,220,000,000.00 USD | 5,950,000.00 USD | 5,220,000.00 USD | 5,490,000.00 USD |
| `7D` | `2217.10` | 2,410,000,000.00 USD | 0.00 USD | 2,410,000,000.00 USD | 16,020,000.00 USD | 10,300,000.00 USD | 8,280,000.00 USD |
| `1D` | `2217.90` | 1,210,000,000.00 USD | 0.00 USD | 1,210,000,000.00 USD | 4,610,000.00 USD | 4,240,000.00 USD | 1,460,000.00 USD |
| `7D` | `2219.90` | 2,380,000,000.00 USD | 0.00 USD | 2,380,000,000.00 USD | 12,620,000.00 USD | 10,310,000.00 USD | 3,040,000.00 USD |
| `1D` | `2220.50` | 1,200,000,000.00 USD | 0.00 USD | 1,200,000,000.00 USD | 3,450,000.00 USD | 4,220,000.00 USD | 680,790.00 USD |
| `7D` | `2222.70` | 2,350,000,000.00 USD | 0.00 USD | 2,350,000,000.00 USD | 5,480,000.00 USD | 5,400,000.00 USD | 8,890,000.00 USD |
| `1D` | `2223.10` | 1,190,000,000.00 USD | 0.00 USD | 1,190,000,000.00 USD | 5,770,000.00 USD | 3,810,000.00 USD | 2,870,000.00 USD |
| `7D` | `2225.50` | 2,330,000,000.00 USD | 0.00 USD | 2,330,000,000.00 USD | 12,980,000.00 USD | 13,620,000.00 USD | 9,460,000.00 USD |
| `1D` | `2225.70` | 1,180,000,000.00 USD | 0.00 USD | 1,180,000,000.00 USD | 3,700,000.00 USD | 5,870,000.00 USD | 2,430,000.00 USD |
| `1D` | `2228.30` | 1,160,000,000.00 USD | 0.00 USD | 1,160,000,000.00 USD | 4,150,000.00 USD | 1,310,000.00 USD | 766,720.00 USD |
| `7D` | `2228.30` | 2,300,000,000.00 USD | 0.00 USD | 2,300,000,000.00 USD | 7,790,000.00 USD | 5,070,000.00 USD | 7,280,000.00 USD |
| `1D` | `2230.90` | 1,160,000,000.00 USD | 0.00 USD | 1,160,000,000.00 USD | 3,630,000.00 USD | 2,460,000.00 USD | 3,100,000.00 USD |
| `7D` | `2231.10` | 2,280,000,000.00 USD | 0.00 USD | 2,280,000,000.00 USD | 9,590,000.00 USD | 3,450,000.00 USD | 17,130,000.00 USD |
| `1D` | `2233.50` | 1,150,000,000.00 USD | 0.00 USD | 1,150,000,000.00 USD | 6,590,000.00 USD | 3,820,000.00 USD | 2,280,000.00 USD |
| `7D` | `2233.90` | 2,250,000,000.00 USD | 0.00 USD | 2,250,000,000.00 USD | 18,230,000.00 USD | 10,390,000.00 USD | 6,100,000.00 USD |
| `1D` | `2236.10` | 1,140,000,000.00 USD | 0.00 USD | 1,140,000,000.00 USD | 2,630,000.00 USD | 2,440,000.00 USD | 3,880,000.00 USD |
| `7D` | `2236.70` | 2,210,000,000.00 USD | 0.00 USD | 2,210,000,000.00 USD | 7,440,000.00 USD | 11,700,000.00 USD | 5,850,000.00 USD |
| `1D` | `2238.70` | 1,130,000,000.00 USD | 0.00 USD | 1,130,000,000.00 USD | 1,620,000.00 USD | 2,150,000.00 USD | 844,590.00 USD |
| `7D` | `2239.50` | 2,190,000,000.00 USD | 0.00 USD | 2,190,000,000.00 USD | 6,630,000.00 USD | 6,820,000.00 USD | 6,100,000.00 USD |
| `1D` | `2241.30` | 1,120,000,000.00 USD | 0.00 USD | 1,120,000,000.00 USD | 321,680.00 USD | 216,600.00 USD | 39,130.00 USD |
| `7D` | `2242.30` | 2,170,000,000.00 USD | 0.00 USD | 2,170,000,000.00 USD | 3,580,000.00 USD | 2,780,000.00 USD | 7,090,000.00 USD |
| `1D` | `2243.90` | 1,120,000,000.00 USD | 0.00 USD | 1,120,000,000.00 USD | 2,380,000.00 USD | 423,680.00 USD | 238,690.00 USD |
| `7D` | `2245.10` | 2,150,000,000.00 USD | 0.00 USD | 2,150,000,000.00 USD | 16,710,000.00 USD | 13,060,000.00 USD | 11,660,000.00 USD |
| `1D` | `2246.50` | 1,120,000,000.00 USD | 0.00 USD | 1,120,000,000.00 USD | 883,930.00 USD | 788,500.00 USD | 1,410,000.00 USD |
| `7D` | `2247.90` | 2,110,000,000.00 USD | 0.00 USD | 2,110,000,000.00 USD | 13,600,000.00 USD | 6,160,000.00 USD | 9,920,000.00 USD |
| `1D` | `2249.10` | 1,120,000,000.00 USD | 0.00 USD | 1,120,000,000.00 USD | 4,190,000.00 USD | 1,420,000.00 USD | 2,130,000.00 USD |
| `7D` | `2250.70` | 2,080,000,000.00 USD | 0.00 USD | 2,080,000,000.00 USD | 10,570,000.00 USD | 10,360,000.00 USD | 8,310,000.00 USD |
| `1D` | `2251.70` | 1,110,000,000.00 USD | 0.00 USD | 1,110,000,000.00 USD | 4,500,000.00 USD | 6,550,000.00 USD | 2,810,000.00 USD |
| `7D` | `2253.50` | 2,050,000,000.00 USD | 0.00 USD | 2,050,000,000.00 USD | 24,760,000.00 USD | 21,020,000.00 USD | 19,300,000.00 USD |
| `1D` | `2254.30` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 7,670,000.00 USD | 3,590,000.00 USD | 5,580,000.00 USD |
| `7D` | `2256.30` | 1,990,000,000.00 USD | 0.00 USD | 1,990,000,000.00 USD | 31,260,000.00 USD | 19,100,000.00 USD | 18,030,000.00 USD |
| `1D` | `2256.90` | 1,080,000,000.00 USD | 0.00 USD | 1,080,000,000.00 USD | 5,660,000.00 USD | 5,380,000.00 USD | 4,210,000.00 USD |
| `7D` | `2259.10` | 1,920,000,000.00 USD | 0.00 USD | 1,920,000,000.00 USD | 22,390,000.00 USD | 19,400,000.00 USD | 22,950,000.00 USD |
| `1D` | `2259.50` | 1,060,000,000.00 USD | 0.00 USD | 1,060,000,000.00 USD | 13,310,000.00 USD | 6,270,000.00 USD | 8,070,000.00 USD |
| `7D` | `2261.90` | 1,850,000,000.00 USD | 0.00 USD | 1,850,000,000.00 USD | 48,180,000.00 USD | 29,390,000.00 USD | 21,430,000.00 USD |
| `1D` | `2262.10` | 1,030,000,000.00 USD | 0.00 USD | 1,030,000,000.00 USD | 15,090,000.00 USD | 12,940,000.00 USD | 13,450,000.00 USD |
| `1D` | `2264.70` | 992,660,000.00 USD | 0.00 USD | 992,660,000.00 USD | 15,200,000.00 USD | 12,030,000.00 USD | 6,600,000.00 USD |
| `7D` | `2264.70` | 1,760,000,000.00 USD | 0.00 USD | 1,760,000,000.00 USD | 30,320,000.00 USD | 28,050,000.00 USD | 19,360,000.00 USD |
| `1D` | `2267.30` | 958,830,000.00 USD | 0.00 USD | 958,830,000.00 USD | 5,460,000.00 USD | 10,030,000.00 USD | 3,120,000.00 USD |
| `7D` | `2267.50` | 1,680,000,000.00 USD | 0.00 USD | 1,680,000,000.00 USD | 40,120,000.00 USD | 40,100,000.00 USD | 31,060,000.00 USD |
| `1D` | `2269.90` | 940,220,000.00 USD | 0.00 USD | 940,220,000.00 USD | 14,410,000.00 USD | 11,130,000.00 USD | 8,240,000.00 USD |
| `7D` | `2270.30` | 1,570,000,000.00 USD | 0.00 USD | 1,570,000,000.00 USD | 39,480,000.00 USD | 27,490,000.00 USD | 39,210,000.00 USD |
| `1D` | `2272.50` | 906,440,000.00 USD | 0.00 USD | 906,440,000.00 USD | 14,080,000.00 USD | 10,950,000.00 USD | 10,060,000.00 USD |
| `7D` | `2273.10` | 1,460,000,000.00 USD | 0.00 USD | 1,460,000,000.00 USD | 33,160,000.00 USD | 25,760,000.00 USD | 19,780,000.00 USD |
| `1D` | `2275.10` | 871,350,000.00 USD | 0.00 USD | 871,350,000.00 USD | 9,170,000.00 USD | 15,450,000.00 USD | 4,220,000.00 USD |
| `7D` | `2275.90` | 1,380,000,000.00 USD | 0.00 USD | 1,380,000,000.00 USD | 48,240,000.00 USD | 42,710,000.00 USD | 44,210,000.00 USD |
| `1D` | `2277.70` | 842,510,000.00 USD | 0.00 USD | 842,510,000.00 USD | 16,430,000.00 USD | 8,710,000.00 USD | 18,070,000.00 USD |
| `7D` | `2278.70` | 1,250,000,000.00 USD | 0.00 USD | 1,250,000,000.00 USD | 74,310,000.00 USD | 34,750,000.00 USD | 42,010,000.00 USD |
| `1D` | `2280.30` | 799,300,000.00 USD | 0.00 USD | 799,300,000.00 USD | 24,350,000.00 USD | 14,020,000.00 USD | 8,040,000.00 USD |
| `7D` | `2281.50` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 56,100,000.00 USD | 59,940,000.00 USD | 49,270,000.00 USD |
| `1D` | `2282.90` | 752,900,000.00 USD | 0.00 USD | 752,900,000.00 USD | 22,370,000.00 USD | 16,300,000.00 USD | 19,060,000.00 USD |
| `7D` | `2284.30` | 929,630,000.00 USD | 0.00 USD | 929,630,000.00 USD | 89,220,000.00 USD | 69,840,000.00 USD | 44,200,000.00 USD |
| `1D` | `2285.50` | 695,170,000.00 USD | 0.00 USD | 695,170,000.00 USD | 28,040,000.00 USD | 29,580,000.00 USD | 19,400,000.00 USD |
| `7D` | `2287.10` | 726,370,000.00 USD | 0.00 USD | 726,370,000.00 USD | 58,910,000.00 USD | 53,380,000.00 USD | 45,180,000.00 USD |
| `1D` | `2288.10` | 618,150,000.00 USD | 0.00 USD | 618,150,000.00 USD | 19,180,000.00 USD | 14,480,000.00 USD | 4,720,000.00 USD |
| `7D` | `2289.90` | 568,900,000.00 USD | 0.00 USD | 568,900,000.00 USD | 48,430,000.00 USD | 34,490,000.00 USD | 22,190,000.00 USD |
| `1D` | `2290.70` | 579,780,000.00 USD | 0.00 USD | 579,780,000.00 USD | 12,240,000.00 USD | 7,760,000.00 USD | 2,460,000.00 USD |
| `7D` | `2292.70` | 463,800,000.00 USD | 0.00 USD | 463,800,000.00 USD | 38,110,000.00 USD | 20,900,000.00 USD | 44,070,000.00 USD |
| `1D` | `2293.30` | 557,320,000.00 USD | 0.00 USD | 557,320,000.00 USD | 18,860,000.00 USD | 18,460,000.00 USD | 15,490,000.00 USD |
| `7D` | `2295.50` | 360,720,000.00 USD | 0.00 USD | 360,720,000.00 USD | 17,510,000.00 USD | 8,110,000.00 USD | 7,220,000.00 USD |
| `1D` | `2295.90` | 504,520,000.00 USD | 0.00 USD | 504,520,000.00 USD | 23,870,000.00 USD | 15,930,000.00 USD | 7,210,000.00 USD |
| `7D` | `2298.30` | 327,880,000.00 USD | 0.00 USD | 327,880,000.00 USD | 2,090,000.00 USD | 5,410,000.00 USD | 301,550.00 USD |
| `1D` | `2298.50` | 457,510,000.00 USD | 0.00 USD | 457,510,000.00 USD | 8,010,000.00 USD | 7,220,000.00 USD | 3,250,000.00 USD |
| `1D` | `2301.10` | 439,040,000.00 USD | 0.00 USD | 439,040,000.00 USD | 17,170,000.00 USD | 11,820,000.00 USD | 13,320,000.00 USD |
| `7D` | `2301.10` | 320,070,000.00 USD | 0.00 USD | 320,070,000.00 USD | 11,790,000.00 USD | 2,200,000.00 USD | 7,590,000.00 USD |
| `1D` | `2303.70` | 396,730,000.00 USD | 0.00 USD | 396,730,000.00 USD | 29,770,000.00 USD | 15,890,000.00 USD | 10,680,000.00 USD |
| `7D` | `2303.90` | 298,500,000.00 USD | 0.00 USD | 298,500,000.00 USD | 32,960,000.00 USD | 17,020,000.00 USD | 13,270,000.00 USD |
| `1D` | `2306.30` | 340,400,000.00 USD | 0.00 USD | 340,400,000.00 USD | 4,970,000.00 USD | 5,530,000.00 USD | 15,350,000.00 USD |
| `7D` | `2306.70` | 235,250,000.00 USD | 0.00 USD | 235,250,000.00 USD | 0.00 USD | 3,740,000.00 USD | 10,890,000.00 USD |
| `1D` | `2308.90` | 314,550,000.00 USD | 0.00 USD | 314,550,000.00 USD | 642,440.00 USD | 1,990,000.00 USD | 2,540,000.00 USD |
| `7D` | `2309.50` | 220,620,000.00 USD | 0.00 USD | 220,620,000.00 USD | 282,530.00 USD | 300,580.00 USD | 1,500,000.00 USD |
| `1D` | `2311.50` | 309,380,000.00 USD | 0.00 USD | 309,380,000.00 USD | 7,190,000.00 USD | 3,230,000.00 USD | 5,780,000.00 USD |
| `7D` | `2312.30` | 218,530,000.00 USD | 0.00 USD | 218,530,000.00 USD | 1,740,000.00 USD | 128,300.00 USD | 2,500,000.00 USD |
| `1D` | `2314.10` | 293,190,000.00 USD | 0.00 USD | 293,190,000.00 USD | 10,080,000.00 USD | 3,280,000.00 USD | 688,260.00 USD |
| `7D` | `2315.10` | 214,150,000.00 USD | 0.00 USD | 214,150,000.00 USD | 4,300,000.00 USD | 4,100,000.00 USD | 117,510.00 USD |
| `1D` | `2316.70` | 279,140,000.00 USD | 0.00 USD | 279,140,000.00 USD | 3,450,000.00 USD | 5,270,000.00 USD | 3,700,000.00 USD |
| `7D` | `2317.90` | 205,640,000.00 USD | 0.00 USD | 205,640,000.00 USD | 817,040.00 USD | 3,010,000.00 USD | 0.00 USD |
| `1D` | `2319.30` | 266,720,000.00 USD | 0.00 USD | 266,720,000.00 USD | 8,240,000.00 USD | 2,120,000.00 USD | 795,520.00 USD |
| `7D` | `2320.70` | 201,810,000.00 USD | 0.00 USD | 201,810,000.00 USD | 0.00 USD | 2,790,000.00 USD | 0.00 USD |
| `1D` | `2321.90` | 255,570,000.00 USD | 0.00 USD | 255,570,000.00 USD | 616,250.00 USD | 2,660,000.00 USD | 1,660,000.00 USD |
| `7D` | `2323.50` | 199,020,000.00 USD | 0.00 USD | 199,020,000.00 USD | 4,070,000.00 USD | 1,900,000.00 USD | 0.00 USD |
| `1D` | `2324.50` | 250,630,000.00 USD | 0.00 USD | 250,630,000.00 USD | 8,660,000.00 USD | 2,780,000.00 USD | 2,210,000.00 USD |
| `7D` | `2326.30` | 193,050,000.00 USD | 0.00 USD | 193,050,000.00 USD | 0.00 USD | 0.00 USD | 126,530.00 USD |
| `1D` | `2327.10` | 236,970,000.00 USD | 0.00 USD | 236,970,000.00 USD | 0.00 USD | 3,260,000.00 USD | 4,450,000.00 USD |
| `7D` | `2329.10` | 192,920,000.00 USD | 0.00 USD | 192,920,000.00 USD | 3,860,000.00 USD | 0.00 USD | 4,880,000.00 USD |
| `1D` | `2329.70` | 229,260,000.00 USD | 0.00 USD | 229,260,000.00 USD | 5,520,000.00 USD | 1,150,000.00 USD | 3,040,000.00 USD |
| `7D` | `2331.90` | 184,180,000.00 USD | 0.00 USD | 184,180,000.00 USD | 29,230,000.00 USD | 1,090,000.00 USD | 2,810,000.00 USD |
| `1D` | `2332.30` | 219,550,000.00 USD | 0.00 USD | 219,550,000.00 USD | 17,970,000.00 USD | 2,290,000.00 USD | 107,090.00 USD |
| `7D` | `2334.70` | 151,040,000.00 USD | 0.00 USD | 151,040,000.00 USD | 7,260,000.00 USD | 18,420,000.00 USD | 8,930,000.00 USD |
| `1D` | `2334.90` | 199,180,000.00 USD | 0.00 USD | 199,180,000.00 USD | 28,290,000.00 USD | 25,090,000.00 USD | 16,090,000.00 USD |
| `1D` | `2337.50` | 129,720,000.00 USD | 0.00 USD | 129,720,000.00 USD | 6,570,000.00 USD | 22,000,000.00 USD | 10,170,000.00 USD |
| `7D` | `2337.50` | 116,430,000.00 USD | 0.00 USD | 116,430,000.00 USD | 20,380,000.00 USD | 18,560,000.00 USD | 13,560,000.00 USD |
| `1D` | `2340.10` | 90,980,000.00 USD | 0.00 USD | 90,980,000.00 USD | 4,960,000.00 USD | 21,890,000.00 USD | 7,070,000.00 USD |
| `7D` | `2340.30` | 63,920,000.00 USD | 0.00 USD | 63,920,000.00 USD | 1,630,000.00 USD | 10,010,000.00 USD | 3,380,000.00 USD |
| `1D` | `2342.70` | 57,060,000.00 USD | 0.00 USD | 57,060,000.00 USD | 5,030,000.00 USD | 8,490,000.00 USD | 2,160,000.00 USD |
| `7D` | `2343.10` | 48,890,000.00 USD | 0.00 USD | 48,890,000.00 USD | 0.00 USD | 5,540,000.00 USD | 3,840,000.00 USD |
| `1D` | `2345.30` | 41,380,000.00 USD | 0.00 USD | 41,380,000.00 USD | 963,370.00 USD | 1,770,000.00 USD | 9,990,000.00 USD |
| `7D` | `2345.90` | 39,510,000.00 USD | 0.00 USD | 39,510,000.00 USD | 0.00 USD | 8,310,000.00 USD | 12,830,000.00 USD |
| `1D` | `2347.90` | 28,650,000.00 USD | 0.00 USD | 28,650,000.00 USD | 215,860.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2348.70` | 18,370,000.00 USD | 0.00 USD | 18,370,000.00 USD | 285,680.00 USD | 7,340,000.00 USD | 10,750,000.00 USD |
| `7D` | `2349.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2350.50` | 28,430,000.00 USD | 0.00 USD | 28,430,000.00 USD | 25,900,000.00 USD | 2,510,000.00 USD | 23,220.00 USD |
| `7D` | `2351.50` | 23,900,000.00 USD | 23,900,000.00 USD | 0.00 USD | 782,590.00 USD | 17,440,000.00 USD | 5,680,000.00 USD |
| `1D` | `2351.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2353.10` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 576,450.00 USD | 1,110,000.00 USD | 107,380.00 USD |
| `7D` | `2354.30` | 65,110,000.00 USD | 65,110,000.00 USD | 0.00 USD | 5,960,000.00 USD | 35,020,000.00 USD | 237,340.00 USD |
| `1D` | `2355.70` | 19,330,000.00 USD | 19,330,000.00 USD | 0.00 USD | 318,080.00 USD | 15,970,000.00 USD | 1,240,000.00 USD |
| `7D` | `2357.10` | 78,410,000.00 USD | 78,410,000.00 USD | 0.00 USD | 7,900,000.00 USD | 5,400,000.00 USD | 0.00 USD |
| `1D` | `2358.30` | 19,520,000.00 USD | 19,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 198,570.00 USD |
| `7D` | `2359.90` | 80,630,000.00 USD | 80,630,000.00 USD | 0.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2360.90` | 21,470,000.00 USD | 21,470,000.00 USD | 0.00 USD | 1,850,000.00 USD | 0.00 USD | 93,130.00 USD |
| `7D` | `2362.70` | 82,790,000.00 USD | 82,790,000.00 USD | 0.00 USD | 467,570.00 USD | 0.00 USD | 1,690,000.00 USD |
| `1D` | `2363.50` | 24,580,000.00 USD | 24,580,000.00 USD | 0.00 USD | 929,610.00 USD | 1,840,000.00 USD | 341,510.00 USD |
| `7D` | `2365.50` | 90,790,000.00 USD | 90,790,000.00 USD | 0.00 USD | 6,340,000.00 USD | 0.00 USD | 1,660,000.00 USD |
| `1D` | `2366.10` | 24,820,000.00 USD | 24,820,000.00 USD | 0.00 USD | 61,300.00 USD | 0.00 USD | 170,870.00 USD |
| `7D` | `2368.30` | 100,760,000.00 USD | 100,760,000.00 USD | 0.00 USD | 9,590,000.00 USD | 0.00 USD | 370,810.00 USD |
| `1D` | `2368.70` | 37,300,000.00 USD | 37,300,000.00 USD | 0.00 USD | 8,060,000.00 USD | 3,260,000.00 USD | 1,170,000.00 USD |
| `7D` | `2371.10` | 162,550,000.00 USD | 162,550,000.00 USD | 0.00 USD | 16,760,000.00 USD | 0.00 USD | 45,040,000.00 USD |
| `1D` | `2371.30` | 75,680,000.00 USD | 75,680,000.00 USD | 0.00 USD | 17,050,000.00 USD | 12,840,000.00 USD | 8,490,000.00 USD |
| `1D` | `2373.90` | 93,230,000.00 USD | 93,230,000.00 USD | 0.00 USD | 13,630,000.00 USD | 955,690.00 USD | 2,970,000.00 USD |
| `7D` | `2373.90` | 185,110,000.00 USD | 185,110,000.00 USD | 0.00 USD | 15,830,000.00 USD | 0.00 USD | 6,730,000.00 USD |
| `1D` | `2376.50` | 119,130,000.00 USD | 119,130,000.00 USD | 0.00 USD | 12,130,000.00 USD | 3,180,000.00 USD | 10,590,000.00 USD |
| `7D` | `2376.70` | 225,250,000.00 USD | 225,250,000.00 USD | 0.00 USD | 12,140,000.00 USD | 5,950,000.00 USD | 22,050,000.00 USD |
| `1D` | `2379.10` | 150,490,000.00 USD | 150,490,000.00 USD | 0.00 USD | 5,850,000.00 USD | 13,800,000.00 USD | 11,720,000.00 USD |
| `7D` | `2379.50` | 252,570,000.00 USD | 252,570,000.00 USD | 0.00 USD | 7,180,000.00 USD | 2,580,000.00 USD | 17,560,000.00 USD |
| `1D` | `2381.70` | 192,290,000.00 USD | 192,290,000.00 USD | 0.00 USD | 15,410,000.00 USD | 10,970,000.00 USD | 15,420,000.00 USD |
| `7D` | `2382.30` | 293,920,000.00 USD | 293,920,000.00 USD | 0.00 USD | 7,910,000.00 USD | 12,120,000.00 USD | 21,320,000.00 USD |
| `1D` | `2384.30` | 241,320,000.00 USD | 241,320,000.00 USD | 0.00 USD | 20,840,000.00 USD | 17,560,000.00 USD | 10,610,000.00 USD |
| `7D` | `2385.10` | 380,660,000.00 USD | 380,660,000.00 USD | 0.00 USD | 14,990,000.00 USD | 28,990,000.00 USD | 42,760,000.00 USD |
| `1D` | `2386.90` | 271,590,000.00 USD | 271,590,000.00 USD | 0.00 USD | 12,200,000.00 USD | 11,050,000.00 USD | 7,020,000.00 USD |
| `7D` | `2387.90` | 460,800,000.00 USD | 460,800,000.00 USD | 0.00 USD | 4,870,000.00 USD | 32,720,000.00 USD | 42,550,000.00 USD |
| `1D` | `2389.50` | 295,530,000.00 USD | 295,530,000.00 USD | 0.00 USD | 9,590,000.00 USD | 8,400,000.00 USD | 5,950,000.00 USD |
| `7D` | `2390.70` | 560,480,000.00 USD | 560,480,000.00 USD | 0.00 USD | 5,470,000.00 USD | 45,700,000.00 USD | 48,520,000.00 USD |
| `1D` | `2392.10` | 323,270,000.00 USD | 323,270,000.00 USD | 0.00 USD | 5,340,000.00 USD | 13,820,000.00 USD | 8,570,000.00 USD |
| `7D` | `2393.50` | 658,950,000.00 USD | 658,950,000.00 USD | 0.00 USD | 43,890,000.00 USD | 22,890,000.00 USD | 31,690,000.00 USD |
| `1D` | `2394.70` | 354,220,000.00 USD | 354,220,000.00 USD | 0.00 USD | 14,780,000.00 USD | 13,450,000.00 USD | 2,740,000.00 USD |
| `7D` | `2396.30` | 742,990,000.00 USD | 742,990,000.00 USD | 0.00 USD | 29,820,000.00 USD | 32,850,000.00 USD | 21,360,000.00 USD |
| `1D` | `2397.30` | 373,410,000.00 USD | 373,410,000.00 USD | 0.00 USD | 5,540,000.00 USD | 8,740,000.00 USD | 4,910,000.00 USD |
| `7D` | `2399.10` | 832,520,000.00 USD | 832,520,000.00 USD | 0.00 USD | 39,350,000.00 USD | 31,200,000.00 USD | 18,980,000.00 USD |
| `1D` | `2399.90` | 414,720,000.00 USD | 414,720,000.00 USD | 0.00 USD | 17,930,000.00 USD | 9,240,000.00 USD | 14,130,000.00 USD |
| `7D` | `2401.90` | 943,310,000.00 USD | 943,310,000.00 USD | 0.00 USD | 53,530,000.00 USD | 24,490,000.00 USD | 32,780,000.00 USD |
| `1D` | `2402.50` | 441,220,000.00 USD | 441,220,000.00 USD | 0.00 USD | 8,820,000.00 USD | 9,710,000.00 USD | 7,970,000.00 USD |
| `7D` | `2404.70` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 0.00 USD | 36,370,000.00 USD | 25,840,000.00 USD | 15,520,000.00 USD |
| `1D` | `2405.10` | 474,650,000.00 USD | 474,650,000.00 USD | 0.00 USD | 13,880,000.00 USD | 10,580,000.00 USD | 8,970,000.00 USD |
| `7D` | `2407.50` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 22,760,000.00 USD | 29,510,000.00 USD | 18,930,000.00 USD |
| `1D` | `2407.70` | 509,790,000.00 USD | 509,790,000.00 USD | 0.00 USD | 14,050,000.00 USD | 11,560,000.00 USD | 9,530,000.00 USD |
| `1D` | `2410.30` | 534,440,000.00 USD | 534,440,000.00 USD | 0.00 USD | 9,390,000.00 USD | 8,300,000.00 USD | 6,950,000.00 USD |
| `7D` | `2410.30` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 26,620,000.00 USD | 26,620,000.00 USD | 23,370,000.00 USD |
| `1D` | `2412.90` | 553,970,000.00 USD | 553,970,000.00 USD | 0.00 USD | 9,190,000.00 USD | 6,900,000.00 USD | 3,440,000.00 USD |
| `7D` | `2413.10` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 13,360,000.00 USD | 15,180,000.00 USD | 13,360,000.00 USD |
| `1D` | `2415.50` | 566,990,000.00 USD | 566,990,000.00 USD | 0.00 USD | 3,550,000.00 USD | 5,790,000.00 USD | 3,690,000.00 USD |
| `7D` | `2415.90` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 0.00 USD | 28,030,000.00 USD | 17,450,000.00 USD | 32,370,000.00 USD |
| `1D` | `2418.10` | 579,910,000.00 USD | 579,910,000.00 USD | 0.00 USD | 4,840,000.00 USD | 5,370,000.00 USD | 2,700,000.00 USD |
| `7D` | `2418.70` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 28,840,000.00 USD | 18,500,000.00 USD | 12,150,000.00 USD |
| `1D` | `2420.70` | 594,840,000.00 USD | 594,840,000.00 USD | 0.00 USD | 6,810,000.00 USD | 5,220,000.00 USD | 2,900,000.00 USD |
| `7D` | `2421.50` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 23,440,000.00 USD | 25,120,000.00 USD | 18,550,000.00 USD |
| `1D` | `2423.30` | 608,680,000.00 USD | 608,680,000.00 USD | 0.00 USD | 4,570,000.00 USD | 3,780,000.00 USD | 5,490,000.00 USD |
| `7D` | `2424.30` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 0.00 USD | 25,250,000.00 USD | 29,620,000.00 USD | 33,670,000.00 USD |
| `1D` | `2425.90` | 611,780,000.00 USD | 611,780,000.00 USD | 0.00 USD | 516,070.00 USD | 2,560,000.00 USD | 27,530.00 USD |
| `7D` | `2427.10` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 24,580,000.00 USD | 22,020,000.00 USD | 23,630,000.00 USD |
| `1D` | `2428.50` | 613,900,000.00 USD | 613,900,000.00 USD | 0.00 USD | 2,090,000.00 USD | 12,140.00 USD | 19,240.00 USD |
| `7D` | `2429.90` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 6,160,000.00 USD | 14,060,000.00 USD | 6,850,000.00 USD |
| `1D` | `2431.10` | 616,750,000.00 USD | 616,750,000.00 USD | 0.00 USD | 2,090,000.00 USD | 507,190.00 USD | 254,180.00 USD |
| `7D` | `2432.70` | 1,640,000,000.00 USD | 1,640,000,000.00 USD | 0.00 USD | 17,740,000.00 USD | 13,220,000.00 USD | 6,540,000.00 USD |
| `1D` | `2433.70` | 619,600,000.00 USD | 619,600,000.00 USD | 0.00 USD | 314,980.00 USD | 534,830.00 USD | 2,000,000.00 USD |
| `7D` | `2435.50` | 1,690,000,000.00 USD | 1,690,000,000.00 USD | 0.00 USD | 22,360,000.00 USD | 14,140,000.00 USD | 15,430,000.00 USD |
| `1D` | `2436.30` | 624,470,000.00 USD | 624,470,000.00 USD | 0.00 USD | 3,340,000.00 USD | 1,270,000.00 USD | 261,300.00 USD |
| `7D` | `2438.30` | 1,750,000,000.00 USD | 1,750,000,000.00 USD | 0.00 USD | 17,900,000.00 USD | 23,900,000.00 USD | 15,750,000.00 USD |
| `1D` | `2438.90` | 629,050,000.00 USD | 629,050,000.00 USD | 0.00 USD | 1,260,000.00 USD | 1,610,000.00 USD | 1,710,000.00 USD |
| `7D` | `2441.10` | 1,790,000,000.00 USD | 1,790,000,000.00 USD | 0.00 USD | 17,250,000.00 USD | 6,990,000.00 USD | 14,660,000.00 USD |
| `1D` | `2441.50` | 637,910,000.00 USD | 637,910,000.00 USD | 0.00 USD | 4,710,000.00 USD | 3,380,000.00 USD | 767,510.00 USD |
| `7D` | `2443.90` | 1,820,000,000.00 USD | 1,820,000,000.00 USD | 0.00 USD | 6,650,000.00 USD | 13,590,000.00 USD | 7,960,000.00 USD |
| `1D` | `2444.10` | 641,140,000.00 USD | 641,140,000.00 USD | 0.00 USD | 791,730.00 USD | 798,660.00 USD | 1,640,000.00 USD |
| `1D` | `2446.70` | 648,900,000.00 USD | 648,900,000.00 USD | 0.00 USD | 4,320,000.00 USD | 1,500,000.00 USD | 1,940,000.00 USD |
| `7D` | `2446.70` | 1,850,000,000.00 USD | 1,850,000,000.00 USD | 0.00 USD | 11,870,000.00 USD | 7,020,000.00 USD | 18,970,000.00 USD |
| `1D` | `2449.30` | 655,440,000.00 USD | 655,440,000.00 USD | 0.00 USD | 2,040,000.00 USD | 1,740,000.00 USD | 2,760,000.00 USD |
| `7D` | `2449.50` | 1,890,000,000.00 USD | 1,890,000,000.00 USD | 0.00 USD | 15,780,000.00 USD | 9,650,000.00 USD | 14,870,000.00 USD |
| `1D` | `2451.90` | 667,710,000.00 USD | 667,710,000.00 USD | 0.00 USD | 3,860,000.00 USD | 3,720,000.00 USD | 4,690,000.00 USD |
| `7D` | `2452.30` | 1,920,000,000.00 USD | 1,920,000,000.00 USD | 0.00 USD | 10,050,000.00 USD | 9,630,000.00 USD | 7,330,000.00 USD |
| `1D` | `2454.50` | 677,880,000.00 USD | 677,880,000.00 USD | 0.00 USD | 4,200,000.00 USD | 3,460,000.00 USD | 2,510,000.00 USD |
| `7D` | `2455.10` | 1,940,000,000.00 USD | 1,940,000,000.00 USD | 0.00 USD | 5,550,000.00 USD | 5,830,000.00 USD | 3,620,000.00 USD |
| `1D` | `2457.10` | 685,030,000.00 USD | 685,030,000.00 USD | 0.00 USD | 2,160,000.00 USD | 2,720,000.00 USD | 2,270,000.00 USD |
| `7D` | `2457.90` | 1,970,000,000.00 USD | 1,970,000,000.00 USD | 0.00 USD | 12,470,000.00 USD | 11,200,000.00 USD | 13,240,000.00 USD |
| `1D` | `2459.70` | 690,710,000.00 USD | 690,710,000.00 USD | 0.00 USD | 2,370,000.00 USD | 1,970,000.00 USD | 1,340,000.00 USD |
| `7D` | `2460.70` | 2,000,000,000.00 USD | 2,000,000,000.00 USD | 0.00 USD | 7,010,000.00 USD | 10,640,000.00 USD | 5,770,000.00 USD |
| `1D` | `2462.30` | 694,030,000.00 USD | 694,030,000.00 USD | 0.00 USD | 174,920.00 USD | 2,050,000.00 USD | 1,100,000.00 USD |
| `7D` | `2463.50` | 2,020,000,000.00 USD | 2,020,000,000.00 USD | 0.00 USD | 9,490,000.00 USD | 9,600,000.00 USD | 8,830,000.00 USD |
| `1D` | `2464.90` | 696,100,000.00 USD | 696,100,000.00 USD | 0.00 USD | 820,990.00 USD | 1,240,000.00 USD | 5,650.00 USD |
| `7D` | `2466.30` | 2,030,000,000.00 USD | 2,030,000,000.00 USD | 0.00 USD | 5,400,000.00 USD | 2,080,000.00 USD | 1,330,000.00 USD |
| `1D` | `2467.50` | 696,480,000.00 USD | 696,480,000.00 USD | 0.00 USD | 0.00 USD | 370,410.00 USD | 7,190.00 USD |
| `7D` | `2469.10` | 2,040,000,000.00 USD | 2,040,000,000.00 USD | 0.00 USD | 2,770,000.00 USD | 3,570,000.00 USD | 408,300.00 USD |
| `1D` | `2470.10` | 700,530,000.00 USD | 700,530,000.00 USD | 0.00 USD | 1,390,000.00 USD | 1,510,000.00 USD | 1,160,000.00 USD |
| `7D` | `2471.90` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 0.00 USD | 3,090,000.00 USD | 2,760,000.00 USD | 814,440.00 USD |
| `1D` | `2472.70` | 700,770,000.00 USD | 700,770,000.00 USD | 0.00 USD | 0.00 USD | 232,740.00 USD | 3,820.00 USD |
| `7D` | `2474.70` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 0.00 USD | 5,400,000.00 USD | 866,790.00 USD | 1,720,000.00 USD |
| `1D` | `2475.30` | 701,510,000.00 USD | 701,510,000.00 USD | 0.00 USD | 738,780.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2477.50` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 0.00 USD | 790,860.00 USD | 3,880,000.00 USD | 1,200,000.00 USD |
| `1D` | `2477.90` | 701,560,000.00 USD | 701,560,000.00 USD | 0.00 USD | 0.00 USD | 41,760.00 USD | 7,750.00 USD |
| `7D` | `2480.30` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 0.00 USD | 2,300,000.00 USD | 1,740,000.00 USD | 0.00 USD |
| `1D` | `2480.50` | 702,110,000.00 USD | 702,110,000.00 USD | 0.00 USD | 0.00 USD | 27,720.00 USD | 518,550.00 USD |
| `1D` | `2483.10` | 702,730,000.00 USD | 702,730,000.00 USD | 0.00 USD | 628,130.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2483.10` | 2,070,000,000.00 USD | 2,070,000,000.00 USD | 0.00 USD | 2,010,000.00 USD | 1,330,000.00 USD | 1,990,000.00 USD |
| `7D` | `2485.90` | 2,070,000,000.00 USD | 2,070,000,000.00 USD | 0.00 USD | 586,480.00 USD | 1,560,000.00 USD | 77,610.00 USD |
| `7D` | `2488.70` | 2,080,000,000.00 USD | 2,080,000,000.00 USD | 0.00 USD | 1,710,000.00 USD | 842,740.00 USD | 2,100,000.00 USD |
| `7D` | `2491.50` | 2,080,000,000.00 USD | 2,080,000,000.00 USD | 0.00 USD | 1,660,000.00 USD | 2,550,000.00 USD | 672,990.00 USD |
| `7D` | `2494.30` | 2,090,000,000.00 USD | 2,090,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,730,000.00 USD | 5,000,000.00 USD |
| `7D` | `2497.10` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 0.00 USD | 3,640,000.00 USD | 3,570,000.00 USD | 6,690,000.00 USD |
| `7D` | `2499.90` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 0.00 USD | 1,110,000.00 USD | 2,430,000.00 USD | 1,090,000.00 USD |
| `7D` | `2502.70` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 0.00 USD | 110,450.00 USD | 1,430,000.00 USD | 170,270.00 USD |
| `7D` | `2505.50` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 0.00 USD | 3,200,000.00 USD | 2,320,000.00 USD | 59,220.00 USD |
| `7D` | `2508.30` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 0.00 USD | 1,150,000.00 USD | 1,270,000.00 USD | 1,990,000.00 USD |
| `7D` | `2511.10` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 0.00 USD | 2,560,000.00 USD | 3,230,000.00 USD | 2,640,000.00 USD |
| `7D` | `2513.90` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 0.00 USD | 776,920.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2516.70` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 0.00 USD | 97,050.00 USD | 189,640.00 USD | 0.00 USD |
| `7D` | `2519.50` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD |
| `1D` | `2522.10` | 702,970,000.00 USD | 702,970,000.00 USD | 0.00 USD | 80,610.00 USD | 61,830.00 USD | 90,130.00 USD |
| `7D` | `2522.30` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 0.00 USD | 1,050,000.00 USD | 0.00 USD | 945,860.00 USD |
| `1D` | `2524.70` | 703,420,000.00 USD | 703,420,000.00 USD | 0.00 USD | 421,540.00 USD | 0.00 USD | 30,180.00 USD |
| `7D` | `2525.10` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 0.00 USD | 307,040.00 USD | 224,130.00 USD | 178,180.00 USD |
| `1D` | `2527.30` | 703,530,000.00 USD | 703,530,000.00 USD | 0.00 USD | 0.00 USD | 57,450.00 USD | 50,470.00 USD |
| `7D` | `2527.90` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 0.00 USD | 1,520,000.00 USD | 871,200.00 USD | 749,440.00 USD |
| `1D` | `2529.90` | 705,610,000.00 USD | 705,610,000.00 USD | 0.00 USD | 995,550.00 USD | 645,910.00 USD | 437,490.00 USD |
| `7D` | `2530.70` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 0.00 USD | 2,140,000.00 USD | 1,930,000.00 USD | 1,220,000.00 USD |
| `1D` | `2532.50` | 705,970,000.00 USD | 705,970,000.00 USD | 0.00 USD | 359,430.00 USD | 0.00 USD | 7,120.00 USD |
| `7D` | `2533.50` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 0.00 USD | 2,620,000.00 USD | 1,770,000.00 USD | 1,390,000.00 USD |
| `1D` | `2535.10` | 706,740,000.00 USD | 706,740,000.00 USD | 0.00 USD | 229,190.00 USD | 41,990.00 USD | 499,440.00 USD |
| `7D` | `2536.30` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 0.00 USD | 2,810,000.00 USD | 2,460,000.00 USD | 2,740,000.00 USD |
| `1D` | `2537.70` | 711,300,000.00 USD | 711,300,000.00 USD | 0.00 USD | 2,030,000.00 USD | 901,140.00 USD | 1,620,000.00 USD |
| `7D` | `2539.10` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 0.00 USD | 3,530,000.00 USD | 3,180,000.00 USD | 1,090,000.00 USD |
| `1D` | `2540.30` | 714,150,000.00 USD | 714,150,000.00 USD | 0.00 USD | 1,140,000.00 USD | 1,100,000.00 USD | 617,540.00 USD |
| `7D` | `2541.90` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 0.00 USD | 3,400,000.00 USD | 2,740,000.00 USD | 2,240,000.00 USD |
| `1D` | `2542.90` | 716,340,000.00 USD | 716,340,000.00 USD | 0.00 USD | 1,100,000.00 USD | 1,070,000.00 USD | 19,390.00 USD |
| `7D` | `2544.70` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 0.00 USD | 2,170,000.00 USD | 1,830,000.00 USD | 1,350,000.00 USD |
| `1D` | `2545.50` | 717,750,000.00 USD | 717,750,000.00 USD | 0.00 USD | 590,640.00 USD | 800,740.00 USD | 12,050.00 USD |
| `7D` | `2547.50` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 938,680.00 USD | 2,240,000.00 USD |
| `1D` | `2548.10` | 720,690,000.00 USD | 720,690,000.00 USD | 0.00 USD | 1,370,000.00 USD | 832,850.00 USD | 743,470.00 USD |
| `7D` | `2550.30` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 0.00 USD | 2,860,000.00 USD | 2,690,000.00 USD | 1,800,000.00 USD |
| `1D` | `2550.70` | 724,150,000.00 USD | 724,150,000.00 USD | 0.00 USD | 1,380,000.00 USD | 1,460,000.00 USD | 618,500.00 USD |
| `7D` | `2553.10` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 0.00 USD | 2,120,000.00 USD | 788,360.00 USD | 1,670,000.00 USD |
| `1D` | `2553.30` | 724,930,000.00 USD | 724,930,000.00 USD | 0.00 USD | 468,780.00 USD | 220,540.00 USD | 90,660.00 USD |
| `1D` | `2555.90` | 726,700,000.00 USD | 726,700,000.00 USD | 0.00 USD | 1,010,000.00 USD | 398,720.00 USD | 366,540.00 USD |
| `7D` | `2555.90` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 0.00 USD | 3,290,000.00 USD | 255,750.00 USD | 5,860,000.00 USD |
| `1D` | `2558.50` | 728,310,000.00 USD | 728,310,000.00 USD | 0.00 USD | 722,170.00 USD | 141,030.00 USD | 745,190.00 USD |
| `7D` | `2558.70` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 0.00 USD | 3,850,000.00 USD | 1,200,000.00 USD | 2,340,000.00 USD |
| `1D` | `2561.10` | 732,550,000.00 USD | 732,550,000.00 USD | 0.00 USD | 1,640,000.00 USD | 1,270,000.00 USD | 1,320,000.00 USD |
| `7D` | `2561.50` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 0.00 USD | 2,780,000.00 USD | 2,030,000.00 USD | 426,110.00 USD |
| `1D` | `2563.70` | 734,270,000.00 USD | 734,270,000.00 USD | 0.00 USD | 440,660.00 USD | 975,880.00 USD | 309,770.00 USD |
| `7D` | `2564.30` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 0.00 USD | 1,800,000.00 USD | 2,150,000.00 USD | 1,460,000.00 USD |
| `1D` | `2566.30` | 734,420,000.00 USD | 734,420,000.00 USD | 0.00 USD | 121,690.00 USD | 11,860.00 USD | 11,930.00 USD |
| `7D` | `2567.10` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 0.00 USD | 575,630.00 USD | 1,510,000.00 USD | 2,700,000.00 USD |
| `1D` | `2568.90` | 734,580,000.00 USD | 734,580,000.00 USD | 0.00 USD | 162,270.00 USD | 0.00 USD | 3,730.00 USD |
| `7D` | `2569.90` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 0.00 USD | 125,250.00 USD | 290,680.00 USD | 1,180,000.00 USD |
| `1D` | `2571.50` | 735,530,000.00 USD | 735,530,000.00 USD | 0.00 USD | 770,210.00 USD | 169,470.00 USD | 5,200.00 USD |
| `7D` | `2572.70` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 890,480.00 USD | 1,790,000.00 USD |
| `1D` | `2574.10` | 736,220,000.00 USD | 736,220,000.00 USD | 0.00 USD | 121,300.00 USD | 191,750.00 USD | 381,370.00 USD |
| `7D` | `2575.50` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 0.00 USD | 2,180,000.00 USD | 440,740.00 USD | 1,060,000.00 USD |
| `1D` | `2576.70` | 736,870,000.00 USD | 736,870,000.00 USD | 0.00 USD | 439,020.00 USD | 209,570.00 USD | 3,450.00 USD |
| `7D` | `2578.30` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 0.00 USD | 734,040.00 USD | 1,480,000.00 USD | 1,750,000.00 USD |
| `1D` | `2579.30` | 738,210,000.00 USD | 738,210,000.00 USD | 0.00 USD | 308,690.00 USD | 314,010.00 USD | 710,940.00 USD |
| `7D` | `2581.10` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 0.00 USD | 3,270,000.00 USD | 864,580.00 USD | 1,220,000.00 USD |
| `1D` | `2581.90` | 740,960,000.00 USD | 740,960,000.00 USD | 0.00 USD | 1,580,000.00 USD | 935,910.00 USD | 234,280.00 USD |
| `7D` | `2583.90` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 0.00 USD | 740,840.00 USD | 1,260,000.00 USD | 3,550,000.00 USD |
| `1D` | `2584.50` | 741,960,000.00 USD | 741,960,000.00 USD | 0.00 USD | 287,140.00 USD | 153,810.00 USD | 554,400.00 USD |
| `7D` | `2586.70` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 0.00 USD | 1,900,000.00 USD | 2,190,000.00 USD | 1,530,000.00 USD |
| `1D` | `2587.10` | 743,990,000.00 USD | 743,990,000.00 USD | 0.00 USD | 1,260,000.00 USD | 335,670.00 USD | 439,060.00 USD |
| `7D` | `2589.50` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 0.00 USD | 2,840,000.00 USD | 446,810.00 USD | 2,140,000.00 USD |
| `1D` | `2589.70` | 745,300,000.00 USD | 745,300,000.00 USD | 0.00 USD | 445,920.00 USD | 99,440.00 USD | 763,970.00 USD |
| `1D` | `2592.30` | 747,540,000.00 USD | 747,540,000.00 USD | 0.00 USD | 971,410.00 USD | 349,000.00 USD | 919,490.00 USD |
| `7D` | `2592.30` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 0.00 USD | 2,340,000.00 USD | 1,280,000.00 USD | 1,550,000.00 USD |
| `1D` | `2594.90` | 750,640,000.00 USD | 750,640,000.00 USD | 0.00 USD | 886,830.00 USD | 1,220,000.00 USD | 995,020.00 USD |
| `7D` | `2595.10` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 0.00 USD | 452,020.00 USD | 569,790.00 USD | 752,870.00 USD |
| `1D` | `2597.50` | 751,600,000.00 USD | 751,600,000.00 USD | 0.00 USD | 179,030.00 USD | 442,330.00 USD | 339,490.00 USD |
| `7D` | `2597.90` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 0.00 USD | 2,280,000.00 USD | 1,630,000.00 USD | 2,420,000.00 USD |
| `1D` | `2600.10` | 752,890,000.00 USD | 752,890,000.00 USD | 0.00 USD | 258,900.00 USD | 724,120.00 USD | 303,400.00 USD |
| `7D` | `2600.70` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 0.00 USD | 496,060.00 USD | 1,960,000.00 USD | 1,610,000.00 USD |
| `1D` | `2602.70` | 753,770,000.00 USD | 753,770,000.00 USD | 0.00 USD | 107,010.00 USD | 453,880.00 USD | 318,170.00 USD |
| `7D` | `2603.50` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 2,040,000.00 USD | 1,580,000.00 USD | 1,660,000.00 USD |
| `1D` | `2605.30` | 754,750,000.00 USD | 754,750,000.00 USD | 0.00 USD | 0.00 USD | 644,330.00 USD | 336,530.00 USD |
| `7D` | `2606.30` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 1,480,000.00 USD | 229,360.00 USD | 342,240.00 USD |
| `1D` | `2607.90` | 755,430,000.00 USD | 755,430,000.00 USD | 0.00 USD | 187,520.00 USD | 497,320.00 USD | 0.00 USD |
| `7D` | `2609.10` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD |
| `1D` | `2610.50` | 755,730,000.00 USD | 755,730,000.00 USD | 0.00 USD | 0.00 USD | 294,600.00 USD | 2,870.00 USD |
| `7D` | `2611.90` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 724,220.00 USD | 608,060.00 USD | 43,560.00 USD |
| `1D` | `2613.10` | 756,740,000.00 USD | 756,740,000.00 USD | 0.00 USD | 555,320.00 USD | 250,240.00 USD | 205,180.00 USD |
| `7D` | `2614.70` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 0.00 USD | 1,110,000.00 USD | 1,000,000.00 USD | 409,160.00 USD |
| `7D` | `2617.50` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 0.00 USD | 1,550,000.00 USD | 209,240.00 USD | 392,750.00 USD |
| `1D` | `2618.30` | 757,040,000.00 USD | 757,040,000.00 USD | 0.00 USD | 295,510.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2620.30` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 0.00 USD | 47,360.00 USD | 1,120,000.00 USD | 268,500.00 USD |
| `7D` | `2623.10` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 0.00 USD | 631,440.00 USD | 410,460.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `30.21B` | Total OI Tokens: `12,865,653.6 ETH`
  * 1h OI Change: `-0.37%` | 4h OI Change: `-0.05%` | 24h OI Change: `+1.27%`
  * Exchange Breakdown: Binance=`8.97B` | Bybit=`2.13B` | OKX=`1.83B` | Hyperliquid=`2.58B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `1.18M` | Last 24h: `2.27M` | Last 3d: `7.66M` | Last 7d: `13.85M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0078%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0098%` | **USDT Bitget** | `0.0039%` |
| **CoinM Binance** | `0.0098%` | **CoinM OKX** | `0.0069%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `55.59%` | `44.41%` | `1.25` | 443,480,000.00 USD |
| `15M` | `Binance` | `48.6%` | `51.4%` | `0.95` | 123,120,000.00 USD |
| `15M` | `OKX` | `50.98%` | `49.02%` | `1.04` | 59,710,000.00 USD |
| `15M` | `Bybit` | `61.16%` | `38.84%` | `1.57` | 39,710,000.00 USD |
| `15M` | `KuCoin` | `44.62%` | `55.38%` | `0.81` | 1,600,000.00 USD |
| `15M` | `Gate` | `54.13%` | `45.87%` | `1.18` | 53,300,000.00 USD |
| `15M` | `Bitget` | `58.02%` | `41.98%` | `1.38` | 25,680,000.00 USD |
| `15M` | `BingX` | `77.52%` | `22.48%` | `3.45` | 7,930,000.00 USD |
| `15M` | `MEXC` | `58.72%` | `41.28%` | `1.42` | 31,830,000.00 USD |
| `15M` | `Bitunix` | `48.99%` | `51.01%` | `0.96` | 22,780,000.00 USD |
| `15M` | `Hyperliquid` | `89.09%` | `10.91%` | `8.17` | 24,040,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `62.16%` | `37.84%` | `1.64` | 3,280,000.00 USD |
| `15M` | `Crypto.com` | `53.46%` | `46.54%` | `1.15` | 6,570,000.00 USD |
| `15M` | `WhiteBIT` | `57.74%` | `42.26%` | `1.37` | 12,630,000.00 USD |
| `15M` | `HTX` | `52.73%` | `47.27%` | `1.12` | 1,310,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `63.15%` | `36.85%` | `1.71` | 13,510,000.00 USD |
| `15M` | `Bitfinex` | `35.08%` | `64.92%` | `0.54` | 225,350.00 USD |
| `15M` | `Kraken` | `34.5%` | `65.5%` | `0.53` | 2,520,000.00 USD |
| `15M` | `Aster` | `55.66%` | `44.34%` | `1.26` | 3,430,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `50.22%` | `49.78%` | `1.01` | 10,310,000.00 USD |
| `15M` | `Whale Positions` | `48.6%` | `51.4%` | `0.95` | 123,120,000.00 USD |
| `15M` | `Global Accounts` | `55.59%` | `44.41%` | `1.25` | 443,480,000.00 USD |
| `1H` | `ETH` | `47.59%` | `52.41%` | `0.91` | 3,020,000,000.00 USD |
| `1H` | `Binance` | `41.38%` | `58.62%` | `0.71` | 1,010,000,000.00 USD |
| `1H` | `OKX` | `47.47%` | `52.53%` | `0.90` | 393,950,000.00 USD |
| `1H` | `Bybit` | `49.19%` | `50.81%` | `0.97` | 266,380,000.00 USD |
| `1H` | `KuCoin` | `46.22%` | `53.78%` | `0.86` | 7,610,000.00 USD |
| `1H` | `Gate` | `49.14%` | `50.86%` | `0.97` | 350,980,000.00 USD |
| `1H` | `Bitget` | `47.67%` | `52.33%` | `0.91` | 157,250,000.00 USD |
| `1H` | `BingX` | `65.61%` | `34.39%` | `1.91` | 54,610,000.00 USD |
| `1H` | `MEXC` | `51.53%` | `48.47%` | `1.06` | 166,570,000.00 USD |
| `1H` | `Bitunix` | `49.59%` | `50.41%` | `0.98` | 124,550,000.00 USD |
| `1H` | `Hyperliquid` | `57.81%` | `42.19%` | `1.37` | 150,050,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `62.56%` | `37.44%` | `1.67` | 22,110,000.00 USD |
| `1H` | `Crypto.com` | `49.4%` | `50.6%` | `0.98` | 30,870,000.00 USD |
| `1H` | `WhiteBIT` | `63.99%` | `36.01%` | `1.78` | 75,230,000.00 USD |
| `1H` | `HTX` | `42.24%` | `57.76%` | `0.73` | 11,830,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `58.31%` | `41.69%` | `1.40` | 78,050,000.00 USD |
| `1H` | `Bitfinex` | `39.05%` | `60.95%` | `0.64` | 2,040,000.00 USD |
| `1H` | `Kraken` | `46.71%` | `53.29%` | `0.88` | 28,540,000.00 USD |
| `1H` | `Aster` | `36.19%` | `63.81%` | `0.57` | 34,600,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `47%` | `53%` | `0.89` | 55,660,000.00 USD |
| `1H` | `Whale Positions` | `41.38%` | `58.62%` | `0.71` | 1,010,000,000.00 USD |
| `1H` | `Global Accounts` | `47.59%` | `52.41%` | `0.91` | 3,020,000,000.00 USD |
| `4H` | `ETH` | `50.35%` | `49.65%` | `1.01` | 20,920,000,000.00 USD |
| `4H` | `Binance` | `49.55%` | `50.45%` | `0.98` | 6,600,000,000.00 USD |
| `4H` | `OKX` | `50.23%` | `49.77%` | `1.01` | 3,030,000,000.00 USD |
| `4H` | `Bybit` | `49.86%` | `50.14%` | `0.99` | 2,090,000,000.00 USD |
| `4H` | `KuCoin` | `47.68%` | `52.32%` | `0.91` | 83,750,000.00 USD |
| `4H` | `Gate` | `50.25%` | `49.75%` | `1.01` | 2,490,000,000.00 USD |
| `4H` | `Bitget` | `49.8%` | `50.2%` | `0.99` | 1,260,000,000.00 USD |
| `4H` | `BingX` | `50.26%` | `49.74%` | `1.01` | 385,240,000.00 USD |
| `4H` | `MEXC` | `54.66%` | `45.34%` | `1.21` | 1,150,000,000.00 USD |
| `4H` | `Bitunix` | `47.42%` | `52.58%` | `0.90` | 1,040,000,000.00 USD |
| `4H` | `Hyperliquid` | `53.63%` | `46.37%` | `1.16` | 972,710,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.39%` | `50.61%` | `0.98` | 133,450,000.00 USD |
| `4H` | `Crypto.com` | `47.99%` | `52.01%` | `0.92` | 138,950,000.00 USD |
| `4H` | `WhiteBIT` | `57.76%` | `42.24%` | `1.37` | 376,270,000.00 USD |
| `4H` | `HTX` | `47.39%` | `52.61%` | `0.90` | 84,100,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `51.71%` | `48.29%` | `1.07` | 396,300,000.00 USD |
| `4H` | `Bitfinex` | `65.77%` | `34.23%` | `1.92` | 29,010,000.00 USD |
| `4H` | `Kraken` | `52.72%` | `47.28%` | `1.12` | 160,940,000.00 USD |
| `4H` | `Aster` | `47.9%` | `52.1%` | `0.92` | 225,740,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.11%` | `49.89%` | `1.00` | 268,460,000.00 USD |
| `4H` | `Whale Positions` | `49.55%` | `50.45%` | `0.98` | 6,600,000,000.00 USD |
| `4H` | `Global Accounts` | `50.35%` | `49.65%` | `1.01` | 20,920,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `2357.75` | `2358.45` | `2357.75` | `2365.75` | `2355.25` | 136,642,531.53 USD | 60,568,643.70 USD | 76,073,887.82 USD | -15,505,244.12 USD | `-11.35%` | `1B / 5S` |
| `0:00 UTC` | `2364.75` | `2364.47` | `2364.75` | `2369.25` | `2356.75` | 211,703,599.24 USD | 122,647,689.31 USD | 89,055,909.93 USD | 33,591,779.37 USD | `+15.87%` | `9B / 0S` |
| `5:00 UTC` | `2370.25` | `2367.30` | `2370.25` | `2372.25` | `2362.75` | 152,368,912.49 USD | 65,939,044.63 USD | 86,429,867.86 USD | -20,490,823.24 USD | `-13.45%` | `0B / 0S` |
| `0:00 UTC` | `2367.25` | `2370.68` | `2367.25` | `2378.75` | `2362.25` | 227,963,041.65 USD | 108,724,843.75 USD | 119,238,197.91 USD | -10,513,354.16 USD | `-4.61%` | `6B / 3S` |
| `5:00 UTC` | `2360.25` | `2359.15` | `2360.25` | `2367.25` | `2354.75` | 178,447,053.53 USD | 59,723,171.00 USD | 118,723,882.53 USD | -59,000,711.54 USD | `-33.06%` | `0B / 9S` |
| `0:00 UTC` | `2358.25` | `2354.41` | `2358.25` | `2359.25` | `2350.25` | 125,220,561.61 USD | 53,594,674.80 USD | 71,625,886.81 USD | -18,031,212.02 USD | `-14.40%` | `0B / 1S` |
| `5:00 UTC` | `2353.75` | `2353.63` | `2353.75` | `2358.25` | `2350.75` | 70,925,128.95 USD | 26,607,996.94 USD | 44,317,132.01 USD | -17,709,135.06 USD | `-24.97%` | `0B / 2S` |
| `0:00 UTC` | `2350.75` | `2351.46` | `2350.75` | `2353.75` | `2348.75` | 91,943,279.10 USD | 36,371,657.16 USD | 55,571,621.93 USD | -19,199,964.77 USD | `-20.88%` | `0B / 3S` |
| `5:00 UTC` | `2350.25` | `2349.30` | `2350.25` | `2352.75` | `2346.75` | 77,932,643.01 USD | 38,640,268.57 USD | 39,292,374.44 USD | -652,105.87 USD | `-0.84%` | `1B / 1S` |
| `0:00 UTC` | `2351.75` | `2350.29` | `2351.75` | `2352.75` | `2347.75` | 9,300,360.56 USD | 4,321,657.63 USD | 4,978,702.93 USD | -657,045.30 USD | `-7.06%` | `1B / 2S` |

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
| `5m` | 5,420,000.00 USD | 93,710.00 USD | **`ACCUMULATION`** |
| `15m` | 5,380,000.00 USD | -945,210.00 USD | **`ACCUMULATION`** |
| `30m` | 2,750,000.00 USD | -36,980,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 2,590,000.00 USD | -63,200,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 3,170,000.00 USD | -284,770,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 24,690,000.00 USD | 54,560,000.00 USD | **`ACCUMULATION`** |
| `6h` | 20,390,000.00 USD | 66,400,000.00 USD | **`ACCUMULATION`** |
| `8h` | 19,240,000.00 USD | 32,950,000.00 USD | **`ACCUMULATION`** |
| `12h` | 28,250,000.00 USD | -54,900,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -5,880,000.00 USD | -206,510,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -9,040,000.00 USD | -835,800,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,000,000,000.00 USD | -7,960,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+5.42M` | 15m=`+5.38M` | 1h=`+2.59M` | 24h=`-5.88M`
* Futures Capital Netflows: 5m=`+93.71K` | 15m=`-945.21K` | 1h=`-63.20M` | 24h=`-206.51M`
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
  * `2026-10-29 23:01:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:45:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:02:06 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `2275.67` (Risk Distance: `18.01` pts)
  * +2.5R Take Profit: `2338.71`
  * Mathematical Lot Sizing: **`0.55 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2339.60` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2357.61` (Risk Distance: `18.01` pts)
  * +2.5R Take Profit: `2294.57`
  * Mathematical Lot Sizing: **`0.55 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2365.32`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
