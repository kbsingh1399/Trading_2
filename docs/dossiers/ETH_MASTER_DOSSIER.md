# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 01:36:03 IST` (`2026-10-29 20:06:03 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2318.70` | **Live Ask Quote**: `2322.00` | **Mid Price**: `2320.35`
- **Spread Points**: `330.00` | **Spread BPS**: `14.22 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2324.21` | VWAP Z-Score: `+0.44` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `10.35` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `48.03` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2378.33` | Lower -3.00σ Band: `2270.10`
  * Upper +2.51σ Band: `2369.49` | Lower -2.51σ Band: `2278.94`
  * Upper +2.01σ Band: `2360.47` | Lower -2.01σ Band: `2287.96`
  * Upper +2.00σ Band: `2360.29` | Lower -2.00σ Band: `2288.14`
  * Upper +1.28σ Band: `2347.30` | Lower -1.28σ Band: `2301.12`
  * Upper +1.00σ Band: `2342.25` | Lower -1.00σ Band: `2306.18`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2331.71` | EMA-20=`2334.66` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2332.14` (Slope: `+0.0000`) | EMA-100=`2331.66`
  * Institutional Anchors: EMA-144=`2331.43` | EMA-200=`2330.42` (Slope: `+0.0136`) | EMA-233=`2329.84`
- **Range Boundaries**: 24H High=`2387.80` | 24H Low=`2288.80` | Weekly High=`2387.80` | Weekly Low=`2288.80`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2336.73` (Distance: `-0.60%`)
  * Point of Control (POC) = `2318.94` (Distance: `+0.16%`)
  * Value Area Low (VAL) = `2297.70` (Distance: `+1.09%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2367.21` | POC=`2350.17` | VAL=`2335.02`
  * Prior Day Extremes: PDH=`2387.80` | PDL=`2316.80` | PDC=`2356.60`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2340.37` | Weekly POC=`2309.86` | Weekly VAL=`2299.24`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2367.70` | Low=`2288.80`
  * London Session (08:00-16:00 UTC): High=`2331.00` | Low=`2299.00`
  * New York Session (13:00-21:00 UTC): High=`2374.90` | Low=`2307.50`
  * Initial Balance (First Hour): IB High=`2331.00` | IB Low=`2299.30`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2311.07` - `2329.63`
  * Optimal Trade Entry (OTE 0.705): `2324.99`
  * Structural Invalidation Anchor (0.786): `2338.91`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2335.02` | `2338.58` | `2335.02` | `2336.82` | `8,526` | 19,928,241.44 USD | -3,419,149.63 USD | `-17.16%` | -409,398,130.09 USD | `-0.09` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `2336.82` | `2336.82` | `2334.28` | `2335.68` | `11,085` | 25,891,041.19 USD | -12,546,047.56 USD | `-48.46%` | -421,944,177.65 USD | `-0.75` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `2335.68` | `2335.92` | `2321.15` | `2323.72` | `24,998` | 58,174,050.78 USD | -22,041,046.21 USD | `-37.89%` | -443,985,223.86 USD | `-1.36` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `2330.06` | `2336.45` | `2330.06` | `2333.76` | `15,581` | 36,369,004.25 USD | 3,405,952.27 USD | `+9.36%` | -366,674,308.58 USD | `+0.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `2333.76` | `2338.58` | `2332.70` | `2335.68` | `23,252` | 54,317,401.94 USD | -15,763,811.25 USD | `-29.02%` | -382,438,119.83 USD | `-0.32` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `2335.68` | `2335.92` | `2321.15` | `2322.81` | `25,200` | 58,643,747.46 USD | -22,157,197.91 USD | `-37.78%` | -404,595,317.74 USD | `-0.49` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `2340.61` | `2342.29` | `2323.01` | `2330.23` | `146,197` | 340,744,443.34 USD | -42,605,787.87 USD | `-12.50%` | -327,552,864.00 USD | `-0.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2330.22` | `2338.58` | `2325.76` | `2335.68` | `63,571` | 148,285,696.23 USD | -15,505,202.15 USD | `-10.46%` | -343,058,066.15 USD | `+0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `2335.68` | `2335.92` | `2321.15` | `2323.08` | `25,241` | 58,739,112.73 USD | -22,154,580.34 USD | `-37.72%` | -365,212,646.49 USD | `-0.07` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -163,611,405.07 USD | `+1.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -365,767,522.01 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2321.15` | `2323.33` | `25,256` | 58,773,924.10 USD | -22,155,018.33 USD | `-37.70%` | -387,922,540.33 USD | `+0.41` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `2308.03` | `2334.83` | `2303.75` | `2309.10` | `525,175` | 1,216,920,375.04 USD | -34,916,746.14 USD | `-2.87%` | -218,489,329.59 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2309.10` | `2330.05` | `2308.88` | `2324.26` | `409,016` | 949,400,649.22 USD | -49,162,247.72 USD | `-5.18%` | -267,651,577.31 USD | `+0.60` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -163,611,405.07 USD | `+1.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -365,767,522.01 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2321.15` | `2323.33` | `25,256` | 58,773,924.10 USD | -22,155,018.33 USD | `-37.70%` | -387,922,540.33 USD | `+0.41` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`2320.35`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2335.50` | `846.6130` | 1,977,264.66 USD | 11,025,774.37 USD | `20 orders` | `-0.08%` | `-` |
| `BID` | `2335.60` | `221.3755` | 517,044.62 USD | 9,048,509.71 USD | `19 orders` | `-0.08%` | `-` |
| `BID` | `2335.70` | `108.2892` | 252,931.08 USD | 8,531,465.09 USD | `19 orders` | `-0.07%` | `-` |
| `BID` | `2335.80` | `172.5826` | 403,118.44 USD | 8,278,534.01 USD | `12 orders` | `-0.07%` | `-` |
| `BID` | `2335.90` | `646.7527` | 1,510,749.63 USD | 7,875,415.57 USD | `17 orders` | `-0.07%` | `-` |
| `BID` | `2336.00` | `351.7013` | 821,574.24 USD | 6,364,665.94 USD | `15 orders` | `-0.06%` | `-` |
| `BID` | `2336.10` | `147.4310` | 344,413.56 USD | 5,543,091.70 USD | `18 orders` | `-0.06%` | `-` |
| `BID` | `2336.20` | `138.8171` | 324,304.51 USD | 5,198,678.15 USD | `18 orders` | `-0.05%` | `-` |
| `BID` | `2336.30` | `184.2890` | 430,554.39 USD | 4,874,373.64 USD | `9 orders` | `-0.05%` | `-` |
| `BID` | `2336.40` | `152.4119` | 356,095.16 USD | 4,443,819.25 USD | `20 orders` | `-0.04%` | `-` |
| `BID` | `2336.50` | `383.8082` | 896,767.86 USD | 4,087,724.08 USD | `19 orders` | `-0.04%` | `-` |
| `BID` | `2336.60` | `238.8957` | 558,203.69 USD | 3,190,956.22 USD | `23 orders` | `-0.04%` | `-` |
| `BID` | `2336.70` | `110.4245` | 258,028.93 USD | 2,632,752.53 USD | `14 orders` | `-0.03%` | `-` |
| `BID` | `2336.80` | `228.0645` | 532,941.12 USD | 2,374,723.60 USD | `16 orders` | `-0.03%` | `-` |
| `BID` | `2336.90` | `151.4218` | 353,857.60 USD | 1,841,782.48 USD | `13 orders` | `-0.02%` | `-` |
| `BID` | `2337.00` | `199.5760` | 466,409.11 USD | 1,487,924.87 USD | `15 orders` | `-0.02%` | `-` |
| `BID` | `2337.10` | `122.5122` | 286,323.26 USD | 1,021,515.76 USD | `12 orders` | `-0.01%` | `-` |
| `BID` | `2337.20` | `88.5990` | 207,073.58 USD | 735,192.50 USD | `18 orders` | `-0.01%` | `-` |
| `BID` | `2337.30` | `46.9345` | 109,700.01 USD | 528,118.92 USD | `6 orders` | `-0.01%` | `-` |
| `BID` | `2337.40` | `179.0104` | 418,418.91 USD | 418,418.91 USD | `42 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2337.45` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,337.45` | `0.00%` | `-` |
| `ASK` | `2337.50` | `37.1762` | 86,899.37 USD | 86,899.37 USD | `11 orders` | `+0.00%` | `-` |
| `ASK` | `2337.60` | `88.9641` | 207,962.48 USD | 294,861.85 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `2337.70` | `115.4966` | 269,996.40 USD | 564,858.25 USD | `12 orders` | `+0.01%` | `-` |
| `ASK` | `2337.80` | `149.8572` | 350,336.16 USD | 915,194.41 USD | `23 orders` | `+0.01%` | `-` |
| `ASK` | `2337.90` | `99.8957` | 233,546.16 USD | 1,148,740.57 USD | `19 orders` | `+0.02%` | `-` |
| `ASK` | `2338.00` | `223.8168` | 523,283.68 USD | 1,672,024.25 USD | `16 orders` | `+0.02%` | `-` |
| `ASK` | `2338.10` | `233.4308` | 545,784.55 USD | 2,217,808.80 USD | `22 orders` | `+0.03%` | `-` |
| `ASK` | `2338.20` | `319.2200` | 746,400.20 USD | 2,964,209.00 USD | `22 orders` | `+0.03%` | `-` |
| `ASK` | `2338.30` | `255.5009` | 597,437.75 USD | 3,561,646.76 USD | `28 orders` | `+0.04%` | `-` |
| `ASK` | `2338.40` | `178.4224` | 417,222.94 USD | 3,978,869.70 USD | `26 orders` | `+0.04%` | `-` |
| `ASK` | `2338.50` | `456.9234` | 1,068,515.37 USD | 5,047,385.07 USD | `24 orders` | `+0.04%` | `-` |
| `ASK` | `2338.60` | `81.9305` | 191,602.67 USD | 5,238,987.74 USD | `13 orders` | `+0.05%` | `-` |
| `ASK` | `2338.70` | `167.8661` | 392,588.45 USD | 5,631,576.19 USD | `14 orders` | `+0.05%` | `-` |
| `ASK` | `2338.80` | `347.2875` | 812,236.01 USD | 6,443,812.19 USD | `19 orders` | `+0.06%` | `-` |
| `ASK` | `2338.90` | `411.4816` | 962,414.31 USD | 7,406,226.50 USD | `16 orders` | `+0.06%` | `-` |
| `ASK` | `2339.00` | `200.7395` | 469,529.69 USD | 7,875,756.20 USD | `14 orders` | `+0.07%` | `-` |
| `ASK` | `2339.10` | `167.9294` | 392,803.66 USD | 8,268,559.85 USD | `17 orders` | `+0.07%` | `-` |
| `ASK` | `2339.20` | `278.0474` | 650,408.48 USD | 8,918,968.33 USD | `14 orders` | `+0.07%` | `-` |
| `ASK` | `2339.30` | `345.1118` | 807,320.03 USD | 9,726,288.37 USD | `17 orders` | `+0.08%` | `-` |
| `ASK` | `2339.40` | `117.2493` | 274,293.01 USD | 10,000,581.38 USD | `18 orders` | `+0.08%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:33:46 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1918.80` | `8,092.45` | 15,527,789.21 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 01:33:46 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2040.72` | `7,964.66` | 16,253,666.81 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-30 01:33:46 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2115.25` | `7,500.00` | 15,864,343.04 USD | `AT_RISK_LIQ` | `0x524ed67d71` | `2026-10-30 01:33:46 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2171.19` | `48,499.51` | 105,301,442.50 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 01:33:46 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2180.25` | `44,734.81` | 97,532,977.35 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 01:33:46 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2250.00` | `6,500.00` | 14,625,000.00 USD | `TRIGGER_STOP` | `0x6eae4120a8` | `2026-10-30 01:33:46 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2250.00` | `1,232.10` | 2,772,234.90 USD | `TRIGGER_STOP` | `0x42020d2569` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2283.20` | `2,054.62` | 4,691,116.38 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2286.60` | `5,298.91` | 12,116,489.44 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2289.30` | `1,522.10` | 3,484,547.19 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 01:33:46 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2292.00` | `2,500.00` | 5,730,000.00 USD | `TRIGGER_STOP` | `0x934de82f50` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2297.30` | `348.27` | 800,091.47 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2297.30` | `334.09` | 767,507.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2297.60` | `593.51` | 1,363,650.87 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:33:46 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2298.00` | `1,310.00` | 3,010,380.00 USD | `TRIGGER_STOP` | `0x29de2668d0` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2300.40` | `1,031.12` | 2,371,999.95 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2301.60` | `2,733.12` | 6,290,554.29 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2302.00` | `395.43` | 910,280.78 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x76bf72092b` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2304.00` | `703.07` | 1,619,875.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2304.50` | `428.22` | 986,830.69 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2305.70` | `593.51` | 1,368,458.31 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2306.10` | `316.50` | 729,870.27 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2306.90` | `1,735.97` | 4,004,700.20 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 01:33:46 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2307.20` | `599,999.99` | 1,384,319,976.93 USD | `TRIGGER_STOP` | `0x069604ebfb` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2309.20` | `1,300.70` | 3,003,578.52 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2309.40` | `1,394.45` | 3,220,343.29 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2309.40` | `696.24` | 1,607,886.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2309.60` | `593.51` | 1,370,773.01 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:33:46 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2310.00` | `2,000.00` | 4,620,000.00 USD | `TRIGGER_STOP` | `0x524ed67d71` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2311.50` | `866.24` | 2,002,317.46 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2312.20` | `428.22` | 990,127.97 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2313.20` | `649.18` | 1,501,679.01 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2314.20` | `1,015.35` | 2,349,715.10 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x674982e841` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2314.50` | `395.68` | 915,805.99 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2314.70` | `432.50` | 1,001,113.07 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2315.90` | `324.22` | 750,868.74 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2315.90` | `321.16` | 743,783.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2316.00` | `908.97` | 2,105,170.81 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x0c4a3a7ac7` | `2026-10-30 01:33:46 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2319.00` | `2,500.00` | 5,797,500.00 USD | `TRIGGER_STOP` | `0x524ed67d71` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2321.20` | `323.49` | 750,894.74 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2321.30` | `321.16` | 745,517.99 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2322.20` | `431.15` | 1,001,219.32 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2323.00` | `395.64` | 919,076.37 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2323.80` | `646.27` | 1,501,813.84 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2325.10` | `428.22` | 995,652.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2326.00` | `860.85` | 2,002,325.94 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2327.60` | `593.51` | 1,381,456.20 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2328.20` | `507.91` | 1,182,520.95 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2328.30` | `1,289.98` | 3,003,450.19 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2329.30` | `1,394.45` | 3,248,092.85 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2330.70` | `1,718.26` | 4,004,759.30 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2331.60` | `593.51` | 1,383,830.25 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2332.70` | `428.22` | 998,906.46 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2333.50` | `749.28` | 1,748,440.68 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2333.90` | `390.04` | 910,322.52 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x76bf72092b` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2337.10` | `2,733.12` | 6,387,580.13 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2339.70` | `593.51` | 1,388,637.69 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2341.10` | `1,035.69` | 2,424,647.77 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2346.90` | `340.91` | 800,091.54 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2346.90` | `327.03` | 767,507.65 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2352.00` | `5,298.91` | 12,463,038.20 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 01:33:46 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2355.60` | `1,474.34` | 3,472,959.54 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 01:33:46 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2440.00` | `4,002.10` | 9,765,127.17 USD | `TRIGGER_STOP` | `0xfb941d2344` | `2026-10-30 01:33:46 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `3,058.48` | 7,688,708.10 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-30 01:33:46 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2585.94` | `6,224.05` | 16,095,035.80 USD | `AT_RISK_LIQ` | `0x08bf75d170` | `2026-10-30 01:33:46 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2658.69` | `9,700.00` | 25,789,335.09 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-30 01:33:46 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2709.05` | `8,500.00` | 23,026,892.90 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-30 01:33:46 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 248,740,758.16 USD | `106,417.71` | `2322.74` | `2336.80` | `3830.44` | -1,559,746.01 USD | `-0.63%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 152,436,645.49 USD | `65,205.17` | `2375.30` | `2336.80` | `4380.81` | 2,445,617.61 USD | `+1.60%` | `5X Cross` |
| `6` | `0x77dd...e0e9` | `LONG` | 113,348,209.26 USD | `48,499.51` | `2610.31` | `2336.80` | `2171.19` | -13,250,674.60 USD | `-11.69%` | `10X Cross` |
| `7` | `0x0392...d7d9` | `LONG` | 104,583,730.86 USD | `44,734.81` | `2518.71` | `2336.80` | `2180.25` | -8,090,575.72 USD | `-7.74%` | `9X Cross` |
| `15` | `0xde8d...9524` | `LONG` | 70,796,928.32 USD | `30,282.40` | `2134.45` | `2336.80` | `1787.14` | 6,160,597.74 USD | `+8.70%` | `20X Cross` |
| `18` | `0x7fda...17d1` | `SHORT` | 64,895,570.33 USD | `27,764.00` | `2437.59` | `2336.80` | `3636.14` | 2,781,875.58 USD | `+4.29%` | `25X Cross` |
| `25` | `0xdf95...7d72` | `SHORT` | 52,942,943.05 USD | `22,650.36` | `2402.54` | `2336.80` | `3971.31` | 1,475,476.03 USD | `+2.79%` | `25X Cross` |
| `28` | `0xeced...6210` | `SHORT` | 43,678,472.09 USD | `18,687.58` | `2522.09` | `2336.80` | `3349.53` | 3,453,440.37 USD | `+7.91%` | `20X Cross` |
| `34` | `0xb695...a92d` | `SHORT` | 39,040,366.23 USD | `16,704.62` | `2557.74` | `2336.80` | `4033.00` | 3,685,798.82 USD | `+9.44%` | `20X Cross` |
| `35` | `0x6046...b21d` | `LONG` | 37,236,952.68 USD | `15,927.59` | `2410.19` | `2336.80` | `1547.85` | -1,151,666.96 USD | `-3.09%` | `6X Cross` |
| `38` | `0x45d2...4029` | `SHORT` | 32,602,545.00 USD | `13,950.00` | `2443.60` | `2336.80` | `5007.27` | 1,485,737.46 USD | `+4.56%` | `20X Cross` |
| `43` | `0x0622...8088` | `LONG` | 28,794,565.47 USD | `12,319.06` | `2342.25` | `2336.80` | `1515.60` | -59,848.38 USD | `-0.21%` | `5X Cross` |
| `44` | `0x2371...0883` | `LONG` | 28,053,600.00 USD | `12,000.00` | `2421.77` | `2336.80` | `1280.11` | -1,007,694.85 USD | `-3.59%` | `20X Cross` |
| `45` | `0xbd1c...ff0e` | `LONG` | 28,045,200.00 USD | `12,000.00` | `2419.91` | `2336.80` | `1521.02` | -993,832.39 USD | `-3.54%` | `20X Cross` |
| `50` | `0x6c93...59a4` | `LONG` | 25,712,500.00 USD | `11,000.00` | `2441.15` | `2336.80` | `1603.05` | -1,140,172.73 USD | `-4.43%` | `20X Cross` |
| `51` | `0xa9de...e049` | `LONG` | 25,711,400.00 USD | `11,000.00` | `2481.81` | `2336.80` | `1644.76` | -1,588,579.46 USD | `-6.18%` | `20X Cross` |
| `52` | `0x0c5d...36b3` | `LONG` | 25,711,400.00 USD | `11,000.00` | `2482.20` | `2336.80` | `1645.09` | -1,592,853.24 USD | `-6.20%` | `20X Cross` |
| `53` | `0x09dc...c094` | `LONG` | 25,710,300.00 USD | `11,000.00` | `2465.31` | `2336.80` | `1638.08` | -1,408,123.04 USD | `-5.48%` | `20X Cross` |
| `55` | `0xa61c...66b9` | `LONG` | 25,452,877.60 USD | `10,888.00` | `2398.32` | `2336.80` | `1404.44` | -660,079.79 USD | `-2.59%` | `10X Cross` |
| `59` | `0x4487...c92d` | `SHORT` | 24,617,722.26 USD | `10,533.45` | `2373.98` | `2336.80` | `2864.10` | 388,570.76 USD | `+1.58%` | `10X Cross` |
| `65` | `0xa2ce...3126` | `LONG` | 23,410,439.03 USD | `10,016.88` | `2162.83` | `2336.80` | `1438.17` | 1,745,636.98 USD | `+7.46%` | `10X Cross` |
| `67` | `0x15a4...dfdb` | `LONG` | 23,374,000.00 USD | `10,000.00` | `1761.94` | `2336.80` | `12.57` | 5,754,518.97 USD | `+24.62%` | `20X Cross` |
| `68` | `0xec7f...df39` | `LONG` | 23,373,000.00 USD | `10,000.00` | `2719.35` | `2336.80` | `1721.61` | -3,820,548.52 USD | `-16.35%` | `20X Cross` |
| `69` | `0x6646...6de5` | `LONG` | 23,371,000.00 USD | `10,000.00` | `1765.80` | `2336.80` | `1732.81` | 5,712,942.55 USD | `+24.44%` | `25X Cross` |
| `75` | `0xaeaa...2416` | `SHORT` | 22,676,660.00 USD | `9,700.00` | `2311.92` | `2336.80` | `2658.69` | -250,977.60 USD | `-1.11%` | `25X Cross` |
| `81` | `0xca49...53c8` | `SHORT` | 21,652,431.74 USD | `9,264.26` | `2549.47` | `2336.80` | `3731.71` | 1,966,592.99 USD | `+9.08%` | `25X Cross` |
| `83` | `0xba5d...a352` | `SHORT` | 21,163,105.00 USD | `9,054.12` | `2493.89` | `2336.80` | `2924.84` | 1,416,902.26 USD | `+6.70%` | `20X Cross` |
| `84` | `0xea00...a918` | `LONG` | 21,049,685.35 USD | `9,003.83` | `2003.01` | `2336.80` | `1243.04` | 3,014,906.49 USD | `+14.32%` | `5X Cross` |
| `93` | `0xb37f...66ca` | `SHORT` | 19,865,350.00 USD | `8,500.00` | `2308.30` | `2336.80` | `2709.05` | -244,795.81 USD | `-1.23%` | `25X Cross` |
| `102` | `0x9eec...daab` | `LONG` | 18,912,869.80 USD | `8,092.45` | `1658.44` | `2336.80` | `1918.80` | 5,492,005.27 USD | `+29.04%` | `15X Cross` |
| `109` | `0x218a...7da2` | `SHORT` | 18,695,218.59 USD | `7,997.78` | `2208.16` | `2336.80` | `2877.26` | -1,034,823.37 USD | `-5.54%` | `10X Cross` |
| `110` | `0x5f91...65aa` | `LONG` | 18,620,489.38 USD | `7,964.66` | `1626.99` | `2336.80` | `2040.72` | 5,662,046.32 USD | `+30.41%` | `16X Cross` |
| `112` | `0xecb6...2b00` | `SHORT` | 18,026,777.70 USD | `7,712.32` | `2327.65` | `2336.80` | `5911.82` | -75,142.71 USD | `-0.42%` | `15X Cross` |
| `114` | `0xcf53...ee11` | `SHORT` | 17,770,438.77 USD | `7,603.63` | `1862.69` | `2336.80` | `3993.12` | -3,607,174.82 USD | `-20.30%` | `7X Cross` |
| `115` | `0x524e...0de0` | `LONG` | 17,533,500.00 USD | `7,500.00` | `2320.35` | `2336.80` | `2115.25` | 130,813.78 USD | `+0.75%` | `10X Cross` |
| `119` | `0x939f...04d2` | `LONG` | 16,886,023.84 USD | `7,223.81` | `2500.18` | `2336.80` | `1770.26` | -1,174,866.33 USD | `-6.96%` | `25X Cross` |
| `122` | `0xec0b...b078` | `LONG` | 16,382,131.49 USD | `7,007.80` | `2065.97` | `2336.80` | `1002.89` | 1,904,201.90 USD | `+11.62%` | `25X Cross` |
| `123` | `0x1ee7...edf5` | `LONG` | 16,365,020.00 USD | `7,000.00` | `2330.22` | `2336.80` | `2153.94` | 53,457.80 USD | `+0.33%` | `25X Cross` |
| `130` | `0x418a...8888` | `SHORT` | 15,716,899.92 USD | `6,724.38` | `2494.55` | `2336.80` | `2957.99` | 1,057,423.26 USD | `+6.73%` | `25X Cross` |
| `131` | `0x4ff9...38d3` | `LONG` | 15,342,924.30 USD | `6,564.10` | `2447.40` | `2336.80` | `1670.70` | -722,098.44 USD | `-4.71%` | `3X Isolated` |
| `133` | `0xf78c...c581` | `LONG` | 15,196,607.84 USD | `6,500.22` | `2521.53` | `2336.80` | `1914.18` | -1,193,933.11 USD | `-7.86%` | `20X Cross` |
| `140` | `0x799f...5f4c` | `LONG` | 14,751,736.46 USD | `6,310.90` | `2390.33` | `2336.80` | `1713.26` | -333,428.15 USD | `-2.26%` | `20X Cross` |
| `143` | `0x08bf...7872` | `SHORT` | 14,547,465.99 USD | `6,224.05` | `2258.00` | `2336.80` | `2585.94` | -493,549.88 USD | `-3.39%` | `20X Cross` |
| `150` | `0xd9e7...4aff` | `LONG` | 14,025,300.00 USD | `6,000.00` | `2480.18` | `2336.80` | `1408.47` | -855,824.33 USD | `-6.10%` | `20X Cross` |
| `157` | `0x0c4a...1b19` | `LONG` | 13,337,536.70 USD | `5,706.39` | `2382.15` | `2336.80` | `2185.23` | -255,934.47 USD | `-1.92%` | `25X Isolated` |
| `173` | `0x645b...87b8` | `SHORT` | 11,858,793.99 USD | `5,073.50` | `2421.68` | `2336.80` | `6231.86` | 427,608.31 USD | `+3.61%` | `10X Cross` |
| `180` | `0x45ab...6cbc` | `LONG` | 11,504,668.32 USD | `4,920.96` | `2727.66` | `2336.80` | `1366.31` | -1,918,075.48 USD | `-16.67%` | `7X Cross` |
| `183` | `0xfb18...eb17` | `SHORT` | 11,387,881.73 USD | `4,872.45` | `2315.54` | `2336.80` | `2708.60` | -105,508.69 USD | `-0.93%` | `25X Cross` |
| `186` | `0x64b7...9da9` | `LONG` | 11,353,833.00 USD | `4,856.84` | `2604.61` | `2336.80` | `1445.72` | -1,296,381.42 USD | `-11.42%` | `25X Cross` |
| `193` | `0x5559...d43b` | `SHORT` | 11,116,499.80 USD | `4,755.93` | `2262.69` | `2336.80` | `2861.53` | -355,293.92 USD | `-3.20%` | `25X Cross` |
| `208` | `0xe091...6705` | `SHORT` | 10,518,300.47 USD | `4,500.00` | `2467.33` | `2336.80` | `2572.99` | 584,708.04 USD | `+5.56%` | `20X Cross` |
| `214` | `0xfe7c...b7ae` | `SHORT` | 10,292,621.76 USD | `4,402.58` | `2440.17` | `2336.80` | `4229.22` | 450,466.11 USD | `+4.38%` | `25X Cross` |
| `228` | `0xc179...e0c8` | `LONG` | 10,074,330.62 USD | `4,309.16` | `2342.89` | `2336.80` | `856.98` | -21,548.18 USD | `-0.21%` | `10X Cross` |
| `234` | `0x12d2...f97f` | `LONG` | 9,968,749.25 USD | `4,264.34` | `2623.90` | `2336.80` | `1829.74` | -1,220,485.16 USD | `-12.24%` | `20X Cross` |
| `239` | `0x28bb...fca6` | `SHORT` | 9,840,815.12 USD | `4,209.61` | `1896.10` | `2336.80` | `3047.38` | -1,858,932.55 USD | `-18.89%` | `20X Cross` |
| `243` | `0x6ea4...0ea7` | `SHORT` | 9,779,291.95 USD | `4,184.01` | `2602.13` | `2336.80` | `3426.01` | 1,108,054.72 USD | `+11.33%` | `20X Cross` |
| `252` | `0x5e9e...35ee` | `SHORT` | 9,366,459.18 USD | `4,007.56` | `1796.39` | `2336.80` | `2586.50` | -2,167,309.09 USD | `-23.14%` | `20X Cross` |
| `253` | `0xfb94...0ddf` | `SHORT` | 9,356,472.61 USD | `4,002.10` | `2382.44` | `2336.80` | `5105.40` | 178,311.54 USD | `+1.91%` | `20X Cross` |
| `254` | `0x95fe...f8fa` | `LONG` | 9,351,200.00 USD | `4,000.00` | `2341.35` | `2336.80` | `2259.00` | -14,216.51 USD | `-0.15%` | `20X Isolated` |
| `255` | `0x3dc9...54b0` | `SHORT` | 9,350,715.73 USD | `3,999.69` | `2480.32` | `2336.80` | `5974.71` | 569,820.82 USD | `+6.09%` | `20X Cross` |
| `256` | `0x8cc9...2b6a` | `SHORT` | 9,349,600.00 USD | `4,000.00` | `1791.18` | `2336.80` | `3869.91` | -2,184,853.33 USD | `-23.37%` | `25X Cross` |
| `257` | `0x77ee...2902` | `SHORT` | 9,307,664.08 USD | `3,982.23` | `2476.53` | `2336.80` | `4267.23` | 554,457.51 USD | `+5.96%` | `25X Cross` |
| `268` | `0xf02d...5eb3` | `LONG` | 9,013,366.11 USD | `3,855.99` | `2513.67` | `2336.80` | `333.32` | -679,346.21 USD | `-7.54%` | `20X Cross` |
| `270` | `0x4b67...f4e7` | `LONG` | 8,932,708.07 USD | `3,820.84` | `2591.51` | `2336.80` | `1591.87` | -969,065.47 USD | `-10.85%` | `20X Cross` |
| `292` | `0x8ae4...3d60` | `LONG` | 8,316,576.89 USD | `3,558.20` | `2482.21` | `2336.80` | `355.43` | -515,621.15 USD | `-6.20%` | `10X Cross` |
| `293` | `0x382b...3e39` | `SHORT` | 8,313,924.24 USD | `3,556.91` | `2299.51` | `2336.80` | `3753.97` | -134,766.63 USD | `-1.62%` | `25X Cross` |
| `319` | `0x9c06...0560` | `SHORT` | 7,721,787.89 USD | `3,303.58` | `2270.55` | `2336.80` | `3313.26` | -220,823.95 USD | `-2.86%` | `25X Cross` |
| `328` | `0x984e...14c2` | `SHORT` | 7,273,025.75 USD | `3,111.99` | `2357.50` | `2336.80` | `2434.97` | 63,497.01 USD | `+0.87%` | `20X Cross` |
| `333` | `0x9c2a...f6a8` | `SHORT` | 7,150,293.61 USD | `3,058.48` | `2543.83` | `2336.80` | `2592.40` | 629,967.01 USD | `+8.81%` | `20X Cross` |
| `338` | `0x39b4...5c34` | `SHORT` | 7,015,710.96 USD | `3,000.91` | `2329.97` | `2336.80` | `2401.92` | -23,667.21 USD | `-0.34%` | `25X Cross` |
| `339` | `0x007d...67a0` | `LONG` | 7,011,600.00 USD | `3,000.00` | `2400.00` | `2336.80` | `1488.87` | -188,400.00 USD | `-2.69%` | `25X Cross` |
| `340` | `0x4a20...3c26` | `LONG` | 7,011,300.00 USD | `3,000.00` | `2428.72` | `2336.80` | `273.70` | -274,860.28 USD | `-3.92%` | `20X Cross` |
| `378` | `0xf517...c032` | `SHORT` | 6,400,786.94 USD | `2,738.07` | `2053.90` | `2336.80` | `5529.27` | -777,045.03 USD | `-12.14%` | `25X Cross` |
| `393` | `0xbb34...1696` | `LONG` | 6,078,514.00 USD | `2,600.00` | `2318.80` | `2336.80` | `1978.45` | 49,613.15 USD | `+0.82%` | `25X Cross` |
| `394` | `0xc619...10f5` | `LONG` | 6,077,240.00 USD | `2,600.00` | `2318.40` | `2336.80` | `1861.84` | 49,391.09 USD | `+0.81%` | `25X Cross` |
| `397` | `0x8328...f54a` | `SHORT` | 6,023,459.26 USD | `2,576.45` | `2292.01` | `2336.80` | `3280.24` | -118,187.97 USD | `-1.96%` | `25X Cross` |
| `399` | `0xed48...7c9b` | `SHORT` | 5,962,247.09 USD | `2,551.13` | `2460.02` | `2336.80` | `3232.97` | 313,599.32 USD | `+5.26%` | `20X Cross` |
| `403` | `0x934d...92c9` | `LONG` | 5,843,750.00 USD | `2,500.00` | `2343.98` | `2336.80` | `2156.36` | -16,214.51 USD | `-0.28%` | `25X Cross` |
| `421` | `0xfbe2...c8ea` | `SHORT` | 5,618,567.89 USD | `2,404.08` | `2041.57` | `2336.80` | `2687.83` | -710,475.16 USD | `-12.65%` | `20X Cross` |
| `427` | `0x1c98...7fc7` | `LONG` | 5,511,363.92 USD | `2,358.00` | `2467.15` | `2336.80` | `1897.22` | -306,207.57 USD | `-5.56%` | `10X Cross` |
| `440` | `0x6859...7e1e` | `SHORT` | 5,199,953.41 USD | `2,224.58` | `2200.39` | `2336.80` | `3722.53` | -305,000.69 USD | `-5.87%` | `25X Cross` |
| `455` | `0xd507...c948` | `SHORT` | 5,077,049.77 USD | `2,172.00` | `2387.49` | `2336.80` | `2707.43` | 108,591.26 USD | `+2.14%` | `5X Isolated` |
| `458` | `0xb829...3a81` | `LONG` | 5,034,336.18 USD | `2,153.91` | `2537.61` | `2336.80` | `778.45` | -431,460.55 USD | `-8.57%` | `20X Cross` |
| `493` | `0x3440...32c5` | `SHORT` | 4,676,321.16 USD | `2,000.57` | `2198.21` | `2336.80` | `3538.25` | -278,658.02 USD | `-5.96%` | `25X Cross` |
| `494` | `0xf929...d1f9` | `SHORT` | 4,674,800.00 USD | `2,000.00` | `2423.37` | `2336.80` | `2548.82` | 171,940.34 USD | `+3.68%` | `25X Cross` |
| `504` | `0x0514...bdfe` | `SHORT` | 4,557,345.00 USD | `1,950.00` | `1988.74` | `2336.80` | `2942.46` | -679,285.37 USD | `-14.91%` | `25X Cross` |
| `509` | `0x8376...9a1e` | `SHORT` | 4,466,529.49 USD | `1,910.50` | `2477.72` | `2336.80` | `3156.76` | 267,158.68 USD | `+5.98%` | `20X Cross` |
| `533` | `0x7a6d...f79c` | `SHORT` | 4,266,105.80 USD | `1,825.07` | `2433.80` | `2336.80` | `2783.77` | 175,763.08 USD | `+4.12%` | `25X Cross` |
| `538` | `0x541e...071d` | `SHORT` | 4,218,465.50 USD | `1,805.00` | `2648.19` | `2336.80` | `3023.21` | 561,519.34 USD | `+13.31%` | `25X Cross` |
| `542` | `0x7265...91a5` | `LONG` | 4,211,689.54 USD | `1,801.87` | `2533.96` | `2336.80` | `1988.15` | -354,176.92 USD | `-8.41%` | `20X Cross` |
| `543` | `0x739c...cfb2` | `SHORT` | 4,208,148.00 USD | `1,800.00` | `2427.60` | `2336.80` | `2654.74` | 161,548.38 USD | `+3.84%` | `25X Cross` |
| `554` | `0xa445...329d` | `LONG` | 4,152,440.79 USD | `1,776.75` | `2398.85` | `2336.80` | `1815.06` | -109,728.56 USD | `-2.64%` | `25X Cross` |
| `559` | `0x91a9...3f70` | `SHORT` | 4,132,014.74 USD | `1,767.48` | `2156.23` | `2336.80` | `3640.46` | -320,910.66 USD | `-7.77%` | `4X Cross` |
| `562` | `0x3453...b323` | `SHORT` | 4,091,542.79 USD | `1,750.12` | `2328.82` | `2336.80` | `2393.58` | -15,810.66 USD | `-0.39%` | `25X Cross` |
| `580` | `0xd4c1...3d1d` | `SHORT` | 4,001,023.33 USD | `1,711.38` | `2336.05` | `2336.80` | `5175.24` | -3,136.21 USD | `-0.08%` | `12X Cross` |
| `589` | `0xfeec...4e9c` | `SHORT` | 3,954,603.07 USD | `1,691.81` | `2566.49` | `2336.80` | `2651.27` | 387,421.44 USD | `+9.80%` | `10X Cross` |
| `591` | `0x936c...bb0f` | `SHORT` | 3,947,134.66 USD | `1,688.69` | `2434.60` | `2336.80` | `8543.75` | 164,152.45 USD | `+4.16%` | `20X Cross` |
| `610` | `0xeee0...0b53` | `LONG` | 3,827,415.59 USD | `1,637.12` | `2468.64` | `2336.80` | `134.76` | -214,060.47 USD | `-5.59%` | `7X Cross` |
| `614` | `0x27b8...12fc` | `LONG` | 3,805,405.11 USD | `1,628.12` | `2468.73` | `2336.80` | `441.23` | -213,989.52 USD | `-5.62%` | `10X Cross` |
| `615` | `0x982b...4606` | `LONG` | 3,803,271.09 USD | `1,626.82` | `2575.24` | `2336.80` | `1548.43` | -386,181.98 USD | `-10.15%` | `5X Isolated` |
| `624` | `0x73d7...8be1` | `LONG` | 3,742,945.17 USD | `1,601.47` | `2410.40` | `2336.80` | `2048.35` | -117,233.75 USD | `-3.13%` | `25X Cross` |
| `647` | `0xe170...9300` | `SHORT` | 3,584,169.16 USD | `1,533.40` | `2076.39` | `2336.80` | `3225.87` | -400,219.66 USD | `-11.17%` | `25X Cross` |
| `657` | `0x2e2b...2fab` | `LONG` | 3,523,945.95 USD | `1,507.38` | `2245.53` | `2336.80` | `1121.76` | 139,072.85 USD | `+3.95%` | `25X Cross` |
| `662` | `0x251f...6e5d` | `LONG` | 3,506,550.00 USD | `1,500.00` | `2346.68` | `2336.80` | `1625.80` | -13,480.49 USD | `-0.38%` | `20X Cross` |
| `674` | `0xfc27...9d9d` | `SHORT` | 3,431,325.08 USD | `1,468.20` | `2402.13` | `2336.80` | `12152.83` | 95,487.06 USD | `+2.78%` | `25X Cross` |
| `680` | `0xad54...6203` | `LONG` | 3,408,350.63 USD | `1,458.18` | `2627.45` | `2336.80` | `2145.31` | -422,956.05 USD | `-12.41%` | `10X Isolated` |
| `682` | `0x023a...2355` | `LONG` | 3,399,817.95 USD | `1,454.53` | `2339.96` | `2336.80` | `0.000000` | -3,732.04 USD | `-0.11%` | `25X Cross` |
| `687` | `0xef70...a84c` | `SHORT` | 3,372,701.25 USD | `1,442.74` | `2424.73` | `2336.80` | `3447.64` | 125,569.58 USD | `+3.72%` | `25X Cross` |
| `693` | `0x4b5f...0dd8` | `LONG` | 3,347,628.61 USD | `1,431.96` | `2339.45` | `2336.80` | `2148.71` | -2,364.34 USD | `-0.07%` | `10X Cross` |
| `695` | `0xbadb...9ee6` | `LONG` | 3,338,324.00 USD | `1,428.16` | `1936.00` | `2336.80` | `1045.61` | 573,402.35 USD | `+17.18%` | `20X Cross` |
| `700` | `0x3bca...66f3` | `SHORT` | 3,315,590.69 USD | `1,418.20` | `2337.45` | `2336.80` | `7717.66` | -612.13 USD | `-0.02%` | `25X Cross` |
| `762` | `0x880a...311c` | `SHORT` | 3,085,757.45 USD | `1,320.22` | `2425.76` | `2336.80` | `8247.16` | 116,791.70 USD | `+3.78%` | `9X Cross` |
| `771` | `0x29de...3e93` | `LONG` | 3,062,518.00 USD | `1,310.00` | `2352.60` | `2336.80` | `1922.24` | -19,390.82 USD | `-0.63%` | `5X Isolated` |
| `805` | `0xc435...c905` | `SHORT` | 2,917,262.40 USD | `1,248.00` | `2704.38` | `2336.80` | `4878.62` | 457,807.95 USD | `+15.69%` | `20X Cross` |
| `815` | `0x4202...aaf5` | `SHORT` | 2,879,551.19 USD | `1,232.10` | `2321.73` | `2336.80` | `2733.56` | -18,926.89 USD | `-0.66%` | `5X Isolated` |
| `820` | `0x7178...0854` | `LONG` | 2,848,429.27 USD | `1,218.63` | `2461.81` | `2336.80` | `1060.39` | -151,617.13 USD | `-5.32%` | `10X Cross` |
| `860` | `0x07fd...689d` | `LONG` | 2,655,506.08 USD | `1,135.90` | `2423.84` | `2336.80` | `0.000000` | -97,737.11 USD | `-3.68%` | `25X Cross` |
| `901` | `0x2f80...f203` | `SHORT` | 2,545,182.03 USD | `1,088.94` | `1984.00` | `2336.80` | `3074.54` | -384,714.84 USD | `-15.12%` | `20X Cross` |
| `909` | `0x6f11...0389` | `SHORT` | 2,522,486.20 USD | `1,079.00` | `2333.39` | `2336.80` | `3199.70` | -4,757.29 USD | `-0.19%` | `25X Cross` |
| `912` | `0x2b61...2f6c` | `SHORT` | 2,516,330.64 USD | `1,076.60` | `2681.75` | `2336.80` | `6397.88` | 370,842.10 USD | `+14.74%` | `10X Cross` |
| `953` | `0x1b2a...f7a6` | `LONG` | 2,397,197.59 USD | `1,025.37` | `2737.51` | `2336.80` | `953.36` | -409,762.34 USD | `-17.09%` | `10X Cross` |
| `954` | `0xb15b...dbae` | `SHORT` | 2,396,169.72 USD | `1,025.14` | `2338.37` | `2336.80` | `2381.08` | 1,004.00 USD | `+0.04%` | `25X Cross` |
| `959` | `0x6749...ce07` | `SHORT` | 2,373,169.61 USD | `1,015.35` | `2318.56` | `2336.80` | `5904.65` | -19,026.25 USD | `-0.80%` | `20X Cross` |
| `966` | `0x001a...fef6` | `SHORT` | 2,354,420.72 USD | `1,007.33` | `2022.19` | `2336.80` | `3038.90` | -317,412.77 USD | `-13.48%` | `10X Cross` |
| `967` | `0x02aa...1806` | `SHORT` | 2,354,297.90 USD | `1,007.10` | `2654.68` | `2336.80` | `3613.69` | 319,234.20 USD | `+13.56%` | `20X Cross` |
| `971` | `0xdb3a...cf3b` | `LONG` | 2,345,316.26 USD | `1,003.22` | `2705.01` | `2336.80` | `0.000000` | -368,390.63 USD | `-15.71%` | `4X Cross` |
| `980` | `0x4044...794c` | `LONG` | 2,337,890.00 USD | `1,000.00` | `2332.68` | `2336.80` | `0.000000` | 5,200.16 USD | `+0.22%` | `25X Cross` |
| `981` | `0xdf60...d3c7` | `LONG` | 2,337,800.00 USD | `1,000.00` | `2736.24` | `2336.80` | `2246.09` | -398,442.88 USD | `-17.04%` | `10X Isolated` |
| `982` | `0xfe82...ce65` | `SHORT` | 2,337,800.00 USD | `1,000.00` | `2300.50` | `2336.80` | `2718.44` | -37,292.07 USD | `-1.60%` | `25X Cross` |
| `983` | `0x2828...93a0` | `LONG` | 2,337,400.00 USD | `1,000.00` | `2393.30` | `2336.80` | `2272.63` | -55,909.16 USD | `-2.39%` | `25X Cross` |
| `984` | `0x5272...fcd9` | `SHORT` | 2,337,300.00 USD | `1,000.00` | `2241.82` | `2336.80` | `2880.77` | -95,475.51 USD | `-4.08%` | `5X Cross` |
| `985` | `0x5986...89d9` | `LONG` | 2,337,300.00 USD | `1,000.00` | `2346.34` | `2336.80` | `1263.54` | -9,049.54 USD | `-0.39%` | `25X Cross` |
| `1013` | `0xb002...ed8a` | `SHORT` | 2,250,883.09 USD | `962.78` | `2299.66` | `2336.80` | `4189.83` | -36,805.18 USD | `-1.64%` | `25X Cross` |
| `1026` | `0x2e30...4cb5` | `SHORT` | 2,210,392.88 USD | `945.74` | `2340.09` | `2336.80` | `7239.92` | 2,738.81 USD | `+0.12%` | `2X Cross` |
| `1033` | `0xc8fe...afa4` | `LONG` | 2,188,956.36 USD | `936.37` | `2331.34` | `2336.80` | `2145.82` | 5,952.12 USD | `+0.27%` | `10X Isolated` |
| `1050` | `0x9606...4e5d` | `SHORT` | 2,134,038.49 USD | `913.00` | `2478.70` | `2336.80` | `3985.11` | 129,015.12 USD | `+6.05%` | `20X Cross` |
| `1057` | `0xaeea...bfa7` | `LONG` | 2,124,194.48 USD | `908.75` | `2339.31` | `2336.80` | `2286.73` | -1,647.63 USD | `-0.08%` | `23X Isolated` |
| `1084` | `0x60f7...d1ee` | `LONG` | 2,080,019.00 USD | `890.00` | `2343.49` | `2336.80` | `2263.94` | -5,690.96 USD | `-0.27%` | `25X Cross` |
| `1174` | `0xcd27...52a8` | `LONG` | 1,957,225.56 USD | `837.21` | `2553.56` | `2336.80` | `1404.24` | -180,639.21 USD | `-9.23%` | `2X Cross` |
| `1186` | `0xbef3...0d3e` | `LONG` | 1,942,770.22 USD | `830.99` | `2332.88` | `2336.80` | `2110.70` | 4,158.98 USD | `+0.21%` | `20X Cross` |
| `1189` | `0x6a41...a3b9` | `LONG` | 1,930,913.85 USD | `826.06` | `2332.61` | `2336.80` | `2112.89` | 4,038.99 USD | `+0.21%` | `20X Cross` |
| `1218` | `0x3fc5...c0c1` | `SHORT` | 1,880,243.08 USD | `804.26` | `2702.11` | `2336.80` | `4937.55` | 292,958.45 USD | `+15.58%` | `25X Cross` |
| `1220` | `0xf83f...625f` | `SHORT` | 1,876,806.52 USD | `803.05` | `2601.00` | `2336.80` | `6033.61` | 211,929.93 USD | `+11.29%` | `20X Cross` |
| `1232` | `0x04a9...95aa` | `LONG` | 1,870,240.00 USD | `800.00` | `2595.13` | `2336.80` | `1862.56` | -205,866.74 USD | `-11.01%` | `5X Cross` |
| `1233` | `0x7737...bf66` | `SHORT` | 1,869,433.59 USD | `799.79` | `2494.83` | `2336.80` | `24785.24` | 125,912.44 USD | `+6.74%` | `15X Cross` |
| `1260` | `0x2577...4897` | `LONG` | 1,826,690.40 USD | `781.54` | `2355.83` | `2336.80` | `0.000000` | -14,482.99 USD | `-0.79%` | `15X Cross` |
| `1272` | `0x458d...ab3b` | `LONG` | 1,811,009.85 USD | `774.75` | `2740.41` | `2336.80` | `1887.99` | -312,119.33 USD | `-17.23%` | `3X Isolated` |
| `1304` | `0x7743...e4fe` | `SHORT` | 1,754,650.28 USD | `750.56` | `2326.87` | `2336.80` | `5895.14` | -8,196.15 USD | `-0.47%` | `25X Cross` |
| `1305` | `0x5f10...d49d` | `SHORT` | 1,752,975.00 USD | `750.00` | `2350.92` | `2336.80` | `2842.53` | 10,221.61 USD | `+0.58%` | `25X Cross` |
| `1339` | `0x51a0...3543` | `SHORT` | 1,693,843.17 USD | `724.55` | `2627.71` | `2336.80` | `7715.54` | 210,053.58 USD | `+12.40%` | `20X Cross` |
| `1346` | `0x4b1c...bc38` | `SHORT` | 1,688,284.35 USD | `722.14` | `2529.31` | `2336.80` | `4512.18` | 138,237.61 USD | `+8.19%` | `10X Cross` |
| `1352` | `0xa189...94d7` | `SHORT` | 1,682,662.92 USD | `719.98` | `2691.84` | `2336.80` | `3051.94` | 255,409.74 USD | `+15.18%` | `25X Cross` |
| `1362` | `0x3ee5...4fab` | `SHORT` | 1,671,559.60 USD | `715.17` | `2759.35` | `2336.80` | `3415.36` | 301,840.37 USD | `+18.06%` | `20X Cross` |
| `1374` | `0x2f93...4404` | `LONG` | 1,653,431.64 USD | `707.47` | `1700.45` | `2336.80` | `1369.63` | 450,405.27 USD | `+27.24%` | `4X Isolated` |
| `1384` | `0x5605...fe0f` | `SHORT` | 1,641,120.24 USD | `702.14` | `2566.90` | `2336.80` | `3060.31` | 161,212.41 USD | `+9.82%` | `20X Cross` |
| `1391` | `0xaa53...9cb7` | `LONG` | 1,636,110.00 USD | `700.00` | `2394.46` | `2336.80` | `1920.45` | -40,012.07 USD | `-2.45%` | `20X Cross` |
| `1431` | `0xdbd1...29dd` | `SHORT` | 1,590,869.81 USD | `680.70` | `3030.57` | `2336.80` | `4100.89` | 472,051.31 USD | `+29.67%` | `6X Cross` |
| `1436` | `0x71e5...be04` | `LONG` | 1,583,910.61 USD | `677.67` | `2727.27` | `2336.80` | `1471.77` | -264,274.99 USD | `-16.68%` | `20X Cross` |
| `1441` | `0x0b23...f37b` | `LONG` | 1,577,677.50 USD | `675.00` | `2238.15` | `2336.80` | `581.46` | 66,920.86 USD | `+4.24%` | `5X Cross` |
| `1467` | `0x0cac...6170` | `SHORT` | 1,548,395.00 USD | `662.50` | `2146.55` | `2336.80` | `2835.40` | -126,300.01 USD | `-8.16%` | `20X Cross` |
| `1473` | `0x0082...1ae3` | `LONG` | 1,542,987.60 USD | `660.00` | `2448.58` | `2336.80` | `2244.97` | -73,081.04 USD | `-4.74%` | `25X Cross` |
| `1508` | `0xffb2...5ed6` | `SHORT` | 1,497,728.32 USD | `640.77` | `2672.96` | `2336.80` | `2562.08` | 215,020.03 USD | `+14.36%` | `20X Cross` |
| `1531` | `0xfce0...f4c0` | `SHORT` | 1,457,889.50 USD | `623.60` | `3129.61` | `2336.80` | `2788.44` | 493,737.09 USD | `+33.87%` | `20X Cross` |
| `1558` | `0x7663...cb5a` | `SHORT` | 1,433,960.55 USD | `613.54` | `2342.35` | `2336.80` | `3635.99` | 3,159.94 USD | `+0.22%` | `3X Cross` |
| `1590` | `0xad02...eb65` | `LONG` | 1,404,129.90 USD | `600.62` | `2460.69` | `2336.80` | `1079.69` | -73,810.66 USD | `-5.26%` | `5X Cross` |
| `1591` | `0x26e6...6b28` | `LONG` | 1,402,716.00 USD | `600.00` | `1769.78` | `2336.80` | `2005.49` | 340,844.47 USD | `+24.30%` | `20X Cross` |
| `1592` | `0x0deb...0bc5` | `LONG` | 1,402,500.00 USD | `600.00` | `2038.23` | `2336.80` | `1478.70` | 179,561.36 USD | `+12.80%` | `20X Cross` |
| `1593` | `0x0a84...6ddd` | `LONG` | 1,402,500.00 USD | `600.00` | `2222.36` | `2336.80` | `1774.81` | 69,081.66 USD | `+4.93%` | `25X Cross` |
| `1594` | `0x67c3...609d` | `SHORT` | 1,402,380.00 USD | `600.00` | `2386.55` | `2336.80` | `2560.78` | 29,551.89 USD | `+2.11%` | `25X Cross` |
| `1595` | `0x638f...f5f0` | `LONG` | 1,402,320.00 USD | `600.00` | `4011.50` | `2336.80` | `36.61` | -1,004,583.53 USD | `-71.64%` | `25X Cross` |
| `1614` | `0x94b6...e5b3` | `SHORT` | 1,371,258.61 USD | `586.71` | `2377.90` | `2336.80` | `2485.64` | 23,879.63 USD | `+1.74%` | `25X Cross` |
| `1621` | `0x0dd5...f6ee` | `LONG` | 1,359,903.06 USD | `581.80` | `2332.22` | `2336.80` | `789.27` | 3,012.42 USD | `+0.22%` | `5X Cross` |
| `1659` | `0xfb99...37f3` | `LONG` | 1,321,688.34 USD | `565.34` | `2362.35` | `2336.80` | `1207.03` | -13,848.01 USD | `-1.05%` | `3X Cross` |
| `1671` | `0x844b...7f42` | `SHORT` | 1,311,281.40 USD | `561.00` | `2026.17` | `2336.80` | `3030.46` | -174,597.99 USD | `-13.32%` | `25X Cross` |
| `1684` | `0xabe6...1d99` | `SHORT` | 1,299,659.35 USD | `556.00` | `2484.68` | `2336.80` | `2947.20` | 81,836.54 USD | `+6.30%` | `20X Cross` |
| `1737` | `0xfc66...ca06` | `LONG` | 1,251,120.93 USD | `535.28` | `2336.47` | `2336.80` | `0.000000` | 440.32 USD | `+0.04%` | `20X Cross` |
| `1742` | `0xad21...fb6a` | `LONG` | 1,243,031.74 USD | `531.87` | `2574.89` | `2336.80` | `1682.35` | -126,473.76 USD | `-10.17%` | `7X Cross` |
| `1774` | `0x8923...1bac` | `SHORT` | 1,209,019.87 USD | `517.18` | `2348.15` | `2336.80` | `3136.31` | 5,405.23 USD | `+0.45%` | `25X Cross` |
| `1794` | `0x0c7a...2f50` | `SHORT` | 1,190,259.04 USD | `509.25` | `2122.56` | `2336.80` | `4070.64` | -109,353.61 USD | `-9.19%` | `20X Cross` |
| `1817` | `0x89b2...9ca6` | `LONG` | 1,168,550.00 USD | `500.00` | `2484.03` | `2336.80` | `1954.22` | -73,469.35 USD | `-6.29%` | `25X Cross` |
| `1821` | `0x7298...7d6c` | `SHORT` | 1,164,618.27 USD | `498.15` | `3426.75` | `2336.80` | `5422.40` | 542,417.55 USD | `+46.57%` | `20X Cross` |
| `1838` | `0xc10f...23b3` | `LONG` | 1,145,326.00 USD | `490.00` | `2402.16` | `2336.80` | `2082.07` | -31,736.83 USD | `-2.77%` | `25X Cross` |
| `1841` | `0x404c...5f03` | `SHORT` | 1,144,677.22 USD | `489.79` | `2671.94` | `2336.80` | `4346.53` | 164,002.33 USD | `+14.33%` | `20X Cross` |
| `1843` | `0x321f...1c84` | `SHORT` | 1,140,687.20 USD | `488.02` | `2370.09` | `2336.80` | `3010.06` | 15,957.40 USD | `+1.40%` | `10X Cross` |
| `1913` | `0x82c6...fe42` | `LONG` | 1,081,260.25 USD | `462.50` | `2501.38` | `2336.80` | `2054.47` | -75,630.32 USD | `-6.99%` | `5X Isolated` |
| `1923` | `0x617e...0f97` | `SHORT` | 1,070,143.09 USD | `457.85` | `2205.60` | `2336.80` | `3684.01` | -60,299.25 USD | `-5.63%` | `10X Cross` |
| `1949` | `0xae55...2236` | `LONG` | 1,051,695.00 USD | `450.00` | `2510.21` | `2336.80` | `0.000000` | -77,902.50 USD | `-7.41%` | `25X Cross` |
| `1958` | `0xac26...a9c7` | `SHORT` | 1,042,993.74 USD | `446.28` | `2192.58` | `2336.80` | `8586.71` | -64,494.04 USD | `-6.18%` | `20X Cross` |
| `1962` | `0x53f8...ceff` | `LONG` | 1,041,717.84 USD | `445.60` | `2399.81` | `2336.80` | `0.000000` | -27,632.76 USD | `-2.65%` | `20X Cross` |
| `1975` | `0xd8a1...6687` | `LONG` | 1,031,906.77 USD | `441.53` | `2804.24` | `2336.80` | `2151.03` | -206,261.66 USD | `-19.99%` | `20X Cross` |
| `2000` | `0x248e...6be2` | `SHORT` | 1,019,988.60 USD | `436.40` | `2314.49` | `2336.80` | `4425.46` | -9,953.89 USD | `-0.98%` | `20X Cross` |
| `2007` | `0x80f2...0c3a` | `LONG` | 1,015,749.41 USD | `434.55` | `2564.17` | `2336.80` | `881.74` | -98,499.47 USD | `-9.70%` | `5X Cross` |
| `2039` | `0x15c8...045f` | `SHORT` | 1,002,548.84 USD | `428.90` | `1903.23` | `2336.80` | `3090.33` | -186,255.79 USD | `-18.58%` | `25X Cross` |
| `2045` | `0x4e6b...b7d4` | `LONG` | 1,000,048.19 USD | `427.77` | `2744.83` | `2336.80` | `102.47` | -174,116.84 USD | `-17.41%` | `25X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `ANNOUNCEMENT` | `INFO` | `4217.50` | 7,256.21 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 7.26K USD at 4217.5000 USD [API] | `2025-08-19 03:43:25` |
| `ANNOUNCEMENT` | `INFO` | `2359.70` | 3,992.38 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 3.99K USD at 2359.7000 USD [API] | `2026-05-10 17:51:00` |
| `ANNOUNCEMENT` | `INFO` | `2305.90` | 3,472.45 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 3.47K USD at 2305.9000 USD [API] | `2026-05-07 13:47:46` |
| `ANNOUNCEMENT` | `INFO` | `2305.90` | 6,636.15 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 6.64K USD at 2305.9000 USD [API] | `2026-05-07 13:47:46` |
| `ANNOUNCEMENT` | `INFO` | `2939.60` | 3,422.28 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 3.42K USD at 2939.6000 USD [API] | `2025-12-07 14:25:17` |
| `ANNOUNCEMENT` | `INFO` | `2359.50` | 21,748.93 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 21.75K USD at 2359.5000 USD [API] | `2026-10-22 16:53:08` |
| `ANNOUNCEMENT` | `INFO` | `2359.50` | 13,871.74 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 13.87K USD at 2359.5000 USD [API] | `2026-10-22 16:53:08` |
| `ANNOUNCEMENT` | `INFO` | `2359.50` | 12,701.90 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 12.70K USD at 2359.5000 USD [API] | `2026-10-22 16:53:08` |
| `ANNOUNCEMENT` | `INFO` | `2369.00` | 30,496.37 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 30.50K USD at 2369.0000 USD [API] | `2026-10-22 16:47:50` |
| `ANNOUNCEMENT` | `INFO` | `2369.00` | 30,150.03 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 30.15K USD at 2369.0000 USD [API] | `2026-10-22 16:47:50` |
| `ANNOUNCEMENT` | `INFO` | `2383.00` | 13,411.05 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 13.41K USD at 2383.0000 USD [API] | `2026-10-22 16:43:22` |
| `ANNOUNCEMENT` | `INFO` | `2383.00` | 107.95 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.11K USD at 2383.0000 USD [API] | `2026-10-22 16:43:22` |
| `ANNOUNCEMENT` | `INFO` | `2383.00` | 17.87 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.02K USD at 2383.0000 USD [API] | `2026-10-22 16:43:22` |
| `ANNOUNCEMENT` | `INFO` | `2383.00` | 20,000.04 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 20.00K USD at 2383.0000 USD [API] | `2026-10-22 16:43:22` |
| `ANNOUNCEMENT` | `INFO` | `2383.00` | 30,000.06 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 30.00K USD at 2383.0000 USD [API] | `2026-10-22 16:43:22` |
| `ANNOUNCEMENT` | `INFO` | `2383.00` | 10,000.02 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 10.00K USD at 2383.0000 USD [API] | `2026-10-22 16:43:22` |
| `ANNOUNCEMENT` | `INFO` | `2383.00` | 2,719.00 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 2.72K USD at 2383.0000 USD [API] | `2026-10-22 16:43:22` |
| `ANNOUNCEMENT` | `INFO` | `2410.40` | 14,993.41 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 14.99K USD at 2410.4000 USD [API] | `2026-10-22 08:34:05` |
| `ANNOUNCEMENT` | `INFO` | `2410.40` | 28,495.03 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 28.50K USD at 2410.4000 USD [API] | `2026-10-22 08:34:05` |
| `ANNOUNCEMENT` | `INFO` | `2410.40` | 11,745.88 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 11.75K USD at 2410.4000 USD [API] | `2026-10-22 08:34:05` |
| `ANNOUNCEMENT` | `INFO` | `2410.40` | 10,000.03 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 10.00K USD at 2410.4000 USD [API] | `2026-10-22 08:34:05` |
| `ANNOUNCEMENT` | `INFO` | `2410.40` | 10,000.03 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 10.00K USD at 2410.4000 USD [API] | `2026-10-22 08:34:05` |
| `ANNOUNCEMENT` | `INFO` | `2410.40` | 21,181.63 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 21.18K USD at 2410.4000 USD [API] | `2026-10-22 08:34:05` |
| `ANNOUNCEMENT` | `INFO` | `2345.40` | 56,289.60 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 56.29K USD at 2345.4000 USD [API] | `2026-10-18 19:30:48` |
| `ANNOUNCEMENT` | `INFO` | `2361.60` | 27,399.52 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 27.40K USD at 2361.6000 USD [API] | `2026-10-18 16:46:41` |
| `ANNOUNCEMENT` | `INFO` | `2361.60` | 289.77 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.29K USD at 2361.6000 USD [API] | `2026-10-18 16:46:41` |
| `ANNOUNCEMENT` | `INFO` | `2361.60` | 290.24 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.29K USD at 2361.6000 USD [API] | `2026-10-18 16:46:41` |
| `ANNOUNCEMENT` | `INFO` | `2361.60` | 340.07 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.34K USD at 2361.6000 USD [API] | `2026-10-18 16:46:41` |
| `ANNOUNCEMENT` | `INFO` | `2361.60` | 264.50 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.26K USD at 2361.6000 USD [API] | `2026-10-18 16:46:41` |
| `ANNOUNCEMENT` | `INFO` | `2361.60` | 1,497.49 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.50K USD at 2361.6000 USD [API] | `2026-10-18 16:46:41` |
| `ANNOUNCEMENT` | `INFO` | `2361.60` | 11.57 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.01K USD at 2361.6000 USD [API] | `2026-10-18 16:46:41` |
| `ANNOUNCEMENT` | `INFO` | `2361.70` | 250.34 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.25K USD at 2361.7000 USD [API] | `2026-10-18 16:46:41` |
| `ANNOUNCEMENT` | `INFO` | `2361.70` | 250.34 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.25K USD at 2361.7000 USD [API] | `2026-10-18 16:46:41` |
| `ANNOUNCEMENT` | `INFO` | `2361.70` | 49.83 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.05K USD at 2361.7000 USD [API] | `2026-10-18 16:46:41` |
| `ANNOUNCEMENT` | `INFO` | `2361.70` | 49.83 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.05K USD at 2361.7000 USD [API] | `2026-10-18 16:46:41` |
| `ANNOUNCEMENT` | `INFO` | `2361.80` | 40,050.93 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 40.05K USD at 2361.8000 USD [API] | `2026-10-18 16:46:41` |
| `ANNOUNCEMENT` | `INFO` | `2361.80` | 49.83 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.05K USD at 2361.8000 USD [API] | `2026-10-18 16:46:41` |
| `ANNOUNCEMENT` | `INFO` | `2361.90` | 15.35 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.02K USD at 2361.9000 USD [API] | `2026-10-18 16:46:41` |
| `ANNOUNCEMENT` | `INFO` | `2362.00` | 11.81 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.01K USD at 2362.0000 USD [API] | `2026-10-18 16:46:41` |
| `ANNOUNCEMENT` | `INFO` | `2362.10` | 30.00 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.03K USD at 2362.1000 USD [API] | `2026-10-18 16:46:41` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`2401.93` (Vol: 18,600,000.00 USD, Dist: `+2.94%`) | Long MP=`2284.33` (Vol: 27,300,000.00 USD, Dist: `--2.10%`)
  * 48H Horizon: Short MP=`2401.93` (Vol: 25,300,000.00 USD, Dist: `+2.94%`) | Long MP=`2284.33` (Vol: 30,000,000.00 USD, Dist: `--2.10%`)
  * 3D Horizon: Short MP=`2401.93` (Vol: 26,700,000.00 USD, Dist: `+2.94%`) | Long MP=`2286.29` (Vol: 37,900,000.00 USD, Dist: `--2.01%`)
  * 7D Horizon: Short MP=`2402.93` (Vol: 47,100,000.00 USD, Dist: `+2.99%`) | Long MP=`2284.60` (Vol: 72,300,000.00 USD, Dist: `--2.08%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `465.00` | 8,990.00 USD | 872,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `475.00` | 38,510.00 USD | 872,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.00` | 16,660.00 USD | 872,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `495.00` | 3,730.00 USD | 872,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.00` | 1,420.00 USD | 872,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.00` | 8,360.00 USD | 872,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.00` | 7,830.00 USD | 872,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.00` | 7,800.00 USD | 872,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.00` | 183,350.00 USD | 872,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.00` | 23,730.00 USD | 871,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `565.00` | 77,720.00 USD | 871,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `575.00` | 8,530.00 USD | 871,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.00` | 461,390.00 USD | 871,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.00` | 868.52 USD | 871,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `605.00` | 17,020.00 USD | 871,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.00` | 34,040.00 USD | 871,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.00` | 101,730.00 USD | 871,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.00` | 4,650.00 USD | 871,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `645.00` | 1,310.00 USD | 871,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `655.00` | 37,950.00 USD | 871,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `665.00` | 55,130.00 USD | 871,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `675.00` | 106,820.00 USD | 871,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `685.00` | 25,510.00 USD | 870,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `695.00` | 16,540.00 USD | 870,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `705.00` | 111,270.00 USD | 870,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `715.00` | 2,070.00 USD | 870,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `725.00` | 396,310.00 USD | 870,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `735.00` | 47,970.00 USD | 870,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `745.00` | 7,620.00 USD | 870,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `755.00` | 26,430.00 USD | 870,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `765.00` | 30,660.00 USD | 870,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `775.00` | 1,740,000.00 USD | 870,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `785.00` | 40,690.00 USD | 868,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `795.00` | 58,880.00 USD | 868,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `805.00` | 231,460.00 USD | 868,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `815.00` | 51,830.00 USD | 868,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `825.00` | 382,270.00 USD | 868,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `835.00` | 129,920.00 USD | 867,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `845.00` | 7,240.00 USD | 867,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `855.00` | 2,900.00 USD | 867,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `865.00` | 3,780,000.00 USD | 867,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `875.00` | 44,640.00 USD | 863,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `885.00` | 7,390.00 USD | 863,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `895.00` | 407,820.00 USD | 863,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `905.00` | 80,220.00 USD | 863,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `915.00` | 740,670.00 USD | 863,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `925.00` | 151,670.00 USD | 862,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `935.00` | 1,010,000.00 USD | 862,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `945.00` | 8,990.00 USD | 861,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `955.00` | 179,010.00 USD | 861,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `965.00` | 81,690.00 USD | 861,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `975.00` | 73,410.00 USD | 861,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `985.00` | 19,550.00 USD | 861,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `995.00` | 199,260.00 USD | 861,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1005.00` | 44,810.00 USD | 860,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1015.00` | 7,140,000.00 USD | 860,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1025.00` | 117,290.00 USD | 853,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1035.00` | 1,530,000.00 USD | 853,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1045.00` | 419,240.00 USD | 852,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1055.00` | 1,310,000.00 USD | 851,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1065.00` | 184,790.00 USD | 850,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1075.00` | 670,040.00 USD | 850,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1085.00` | 33,280.00 USD | 849,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1095.00` | 1,700,000.00 USD | 849,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1105.00` | 220,280.00 USD | 847,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1115.00` | 102,200.00 USD | 847,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1125.00` | 75,690.00 USD | 847,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1135.00` | 252,620.00 USD | 847,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1145.00` | 287,050.00 USD | 847,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1155.00` | 471,300.00 USD | 846,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1165.00` | 14,090.00 USD | 846,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1175.00` | 212,590.00 USD | 846,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1185.00` | 270,070.00 USD | 846,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1195.00` | 346,720.00 USD | 845,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1205.00` | 908,570.00 USD | 845,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1215.00` | 180,900.00 USD | 844,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1225.00` | 11,270,000.00 USD | 844,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1235.00` | 195,730.00 USD | 833,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1245.00` | 313,430.00 USD | 832,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1255.00` | 667,560.00 USD | 832,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1265.00` | 1,580,000.00 USD | 831,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1275.00` | 66,370.00 USD | 830,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1285.00` | 16,150,000.00 USD | 830,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1295.00` | 398,630.00 USD | 814,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1305.00` | 198,210.00 USD | 813,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1315.00` | 504,350.00 USD | 813,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1325.00` | 562,110.00 USD | 813,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1335.00` | 373,490.00 USD | 812,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1345.00` | 644,470.00 USD | 812,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1355.00` | 61,580.00 USD | 811,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1365.00` | 7,930,000.00 USD | 811,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1375.00` | 245,580.00 USD | 803,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1385.00` | 171,880.00 USD | 803,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1395.00` | 302,930.00 USD | 803,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1405.00` | 10,010,000.00 USD | 802,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1415.00` | 22,360,000.00 USD | 792,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1425.00` | 1,430,000.00 USD | 770,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1435.00` | 451,460.00 USD | 768,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1445.00` | 57,490.00 USD | 768,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1455.00` | 14,630,000.00 USD | 768,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1465.00` | 390,720.00 USD | 753,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1475.00` | 2,310,000.00 USD | 753,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1485.00` | 4,640,000.00 USD | 751,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1495.00` | 345,390.00 USD | 746,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1505.00` | 389,670.00 USD | 746,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1515.00` | 415,830.00 USD | 745,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1525.00` | 18,520,000.00 USD | 745,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1535.00` | 1,030,000.00 USD | 726,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1545.00` | 22,690,000.00 USD | 725,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1555.00` | 507,200.00 USD | 703,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1565.00` | 25,200,000.00 USD | 702,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1575.00` | 277,870.00 USD | 677,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1585.00` | 252,400.00 USD | 677,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1595.00` | 7,530,000.00 USD | 676,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1605.00` | 18,470,000.00 USD | 669,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1615.00` | 266,450.00 USD | 650,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1625.00` | 170,470.00 USD | 650,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1635.00` | 21,150,000.00 USD | 650,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1645.00` | 36,490,000.00 USD | 629,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1655.00` | 965,970.00 USD | 592,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1665.00` | 773,230.00 USD | 591,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1675.00` | 11,590,000.00 USD | 591,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1685.00` | 1,390,000.00 USD | 579,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1695.00` | 596,490.00 USD | 578,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1705.00` | 1,510,000.00 USD | 577,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1715.00` | 461,590.00 USD | 575,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1725.00` | 29,000,000.00 USD | 575,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1735.00` | 18,850,000.00 USD | 546,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1745.00` | 1,460,000.00 USD | 527,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1755.00` | 1,100,000.00 USD | 526,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1765.00` | 1,230,000.00 USD | 525,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1775.00` | 1,440,000.00 USD | 523,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1785.00` | 54,240,000.00 USD | 522,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1795.00` | 16,770,000.00 USD | 468,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1805.00` | 1,860,000.00 USD | 451,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1815.00` | 712,350.00 USD | 449,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1825.00` | 620,950.00 USD | 448,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1835.00` | 1,690,000.00 USD | 448,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1845.00` | 1,260,000.00 USD | 446,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1855.00` | 13,970,000.00 USD | 445,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1865.00` | 2,030,000.00 USD | 431,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1875.00` | 5,580,000.00 USD | 429,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1885.00` | 2,740,000.00 USD | 423,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1895.00` | 5,240,000.00 USD | 420,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1905.00` | 1,510,000.00 USD | 415,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1915.00` | 28,440,000.00 USD | 414,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1925.00` | 4,070,000.00 USD | 385,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1935.00` | 1,130,000.00 USD | 381,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1945.00` | 657,850.00 USD | 380,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1955.00` | 3,580,000.00 USD | 379,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1965.00` | 751,430.00 USD | 376,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1975.00` | 6,100,000.00 USD | 375,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1985.00` | 5,230,000.00 USD | 369,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1995.00` | 576,630.00 USD | 364,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2005.00` | 2,810,000.00 USD | 363,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2015.00` | 3,250,000.00 USD | 360,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2025.00` | 1,130,000.00 USD | 357,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2035.00` | 1,050,000.00 USD | 356,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2045.00` | 20,160,000.00 USD | 355,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2055.00` | 4,750,000.00 USD | 335,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2065.00` | 1,260,000.00 USD | 330,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2075.00` | 1,330,000.00 USD | 329,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2077.20` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 4,860,000.00 USD | 4,190,000.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2080.00` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 3,400,000.00 USD | 3,020,000.00 USD | 2,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2082.80` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 2,420,000.00 USD | 1,860,000.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 2,380,000.00 USD | 327,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2085.60` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 3,840,000.00 USD | 2,320,000.00 USD | 3,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2088.40` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 2,280,000.00 USD | 1,370,000.00 USD | 893,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2091.20` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 4,280,000.00 USD | 952,210.00 USD | 6,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2091.30` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 1,070,000.00 USD | 493,460.00 USD | 671,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2093.80` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 1,800,000.00 USD | 930,100.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2094.00` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 5,200,000.00 USD | 1,660,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 1,200,000.00 USD | 325,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2096.30` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 655,450.00 USD | 751,890.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2096.80` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 1,940,000.00 USD | 3,320,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2098.80` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 547,670.00 USD | 669,810.00 USD | 248,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2099.60` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 1,880,000.00 USD | 1,920,000.00 USD | 3,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2101.30` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 46,810.00 USD | 31,040.00 USD | 304,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2102.40` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 125,250.00 USD | 341,900.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2103.80` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 1,070,000.00 USD | 561,040.00 USD | 183,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 1,690,000.00 USD | 324,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2105.20` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,800,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2106.30` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 251,360.00 USD | 400,040.00 USD | 510,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2108.00` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 2,400,000.00 USD | 930,280.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2108.80` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 412,950.00 USD | 21,400.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2110.80` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 2,750,000.00 USD | 1,780,000.00 USD | 2,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2111.30` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 490,860.00 USD | 19,060.00 USD | 193,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2113.60` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 1,780,000.00 USD | 1,280,000.00 USD | 2,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2113.80` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 420,950.00 USD | 634,310.00 USD | 241,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 20,530,000.00 USD | 322,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2116.30` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 13,230.00 USD | 759,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2116.40` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 1,900,000.00 USD | 2,210,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2118.80` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 695,080.00 USD | 99,440.00 USD | 864,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2119.20` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 2,920,000.00 USD | 750,810.00 USD | 2,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2121.30` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 916,680.00 USD | 846,370.00 USD | 777,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2122.00` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 2,300,000.00 USD | 1,020,000.00 USD | 1,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2123.80` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 966,890.00 USD | 854,260.00 USD | 996,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2124.80` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 2,680,000.00 USD | 939,650.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 1,010,000.00 USD | 302,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2126.30` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 58,860.00 USD | 841,670.00 USD | 628,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2127.60` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 514,750.00 USD | 2,620,000.00 USD | 2,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2128.80` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 356,740.00 USD | 475,750.00 USD | 323,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2130.40` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 2,040,000.00 USD | 2,130,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2131.30` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 644,330.00 USD | 336,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2133.20` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 1,930,000.00 USD | 715,940.00 USD | 323,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2133.80` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 187,520.00 USD | 497,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 3,270,000.00 USD | 301,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2136.00` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 1,370,000.00 USD | 596,290.00 USD | 18,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2136.30` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 294,600.00 USD | 2,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2138.80` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 555,320.00 USD | 250,240.00 USD | 205,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2138.80` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 1,110,000.00 USD | 1,250,000.00 USD | 60,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2141.60` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 1,550,000.00 USD | 209,240.00 USD | 766,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2143.80` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 295,510.00 USD | 16,700.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2144.40` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 465,960.00 USD | 1,530,000.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 9,500,000.00 USD | 297,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2146.30` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 11,090.00 USD | 207,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2147.20` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 239,110.00 USD | 10,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2148.80` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 251,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2150.00` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 459,630.00 USD | 463,640.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2152.80` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 29,510.00 USD | 331,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 17,990,000.00 USD | 288,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2155.60` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 157,380.00 USD | 430,180.00 USD | 66,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2158.40` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 687,180.00 USD | 1,010,000.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2161.20` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 1,490,000.00 USD | 1,050,000.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2164.00` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 36,870.00 USD | 329,690.00 USD | 409,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 6,290,000.00 USD | 270,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2166.80` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 25,540.00 USD | 0.00 USD | 68,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2169.60` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 1,700,000.00 USD | 726,240.00 USD | 810,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2172.40` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 479,540.00 USD | 1,150,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 108,810,000.00 USD | 264,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2185.00` | 111,820,000.00 USD | 155,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2194.80` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 141,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 1,260,000.00 USD | 43,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2197.60` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 2,440,000.00 USD | 3,270,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2200.40` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 3,000,000.00 USD | 3,140,000.00 USD | 3,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2201.30` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 284,470.00 USD | 217,490.00 USD | 225,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2203.20` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 3,240,000.00 USD | 624,500.00 USD | 2,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2203.80` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 1,050,000.00 USD | 207,110.00 USD | 755,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 1,290,000.00 USD | 42,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2206.00` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 6,050,000.00 USD | 4,010,000.00 USD | 4,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2206.30` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 611,820.00 USD | 2,270,000.00 USD | 722,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2208.80` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 2,490,000.00 USD | 668,670.00 USD | 3,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2208.80` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 10,060,000.00 USD | 7,030,000.00 USD | 3,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2211.30` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 2,770,000.00 USD | 1,250,000.00 USD | 573,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2211.60` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 8,410,000.00 USD | 7,020,000.00 USD | 7,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2213.80` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 3,890,000.00 USD | 2,980,000.00 USD | 2,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2214.40` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 12,890,000.00 USD | 12,380,000.00 USD | 9,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 1,710,000.00 USD | 40,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2216.30` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 6,130,000.00 USD | 6,230,000.00 USD | 4,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2217.20` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 16,020,000.00 USD | 10,280,000.00 USD | 8,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2218.80` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 4,630,000.00 USD | 3,610,000.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2220.00` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 12,900,000.00 USD | 10,310,000.00 USD | 3,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2221.30` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 1,750,000.00 USD | 2,050,000.00 USD | 733,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2222.80` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 5,190,000.00 USD | 5,430,000.00 USD | 8,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2223.80` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 4,950,000.00 USD | 4,260,000.00 USD | 3,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2225.00` | 2,840,000.00 USD | 39,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2225.60` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 13,090,000.00 USD | 13,590,000.00 USD | 9,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2226.30` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 5,340,000.00 USD | 4,790,000.00 USD | 2,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2228.40` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 7,680,000.00 USD | 5,550,000.00 USD | 8,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2228.80` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 2,720,000.00 USD | 1,580,000.00 USD | 812,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2231.20` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 9,590,000.00 USD | 2,970,000.00 USD | 16,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2231.30` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 3,330,000.00 USD | 2,610,000.00 USD | 3,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2233.80` | 995,370,000.00 USD | 995,370,000.00 USD | 6,920,000.00 USD | 3,770,000.00 USD | 3,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2234.00` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 18,760,000.00 USD | 10,880,000.00 USD | 6,070,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2235.00` | 1,030,000.00 USD | 36,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2236.30` | 981,000,000.00 USD | 981,000,000.00 USD | 2,430,000.00 USD | 2,100,000.00 USD | 3,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2236.80` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 6,910,000.00 USD | 11,270,000.00 USD | 5,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2238.80` | 972,700,000.00 USD | 972,700,000.00 USD | 1,580,000.00 USD | 2,180,000.00 USD | 844,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2239.60` | 2,090,000,000.00 USD | 2,090,000,000.00 USD | 6,630,000.00 USD | 7,850,000.00 USD | 8,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2241.30` | 968,090,000.00 USD | 968,090,000.00 USD | 456,710.00 USD | 542,280.00 USD | 740,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2242.40` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 4,840,000.00 USD | 1,890,000.00 USD | 4,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2243.80` | 966,350,000.00 USD | 966,350,000.00 USD | 1,520,000.00 USD | 1,590,000.00 USD | 991,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2245.00` | 4,620,000.00 USD | 35,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2245.20` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 16,830,000.00 USD | 13,940,000.00 USD | 11,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2246.30` | 962,250,000.00 USD | 962,250,000.00 USD | 2,730,000.00 USD | 2,020,000.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2248.00` | 2,010,000,000.00 USD | 2,010,000,000.00 USD | 13,600,000.00 USD | 6,140,000.00 USD | 10,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2248.80` | 955,590,000.00 USD | 955,590,000.00 USD | 4,450,000.00 USD | 601,150.00 USD | 1,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2250.80` | 1,980,000,000.00 USD | 1,980,000,000.00 USD | 10,570,000.00 USD | 10,480,000.00 USD | 8,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2251.30` | 948,810,000.00 USD | 948,810,000.00 USD | 304,760.00 USD | 1,060,000.00 USD | 1,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2253.60` | 1,950,000,000.00 USD | 1,950,000,000.00 USD | 24,760,000.00 USD | 21,020,000.00 USD | 21,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2253.80` | 945,540,000.00 USD | 945,540,000.00 USD | 8,560,000.00 USD | 6,780,000.00 USD | 5,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2255.00` | 11,260,000.00 USD | 30,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2256.30` | 924,500,000.00 USD | 924,500,000.00 USD | 3,260,000.00 USD | 2,970,000.00 USD | 3,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2256.40` | 1,880,000,000.00 USD | 1,880,000,000.00 USD | 31,260,000.00 USD | 19,360,000.00 USD | 15,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2258.80` | 914,390,000.00 USD | 914,390,000.00 USD | 6,260,000.00 USD | 2,980,000.00 USD | 4,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2259.20` | 1,820,000,000.00 USD | 1,820,000,000.00 USD | 24,810,000.00 USD | 20,200,000.00 USD | 22,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2261.30` | 900,610,000.00 USD | 900,610,000.00 USD | 12,710,000.00 USD | 12,030,000.00 USD | 13,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2262.00` | 1,750,000,000.00 USD | 1,750,000,000.00 USD | 45,920,000.00 USD | 30,170,000.00 USD | 22,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2263.80` | 862,760,000.00 USD | 862,760,000.00 USD | 12,170,000.00 USD | 11,500,000.00 USD | 7,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2264.80` | 1,650,000,000.00 USD | 1,650,000,000.00 USD | 30,210,000.00 USD | 26,720,000.00 USD | 18,300,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2265.00` | 4,930,000.00 USD | 19,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2266.30` | 831,570,000.00 USD | 831,570,000.00 USD | 11,310,000.00 USD | 12,590,000.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2267.60` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 40,210,000.00 USD | 41,610,000.00 USD | 31,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2268.80` | 804,280,000.00 USD | 804,280,000.00 USD | 14,280,000.00 USD | 9,540,000.00 USD | 7,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2270.40` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 46,080,000.00 USD | 25,460,000.00 USD | 39,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2271.30` | 772,630,000.00 USD | 772,630,000.00 USD | 4,880,000.00 USD | 8,750,000.00 USD | 6,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2273.20` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 26,430,000.00 USD | 25,760,000.00 USD | 20,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2273.80` | 752,450,000.00 USD | 752,450,000.00 USD | 15,670,000.00 USD | 9,050,000.00 USD | 5,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2275.00` | 4,720,000.00 USD | 14,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2276.00` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 52,620,000.00 USD | 46,680,000.00 USD | 45,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2276.30` | 722,160,000.00 USD | 722,160,000.00 USD | 15,330,000.00 USD | 14,330,000.00 USD | 12,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2278.80` | 679,540,000.00 USD | 679,540,000.00 USD | 18,640,000.00 USD | 9,000,000.00 USD | 13,280,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2278.80` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 69,920,000.00 USD | 30,780,000.00 USD | 43,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2281.30` | 638,620,000.00 USD | 638,620,000.00 USD | 20,900,000.00 USD | 13,540,000.00 USD | 14,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2281.60` | 989,680,000.00 USD | 989,680,000.00 USD | 61,930,000.00 USD | 60,060,000.00 USD | 46,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2283.80` | 589,590,000.00 USD | 589,590,000.00 USD | 29,350,000.00 USD | 22,160,000.00 USD | 22,940,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2284.40` | 821,100,000.00 USD | 821,100,000.00 USD | 84,440,000.00 USD | 69,880,000.00 USD | 44,650,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2285.00` | 3,920,000.00 USD | 9,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2286.30` | 515,140,000.00 USD | 515,140,000.00 USD | 18,110,000.00 USD | 24,680,000.00 USD | 10,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2287.20` | 622,130,000.00 USD | 622,130,000.00 USD | 59,100,000.00 USD | 55,220,000.00 USD | 44,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2288.80` | 461,650,000.00 USD | 461,650,000.00 USD | 17,050,000.00 USD | 15,760,000.00 USD | 5,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2290.00` | 463,560,000.00 USD | 463,560,000.00 USD | 49,600,000.00 USD | 34,580,000.00 USD | 24,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2291.30` | 423,020,000.00 USD | 423,020,000.00 USD | 16,070,000.00 USD | 18,680,000.00 USD | 5,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2292.80` | 355,060,000.00 USD | 355,060,000.00 USD | 38,470,000.00 USD | 20,900,000.00 USD | 42,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2293.80` | 382,940,000.00 USD | 382,940,000.00 USD | 19,790,000.00 USD | 13,900,000.00 USD | 14,840,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2295.00` | 3,480,000.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2295.60` | 253,330,000.00 USD | 253,330,000.00 USD | 17,510,000.00 USD | 8,110,000.00 USD | 6,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2296.30` | 334,420,000.00 USD | 334,420,000.00 USD | 20,750,000.00 USD | 10,930,000.00 USD | 6,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2298.40` | 220,910,000.00 USD | 220,910,000.00 USD | 2,090,000.00 USD | 5,820,000.00 USD | 301,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2298.80` | 296,200,000.00 USD | 296,200,000.00 USD | 10,060,000.00 USD | 8,310,000.00 USD | 3,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2301.20` | 212,700,000.00 USD | 212,700,000.00 USD | 11,790,000.00 USD | 2,120,000.00 USD | 7,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2301.30` | 274,290,000.00 USD | 274,290,000.00 USD | 17,220,000.00 USD | 11,670,000.00 USD | 12,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2303.80` | 233,060,000.00 USD | 233,060,000.00 USD | 27,640,000.00 USD | 15,560,000.00 USD | 16,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2304.00` | 191,200,000.00 USD | 191,200,000.00 USD | 32,960,000.00 USD | 17,170,000.00 USD | 13,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2305.00` | 1,030,000.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2306.30` | 173,340,000.00 USD | 173,340,000.00 USD | 6,150,000.00 USD | 5,110,000.00 USD | 16,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2306.80` | 127,800,000.00 USD | 127,800,000.00 USD | 0.00 USD | 3,740,000.00 USD | 11,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2308.80` | 145,620,000.00 USD | 145,620,000.00 USD | 1,370,000.00 USD | 2,120,000.00 USD | 2,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2309.60` | 113,040,000.00 USD | 113,040,000.00 USD | 282,530.00 USD | 300,580.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2311.30` | 139,580,000.00 USD | 139,580,000.00 USD | 8,550,000.00 USD | 5,190,000.00 USD | 6,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2312.40` | 110,950,000.00 USD | 110,950,000.00 USD | 6,560,000.00 USD | 640,510.00 USD | 2,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2313.80` | 118,990,000.00 USD | 118,990,000.00 USD | 6,160,000.00 USD | 6,220,000.00 USD | 5,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2315.00` | 938,780.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2315.20` | 101,250,000.00 USD | 101,250,000.00 USD | 5,020,000.00 USD | 7,520,000.00 USD | 117,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2316.30` | 101,180,000.00 USD | 101,180,000.00 USD | 10,440,000.00 USD | 11,520,000.00 USD | 5,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2318.00` | 88,590,000.00 USD | 88,590,000.00 USD | 817,040.00 USD | 3,010,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2318.80` | 73,380,000.00 USD | 73,380,000.00 USD | 11,680,000.00 USD | 4,080,000.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2320.80` | 84,770,000.00 USD | 84,770,000.00 USD | 0.00 USD | 2,960,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2321.30` | 55,370,000.00 USD | 55,370,000.00 USD | 255,100.00 USD | 2,970,000.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2323.60` | 81,810,000.00 USD | 81,810,000.00 USD | 4,070,000.00 USD | 2,210,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2323.80` | 50,420,000.00 USD | 50,420,000.00 USD | 8,620,000.00 USD | 2,890,000.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2325.00` | 344,610.00 USD | 344,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2326.30` | 36,690,000.00 USD | 36,690,000.00 USD | 0.00 USD | 2,910,000.00 USD | 66,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2326.40` | 75,530,000.00 USD | 75,530,000.00 USD | 0.00 USD | 0.00 USD | 126,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2328.80` | 33,720,000.00 USD | 33,720,000.00 USD | 1,890,000.00 USD | 1,150,000.00 USD | 237,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2329.20` | 75,400,000.00 USD | 75,400,000.00 USD | 3,860,000.00 USD | 0.00 USD | 4,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2331.30` | 30,440,000.00 USD | 30,440,000.00 USD | 13,200,000.00 USD | 0.00 USD | 126,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2332.00` | 66,660,000.00 USD | 66,660,000.00 USD | 29,230,000.00 USD | 0.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2333.80` | 17,110,000.00 USD | 17,110,000.00 USD | 3,620,000.00 USD | 12,110,000.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2334.80` | 34,610,000.00 USD | 34,610,000.00 USD | 7,260,000.00 USD | 18,420,000.00 USD | 8,930,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2335.00` | 735.29 USD | 735.29 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2336.30` | 7,590,000.00 USD | 7,590,000.00 USD | 7,590,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2337.60` | 23,130,000.00 USD | 23,130,000.00 USD | 9,570,000.00 USD | 0.00 USD | 13,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2338.80` | 9,010,000.00 USD | 9,010,000.00 USD | 0.00 USD | 0.00 USD | 1,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2340.40` | 36,520,000.00 USD | 36,520,000.00 USD | 0.00 USD | 10,010,000.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2343.20` | 45,900,000.00 USD | 45,900,000.00 USD | 0.00 USD | 5,540,000.00 USD | 3,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2343.80` | 17,240,000.00 USD | 17,240,000.00 USD | 0.00 USD | 1,960,000.00 USD | 6,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2346.00` | 66,650,000.00 USD | 66,650,000.00 USD | 0.00 USD | 7,920,000.00 USD | 12,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2346.30` | 22,790,000.00 USD | 22,790,000.00 USD | 1,130,000.00 USD | 0.00 USD | 4,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2348.80` | 29,530,000.00 USD | 29,530,000.00 USD | 5,710,000.00 USD | 42,760.00 USD | 990,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2348.80` | 85,130,000.00 USD | 85,130,000.00 USD | 495,290.00 USD | 7,240,000.00 USD | 10,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2351.30` | 59,850,000.00 USD | 59,850,000.00 USD | 21,660,000.00 USD | 2,630,000.00 USD | 6,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2351.60` | 109,340,000.00 USD | 109,340,000.00 USD | 572,980.00 USD | 17,950,000.00 USD | 5,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2353.80` | 70,290,000.00 USD | 70,290,000.00 USD | 858,830.00 USD | 9,490,000.00 USD | 90,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2354.40` | 150,580,000.00 USD | 150,580,000.00 USD | 6,120,000.00 USD | 34,750,000.00 USD | 371,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2356.30` | 81,690,000.00 USD | 81,690,000.00 USD | 2,090,000.00 USD | 7,920,000.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2357.20` | 164,960,000.00 USD | 164,960,000.00 USD | 8,470,000.00 USD | 5,920,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2358.80` | 90,660,000.00 USD | 90,660,000.00 USD | 74,690.00 USD | 3,010,000.00 USD | 5,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2360.00` | 174,680,000.00 USD | 174,680,000.00 USD | 6,300,000.00 USD | 3,430,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2361.30` | 103,450,000.00 USD | 103,450,000.00 USD | 4,190,000.00 USD | 8,350,000.00 USD | 261,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2362.80` | 177,560,000.00 USD | 177,560,000.00 USD | 1,180,000.00 USD | 0.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2363.80` | 115,860,000.00 USD | 115,860,000.00 USD | 4,890,000.00 USD | 3,710,000.00 USD | 3,810,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 602.37 USD | 1,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2365.60` | 185,560,000.00 USD | 185,560,000.00 USD | 6,340,000.00 USD | 0.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2366.30` | 116,230,000.00 USD | 116,230,000.00 USD | 192,950.00 USD | 0.00 USD | 171,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2368.40` | 196,030,000.00 USD | 196,030,000.00 USD | 9,590,000.00 USD | 475,460.00 USD | 404,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2368.80` | 129,510,000.00 USD | 129,510,000.00 USD | 8,900,000.00 USD | 3,260,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2371.20` | 258,470,000.00 USD | 258,470,000.00 USD | 16,760,000.00 USD | 0.00 USD | 45,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2371.30` | 166,930,000.00 USD | 166,930,000.00 USD | 15,980,000.00 USD | 12,950,000.00 USD | 8,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2373.80` | 187,400,000.00 USD | 187,400,000.00 USD | 13,540,000.00 USD | 1,040,000.00 USD | 5,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2374.00` | 280,480,000.00 USD | 280,480,000.00 USD | 15,830,000.00 USD | 121,480.00 USD | 6,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 488,660.00 USD | 490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2376.30` | 211,760,000.00 USD | 211,760,000.00 USD | 11,340,000.00 USD | 3,120,000.00 USD | 9,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2376.80` | 320,690,000.00 USD | 320,690,000.00 USD | 12,140,000.00 USD | 5,950,000.00 USD | 22,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2378.80` | 239,880,000.00 USD | 239,880,000.00 USD | 5,000,000.00 USD | 12,440,000.00 USD | 10,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2379.60` | 348,000,000.00 USD | 348,000,000.00 USD | 7,180,000.00 USD | 2,580,000.00 USD | 17,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2381.30` | 283,540,000.00 USD | 283,540,000.00 USD | 14,790,000.00 USD | 11,660,000.00 USD | 17,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2382.40` | 390,210,000.00 USD | 390,210,000.00 USD | 8,510,000.00 USD | 12,380,000.00 USD | 21,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2383.80` | 330,580,000.00 USD | 330,580,000.00 USD | 20,120,000.00 USD | 16,140,000.00 USD | 10,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 3,920,000.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2385.20` | 489,090,000.00 USD | 489,090,000.00 USD | 17,480,000.00 USD | 30,700,000.00 USD | 50,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2386.30` | 369,760,000.00 USD | 369,760,000.00 USD | 13,990,000.00 USD | 15,160,000.00 USD | 10,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2388.00` | 562,530,000.00 USD | 562,530,000.00 USD | 4,540,000.00 USD | 34,290,000.00 USD | 34,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2388.80` | 393,020,000.00 USD | 393,020,000.00 USD | 11,070,000.00 USD | 5,020,000.00 USD | 7,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2390.80` | 660,760,000.00 USD | 660,760,000.00 USD | 5,470,000.00 USD | 44,170,000.00 USD | 48,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2391.30` | 415,200,000.00 USD | 415,200,000.00 USD | 3,340,000.00 USD | 11,960,000.00 USD | 6,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2393.60` | 759,660,000.00 USD | 759,660,000.00 USD | 44,040,000.00 USD | 23,140,000.00 USD | 31,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2393.80` | 439,560,000.00 USD | 439,560,000.00 USD | 10,210,000.00 USD | 10,400,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 4,260,000.00 USD | 8,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2396.30` | 450,850,000.00 USD | 450,850,000.00 USD | 2,630,000.00 USD | 4,140,000.00 USD | 4,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2396.40` | 847,020,000.00 USD | 847,020,000.00 USD | 29,670,000.00 USD | 34,800,000.00 USD | 22,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2398.80` | 485,560,000.00 USD | 485,560,000.00 USD | 12,530,000.00 USD | 11,030,000.00 USD | 11,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2399.20` | 939,540,000.00 USD | 939,540,000.00 USD | 41,690,000.00 USD | 31,030,000.00 USD | 19,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2401.30` | 508,420,000.00 USD | 508,420,000.00 USD | 7,850,000.00 USD | 7,800,000.00 USD | 7,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2402.00` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 51,500,000.00 USD | 23,600,000.00 USD | 30,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2403.80` | 537,340,000.00 USD | 537,340,000.00 USD | 12,130,000.00 USD | 9,550,000.00 USD | 7,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2404.80` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 36,380,000.00 USD | 25,660,000.00 USD | 15,080,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 9,070,000.00 USD | 17,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2406.30` | 563,240,000.00 USD | 563,240,000.00 USD | 11,630,000.00 USD | 7,530,000.00 USD | 6,750,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2407.60` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 26,430,000.00 USD | 30,520,000.00 USD | 18,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2408.80` | 592,770,000.00 USD | 592,770,000.00 USD | 7,930,000.00 USD | 12,550,000.00 USD | 9,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2410.40` | 1,270,000,000.00 USD | 1,270,000,000.00 USD | 22,760,000.00 USD | 27,140,000.00 USD | 24,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2411.30` | 615,630,000.00 USD | 615,630,000.00 USD | 11,090,000.00 USD | 7,730,000.00 USD | 4,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2413.20` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 13,250,000.00 USD | 13,960,000.00 USD | 12,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2413.80` | 623,750,000.00 USD | 623,750,000.00 USD | 4,070,000.00 USD | 1,390,000.00 USD | 2,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 255,650.00 USD | 17,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2416.00` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 27,740,000.00 USD | 17,520,000.00 USD | 32,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2416.30` | 640,050,000.00 USD | 640,050,000.00 USD | 4,650,000.00 USD | 7,220,000.00 USD | 4,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2418.80` | 650,170,000.00 USD | 650,170,000.00 USD | 3,840,000.00 USD | 3,140,000.00 USD | 3,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2418.80` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 27,450,000.00 USD | 16,840,000.00 USD | 12,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2421.30` | 667,980,000.00 USD | 667,980,000.00 USD | 6,170,000.00 USD | 5,620,000.00 USD | 6,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2421.60` | 1,510,000,000.00 USD | 1,510,000,000.00 USD | 22,900,000.00 USD | 25,380,000.00 USD | 18,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2423.80` | 680,260,000.00 USD | 680,260,000.00 USD | 4,540,000.00 USD | 4,960,000.00 USD | 2,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.40` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 26,330,000.00 USD | 29,850,000.00 USD | 33,610,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 815,490.00 USD | 18,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2426.30` | 682,110,000.00 USD | 682,110,000.00 USD | 972,850.00 USD | 835,420.00 USD | 37,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2427.20` | 1,670,000,000.00 USD | 1,670,000,000.00 USD | 22,440,000.00 USD | 21,730,000.00 USD | 23,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2428.80` | 686,250,000.00 USD | 686,250,000.00 USD | 1,900,000.00 USD | 751,750.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2430.00` | 1,700,000,000.00 USD | 1,700,000,000.00 USD | 9,270,000.00 USD | 16,890,000.00 USD | 7,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2431.30` | 691,680,000.00 USD | 691,680,000.00 USD | 2,600,000.00 USD | 2,580,000.00 USD | 252,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2432.80` | 1,740,000,000.00 USD | 1,740,000,000.00 USD | 15,460,000.00 USD | 11,210,000.00 USD | 5,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2433.80` | 696,810,000.00 USD | 696,810,000.00 USD | 2,080,000.00 USD | 565,750.00 USD | 2,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 7,920,000.00 USD | 26,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2435.60` | 1,780,000,000.00 USD | 1,780,000,000.00 USD | 20,760,000.00 USD | 13,900,000.00 USD | 12,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2436.30` | 699,910,000.00 USD | 699,910,000.00 USD | 2,290,000.00 USD | 475,290.00 USD | 339,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2438.40` | 1,840,000,000.00 USD | 1,840,000,000.00 USD | 16,830,000.00 USD | 21,000,000.00 USD | 14,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2438.80` | 701,340,000.00 USD | 701,340,000.00 USD | 304,760.00 USD | 641,280.00 USD | 476,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2441.20` | 1,870,000,000.00 USD | 1,870,000,000.00 USD | 15,870,000.00 USD | 6,990,000.00 USD | 10,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2441.30` | 706,480,000.00 USD | 706,480,000.00 USD | 2,360,000.00 USD | 2,020,000.00 USD | 767,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2443.80` | 708,430,000.00 USD | 708,430,000.00 USD | 50,900.00 USD | 556,820.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2444.00` | 1,900,000,000.00 USD | 1,900,000,000.00 USD | 5,220,000.00 USD | 13,460,000.00 USD | 7,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 158,630.00 USD | 26,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2446.30` | 712,190,000.00 USD | 712,190,000.00 USD | 1,840,000.00 USD | 675,040.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2446.80` | 1,930,000,000.00 USD | 1,930,000,000.00 USD | 11,620,000.00 USD | 7,020,000.00 USD | 18,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2448.80` | 716,330,000.00 USD | 716,330,000.00 USD | 387,180.00 USD | 1,500,000.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2449.60` | 1,980,000,000.00 USD | 1,980,000,000.00 USD | 18,130,000.00 USD | 10,300,000.00 USD | 14,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2451.30` | 725,960,000.00 USD | 725,960,000.00 USD | 2,700,000.00 USD | 3,090,000.00 USD | 3,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2452.40` | 2,000,000,000.00 USD | 2,000,000,000.00 USD | 7,700,000.00 USD | 8,980,000.00 USD | 7,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2453.80` | 736,710,000.00 USD | 736,710,000.00 USD | 5,060,000.00 USD | 3,010,000.00 USD | 2,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 98,850.00 USD | 26,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2455.20` | 2,020,000,000.00 USD | 2,020,000,000.00 USD | 6,850,000.00 USD | 5,830,000.00 USD | 3,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2456.30` | 743,500,000.00 USD | 743,500,000.00 USD | 1,340,000.00 USD | 3,130,000.00 USD | 2,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2458.00` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 11,170,000.00 USD | 11,200,000.00 USD | 13,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2458.80` | 747,480,000.00 USD | 747,480,000.00 USD | 2,400,000.00 USD | 1,250,000.00 USD | 322,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2460.80` | 2,080,000,000.00 USD | 2,080,000,000.00 USD | 7,010,000.00 USD | 10,680,000.00 USD | 9,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2461.30` | 749,420,000.00 USD | 749,420,000.00 USD | 470,530.00 USD | 46,520.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2463.60` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 10,390,000.00 USD | 9,560,000.00 USD | 5,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2463.80` | 753,390,000.00 USD | 753,390,000.00 USD | 352,200.00 USD | 2,790,000.00 USD | 829,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 79,760.00 USD | 27,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2466.30` | 754,330,000.00 USD | 754,330,000.00 USD | 468,790.00 USD | 463,300.00 USD | 5,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2466.40` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 4,790,000.00 USD | 2,080,000.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2468.80` | 755,730,000.00 USD | 755,730,000.00 USD | 0.00 USD | 998,350.00 USD | 399,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2469.20` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 2,490,000.00 USD | 3,570,000.00 USD | 408,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2471.30` | 758,760,000.00 USD | 758,760,000.00 USD | 1,390,000.00 USD | 883,290.00 USD | 764,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2472.00` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 3,090,000.00 USD | 2,760,000.00 USD | 814,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2473.80` | 759,000,000.00 USD | 759,000,000.00 USD | 0.00 USD | 232,740.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2474.80` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 5,400,000.00 USD | 866,790.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 836,210.00 USD | 27,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2476.30` | 759,750,000.00 USD | 759,750,000.00 USD | 738,780.00 USD | 0.00 USD | 7,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2477.60` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 790,860.00 USD | 3,880,000.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2478.80` | 759,790,000.00 USD | 759,790,000.00 USD | 0.00 USD | 41,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2480.40` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 2,110,000.00 USD | 1,740,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2481.30` | 760,340,000.00 USD | 760,340,000.00 USD | 0.00 USD | 27,720.00 USD | 518,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2483.20` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 1,210,000.00 USD | 1,190,000.00 USD | 77,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2483.80` | 760,960,000.00 USD | 760,960,000.00 USD | 628,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 2,000,000.00 USD | 29,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2486.00` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 49,690.00 USD | 51,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2488.80` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 977,620.00 USD | 857,130.00 USD | 101,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2491.60` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 1,780,000.00 USD | 2,470,000.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2494.40` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 1,470,000.00 USD | 2,730,000.00 USD | 6,820,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 886,080.00 USD | 30,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2497.20` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 3,640,000.00 USD | 3,570,000.00 USD | 4,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2500.00` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 1,110,000.00 USD | 2,430,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2502.80` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 110,450.00 USD | 1,430,000.00 USD | 170,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 120,200.00 USD | 30,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2505.60` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 3,200,000.00 USD | 2,320,000.00 USD | 59,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2508.40` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 1,810,000.00 USD | 1,270,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2511.20` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 1,900,000.00 USD | 3,230,000.00 USD | 2,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2514.00` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 776,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 142,620.00 USD | 31,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2516.80` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 97,050.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2519.60` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2521.30` | 761,200,000.00 USD | 761,200,000.00 USD | 80,610.00 USD | 61,830.00 USD | 90,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2522.40` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 1,050,000.00 USD | 0.00 USD | 945,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2523.80` | 761,650,000.00 USD | 761,650,000.00 USD | 421,540.00 USD | 0.00 USD | 30,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 1,070,000.00 USD | 32,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2525.20` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 307,040.00 USD | 224,130.00 USD | 200,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2526.30` | 761,730,000.00 USD | 761,730,000.00 USD | 0.00 USD | 57,450.00 USD | 23,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2528.00` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 1,580,000.00 USD | 1,690,000.00 USD | 727,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2528.80` | 763,420,000.00 USD | 763,420,000.00 USD | 583,810.00 USD | 645,910.00 USD | 464,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2530.80` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 2,080,000.00 USD | 1,110,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2531.30` | 763,840,000.00 USD | 763,840,000.00 USD | 411,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2533.60` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 2,680,000.00 USD | 2,100,000.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2533.80` | 764,290,000.00 USD | 764,290,000.00 USD | 394,310.00 USD | 41,990.00 USD | 18,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2535.00` | 1,310,000.00 USD | 33,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2536.30` | 767,220,000.00 USD | 767,220,000.00 USD | 1,200,000.00 USD | 656,520.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2536.40` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 3,670,000.00 USD | 2,850,000.00 USD | 2,740,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2538.80` | 771,200,000.00 USD | 771,200,000.00 USD | 1,640,000.00 USD | 738,070.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2539.20` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 2,620,000.00 USD | 2,470,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2541.30` | 772,580,000.00 USD | 772,580,000.00 USD | 692,360.00 USD | 619,310.00 USD | 69,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2542.00` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 3,400,000.00 USD | 2,740,000.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2543.80` | 774,590,000.00 USD | 774,590,000.00 USD | 937,360.00 USD | 1,060,000.00 USD | 14,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2544.80` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 2,170,000.00 USD | 1,830,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2545.00` | 6,130,000.00 USD | 39,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2546.30` | 777,920,000.00 USD | 777,920,000.00 USD | 1,370,000.00 USD | 1,400,000.00 USD | 565,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2547.60` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 2,380,000.00 USD | 938,680.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2548.80` | 779,790,000.00 USD | 779,790,000.00 USD | 705,770.00 USD | 714,090.00 USD | 453,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2550.40` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 2,920,000.00 USD | 2,690,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2551.30` | 782,540,000.00 USD | 782,540,000.00 USD | 1,340,000.00 USD | 983,350.00 USD | 423,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2553.20` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 2,590,000.00 USD | 788,360.00 USD | 2,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2553.80` | 783,450,000.00 USD | 783,450,000.00 USD | 669,670.00 USD | 220,540.00 USD | 21,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2555.00` | 924,540.00 USD | 40,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2556.00` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 2,760,000.00 USD | 255,750.00 USD | 5,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2556.30` | 785,320,000.00 USD | 785,320,000.00 USD | 754,830.00 USD | 469,640.00 USD | 644,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2558.80` | 787,730,000.00 USD | 787,730,000.00 USD | 1,250,000.00 USD | 468,930.00 USD | 696,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2558.80` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 3,850,000.00 USD | 1,640,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2561.30` | 791,290,000.00 USD | 791,290,000.00 USD | 1,100,000.00 USD | 886,200.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2561.60` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 2,780,000.00 USD | 1,960,000.00 USD | 785,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2563.80` | 793,040,000.00 USD | 793,040,000.00 USD | 463,350.00 USD | 975,880.00 USD | 309,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2564.40` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 1,800,000.00 USD | 1,780,000.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2565.00` | 3,420,000.00 USD | 43,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2566.30` | 793,270,000.00 USD | 793,270,000.00 USD | 172,210.00 USD | 44,780.00 USD | 11,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2567.20` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 575,630.00 USD | 1,560,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2568.80` | 794,000,000.00 USD | 794,000,000.00 USD | 162,270.00 USD | 106,440.00 USD | 466,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2570.00` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 125,250.00 USD | 290,680.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2571.30` | 795,330,000.00 USD | 795,330,000.00 USD | 957,520.00 USD | 360,840.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2572.80` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2573.80` | 796,400,000.00 USD | 796,400,000.00 USD | 63,920.00 USD | 493,800.00 USD | 510,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2575.00` | 12,110,000.00 USD | 56,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2575.60` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 2,180,000.00 USD | 344,620.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2576.30` | 796,880,000.00 USD | 796,880,000.00 USD | 482,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2578.40` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 734,040.00 USD | 1,480,000.00 USD | 1,750,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2581.20` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 3,870,000.00 USD | 912,130.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2584.00` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 146,630.00 USD | 1,490,000.00 USD | 3,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2585.00` | 26,480,000.00 USD | 82,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2586.80` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 1,900,000.00 USD | 1,970,000.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2589.60` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 2,840,000.00 USD | 446,810.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2592.40` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 2,340,000.00 USD | 1,280,000.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2595.00` | 8,300,000.00 USD | 90,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2595.20` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 452,020.00 USD | 569,790.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2598.00` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 2,280,000.00 USD | 1,630,000.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2600.80` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 931,390.00 USD | 1,960,000.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2603.60` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 1,600,000.00 USD | 1,580,000.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2605.00` | 534,220.00 USD | 91,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2606.40` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 1,480,000.00 USD | 229,360.00 USD | 320,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2609.20` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2612.00` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 770,330.00 USD | 608,060.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2614.80` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 1,060,000.00 USD | 1,000,000.00 USD | 409,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2615.00` | 926,240.00 USD | 92,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2617.60` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 1,550,000.00 USD | 209,240.00 USD | 392,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2620.40` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 47,360.00 USD | 1,120,000.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2623.20` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 418,600.00 USD | 410,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2625.00` | 637,700.00 USD | 92,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2635.00` | 99,330.00 USD | 92,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2645.00` | 681,840.00 USD | 93,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2655.00` | 35,210,000.00 USD | 128,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2665.00` | 62,560.00 USD | 128,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2675.00` | 310,460.00 USD | 129,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2685.00` | 7,320,000.00 USD | 136,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2695.00` | 395,990.00 USD | 136,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2705.00` | 29,550,000.00 USD | 166,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2715.00` | 16,020,000.00 USD | 182,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2725.00` | 454,310.00 USD | 183,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2735.00` | 3,610,000.00 USD | 186,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2745.00` | 1,010,000.00 USD | 187,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2755.00` | 735,710.00 USD | 188,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2765.00` | 149,020.00 USD | 188,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2775.00` | 334,480.00 USD | 188,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2785.00` | 6,950,000.00 USD | 195,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2795.00` | 228,090.00 USD | 196,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2805.00` | 595,820.00 USD | 196,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2815.00` | 286,110.00 USD | 196,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2825.00` | 58,720.00 USD | 196,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2835.00` | 3,350,000.00 USD | 200,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2845.00` | 2,290,000.00 USD | 202,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2855.00` | 253,200.00 USD | 202,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2865.00` | 31,290,000.00 USD | 234,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2875.00` | 36,840,000.00 USD | 270,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2885.00` | 4,650,000.00 USD | 275,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2895.00` | 645,080.00 USD | 276,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2905.00` | 736,740.00 USD | 277,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2915.00` | 183,180.00 USD | 277,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2925.00` | 26,630,000.00 USD | 303,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2935.00` | 27,250.00 USD | 303,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2945.00` | 919,870.00 USD | 304,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2955.00` | 7,810,000.00 USD | 312,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2965.00` | 20,840,000.00 USD | 333,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2975.00` | 1,330,000.00 USD | 334,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2985.00` | 955,840.00 USD | 335,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2995.00` | 989,880.00 USD | 336,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3005.00` | 2,230,000.00 USD | 338,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3015.00` | 2,400,000.00 USD | 341,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3025.00` | 2,440,000.00 USD | 343,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3035.00` | 9,130,000.00 USD | 352,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3045.00` | 14,980,000.00 USD | 367,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3055.00` | 4,010,000.00 USD | 371,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3065.00` | 329,030.00 USD | 372,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3075.00` | 4,010,000.00 USD | 376,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3085.00` | 1,470,000.00 USD | 377,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3095.00` | 548,480.00 USD | 378,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3105.00` | 102,180.00 USD | 378,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3115.00` | 390,660.00 USD | 378,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3125.00` | 150,120.00 USD | 378,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3135.00` | 1,720,000.00 USD | 380,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3145.00` | 284,010.00 USD | 380,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3155.00` | 6,160,000.00 USD | 387,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3165.00` | 28,620.00 USD | 387,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3175.00` | 659,480.00 USD | 387,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3185.00` | 800,040.00 USD | 388,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3195.00` | 3,800,000.00 USD | 392,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3205.00` | 57,210.00 USD | 392,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3215.00` | 5,690,000.00 USD | 398,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3225.00` | 231,490.00 USD | 398,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3235.00` | 8,580,000.00 USD | 406,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3245.00` | 192,580.00 USD | 407,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3255.00` | 362,380.00 USD | 407,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3265.00` | 6,720.00 USD | 407,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3275.00` | 39,320.00 USD | 407,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3285.00` | 8,570,000.00 USD | 416,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3295.00` | 1,340,000.00 USD | 417,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3305.00` | 10,180.00 USD | 417,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3315.00` | 11,650,000.00 USD | 429,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3325.00` | 31,050.00 USD | 429,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3335.00` | 55,420.00 USD | 429,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3345.00` | 790,070.00 USD | 429,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3355.00` | 65,150,000.00 USD | 495,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3365.00` | 542,970.00 USD | 495,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3375.00` | 602,790.00 USD | 496,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3385.00` | 156,030.00 USD | 496,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3395.00` | 240,880.00 USD | 496,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3405.00` | 106,090.00 USD | 496,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3415.00` | 34,350.00 USD | 496,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3425.00` | 15,150,000.00 USD | 511,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3435.00` | 158,730.00 USD | 512,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3445.00` | 5,200,000.00 USD | 517,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3455.00` | 685,470.00 USD | 517,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3465.00` | 377,080.00 USD | 518,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3475.00` | 1,260,000.00 USD | 519,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3485.00` | 8,230.00 USD | 519,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3495.00` | 1,120,000.00 USD | 520,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3505.00` | 206,250.00 USD | 520,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3515.00` | 35,780.00 USD | 520,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3525.00` | 128,540.00 USD | 521,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3535.00` | 22,000.00 USD | 521,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3545.00` | 7,150,000.00 USD | 528,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3555.00` | 143,930.00 USD | 528,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3565.00` | 42,110.00 USD | 528,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3575.00` | 95,920.00 USD | 528,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3585.00` | 490,870.00 USD | 529,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3595.00` | 550,480.00 USD | 529,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3605.00` | 90,010.00 USD | 529,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3615.00` | 4,000,000.00 USD | 533,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3625.00` | 108,950,000.00 USD | 642,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3635.00` | 2,320,000.00 USD | 644,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3645.00` | 218,570.00 USD | 645,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3655.00` | 117,810.00 USD | 645,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3665.00` | 216,740.00 USD | 645,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3675.00` | 872,350.00 USD | 646,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3685.00` | 8,200,000.00 USD | 654,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3695.00` | 1,720,000.00 USD | 656,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3705.00` | 731,540.00 USD | 657,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3715.00` | 459,630.00 USD | 657,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3725.00` | 259,140.00 USD | 657,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3735.00` | 34,760,000.00 USD | 692,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3745.00` | 863,120.00 USD | 693,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3755.00` | 13,470,000.00 USD | 706,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3765.00` | 66,550.00 USD | 706,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3775.00` | 367,220.00 USD | 707,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3785.00` | 39,580.00 USD | 707,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3795.00` | 81,940.00 USD | 707,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3805.00` | 472,390.00 USD | 707,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3815.00` | 2,690.00 USD | 707,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3825.00` | 328,880.00 USD | 708,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3835.00` | 408,860,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3845.00` | 2,160,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3855.00` | 176,530.00 USD | 1,120,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3865.00` | 1,030,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3875.00` | 12,320.00 USD | 1,120,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3885.00` | 17,110,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3895.00` | 100,530.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3905.00` | 616,790.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3915.00` | 567,550.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3925.00` | 355,780.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3935.00` | 57,480.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3945.00` | 246,510.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3955.00` | 3,410,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3965.00` | 566,950.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3975.00` | 93,670,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3985.00` | 123,680.00 USD | 1,240,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3995.00` | 30,680,000.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4005.00` | 106,160.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4015.00` | 146,060.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4025.00` | 247,410.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4035.00` | 660,940.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4045.00` | 70,130,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4055.00` | 538,130.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4065.00` | 2,770,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4075.00` | 3,490,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4085.00` | 40,820.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4095.00` | 81,900.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4105.00` | 93,840.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4115.00` | 1,250.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4135.00` | 984,160.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4145.00` | 401,910.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4155.00` | 531,930.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4165.00` | 257,470.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4185.00` | 41,230.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4195.00` | 4,060,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4205.00` | 44,500.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4215.00` | 12,850.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4225.00` | 93,870.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4235.00` | 18,650,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4245.00` | 155,690.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4255.00` | 121,540.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4265.00` | 68,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4275.00` | 1,070.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4285.00` | 17,280,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4295.00` | 63,150.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4305.00` | 200,540.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4315.00` | 6,590.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4325.00` | 5,830.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4335.00` | 114,010.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4355.00` | 22,600.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4365.00` | 591,120.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4375.00` | 2,160,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4385.00` | 849,910.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4395.00` | 286,590,000.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4405.00` | 102,320.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4415.00` | 471,100.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4425.00` | 259,220.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4435.00` | 1,940,000.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4445.00` | 446,190.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4455.00` | 1,380,000.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4465.00` | 319,690.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4475.00` | 33,190.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4485.00` | 30,710.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4495.00` | 24,840.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4505.00` | 99,370.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4515.00` | 404,790.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4525.00` | 1,080,000.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4535.00` | 3,360,000.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4545.00` | 17,760.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4555.00` | 1,030,000.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4565.00` | 95,220.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4575.00` | 41,230.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4585.00` | 1,160,000.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4595.00` | 187,730.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4605.00` | 37,010.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4615.00` | 100,540.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4625.00` | 412,820.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4635.00` | 236,720.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4645.00` | 170,520.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4655.00` | 445,590.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4665.00` | 29,990.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `465.00` | 871,470,000.00 USD | 0.00 USD | 8,890.00 USD | `-80.09%` | `19.12` |
| `Live` | `Long` | `475.00` | 871,460,000.00 USD | 0.00 USD | 18,650.00 USD | `-79.67%` | `39.27` |
| `Live` | `Long` | `485.00` | 871,440,000.00 USD | 0.00 USD | 10,700.00 USD | `-79.24%` | `22.06` |
| `Live` | `Long` | `495.00` | 871,430,000.00 USD | 0.00 USD | 3,170.00 USD | `-78.81%` | `6.41` |
| `Live` | `Long` | `505.00` | 871,430,000.00 USD | 0.00 USD | 40,200.00 USD | `-78.38%` | `79.61` |
| `Live` | `Long` | `515.00` | 871,390,000.00 USD | 0.00 USD | 8,310.00 USD | `-77.95%` | `16.13` |
| `Live` | `Long` | `525.00` | 871,380,000.00 USD | 0.00 USD | 5,110.00 USD | `-77.53%` | `9.73` |
| `Live` | `Long` | `535.00` | 871,370,000.00 USD | 0.00 USD | 16,270.00 USD | `-77.10%` | `30.42` |
| `Live` | `Long` | `545.00` | 871,360,000.00 USD | 0.00 USD | 22,070.00 USD | `-76.67%` | `40.50` |
| `Live` | `Long` | `555.00` | 871,330,000.00 USD | 0.00 USD | 144,570.00 USD | `-76.24%` | `260.49` |
| `Live` | `Long` | `565.00` | 871,190,000.00 USD | 0.00 USD | 113,200.00 USD | `-75.81%` | `200.35` |
| `Live` | `Long` | `575.00` | 871,080,000.00 USD | 0.00 USD | 17,490.00 USD | `-75.38%` | `30.42` |
| `Live` | `Long` | `585.00` | 871,060,000.00 USD | 0.00 USD | 396,730.00 USD | `-74.96%` | `678.17` |
| `Live` | `Long` | `595.00` | 870,660,000.00 USD | 0.00 USD | 8,390.00 USD | `-74.53%` | `14.10` |
| `Live` | `Long` | `605.00` | 870,650,000.00 USD | 0.00 USD | 21,280.00 USD | `-74.10%` | `35.17` |
| `Live` | `Long` | `615.00` | 870,630,000.00 USD | 0.00 USD | 90,210.00 USD | `-73.67%` | `146.69` |
| `Live` | `Long` | `625.00` | 870,540,000.00 USD | 0.00 USD | 12,690.00 USD | `-73.24%` | `20.30` |
| `Live` | `Long` | `635.00` | 870,530,000.00 USD | 0.00 USD | 2,240.00 USD | `-72.82%` | `3.52` |
| `Live` | `Long` | `645.00` | 870,530,000.00 USD | 0.00 USD | 4,850.00 USD | `-72.39%` | `7.52` |
| `Live` | `Long` | `655.00` | 870,520,000.00 USD | 0.00 USD | 54,920.00 USD | `-71.96%` | `83.84` |
| `Live` | `Long` | `665.00` | 870,470,000.00 USD | 0.00 USD | 99,080.00 USD | `-71.53%` | `149.00` |
| `Live` | `Long` | `675.00` | 870,370,000.00 USD | 0.00 USD | 123,080.00 USD | `-71.10%` | `182.34` |
| `Live` | `Long` | `685.00` | 870,250,000.00 USD | 0.00 USD | 35,700.00 USD | `-70.68%` | `52.11` |
| `Live` | `Long` | `695.00` | 870,210,000.00 USD | 0.00 USD | 107,880.00 USD | `-70.25%` | `155.22` |
| `Live` | `Long` | `705.00` | 870,100,000.00 USD | 0.00 USD | 4,070.00 USD | `-69.82%` | `5.77` |
| `Live` | `Long` | `715.00` | 870,100,000.00 USD | 0.00 USD | 15,690.00 USD | `-69.39%` | `21.95` |
| `Live` | `Long` | `725.00` | 870,080,000.00 USD | 0.00 USD | 383,190.00 USD | `-68.96%` | `528.54` |
| `Live` | `Long` | `735.00` | 869,700,000.00 USD | 0.00 USD | 52,700.00 USD | `-68.54%` | `71.71` |
| `Live` | `Long` | `745.00` | 869,650,000.00 USD | 0.00 USD | 1,820.00 USD | `-68.11%` | `2.44` |
| `Live` | `Long` | `755.00` | 869,650,000.00 USD | 0.00 USD | 27,110.00 USD | `-67.68%` | `35.91` |
| `Live` | `Long` | `765.00` | 869,620,000.00 USD | 0.00 USD | 87,060.00 USD | `-67.25%` | `113.81` |
| `Live` | `Long` | `775.00` | 869,530,000.00 USD | 0.00 USD | 1,710,000.00 USD | `-66.82%` | `2,202.45` |
| `Live` | `Long` | `785.00` | 867,820,000.00 USD | 0.00 USD | 62,570.00 USD | `-66.39%` | `79.71` |
| `Live` | `Long` | `795.00` | 867,760,000.00 USD | 0.00 USD | 468,490.00 USD | `-65.97%` | `589.29` |
| `Live` | `Long` | `805.00` | 867,290,000.00 USD | 0.00 USD | 2,400.00 USD | `-65.54%` | `2.99` |
| `Live` | `Long` | `815.00` | 867,290,000.00 USD | 0.00 USD | 444,920.00 USD | `-65.11%` | `545.91` |
| `Live` | `Long` | `825.00` | 866,850,000.00 USD | 0.00 USD | 93,820.00 USD | `-64.68%` | `113.72` |
| `Live` | `Long` | `835.00` | 866,750,000.00 USD | 0.00 USD | 264,560.00 USD | `-64.25%` | `316.84` |
| `Live` | `Long` | `845.00` | 866,490,000.00 USD | 0.00 USD | 19,780.00 USD | `-63.83%` | `23.41` |
| `Live` | `Long` | `855.00` | 866,470,000.00 USD | 0.00 USD | 5,300.00 USD | `-63.40%` | `6.20` |
| `Live` | `Long` | `865.00` | 866,460,000.00 USD | 0.00 USD | 3,780,000.00 USD | `-62.97%` | `4,364.25` |
| `Live` | `Long` | `875.00` | 862,690,000.00 USD | 0.00 USD | 35,210.00 USD | `-62.54%` | `40.24` |
| `Live` | `Long` | `885.00` | 862,650,000.00 USD | 0.00 USD | 422,370.00 USD | `-62.11%` | `477.25` |
| `Live` | `Long` | `895.00` | 862,230,000.00 USD | 0.00 USD | 28,550.00 USD | `-61.69%` | `31.90` |
| `Live` | `Long` | `905.00` | 862,200,000.00 USD | 0.00 USD | 77,340.00 USD | `-61.26%` | `85.46` |
| `Live` | `Long` | `915.00` | 862,120,000.00 USD | 0.00 USD | 233,800.00 USD | `-60.83%` | `255.52` |
| `Live` | `Long` | `925.00` | 861,890,000.00 USD | 0.00 USD | 131,200.00 USD | `-60.40%` | `141.84` |
| `Live` | `Long` | `935.00` | 861,760,000.00 USD | 0.00 USD | 31,510.00 USD | `-59.97%` | `33.70` |
| `Live` | `Long` | `945.00` | 861,730,000.00 USD | 0.00 USD | 23,750.00 USD | `-59.55%` | `25.14` |
| `Live` | `Long` | `955.00` | 861,700,000.00 USD | 0.00 USD | 1,140,000.00 USD | `-59.12%` | `1,194.14` |
| `Live` | `Long` | `965.00` | 860,560,000.00 USD | 0.00 USD | 23,360.00 USD | `-58.69%` | `24.21` |
| `Live` | `Long` | `975.00` | 860,540,000.00 USD | 0.00 USD | 74,510.00 USD | `-58.26%` | `76.42` |
| `Live` | `Long` | `985.00` | 860,470,000.00 USD | 0.00 USD | 21,080.00 USD | `-57.83%` | `21.41` |
| `Live` | `Long` | `995.00` | 860,440,000.00 USD | 0.00 USD | 54,120.00 USD | `-57.40%` | `54.39` |
| `Live` | `Long` | `1005.00` | 860,390,000.00 USD | 0.00 USD | 7,080,000.00 USD | `-56.98%` | `7,046.92` |
| `Live` | `Long` | `1015.00` | 853,310,000.00 USD | 0.00 USD | 63,250.00 USD | `-56.55%` | `62.32` |
| `Live` | `Long` | `1025.00` | 853,240,000.00 USD | 0.00 USD | 122,850.00 USD | `-56.12%` | `119.85` |
| `Live` | `Long` | `1035.00` | 853,120,000.00 USD | 0.00 USD | 29,510.00 USD | `-55.69%` | `28.51` |
| `Live` | `Long` | `1045.00` | 853,090,000.00 USD | 0.00 USD | 1,900,000.00 USD | `-55.26%` | `1,820.68` |
| `Live` | `Long` | `1055.00` | 851,190,000.00 USD | 0.00 USD | 31,060.00 USD | `-54.84%` | `29.44` |
| `Live` | `Long` | `1065.00` | 851,160,000.00 USD | 0.00 USD | 1,500,000.00 USD | `-54.41%` | `1,406.95` |
| `Live` | `Long` | `1075.00` | 849,660,000.00 USD | 0.00 USD | 872,800.00 USD | `-53.98%` | `811.91` |
| `Live` | `Long` | `1085.00` | 848,790,000.00 USD | 0.00 USD | 35,080.00 USD | `-53.55%` | `32.34` |
| `Live` | `Long` | `1095.00` | 848,750,000.00 USD | 0.00 USD | 117,660.00 USD | `-53.12%` | `107.45` |
| `Live` | `Long` | `1105.00` | 848,630,000.00 USD | 0.00 USD | 144,030.00 USD | `-52.70%` | `130.35` |
| `Live` | `Long` | `1115.00` | 848,490,000.00 USD | 0.00 USD | 145,270.00 USD | `-52.27%` | `130.29` |
| `Live` | `Long` | `1125.00` | 848,350,000.00 USD | 0.00 USD | 1,760,000.00 USD | `-51.84%` | `1,561.76` |
| `Live` | `Long` | `1135.00` | 846,590,000.00 USD | 0.00 USD | 76,690.00 USD | `-51.41%` | `67.57` |
| `Live` | `Long` | `1145.00` | 846,510,000.00 USD | 0.00 USD | 217,980.00 USD | `-50.98%` | `190.38` |
| `Live` | `Long` | `1155.00` | 846,290,000.00 USD | 0.00 USD | 345,860.00 USD | `-50.56%` | `299.45` |
| `Live` | `Long` | `1165.00` | 845,950,000.00 USD | 0.00 USD | 14,960.00 USD | `-50.13%` | `12.84` |
| `Live` | `Long` | `1175.00` | 845,930,000.00 USD | 0.00 USD | 337,640.00 USD | `-49.70%` | `287.35` |
| `Live` | `Long` | `1185.00` | 845,600,000.00 USD | 0.00 USD | 123,330.00 USD | `-49.27%` | `104.07` |
| `Live` | `Long` | `1195.00` | 845,470,000.00 USD | 0.00 USD | 305,420.00 USD | `-48.84%` | `255.58` |
| `Live` | `Long` | `1205.00` | 845,170,000.00 USD | 0.00 USD | 1,230,000.00 USD | `-48.41%` | `1,024.18` |
| `Live` | `Long` | `1215.00` | 843,930,000.00 USD | 0.00 USD | 118,830.00 USD | `-47.99%` | `97.80` |
| `Live` | `Long` | `1225.00` | 843,810,000.00 USD | 0.00 USD | 250,230.00 USD | `-47.56%` | `204.27` |
| `Live` | `Long` | `1235.00` | 843,560,000.00 USD | 0.00 USD | 247,580.00 USD | `-47.13%` | `200.47` |
| `Live` | `Long` | `1245.00` | 843,320,000.00 USD | 0.00 USD | 11,610,000.00 USD | `-46.70%` | `9,323.05` |
| `Live` | `Long` | `1255.00` | 831,710,000.00 USD | 0.00 USD | 439,960.00 USD | `-46.27%` | `350.56` |
| `Live` | `Long` | `1265.00` | 831,270,000.00 USD | 0.00 USD | 1,550,000.00 USD | `-45.85%` | `1,225.28` |
| `Live` | `Long` | `1275.00` | 829,720,000.00 USD | 0.00 USD | 94,640.00 USD | `-45.42%` | `74.22` |
| `Live` | `Long` | `1285.00` | 829,620,000.00 USD | 0.00 USD | 16,260,000.00 USD | `-44.99%` | `12,655.90` |
| `Live` | `Long` | `1295.00` | 813,360,000.00 USD | 0.00 USD | 413,680.00 USD | `-44.56%` | `319.45` |
| `Live` | `Long` | `1305.00` | 812,950,000.00 USD | 0.00 USD | 160,590.00 USD | `-44.13%` | `123.06` |
| `Live` | `Long` | `1315.00` | 812,790,000.00 USD | 0.00 USD | 92,010.00 USD | `-43.71%` | `69.97` |
| `Live` | `Long` | `1325.00` | 812,690,000.00 USD | 0.00 USD | 565,280.00 USD | `-43.28%` | `426.62` |
| `Live` | `Long` | `1335.00` | 812,130,000.00 USD | 0.00 USD | 410,380.00 USD | `-42.85%` | `307.40` |
| `Live` | `Long` | `1345.00` | 811,720,000.00 USD | 0.00 USD | 569,800.00 USD | `-42.42%` | `423.64` |
| `Live` | `Long` | `1355.00` | 811,150,000.00 USD | 0.00 USD | 112,370.00 USD | `-41.99%` | `82.93` |
| `Live` | `Long` | `1365.00` | 811,040,000.00 USD | 0.00 USD | 7,800,000.00 USD | `-41.57%` | `5,716.11` |
| `Live` | `Long` | `1375.00` | 803,230,000.00 USD | 0.00 USD | 343,870.00 USD | `-41.14%` | `250.09` |
| `Live` | `Long` | `1385.00` | 802,890,000.00 USD | 0.00 USD | 136,090.00 USD | `-40.71%` | `98.26` |
| `Live` | `Long` | `1395.00` | 802,750,000.00 USD | 0.00 USD | 321,060.00 USD | `-40.28%` | `230.15` |
| `Live` | `Long` | `1405.00` | 802,430,000.00 USD | 0.00 USD | 25,310,000.00 USD | `-39.85%` | `18,011.40` |
| `Live` | `Long` | `1415.00` | 777,130,000.00 USD | 0.00 USD | 60,360.00 USD | `-39.42%` | `42.65` |
| `Live` | `Long` | `1425.00` | 777,070,000.00 USD | 0.00 USD | 1,110,000.00 USD | `-39.00%` | `776.18` |
| `Live` | `Long` | `1435.00` | 775,960,000.00 USD | 0.00 USD | 14,830,000.00 USD | `-38.57%` | `10,334.64` |
| `Live` | `Long` | `1445.00` | 761,130,000.00 USD | 0.00 USD | 164,980.00 USD | `-38.14%` | `114.17` |
| `Live` | `Long` | `1455.00` | 760,970,000.00 USD | 0.00 USD | 7,350,000.00 USD | `-37.71%` | `5,050.47` |
| `Live` | `Long` | `1465.00` | 753,620,000.00 USD | 0.00 USD | 413,140.00 USD | `-37.28%` | `282.01` |
| `Live` | `Long` | `1475.00` | 753,200,000.00 USD | 0.00 USD | 2,070,000.00 USD | `-36.86%` | `1,400.19` |
| `Live` | `Long` | `1485.00` | 751,140,000.00 USD | 0.00 USD | 5,120,000.00 USD | `-36.43%` | `3,448.89` |
| `Live` | `Long` | `1495.00` | 746,020,000.00 USD | 0.00 USD | 510,410.00 USD | `-36.00%` | `341.41` |
| `Live` | `Long` | `1505.00` | 745,510,000.00 USD | 0.00 USD | 457,390.00 USD | `-35.57%` | `303.91` |
| `Live` | `Long` | `1515.00` | 745,050,000.00 USD | 0.00 USD | 18,940,000.00 USD | `-35.14%` | `12,503.85` |
| `Live` | `Long` | `1525.00` | 726,110,000.00 USD | 0.00 USD | 18,620,000.00 USD | `-34.72%` | `12,210.54` |
| `Live` | `Long` | `1535.00` | 707,490,000.00 USD | 0.00 USD | 646,040.00 USD | `-34.29%` | `420.87` |
| `Live` | `Long` | `1545.00` | 706,840,000.00 USD | 0.00 USD | 27,510,000.00 USD | `-33.86%` | `17,804.83` |
| `Live` | `Long` | `1555.00` | 679,330,000.00 USD | 0.00 USD | 974,100.00 USD | `-33.43%` | `626.43` |
| `Live` | `Long` | `1565.00` | 678,360,000.00 USD | 0.00 USD | 264,610.00 USD | `-33.00%` | `169.08` |
| `Live` | `Long` | `1575.00` | 678,090,000.00 USD | 0.00 USD | 204,780.00 USD | `-32.58%` | `130.02` |
| `Live` | `Long` | `1585.00` | 677,890,000.00 USD | 0.00 USD | 262,710.00 USD | `-32.15%` | `165.75` |
| `Live` | `Long` | `1595.00` | 677,620,000.00 USD | 0.00 USD | 7,660,000.00 USD | `-31.72%` | `4,801.14` |
| `Live` | `Long` | `1605.00` | 669,970,000.00 USD | 0.00 USD | 18,380,000.00 USD | `-31.29%` | `11,453.55` |
| `Live` | `Long` | `1615.00` | 651,580,000.00 USD | 0.00 USD | 278,310.00 USD | `-30.86%` | `172.33` |
| `Live` | `Long` | `1625.00` | 651,310,000.00 USD | 0.00 USD | 3,020,000.00 USD | `-30.43%` | `1,858.04` |
| `Live` | `Long` | `1635.00` | 648,290,000.00 USD | 0.00 USD | 18,260,000.00 USD | `-30.01%` | `11,168.96` |
| `Live` | `Long` | `1645.00` | 630,020,000.00 USD | 0.00 USD | 36,410,000.00 USD | `-29.58%` | `22,133.50` |
| `Live` | `Long` | `1655.00` | 593,620,000.00 USD | 0.00 USD | 997,270.00 USD | `-29.15%` | `602.58` |
| `Live` | `Long` | `1665.00` | 592,620,000.00 USD | 0.00 USD | 845,700.00 USD | `-28.72%` | `507.93` |
| `Live` | `Long` | `1675.00` | 591,770,000.00 USD | 0.00 USD | 11,660,000.00 USD | `-28.29%` | `6,958.37` |
| `Live` | `Long` | `1685.00` | 580,120,000.00 USD | 0.00 USD | 2,030,000.00 USD | `-27.87%` | `1,207.64` |
| `Live` | `Long` | `1695.00` | 578,080,000.00 USD | 0.00 USD | 444,640.00 USD | `-27.44%` | `262.33` |
| `Live` | `Long` | `1705.00` | 577,640,000.00 USD | 0.00 USD | 1,240,000.00 USD | `-27.01%` | `726.69` |
| `Live` | `Long` | `1715.00` | 576,400,000.00 USD | 0.00 USD | 11,040,000.00 USD | `-26.58%` | `6,437.84` |
| `Live` | `Long` | `1725.00` | 565,360,000.00 USD | 0.00 USD | 18,000,000.00 USD | `-26.15%` | `10,436.95` |
| `Live` | `Long` | `1735.00` | 547,350,000.00 USD | 0.00 USD | 18,130,000.00 USD | `-25.73%` | `10,448.55` |
| `Live` | `Long` | `1745.00` | 529,230,000.00 USD | 0.00 USD | 2,120,000.00 USD | `-25.30%` | `1,214.80` |
| `Live` | `Long` | `1755.00` | 527,110,000.00 USD | 0.00 USD | 968,460.00 USD | `-24.87%` | `551.83` |
| `Live` | `Long` | `1765.00` | 526,140,000.00 USD | 0.00 USD | 1,060,000.00 USD | `-24.44%` | `602.22` |
| `Live` | `Long` | `1775.00` | 525,070,000.00 USD | 0.00 USD | 14,310,000.00 USD | `-24.01%` | `8,061.27` |
| `Live` | `Long` | `1785.00` | 510,770,000.00 USD | 0.00 USD | 54,670,000.00 USD | `-23.59%` | `30,624.87` |
| `Live` | `Long` | `1795.00` | 456,100,000.00 USD | 0.00 USD | 337,900.00 USD | `-23.16%` | `188.25` |
| `Live` | `Long` | `1805.00` | 455,760,000.00 USD | 0.00 USD | 1,610,000.00 USD | `-22.73%` | `894.21` |
| `Live` | `Long` | `1815.00` | 454,150,000.00 USD | 0.00 USD | 4,520,000.00 USD | `-22.30%` | `2,488.29` |
| `Live` | `Long` | `1825.00` | 449,630,000.00 USD | 0.00 USD | 9,600,000.00 USD | `-21.87%` | `5,262.26` |
| `Live` | `Long` | `1835.00` | 440,030,000.00 USD | 0.00 USD | 1,310,000.00 USD | `-21.44%` | `713.43` |
| `Live` | `Long` | `1845.00` | 438,720,000.00 USD | 0.00 USD | 290,390.00 USD | `-21.02%` | `157.39` |
| `Live` | `Long` | `1855.00` | 438,430,000.00 USD | 0.00 USD | 1,020,000.00 USD | `-20.59%` | `548.92` |
| `Live` | `Long` | `1865.00` | 437,410,000.00 USD | 0.00 USD | 6,820,000.00 USD | `-20.16%` | `3,654.78` |
| `Live` | `Long` | `1875.00` | 430,590,000.00 USD | 0.00 USD | 5,580,000.00 USD | `-19.73%` | `2,974.98` |
| `Live` | `Long` | `1885.00` | 425,020,000.00 USD | 0.00 USD | 2,730,000.00 USD | `-19.30%` | `1,448.44` |
| `Live` | `Long` | `1895.00` | 422,290,000.00 USD | 0.00 USD | 5,510,000.00 USD | `-18.88%` | `2,905.61` |
| `Live` | `Long` | `1905.00` | 416,780,000.00 USD | 0.00 USD | 1,280,000.00 USD | `-18.45%` | `670.47` |
| `Live` | `Long` | `1915.00` | 415,500,000.00 USD | 0.00 USD | 30,800,000.00 USD | `-18.02%` | `16,082.67` |
| `Live` | `Long` | `1925.00` | 384,700,000.00 USD | 0.00 USD | 2,930,000.00 USD | `-17.59%` | `1,522.82` |
| `Live` | `Long` | `1935.00` | 381,770,000.00 USD | 0.00 USD | 1,570,000.00 USD | `-17.16%` | `810.91` |
| `Live` | `Long` | `1945.00` | 380,200,000.00 USD | 0.00 USD | 789,440.00 USD | `-16.74%` | `405.88` |
| `Live` | `Long` | `1955.00` | 379,410,000.00 USD | 0.00 USD | 3,430,000.00 USD | `-16.31%` | `1,754.10` |
| `Live` | `Long` | `1965.00` | 375,990,000.00 USD | 0.00 USD | 748,720.00 USD | `-15.88%` | `381.03` |
| `Live` | `Long` | `1975.00` | 375,240,000.00 USD | 0.00 USD | 6,210,000.00 USD | `-15.45%` | `3,146.47` |
| `Live` | `Long` | `1985.00` | 369,020,000.00 USD | 0.00 USD | 4,430,000.00 USD | `-15.02%` | `2,230.98` |
| `Live` | `Long` | `1995.00` | 364,590,000.00 USD | 0.00 USD | 926,340.00 USD | `-14.60%` | `464.33` |
| `Live` | `Long` | `2005.00` | 363,670,000.00 USD | 0.00 USD | 2,840,000.00 USD | `-14.17%` | `1,415.81` |
| `Live` | `Long` | `2015.00` | 360,830,000.00 USD | 0.00 USD | 3,290,000.00 USD | `-13.74%` | `1,631.09` |
| `Live` | `Long` | `2025.00` | 357,540,000.00 USD | 0.00 USD | 1,470,000.00 USD | `-13.31%` | `724.79` |
| `Live` | `Long` | `2035.00` | 356,070,000.00 USD | 0.00 USD | 1,050,000.00 USD | `-12.88%` | `516.68` |
| `Live` | `Long` | `2045.00` | 355,020,000.00 USD | 0.00 USD | 20,110,000.00 USD | `-12.45%` | `9,833.08` |
| `Live` | `Long` | `2055.00` | 334,910,000.00 USD | 0.00 USD | 4,320,000.00 USD | `-12.03%` | `2,103.87` |
| `Live` | `Long` | `2065.00` | 330,590,000.00 USD | 0.00 USD | 1,360,000.00 USD | `-11.60%` | `659.02` |
| `Live` | `Long` | `2075.00` | 329,230,000.00 USD | 0.00 USD | 921,260.00 USD | `-11.17%` | `443.98` |
| `Live` | `Long` | `2085.00` | 328,310,000.00 USD | 0.00 USD | 2,640,000.00 USD | `-10.74%` | `1,266.86` |
| `Live` | `Long` | `2095.00` | 325,670,000.00 USD | 0.00 USD | 1,420,000.00 USD | `-10.31%` | `678.82` |
| `Live` | `Long` | `2105.00` | 324,250,000.00 USD | 0.00 USD | 1,220,000.00 USD | `-9.89%` | `581.37` |
| `Live` | `Long` | `2115.00` | 323,020,000.00 USD | 0.00 USD | 20,470,000.00 USD | `-9.46%` | `9,677.80` |
| `Live` | `Long` | `2125.00` | 302,550,000.00 USD | 0.00 USD | 1,030,000.00 USD | `-9.03%` | `483.27` |
| `Live` | `Long` | `2135.00` | 301,530,000.00 USD | 0.00 USD | 3,440,000.00 USD | `-8.60%` | `1,611.69` |
| `Live` | `Long` | `2145.00` | 298,080,000.00 USD | 0.00 USD | 9,300,000.00 USD | `-8.17%` | `4,334.62` |
| `Live` | `Long` | `2155.00` | 288,790,000.00 USD | 0.00 USD | 23,380,000.00 USD | `-7.75%` | `10,850.53` |
| `Live` | `Long` | `2165.00` | 265,400,000.00 USD | 0.00 USD | 904,350.00 USD | `-7.32%` | `417.71` |
| `Live` | `Long` | `2175.00` | 264,500,000.00 USD | 0.00 USD | 109,710,000.00 USD | `-6.89%` | `50,442.76` |
| `Live` | `Long` | `2185.00` | 154,790,000.00 USD | 0.00 USD | 112,420,000.00 USD | `-6.46%` | `51,451.85` |
| `Live` | `Long` | `2195.00` | 42,360,000.00 USD | 0.00 USD | 909,930.00 USD | `-6.03%` | `414.55` |
| `Live` | `Long` | `2205.00` | 41,450,000.00 USD | 0.00 USD | 1,470,000.00 USD | `-5.61%` | `664.59` |
| `Live` | `Long` | `2215.00` | 39,990,000.00 USD | 0.00 USD | 1,830,000.00 USD | `-5.18%` | `828.07` |
| `Live` | `Long` | `2225.00` | 38,150,000.00 USD | 0.00 USD | 1,590,000.00 USD | `-4.75%` | `715.56` |
| `Live` | `Long` | `2235.00` | 36,560,000.00 USD | 0.00 USD | 1,290,000.00 USD | `-4.32%` | `574.95` |
| `Live` | `Long` | `2245.00` | 35,280,000.00 USD | 0.00 USD | 4,640,000.00 USD | `-3.89%` | `2,068.51` |
| `Live` | `Long` | `2255.00` | 30,630,000.00 USD | 0.00 USD | 10,910,000.00 USD | `-3.46%` | `4,838.43` |
| `Live` | `Long` | `2265.00` | 19,720,000.00 USD | 0.00 USD | 3,260,000.00 USD | `-3.04%` | `1,440.00` |
| `Live` | `Long` | `2275.00` | 16,460,000.00 USD | 0.00 USD | 6,850,000.00 USD | `-2.61%` | `3,011.34` |
| `Live` | `Long` | `2285.00` | 9,610,000.00 USD | 0.00 USD | 4,100,000.00 USD | `-2.18%` | `1,792.64` |
| `Live` | `Long` | `2295.00` | 5,510,000.00 USD | 0.00 USD | 3,310,000.00 USD | `-1.75%` | `1,443.30` |
| `Live` | `Long` | `2305.00` | 2,200,000.00 USD | 0.00 USD | 940,780.00 USD | `-1.32%` | `408.15` |
| `Live` | `Long` | `2315.00` | 1,260,000.00 USD | 0.00 USD | 932,620.00 USD | `-0.90%` | `402.86` |
| `Live` | `Long` | `2325.00` | 329,000.00 USD | 0.00 USD | 321,320.00 USD | `-0.47%` | `138.20` |
| `Live` | `Long` | `2335.00` | 7,680.00 USD | 0.00 USD | 7,680.00 USD | `-0.04%` | `3.29` |
| `Live` | `Short` | `2365.00` | 1,020.00 USD | 1,020.00 USD | 0.00 USD | `+1.24%` | `0.43` |
| `Live` | `Short` | `2375.00` | 48,040.00 USD | 47,010.00 USD | 0.00 USD | `+1.67%` | `19.79` |
| `Live` | `Short` | `2385.00` | 3,780,000.00 USD | 3,730,000.00 USD | 0.00 USD | `+2.10%` | `1,563.35` |
| `Live` | `Short` | `2395.00` | 8,190,000.00 USD | 4,420,000.00 USD | 0.00 USD | `+2.53%` | `1,843.46` |
| `Live` | `Short` | `2405.00` | 17,310,000.00 USD | 9,120,000.00 USD | 0.00 USD | `+2.96%` | `3,793.22` |
| `Live` | `Short` | `2415.00` | 17,770,000.00 USD | 459,730.00 USD | 0.00 USD | `+3.38%` | `190.37` |
| `Live` | `Short` | `2425.00` | 18,590,000.00 USD | 816,560.00 USD | 0.00 USD | `+3.81%` | `336.73` |
| `Live` | `Short` | `2435.00` | 26,630,000.00 USD | 8,040,000.00 USD | 0.00 USD | `+4.24%` | `3,301.66` |
| `Live` | `Short` | `2445.00` | 26,770,000.00 USD | 143,630.00 USD | 0.00 USD | `+4.67%` | `58.74` |
| `Live` | `Short` | `2455.00` | 26,880,000.00 USD | 106,960.00 USD | 0.00 USD | `+5.10%` | `43.57` |
| `Live` | `Short` | `2465.00` | 27,360,000.00 USD | 483,330.00 USD | 0.00 USD | `+5.52%` | `196.08` |
| `Live` | `Short` | `2475.00` | 27,750,000.00 USD | 386,010.00 USD | 0.00 USD | `+5.95%` | `155.97` |
| `Live` | `Short` | `2485.00` | 29,750,000.00 USD | 2,000,000.00 USD | 0.00 USD | `+6.38%` | `804.23` |
| `Live` | `Short` | `2495.00` | 30,690,000.00 USD | 941,300.00 USD | 0.00 USD | `+6.81%` | `377.28` |
| `Live` | `Short` | `2505.00` | 30,810,000.00 USD | 119,320.00 USD | 0.00 USD | `+7.24%` | `47.63` |
| `Live` | `Short` | `2515.00` | 30,950,000.00 USD | 139,000.00 USD | 0.00 USD | `+7.67%` | `55.27` |
| `Live` | `Short` | `2525.00` | 32,110,000.00 USD | 1,160,000.00 USD | 0.00 USD | `+8.09%` | `460.76` |
| `Live` | `Short` | `2535.00` | 32,780,000.00 USD | 663,280.00 USD | 0.00 USD | `+8.52%` | `261.65` |
| `Live` | `Short` | `2545.00` | 39,240,000.00 USD | 6,460,000.00 USD | 0.00 USD | `+8.95%` | `2,539.27` |
| `Live` | `Short` | `2555.00` | 42,070,000.00 USD | 2,830,000.00 USD | 0.00 USD | `+9.38%` | `1,107.61` |
| `Live` | `Short` | `2565.00` | 43,850,000.00 USD | 1,790,000.00 USD | 0.00 USD | `+9.81%` | `696.75` |
| `Live` | `Short` | `2575.00` | 55,690,000.00 USD | 11,830,000.00 USD | 0.00 USD | `+10.23%` | `4,596.01` |
| `Live` | `Short` | `2585.00` | 82,160,000.00 USD | 26,470,000.00 USD | 0.00 USD | `+10.66%` | `10,240.90` |
| `Live` | `Short` | `2595.00` | 90,340,000.00 USD | 8,180,000.00 USD | 0.00 USD | `+11.09%` | `3,151.01` |
| `Live` | `Short` | `2605.00` | 91,000,000.00 USD | 660,550.00 USD | 0.00 USD | `+11.52%` | `253.57` |
| `Live` | `Short` | `2615.00` | 92,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | `+11.95%` | `454.32` |
| `Live` | `Short` | `2625.00` | 92,640,000.00 USD | 453,080.00 USD | 0.00 USD | `+12.37%` | `172.60` |
| `Live` | `Short` | `2635.00` | 92,820,000.00 USD | 175,730.00 USD | 0.00 USD | `+12.80%` | `66.69` |
| `Live` | `Short` | `2645.00` | 92,980,000.00 USD | 163,860.00 USD | 0.00 USD | `+13.23%` | `61.95` |
| `Live` | `Short` | `2655.00` | 128,620,000.00 USD | 35,640,000.00 USD | 0.00 USD | `+13.66%` | `13,424.44` |
| `Live` | `Short` | `2665.00` | 128,690,000.00 USD | 68,220.00 USD | 0.00 USD | `+14.09%` | `25.60` |
| `Live` | `Short` | `2675.00` | 128,810,000.00 USD | 121,140.00 USD | 0.00 USD | `+14.51%` | `45.29` |
| `Live` | `Short` | `2685.00` | 136,490,000.00 USD | 7,680,000.00 USD | 0.00 USD | `+14.94%` | `2,860.98` |
| `Live` | `Short` | `2695.00` | 136,630,000.00 USD | 132,910.00 USD | 0.00 USD | `+15.37%` | `49.32` |
| `Live` | `Short` | `2705.00` | 179,150,000.00 USD | 42,520,000.00 USD | 0.00 USD | `+15.80%` | `15,720.40` |
| `Live` | `Short` | `2715.00` | 182,610,000.00 USD | 3,460,000.00 USD | 0.00 USD | `+16.23%` | `1,273.26` |
| `Live` | `Short` | `2725.00` | 182,950,000.00 USD | 347,630.00 USD | 0.00 USD | `+16.66%` | `127.57` |
| `Live` | `Short` | `2735.00` | 186,560,000.00 USD | 3,610,000.00 USD | 0.00 USD | `+17.08%` | `1,318.35` |
| `Live` | `Short` | `2745.00` | 187,500,000.00 USD | 937,840.00 USD | 0.00 USD | `+17.51%` | `341.65` |
| `Live` | `Short` | `2755.00` | 188,130,000.00 USD | 632,790.00 USD | 0.00 USD | `+17.94%` | `229.69` |
| `Live` | `Short` | `2765.00` | 188,430,000.00 USD | 299,800.00 USD | 0.00 USD | `+18.37%` | `108.43` |
| `Live` | `Short` | `2775.00` | 188,530,000.00 USD | 97,340.00 USD | 0.00 USD | `+18.80%` | `35.08` |
| `Live` | `Short` | `2785.00` | 195,450,000.00 USD | 6,920,000.00 USD | 0.00 USD | `+19.22%` | `2,485.02` |
| `Live` | `Short` | `2795.00` | 195,560,000.00 USD | 115,010.00 USD | 0.00 USD | `+19.65%` | `41.15` |
| `Live` | `Short` | `2805.00` | 196,420,000.00 USD | 859,600.00 USD | 0.00 USD | `+20.08%` | `306.45` |
| `Live` | `Short` | `2815.00` | 196,710,000.00 USD | 284,990.00 USD | 0.00 USD | `+20.51%` | `101.24` |
| `Live` | `Short` | `2825.00` | 196,790,000.00 USD | 83,990.00 USD | 0.00 USD | `+20.94%` | `29.73` |
| `Live` | `Short` | `2835.00` | 200,160,000.00 USD | 3,370,000.00 USD | 0.00 USD | `+21.36%` | `1,187.28` |
| `Live` | `Short` | `2845.00` | 202,520,000.00 USD | 2,360,000.00 USD | 0.00 USD | `+21.79%` | `830.77` |
| `Live` | `Short` | `2855.00` | 202,710,000.00 USD | 188,540.00 USD | 0.00 USD | `+22.22%` | `66.04` |
| `Live` | `Short` | `2865.00` | 247,440,000.00 USD | 44,730,000.00 USD | 0.00 USD | `+22.65%` | `15,613.46` |
| `Live` | `Short` | `2875.00` | 270,510,000.00 USD | 23,070,000.00 USD | 0.00 USD | `+23.08%` | `8,024.22` |
| `Live` | `Short` | `2885.00` | 274,410,000.00 USD | 3,890,000.00 USD | 0.00 USD | `+23.50%` | `1,349.31` |
| `Live` | `Short` | `2895.00` | 275,810,000.00 USD | 1,400,000.00 USD | 0.00 USD | `+23.93%` | `484.66` |
| `Live` | `Short` | `2905.00` | 276,260,000.00 USD | 453,700.00 USD | 0.00 USD | `+24.36%` | `156.18` |
| `Live` | `Short` | `2915.00` | 276,710,000.00 USD | 447,640.00 USD | 0.00 USD | `+24.79%` | `153.56` |
| `Live` | `Short` | `2925.00` | 303,210,000.00 USD | 26,510,000.00 USD | 0.00 USD | `+25.22%` | `9,061.67` |
| `Live` | `Short` | `2935.00` | 304,650,000.00 USD | 1,440,000.00 USD | 0.00 USD | `+25.65%` | `490.52` |
| `Live` | `Short` | `2945.00` | 312,130,000.00 USD | 7,480,000.00 USD | 0.00 USD | `+26.07%` | `2,538.42` |
| `Live` | `Short` | `2955.00` | 333,210,000.00 USD | 21,080,000.00 USD | 0.00 USD | `+26.50%` | `7,133.40` |
| `Live` | `Short` | `2965.00` | 334,630,000.00 USD | 1,420,000.00 USD | 0.00 USD | `+26.93%` | `478.84` |
| `Live` | `Short` | `2975.00` | 334,850,000.00 USD | 221,010.00 USD | 0.00 USD | `+27.36%` | `74.29` |
| `Live` | `Short` | `2985.00` | 335,670,000.00 USD | 818,270.00 USD | 0.00 USD | `+27.79%` | `274.13` |
| `Live` | `Short` | `2995.00` | 336,480,000.00 USD | 814,800.00 USD | 0.00 USD | `+28.21%` | `272.05` |
| `Live` | `Short` | `3005.00` | 340,010,000.00 USD | 3,520,000.00 USD | 0.00 USD | `+28.64%` | `1,172.27` |
| `Live` | `Short` | `3015.00` | 340,370,000.00 USD | 363,690.00 USD | 0.00 USD | `+29.07%` | `120.63` |
| `Live` | `Short` | `3025.00` | 348,650,000.00 USD | 8,280,000.00 USD | 0.00 USD | `+29.50%` | `2,736.90` |
| `Live` | `Short` | `3035.00` | 352,290,000.00 USD | 3,640,000.00 USD | 0.00 USD | `+29.93%` | `1,198.71` |
| `Live` | `Short` | `3045.00` | 365,430,000.00 USD | 13,150,000.00 USD | 0.00 USD | `+30.35%` | `4,317.20` |
| `Live` | `Short` | `3055.00` | 370,260,000.00 USD | 4,830,000.00 USD | 0.00 USD | `+30.78%` | `1,581.75` |
| `Live` | `Short` | `3065.00` | 370,900,000.00 USD | 632,420.00 USD | 0.00 USD | `+31.21%` | `206.34` |
| `Live` | `Short` | `3075.00` | 374,910,000.00 USD | 4,010,000.00 USD | 0.00 USD | `+31.64%` | `1,303.86` |
| `Live` | `Short` | `3085.00` | 375,020,000.00 USD | 110,980.00 USD | 0.00 USD | `+32.07%` | `35.97` |
| `Live` | `Short` | `3095.00` | 376,800,000.00 USD | 1,790,000.00 USD | 0.00 USD | `+32.49%` | `576.89` |
| `Live` | `Short` | `3105.00` | 377,400,000.00 USD | 597,120.00 USD | 0.00 USD | `+32.92%` | `192.31` |
| `Live` | `Short` | `3115.00` | 377,500,000.00 USD | 104,410.00 USD | 0.00 USD | `+33.35%` | `33.52` |
| `Live` | `Short` | `3125.00` | 377,640,000.00 USD | 136,660.00 USD | 0.00 USD | `+33.78%` | `43.73` |
| `Live` | `Short` | `3135.00` | 379,310,000.00 USD | 1,670,000.00 USD | 0.00 USD | `+34.21%` | `531.88` |
| `Live` | `Short` | `3145.00` | 380,840,000.00 USD | 1,530,000.00 USD | 0.00 USD | `+34.64%` | `486.59` |
| `Live` | `Short` | `3155.00` | 387,060,000.00 USD | 6,220,000.00 USD | 0.00 USD | `+35.06%` | `1,971.96` |
| `Live` | `Short` | `3165.00` | 387,060,000.00 USD | 1,480.00 USD | 0.00 USD | `+35.49%` | `0.47` |
| `Live` | `Short` | `3175.00` | 387,720,000.00 USD | 658,490.00 USD | 0.00 USD | `+35.92%` | `207.40` |
| `Live` | `Short` | `3185.00` | 388,790,000.00 USD | 1,070,000.00 USD | 0.00 USD | `+36.35%` | `336.70` |
| `Live` | `Short` | `3195.00` | 392,300,000.00 USD | 3,510,000.00 USD | 0.00 USD | `+36.78%` | `1,097.57` |
| `Live` | `Short` | `3205.00` | 392,390,000.00 USD | 90,340.00 USD | 0.00 USD | `+37.20%` | `28.19` |
| `Live` | `Short` | `3215.00` | 392,980,000.00 USD | 590,760.00 USD | 0.00 USD | `+37.63%` | `183.75` |
| `Live` | `Short` | `3225.00` | 397,980,000.00 USD | 5,000,000.00 USD | 0.00 USD | `+38.06%` | `1,550.29` |
| `Live` | `Short` | `3235.00` | 407,060,000.00 USD | 9,070,000.00 USD | 0.00 USD | `+38.49%` | `2,805.25` |
| `Live` | `Short` | `3245.00` | 407,080,000.00 USD | 20,630.00 USD | 0.00 USD | `+38.92%` | `6.36` |
| `Live` | `Short` | `3255.00` | 407,380,000.00 USD | 303,690.00 USD | 0.00 USD | `+39.34%` | `93.30` |
| `Live` | `Short` | `3265.00` | 407,740,000.00 USD | 359,730.00 USD | 0.00 USD | `+39.77%` | `110.18` |
| `Live` | `Short` | `3275.00` | 407,860,000.00 USD | 117,840.00 USD | 0.00 USD | `+40.20%` | `35.98` |
| `Live` | `Short` | `3285.00` | 416,990,000.00 USD | 9,130,000.00 USD | 0.00 USD | `+40.63%` | `2,779.70` |
| `Live` | `Short` | `3295.00` | 418,250,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+41.06%` | `384.02` |
| `Live` | `Short` | `3305.00` | 418,320,000.00 USD | 66,520.00 USD | 0.00 USD | `+41.48%` | `20.13` |
| `Live` | `Short` | `3315.00` | 429,980,000.00 USD | 11,660,000.00 USD | 0.00 USD | `+41.91%` | `3,517.92` |
| `Live` | `Short` | `3325.00` | 430,110,000.00 USD | 130,190.00 USD | 0.00 USD | `+42.34%` | `39.15` |
| `Live` | `Short` | `3335.00` | 430,140,000.00 USD | 27,410.00 USD | 0.00 USD | `+42.77%` | `8.22` |
| `Live` | `Short` | `3345.00` | 430,980,000.00 USD | 839,420.00 USD | 0.00 USD | `+43.20%` | `250.95` |
| `Live` | `Short` | `3355.00` | 493,710,000.00 USD | 62,730,000.00 USD | 0.00 USD | `+43.63%` | `18,698.08` |
| `Live` | `Short` | `3365.00` | 494,750,000.00 USD | 1,040,000.00 USD | 0.00 USD | `+44.05%` | `308.04` |
| `Live` | `Short` | `3375.00` | 494,860,000.00 USD | 110,710.00 USD | 0.00 USD | `+44.48%` | `32.80` |
| `Live` | `Short` | `3385.00` | 495,020,000.00 USD | 162,990.00 USD | 0.00 USD | `+44.91%` | `48.15` |
| `Live` | `Short` | `3395.00` | 495,260,000.00 USD | 238,960.00 USD | 0.00 USD | `+45.34%` | `70.38` |
| `Live` | `Short` | `3405.00` | 495,390,000.00 USD | 125,120.00 USD | 0.00 USD | `+45.77%` | `36.75` |
| `Live` | `Short` | `3415.00` | 498,520,000.00 USD | 3,140,000.00 USD | 0.00 USD | `+46.19%` | `918.62` |
| `Live` | `Short` | `3425.00` | 512,990,000.00 USD | 14,460,000.00 USD | 0.00 USD | `+46.62%` | `4,222.61` |
| `Live` | `Short` | `3435.00` | 513,230,000.00 USD | 240,520.00 USD | 0.00 USD | `+47.05%` | `70.02` |
| `Live` | `Short` | `3445.00` | 513,270,000.00 USD | 40,690.00 USD | 0.00 USD | `+47.48%` | `11.81` |
| `Live` | `Short` | `3455.00` | 518,720,000.00 USD | 5,450,000.00 USD | 0.00 USD | `+47.91%` | `1,577.50` |
| `Live` | `Short` | `3465.00` | 519,870,000.00 USD | 1,150,000.00 USD | 0.00 USD | `+48.33%` | `333.18` |
| `Live` | `Short` | `3475.00` | 520,310,000.00 USD | 442,570.00 USD | 0.00 USD | `+48.76%` | `127.36` |
| `Live` | `Short` | `3485.00` | 520,390,000.00 USD | 79,550.00 USD | 0.00 USD | `+49.19%` | `22.83` |
| `Live` | `Short` | `3495.00` | 522,070,000.00 USD | 1,670,000.00 USD | 0.00 USD | `+49.62%` | `479.24` |
| `Live` | `Short` | `3505.00` | 522,080,000.00 USD | 15,890.00 USD | 0.00 USD | `+50.05%` | `4.53` |
| `Live` | `Short` | `3515.00` | 522,120,000.00 USD | 35,660.00 USD | 0.00 USD | `+50.47%` | `10.15` |
| `Live` | `Short` | `3525.00` | 522,200,000.00 USD | 78,800.00 USD | 0.00 USD | `+50.90%` | `22.35` |
| `Live` | `Short` | `3535.00` | 522,240,000.00 USD | 39,410.00 USD | 0.00 USD | `+51.33%` | `11.15` |
| `Live` | `Short` | `3545.00` | 529,390,000.00 USD | 7,150,000.00 USD | 0.00 USD | `+51.76%` | `2,018.17` |
| `Live` | `Short` | `3555.00` | 529,540,000.00 USD | 143,600.00 USD | 0.00 USD | `+52.19%` | `40.40` |
| `Live` | `Short` | `3565.00` | 529,850,000.00 USD | 310,340.00 USD | 0.00 USD | `+52.62%` | `87.05` |
| `Live` | `Short` | `3575.00` | 529,920,000.00 USD | 78,340.00 USD | 0.00 USD | `+53.04%` | `21.91` |
| `Live` | `Short` | `3585.00` | 530,400,000.00 USD | 477,460.00 USD | 0.00 USD | `+53.47%` | `133.18` |
| `Live` | `Short` | `3595.00` | 530,700,000.00 USD | 302,580.00 USD | 0.00 USD | `+53.90%` | `84.17` |
| `Live` | `Short` | `3605.00` | 530,780,000.00 USD | 71,590.00 USD | 0.00 USD | `+54.33%` | `19.86` |
| `Live` | `Short` | `3615.00` | 534,600,000.00 USD | 3,830,000.00 USD | 0.00 USD | `+54.76%` | `1,058.13` |
| `Live` | `Short` | `3625.00` | 535,140,000.00 USD | 539,240.00 USD | 0.00 USD | `+55.18%` | `148.75` |
| `Live` | `Short` | `3635.00` | 638,380,000.00 USD | 103,240,000.00 USD | 0.00 USD | `+55.61%` | `28,401.85` |
| `Live` | `Short` | `3645.00` | 644,950,000.00 USD | 6,570,000.00 USD | 0.00 USD | `+56.04%` | `1,802.98` |
| `Live` | `Short` | `3655.00` | 645,330,000.00 USD | 378,780.00 USD | 0.00 USD | `+56.47%` | `103.63` |
| `Live` | `Short` | `3665.00` | 646,430,000.00 USD | 1,100,000.00 USD | 0.00 USD | `+56.90%` | `300.26` |
| `Live` | `Short` | `3675.00` | 646,800,000.00 USD | 367,730.00 USD | 0.00 USD | `+57.32%` | `100.06` |
| `Live` | `Short` | `3685.00` | 648,700,000.00 USD | 1,900,000.00 USD | 0.00 USD | `+57.75%` | `515.35` |
| `Live` | `Short` | `3695.00` | 649,790,000.00 USD | 1,090,000.00 USD | 0.00 USD | `+58.18%` | `295.40` |
| `Live` | `Short` | `3705.00` | 650,100,000.00 USD | 305,070.00 USD | 0.00 USD | `+58.61%` | `82.34` |
| `Live` | `Short` | `3715.00` | 658,410,000.00 USD | 8,320,000.00 USD | 0.00 USD | `+59.04%` | `2,238.72` |
| `Live` | `Short` | `3725.00` | 658,660,000.00 USD | 249,910.00 USD | 0.00 USD | `+59.46%` | `67.09` |
| `Live` | `Short` | `3735.00` | 693,440,000.00 USD | 34,780,000.00 USD | 0.00 USD | `+59.89%` | `9,311.39` |
| `Live` | `Short` | `3745.00` | 694,280,000.00 USD | 841,120.00 USD | 0.00 USD | `+60.32%` | `224.60` |
| `Live` | `Short` | `3755.00` | 707,730,000.00 USD | 13,450,000.00 USD | 0.00 USD | `+60.75%` | `3,581.65` |
| `Live` | `Short` | `3765.00` | 707,820,000.00 USD | 84,490.00 USD | 0.00 USD | `+61.18%` | `22.44` |
| `Live` | `Short` | `3775.00` | 708,170,000.00 USD | 351,950.00 USD | 0.00 USD | `+61.61%` | `93.23` |
| `Live` | `Short` | `3785.00` | 708,210,000.00 USD | 45,720.00 USD | 0.00 USD | `+62.03%` | `12.08` |
| `Live` | `Short` | `3795.00` | 708,480,000.00 USD | 271,140.00 USD | 0.00 USD | `+62.46%` | `71.45` |
| `Live` | `Short` | `3805.00` | 708,570,000.00 USD | 81,730.00 USD | 0.00 USD | `+62.89%` | `21.48` |
| `Live` | `Short` | `3815.00` | 708,780,000.00 USD | 211,350.00 USD | 0.00 USD | `+63.32%` | `55.40` |
| `Live` | `Short` | `3825.00` | 709,120,000.00 USD | 338,010.00 USD | 0.00 USD | `+63.75%` | `88.37` |
| `Live` | `Short` | `3835.00` | 1,120,000,000.00 USD | 408,410,000.00 USD | 0.00 USD | `+64.17%` | `106,495.35` |
| `Live` | `Short` | `3845.00` | 1,120,000,000.00 USD | 1,590,000.00 USD | 0.00 USD | `+64.60%` | `414.62` |
| `Live` | `Short` | `3855.00` | 1,120,000,000.00 USD | 1,780,000.00 USD | 0.00 USD | `+65.03%` | `462.85` |
| `Live` | `Short` | `3865.00` | 1,140,000,000.00 USD | 15,960,000.00 USD | 0.00 USD | `+65.46%` | `4,128.41` |
| `Live` | `Short` | `3885.00` | 1,140,000,000.00 USD | 1,420,000.00 USD | 0.00 USD | `+66.31%` | `365.27` |
| `Live` | `Short` | `3895.00` | 1,140,000,000.00 USD | 130,520.00 USD | 0.00 USD | `+66.74%` | `33.51` |
| `Live` | `Short` | `3905.00` | 1,140,000,000.00 USD | 1,430,000.00 USD | 0.00 USD | `+67.17%` | `366.29` |
| `Live` | `Short` | `3915.00` | 1,140,000,000.00 USD | 4,700.00 USD | 0.00 USD | `+67.60%` | `1.20` |
| `Live` | `Short` | `3925.00` | 1,140,000,000.00 USD | 199,870.00 USD | 0.00 USD | `+68.03%` | `50.92` |
| `Live` | `Short` | `3935.00` | 1,140,000,000.00 USD | 1,640,000.00 USD | 0.00 USD | `+68.45%` | `417.94` |
| `Live` | `Short` | `3945.00` | 1,140,000,000.00 USD | 25,640.00 USD | 0.00 USD | `+68.88%` | `6.50` |
| `Live` | `Short` | `3955.00` | 1,140,000,000.00 USD | 404,950.00 USD | 0.00 USD | `+69.31%` | `102.39` |
| `Live` | `Short` | `3965.00` | 1,140,000,000.00 USD | 680,870.00 USD | 0.00 USD | `+69.74%` | `171.72` |
| `Live` | `Short` | `3975.00` | 1,230,000,000.00 USD | 90,050,000.00 USD | 0.00 USD | `+70.17%` | `22,654.42` |
| `Live` | `Short` | `3985.00` | 1,240,000,000.00 USD | 3,920,000.00 USD | 0.00 USD | `+70.60%` | `983.10` |
| `Live` | `Short` | `3995.00` | 1,270,000,000.00 USD | 30,460,000.00 USD | 0.00 USD | `+71.02%` | `7,624.43` |
| `Live` | `Short` | `4005.00` | 1,270,000,000.00 USD | 216,180.00 USD | 0.00 USD | `+71.45%` | `53.98` |
| `Live` | `Short` | `4015.00` | 1,270,000,000.00 USD | 117,490.00 USD | 0.00 USD | `+71.88%` | `29.26` |
| `Live` | `Short` | `4025.00` | 1,270,000,000.00 USD | 824,230.00 USD | 0.00 USD | `+72.31%` | `204.78` |
| `Live` | `Short` | `4035.00` | 1,340,000,000.00 USD | 67,410,000.00 USD | 0.00 USD | `+72.74%` | `16,707.06` |
| `Live` | `Short` | `4045.00` | 1,340,000,000.00 USD | 1,580,000.00 USD | 0.00 USD | `+73.16%` | `391.77` |
| `Live` | `Short` | `4055.00` | 1,340,000,000.00 USD | 470,000.00 USD | 0.00 USD | `+73.59%` | `115.91` |
| `Live` | `Short` | `4065.00` | 1,340,000,000.00 USD | 2,090,000.00 USD | 0.00 USD | `+74.02%` | `515.28` |
| `Live` | `Short` | `4075.00` | 1,340,000,000.00 USD | 2,430,000.00 USD | 0.00 USD | `+74.45%` | `597.07` |
| `Live` | `Short` | `4085.00` | 1,340,000,000.00 USD | 287,790.00 USD | 0.00 USD | `+74.88%` | `70.45` |
| `Live` | `Short` | `4105.00` | 1,350,000,000.00 USD | 2,890,000.00 USD | 0.00 USD | `+75.73%` | `703.56` |
| `Live` | `Short` | `4115.00` | 1,350,000,000.00 USD | 83,350.00 USD | 0.00 USD | `+76.16%` | `20.25` |
| `Live` | `Short` | `4125.00` | 1,350,000,000.00 USD | 27,910.00 USD | 0.00 USD | `+76.59%` | `6.77` |
| `Live` | `Short` | `4135.00` | 1,350,000,000.00 USD | 864,500.00 USD | 0.00 USD | `+77.02%` | `209.07` |
| `Live` | `Short` | `4145.00` | 1,350,000,000.00 USD | 169,420.00 USD | 0.00 USD | `+77.44%` | `40.87` |
| `Live` | `Short` | `4155.00` | 1,350,000,000.00 USD | 492,990.00 USD | 0.00 USD | `+77.87%` | `118.65` |
| `Live` | `Short` | `4165.00` | 1,350,000,000.00 USD | 280,240.00 USD | 0.00 USD | `+78.30%` | `67.29` |
| `Live` | `Short` | `4185.00` | 1,350,000,000.00 USD | 4,130,000.00 USD | 0.00 USD | `+79.16%` | `986.45` |
| `Live` | `Short` | `4195.00` | 1,350,000,000.00 USD | 84,530.00 USD | 0.00 USD | `+79.59%` | `20.15` |
| `Live` | `Short` | `4205.00` | 1,350,000,000.00 USD | 674.90 USD | 0.00 USD | `+80.01%` | `0.16` |
| `Live` | `Short` | `4215.00` | 1,350,000,000.00 USD | 6,950.00 USD | 0.00 USD | `+80.44%` | `1.65` |
| `Live` | `Short` | `4225.00` | 1,370,000,000.00 USD | 18,600,000.00 USD | 0.00 USD | `+80.87%` | `4,402.96` |
| `Live` | `Short` | `4235.00` | 1,370,000,000.00 USD | 1,420.00 USD | 0.00 USD | `+81.30%` | `0.33` |
| `Live` | `Short` | `4245.00` | 1,370,000,000.00 USD | 4,670.00 USD | 0.00 USD | `+81.73%` | `1.10` |
| `Live` | `Short` | `4255.00` | 1,370,000,000.00 USD | 99,390.00 USD | 0.00 USD | `+82.15%` | `23.36` |
| `Live` | `Short` | `4265.00` | 1,370,000,000.00 USD | 68,000.00 USD | 0.00 USD | `+82.58%` | `15.94` |
| `Live` | `Short` | `4275.00` | 1,390,000,000.00 USD | 17,020,000.00 USD | 0.00 USD | `+83.01%` | `3,982.33` |
| `Live` | `Short` | `4285.00` | 1,390,000,000.00 USD | 217,490.00 USD | 0.00 USD | `+83.44%` | `50.76` |
| `Live` | `Short` | `4295.00` | 1,390,000,000.00 USD | 2,460.00 USD | 0.00 USD | `+83.87%` | `0.57` |
| `Live` | `Short` | `4305.00` | 1,390,000,000.00 USD | 8,250.00 USD | 0.00 USD | `+84.29%` | `1.92` |
| `Live` | `Short` | `4315.00` | 1,390,000,000.00 USD | 328,280.00 USD | 0.00 USD | `+84.72%` | `76.08` |
| `Live` | `Short` | `4325.00` | 1,390,000,000.00 USD | 31,660.00 USD | 0.00 USD | `+85.15%` | `7.32` |
| `Live` | `Short` | `4335.00` | 1,390,000,000.00 USD | 19,940.00 USD | 0.00 USD | `+85.58%` | `4.60` |
| `Live` | `Short` | `4345.00` | 1,390,000,000.00 USD | 2,270,000.00 USD | 0.00 USD | `+86.01%` | `521.38` |
| `Live` | `Short` | `4355.00` | 1,390,000,000.00 USD | 43,740.00 USD | 0.00 USD | `+86.43%` | `10.04` |
| `Live` | `Short` | `4365.00` | 1,390,000,000.00 USD | 598,460.00 USD | 0.00 USD | `+86.86%` | `137.10` |
| `Live` | `Short` | `4375.00` | 1,390,000,000.00 USD | 849,070.00 USD | 0.00 USD | `+87.29%` | `194.07` |
| `Live` | `Short` | `4385.00` | 1,680,000,000.00 USD | 285,930,000.00 USD | 0.00 USD | `+87.72%` | `65,205.81` |
| `Live` | `Short` | `4395.00` | 1,680,000,000.00 USD | 93,330.00 USD | 0.00 USD | `+88.15%` | `21.23` |
| `Live` | `Short` | `4405.00` | 1,680,000,000.00 USD | 26,050.00 USD | 0.00 USD | `+88.58%` | `5.91` |
| `Live` | `Short` | `4415.00` | 1,680,000,000.00 USD | 633,470.00 USD | 0.00 USD | `+89.00%` | `143.48` |
| `Live` | `Short` | `4425.00` | 1,680,000,000.00 USD | 1,930,000.00 USD | 0.00 USD | `+89.43%` | `436.79` |
| `Live` | `Short` | `4445.00` | 1,680,000,000.00 USD | 685,460.00 USD | 0.00 USD | `+90.29%` | `154.21` |
| `Live` | `Short` | `4455.00` | 1,680,000,000.00 USD | 490,070.00 USD | 0.00 USD | `+90.72%` | `110.00` |
| `Live` | `Short` | `4465.00` | 1,680,000,000.00 USD | 80,330.00 USD | 0.00 USD | `+91.14%` | `17.99` |
| `Live` | `Short` | `4475.00` | 1,680,000,000.00 USD | 36,810.00 USD | 0.00 USD | `+91.57%` | `8.23` |
| `Live` | `Short` | `4485.00` | 1,680,000,000.00 USD | 20,940.00 USD | 0.00 USD | `+92.00%` | `4.67` |
| `Live` | `Short` | `4495.00` | 1,680,000,000.00 USD | 12,800.00 USD | 0.00 USD | `+92.43%` | `2.85` |
| `Live` | `Short` | `4505.00` | 1,680,000,000.00 USD | 2,440,000.00 USD | 0.00 USD | `+92.86%` | `541.58` |
| `Live` | `Short` | `4515.00` | 1,690,000,000.00 USD | 3,840,000.00 USD | 0.00 USD | `+93.28%` | `851.21` |
| `Live` | `Short` | `4525.00` | 1,690,000,000.00 USD | 981,310.00 USD | 0.00 USD | `+93.71%` | `216.86` |
| `Live` | `Short` | `4535.00` | 1,690,000,000.00 USD | 86,800.00 USD | 0.00 USD | `+94.14%` | `19.14` |
| `Live` | `Short` | `4545.00` | 1,690,000,000.00 USD | 23,190.00 USD | 0.00 USD | `+94.57%` | `5.10` |
| `Live` | `Short` | `4555.00` | 1,690,000,000.00 USD | 43,530.00 USD | 0.00 USD | `+95.00%` | `9.56` |
| `Live` | `Short` | `4565.00` | 1,690,000,000.00 USD | 265,340.00 USD | 0.00 USD | `+95.42%` | `58.13` |
| `Live` | `Short` | `4575.00` | 1,690,000,000.00 USD | 137,500.00 USD | 0.00 USD | `+95.85%` | `30.05` |
| `Live` | `Short` | `4585.00` | 1,690,000,000.00 USD | 35,590.00 USD | 0.00 USD | `+96.28%` | `7.76` |
| `Live` | `Short` | `4595.00` | 1,690,000,000.00 USD | 251,050.00 USD | 0.00 USD | `+96.71%` | `54.64` |
| `Live` | `Short` | `4605.00` | 1,690,000,000.00 USD | 37,010.00 USD | 0.00 USD | `+97.14%` | `8.04` |
| `Live` | `Short` | `4615.00` | 1,690,000,000.00 USD | 52,010.00 USD | 0.00 USD | `+97.57%` | `11.27` |
| `Live` | `Short` | `4625.00` | 1,690,000,000.00 USD | 406,220.00 USD | 0.00 USD | `+97.99%` | `87.83` |
| `Live` | `Short` | `4635.00` | 1,690,000,000.00 USD | 231,230.00 USD | 0.00 USD | `+98.42%` | `49.89` |
| `Live` | `Short` | `4645.00` | 1,690,000,000.00 USD | 175,430.00 USD | 0.00 USD | `+98.85%` | `37.77` |
| `Live` | `Short` | `4655.00` | 1,690,000,000.00 USD | 1,360,000.00 USD | 0.00 USD | `+99.28%` | `291.51` |
| `Live` | `Short` | `4665.00` | 1,690,000,000.00 USD | 35,090.00 USD | 0.00 USD | `+99.71%` | `7.52` |
| `Live` | `Short` | `4675.00` | 1,690,000,000.00 USD | 50,490.00 USD | 0.00 USD | `+100.13%` | `10.80` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `505.00` | 1,500,000,000.00 USD | 0.00 USD | 16,750.00 USD | `-78.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.00` | 1,500,000,000.00 USD | 0.00 USD | 563.16 USD | `-76.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.00` | 1,500,000,000.00 USD | 0.00 USD | 885.90 USD | `-69.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `755.00` | 1,500,000,000.00 USD | 0.00 USD | 177.27 USD | `-67.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `795.00` | 1,500,000,000.00 USD | 0.00 USD | 104.22 USD | `-65.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `805.00` | 1,500,000,000.00 USD | 0.00 USD | 2,090.00 USD | `-65.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `835.00` | 1,500,000,000.00 USD | 0.00 USD | 1,670.00 USD | `-64.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `865.00` | 1,500,000,000.00 USD | 0.00 USD | 139,280.00 USD | `-62.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `885.00` | 1,500,000,000.00 USD | 0.00 USD | 3,130.00 USD | `-62.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `905.00` | 1,500,000,000.00 USD | 0.00 USD | 2,780.00 USD | `-61.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `985.00` | 1,500,000,000.00 USD | 0.00 USD | 516.34 USD | `-57.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `995.00` | 1,500,000,000.00 USD | 0.00 USD | 100.50 USD | `-57.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1005.00` | 1,500,000,000.00 USD | 0.00 USD | 222,040.00 USD | `-56.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1025.00` | 1,500,000,000.00 USD | 0.00 USD | 112.03 USD | `-56.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1065.00` | 1,500,000,000.00 USD | 0.00 USD | 1,060.00 USD | `-54.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1075.00` | 1,500,000,000.00 USD | 0.00 USD | 995.34 USD | `-53.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1105.00` | 1,500,000,000.00 USD | 0.00 USD | 1,610.00 USD | `-52.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1115.00` | 1,500,000,000.00 USD | 0.00 USD | 11,050.00 USD | `-52.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1125.00` | 1,500,000,000.00 USD | 0.00 USD | 1,320.00 USD | `-51.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1155.00` | 1,500,000,000.00 USD | 0.00 USD | 1,000.00 USD | `-50.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1175.00` | 1,500,000,000.00 USD | 0.00 USD | 203.98 USD | `-49.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1185.00` | 1,500,000,000.00 USD | 0.00 USD | 228.47 USD | `-49.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1205.00` | 1,500,000,000.00 USD | 0.00 USD | 3,110.00 USD | `-48.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1225.00` | 1,500,000,000.00 USD | 0.00 USD | 995.93 USD | `-47.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1245.00` | 1,500,000,000.00 USD | 0.00 USD | 951.93 USD | `-46.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1255.00` | 1,500,000,000.00 USD | 0.00 USD | 6,810.00 USD | `-46.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1285.00` | 1,500,000,000.00 USD | 0.00 USD | 9,050.00 USD | `-44.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1295.00` | 1,500,000,000.00 USD | 0.00 USD | 7,030.00 USD | `-44.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1305.00` | 1,500,000,000.00 USD | 0.00 USD | 23,030.00 USD | `-44.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1315.00` | 1,500,000,000.00 USD | 0.00 USD | 1,440.00 USD | `-43.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1345.00` | 1,500,000,000.00 USD | 0.00 USD | 141,950.00 USD | `-42.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1355.00` | 1,500,000,000.00 USD | 0.00 USD | 128.86 USD | `-41.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1375.00` | 1,500,000,000.00 USD | 0.00 USD | 4,160.00 USD | `-41.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1395.00` | 1,500,000,000.00 USD | 0.00 USD | 535,600.00 USD | `-40.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1405.00` | 1,500,000,000.00 USD | 0.00 USD | 20,270.00 USD | `-39.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1425.00` | 1,500,000,000.00 USD | 0.00 USD | 6,450.00 USD | `-39.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1435.00` | 1,500,000,000.00 USD | 0.00 USD | 852.10 USD | `-38.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1445.00` | 1,500,000,000.00 USD | 0.00 USD | 1,490.00 USD | `-38.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1455.00` | 1,500,000,000.00 USD | 0.00 USD | 5,680.00 USD | `-37.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1465.00` | 1,500,000,000.00 USD | 0.00 USD | 19,350.00 USD | `-37.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1475.00` | 1,500,000,000.00 USD | 0.00 USD | 2,600.00 USD | `-36.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1485.00` | 1,500,000,000.00 USD | 0.00 USD | 18,710.00 USD | `-36.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1495.00` | 1,500,000,000.00 USD | 0.00 USD | 11,460.00 USD | `-36.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1505.00` | 1,500,000,000.00 USD | 0.00 USD | 78,910.00 USD | `-35.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1515.00` | 1,500,000,000.00 USD | 0.00 USD | 11,140.00 USD | `-35.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1525.00` | 1,500,000,000.00 USD | 0.00 USD | 32,310.00 USD | `-34.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1535.00` | 1,500,000,000.00 USD | 0.00 USD | 983.78 USD | `-34.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1545.00` | 1,500,000,000.00 USD | 0.00 USD | 17,470.00 USD | `-33.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1555.00` | 1,500,000,000.00 USD | 0.00 USD | 4,210.00 USD | `-33.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1565.00` | 1,500,000,000.00 USD | 0.00 USD | 6,260.00 USD | `-33.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1575.00` | 1,500,000,000.00 USD | 0.00 USD | 190,890.00 USD | `-32.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1585.00` | 1,500,000,000.00 USD | 0.00 USD | 3,390.00 USD | `-32.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1595.00` | 1,500,000,000.00 USD | 0.00 USD | 4,040.00 USD | `-31.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1605.00` | 1,500,000,000.00 USD | 0.00 USD | 435,900.00 USD | `-31.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1615.00` | 1,500,000,000.00 USD | 0.00 USD | 25,840.00 USD | `-30.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1625.00` | 1,500,000,000.00 USD | 0.00 USD | 13,590.00 USD | `-30.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1635.00` | 1,500,000,000.00 USD | 0.00 USD | 5,510.00 USD | `-30.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1645.00` | 1,500,000,000.00 USD | 0.00 USD | 328,140.00 USD | `-29.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1655.00` | 1,500,000,000.00 USD | 0.00 USD | 22,220.00 USD | `-29.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1665.00` | 1,500,000,000.00 USD | 0.00 USD | 3,110.00 USD | `-28.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1675.00` | 1,500,000,000.00 USD | 0.00 USD | 3,440.00 USD | `-28.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1685.00` | 1,500,000,000.00 USD | 0.00 USD | 58,890.00 USD | `-27.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1695.00` | 1,500,000,000.00 USD | 0.00 USD | 6,800.00 USD | `-27.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1705.00` | 1,500,000,000.00 USD | 0.00 USD | 81,190.00 USD | `-27.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1715.00` | 1,500,000,000.00 USD | 0.00 USD | 28,180.00 USD | `-26.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1725.00` | 1,500,000,000.00 USD | 0.00 USD | 47,500.00 USD | `-26.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1735.00` | 1,500,000,000.00 USD | 0.00 USD | 28,150.00 USD | `-25.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1745.00` | 1,500,000,000.00 USD | 0.00 USD | 3,180.00 USD | `-25.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1755.00` | 1,500,000,000.00 USD | 0.00 USD | 498,170.00 USD | `-24.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1765.00` | 1,500,000,000.00 USD | 0.00 USD | 75,630.00 USD | `-24.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1775.00` | 1,500,000,000.00 USD | 0.00 USD | 3,090.00 USD | `-24.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1785.00` | 1,500,000,000.00 USD | 0.00 USD | 4,930.00 USD | `-23.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1795.00` | 1,500,000,000.00 USD | 0.00 USD | 184,330.00 USD | `-23.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1805.00` | 1,500,000,000.00 USD | 0.00 USD | 283,470.00 USD | `-22.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1815.00` | 1,500,000,000.00 USD | 0.00 USD | 114,830.00 USD | `-22.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1825.00` | 1,500,000,000.00 USD | 0.00 USD | 26,680.00 USD | `-21.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1835.00` | 1,500,000,000.00 USD | 0.00 USD | 2,390.00 USD | `-21.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1845.00` | 1,500,000,000.00 USD | 0.00 USD | 9,040.00 USD | `-21.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1855.00` | 1,500,000,000.00 USD | 0.00 USD | 467,010.00 USD | `-20.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1865.00` | 1,500,000,000.00 USD | 0.00 USD | 32,910.00 USD | `-20.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1875.00` | 1,500,000,000.00 USD | 0.00 USD | 18,210,000.00 USD | `-19.73%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1885.00` | 1,480,000,000.00 USD | 0.00 USD | 2,390.00 USD | `-19.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1895.00` | 1,480,000,000.00 USD | 0.00 USD | 61,700.00 USD | `-18.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1905.00` | 1,480,000,000.00 USD | 0.00 USD | 162,190.00 USD | `-18.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1915.00` | 1,480,000,000.00 USD | 0.00 USD | 8,110,000.00 USD | `-18.02%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1925.00` | 1,470,000,000.00 USD | 0.00 USD | 16,410,000.00 USD | `-17.59%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1935.00` | 1,450,000,000.00 USD | 0.00 USD | 79,950.00 USD | `-17.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1945.00` | 1,450,000,000.00 USD | 0.00 USD | 44,850.00 USD | `-16.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1955.00` | 1,450,000,000.00 USD | 0.00 USD | 54,180.00 USD | `-16.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1965.00` | 1,450,000,000.00 USD | 0.00 USD | 510.51 USD | `-15.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1975.00` | 1,450,000,000.00 USD | 0.00 USD | 78,230.00 USD | `-15.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1985.00` | 1,450,000,000.00 USD | 0.00 USD | 98,040.00 USD | `-15.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1995.00` | 1,450,000,000.00 USD | 0.00 USD | 104,260.00 USD | `-14.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2005.00` | 1,450,000,000.00 USD | 0.00 USD | 1,360,000.00 USD | `-14.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2015.00` | 1,450,000,000.00 USD | 0.00 USD | 69,270.00 USD | `-13.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2025.00` | 1,450,000,000.00 USD | 0.00 USD | 5,040.00 USD | `-13.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2035.00` | 1,450,000,000.00 USD | 0.00 USD | 103,890.00 USD | `-12.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2045.00` | 1,450,000,000.00 USD | 0.00 USD | 15,220.00 USD | `-12.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2055.00` | 1,450,000,000.00 USD | 0.00 USD | 212,720.00 USD | `-12.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2065.00` | 1,450,000,000.00 USD | 0.00 USD | 91,330.00 USD | `-11.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2075.00` | 1,450,000,000.00 USD | 0.00 USD | 32,400.00 USD | `-11.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2085.00` | 1,450,000,000.00 USD | 0.00 USD | 52,030.00 USD | `-10.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2095.00` | 1,450,000,000.00 USD | 0.00 USD | 29,710.00 USD | `-10.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2105.00` | 1,450,000,000.00 USD | 0.00 USD | 351,510.00 USD | `-9.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2115.00` | 1,450,000,000.00 USD | 0.00 USD | 123,820.00 USD | `-9.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2125.00` | 1,450,000,000.00 USD | 0.00 USD | 81,460.00 USD | `-9.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2135.00` | 1,450,000,000.00 USD | 0.00 USD | 19,470.00 USD | `-8.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2145.00` | 1,450,000,000.00 USD | 0.00 USD | 217,830.00 USD | `-8.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2155.00` | 1,450,000,000.00 USD | 0.00 USD | 100,400.00 USD | `-7.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2165.00` | 1,450,000,000.00 USD | 0.00 USD | 902,640.00 USD | `-7.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2175.00` | 1,450,000,000.00 USD | 0.00 USD | 1,360,000.00 USD | `-6.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2185.00` | 1,450,000,000.00 USD | 0.00 USD | 92,000.00 USD | `-6.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2195.00` | 1,450,000,000.00 USD | 0.00 USD | 438,560.00 USD | `-6.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2205.00` | 1,450,000,000.00 USD | 0.00 USD | 2,270,000.00 USD | `-5.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2215.00` | 1,450,000,000.00 USD | 0.00 USD | 1,020,000.00 USD | `-5.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2225.00` | 1,440,000,000.00 USD | 0.00 USD | 1,010,000.00 USD | `-4.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2235.00` | 1,440,000,000.00 USD | 0.00 USD | 127,280.00 USD | `-4.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2245.00` | 1,440,000,000.00 USD | 0.00 USD | 1,450,000.00 USD | `-3.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2255.00` | 1,440,000,000.00 USD | 0.00 USD | 23,300,000.00 USD | `-3.46%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2265.00` | 1,420,000,000.00 USD | 0.00 USD | 521,190.00 USD | `-3.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2275.00` | 1,420,000,000.00 USD | 0.00 USD | 4,690,000.00 USD | `-2.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2285.00` | 1,410,000,000.00 USD | 0.00 USD | 4,210,000.00 USD | `-2.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2295.00` | 1,410,000,000.00 USD | 0.00 USD | 11,280,000.00 USD | `-1.75%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2305.00` | 1,400,000,000.00 USD | 0.00 USD | 1,380,000,000.00 USD | `-1.32%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2315.00` | 13,040,000.00 USD | 0.00 USD | 11,590,000.00 USD | `-0.90%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2325.00` | 1,450,000.00 USD | 0.00 USD | 1,150,000.00 USD | `-0.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2335.00` | 302,810.00 USD | 0.00 USD | 302,810.00 USD | `-0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2345.00` | 588,660.00 USD | 588,660.00 USD | 0.00 USD | `+0.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2355.00` | 3,170,000.00 USD | 2,580,000.00 USD | 0.00 USD | `+0.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2365.00` | 3,510,000.00 USD | 339,140.00 USD | 0.00 USD | `+1.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2375.00` | 3,650,000.00 USD | 133,560.00 USD | 0.00 USD | `+1.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2385.00` | 5,380,000.00 USD | 1,740,000.00 USD | 0.00 USD | `+2.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2395.00` | 6,940,000.00 USD | 1,560,000.00 USD | 0.00 USD | `+2.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2405.00` | 9,290,000.00 USD | 2,350,000.00 USD | 0.00 USD | `+2.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2415.00` | 9,820,000.00 USD | 535,610.00 USD | 0.00 USD | `+3.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2425.00` | 13,290,000.00 USD | 3,470,000.00 USD | 0.00 USD | `+3.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2435.00` | 13,630,000.00 USD | 333,010.00 USD | 0.00 USD | `+4.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2445.00` | 24,170,000.00 USD | 10,550,000.00 USD | 0.00 USD | `+4.67%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2455.00` | 24,400,000.00 USD | 226,060.00 USD | 0.00 USD | `+5.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2465.00` | 26,580,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+5.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2475.00` | 26,920,000.00 USD | 344,170.00 USD | 0.00 USD | `+5.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2485.00` | 29,070,000.00 USD | 2,160,000.00 USD | 0.00 USD | `+6.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2495.00` | 29,520,000.00 USD | 440,780.00 USD | 0.00 USD | `+6.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2505.00` | 34,890,000.00 USD | 5,380,000.00 USD | 0.00 USD | `+7.24%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2515.00` | 42,670,000.00 USD | 7,780,000.00 USD | 0.00 USD | `+7.67%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2525.00` | 45,930,000.00 USD | 3,260,000.00 USD | 0.00 USD | `+8.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2535.00` | 46,000,000.00 USD | 72,380.00 USD | 0.00 USD | `+8.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2545.00` | 48,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | `+8.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2555.00` | 48,490,000.00 USD | 333,630.00 USD | 0.00 USD | `+9.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2565.00` | 50,830,000.00 USD | 2,330,000.00 USD | 0.00 USD | `+9.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2575.00` | 50,990,000.00 USD | 159,570.00 USD | 0.00 USD | `+10.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2585.00` | 53,440,000.00 USD | 2,450,000.00 USD | 0.00 USD | `+10.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2595.00` | 53,450,000.00 USD | 14,580.00 USD | 0.00 USD | `+11.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2605.00` | 56,550,000.00 USD | 3,100,000.00 USD | 0.00 USD | `+11.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2615.00` | 56,730,000.00 USD | 177,120.00 USD | 0.00 USD | `+11.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2625.00` | 58,920,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+12.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2635.00` | 59,210,000.00 USD | 292,470.00 USD | 0.00 USD | `+12.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2645.00` | 61,380,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+13.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2655.00` | 61,630,000.00 USD | 251,320.00 USD | 0.00 USD | `+13.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2665.00` | 63,780,000.00 USD | 2,160,000.00 USD | 0.00 USD | `+14.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2675.00` | 64,180,000.00 USD | 393,350.00 USD | 0.00 USD | `+14.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2685.00` | 66,360,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+14.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2695.00` | 66,540,000.00 USD | 172,910.00 USD | 0.00 USD | `+15.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2705.00` | 71,210,000.00 USD | 4,670,000.00 USD | 0.00 USD | `+15.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2715.00` | 71,280,000.00 USD | 76,900.00 USD | 0.00 USD | `+16.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2725.00` | 73,750,000.00 USD | 2,470,000.00 USD | 0.00 USD | `+16.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2735.00` | 73,810,000.00 USD | 55,280.00 USD | 0.00 USD | `+17.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2745.00` | 76,110,000.00 USD | 2,300,000.00 USD | 0.00 USD | `+17.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2755.00` | 76,800,000.00 USD | 687,450.00 USD | 0.00 USD | `+17.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2765.00` | 79,180,000.00 USD | 2,380,000.00 USD | 0.00 USD | `+18.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2775.00` | 79,800,000.00 USD | 620,300.00 USD | 0.00 USD | `+18.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2785.00` | 82,100,000.00 USD | 2,290,000.00 USD | 0.00 USD | `+19.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2795.00` | 82,130,000.00 USD | 36,990.00 USD | 0.00 USD | `+19.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2805.00` | 86,120,000.00 USD | 3,990,000.00 USD | 0.00 USD | `+20.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2815.00` | 86,170,000.00 USD | 53,260.00 USD | 0.00 USD | `+20.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2825.00` | 86,240,000.00 USD | 62,020.00 USD | 0.00 USD | `+20.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2835.00` | 86,520,000.00 USD | 289,110.00 USD | 0.00 USD | `+21.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2845.00` | 87,540,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+21.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2855.00` | 88,820,000.00 USD | 1,280,000.00 USD | 0.00 USD | `+22.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2865.00` | 88,830,000.00 USD | 10,290.00 USD | 0.00 USD | `+22.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2875.00` | 88,830,000.00 USD | 3,630.00 USD | 0.00 USD | `+23.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2885.00` | 89,120,000.00 USD | 292,580.00 USD | 0.00 USD | `+23.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2895.00` | 89,150,000.00 USD | 23,020.00 USD | 0.00 USD | `+23.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2905.00` | 90,690,000.00 USD | 1,540,000.00 USD | 0.00 USD | `+24.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2915.00` | 90,700,000.00 USD | 10,340.00 USD | 0.00 USD | `+24.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2925.00` | 90,700,000.00 USD | 3,040.00 USD | 0.00 USD | `+25.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2935.00` | 90,750,000.00 USD | 54,540.00 USD | 0.00 USD | `+25.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2945.00` | 90,790,000.00 USD | 34,650.00 USD | 0.00 USD | `+26.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2955.00` | 90,860,000.00 USD | 74,770.00 USD | 0.00 USD | `+26.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2965.00` | 90,970,000.00 USD | 111,790.00 USD | 0.00 USD | `+26.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2975.00` | 91,120,000.00 USD | 148,070.00 USD | 0.00 USD | `+27.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2985.00` | 95,210,000.00 USD | 4,090,000.00 USD | 0.00 USD | `+27.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2995.00` | 97,130,000.00 USD | 1,920,000.00 USD | 0.00 USD | `+28.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3005.00` | 99,120,000.00 USD | 1,990,000.00 USD | 0.00 USD | `+28.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3015.00` | 99,130,000.00 USD | 6,950.00 USD | 0.00 USD | `+29.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3025.00` | 99,170,000.00 USD | 37,410.00 USD | 0.00 USD | `+29.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3035.00` | 99,240,000.00 USD | 70,360.00 USD | 0.00 USD | `+29.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3045.00` | 99,260,000.00 USD | 22,460.00 USD | 0.00 USD | `+30.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3055.00` | 100,050,000.00 USD | 786,100.00 USD | 0.00 USD | `+30.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3065.00` | 100,050,000.00 USD | 3,360.00 USD | 0.00 USD | `+31.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3075.00` | 100,100,000.00 USD | 50,370.00 USD | 0.00 USD | `+31.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3085.00` | 100,120,000.00 USD | 19,860.00 USD | 0.00 USD | `+32.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3095.00` | 100,120,000.00 USD | 928.50 USD | 0.00 USD | `+32.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3105.00` | 113,530,000.00 USD | 13,410,000.00 USD | 0.00 USD | `+32.92%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `3115.00` | 113,650,000.00 USD | 118,040.00 USD | 0.00 USD | `+33.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3125.00` | 114,010,000.00 USD | 367,790.00 USD | 0.00 USD | `+33.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3145.00` | 114,020,000.00 USD | 1,860.00 USD | 0.00 USD | `+34.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3155.00` | 114,080,000.00 USD | 68,940.00 USD | 0.00 USD | `+35.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3165.00` | 114,090,000.00 USD | 9,860.00 USD | 0.00 USD | `+35.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3175.00` | 114,110,000.00 USD | 16,410.00 USD | 0.00 USD | `+35.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3185.00` | 114,110,000.00 USD | 1,980.00 USD | 0.00 USD | `+36.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3195.00` | 114,140,000.00 USD | 29,580.00 USD | 0.00 USD | `+36.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3205.00` | 115,050,000.00 USD | 910,780.00 USD | 0.00 USD | `+37.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3215.00` | 115,050,000.00 USD | 1,290.00 USD | 0.00 USD | `+37.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3225.00` | 115,060,000.00 USD | 3,740.00 USD | 0.00 USD | `+38.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3235.00` | 115,090,000.00 USD | 30,790.00 USD | 0.00 USD | `+38.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3245.00` | 115,150,000.00 USD | 56,110.00 USD | 0.00 USD | `+38.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3255.00` | 115,350,000.00 USD | 204,030.00 USD | 0.00 USD | `+39.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3265.00` | 115,360,000.00 USD | 15,710.00 USD | 0.00 USD | `+39.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3275.00` | 115,370,000.00 USD | 1,630.00 USD | 0.00 USD | `+40.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3285.00` | 115,510,000.00 USD | 141,980.00 USD | 0.00 USD | `+40.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3295.00` | 115,530,000.00 USD | 16,780.00 USD | 0.00 USD | `+41.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3305.00` | 116,800,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+41.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3315.00` | 117,180,000.00 USD | 385,510.00 USD | 0.00 USD | `+41.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3325.00` | 117,200,000.00 USD | 18,270.00 USD | 0.00 USD | `+42.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3335.00` | 117,210,000.00 USD | 14,190.00 USD | 0.00 USD | `+42.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3345.00` | 117,210,000.00 USD | 617.15 USD | 0.00 USD | `+43.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3355.00` | 117,210,000.00 USD | 334.49 USD | 0.00 USD | `+43.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3365.00` | 117,210,000.00 USD | 597.29 USD | 0.00 USD | `+44.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3375.00` | 117,240,000.00 USD | 23,460.00 USD | 0.00 USD | `+44.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3385.00` | 117,300,000.00 USD | 58,010.00 USD | 0.00 USD | `+44.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3395.00` | 117,650,000.00 USD | 355,050.00 USD | 0.00 USD | `+45.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3405.00` | 119,250,000.00 USD | 1,600,000.00 USD | 0.00 USD | `+45.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3415.00` | 119,260,000.00 USD | 3,510.00 USD | 0.00 USD | `+46.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3425.00` | 119,270,000.00 USD | 16,310.00 USD | 0.00 USD | `+46.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3445.00` | 119,290,000.00 USD | 15,030.00 USD | 0.00 USD | `+47.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3455.00` | 119,310,000.00 USD | 18,600.00 USD | 0.00 USD | `+47.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3465.00` | 119,620,000.00 USD | 311,800.00 USD | 0.00 USD | `+48.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3475.00` | 119,620,000.00 USD | 2,980.00 USD | 0.00 USD | `+48.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3485.00` | 119,670,000.00 USD | 43,610.00 USD | 0.00 USD | `+49.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3495.00` | 119,670,000.00 USD | 158.32 USD | 0.00 USD | `+49.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3505.00` | 120,220,000.00 USD | 550,300.00 USD | 0.00 USD | `+50.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3515.00` | 120,260,000.00 USD | 43,200.00 USD | 0.00 USD | `+50.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3525.00` | 120,260,000.00 USD | 3,690.00 USD | 0.00 USD | `+50.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3535.00` | 120,270,000.00 USD | 9,810.00 USD | 0.00 USD | `+51.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3545.00` | 120,270,000.00 USD | 179.38 USD | 0.00 USD | `+51.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3555.00` | 120,360,000.00 USD | 90,810.00 USD | 0.00 USD | `+52.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3565.00` | 120,370,000.00 USD | 2,300.00 USD | 0.00 USD | `+52.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3585.00` | 120,370,000.00 USD | 354.92 USD | 0.00 USD | `+53.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3595.00` | 120,380,000.00 USD | 13,160.00 USD | 0.00 USD | `+53.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3605.00` | 120,490,000.00 USD | 105,860.00 USD | 0.00 USD | `+54.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3625.00` | 120,500,000.00 USD | 10,210.00 USD | 0.00 USD | `+55.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3635.00` | 120,500,000.00 USD | 7,790.00 USD | 0.00 USD | `+55.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3645.00` | 120,510,000.00 USD | 3,860.00 USD | 0.00 USD | `+56.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3655.00` | 120,520,000.00 USD | 7,740.00 USD | 0.00 USD | `+56.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3665.00` | 120,520,000.00 USD | 8,130.00 USD | 0.00 USD | `+56.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3675.00` | 120,580,000.00 USD | 55,120.00 USD | 0.00 USD | `+57.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3685.00` | 120,580,000.00 USD | 3,550.00 USD | 0.00 USD | `+57.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3705.00` | 120,580,000.00 USD | 819.92 USD | 0.00 USD | `+58.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3715.00` | 120,580,000.00 USD | 323.58 USD | 0.00 USD | `+59.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3725.00` | 120,590,000.00 USD | 1,400.00 USD | 0.00 USD | `+59.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3735.00` | 120,590,000.00 USD | 6,490.00 USD | 0.00 USD | `+59.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3755.00` | 120,590,000.00 USD | 751.00 USD | 0.00 USD | `+60.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3785.00` | 120,590,000.00 USD | 286.90 USD | 0.00 USD | `+62.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3795.00` | 120,590,000.00 USD | 1,560.00 USD | 0.00 USD | `+62.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3805.00` | 121,330,000.00 USD | 734,090.00 USD | 0.00 USD | `+62.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3815.00` | 121,350,000.00 USD | 20,930.00 USD | 0.00 USD | `+63.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3825.00` | 121,360,000.00 USD | 8,380.00 USD | 0.00 USD | `+63.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3835.00` | 121,360,000.00 USD | 711.78 USD | 0.00 USD | `+64.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3845.00` | 121,360,000.00 USD | 932.03 USD | 0.00 USD | `+64.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3855.00` | 121,560,000.00 USD | 203,880.00 USD | 0.00 USD | `+65.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3885.00` | 121,580,000.00 USD | 21,210.00 USD | 0.00 USD | `+66.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3905.00` | 121,760,000.00 USD | 180,010.00 USD | 0.00 USD | `+67.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3915.00` | 122,410,000.00 USD | 646,840.00 USD | 0.00 USD | `+67.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3925.00` | 122,410,000.00 USD | 3,260.00 USD | 0.00 USD | `+68.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3935.00` | 122,460,000.00 USD | 42,570.00 USD | 0.00 USD | `+68.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3945.00` | 122,480,000.00 USD | 19,730.00 USD | 0.00 USD | `+68.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3955.00` | 122,480,000.00 USD | 1,380.00 USD | 0.00 USD | `+69.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3965.00` | 122,480,000.00 USD | 323.54 USD | 0.00 USD | `+69.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3975.00` | 122,490,000.00 USD | 6,960.00 USD | 0.00 USD | `+70.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3985.00` | 122,500,000.00 USD | 14,610.00 USD | 0.00 USD | `+70.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3995.00` | 122,500,000.00 USD | 4,280.00 USD | 0.00 USD | `+71.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4005.00` | 125,170,000.00 USD | 2,670,000.00 USD | 0.00 USD | `+71.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4035.00` | 125,170,000.00 USD | 898.59 USD | 0.00 USD | `+72.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4055.00` | 125,170,000.00 USD | 811.00 USD | 0.00 USD | `+73.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4075.00` | 125,180,000.00 USD | 4,310.00 USD | 0.00 USD | `+74.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4085.00` | 125,180,000.00 USD | 2,800.00 USD | 0.00 USD | `+74.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4095.00` | 125,180,000.00 USD | 2,750.00 USD | 0.00 USD | `+75.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4105.00` | 125,230,000.00 USD | 48,190.00 USD | 0.00 USD | `+75.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4115.00` | 125,240,000.00 USD | 5,990.00 USD | 0.00 USD | `+76.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4125.00` | 125,240,000.00 USD | 372.90 USD | 0.00 USD | `+76.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4145.00` | 125,240,000.00 USD | 395.43 USD | 0.00 USD | `+77.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4185.00` | 125,240,000.00 USD | 376.65 USD | 0.00 USD | `+79.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4205.00` | 125,270,000.00 USD | 28,760.00 USD | 0.00 USD | `+80.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4215.00` | 125,270,000.00 USD | 460.70 USD | 0.00 USD | `+80.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4225.00` | 125,270,000.00 USD | 1,270.00 USD | 0.00 USD | `+80.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4255.00` | 125,270,000.00 USD | 4,300.00 USD | 0.00 USD | `+82.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4265.00` | 125,280,000.00 USD | 4,010.00 USD | 0.00 USD | `+82.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4275.00` | 125,340,000.00 USD | 64,550.00 USD | 0.00 USD | `+83.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4285.00` | 125,340,000.00 USD | 1,610.00 USD | 0.00 USD | `+83.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4305.00` | 125,440,000.00 USD | 97,670.00 USD | 0.00 USD | `+84.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4315.00` | 125,440,000.00 USD | 1,070.00 USD | 0.00 USD | `+84.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4345.00` | 125,450,000.00 USD | 11,270.00 USD | 0.00 USD | `+86.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4355.00` | 125,460,000.00 USD | 3,250.00 USD | 0.00 USD | `+86.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4375.00` | 125,500,000.00 USD | 43,750.00 USD | 0.00 USD | `+87.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4385.00` | 125,570,000.00 USD | 64,570.00 USD | 0.00 USD | `+87.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4395.00` | 125,570,000.00 USD | 1,050.00 USD | 0.00 USD | `+88.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4405.00` | 125,610,000.00 USD | 44,640.00 USD | 0.00 USD | `+88.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4415.00` | 125,620,000.00 USD | 11,480.00 USD | 0.00 USD | `+89.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4425.00` | 125,630,000.00 USD | 2,510.00 USD | 0.00 USD | `+89.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4435.00` | 125,800,000.00 USD | 177,400.00 USD | 0.00 USD | `+89.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4455.00` | 125,800,000.00 USD | 641.97 USD | 0.00 USD | `+90.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4465.00` | 125,800,000.00 USD | 1,030.00 USD | 0.00 USD | `+91.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4505.00` | 126,150,000.00 USD | 343,680.00 USD | 0.00 USD | `+92.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4515.00` | 126,150,000.00 USD | 2,280.00 USD | 0.00 USD | `+93.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4525.00` | 126,160,000.00 USD | 6,560.00 USD | 0.00 USD | `+93.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4565.00` | 126,260,000.00 USD | 97,750.00 USD | 0.00 USD | `+95.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4585.00` | 126,260,000.00 USD | 1,420.00 USD | 0.00 USD | `+96.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4595.00` | 126,260,000.00 USD | 2,610.00 USD | 0.00 USD | `+96.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4605.00` | 126,320,000.00 USD | 64,120.00 USD | 0.00 USD | `+97.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4645.00` | 126,350,000.00 USD | 27,410.00 USD | 0.00 USD | `+98.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4655.00` | 126,530,000.00 USD | 174,790.00 USD | 0.00 USD | `+99.28%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `2077.20` | 2,590,000,000.00 USD | 0.00 USD | 2,590,000,000.00 USD | 4,860,000.00 USD | 4,190,000.00 USD | 2,130,000.00 USD |
| `7D` | `2080.00` | 2,580,000,000.00 USD | 0.00 USD | 2,580,000,000.00 USD | 3,400,000.00 USD | 3,020,000.00 USD | 2,510,000.00 USD |
| `7D` | `2082.80` | 2,570,000,000.00 USD | 0.00 USD | 2,570,000,000.00 USD | 2,420,000.00 USD | 1,860,000.00 USD | 1,910,000.00 USD |
| `7D` | `2085.60` | 2,560,000,000.00 USD | 0.00 USD | 2,560,000,000.00 USD | 3,840,000.00 USD | 2,320,000.00 USD | 3,140,000.00 USD |
| `7D` | `2088.40` | 2,550,000,000.00 USD | 0.00 USD | 2,550,000,000.00 USD | 2,280,000.00 USD | 1,370,000.00 USD | 893,940.00 USD |
| `7D` | `2091.20` | 2,550,000,000.00 USD | 0.00 USD | 2,550,000,000.00 USD | 4,280,000.00 USD | 952,210.00 USD | 6,980,000.00 USD |
| `1D` | `2091.30` | 1,120,000,000.00 USD | 0.00 USD | 1,120,000,000.00 USD | 1,070,000.00 USD | 493,460.00 USD | 671,530.00 USD |
| `1D` | `2093.80` | 1,120,000,000.00 USD | 0.00 USD | 1,120,000,000.00 USD | 1,800,000.00 USD | 930,100.00 USD | 1,070,000.00 USD |
| `7D` | `2094.00` | 2,540,000,000.00 USD | 0.00 USD | 2,540,000,000.00 USD | 5,200,000.00 USD | 1,660,000.00 USD | 2,340,000.00 USD |
| `1D` | `2096.30` | 1,120,000,000.00 USD | 0.00 USD | 1,120,000,000.00 USD | 655,450.00 USD | 751,890.00 USD | 1,260,000.00 USD |
| `7D` | `2096.80` | 2,530,000,000.00 USD | 0.00 USD | 2,530,000,000.00 USD | 1,940,000.00 USD | 3,320,000.00 USD | 1,290,000.00 USD |
| `1D` | `2098.80` | 1,110,000,000.00 USD | 0.00 USD | 1,110,000,000.00 USD | 547,670.00 USD | 669,810.00 USD | 248,570.00 USD |
| `7D` | `2099.60` | 2,520,000,000.00 USD | 0.00 USD | 2,520,000,000.00 USD | 1,880,000.00 USD | 1,920,000.00 USD | 3,000,000.00 USD |
| `1D` | `2101.30` | 1,110,000,000.00 USD | 0.00 USD | 1,110,000,000.00 USD | 46,810.00 USD | 31,040.00 USD | 304,180.00 USD |
| `7D` | `2102.40` | 2,510,000,000.00 USD | 0.00 USD | 2,510,000,000.00 USD | 125,250.00 USD | 341,900.00 USD | 1,480,000.00 USD |
| `1D` | `2103.80` | 1,110,000,000.00 USD | 0.00 USD | 1,110,000,000.00 USD | 1,070,000.00 USD | 561,040.00 USD | 183,190.00 USD |
| `7D` | `2105.20` | 2,510,000,000.00 USD | 0.00 USD | 2,510,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,800,000.00 USD |
| `1D` | `2106.30` | 1,110,000,000.00 USD | 0.00 USD | 1,110,000,000.00 USD | 251,360.00 USD | 400,040.00 USD | 510,340.00 USD |
| `7D` | `2108.00` | 2,510,000,000.00 USD | 0.00 USD | 2,510,000,000.00 USD | 2,400,000.00 USD | 930,280.00 USD | 1,640,000.00 USD |
| `1D` | `2108.80` | 1,110,000,000.00 USD | 0.00 USD | 1,110,000,000.00 USD | 412,950.00 USD | 21,400.00 USD | 6,190.00 USD |
| `7D` | `2110.80` | 2,500,000,000.00 USD | 0.00 USD | 2,500,000,000.00 USD | 2,750,000.00 USD | 1,780,000.00 USD | 2,160,000.00 USD |
| `1D` | `2111.30` | 1,110,000,000.00 USD | 0.00 USD | 1,110,000,000.00 USD | 490,860.00 USD | 19,060.00 USD | 193,960.00 USD |
| `7D` | `2113.60` | 2,500,000,000.00 USD | 0.00 USD | 2,500,000,000.00 USD | 1,780,000.00 USD | 1,280,000.00 USD | 2,730,000.00 USD |
| `1D` | `2113.80` | 1,110,000,000.00 USD | 0.00 USD | 1,110,000,000.00 USD | 420,950.00 USD | 634,310.00 USD | 241,220.00 USD |
| `1D` | `2116.30` | 1,110,000,000.00 USD | 0.00 USD | 1,110,000,000.00 USD | 0.00 USD | 13,230.00 USD | 759,840.00 USD |
| `7D` | `2116.40` | 2,490,000,000.00 USD | 0.00 USD | 2,490,000,000.00 USD | 1,900,000.00 USD | 2,210,000.00 USD | 2,570,000.00 USD |
| `1D` | `2118.80` | 1,110,000,000.00 USD | 0.00 USD | 1,110,000,000.00 USD | 695,080.00 USD | 99,440.00 USD | 864,710.00 USD |
| `7D` | `2119.20` | 2,480,000,000.00 USD | 0.00 USD | 2,480,000,000.00 USD | 2,920,000.00 USD | 750,810.00 USD | 2,590,000.00 USD |
| `1D` | `2121.30` | 1,100,000,000.00 USD | 0.00 USD | 1,100,000,000.00 USD | 916,680.00 USD | 846,370.00 USD | 777,680.00 USD |
| `7D` | `2122.00` | 2,480,000,000.00 USD | 0.00 USD | 2,480,000,000.00 USD | 2,300,000.00 USD | 1,020,000.00 USD | 1,630,000.00 USD |
| `1D` | `2123.80` | 1,100,000,000.00 USD | 0.00 USD | 1,100,000,000.00 USD | 966,890.00 USD | 854,260.00 USD | 996,930.00 USD |
| `7D` | `2124.80` | 2,470,000,000.00 USD | 0.00 USD | 2,470,000,000.00 USD | 2,680,000.00 USD | 939,650.00 USD | 1,790,000.00 USD |
| `1D` | `2126.30` | 1,100,000,000.00 USD | 0.00 USD | 1,100,000,000.00 USD | 58,860.00 USD | 841,670.00 USD | 628,390.00 USD |
| `7D` | `2127.60` | 2,470,000,000.00 USD | 0.00 USD | 2,470,000,000.00 USD | 514,750.00 USD | 2,620,000.00 USD | 2,480,000.00 USD |
| `1D` | `2128.80` | 1,100,000,000.00 USD | 0.00 USD | 1,100,000,000.00 USD | 356,740.00 USD | 475,750.00 USD | 323,070.00 USD |
| `7D` | `2130.40` | 2,460,000,000.00 USD | 0.00 USD | 2,460,000,000.00 USD | 2,040,000.00 USD | 2,130,000.00 USD | 1,690,000.00 USD |
| `1D` | `2131.30` | 1,100,000,000.00 USD | 0.00 USD | 1,100,000,000.00 USD | 0.00 USD | 644,330.00 USD | 336,530.00 USD |
| `7D` | `2133.20` | 2,460,000,000.00 USD | 0.00 USD | 2,460,000,000.00 USD | 1,930,000.00 USD | 715,940.00 USD | 323,430.00 USD |
| `1D` | `2133.80` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 187,520.00 USD | 497,320.00 USD | 0.00 USD |
| `7D` | `2136.00` | 2,450,000,000.00 USD | 0.00 USD | 2,450,000,000.00 USD | 1,370,000.00 USD | 596,290.00 USD | 18,020.00 USD |
| `1D` | `2136.30` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 0.00 USD | 294,600.00 USD | 2,870.00 USD |
| `1D` | `2138.80` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 555,320.00 USD | 250,240.00 USD | 205,180.00 USD |
| `7D` | `2138.80` | 2,450,000,000.00 USD | 0.00 USD | 2,450,000,000.00 USD | 1,110,000.00 USD | 1,250,000.00 USD | 60,730.00 USD |
| `7D` | `2141.60` | 2,450,000,000.00 USD | 0.00 USD | 2,450,000,000.00 USD | 1,550,000.00 USD | 209,240.00 USD | 766,720.00 USD |
| `1D` | `2143.80` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 295,510.00 USD | 16,700.00 USD | 3,100.00 USD |
| `7D` | `2144.40` | 2,450,000,000.00 USD | 0.00 USD | 2,450,000,000.00 USD | 465,960.00 USD | 1,530,000.00 USD | 268,500.00 USD |
| `1D` | `2146.30` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 0.00 USD | 11,090.00 USD | 207,420.00 USD |
| `7D` | `2147.20` | 2,440,000,000.00 USD | 0.00 USD | 2,440,000,000.00 USD | 239,110.00 USD | 10,850.00 USD | 0.00 USD |
| `1D` | `2148.80` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 251,250.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2150.00` | 2,440,000,000.00 USD | 0.00 USD | 2,440,000,000.00 USD | 459,630.00 USD | 463,640.00 USD | 31,040.00 USD |
| `7D` | `2152.80` | 2,440,000,000.00 USD | 0.00 USD | 2,440,000,000.00 USD | 29,510.00 USD | 331,520.00 USD | 0.00 USD |
| `7D` | `2155.60` | 2,440,000,000.00 USD | 0.00 USD | 2,440,000,000.00 USD | 157,380.00 USD | 430,180.00 USD | 66,320.00 USD |
| `7D` | `2158.40` | 2,440,000,000.00 USD | 0.00 USD | 2,440,000,000.00 USD | 687,180.00 USD | 1,010,000.00 USD | 1,590,000.00 USD |
| `7D` | `2161.20` | 2,440,000,000.00 USD | 0.00 USD | 2,440,000,000.00 USD | 1,490,000.00 USD | 1,050,000.00 USD | 2,240,000.00 USD |
| `7D` | `2164.00` | 2,430,000,000.00 USD | 0.00 USD | 2,430,000,000.00 USD | 36,870.00 USD | 329,690.00 USD | 409,110.00 USD |
| `7D` | `2166.80` | 2,430,000,000.00 USD | 0.00 USD | 2,430,000,000.00 USD | 25,540.00 USD | 0.00 USD | 68,110.00 USD |
| `7D` | `2169.60` | 2,430,000,000.00 USD | 0.00 USD | 2,430,000,000.00 USD | 1,700,000.00 USD | 726,240.00 USD | 810,540.00 USD |
| `7D` | `2172.40` | 2,430,000,000.00 USD | 0.00 USD | 2,430,000,000.00 USD | 479,540.00 USD | 1,150,000.00 USD | 0.00 USD |
| `7D` | `2194.80` | 2,430,000,000.00 USD | 0.00 USD | 2,430,000,000.00 USD | 141,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2197.60` | 2,430,000,000.00 USD | 0.00 USD | 2,430,000,000.00 USD | 2,440,000.00 USD | 3,270,000.00 USD | 0.00 USD |
| `7D` | `2200.40` | 2,420,000,000.00 USD | 0.00 USD | 2,420,000,000.00 USD | 3,000,000.00 USD | 3,140,000.00 USD | 3,200,000.00 USD |
| `1D` | `2201.30` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 284,470.00 USD | 217,490.00 USD | 225,330.00 USD |
| `7D` | `2203.20` | 2,410,000,000.00 USD | 0.00 USD | 2,410,000,000.00 USD | 3,240,000.00 USD | 624,500.00 USD | 2,720,000.00 USD |
| `1D` | `2203.80` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 1,050,000.00 USD | 207,110.00 USD | 755,300.00 USD |
| `7D` | `2206.00` | 2,410,000,000.00 USD | 0.00 USD | 2,410,000,000.00 USD | 6,050,000.00 USD | 4,010,000.00 USD | 4,980,000.00 USD |
| `1D` | `2206.30` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 611,820.00 USD | 2,270,000.00 USD | 722,570.00 USD |
| `1D` | `2208.80` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 2,490,000.00 USD | 668,670.00 USD | 3,050,000.00 USD |
| `7D` | `2208.80` | 2,390,000,000.00 USD | 0.00 USD | 2,390,000,000.00 USD | 10,060,000.00 USD | 7,030,000.00 USD | 3,080,000.00 USD |
| `1D` | `2211.30` | 1,080,000,000.00 USD | 0.00 USD | 1,080,000,000.00 USD | 2,770,000.00 USD | 1,250,000.00 USD | 573,370.00 USD |
| `7D` | `2211.60` | 2,370,000,000.00 USD | 0.00 USD | 2,370,000,000.00 USD | 8,410,000.00 USD | 7,020,000.00 USD | 7,930,000.00 USD |
| `1D` | `2213.80` | 1,070,000,000.00 USD | 0.00 USD | 1,070,000,000.00 USD | 3,890,000.00 USD | 2,980,000.00 USD | 2,910,000.00 USD |
| `7D` | `2214.40` | 2,350,000,000.00 USD | 0.00 USD | 2,350,000,000.00 USD | 12,890,000.00 USD | 12,380,000.00 USD | 9,100,000.00 USD |
| `1D` | `2216.30` | 1,060,000,000.00 USD | 0.00 USD | 1,060,000,000.00 USD | 6,130,000.00 USD | 6,230,000.00 USD | 4,430,000.00 USD |
| `7D` | `2217.20` | 2,310,000,000.00 USD | 0.00 USD | 2,310,000,000.00 USD | 16,020,000.00 USD | 10,280,000.00 USD | 8,240,000.00 USD |
| `1D` | `2218.80` | 1,050,000,000.00 USD | 0.00 USD | 1,050,000,000.00 USD | 4,630,000.00 USD | 3,610,000.00 USD | 1,160,000.00 USD |
| `7D` | `2220.00` | 2,280,000,000.00 USD | 0.00 USD | 2,280,000,000.00 USD | 12,900,000.00 USD | 10,310,000.00 USD | 3,040,000.00 USD |
| `1D` | `2221.30` | 1,040,000,000.00 USD | 0.00 USD | 1,040,000,000.00 USD | 1,750,000.00 USD | 2,050,000.00 USD | 733,440.00 USD |
| `7D` | `2222.80` | 2,250,000,000.00 USD | 0.00 USD | 2,250,000,000.00 USD | 5,190,000.00 USD | 5,430,000.00 USD | 8,890,000.00 USD |
| `1D` | `2223.80` | 1,030,000,000.00 USD | 0.00 USD | 1,030,000,000.00 USD | 4,950,000.00 USD | 4,260,000.00 USD | 3,170,000.00 USD |
| `7D` | `2225.60` | 2,230,000,000.00 USD | 0.00 USD | 2,230,000,000.00 USD | 13,090,000.00 USD | 13,590,000.00 USD | 9,460,000.00 USD |
| `1D` | `2226.30` | 1,020,000,000.00 USD | 0.00 USD | 1,020,000,000.00 USD | 5,340,000.00 USD | 4,790,000.00 USD | 2,190,000.00 USD |
| `7D` | `2228.40` | 2,200,000,000.00 USD | 0.00 USD | 2,200,000,000.00 USD | 7,680,000.00 USD | 5,550,000.00 USD | 8,240,000.00 USD |
| `1D` | `2228.80` | 1,010,000,000.00 USD | 0.00 USD | 1,010,000,000.00 USD | 2,720,000.00 USD | 1,580,000.00 USD | 812,110.00 USD |
| `7D` | `2231.20` | 2,170,000,000.00 USD | 0.00 USD | 2,170,000,000.00 USD | 9,590,000.00 USD | 2,970,000.00 USD | 16,200,000.00 USD |
| `1D` | `2231.30` | 1,000,000,000.00 USD | 0.00 USD | 1,000,000,000.00 USD | 3,330,000.00 USD | 2,610,000.00 USD | 3,070,000.00 USD |
| `1D` | `2233.80` | 995,370,000.00 USD | 0.00 USD | 995,370,000.00 USD | 6,920,000.00 USD | 3,770,000.00 USD | 3,680,000.00 USD |
| `7D` | `2234.00` | 2,150,000,000.00 USD | 0.00 USD | 2,150,000,000.00 USD | 18,760,000.00 USD | 10,880,000.00 USD | 6,070,000.00 USD |
| `1D` | `2236.30` | 981,000,000.00 USD | 0.00 USD | 981,000,000.00 USD | 2,430,000.00 USD | 2,100,000.00 USD | 3,770,000.00 USD |
| `7D` | `2236.80` | 2,110,000,000.00 USD | 0.00 USD | 2,110,000,000.00 USD | 6,910,000.00 USD | 11,270,000.00 USD | 5,890,000.00 USD |
| `1D` | `2238.80` | 972,700,000.00 USD | 0.00 USD | 972,700,000.00 USD | 1,580,000.00 USD | 2,180,000.00 USD | 844,590.00 USD |
| `7D` | `2239.60` | 2,090,000,000.00 USD | 0.00 USD | 2,090,000,000.00 USD | 6,630,000.00 USD | 7,850,000.00 USD | 8,430,000.00 USD |
| `1D` | `2241.30` | 968,090,000.00 USD | 0.00 USD | 968,090,000.00 USD | 456,710.00 USD | 542,280.00 USD | 740,930.00 USD |
| `7D` | `2242.40` | 2,060,000,000.00 USD | 0.00 USD | 2,060,000,000.00 USD | 4,840,000.00 USD | 1,890,000.00 USD | 4,750,000.00 USD |
| `1D` | `2243.80` | 966,350,000.00 USD | 0.00 USD | 966,350,000.00 USD | 1,520,000.00 USD | 1,590,000.00 USD | 991,710.00 USD |
| `7D` | `2245.20` | 2,050,000,000.00 USD | 0.00 USD | 2,050,000,000.00 USD | 16,830,000.00 USD | 13,940,000.00 USD | 11,660,000.00 USD |
| `1D` | `2246.30` | 962,250,000.00 USD | 0.00 USD | 962,250,000.00 USD | 2,730,000.00 USD | 2,020,000.00 USD | 1,910,000.00 USD |
| `7D` | `2248.00` | 2,010,000,000.00 USD | 0.00 USD | 2,010,000,000.00 USD | 13,600,000.00 USD | 6,140,000.00 USD | 10,080,000.00 USD |
| `1D` | `2248.80` | 955,590,000.00 USD | 0.00 USD | 955,590,000.00 USD | 4,450,000.00 USD | 601,150.00 USD | 1,730,000.00 USD |
| `7D` | `2250.80` | 1,980,000,000.00 USD | 0.00 USD | 1,980,000,000.00 USD | 10,570,000.00 USD | 10,480,000.00 USD | 8,150,000.00 USD |
| `1D` | `2251.30` | 948,810,000.00 USD | 0.00 USD | 948,810,000.00 USD | 304,760.00 USD | 1,060,000.00 USD | 1,900,000.00 USD |
| `7D` | `2253.60` | 1,950,000,000.00 USD | 0.00 USD | 1,950,000,000.00 USD | 24,760,000.00 USD | 21,020,000.00 USD | 21,780,000.00 USD |
| `1D` | `2253.80` | 945,540,000.00 USD | 0.00 USD | 945,540,000.00 USD | 8,560,000.00 USD | 6,780,000.00 USD | 5,710,000.00 USD |
| `1D` | `2256.30` | 924,500,000.00 USD | 0.00 USD | 924,500,000.00 USD | 3,260,000.00 USD | 2,970,000.00 USD | 3,870,000.00 USD |
| `7D` | `2256.40` | 1,880,000,000.00 USD | 0.00 USD | 1,880,000,000.00 USD | 31,260,000.00 USD | 19,360,000.00 USD | 15,540,000.00 USD |
| `1D` | `2258.80` | 914,390,000.00 USD | 0.00 USD | 914,390,000.00 USD | 6,260,000.00 USD | 2,980,000.00 USD | 4,540,000.00 USD |
| `7D` | `2259.20` | 1,820,000,000.00 USD | 0.00 USD | 1,820,000,000.00 USD | 24,810,000.00 USD | 20,200,000.00 USD | 22,950,000.00 USD |
| `1D` | `2261.30` | 900,610,000.00 USD | 0.00 USD | 900,610,000.00 USD | 12,710,000.00 USD | 12,030,000.00 USD | 13,110,000.00 USD |
| `7D` | `2262.00` | 1,750,000,000.00 USD | 0.00 USD | 1,750,000,000.00 USD | 45,920,000.00 USD | 30,170,000.00 USD | 22,490,000.00 USD |
| `1D` | `2263.80` | 862,760,000.00 USD | 0.00 USD | 862,760,000.00 USD | 12,170,000.00 USD | 11,500,000.00 USD | 7,520,000.00 USD |
| `7D` | `2264.80` | 1,650,000,000.00 USD | 0.00 USD | 1,650,000,000.00 USD | 30,210,000.00 USD | 26,720,000.00 USD | 18,300,000.00 USD |
| `1D` | `2266.30` | 831,570,000.00 USD | 0.00 USD | 831,570,000.00 USD | 11,310,000.00 USD | 12,590,000.00 USD | 3,380,000.00 USD |
| `7D` | `2267.60` | 1,570,000,000.00 USD | 0.00 USD | 1,570,000,000.00 USD | 40,210,000.00 USD | 41,610,000.00 USD | 31,060,000.00 USD |
| `1D` | `2268.80` | 804,280,000.00 USD | 0.00 USD | 804,280,000.00 USD | 14,280,000.00 USD | 9,540,000.00 USD | 7,840,000.00 USD |
| `7D` | `2270.40` | 1,460,000,000.00 USD | 0.00 USD | 1,460,000,000.00 USD | 46,080,000.00 USD | 25,460,000.00 USD | 39,210,000.00 USD |
| `1D` | `2271.30` | 772,630,000.00 USD | 0.00 USD | 772,630,000.00 USD | 4,880,000.00 USD | 8,750,000.00 USD | 6,540,000.00 USD |
| `7D` | `2273.20` | 1,350,000,000.00 USD | 0.00 USD | 1,350,000,000.00 USD | 26,430,000.00 USD | 25,760,000.00 USD | 20,220,000.00 USD |
| `1D` | `2273.80` | 752,450,000.00 USD | 0.00 USD | 752,450,000.00 USD | 15,670,000.00 USD | 9,050,000.00 USD | 5,570,000.00 USD |
| `7D` | `2276.00` | 1,280,000,000.00 USD | 0.00 USD | 1,280,000,000.00 USD | 52,620,000.00 USD | 46,680,000.00 USD | 45,920,000.00 USD |
| `1D` | `2276.30` | 722,160,000.00 USD | 0.00 USD | 722,160,000.00 USD | 15,330,000.00 USD | 14,330,000.00 USD | 12,950,000.00 USD |
| `1D` | `2278.80` | 679,540,000.00 USD | 0.00 USD | 679,540,000.00 USD | 18,640,000.00 USD | 9,000,000.00 USD | 13,280,000.00 USD |
| `7D` | `2278.80` | 1,130,000,000.00 USD | 0.00 USD | 1,130,000,000.00 USD | 69,920,000.00 USD | 30,780,000.00 USD | 43,080,000.00 USD |
| `1D` | `2281.30` | 638,620,000.00 USD | 0.00 USD | 638,620,000.00 USD | 20,900,000.00 USD | 13,540,000.00 USD | 14,590,000.00 USD |
| `7D` | `2281.60` | 989,680,000.00 USD | 0.00 USD | 989,680,000.00 USD | 61,930,000.00 USD | 60,060,000.00 USD | 46,590,000.00 USD |
| `1D` | `2283.80` | 589,590,000.00 USD | 0.00 USD | 589,590,000.00 USD | 29,350,000.00 USD | 22,160,000.00 USD | 22,940,000.00 USD |
| `7D` | `2284.40` | 821,100,000.00 USD | 0.00 USD | 821,100,000.00 USD | 84,440,000.00 USD | 69,880,000.00 USD | 44,650,000.00 USD |
| `1D` | `2286.30` | 515,140,000.00 USD | 0.00 USD | 515,140,000.00 USD | 18,110,000.00 USD | 24,680,000.00 USD | 10,700,000.00 USD |
| `7D` | `2287.20` | 622,130,000.00 USD | 0.00 USD | 622,130,000.00 USD | 59,100,000.00 USD | 55,220,000.00 USD | 44,250,000.00 USD |
| `1D` | `2288.80` | 461,650,000.00 USD | 0.00 USD | 461,650,000.00 USD | 17,050,000.00 USD | 15,760,000.00 USD | 5,820,000.00 USD |
| `7D` | `2290.00` | 463,560,000.00 USD | 0.00 USD | 463,560,000.00 USD | 49,600,000.00 USD | 34,580,000.00 USD | 24,320,000.00 USD |
| `1D` | `2291.30` | 423,020,000.00 USD | 0.00 USD | 423,020,000.00 USD | 16,070,000.00 USD | 18,680,000.00 USD | 5,320,000.00 USD |
| `7D` | `2292.80` | 355,060,000.00 USD | 0.00 USD | 355,060,000.00 USD | 38,470,000.00 USD | 20,900,000.00 USD | 42,370,000.00 USD |
| `1D` | `2293.80` | 382,940,000.00 USD | 0.00 USD | 382,940,000.00 USD | 19,790,000.00 USD | 13,900,000.00 USD | 14,840,000.00 USD |
| `7D` | `2295.60` | 253,330,000.00 USD | 0.00 USD | 253,330,000.00 USD | 17,510,000.00 USD | 8,110,000.00 USD | 6,790,000.00 USD |
| `1D` | `2296.30` | 334,420,000.00 USD | 0.00 USD | 334,420,000.00 USD | 20,750,000.00 USD | 10,930,000.00 USD | 6,530,000.00 USD |
| `7D` | `2298.40` | 220,910,000.00 USD | 0.00 USD | 220,910,000.00 USD | 2,090,000.00 USD | 5,820,000.00 USD | 301,550.00 USD |
| `1D` | `2298.80` | 296,200,000.00 USD | 0.00 USD | 296,200,000.00 USD | 10,060,000.00 USD | 8,310,000.00 USD | 3,540,000.00 USD |
| `7D` | `2301.20` | 212,700,000.00 USD | 0.00 USD | 212,700,000.00 USD | 11,790,000.00 USD | 2,120,000.00 USD | 7,590,000.00 USD |
| `1D` | `2301.30` | 274,290,000.00 USD | 0.00 USD | 274,290,000.00 USD | 17,220,000.00 USD | 11,670,000.00 USD | 12,350,000.00 USD |
| `1D` | `2303.80` | 233,060,000.00 USD | 0.00 USD | 233,060,000.00 USD | 27,640,000.00 USD | 15,560,000.00 USD | 16,510,000.00 USD |
| `7D` | `2304.00` | 191,200,000.00 USD | 0.00 USD | 191,200,000.00 USD | 32,960,000.00 USD | 17,170,000.00 USD | 13,270,000.00 USD |
| `1D` | `2306.30` | 173,340,000.00 USD | 0.00 USD | 173,340,000.00 USD | 6,150,000.00 USD | 5,110,000.00 USD | 16,460,000.00 USD |
| `7D` | `2306.80` | 127,800,000.00 USD | 0.00 USD | 127,800,000.00 USD | 0.00 USD | 3,740,000.00 USD | 11,030,000.00 USD |
| `1D` | `2308.80` | 145,620,000.00 USD | 0.00 USD | 145,620,000.00 USD | 1,370,000.00 USD | 2,120,000.00 USD | 2,540,000.00 USD |
| `7D` | `2309.60` | 113,040,000.00 USD | 0.00 USD | 113,040,000.00 USD | 282,530.00 USD | 300,580.00 USD | 1,500,000.00 USD |
| `1D` | `2311.30` | 139,580,000.00 USD | 0.00 USD | 139,580,000.00 USD | 8,550,000.00 USD | 5,190,000.00 USD | 6,850,000.00 USD |
| `7D` | `2312.40` | 110,950,000.00 USD | 0.00 USD | 110,950,000.00 USD | 6,560,000.00 USD | 640,510.00 USD | 2,500,000.00 USD |
| `1D` | `2313.80` | 118,990,000.00 USD | 0.00 USD | 118,990,000.00 USD | 6,160,000.00 USD | 6,220,000.00 USD | 5,430,000.00 USD |
| `7D` | `2315.20` | 101,250,000.00 USD | 0.00 USD | 101,250,000.00 USD | 5,020,000.00 USD | 7,520,000.00 USD | 117,510.00 USD |
| `1D` | `2316.30` | 101,180,000.00 USD | 0.00 USD | 101,180,000.00 USD | 10,440,000.00 USD | 11,520,000.00 USD | 5,830,000.00 USD |
| `7D` | `2318.00` | 88,590,000.00 USD | 0.00 USD | 88,590,000.00 USD | 817,040.00 USD | 3,010,000.00 USD | 0.00 USD |
| `1D` | `2318.80` | 73,380,000.00 USD | 0.00 USD | 73,380,000.00 USD | 11,680,000.00 USD | 4,080,000.00 USD | 2,250,000.00 USD |
| `7D` | `2320.80` | 84,770,000.00 USD | 0.00 USD | 84,770,000.00 USD | 0.00 USD | 2,960,000.00 USD | 0.00 USD |
| `1D` | `2321.30` | 55,370,000.00 USD | 0.00 USD | 55,370,000.00 USD | 255,100.00 USD | 2,970,000.00 USD | 1,720,000.00 USD |
| `7D` | `2323.60` | 81,810,000.00 USD | 0.00 USD | 81,810,000.00 USD | 4,070,000.00 USD | 2,210,000.00 USD | 0.00 USD |
| `1D` | `2323.80` | 50,420,000.00 USD | 0.00 USD | 50,420,000.00 USD | 8,620,000.00 USD | 2,890,000.00 USD | 2,210,000.00 USD |
| `1D` | `2326.30` | 36,690,000.00 USD | 0.00 USD | 36,690,000.00 USD | 0.00 USD | 2,910,000.00 USD | 66,960.00 USD |
| `7D` | `2326.40` | 75,530,000.00 USD | 0.00 USD | 75,530,000.00 USD | 0.00 USD | 0.00 USD | 126,530.00 USD |
| `1D` | `2328.80` | 33,720,000.00 USD | 0.00 USD | 33,720,000.00 USD | 1,890,000.00 USD | 1,150,000.00 USD | 237,640.00 USD |
| `7D` | `2329.20` | 75,400,000.00 USD | 0.00 USD | 75,400,000.00 USD | 3,860,000.00 USD | 0.00 USD | 4,880,000.00 USD |
| `1D` | `2331.30` | 30,440,000.00 USD | 0.00 USD | 30,440,000.00 USD | 13,200,000.00 USD | 0.00 USD | 126,990.00 USD |
| `7D` | `2332.00` | 66,660,000.00 USD | 0.00 USD | 66,660,000.00 USD | 29,230,000.00 USD | 0.00 USD | 2,810,000.00 USD |
| `1D` | `2333.80` | 17,110,000.00 USD | 0.00 USD | 17,110,000.00 USD | 3,620,000.00 USD | 12,110,000.00 USD | 1,380,000.00 USD |
| `7D` | `2334.80` | 34,610,000.00 USD | 0.00 USD | 34,610,000.00 USD | 7,260,000.00 USD | 18,420,000.00 USD | 8,930,000.00 USD |
| `7D` | `2335.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2335.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2336.30` | 7,590,000.00 USD | 7,590,000.00 USD | 0.00 USD | 7,590,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2337.60` | 23,130,000.00 USD | 23,130,000.00 USD | 0.00 USD | 9,570,000.00 USD | 0.00 USD | 13,560,000.00 USD |
| `1D` | `2338.80` | 9,010,000.00 USD | 9,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,420,000.00 USD |
| `7D` | `2340.40` | 36,520,000.00 USD | 36,520,000.00 USD | 0.00 USD | 0.00 USD | 10,010,000.00 USD | 3,380,000.00 USD |
| `7D` | `2343.20` | 45,900,000.00 USD | 45,900,000.00 USD | 0.00 USD | 0.00 USD | 5,540,000.00 USD | 3,840,000.00 USD |
| `1D` | `2343.80` | 17,240,000.00 USD | 17,240,000.00 USD | 0.00 USD | 0.00 USD | 1,960,000.00 USD | 6,270,000.00 USD |
| `7D` | `2346.00` | 66,650,000.00 USD | 66,650,000.00 USD | 0.00 USD | 0.00 USD | 7,920,000.00 USD | 12,830,000.00 USD |
| `1D` | `2346.30` | 22,790,000.00 USD | 22,790,000.00 USD | 0.00 USD | 1,130,000.00 USD | 0.00 USD | 4,420,000.00 USD |
| `1D` | `2348.80` | 29,530,000.00 USD | 29,530,000.00 USD | 0.00 USD | 5,710,000.00 USD | 42,760.00 USD | 990,800.00 USD |
| `7D` | `2348.80` | 85,130,000.00 USD | 85,130,000.00 USD | 0.00 USD | 495,290.00 USD | 7,240,000.00 USD | 10,750,000.00 USD |
| `1D` | `2351.30` | 59,850,000.00 USD | 59,850,000.00 USD | 0.00 USD | 21,660,000.00 USD | 2,630,000.00 USD | 6,020,000.00 USD |
| `7D` | `2351.60` | 109,340,000.00 USD | 109,340,000.00 USD | 0.00 USD | 572,980.00 USD | 17,950,000.00 USD | 5,680,000.00 USD |
| `1D` | `2353.80` | 70,290,000.00 USD | 70,290,000.00 USD | 0.00 USD | 858,830.00 USD | 9,490,000.00 USD | 90,430.00 USD |
| `7D` | `2354.40` | 150,580,000.00 USD | 150,580,000.00 USD | 0.00 USD | 6,120,000.00 USD | 34,750,000.00 USD | 371,510.00 USD |
| `1D` | `2356.30` | 81,690,000.00 USD | 81,690,000.00 USD | 0.00 USD | 2,090,000.00 USD | 7,920,000.00 USD | 1,400,000.00 USD |
| `7D` | `2357.20` | 164,960,000.00 USD | 164,960,000.00 USD | 0.00 USD | 8,470,000.00 USD | 5,920,000.00 USD | 0.00 USD |
| `1D` | `2358.80` | 90,660,000.00 USD | 90,660,000.00 USD | 0.00 USD | 74,690.00 USD | 3,010,000.00 USD | 5,880,000.00 USD |
| `7D` | `2360.00` | 174,680,000.00 USD | 174,680,000.00 USD | 0.00 USD | 6,300,000.00 USD | 3,430,000.00 USD | 0.00 USD |
| `1D` | `2361.30` | 103,450,000.00 USD | 103,450,000.00 USD | 0.00 USD | 4,190,000.00 USD | 8,350,000.00 USD | 261,260.00 USD |
| `7D` | `2362.80` | 177,560,000.00 USD | 177,560,000.00 USD | 0.00 USD | 1,180,000.00 USD | 0.00 USD | 1,690,000.00 USD |
| `1D` | `2363.80` | 115,860,000.00 USD | 115,860,000.00 USD | 0.00 USD | 4,890,000.00 USD | 3,710,000.00 USD | 3,810,000.00 USD |
| `7D` | `2365.60` | 185,560,000.00 USD | 185,560,000.00 USD | 0.00 USD | 6,340,000.00 USD | 0.00 USD | 1,660,000.00 USD |
| `1D` | `2366.30` | 116,230,000.00 USD | 116,230,000.00 USD | 0.00 USD | 192,950.00 USD | 0.00 USD | 171,590.00 USD |
| `7D` | `2368.40` | 196,030,000.00 USD | 196,030,000.00 USD | 0.00 USD | 9,590,000.00 USD | 475,460.00 USD | 404,380.00 USD |
| `1D` | `2368.80` | 129,510,000.00 USD | 129,510,000.00 USD | 0.00 USD | 8,900,000.00 USD | 3,260,000.00 USD | 1,130,000.00 USD |
| `7D` | `2371.20` | 258,470,000.00 USD | 258,470,000.00 USD | 0.00 USD | 16,760,000.00 USD | 0.00 USD | 45,680,000.00 USD |
| `1D` | `2371.30` | 166,930,000.00 USD | 166,930,000.00 USD | 0.00 USD | 15,980,000.00 USD | 12,950,000.00 USD | 8,490,000.00 USD |
| `1D` | `2373.80` | 187,400,000.00 USD | 187,400,000.00 USD | 0.00 USD | 13,540,000.00 USD | 1,040,000.00 USD | 5,890,000.00 USD |
| `7D` | `2374.00` | 280,480,000.00 USD | 280,480,000.00 USD | 0.00 USD | 15,830,000.00 USD | 121,480.00 USD | 6,050,000.00 USD |
| `1D` | `2376.30` | 211,760,000.00 USD | 211,760,000.00 USD | 0.00 USD | 11,340,000.00 USD | 3,120,000.00 USD | 9,900,000.00 USD |
| `7D` | `2376.80` | 320,690,000.00 USD | 320,690,000.00 USD | 0.00 USD | 12,140,000.00 USD | 5,950,000.00 USD | 22,120,000.00 USD |
| `1D` | `2378.80` | 239,880,000.00 USD | 239,880,000.00 USD | 0.00 USD | 5,000,000.00 USD | 12,440,000.00 USD | 10,670,000.00 USD |
| `7D` | `2379.60` | 348,000,000.00 USD | 348,000,000.00 USD | 0.00 USD | 7,180,000.00 USD | 2,580,000.00 USD | 17,560,000.00 USD |
| `1D` | `2381.30` | 283,540,000.00 USD | 283,540,000.00 USD | 0.00 USD | 14,790,000.00 USD | 11,660,000.00 USD | 17,210,000.00 USD |
| `7D` | `2382.40` | 390,210,000.00 USD | 390,210,000.00 USD | 0.00 USD | 8,510,000.00 USD | 12,380,000.00 USD | 21,320,000.00 USD |
| `1D` | `2383.80` | 330,580,000.00 USD | 330,580,000.00 USD | 0.00 USD | 20,120,000.00 USD | 16,140,000.00 USD | 10,780,000.00 USD |
| `7D` | `2385.20` | 489,090,000.00 USD | 489,090,000.00 USD | 0.00 USD | 17,480,000.00 USD | 30,700,000.00 USD | 50,710,000.00 USD |
| `1D` | `2386.30` | 369,760,000.00 USD | 369,760,000.00 USD | 0.00 USD | 13,990,000.00 USD | 15,160,000.00 USD | 10,030,000.00 USD |
| `7D` | `2388.00` | 562,530,000.00 USD | 562,530,000.00 USD | 0.00 USD | 4,540,000.00 USD | 34,290,000.00 USD | 34,610,000.00 USD |
| `1D` | `2388.80` | 393,020,000.00 USD | 393,020,000.00 USD | 0.00 USD | 11,070,000.00 USD | 5,020,000.00 USD | 7,180,000.00 USD |
| `7D` | `2390.80` | 660,760,000.00 USD | 660,760,000.00 USD | 0.00 USD | 5,470,000.00 USD | 44,170,000.00 USD | 48,590,000.00 USD |
| `1D` | `2391.30` | 415,200,000.00 USD | 415,200,000.00 USD | 0.00 USD | 3,340,000.00 USD | 11,960,000.00 USD | 6,880,000.00 USD |
| `7D` | `2393.60` | 759,660,000.00 USD | 759,660,000.00 USD | 0.00 USD | 44,040,000.00 USD | 23,140,000.00 USD | 31,720,000.00 USD |
| `1D` | `2393.80` | 439,560,000.00 USD | 439,560,000.00 USD | 0.00 USD | 10,210,000.00 USD | 10,400,000.00 USD | 3,750,000.00 USD |
| `1D` | `2396.30` | 450,850,000.00 USD | 450,850,000.00 USD | 0.00 USD | 2,630,000.00 USD | 4,140,000.00 USD | 4,530,000.00 USD |
| `7D` | `2396.40` | 847,020,000.00 USD | 847,020,000.00 USD | 0.00 USD | 29,670,000.00 USD | 34,800,000.00 USD | 22,890,000.00 USD |
| `1D` | `2398.80` | 485,560,000.00 USD | 485,560,000.00 USD | 0.00 USD | 12,530,000.00 USD | 11,030,000.00 USD | 11,140,000.00 USD |
| `7D` | `2399.20` | 939,540,000.00 USD | 939,540,000.00 USD | 0.00 USD | 41,690,000.00 USD | 31,030,000.00 USD | 19,790,000.00 USD |
| `1D` | `2401.30` | 508,420,000.00 USD | 508,420,000.00 USD | 0.00 USD | 7,850,000.00 USD | 7,800,000.00 USD | 7,210,000.00 USD |
| `7D` | `2402.00` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 51,500,000.00 USD | 23,600,000.00 USD | 30,780,000.00 USD |
| `1D` | `2403.80` | 537,340,000.00 USD | 537,340,000.00 USD | 0.00 USD | 12,130,000.00 USD | 9,550,000.00 USD | 7,230,000.00 USD |
| `7D` | `2404.80` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 36,380,000.00 USD | 25,660,000.00 USD | 15,080,000.00 USD |
| `1D` | `2406.30` | 563,240,000.00 USD | 563,240,000.00 USD | 0.00 USD | 11,630,000.00 USD | 7,530,000.00 USD | 6,750,000.00 USD |
| `7D` | `2407.60` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 26,430,000.00 USD | 30,520,000.00 USD | 18,910,000.00 USD |
| `1D` | `2408.80` | 592,770,000.00 USD | 592,770,000.00 USD | 0.00 USD | 7,930,000.00 USD | 12,550,000.00 USD | 9,050,000.00 USD |
| `7D` | `2410.40` | 1,270,000,000.00 USD | 1,270,000,000.00 USD | 0.00 USD | 22,760,000.00 USD | 27,140,000.00 USD | 24,200,000.00 USD |
| `1D` | `2411.30` | 615,630,000.00 USD | 615,630,000.00 USD | 0.00 USD | 11,090,000.00 USD | 7,730,000.00 USD | 4,040,000.00 USD |
| `7D` | `2413.20` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 0.00 USD | 13,250,000.00 USD | 13,960,000.00 USD | 12,550,000.00 USD |
| `1D` | `2413.80` | 623,750,000.00 USD | 623,750,000.00 USD | 0.00 USD | 4,070,000.00 USD | 1,390,000.00 USD | 2,670,000.00 USD |
| `7D` | `2416.00` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 27,740,000.00 USD | 17,520,000.00 USD | 32,340,000.00 USD |
| `1D` | `2416.30` | 640,050,000.00 USD | 640,050,000.00 USD | 0.00 USD | 4,650,000.00 USD | 7,220,000.00 USD | 4,440,000.00 USD |
| `1D` | `2418.80` | 650,170,000.00 USD | 650,170,000.00 USD | 0.00 USD | 3,840,000.00 USD | 3,140,000.00 USD | 3,140,000.00 USD |
| `7D` | `2418.80` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 0.00 USD | 27,450,000.00 USD | 16,840,000.00 USD | 12,150,000.00 USD |
| `1D` | `2421.30` | 667,980,000.00 USD | 667,980,000.00 USD | 0.00 USD | 6,170,000.00 USD | 5,620,000.00 USD | 6,020,000.00 USD |
| `7D` | `2421.60` | 1,510,000,000.00 USD | 1,510,000,000.00 USD | 0.00 USD | 22,900,000.00 USD | 25,380,000.00 USD | 18,640,000.00 USD |
| `1D` | `2423.80` | 680,260,000.00 USD | 680,260,000.00 USD | 0.00 USD | 4,540,000.00 USD | 4,960,000.00 USD | 2,780,000.00 USD |
| `7D` | `2424.40` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 26,330,000.00 USD | 29,850,000.00 USD | 33,610,000.00 USD |
| `1D` | `2426.30` | 682,110,000.00 USD | 682,110,000.00 USD | 0.00 USD | 972,850.00 USD | 835,420.00 USD | 37,460.00 USD |
| `7D` | `2427.20` | 1,670,000,000.00 USD | 1,670,000,000.00 USD | 0.00 USD | 22,440,000.00 USD | 21,730,000.00 USD | 23,630,000.00 USD |
| `1D` | `2428.80` | 686,250,000.00 USD | 686,250,000.00 USD | 0.00 USD | 1,900,000.00 USD | 751,750.00 USD | 1,480,000.00 USD |
| `7D` | `2430.00` | 1,700,000,000.00 USD | 1,700,000,000.00 USD | 0.00 USD | 9,270,000.00 USD | 16,890,000.00 USD | 7,560,000.00 USD |
| `1D` | `2431.30` | 691,680,000.00 USD | 691,680,000.00 USD | 0.00 USD | 2,600,000.00 USD | 2,580,000.00 USD | 252,660.00 USD |
| `7D` | `2432.80` | 1,740,000,000.00 USD | 1,740,000,000.00 USD | 0.00 USD | 15,460,000.00 USD | 11,210,000.00 USD | 5,820,000.00 USD |
| `1D` | `2433.80` | 696,810,000.00 USD | 696,810,000.00 USD | 0.00 USD | 2,080,000.00 USD | 565,750.00 USD | 2,480,000.00 USD |
| `7D` | `2435.60` | 1,780,000,000.00 USD | 1,780,000,000.00 USD | 0.00 USD | 20,760,000.00 USD | 13,900,000.00 USD | 12,830,000.00 USD |
| `1D` | `2436.30` | 699,910,000.00 USD | 699,910,000.00 USD | 0.00 USD | 2,290,000.00 USD | 475,290.00 USD | 339,140.00 USD |
| `7D` | `2438.40` | 1,840,000,000.00 USD | 1,840,000,000.00 USD | 0.00 USD | 16,830,000.00 USD | 21,000,000.00 USD | 14,370,000.00 USD |
| `1D` | `2438.80` | 701,340,000.00 USD | 701,340,000.00 USD | 0.00 USD | 304,760.00 USD | 641,280.00 USD | 476,620.00 USD |
| `7D` | `2441.20` | 1,870,000,000.00 USD | 1,870,000,000.00 USD | 0.00 USD | 15,870,000.00 USD | 6,990,000.00 USD | 10,660,000.00 USD |
| `1D` | `2441.30` | 706,480,000.00 USD | 706,480,000.00 USD | 0.00 USD | 2,360,000.00 USD | 2,020,000.00 USD | 767,510.00 USD |
| `1D` | `2443.80` | 708,430,000.00 USD | 708,430,000.00 USD | 0.00 USD | 50,900.00 USD | 556,820.00 USD | 1,340,000.00 USD |
| `7D` | `2444.00` | 1,900,000,000.00 USD | 1,900,000,000.00 USD | 0.00 USD | 5,220,000.00 USD | 13,460,000.00 USD | 7,960,000.00 USD |
| `1D` | `2446.30` | 712,190,000.00 USD | 712,190,000.00 USD | 0.00 USD | 1,840,000.00 USD | 675,040.00 USD | 1,250,000.00 USD |
| `7D` | `2446.80` | 1,930,000,000.00 USD | 1,930,000,000.00 USD | 0.00 USD | 11,620,000.00 USD | 7,020,000.00 USD | 18,970,000.00 USD |
| `1D` | `2448.80` | 716,330,000.00 USD | 716,330,000.00 USD | 0.00 USD | 387,180.00 USD | 1,500,000.00 USD | 2,240,000.00 USD |
| `7D` | `2449.60` | 1,980,000,000.00 USD | 1,980,000,000.00 USD | 0.00 USD | 18,130,000.00 USD | 10,300,000.00 USD | 14,870,000.00 USD |
| `1D` | `2451.30` | 725,960,000.00 USD | 725,960,000.00 USD | 0.00 USD | 2,700,000.00 USD | 3,090,000.00 USD | 3,840,000.00 USD |
| `7D` | `2452.40` | 2,000,000,000.00 USD | 2,000,000,000.00 USD | 0.00 USD | 7,700,000.00 USD | 8,980,000.00 USD | 7,330,000.00 USD |
| `1D` | `2453.80` | 736,710,000.00 USD | 736,710,000.00 USD | 0.00 USD | 5,060,000.00 USD | 3,010,000.00 USD | 2,670,000.00 USD |
| `7D` | `2455.20` | 2,020,000,000.00 USD | 2,020,000,000.00 USD | 0.00 USD | 6,850,000.00 USD | 5,830,000.00 USD | 3,620,000.00 USD |
| `1D` | `2456.30` | 743,500,000.00 USD | 743,500,000.00 USD | 0.00 USD | 1,340,000.00 USD | 3,130,000.00 USD | 2,330,000.00 USD |
| `7D` | `2458.00` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 0.00 USD | 11,170,000.00 USD | 11,200,000.00 USD | 13,580,000.00 USD |
| `1D` | `2458.80` | 747,480,000.00 USD | 747,480,000.00 USD | 0.00 USD | 2,400,000.00 USD | 1,250,000.00 USD | 322,910.00 USD |
| `7D` | `2460.80` | 2,080,000,000.00 USD | 2,080,000,000.00 USD | 0.00 USD | 7,010,000.00 USD | 10,680,000.00 USD | 9,010,000.00 USD |
| `1D` | `2461.30` | 749,420,000.00 USD | 749,420,000.00 USD | 0.00 USD | 470,530.00 USD | 46,520.00 USD | 1,430,000.00 USD |
| `7D` | `2463.60` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 0.00 USD | 10,390,000.00 USD | 9,560,000.00 USD | 5,240,000.00 USD |
| `1D` | `2463.80` | 753,390,000.00 USD | 753,390,000.00 USD | 0.00 USD | 352,200.00 USD | 2,790,000.00 USD | 829,050.00 USD |
| `1D` | `2466.30` | 754,330,000.00 USD | 754,330,000.00 USD | 0.00 USD | 468,790.00 USD | 463,300.00 USD | 5,650.00 USD |
| `7D` | `2466.40` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 0.00 USD | 4,790,000.00 USD | 2,080,000.00 USD | 1,330,000.00 USD |
| `1D` | `2468.80` | 755,730,000.00 USD | 755,730,000.00 USD | 0.00 USD | 0.00 USD | 998,350.00 USD | 399,070.00 USD |
| `7D` | `2469.20` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 0.00 USD | 2,490,000.00 USD | 3,570,000.00 USD | 408,300.00 USD |
| `1D` | `2471.30` | 758,760,000.00 USD | 758,760,000.00 USD | 0.00 USD | 1,390,000.00 USD | 883,290.00 USD | 764,250.00 USD |
| `7D` | `2472.00` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 0.00 USD | 3,090,000.00 USD | 2,760,000.00 USD | 814,440.00 USD |
| `1D` | `2473.80` | 759,000,000.00 USD | 759,000,000.00 USD | 0.00 USD | 0.00 USD | 232,740.00 USD | 3,820.00 USD |
| `7D` | `2474.80` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 0.00 USD | 5,400,000.00 USD | 866,790.00 USD | 1,720,000.00 USD |
| `1D` | `2476.30` | 759,750,000.00 USD | 759,750,000.00 USD | 0.00 USD | 738,780.00 USD | 0.00 USD | 7,750.00 USD |
| `7D` | `2477.60` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 0.00 USD | 790,860.00 USD | 3,880,000.00 USD | 1,200,000.00 USD |
| `1D` | `2478.80` | 759,790,000.00 USD | 759,790,000.00 USD | 0.00 USD | 0.00 USD | 41,760.00 USD | 0.00 USD |
| `7D` | `2480.40` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 0.00 USD | 2,110,000.00 USD | 1,740,000.00 USD | 0.00 USD |
| `1D` | `2481.30` | 760,340,000.00 USD | 760,340,000.00 USD | 0.00 USD | 0.00 USD | 27,720.00 USD | 518,550.00 USD |
| `7D` | `2483.20` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 0.00 USD | 1,210,000.00 USD | 1,190,000.00 USD | 77,610.00 USD |
| `1D` | `2483.80` | 760,960,000.00 USD | 760,960,000.00 USD | 0.00 USD | 628,130.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2486.00` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 0.00 USD | 49,690.00 USD | 51,150.00 USD | 0.00 USD |
| `7D` | `2488.80` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 0.00 USD | 977,620.00 USD | 857,130.00 USD | 101,890.00 USD |
| `7D` | `2491.60` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 0.00 USD | 1,780,000.00 USD | 2,470,000.00 USD | 1,120,000.00 USD |
| `7D` | `2494.40` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 0.00 USD | 1,470,000.00 USD | 2,730,000.00 USD | 6,820,000.00 USD |
| `7D` | `2497.20` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 0.00 USD | 3,640,000.00 USD | 3,570,000.00 USD | 4,430,000.00 USD |
| `7D` | `2500.00` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 0.00 USD | 1,110,000.00 USD | 2,430,000.00 USD | 1,090,000.00 USD |
| `7D` | `2502.80` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 0.00 USD | 110,450.00 USD | 1,430,000.00 USD | 170,270.00 USD |
| `7D` | `2505.60` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 0.00 USD | 3,200,000.00 USD | 2,320,000.00 USD | 59,220.00 USD |
| `7D` | `2508.40` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 0.00 USD | 1,810,000.00 USD | 1,270,000.00 USD | 1,990,000.00 USD |
| `7D` | `2511.20` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 0.00 USD | 1,900,000.00 USD | 3,230,000.00 USD | 2,640,000.00 USD |
| `7D` | `2514.00` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 0.00 USD | 776,920.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2516.80` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 0.00 USD | 97,050.00 USD | 189,640.00 USD | 0.00 USD |
| `7D` | `2519.60` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD |
| `1D` | `2521.30` | 761,200,000.00 USD | 761,200,000.00 USD | 0.00 USD | 80,610.00 USD | 61,830.00 USD | 90,130.00 USD |
| `7D` | `2522.40` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 0.00 USD | 1,050,000.00 USD | 0.00 USD | 945,860.00 USD |
| `1D` | `2523.80` | 761,650,000.00 USD | 761,650,000.00 USD | 0.00 USD | 421,540.00 USD | 0.00 USD | 30,180.00 USD |
| `7D` | `2525.20` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 0.00 USD | 307,040.00 USD | 224,130.00 USD | 200,040.00 USD |
| `1D` | `2526.30` | 761,730,000.00 USD | 761,730,000.00 USD | 0.00 USD | 0.00 USD | 57,450.00 USD | 23,500.00 USD |
| `7D` | `2528.00` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 0.00 USD | 1,580,000.00 USD | 1,690,000.00 USD | 727,590.00 USD |
| `1D` | `2528.80` | 763,420,000.00 USD | 763,420,000.00 USD | 0.00 USD | 583,810.00 USD | 645,910.00 USD | 464,460.00 USD |
| `7D` | `2530.80` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 0.00 USD | 2,080,000.00 USD | 1,110,000.00 USD | 1,220,000.00 USD |
| `1D` | `2531.30` | 763,840,000.00 USD | 763,840,000.00 USD | 0.00 USD | 411,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2533.60` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 0.00 USD | 2,680,000.00 USD | 2,100,000.00 USD | 1,390,000.00 USD |
| `1D` | `2533.80` | 764,290,000.00 USD | 764,290,000.00 USD | 0.00 USD | 394,310.00 USD | 41,990.00 USD | 18,540.00 USD |
| `1D` | `2536.30` | 767,220,000.00 USD | 767,220,000.00 USD | 0.00 USD | 1,200,000.00 USD | 656,520.00 USD | 1,070,000.00 USD |
| `7D` | `2536.40` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 0.00 USD | 3,670,000.00 USD | 2,850,000.00 USD | 2,740,000.00 USD |
| `1D` | `2538.80` | 771,200,000.00 USD | 771,200,000.00 USD | 0.00 USD | 1,640,000.00 USD | 738,070.00 USD | 1,590,000.00 USD |
| `7D` | `2539.20` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 0.00 USD | 2,620,000.00 USD | 2,470,000.00 USD | 1,090,000.00 USD |
| `1D` | `2541.30` | 772,580,000.00 USD | 772,580,000.00 USD | 0.00 USD | 692,360.00 USD | 619,310.00 USD | 69,460.00 USD |
| `7D` | `2542.00` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 0.00 USD | 3,400,000.00 USD | 2,740,000.00 USD | 2,240,000.00 USD |
| `1D` | `2543.80` | 774,590,000.00 USD | 774,590,000.00 USD | 0.00 USD | 937,360.00 USD | 1,060,000.00 USD | 14,440.00 USD |
| `7D` | `2544.80` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 0.00 USD | 2,170,000.00 USD | 1,830,000.00 USD | 1,350,000.00 USD |
| `1D` | `2546.30` | 777,920,000.00 USD | 777,920,000.00 USD | 0.00 USD | 1,370,000.00 USD | 1,400,000.00 USD | 565,880.00 USD |
| `7D` | `2547.60` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 938,680.00 USD | 2,940,000.00 USD |
| `1D` | `2548.80` | 779,790,000.00 USD | 779,790,000.00 USD | 0.00 USD | 705,770.00 USD | 714,090.00 USD | 453,900.00 USD |
| `7D` | `2550.40` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 0.00 USD | 2,920,000.00 USD | 2,690,000.00 USD | 1,130,000.00 USD |
| `1D` | `2551.30` | 782,540,000.00 USD | 782,540,000.00 USD | 0.00 USD | 1,340,000.00 USD | 983,350.00 USD | 423,000.00 USD |
| `7D` | `2553.20` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 0.00 USD | 2,590,000.00 USD | 788,360.00 USD | 2,180,000.00 USD |
| `1D` | `2553.80` | 783,450,000.00 USD | 783,450,000.00 USD | 0.00 USD | 669,670.00 USD | 220,540.00 USD | 21,380.00 USD |
| `7D` | `2556.00` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 0.00 USD | 2,760,000.00 USD | 255,750.00 USD | 5,320,000.00 USD |
| `1D` | `2556.30` | 785,320,000.00 USD | 785,320,000.00 USD | 0.00 USD | 754,830.00 USD | 469,640.00 USD | 644,420.00 USD |
| `1D` | `2558.80` | 787,730,000.00 USD | 787,730,000.00 USD | 0.00 USD | 1,250,000.00 USD | 468,930.00 USD | 696,940.00 USD |
| `7D` | `2558.80` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 3,850,000.00 USD | 1,640,000.00 USD | 2,340,000.00 USD |
| `1D` | `2561.30` | 791,290,000.00 USD | 791,290,000.00 USD | 0.00 USD | 1,100,000.00 USD | 886,200.00 USD | 1,570,000.00 USD |
| `7D` | `2561.60` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 2,780,000.00 USD | 1,960,000.00 USD | 785,020.00 USD |
| `1D` | `2563.80` | 793,040,000.00 USD | 793,040,000.00 USD | 0.00 USD | 463,350.00 USD | 975,880.00 USD | 309,770.00 USD |
| `7D` | `2564.40` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 0.00 USD | 1,800,000.00 USD | 1,780,000.00 USD | 1,120,000.00 USD |
| `1D` | `2566.30` | 793,270,000.00 USD | 793,270,000.00 USD | 0.00 USD | 172,210.00 USD | 44,780.00 USD | 11,930.00 USD |
| `7D` | `2567.20` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 0.00 USD | 575,630.00 USD | 1,560,000.00 USD | 2,690,000.00 USD |
| `1D` | `2568.80` | 794,000,000.00 USD | 794,000,000.00 USD | 0.00 USD | 162,270.00 USD | 106,440.00 USD | 466,670.00 USD |
| `7D` | `2570.00` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 0.00 USD | 125,250.00 USD | 290,680.00 USD | 1,180,000.00 USD |
| `1D` | `2571.30` | 795,330,000.00 USD | 795,330,000.00 USD | 0.00 USD | 957,520.00 USD | 360,840.00 USD | 8,780.00 USD |
| `7D` | `2572.80` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,790,000.00 USD |
| `1D` | `2573.80` | 796,400,000.00 USD | 796,400,000.00 USD | 0.00 USD | 63,920.00 USD | 493,800.00 USD | 510,340.00 USD |
| `7D` | `2575.60` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 0.00 USD | 2,180,000.00 USD | 344,620.00 USD | 1,060,000.00 USD |
| `1D` | `2576.30` | 796,880,000.00 USD | 796,880,000.00 USD | 0.00 USD | 482,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2578.40` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 0.00 USD | 734,040.00 USD | 1,480,000.00 USD | 1,750,000.00 USD |
| `7D` | `2581.20` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 0.00 USD | 3,870,000.00 USD | 912,130.00 USD | 1,670,000.00 USD |
| `7D` | `2584.00` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 0.00 USD | 146,630.00 USD | 1,490,000.00 USD | 3,100,000.00 USD |
| `7D` | `2586.80` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 0.00 USD | 1,900,000.00 USD | 1,970,000.00 USD | 1,530,000.00 USD |
| `7D` | `2589.60` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 0.00 USD | 2,840,000.00 USD | 446,810.00 USD | 2,140,000.00 USD |
| `7D` | `2592.40` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 0.00 USD | 2,340,000.00 USD | 1,280,000.00 USD | 1,550,000.00 USD |
| `7D` | `2595.20` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 0.00 USD | 452,020.00 USD | 569,790.00 USD | 1,260,000.00 USD |
| `7D` | `2598.00` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 0.00 USD | 2,280,000.00 USD | 1,630,000.00 USD | 1,910,000.00 USD |
| `7D` | `2600.80` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 931,390.00 USD | 1,960,000.00 USD | 1,610,000.00 USD |
| `7D` | `2603.60` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,580,000.00 USD | 1,680,000.00 USD |
| `7D` | `2606.40` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 1,480,000.00 USD | 229,360.00 USD | 320,080.00 USD |
| `7D` | `2609.20` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 0.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD |
| `7D` | `2612.00` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 0.00 USD | 770,330.00 USD | 608,060.00 USD | 43,560.00 USD |
| `7D` | `2614.80` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 0.00 USD | 1,060,000.00 USD | 1,000,000.00 USD | 409,160.00 USD |
| `7D` | `2617.60` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 0.00 USD | 1,550,000.00 USD | 209,240.00 USD | 392,750.00 USD |
| `7D` | `2620.40` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 0.00 USD | 47,360.00 USD | 1,120,000.00 USD | 268,500.00 USD |
| `7D` | `2623.20` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 0.00 USD | 418,600.00 USD | 410,460.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `29.80B` | Total OI Tokens: `12,751,256.4 ETH`
  * 1h OI Change: `+0.13%` | 4h OI Change: `-2.46%` | 24h OI Change: `-1.01%`
  * Exchange Breakdown: Binance=`8.84B` | Bybit=`2.11B` | OKX=`1.77B` | Hyperliquid=`2.54B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `996.75K` | Last 24h: `2.27M` | Last 3d: `7.66M` | Last 7d: `13.85M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0093%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0053%` | **USDT KuCoin** | `0.0062%` |
| **USDT MEXC** | `0.0093%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0079%` | **USDT Bitget** | `0.0062%` |
| **CoinM Binance** | `0.0096%` | **CoinM OKX** | `0.0098%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `53.58%` | `46.42%` | `1.15` | 248,400,000.00 USD |
| `15M` | `Binance` | `53.46%` | `46.54%` | `1.15` | 73,130,000.00 USD |
| `15M` | `OKX` | `69.34%` | `30.66%` | `2.26` | 30,130,000.00 USD |
| `15M` | `Bybit` | `61.57%` | `38.43%` | `1.60` | 26,590,000.00 USD |
| `15M` | `KuCoin` | `60.15%` | `39.85%` | `1.51` | 605,580.00 USD |
| `15M` | `Gate` | `53.52%` | `46.48%` | `1.15` | 29,540,000.00 USD |
| `15M` | `Bitget` | `48.47%` | `51.53%` | `0.94` | 18,580,000.00 USD |
| `15M` | `BingX` | `30.21%` | `69.79%` | `0.43` | 3,780,000.00 USD |
| `15M` | `MEXC` | `36.16%` | `63.84%` | `0.57` | 10,160,000.00 USD |
| `15M` | `Bitunix` | `55.71%` | `44.29%` | `1.26` | 8,990,000.00 USD |
| `15M` | `Hyperliquid` | `69.34%` | `30.66%` | `2.26` | 7,170,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `52.97%` | `47.03%` | `1.13` | 1,740,000.00 USD |
| `15M` | `Crypto.com` | `55.14%` | `44.86%` | `1.23` | 1,410,000.00 USD |
| `15M` | `WhiteBIT` | `27.97%` | `72.03%` | `0.39` | 10,080,000.00 USD |
| `15M` | `HTX` | `44.89%` | `55.11%` | `0.81` | 1,340,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `50.77%` | `49.23%` | `1.03` | 9,370,000.00 USD |
| `15M` | `Bitfinex` | `52.36%` | `47.64%` | `1.10` | 495,950.00 USD |
| `15M` | `Kraken` | `55.07%` | `44.93%` | `1.23` | 3,780,000.00 USD |
| `15M` | `Aster` | `58.46%` | `41.54%` | `1.41` | 1,870,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `35.76%` | `64.24%` | `0.56` | 9,640,000.00 USD |
| `15M` | `Whale Positions` | `53.46%` | `46.54%` | `1.15` | 73,130,000.00 USD |
| `15M` | `Global Accounts` | `53.58%` | `46.42%` | `1.15` | 248,400,000.00 USD |
| `1H` | `ETH` | `55.26%` | `44.74%` | `1.24` | 962,950,000.00 USD |
| `1H` | `Binance` | `53.8%` | `46.2%` | `1.16` | 258,430,000.00 USD |
| `1H` | `OKX` | `61.16%` | `38.84%` | `1.57` | 120,750,000.00 USD |
| `1H` | `Bybit` | `58.01%` | `41.99%` | `1.38` | 112,330,000.00 USD |
| `1H` | `KuCoin` | `58.63%` | `41.37%` | `1.42` | 735,980.00 USD |
| `1H` | `Gate` | `54.37%` | `45.63%` | `1.19` | 116,270,000.00 USD |
| `1H` | `Bitget` | `54.45%` | `45.55%` | `1.20` | 46,360,000.00 USD |
| `1H` | `BingX` | `60.02%` | `39.98%` | `1.50` | 17,500,000.00 USD |
| `1H` | `MEXC` | `50.42%` | `49.58%` | `1.02` | 62,570,000.00 USD |
| `1H` | `Bitunix` | `58.23%` | `41.77%` | `1.39` | 44,740,000.00 USD |
| `1H` | `Hyperliquid` | `58.42%` | `41.58%` | `1.41` | 30,850,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `52.97%` | `47.03%` | `1.13` | 9,120,000.00 USD |
| `1H` | `Crypto.com` | `57.44%` | `42.56%` | `1.35` | 4,230,000.00 USD |
| `1H` | `WhiteBIT` | `50.57%` | `49.43%` | `1.02` | 26,040,000.00 USD |
| `1H` | `HTX` | `55.25%` | `44.75%` | `1.23` | 6,550,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `57.17%` | `42.83%` | `1.33` | 37,640,000.00 USD |
| `1H` | `Bitfinex` | `52.91%` | `47.09%` | `1.12` | 1,070,000.00 USD |
| `1H` | `Kraken` | `55.83%` | `44.17%` | `1.26` | 8,360,000.00 USD |
| `1H` | `Aster` | `59.37%` | `40.63%` | `1.46` | 10,190,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `45.04%` | `54.96%` | `0.82` | 49,180,000.00 USD |
| `1H` | `Whale Positions` | `53.8%` | `46.2%` | `1.16` | 258,430,000.00 USD |
| `1H` | `Global Accounts` | `55.26%` | `44.74%` | `1.24` | 962,950,000.00 USD |
| `4H` | `ETH` | `48.25%` | `51.75%` | `0.93` | 10,590,000,000.00 USD |
| `4H` | `Binance` | `44.99%` | `55.01%` | `0.82` | 3,250,000,000.00 USD |
| `4H` | `OKX` | `47.7%` | `52.3%` | `0.91` | 1,460,000,000.00 USD |
| `4H` | `Bybit` | `46.48%` | `53.52%` | `0.87` | 1,010,000,000.00 USD |
| `4H` | `KuCoin` | `31.45%` | `68.55%` | `0.46` | 40,880,000.00 USD |
| `4H` | `Gate` | `51.54%` | `48.46%` | `1.06` | 1,220,000,000.00 USD |
| `4H` | `Bitget` | `46.69%` | `53.31%` | `0.88` | 573,140,000.00 USD |
| `4H` | `BingX` | `53.86%` | `46.14%` | `1.17` | 197,690,000.00 USD |
| `4H` | `MEXC` | `50.63%` | `49.37%` | `1.03` | 610,410,000.00 USD |
| `4H` | `Bitunix` | `51.44%` | `48.56%` | `1.06` | 547,270,000.00 USD |
| `4H` | `Hyperliquid` | `52.03%` | `47.97%` | `1.08` | 568,500,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `56.04%` | `43.96%` | `1.27` | 77,000,000.00 USD |
| `4H` | `Crypto.com` | `49.09%` | `50.91%` | `0.96` | 81,040,000.00 USD |
| `4H` | `WhiteBIT` | `57.55%` | `42.45%` | `1.36` | 214,860,000.00 USD |
| `4H` | `HTX` | `48.37%` | `51.63%` | `0.94` | 46,700,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `56.45%` | `43.55%` | `1.30` | 280,260,000.00 USD |
| `4H` | `Bitfinex` | `40.88%` | `59.12%` | `0.69` | 7,610,000.00 USD |
| `4H` | `Kraken` | `45.11%` | `54.89%` | `0.82` | 81,790,000.00 USD |
| `4H` | `Aster` | `44.48%` | `55.52%` | `0.80` | 121,380,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.55%` | `51.45%` | `0.94` | 208,250,000.00 USD |
| `4H` | `Whale Positions` | `44.99%` | `55.01%` | `0.82` | 3,250,000,000.00 USD |
| `4H` | `Global Accounts` | `48.25%` | `51.75%` | `0.93` | 10,590,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `2340.25` | `2342.19` | `2340.25` | `2353.25` | `2334.75` | 172,183,772.38 USD | 75,695,646.18 USD | 96,488,126.21 USD | -20,792,480.03 USD | `-12.08%` | `0B / 3S` |
| `5:00 UTC` | `2335.75` | `2335.37` | `2335.75` | `2340.75` | `2330.75` | 125,556,310.13 USD | 63,692,130.92 USD | 61,864,179.21 USD | 1,827,951.70 USD | `+1.46%` | `1B / 1S` |
| `0:00 UTC` | `2337.75` | `2338.67` | `2337.75` | `2341.75` | `2335.75` | 48,324,873.75 USD | 25,087,349.31 USD | 23,237,524.44 USD | 1,849,824.87 USD | `+3.83%` | `0B / 0S` |
| `5:00 UTC` | `2340.25` | `2338.33` | `2340.25` | `2342.25` | `2333.75` | 43,794,873.23 USD | 24,013,000.37 USD | 19,781,872.86 USD | 4,231,127.51 USD | `+9.66%` | `0B / 2S` |
| `0:00 UTC` | `2327.25` | `2327.16` | `2327.25` | `2335.25` | `2323.25` | 195,411,305.09 USD | 64,523,153.35 USD | 130,888,151.74 USD | -66,364,998.40 USD | `-33.96%` | `0B / 9S` |
| `5:00 UTC` | `2331.25` | `2330.55` | `2331.25` | `2334.25` | `2325.75` | 53,213,391.28 USD | 35,445,824.71 USD | 17,767,566.57 USD | 17,678,258.14 USD | `+33.22%` | `4B / 0S` |
| `0:00 UTC` | `2327.75` | `2328.10` | `2327.75` | `2331.25` | `2326.25` | 28,953,047.89 USD | 13,068,031.79 USD | 15,885,016.10 USD | -2,816,984.30 USD | `-9.73%` | `0B / 1S` |
| `5:00 UTC` | `2326.75` | `2328.61` | `2326.75` | `2331.75` | `2325.75` | 28,646,242.16 USD | 14,157,941.65 USD | 14,488,300.51 USD | -330,358.86 USD | `-1.15%` | `0B / 1S` |
| `0:00 UTC` | `2334.75` | `2334.23` | `2334.75` | `2336.25` | `2330.25` | 36,369,004.25 USD | 19,887,478.26 USD | 16,481,525.99 USD | 3,405,952.27 USD | `+9.36%` | `1B / 1S` |
| `5:00 UTC` | `2337.75` | `2336.10` | `2337.75` | `2338.75` | `2332.75` | 49,392,448.38 USD | 17,604,769.72 USD | 31,787,678.66 USD | -14,182,908.93 USD | `-28.71%` | `0B / 3S` |

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
| `5m` | -7,410,000.00 USD | -84,270,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -15,370,000.00 USD | -104,100,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -16,780,000.00 USD | -101,820,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -9,380,000.00 USD | -72,900,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -10,920,000.00 USD | -157,460,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -21,140,000.00 USD | -441,740,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 10,800,000.00 USD | -176,440,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 4,090,000.00 USD | -200,410,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 13,670,000.00 USD | -186,150,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -52,990,000.00 USD | -735,380,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -25,510,000.00 USD | -1,120,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,020,000,000.00 USD | -8,270,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-7.41M` | 15m=`-15.37M` | 1h=`-9.38M` | 24h=`-52.99M`
* Futures Capital Netflows: 5m=`-84.27M` | 15m=`-104.10M` | 1h=`-72.90M` | 24h=`-735.38M`
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
  * `2026-10-30 00:58:24 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:24 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:28:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:28:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:29:24 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:29:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `2297.70` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2280.33` (Risk Distance: `17.37` pts)
  * +2.5R Take Profit: `2341.14`
  * Mathematical Lot Sizing: **`0.57 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2336.73` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2354.10` (Risk Distance: `17.37` pts)
  * +2.5R Take Profit: `2293.29`
  * Mathematical Lot Sizing: **`0.57 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2338.91`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
