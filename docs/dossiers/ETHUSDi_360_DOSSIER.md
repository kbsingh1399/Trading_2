# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-29 23:43:52 IST` (`2026-10-29 18:13:52 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2335.80` | **Live Ask Quote**: `2338.80` | **Mid Price**: `2337.30`
- **Spread Points**: `300.00` | **Spread BPS**: `12.84 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2323.76` | VWAP Z-Score: `+0.72` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `11.60` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `48.92` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2380.22` | Lower -3.00σ Band: `2267.30`
  * Upper +2.51σ Band: `2371.00` | Lower -2.51σ Band: `2276.52`
  * Upper +2.01σ Band: `2361.59` | Lower -2.01σ Band: `2285.93`
  * Upper +2.00σ Band: `2361.40` | Lower -2.00σ Band: `2286.12`
  * Upper +1.28σ Band: `2347.85` | Lower -1.28σ Band: `2299.67`
  * Upper +1.00σ Band: `2342.58` | Lower -1.00σ Band: `2304.94`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2344.88` | EMA-20=`2341.64` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2333.32` (Slope: `+0.0000`) | EMA-100=`2332.18`
  * Institutional Anchors: EMA-144=`2331.88` | EMA-200=`2330.53` (Slope: `+0.1182`) | EMA-233=`2329.18`
- **Range Boundaries**: 24H High=`2387.80` | 24H Low=`2288.80` | Weekly High=`2387.80` | Weekly Low=`2288.80`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2340.17` (Distance: `-0.06%`)
  * Point of Control (POC) = `2318.94` (Distance: `+0.85%`)
  * Value Area Low (VAL) = `2297.12` (Distance: `+1.81%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
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
  * Golden Pocket Zone (0.618 - 0.650): `2327.95` - `2346.65`
  * Optimal Trade Entry (OTE 0.705): `2341.97`
  * Structural Invalidation Anchor (0.786): `2356.00`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2334.57` | `2340.66` | `2334.56` | `2340.62` | `10,960` | 25,629,846.64 USD | 10,697,576.16 USD | `+41.74%` | -276,699,672.72 USD | `+1.93` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `2340.61` | `2341.50` | `2337.00` | `2338.88` | `11,179` | 26,145,341.24 USD | 1,456,706.48 USD | `+5.57%` | -275,242,966.23 USD | `+0.75` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `2338.87` | `2339.99` | `2338.41` | `2339.99` | `495` | 1,158,015.31 USD | 387,855.82 USD | `+33.49%` | -274,855,110.42 USD | `+0.59` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `2349.52` | `2353.10` | `2334.53` | `2338.55` | `73,514` | 172,182,390.30 USD | -20,793,862.11 USD | `-12.08%` | -287,611,760.49 USD | `-0.62` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `2338.55` | `2340.66` | `2330.81` | `2340.62` | `53,764` | 125,557,692.22 USD | 1,829,333.79 USD | `+1.46%` | -285,782,426.70 USD | `+0.11` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `2340.61` | `2341.50` | `2337.00` | `2339.46` | `11,645` | 27,234,200.74 USD | 1,795,753.49 USD | `+6.59%` | -283,986,673.21 USD | `+0.10` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `2368.02` | `2378.69` | `2350.25` | `2352.18` | `255,135` | 602,581,670.57 USD | -105,228,527.95 USD | `-17.46%` | -260,746,003.15 USD | `-2.06` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `2352.18` | `2353.79` | `2330.81` | `2340.62` | `199,552` | 467,616,004.62 USD | -38,816,598.96 USD | `-8.30%` | -299,562,602.11 USD | `-0.52` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2340.61` | `2341.50` | `2337.00` | `2340.48` | `11,971` | 27,997,930.19 USD | 2,508,809.09 USD | `+8.96%` | -297,053,793.02 USD | `+0.41` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `2309.10` | `2330.05` | `2308.88` | `2324.26` | `409,016` | 949,400,649.22 USD | -49,162,247.72 USD | `-5.18%` | -277,081,181.03 USD | `+0.30` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -173,041,008.80 USD | `+1.51` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2330.81` | `2339.81` | `466,351` | 1,097,475,990.82 USD | -142,214,556.95 USD | `-12.96%` | -315,255,565.74 USD | `-0.96` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2358.56` | `2360.38` | `2292.20` | `2308.04` | `812,683` | 1,883,052,517.85 USD | -183,572,583.45 USD | `-9.75%` | -193,002,187.18 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2308.03` | `2334.83` | `2303.75` | `2309.10` | `525,175` | 1,216,920,375.04 USD | -34,916,746.14 USD | `-2.87%` | -227,918,933.31 USD | `+0.53` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2309.10` | `2330.05` | `2308.88` | `2324.26` | `409,016` | 949,400,649.22 USD | -49,162,247.72 USD | `-5.18%` | -277,081,181.03 USD | `+0.30` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -173,041,008.80 USD | `+1.51` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2330.81` | `2339.81` | `466,351` | 1,097,475,990.82 USD | -142,214,556.95 USD | `-12.96%` | -315,255,565.74 USD | `-0.96` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`2337.30`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2338.30` | `600.7222` | 1,404,668.72 USD | 10,384,683.08 USD | `24 orders` | `-0.08%` | `-` |
| `BID` | `2338.40` | `150.5683` | 352,088.91 USD | 8,980,014.36 USD | `10 orders` | `-0.08%` | `-` |
| `BID` | `2338.50` | `230.5096` | 539,046.70 USD | 8,627,925.45 USD | `21 orders` | `-0.07%` | `-` |
| `BID` | `2338.60` | `306.9576` | 717,851.04 USD | 8,088,878.75 USD | `11 orders` | `-0.07%` | `-` |
| `BID` | `2338.70` | `92.6240` | 216,619.75 USD | 7,371,027.71 USD | `15 orders` | `-0.07%` | `-` |
| `BID` | `2338.80` | `203.6696` | 476,342.46 USD | 7,154,407.96 USD | `12 orders` | `-0.06%` | `-` |
| `BID` | `2338.90` | `368.8752` | 862,762.21 USD | 6,678,065.50 USD | `16 orders` | `-0.06%` | `-` |
| `BID` | `2339.00` | `138.9799` | 325,073.99 USD | 5,815,303.29 USD | `17 orders` | `-0.05%` | `-` |
| `BID` | `2339.10` | `281.0471` | 657,397.27 USD | 5,490,229.30 USD | `18 orders` | `-0.05%` | `-` |
| `BID` | `2339.20` | `111.8871` | 261,726.30 USD | 4,832,832.03 USD | `21 orders` | `-0.04%` | `-` |
| `BID` | `2339.30` | `624.3894` | 1,460,634.12 USD | 4,571,105.73 USD | `33 orders` | `-0.04%` | `-` |
| `BID` | `2339.40` | `196.9340` | 460,707.40 USD | 3,110,471.61 USD | `16 orders` | `-0.04%` | `-` |
| `BID` | `2339.50` | `151.7471` | 355,012.34 USD | 2,649,764.21 USD | `15 orders` | `-0.03%` | `-` |
| `BID` | `2339.60` | `398.3414` | 931,959.54 USD | 2,294,751.87 USD | `27 orders` | `-0.03%` | `-` |
| `BID` | `2339.70` | `142.5157` | 333,443.98 USD | 1,362,792.33 USD | `12 orders` | `-0.02%` | `-` |
| `BID` | `2339.80` | `154.8524` | 362,323.65 USD | 1,029,348.34 USD | `17 orders` | `-0.02%` | `-` |
| `BID` | `2339.90` | `22.0332` | 51,555.48 USD | 667,024.70 USD | `9 orders` | `-0.01%` | `-` |
| `BID` | `2340.00` | `86.5267` | 202,472.48 USD | 615,469.21 USD | `8 orders` | `-0.01%` | `-` |
| `BID` | `2340.10` | `19.9540` | 46,694.36 USD | 412,996.73 USD | `6 orders` | `-0.01%` | `-` |
| `BID` | `2340.20` | `156.5261` | 366,302.38 USD | 366,302.38 USD | `40 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2340.25` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,340.25` | `0.00%` | `-` |
| `ASK` | `2340.30` | `60.7602` | 142,197.10 USD | 142,197.10 USD | `11 orders` | `+0.00%` | `-` |
| `ASK` | `2340.40` | `20.3049` | 47,521.59 USD | 189,718.68 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `2340.50` | `0.9963` | 2,331.84 USD | 192,050.52 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `2340.60` | `75.4560` | 176,612.31 USD | 368,662.84 USD | `10 orders` | `+0.01%` | `-` |
| `ASK` | `2340.70` | `190.2097` | 445,223.84 USD | 813,886.68 USD | `11 orders` | `+0.02%` | `-` |
| `ASK` | `2340.80` | `92.2008` | 215,823.63 USD | 1,029,710.32 USD | `9 orders` | `+0.02%` | `-` |
| `ASK` | `2340.90` | `352.5009` | 825,169.36 USD | 1,854,879.67 USD | `13 orders` | `+0.03%` | `-` |
| `ASK` | `2341.00` | `338.3778` | 792,142.43 USD | 2,647,022.10 USD | `21 orders` | `+0.03%` | `-` |
| `ASK` | `2341.10` | `439.7827` | 1,029,575.28 USD | 3,676,597.38 USD | `23 orders` | `+0.04%` | `-` |
| `ASK` | `2341.20` | `149.2706` | 349,472.33 USD | 4,026,069.71 USD | `22 orders` | `+0.04%` | `-` |
| `ASK` | `2341.30` | `225.6708` | 528,363.04 USD | 4,554,432.75 USD | `22 orders` | `+0.04%` | `-` |
| `ASK` | `2341.40` | `194.8742` | 456,278.45 USD | 5,010,711.21 USD | `14 orders` | `+0.05%` | `-` |
| `ASK` | `2341.50` | `159.5392` | 373,561.04 USD | 5,384,272.24 USD | `33 orders` | `+0.05%` | `-` |
| `ASK` | `2341.60` | `358.8492` | 840,281.29 USD | 6,224,553.53 USD | `20 orders` | `+0.06%` | `-` |
| `ASK` | `2341.70` | `276.7739` | 648,121.44 USD | 6,872,674.97 USD | `22 orders` | `+0.06%` | `-` |
| `ASK` | `2341.80` | `281.8170` | 659,959.05 USD | 7,532,634.02 USD | `14 orders` | `+0.07%` | `-` |
| `ASK` | `2341.90` | `175.5635` | 411,152.16 USD | 7,943,786.18 USD | `17 orders` | `+0.07%` | `-` |
| `ASK` | `2342.00` | `278.0514` | 651,196.38 USD | 8,594,982.56 USD | `18 orders` | `+0.07%` | `-` |
| `ASK` | `2342.10` | `152.8525` | 357,995.84 USD | 8,952,978.40 USD | `15 orders` | `+0.08%` | `-` |
| `ASK` | `2342.20` | `495.4429` | 1,160,426.36 USD | 10,113,404.76 USD | `13 orders` | `+0.08%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:36:01 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-29 23:36:01 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1918.00` | `4,184.01` | 8,024,935.59 USD | `TRIGGER_STOP` | `0x6ea486a342` | `2026-10-29 23:36:01 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1918.99` | `8,092.45` | 15,529,329.85 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-29 23:36:01 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `8,500.00` | 16,371,850.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-29 23:36:01 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2040.68` | `7,964.66` | 16,253,321.14 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-29 23:36:01 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2115.20` | `7,500.00` | 15,864,017.53 USD | `AT_RISK_LIQ` | `0x524ed67d71` | `2026-10-29 23:36:01 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2171.14` | `48,499.51` | 105,299,308.58 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-29 23:36:01 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2180.20` | `44,734.81` | 97,531,035.84 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-29 23:36:01 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2250.00` | `6,500.00` | 14,625,000.00 USD | `TRIGGER_STOP` | `0x6eae4120a8` | `2026-10-29 23:36:01 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2292.00` | `2,500.00` | 5,730,000.00 USD | `TRIGGER_STOP` | `0x934de82f50` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2298.90` | `2,031.63` | 4,670,505.93 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2300.00` | `502.36` | 1,155,425.70 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xa5d0a11e20` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2302.90` | `5,457.62` | 12,568,356.55 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2303.00` | `908.97` | 2,093,354.23 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x0c4a3a7ac7` | `2026-10-29 23:36:01 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2307.20` | `599,999.99` | 1,384,319,976.93 USD | `TRIGGER_STOP` | `0x069604ebfb` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2310.60` | `1,308.67` | 3,023,822.38 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2311.00` | `1,015.35` | 2,346,465.99 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x674982e841` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2315.40` | `345.55` | 800,091.33 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2315.40` | `331.48` | 767,507.63 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2318.40` | `603.41` | 1,398,941.11 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 23:36:01 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2319.00` | `2,500.00` | 5,797,500.00 USD | `TRIGGER_STOP` | `0x524ed67d71` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2319.30` | `959.81` | 2,226,084.32 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2320.30` | `2,812.93` | 6,526,842.87 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2320.40` | `410.08` | 951,542.90 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x7b7f72a28f` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2322.90` | `435.69` | 1,012,052.69 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2324.70` | `603.78` | 1,403,602.72 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2326.20` | `669.42` | 1,557,208.29 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2326.50` | `1,721.16` | 4,004,277.34 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2328.70` | `1,289.65` | 3,003,197.24 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2328.70` | `603.48` | 1,405,326.20 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2330.30` | `859.18` | 2,002,141.33 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2330.90` | `1,433.72` | 3,341,868.90 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2331.10` | `454.70` | 1,059,951.87 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2331.20` | `435.37` | 1,014,934.54 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2332.10` | `643.90` | 1,501,630.79 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2333.50` | `402.34` | 938,860.39 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2333.90` | `381.52` | 890,419.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x76bf72092b` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2334.30` | `428.85` | 1,001,065.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2337.50` | `427.81` | 999,999.80 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x823ecdcdfc` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2340.60` | `427.72` | 1,001,120.26 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2341.20` | `402.35` | 941,979.48 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2342.30` | `380.16` | 890,459.31 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x76bf72092b` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2342.50` | `641.05` | 1,501,654.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2343.90` | `435.59` | 1,020,986.43 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2344.70` | `853.93` | 2,002,208.03 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2345.00` | `454.12` | 1,064,899.91 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2346.70` | `1,435.17` | 3,367,910.62 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2347.00` | `603.69` | 1,416,851.04 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2349.10` | `679.44` | 1,596,066.16 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2349.40` | `1,704.40` | 4,004,306.08 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2350.30` | `1,277.83` | 3,003,284.79 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2350.30` | `603.88` | 1,419,308.57 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2352.20` | `435.62` | 1,024,663.01 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2357.30` | `409.16` | 964,521.83 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x7b7f72a28f` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2357.40` | `2,810.10` | 6,624,529.98 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2358.40` | `957.13` | 2,257,299.64 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2358.90` | `603.90` | 1,424,542.07 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2361.50` | `338.81` | 800,091.31 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2361.50` | `325.01` | 767,507.81 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2364.90` | `5,463.46` | 12,920,534.43 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2366.10` | `1,320.07` | 3,123,426.85 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 23:36:01 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2379.30` | `1,948.50` | 4,636,057.01 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 23:36:01 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2440.00` | `4,002.10` | 9,765,127.17 USD | `TRIGGER_STOP` | `0xfb941d2344` | `2026-10-29 23:36:01 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2585.90` | `6,224.05` | 16,094,776.27 USD | `AT_RISK_LIQ` | `0x08bf75d170` | `2026-10-29 23:36:01 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2658.65` | `9,700.00` | 25,788,913.40 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-29 23:36:01 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2709.00` | `8,500.00` | 23,026,520.04 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-29 23:36:01 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 248,996,160.67 USD | `106,417.71` | `2322.74` | `2339.60` | `3817.44` | -1,815,148.51 USD | `-0.73%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 152,554,014.80 USD | `65,205.17` | `2375.30` | `2339.60` | `4362.23` | 2,328,248.30 USD | `+1.53%` | `5X Cross` |
| `6` | `0x77dd...e0e9` | `LONG` | 113,479,157.94 USD | `48,499.51` | `2610.31` | `2339.60` | `2171.17` | -13,119,725.92 USD | `-11.56%` | `10X Cross` |
| `7` | `0x0392...d7d9` | `LONG` | 104,661,569.43 USD | `44,734.81` | `2518.71` | `2339.60` | `2180.23` | -8,012,737.14 USD | `-7.66%` | `9X Cross` |
| `15` | `0xde8d...9524` | `LONG` | 70,830,541.79 USD | `30,282.40` | `2134.45` | `2339.60` | `1787.12` | 6,194,211.21 USD | `+8.75%` | `20X Cross` |
| `17` | `0x7fda...17d1` | `SHORT` | 65,524,238.59 USD | `28,014.98` | `2437.60` | `2339.60` | `3716.68` | 2,765,280.44 USD | `+4.22%` | `25X Cross` |
| `25` | `0xdf95...7d72` | `SHORT` | 52,997,252.43 USD | `22,650.33` | `2402.54` | `2339.60` | `3963.11` | 1,421,115.45 USD | `+2.68%` | `25X Cross` |
| `28` | `0xeced...6210` | `SHORT` | 43,742,009.85 USD | `18,687.58` | `2522.09` | `2339.60` | `3351.33` | 3,389,902.61 USD | `+7.75%` | `20X Cross` |
| `34` | `0xb695...a92d` | `SHORT` | 39,085,468.71 USD | `16,704.62` | `2557.74` | `2339.60` | `4026.78` | 3,640,696.34 USD | `+9.31%` | `20X Cross` |
| `35` | `0x6046...b21d` | `LONG` | 37,254,632.31 USD | `15,927.59` | `2410.19` | `2339.60` | `1553.43` | -1,133,987.34 USD | `-3.04%` | `6X Cross` |
| `38` | `0x45d2...4029` | `SHORT` | 32,640,210.00 USD | `13,950.00` | `2443.60` | `2339.60` | `4963.44` | 1,448,072.46 USD | `+4.44%` | `20X Cross` |
| `39` | `0x0622...8088` | `LONG` | 32,194,838.90 USD | `13,759.65` | `2342.49` | `2339.60` | `1617.36` | -37,084.69 USD | `-0.12%` | `5X Cross` |
| `45` | `0xbd1c...ff0e` | `LONG` | 28,077,600.00 USD | `12,000.00` | `2419.91` | `2339.60` | `1521.00` | -961,432.39 USD | `-3.42%` | `20X Cross` |
| `46` | `0x2371...0883` | `LONG` | 28,075,200.00 USD | `12,000.00` | `2421.77` | `2339.60` | `1280.10` | -986,094.85 USD | `-3.51%` | `20X Cross` |
| `50` | `0xa9de...e049` | `LONG` | 25,739,340.00 USD | `11,000.00` | `2481.81` | `2339.60` | `1644.74` | -1,560,639.46 USD | `-6.06%` | `20X Cross` |
| `51` | `0x6c93...59a4` | `LONG` | 25,737,800.00 USD | `11,000.00` | `2441.15` | `2339.60` | `1603.03` | -1,114,872.73 USD | `-4.33%` | `20X Cross` |
| `52` | `0x09dc...c094` | `LONG` | 25,734,500.00 USD | `11,000.00` | `2465.31` | `2339.60` | `1638.07` | -1,383,923.04 USD | `-5.38%` | `20X Cross` |
| `53` | `0x0c5d...36b3` | `LONG` | 25,727,900.00 USD | `11,000.00` | `2482.20` | `2339.60` | `1645.07` | -1,576,353.24 USD | `-6.13%` | `20X Cross` |
| `55` | `0xa61c...66b9` | `LONG` | 25,473,564.80 USD | `10,888.00` | `2398.32` | `2339.60` | `1404.52` | -639,392.59 USD | `-2.51%` | `10X Cross` |
| `59` | `0x4487...c92d` | `SHORT` | 24,953,784.03 USD | `10,664.92` | `2373.98` | `2339.60` | `2873.89` | 364,625.42 USD | `+1.46%` | `10X Cross` |
| `66` | `0xa2ce...3126` | `LONG` | 23,437,484.59 USD | `10,016.88` | `2162.83` | `2339.60` | `1451.77` | 1,772,682.54 USD | `+7.56%` | `10X Cross` |
| `67` | `0x15a4...dfdb` | `LONG` | 23,399,400.00 USD | `10,000.00` | `1761.94` | `2339.60` | `18.90` | 5,779,918.97 USD | `+24.70%` | `20X Cross` |
| `68` | `0x6646...6de5` | `LONG` | 23,399,000.00 USD | `10,000.00` | `1765.80` | `2339.60` | `1733.50` | 5,740,942.55 USD | `+24.53%` | `25X Cross` |
| `69` | `0xec7f...df39` | `LONG` | 23,395,000.00 USD | `10,000.00` | `2719.35` | `2339.60` | `1721.59` | -3,798,548.52 USD | `-16.24%` | `20X Cross` |
| `76` | `0xaeaa...2416` | `SHORT` | 22,694,120.00 USD | `9,700.00` | `2311.92` | `2339.60` | `2658.68` | -268,437.60 USD | `-1.18%` | `25X Cross` |
| `81` | `0xca49...53c8` | `SHORT` | 21,676,518.82 USD | `9,264.26` | `2549.47` | `2339.60` | `3717.92` | 1,942,505.92 USD | `+8.96%` | `25X Cross` |
| `84` | `0xba5d...a352` | `SHORT` | 21,192,983.60 USD | `9,054.12` | `2493.89` | `2339.60` | `2909.87` | 1,387,023.66 USD | `+6.54%` | `20X Cross` |
| `85` | `0xea00...a918` | `LONG` | 21,065,352.01 USD | `9,003.83` | `2003.01` | `2339.60` | `1207.44` | 3,030,573.15 USD | `+14.39%` | `5X Cross` |
| `90` | `0xecb6...2b00` | `SHORT` | 20,259,603.49 USD | `8,662.02` | `2327.63` | `2339.60` | `5654.31` | -97,535.16 USD | `-0.48%` | `15X Cross` |
| `93` | `0xb37f...66ca` | `SHORT` | 19,888,300.00 USD | `8,500.00` | `2308.30` | `2339.60` | `2709.03` | -267,745.81 USD | `-1.35%` | `25X Cross` |
| `102` | `0x9eec...daab` | `LONG` | 18,934,719.42 USD | `8,092.45` | `1658.44` | `2339.60` | `1918.99` | 5,513,854.90 USD | `+29.12%` | `15X Cross` |
| `108` | `0x218a...7da2` | `SHORT` | 18,706,815.37 USD | `7,997.78` | `2208.16` | `2339.60` | `2877.25` | -1,046,420.16 USD | `-5.59%` | `10X Cross` |
| `110` | `0x5f91...65aa` | `LONG` | 18,629,330.15 USD | `7,964.66` | `1626.99` | `2339.60` | `2040.71` | 5,670,887.09 USD | `+30.44%` | `16X Cross` |
| `113` | `0xcf53...ee11` | `SHORT` | 17,787,927.11 USD | `7,603.63` | `1862.69` | `2339.60` | `3984.29` | -3,624,663.17 USD | `-20.38%` | `7X Cross` |
| `114` | `0x524e...0de0` | `LONG` | 17,547,000.00 USD | `7,500.00` | `2320.35` | `2339.60` | `2115.23` | 144,313.78 USD | `+0.82%` | `10X Cross` |
| `119` | `0x939f...04d2` | `LONG` | 16,896,498.37 USD | `7,223.81` | `2500.18` | `2339.60` | `1787.46` | -1,164,391.80 USD | `-6.89%` | `25X Cross` |
| `121` | `0xec0b...b078` | `LONG` | 16,395,446.31 USD | `7,007.80` | `2065.97` | `2339.60` | `1002.71` | 1,917,516.72 USD | `+11.70%` | `25X Cross` |
| `122` | `0x1ee7...edf5` | `LONG` | 16,377,200.00 USD | `7,000.00` | `2330.22` | `2339.60` | `2153.93` | 65,637.80 USD | `+0.40%` | `25X Cross` |
| `129` | `0x418a...8888` | `SHORT` | 15,731,693.56 USD | `6,724.38` | `2494.55` | `2339.60` | `2958.80` | 1,042,629.61 USD | `+6.63%` | `25X Cross` |
| `130` | `0x4ff9...38d3` | `LONG` | 15,356,708.91 USD | `6,564.10` | `2447.40` | `2339.60` | `1670.69` | -708,313.84 USD | `-4.61%` | `3X Isolated` |
| `132` | `0xf78c...c581` | `LONG` | 15,207,918.22 USD | `6,500.22` | `2521.53` | `2339.60` | `1914.17` | -1,182,622.73 USD | `-7.78%` | `20X Cross` |
| `139` | `0x799f...5f4c` | `LONG` | 14,766,251.54 USD | `6,310.90` | `2390.33` | `2339.60` | `1715.48` | -318,913.07 USD | `-2.16%` | `20X Cross` |
| `141` | `0x08bf...7872` | `SHORT` | 14,563,026.11 USD | `6,224.05` | `2258.00` | `2339.60` | `2585.93` | -509,110.00 USD | `-3.50%` | `20X Cross` |
| `149` | `0xd9e7...4aff` | `LONG` | 14,039,640.00 USD | `6,000.00` | `2480.18` | `2339.60` | `1408.46` | -841,484.33 USD | `-5.99%` | `20X Cross` |
| `156` | `0x0c4a...1b19` | `LONG` | 13,350,090.75 USD | `5,706.39` | `2382.15` | `2339.60` | `2185.22` | -243,380.42 USD | `-1.82%` | `25X Isolated` |
| `174` | `0x645b...87b8` | `SHORT` | 11,871,730.75 USD | `5,073.52` | `2421.68` | `2339.60` | `6165.62` | 414,723.38 USD | `+3.49%` | `10X Cross` |
| `179` | `0x45ab...6cbc` | `LONG` | 11,510,130.59 USD | `4,920.96` | `2727.66` | `2339.60` | `1361.30` | -1,912,613.21 USD | `-16.62%` | `7X Cross` |
| `184` | `0xfb18...eb17` | `SHORT` | 11,400,550.09 USD | `4,872.45` | `2315.54` | `2339.60` | `2708.96` | -118,177.05 USD | `-1.04%` | `25X Cross` |
| `186` | `0x64b7...9da9` | `LONG` | 11,363,060.99 USD | `4,856.84` | `2604.61` | `2339.60` | `1402.26` | -1,287,153.42 USD | `-11.33%` | `25X Cross` |
| `194` | `0x5559...d43b` | `SHORT` | 11,128,579.85 USD | `4,755.93` | `2262.69` | `2339.60` | `2872.16` | -367,373.97 USD | `-3.30%` | `25X Cross` |
| `209` | `0xe091...6705` | `SHORT` | 10,525,050.47 USD | `4,500.00` | `2467.33` | `2339.60` | `2572.98` | 577,958.04 USD | `+5.49%` | `20X Cross` |
| `219` | `0xfe7c...b7ae` | `SHORT` | 10,297,640.70 USD | `4,402.58` | `2440.17` | `2339.60` | `4195.86` | 445,447.17 USD | `+4.33%` | `25X Cross` |
| `228` | `0xc179...e0c8` | `LONG` | 10,078,682.86 USD | `4,309.16` | `2342.89` | `2339.60` | `886.03` | -17,195.93 USD | `-0.17%` | `10X Cross` |
| `234` | `0x12d2...f97f` | `LONG` | 9,976,851.50 USD | `4,264.34` | `2623.90` | `2339.60` | `1834.95` | -1,212,382.92 USD | `-12.15%` | `20X Cross` |
| `240` | `0x28bb...fca6` | `SHORT` | 9,848,813.38 USD | `4,209.61` | `1896.10` | `2339.60` | `3046.07` | -1,866,930.82 USD | `-18.96%` | `20X Cross` |
| `241` | `0x6ea4...0ea7` | `SHORT` | 9,788,496.78 USD | `4,184.01` | `2602.13` | `2339.60` | `3425.99` | 1,098,849.89 USD | `+11.23%` | `20X Cross` |
| `250` | `0x5e9e...35ee` | `SHORT` | 9,376,878.83 USD | `4,007.56` | `1796.39` | `2339.60` | `2586.49` | -2,177,728.74 USD | `-23.22%` | `20X Cross` |
| `251` | `0xfb94...0ddf` | `SHORT` | 9,360,914.94 USD | `4,002.10` | `2382.44` | `2339.60` | `5105.38` | 173,869.21 USD | `+1.86%` | `20X Cross` |
| `252` | `0x8cc9...2b6a` | `SHORT` | 9,359,200.00 USD | `4,000.00` | `1791.18` | `2339.60` | `3848.75` | -2,194,453.33 USD | `-23.45%` | `25X Cross` |
| `253` | `0x95fe...f8fa` | `LONG` | 9,358,400.00 USD | `4,000.00` | `2341.35` | `2339.60` | `2258.99` | -7,016.51 USD | `-0.07%` | `20X Isolated` |
| `254` | `0x3dc9...54b0` | `SHORT` | 9,357,675.19 USD | `3,999.69` | `2480.32` | `2339.60` | `5877.88` | 562,861.36 USD | `+6.01%` | `20X Cross` |
| `256` | `0x77ee...2902` | `SHORT` | 9,316,424.98 USD | `3,982.23` | `2476.53` | `2339.60` | `4317.64` | 545,696.60 USD | `+5.86%` | `25X Cross` |
| `268` | `0xf02d...5eb3` | `LONG` | 9,022,234.87 USD | `3,855.99` | `2513.67` | `2339.60` | `323.92` | -670,477.44 USD | `-7.43%` | `20X Cross` |
| `270` | `0x4b67...f4e7` | `LONG` | 8,936,949.20 USD | `3,820.84` | `2591.51` | `2339.60` | `1587.34` | -964,824.34 USD | `-10.80%` | `20X Cross` |
| `291` | `0x382b...3e39` | `SHORT` | 8,354,302.64 USD | `3,571.89` | `2299.50` | `2339.60` | `3762.23` | -140,706.94 USD | `-1.68%` | `25X Cross` |
| `292` | `0x8ae4...3d60` | `LONG` | 8,324,404.92 USD | `3,558.20` | `2482.21` | `2339.60` | `330.06` | -507,793.11 USD | `-6.10%` | `10X Cross` |
| `320` | `0x9c06...0560` | `SHORT` | 7,730,707.56 USD | `3,303.58` | `2270.55` | `2339.60` | `3301.77` | -229,743.61 USD | `-2.97%` | `25X Cross` |
| `328` | `0x984e...14c2` | `SHORT` | 7,281,739.32 USD | `3,111.99` | `2357.50` | `2339.60` | `2434.95` | 54,783.44 USD | `+0.75%` | `20X Cross` |
| `333` | `0x9c2a...f6a8` | `SHORT` | 7,155,615.36 USD | `3,058.48` | `2543.83` | `2339.60` | `2589.02` | 624,645.26 USD | `+8.73%` | `20X Cross` |
| `338` | `0x39b4...5c34` | `SHORT` | 7,020,932.55 USD | `3,000.91` | `2329.97` | `2339.60` | `2405.88` | -28,888.80 USD | `-0.41%` | `25X Cross` |
| `339` | `0x4a20...3c26` | `LONG` | 7,019,400.00 USD | `3,000.00` | `2428.72` | `2339.60` | `212.04` | -266,760.28 USD | `-3.80%` | `20X Cross` |
| `340` | `0x007d...67a0` | `LONG` | 7,019,400.00 USD | `3,000.00` | `2400.00` | `2339.60` | `1490.85` | -180,600.00 USD | `-2.57%` | `25X Cross` |
| `378` | `0xf517...c032` | `SHORT` | 6,405,989.27 USD | `2,738.07` | `2053.90` | `2339.60` | `5573.75` | -782,247.36 USD | `-12.21%` | `25X Cross` |
| `393` | `0xc619...10f5` | `LONG` | 6,083,480.00 USD | `2,600.00` | `2318.40` | `2339.60` | `1858.18` | 55,631.09 USD | `+0.91%` | `25X Cross` |
| `394` | `0xbb34...1696` | `LONG` | 6,081,400.00 USD | `2,600.00` | `2318.80` | `2339.60` | `1975.05` | 52,499.15 USD | `+0.86%` | `25X Cross` |
| `398` | `0x8328...f54a` | `SHORT` | 6,026,319.12 USD | `2,576.45` | `2292.01` | `2339.60` | `3280.23` | -121,047.83 USD | `-2.01%` | `25X Cross` |
| `400` | `0xed48...7c9b` | `SHORT` | 5,969,135.14 USD | `2,551.13` | `2460.02` | `2339.60` | `3237.00` | 306,711.27 USD | `+5.14%` | `20X Cross` |
| `402` | `0x934d...92c9` | `LONG` | 5,849,500.00 USD | `2,500.00` | `2343.98` | `2339.60` | `2158.20` | -10,464.51 USD | `-0.18%` | `25X Cross` |
| `420` | `0xfbe2...c8ea` | `SHORT` | 5,625,058.90 USD | `2,404.08` | `2041.57` | `2339.60` | `2697.48` | -716,966.17 USD | `-12.75%` | `20X Cross` |
| `428` | `0x1c98...7fc7` | `LONG` | 5,516,551.53 USD | `2,358.00` | `2467.15` | `2339.60` | `1897.21` | -301,019.96 USD | `-5.46%` | `10X Cross` |
| `444` | `0x6859...7e1e` | `SHORT` | 5,204,625.03 USD | `2,224.58` | `2200.39` | `2339.60` | `3652.14` | -309,672.30 USD | `-5.95%` | `25X Cross` |
| `455` | `0xd507...c948` | `SHORT` | 5,081,610.97 USD | `2,172.00` | `2387.49` | `2339.60` | `2707.41` | 104,030.06 USD | `+2.05%` | `5X Isolated` |
| `460` | `0xb829...3a81` | `LONG` | 5,039,074.78 USD | `2,153.91` | `2537.61` | `2339.60` | `780.02` | -426,721.95 USD | `-8.47%` | `20X Cross` |
| `490` | `0x3440...32c5` | `SHORT` | 4,680,922.46 USD | `2,000.57` | `2198.21` | `2339.60` | `3523.72` | -283,259.32 USD | `-6.05%` | `25X Cross` |
| `492` | `0xf929...d1f9` | `SHORT` | 4,679,880.00 USD | `2,000.00` | `2423.37` | `2339.60` | `2548.81` | 166,860.34 USD | `+3.57%` | `25X Cross` |
| `505` | `0xd4c1...3d1d` | `SHORT` | 4,583,198.37 USD | `1,958.80` | `2336.05` | `2339.60` | `4728.35` | -7,330.92 USD | `-0.16%` | `12X Cross` |
| `507` | `0x0514...bdfe` | `SHORT` | 4,562,220.00 USD | `1,950.00` | `1988.74` | `2339.60` | `2936.43` | -684,160.37 USD | `-15.00%` | `25X Cross` |
| `515` | `0x8376...9a1e` | `SHORT` | 4,468,650.14 USD | `1,910.50` | `2477.72` | `2339.60` | `3155.63` | 265,038.03 USD | `+5.93%` | `20X Cross` |
| `535` | `0x7a6d...f79c` | `SHORT` | 4,270,558.98 USD | `1,825.07` | `2433.80` | `2339.60` | `2784.05` | 171,309.90 USD | `+4.01%` | `25X Cross` |
| `541` | `0x541e...071d` | `SHORT` | 4,223,339.00 USD | `1,805.00` | `2648.19` | `2339.60` | `3019.01` | 556,645.84 USD | `+13.18%` | `25X Cross` |
| `542` | `0x7265...91a5` | `LONG` | 4,216,266.28 USD | `1,801.87` | `2533.96` | `2339.60` | `1988.14` | -349,600.17 USD | `-8.29%` | `20X Cross` |
| `543` | `0x739c...cfb2` | `SHORT` | 4,211,280.00 USD | `1,800.00` | `2427.60` | `2339.60` | `2668.73` | 158,416.38 USD | `+3.76%` | `25X Cross` |
| `549` | `0xa445...329d` | `LONG` | 4,157,238.01 USD | `1,776.75` | `2398.85` | `2339.60` | `1787.88` | -104,931.34 USD | `-2.52%` | `25X Cross` |
| `556` | `0x91a9...3f70` | `SHORT` | 4,135,196.21 USD | `1,767.48` | `2156.23` | `2339.60` | `3634.44` | -324,092.13 USD | `-7.84%` | `4X Cross` |
| `560` | `0x3453...b323` | `SHORT` | 4,094,588.00 USD | `1,750.12` | `2328.82` | `2339.60` | `2400.43` | -18,855.87 USD | `-0.46%` | `25X Cross` |
| `585` | `0xfeec...4e9c` | `SHORT` | 3,958,494.23 USD | `1,691.81` | `2566.49` | `2339.60` | `2650.55` | 383,530.28 USD | `+9.69%` | `10X Cross` |
| `586` | `0x936c...bb0f` | `SHORT` | 3,951,187.50 USD | `1,688.69` | `2434.60` | `2339.60` | `8520.88` | 160,099.60 USD | `+4.05%` | `20X Cross` |
| `610` | `0xeee0...0b53` | `LONG` | 3,829,232.80 USD | `1,637.12` | `2468.64` | `2339.60` | `115.84` | -212,243.26 USD | `-5.54%` | `7X Cross` |
| `614` | `0x27b8...12fc` | `LONG` | 3,808,986.97 USD | `1,628.12` | `2468.73` | `2339.60` | `419.72` | -210,407.66 USD | `-5.52%` | `10X Cross` |
| `615` | `0x982b...4606` | `LONG` | 3,805,125.66 USD | `1,626.82` | `2575.24` | `2339.60` | `1548.41` | -384,327.41 USD | `-10.10%` | `5X Isolated` |
| `622` | `0x73d7...8be1` | `LONG` | 3,747,108.98 USD | `1,601.47` | `2410.40` | `2339.60` | `2037.42` | -113,069.94 USD | `-3.02%` | `25X Cross` |
| `643` | `0xfc27...9d9d` | `SHORT` | 3,618,812.83 USD | `1,546.63` | `2402.17` | `2339.60` | `11619.71` | 96,465.59 USD | `+2.67%` | `25X Cross` |
| `648` | `0xe170...9300` | `SHORT` | 3,588,309.34 USD | `1,533.40` | `2076.39` | `2339.60` | `3217.98` | -404,359.84 USD | `-11.27%` | `25X Cross` |
| `661` | `0x2e2b...2fab` | `LONG` | 3,526,659.23 USD | `1,507.38` | `2245.53` | `2339.60` | `1082.22` | 141,786.13 USD | `+4.02%` | `25X Cross` |
| `664` | `0x251f...6e5d` | `LONG` | 3,509,400.00 USD | `1,500.00` | `2346.68` | `2339.60` | `1599.45` | -10,630.49 USD | `-0.30%` | `20X Cross` |
| `678` | `0xad54...6203` | `LONG` | 3,412,054.41 USD | `1,458.18` | `2627.45` | `2339.60` | `2146.47` | -419,252.27 USD | `-12.29%` | `10X Isolated` |
| `683` | `0xef70...a84c` | `SHORT` | 3,375,442.46 USD | `1,442.74` | `2424.73` | `2339.60` | `3457.39` | 122,828.37 USD | `+3.64%` | `25X Cross` |
| `692` | `0x4b5f...0dd8` | `LONG` | 3,350,206.13 USD | `1,431.96` | `2339.45` | `2339.60` | `2148.70` | 213.18 USD | `+0.01%` | `10X Cross` |
| `693` | `0xbadb...9ee6` | `LONG` | 3,341,808.71 USD | `1,428.16` | `1936.00` | `2339.60` | `1038.93` | 576,887.06 USD | `+17.26%` | `20X Cross` |
| `757` | `0x880a...311c` | `SHORT` | 3,088,661.94 USD | `1,320.22` | `2425.76` | `2339.60` | `8176.87` | 113,887.21 USD | `+3.69%` | `9X Cross` |
| `766` | `0x023a...2355` | `LONG` | 3,071,383.83 USD | `1,312.78` | `2341.02` | `2339.60` | `0.000000` | -1,871.86 USD | `-0.06%` | `25X Cross` |
| `769` | `0x29de...3e93` | `LONG` | 3,064,876.00 USD | `1,310.00` | `2352.60` | `2339.60` | `1922.23` | -17,032.82 USD | `-0.56%` | `5X Isolated` |
| `804` | `0xc435...c905` | `SHORT` | 2,918,947.20 USD | `1,248.00` | `2704.38` | `2339.60` | `4825.56` | 456,123.15 USD | `+15.63%` | `20X Cross` |
| `809` | `0x4202...aaf5` | `SHORT` | 2,882,877.88 USD | `1,232.10` | `2321.73` | `2339.60` | `2733.54` | -22,253.57 USD | `-0.77%` | `5X Isolated` |
| `813` | `0x7178...0854` | `LONG` | 2,851,719.57 USD | `1,218.63` | `2461.81` | `2339.60` | `1040.79` | -148,326.83 USD | `-5.20%` | `10X Cross` |
| `865` | `0x07fd...689d` | `LONG` | 2,657,550.70 USD | `1,135.90` | `2423.84` | `2339.60` | `0.000000` | -95,692.49 USD | `-3.60%` | `25X Cross` |
| `898` | `0x2f80...f203` | `SHORT` | 2,547,577.70 USD | `1,088.94` | `1984.00` | `2339.60` | `3074.12` | -387,110.51 USD | `-15.20%` | `20X Cross` |
| `908` | `0x6f11...0389` | `SHORT` | 2,524,428.40 USD | `1,079.00` | `2333.39` | `2339.60` | `3199.68` | -6,699.49 USD | `-0.27%` | `25X Cross` |
| `911` | `0x2b61...2f6c` | `SHORT` | 2,518,699.15 USD | `1,076.60` | `2681.75` | `2339.60` | `6342.89` | 368,473.59 USD | `+14.63%` | `10X Cross` |
| `954` | `0xb15b...dbae` | `SHORT` | 2,398,630.06 USD | `1,025.14` | `2338.37` | `2339.60` | `2381.06` | -1,456.34 USD | `-0.06%` | `25X Cross` |
| `955` | `0x1b2a...f7a6` | `LONG` | 2,398,335.75 USD | `1,025.37` | `2737.51` | `2339.60` | `943.68` | -408,624.19 USD | `-17.04%` | `10X Cross` |
| `960` | `0x6749...ce07` | `SHORT` | 2,375,707.97 USD | `1,015.35` | `2318.56` | `2339.60` | `5889.26` | -21,564.62 USD | `-0.91%` | `20X Cross` |
| `967` | `0x001a...fef6` | `SHORT` | 2,356,939.04 USD | `1,007.33` | `2022.19` | `2339.60` | `3033.69` | -319,931.08 USD | `-13.57%` | `10X Cross` |
| `969` | `0x02aa...1806` | `SHORT` | 2,356,211.39 USD | `1,007.10` | `2654.68` | `2339.60` | `3613.68` | 317,320.71 USD | `+13.47%` | `20X Cross` |
| `972` | `0xdb3a...cf3b` | `LONG` | 2,347,122.05 USD | `1,003.22` | `2705.01` | `2339.60` | `0.000000` | -366,584.85 USD | `-15.62%` | `4X Cross` |
| `978` | `0x2828...93a0` | `LONG` | 2,339,940.00 USD | `1,000.00` | `2393.30` | `2339.60` | `2266.85` | -53,369.16 USD | `-2.28%` | `25X Cross` |
| `979` | `0x5272...fcd9` | `SHORT` | 2,339,800.00 USD | `1,000.00` | `2241.82` | `2339.60` | `2880.75` | -97,975.51 USD | `-4.19%` | `5X Cross` |
| `980` | `0xdf60...d3c7` | `LONG` | 2,339,600.00 USD | `1,000.00` | `2736.24` | `2339.60` | `2246.08` | -396,642.88 USD | `-16.95%` | `10X Isolated` |
| `981` | `0xfe82...ce65` | `SHORT` | 2,339,600.00 USD | `1,000.00` | `2300.50` | `2339.60` | `2718.42` | -39,092.07 USD | `-1.67%` | `25X Cross` |
| `982` | `0x5986...89d9` | `LONG` | 2,339,500.00 USD | `1,000.00` | `2346.34` | `2339.60` | `1230.06` | -6,849.54 USD | `-0.29%` | `25X Cross` |
| `983` | `0x4044...794c` | `LONG` | 2,339,000.00 USD | `1,000.00` | `2332.68` | `2339.60` | `0.000000` | 6,310.16 USD | `+0.27%` | `25X Cross` |
| `1011` | `0xb002...ed8a` | `SHORT` | 2,251,951.78 USD | `962.78` | `2299.66` | `2339.60` | `4193.01` | -37,873.87 USD | `-1.68%` | `25X Cross` |
| `1020` | `0x2e30...4cb5` | `SHORT` | 2,232,152.82 USD | `953.99` | `2340.09` | `2339.60` | `7201.25` | 284.45 USD | `+0.01%` | `2X Cross` |
| `1032` | `0xc8fe...afa4` | `LONG` | 2,190,735.46 USD | `936.37` | `2331.34` | `2339.60` | `2145.81` | 7,731.23 USD | `+0.35%` | `10X Isolated` |
| `1051` | `0x9606...4e5d` | `SHORT` | 2,136,503.58 USD | `913.00` | `2478.70` | `2339.60` | `3921.83` | 126,550.03 USD | `+5.92%` | `20X Cross` |
| `1058` | `0xaeea...bfa7` | `LONG` | 2,126,284.59 USD | `908.75` | `2339.31` | `2339.60` | `2286.72` | 442.49 USD | `+0.02%` | `23X Isolated` |
| `1079` | `0x60f7...d1ee` | `LONG` | 2,082,422.00 USD | `890.00` | `2343.49` | `2339.60` | `2265.73` | -3,287.96 USD | `-0.16%` | `25X Cross` |
| `1172` | `0xcd27...52a8` | `LONG` | 1,958,732.54 USD | `837.21` | `2553.56` | `2339.60` | `1404.23` | -179,132.24 USD | `-9.15%` | `2X Cross` |
| `1178` | `0xbef3...0d3e` | `LONG` | 1,943,692.63 USD | `830.99` | `2332.88` | `2339.60` | `2110.69` | 5,081.38 USD | `+0.26%` | `20X Cross` |
| `1183` | `0x6a41...a3b9` | `LONG` | 1,932,813.78 USD | `826.06` | `2332.61` | `2339.60` | `2112.87` | 5,938.93 USD | `+0.31%` | `20X Cross` |
| `1204` | `0x2577...4897` | `LONG` | 1,902,006.11 USD | `813.21` | `2356.56` | `2339.60` | `0.000000` | -14,364.90 USD | `-0.76%` | `15X Cross` |
| `1221` | `0x3fc5...c0c1` | `SHORT` | 1,881,642.48 USD | `804.26` | `2702.11` | `2339.60` | `4867.88` | 291,559.04 USD | `+15.49%` | `25X Cross` |
| `1224` | `0xf83f...625f` | `SHORT` | 1,879,055.06 USD | `803.05` | `2601.00` | `2339.60` | `6032.39` | 209,681.40 USD | `+11.16%` | `20X Cross` |
| `1229` | `0x04a9...95aa` | `LONG` | 1,871,680.00 USD | `800.00` | `2595.13` | `2339.60` | `1858.50` | -204,426.74 USD | `-10.92%` | `5X Cross` |
| `1230` | `0x7737...bf66` | `SHORT` | 1,871,593.03 USD | `799.79` | `2494.83` | `2339.60` | `25367.68` | 123,753.00 USD | `+6.61%` | `15X Cross` |
| `1264` | `0x458d...ab3b` | `LONG` | 1,812,133.23 USD | `774.75` | `2740.41` | `2339.60` | `1887.98` | -310,995.95 USD | `-17.16%` | `3X Isolated` |
| `1297` | `0x7743...e4fe` | `SHORT` | 1,756,001.29 USD | `750.56` | `2326.87` | `2339.60` | `5895.10` | -9,547.15 USD | `-0.54%` | `25X Cross` |
| `1300` | `0x5f10...d49d` | `SHORT` | 1,754,850.00 USD | `750.00` | `2350.92` | `2339.60` | `2842.52` | 8,346.61 USD | `+0.48%` | `25X Cross` |
| `1326` | `0x4b1c...bc38` | `SHORT` | 1,707,086.40 USD | `729.84` | `2529.31` | `2339.60` | `4461.99` | 138,900.68 USD | `+8.14%` | `10X Cross` |
| `1341` | `0x51a0...3543` | `SHORT` | 1,695,147.35 USD | `724.55` | `2627.71` | `2339.60` | `7698.91` | 208,749.40 USD | `+12.31%` | `20X Cross` |
| `1349` | `0xa189...94d7` | `SHORT` | 1,684,606.86 USD | `719.98` | `2691.84` | `2339.60` | `3051.93` | 253,465.80 USD | `+15.05%` | `25X Cross` |
| `1354` | `0x3ee5...4fab` | `SHORT` | 1,673,132.96 USD | `715.17` | `2759.35` | `2339.60` | `3449.91` | 300,267.01 USD | `+17.95%` | `20X Cross` |
| `1356` | `0x3bca...66f3` | `SHORT` | 1,672,058.78 USD | `714.68` | `2347.84` | `2339.60` | `13124.00` | 5,895.23 USD | `+0.35%` | `25X Cross` |
| `1369` | `0x2f93...4404` | `LONG` | 1,655,341.82 USD | `707.47` | `1700.45` | `2339.60` | `1369.61` | 452,315.44 USD | `+27.32%` | `4X Isolated` |
| `1373` | `0x5605...fe0f` | `SHORT` | 1,642,664.95 USD | `702.14` | `2566.90` | `2339.60` | `3053.40` | 159,667.70 USD | `+9.72%` | `20X Cross` |
| `1378` | `0xaa53...9cb7` | `LONG` | 1,637,860.00 USD | `700.00` | `2394.46` | `2339.60` | `1942.58` | -38,262.07 USD | `-2.34%` | `20X Cross` |
| `1431` | `0xdbd1...29dd` | `SHORT` | 1,592,775.78 USD | `680.70` | `3030.57` | `2339.60` | `4067.68` | 470,145.34 USD | `+29.52%` | `6X Cross` |
| `1435` | `0x71e5...be04` | `LONG` | 1,585,604.78 USD | `677.67` | `2727.27` | `2339.60` | `1471.76` | -262,580.83 USD | `-16.56%` | `20X Cross` |
| `1439` | `0x0b23...f37b` | `LONG` | 1,579,162.50 USD | `675.00` | `2238.15` | `2339.60` | `576.65` | 68,405.86 USD | `+4.33%` | `5X Cross` |
| `1463` | `0x0cac...6170` | `SHORT` | 1,550,117.50 USD | `662.50` | `2146.55` | `2339.60` | `2835.39` | -128,022.51 USD | `-8.26%` | `20X Cross` |
| `1469` | `0x0082...1ae3` | `LONG` | 1,544,136.00 USD | `660.00` | `2448.58` | `2339.60` | `2244.96` | -71,932.64 USD | `-4.66%` | `25X Cross` |
| `1504` | `0xffb2...5ed6` | `SHORT` | 1,499,266.16 USD | `640.77` | `2672.96` | `2339.60` | `2585.47` | 213,482.19 USD | `+14.24%` | `20X Cross` |
| `1530` | `0xfce0...f4c0` | `SHORT` | 1,458,974.56 USD | `623.60` | `3129.61` | `2339.60` | `2788.42` | 492,652.03 USD | `+33.77%` | `20X Cross` |
| `1555` | `0x7663...cb5a` | `SHORT` | 1,435,555.74 USD | `613.54` | `2342.35` | `2339.60` | `3628.43` | 1,564.74 USD | `+0.11%` | `3X Cross` |
| `1586` | `0xad02...eb65` | `LONG` | 1,405,211.02 USD | `600.62` | `2460.69` | `2339.60` | `1079.68` | -72,729.54 USD | `-5.18%` | `5X Cross` |
| `1587` | `0x638f...f5f0` | `LONG` | 1,403,880.00 USD | `600.00` | `4011.50` | `2339.60` | `0.000000` | -1,003,023.53 USD | `-71.45%` | `25X Cross` |
| `1588` | `0x0deb...0bc5` | `LONG` | 1,403,880.00 USD | `600.00` | `2038.23` | `2339.60` | `1478.69` | 180,941.36 USD | `+12.89%` | `20X Cross` |
| `1589` | `0x0a84...6ddd` | `LONG` | 1,403,880.00 USD | `600.00` | `2222.36` | `2339.60` | `1774.80` | 70,461.66 USD | `+5.02%` | `25X Cross` |
| `1590` | `0x26e6...6b28` | `LONG` | 1,403,760.00 USD | `600.00` | `1769.78` | `2339.60` | `2005.48` | 341,888.47 USD | `+24.36%` | `20X Cross` |
| `1591` | `0x67c3...609d` | `SHORT` | 1,403,700.00 USD | `600.00` | `2386.55` | `2339.60` | `2560.77` | 28,231.89 USD | `+2.01%` | `25X Cross` |
| `1611` | `0x94b6...e5b3` | `SHORT` | 1,372,784.06 USD | `586.71` | `2377.90` | `2339.60` | `2492.84` | 22,354.18 USD | `+1.63%` | `25X Cross` |
| `1635` | `0x823e...76c9` | `LONG` | 1,337,144.69 USD | `571.48` | `2339.20` | `2339.60` | `2083.06` | 342.89 USD | `+0.03%` | `25X Cross` |
| `1650` | `0xfb99...37f3` | `LONG` | 1,322,672.04 USD | `565.34` | `2362.35` | `2339.60` | `1208.17` | -12,864.32 USD | `-0.97%` | `3X Cross` |
| `1664` | `0x844b...7f42` | `SHORT` | 1,312,627.80 USD | `561.00` | `2026.17` | `2339.60` | `2991.79` | -175,944.39 USD | `-13.40%` | `25X Cross` |
| `1683` | `0xabe6...1d99` | `SHORT` | 1,300,826.96 USD | `556.00` | `2484.68` | `2339.60` | `2941.68` | 80,668.93 USD | `+6.20%` | `20X Cross` |
| `1729` | `0xad21...fb6a` | `LONG` | 1,244,467.79 USD | `531.87` | `2574.89` | `2339.60` | `1681.70` | -125,037.71 USD | `-10.05%` | `7X Cross` |
| `1767` | `0x8923...1bac` | `SHORT` | 1,210,002.52 USD | `517.18` | `2348.15` | `2339.60` | `3172.22` | 4,422.58 USD | `+0.37%` | `25X Cross` |
| `1785` | `0x0c7a...2f50` | `SHORT` | 1,191,532.15 USD | `509.25` | `2122.56` | `2339.60` | `4066.41` | -110,626.72 USD | `-9.28%` | `20X Cross` |
| `1812` | `0x0e1c...ce6d` | `LONG` | 1,169,800.00 USD | `500.00` | `2329.15` | `2339.60` | `2003.18` | 5,223.27 USD | `+0.45%` | `15X Cross` |
| `1813` | `0x89b2...9ca6` | `LONG` | 1,169,700.00 USD | `500.00` | `2484.03` | `2339.60` | `1954.21` | -72,319.35 USD | `-6.18%` | `25X Cross` |
| `1814` | `0x7298...7d6c` | `SHORT` | 1,165,171.21 USD | `498.15` | `3426.75` | `2339.60` | `5422.39` | 541,864.61 USD | `+46.51%` | `20X Cross` |
| `1834` | `0xc10f...23b3` | `LONG` | 1,146,502.00 USD | `490.00` | `2402.16` | `2339.60` | `2082.05` | -30,560.83 USD | `-2.67%` | `25X Cross` |
| `1835` | `0x404c...5f03` | `SHORT` | 1,145,803.73 USD | `489.79` | `2671.94` | `2339.60` | `4268.27` | 162,875.83 USD | `+14.21%` | `20X Cross` |
| `1840` | `0x321f...1c84` | `SHORT` | 1,142,004.84 USD | `488.02` | `2370.09` | `2339.60` | `3020.54` | 14,639.76 USD | `+1.28%` | `10X Cross` |
| `1871` | `0x72d0...62ea` | `LONG` | 1,109,656.60 USD | `474.29` | `2337.14` | `2339.60` | `0.000000` | 1,164.99 USD | `+0.10%` | `5X Cross` |
| `1900` | `0x82c6...fe42` | `LONG` | 1,082,065.00 USD | `462.50` | `2501.38` | `2339.60` | `2054.46` | -74,825.57 USD | `-6.92%` | `5X Isolated` |
| `1913` | `0x617e...0f97` | `SHORT` | 1,071,287.73 USD | `457.85` | `2205.60` | `2339.60` | `3655.13` | -61,443.89 USD | `-5.74%` | `10X Cross` |
| `1946` | `0xae55...2236` | `LONG` | 1,052,910.00 USD | `450.00` | `2510.21` | `2339.60` | `0.000000` | -76,687.50 USD | `-7.28%` | `25X Cross` |
| `1954` | `0x0dd5...f6ee` | `LONG` | 1,048,516.12 USD | `448.10` | `2336.33` | `2339.60` | `318.62` | 1,615.80 USD | `+0.15%` | `5X Cross` |
| `1959` | `0xac26...a9c7` | `SHORT` | 1,044,198.69 USD | `446.28` | `2192.58` | `2339.60` | `8596.06` | -65,698.99 USD | `-6.29%` | `20X Cross` |
| `1962` | `0x53f8...ceff` | `LONG` | 1,042,519.91 USD | `445.60` | `2399.81` | `2339.60` | `0.000000` | -26,830.69 USD | `-2.57%` | `20X Cross` |
| `1976` | `0xd8a1...6687` | `LONG` | 1,032,922.30 USD | `441.53` | `2804.24` | `2339.60` | `2151.01` | -205,246.14 USD | `-19.87%` | `20X Cross` |
| `1989` | `0x248e...6be2` | `SHORT` | 1,020,948.68 USD | `436.40` | `2314.49` | `2339.60` | `4394.49` | -10,913.96 USD | `-1.07%` | `20X Cross` |
| `1995` | `0x80f2...0c3a` | `LONG` | 1,016,748.86 USD | `434.55` | `2564.17` | `2339.60` | `890.10` | -97,500.02 USD | `-9.59%` | `5X Cross` |
| `2018` | `0x15c8...045f` | `SHORT` | 1,003,535.31 USD | `428.90` | `1903.23` | `2339.60` | `3085.49` | -187,242.26 USD | `-18.66%` | `25X Cross` |
| `2033` | `0x4e6b...b7d4` | `LONG` | 1,000,818.18 USD | `427.77` | `2744.83` | `2339.60` | `82.76` | -173,346.85 USD | `-17.32%` | `25X Cross` |

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
  * 24H Horizon: Short MP=`2401.93` (Vol: 17,300,000.00 USD, Dist: `+2.72%`) | Long MP=`2284.33` (Vol: 27,300,000.00 USD, Dist: `--2.31%`)
  * 48H Horizon: Short MP=`2401.93` (Vol: 25,300,000.00 USD, Dist: `+2.72%`) | Long MP=`2284.33` (Vol: 30,000,000.00 USD, Dist: `--2.31%`)
  * 3D Horizon: Short MP=`2401.93` (Vol: 26,700,000.00 USD, Dist: `+2.72%`) | Long MP=`2286.29` (Vol: 37,900,000.00 USD, Dist: `--2.23%`)
  * 7D Horizon: Short MP=`2402.93` (Vol: 47,100,000.00 USD, Dist: `+2.76%`) | Long MP=`2284.60` (Vol: 72,300,000.00 USD, Dist: `--2.30%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `475.00` | 7,100.00 USD | 873,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.00` | 65,780.00 USD | 873,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `495.00` | 14,280.00 USD | 873,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.00` | 12,510.00 USD | 873,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.00` | 5,560.00 USD | 873,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.00` | 6,230.00 USD | 873,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.00` | 10,400.00 USD | 873,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.00` | 68,610.00 USD | 873,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.00` | 143,270.00 USD | 873,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `565.00` | 14,660.00 USD | 873,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `575.00` | 397,980.00 USD | 873,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.00` | 23,700.00 USD | 873,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.00` | 8,970.00 USD | 873,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `605.00` | 47,100.00 USD | 873,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.00` | 69,280.00 USD | 873,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.00` | 36,410.00 USD | 873,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.00` | 51,290.00 USD | 873,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `645.00` | 27,830.00 USD | 872,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `655.00` | 135,660.00 USD | 872,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `665.00` | 30,410.00 USD | 872,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `675.00` | 30,650.00 USD | 872,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `685.00` | 124,480.00 USD | 872,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `695.00` | 2,010.00 USD | 872,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `705.00` | 6,260.00 USD | 872,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `715.00` | 1,620.00 USD | 872,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `725.00` | 383,190.00 USD | 872,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `735.00` | 42,360.00 USD | 872,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `745.00` | 23,330.00 USD | 872,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `755.00` | 27,030.00 USD | 872,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `765.00` | 76,850.00 USD | 872,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `775.00` | 1,750,000.00 USD | 872,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `785.00` | 16,520.00 USD | 870,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `795.00` | 24,890.00 USD | 870,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `805.00` | 250,090.00 USD | 870,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `815.00` | 373,250.00 USD | 870,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `825.00` | 144,310.00 USD | 869,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `835.00` | 20,760.00 USD | 869,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `845.00` | 7,110.00 USD | 869,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `855.00` | 6,250.00 USD | 869,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `865.00` | 59,400.00 USD | 869,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `875.00` | 32,500.00 USD | 869,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `885.00` | 418,200.00 USD | 869,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `895.00` | 29,870.00 USD | 868,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `905.00` | 93,070.00 USD | 868,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `915.00` | 160,780.00 USD | 868,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `925.00` | 130,820.00 USD | 868,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `935.00` | 4,110,000.00 USD | 868,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `945.00` | 77,190.00 USD | 864,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `955.00` | 1,130,000.00 USD | 864,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `965.00` | 27,170.00 USD | 863,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `975.00` | 67,650.00 USD | 863,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `985.00` | 30,850.00 USD | 863,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `995.00` | 226,950.00 USD | 863,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1005.00` | 7,090,000.00 USD | 862,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1015.00` | 23,200.00 USD | 855,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1025.00` | 173,670.00 USD | 855,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1035.00` | 41,110.00 USD | 855,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1045.00` | 3,170,000.00 USD | 855,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1055.00` | 34,380.00 USD | 852,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1065.00` | 153,900.00 USD | 852,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1075.00` | 675,850.00 USD | 852,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1085.00` | 78,450.00 USD | 851,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1095.00` | 1,770,000.00 USD | 851,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1105.00` | 143,580.00 USD | 849,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1115.00` | 88,800.00 USD | 849,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1125.00` | 491,080.00 USD | 849,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1135.00` | 134,860.00 USD | 848,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1145.00` | 27,690.00 USD | 848,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1155.00` | 351,020.00 USD | 848,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1165.00` | 11,000.00 USD | 848,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1175.00` | 300,400.00 USD | 848,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1185.00` | 186,300.00 USD | 848,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1195.00` | 368,940.00 USD | 847,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1205.00` | 1,110,000.00 USD | 847,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1215.00` | 11,090,000.00 USD | 846,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1225.00` | 1,470,000.00 USD | 835,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1235.00` | 183,930.00 USD | 833,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1245.00` | 424,530.00 USD | 833,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1255.00` | 385,620.00 USD | 833,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1265.00` | 821,130.00 USD | 832,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1275.00` | 207,090.00 USD | 832,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1285.00` | 15,590,000.00 USD | 831,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1295.00` | 135,220.00 USD | 816,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1305.00` | 173,350.00 USD | 816,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1315.00` | 502,710.00 USD | 816,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1325.00` | 703,060.00 USD | 815,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1335.00` | 289,550.00 USD | 814,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1345.00` | 548,280.00 USD | 814,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1355.00` | 6,750,000.00 USD | 813,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1365.00` | 1,120,000.00 USD | 807,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1375.00` | 241,210.00 USD | 806,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1385.00` | 153,390.00 USD | 805,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1395.00` | 15,500,000.00 USD | 805,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1405.00` | 16,810,000.00 USD | 790,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1415.00` | 135,850.00 USD | 773,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1425.00` | 1,540,000.00 USD | 773,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1435.00` | 291,120.00 USD | 771,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1445.00` | 359,980.00 USD | 771,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1455.00` | 14,630,000.00 USD | 771,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1465.00` | 530,740.00 USD | 756,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1475.00` | 2,400,000.00 USD | 755,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1485.00` | 328,080.00 USD | 753,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1495.00` | 5,000,000.00 USD | 753,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1505.00` | 150,430.00 USD | 748,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1515.00` | 369,220.00 USD | 748,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1525.00` | 18,690,000.00 USD | 747,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1535.00` | 608,550.00 USD | 728,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1545.00` | 2,860,000.00 USD | 728,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1555.00` | 25,730,000.00 USD | 725,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1565.00` | 185,480.00 USD | 699,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1575.00` | 251,000.00 USD | 699,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1585.00` | 218,590.00 USD | 699,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1595.00` | 7,590,000.00 USD | 699,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1605.00` | 20,850,000.00 USD | 691,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1615.00` | 119,070.00 USD | 670,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1625.00` | 620,560.00 USD | 670,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1635.00` | 18,320,000.00 USD | 669,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1645.00` | 59,700,000.00 USD | 651,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1655.00` | 602,670.00 USD | 591,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1665.00` | 1,110,000.00 USD | 591,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1675.00` | 12,040,000.00 USD | 590,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1685.00` | 1,390,000.00 USD | 578,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1695.00` | 460,530.00 USD | 576,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1705.00` | 1,510,000.00 USD | 576,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1715.00` | 12,670,000.00 USD | 574,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1725.00` | 17,850,000.00 USD | 562,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1735.00` | 17,950,000.00 USD | 544,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1745.00` | 1,150,000.00 USD | 526,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1755.00` | 1,400,000.00 USD | 525,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1765.00` | 874,200.00 USD | 523,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1775.00` | 14,290,000.00 USD | 522,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1785.00` | 54,540,000.00 USD | 508,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1795.00` | 3,520,000.00 USD | 454,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1805.00` | 1,640,000.00 USD | 450,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1815.00` | 331,980.00 USD | 448,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1825.00` | 1,940,000.00 USD | 448,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1835.00` | 847,330.00 USD | 446,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1845.00` | 8,960,000.00 USD | 445,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1855.00` | 2,850,000.00 USD | 436,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1865.00` | 5,430,000.00 USD | 433,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1875.00` | 5,660,000.00 USD | 428,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1885.00` | 2,680,000.00 USD | 422,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1895.00` | 5,390,000.00 USD | 420,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1905.00` | 1,570,000.00 USD | 414,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1915.00` | 28,410,000.00 USD | 413,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1925.00` | 3,380,000.00 USD | 384,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1935.00` | 2,270,000.00 USD | 381,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1945.00` | 635,200.00 USD | 379,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1955.00` | 2,610,000.00 USD | 378,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1965.00` | 1,200,000.00 USD | 375,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1975.00` | 6,040,000.00 USD | 374,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1985.00` | 4,410,000.00 USD | 368,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1995.00` | 658,250.00 USD | 364,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2005.00` | 3,690,000.00 USD | 363,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2015.00` | 2,570,000.00 USD | 359,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2025.00` | 1,100,000.00 USD | 357,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2035.00` | 5,320,000.00 USD | 356,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2045.00` | 17,040,000.00 USD | 350,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2055.00` | 4,070,000.00 USD | 333,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2065.00` | 1,310,000.00 USD | 329,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2074.60` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 3,960,000.00 USD | 3,150,000.00 USD | 2,680,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 599,560.00 USD | 328,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2077.40` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 4,430,000.00 USD | 3,940,000.00 USD | 1,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2080.20` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 3,480,000.00 USD | 2,740,000.00 USD | 2,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2083.00` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 2,340,000.00 USD | 1,900,000.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 2,870,000.00 USD | 327,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2085.80` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 4,270,000.00 USD | 2,570,000.00 USD | 3,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2088.60` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 1,920,000.00 USD | 1,480,000.00 USD | 1,470,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2091.40` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 4,210,000.00 USD | 549,010.00 USD | 6,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2094.20` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 5,310,000.00 USD | 1,660,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 5,740,000.00 USD | 325,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2096.00` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 2,150,000.00 USD | 1,620,000.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2097.00` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 1,830,000.00 USD | 3,320,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2098.70` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 513,340.00 USD | 682,000.00 USD | 248,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2099.80` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 1,880,000.00 USD | 1,920,000.00 USD | 3,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2101.40` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 46,810.00 USD | 31,040.00 USD | 144,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2102.60` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 125,250.00 USD | 341,900.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2104.10` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 907,940.00 USD | 570,780.00 USD | 12,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 1,420,000.00 USD | 319,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2105.40` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 2,050,000.00 USD | 986,590.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2106.80` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 358,850.00 USD | 17,140.00 USD | 265,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2108.20` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 2,350,000.00 USD | 1,090,000.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2109.50` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 151,690.00 USD | 401,490.00 USD | 148,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2111.00` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 3,450,000.00 USD | 1,620,000.00 USD | 2,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2112.20` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 1,290,000.00 USD | 946,650.00 USD | 556,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2113.80` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 1,080,000.00 USD | 1,300,000.00 USD | 2,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2114.90` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 9,210.00 USD | 0.00 USD | 441,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 17,610,000.00 USD | 317,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2116.60` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 2,360,000.00 USD | 2,350,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2117.60` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 1,280,000.00 USD | 339,800.00 USD | 811,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2119.40` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 2,530,000.00 USD | 606,940.00 USD | 2,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2120.30` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 650,890.00 USD | 428,990.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2122.20` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 2,230,000.00 USD | 1,000,000.00 USD | 1,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2123.00` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 1,630,000.00 USD | 716,530.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2125.00` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 2,700,000.00 USD | 2,150,000.00 USD | 2,640,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 1,030,000.00 USD | 300,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2125.70` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 179,030.00 USD | 1,520,000.00 USD | 513,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2127.80` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 496,060.00 USD | 1,960,000.00 USD | 1,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2128.40` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 365,910.00 USD | 623,840.00 USD | 129,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2130.60` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 2,040,000.00 USD | 1,750,000.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2131.10` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 644,330.00 USD | 654,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2133.40` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 2,120,000.00 USD | 550,450.00 USD | 316,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2133.80` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 187,520.00 USD | 497,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 2,720,000.00 USD | 299,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2136.20` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 1,170,000.00 USD | 845,110.00 USD | 18,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2136.50` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 294,600.00 USD | 2,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2139.00` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 1,110,000.00 USD | 1,000,000.00 USD | 276,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2139.20` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 555,320.00 USD | 250,240.00 USD | 205,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2141.80` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 1,550,000.00 USD | 209,240.00 USD | 819,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2144.60` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 295,510.00 USD | 16,700.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2144.60` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 547,980.00 USD | 1,530,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 9,660,000.00 USD | 296,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2147.30` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 11,090.00 USD | 207,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2147.40` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 157,100.00 USD | 32,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2150.00` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 251,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2150.20` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 459,630.00 USD | 482,820.00 USD | 537,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2153.00` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 58,340.00 USD | 681,070.00 USD | 800,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 23,300,000.00 USD | 286,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2155.80` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 191,860.00 USD | 454,940.00 USD | 66,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2158.60` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 774,660.00 USD | 1,260,000.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2161.40` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 1,450,000.00 USD | 804,860.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2164.20` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 36,870.00 USD | 329,690.00 USD | 409,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 857,510.00 USD | 263,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2167.00` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 25,540.00 USD | 0.00 USD | 84,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2169.80` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 1,700,000.00 USD | 726,240.00 USD | 794,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2172.60` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 479,540.00 USD | 1,150,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 108,630,000.00 USD | 262,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2185.00` | 111,630,000.00 USD | 154,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2195.00` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 141,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 1,510,000.00 USD | 42,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2197.80` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 2,440,000.00 USD | 3,270,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2200.60` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 3,120,000.00 USD | 3,140,000.00 USD | 3,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2201.30` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 284,470.00 USD | 217,490.00 USD | 225,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2203.40` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 3,280,000.00 USD | 624,500.00 USD | 2,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2204.00` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 1,050,000.00 USD | 207,110.00 USD | 792,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 1,240,000.00 USD | 40,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2206.20` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 6,770,000.00 USD | 4,010,000.00 USD | 4,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2206.70` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 2,070,000.00 USD | 2,270,000.00 USD | 1,760,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2209.00` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 9,190,000.00 USD | 7,030,000.00 USD | 4,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2209.40` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 1,170,000.00 USD | 668,670.00 USD | 1,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2211.80` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 8,790,000.00 USD | 8,110,000.00 USD | 6,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2212.10` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 3,180,000.00 USD | 1,580,000.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2214.60` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 14,850,000.00 USD | 14,220,000.00 USD | 10,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2214.80` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 6,410,000.00 USD | 4,340,000.00 USD | 5,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 1,970,000.00 USD | 39,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2217.40` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 13,750,000.00 USD | 10,950,000.00 USD | 7,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2217.50` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 4,250,000.00 USD | 5,300,000.00 USD | 1,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2220.20` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 3,770,000.00 USD | 4,230,000.00 USD | 574,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2220.20` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 12,830,000.00 USD | 7,840,000.00 USD | 3,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2222.90` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 5,840,000.00 USD | 3,820,000.00 USD | 2,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2223.00` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 6,930,000.00 USD | 5,300,000.00 USD | 11,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2225.00` | 2,130,000.00 USD | 37,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2225.60` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 2,730,000.00 USD | 5,760,000.00 USD | 2,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2225.80` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 11,900,000.00 USD | 12,610,000.00 USD | 6,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2228.30` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 5,110,000.00 USD | 1,430,000.00 USD | 771,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2228.60` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 7,530,000.00 USD | 5,580,000.00 USD | 9,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2231.00` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 3,720,000.00 USD | 2,610,000.00 USD | 3,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2231.40` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 10,960,000.00 USD | 2,990,000.00 USD | 14,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2233.70` | 991,260,000.00 USD | 991,260,000.00 USD | 7,010,000.00 USD | 4,050,000.00 USD | 2,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2234.20` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 17,000,000.00 USD | 12,020,000.00 USD | 7,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2235.00` | 671,070.00 USD | 35,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2236.40` | 977,760,000.00 USD | 977,760,000.00 USD | 2,710,000.00 USD | 2,070,000.00 USD | 3,930,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2237.00` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 6,950,000.00 USD | 11,130,000.00 USD | 4,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2239.10` | 969,050,000.00 USD | 969,050,000.00 USD | 1,130,000.00 USD | 2,260,000.00 USD | 621,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2239.80` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 7,410,000.00 USD | 6,730,000.00 USD | 9,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2241.80` | 965,040,000.00 USD | 965,040,000.00 USD | 736,150.00 USD | 12,140.00 USD | 360,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2242.60` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 7,790,000.00 USD | 2,710,000.00 USD | 4,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2244.50` | 963,930,000.00 USD | 963,930,000.00 USD | 2,500,000.00 USD | 1,860,000.00 USD | 265,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2245.00` | 4,720,000.00 USD | 34,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2245.40` | 2,080,000,000.00 USD | 2,080,000,000.00 USD | 12,040,000.00 USD | 12,530,000.00 USD | 10,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2247.20` | 959,310,000.00 USD | 959,310,000.00 USD | 1,800,000.00 USD | 946,140.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2248.20` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 13,950,000.00 USD | 5,870,000.00 USD | 11,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2249.90` | 955,450,000.00 USD | 955,450,000.00 USD | 3,390,000.00 USD | 1,710,000.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2251.00` | 2,020,000,000.00 USD | 2,020,000,000.00 USD | 12,710,000.00 USD | 11,300,000.00 USD | 8,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2252.60` | 948,560,000.00 USD | 948,560,000.00 USD | 7,060,000.00 USD | 7,800,000.00 USD | 5,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2253.80` | 1,990,000,000.00 USD | 1,990,000,000.00 USD | 25,660,000.00 USD | 20,190,000.00 USD | 19,820,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2255.00` | 11,410,000.00 USD | 30,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2255.30` | 928,430,000.00 USD | 928,430,000.00 USD | 3,350,000.00 USD | 2,460,000.00 USD | 5,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2256.60` | 1,920,000,000.00 USD | 1,920,000,000.00 USD | 29,170,000.00 USD | 24,230,000.00 USD | 17,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2258.00` | 917,130,000.00 USD | 917,130,000.00 USD | 10,230,000.00 USD | 4,670,000.00 USD | 4,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2259.40` | 1,850,000,000.00 USD | 1,850,000,000.00 USD | 25,970,000.00 USD | 15,650,000.00 USD | 27,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2260.70` | 897,400,000.00 USD | 897,400,000.00 USD | 15,440,000.00 USD | 9,960,000.00 USD | 10,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2262.20` | 1,780,000,000.00 USD | 1,780,000,000.00 USD | 46,580,000.00 USD | 30,720,000.00 USD | 19,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2263.40` | 861,180,000.00 USD | 861,180,000.00 USD | 11,650,000.00 USD | 14,790,000.00 USD | 11,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2265.00` | 1,680,000,000.00 USD | 1,680,000,000.00 USD | 29,070,000.00 USD | 25,860,000.00 USD | 16,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2265.00` | 5,260,000.00 USD | 18,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2266.10` | 823,540,000.00 USD | 823,540,000.00 USD | 12,420,000.00 USD | 11,610,000.00 USD | 3,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2267.80` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 41,280,000.00 USD | 43,110,000.00 USD | 32,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2268.80` | 796,060,000.00 USD | 796,060,000.00 USD | 14,780,000.00 USD | 11,070,000.00 USD | 8,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2270.60` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 43,030,000.00 USD | 30,540,000.00 USD | 36,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2271.50` | 761,350,000.00 USD | 761,350,000.00 USD | 9,670,000.00 USD | 10,000,000.00 USD | 9,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2273.40` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 27,330,000.00 USD | 19,600,000.00 USD | 20,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2274.20` | 732,460,000.00 USD | 732,460,000.00 USD | 11,980,000.00 USD | 9,210,000.00 USD | 5,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2275.00` | 3,330,000.00 USD | 13,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2276.20` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 55,750,000.00 USD | 46,480,000.00 USD | 59,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2276.90` | 705,720,000.00 USD | 705,720,000.00 USD | 21,220,000.00 USD | 14,790,000.00 USD | 14,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2279.00` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 71,690,000.00 USD | 30,780,000.00 USD | 36,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2279.60` | 655,130,000.00 USD | 655,130,000.00 USD | 18,510,000.00 USD | 12,820,000.00 USD | 11,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2281.80` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 64,270,000.00 USD | 63,850,000.00 USD | 39,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2282.30` | 612,560,000.00 USD | 612,560,000.00 USD | 23,240,000.00 USD | 18,900,000.00 USD | 19,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2284.60` | 849,390,000.00 USD | 849,390,000.00 USD | 84,980,000.00 USD | 71,990,000.00 USD | 47,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2285.00` | 550,870,000.00 USD | 550,870,000.00 USD | 29,050,000.00 USD | 25,280,000.00 USD | 19,700,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2285.00` | 5,830,000.00 USD | 10,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2287.40` | 644,830,000.00 USD | 644,830,000.00 USD | 57,800,000.00 USD | 54,380,000.00 USD | 45,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2287.70` | 476,840,000.00 USD | 476,840,000.00 USD | 22,660,000.00 USD | 14,830,000.00 USD | 5,280,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2290.20` | 486,890,000.00 USD | 486,890,000.00 USD | 45,650,000.00 USD | 33,150,000.00 USD | 39,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2290.40` | 434,070,000.00 USD | 434,070,000.00 USD | 10,470,000.00 USD | 15,850,000.00 USD | 3,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2293.00` | 369,060,000.00 USD | 369,060,000.00 USD | 33,030,000.00 USD | 15,200,000.00 USD | 23,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2293.10` | 404,670,000.00 USD | 404,670,000.00 USD | 23,490,000.00 USD | 20,570,000.00 USD | 13,980,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2295.00` | 1,910,000.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2295.80` | 346,630,000.00 USD | 346,630,000.00 USD | 22,630,000.00 USD | 15,930,000.00 USD | 8,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2295.80` | 297,690,000.00 USD | 297,690,000.00 USD | 17,510,000.00 USD | 9,480,000.00 USD | 6,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2298.50` | 299,290,000.00 USD | 299,290,000.00 USD | 9,030,000.00 USD | 7,220,000.00 USD | 3,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2298.60` | 263,910,000.00 USD | 263,910,000.00 USD | 2,760,000.00 USD | 4,450,000.00 USD | 358,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2301.20` | 279,770,000.00 USD | 279,770,000.00 USD | 17,170,000.00 USD | 12,340,000.00 USD | 13,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2301.40` | 256,340,000.00 USD | 256,340,000.00 USD | 11,120,000.00 USD | 2,120,000.00 USD | 7,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2303.90` | 236,930,000.00 USD | 236,930,000.00 USD | 29,770,000.00 USD | 16,570,000.00 USD | 13,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2304.20` | 235,560,000.00 USD | 235,560,000.00 USD | 32,960,000.00 USD | 16,920,000.00 USD | 13,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2305.00` | 1,080,000.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2306.60` | 177,460,000.00 USD | 177,460,000.00 USD | 4,970,000.00 USD | 4,390,000.00 USD | 15,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2307.00` | 172,410,000.00 USD | 172,410,000.00 USD | 0.00 USD | 3,740,000.00 USD | 10,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2309.30` | 152,750,000.00 USD | 152,750,000.00 USD | 3,760,000.00 USD | 2,320,000.00 USD | 822,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2309.80` | 157,780,000.00 USD | 157,780,000.00 USD | 282,530.00 USD | 300,580.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2312.00` | 145,850,000.00 USD | 145,850,000.00 USD | 9,070,000.00 USD | 5,970,000.00 USD | 6,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2312.60` | 155,690,000.00 USD | 155,690,000.00 USD | 2,470,000.00 USD | 640,510.00 USD | 2,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2314.70` | 124,520,000.00 USD | 124,520,000.00 USD | 8,520,000.00 USD | 9,160,000.00 USD | 1,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2315.00` | 657,320.00 USD | 657,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2315.40` | 149,960,000.00 USD | 149,960,000.00 USD | 5,830,000.00 USD | 4,100,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2317.40` | 105,090,000.00 USD | 105,090,000.00 USD | 8,380,000.00 USD | 4,290,000.00 USD | 3,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2318.20` | 140,030,000.00 USD | 140,030,000.00 USD | 0.00 USD | 3,010,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2320.10` | 89,030,000.00 USD | 89,030,000.00 USD | 4,730,000.00 USD | 3,110,000.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2321.00` | 137,020,000.00 USD | 137,020,000.00 USD | 947,800.00 USD | 2,960,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2322.80` | 79,470,000.00 USD | 79,470,000.00 USD | 5,160,000.00 USD | 1,870,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2323.80` | 133,110,000.00 USD | 133,110,000.00 USD | 3,130,000.00 USD | 2,210,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2325.00` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2325.50` | 72,440,000.00 USD | 72,440,000.00 USD | 4,120,000.00 USD | 2,830,000.00 USD | 3,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2326.60` | 127,780,000.00 USD | 127,780,000.00 USD | 0.00 USD | 0.00 USD | 126,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2328.20` | 62,200,000.00 USD | 62,200,000.00 USD | 1,890,000.00 USD | 3,130,000.00 USD | 3,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2329.40` | 127,650,000.00 USD | 127,650,000.00 USD | 3,860,000.00 USD | 0.00 USD | 4,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2330.90` | 53,580,000.00 USD | 53,580,000.00 USD | 5,350,000.00 USD | 1,150,000.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2332.20` | 118,910,000.00 USD | 118,910,000.00 USD | 29,230,000.00 USD | 0.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2333.60` | 44,270,000.00 USD | 44,270,000.00 USD | 7,850,000.00 USD | 12,110,000.00 USD | 5,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2335.00` | 86,860,000.00 USD | 86,860,000.00 USD | 13,560,000.00 USD | 18,420,000.00 USD | 8,930,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2335.00` | 1,060.00 USD | 1,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2336.30` | 18,850,000.00 USD | 18,850,000.00 USD | 12,670,000.00 USD | 6,180,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2337.80` | 45,960,000.00 USD | 45,960,000.00 USD | 14,090,000.00 USD | 18,310,000.00 USD | 13,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2339.00` | 10,810,000.00 USD | 10,810,000.00 USD | 0.00 USD | 0.00 USD | 10,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2340.60` | 18,930,000.00 USD | 18,930,000.00 USD | 0.00 USD | 15,560,000.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2341.70` | 14,160,000.00 USD | 14,160,000.00 USD | 1,880,000.00 USD | 0.00 USD | 1,470,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2343.40` | 26,100,000.00 USD | 26,100,000.00 USD | 0.00 USD | 0.00 USD | 7,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2344.40` | 23,760,000.00 USD | 23,760,000.00 USD | 963,370.00 USD | 1,960,000.00 USD | 6,680,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2345.00` | 5,140.00 USD | 662,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2346.20` | 43,520,000.00 USD | 43,520,000.00 USD | 0.00 USD | 7,920,000.00 USD | 9,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2347.10` | 27,770,000.00 USD | 27,770,000.00 USD | 0.00 USD | 0.00 USD | 4,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2349.00` | 71,940,000.00 USD | 71,940,000.00 USD | 495,290.00 USD | 11,840,000.00 USD | 16,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2349.80` | 53,260,000.00 USD | 53,260,000.00 USD | 22,960,000.00 USD | 2,510,000.00 USD | 23,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2351.80` | 85,960,000.00 USD | 85,960,000.00 USD | 572,980.00 USD | 13,100,000.00 USD | 351,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2352.50` | 57,190,000.00 USD | 57,190,000.00 USD | 3,690,000.00 USD | 121,980.00 USD | 107,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2354.60` | 130,750,000.00 USD | 130,750,000.00 USD | 9,800,000.00 USD | 34,750,000.00 USD | 237,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 73,520.00 USD | 735,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2355.20` | 76,190,000.00 USD | 76,190,000.00 USD | 663,120.00 USD | 17,100,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2357.40` | 141,700,000.00 USD | 141,700,000.00 USD | 5,040,000.00 USD | 5,920,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2357.90` | 77,980,000.00 USD | 77,980,000.00 USD | 1,400,000.00 USD | 191,800.00 USD | 198,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2360.20` | 144,140,000.00 USD | 144,140,000.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2360.60` | 83,150,000.00 USD | 83,150,000.00 USD | 2,010,000.00 USD | 1,830,000.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2363.00` | 146,540,000.00 USD | 146,540,000.00 USD | 715,490.00 USD | 0.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2363.30` | 94,890,000.00 USD | 94,890,000.00 USD | 3,730,000.00 USD | 7,640,000.00 USD | 360,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 2,900.00 USD | 738,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2365.80` | 154,540,000.00 USD | 154,540,000.00 USD | 6,340,000.00 USD | 0.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2366.00` | 95,270,000.00 USD | 95,270,000.00 USD | 192,950.00 USD | 0.00 USD | 189,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2368.60` | 165,020,000.00 USD | 165,020,000.00 USD | 9,590,000.00 USD | 475,460.00 USD | 404,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2368.70` | 107,540,000.00 USD | 107,540,000.00 USD | 7,840,000.00 USD | 3,260,000.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2371.40` | 147,510,000.00 USD | 147,510,000.00 USD | 17,450,000.00 USD | 13,550,000.00 USD | 8,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2371.40` | 230,830,000.00 USD | 230,830,000.00 USD | 18,630,000.00 USD | 0.00 USD | 47,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2374.10` | 163,580,000.00 USD | 163,580,000.00 USD | 13,230,000.00 USD | 349,710.00 USD | 2,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2374.20` | 249,340,000.00 USD | 249,340,000.00 USD | 13,960,000.00 USD | 0.00 USD | 4,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 16,680.00 USD | 755,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2376.80` | 192,950,000.00 USD | 192,950,000.00 USD | 12,180,000.00 USD | 5,320,000.00 USD | 11,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2377.00` | 289,730,000.00 USD | 289,730,000.00 USD | 12,140,000.00 USD | 6,190,000.00 USD | 22,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2379.50` | 226,210,000.00 USD | 226,210,000.00 USD | 7,980,000.00 USD | 12,400,000.00 USD | 12,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2379.80` | 317,920,000.00 USD | 317,920,000.00 USD | 7,180,000.00 USD | 2,330,000.00 USD | 18,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2382.20` | 272,040,000.00 USD | 272,040,000.00 USD | 20,360,000.00 USD | 11,020,000.00 USD | 14,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2382.60` | 359,310,000.00 USD | 359,310,000.00 USD | 8,620,000.00 USD | 12,380,000.00 USD | 20,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2384.90` | 323,330,000.00 USD | 323,330,000.00 USD | 19,430,000.00 USD | 22,000,000.00 USD | 9,870,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 3,320,000.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2385.40` | 455,660,000.00 USD | 455,660,000.00 USD | 15,530,000.00 USD | 30,320,000.00 USD | 50,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2387.60` | 357,190,000.00 USD | 357,190,000.00 USD | 13,120,000.00 USD | 13,690,000.00 USD | 7,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2388.20` | 532,620,000.00 USD | 532,620,000.00 USD | 4,500,000.00 USD | 34,050,000.00 USD | 38,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2390.30` | 375,800,000.00 USD | 375,800,000.00 USD | 5,560,000.00 USD | 6,220,000.00 USD | 6,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2391.00` | 629,010,000.00 USD | 629,010,000.00 USD | 5,620,000.00 USD | 45,790,000.00 USD | 44,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2393.00` | 406,320,000.00 USD | 406,320,000.00 USD | 7,290,000.00 USD | 15,180,000.00 USD | 8,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2393.80` | 741,320,000.00 USD | 741,320,000.00 USD | 48,290,000.00 USD | 27,870,000.00 USD | 36,150,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 91,230.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2395.70` | 427,630,000.00 USD | 427,630,000.00 USD | 9,390,000.00 USD | 9,260,000.00 USD | 2,650,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2396.60` | 815,610,000.00 USD | 815,610,000.00 USD | 26,490,000.00 USD | 29,530,000.00 USD | 18,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2398.40` | 458,080,000.00 USD | 458,080,000.00 USD | 6,170,000.00 USD | 12,390,000.00 USD | 11,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2399.40` | 913,790,000.00 USD | 913,790,000.00 USD | 49,120,000.00 USD | 29,120,000.00 USD | 19,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2401.10` | 495,610,000.00 USD | 495,610,000.00 USD | 20,930,000.00 USD | 8,040,000.00 USD | 8,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2402.20` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 45,210,000.00 USD | 27,170,000.00 USD | 31,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2403.80` | 531,140,000.00 USD | 531,140,000.00 USD | 14,520,000.00 USD | 11,360,000.00 USD | 9,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2405.00` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 35,270,000.00 USD | 26,450,000.00 USD | 17,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 13,290,000.00 USD | 17,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2406.50` | 562,050,000.00 USD | 562,050,000.00 USD | 11,930,000.00 USD | 10,410,000.00 USD | 8,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2407.80` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 26,280,000.00 USD | 26,510,000.00 USD | 16,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2409.20` | 590,780,000.00 USD | 590,780,000.00 USD | 7,630,000.00 USD | 11,180,000.00 USD | 9,930,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2410.60` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 23,140,000.00 USD | 26,640,000.00 USD | 27,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2411.90` | 618,440,000.00 USD | 618,440,000.00 USD | 14,580,000.00 USD | 8,760,000.00 USD | 4,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2413.40` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 15,370,000.00 USD | 14,870,000.00 USD | 9,740,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2414.60` | 630,060,000.00 USD | 630,060,000.00 USD | 3,070,000.00 USD | 3,950,000.00 USD | 4,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 362,060.00 USD | 17,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2416.20` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 26,140,000.00 USD | 16,790,000.00 USD | 32,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2417.30` | 643,950,000.00 USD | 643,950,000.00 USD | 3,970,000.00 USD | 6,830,000.00 USD | 3,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2419.00` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 30,180,000.00 USD | 17,120,000.00 USD | 11,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2420.00` | 658,530,000.00 USD | 658,530,000.00 USD | 7,860,000.00 USD | 4,500,000.00 USD | 2,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2421.80` | 1,490,000,000.00 USD | 1,490,000,000.00 USD | 21,830,000.00 USD | 26,230,000.00 USD | 20,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2422.70` | 674,340,000.00 USD | 674,340,000.00 USD | 4,910,000.00 USD | 5,090,000.00 USD | 5,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.60` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 25,990,000.00 USD | 31,850,000.00 USD | 32,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 890,120.00 USD | 18,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2425.40` | 679,340,000.00 USD | 679,340,000.00 USD | 1,500,000.00 USD | 2,650,000.00 USD | 852,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2427.40` | 1,640,000,000.00 USD | 1,640,000,000.00 USD | 25,000,000.00 USD | 18,790,000.00 USD | 24,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2428.10` | 681,390,000.00 USD | 681,390,000.00 USD | 1,930,000.00 USD | 89,750.00 USD | 39,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2430.20` | 1,670,000,000.00 USD | 1,670,000,000.00 USD | 6,090,000.00 USD | 16,890,000.00 USD | 6,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2430.80` | 684,010,000.00 USD | 684,010,000.00 USD | 1,100,000.00 USD | 964,820.00 USD | 562,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2433.00` | 1,710,000,000.00 USD | 1,710,000,000.00 USD | 15,680,000.00 USD | 12,450,000.00 USD | 5,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2433.50` | 689,460,000.00 USD | 689,460,000.00 USD | 2,160,000.00 USD | 1,550,000.00 USD | 1,740,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 7,770,000.00 USD | 26,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2435.80` | 1,760,000,000.00 USD | 1,760,000,000.00 USD | 20,300,000.00 USD | 12,110,000.00 USD | 17,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2436.20` | 694,100,000.00 USD | 694,100,000.00 USD | 3,200,000.00 USD | 1,240,000.00 USD | 199,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2438.60` | 1,820,000,000.00 USD | 1,820,000,000.00 USD | 21,710,000.00 USD | 24,630,000.00 USD | 15,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2438.90` | 696,720,000.00 USD | 696,720,000.00 USD | 340,220.00 USD | 1,090,000.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2441.40` | 1,850,000,000.00 USD | 1,850,000,000.00 USD | 13,540,000.00 USD | 6,350,000.00 USD | 13,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2441.60` | 704,010,000.00 USD | 704,010,000.00 USD | 3,730,000.00 USD | 2,790,000.00 USD | 767,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2444.20` | 1,890,000,000.00 USD | 1,890,000,000.00 USD | 9,430,000.00 USD | 15,220,000.00 USD | 11,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2444.30` | 707,710,000.00 USD | 707,710,000.00 USD | 787,570.00 USD | 1,430,000.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 149,300.00 USD | 26,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2447.00` | 713,990,000.00 USD | 713,990,000.00 USD | 3,610,000.00 USD | 642,690.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2447.00` | 1,920,000,000.00 USD | 1,920,000,000.00 USD | 11,560,000.00 USD | 5,380,000.00 USD | 18,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2449.70` | 722,360,000.00 USD | 722,360,000.00 USD | 2,500,000.00 USD | 2,360,000.00 USD | 3,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2449.80` | 1,960,000,000.00 USD | 1,960,000,000.00 USD | 16,990,000.00 USD | 11,970,000.00 USD | 11,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2452.40` | 733,590,000.00 USD | 733,590,000.00 USD | 3,790,000.00 USD | 3,100,000.00 USD | 4,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2452.60` | 1,980,000,000.00 USD | 1,980,000,000.00 USD | 6,280,000.00 USD | 7,310,000.00 USD | 6,840,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 288,140.00 USD | 26,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2455.10` | 744,430,000.00 USD | 744,430,000.00 USD | 3,950,000.00 USD | 4,190,000.00 USD | 2,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2455.40` | 2,010,000,000.00 USD | 2,010,000,000.00 USD | 8,340,000.00 USD | 10,630,000.00 USD | 5,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2457.80` | 751,540,000.00 USD | 751,540,000.00 USD | 3,120,000.00 USD | 2,530,000.00 USD | 1,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2458.20` | 2,040,000,000.00 USD | 2,040,000,000.00 USD | 9,800,000.00 USD | 7,130,000.00 USD | 11,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2460.50` | 755,550,000.00 USD | 755,550,000.00 USD | 1,260,000.00 USD | 1,430,000.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2461.00` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 6,890,000.00 USD | 10,680,000.00 USD | 9,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2463.20` | 758,870,000.00 USD | 758,870,000.00 USD | 174,920.00 USD | 2,050,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2463.80` | 2,090,000,000.00 USD | 2,090,000,000.00 USD | 10,390,000.00 USD | 8,820,000.00 USD | 5,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 180,420.00 USD | 27,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2465.90` | 760,940,000.00 USD | 760,940,000.00 USD | 820,990.00 USD | 1,240,000.00 USD | 5,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2466.60` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 4,840,000.00 USD | 2,680,000.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2468.60` | 762,340,000.00 USD | 762,340,000.00 USD | 0.00 USD | 998,350.00 USD | 399,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2469.40` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 2,470,000.00 USD | 2,980,000.00 USD | 408,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2471.30` | 765,380,000.00 USD | 765,380,000.00 USD | 1,390,000.00 USD | 883,290.00 USD | 764,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2472.20` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 3,060,000.00 USD | 2,760,000.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2474.00` | 765,610,000.00 USD | 765,610,000.00 USD | 0.00 USD | 232,740.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2475.00` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 5,400,000.00 USD | 866,790.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 32,880.00 USD | 27,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2476.70` | 766,360,000.00 USD | 766,360,000.00 USD | 738,780.00 USD | 0.00 USD | 7,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2477.80` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 1,840,000.00 USD | 5,290,000.00 USD | 505,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2479.40` | 766,950,000.00 USD | 766,950,000.00 USD | 0.00 USD | 69,480.00 USD | 518,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2480.60` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 1,070,000.00 USD | 350,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2482.10` | 767,580,000.00 USD | 767,580,000.00 USD | 628,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2483.40` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 1,310,000.00 USD | 1,310,000.00 USD | 2,070,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 589,540.00 USD | 27,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2486.20` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 586,480.00 USD | 1,560,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2489.00` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 1,760,000.00 USD | 857,130.00 USD | 2,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2491.80` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 2,400,000.00 USD | 3,310,000.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2494.60` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 1,600,000.00 USD | 1,950,000.00 USD | 6,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 2,340,000.00 USD | 30,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2497.40` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 3,640,000.00 USD | 3,570,000.00 USD | 4,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2500.20` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 1,160,000.00 USD | 2,430,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2503.00` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 111,800.00 USD | 1,430,000.00 USD | 170,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 244,330.00 USD | 30,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2505.80` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 4,240,000.00 USD | 2,320,000.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2508.60` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 714,660.00 USD | 1,270,000.00 USD | 629,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2511.40` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 1,900,000.00 USD | 3,230,000.00 USD | 2,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2514.20` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 776,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 118,730.00 USD | 30,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2517.00` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 97,050.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2519.80` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2519.90` | 767,610,000.00 USD | 767,610,000.00 USD | 0.00 USD | 0.00 USD | 32,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2522.60` | 767,810,000.00 USD | 767,810,000.00 USD | 80,610.00 USD | 61,830.00 USD | 57,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2522.60` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 1,050,000.00 USD | 0.00 USD | 945,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 1,080,000.00 USD | 31,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2525.30` | 768,340,000.00 USD | 768,340,000.00 USD | 421,540.00 USD | 57,450.00 USD | 53,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2525.40` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 307,040.00 USD | 224,130.00 USD | 200,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2528.00` | 769,020,000.00 USD | 769,020,000.00 USD | 0.00 USD | 645,910.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2528.20` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 1,580,000.00 USD | 1,690,000.00 USD | 727,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2530.70` | 770,450,000.00 USD | 770,450,000.00 USD | 995,550.00 USD | 0.00 USD | 437,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2531.00` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 2,080,000.00 USD | 1,480,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2533.40` | 770,860,000.00 USD | 770,860,000.00 USD | 394,310.00 USD | 0.00 USD | 16,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2533.80` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 2,750,000.00 USD | 1,730,000.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2535.00` | 1,510,000.00 USD | 33,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2536.10` | 773,760,000.00 USD | 773,760,000.00 USD | 1,130,000.00 USD | 698,510.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2536.60` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 3,590,000.00 USD | 2,850,000.00 USD | 2,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2538.80` | 777,810,000.00 USD | 777,810,000.00 USD | 1,710,000.00 USD | 738,070.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2539.40` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 2,620,000.00 USD | 2,580,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2541.50` | 779,430,000.00 USD | 779,430,000.00 USD | 692,360.00 USD | 856,910.00 USD | 69,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2542.20` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 3,400,000.00 USD | 2,620,000.00 USD | 2,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2544.20` | 781,430,000.00 USD | 781,430,000.00 USD | 996,980.00 USD | 983,870.00 USD | 16,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2545.00` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 2,170,000.00 USD | 1,830,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2545.00` | 6,150,000.00 USD | 39,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2546.90` | 785,130,000.00 USD | 785,130,000.00 USD | 1,680,000.00 USD | 1,280,000.00 USD | 749,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2547.80` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 2,380,000.00 USD | 938,680.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2549.60` | 786,900,000.00 USD | 786,900,000.00 USD | 338,020.00 USD | 949,700.00 USD | 481,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2550.60` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 2,920,000.00 USD | 2,720,000.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2552.30` | 789,570,000.00 USD | 789,570,000.00 USD | 1,720,000.00 USD | 728,770.00 USD | 224,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2553.40` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 2,590,000.00 USD | 756,730.00 USD | 2,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2555.00` | 790,830,000.00 USD | 790,830,000.00 USD | 775,150.00 USD | 215,880.00 USD | 268,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2555.00` | 943,640.00 USD | 40,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2556.20` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 2,760,000.00 USD | 255,750.00 USD | 4,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2557.70` | 792,790,000.00 USD | 792,790,000.00 USD | 758,880.00 USD | 518,220.00 USD | 680,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2559.00` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 4,380,000.00 USD | 1,640,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2560.40` | 796,530,000.00 USD | 796,530,000.00 USD | 1,840,000.00 USD | 1,090,000.00 USD | 809,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2561.80` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 2,260,000.00 USD | 1,960,000.00 USD | 802,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2563.10` | 798,460,000.00 USD | 798,460,000.00 USD | 440,660.00 USD | 504,630.00 USD | 984,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2564.60` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 1,800,000.00 USD | 2,100,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2565.00` | 2,030,000.00 USD | 42,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2565.80` | 799,320,000.00 USD | 799,320,000.00 USD | 160,570.00 USD | 700,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2567.40` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 575,630.00 USD | 1,240,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2568.50` | 799,510,000.00 USD | 799,510,000.00 USD | 46,810.00 USD | 0.00 USD | 144,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2570.20` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 125,250.00 USD | 290,680.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2571.20` | 800,570,000.00 USD | 800,570,000.00 USD | 874,480.00 USD | 182,720.00 USD | 5,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2573.00` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2573.90` | 801,350,000.00 USD | 801,350,000.00 USD | 97,380.00 USD | 405,200.00 USD | 272,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2575.00` | 11,890,000.00 USD | 54,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2575.80` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 2,180,000.00 USD | 344,620.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2576.60` | 801,980,000.00 USD | 801,980,000.00 USD | 432,440.00 USD | 198,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2578.60` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 797,100.00 USD | 1,500,000.00 USD | 1,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2579.30` | 802,680,000.00 USD | 802,680,000.00 USD | 14,180.00 USD | 203,420.00 USD | 479,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2581.40` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 3,860,000.00 USD | 895,740.00 USD | 3,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2582.00` | 805,160,000.00 USD | 805,160,000.00 USD | 1,300,000.00 USD | 946,650.00 USD | 234,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2584.20` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 88,840.00 USD | 1,820,000.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2584.70` | 805,590,000.00 USD | 805,590,000.00 USD | 0.00 USD | 0.00 USD | 431,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2585.00` | 36,040,000.00 USD | 90,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2587.00` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 2,360,000.00 USD | 1,800,000.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2587.40` | 807,620,000.00 USD | 807,620,000.00 USD | 1,260,000.00 USD | 337,700.00 USD | 439,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2589.80` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 2,470,000.00 USD | 287,400.00 USD | 2,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2590.10` | 809,230,000.00 USD | 809,230,000.00 USD | 493,030.00 USD | 199,120.00 USD | 916,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2592.60` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 2,300,000.00 USD | 1,280,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2592.80` | 811,730,000.00 USD | 811,730,000.00 USD | 973,570.00 USD | 759,970.00 USD | 766,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2595.00` | 332,910.00 USD | 90,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2595.40` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 413,920.00 USD | 569,790.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2595.50` | 814,490,000.00 USD | 814,490,000.00 USD | 898,410.00 USD | 861,700.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2598.20` | 815,960,000.00 USD | 815,960,000.00 USD | 118,170.00 USD | 845,320.00 USD | 506,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2598.20` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 2,280,000.00 USD | 1,910,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2600.90` | 817,080,000.00 USD | 817,080,000.00 USD | 365,910.00 USD | 623,840.00 USD | 129,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2601.00` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 931,390.00 USD | 1,670,000.00 USD | 955,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2603.60` | 817,420,000.00 USD | 817,420,000.00 USD | 0.00 USD | 18,610.00 USD | 323,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2603.80` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 1,600,000.00 USD | 1,580,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2605.00` | 533,700.00 USD | 90,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2606.30` | 818,690,000.00 USD | 818,690,000.00 USD | 0.00 USD | 937,720.00 USD | 331,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2606.60` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 1,480,000.00 USD | 463,200.00 USD | 312,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2609.00` | 819,060,000.00 USD | 819,060,000.00 USD | 187,520.00 USD | 185,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2609.40` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 1,090,000.00 USD | 489,790.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2611.70` | 819,610,000.00 USD | 819,610,000.00 USD | 0.00 USD | 544,840.00 USD | 2,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2612.20` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 770,330.00 USD | 608,060.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2614.40` | 820,370,000.00 USD | 820,370,000.00 USD | 555,320.00 USD | 0.00 USD | 205,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2615.00` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 1,060,000.00 USD | 1,000,000.00 USD | 635,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2615.00` | 1,190,000.00 USD | 92,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2617.80` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 1,550,000.00 USD | 209,240.00 USD | 434,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2620.60` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 465,960.00 USD | 1,530,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2625.00` | 390,230.00 USD | 92,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2635.00` | 174,490.00 USD | 92,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2645.00` | 749,350.00 USD | 93,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2655.00` | 30,370,000.00 USD | 123,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2665.00` | 5,020,000.00 USD | 128,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2675.00` | 125,980.00 USD | 128,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2685.00` | 1,050,000.00 USD | 130,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2695.00` | 174,230.00 USD | 130,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2705.00` | 49,500,000.00 USD | 179,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2715.00` | 2,780,000.00 USD | 182,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2725.00` | 341,060.00 USD | 182,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2735.00` | 3,600,000.00 USD | 186,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2745.00` | 751,410.00 USD | 187,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2755.00` | 606,850.00 USD | 187,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2765.00` | 161,760.00 USD | 187,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2775.00` | 373,700.00 USD | 188,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2785.00` | 6,910,000.00 USD | 195,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2795.00` | 68,140.00 USD | 195,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2805.00` | 726,690.00 USD | 196,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2815.00` | 351,810.00 USD | 196,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2825.00` | 60,240.00 USD | 196,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2835.00` | 3,430,000.00 USD | 199,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2845.00` | 2,410,000.00 USD | 202,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2855.00` | 137,220.00 USD | 202,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2865.00` | 14,510,000.00 USD | 216,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2875.00` | 23,130,000.00 USD | 240,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2885.00` | 35,350,000.00 USD | 275,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2895.00` | 647,590.00 USD | 276,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2905.00` | 459,030.00 USD | 276,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2915.00` | 26,950,000.00 USD | 303,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2925.00` | 48,700.00 USD | 303,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2935.00` | 25,710.00 USD | 303,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2945.00` | 7,540,000.00 USD | 311,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2955.00` | 21,160,000.00 USD | 332,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2965.00` | 874,540.00 USD | 333,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2975.00` | 282,890.00 USD | 333,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2985.00` | 797,000.00 USD | 334,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2995.00` | 3,960,000.00 USD | 338,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3005.00` | 2,070,000.00 USD | 340,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3015.00` | 2,210,000.00 USD | 342,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3025.00` | 6,500,000.00 USD | 348,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3035.00` | 3,740,000.00 USD | 352,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3045.00` | 12,970,000.00 USD | 365,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3055.00` | 5,280,000.00 USD | 370,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3065.00` | 352,560.00 USD | 371,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3075.00` | 4,040,000.00 USD | 375,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3085.00` | 1,370,000.00 USD | 376,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3095.00` | 831,610.00 USD | 377,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3105.00` | 167,380.00 USD | 377,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3115.00` | 14,130.00 USD | 377,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3125.00` | 150,120.00 USD | 377,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3135.00` | 188,170.00 USD | 378,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3145.00` | 278,620.00 USD | 378,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3155.00` | 6,210,000.00 USD | 384,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3165.00` | 70,120.00 USD | 384,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3175.00` | 2,340,000.00 USD | 386,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3185.00` | 772,400.00 USD | 387,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3195.00` | 4,070,000.00 USD | 391,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3205.00` | 50,020.00 USD | 391,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3215.00` | 775,140.00 USD | 392,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3225.00` | 4,980,000.00 USD | 397,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3235.00` | 8,680,000.00 USD | 406,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3245.00` | 3,440.00 USD | 406,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3255.00` | 108,390.00 USD | 406,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3265.00` | 355,140.00 USD | 406,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3275.00` | 77,930.00 USD | 406,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3285.00` | 8,660,000.00 USD | 415,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3295.00` | 1,260,000.00 USD | 416,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3305.00` | 10,930,000.00 USD | 427,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3315.00` | 689,770.00 USD | 428,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3325.00` | 31,050.00 USD | 428,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3335.00` | 267,950.00 USD | 428,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3345.00` | 564,690.00 USD | 429,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3355.00` | 62,730,000.00 USD | 491,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3365.00` | 475,760.00 USD | 492,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3375.00` | 606,020.00 USD | 493,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3385.00` | 481,580.00 USD | 493,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3395.00` | 342,730.00 USD | 493,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3405.00` | 118,360.00 USD | 493,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3415.00` | 39,050.00 USD | 494,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3425.00` | 15,110,000.00 USD | 509,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3435.00` | 2,590,000.00 USD | 511,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3445.00` | 458,460.00 USD | 512,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3455.00` | 5,350,000.00 USD | 517,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3465.00` | 1,140,000.00 USD | 518,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3475.00` | 304,420.00 USD | 518,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3485.00` | 25,650.00 USD | 518,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3495.00` | 1,280,000.00 USD | 520,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3505.00` | 417,980.00 USD | 520,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3515.00` | 49,720.00 USD | 520,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3525.00` | 7,130,000.00 USD | 527,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3535.00` | 21,730.00 USD | 527,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3545.00` | 32,590.00 USD | 527,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3555.00` | 294,180.00 USD | 528,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3565.00` | 42,990.00 USD | 528,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3575.00` | 346,170.00 USD | 528,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3585.00` | 474,410.00 USD | 529,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3595.00` | 303,870.00 USD | 529,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3605.00` | 74,080.00 USD | 529,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3615.00` | 4,910,000.00 USD | 534,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3625.00` | 2,710,000.00 USD | 537,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3635.00` | 6,500,000.00 USD | 543,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3645.00` | 1,680,000.00 USD | 545,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3655.00` | 340,180.00 USD | 545,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3665.00` | 8,310,000.00 USD | 553,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3675.00` | 625,550.00 USD | 554,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3685.00` | 219,210.00 USD | 554,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3695.00` | 826,470.00 USD | 555,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3705.00` | 104,400,000.00 USD | 659,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3715.00` | 198,940.00 USD | 660,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3725.00` | 34,760,000.00 USD | 694,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3735.00` | 135,200.00 USD | 695,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3745.00` | 937,810.00 USD | 696,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3755.00` | 13,580,000.00 USD | 709,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3765.00` | 60,370.00 USD | 709,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3775.00` | 379,790.00 USD | 710,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3785.00` | 5,780.00 USD | 710,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3795.00` | 348,180.00 USD | 710,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3805.00` | 307,620.00 USD | 710,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3815.00` | 406,060,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3825.00` | 233,440.00 USD | 1,120,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3835.00` | 282,180.00 USD | 1,120,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3845.00` | 16,950,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3855.00` | 1,150,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3865.00` | 1,010,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3875.00` | 58,040.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3885.00` | 1,410,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3895.00` | 76,850.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3905.00` | 812,040.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3915.00` | 2,360,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3925.00` | 413,140.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3935.00` | 5,010,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3945.00` | 49,500.00 USD | 1,150,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3955.00` | 213,550.00 USD | 1,150,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3965.00` | 90,380,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3975.00` | 158,970.00 USD | 1,240,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3985.00` | 30,500,000.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3995.00` | 103,380.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4005.00` | 110,190.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4015.00` | 210,020.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4025.00` | 68,130,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4035.00` | 97,400.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4045.00` | 1,990,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4055.00` | 1,250,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4065.00` | 2,460,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4075.00` | 2,820,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4085.00` | 21,510.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4095.00` | 850,980.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4105.00` | 97,360.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4115.00` | 913.53 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4125.00` | 827,880.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4135.00` | 70,460.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4145.00` | 4,480.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4155.00` | 691,950.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4165.00` | 243,490.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4175.00` | 1,040.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4185.00` | 47,650.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4195.00` | 22,570,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4205.00` | 50,590.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4215.00` | 40,700.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4225.00` | 1,610.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4235.00` | 1,650.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4245.00` | 89,170.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4255.00` | 109,220.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4265.00` | 86,860.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4275.00` | 2,090,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4285.00` | 236,310.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4305.00` | 17,890,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4315.00` | 278,830.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4325.00` | 1,030.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4335.00` | 19,070.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4345.00` | 16,920.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4355.00` | 63,350.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4365.00` | 285,190,000.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4375.00` | 1,440,000.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4385.00` | 61,640.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4395.00` | 1,920,000.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4405.00` | 23,280.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4415.00` | 693,140.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4425.00` | 584.54 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4435.00` | 3,280,000.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4445.00` | 675,540.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4455.00` | 13,720.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4465.00` | 89,320.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4475.00` | 33,360.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4485.00` | 25,450.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4495.00` | 12,800.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4505.00` | 1,540.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4515.00` | 1,610,000.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4525.00` | 1,400.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4535.00` | 1,150,000.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4545.00` | 99,530.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4555.00` | 222,250.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4565.00` | 175,020.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4575.00` | 195,540.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4585.00` | 951,120.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4595.00` | 184,920.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4605.00` | 107,870.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4615.00` | 53,500.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4625.00` | 486,100.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4635.00` | 24,980.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4645.00` | 112,490.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4655.00` | 424,480.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4665.00` | 49,460.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4675.00` | 1,880.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4685.00` | 4,370.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `475.00` | 873,970,000.00 USD | 0.00 USD | 7,100.00 USD | `-79.71%` | `14.94` |
| `Live` | `Long` | `485.00` | 873,970,000.00 USD | 0.00 USD | 65,780.00 USD | `-79.28%` | `135.63` |
| `Live` | `Long` | `495.00` | 873,900,000.00 USD | 0.00 USD | 14,280.00 USD | `-78.86%` | `28.85` |
| `Live` | `Long` | `505.00` | 873,890,000.00 USD | 0.00 USD | 12,510.00 USD | `-78.43%` | `24.77` |
| `Live` | `Long` | `515.00` | 873,870,000.00 USD | 0.00 USD | 5,560.00 USD | `-78.00%` | `10.79` |
| `Live` | `Long` | `525.00` | 873,870,000.00 USD | 0.00 USD | 6,230.00 USD | `-77.57%` | `11.86` |
| `Live` | `Long` | `535.00` | 873,860,000.00 USD | 0.00 USD | 10,400.00 USD | `-77.15%` | `19.44` |
| `Live` | `Long` | `545.00` | 873,850,000.00 USD | 0.00 USD | 68,610.00 USD | `-76.72%` | `125.89` |
| `Live` | `Long` | `555.00` | 873,780,000.00 USD | 0.00 USD | 143,270.00 USD | `-76.29%` | `258.14` |
| `Live` | `Long` | `565.00` | 873,640,000.00 USD | 0.00 USD | 14,660.00 USD | `-75.87%` | `25.94` |
| `Live` | `Long` | `575.00` | 873,630,000.00 USD | 0.00 USD | 397,980.00 USD | `-75.44%` | `692.14` |
| `Live` | `Long` | `585.00` | 873,230,000.00 USD | 0.00 USD | 23,700.00 USD | `-75.01%` | `40.51` |
| `Live` | `Long` | `595.00` | 873,200,000.00 USD | 0.00 USD | 8,970.00 USD | `-74.58%` | `15.08` |
| `Live` | `Long` | `605.00` | 873,200,000.00 USD | 0.00 USD | 47,100.00 USD | `-74.16%` | `77.85` |
| `Live` | `Long` | `615.00` | 873,150,000.00 USD | 0.00 USD | 69,280.00 USD | `-73.73%` | `112.65` |
| `Live` | `Long` | `625.00` | 873,080,000.00 USD | 0.00 USD | 36,410.00 USD | `-73.30%` | `58.25` |
| `Live` | `Long` | `635.00` | 873,040,000.00 USD | 0.00 USD | 51,290.00 USD | `-72.87%` | `80.77` |
| `Live` | `Long` | `645.00` | 872,990,000.00 USD | 0.00 USD | 27,830.00 USD | `-72.45%` | `43.15` |
| `Live` | `Long` | `655.00` | 872,960,000.00 USD | 0.00 USD | 135,660.00 USD | `-72.02%` | `207.12` |
| `Live` | `Long` | `665.00` | 872,830,000.00 USD | 0.00 USD | 30,410.00 USD | `-71.59%` | `45.73` |
| `Live` | `Long` | `675.00` | 872,800,000.00 USD | 0.00 USD | 30,650.00 USD | `-71.17%` | `45.40` |
| `Live` | `Long` | `685.00` | 872,770,000.00 USD | 0.00 USD | 124,480.00 USD | `-70.74%` | `181.72` |
| `Live` | `Long` | `695.00` | 872,640,000.00 USD | 0.00 USD | 2,010.00 USD | `-70.31%` | `2.90` |
| `Live` | `Long` | `705.00` | 872,640,000.00 USD | 0.00 USD | 6,260.00 USD | `-69.88%` | `8.87` |
| `Live` | `Long` | `715.00` | 872,630,000.00 USD | 0.00 USD | 1,620.00 USD | `-69.46%` | `2.26` |
| `Live` | `Long` | `725.00` | 872,630,000.00 USD | 0.00 USD | 383,190.00 USD | `-69.03%` | `528.54` |
| `Live` | `Long` | `735.00` | 872,250,000.00 USD | 0.00 USD | 42,360.00 USD | `-68.60%` | `57.63` |
| `Live` | `Long` | `745.00` | 872,210,000.00 USD | 0.00 USD | 23,330.00 USD | `-68.18%` | `31.32` |
| `Live` | `Long` | `755.00` | 872,180,000.00 USD | 0.00 USD | 27,030.00 USD | `-67.75%` | `35.80` |
| `Live` | `Long` | `765.00` | 872,160,000.00 USD | 0.00 USD | 76,850.00 USD | `-67.32%` | `100.46` |
| `Live` | `Long` | `775.00` | 872,080,000.00 USD | 0.00 USD | 1,750,000.00 USD | `-66.89%` | `2,251.79` |
| `Live` | `Long` | `785.00` | 870,330,000.00 USD | 0.00 USD | 16,520.00 USD | `-66.47%` | `21.05` |
| `Live` | `Long` | `795.00` | 870,320,000.00 USD | 0.00 USD | 24,890.00 USD | `-66.04%` | `31.31` |
| `Live` | `Long` | `805.00` | 870,290,000.00 USD | 0.00 USD | 250,090.00 USD | `-65.61%` | `310.67` |
| `Live` | `Long` | `815.00` | 870,040,000.00 USD | 0.00 USD | 373,250.00 USD | `-65.19%` | `457.97` |
| `Live` | `Long` | `825.00` | 869,670,000.00 USD | 0.00 USD | 144,310.00 USD | `-64.76%` | `174.93` |
| `Live` | `Long` | `835.00` | 869,530,000.00 USD | 0.00 USD | 20,760.00 USD | `-64.33%` | `24.87` |
| `Live` | `Long` | `845.00` | 869,500,000.00 USD | 0.00 USD | 7,110.00 USD | `-63.90%` | `8.41` |
| `Live` | `Long` | `855.00` | 869,500,000.00 USD | 0.00 USD | 6,250.00 USD | `-63.48%` | `7.30` |
| `Live` | `Long` | `865.00` | 869,490,000.00 USD | 0.00 USD | 59,400.00 USD | `-63.05%` | `68.67` |
| `Live` | `Long` | `875.00` | 869,430,000.00 USD | 0.00 USD | 32,500.00 USD | `-62.62%` | `37.14` |
| `Live` | `Long` | `885.00` | 869,400,000.00 USD | 0.00 USD | 418,200.00 USD | `-62.20%` | `472.55` |
| `Live` | `Long` | `895.00` | 868,980,000.00 USD | 0.00 USD | 29,870.00 USD | `-61.77%` | `33.38` |
| `Live` | `Long` | `905.00` | 868,950,000.00 USD | 0.00 USD | 93,070.00 USD | `-61.34%` | `102.84` |
| `Live` | `Long` | `915.00` | 868,860,000.00 USD | 0.00 USD | 160,780.00 USD | `-60.91%` | `175.71` |
| `Live` | `Long` | `925.00` | 868,700,000.00 USD | 0.00 USD | 130,820.00 USD | `-60.49%` | `141.43` |
| `Live` | `Long` | `935.00` | 868,570,000.00 USD | 0.00 USD | 4,110,000.00 USD | `-60.06%` | `4,400.41` |
| `Live` | `Long` | `945.00` | 864,450,000.00 USD | 0.00 USD | 77,190.00 USD | `-59.63%` | `81.68` |
| `Live` | `Long` | `955.00` | 864,380,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-59.21%` | `1,186.88` |
| `Live` | `Long` | `965.00` | 863,240,000.00 USD | 0.00 USD | 27,170.00 USD | `-58.78%` | `28.16` |
| `Live` | `Long` | `975.00` | 863,210,000.00 USD | 0.00 USD | 67,650.00 USD | `-58.35%` | `69.38` |
| `Live` | `Long` | `985.00` | 863,150,000.00 USD | 0.00 USD | 30,850.00 USD | `-57.92%` | `31.32` |
| `Live` | `Long` | `995.00` | 863,120,000.00 USD | 0.00 USD | 226,950.00 USD | `-57.50%` | `228.09` |
| `Live` | `Long` | `1005.00` | 862,890,000.00 USD | 0.00 USD | 7,090,000.00 USD | `-57.07%` | `7,052.71` |
| `Live` | `Long` | `1015.00` | 855,800,000.00 USD | 0.00 USD | 23,200.00 USD | `-56.64%` | `22.85` |
| `Live` | `Long` | `1025.00` | 855,780,000.00 USD | 0.00 USD | 173,670.00 USD | `-56.22%` | `169.43` |
| `Live` | `Long` | `1035.00` | 855,600,000.00 USD | 0.00 USD | 41,110.00 USD | `-55.79%` | `39.72` |
| `Live` | `Long` | `1045.00` | 855,560,000.00 USD | 0.00 USD | 3,170,000.00 USD | `-55.36%` | `3,029.55` |
| `Live` | `Long` | `1055.00` | 852,400,000.00 USD | 0.00 USD | 34,380.00 USD | `-54.93%` | `32.59` |
| `Live` | `Long` | `1065.00` | 852,360,000.00 USD | 0.00 USD | 153,900.00 USD | `-54.51%` | `144.51` |
| `Live` | `Long` | `1075.00` | 852,210,000.00 USD | 0.00 USD | 675,850.00 USD | `-54.08%` | `628.69` |
| `Live` | `Long` | `1085.00` | 851,530,000.00 USD | 0.00 USD | 78,450.00 USD | `-53.65%` | `72.30` |
| `Live` | `Long` | `1095.00` | 851,450,000.00 USD | 0.00 USD | 1,770,000.00 USD | `-53.23%` | `1,616.76` |
| `Live` | `Long` | `1105.00` | 849,680,000.00 USD | 0.00 USD | 143,580.00 USD | `-52.80%` | `129.94` |
| `Live` | `Long` | `1115.00` | 849,540,000.00 USD | 0.00 USD | 88,800.00 USD | `-52.37%` | `79.64` |
| `Live` | `Long` | `1125.00` | 849,450,000.00 USD | 0.00 USD | 491,080.00 USD | `-51.94%` | `436.52` |
| `Live` | `Long` | `1135.00` | 848,960,000.00 USD | 0.00 USD | 134,860.00 USD | `-51.52%` | `118.82` |
| `Live` | `Long` | `1145.00` | 848,830,000.00 USD | 0.00 USD | 27,690.00 USD | `-51.09%` | `24.18` |
| `Live` | `Long` | `1155.00` | 848,800,000.00 USD | 0.00 USD | 351,020.00 USD | `-50.66%` | `303.92` |
| `Live` | `Long` | `1165.00` | 848,450,000.00 USD | 0.00 USD | 11,000.00 USD | `-50.23%` | `9.44` |
| `Live` | `Long` | `1175.00` | 848,440,000.00 USD | 0.00 USD | 300,400.00 USD | `-49.81%` | `255.66` |
| `Live` | `Long` | `1185.00` | 848,140,000.00 USD | 0.00 USD | 186,300.00 USD | `-49.38%` | `157.22` |
| `Live` | `Long` | `1195.00` | 847,950,000.00 USD | 0.00 USD | 368,940.00 USD | `-48.95%` | `308.74` |
| `Live` | `Long` | `1205.00` | 847,580,000.00 USD | 0.00 USD | 1,110,000.00 USD | `-48.53%` | `918.08` |
| `Live` | `Long` | `1215.00` | 846,470,000.00 USD | 0.00 USD | 11,090,000.00 USD | `-48.10%` | `9,124.44` |
| `Live` | `Long` | `1225.00` | 835,390,000.00 USD | 0.00 USD | 1,470,000.00 USD | `-47.67%` | `1,198.39` |
| `Live` | `Long` | `1235.00` | 833,920,000.00 USD | 0.00 USD | 183,930.00 USD | `-47.24%` | `148.93` |
| `Live` | `Long` | `1245.00` | 833,740,000.00 USD | 0.00 USD | 424,530.00 USD | `-46.82%` | `340.99` |
| `Live` | `Long` | `1255.00` | 833,310,000.00 USD | 0.00 USD | 385,620.00 USD | `-46.39%` | `307.27` |
| `Live` | `Long` | `1265.00` | 832,930,000.00 USD | 0.00 USD | 821,130.00 USD | `-45.96%` | `649.11` |
| `Live` | `Long` | `1275.00` | 832,110,000.00 USD | 0.00 USD | 207,090.00 USD | `-45.54%` | `162.42` |
| `Live` | `Long` | `1285.00` | 831,900,000.00 USD | 0.00 USD | 15,590,000.00 USD | `-45.11%` | `12,131.93` |
| `Live` | `Long` | `1295.00` | 816,310,000.00 USD | 0.00 USD | 135,220.00 USD | `-44.68%` | `104.42` |
| `Live` | `Long` | `1305.00` | 816,170,000.00 USD | 0.00 USD | 173,350.00 USD | `-44.25%` | `132.84` |
| `Live` | `Long` | `1315.00` | 816,000,000.00 USD | 0.00 USD | 502,710.00 USD | `-43.83%` | `382.29` |
| `Live` | `Long` | `1325.00` | 815,500,000.00 USD | 0.00 USD | 703,060.00 USD | `-43.40%` | `530.61` |
| `Live` | `Long` | `1335.00` | 814,790,000.00 USD | 0.00 USD | 289,550.00 USD | `-42.97%` | `216.89` |
| `Live` | `Long` | `1345.00` | 814,500,000.00 USD | 0.00 USD | 548,280.00 USD | `-42.55%` | `407.64` |
| `Live` | `Long` | `1355.00` | 813,960,000.00 USD | 0.00 USD | 6,750,000.00 USD | `-42.12%` | `4,981.70` |
| `Live` | `Long` | `1365.00` | 807,210,000.00 USD | 0.00 USD | 1,120,000.00 USD | `-41.69%` | `824.02` |
| `Live` | `Long` | `1375.00` | 806,080,000.00 USD | 0.00 USD | 241,210.00 USD | `-41.26%` | `175.42` |
| `Live` | `Long` | `1385.00` | 805,840,000.00 USD | 0.00 USD | 153,390.00 USD | `-40.84%` | `110.75` |
| `Live` | `Long` | `1395.00` | 805,690,000.00 USD | 0.00 USD | 15,500,000.00 USD | `-40.41%` | `11,111.71` |
| `Live` | `Long` | `1405.00` | 790,190,000.00 USD | 0.00 USD | 16,810,000.00 USD | `-39.98%` | `11,962.02` |
| `Live` | `Long` | `1415.00` | 773,380,000.00 USD | 0.00 USD | 135,850.00 USD | `-39.56%` | `96.01` |
| `Live` | `Long` | `1425.00` | 773,240,000.00 USD | 0.00 USD | 1,540,000.00 USD | `-39.13%` | `1,083.34` |
| `Live` | `Long` | `1435.00` | 771,700,000.00 USD | 0.00 USD | 291,120.00 USD | `-38.70%` | `202.87` |
| `Live` | `Long` | `1445.00` | 771,410,000.00 USD | 0.00 USD | 359,980.00 USD | `-38.27%` | `249.12` |
| `Live` | `Long` | `1455.00` | 771,050,000.00 USD | 0.00 USD | 14,630,000.00 USD | `-37.85%` | `10,054.07` |
| `Live` | `Long` | `1465.00` | 756,420,000.00 USD | 0.00 USD | 530,740.00 USD | `-37.42%` | `362.28` |
| `Live` | `Long` | `1475.00` | 755,890,000.00 USD | 0.00 USD | 2,400,000.00 USD | `-36.99%` | `1,630.48` |
| `Live` | `Long` | `1485.00` | 753,480,000.00 USD | 0.00 USD | 328,080.00 USD | `-36.57%` | `220.93` |
| `Live` | `Long` | `1495.00` | 753,160,000.00 USD | 0.00 USD | 5,000,000.00 USD | `-36.14%` | `3,345.68` |
| `Live` | `Long` | `1505.00` | 748,150,000.00 USD | 0.00 USD | 150,430.00 USD | `-35.71%` | `99.95` |
| `Live` | `Long` | `1515.00` | 748,000,000.00 USD | 0.00 USD | 369,220.00 USD | `-35.28%` | `243.71` |
| `Live` | `Long` | `1525.00` | 747,630,000.00 USD | 0.00 USD | 18,690,000.00 USD | `-34.86%` | `12,253.57` |
| `Live` | `Long` | `1535.00` | 728,950,000.00 USD | 0.00 USD | 608,550.00 USD | `-34.43%` | `396.45` |
| `Live` | `Long` | `1545.00` | 728,340,000.00 USD | 0.00 USD | 2,860,000.00 USD | `-34.00%` | `1,850.21` |
| `Live` | `Long` | `1555.00` | 725,480,000.00 USD | 0.00 USD | 25,730,000.00 USD | `-33.58%` | `16,544.61` |
| `Live` | `Long` | `1565.00` | 699,750,000.00 USD | 0.00 USD | 185,480.00 USD | `-33.15%` | `118.52` |
| `Live` | `Long` | `1575.00` | 699,570,000.00 USD | 0.00 USD | 251,000.00 USD | `-32.72%` | `159.37` |
| `Live` | `Long` | `1585.00` | 699,320,000.00 USD | 0.00 USD | 218,590.00 USD | `-32.29%` | `137.91` |
| `Live` | `Long` | `1595.00` | 699,100,000.00 USD | 0.00 USD | 7,590,000.00 USD | `-31.87%` | `4,758.47` |
| `Live` | `Long` | `1605.00` | 691,510,000.00 USD | 0.00 USD | 20,850,000.00 USD | `-31.44%` | `12,992.70` |
| `Live` | `Long` | `1615.00` | 670,660,000.00 USD | 0.00 USD | 119,070.00 USD | `-31.01%` | `73.73` |
| `Live` | `Long` | `1625.00` | 670,540,000.00 USD | 0.00 USD | 620,560.00 USD | `-30.59%` | `381.88` |
| `Live` | `Long` | `1635.00` | 669,920,000.00 USD | 0.00 USD | 18,320,000.00 USD | `-30.16%` | `11,206.97` |
| `Live` | `Long` | `1645.00` | 651,590,000.00 USD | 0.00 USD | 59,700,000.00 USD | `-29.73%` | `36,293.43` |
| `Live` | `Long` | `1655.00` | 591,890,000.00 USD | 0.00 USD | 602,670.00 USD | `-29.30%` | `364.15` |
| `Live` | `Long` | `1665.00` | 591,290,000.00 USD | 0.00 USD | 1,110,000.00 USD | `-28.88%` | `665.90` |
| `Live` | `Long` | `1675.00` | 590,180,000.00 USD | 0.00 USD | 12,040,000.00 USD | `-28.45%` | `7,189.86` |
| `Live` | `Long` | `1685.00` | 578,140,000.00 USD | 0.00 USD | 1,390,000.00 USD | `-28.02%` | `823.20` |
| `Live` | `Long` | `1695.00` | 576,750,000.00 USD | 0.00 USD | 460,530.00 USD | `-27.60%` | `271.70` |
| `Live` | `Long` | `1705.00` | 576,290,000.00 USD | 0.00 USD | 1,510,000.00 USD | `-27.17%` | `887.69` |
| `Live` | `Long` | `1715.00` | 574,770,000.00 USD | 0.00 USD | 12,670,000.00 USD | `-26.74%` | `7,389.03` |
| `Live` | `Long` | `1725.00` | 562,100,000.00 USD | 0.00 USD | 17,850,000.00 USD | `-26.31%` | `10,345.09` |
| `Live` | `Long` | `1735.00` | 544,260,000.00 USD | 0.00 USD | 17,950,000.00 USD | `-25.89%` | `10,346.03` |
| `Live` | `Long` | `1745.00` | 526,310,000.00 USD | 0.00 USD | 1,150,000.00 USD | `-25.46%` | `659.78` |
| `Live` | `Long` | `1755.00` | 525,160,000.00 USD | 0.00 USD | 1,400,000.00 USD | `-25.03%` | `796.69` |
| `Live` | `Long` | `1765.00` | 523,760,000.00 USD | 0.00 USD | 874,200.00 USD | `-24.60%` | `495.30` |
| `Live` | `Long` | `1775.00` | 522,880,000.00 USD | 0.00 USD | 14,290,000.00 USD | `-24.18%` | `8,051.70` |
| `Live` | `Long` | `1785.00` | 508,590,000.00 USD | 0.00 USD | 54,540,000.00 USD | `-23.75%` | `30,554.96` |
| `Live` | `Long` | `1795.00` | 454,050,000.00 USD | 0.00 USD | 3,520,000.00 USD | `-23.32%` | `1,962.35` |
| `Live` | `Long` | `1805.00` | 450,530,000.00 USD | 0.00 USD | 1,640,000.00 USD | `-22.90%` | `906.23` |
| `Live` | `Long` | `1815.00` | 448,890,000.00 USD | 0.00 USD | 331,980.00 USD | `-22.47%` | `182.91` |
| `Live` | `Long` | `1825.00` | 448,560,000.00 USD | 0.00 USD | 1,940,000.00 USD | `-22.04%` | `1,064.38` |
| `Live` | `Long` | `1835.00` | 446,620,000.00 USD | 0.00 USD | 847,330.00 USD | `-21.61%` | `461.76` |
| `Live` | `Long` | `1845.00` | 445,770,000.00 USD | 0.00 USD | 8,960,000.00 USD | `-21.19%` | `4,856.89` |
| `Live` | `Long` | `1855.00` | 436,810,000.00 USD | 0.00 USD | 2,850,000.00 USD | `-20.76%` | `1,535.00` |
| `Live` | `Long` | `1865.00` | 433,960,000.00 USD | 0.00 USD | 5,430,000.00 USD | `-20.33%` | `2,910.91` |
| `Live` | `Long` | `1875.00` | 428,530,000.00 USD | 0.00 USD | 5,660,000.00 USD | `-19.91%` | `3,017.75` |
| `Live` | `Long` | `1885.00` | 422,880,000.00 USD | 0.00 USD | 2,680,000.00 USD | `-19.48%` | `1,421.91` |
| `Live` | `Long` | `1895.00` | 420,190,000.00 USD | 0.00 USD | 5,390,000.00 USD | `-19.05%` | `2,842.25` |
| `Live` | `Long` | `1905.00` | 414,810,000.00 USD | 0.00 USD | 1,570,000.00 USD | `-18.62%` | `824.77` |
| `Live` | `Long` | `1915.00` | 413,240,000.00 USD | 0.00 USD | 28,410,000.00 USD | `-18.20%` | `14,833.49` |
| `Live` | `Long` | `1925.00` | 384,830,000.00 USD | 0.00 USD | 3,380,000.00 USD | `-17.77%` | `1,757.28` |
| `Live` | `Long` | `1935.00` | 381,450,000.00 USD | 0.00 USD | 2,270,000.00 USD | `-17.34%` | `1,170.98` |
| `Live` | `Long` | `1945.00` | 379,180,000.00 USD | 0.00 USD | 635,200.00 USD | `-16.92%` | `326.58` |
| `Live` | `Long` | `1955.00` | 378,550,000.00 USD | 0.00 USD | 2,610,000.00 USD | `-16.49%` | `1,335.71` |
| `Live` | `Long` | `1965.00` | 375,940,000.00 USD | 0.00 USD | 1,200,000.00 USD | `-16.06%` | `608.94` |
| `Live` | `Long` | `1975.00` | 374,740,000.00 USD | 0.00 USD | 6,040,000.00 USD | `-15.63%` | `3,060.72` |
| `Live` | `Long` | `1985.00` | 368,690,000.00 USD | 0.00 USD | 4,410,000.00 USD | `-15.21%` | `2,220.98` |
| `Live` | `Long` | `1995.00` | 364,290,000.00 USD | 0.00 USD | 658,250.00 USD | `-14.78%` | `329.95` |
| `Live` | `Long` | `2005.00` | 363,630,000.00 USD | 0.00 USD | 3,690,000.00 USD | `-14.35%` | `1,841.13` |
| `Live` | `Long` | `2015.00` | 359,940,000.00 USD | 0.00 USD | 2,570,000.00 USD | `-13.93%` | `1,275.65` |
| `Live` | `Long` | `2025.00` | 357,370,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-13.50%` | `541.06` |
| `Live` | `Long` | `2035.00` | 356,270,000.00 USD | 0.00 USD | 5,320,000.00 USD | `-13.07%` | `2,613.04` |
| `Live` | `Long` | `2045.00` | 350,950,000.00 USD | 0.00 USD | 17,040,000.00 USD | `-12.64%` | `8,330.82` |
| `Live` | `Long` | `2055.00` | 333,920,000.00 USD | 0.00 USD | 4,070,000.00 USD | `-12.22%` | `1,982.24` |
| `Live` | `Long` | `2065.00` | 329,840,000.00 USD | 0.00 USD | 1,310,000.00 USD | `-11.79%` | `636.55` |
| `Live` | `Long` | `2075.00` | 328,530,000.00 USD | 0.00 USD | 599,560.00 USD | `-11.36%` | `288.94` |
| `Live` | `Long` | `2085.00` | 327,930,000.00 USD | 0.00 USD | 2,870,000.00 USD | `-10.94%` | `1,377.40` |
| `Live` | `Long` | `2095.00` | 325,060,000.00 USD | 0.00 USD | 5,740,000.00 USD | `-10.51%` | `2,742.10` |
| `Live` | `Long` | `2105.00` | 319,310,000.00 USD | 0.00 USD | 1,420,000.00 USD | `-10.08%` | `672.35` |
| `Live` | `Long` | `2115.00` | 317,900,000.00 USD | 0.00 USD | 17,610,000.00 USD | `-9.65%` | `8,326.54` |
| `Live` | `Long` | `2125.00` | 300,290,000.00 USD | 0.00 USD | 1,030,000.00 USD | `-9.23%` | `485.03` |
| `Live` | `Long` | `2135.00` | 299,260,000.00 USD | 0.00 USD | 2,720,000.00 USD | `-8.80%` | `1,272.21` |
| `Live` | `Long` | `2145.00` | 296,540,000.00 USD | 0.00 USD | 9,660,000.00 USD | `-8.37%` | `4,504.10` |
| `Live` | `Long` | `2155.00` | 286,880,000.00 USD | 0.00 USD | 23,300,000.00 USD | `-7.95%` | `10,810.79` |
| `Live` | `Long` | `2165.00` | 263,580,000.00 USD | 0.00 USD | 857,510.00 USD | `-7.52%` | `396.08` |
| `Live` | `Long` | `2175.00` | 262,720,000.00 USD | 0.00 USD | 108,630,000.00 USD | `-7.09%` | `49,946.09` |
| `Live` | `Long` | `2185.00` | 154,090,000.00 USD | 0.00 USD | 111,630,000.00 USD | `-6.66%` | `51,087.81` |
| `Live` | `Long` | `2195.00` | 42,460,000.00 USD | 0.00 USD | 1,510,000.00 USD | `-6.24%` | `688.75` |
| `Live` | `Long` | `2205.00` | 40,950,000.00 USD | 0.00 USD | 1,240,000.00 USD | `-5.81%` | `564.60` |
| `Live` | `Long` | `2215.00` | 39,710,000.00 USD | 0.00 USD | 1,970,000.00 USD | `-5.38%` | `889.65` |
| `Live` | `Long` | `2225.00` | 37,740,000.00 USD | 0.00 USD | 2,130,000.00 USD | `-4.96%` | `956.10` |
| `Live` | `Long` | `2235.00` | 35,610,000.00 USD | 0.00 USD | 671,070.00 USD | `-4.53%` | `300.26` |
| `Live` | `Long` | `2245.00` | 34,940,000.00 USD | 0.00 USD | 4,720,000.00 USD | `-4.10%` | `2,103.32` |
| `Live` | `Long` | `2255.00` | 30,220,000.00 USD | 0.00 USD | 11,410,000.00 USD | `-3.67%` | `5,059.48` |
| `Live` | `Long` | `2265.00` | 18,810,000.00 USD | 0.00 USD | 5,260,000.00 USD | `-3.25%` | `2,321.38` |
| `Live` | `Long` | `2275.00` | 13,550,000.00 USD | 0.00 USD | 3,330,000.00 USD | `-2.82%` | `1,463.09` |
| `Live` | `Long` | `2285.00` | 10,220,000.00 USD | 0.00 USD | 5,830,000.00 USD | `-2.39%` | `2,550.86` |
| `Live` | `Long` | `2295.00` | 4,390,000.00 USD | 0.00 USD | 1,910,000.00 USD | `-1.96%` | `831.77` |
| `Live` | `Long` | `2305.00` | 2,480,000.00 USD | 0.00 USD | 1,080,000.00 USD | `-1.54%` | `469.60` |
| `Live` | `Short` | `2315.00` | 657,320.00 USD | 657,320.00 USD | 0.00 USD | `-1.11%` | `283.94` |
| `Live` | `Long` | `2325.00` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | `-0.68%` | `601.87` |
| `Live` | `Long` | `2335.00` | 1,060.00 USD | 0.00 USD | 1,060.00 USD | `-0.26%` | `0.45` |
| `Live` | `Short` | `2345.00` | 662,460.00 USD | 5,140.00 USD | 0.00 USD | `+0.17%` | `2.19` |
| `Live` | `Short` | `2355.00` | 735,980.00 USD | 73,520.00 USD | 0.00 USD | `+0.60%` | `31.22` |
| `Live` | `Short` | `2365.00` | 738,870.00 USD | 2,900.00 USD | 0.00 USD | `+1.03%` | `1.23` |
| `Live` | `Short` | `2375.00` | 755,550.00 USD | 16,680.00 USD | 0.00 USD | `+1.45%` | `7.02` |
| `Live` | `Short` | `2385.00` | 4,080,000.00 USD | 3,320,000.00 USD | 0.00 USD | `+1.88%` | `1,392.95` |
| `Live` | `Short` | `2395.00` | 4,170,000.00 USD | 91,230.00 USD | 0.00 USD | `+2.31%` | `38.09` |
| `Live` | `Short` | `2405.00` | 17,460,000.00 USD | 13,290,000.00 USD | 0.00 USD | `+2.73%` | `5,526.12` |
| `Live` | `Short` | `2415.00` | 17,820,000.00 USD | 362,060.00 USD | 0.00 USD | `+3.16%` | `149.92` |
| `Live` | `Short` | `2425.00` | 18,710,000.00 USD | 890,120.00 USD | 0.00 USD | `+3.59%` | `367.06` |
| `Live` | `Short` | `2435.00` | 26,480,000.00 USD | 7,770,000.00 USD | 0.00 USD | `+4.02%` | `3,191.53` |
| `Live` | `Short` | `2445.00` | 26,630,000.00 USD | 149,300.00 USD | 0.00 USD | `+4.44%` | `61.06` |
| `Live` | `Short` | `2455.00` | 26,920,000.00 USD | 288,140.00 USD | 0.00 USD | `+4.87%` | `117.37` |
| `Live` | `Short` | `2465.00` | 27,100,000.00 USD | 180,420.00 USD | 0.00 USD | `+5.30%` | `73.19` |
| `Live` | `Short` | `2475.00` | 27,130,000.00 USD | 32,880.00 USD | 0.00 USD | `+5.72%` | `13.28` |
| `Live` | `Short` | `2485.00` | 27,720,000.00 USD | 589,540.00 USD | 0.00 USD | `+6.15%` | `237.24` |
| `Live` | `Short` | `2495.00` | 30,070,000.00 USD | 2,340,000.00 USD | 0.00 USD | `+6.58%` | `939.33` |
| `Live` | `Short` | `2505.00` | 30,310,000.00 USD | 244,330.00 USD | 0.00 USD | `+7.01%` | `97.54` |
| `Live` | `Short` | `2515.00` | 30,430,000.00 USD | 118,730.00 USD | 0.00 USD | `+7.43%` | `47.21` |
| `Live` | `Short` | `2525.00` | 31,510,000.00 USD | 1,080,000.00 USD | 0.00 USD | `+7.86%` | `428.42` |
| `Live` | `Short` | `2535.00` | 33,020,000.00 USD | 1,510,000.00 USD | 0.00 USD | `+8.29%` | `596.33` |
| `Live` | `Short` | `2545.00` | 39,170,000.00 USD | 6,150,000.00 USD | 0.00 USD | `+8.71%` | `2,414.90` |
| `Live` | `Short` | `2555.00` | 40,110,000.00 USD | 943,640.00 USD | 0.00 USD | `+9.14%` | `369.33` |
| `Live` | `Short` | `2565.00` | 42,150,000.00 USD | 2,030,000.00 USD | 0.00 USD | `+9.57%` | `793.33` |
| `Live` | `Short` | `2575.00` | 54,030,000.00 USD | 11,890,000.00 USD | 0.00 USD | `+10.00%` | `4,615.55` |
| `Live` | `Short` | `2585.00` | 90,070,000.00 USD | 36,040,000.00 USD | 0.00 USD | `+10.42%` | `13,940.66` |
| `Live` | `Short` | `2595.00` | 90,400,000.00 USD | 332,910.00 USD | 0.00 USD | `+10.85%` | `128.29` |
| `Live` | `Short` | `2605.00` | 90,940,000.00 USD | 533,700.00 USD | 0.00 USD | `+11.28%` | `204.87` |
| `Live` | `Short` | `2615.00` | 92,120,000.00 USD | 1,190,000.00 USD | 0.00 USD | `+11.70%` | `454.20` |
| `Live` | `Short` | `2625.00` | 92,510,000.00 USD | 390,230.00 USD | 0.00 USD | `+12.13%` | `148.66` |
| `Live` | `Short` | `2635.00` | 92,690,000.00 USD | 174,490.00 USD | 0.00 USD | `+12.56%` | `66.22` |
| `Live` | `Short` | `2645.00` | 93,440,000.00 USD | 749,350.00 USD | 0.00 USD | `+12.99%` | `283.31` |
| `Live` | `Short` | `2655.00` | 123,810,000.00 USD | 30,370,000.00 USD | 0.00 USD | `+13.41%` | `11,438.73` |
| `Live` | `Short` | `2665.00` | 128,830,000.00 USD | 5,020,000.00 USD | 0.00 USD | `+13.84%` | `1,884.58` |
| `Live` | `Short` | `2675.00` | 128,960,000.00 USD | 125,980.00 USD | 0.00 USD | `+14.27%` | `47.09` |
| `Live` | `Short` | `2685.00` | 130,010,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+14.69%` | `391.96` |
| `Live` | `Short` | `2695.00` | 130,180,000.00 USD | 174,230.00 USD | 0.00 USD | `+15.12%` | `64.65` |
| `Live` | `Short` | `2705.00` | 179,680,000.00 USD | 49,500,000.00 USD | 0.00 USD | `+15.55%` | `18,299.48` |
| `Live` | `Short` | `2715.00` | 182,460,000.00 USD | 2,780,000.00 USD | 0.00 USD | `+15.98%` | `1,023.56` |
| `Live` | `Short` | `2725.00` | 182,800,000.00 USD | 341,060.00 USD | 0.00 USD | `+16.40%` | `125.16` |
| `Live` | `Short` | `2735.00` | 186,400,000.00 USD | 3,600,000.00 USD | 0.00 USD | `+16.83%` | `1,316.74` |
| `Live` | `Short` | `2745.00` | 187,160,000.00 USD | 751,410.00 USD | 0.00 USD | `+17.26%` | `273.74` |
| `Live` | `Short` | `2755.00` | 187,760,000.00 USD | 606,850.00 USD | 0.00 USD | `+17.68%` | `220.27` |
| `Live` | `Short` | `2765.00` | 187,920,000.00 USD | 161,760.00 USD | 0.00 USD | `+18.11%` | `58.50` |
| `Live` | `Short` | `2775.00` | 188,300,000.00 USD | 373,700.00 USD | 0.00 USD | `+18.54%` | `134.67` |
| `Live` | `Short` | `2785.00` | 195,210,000.00 USD | 6,910,000.00 USD | 0.00 USD | `+18.97%` | `2,480.21` |
| `Live` | `Short` | `2795.00` | 195,270,000.00 USD | 68,140.00 USD | 0.00 USD | `+19.39%` | `24.38` |
| `Live` | `Short` | `2805.00` | 196,000,000.00 USD | 726,690.00 USD | 0.00 USD | `+19.82%` | `259.07` |
| `Live` | `Short` | `2815.00` | 196,350,000.00 USD | 351,810.00 USD | 0.00 USD | `+20.25%` | `124.98` |
| `Live` | `Short` | `2825.00` | 196,410,000.00 USD | 60,240.00 USD | 0.00 USD | `+20.67%` | `21.33` |
| `Live` | `Short` | `2835.00` | 199,840,000.00 USD | 3,430,000.00 USD | 0.00 USD | `+21.10%` | `1,209.85` |
| `Live` | `Short` | `2845.00` | 202,260,000.00 USD | 2,410,000.00 USD | 0.00 USD | `+21.53%` | `848.29` |
| `Live` | `Short` | `2855.00` | 202,390,000.00 USD | 137,220.00 USD | 0.00 USD | `+21.96%` | `48.06` |
| `Live` | `Short` | `2865.00` | 216,900,000.00 USD | 14,510,000.00 USD | 0.00 USD | `+22.38%` | `5,065.29` |
| `Live` | `Short` | `2875.00` | 240,040,000.00 USD | 23,130,000.00 USD | 0.00 USD | `+22.81%` | `8,045.70` |
| `Live` | `Short` | `2885.00` | 275,390,000.00 USD | 35,350,000.00 USD | 0.00 USD | `+23.24%` | `12,254.51` |
| `Live` | `Short` | `2895.00` | 276,040,000.00 USD | 647,590.00 USD | 0.00 USD | `+23.67%` | `223.69` |
| `Live` | `Short` | `2905.00` | 276,500,000.00 USD | 459,030.00 USD | 0.00 USD | `+24.09%` | `158.01` |
| `Live` | `Short` | `2915.00` | 303,450,000.00 USD | 26,950,000.00 USD | 0.00 USD | `+24.52%` | `9,245.32` |
| `Live` | `Short` | `2925.00` | 303,500,000.00 USD | 48,700.00 USD | 0.00 USD | `+24.95%` | `16.65` |
| `Live` | `Short` | `2935.00` | 303,520,000.00 USD | 25,710.00 USD | 0.00 USD | `+25.37%` | `8.76` |
| `Live` | `Short` | `2945.00` | 311,070,000.00 USD | 7,540,000.00 USD | 0.00 USD | `+25.80%` | `2,561.88` |
| `Live` | `Short` | `2955.00` | 332,230,000.00 USD | 21,160,000.00 USD | 0.00 USD | `+26.23%` | `7,162.10` |
| `Live` | `Short` | `2965.00` | 333,100,000.00 USD | 874,540.00 USD | 0.00 USD | `+26.66%` | `294.95` |
| `Live` | `Short` | `2975.00` | 333,390,000.00 USD | 282,890.00 USD | 0.00 USD | `+27.08%` | `95.09` |
| `Live` | `Short` | `2985.00` | 334,180,000.00 USD | 797,000.00 USD | 0.00 USD | `+27.51%` | `267.00` |
| `Live` | `Short` | `2995.00` | 338,140,000.00 USD | 3,960,000.00 USD | 0.00 USD | `+27.94%` | `1,321.59` |
| `Live` | `Short` | `3005.00` | 340,210,000.00 USD | 2,070,000.00 USD | 0.00 USD | `+28.36%` | `689.58` |
| `Live` | `Short` | `3015.00` | 342,430,000.00 USD | 2,210,000.00 USD | 0.00 USD | `+28.79%` | `733.21` |
| `Live` | `Short` | `3025.00` | 348,930,000.00 USD | 6,500,000.00 USD | 0.00 USD | `+29.22%` | `2,149.89` |
| `Live` | `Short` | `3035.00` | 352,670,000.00 USD | 3,740,000.00 USD | 0.00 USD | `+29.65%` | `1,233.72` |
| `Live` | `Short` | `3045.00` | 365,650,000.00 USD | 12,970,000.00 USD | 0.00 USD | `+30.07%` | `4,260.37` |
| `Live` | `Short` | `3055.00` | 370,920,000.00 USD | 5,280,000.00 USD | 0.00 USD | `+30.50%` | `1,727.18` |
| `Live` | `Short` | `3065.00` | 371,280,000.00 USD | 352,560.00 USD | 0.00 USD | `+30.93%` | `115.03` |
| `Live` | `Short` | `3075.00` | 375,320,000.00 USD | 4,040,000.00 USD | 0.00 USD | `+31.35%` | `1,314.90` |
| `Live` | `Short` | `3085.00` | 376,690,000.00 USD | 1,370,000.00 USD | 0.00 USD | `+31.78%` | `443.84` |
| `Live` | `Short` | `3095.00` | 377,520,000.00 USD | 831,610.00 USD | 0.00 USD | `+32.21%` | `268.69` |
| `Live` | `Short` | `3105.00` | 377,690,000.00 USD | 167,380.00 USD | 0.00 USD | `+32.64%` | `53.91` |
| `Live` | `Short` | `3115.00` | 377,700,000.00 USD | 14,130.00 USD | 0.00 USD | `+33.06%` | `4.54` |
| `Live` | `Short` | `3125.00` | 377,850,000.00 USD | 150,120.00 USD | 0.00 USD | `+33.49%` | `48.04` |
| `Live` | `Short` | `3135.00` | 378,040,000.00 USD | 188,170.00 USD | 0.00 USD | `+33.92%` | `60.02` |
| `Live` | `Short` | `3145.00` | 378,320,000.00 USD | 278,620.00 USD | 0.00 USD | `+34.34%` | `88.59` |
| `Live` | `Short` | `3155.00` | 384,520,000.00 USD | 6,210,000.00 USD | 0.00 USD | `+34.77%` | `1,967.08` |
| `Live` | `Short` | `3165.00` | 384,590,000.00 USD | 70,120.00 USD | 0.00 USD | `+35.20%` | `22.16` |
| `Live` | `Short` | `3175.00` | 386,930,000.00 USD | 2,340,000.00 USD | 0.00 USD | `+35.63%` | `737.16` |
| `Live` | `Short` | `3185.00` | 387,710,000.00 USD | 772,400.00 USD | 0.00 USD | `+36.05%` | `242.51` |
| `Live` | `Short` | `3195.00` | 391,770,000.00 USD | 4,070,000.00 USD | 0.00 USD | `+36.48%` | `1,272.55` |
| `Live` | `Short` | `3205.00` | 391,820,000.00 USD | 50,020.00 USD | 0.00 USD | `+36.91%` | `15.61` |
| `Live` | `Short` | `3215.00` | 392,600,000.00 USD | 775,140.00 USD | 0.00 USD | `+37.33%` | `241.10` |
| `Live` | `Short` | `3225.00` | 397,580,000.00 USD | 4,980,000.00 USD | 0.00 USD | `+37.76%` | `1,545.18` |
| `Live` | `Short` | `3235.00` | 406,260,000.00 USD | 8,680,000.00 USD | 0.00 USD | `+38.19%` | `2,682.59` |
| `Live` | `Short` | `3245.00` | 406,260,000.00 USD | 3,440.00 USD | 0.00 USD | `+38.62%` | `1.06` |
| `Live` | `Short` | `3255.00` | 406,370,000.00 USD | 108,390.00 USD | 0.00 USD | `+39.04%` | `33.30` |
| `Live` | `Short` | `3265.00` | 406,730,000.00 USD | 355,140.00 USD | 0.00 USD | `+39.47%` | `108.77` |
| `Live` | `Short` | `3275.00` | 406,800,000.00 USD | 77,930.00 USD | 0.00 USD | `+39.90%` | `23.80` |
| `Live` | `Short` | `3285.00` | 415,460,000.00 USD | 8,660,000.00 USD | 0.00 USD | `+40.32%` | `2,635.24` |
| `Live` | `Short` | `3295.00` | 416,720,000.00 USD | 1,260,000.00 USD | 0.00 USD | `+40.75%` | `383.35` |
| `Live` | `Short` | `3305.00` | 427,660,000.00 USD | 10,930,000.00 USD | 0.00 USD | `+41.18%` | `3,308.58` |
| `Live` | `Short` | `3315.00` | 428,350,000.00 USD | 689,770.00 USD | 0.00 USD | `+41.61%` | `208.08` |
| `Live` | `Short` | `3325.00` | 428,380,000.00 USD | 31,050.00 USD | 0.00 USD | `+42.03%` | `9.34` |
| `Live` | `Short` | `3335.00` | 428,650,000.00 USD | 267,950.00 USD | 0.00 USD | `+42.46%` | `80.34` |
| `Live` | `Short` | `3345.00` | 429,210,000.00 USD | 564,690.00 USD | 0.00 USD | `+42.89%` | `168.82` |
| `Live` | `Short` | `3355.00` | 491,940,000.00 USD | 62,730,000.00 USD | 0.00 USD | `+43.31%` | `18,696.41` |
| `Live` | `Short` | `3365.00` | 492,410,000.00 USD | 475,760.00 USD | 0.00 USD | `+43.74%` | `141.38` |
| `Live` | `Short` | `3375.00` | 493,020,000.00 USD | 606,020.00 USD | 0.00 USD | `+44.17%` | `179.56` |
| `Live` | `Short` | `3385.00` | 493,500,000.00 USD | 481,580.00 USD | 0.00 USD | `+44.60%` | `142.27` |
| `Live` | `Short` | `3395.00` | 493,850,000.00 USD | 342,730.00 USD | 0.00 USD | `+45.02%` | `100.95` |
| `Live` | `Short` | `3405.00` | 493,960,000.00 USD | 118,360.00 USD | 0.00 USD | `+45.45%` | `34.76` |
| `Live` | `Short` | `3415.00` | 494,000,000.00 USD | 39,050.00 USD | 0.00 USD | `+45.88%` | `11.44` |
| `Live` | `Short` | `3425.00` | 509,110,000.00 USD | 15,110,000.00 USD | 0.00 USD | `+46.30%` | `4,411.99` |
| `Live` | `Short` | `3435.00` | 511,710,000.00 USD | 2,590,000.00 USD | 0.00 USD | `+46.73%` | `755.15` |
| `Live` | `Short` | `3445.00` | 512,170,000.00 USD | 458,460.00 USD | 0.00 USD | `+47.16%` | `133.08` |
| `Live` | `Short` | `3455.00` | 517,520,000.00 USD | 5,350,000.00 USD | 0.00 USD | `+47.59%` | `1,549.00` |
| `Live` | `Short` | `3465.00` | 518,650,000.00 USD | 1,140,000.00 USD | 0.00 USD | `+48.01%` | `328.14` |
| `Live` | `Short` | `3475.00` | 518,960,000.00 USD | 304,420.00 USD | 0.00 USD | `+48.44%` | `87.60` |
| `Live` | `Short` | `3485.00` | 518,980,000.00 USD | 25,650.00 USD | 0.00 USD | `+48.87%` | `7.36` |
| `Live` | `Short` | `3495.00` | 520,260,000.00 USD | 1,280,000.00 USD | 0.00 USD | `+49.30%` | `364.98` |
| `Live` | `Short` | `3505.00` | 520,680,000.00 USD | 417,980.00 USD | 0.00 USD | `+49.72%` | `119.25` |
| `Live` | `Short` | `3515.00` | 520,730,000.00 USD | 49,720.00 USD | 0.00 USD | `+50.15%` | `14.15` |
| `Live` | `Short` | `3525.00` | 527,860,000.00 USD | 7,130,000.00 USD | 0.00 USD | `+50.58%` | `2,023.32` |
| `Live` | `Short` | `3535.00` | 527,880,000.00 USD | 21,730.00 USD | 0.00 USD | `+51.00%` | `6.15` |
| `Live` | `Short` | `3545.00` | 527,910,000.00 USD | 32,590.00 USD | 0.00 USD | `+51.43%` | `9.19` |
| `Live` | `Short` | `3555.00` | 528,210,000.00 USD | 294,180.00 USD | 0.00 USD | `+51.86%` | `82.75` |
| `Live` | `Short` | `3565.00` | 528,250,000.00 USD | 42,990.00 USD | 0.00 USD | `+52.29%` | `12.06` |
| `Live` | `Short` | `3575.00` | 528,600,000.00 USD | 346,170.00 USD | 0.00 USD | `+52.71%` | `96.83` |
| `Live` | `Short` | `3585.00` | 529,070,000.00 USD | 474,410.00 USD | 0.00 USD | `+53.14%` | `132.33` |
| `Live` | `Short` | `3595.00` | 529,380,000.00 USD | 303,870.00 USD | 0.00 USD | `+53.57%` | `84.53` |
| `Live` | `Short` | `3605.00` | 529,450,000.00 USD | 74,080.00 USD | 0.00 USD | `+53.99%` | `20.55` |
| `Live` | `Short` | `3615.00` | 534,360,000.00 USD | 4,910,000.00 USD | 0.00 USD | `+54.42%` | `1,357.25` |
| `Live` | `Short` | `3625.00` | 537,060,000.00 USD | 2,710,000.00 USD | 0.00 USD | `+54.85%` | `746.23` |
| `Live` | `Short` | `3635.00` | 543,560,000.00 USD | 6,500,000.00 USD | 0.00 USD | `+55.28%` | `1,788.44` |
| `Live` | `Short` | `3645.00` | 545,250,000.00 USD | 1,680,000.00 USD | 0.00 USD | `+55.70%` | `462.20` |
| `Live` | `Short` | `3655.00` | 545,590,000.00 USD | 340,180.00 USD | 0.00 USD | `+56.13%` | `93.07` |
| `Live` | `Short` | `3665.00` | 553,900,000.00 USD | 8,310,000.00 USD | 0.00 USD | `+56.56%` | `2,268.26` |
| `Live` | `Short` | `3675.00` | 554,530,000.00 USD | 625,550.00 USD | 0.00 USD | `+56.98%` | `170.22` |
| `Live` | `Short` | `3685.00` | 554,750,000.00 USD | 219,210.00 USD | 0.00 USD | `+57.41%` | `59.49` |
| `Live` | `Short` | `3695.00` | 555,570,000.00 USD | 826,470.00 USD | 0.00 USD | `+57.84%` | `223.67` |
| `Live` | `Short` | `3705.00` | 659,980,000.00 USD | 104,400,000.00 USD | 0.00 USD | `+58.27%` | `28,179.37` |
| `Live` | `Short` | `3715.00` | 660,180,000.00 USD | 198,940.00 USD | 0.00 USD | `+58.69%` | `53.55` |
| `Live` | `Short` | `3725.00` | 694,940,000.00 USD | 34,760,000.00 USD | 0.00 USD | `+59.12%` | `9,332.45` |
| `Live` | `Short` | `3735.00` | 695,070,000.00 USD | 135,200.00 USD | 0.00 USD | `+59.55%` | `36.20` |
| `Live` | `Short` | `3745.00` | 696,010,000.00 USD | 937,810.00 USD | 0.00 USD | `+59.97%` | `250.42` |
| `Live` | `Short` | `3755.00` | 709,600,000.00 USD | 13,580,000.00 USD | 0.00 USD | `+60.40%` | `3,617.83` |
| `Live` | `Short` | `3765.00` | 709,660,000.00 USD | 60,370.00 USD | 0.00 USD | `+60.83%` | `16.03` |
| `Live` | `Short` | `3775.00` | 710,040,000.00 USD | 379,790.00 USD | 0.00 USD | `+61.26%` | `100.61` |
| `Live` | `Short` | `3785.00` | 710,040,000.00 USD | 5,780.00 USD | 0.00 USD | `+61.68%` | `1.53` |
| `Live` | `Short` | `3795.00` | 710,390,000.00 USD | 348,180.00 USD | 0.00 USD | `+62.11%` | `91.75` |
| `Live` | `Short` | `3805.00` | 710,700,000.00 USD | 307,620.00 USD | 0.00 USD | `+62.54%` | `80.85` |
| `Live` | `Short` | `3815.00` | 1,120,000,000.00 USD | 406,060,000.00 USD | 0.00 USD | `+62.96%` | `106,438.44` |
| `Live` | `Short` | `3825.00` | 1,120,000,000.00 USD | 233,440.00 USD | 0.00 USD | `+63.39%` | `61.03` |
| `Live` | `Short` | `3835.00` | 1,120,000,000.00 USD | 282,180.00 USD | 0.00 USD | `+63.82%` | `73.58` |
| `Live` | `Short` | `3845.00` | 1,130,000,000.00 USD | 16,950,000.00 USD | 0.00 USD | `+64.25%` | `4,408.00` |
| `Live` | `Short` | `3855.00` | 1,140,000,000.00 USD | 1,150,000.00 USD | 0.00 USD | `+64.67%` | `297.48` |
| `Live` | `Short` | `3865.00` | 1,140,000,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+65.10%` | `261.42` |
| `Live` | `Short` | `3875.00` | 1,140,000,000.00 USD | 58,040.00 USD | 0.00 USD | `+65.53%` | `14.98` |
| `Live` | `Short` | `3885.00` | 1,140,000,000.00 USD | 1,410,000.00 USD | 0.00 USD | `+65.95%` | `363.97` |
| `Live` | `Short` | `3895.00` | 1,140,000,000.00 USD | 76,850.00 USD | 0.00 USD | `+66.38%` | `19.73` |
| `Live` | `Short` | `3905.00` | 1,140,000,000.00 USD | 812,040.00 USD | 0.00 USD | `+66.81%` | `207.95` |
| `Live` | `Short` | `3915.00` | 1,140,000,000.00 USD | 2,360,000.00 USD | 0.00 USD | `+67.24%` | `601.88` |
| `Live` | `Short` | `3925.00` | 1,140,000,000.00 USD | 413,140.00 USD | 0.00 USD | `+67.66%` | `105.26` |
| `Live` | `Short` | `3935.00` | 1,150,000,000.00 USD | 5,010,000.00 USD | 0.00 USD | `+68.09%` | `1,274.19` |
| `Live` | `Short` | `3945.00` | 1,150,000,000.00 USD | 49,500.00 USD | 0.00 USD | `+68.52%` | `12.55` |
| `Live` | `Short` | `3955.00` | 1,150,000,000.00 USD | 213,550.00 USD | 0.00 USD | `+68.94%` | `53.99` |
| `Live` | `Short` | `3965.00` | 1,240,000,000.00 USD | 90,380,000.00 USD | 0.00 USD | `+69.37%` | `22,793.28` |
| `Live` | `Short` | `3975.00` | 1,240,000,000.00 USD | 158,970.00 USD | 0.00 USD | `+69.80%` | `39.99` |
| `Live` | `Short` | `3985.00` | 1,270,000,000.00 USD | 30,500,000.00 USD | 0.00 USD | `+70.23%` | `7,652.71` |
| `Live` | `Short` | `3995.00` | 1,270,000,000.00 USD | 103,380.00 USD | 0.00 USD | `+70.65%` | `25.88` |
| `Live` | `Short` | `4005.00` | 1,270,000,000.00 USD | 110,190.00 USD | 0.00 USD | `+71.08%` | `27.51` |
| `Live` | `Short` | `4015.00` | 1,270,000,000.00 USD | 210,020.00 USD | 0.00 USD | `+71.51%` | `52.31` |
| `Live` | `Short` | `4025.00` | 1,340,000,000.00 USD | 68,130,000.00 USD | 0.00 USD | `+71.94%` | `16,927.06` |
| `Live` | `Short` | `4035.00` | 1,340,000,000.00 USD | 97,400.00 USD | 0.00 USD | `+72.36%` | `24.14` |
| `Live` | `Short` | `4045.00` | 1,340,000,000.00 USD | 1,990,000.00 USD | 0.00 USD | `+72.79%` | `492.23` |
| `Live` | `Short` | `4055.00` | 1,340,000,000.00 USD | 1,250,000.00 USD | 0.00 USD | `+73.22%` | `308.30` |
| `Live` | `Short` | `4065.00` | 1,340,000,000.00 USD | 2,460,000.00 USD | 0.00 USD | `+73.64%` | `605.36` |
| `Live` | `Short` | `4075.00` | 1,340,000,000.00 USD | 2,820,000.00 USD | 0.00 USD | `+74.07%` | `691.30` |
| `Live` | `Short` | `4085.00` | 1,350,000,000.00 USD | 21,510.00 USD | 0.00 USD | `+74.50%` | `5.27` |
| `Live` | `Short` | `4095.00` | 1,350,000,000.00 USD | 850,980.00 USD | 0.00 USD | `+74.93%` | `207.81` |
| `Live` | `Short` | `4105.00` | 1,350,000,000.00 USD | 97,360.00 USD | 0.00 USD | `+75.35%` | `23.72` |
| `Live` | `Short` | `4115.00` | 1,350,000,000.00 USD | 913.53 USD | 0.00 USD | `+75.78%` | `0.22` |
| `Live` | `Short` | `4125.00` | 1,350,000,000.00 USD | 827,880.00 USD | 0.00 USD | `+76.21%` | `200.70` |
| `Live` | `Short` | `4135.00` | 1,350,000,000.00 USD | 70,460.00 USD | 0.00 USD | `+76.63%` | `17.04` |
| `Live` | `Short` | `4145.00` | 1,350,000,000.00 USD | 4,480.00 USD | 0.00 USD | `+77.06%` | `1.08` |
| `Live` | `Short` | `4155.00` | 1,350,000,000.00 USD | 691,950.00 USD | 0.00 USD | `+77.49%` | `166.53` |
| `Live` | `Short` | `4165.00` | 1,350,000,000.00 USD | 243,490.00 USD | 0.00 USD | `+77.92%` | `58.46` |
| `Live` | `Short` | `4175.00` | 1,350,000,000.00 USD | 1,040.00 USD | 0.00 USD | `+78.34%` | `0.25` |
| `Live` | `Short` | `4185.00` | 1,350,000,000.00 USD | 47,650.00 USD | 0.00 USD | `+78.77%` | `11.39` |
| `Live` | `Short` | `4195.00` | 1,370,000,000.00 USD | 22,570,000.00 USD | 0.00 USD | `+79.20%` | `5,379.56` |
| `Live` | `Short` | `4205.00` | 1,370,000,000.00 USD | 50,590.00 USD | 0.00 USD | `+79.62%` | `12.03` |
| `Live` | `Short` | `4215.00` | 1,370,000,000.00 USD | 40,700.00 USD | 0.00 USD | `+80.05%` | `9.66` |
| `Live` | `Short` | `4225.00` | 1,370,000,000.00 USD | 1,610.00 USD | 0.00 USD | `+80.48%` | `0.38` |
| `Live` | `Short` | `4235.00` | 1,370,000,000.00 USD | 1,650.00 USD | 0.00 USD | `+80.91%` | `0.39` |
| `Live` | `Short` | `4245.00` | 1,370,000,000.00 USD | 89,170.00 USD | 0.00 USD | `+81.33%` | `21.01` |
| `Live` | `Short` | `4255.00` | 1,370,000,000.00 USD | 109,220.00 USD | 0.00 USD | `+81.76%` | `25.67` |
| `Live` | `Short` | `4265.00` | 1,370,000,000.00 USD | 86,860.00 USD | 0.00 USD | `+82.19%` | `20.36` |
| `Live` | `Short` | `4275.00` | 1,370,000,000.00 USD | 2,090,000.00 USD | 0.00 USD | `+82.61%` | `489.83` |
| `Live` | `Short` | `4285.00` | 1,370,000,000.00 USD | 236,310.00 USD | 0.00 USD | `+83.04%` | `55.15` |
| `Live` | `Short` | `4305.00` | 1,390,000,000.00 USD | 17,890,000.00 USD | 0.00 USD | `+83.90%` | `4,156.68` |
| `Live` | `Short` | `4315.00` | 1,390,000,000.00 USD | 278,830.00 USD | 0.00 USD | `+84.32%` | `64.62` |
| `Live` | `Short` | `4325.00` | 1,390,000,000.00 USD | 1,030.00 USD | 0.00 USD | `+84.75%` | `0.24` |
| `Live` | `Short` | `4335.00` | 1,390,000,000.00 USD | 19,070.00 USD | 0.00 USD | `+85.18%` | `4.40` |
| `Live` | `Short` | `4345.00` | 1,390,000,000.00 USD | 16,920.00 USD | 0.00 USD | `+85.60%` | `3.89` |
| `Live` | `Short` | `4355.00` | 1,390,000,000.00 USD | 63,350.00 USD | 0.00 USD | `+86.03%` | `14.55` |
| `Live` | `Short` | `4365.00` | 1,680,000,000.00 USD | 285,190,000.00 USD | 0.00 USD | `+86.46%` | `65,334.91` |
| `Live` | `Short` | `4375.00` | 1,680,000,000.00 USD | 1,440,000.00 USD | 0.00 USD | `+86.89%` | `330.27` |
| `Live` | `Short` | `4385.00` | 1,680,000,000.00 USD | 61,640.00 USD | 0.00 USD | `+87.31%` | `14.06` |
| `Live` | `Short` | `4395.00` | 1,680,000,000.00 USD | 1,920,000.00 USD | 0.00 USD | `+87.74%` | `436.59` |
| `Live` | `Short` | `4405.00` | 1,680,000,000.00 USD | 23,280.00 USD | 0.00 USD | `+88.17%` | `5.28` |
| `Live` | `Short` | `4415.00` | 1,680,000,000.00 USD | 693,140.00 USD | 0.00 USD | `+88.59%` | `157.00` |
| `Live` | `Short` | `4425.00` | 1,680,000,000.00 USD | 584.54 USD | 0.00 USD | `+89.02%` | `0.13` |
| `Live` | `Short` | `4435.00` | 1,680,000,000.00 USD | 3,280,000.00 USD | 0.00 USD | `+89.45%` | `739.23` |
| `Live` | `Short` | `4445.00` | 1,680,000,000.00 USD | 675,540.00 USD | 0.00 USD | `+89.88%` | `151.98` |
| `Live` | `Short` | `4455.00` | 1,680,000,000.00 USD | 13,720.00 USD | 0.00 USD | `+90.30%` | `3.08` |
| `Live` | `Short` | `4465.00` | 1,680,000,000.00 USD | 89,320.00 USD | 0.00 USD | `+90.73%` | `20.00` |
| `Live` | `Short` | `4475.00` | 1,680,000,000.00 USD | 33,360.00 USD | 0.00 USD | `+91.16%` | `7.45` |
| `Live` | `Short` | `4485.00` | 1,680,000,000.00 USD | 25,450.00 USD | 0.00 USD | `+91.58%` | `5.67` |
| `Live` | `Short` | `4495.00` | 1,680,000,000.00 USD | 12,800.00 USD | 0.00 USD | `+92.01%` | `2.85` |
| `Live` | `Short` | `4505.00` | 1,680,000,000.00 USD | 1,540.00 USD | 0.00 USD | `+92.44%` | `0.34` |
| `Live` | `Short` | `4515.00` | 1,690,000,000.00 USD | 1,610,000.00 USD | 0.00 USD | `+92.87%` | `356.45` |
| `Live` | `Short` | `4525.00` | 1,690,000,000.00 USD | 1,400.00 USD | 0.00 USD | `+93.29%` | `0.31` |
| `Live` | `Short` | `4535.00` | 1,690,000,000.00 USD | 1,150,000.00 USD | 0.00 USD | `+93.72%` | `252.94` |
| `Live` | `Short` | `4545.00` | 1,690,000,000.00 USD | 99,530.00 USD | 0.00 USD | `+94.15%` | `21.90` |
| `Live` | `Short` | `4555.00` | 1,690,000,000.00 USD | 222,250.00 USD | 0.00 USD | `+94.57%` | `48.79` |
| `Live` | `Short` | `4565.00` | 1,690,000,000.00 USD | 175,020.00 USD | 0.00 USD | `+95.00%` | `38.34` |
| `Live` | `Short` | `4575.00` | 1,690,000,000.00 USD | 195,540.00 USD | 0.00 USD | `+95.43%` | `42.74` |
| `Live` | `Short` | `4585.00` | 1,690,000,000.00 USD | 951,120.00 USD | 0.00 USD | `+95.86%` | `207.44` |
| `Live` | `Short` | `4595.00` | 1,690,000,000.00 USD | 184,920.00 USD | 0.00 USD | `+96.28%` | `40.24` |
| `Live` | `Short` | `4605.00` | 1,690,000,000.00 USD | 107,870.00 USD | 0.00 USD | `+96.71%` | `23.42` |
| `Live` | `Short` | `4615.00` | 1,690,000,000.00 USD | 53,500.00 USD | 0.00 USD | `+97.14%` | `11.59` |
| `Live` | `Short` | `4625.00` | 1,690,000,000.00 USD | 486,100.00 USD | 0.00 USD | `+97.57%` | `105.10` |
| `Live` | `Short` | `4635.00` | 1,690,000,000.00 USD | 24,980.00 USD | 0.00 USD | `+97.99%` | `5.39` |
| `Live` | `Short` | `4645.00` | 1,690,000,000.00 USD | 112,490.00 USD | 0.00 USD | `+98.42%` | `24.22` |
| `Live` | `Short` | `4655.00` | 1,690,000,000.00 USD | 424,480.00 USD | 0.00 USD | `+98.85%` | `91.19` |
| `Live` | `Short` | `4665.00` | 1,690,000,000.00 USD | 49,460.00 USD | 0.00 USD | `+99.27%` | `10.60` |
| `Live` | `Short` | `4675.00` | 1,690,000,000.00 USD | 1,880.00 USD | 0.00 USD | `+99.70%` | `0.40` |
| `Live` | `Short` | `4685.00` | 1,690,000,000.00 USD | 4,370.00 USD | 0.00 USD | `+100.13%` | `0.93` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `505.00` | 1,500,000,000.00 USD | 0.00 USD | 16,940.00 USD | `-78.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.00` | 1,500,000,000.00 USD | 0.00 USD | 563.16 USD | `-76.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.00` | 1,500,000,000.00 USD | 0.00 USD | 383.31 USD | `-69.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `755.00` | 1,500,000,000.00 USD | 0.00 USD | 177.27 USD | `-67.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `795.00` | 1,500,000,000.00 USD | 0.00 USD | 104.22 USD | `-66.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `805.00` | 1,500,000,000.00 USD | 0.00 USD | 2,090.00 USD | `-65.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `835.00` | 1,500,000,000.00 USD | 0.00 USD | 1,670.00 USD | `-64.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `865.00` | 1,500,000,000.00 USD | 0.00 USD | 139,280.00 USD | `-63.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `885.00` | 1,500,000,000.00 USD | 0.00 USD | 3,130.00 USD | `-62.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `905.00` | 1,500,000,000.00 USD | 0.00 USD | 2,780.00 USD | `-61.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `985.00` | 1,500,000,000.00 USD | 0.00 USD | 516.34 USD | `-57.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `995.00` | 1,500,000,000.00 USD | 0.00 USD | 100.50 USD | `-57.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1005.00` | 1,500,000,000.00 USD | 0.00 USD | 222,040.00 USD | `-57.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1025.00` | 1,500,000,000.00 USD | 0.00 USD | 112.03 USD | `-56.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1065.00` | 1,500,000,000.00 USD | 0.00 USD | 1,060.00 USD | `-54.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1075.00` | 1,500,000,000.00 USD | 0.00 USD | 995.34 USD | `-54.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1105.00` | 1,500,000,000.00 USD | 0.00 USD | 1,610.00 USD | `-52.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1115.00` | 1,500,000,000.00 USD | 0.00 USD | 11,050.00 USD | `-52.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1125.00` | 1,500,000,000.00 USD | 0.00 USD | 1,320.00 USD | `-51.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1155.00` | 1,500,000,000.00 USD | 0.00 USD | 1,000.00 USD | `-50.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1175.00` | 1,500,000,000.00 USD | 0.00 USD | 203.98 USD | `-49.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1185.00` | 1,500,000,000.00 USD | 0.00 USD | 228.47 USD | `-49.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1205.00` | 1,500,000,000.00 USD | 0.00 USD | 27,760.00 USD | `-48.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1225.00` | 1,500,000,000.00 USD | 0.00 USD | 995.93 USD | `-47.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1245.00` | 1,500,000,000.00 USD | 0.00 USD | 951.93 USD | `-46.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1255.00` | 1,500,000,000.00 USD | 0.00 USD | 6,810.00 USD | `-46.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1285.00` | 1,500,000,000.00 USD | 0.00 USD | 9,050.00 USD | `-45.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1295.00` | 1,500,000,000.00 USD | 0.00 USD | 7,030.00 USD | `-44.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1305.00` | 1,500,000,000.00 USD | 0.00 USD | 23,030.00 USD | `-44.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1315.00` | 1,500,000,000.00 USD | 0.00 USD | 1,440.00 USD | `-43.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1345.00` | 1,500,000,000.00 USD | 0.00 USD | 141,950.00 USD | `-42.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1355.00` | 1,500,000,000.00 USD | 0.00 USD | 128.86 USD | `-42.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1375.00` | 1,500,000,000.00 USD | 0.00 USD | 4,160.00 USD | `-41.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1395.00` | 1,500,000,000.00 USD | 0.00 USD | 535,600.00 USD | `-40.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1405.00` | 1,500,000,000.00 USD | 0.00 USD | 20,270.00 USD | `-39.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1425.00` | 1,500,000,000.00 USD | 0.00 USD | 6,450.00 USD | `-39.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1435.00` | 1,500,000,000.00 USD | 0.00 USD | 852.10 USD | `-38.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1445.00` | 1,500,000,000.00 USD | 0.00 USD | 1,490.00 USD | `-38.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1455.00` | 1,500,000,000.00 USD | 0.00 USD | 5,680.00 USD | `-37.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1465.00` | 1,500,000,000.00 USD | 0.00 USD | 19,350.00 USD | `-37.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1475.00` | 1,500,000,000.00 USD | 0.00 USD | 2,600.00 USD | `-36.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1485.00` | 1,500,000,000.00 USD | 0.00 USD | 18,710.00 USD | `-36.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1495.00` | 1,500,000,000.00 USD | 0.00 USD | 11,460.00 USD | `-36.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1505.00` | 1,500,000,000.00 USD | 0.00 USD | 78,910.00 USD | `-35.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1515.00` | 1,500,000,000.00 USD | 0.00 USD | 11,140.00 USD | `-35.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1525.00` | 1,500,000,000.00 USD | 0.00 USD | 32,310.00 USD | `-34.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1535.00` | 1,500,000,000.00 USD | 0.00 USD | 983.78 USD | `-34.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1545.00` | 1,500,000,000.00 USD | 0.00 USD | 17,470.00 USD | `-34.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1555.00` | 1,500,000,000.00 USD | 0.00 USD | 4,210.00 USD | `-33.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1565.00` | 1,500,000,000.00 USD | 0.00 USD | 6,260.00 USD | `-33.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1575.00` | 1,500,000,000.00 USD | 0.00 USD | 190,890.00 USD | `-32.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1585.00` | 1,500,000,000.00 USD | 0.00 USD | 3,390.00 USD | `-32.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1595.00` | 1,500,000,000.00 USD | 0.00 USD | 4,040.00 USD | `-31.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1605.00` | 1,500,000,000.00 USD | 0.00 USD | 435,900.00 USD | `-31.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1615.00` | 1,500,000,000.00 USD | 0.00 USD | 25,840.00 USD | `-31.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1625.00` | 1,500,000,000.00 USD | 0.00 USD | 13,590.00 USD | `-30.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1635.00` | 1,500,000,000.00 USD | 0.00 USD | 5,510.00 USD | `-30.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1645.00` | 1,500,000,000.00 USD | 0.00 USD | 328,140.00 USD | `-29.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1655.00` | 1,500,000,000.00 USD | 0.00 USD | 22,220.00 USD | `-29.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1665.00` | 1,500,000,000.00 USD | 0.00 USD | 3,110.00 USD | `-28.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1675.00` | 1,500,000,000.00 USD | 0.00 USD | 3,440.00 USD | `-28.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1685.00` | 1,500,000,000.00 USD | 0.00 USD | 58,890.00 USD | `-28.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1695.00` | 1,500,000,000.00 USD | 0.00 USD | 6,800.00 USD | `-27.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1705.00` | 1,500,000,000.00 USD | 0.00 USD | 81,190.00 USD | `-27.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1715.00` | 1,500,000,000.00 USD | 0.00 USD | 28,180.00 USD | `-26.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1725.00` | 1,500,000,000.00 USD | 0.00 USD | 47,500.00 USD | `-26.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1735.00` | 1,500,000,000.00 USD | 0.00 USD | 28,150.00 USD | `-25.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1745.00` | 1,500,000,000.00 USD | 0.00 USD | 3,180.00 USD | `-25.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1755.00` | 1,500,000,000.00 USD | 0.00 USD | 498,120.00 USD | `-25.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1765.00` | 1,500,000,000.00 USD | 0.00 USD | 75,630.00 USD | `-24.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1775.00` | 1,500,000,000.00 USD | 0.00 USD | 3,090.00 USD | `-24.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1785.00` | 1,500,000,000.00 USD | 0.00 USD | 4,930.00 USD | `-23.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1795.00` | 1,500,000,000.00 USD | 0.00 USD | 184,330.00 USD | `-23.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1805.00` | 1,500,000,000.00 USD | 0.00 USD | 238,740.00 USD | `-22.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1815.00` | 1,500,000,000.00 USD | 0.00 USD | 114,830.00 USD | `-22.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1825.00` | 1,500,000,000.00 USD | 0.00 USD | 26,790.00 USD | `-22.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1835.00` | 1,500,000,000.00 USD | 0.00 USD | 2,500.00 USD | `-21.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1845.00` | 1,500,000,000.00 USD | 0.00 USD | 9,040.00 USD | `-21.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1855.00` | 1,500,000,000.00 USD | 0.00 USD | 467,010.00 USD | `-20.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1865.00` | 1,500,000,000.00 USD | 0.00 USD | 32,910.00 USD | `-20.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1875.00` | 1,500,000,000.00 USD | 0.00 USD | 18,210,000.00 USD | `-19.91%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1885.00` | 1,480,000,000.00 USD | 0.00 USD | 2,390.00 USD | `-19.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1895.00` | 1,480,000,000.00 USD | 0.00 USD | 61,700.00 USD | `-19.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1905.00` | 1,480,000,000.00 USD | 0.00 USD | 162,190.00 USD | `-18.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1915.00` | 1,480,000,000.00 USD | 0.00 USD | 8,110,000.00 USD | `-18.20%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1925.00` | 1,470,000,000.00 USD | 0.00 USD | 16,410,000.00 USD | `-17.77%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1935.00` | 1,460,000,000.00 USD | 0.00 USD | 79,950.00 USD | `-17.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1945.00` | 1,460,000,000.00 USD | 0.00 USD | 44,850.00 USD | `-16.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1955.00` | 1,460,000,000.00 USD | 0.00 USD | 52,220.00 USD | `-16.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1965.00` | 1,460,000,000.00 USD | 0.00 USD | 510.51 USD | `-16.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1975.00` | 1,460,000,000.00 USD | 0.00 USD | 59,770.00 USD | `-15.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1985.00` | 1,460,000,000.00 USD | 0.00 USD | 95,270.00 USD | `-15.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1995.00` | 1,460,000,000.00 USD | 0.00 USD | 164,110.00 USD | `-14.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2005.00` | 1,460,000,000.00 USD | 0.00 USD | 1,320,000.00 USD | `-14.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2015.00` | 1,450,000,000.00 USD | 0.00 USD | 69,640.00 USD | `-13.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2025.00` | 1,450,000,000.00 USD | 0.00 USD | 5,040.00 USD | `-13.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2035.00` | 1,450,000,000.00 USD | 0.00 USD | 103,890.00 USD | `-13.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2045.00` | 1,450,000,000.00 USD | 0.00 USD | 15,220.00 USD | `-12.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2055.00` | 1,450,000,000.00 USD | 0.00 USD | 140,840.00 USD | `-12.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2065.00` | 1,450,000,000.00 USD | 0.00 USD | 47,480.00 USD | `-11.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2075.00` | 1,450,000,000.00 USD | 0.00 USD | 76,450.00 USD | `-11.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2085.00` | 1,450,000,000.00 USD | 0.00 USD | 52,030.00 USD | `-10.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2095.00` | 1,450,000,000.00 USD | 0.00 USD | 29,710.00 USD | `-10.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2105.00` | 1,450,000,000.00 USD | 0.00 USD | 330,470.00 USD | `-10.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2115.00` | 1,450,000,000.00 USD | 0.00 USD | 119,630.00 USD | `-9.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2125.00` | 1,450,000,000.00 USD | 0.00 USD | 81,460.00 USD | `-9.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2135.00` | 1,450,000,000.00 USD | 0.00 USD | 19,470.00 USD | `-8.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2145.00` | 1,450,000,000.00 USD | 0.00 USD | 217,830.00 USD | `-8.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2155.00` | 1,450,000,000.00 USD | 0.00 USD | 104,580.00 USD | `-7.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2165.00` | 1,450,000,000.00 USD | 0.00 USD | 871,350.00 USD | `-7.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2175.00` | 1,450,000,000.00 USD | 0.00 USD | 1,360,000.00 USD | `-7.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2185.00` | 1,450,000,000.00 USD | 0.00 USD | 92,000.00 USD | `-6.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2195.00` | 1,450,000,000.00 USD | 0.00 USD | 438,560.00 USD | `-6.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2205.00` | 1,450,000,000.00 USD | 0.00 USD | 2,140,000.00 USD | `-5.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2215.00` | 1,450,000,000.00 USD | 0.00 USD | 1,020,000.00 USD | `-5.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2225.00` | 1,450,000,000.00 USD | 0.00 USD | 992,450.00 USD | `-4.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2235.00` | 1,450,000,000.00 USD | 0.00 USD | 125,690.00 USD | `-4.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2245.00` | 1,450,000,000.00 USD | 0.00 USD | 1,590,000.00 USD | `-4.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2255.00` | 1,440,000,000.00 USD | 0.00 USD | 23,250,000.00 USD | `-3.67%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2265.00` | 1,420,000,000.00 USD | 0.00 USD | 653,600.00 USD | `-3.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2275.00` | 1,420,000,000.00 USD | 0.00 USD | 4,680,000.00 USD | `-2.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2285.00` | 1,420,000,000.00 USD | 0.00 USD | 4,200,000.00 USD | `-2.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2295.00` | 1,410,000,000.00 USD | 0.00 USD | 10,550,000.00 USD | `-1.96%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2305.00` | 1,400,000,000.00 USD | 0.00 USD | 1,390,000,000.00 USD | `-1.54%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2315.00` | 14,970,000.00 USD | 0.00 USD | 11,460,000.00 USD | `-1.11%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2325.00` | 3,510,000.00 USD | 0.00 USD | 1,610,000.00 USD | `-0.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2335.00` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | `-0.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2345.00` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+0.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2355.00` | 2,030,000.00 USD | 1,020,000.00 USD | 0.00 USD | `+0.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2365.00` | 2,130,000.00 USD | 102,380.00 USD | 0.00 USD | `+1.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2375.00` | 3,200,000.00 USD | 1,070,000.00 USD | 0.00 USD | `+1.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2385.00` | 5,210,000.00 USD | 2,000,000.00 USD | 0.00 USD | `+1.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2395.00` | 16,080,000.00 USD | 10,880,000.00 USD | 0.00 USD | `+2.31%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2405.00` | 18,410,000.00 USD | 2,320,000.00 USD | 0.00 USD | `+2.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2415.00` | 19,570,000.00 USD | 1,160,000.00 USD | 0.00 USD | `+3.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2425.00` | 23,070,000.00 USD | 3,510,000.00 USD | 0.00 USD | `+3.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2435.00` | 23,560,000.00 USD | 482,650.00 USD | 0.00 USD | `+4.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2445.00` | 34,070,000.00 USD | 10,520,000.00 USD | 0.00 USD | `+4.44%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2455.00` | 34,310,000.00 USD | 233,060.00 USD | 0.00 USD | `+4.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2465.00` | 36,480,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+5.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2475.00` | 36,810,000.00 USD | 327,070.00 USD | 0.00 USD | `+5.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2485.00` | 38,960,000.00 USD | 2,150,000.00 USD | 0.00 USD | `+6.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2495.00` | 39,450,000.00 USD | 486,690.00 USD | 0.00 USD | `+6.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2505.00` | 44,750,000.00 USD | 5,300,000.00 USD | 0.00 USD | `+7.01%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2515.00` | 52,530,000.00 USD | 7,780,000.00 USD | 0.00 USD | `+7.43%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2525.00` | 55,730,000.00 USD | 3,200,000.00 USD | 0.00 USD | `+7.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2535.00` | 55,800,000.00 USD | 72,580.00 USD | 0.00 USD | `+8.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2545.00` | 57,970,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+8.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2555.00` | 58,310,000.00 USD | 332,460.00 USD | 0.00 USD | `+9.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2565.00` | 60,640,000.00 USD | 2,330,000.00 USD | 0.00 USD | `+9.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2575.00` | 60,800,000.00 USD | 154,870.00 USD | 0.00 USD | `+10.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2585.00` | 63,250,000.00 USD | 2,450,000.00 USD | 0.00 USD | `+10.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2595.00` | 63,260,000.00 USD | 14,590.00 USD | 0.00 USD | `+10.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2605.00` | 66,370,000.00 USD | 3,100,000.00 USD | 0.00 USD | `+11.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2615.00` | 66,580,000.00 USD | 218,380.00 USD | 0.00 USD | `+11.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2625.00` | 68,770,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+12.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2635.00` | 69,080,000.00 USD | 303,700.00 USD | 0.00 USD | `+12.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2645.00` | 71,250,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+12.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2655.00` | 71,530,000.00 USD | 285,850.00 USD | 0.00 USD | `+13.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2665.00` | 73,690,000.00 USD | 2,160,000.00 USD | 0.00 USD | `+13.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2675.00` | 74,080,000.00 USD | 393,350.00 USD | 0.00 USD | `+14.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2685.00` | 76,270,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+14.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2695.00` | 76,440,000.00 USD | 175,980.00 USD | 0.00 USD | `+15.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2705.00` | 81,070,000.00 USD | 4,630,000.00 USD | 0.00 USD | `+15.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2715.00` | 81,150,000.00 USD | 76,900.00 USD | 0.00 USD | `+15.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2725.00` | 83,620,000.00 USD | 2,470,000.00 USD | 0.00 USD | `+16.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2735.00` | 83,670,000.00 USD | 55,720.00 USD | 0.00 USD | `+16.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2745.00` | 85,980,000.00 USD | 2,300,000.00 USD | 0.00 USD | `+17.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2755.00` | 87,490,000.00 USD | 1,510,000.00 USD | 0.00 USD | `+17.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2765.00` | 89,870,000.00 USD | 2,380,000.00 USD | 0.00 USD | `+18.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2775.00` | 90,490,000.00 USD | 620,300.00 USD | 0.00 USD | `+18.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2785.00` | 92,790,000.00 USD | 2,300,000.00 USD | 0.00 USD | `+18.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2795.00` | 92,830,000.00 USD | 36,990.00 USD | 0.00 USD | `+19.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2805.00` | 95,970,000.00 USD | 3,140,000.00 USD | 0.00 USD | `+19.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2815.00` | 96,020,000.00 USD | 53,260.00 USD | 0.00 USD | `+20.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2825.00` | 96,090,000.00 USD | 62,020.00 USD | 0.00 USD | `+20.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2835.00` | 96,380,000.00 USD | 289,110.00 USD | 0.00 USD | `+21.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2845.00` | 97,390,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+21.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2855.00` | 98,670,000.00 USD | 1,280,000.00 USD | 0.00 USD | `+21.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2865.00` | 98,680,000.00 USD | 10,290.00 USD | 0.00 USD | `+22.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2875.00` | 98,680,000.00 USD | 3,630.00 USD | 0.00 USD | `+22.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2885.00` | 98,970,000.00 USD | 290,880.00 USD | 0.00 USD | `+23.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2895.00` | 99,000,000.00 USD | 23,020.00 USD | 0.00 USD | `+23.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2905.00` | 100,950,000.00 USD | 1,960,000.00 USD | 0.00 USD | `+24.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2915.00` | 100,960,000.00 USD | 10,340.00 USD | 0.00 USD | `+24.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2925.00` | 100,960,000.00 USD | 3,040.00 USD | 0.00 USD | `+24.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2935.00` | 101,020,000.00 USD | 54,540.00 USD | 0.00 USD | `+25.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2945.00` | 101,050,000.00 USD | 34,650.00 USD | 0.00 USD | `+25.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2955.00` | 101,130,000.00 USD | 74,770.00 USD | 0.00 USD | `+26.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2965.00` | 101,240,000.00 USD | 111,790.00 USD | 0.00 USD | `+26.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2975.00` | 101,390,000.00 USD | 148,070.00 USD | 0.00 USD | `+27.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2985.00` | 105,480,000.00 USD | 4,090,000.00 USD | 0.00 USD | `+27.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2995.00` | 107,400,000.00 USD | 1,920,000.00 USD | 0.00 USD | `+27.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3005.00` | 109,390,000.00 USD | 1,990,000.00 USD | 0.00 USD | `+28.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3015.00` | 109,390,000.00 USD | 6,950.00 USD | 0.00 USD | `+28.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3025.00` | 109,430,000.00 USD | 37,410.00 USD | 0.00 USD | `+29.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3035.00` | 109,500,000.00 USD | 70,360.00 USD | 0.00 USD | `+29.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3045.00` | 109,520,000.00 USD | 22,460.00 USD | 0.00 USD | `+30.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3055.00` | 110,310,000.00 USD | 786,100.00 USD | 0.00 USD | `+30.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3065.00` | 110,310,000.00 USD | 3,080.00 USD | 0.00 USD | `+30.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3075.00` | 110,360,000.00 USD | 50,370.00 USD | 0.00 USD | `+31.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3085.00` | 110,380,000.00 USD | 19,860.00 USD | 0.00 USD | `+31.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3095.00` | 110,420,000.00 USD | 34,020.00 USD | 0.00 USD | `+32.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3105.00` | 123,830,000.00 USD | 13,410,000.00 USD | 0.00 USD | `+32.64%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `3115.00` | 123,940,000.00 USD | 118,040.00 USD | 0.00 USD | `+33.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3125.00` | 124,300,000.00 USD | 352,160.00 USD | 0.00 USD | `+33.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3145.00` | 124,300,000.00 USD | 1,860.00 USD | 0.00 USD | `+34.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3155.00` | 124,370,000.00 USD | 68,940.00 USD | 0.00 USD | `+34.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3165.00` | 124,380,000.00 USD | 9,860.00 USD | 0.00 USD | `+35.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3175.00` | 124,390,000.00 USD | 16,410.00 USD | 0.00 USD | `+35.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3185.00` | 124,390,000.00 USD | 1,330.00 USD | 0.00 USD | `+36.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3195.00` | 124,420,000.00 USD | 29,580.00 USD | 0.00 USD | `+36.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3205.00` | 125,330,000.00 USD | 910,780.00 USD | 0.00 USD | `+36.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3215.00` | 125,340,000.00 USD | 1,290.00 USD | 0.00 USD | `+37.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3225.00` | 125,340,000.00 USD | 3,740.00 USD | 0.00 USD | `+37.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3235.00` | 125,370,000.00 USD | 31,330.00 USD | 0.00 USD | `+38.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3245.00` | 125,430,000.00 USD | 56,110.00 USD | 0.00 USD | `+38.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3255.00` | 125,630,000.00 USD | 204,030.00 USD | 0.00 USD | `+39.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3265.00` | 125,650,000.00 USD | 15,710.00 USD | 0.00 USD | `+39.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3275.00` | 125,650,000.00 USD | 1,630.00 USD | 0.00 USD | `+39.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3285.00` | 125,790,000.00 USD | 142,210.00 USD | 0.00 USD | `+40.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3295.00` | 125,810,000.00 USD | 16,780.00 USD | 0.00 USD | `+40.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3305.00` | 127,080,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+41.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3315.00` | 127,460,000.00 USD | 385,510.00 USD | 0.00 USD | `+41.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3325.00` | 127,480,000.00 USD | 18,270.00 USD | 0.00 USD | `+42.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3335.00` | 127,500,000.00 USD | 14,190.00 USD | 0.00 USD | `+42.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3345.00` | 127,500,000.00 USD | 617.15 USD | 0.00 USD | `+42.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3355.00` | 127,500,000.00 USD | 334.49 USD | 0.00 USD | `+43.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3365.00` | 127,500,000.00 USD | 597.29 USD | 0.00 USD | `+43.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3375.00` | 127,520,000.00 USD | 23,460.00 USD | 0.00 USD | `+44.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3385.00` | 127,580,000.00 USD | 58,010.00 USD | 0.00 USD | `+44.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3395.00` | 127,930,000.00 USD | 355,050.00 USD | 0.00 USD | `+45.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3405.00` | 129,530,000.00 USD | 1,600,000.00 USD | 0.00 USD | `+45.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3415.00` | 129,540,000.00 USD | 3,510.00 USD | 0.00 USD | `+45.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3425.00` | 129,550,000.00 USD | 16,310.00 USD | 0.00 USD | `+46.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3445.00` | 129,570,000.00 USD | 15,030.00 USD | 0.00 USD | `+47.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3455.00` | 129,590,000.00 USD | 18,600.00 USD | 0.00 USD | `+47.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3465.00` | 129,900,000.00 USD | 311,800.00 USD | 0.00 USD | `+48.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3475.00` | 129,900,000.00 USD | 2,980.00 USD | 0.00 USD | `+48.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3485.00` | 129,950,000.00 USD | 43,610.00 USD | 0.00 USD | `+48.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3495.00` | 129,950,000.00 USD | 158.32 USD | 0.00 USD | `+49.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3505.00` | 130,500,000.00 USD | 550,300.00 USD | 0.00 USD | `+49.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3515.00` | 130,540,000.00 USD | 43,200.00 USD | 0.00 USD | `+50.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3525.00` | 130,540,000.00 USD | 3,690.00 USD | 0.00 USD | `+50.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3535.00` | 130,550,000.00 USD | 9,810.00 USD | 0.00 USD | `+51.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3545.00` | 130,550,000.00 USD | 179.38 USD | 0.00 USD | `+51.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3555.00` | 130,640,000.00 USD | 90,810.00 USD | 0.00 USD | `+51.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3565.00` | 130,650,000.00 USD | 2,300.00 USD | 0.00 USD | `+52.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3585.00` | 130,650,000.00 USD | 354.92 USD | 0.00 USD | `+53.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3595.00` | 130,660,000.00 USD | 13,160.00 USD | 0.00 USD | `+53.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3605.00` | 130,770,000.00 USD | 105,860.00 USD | 0.00 USD | `+53.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3625.00` | 130,780,000.00 USD | 10,210.00 USD | 0.00 USD | `+54.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3635.00` | 130,780,000.00 USD | 7,790.00 USD | 0.00 USD | `+55.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3645.00` | 130,790,000.00 USD | 3,860.00 USD | 0.00 USD | `+55.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3655.00` | 130,800,000.00 USD | 7,740.00 USD | 0.00 USD | `+56.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3665.00` | 130,800,000.00 USD | 8,130.00 USD | 0.00 USD | `+56.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3675.00` | 130,860,000.00 USD | 55,120.00 USD | 0.00 USD | `+56.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3685.00` | 130,860,000.00 USD | 3,550.00 USD | 0.00 USD | `+57.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3705.00` | 130,860,000.00 USD | 819.92 USD | 0.00 USD | `+58.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3715.00` | 130,860,000.00 USD | 323.58 USD | 0.00 USD | `+58.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3725.00` | 130,870,000.00 USD | 1,400.00 USD | 0.00 USD | `+59.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3735.00` | 130,870,000.00 USD | 6,490.00 USD | 0.00 USD | `+59.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3755.00` | 130,870,000.00 USD | 751.00 USD | 0.00 USD | `+60.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3785.00` | 130,870,000.00 USD | 286.90 USD | 0.00 USD | `+61.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3795.00` | 130,870,000.00 USD | 1,560.00 USD | 0.00 USD | `+62.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3805.00` | 131,610,000.00 USD | 734,090.00 USD | 0.00 USD | `+62.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3815.00` | 131,630,000.00 USD | 20,930.00 USD | 0.00 USD | `+62.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3825.00` | 131,640,000.00 USD | 8,380.00 USD | 0.00 USD | `+63.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3835.00` | 131,640,000.00 USD | 711.78 USD | 0.00 USD | `+63.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3845.00` | 131,640,000.00 USD | 932.03 USD | 0.00 USD | `+64.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3855.00` | 131,840,000.00 USD | 203,880.00 USD | 0.00 USD | `+64.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3875.00` | 131,880,000.00 USD | 41,200.00 USD | 0.00 USD | `+65.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3885.00` | 131,910,000.00 USD | 21,210.00 USD | 0.00 USD | `+65.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3905.00` | 132,090,000.00 USD | 180,010.00 USD | 0.00 USD | `+66.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3915.00` | 132,730,000.00 USD | 646,840.00 USD | 0.00 USD | `+67.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3925.00` | 132,740,000.00 USD | 3,260.00 USD | 0.00 USD | `+67.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3935.00` | 132,780,000.00 USD | 42,570.00 USD | 0.00 USD | `+68.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3945.00` | 132,800,000.00 USD | 19,730.00 USD | 0.00 USD | `+68.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3955.00` | 132,800,000.00 USD | 1,380.00 USD | 0.00 USD | `+68.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3965.00` | 132,800,000.00 USD | 323.54 USD | 0.00 USD | `+69.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3975.00` | 132,810,000.00 USD | 6,960.00 USD | 0.00 USD | `+69.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3985.00` | 132,820,000.00 USD | 14,610.00 USD | 0.00 USD | `+70.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3995.00` | 132,830,000.00 USD | 4,280.00 USD | 0.00 USD | `+70.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4005.00` | 135,500,000.00 USD | 2,680,000.00 USD | 0.00 USD | `+71.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4035.00` | 135,500,000.00 USD | 898.59 USD | 0.00 USD | `+72.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4055.00` | 135,510,000.00 USD | 811.00 USD | 0.00 USD | `+73.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4075.00` | 135,510,000.00 USD | 4,310.00 USD | 0.00 USD | `+74.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4085.00` | 135,510,000.00 USD | 2,800.00 USD | 0.00 USD | `+74.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4095.00` | 135,520,000.00 USD | 2,750.00 USD | 0.00 USD | `+74.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4105.00` | 135,560,000.00 USD | 43,660.00 USD | 0.00 USD | `+75.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4115.00` | 135,570,000.00 USD | 5,990.00 USD | 0.00 USD | `+75.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4125.00` | 135,570,000.00 USD | 372.90 USD | 0.00 USD | `+76.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4145.00` | 135,570,000.00 USD | 395.43 USD | 0.00 USD | `+77.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4175.00` | 135,570,000.00 USD | 2,890.00 USD | 0.00 USD | `+78.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4185.00` | 135,570,000.00 USD | 376.65 USD | 0.00 USD | `+78.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4205.00` | 135,600,000.00 USD | 28,760.00 USD | 0.00 USD | `+79.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4215.00` | 135,600,000.00 USD | 460.70 USD | 0.00 USD | `+80.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4225.00` | 135,600,000.00 USD | 1,270.00 USD | 0.00 USD | `+80.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4255.00` | 135,600,000.00 USD | 4,300.00 USD | 0.00 USD | `+81.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4265.00` | 135,610,000.00 USD | 4,010.00 USD | 0.00 USD | `+82.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4275.00` | 135,670,000.00 USD | 64,550.00 USD | 0.00 USD | `+82.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4285.00` | 135,670,000.00 USD | 1,610.00 USD | 0.00 USD | `+83.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4305.00` | 135,770,000.00 USD | 97,670.00 USD | 0.00 USD | `+83.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4315.00` | 135,770,000.00 USD | 1,070.00 USD | 0.00 USD | `+84.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4345.00` | 135,780,000.00 USD | 11,270.00 USD | 0.00 USD | `+85.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4355.00` | 135,790,000.00 USD | 3,250.00 USD | 0.00 USD | `+86.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4375.00` | 135,830,000.00 USD | 43,750.00 USD | 0.00 USD | `+86.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4385.00` | 135,900,000.00 USD | 64,570.00 USD | 0.00 USD | `+87.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4395.00` | 135,900,000.00 USD | 1,050.00 USD | 0.00 USD | `+87.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4405.00` | 137,120,000.00 USD | 1,230,000.00 USD | 0.00 USD | `+88.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4415.00` | 137,130,000.00 USD | 11,480.00 USD | 0.00 USD | `+88.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4425.00` | 137,140,000.00 USD | 2,510.00 USD | 0.00 USD | `+89.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4435.00` | 137,310,000.00 USD | 177,400.00 USD | 0.00 USD | `+89.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4455.00` | 137,320,000.00 USD | 641.97 USD | 0.00 USD | `+90.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4505.00` | 137,660,000.00 USD | 343,680.00 USD | 0.00 USD | `+92.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4515.00` | 137,660,000.00 USD | 2,280.00 USD | 0.00 USD | `+92.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4525.00` | 137,670,000.00 USD | 6,560.00 USD | 0.00 USD | `+93.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4545.00` | 137,870,000.00 USD | 197,950.00 USD | 0.00 USD | `+94.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4565.00` | 137,960,000.00 USD | 97,750.00 USD | 0.00 USD | `+95.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4585.00` | 137,960,000.00 USD | 1,420.00 USD | 0.00 USD | `+95.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4595.00` | 137,970,000.00 USD | 2,610.00 USD | 0.00 USD | `+96.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4605.00` | 138,030,000.00 USD | 64,120.00 USD | 0.00 USD | `+96.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4645.00` | 138,060,000.00 USD | 27,410.00 USD | 0.00 USD | `+98.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4655.00` | 138,230,000.00 USD | 174,790.00 USD | 0.00 USD | `+98.85%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `2074.60` | 2,640,000,000.00 USD | 0.00 USD | 2,640,000,000.00 USD | 3,960,000.00 USD | 3,150,000.00 USD | 2,680,000.00 USD |
| `7D` | `2077.40` | 2,630,000,000.00 USD | 0.00 USD | 2,630,000,000.00 USD | 4,430,000.00 USD | 3,940,000.00 USD | 1,980,000.00 USD |
| `7D` | `2080.20` | 2,620,000,000.00 USD | 0.00 USD | 2,620,000,000.00 USD | 3,480,000.00 USD | 2,740,000.00 USD | 2,540,000.00 USD |
| `7D` | `2083.00` | 2,610,000,000.00 USD | 0.00 USD | 2,610,000,000.00 USD | 2,340,000.00 USD | 1,900,000.00 USD | 1,890,000.00 USD |
| `7D` | `2085.80` | 2,600,000,000.00 USD | 0.00 USD | 2,600,000,000.00 USD | 4,270,000.00 USD | 2,570,000.00 USD | 3,130,000.00 USD |
| `7D` | `2088.60` | 2,590,000,000.00 USD | 0.00 USD | 2,590,000,000.00 USD | 1,920,000.00 USD | 1,480,000.00 USD | 1,470,000.00 USD |
| `7D` | `2091.40` | 2,590,000,000.00 USD | 0.00 USD | 2,590,000,000.00 USD | 4,210,000.00 USD | 549,010.00 USD | 6,400,000.00 USD |
| `7D` | `2094.20` | 2,580,000,000.00 USD | 0.00 USD | 2,580,000,000.00 USD | 5,310,000.00 USD | 1,660,000.00 USD | 2,340,000.00 USD |
| `1D` | `2096.00` | 1,120,000,000.00 USD | 0.00 USD | 1,120,000,000.00 USD | 2,150,000.00 USD | 1,620,000.00 USD | 1,660,000.00 USD |
| `7D` | `2097.00` | 2,570,000,000.00 USD | 0.00 USD | 2,570,000,000.00 USD | 1,830,000.00 USD | 3,320,000.00 USD | 1,290,000.00 USD |
| `1D` | `2098.70` | 1,110,000,000.00 USD | 0.00 USD | 1,110,000,000.00 USD | 513,340.00 USD | 682,000.00 USD | 248,570.00 USD |
| `7D` | `2099.80` | 2,560,000,000.00 USD | 0.00 USD | 2,560,000,000.00 USD | 1,880,000.00 USD | 1,920,000.00 USD | 3,300,000.00 USD |
| `1D` | `2101.40` | 1,110,000,000.00 USD | 0.00 USD | 1,110,000,000.00 USD | 46,810.00 USD | 31,040.00 USD | 144,080.00 USD |
| `7D` | `2102.60` | 2,550,000,000.00 USD | 0.00 USD | 2,550,000,000.00 USD | 125,250.00 USD | 341,900.00 USD | 1,190,000.00 USD |
| `1D` | `2104.10` | 1,110,000,000.00 USD | 0.00 USD | 1,110,000,000.00 USD | 907,940.00 USD | 570,780.00 USD | 12,700.00 USD |
| `7D` | `2105.40` | 2,550,000,000.00 USD | 0.00 USD | 2,550,000,000.00 USD | 2,050,000.00 USD | 986,590.00 USD | 1,790,000.00 USD |
| `1D` | `2106.80` | 1,110,000,000.00 USD | 0.00 USD | 1,110,000,000.00 USD | 358,850.00 USD | 17,140.00 USD | 265,430.00 USD |
| `7D` | `2108.20` | 2,550,000,000.00 USD | 0.00 USD | 2,550,000,000.00 USD | 2,350,000.00 USD | 1,090,000.00 USD | 1,640,000.00 USD |
| `1D` | `2109.50` | 1,110,000,000.00 USD | 0.00 USD | 1,110,000,000.00 USD | 151,690.00 USD | 401,490.00 USD | 148,130.00 USD |
| `7D` | `2111.00` | 2,540,000,000.00 USD | 0.00 USD | 2,540,000,000.00 USD | 3,450,000.00 USD | 1,620,000.00 USD | 2,160,000.00 USD |
| `1D` | `2112.20` | 1,110,000,000.00 USD | 0.00 USD | 1,110,000,000.00 USD | 1,290,000.00 USD | 946,650.00 USD | 556,430.00 USD |
| `7D` | `2113.80` | 2,540,000,000.00 USD | 0.00 USD | 2,540,000,000.00 USD | 1,080,000.00 USD | 1,300,000.00 USD | 2,730,000.00 USD |
| `1D` | `2114.90` | 1,100,000,000.00 USD | 0.00 USD | 1,100,000,000.00 USD | 9,210.00 USD | 0.00 USD | 441,270.00 USD |
| `7D` | `2116.60` | 2,530,000,000.00 USD | 0.00 USD | 2,530,000,000.00 USD | 2,360,000.00 USD | 2,350,000.00 USD | 2,570,000.00 USD |
| `1D` | `2117.60` | 1,100,000,000.00 USD | 0.00 USD | 1,100,000,000.00 USD | 1,280,000.00 USD | 339,800.00 USD | 811,240.00 USD |
| `7D` | `2119.40` | 2,520,000,000.00 USD | 0.00 USD | 2,520,000,000.00 USD | 2,530,000.00 USD | 606,940.00 USD | 2,590,000.00 USD |
| `1D` | `2120.30` | 1,100,000,000.00 USD | 0.00 USD | 1,100,000,000.00 USD | 650,890.00 USD | 428,990.00 USD | 1,250,000.00 USD |
| `7D` | `2122.20` | 2,520,000,000.00 USD | 0.00 USD | 2,520,000,000.00 USD | 2,230,000.00 USD | 1,000,000.00 USD | 1,630,000.00 USD |
| `1D` | `2123.00` | 1,100,000,000.00 USD | 0.00 USD | 1,100,000,000.00 USD | 1,630,000.00 USD | 716,530.00 USD | 1,050,000.00 USD |
| `7D` | `2125.00` | 2,510,000,000.00 USD | 0.00 USD | 2,510,000,000.00 USD | 2,700,000.00 USD | 2,150,000.00 USD | 2,640,000.00 USD |
| `1D` | `2125.70` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 179,030.00 USD | 1,520,000.00 USD | 513,720.00 USD |
| `7D` | `2127.80` | 2,510,000,000.00 USD | 0.00 USD | 2,510,000,000.00 USD | 496,060.00 USD | 1,960,000.00 USD | 1,630,000.00 USD |
| `1D` | `2128.40` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 365,910.00 USD | 623,840.00 USD | 129,160.00 USD |
| `7D` | `2130.60` | 2,500,000,000.00 USD | 0.00 USD | 2,500,000,000.00 USD | 2,040,000.00 USD | 1,750,000.00 USD | 1,700,000.00 USD |
| `1D` | `2131.10` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 0.00 USD | 644,330.00 USD | 654,700.00 USD |
| `7D` | `2133.40` | 2,500,000,000.00 USD | 0.00 USD | 2,500,000,000.00 USD | 2,120,000.00 USD | 550,450.00 USD | 316,050.00 USD |
| `1D` | `2133.80` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 187,520.00 USD | 497,320.00 USD | 0.00 USD |
| `7D` | `2136.20` | 2,490,000,000.00 USD | 0.00 USD | 2,490,000,000.00 USD | 1,170,000.00 USD | 845,110.00 USD | 18,020.00 USD |
| `1D` | `2136.50` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 0.00 USD | 294,600.00 USD | 2,870.00 USD |
| `7D` | `2139.00` | 2,490,000,000.00 USD | 0.00 USD | 2,490,000,000.00 USD | 1,110,000.00 USD | 1,000,000.00 USD | 276,890.00 USD |
| `1D` | `2139.20` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 555,320.00 USD | 250,240.00 USD | 205,180.00 USD |
| `7D` | `2141.80` | 2,490,000,000.00 USD | 0.00 USD | 2,490,000,000.00 USD | 1,550,000.00 USD | 209,240.00 USD | 819,060.00 USD |
| `1D` | `2144.60` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 295,510.00 USD | 16,700.00 USD | 3,100.00 USD |
| `7D` | `2144.60` | 2,490,000,000.00 USD | 0.00 USD | 2,490,000,000.00 USD | 547,980.00 USD | 1,530,000.00 USD | 0.00 USD |
| `1D` | `2147.30` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 0.00 USD | 11,090.00 USD | 207,420.00 USD |
| `7D` | `2147.40` | 2,480,000,000.00 USD | 0.00 USD | 2,480,000,000.00 USD | 157,100.00 USD | 32,210.00 USD | 0.00 USD |
| `1D` | `2150.00` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 251,250.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2150.20` | 2,480,000,000.00 USD | 0.00 USD | 2,480,000,000.00 USD | 459,630.00 USD | 482,820.00 USD | 537,180.00 USD |
| `7D` | `2153.00` | 2,480,000,000.00 USD | 0.00 USD | 2,480,000,000.00 USD | 58,340.00 USD | 681,070.00 USD | 800,440.00 USD |
| `7D` | `2155.80` | 2,480,000,000.00 USD | 0.00 USD | 2,480,000,000.00 USD | 191,860.00 USD | 454,940.00 USD | 66,320.00 USD |
| `7D` | `2158.60` | 2,480,000,000.00 USD | 0.00 USD | 2,480,000,000.00 USD | 774,660.00 USD | 1,260,000.00 USD | 1,660,000.00 USD |
| `7D` | `2161.40` | 2,480,000,000.00 USD | 0.00 USD | 2,480,000,000.00 USD | 1,450,000.00 USD | 804,860.00 USD | 2,170,000.00 USD |
| `7D` | `2164.20` | 2,470,000,000.00 USD | 0.00 USD | 2,470,000,000.00 USD | 36,870.00 USD | 329,690.00 USD | 409,110.00 USD |
| `7D` | `2167.00` | 2,470,000,000.00 USD | 0.00 USD | 2,470,000,000.00 USD | 25,540.00 USD | 0.00 USD | 84,450.00 USD |
| `7D` | `2169.80` | 2,470,000,000.00 USD | 0.00 USD | 2,470,000,000.00 USD | 1,700,000.00 USD | 726,240.00 USD | 794,200.00 USD |
| `7D` | `2172.60` | 2,470,000,000.00 USD | 0.00 USD | 2,470,000,000.00 USD | 479,540.00 USD | 1,150,000.00 USD | 0.00 USD |
| `7D` | `2195.00` | 2,470,000,000.00 USD | 0.00 USD | 2,470,000,000.00 USD | 141,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2197.80` | 2,470,000,000.00 USD | 0.00 USD | 2,470,000,000.00 USD | 2,440,000.00 USD | 3,270,000.00 USD | 0.00 USD |
| `7D` | `2200.60` | 2,460,000,000.00 USD | 0.00 USD | 2,460,000,000.00 USD | 3,120,000.00 USD | 3,140,000.00 USD | 3,200,000.00 USD |
| `1D` | `2201.30` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 284,470.00 USD | 217,490.00 USD | 225,330.00 USD |
| `7D` | `2203.40` | 2,450,000,000.00 USD | 0.00 USD | 2,450,000,000.00 USD | 3,280,000.00 USD | 624,500.00 USD | 2,720,000.00 USD |
| `1D` | `2204.00` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 1,050,000.00 USD | 207,110.00 USD | 792,260.00 USD |
| `7D` | `2206.20` | 2,440,000,000.00 USD | 0.00 USD | 2,440,000,000.00 USD | 6,770,000.00 USD | 4,010,000.00 USD | 4,980,000.00 USD |
| `1D` | `2206.70` | 1,080,000,000.00 USD | 0.00 USD | 1,080,000,000.00 USD | 2,070,000.00 USD | 2,270,000.00 USD | 1,760,000.00 USD |
| `7D` | `2209.00` | 2,430,000,000.00 USD | 0.00 USD | 2,430,000,000.00 USD | 9,190,000.00 USD | 7,030,000.00 USD | 4,130,000.00 USD |
| `1D` | `2209.40` | 1,080,000,000.00 USD | 0.00 USD | 1,080,000,000.00 USD | 1,170,000.00 USD | 668,670.00 USD | 1,970,000.00 USD |
| `7D` | `2211.80` | 2,410,000,000.00 USD | 0.00 USD | 2,410,000,000.00 USD | 8,790,000.00 USD | 8,110,000.00 USD | 6,870,000.00 USD |
| `1D` | `2212.10` | 1,070,000,000.00 USD | 0.00 USD | 1,070,000,000.00 USD | 3,180,000.00 USD | 1,580,000.00 USD | 1,790,000.00 USD |
| `7D` | `2214.60` | 2,380,000,000.00 USD | 0.00 USD | 2,380,000,000.00 USD | 14,850,000.00 USD | 14,220,000.00 USD | 10,020,000.00 USD |
| `1D` | `2214.80` | 1,070,000,000.00 USD | 0.00 USD | 1,070,000,000.00 USD | 6,410,000.00 USD | 4,340,000.00 USD | 5,100,000.00 USD |
| `7D` | `2217.40` | 2,340,000,000.00 USD | 0.00 USD | 2,340,000,000.00 USD | 13,750,000.00 USD | 10,950,000.00 USD | 7,320,000.00 USD |
| `1D` | `2217.50` | 1,050,000,000.00 USD | 0.00 USD | 1,050,000,000.00 USD | 4,250,000.00 USD | 5,300,000.00 USD | 1,840,000.00 USD |
| `1D` | `2220.20` | 1,040,000,000.00 USD | 0.00 USD | 1,040,000,000.00 USD | 3,770,000.00 USD | 4,230,000.00 USD | 574,920.00 USD |
| `7D` | `2220.20` | 2,310,000,000.00 USD | 0.00 USD | 2,310,000,000.00 USD | 12,830,000.00 USD | 7,840,000.00 USD | 3,390,000.00 USD |
| `1D` | `2222.90` | 1,030,000,000.00 USD | 0.00 USD | 1,030,000,000.00 USD | 5,840,000.00 USD | 3,820,000.00 USD | 2,990,000.00 USD |
| `7D` | `2223.00` | 2,290,000,000.00 USD | 0.00 USD | 2,290,000,000.00 USD | 6,930,000.00 USD | 5,300,000.00 USD | 11,550,000.00 USD |
| `1D` | `2225.60` | 1,020,000,000.00 USD | 0.00 USD | 1,020,000,000.00 USD | 2,730,000.00 USD | 5,760,000.00 USD | 2,420,000.00 USD |
| `7D` | `2225.80` | 2,260,000,000.00 USD | 0.00 USD | 2,260,000,000.00 USD | 11,900,000.00 USD | 12,610,000.00 USD | 6,520,000.00 USD |
| `1D` | `2228.30` | 1,010,000,000.00 USD | 0.00 USD | 1,010,000,000.00 USD | 5,110,000.00 USD | 1,430,000.00 USD | 771,090.00 USD |
| `7D` | `2228.60` | 2,230,000,000.00 USD | 0.00 USD | 2,230,000,000.00 USD | 7,530,000.00 USD | 5,580,000.00 USD | 9,590,000.00 USD |
| `1D` | `2231.00` | 1,000,000,000.00 USD | 0.00 USD | 1,000,000,000.00 USD | 3,720,000.00 USD | 2,610,000.00 USD | 3,110,000.00 USD |
| `7D` | `2231.40` | 2,210,000,000.00 USD | 0.00 USD | 2,210,000,000.00 USD | 10,960,000.00 USD | 2,990,000.00 USD | 14,790,000.00 USD |
| `1D` | `2233.70` | 991,260,000.00 USD | 0.00 USD | 991,260,000.00 USD | 7,010,000.00 USD | 4,050,000.00 USD | 2,450,000.00 USD |
| `7D` | `2234.20` | 2,180,000,000.00 USD | 0.00 USD | 2,180,000,000.00 USD | 17,000,000.00 USD | 12,020,000.00 USD | 7,540,000.00 USD |
| `1D` | `2236.40` | 977,760,000.00 USD | 0.00 USD | 977,760,000.00 USD | 2,710,000.00 USD | 2,070,000.00 USD | 3,930,000.00 USD |
| `7D` | `2237.00` | 2,150,000,000.00 USD | 0.00 USD | 2,150,000,000.00 USD | 6,950,000.00 USD | 11,130,000.00 USD | 4,810,000.00 USD |
| `1D` | `2239.10` | 969,050,000.00 USD | 0.00 USD | 969,050,000.00 USD | 1,130,000.00 USD | 2,260,000.00 USD | 621,440.00 USD |
| `7D` | `2239.80` | 2,120,000,000.00 USD | 0.00 USD | 2,120,000,000.00 USD | 7,410,000.00 USD | 6,730,000.00 USD | 9,280,000.00 USD |
| `1D` | `2241.80` | 965,040,000.00 USD | 0.00 USD | 965,040,000.00 USD | 736,150.00 USD | 12,140.00 USD | 360,200.00 USD |
| `7D` | `2242.60` | 2,100,000,000.00 USD | 0.00 USD | 2,100,000,000.00 USD | 7,790,000.00 USD | 2,710,000.00 USD | 4,500,000.00 USD |
| `1D` | `2244.50` | 963,930,000.00 USD | 0.00 USD | 963,930,000.00 USD | 2,500,000.00 USD | 1,860,000.00 USD | 265,580.00 USD |
| `7D` | `2245.40` | 2,080,000,000.00 USD | 0.00 USD | 2,080,000,000.00 USD | 12,040,000.00 USD | 12,530,000.00 USD | 10,610,000.00 USD |
| `1D` | `2247.20` | 959,310,000.00 USD | 0.00 USD | 959,310,000.00 USD | 1,800,000.00 USD | 946,140.00 USD | 1,110,000.00 USD |
| `7D` | `2248.20` | 2,050,000,000.00 USD | 0.00 USD | 2,050,000,000.00 USD | 13,950,000.00 USD | 5,870,000.00 USD | 11,630,000.00 USD |
| `1D` | `2249.90` | 955,450,000.00 USD | 0.00 USD | 955,450,000.00 USD | 3,390,000.00 USD | 1,710,000.00 USD | 1,790,000.00 USD |
| `7D` | `2251.00` | 2,020,000,000.00 USD | 0.00 USD | 2,020,000,000.00 USD | 12,710,000.00 USD | 11,300,000.00 USD | 8,550,000.00 USD |
| `1D` | `2252.60` | 948,560,000.00 USD | 0.00 USD | 948,560,000.00 USD | 7,060,000.00 USD | 7,800,000.00 USD | 5,270,000.00 USD |
| `7D` | `2253.80` | 1,990,000,000.00 USD | 0.00 USD | 1,990,000,000.00 USD | 25,660,000.00 USD | 20,190,000.00 USD | 19,820,000.00 USD |
| `1D` | `2255.30` | 928,430,000.00 USD | 0.00 USD | 928,430,000.00 USD | 3,350,000.00 USD | 2,460,000.00 USD | 5,490,000.00 USD |
| `7D` | `2256.60` | 1,920,000,000.00 USD | 0.00 USD | 1,920,000,000.00 USD | 29,170,000.00 USD | 24,230,000.00 USD | 17,560,000.00 USD |
| `1D` | `2258.00` | 917,130,000.00 USD | 0.00 USD | 917,130,000.00 USD | 10,230,000.00 USD | 4,670,000.00 USD | 4,840,000.00 USD |
| `7D` | `2259.40` | 1,850,000,000.00 USD | 0.00 USD | 1,850,000,000.00 USD | 25,970,000.00 USD | 15,650,000.00 USD | 27,050,000.00 USD |
| `1D` | `2260.70` | 897,400,000.00 USD | 0.00 USD | 897,400,000.00 USD | 15,440,000.00 USD | 9,960,000.00 USD | 10,820,000.00 USD |
| `7D` | `2262.20` | 1,780,000,000.00 USD | 0.00 USD | 1,780,000,000.00 USD | 46,580,000.00 USD | 30,720,000.00 USD | 19,820,000.00 USD |
| `1D` | `2263.40` | 861,180,000.00 USD | 0.00 USD | 861,180,000.00 USD | 11,650,000.00 USD | 14,790,000.00 USD | 11,190,000.00 USD |
| `7D` | `2265.00` | 1,680,000,000.00 USD | 0.00 USD | 1,680,000,000.00 USD | 29,070,000.00 USD | 25,860,000.00 USD | 16,140,000.00 USD |
| `1D` | `2266.10` | 823,540,000.00 USD | 0.00 USD | 823,540,000.00 USD | 12,420,000.00 USD | 11,610,000.00 USD | 3,450,000.00 USD |
| `7D` | `2267.80` | 1,610,000,000.00 USD | 0.00 USD | 1,610,000,000.00 USD | 41,280,000.00 USD | 43,110,000.00 USD | 32,090,000.00 USD |
| `1D` | `2268.80` | 796,060,000.00 USD | 0.00 USD | 796,060,000.00 USD | 14,780,000.00 USD | 11,070,000.00 USD | 8,860,000.00 USD |
| `7D` | `2270.60` | 1,500,000,000.00 USD | 0.00 USD | 1,500,000,000.00 USD | 43,030,000.00 USD | 30,540,000.00 USD | 36,990,000.00 USD |
| `1D` | `2271.50` | 761,350,000.00 USD | 0.00 USD | 761,350,000.00 USD | 9,670,000.00 USD | 10,000,000.00 USD | 9,220,000.00 USD |
| `7D` | `2273.40` | 1,380,000,000.00 USD | 0.00 USD | 1,380,000,000.00 USD | 27,330,000.00 USD | 19,600,000.00 USD | 20,130,000.00 USD |
| `1D` | `2274.20` | 732,460,000.00 USD | 0.00 USD | 732,460,000.00 USD | 11,980,000.00 USD | 9,210,000.00 USD | 5,550,000.00 USD |
| `7D` | `2276.20` | 1,320,000,000.00 USD | 0.00 USD | 1,320,000,000.00 USD | 55,750,000.00 USD | 46,480,000.00 USD | 59,460,000.00 USD |
| `1D` | `2276.90` | 705,720,000.00 USD | 0.00 USD | 705,720,000.00 USD | 21,220,000.00 USD | 14,790,000.00 USD | 14,590,000.00 USD |
| `7D` | `2279.00` | 1,160,000,000.00 USD | 0.00 USD | 1,160,000,000.00 USD | 71,690,000.00 USD | 30,780,000.00 USD | 36,640,000.00 USD |
| `1D` | `2279.60` | 655,130,000.00 USD | 0.00 USD | 655,130,000.00 USD | 18,510,000.00 USD | 12,820,000.00 USD | 11,240,000.00 USD |
| `7D` | `2281.80` | 1,020,000,000.00 USD | 0.00 USD | 1,020,000,000.00 USD | 64,270,000.00 USD | 63,850,000.00 USD | 39,490,000.00 USD |
| `1D` | `2282.30` | 612,560,000.00 USD | 0.00 USD | 612,560,000.00 USD | 23,240,000.00 USD | 18,900,000.00 USD | 19,550,000.00 USD |
| `7D` | `2284.60` | 849,390,000.00 USD | 0.00 USD | 849,390,000.00 USD | 84,980,000.00 USD | 71,990,000.00 USD | 47,600,000.00 USD |
| `1D` | `2285.00` | 550,870,000.00 USD | 0.00 USD | 550,870,000.00 USD | 29,050,000.00 USD | 25,280,000.00 USD | 19,700,000.00 USD |
| `7D` | `2287.40` | 644,830,000.00 USD | 0.00 USD | 644,830,000.00 USD | 57,800,000.00 USD | 54,380,000.00 USD | 45,750,000.00 USD |
| `1D` | `2287.70` | 476,840,000.00 USD | 0.00 USD | 476,840,000.00 USD | 22,660,000.00 USD | 14,830,000.00 USD | 5,280,000.00 USD |
| `7D` | `2290.20` | 486,890,000.00 USD | 0.00 USD | 486,890,000.00 USD | 45,650,000.00 USD | 33,150,000.00 USD | 39,040,000.00 USD |
| `1D` | `2290.40` | 434,070,000.00 USD | 0.00 USD | 434,070,000.00 USD | 10,470,000.00 USD | 15,850,000.00 USD | 3,080,000.00 USD |
| `7D` | `2293.00` | 369,060,000.00 USD | 0.00 USD | 369,060,000.00 USD | 33,030,000.00 USD | 15,200,000.00 USD | 23,140,000.00 USD |
| `1D` | `2293.10` | 404,670,000.00 USD | 0.00 USD | 404,670,000.00 USD | 23,490,000.00 USD | 20,570,000.00 USD | 13,980,000.00 USD |
| `1D` | `2295.80` | 346,630,000.00 USD | 0.00 USD | 346,630,000.00 USD | 22,630,000.00 USD | 15,930,000.00 USD | 8,770,000.00 USD |
| `7D` | `2295.80` | 297,690,000.00 USD | 0.00 USD | 297,690,000.00 USD | 17,510,000.00 USD | 9,480,000.00 USD | 6,790,000.00 USD |
| `1D` | `2298.50` | 299,290,000.00 USD | 0.00 USD | 299,290,000.00 USD | 9,030,000.00 USD | 7,220,000.00 USD | 3,270,000.00 USD |
| `7D` | `2298.60` | 263,910,000.00 USD | 0.00 USD | 263,910,000.00 USD | 2,760,000.00 USD | 4,450,000.00 USD | 358,390.00 USD |
| `1D` | `2301.20` | 279,770,000.00 USD | 0.00 USD | 279,770,000.00 USD | 17,170,000.00 USD | 12,340,000.00 USD | 13,340,000.00 USD |
| `7D` | `2301.40` | 256,340,000.00 USD | 0.00 USD | 256,340,000.00 USD | 11,120,000.00 USD | 2,120,000.00 USD | 7,540,000.00 USD |
| `1D` | `2303.90` | 236,930,000.00 USD | 0.00 USD | 236,930,000.00 USD | 29,770,000.00 USD | 16,570,000.00 USD | 13,120,000.00 USD |
| `7D` | `2304.20` | 235,560,000.00 USD | 0.00 USD | 235,560,000.00 USD | 32,960,000.00 USD | 16,920,000.00 USD | 13,270,000.00 USD |
| `1D` | `2306.60` | 177,460,000.00 USD | 0.00 USD | 177,460,000.00 USD | 4,970,000.00 USD | 4,390,000.00 USD | 15,360,000.00 USD |
| `7D` | `2307.00` | 172,410,000.00 USD | 0.00 USD | 172,410,000.00 USD | 0.00 USD | 3,740,000.00 USD | 10,890,000.00 USD |
| `1D` | `2309.30` | 152,750,000.00 USD | 0.00 USD | 152,750,000.00 USD | 3,760,000.00 USD | 2,320,000.00 USD | 822,750.00 USD |
| `7D` | `2309.80` | 157,780,000.00 USD | 0.00 USD | 157,780,000.00 USD | 282,530.00 USD | 300,580.00 USD | 1,500,000.00 USD |
| `1D` | `2312.00` | 145,850,000.00 USD | 0.00 USD | 145,850,000.00 USD | 9,070,000.00 USD | 5,970,000.00 USD | 6,290,000.00 USD |
| `7D` | `2312.60` | 155,690,000.00 USD | 0.00 USD | 155,690,000.00 USD | 2,470,000.00 USD | 640,510.00 USD | 2,620,000.00 USD |
| `1D` | `2314.70` | 124,520,000.00 USD | 0.00 USD | 124,520,000.00 USD | 8,520,000.00 USD | 9,160,000.00 USD | 1,750,000.00 USD |
| `7D` | `2315.40` | 149,960,000.00 USD | 0.00 USD | 149,960,000.00 USD | 5,830,000.00 USD | 4,100,000.00 USD | 0.00 USD |
| `1D` | `2317.40` | 105,090,000.00 USD | 0.00 USD | 105,090,000.00 USD | 8,380,000.00 USD | 4,290,000.00 USD | 3,390,000.00 USD |
| `7D` | `2318.20` | 140,030,000.00 USD | 0.00 USD | 140,030,000.00 USD | 0.00 USD | 3,010,000.00 USD | 0.00 USD |
| `1D` | `2320.10` | 89,030,000.00 USD | 0.00 USD | 89,030,000.00 USD | 4,730,000.00 USD | 3,110,000.00 USD | 1,720,000.00 USD |
| `7D` | `2321.00` | 137,020,000.00 USD | 0.00 USD | 137,020,000.00 USD | 947,800.00 USD | 2,960,000.00 USD | 0.00 USD |
| `1D` | `2322.80` | 79,470,000.00 USD | 0.00 USD | 79,470,000.00 USD | 5,160,000.00 USD | 1,870,000.00 USD | 0.00 USD |
| `7D` | `2323.80` | 133,110,000.00 USD | 0.00 USD | 133,110,000.00 USD | 3,130,000.00 USD | 2,210,000.00 USD | 0.00 USD |
| `1D` | `2325.50` | 72,440,000.00 USD | 0.00 USD | 72,440,000.00 USD | 4,120,000.00 USD | 2,830,000.00 USD | 3,290,000.00 USD |
| `7D` | `2326.60` | 127,780,000.00 USD | 0.00 USD | 127,780,000.00 USD | 0.00 USD | 0.00 USD | 126,530.00 USD |
| `1D` | `2328.20` | 62,200,000.00 USD | 0.00 USD | 62,200,000.00 USD | 1,890,000.00 USD | 3,130,000.00 USD | 3,600,000.00 USD |
| `7D` | `2329.40` | 127,650,000.00 USD | 0.00 USD | 127,650,000.00 USD | 3,860,000.00 USD | 0.00 USD | 4,880,000.00 USD |
| `1D` | `2330.90` | 53,580,000.00 USD | 0.00 USD | 53,580,000.00 USD | 5,350,000.00 USD | 1,150,000.00 USD | 2,810,000.00 USD |
| `7D` | `2332.20` | 118,910,000.00 USD | 0.00 USD | 118,910,000.00 USD | 29,230,000.00 USD | 0.00 USD | 2,810,000.00 USD |
| `1D` | `2333.60` | 44,270,000.00 USD | 0.00 USD | 44,270,000.00 USD | 7,850,000.00 USD | 12,110,000.00 USD | 5,460,000.00 USD |
| `7D` | `2335.00` | 86,860,000.00 USD | 0.00 USD | 86,860,000.00 USD | 13,560,000.00 USD | 18,420,000.00 USD | 8,930,000.00 USD |
| `1D` | `2336.30` | 18,850,000.00 USD | 0.00 USD | 18,850,000.00 USD | 12,670,000.00 USD | 6,180,000.00 USD | 0.00 USD |
| `7D` | `2337.80` | 45,960,000.00 USD | 0.00 USD | 45,960,000.00 USD | 14,090,000.00 USD | 18,310,000.00 USD | 13,560,000.00 USD |
| `7D` | `2338.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2338.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2339.00` | 10,810,000.00 USD | 10,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,810,000.00 USD |
| `7D` | `2340.60` | 18,930,000.00 USD | 18,930,000.00 USD | 0.00 USD | 0.00 USD | 15,560,000.00 USD | 3,380,000.00 USD |
| `1D` | `2341.70` | 14,160,000.00 USD | 14,160,000.00 USD | 0.00 USD | 1,880,000.00 USD | 0.00 USD | 1,470,000.00 USD |
| `7D` | `2343.40` | 26,100,000.00 USD | 26,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,160,000.00 USD |
| `1D` | `2344.40` | 23,760,000.00 USD | 23,760,000.00 USD | 0.00 USD | 963,370.00 USD | 1,960,000.00 USD | 6,680,000.00 USD |
| `7D` | `2346.20` | 43,520,000.00 USD | 43,520,000.00 USD | 0.00 USD | 0.00 USD | 7,920,000.00 USD | 9,500,000.00 USD |
| `1D` | `2347.10` | 27,770,000.00 USD | 27,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,000,000.00 USD |
| `7D` | `2349.00` | 71,940,000.00 USD | 71,940,000.00 USD | 0.00 USD | 495,290.00 USD | 11,840,000.00 USD | 16,080,000.00 USD |
| `1D` | `2349.80` | 53,260,000.00 USD | 53,260,000.00 USD | 0.00 USD | 22,960,000.00 USD | 2,510,000.00 USD | 23,220.00 USD |
| `7D` | `2351.80` | 85,960,000.00 USD | 85,960,000.00 USD | 0.00 USD | 572,980.00 USD | 13,100,000.00 USD | 351,920.00 USD |
| `1D` | `2352.50` | 57,190,000.00 USD | 57,190,000.00 USD | 0.00 USD | 3,690,000.00 USD | 121,980.00 USD | 107,380.00 USD |
| `7D` | `2354.60` | 130,750,000.00 USD | 130,750,000.00 USD | 0.00 USD | 9,800,000.00 USD | 34,750,000.00 USD | 237,340.00 USD |
| `1D` | `2355.20` | 76,190,000.00 USD | 76,190,000.00 USD | 0.00 USD | 663,120.00 USD | 17,100,000.00 USD | 1,240,000.00 USD |
| `7D` | `2357.40` | 141,700,000.00 USD | 141,700,000.00 USD | 0.00 USD | 5,040,000.00 USD | 5,920,000.00 USD | 0.00 USD |
| `1D` | `2357.90` | 77,980,000.00 USD | 77,980,000.00 USD | 0.00 USD | 1,400,000.00 USD | 191,800.00 USD | 198,570.00 USD |
| `7D` | `2360.20` | 144,140,000.00 USD | 144,140,000.00 USD | 0.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2360.60` | 83,150,000.00 USD | 83,150,000.00 USD | 0.00 USD | 2,010,000.00 USD | 1,830,000.00 USD | 1,330,000.00 USD |
| `7D` | `2363.00` | 146,540,000.00 USD | 146,540,000.00 USD | 0.00 USD | 715,490.00 USD | 0.00 USD | 1,690,000.00 USD |
| `1D` | `2363.30` | 94,890,000.00 USD | 94,890,000.00 USD | 0.00 USD | 3,730,000.00 USD | 7,640,000.00 USD | 360,460.00 USD |
| `7D` | `2365.80` | 154,540,000.00 USD | 154,540,000.00 USD | 0.00 USD | 6,340,000.00 USD | 0.00 USD | 1,660,000.00 USD |
| `1D` | `2366.00` | 95,270,000.00 USD | 95,270,000.00 USD | 0.00 USD | 192,950.00 USD | 0.00 USD | 189,560.00 USD |
| `7D` | `2368.60` | 165,020,000.00 USD | 165,020,000.00 USD | 0.00 USD | 9,590,000.00 USD | 475,460.00 USD | 404,380.00 USD |
| `1D` | `2368.70` | 107,540,000.00 USD | 107,540,000.00 USD | 0.00 USD | 7,840,000.00 USD | 3,260,000.00 USD | 1,170,000.00 USD |
| `1D` | `2371.40` | 147,510,000.00 USD | 147,510,000.00 USD | 0.00 USD | 17,450,000.00 USD | 13,550,000.00 USD | 8,970,000.00 USD |
| `7D` | `2371.40` | 230,830,000.00 USD | 230,830,000.00 USD | 0.00 USD | 18,630,000.00 USD | 0.00 USD | 47,190,000.00 USD |
| `1D` | `2374.10` | 163,580,000.00 USD | 163,580,000.00 USD | 0.00 USD | 13,230,000.00 USD | 349,710.00 USD | 2,490,000.00 USD |
| `7D` | `2374.20` | 249,340,000.00 USD | 249,340,000.00 USD | 0.00 USD | 13,960,000.00 USD | 0.00 USD | 4,550,000.00 USD |
| `1D` | `2376.80` | 192,950,000.00 USD | 192,950,000.00 USD | 0.00 USD | 12,180,000.00 USD | 5,320,000.00 USD | 11,870,000.00 USD |
| `7D` | `2377.00` | 289,730,000.00 USD | 289,730,000.00 USD | 0.00 USD | 12,140,000.00 USD | 6,190,000.00 USD | 22,050,000.00 USD |
| `1D` | `2379.50` | 226,210,000.00 USD | 226,210,000.00 USD | 0.00 USD | 7,980,000.00 USD | 12,400,000.00 USD | 12,870,000.00 USD |
| `7D` | `2379.80` | 317,920,000.00 USD | 317,920,000.00 USD | 0.00 USD | 7,180,000.00 USD | 2,330,000.00 USD | 18,680,000.00 USD |
| `1D` | `2382.20` | 272,040,000.00 USD | 272,040,000.00 USD | 0.00 USD | 20,360,000.00 USD | 11,020,000.00 USD | 14,460,000.00 USD |
| `7D` | `2382.60` | 359,310,000.00 USD | 359,310,000.00 USD | 0.00 USD | 8,620,000.00 USD | 12,380,000.00 USD | 20,400,000.00 USD |
| `1D` | `2384.90` | 323,330,000.00 USD | 323,330,000.00 USD | 0.00 USD | 19,430,000.00 USD | 22,000,000.00 USD | 9,870,000.00 USD |
| `7D` | `2385.40` | 455,660,000.00 USD | 455,660,000.00 USD | 0.00 USD | 15,530,000.00 USD | 30,320,000.00 USD | 50,510,000.00 USD |
| `1D` | `2387.60` | 357,190,000.00 USD | 357,190,000.00 USD | 0.00 USD | 13,120,000.00 USD | 13,690,000.00 USD | 7,050,000.00 USD |
| `7D` | `2388.20` | 532,620,000.00 USD | 532,620,000.00 USD | 0.00 USD | 4,500,000.00 USD | 34,050,000.00 USD | 38,400,000.00 USD |
| `1D` | `2390.30` | 375,800,000.00 USD | 375,800,000.00 USD | 0.00 USD | 5,560,000.00 USD | 6,220,000.00 USD | 6,820,000.00 USD |
| `7D` | `2391.00` | 629,010,000.00 USD | 629,010,000.00 USD | 0.00 USD | 5,620,000.00 USD | 45,790,000.00 USD | 44,980,000.00 USD |
| `1D` | `2393.00` | 406,320,000.00 USD | 406,320,000.00 USD | 0.00 USD | 7,290,000.00 USD | 15,180,000.00 USD | 8,050,000.00 USD |
| `7D` | `2393.80` | 741,320,000.00 USD | 741,320,000.00 USD | 0.00 USD | 48,290,000.00 USD | 27,870,000.00 USD | 36,150,000.00 USD |
| `1D` | `2395.70` | 427,630,000.00 USD | 427,630,000.00 USD | 0.00 USD | 9,390,000.00 USD | 9,260,000.00 USD | 2,650,000.00 USD |
| `7D` | `2396.60` | 815,610,000.00 USD | 815,610,000.00 USD | 0.00 USD | 26,490,000.00 USD | 29,530,000.00 USD | 18,270,000.00 USD |
| `1D` | `2398.40` | 458,080,000.00 USD | 458,080,000.00 USD | 0.00 USD | 6,170,000.00 USD | 12,390,000.00 USD | 11,890,000.00 USD |
| `7D` | `2399.40` | 913,790,000.00 USD | 913,790,000.00 USD | 0.00 USD | 49,120,000.00 USD | 29,120,000.00 USD | 19,940,000.00 USD |
| `1D` | `2401.10` | 495,610,000.00 USD | 495,610,000.00 USD | 0.00 USD | 20,930,000.00 USD | 8,040,000.00 USD | 8,550,000.00 USD |
| `7D` | `2402.20` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 0.00 USD | 45,210,000.00 USD | 27,170,000.00 USD | 31,130,000.00 USD |
| `1D` | `2403.80` | 531,140,000.00 USD | 531,140,000.00 USD | 0.00 USD | 14,520,000.00 USD | 11,360,000.00 USD | 9,660,000.00 USD |
| `7D` | `2405.00` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 35,270,000.00 USD | 26,450,000.00 USD | 17,010,000.00 USD |
| `1D` | `2406.50` | 562,050,000.00 USD | 562,050,000.00 USD | 0.00 USD | 11,930,000.00 USD | 10,410,000.00 USD | 8,560,000.00 USD |
| `7D` | `2407.80` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 26,280,000.00 USD | 26,510,000.00 USD | 16,810,000.00 USD |
| `1D` | `2409.20` | 590,780,000.00 USD | 590,780,000.00 USD | 0.00 USD | 7,630,000.00 USD | 11,180,000.00 USD | 9,930,000.00 USD |
| `7D` | `2410.60` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 23,140,000.00 USD | 26,640,000.00 USD | 27,330,000.00 USD |
| `1D` | `2411.90` | 618,440,000.00 USD | 618,440,000.00 USD | 0.00 USD | 14,580,000.00 USD | 8,760,000.00 USD | 4,330,000.00 USD |
| `7D` | `2413.40` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 0.00 USD | 15,370,000.00 USD | 14,870,000.00 USD | 9,740,000.00 USD |
| `1D` | `2414.60` | 630,060,000.00 USD | 630,060,000.00 USD | 0.00 USD | 3,070,000.00 USD | 3,950,000.00 USD | 4,590,000.00 USD |
| `7D` | `2416.20` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 0.00 USD | 26,140,000.00 USD | 16,790,000.00 USD | 32,420,000.00 USD |
| `1D` | `2417.30` | 643,950,000.00 USD | 643,950,000.00 USD | 0.00 USD | 3,970,000.00 USD | 6,830,000.00 USD | 3,080,000.00 USD |
| `7D` | `2419.00` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 30,180,000.00 USD | 17,120,000.00 USD | 11,520,000.00 USD |
| `1D` | `2420.00` | 658,530,000.00 USD | 658,530,000.00 USD | 0.00 USD | 7,860,000.00 USD | 4,500,000.00 USD | 2,230,000.00 USD |
| `7D` | `2421.80` | 1,490,000,000.00 USD | 1,490,000,000.00 USD | 0.00 USD | 21,830,000.00 USD | 26,230,000.00 USD | 20,940,000.00 USD |
| `1D` | `2422.70` | 674,340,000.00 USD | 674,340,000.00 USD | 0.00 USD | 4,910,000.00 USD | 5,090,000.00 USD | 5,810,000.00 USD |
| `7D` | `2424.60` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 25,990,000.00 USD | 31,850,000.00 USD | 32,010,000.00 USD |
| `1D` | `2425.40` | 679,340,000.00 USD | 679,340,000.00 USD | 0.00 USD | 1,500,000.00 USD | 2,650,000.00 USD | 852,240.00 USD |
| `7D` | `2427.40` | 1,640,000,000.00 USD | 1,640,000,000.00 USD | 0.00 USD | 25,000,000.00 USD | 18,790,000.00 USD | 24,200,000.00 USD |
| `1D` | `2428.10` | 681,390,000.00 USD | 681,390,000.00 USD | 0.00 USD | 1,930,000.00 USD | 89,750.00 USD | 39,130.00 USD |
| `7D` | `2430.20` | 1,670,000,000.00 USD | 1,670,000,000.00 USD | 0.00 USD | 6,090,000.00 USD | 16,890,000.00 USD | 6,180,000.00 USD |
| `1D` | `2430.80` | 684,010,000.00 USD | 684,010,000.00 USD | 0.00 USD | 1,100,000.00 USD | 964,820.00 USD | 562,240.00 USD |
| `7D` | `2433.00` | 1,710,000,000.00 USD | 1,710,000,000.00 USD | 0.00 USD | 15,680,000.00 USD | 12,450,000.00 USD | 5,820,000.00 USD |
| `1D` | `2433.50` | 689,460,000.00 USD | 689,460,000.00 USD | 0.00 USD | 2,160,000.00 USD | 1,550,000.00 USD | 1,740,000.00 USD |
| `7D` | `2435.80` | 1,760,000,000.00 USD | 1,760,000,000.00 USD | 0.00 USD | 20,300,000.00 USD | 12,110,000.00 USD | 17,110,000.00 USD |
| `1D` | `2436.20` | 694,100,000.00 USD | 694,100,000.00 USD | 0.00 USD | 3,200,000.00 USD | 1,240,000.00 USD | 199,720.00 USD |
| `7D` | `2438.60` | 1,820,000,000.00 USD | 1,820,000,000.00 USD | 0.00 USD | 21,710,000.00 USD | 24,630,000.00 USD | 15,730,000.00 USD |
| `1D` | `2438.90` | 696,720,000.00 USD | 696,720,000.00 USD | 0.00 USD | 340,220.00 USD | 1,090,000.00 USD | 1,180,000.00 USD |
| `7D` | `2441.40` | 1,850,000,000.00 USD | 1,850,000,000.00 USD | 0.00 USD | 13,540,000.00 USD | 6,350,000.00 USD | 13,870,000.00 USD |
| `1D` | `2441.60` | 704,010,000.00 USD | 704,010,000.00 USD | 0.00 USD | 3,730,000.00 USD | 2,790,000.00 USD | 767,510.00 USD |
| `7D` | `2444.20` | 1,890,000,000.00 USD | 1,890,000,000.00 USD | 0.00 USD | 9,430,000.00 USD | 15,220,000.00 USD | 11,100,000.00 USD |
| `1D` | `2444.30` | 707,710,000.00 USD | 707,710,000.00 USD | 0.00 USD | 787,570.00 USD | 1,430,000.00 USD | 1,490,000.00 USD |
| `1D` | `2447.00` | 713,990,000.00 USD | 713,990,000.00 USD | 0.00 USD | 3,610,000.00 USD | 642,690.00 USD | 2,030,000.00 USD |
| `7D` | `2447.00` | 1,920,000,000.00 USD | 1,920,000,000.00 USD | 0.00 USD | 11,560,000.00 USD | 5,380,000.00 USD | 18,490,000.00 USD |
| `1D` | `2449.70` | 722,360,000.00 USD | 722,360,000.00 USD | 0.00 USD | 2,500,000.00 USD | 2,360,000.00 USD | 3,510,000.00 USD |
| `7D` | `2449.80` | 1,960,000,000.00 USD | 1,960,000,000.00 USD | 0.00 USD | 16,990,000.00 USD | 11,970,000.00 USD | 11,930,000.00 USD |
| `1D` | `2452.40` | 733,590,000.00 USD | 733,590,000.00 USD | 0.00 USD | 3,790,000.00 USD | 3,100,000.00 USD | 4,330,000.00 USD |
| `7D` | `2452.60` | 1,980,000,000.00 USD | 1,980,000,000.00 USD | 0.00 USD | 6,280,000.00 USD | 7,310,000.00 USD | 6,840,000.00 USD |
| `1D` | `2455.10` | 744,430,000.00 USD | 744,430,000.00 USD | 0.00 USD | 3,950,000.00 USD | 4,190,000.00 USD | 2,700,000.00 USD |
| `7D` | `2455.40` | 2,010,000,000.00 USD | 2,010,000,000.00 USD | 0.00 USD | 8,340,000.00 USD | 10,630,000.00 USD | 5,580,000.00 USD |
| `1D` | `2457.80` | 751,540,000.00 USD | 751,540,000.00 USD | 0.00 USD | 3,120,000.00 USD | 2,530,000.00 USD | 1,460,000.00 USD |
| `7D` | `2458.20` | 2,040,000,000.00 USD | 2,040,000,000.00 USD | 0.00 USD | 9,800,000.00 USD | 7,130,000.00 USD | 11,540,000.00 USD |
| `1D` | `2460.50` | 755,550,000.00 USD | 755,550,000.00 USD | 0.00 USD | 1,260,000.00 USD | 1,430,000.00 USD | 1,330,000.00 USD |
| `7D` | `2461.00` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 0.00 USD | 6,890,000.00 USD | 10,680,000.00 USD | 9,050,000.00 USD |
| `1D` | `2463.20` | 758,870,000.00 USD | 758,870,000.00 USD | 0.00 USD | 174,920.00 USD | 2,050,000.00 USD | 1,100,000.00 USD |
| `7D` | `2463.80` | 2,090,000,000.00 USD | 2,090,000,000.00 USD | 0.00 USD | 10,390,000.00 USD | 8,820,000.00 USD | 5,210,000.00 USD |
| `1D` | `2465.90` | 760,940,000.00 USD | 760,940,000.00 USD | 0.00 USD | 820,990.00 USD | 1,240,000.00 USD | 5,650.00 USD |
| `7D` | `2466.60` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 0.00 USD | 4,840,000.00 USD | 2,680,000.00 USD | 1,330,000.00 USD |
| `1D` | `2468.60` | 762,340,000.00 USD | 762,340,000.00 USD | 0.00 USD | 0.00 USD | 998,350.00 USD | 399,070.00 USD |
| `7D` | `2469.40` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 0.00 USD | 2,470,000.00 USD | 2,980,000.00 USD | 408,300.00 USD |
| `1D` | `2471.30` | 765,380,000.00 USD | 765,380,000.00 USD | 0.00 USD | 1,390,000.00 USD | 883,290.00 USD | 764,250.00 USD |
| `7D` | `2472.20` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 0.00 USD | 3,060,000.00 USD | 2,760,000.00 USD | 1,210,000.00 USD |
| `1D` | `2474.00` | 765,610,000.00 USD | 765,610,000.00 USD | 0.00 USD | 0.00 USD | 232,740.00 USD | 3,820.00 USD |
| `7D` | `2475.00` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 0.00 USD | 5,400,000.00 USD | 866,790.00 USD | 2,020,000.00 USD |
| `1D` | `2476.70` | 766,360,000.00 USD | 766,360,000.00 USD | 0.00 USD | 738,780.00 USD | 0.00 USD | 7,750.00 USD |
| `7D` | `2477.80` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 0.00 USD | 1,840,000.00 USD | 5,290,000.00 USD | 505,810.00 USD |
| `1D` | `2479.40` | 766,950,000.00 USD | 766,950,000.00 USD | 0.00 USD | 0.00 USD | 69,480.00 USD | 518,550.00 USD |
| `7D` | `2480.60` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 0.00 USD | 1,070,000.00 USD | 350,090.00 USD | 0.00 USD |
| `1D` | `2482.10` | 767,580,000.00 USD | 767,580,000.00 USD | 0.00 USD | 628,130.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2483.40` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 0.00 USD | 1,310,000.00 USD | 1,310,000.00 USD | 2,070,000.00 USD |
| `7D` | `2486.20` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 0.00 USD | 586,480.00 USD | 1,560,000.00 USD | 0.00 USD |
| `7D` | `2489.00` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 0.00 USD | 1,760,000.00 USD | 857,130.00 USD | 2,100,000.00 USD |
| `7D` | `2491.80` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 0.00 USD | 2,400,000.00 USD | 3,310,000.00 USD | 1,720,000.00 USD |
| `7D` | `2494.60` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,950,000.00 USD | 6,220,000.00 USD |
| `7D` | `2497.40` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 0.00 USD | 3,640,000.00 USD | 3,570,000.00 USD | 4,430,000.00 USD |
| `7D` | `2500.20` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 0.00 USD | 1,160,000.00 USD | 2,430,000.00 USD | 1,090,000.00 USD |
| `7D` | `2503.00` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 0.00 USD | 111,800.00 USD | 1,430,000.00 USD | 170,270.00 USD |
| `7D` | `2505.80` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 0.00 USD | 4,240,000.00 USD | 2,320,000.00 USD | 2,040,000.00 USD |
| `7D` | `2508.60` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 0.00 USD | 714,660.00 USD | 1,270,000.00 USD | 629,120.00 USD |
| `7D` | `2511.40` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 0.00 USD | 1,900,000.00 USD | 3,230,000.00 USD | 2,010,000.00 USD |
| `7D` | `2514.20` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 0.00 USD | 776,920.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2517.00` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 0.00 USD | 97,050.00 USD | 189,640.00 USD | 0.00 USD |
| `7D` | `2519.80` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD |
| `1D` | `2519.90` | 767,610,000.00 USD | 767,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 32,260.00 USD |
| `1D` | `2522.60` | 767,810,000.00 USD | 767,810,000.00 USD | 0.00 USD | 80,610.00 USD | 61,830.00 USD | 57,880.00 USD |
| `7D` | `2522.60` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 0.00 USD | 1,050,000.00 USD | 0.00 USD | 945,860.00 USD |
| `1D` | `2525.30` | 768,340,000.00 USD | 768,340,000.00 USD | 0.00 USD | 421,540.00 USD | 57,450.00 USD | 53,680.00 USD |
| `7D` | `2525.40` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 0.00 USD | 307,040.00 USD | 224,130.00 USD | 200,040.00 USD |
| `1D` | `2528.00` | 769,020,000.00 USD | 769,020,000.00 USD | 0.00 USD | 0.00 USD | 645,910.00 USD | 26,970.00 USD |
| `7D` | `2528.20` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 0.00 USD | 1,580,000.00 USD | 1,690,000.00 USD | 727,590.00 USD |
| `1D` | `2530.70` | 770,450,000.00 USD | 770,450,000.00 USD | 0.00 USD | 995,550.00 USD | 0.00 USD | 437,490.00 USD |
| `7D` | `2531.00` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 0.00 USD | 2,080,000.00 USD | 1,480,000.00 USD | 1,230,000.00 USD |
| `1D` | `2533.40` | 770,860,000.00 USD | 770,860,000.00 USD | 0.00 USD | 394,310.00 USD | 0.00 USD | 16,730.00 USD |
| `7D` | `2533.80` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 0.00 USD | 2,750,000.00 USD | 1,730,000.00 USD | 1,370,000.00 USD |
| `1D` | `2536.10` | 773,760,000.00 USD | 773,760,000.00 USD | 0.00 USD | 1,130,000.00 USD | 698,510.00 USD | 1,080,000.00 USD |
| `7D` | `2536.60` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 0.00 USD | 3,590,000.00 USD | 2,850,000.00 USD | 2,750,000.00 USD |
| `1D` | `2538.80` | 777,810,000.00 USD | 777,810,000.00 USD | 0.00 USD | 1,710,000.00 USD | 738,070.00 USD | 1,590,000.00 USD |
| `7D` | `2539.40` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 0.00 USD | 2,620,000.00 USD | 2,580,000.00 USD | 1,090,000.00 USD |
| `1D` | `2541.50` | 779,430,000.00 USD | 779,430,000.00 USD | 0.00 USD | 692,360.00 USD | 856,910.00 USD | 69,460.00 USD |
| `7D` | `2542.20` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 0.00 USD | 3,400,000.00 USD | 2,620,000.00 USD | 2,230,000.00 USD |
| `1D` | `2544.20` | 781,430,000.00 USD | 781,430,000.00 USD | 0.00 USD | 996,980.00 USD | 983,870.00 USD | 16,590.00 USD |
| `7D` | `2545.00` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 0.00 USD | 2,170,000.00 USD | 1,830,000.00 USD | 1,350,000.00 USD |
| `1D` | `2546.90` | 785,130,000.00 USD | 785,130,000.00 USD | 0.00 USD | 1,680,000.00 USD | 1,280,000.00 USD | 749,430.00 USD |
| `7D` | `2547.80` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 938,680.00 USD | 2,940,000.00 USD |
| `1D` | `2549.60` | 786,900,000.00 USD | 786,900,000.00 USD | 0.00 USD | 338,020.00 USD | 949,700.00 USD | 481,610.00 USD |
| `7D` | `2550.60` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 0.00 USD | 2,920,000.00 USD | 2,720,000.00 USD | 1,610,000.00 USD |
| `1D` | `2552.30` | 789,570,000.00 USD | 789,570,000.00 USD | 0.00 USD | 1,720,000.00 USD | 728,770.00 USD | 224,040.00 USD |
| `7D` | `2553.40` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 0.00 USD | 2,590,000.00 USD | 756,730.00 USD | 2,090,000.00 USD |
| `1D` | `2555.00` | 790,830,000.00 USD | 790,830,000.00 USD | 0.00 USD | 775,150.00 USD | 215,880.00 USD | 268,410.00 USD |
| `7D` | `2556.20` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 0.00 USD | 2,760,000.00 USD | 255,750.00 USD | 4,940,000.00 USD |
| `1D` | `2557.70` | 792,790,000.00 USD | 792,790,000.00 USD | 0.00 USD | 758,880.00 USD | 518,220.00 USD | 680,960.00 USD |
| `7D` | `2559.00` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 0.00 USD | 4,380,000.00 USD | 1,640,000.00 USD | 2,340,000.00 USD |
| `1D` | `2560.40` | 796,530,000.00 USD | 796,530,000.00 USD | 0.00 USD | 1,840,000.00 USD | 1,090,000.00 USD | 809,280.00 USD |
| `7D` | `2561.80` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 2,260,000.00 USD | 1,960,000.00 USD | 802,060.00 USD |
| `1D` | `2563.10` | 798,460,000.00 USD | 798,460,000.00 USD | 0.00 USD | 440,660.00 USD | 504,630.00 USD | 984,190.00 USD |
| `7D` | `2564.60` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 1,800,000.00 USD | 2,100,000.00 USD | 1,100,000.00 USD |
| `1D` | `2565.80` | 799,320,000.00 USD | 799,320,000.00 USD | 0.00 USD | 160,570.00 USD | 700,850.00 USD | 0.00 USD |
| `7D` | `2567.40` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 575,630.00 USD | 1,240,000.00 USD | 2,690,000.00 USD |
| `1D` | `2568.50` | 799,510,000.00 USD | 799,510,000.00 USD | 0.00 USD | 46,810.00 USD | 0.00 USD | 144,080.00 USD |
| `7D` | `2570.20` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 0.00 USD | 125,250.00 USD | 290,680.00 USD | 1,210,000.00 USD |
| `1D` | `2571.20` | 800,570,000.00 USD | 800,570,000.00 USD | 0.00 USD | 874,480.00 USD | 182,720.00 USD | 5,200.00 USD |
| `7D` | `2573.00` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,770,000.00 USD |
| `1D` | `2573.90` | 801,350,000.00 USD | 801,350,000.00 USD | 0.00 USD | 97,380.00 USD | 405,200.00 USD | 272,920.00 USD |
| `7D` | `2575.80` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 0.00 USD | 2,180,000.00 USD | 344,620.00 USD | 1,060,000.00 USD |
| `1D` | `2576.60` | 801,980,000.00 USD | 801,980,000.00 USD | 0.00 USD | 432,440.00 USD | 198,080.00 USD | 0.00 USD |
| `7D` | `2578.60` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 0.00 USD | 797,100.00 USD | 1,500,000.00 USD | 1,760,000.00 USD |
| `1D` | `2579.30` | 802,680,000.00 USD | 802,680,000.00 USD | 0.00 USD | 14,180.00 USD | 203,420.00 USD | 479,750.00 USD |
| `7D` | `2581.40` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 0.00 USD | 3,860,000.00 USD | 895,740.00 USD | 3,210,000.00 USD |
| `1D` | `2582.00` | 805,160,000.00 USD | 805,160,000.00 USD | 0.00 USD | 1,300,000.00 USD | 946,650.00 USD | 234,280.00 USD |
| `7D` | `2584.20` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 0.00 USD | 88,840.00 USD | 1,820,000.00 USD | 1,570,000.00 USD |
| `1D` | `2584.70` | 805,590,000.00 USD | 805,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 431,790.00 USD |
| `7D` | `2587.00` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 0.00 USD | 2,360,000.00 USD | 1,800,000.00 USD | 1,510,000.00 USD |
| `1D` | `2587.40` | 807,620,000.00 USD | 807,620,000.00 USD | 0.00 USD | 1,260,000.00 USD | 337,700.00 USD | 439,060.00 USD |
| `7D` | `2589.80` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 0.00 USD | 2,470,000.00 USD | 287,400.00 USD | 2,590,000.00 USD |
| `1D` | `2590.10` | 809,230,000.00 USD | 809,230,000.00 USD | 0.00 USD | 493,030.00 USD | 199,120.00 USD | 916,490.00 USD |
| `7D` | `2592.60` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 0.00 USD | 2,300,000.00 USD | 1,280,000.00 USD | 1,130,000.00 USD |
| `1D` | `2592.80` | 811,730,000.00 USD | 811,730,000.00 USD | 0.00 USD | 973,570.00 USD | 759,970.00 USD | 766,970.00 USD |
| `7D` | `2595.40` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 0.00 USD | 413,920.00 USD | 569,790.00 USD | 1,240,000.00 USD |
| `1D` | `2595.50` | 814,490,000.00 USD | 814,490,000.00 USD | 0.00 USD | 898,410.00 USD | 861,700.00 USD | 1,000,000.00 USD |
| `1D` | `2598.20` | 815,960,000.00 USD | 815,960,000.00 USD | 0.00 USD | 118,170.00 USD | 845,320.00 USD | 506,380.00 USD |
| `7D` | `2598.20` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 0.00 USD | 2,280,000.00 USD | 1,910,000.00 USD | 2,570,000.00 USD |
| `1D` | `2600.90` | 817,080,000.00 USD | 817,080,000.00 USD | 0.00 USD | 365,910.00 USD | 623,840.00 USD | 129,160.00 USD |
| `7D` | `2601.00` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 0.00 USD | 931,390.00 USD | 1,670,000.00 USD | 955,630.00 USD |
| `1D` | `2603.60` | 817,420,000.00 USD | 817,420,000.00 USD | 0.00 USD | 0.00 USD | 18,610.00 USD | 323,080.00 USD |
| `7D` | `2603.80` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,580,000.00 USD | 1,690,000.00 USD |
| `1D` | `2606.30` | 818,690,000.00 USD | 818,690,000.00 USD | 0.00 USD | 0.00 USD | 937,720.00 USD | 331,620.00 USD |
| `7D` | `2606.60` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 1,480,000.00 USD | 463,200.00 USD | 312,730.00 USD |
| `1D` | `2609.00` | 819,060,000.00 USD | 819,060,000.00 USD | 0.00 USD | 187,520.00 USD | 185,320.00 USD | 0.00 USD |
| `7D` | `2609.40` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 1,090,000.00 USD | 489,790.00 USD | 10,700.00 USD |
| `1D` | `2611.70` | 819,610,000.00 USD | 819,610,000.00 USD | 0.00 USD | 0.00 USD | 544,840.00 USD | 2,870.00 USD |
| `7D` | `2612.20` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 770,330.00 USD | 608,060.00 USD | 43,560.00 USD |
| `1D` | `2614.40` | 820,370,000.00 USD | 820,370,000.00 USD | 0.00 USD | 555,320.00 USD | 0.00 USD | 205,180.00 USD |
| `7D` | `2615.00` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 1,060,000.00 USD | 1,000,000.00 USD | 635,670.00 USD |
| `7D` | `2617.80` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 1,550,000.00 USD | 209,240.00 USD | 434,750.00 USD |
| `7D` | `2620.60` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 0.00 USD | 465,960.00 USD | 1,530,000.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `LONGS_FLUSHED` | 349,060.00 USD | 0.00 USD | 349,060.00 USD | -349,060.00 USD | `6` | `2026-10-29 18:05:00 UTC - 2026-10-29 18:10:00 UTC` |
| `15m` | `LONGS_FLUSHED` | 349,060.00 USD | 0.00 USD | 349,060.00 USD | -349,060.00 USD | `6` | `2026-10-29 18:00:00 UTC - 2026-10-29 18:15:00 UTC` |
| `1h` | `LONGS_FLUSHED` | 349,060.00 USD | 0.00 USD | 349,060.00 USD | -349,060.00 USD | `6` | `2026-10-29 18:00:00 UTC - 2026-10-29 19:00:00 UTC` |
| `4h` | `LONGS_FLUSHED` | 349,060.00 USD | 0.00 USD | 349,060.00 USD | -349,060.00 USD | `6` | `2026-10-29 16:00:00 UTC - 2026-10-29 20:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `29.94B` | Total OI Tokens: `12,799,153.7 ETH`
  * 1h OI Change: `-1.14%` | 4h OI Change: `-1.13%` | 24h OI Change: `+0.29%`
  * Exchange Breakdown: Binance=`8.91B` | Bybit=`2.11B` | OKX=`1.80B` | Hyperliquid=`2.55B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `1.16M` | Last 24h: `2.27M` | Last 3d: `7.66M` | Last 7d: `13.85M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0095%` | **USDT KuCoin** | `0.0078%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0045%` |
| **CoinM Binance** | `0.0094%` | **CoinM OKX** | `0.0073%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `59.04%` | `40.96%` | `1.44` | 410,390,000.00 USD |
| `15M` | `Binance` | `56.9%` | `43.1%` | `1.32` | 112,940,000.00 USD |
| `15M` | `OKX` | `59.28%` | `40.72%` | `1.46` | 82,970,000.00 USD |
| `15M` | `Bybit` | `65.73%` | `34.27%` | `1.92` | 18,770,000.00 USD |
| `15M` | `KuCoin` | `60.94%` | `39.06%` | `1.56` | 1,220,000.00 USD |
| `15M` | `Gate` | `57.28%` | `42.72%` | `1.34` | 72,540,000.00 USD |
| `15M` | `Bitget` | `60.8%` | `39.2%` | `1.55` | 19,590,000.00 USD |
| `15M` | `BingX` | `72.9%` | `27.1%` | `2.69` | 5,360,000.00 USD |
| `15M` | `MEXC` | `57.5%` | `42.5%` | `1.35` | 25,950,000.00 USD |
| `15M` | `Bitunix` | `52.06%` | `47.94%` | `1.09` | 16,080,000.00 USD |
| `15M` | `Hyperliquid` | `42.92%` | `57.08%` | `0.75` | 3,650,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `62.57%` | `37.43%` | `1.67` | 1,380,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `77.08%` | `22.92%` | `3.36` | 29,860,000.00 USD |
| `15M` | `HTX` | `52.5%` | `47.5%` | `1.11` | 2,070,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `45.14%` | `54.86%` | `0.82` | 3,650,000.00 USD |
| `15M` | `Bitfinex` | `70.07%` | `29.93%` | `2.34` | 19,790.00 USD |
| `15M` | `Kraken` | `25.82%` | `74.18%` | `0.35` | 1,870,000.00 USD |
| `15M` | `Aster` | `38.48%` | `61.52%` | `0.63` | 5,430,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `61.65%` | `38.35%` | `1.61` | 7,060,000.00 USD |
| `15M` | `Whale Positions` | `56.9%` | `43.1%` | `1.32` | 112,940,000.00 USD |
| `15M` | `Global Accounts` | `59.04%` | `40.96%` | `1.44` | 410,390,000.00 USD |
| `1H` | `ETH` | `48.28%` | `51.72%` | `0.93` | 2,150,000,000.00 USD |
| `1H` | `Binance` | `46%` | `54%` | `0.85` | 605,800,000.00 USD |
| `1H` | `OKX` | `44.77%` | `55.23%` | `0.81` | 435,350,000.00 USD |
| `1H` | `Bybit` | `48.57%` | `51.43%` | `0.94` | 135,390,000.00 USD |
| `1H` | `KuCoin` | `53.82%` | `46.18%` | `1.17` | 5,670,000.00 USD |
| `1H` | `Gate` | `50.13%` | `49.87%` | `1.01` | 336,750,000.00 USD |
| `1H` | `Bitget` | `51.14%` | `48.86%` | `1.05` | 116,560,000.00 USD |
| `1H` | `BingX` | `52.47%` | `47.53%` | `1.10` | 22,200,000.00 USD |
| `1H` | `MEXC` | `50.65%` | `49.35%` | `1.03` | 111,400,000.00 USD |
| `1H` | `Bitunix` | `50.13%` | `49.87%` | `1.01` | 79,070,000.00 USD |
| `1H` | `Hyperliquid` | `70.76%` | `29.24%` | `2.42` | 77,120,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.32%` | `50.68%` | `0.97` | 4,160,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `64.3%` | `35.7%` | `1.80` | 91,460,000.00 USD |
| `1H` | `HTX` | `13.92%` | `86.08%` | `0.16` | 46,700,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `48.98%` | `51.02%` | `0.96` | 23,600,000.00 USD |
| `1H` | `Bitfinex` | `40.19%` | `59.81%` | `0.67` | 238,730.00 USD |
| `1H` | `Kraken` | `32.96%` | `67.04%` | `0.49` | 6,360,000.00 USD |
| `1H` | `Aster` | `41.17%` | `58.83%` | `0.70` | 24,870,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `49.93%` | `50.07%` | `1.00` | 29,790,000.00 USD |
| `1H` | `Whale Positions` | `46%` | `54%` | `0.85` | 605,800,000.00 USD |
| `1H` | `Global Accounts` | `48.28%` | `51.72%` | `0.93` | 2,150,000,000.00 USD |
| `4H` | `ETH` | `49.97%` | `50.03%` | `1.00` | 20,860,000,000.00 USD |
| `4H` | `Binance` | `48.85%` | `51.15%` | `0.96` | 6,550,000,000.00 USD |
| `4H` | `OKX` | `49.67%` | `50.33%` | `0.99` | 3,020,000,000.00 USD |
| `4H` | `Bybit` | `49%` | `51%` | `0.96` | 2,100,000,000.00 USD |
| `4H` | `KuCoin` | `40.61%` | `59.39%` | `0.68` | 82,850,000.00 USD |
| `4H` | `Gate` | `50.99%` | `49.01%` | `1.04` | 2,450,000,000.00 USD |
| `4H` | `Bitget` | `49.53%` | `50.47%` | `0.98` | 1,260,000,000.00 USD |
| `4H` | `BingX` | `50.52%` | `49.48%` | `1.02` | 391,440,000.00 USD |
| `4H` | `MEXC` | `52.56%` | `47.44%` | `1.11` | 1,110,000,000.00 USD |
| `4H` | `Bitunix` | `47.78%` | `52.22%` | `0.91` | 1,030,000,000.00 USD |
| `4H` | `Hyperliquid` | `53.12%` | `46.88%` | `1.13` | 1,040,000,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.79%` | `50.21%` | `0.99` | 129,920,000.00 USD |
| `4H` | `Crypto.com` | `48.4%` | `51.6%` | `0.94` | 141,140,000.00 USD |
| `4H` | `WhiteBIT` | `58.65%` | `41.35%` | `1.42` | 394,300,000.00 USD |
| `4H` | `HTX` | `46.99%` | `53.01%` | `0.89` | 84,050,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `54.27%` | `45.73%` | `1.19` | 396,920,000.00 USD |
| `4H` | `Bitfinex` | `63.09%` | `36.91%` | `1.71` | 24,190,000.00 USD |
| `4H` | `Kraken` | `53.53%` | `46.47%` | `1.15` | 154,980,000.00 USD |
| `4H` | `Aster` | `47.56%` | `52.44%` | `0.91` | 229,460,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.29%` | `49.71%` | `1.01` | 266,760,000.00 USD |
| `4H` | `Whale Positions` | `48.85%` | `51.15%` | `0.96` | 6,550,000,000.00 USD |
| `4H` | `Global Accounts` | `49.97%` | `50.03%` | `1.00` | 20,860,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `2370.25` | `2367.30` | `2370.25` | `2372.25` | `2362.75` | 152,368,912.49 USD | 65,939,044.63 USD | 86,429,867.86 USD | -20,490,823.24 USD | `-13.45%` | `0B / 0S` |
| `0:00 UTC` | `2367.25` | `2370.68` | `2367.25` | `2378.75` | `2362.25` | 227,963,041.65 USD | 108,724,843.75 USD | 119,238,197.91 USD | -10,513,354.16 USD | `-4.61%` | `6B / 3S` |
| `5:00 UTC` | `2360.25` | `2359.15` | `2360.25` | `2367.25` | `2354.75` | 178,447,053.53 USD | 59,723,171.00 USD | 118,723,882.53 USD | -59,000,711.54 USD | `-33.06%` | `0B / 9S` |
| `0:00 UTC` | `2358.25` | `2354.41` | `2358.25` | `2359.25` | `2350.25` | 125,220,561.61 USD | 53,594,674.80 USD | 71,625,886.81 USD | -18,031,212.02 USD | `-14.40%` | `0B / 1S` |
| `5:00 UTC` | `2353.75` | `2353.63` | `2353.75` | `2358.25` | `2350.75` | 70,925,128.95 USD | 26,607,996.94 USD | 44,317,132.01 USD | -17,709,135.06 USD | `-24.97%` | `0B / 2S` |
| `0:00 UTC` | `2350.75` | `2351.46` | `2350.75` | `2353.75` | `2348.75` | 91,943,279.10 USD | 36,371,657.16 USD | 55,571,621.93 USD | -19,199,964.77 USD | `-20.88%` | `0B / 3S` |
| `5:00 UTC` | `2350.25` | `2349.30` | `2350.25` | `2352.75` | `2346.75` | 77,932,643.01 USD | 38,640,268.57 USD | 39,292,374.44 USD | -652,105.87 USD | `-0.84%` | `1B / 1S` |
| `0:00 UTC` | `2340.25` | `2342.19` | `2340.25` | `2353.25` | `2334.75` | 172,183,772.38 USD | 75,695,646.18 USD | 96,488,126.21 USD | -20,792,480.03 USD | `-12.08%` | `0B / 3S` |
| `5:00 UTC` | `2335.75` | `2335.37` | `2335.75` | `2340.75` | `2330.75` | 125,556,310.13 USD | 63,692,130.92 USD | 61,864,179.21 USD | 1,827,951.70 USD | `+1.46%` | `1B / 1S` |
| `0:00 UTC` | `2337.75` | `2338.89` | `2337.75` | `2341.75` | `2337.25` | 40,174,235.35 USD | 20,651,439.51 USD | 19,522,795.84 USD | 1,128,643.67 USD | `+2.81%` | `0B / 0S` |

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
| `5m` | 845,510.00 USD | 5,770,000.00 USD | **`ACCUMULATION`** |
| `15m` | 1,360,000.00 USD | 35,590,000.00 USD | **`ACCUMULATION`** |
| `30m` | -7,770,000.00 USD | -68,660,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -6,380,000.00 USD | -107,910,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -6,030,000.00 USD | -283,230,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 21,280,000.00 USD | -4,790,000.00 USD | **`ACCUMULATION`** |
| `6h` | 14,580,000.00 USD | 37,700,000.00 USD | **`ACCUMULATION`** |
| `8h` | 13,210,000.00 USD | -30,020,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 23,510,000.00 USD | -89,420,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -18,180,000.00 USD | -356,420,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -14,190,000.00 USD | -984,920,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,010,000,000.00 USD | -8,180,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+845.51K` | 15m=`+1.36M` | 1h=`-6.38M` | 24h=`-18.18M`
* Futures Capital Netflows: 5m=`+5.77M` | 15m=`+35.59M` | 1h=`-107.91M` | 24h=`-356.42M`
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
  * `2026-10-29 23:30:59 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:59 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:59 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:59 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:54:59 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:44:59 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:40:59 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:41:59 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:41:59 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:41:59 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:41:59 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `2297.12` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2278.70` (Risk Distance: `18.42` pts)
  * +2.5R Take Profit: `2343.18`
  * Mathematical Lot Sizing: **`0.54 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2340.17` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2358.59` (Risk Distance: `18.42` pts)
  * +2.5R Take Profit: `2294.11`
  * Mathematical Lot Sizing: **`0.54 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2356.00`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
