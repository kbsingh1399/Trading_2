# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 01:42:07 IST` (`2026-10-29 20:12:07 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `1` | `0x5b5d...c060` | `SHORT` | 245,079,988.89 USD | `106,417.71` | `2322.74` | `2303.00` | `3888.76` | 2,101,023.26 USD | `+0.86%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 152,254,071.02 USD | `65,205.17` | `2375.30` | `2303.00` | `4383.49` | 2,628,192.08 USD | `+1.73%` | `5X Cross` |
| `6` | `0x77dd...e0e9` | `LONG` | 111,938,328.45 USD | `48,499.51` | `2610.31` | `2303.00` | `2171.20` | -14,660,555.41 USD | `-13.10%` | `10X Cross` |
| `7` | `0x0392...d7d9` | `LONG` | 103,221,108.44 USD | `44,734.81` | `2518.71` | `2303.00` | `2180.26` | -9,453,198.13 USD | `-9.16%` | `9X Cross` |
| `15` | `0xde8d...9524` | `LONG` | 70,670,045.05 USD | `30,282.40` | `2134.45` | `2303.00` | `1787.15` | 6,033,714.47 USD | `+8.54%` | `20X Cross` |
| `18` | `0x7fda...17d1` | `SHORT` | 63,395,560.69 USD | `27,464.18` | `2437.25` | `2303.00` | `3711.83` | 3,541,720.63 USD | `+5.59%` | `25X Cross` |
| `25` | `0xdf95...7d72` | `SHORT` | 52,282,875.89 USD | `22,649.95` | `2402.54` | `2303.00` | `3999.84` | 2,134,561.15 USD | `+4.08%` | `25X Cross` |
| `28` | `0xeced...6210` | `SHORT` | 43,562,609.11 USD | `18,687.58` | `2522.09` | `2303.00` | `3349.88` | 3,569,303.34 USD | `+8.19%` | `20X Cross` |
| `34` | `0xb695...a92d` | `SHORT` | 38,554,762.94 USD | `16,704.62` | `2557.74` | `2303.00` | `4065.49` | 4,171,402.10 USD | `+10.82%` | `20X Cross` |
| `35` | `0x6046...b21d` | `LONG` | 37,210,035.06 USD | `15,927.59` | `2410.19` | `2303.00` | `1550.51` | -1,178,584.59 USD | `-3.17%` | `6X Cross` |
| `38` | `0x45d2...4029` | `SHORT` | 32,196,600.00 USD | `13,950.00` | `2443.60` | `2303.00` | `5109.36` | 1,891,682.46 USD | `+5.88%` | `20X Cross` |
| `43` | `0x2371...0883` | `LONG` | 28,003,200.00 USD | `12,000.00` | `2421.77` | `2303.00` | `1280.13` | -1,058,094.85 USD | `-3.78%` | `20X Cross` |
| `44` | `0xbd1c...ff0e` | `LONG` | 27,726,000.00 USD | `12,000.00` | `2419.91` | `2303.00` | `1521.03` | -1,313,032.39 USD | `-4.74%` | `20X Cross` |
| `48` | `0xa9de...e049` | `LONG` | 25,699,300.00 USD | `11,000.00` | `2481.81` | `2303.00` | `1644.76` | -1,600,679.46 USD | `-6.23%` | `20X Cross` |
| `49` | `0x0c5d...36b3` | `LONG` | 25,681,700.00 USD | `11,000.00` | `2482.20` | `2303.00` | `1645.10` | -1,622,553.24 USD | `-6.32%` | `20X Cross` |
| `50` | `0x09dc...c094` | `LONG` | 25,637,480.00 USD | `11,000.00` | `2465.31` | `2303.00` | `1638.10` | -1,480,943.04 USD | `-5.78%` | `20X Cross` |
| `53` | `0x6c93...59a4` | `LONG` | 25,463,790.00 USD | `11,000.00` | `2441.15` | `2303.00` | `1603.06` | -1,388,882.73 USD | `-5.45%` | `20X Cross` |
| `55` | `0xa61c...66b9` | `LONG` | 25,125,148.80 USD | `10,888.00` | `2398.32` | `2303.00` | `1446.73` | -987,808.59 USD | `-3.93%` | `10X Cross` |
| `60` | `0x4487...c92d` | `SHORT` | 24,186,702.37 USD | `10,477.69` | `2373.98` | `2303.00` | `2840.75` | 687,223.65 USD | `+2.84%` | `10X Cross` |
| `64` | `0x15a4...dfdb` | `LONG` | 23,363,000.00 USD | `10,000.00` | `1761.94` | `2303.00` | `15.39` | 5,743,518.97 USD | `+24.58%` | `20X Cross` |
| `65` | `0xec7f...df39` | `LONG` | 23,306,800.00 USD | `10,000.00` | `2719.35` | `2303.00` | `1721.62` | -3,886,748.52 USD | `-16.68%` | `20X Cross` |
| `67` | `0xa2ce...3126` | `LONG` | 23,150,000.27 USD | `10,016.88` | `2162.83` | `2303.00` | `1458.80` | 1,485,198.23 USD | `+6.42%` | `10X Cross` |
| `68` | `0x6646...6de5` | `LONG` | 23,084,000.00 USD | `10,000.00` | `1765.80` | `2303.00` | `1728.35` | 5,425,942.55 USD | `+23.51%` | `25X Cross` |
| `74` | `0xaeaa...2416` | `SHORT` | 22,372,080.00 USD | `9,700.00` | `2311.92` | `2303.00` | `2658.71` | 53,602.40 USD | `+0.24%` | `25X Cross` |
| `77` | `0x0622...8088` | `LONG` | 22,135,407.38 USD | `9,597.38` | `2339.89` | `2303.00` | `1273.66` | -321,441.06 USD | `-1.45%` | `5X Cross` |
| `81` | `0xca49...53c8` | `SHORT` | 21,385,621.02 USD | `9,264.26` | `2549.47` | `2303.00` | `3767.79` | 2,233,403.72 USD | `+10.44%` | `25X Cross` |
| `82` | `0xba5d...a352` | `SHORT` | 21,115,118.15 USD | `9,054.12` | `2493.89` | `2303.00` | `2925.49` | 1,464,889.11 USD | `+6.94%` | `20X Cross` |
| `83` | `0xea00...a918` | `LONG` | 21,011,329.05 USD | `9,003.83` | `2003.01` | `2303.00` | `1240.80` | 2,976,550.19 USD | `+14.17%` | `5X Cross` |
| `95` | `0xb37f...66ca` | `SHORT` | 19,666,450.00 USD | `8,500.00` | `2308.30` | `2303.00` | `2709.06` | -45,895.81 USD | `-0.23%` | `25X Cross` |
| `105` | `0x9eec...daab` | `LONG` | 18,677,379.45 USD | `8,092.45` | `1658.44` | `2303.00` | `1921.08` | 5,256,514.92 USD | `+28.14%` | `15X Cross` |
| `106` | `0x218a...7da2` | `SHORT` | 18,664,427.12 USD | `7,997.78` | `2208.16` | `2303.00` | `2877.27` | -1,004,031.90 USD | `-5.38%` | `10X Cross` |
| `109` | `0x5f91...65aa` | `LONG` | 18,587,117.47 USD | `7,964.66` | `1626.99` | `2303.00` | `2040.74` | 5,628,674.41 USD | `+30.28%` | `16X Cross` |
| `114` | `0xcf53...ee11` | `SHORT` | 17,572,744.44 USD | `7,603.63` | `1862.69` | `2303.00` | `3998.88` | -3,409,480.50 USD | `-19.40%` | `7X Cross` |
| `119` | `0x939f...04d2` | `LONG` | 16,876,271.70 USD | `7,223.81` | `2500.18` | `2303.00` | `1773.23` | -1,184,618.48 USD | `-7.02%` | `25X Cross` |
| `121` | `0xecb6...2b00` | `SHORT` | 16,765,415.42 USD | `7,265.93` | `2327.59` | `2303.00` | `6264.36` | 146,755.58 USD | `+0.88%` | `15X Cross` |
| `122` | `0x1ee7...edf5` | `LONG` | 16,335,200.00 USD | `7,000.00` | `2330.22` | `2303.00` | `2153.96` | 23,637.80 USD | `+0.14%` | `25X Cross` |
| `124` | `0xec0b...b078` | `LONG` | 16,164,889.72 USD | `7,007.80` | `2065.97` | `2303.00` | `1009.88` | 1,686,960.13 USD | `+10.44%` | `25X Cross` |
| `130` | `0x418a...8888` | `SHORT` | 15,540,721.09 USD | `6,724.38` | `2494.55` | `2303.00` | `2966.84` | 1,233,602.09 USD | `+7.94%` | `25X Cross` |
| `131` | `0x0c4a...1b19` | `LONG` | 15,321,161.49 USD | `6,615.35` | `2373.06` | `2303.00` | `2197.06` | -377,480.50 USD | `-2.46%` | `25X Isolated` |
| `132` | `0x4ff9...38d3` | `LONG` | 15,303,539.71 USD | `6,564.10` | `2447.40` | `2303.00` | `1670.72` | -761,483.04 USD | `-4.98%` | `3X Isolated` |
| `136` | `0xf78c...c581` | `LONG` | 14,998,611.09 USD | `6,500.22` | `2521.53` | `2303.00` | `1914.20` | -1,391,929.86 USD | `-9.28%` | `20X Cross` |
| `141` | `0x799f...5f4c` | `LONG` | 14,629,936.03 USD | `6,310.90` | `2390.33` | `2303.00` | `1729.19` | -455,228.59 USD | `-3.11%` | `20X Cross` |
| `144` | `0x08bf...7872` | `SHORT` | 14,410,536.95 USD | `6,224.05` | `2258.00` | `2303.00` | `2585.96` | -356,620.84 USD | `-2.47%` | `20X Cross` |
| `148` | `0xd9e7...4aff` | `LONG` | 14,008,200.00 USD | `6,000.00` | `2480.18` | `2303.00` | `1408.49` | -872,924.33 USD | `-6.23%` | `20X Cross` |
| `173` | `0x645b...87b8` | `SHORT` | 11,762,347.69 USD | `5,073.48` | `2421.68` | `2303.00` | `6294.76` | 524,000.44 USD | `+4.45%` | `10X Cross` |
| `178` | `0x524e...0de0` | `LONG` | 11,532,000.00 USD | `5,000.00` | `2320.35` | `2303.00` | `1990.88` | -69,790.81 USD | `-0.61%` | `10X Cross` |
| `179` | `0x45ab...6cbc` | `LONG` | 11,484,049.49 USD | `4,920.96` | `2727.66` | `2303.00` | `1365.94` | -1,938,694.31 USD | `-16.88%` | `7X Cross` |
| `185` | `0x64b7...9da9` | `LONG` | 11,277,094.94 USD | `4,856.84` | `2604.61` | `2303.00` | `1461.40` | -1,373,119.48 USD | `-12.18%` | `25X Cross` |
| `186` | `0xfb18...eb17` | `SHORT` | 11,247,555.27 USD | `4,872.45` | `2315.54` | `2303.00` | `2673.66` | 34,817.76 USD | `+0.31%` | `25X Cross` |
| `192` | `0x5559...d43b` | `SHORT` | 11,111,268.28 USD | `4,755.93` | `2262.69` | `2303.00` | `2861.32` | -350,062.40 USD | `-3.15%` | `25X Cross` |
| `209` | `0xe091...6705` | `SHORT` | 10,512,900.47 USD | `4,500.00` | `2467.33` | `2303.00` | `2572.99` | 590,108.04 USD | `+5.61%` | `20X Cross` |
| `221` | `0xfe7c...b7ae` | `SHORT` | 10,174,808.65 USD | `4,402.58` | `2440.17` | `2303.00` | `4303.04` | 568,279.22 USD | `+5.59%` | `25X Cross` |
| `233` | `0xc179...e0c8` | `LONG` | 9,941,220.82 USD | `4,309.16` | `2342.89` | `2303.00` | `869.52` | -154,657.98 USD | `-1.56%` | `10X Cross` |
| `235` | `0x12d2...f97f` | `LONG` | 9,909,901.35 USD | `4,264.34` | `2623.90` | `2303.00` | `1846.00` | -1,279,333.06 USD | `-12.91%` | `20X Cross` |
| `241` | `0x6ea4...0ea7` | `SHORT` | 9,753,351.07 USD | `4,184.01` | `2602.13` | `2303.00` | `3426.02` | 1,133,995.59 USD | `+11.63%` | `20X Cross` |
| `242` | `0x28bb...fca6` | `SHORT` | 9,717,052.46 USD | `4,209.61` | `1896.10` | `2303.00` | `3040.39` | -1,735,169.90 USD | `-17.86%` | `20X Cross` |
| `249` | `0x3dc9...54b0` | `SHORT` | 9,341,276.46 USD | `3,999.69` | `2480.32` | `2303.00` | `5982.12` | 579,260.09 USD | `+6.20%` | `20X Cross` |
| `250` | `0xfb94...0ddf` | `SHORT` | 9,339,703.80 USD | `4,002.10` | `2382.44` | `2303.00` | `5105.41` | 195,080.35 USD | `+2.09%` | `20X Cross` |
| `252` | `0x95fe...f8fa` | `LONG` | 9,334,000.00 USD | `4,000.00` | `2341.35` | `2303.00` | `2259.02` | -31,416.51 USD | `-0.34%` | `20X Isolated` |
| `255` | `0x77ee...2902` | `SHORT` | 9,282,974.26 USD | `3,982.23` | `2476.53` | `2303.00` | `4277.14` | 579,147.33 USD | `+6.24%` | `25X Cross` |
| `257` | `0x5e9e...35ee` | `SHORT` | 9,251,041.58 USD | `4,007.56` | `1796.39` | `2303.00` | `2586.51` | -2,051,891.49 USD | `-22.18%` | `20X Cross` |
| `259` | `0x8cc9...2b6a` | `SHORT` | 9,230,400.00 USD | `4,000.00` | `1791.18` | `2303.00` | `3917.84` | -2,065,653.33 USD | `-22.38%` | `25X Cross` |
| `269` | `0x4b67...f4e7` | `LONG` | 8,925,868.76 USD | `3,820.84` | `2591.51` | `2303.00` | `1588.73` | -975,904.78 USD | `-10.93%` | `20X Cross` |
| `270` | `0xf02d...5eb3` | `LONG` | 8,900,771.33 USD | `3,855.99` | `2513.67` | `2303.00` | `332.05` | -791,940.98 USD | `-8.90%` | `20X Cross` |
| `292` | `0x8ae4...3d60` | `LONG` | 8,293,768.84 USD | `3,558.20` | `2482.21` | `2303.00` | `367.14` | -538,429.20 USD | `-6.49%` | `10X Cross` |
| `296` | `0x382b...3e39` | `SHORT` | 8,163,307.97 USD | `3,540.95` | `2299.54` | `2303.00` | `3721.34` | -20,739.90 USD | `-0.25%` | `25X Cross` |
| `318` | `0x9c06...0560` | `SHORT` | 7,718,153.95 USD | `3,303.58` | `2270.55` | `2303.00` | `3309.80` | -217,190.01 USD | `-2.81%` | `25X Cross` |
| `331` | `0x984e...14c2` | `SHORT` | 7,190,246.89 USD | `3,111.99` | `2357.50` | `2303.00` | `2434.98` | 146,275.87 USD | `+2.03%` | `20X Cross` |
| `332` | `0x9c2a...f6a8` | `SHORT` | 7,144,910.69 USD | `3,058.48` | `2543.83` | `2303.00` | `2592.52` | 635,349.93 USD | `+8.89%` | `20X Cross` |
| `340` | `0x39b4...5c34` | `SHORT` | 7,002,626.99 USD | `3,000.91` | `2329.97` | `2303.00` | `2401.70` | -10,583.23 USD | `-0.15%` | `25X Cross` |
| `344` | `0x007d...67a0` | `LONG` | 6,925,200.00 USD | `3,000.00` | `2400.00` | `2303.00` | `1483.91` | -274,800.00 USD | `-3.97%` | `25X Cross` |
| `345` | `0x4a20...3c26` | `LONG` | 6,924,090.00 USD | `3,000.00` | `2428.72` | `2303.00` | `369.94` | -362,070.28 USD | `-5.23%` | `20X Cross` |
| `384` | `0xf517...c032` | `SHORT` | 6,320,287.67 USD | `2,738.07` | `2053.90` | `2303.00` | `5485.47` | -696,545.76 USD | `-11.02%` | `25X Cross` |
| `396` | `0xc619...10f5` | `LONG` | 6,074,380.00 USD | `2,600.00` | `2318.40` | `2303.00` | `1860.50` | 46,531.09 USD | `+0.77%` | `25X Cross` |
| `397` | `0xbb34...1696` | `LONG` | 6,067,620.00 USD | `2,600.00` | `2318.80` | `2303.00` | `1977.66` | 38,719.15 USD | `+0.64%` | `25X Cross` |
| `399` | `0x8328...f54a` | `SHORT` | 6,019,105.06 USD | `2,576.45` | `2292.01` | `2303.00` | `3280.24` | -113,833.77 USD | `-1.89%` | `25X Cross` |
| `403` | `0xed48...7c9b` | `SHORT` | 5,886,223.40 USD | `2,551.13` | `2460.02` | `2303.00` | `3237.14` | 389,623.01 USD | `+6.62%` | `20X Cross` |
| `405` | `0x934d...92c9` | `LONG` | 5,770,750.00 USD | `2,500.00` | `2343.98` | `2303.00` | `2180.68` | -89,214.51 USD | `-1.55%` | `25X Cross` |
| `421` | `0xfbe2...c8ea` | `SHORT` | 5,548,609.25 USD | `2,404.08` | `2041.57` | `2303.00` | `2668.61` | -640,516.53 USD | `-11.54%` | `20X Cross` |
| `427` | `0x1c98...7fc7` | `LONG` | 5,496,744.29 USD | `2,358.00` | `2467.15` | `2303.00` | `1897.24` | -320,827.19 USD | `-5.84%` | `10X Cross` |
| `446` | `0x6859...7e1e` | `SHORT` | 5,131,436.38 USD | `2,224.58` | `2200.39` | `2303.00` | `3799.35` | -236,483.65 USD | `-4.61%` | `25X Cross` |
| `457` | `0xb829...3a81` | `LONG` | 5,019,904.98 USD | `2,153.91` | `2537.61` | `2303.00` | `774.50` | -445,891.76 USD | `-8.88%` | `20X Cross` |
| `459` | `0xd507...c948` | `SHORT` | 5,010,803.77 USD | `2,172.00` | `2387.49` | `2303.00` | `2707.44` | 174,837.26 USD | `+3.49%` | `5X Isolated` |
| `486` | `0xf929...d1f9` | `SHORT` | 4,672,600.00 USD | `2,000.00` | `2423.37` | `2303.00` | `2548.82` | 174,140.34 USD | `+3.73%` | `25X Cross` |
| `491` | `0x3440...32c5` | `SHORT` | 4,638,110.36 USD | `2,000.57` | `2198.21` | `2303.00` | `3568.35` | -240,447.23 USD | `-5.18%` | `25X Cross` |
| `498` | `0x0514...bdfe` | `SHORT` | 4,506,645.00 USD | `1,950.00` | `1988.74` | `2303.00` | `2971.34` | -628,585.37 USD | `-13.95%` | `25X Cross` |
| `505` | `0x8376...9a1e` | `SHORT` | 4,458,524.52 USD | `1,910.50` | `2477.72` | `2303.00` | `3157.50` | 275,163.66 USD | `+6.17%` | `20X Cross` |
| `533` | `0x7a6d...f79c` | `SHORT` | 4,209,893.58 USD | `1,825.07` | `2433.80` | `2303.00` | `2676.64` | 231,975.30 USD | `+5.51%` | `25X Cross` |
| `534` | `0x7265...91a5` | `LONG` | 4,209,707.48 USD | `1,801.87` | `2533.96` | `2303.00` | `1988.15` | -356,158.98 USD | `-8.46%` | `20X Cross` |
| `536` | `0x739c...cfb2` | `SHORT` | 4,204,980.00 USD | `1,800.00` | `2427.60` | `2303.00` | `2655.12` | 164,716.38 USD | `+3.92%` | `25X Cross` |
| `541` | `0x541e...071d` | `SHORT` | 4,176,228.50 USD | `1,805.00` | `2648.19` | `2303.00` | `3050.48` | 603,756.34 USD | `+14.46%` | `25X Cross` |
| `552` | `0x91a9...3f70` | `SHORT` | 4,124,591.33 USD | `1,767.48` | `2156.23` | `2303.00` | `3638.33` | -313,487.25 USD | `-7.60%` | `4X Cross` |
| `553` | `0xa445...329d` | `LONG` | 4,100,737.38 USD | `1,776.75` | `2398.85` | `2303.00` | `1854.85` | -161,431.97 USD | `-3.94%` | `25X Cross` |
| `558` | `0x3453...b323` | `SHORT` | 4,084,087.27 USD | `1,750.12` | `2328.82` | `2303.00` | `2394.32` | -8,355.13 USD | `-0.20%` | `25X Cross` |
| `589` | `0xfeec...4e9c` | `SHORT` | 3,905,202.25 USD | `1,691.81` | `2566.49` | `2303.00` | `2652.55` | 436,822.26 USD | `+11.19%` | `10X Cross` |
| `590` | `0x936c...bb0f` | `SHORT` | 3,895,798.60 USD | `1,688.69` | `2434.60` | `2303.00` | `8588.07` | 215,488.50 USD | `+5.53%` | `20X Cross` |
| `591` | `0xd4c1...3d1d` | `SHORT` | 3,895,064.72 USD | `1,688.08` | `2336.05` | `2303.00` | `5445.86` | 48,375.91 USD | `+1.24%` | `12X Cross` |
| `606` | `0xeee0...0b53` | `LONG` | 3,820,556.05 USD | `1,637.12` | `2468.64` | `2303.00` | `132.89` | -220,920.02 USD | `-5.78%` | `7X Cross` |
| `607` | `0x982b...4606` | `LONG` | 3,796,340.85 USD | `1,626.82` | `2575.24` | `2303.00` | `1548.44` | -393,112.22 USD | `-10.36%` | `5X Isolated` |
| `608` | `0x27b8...12fc` | `LONG` | 3,794,496.71 USD | `1,628.12` | `2468.73` | `2303.00` | `454.96` | -224,897.93 USD | `-5.93%` | `10X Cross` |
| `625` | `0x73d7...8be1` | `LONG` | 3,696,822.96 USD | `1,601.47` | `2410.40` | `2303.00` | `2059.56` | -163,355.96 USD | `-4.42%` | `25X Cross` |
| `642` | `0xe170...9300` | `SHORT` | 3,582,482.42 USD | `1,533.40` | `2076.39` | `2303.00` | `3224.36` | -398,532.92 USD | `-11.12%` | `25X Cross` |
| `650` | `0x023a...2355` | `LONG` | 3,541,327.98 USD | `1,535.44` | `2338.86` | `2303.00` | `0.000000` | -49,850.48 USD | `-1.41%` | `25X Cross` |
| `658` | `0x2e2b...2fab` | `LONG` | 3,517,464.23 USD | `1,507.38` | `2245.53` | `2303.00` | `1121.77` | 132,591.13 USD | `+3.77%` | `25X Cross` |
| `670` | `0x251f...6e5d` | `LONG` | 3,461,400.00 USD | `1,500.00` | `2346.68` | `2303.00` | `1706.93` | -58,630.49 USD | `-1.69%` | `20X Cross` |
| `679` | `0xad54...6203` | `LONG` | 3,404,413.55 USD | `1,458.18` | `2627.45` | `2303.00` | `2145.32` | -426,893.13 USD | `-12.54%` | `10X Isolated` |
| `687` | `0xef70...a84c` | `SHORT` | 3,366,497.45 USD | `1,442.74` | `2424.73` | `2303.00` | `3450.61` | 131,773.37 USD | `+3.91%` | `25X Cross` |
| `692` | `0x4b5f...0dd8` | `LONG` | 3,341,471.19 USD | `1,431.96` | `2339.45` | `2303.00` | `2148.73` | -8,521.75 USD | `-0.26%` | `10X Cross` |
| `696` | `0xbadb...9ee6` | `LONG` | 3,334,325.15 USD | `1,428.16` | `1936.00` | `2303.00` | `1042.52` | 569,403.51 USD | `+17.08%` | `20X Cross` |
| `702` | `0xfc27...9d9d` | `SHORT` | 3,310,702.20 USD | `1,434.20` | `2402.13` | `2303.00` | `12952.96` | 134,437.28 USD | `+4.06%` | `25X Cross` |
| `763` | `0x880a...311c` | `SHORT` | 3,077,572.07 USD | `1,320.22` | `2425.76` | `2303.00` | `8250.32` | 124,977.09 USD | `+4.06%` | `9X Cross` |
| `778` | `0x29de...3e93` | `LONG` | 3,021,384.00 USD | `1,310.00` | `2352.60` | `2303.00` | `1922.26` | -60,524.82 USD | `-2.00%` | `5X Isolated` |
| `799` | `0xc435...c905` | `SHORT` | 2,915,577.60 USD | `1,248.00` | `2704.38` | `2303.00` | `4876.43` | 459,492.75 USD | `+15.76%` | `20X Cross` |
| `816` | `0x4202...aaf5` | `SHORT` | 2,846,777.22 USD | `1,232.10` | `2321.73` | `2303.00` | `2733.57` | 13,847.08 USD | `+0.49%` | `5X Isolated` |
| `818` | `0x7178...0854` | `LONG` | 2,844,407.78 USD | `1,218.63` | `2461.81` | `2303.00` | `1064.08` | -155,638.62 USD | `-5.47%` | `10X Cross` |
| `869` | `0x07fd...689d` | `LONG` | 2,624,496.03 USD | `1,135.90` | `2423.84` | `2303.00` | `0.000000` | -128,747.17 USD | `-4.91%` | `25X Cross` |
| `892` | `0x2f80...f203` | `SHORT` | 2,537,886.13 USD | `1,088.94` | `1984.00` | `2303.00` | `3073.63` | -377,418.94 USD | `-14.87%` | `20X Cross` |
| `902` | `0x6f11...0389` | `SHORT` | 2,517,954.40 USD | `1,079.00` | `2333.39` | `2303.00` | `3199.71` | -225.49 USD | `-0.01%` | `25X Cross` |
| `907` | `0x2b61...2f6c` | `SHORT` | 2,509,655.73 USD | `1,076.60` | `2681.75` | `2303.00` | `6389.86` | 377,517.01 USD | `+15.04%` | `10X Cross` |
| `947` | `0xb15b...dbae` | `SHORT` | 2,392,786.74 USD | `1,025.14` | `2338.37` | `2303.00` | `2381.09` | 4,386.97 USD | `+0.18%` | `25X Cross` |
| `951` | `0x1b2a...f7a6` | `LONG` | 2,372,599.02 USD | `1,025.37` | `2737.51` | `2303.00` | `883.11` | -434,360.92 USD | `-18.31%` | `10X Cross` |
| `959` | `0x02aa...1806` | `SHORT` | 2,349,967.37 USD | `1,007.10` | `2654.68` | `2303.00` | `3613.71` | 323,564.73 USD | `+13.77%` | `20X Cross` |
| `969` | `0xfe82...ce65` | `SHORT` | 2,336,100.00 USD | `1,000.00` | `2300.50` | `2303.00` | `2718.44` | -35,592.07 USD | `-1.52%` | `25X Cross` |
| `971` | `0x2828...93a0` | `LONG` | 2,334,700.00 USD | `1,000.00` | `2393.30` | `2302.90` | `2271.82` | -58,609.16 USD | `-2.51%` | `25X Cross` |
| `972` | `0x4044...794c` | `LONG` | 2,333,700.00 USD | `1,000.00` | `2332.68` | `2302.90` | `0.000000` | 1,010.16 USD | `+0.04%` | `25X Cross` |
| `973` | `0xdf60...d3c7` | `LONG` | 2,333,500.00 USD | `1,000.00` | `2736.24` | `2302.90` | `2246.10` | -402,742.88 USD | `-17.26%` | `10X Isolated` |
| `975` | `0x5986...89d9` | `LONG` | 2,330,890.00 USD | `1,000.00` | `2346.34` | `2302.90` | `1279.19` | -15,459.54 USD | `-0.66%` | `25X Cross` |
| `978` | `0x001a...fef6` | `SHORT` | 2,325,208.30 USD | `1,007.33` | `2022.19` | `2302.90` | `3052.30` | -288,200.34 USD | `-12.39%` | `10X Cross` |
| `983` | `0xdb3a...cf3b` | `LONG` | 2,316,022.38 USD | `1,003.22` | `2705.01` | `2302.90` | `0.000000` | -397,684.51 USD | `-17.17%` | `4X Cross` |
| `984` | `0x5272...fcd9` | `SHORT` | 2,314,890.00 USD | `1,000.00` | `2241.82` | `2302.90` | `2880.78` | -73,065.51 USD | `-3.16%` | `5X Cross` |
| `1002` | `0xb002...ed8a` | `SHORT` | 2,246,849.02 USD | `962.78` | `2299.66` | `2302.90` | `4188.32` | -32,771.11 USD | `-1.46%` | `25X Cross` |
| `1024` | `0x2e30...4cb5` | `SHORT` | 2,182,463.39 USD | `945.44` | `2340.09` | `2302.90` | `7339.46` | 29,966.73 USD | `+1.37%` | `2X Cross` |
| `1034` | `0xc8fe...afa4` | `LONG` | 2,160,771.57 USD | `936.37` | `2331.34` | `2302.90` | `2145.83` | -22,232.67 USD | `-1.03%` | `10X Isolated` |
| `1042` | `0x9606...4e5d` | `SHORT` | 2,131,025.60 USD | `913.00` | `2478.70` | `2302.90` | `3981.06` | 132,028.01 USD | `+6.20%` | `20X Cross` |
| `1063` | `0xaeea...bfa7` | `LONG` | 2,097,659.08 USD | `908.75` | `2339.31` | `2302.90` | `2286.75` | -28,183.02 USD | `-1.34%` | `23X Isolated` |
| `1093` | `0x60f7...d1ee` | `LONG` | 2,054,120.00 USD | `890.00` | `2343.49` | `2302.90` | `2269.17` | -31,589.96 USD | `-1.54%` | `25X Cross` |
| `1100` | `0x2577...4897` | `LONG` | 2,034,943.25 USD | `882.11` | `2350.58` | `2302.90` | `0.000000` | -38,537.62 USD | `-1.89%` | `15X Cross` |
| `1167` | `0x3bca...66f3` | `SHORT` | 1,957,324.51 USD | `848.65` | `2337.45` | `2302.90` | `11692.98` | 26,357.66 USD | `+1.35%` | `25X Cross` |
| `1179` | `0xbef3...0d3e` | `LONG` | 1,941,365.85 USD | `830.99` | `2332.88` | `2302.90` | `2110.70` | 2,754.60 USD | `+0.14%` | `20X Cross` |
| `1186` | `0xcd27...52a8` | `LONG` | 1,930,937.22 USD | `837.21` | `2553.56` | `2302.90` | `1404.25` | -206,927.55 USD | `-10.72%` | `2X Cross` |
| `1201` | `0x6a41...a3b9` | `LONG` | 1,906,792.91 USD | `826.06` | `2332.61` | `2302.90` | `2112.90` | -20,081.94 USD | `-1.05%` | `20X Cross` |
| `1216` | `0x3fc5...c0c1` | `SHORT` | 1,876,736.51 USD | `804.26` | `2702.11` | `2302.90` | `4939.04` | 296,465.02 USD | `+15.80%` | `25X Cross` |
| `1223` | `0x7737...bf66` | `SHORT` | 1,867,993.96 USD | `799.79` | `2494.83` | `2302.90` | `24815.62` | 127,352.07 USD | `+6.82%` | `15X Cross` |
| `1224` | `0x04a9...95aa` | `LONG` | 1,866,800.00 USD | `800.00` | `2595.13` | `2302.90` | `1862.97` | -209,306.74 USD | `-11.21%` | `5X Cross` |
| `1240` | `0xf83f...625f` | `SHORT` | 1,853,759.00 USD | `803.05` | `2601.00` | `2302.90` | `6059.67` | 234,977.45 USD | `+12.68%` | `20X Cross` |
| `1267` | `0x458d...ab3b` | `LONG` | 1,809,963.94 USD | `774.75` | `2740.41` | `2302.90` | `1887.99` | -313,165.24 USD | `-17.30%` | `3X Isolated` |
| `1292` | `0x0dd5...f6ee` | `LONG` | 1,763,124.60 USD | `761.64` | `2330.46` | `2302.90` | `1162.93` | -11,856.43 USD | `-0.67%` | `5X Cross` |
| `1298` | `0x7743...e4fe` | `SHORT` | 1,751,422.89 USD | `750.56` | `2326.87` | `2302.90` | `5895.15` | -4,968.76 USD | `-0.28%` | `25X Cross` |
| `1311` | `0x5f10...d49d` | `SHORT` | 1,738,650.00 USD | `750.00` | `2350.92` | `2302.90` | `2842.54` | 24,546.61 USD | `+1.41%` | `25X Cross` |
| `1340` | `0x51a0...3543` | `SHORT` | 1,690,727.62 USD | `724.55` | `2627.71` | `2302.90` | `7726.33` | 213,169.13 USD | `+12.61%` | `20X Cross` |
| `1341` | `0x4b1c...bc38` | `SHORT` | 1,686,991.72 USD | `722.14` | `2529.31` | `2302.90` | `4511.71` | 139,530.24 USD | `+8.27%` | `10X Cross` |
| `1361` | `0x3ee5...4fab` | `SHORT` | 1,666,767.98 USD | `715.17` | `2759.35` | `2302.90` | `3389.07` | 306,631.99 USD | `+18.40%` | `20X Cross` |
| `1366` | `0xa189...94d7` | `SHORT` | 1,661,711.53 USD | `719.98` | `2691.84` | `2302.90` | `3051.96` | 276,361.13 USD | `+16.63%` | `25X Cross` |
| `1387` | `0x5605...fe0f` | `SHORT` | 1,636,415.87 USD | `702.14` | `2566.90` | `2302.90` | `3057.30` | 165,916.77 USD | `+10.14%` | `20X Cross` |
| `1389` | `0x2f93...4404` | `LONG` | 1,634,612.90 USD | `707.47` | `1700.45` | `2302.90` | `1369.64` | 431,586.53 USD | `+26.40%` | `4X Isolated` |
| `1410` | `0xaa53...9cb7` | `LONG` | 1,615,390.00 USD | `700.00` | `2394.46` | `2302.90` | `1930.41` | -60,732.07 USD | `-3.76%` | `20X Cross` |
| `1437` | `0x71e5...be04` | `LONG` | 1,581,403.24 USD | `677.67` | `2727.27` | `2302.90` | `1471.79` | -266,782.36 USD | `-16.87%` | `20X Cross` |
| `1443` | `0x0b23...f37b` | `LONG` | 1,573,492.50 USD | `675.00` | `2238.15` | `2302.90` | `582.90` | 62,735.86 USD | `+3.99%` | `5X Cross` |
| `1444` | `0xdbd1...29dd` | `SHORT` | 1,572,763.13 USD | `680.70` | `3030.57` | `2302.90` | `4087.59` | 490,158.00 USD | `+31.17%` | `6X Cross` |
| `1478` | `0x0cac...6170` | `SHORT` | 1,529,315.00 USD | `662.50` | `2146.55` | `2302.90` | `2835.42` | -107,220.01 USD | `-7.01%` | `20X Cross` |
| `1492` | `0x0082...1ae3` | `LONG` | 1,522,554.00 USD | `660.00` | `2448.58` | `2302.90` | `2244.99` | -93,514.64 USD | `-6.14%` | `25X Cross` |
| `1497` | `0xfc66...ca06` | `LONG` | 1,513,973.32 USD | `656.42` | `2333.96` | `2302.90` | `0.000000` | -18,092.52 USD | `-1.20%` | `20X Cross` |
| `1512` | `0xffb2...5ed6` | `SHORT` | 1,493,883.72 USD | `640.77` | `2672.96` | `2302.90` | `2555.86` | 218,864.63 USD | `+14.65%` | `20X Cross` |
| `1533` | `0xfce0...f4c0` | `SHORT` | 1,455,232.96 USD | `623.60` | `3129.61` | `2302.90` | `2788.45` | 496,393.62 USD | `+34.11%` | `20X Cross` |
| `1570` | `0x7663...cb5a` | `SHORT` | 1,416,290.66 USD | `613.54` | `2342.35` | `2302.90` | `3653.12` | 20,829.83 USD | `+1.47%` | `3X Cross` |
| `1589` | `0x26e6...6b28` | `LONG` | 1,400,160.00 USD | `600.00` | `1769.78` | `2302.90` | `2005.51` | 338,288.47 USD | `+24.16%` | `20X Cross` |
| `1592` | `0x67c3...609d` | `SHORT` | 1,398,660.00 USD | `600.00` | `2386.55` | `2302.90` | `2560.80` | 33,271.89 USD | `+2.38%` | `25X Cross` |
| `1603` | `0x0deb...0bc5` | `LONG` | 1,388,940.00 USD | `600.00` | `2038.23` | `2302.90` | `1478.72` | 166,001.36 USD | `+11.95%` | `20X Cross` |
| `1605` | `0xad02...eb65` | `LONG` | 1,386,591.79 USD | `600.62` | `2460.69` | `2302.90` | `1079.70` | -91,348.76 USD | `-6.59%` | `5X Cross` |
| `1608` | `0x638f...f5f0` | `LONG` | 1,385,040.00 USD | `600.00` | `4011.50` | `2302.90` | `127.04` | -1,021,863.53 USD | `-73.78%` | `25X Cross` |
| `1609` | `0x0a84...6ddd` | `LONG` | 1,384,980.00 USD | `600.00` | `2222.36` | `2302.90` | `1774.83` | 51,561.66 USD | `+3.72%` | `25X Cross` |
| `1631` | `0x94b6...e5b3` | `SHORT` | 1,354,361.36 USD | `586.71` | `2377.90` | `2302.90` | `2466.05` | 40,776.87 USD | `+3.01%` | `25X Cross` |
| `1654` | `0xfb99...37f3` | `LONG` | 1,319,279.99 USD | `565.34` | `2362.35` | `2302.90` | `1207.90` | -16,256.36 USD | `-1.23%` | `3X Cross` |
| `1662` | `0x844b...7f42` | `SHORT` | 1,308,308.10 USD | `561.00` | `2026.17` | `2302.90` | `3030.17` | -171,624.69 USD | `-13.12%` | `25X Cross` |
| `1701` | `0xabe6...1d99` | `SHORT` | 1,282,534.43 USD | `556.00` | `2484.68` | `2302.90` | `2981.18` | 98,961.46 USD | `+7.72%` | `20X Cross` |
| `1746` | `0xad21...fb6a` | `LONG` | 1,227,022.48 USD | `531.87` | `2574.89` | `2302.90` | `1689.31` | -142,483.03 USD | `-11.61%` | `7X Cross` |
| `1783` | `0x8923...1bac` | `SHORT` | 1,193,452.64 USD | `517.18` | `2348.15` | `2302.90` | `3140.21` | 20,972.45 USD | `+1.76%` | `25X Cross` |
| `1784` | `0xf910...0a2d` | `LONG` | 1,192,519.02 USD | `516.62` | `2320.54` | `2302.90` | `0.000000` | -6,328.04 USD | `-0.53%` | `5X Cross` |
| `1794` | `0x0c7a...2f50` | `SHORT` | 1,179,055.64 USD | `509.25` | `2122.56` | `2302.90` | `4079.06` | -98,150.21 USD | `-8.32%` | `20X Cross` |
| `1808` | `0x7298...7d6c` | `SHORT` | 1,163,726.58 USD | `498.15` | `3426.75` | `2302.90` | `5422.40` | 543,309.24 USD | `+46.69%` | `20X Cross` |
| `1816` | `0x89b2...9ca6` | `LONG` | 1,155,550.00 USD | `500.00` | `2484.03` | `2302.90` | `1954.23` | -86,469.35 USD | `-7.48%` | `25X Cross` |
| `1832` | `0xc10f...23b3` | `LONG` | 1,142,729.00 USD | `490.00` | `2402.16` | `2302.90` | `2082.08` | -34,333.83 USD | `-3.00%` | `25X Cross` |
| `1839` | `0x321f...1c84` | `SHORT` | 1,139,076.75 USD | `488.02` | `2370.09` | `2302.90` | `3006.77` | 17,567.85 USD | `+1.54%` | `10X Cross` |
| `1851` | `0x404c...5f03` | `SHORT` | 1,131,942.81 USD | `489.79` | `2671.94` | `2302.90` | `4513.51` | 176,736.75 USD | `+15.61%` | `20X Cross` |
| `1873` | `0xa0fb...96be` | `LONG` | 1,115,177.82 USD | `483.12` | `2324.22` | `2302.90` | `327.74` | -7,693.34 USD | `-0.69%` | `3X Cross` |
| `1909` | `0x82c6...fe42` | `LONG` | 1,079,290.00 USD | `462.50` | `2501.38` | `2302.90` | `2054.49` | -77,600.57 USD | `-7.19%` | `5X Isolated` |
| `1934` | `0x617e...0f97` | `SHORT` | 1,056,270.10 USD | `457.85` | `2205.60` | `2302.90` | `3724.95` | -46,426.27 USD | `-4.40%` | `10X Cross` |
| `1956` | `0x53f8...ceff` | `LONG` | 1,039,801.77 USD | `445.60` | `2399.81` | `2302.90` | `0.000000` | -29,548.83 USD | `-2.84%` | `20X Cross` |
| `1958` | `0xae55...2236` | `LONG` | 1,038,600.00 USD | `450.00` | `2510.21` | `2302.90` | `0.000000` | -90,997.50 USD | `-8.76%` | `25X Cross` |
| `1980` | `0xac26...a9c7` | `SHORT` | 1,030,007.09 USD | `446.28` | `2192.58` | `2302.90` | `8570.31` | -51,507.39 USD | `-5.00%` | `20X Cross` |
| `1993` | `0xd911...961e` | `LONG` | 1,021,912.57 USD | `442.71` | `2321.82` | `2302.90` | `0.000000` | -5,986.76 USD | `-0.59%` | `25X Cross` |
| `1997` | `0xd8a1...6687` | `LONG` | 1,020,426.92 USD | `441.53` | `2804.24` | `2302.90` | `2151.04` | -217,741.52 USD | `-21.34%` | `20X Cross` |
| `2003` | `0x248e...6be2` | `SHORT` | 1,017,099.66 USD | `436.40` | `2314.49` | `2302.90` | `4430.86` | -7,064.94 USD | `-0.69%` | `20X Cross` |
| `2016` | `0x80f2...0c3a` | `LONG` | 1,007,449.59 USD | `434.55` | `2564.17` | `2302.90` | `872.47` | -106,799.29 USD | `-10.60%` | `5X Cross` |

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
| `Live` | `Long Liquidation` | `465.00` | 8,890.00 USD | 871,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `475.00` | 18,650.00 USD | 871,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.00` | 10,700.00 USD | 871,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `495.00` | 3,170.00 USD | 871,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.00` | 40,200.00 USD | 871,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.00` | 8,310.00 USD | 871,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.00` | 5,110.00 USD | 871,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.00` | 16,270.00 USD | 871,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.00` | 22,070.00 USD | 871,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.00` | 144,570.00 USD | 871,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `565.00` | 113,200.00 USD | 871,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `575.00` | 17,490.00 USD | 871,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.00` | 396,730.00 USD | 871,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.00` | 8,390.00 USD | 870,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `605.00` | 21,280.00 USD | 870,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.00` | 90,210.00 USD | 870,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.00` | 12,690.00 USD | 870,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.00` | 2,240.00 USD | 870,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `645.00` | 4,850.00 USD | 870,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `655.00` | 54,920.00 USD | 870,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `665.00` | 99,080.00 USD | 870,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `675.00` | 123,080.00 USD | 870,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `685.00` | 35,700.00 USD | 870,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `695.00` | 107,880.00 USD | 870,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `705.00` | 4,070.00 USD | 870,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `715.00` | 15,690.00 USD | 870,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `725.00` | 383,190.00 USD | 870,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `735.00` | 52,700.00 USD | 869,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `745.00` | 1,820.00 USD | 869,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `755.00` | 27,110.00 USD | 869,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `765.00` | 87,060.00 USD | 869,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `775.00` | 1,710,000.00 USD | 869,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `785.00` | 62,570.00 USD | 867,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `795.00` | 468,490.00 USD | 867,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `805.00` | 2,400.00 USD | 867,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `815.00` | 444,920.00 USD | 867,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `825.00` | 93,820.00 USD | 866,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `835.00` | 264,560.00 USD | 866,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `845.00` | 19,780.00 USD | 866,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `855.00` | 5,300.00 USD | 866,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `865.00` | 3,780,000.00 USD | 866,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `875.00` | 35,210.00 USD | 862,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `885.00` | 422,370.00 USD | 862,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `895.00` | 28,550.00 USD | 862,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `905.00` | 77,340.00 USD | 862,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `915.00` | 233,800.00 USD | 862,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `925.00` | 131,200.00 USD | 861,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `935.00` | 31,510.00 USD | 861,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `945.00` | 23,750.00 USD | 861,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `955.00` | 1,140,000.00 USD | 861,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `965.00` | 23,360.00 USD | 860,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `975.00` | 74,510.00 USD | 860,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `985.00` | 21,080.00 USD | 860,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `995.00` | 54,120.00 USD | 860,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1005.00` | 7,080,000.00 USD | 860,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1015.00` | 63,250.00 USD | 853,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1025.00` | 122,850.00 USD | 853,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1035.00` | 29,510.00 USD | 853,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1045.00` | 1,900,000.00 USD | 853,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1055.00` | 31,060.00 USD | 851,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1065.00` | 1,500,000.00 USD | 851,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1075.00` | 872,800.00 USD | 849,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1085.00` | 35,080.00 USD | 848,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1095.00` | 117,660.00 USD | 848,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1105.00` | 144,030.00 USD | 848,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1115.00` | 145,270.00 USD | 848,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1125.00` | 1,760,000.00 USD | 848,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1135.00` | 76,690.00 USD | 846,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1145.00` | 217,980.00 USD | 846,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1155.00` | 345,860.00 USD | 846,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1165.00` | 14,960.00 USD | 845,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1175.00` | 337,640.00 USD | 845,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1185.00` | 123,330.00 USD | 845,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1195.00` | 305,420.00 USD | 845,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1205.00` | 1,230,000.00 USD | 845,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1215.00` | 118,830.00 USD | 843,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1225.00` | 250,230.00 USD | 843,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1235.00` | 247,580.00 USD | 843,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1245.00` | 11,610,000.00 USD | 843,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1255.00` | 439,960.00 USD | 831,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1265.00` | 1,550,000.00 USD | 831,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1275.00` | 94,640.00 USD | 829,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1285.00` | 16,260,000.00 USD | 829,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1295.00` | 413,680.00 USD | 813,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1305.00` | 160,590.00 USD | 812,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1315.00` | 92,010.00 USD | 812,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1325.00` | 565,280.00 USD | 812,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1335.00` | 410,380.00 USD | 812,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1345.00` | 569,800.00 USD | 811,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1355.00` | 112,370.00 USD | 811,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1365.00` | 7,800,000.00 USD | 811,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1375.00` | 343,870.00 USD | 803,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1385.00` | 136,090.00 USD | 802,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1395.00` | 321,060.00 USD | 802,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1405.00` | 25,310,000.00 USD | 802,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1415.00` | 60,360.00 USD | 777,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1425.00` | 1,110,000.00 USD | 777,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1435.00` | 14,830,000.00 USD | 775,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1445.00` | 164,980.00 USD | 761,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1455.00` | 7,350,000.00 USD | 760,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1465.00` | 413,140.00 USD | 753,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1475.00` | 2,070,000.00 USD | 753,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1485.00` | 5,120,000.00 USD | 751,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1495.00` | 510,410.00 USD | 746,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1505.00` | 457,390.00 USD | 745,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1515.00` | 18,940,000.00 USD | 745,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1525.00` | 18,620,000.00 USD | 726,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1535.00` | 646,040.00 USD | 707,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1545.00` | 27,510,000.00 USD | 706,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1555.00` | 974,100.00 USD | 679,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1565.00` | 264,610.00 USD | 678,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1575.00` | 204,780.00 USD | 678,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1585.00` | 262,710.00 USD | 677,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1595.00` | 7,660,000.00 USD | 677,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1605.00` | 18,380,000.00 USD | 669,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1615.00` | 278,310.00 USD | 651,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1625.00` | 3,020,000.00 USD | 651,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1635.00` | 18,260,000.00 USD | 648,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1645.00` | 36,410,000.00 USD | 630,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1655.00` | 997,270.00 USD | 593,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1665.00` | 845,700.00 USD | 592,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1675.00` | 11,660,000.00 USD | 591,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1685.00` | 2,030,000.00 USD | 580,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1695.00` | 444,640.00 USD | 578,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1705.00` | 1,240,000.00 USD | 577,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1715.00` | 11,040,000.00 USD | 576,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1725.00` | 18,000,000.00 USD | 565,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1735.00` | 18,130,000.00 USD | 547,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1745.00` | 2,120,000.00 USD | 529,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1755.00` | 968,460.00 USD | 527,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1765.00` | 1,060,000.00 USD | 526,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1775.00` | 14,310,000.00 USD | 525,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1785.00` | 54,670,000.00 USD | 510,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1795.00` | 337,900.00 USD | 456,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1805.00` | 1,610,000.00 USD | 455,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1815.00` | 4,520,000.00 USD | 454,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1825.00` | 9,600,000.00 USD | 449,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1835.00` | 1,310,000.00 USD | 440,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1845.00` | 290,390.00 USD | 438,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1855.00` | 1,020,000.00 USD | 438,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1865.00` | 6,820,000.00 USD | 437,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1875.00` | 5,580,000.00 USD | 430,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1885.00` | 2,730,000.00 USD | 425,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1895.00` | 5,510,000.00 USD | 422,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1905.00` | 1,280,000.00 USD | 416,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1915.00` | 30,800,000.00 USD | 415,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1925.00` | 2,930,000.00 USD | 384,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1935.00` | 1,570,000.00 USD | 381,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1945.00` | 789,440.00 USD | 380,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1955.00` | 3,430,000.00 USD | 379,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1965.00` | 748,720.00 USD | 375,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1975.00` | 6,210,000.00 USD | 375,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1985.00` | 4,430,000.00 USD | 369,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1995.00` | 926,340.00 USD | 364,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2005.00` | 2,840,000.00 USD | 363,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2015.00` | 3,290,000.00 USD | 360,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2025.00` | 1,470,000.00 USD | 357,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2035.00` | 1,050,000.00 USD | 356,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2045.00` | 20,110,000.00 USD | 355,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2055.00` | 4,320,000.00 USD | 334,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2065.00` | 1,360,000.00 USD | 330,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2067.30` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 452,190.00 USD | 295,290.00 USD | 262,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2070.20` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 2,800,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2070.70` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 995,550.00 USD | 57,450.00 USD | 487,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2073.10` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 3,550,000.00 USD | 2,100,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2073.30` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 419,970.00 USD | 62,630.00 USD | 506,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 921,260.00 USD | 329,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2075.90` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 2,580,000.00 USD | 901,140.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2076.00` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 3,910,000.00 USD | 4,290,000.00 USD | 3,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2078.50` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 1,140,000.00 USD | 1,100,000.00 USD | 632,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2078.90` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 4,500,000.00 USD | 3,730,000.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2081.10` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 1,140,000.00 USD | 1,080,000.00 USD | 212,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2081.80` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 3,370,000.00 USD | 1,290,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2083.70` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 1,670,000.00 USD | 1,420,000.00 USD | 755,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2084.70` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 4,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 2,640,000.00 USD | 328,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2086.30` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 961,460.00 USD | 1,470,000.00 USD | 649,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2087.60` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 3,960,000.00 USD | 2,750,000.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2088.90` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 1,180,000.00 USD | 430,310.00 USD | 227,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2090.50` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 4,370,000.00 USD | 976,840.00 USD | 6,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2091.50` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 1,260,000.00 USD | 469,640.00 USD | 796,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2093.40` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 3,930,000.00 USD | 1,200,000.00 USD | 2,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2094.10` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 1,990,000.00 USD | 1,090,000.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 1,420,000.00 USD | 325,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2096.30` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 3,150,000.00 USD | 2,430,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2096.70` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 597,710.00 USD | 797,210.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2099.20` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 1,460,000.00 USD | 2,100,000.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2099.30` | 999,100,000.00 USD | 999,100,000.00 USD | 401,170.00 USD | 700,850.00 USD | 256,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2101.90` | 997,740,000.00 USD | 997,740,000.00 USD | 162,270.00 USD | 119,690.00 USD | 470,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2102.10` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 678,000.00 USD | 1,510,000.00 USD | 2,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2104.50` | 996,990,000.00 USD | 996,990,000.00 USD | 957,520.00 USD | 841,400.00 USD | 16,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2105.00` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 2,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 1,220,000.00 USD | 324,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2107.10` | 995,180,000.00 USD | 995,180,000.00 USD | 546,100.00 USD | 0.00 USD | 502,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2107.90` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 2,320,000.00 USD | 356,360.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2109.70` | 994,130,000.00 USD | 994,130,000.00 USD | 118,210.00 USD | 31,550.00 USD | 8,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2110.80` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 2,830,000.00 USD | 2,350,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2112.30` | 993,970,000.00 USD | 993,970,000.00 USD | 902,600.00 USD | 643,210.00 USD | 413,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2113.70` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 1,780,000.00 USD | 1,300,000.00 USD | 2,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2114.90` | 992,010,000.00 USD | 992,010,000.00 USD | 9,210.00 USD | 0.00 USD | 441,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 20,470,000.00 USD | 323,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2116.60` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 2,360,000.00 USD | 2,350,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2117.50` | 991,560,000.00 USD | 991,560,000.00 USD | 679,710.00 USD | 17,360.00 USD | 811,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2119.50` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 2,530,000.00 USD | 606,940.00 USD | 2,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2120.10` | 990,050,000.00 USD | 990,050,000.00 USD | 198,890.00 USD | 428,990.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2122.40` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 2,230,000.00 USD | 1,000,000.00 USD | 1,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2122.70` | 988,410,000.00 USD | 988,410,000.00 USD | 1,030,000.00 USD | 522,540.00 USD | 851,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 1,030,000.00 USD | 302,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2125.30` | 986,000,000.00 USD | 986,000,000.00 USD | 714,970.00 USD | 1,120,000.00 USD | 631,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2125.30` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 2,700,000.00 USD | 2,150,000.00 USD | 2,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2127.90` | 983,530,000.00 USD | 983,530,000.00 USD | 365,910.00 USD | 1,040,000.00 USD | 301,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2128.20` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 931,390.00 USD | 1,960,000.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2130.50` | 981,820,000.00 USD | 981,820,000.00 USD | 0.00 USD | 18,610.00 USD | 654,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2131.10` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 1,980,000.00 USD | 1,750,000.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2133.10` | 981,150,000.00 USD | 981,150,000.00 USD | 0.00 USD | 937,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2134.00` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 2,170,000.00 USD | 550,450.00 USD | 308,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 3,440,000.00 USD | 301,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2135.70` | 980,210,000.00 USD | 980,210,000.00 USD | 0.00 USD | 27,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2136.90` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 746,340.00 USD | 845,110.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2138.30` | 980,190,000.00 USD | 980,190,000.00 USD | 0.00 USD | 251,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2139.80` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 1,110,000.00 USD | 1,000,000.00 USD | 635,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2142.70` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 1,550,000.00 USD | 510,270.00 USD | 434,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 9,300,000.00 USD | 298,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2145.60` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 678,800.00 USD | 1,230,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2148.50` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 485,890.00 USD | 474,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2151.40` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 0.00 USD | 20,460.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2154.30` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 128,430.00 USD | 510,660.00 USD | 32,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 23,380,000.00 USD | 288,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2157.20` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 388,210.00 USD | 831,780.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2160.10` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 497,380.00 USD | 1,170,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2163.00` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 715,680.00 USD | 623,390.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 904,350.00 USD | 265,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2165.90` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 25,540.00 USD | 0.00 USD | 68,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2168.80` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 1,700,000.00 USD | 373,180.00 USD | 810,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2171.70` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 479,540.00 USD | 765,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2174.60` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 0.00 USD | 734,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 109,710,000.00 USD | 264,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2185.00` | 112,420,000.00 USD | 154,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2194.90` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 141,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 909,930.00 USD | 42,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2197.80` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 2,440,000.00 USD | 3,270,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2200.70` | 979,930,000.00 USD | 979,930,000.00 USD | 284,470.00 USD | 217,490.00 USD | 225,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2200.70` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 3,120,000.00 USD | 3,140,000.00 USD | 3,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2203.30` | 979,210,000.00 USD | 979,210,000.00 USD | 1,050,000.00 USD | 0.00 USD | 696,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2203.60` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 3,280,000.00 USD | 624,500.00 USD | 3,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 1,470,000.00 USD | 41,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2205.90` | 977,460,000.00 USD | 977,460,000.00 USD | 611,820.00 USD | 2,480,000.00 USD | 781,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2206.50` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 6,920,000.00 USD | 6,050,000.00 USD | 3,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2208.50` | 973,580,000.00 USD | 973,580,000.00 USD | 2,490,000.00 USD | 101,520.00 USD | 3,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2209.40` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 10,720,000.00 USD | 5,060,000.00 USD | 4,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2211.10` | 967,940,000.00 USD | 967,940,000.00 USD | 2,240,000.00 USD | 1,870,000.00 USD | 568,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2212.30` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 8,350,000.00 USD | 9,670,000.00 USD | 9,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2213.70` | 963,270,000.00 USD | 963,270,000.00 USD | 5,690,000.00 USD | 2,980,000.00 USD | 2,910,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 1,830,000.00 USD | 39,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2215.20` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 17,290,000.00 USD | 12,680,000.00 USD | 8,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2216.30` | 951,690,000.00 USD | 951,690,000.00 USD | 6,130,000.00 USD | 6,230,000.00 USD | 4,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2218.10` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 13,860,000.00 USD | 12,610,000.00 USD | 7,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2218.90` | 934,900,000.00 USD | 934,900,000.00 USD | 4,690,000.00 USD | 3,890,000.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2221.00` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 10,310,000.00 USD | 7,500,000.00 USD | 7,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2221.50` | 924,690,000.00 USD | 924,690,000.00 USD | 2,660,000.00 USD | 3,060,000.00 USD | 741,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2223.90` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 11,430,000.00 USD | 8,700,000.00 USD | 11,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2224.10` | 918,220,000.00 USD | 918,220,000.00 USD | 4,050,000.00 USD | 4,300,000.00 USD | 3,250,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2225.00` | 1,590,000.00 USD | 38,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2226.70` | 906,630,000.00 USD | 906,630,000.00 USD | 5,400,000.00 USD | 3,540,000.00 USD | 2,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2226.80` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 9,460,000.00 USD | 8,430,000.00 USD | 4,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2229.30` | 894,990,000.00 USD | 894,990,000.00 USD | 3,790,000.00 USD | 2,000,000.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2229.70` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 10,530,000.00 USD | 7,740,000.00 USD | 15,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2231.90` | 887,940,000.00 USD | 887,940,000.00 USD | 4,070,000.00 USD | 3,010,000.00 USD | 3,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2232.60` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 13,610,000.00 USD | 4,400,000.00 USD | 12,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2234.50` | 877,540,000.00 USD | 877,540,000.00 USD | 7,150,000.00 USD | 3,320,000.00 USD | 4,610,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2235.00` | 1,290,000.00 USD | 36,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2235.50` | 2,030,000,000.00 USD | 2,030,000,000.00 USD | 12,460,000.00 USD | 12,630,000.00 USD | 4,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2237.10` | 862,460,000.00 USD | 862,460,000.00 USD | 1,850,000.00 USD | 3,250,000.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2238.40` | 2,000,000,000.00 USD | 2,000,000,000.00 USD | 7,230,000.00 USD | 8,790,000.00 USD | 5,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2239.70` | 854,160,000.00 USD | 854,160,000.00 USD | 972,850.00 USD | 1,270,000.00 USD | 29,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2241.30` | 1,980,000,000.00 USD | 1,980,000,000.00 USD | 5,380,000.00 USD | 5,410,000.00 USD | 10,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2242.30` | 851,890,000.00 USD | 851,890,000.00 USD | 836,930.00 USD | 918,390.00 USD | 1,470,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2244.20` | 1,960,000,000.00 USD | 1,960,000,000.00 USD | 10,350,000.00 USD | 8,810,000.00 USD | 12,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2244.90` | 848,670,000.00 USD | 848,670,000.00 USD | 2,500,000.00 USD | 2,540,000.00 USD | 369,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2245.00` | 4,640,000.00 USD | 35,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2247.10` | 1,930,000,000.00 USD | 1,930,000,000.00 USD | 16,790,000.00 USD | 10,060,000.00 USD | 9,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2247.50` | 843,270,000.00 USD | 843,270,000.00 USD | 2,240,000.00 USD | 903,300.00 USD | 2,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2250.00` | 1,890,000,000.00 USD | 1,890,000,000.00 USD | 11,760,000.00 USD | 9,350,000.00 USD | 8,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2250.10` | 838,110,000.00 USD | 838,110,000.00 USD | 3,310,000.00 USD | 958,610.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2252.70` | 832,050,000.00 USD | 832,050,000.00 USD | 5,690,000.00 USD | 6,690,000.00 USD | 4,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2252.90` | 1,860,000,000.00 USD | 1,860,000,000.00 USD | 24,550,000.00 USD | 17,220,000.00 USD | 16,920,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2255.00` | 10,910,000.00 USD | 30,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2255.30` | 815,030,000.00 USD | 815,030,000.00 USD | 3,330,000.00 USD | 2,320,000.00 USD | 5,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2255.80` | 1,800,000,000.00 USD | 1,800,000,000.00 USD | 23,870,000.00 USD | 18,230,000.00 USD | 15,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2257.90` | 803,980,000.00 USD | 803,980,000.00 USD | 8,440,000.00 USD | 3,960,000.00 USD | 4,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2258.70` | 1,750,000,000.00 USD | 1,750,000,000.00 USD | 29,540,000.00 USD | 22,530,000.00 USD | 25,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2260.50` | 786,730,000.00 USD | 786,730,000.00 USD | 15,640,000.00 USD | 9,850,000.00 USD | 10,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2261.60` | 1,670,000,000.00 USD | 1,670,000,000.00 USD | 48,100,000.00 USD | 31,730,000.00 USD | 21,740,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2263.10` | 750,780,000.00 USD | 750,780,000.00 USD | 10,850,000.00 USD | 14,100,000.00 USD | 10,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2264.50` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 33,190,000.00 USD | 30,310,000.00 USD | 21,680,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2265.00` | 3,260,000.00 USD | 19,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2265.70` | 715,400,000.00 USD | 715,400,000.00 USD | 13,000,000.00 USD | 10,690,000.00 USD | 4,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2267.40` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 39,370,000.00 USD | 40,010,000.00 USD | 34,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2268.30` | 687,510,000.00 USD | 687,510,000.00 USD | 9,920,000.00 USD | 10,320,000.00 USD | 5,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2270.30` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 41,070,000.00 USD | 27,630,000.00 USD | 39,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2270.90` | 661,970,000.00 USD | 661,970,000.00 USD | 9,090,000.00 USD | 9,720,000.00 USD | 7,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2273.20` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 33,160,000.00 USD | 25,760,000.00 USD | 20,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2273.50` | 635,890,000.00 USD | 635,890,000.00 USD | 14,150,000.00 USD | 8,430,000.00 USD | 9,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2275.00` | 6,850,000.00 USD | 16,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2276.10` | 604,280,000.00 USD | 604,280,000.00 USD | 17,930,000.00 USD | 14,340,000.00 USD | 10,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2276.10` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 54,840,000.00 USD | 46,910,000.00 USD | 49,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2278.70` | 561,050,000.00 USD | 561,050,000.00 USD | 14,910,000.00 USD | 9,250,000.00 USD | 13,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2279.00` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 74,170,000.00 USD | 30,780,000.00 USD | 49,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2281.30` | 523,230,000.00 USD | 523,230,000.00 USD | 23,500,000.00 USD | 13,310,000.00 USD | 16,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2281.90` | 874,780,000.00 USD | 874,780,000.00 USD | 64,370,000.00 USD | 63,970,000.00 USD | 39,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2283.90` | 470,200,000.00 USD | 470,200,000.00 USD | 34,180,000.00 USD | 23,760,000.00 USD | 22,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2284.80` | 706,560,000.00 USD | 706,560,000.00 USD | 95,240,000.00 USD | 73,600,000.00 USD | 47,330,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2285.00` | 4,100,000.00 USD | 9,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2286.50` | 389,290,000.00 USD | 389,290,000.00 USD | 17,530,000.00 USD | 23,820,000.00 USD | 13,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2287.70` | 490,390,000.00 USD | 490,390,000.00 USD | 55,750,000.00 USD | 55,240,000.00 USD | 51,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2289.10` | 334,780,000.00 USD | 334,780,000.00 USD | 18,070,000.00 USD | 17,140,000.00 USD | 4,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2290.60` | 327,680,000.00 USD | 327,680,000.00 USD | 39,440,000.00 USD | 32,400,000.00 USD | 46,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2291.70` | 294,820,000.00 USD | 294,820,000.00 USD | 22,990,000.00 USD | 19,890,000.00 USD | 11,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2293.50` | 208,910,000.00 USD | 208,910,000.00 USD | 41,720,000.00 USD | 20,380,000.00 USD | 18,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2294.30` | 240,930,000.00 USD | 240,930,000.00 USD | 12,130,000.00 USD | 15,570,000.00 USD | 11,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2295.00` | 3,310,000.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2296.40` | 127,860,000.00 USD | 127,860,000.00 USD | 8,030,000.00 USD | 4,300,000.00 USD | 3,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2296.90` | 201,400,000.00 USD | 201,400,000.00 USD | 20,370,000.00 USD | 9,140,000.00 USD | 5,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2299.30` | 111,820,000.00 USD | 111,820,000.00 USD | 13,410,000.00 USD | 6,480,000.00 USD | 216,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2299.50` | 166,070,000.00 USD | 166,070,000.00 USD | 17,470,000.00 USD | 7,400,000.00 USD | 7,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2302.10` | 133,730,000.00 USD | 133,730,000.00 USD | 16,300,000.00 USD | 12,620,000.00 USD | 14,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2302.20` | 91,720,000.00 USD | 91,720,000.00 USD | 12,400,000.00 USD | 3,870,000.00 USD | 18,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2304.70` | 90,220,000.00 USD | 90,220,000.00 USD | 0.00 USD | 15,080,000.00 USD | 22,080,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2305.00` | 940,780.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2305.10` | 56,520,000.00 USD | 56,520,000.00 USD | 20,580,000.00 USD | 15,290,000.00 USD | 5,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2307.30` | 53,060,000.00 USD | 53,060,000.00 USD | 0.00 USD | 6,370,000.00 USD | 6,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2308.00` | 15,320,000.00 USD | 15,320,000.00 USD | 0.00 USD | 2,150,000.00 USD | 134,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2309.90` | 40,580,000.00 USD | 40,580,000.00 USD | 1,440,000.00 USD | 3,190,000.00 USD | 172,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2310.90` | 13,030,000.00 USD | 13,030,000.00 USD | 1,740,000.00 USD | 512,220.00 USD | 97,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2312.50` | 35,780,000.00 USD | 35,780,000.00 USD | 8,850,000.00 USD | 8,520,000.00 USD | 57,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2313.80` | 10,680,000.00 USD | 10,680,000.00 USD | 2,840,000.00 USD | 7,650,000.00 USD | 188,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2315.00` | 932,620.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2315.10` | 18,350,000.00 USD | 18,350,000.00 USD | 6,990,000.00 USD | 9,370,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2316.70` | 235,270.00 USD | 235,270.00 USD | 0.00 USD | 235,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2317.70` | 13,030,000.00 USD | 13,030,000.00 USD | 8,890,000.00 USD | 4,140,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2319.60` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 5,370,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2320.30` | 17,880,000.00 USD | 17,880,000.00 USD | 1,680,000.00 USD | 3,110,000.00 USD | 61,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2322.50` | 9,570,000.00 USD | 9,570,000.00 USD | 3,130,000.00 USD | 835,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2322.90` | 19,500,000.00 USD | 19,500,000.00 USD | 0.00 USD | 1,620,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2325.00` | 321,320.00 USD | 329,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2325.40` | 11,300,000.00 USD | 11,300,000.00 USD | 0.00 USD | 1,740,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2325.50` | 22,270,000.00 USD | 22,270,000.00 USD | 0.00 USD | 2,700,000.00 USD | 66,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2328.10` | 22,820,000.00 USD | 22,820,000.00 USD | 256,580.00 USD | 206,450.00 USD | 89,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2328.30` | 15,290,000.00 USD | 15,290,000.00 USD | 3,860,000.00 USD | 0.00 USD | 126,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2330.70` | 32,810,000.00 USD | 32,810,000.00 USD | 9,820,000.00 USD | 0.00 USD | 168,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2331.20` | 38,320,000.00 USD | 38,320,000.00 USD | 23,030,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2333.30` | 46,310,000.00 USD | 46,310,000.00 USD | 10,110,000.00 USD | 0.00 USD | 3,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2334.10` | 55,930,000.00 USD | 55,930,000.00 USD | 6,760,000.00 USD | 10,860,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2335.00` | 7,680.00 USD | 7,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2335.90` | 57,870,000.00 USD | 57,870,000.00 USD | 11,430,000.00 USD | 140,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2337.00` | 88,070,000.00 USD | 88,070,000.00 USD | 18,070,000.00 USD | 7,570,000.00 USD | 6,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2338.50` | 59,460,000.00 USD | 59,460,000.00 USD | 0.00 USD | 130,330.00 USD | 1,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2339.90` | 114,680,000.00 USD | 114,680,000.00 USD | 9,570,000.00 USD | 5,360,000.00 USD | 11,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2341.10` | 61,140,000.00 USD | 61,140,000.00 USD | 0.00 USD | 0.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2342.80` | 128,720,000.00 USD | 128,720,000.00 USD | 0.00 USD | 10,200,000.00 USD | 3,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2343.70` | 69,490,000.00 USD | 69,490,000.00 USD | 120,800.00 USD | 1,960,000.00 USD | 6,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2345.70` | 143,590,000.00 USD | 143,590,000.00 USD | 1,350,000.00 USD | 7,920,000.00 USD | 5,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2346.30` | 78,750,000.00 USD | 78,750,000.00 USD | 3,350,000.00 USD | 0.00 USD | 5,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2348.60` | 175,170,000.00 USD | 175,170,000.00 USD | 285,680.00 USD | 7,240,000.00 USD | 24,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2348.90` | 85,490,000.00 USD | 85,490,000.00 USD | 5,710,000.00 USD | 42,760.00 USD | 990,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2351.50` | 116,260,000.00 USD | 116,260,000.00 USD | 21,900,000.00 USD | 2,850,000.00 USD | 6,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2351.50` | 199,310,000.00 USD | 199,310,000.00 USD | 782,590.00 USD | 17,680,000.00 USD | 5,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2354.10` | 133,690,000.00 USD | 133,690,000.00 USD | 3,200,000.00 USD | 13,490,000.00 USD | 743,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2354.40` | 240,820,000.00 USD | 240,820,000.00 USD | 6,120,000.00 USD | 35,020,000.00 USD | 371,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2356.70` | 143,380,000.00 USD | 143,380,000.00 USD | 2,050,000.00 USD | 5,880,000.00 USD | 1,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2357.30` | 255,480,000.00 USD | 255,480,000.00 USD | 8,740,000.00 USD | 5,920,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2359.30` | 156,790,000.00 USD | 156,790,000.00 USD | 2,130,000.00 USD | 5,440,000.00 USD | 5,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2360.20` | 264,770,000.00 USD | 264,770,000.00 USD | 2,690,000.00 USD | 3,430,000.00 USD | 3,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2361.90` | 168,920,000.00 USD | 168,920,000.00 USD | 4,100,000.00 USD | 6,710,000.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2363.10` | 267,170,000.00 USD | 267,170,000.00 USD | 715,490.00 USD | 0.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2364.50` | 179,870,000.00 USD | 179,870,000.00 USD | 3,220,000.00 USD | 3,710,000.00 USD | 4,000,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 1,020.00 USD | 1,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2366.00` | 275,180,000.00 USD | 275,180,000.00 USD | 6,340,000.00 USD | 0.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2367.10` | 183,440,000.00 USD | 183,440,000.00 USD | 3,350,000.00 USD | 0.00 USD | 231,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2368.90` | 296,830,000.00 USD | 296,830,000.00 USD | 20,720,000.00 USD | 475,460.00 USD | 450,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2369.70` | 208,110,000.00 USD | 208,110,000.00 USD | 14,110,000.00 USD | 6,790,000.00 USD | 3,760,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2371.80` | 360,330,000.00 USD | 360,330,000.00 USD | 12,810,000.00 USD | 0.00 USD | 50,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2372.30` | 240,520,000.00 USD | 240,520,000.00 USD | 11,110,000.00 USD | 10,170,000.00 USD | 11,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2374.70` | 387,280,000.00 USD | 387,280,000.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2374.90` | 259,100,000.00 USD | 259,100,000.00 USD | 13,050,000.00 USD | 335,190.00 USD | 5,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 47,010.00 USD | 48,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2377.50` | 292,940,000.00 USD | 292,940,000.00 USD | 11,940,000.00 USD | 10,700,000.00 USD | 11,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2377.60` | 417,610,000.00 USD | 417,610,000.00 USD | 8,770,000.00 USD | 6,190,000.00 USD | 15,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2380.10` | 327,480,000.00 USD | 327,480,000.00 USD | 12,150,000.00 USD | 7,970,000.00 USD | 14,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2380.50` | 447,140,000.00 USD | 447,140,000.00 USD | 6,830,000.00 USD | 2,590,000.00 USD | 20,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2382.70` | 386,390,000.00 USD | 386,390,000.00 USD | 22,820,000.00 USD | 19,890,000.00 USD | 16,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2383.40` | 498,030,000.00 USD | 498,030,000.00 USD | 8,610,000.00 USD | 17,490,000.00 USD | 24,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 3,730,000.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2385.30` | 427,170,000.00 USD | 427,170,000.00 USD | 10,330,000.00 USD | 20,100,000.00 USD | 10,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2386.30` | 612,320,000.00 USD | 612,320,000.00 USD | 17,450,000.00 USD | 41,020,000.00 USD | 55,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2387.90` | 452,200,000.00 USD | 452,200,000.00 USD | 14,010,000.00 USD | 6,140,000.00 USD | 4,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2389.20` | 684,890,000.00 USD | 684,890,000.00 USD | 3,900,000.00 USD | 30,140,000.00 USD | 38,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2390.50` | 471,740,000.00 USD | 471,740,000.00 USD | 6,350,000.00 USD | 5,300,000.00 USD | 7,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2392.10` | 791,710,000.00 USD | 791,710,000.00 USD | 17,810,000.00 USD | 45,620,000.00 USD | 43,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2393.10` | 496,140,000.00 USD | 496,140,000.00 USD | 5,640,000.00 USD | 12,500,000.00 USD | 6,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2395.00` | 896,980,000.00 USD | 896,980,000.00 USD | 47,110,000.00 USD | 28,070,000.00 USD | 30,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 4,420,000.00 USD | 8,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2395.70` | 509,390,000.00 USD | 509,390,000.00 USD | 4,830,000.00 USD | 5,770,000.00 USD | 2,650,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2397.90` | 992,610,000.00 USD | 992,610,000.00 USD | 37,230,000.00 USD | 36,430,000.00 USD | 21,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2398.30` | 529,790,000.00 USD | 529,790,000.00 USD | 5,450,000.00 USD | 8,020,000.00 USD | 6,930,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2400.80` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 42,170,000.00 USD | 25,680,000.00 USD | 25,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2400.90` | 557,460,000.00 USD | 557,460,000.00 USD | 9,660,000.00 USD | 8,230,000.00 USD | 9,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2403.50` | 582,810,000.00 USD | 582,810,000.00 USD | 9,560,000.00 USD | 7,020,000.00 USD | 8,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2403.70` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 56,800,000.00 USD | 25,430,000.00 USD | 29,870,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 9,120,000.00 USD | 17,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2406.10` | 610,590,000.00 USD | 610,590,000.00 USD | 12,760,000.00 USD | 7,480,000.00 USD | 7,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2406.60` | 1,270,000,000.00 USD | 1,270,000,000.00 USD | 23,950,000.00 USD | 34,300,000.00 USD | 16,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2408.70` | 640,440,000.00 USD | 640,440,000.00 USD | 7,950,000.00 USD | 14,910,000.00 USD | 6,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2409.50` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 27,600,000.00 USD | 26,770,000.00 USD | 24,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2411.30` | 661,410,000.00 USD | 661,410,000.00 USD | 8,580,000.00 USD | 7,900,000.00 USD | 4,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2412.40` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 16,560,000.00 USD | 15,580,000.00 USD | 15,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2413.90` | 670,510,000.00 USD | 670,510,000.00 USD | 4,510,000.00 USD | 1,390,000.00 USD | 3,200,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 459,730.00 USD | 17,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2415.30` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 20,360,000.00 USD | 20,510,000.00 USD | 25,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2416.50` | 687,360,000.00 USD | 687,360,000.00 USD | 4,790,000.00 USD | 7,670,000.00 USD | 4,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2418.20` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 31,510,000.00 USD | 13,720,000.00 USD | 19,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2419.10` | 698,140,000.00 USD | 698,140,000.00 USD | 5,120,000.00 USD | 2,280,000.00 USD | 3,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2421.10` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 22,270,000.00 USD | 27,860,000.00 USD | 21,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2421.70` | 714,410,000.00 USD | 714,410,000.00 USD | 4,170,000.00 USD | 6,200,000.00 USD | 5,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.00` | 1,680,000,000.00 USD | 1,680,000,000.00 USD | 18,610,000.00 USD | 31,660,000.00 USD | 30,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2424.30` | 720,250,000.00 USD | 720,250,000.00 USD | 1,790,000.00 USD | 3,040,000.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 816,560.00 USD | 18,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2426.90` | 721,550,000.00 USD | 721,550,000.00 USD | 731,900.00 USD | 369,950.00 USD | 200,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2426.90` | 1,760,000,000.00 USD | 1,760,000,000.00 USD | 27,510,000.00 USD | 22,000,000.00 USD | 26,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2429.50` | 726,260,000.00 USD | 726,260,000.00 USD | 1,330,000.00 USD | 1,770,000.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2429.80` | 1,780,000,000.00 USD | 1,780,000,000.00 USD | 6,630,000.00 USD | 12,550,000.00 USD | 6,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2432.10` | 730,170,000.00 USD | 730,170,000.00 USD | 2,010,000.00 USD | 1,690,000.00 USD | 210,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2432.70` | 1,820,000,000.00 USD | 1,820,000,000.00 USD | 17,550,000.00 USD | 15,730,000.00 USD | 6,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2434.70` | 733,710,000.00 USD | 733,710,000.00 USD | 1,670,000.00 USD | 468,310.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 8,040,000.00 USD | 26,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2435.60` | 1,870,000,000.00 USD | 1,870,000,000.00 USD | 20,760,000.00 USD | 13,900,000.00 USD | 12,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2437.30` | 735,650,000.00 USD | 735,650,000.00 USD | 1,200,000.00 USD | 531,390.00 USD | 205,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2438.50` | 1,930,000,000.00 USD | 1,930,000,000.00 USD | 18,000,000.00 USD | 21,640,000.00 USD | 14,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2439.90` | 738,900,000.00 USD | 738,900,000.00 USD | 1,540,000.00 USD | 1,230,000.00 USD | 479,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2441.40` | 1,960,000,000.00 USD | 1,960,000,000.00 USD | 14,700,000.00 USD | 6,350,000.00 USD | 11,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2442.50` | 742,370,000.00 USD | 742,370,000.00 USD | 1,050,000.00 USD | 1,380,000.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2444.30` | 2,000,000,000.00 USD | 2,000,000,000.00 USD | 8,760,000.00 USD | 15,160,000.00 USD | 13,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 143,630.00 USD | 26,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2445.10` | 744,570,000.00 USD | 744,570,000.00 USD | 50,900.00 USD | 939,450.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2447.20` | 2,030,000,000.00 USD | 2,030,000,000.00 USD | 10,560,000.00 USD | 7,370,000.00 USD | 16,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2447.70` | 749,820,000.00 USD | 749,820,000.00 USD | 1,890,000.00 USD | 659,940.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2450.10` | 2,070,000,000.00 USD | 2,070,000,000.00 USD | 13,890,000.00 USD | 11,970,000.00 USD | 13,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2450.30` | 757,430,000.00 USD | 757,430,000.00 USD | 2,540,000.00 USD | 2,140,000.00 USD | 2,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2452.90` | 766,470,000.00 USD | 766,470,000.00 USD | 3,360,000.00 USD | 2,300,000.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2453.00` | 2,090,000,000.00 USD | 2,090,000,000.00 USD | 8,570,000.00 USD | 7,390,000.00 USD | 6,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 106,960.00 USD | 26,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2455.50` | 775,890,000.00 USD | 775,890,000.00 USD | 2,900,000.00 USD | 4,240,000.00 USD | 2,280,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2455.90` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 5,870,000.00 USD | 8,500,000.00 USD | 6,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2458.10` | 781,160,000.00 USD | 781,160,000.00 USD | 2,250,000.00 USD | 1,790,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2458.80` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 10,310,000.00 USD | 12,000,000.00 USD | 10,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2460.70` | 784,720,000.00 USD | 784,720,000.00 USD | 1,260,000.00 USD | 1,130,000.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2461.70` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 10,100,000.00 USD | 11,320,000.00 USD | 10,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2463.30` | 787,870,000.00 USD | 787,870,000.00 USD | 0.00 USD | 2,050,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2464.60` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 7,830,000.00 USD | 3,900,000.00 USD | 3,560,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 483,330.00 USD | 27,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2465.90` | 789,010,000.00 USD | 789,010,000.00 USD | 352,200.00 USD | 780,010.00 USD | 5,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2467.50` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 4,540,000.00 USD | 3,120,000.00 USD | 586,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2468.50` | 789,960,000.00 USD | 789,960,000.00 USD | 0.00 USD | 957,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2470.40` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 2,330,000.00 USD | 2,290,000.00 USD | 496,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2471.10` | 790,610,000.00 USD | 790,610,000.00 USD | 0.00 USD | 257,700.00 USD | 391,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2473.30` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 5,250,000.00 USD | 2,920,000.00 USD | 2,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 386,010.00 USD | 27,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2476.20` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 2,680,000.00 USD | 1,500,000.00 USD | 872,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2479.10` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 2,170,000.00 USD | 4,160,000.00 USD | 505,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2482.00` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 1,750,000.00 USD | 1,520,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2484.90` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 0.00 USD | 0.00 USD | 77,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 2,000,000.00 USD | 29,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2487.80` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 826,600.00 USD | 828,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2490.70` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 808,320.00 USD | 1,780,000.00 USD | 279,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2493.60` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 1,610,000.00 USD | 1,690,000.00 USD | 3,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 941,300.00 USD | 30,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2496.50` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 1,670,000.00 USD | 4,820,000.00 USD | 6,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2499.40` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 1,900,000.00 USD | 2,950,000.00 USD | 3,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2502.30` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 647,370.00 USD | 1,090,000.00 USD | 125,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 119,320.00 USD | 30,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2505.20` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 1,400,000.00 USD | 2,310,000.00 USD | 103,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2508.10` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 2,940,000.00 USD | 1,640,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2511.00` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 2,560,000.00 USD | 3,230,000.00 USD | 2,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2513.90` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 776,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 139,000.00 USD | 30,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2516.80` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 97,050.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2519.70` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2520.50` | 790,790,000.00 USD | 790,790,000.00 USD | 80,610.00 USD | 61,830.00 USD | 32,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2522.60` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 1,050,000.00 USD | 0.00 USD | 945,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2523.10` | 790,850,000.00 USD | 790,850,000.00 USD | 0.00 USD | 0.00 USD | 57,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 1,160,000.00 USD | 32,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2525.50` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 307,040.00 USD | 241,310.00 USD | 200,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2525.70` | 791,380,000.00 USD | 791,380,000.00 USD | 421,540.00 USD | 57,450.00 USD | 53,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2528.30` | 792,050,000.00 USD | 792,050,000.00 USD | 0.00 USD | 645,910.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2528.40` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 1,580,000.00 USD | 1,670,000.00 USD | 727,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2530.90` | 793,490,000.00 USD | 793,490,000.00 USD | 995,550.00 USD | 0.00 USD | 437,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2531.30` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 2,720,000.00 USD | 1,490,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2533.50` | 793,960,000.00 USD | 793,960,000.00 USD | 394,310.00 USD | 62,630.00 USD | 16,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2534.20` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 2,550,000.00 USD | 1,720,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2535.00` | 663,280.00 USD | 32,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2536.10` | 796,850,000.00 USD | 796,850,000.00 USD | 1,160,000.00 USD | 656,520.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2537.10` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 3,380,000.00 USD | 3,160,000.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2538.70` | 800,840,000.00 USD | 800,840,000.00 USD | 1,870,000.00 USD | 524,750.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2540.00` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 3,930,000.00 USD | 3,190,000.00 USD | 831,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2541.30` | 802,820,000.00 USD | 802,820,000.00 USD | 889,420.00 USD | 832,630.00 USD | 260,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2542.90` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 2,510,000.00 USD | 2,470,000.00 USD | 2,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2543.90` | 805,020,000.00 USD | 805,020,000.00 USD | 959,500.00 USD | 1,230,000.00 USD | 14,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2545.00` | 6,460,000.00 USD | 39,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2545.80` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 1,770,000.00 USD | 1,140,000.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2546.50` | 808,670,000.00 USD | 808,670,000.00 USD | 1,630,000.00 USD | 1,260,000.00 USD | 751,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2548.70` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 3,840,000.00 USD | 1,820,000.00 USD | 3,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2549.10` | 810,380,000.00 USD | 810,380,000.00 USD | 441,860.00 USD | 793,640.00 USD | 479,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2551.60` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 2,250,000.00 USD | 1,800,000.00 USD | 907,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2551.70` | 813,020,000.00 USD | 813,020,000.00 USD | 1,350,000.00 USD | 907,450.00 USD | 382,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2554.30` | 814,580,000.00 USD | 814,580,000.00 USD | 1,100,000.00 USD | 215,480.00 USD | 236,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2554.50` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 3,880,000.00 USD | 948,120.00 USD | 3,930,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2555.00` | 2,830,000.00 USD | 42,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2556.90` | 816,530,000.00 USD | 816,530,000.00 USD | 705,250.00 USD | 506,330.00 USD | 740,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2557.40` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 2,780,000.00 USD | 737,060.00 USD | 5,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2559.50` | 820,370,000.00 USD | 820,370,000.00 USD | 1,830,000.00 USD | 1,040,000.00 USD | 978,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2560.30` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 3,540,000.00 USD | 1,450,000.00 USD | 589,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2562.10` | 822,810,000.00 USD | 822,810,000.00 USD | 451,210.00 USD | 797,210.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2563.20` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 1,400,000.00 USD | 2,900,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2564.70` | 824,160,000.00 USD | 824,160,000.00 USD | 425,980.00 USD | 669,810.00 USD | 248,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2565.00` | 1,790,000.00 USD | 43,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2566.10` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 1,860,000.00 USD | 1,430,000.00 USD | 2,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2567.30` | 824,480,000.00 USD | 824,480,000.00 USD | 121,690.00 USD | 31,040.00 USD | 175,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2569.00` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 56,010.00 USD | 739,480.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2569.90` | 825,610,000.00 USD | 825,610,000.00 USD | 530,980.00 USD | 289,160.00 USD | 302,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2571.90` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 1,390,000.00 USD | 183,530.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2572.50` | 826,880,000.00 USD | 826,880,000.00 USD | 588,810.00 USD | 671,930.00 USD | 16,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2574.80` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 1,450,000.00 USD | 834,660.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2575.00` | 11,830,000.00 USD | 55,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2575.10` | 827,930,000.00 USD | 827,930,000.00 USD | 546,100.00 USD | 0.00 USD | 502,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2577.70` | 828,080,000.00 USD | 828,080,000.00 USD | 118,210.00 USD | 21,400.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2577.70` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 2,090,000.00 USD | 1,570,000.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2580.30` | 828,680,000.00 USD | 828,680,000.00 USD | 414,360.00 USD | 0.00 USD | 188,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2580.60` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 2,990,000.00 USD | 1,140,000.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2583.50` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 1,080,000.00 USD | 1,260,000.00 USD | 2,720,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2585.00` | 26,470,000.00 USD | 82,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2586.40` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 1,430,000.00 USD | 2,010,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2589.30` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 2,060,000.00 USD | 631,590.00 USD | 2,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2592.20` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 3,590,000.00 USD | 1,280,000.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2595.00` | 8,180,000.00 USD | 90,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2595.10` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 452,020.00 USD | 569,790.00 USD | 752,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2598.00` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 2,280,000.00 USD | 1,630,000.00 USD | 2,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2600.90` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 931,390.00 USD | 1,960,000.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2603.80` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 1,600,000.00 USD | 1,580,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2605.00` | 660,550.00 USD | 91,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2606.70` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 1,480,000.00 USD | 463,200.00 USD | 312,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2609.60` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 1,140,000.00 USD | 510,700.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2612.50` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 962,930.00 USD | 622,830.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2615.00` | 1,190,000.00 USD | 92,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2615.40` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 815,100.00 USD | 967,270.00 USD | 635,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2618.30` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 1,550,000.00 USD | 209,240.00 USD | 434,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2621.20` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 547,980.00 USD | 1,530,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2624.10` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 130,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2625.00` | 453,080.00 USD | 92,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2635.00` | 175,730.00 USD | 92,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2645.00` | 163,860.00 USD | 92,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2655.00` | 35,640,000.00 USD | 128,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2665.00` | 68,220.00 USD | 128,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2675.00` | 121,140.00 USD | 128,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2685.00` | 7,680,000.00 USD | 136,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2695.00` | 132,910.00 USD | 136,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2705.00` | 42,520,000.00 USD | 179,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2715.00` | 3,460,000.00 USD | 182,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2725.00` | 347,630.00 USD | 182,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2735.00` | 3,610,000.00 USD | 186,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2745.00` | 937,840.00 USD | 187,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2755.00` | 632,790.00 USD | 188,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2765.00` | 299,800.00 USD | 188,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2775.00` | 97,340.00 USD | 188,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2785.00` | 6,920,000.00 USD | 195,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2795.00` | 115,010.00 USD | 195,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2805.00` | 859,600.00 USD | 196,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2815.00` | 284,990.00 USD | 196,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2825.00` | 83,990.00 USD | 196,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2835.00` | 3,370,000.00 USD | 200,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2845.00` | 2,360,000.00 USD | 202,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2855.00` | 188,540.00 USD | 202,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2865.00` | 44,730,000.00 USD | 247,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2875.00` | 23,070,000.00 USD | 270,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2885.00` | 3,890,000.00 USD | 274,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2895.00` | 1,400,000.00 USD | 275,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2905.00` | 453,700.00 USD | 276,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2915.00` | 447,640.00 USD | 276,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2925.00` | 26,510,000.00 USD | 303,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2935.00` | 1,440,000.00 USD | 304,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2945.00` | 7,480,000.00 USD | 312,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2955.00` | 21,080,000.00 USD | 333,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2965.00` | 1,420,000.00 USD | 334,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2975.00` | 221,010.00 USD | 334,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2985.00` | 818,270.00 USD | 335,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2995.00` | 814,800.00 USD | 336,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3005.00` | 3,520,000.00 USD | 340,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3015.00` | 363,690.00 USD | 340,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3025.00` | 8,280,000.00 USD | 348,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3035.00` | 3,640,000.00 USD | 352,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3045.00` | 13,150,000.00 USD | 365,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3055.00` | 4,830,000.00 USD | 370,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3065.00` | 632,420.00 USD | 370,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3075.00` | 4,010,000.00 USD | 374,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3085.00` | 110,980.00 USD | 375,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3095.00` | 1,790,000.00 USD | 376,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3105.00` | 597,120.00 USD | 377,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3115.00` | 104,410.00 USD | 377,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3125.00` | 136,660.00 USD | 377,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3135.00` | 1,670,000.00 USD | 379,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3145.00` | 1,530,000.00 USD | 380,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3155.00` | 6,220,000.00 USD | 387,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3165.00` | 1,480.00 USD | 387,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3175.00` | 658,490.00 USD | 387,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3185.00` | 1,070,000.00 USD | 388,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3195.00` | 3,510,000.00 USD | 392,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3205.00` | 90,340.00 USD | 392,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3215.00` | 590,760.00 USD | 392,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3225.00` | 5,000,000.00 USD | 397,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3235.00` | 9,070,000.00 USD | 407,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3245.00` | 20,630.00 USD | 407,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3255.00` | 303,690.00 USD | 407,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3265.00` | 359,730.00 USD | 407,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3275.00` | 117,840.00 USD | 407,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3285.00` | 9,130,000.00 USD | 416,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3295.00` | 1,270,000.00 USD | 418,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3305.00` | 66,520.00 USD | 418,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3315.00` | 11,660,000.00 USD | 429,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3325.00` | 130,190.00 USD | 430,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3335.00` | 27,410.00 USD | 430,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3345.00` | 839,420.00 USD | 430,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3355.00` | 62,730,000.00 USD | 493,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3365.00` | 1,040,000.00 USD | 494,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3375.00` | 110,710.00 USD | 494,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3385.00` | 162,990.00 USD | 495,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3395.00` | 238,960.00 USD | 495,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3405.00` | 125,120.00 USD | 495,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3415.00` | 3,140,000.00 USD | 498,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3425.00` | 14,460,000.00 USD | 512,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3435.00` | 240,520.00 USD | 513,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3445.00` | 40,690.00 USD | 513,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3455.00` | 5,450,000.00 USD | 518,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3465.00` | 1,150,000.00 USD | 519,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3475.00` | 442,570.00 USD | 520,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3485.00` | 79,550.00 USD | 520,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3495.00` | 1,670,000.00 USD | 522,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3505.00` | 15,890.00 USD | 522,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3515.00` | 35,660.00 USD | 522,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3525.00` | 78,800.00 USD | 522,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3535.00` | 39,410.00 USD | 522,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3545.00` | 7,150,000.00 USD | 529,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3555.00` | 143,600.00 USD | 529,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3565.00` | 310,340.00 USD | 529,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3575.00` | 78,340.00 USD | 529,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3585.00` | 477,460.00 USD | 530,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3595.00` | 302,580.00 USD | 530,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3605.00` | 71,590.00 USD | 530,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3615.00` | 3,830,000.00 USD | 534,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3625.00` | 539,240.00 USD | 535,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3635.00` | 103,240,000.00 USD | 638,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3645.00` | 6,570,000.00 USD | 644,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3655.00` | 378,780.00 USD | 645,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3665.00` | 1,100,000.00 USD | 646,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3675.00` | 367,730.00 USD | 646,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3685.00` | 1,900,000.00 USD | 648,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3695.00` | 1,090,000.00 USD | 649,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3705.00` | 305,070.00 USD | 650,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3715.00` | 8,320,000.00 USD | 658,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3725.00` | 249,910.00 USD | 658,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3735.00` | 34,780,000.00 USD | 693,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3745.00` | 841,120.00 USD | 694,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3755.00` | 13,450,000.00 USD | 707,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3765.00` | 84,490.00 USD | 707,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3775.00` | 351,950.00 USD | 708,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3785.00` | 45,720.00 USD | 708,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3795.00` | 271,140.00 USD | 708,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3805.00` | 81,730.00 USD | 708,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3815.00` | 211,350.00 USD | 708,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3825.00` | 338,010.00 USD | 709,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3835.00` | 408,410,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3845.00` | 1,590,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3855.00` | 1,780,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3865.00` | 15,960,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3885.00` | 1,420,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3895.00` | 130,520.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3905.00` | 1,430,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3915.00` | 4,700.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3925.00` | 199,870.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3935.00` | 1,640,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3945.00` | 25,640.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3955.00` | 404,950.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3965.00` | 680,870.00 USD | 1,140,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3975.00` | 90,050,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3985.00` | 3,920,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3995.00` | 30,460,000.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4005.00` | 216,180.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4015.00` | 117,490.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4025.00` | 824,230.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4035.00` | 67,410,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4045.00` | 1,580,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4055.00` | 470,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4065.00` | 2,090,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4075.00` | 2,430,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4085.00` | 287,790.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4105.00` | 2,890,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4115.00` | 83,350.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4125.00` | 27,910.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4135.00` | 864,500.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4145.00` | 169,420.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4155.00` | 492,990.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4165.00` | 280,240.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4185.00` | 4,130,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4195.00` | 84,530.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4205.00` | 674.90 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4215.00` | 6,950.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4225.00` | 18,600,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4235.00` | 1,420.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4245.00` | 4,670.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4255.00` | 99,390.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4265.00` | 68,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4275.00` | 17,020,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4285.00` | 217,490.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4295.00` | 2,460.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4305.00` | 8,250.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4315.00` | 328,280.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4325.00` | 31,660.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4335.00` | 19,940.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4345.00` | 2,270,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4355.00` | 43,740.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4365.00` | 598,460.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4375.00` | 849,070.00 USD | 1,390,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4385.00` | 285,930,000.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4395.00` | 93,330.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4405.00` | 26,050.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4415.00` | 633,470.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4425.00` | 1,930,000.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4445.00` | 685,460.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4455.00` | 490,070.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4465.00` | 80,330.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4475.00` | 36,810.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4485.00` | 20,940.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4495.00` | 12,800.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4505.00` | 2,440,000.00 USD | 1,680,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4515.00` | 3,840,000.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4525.00` | 981,310.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4535.00` | 86,800.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4545.00` | 23,190.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4555.00` | 43,530.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4565.00` | 265,340.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4575.00` | 137,500.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4585.00` | 35,590.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4595.00` | 251,050.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4605.00` | 37,010.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4615.00` | 52,010.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4625.00` | 406,220.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4635.00` | 231,230.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4645.00` | 175,430.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4655.00` | 1,360,000.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4665.00` | 35,090.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4675.00` | 50,490.00 USD | 1,690,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

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
| `7D` | `2067.30` | 2,520,000,000.00 USD | 0.00 USD | 2,520,000,000.00 USD | 452,190.00 USD | 295,290.00 USD | 262,430.00 USD |
| `7D` | `2070.20` | 2,520,000,000.00 USD | 0.00 USD | 2,520,000,000.00 USD | 2,800,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD |
| `1D` | `2070.70` | 1,030,000,000.00 USD | 0.00 USD | 1,030,000,000.00 USD | 995,550.00 USD | 57,450.00 USD | 487,960.00 USD |
| `7D` | `2073.10` | 2,510,000,000.00 USD | 0.00 USD | 2,510,000,000.00 USD | 3,550,000.00 USD | 2,100,000.00 USD | 2,030,000.00 USD |
| `1D` | `2073.30` | 1,030,000,000.00 USD | 0.00 USD | 1,030,000,000.00 USD | 419,970.00 USD | 62,630.00 USD | 506,550.00 USD |
| `1D` | `2075.90` | 1,030,000,000.00 USD | 0.00 USD | 1,030,000,000.00 USD | 2,580,000.00 USD | 901,140.00 USD | 1,610,000.00 USD |
| `7D` | `2076.00` | 2,500,000,000.00 USD | 0.00 USD | 2,500,000,000.00 USD | 3,910,000.00 USD | 4,290,000.00 USD | 3,540,000.00 USD |
| `1D` | `2078.50` | 1,020,000,000.00 USD | 0.00 USD | 1,020,000,000.00 USD | 1,140,000.00 USD | 1,100,000.00 USD | 632,440.00 USD |
| `7D` | `2078.90` | 2,490,000,000.00 USD | 0.00 USD | 2,490,000,000.00 USD | 4,500,000.00 USD | 3,730,000.00 USD | 2,040,000.00 USD |
| `1D` | `2081.10` | 1,020,000,000.00 USD | 0.00 USD | 1,020,000,000.00 USD | 1,140,000.00 USD | 1,080,000.00 USD | 212,890.00 USD |
| `7D` | `2081.80` | 2,480,000,000.00 USD | 0.00 USD | 2,480,000,000.00 USD | 3,370,000.00 USD | 1,290,000.00 USD | 1,240,000.00 USD |
| `1D` | `2083.70` | 1,020,000,000.00 USD | 0.00 USD | 1,020,000,000.00 USD | 1,670,000.00 USD | 1,420,000.00 USD | 755,170.00 USD |
| `7D` | `2084.70` | 2,470,000,000.00 USD | 0.00 USD | 2,470,000,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 4,170,000.00 USD |
| `1D` | `2086.30` | 1,010,000,000.00 USD | 0.00 USD | 1,010,000,000.00 USD | 961,460.00 USD | 1,470,000.00 USD | 649,210.00 USD |
| `7D` | `2087.60` | 2,470,000,000.00 USD | 0.00 USD | 2,470,000,000.00 USD | 3,960,000.00 USD | 2,750,000.00 USD | 1,650,000.00 USD |
| `1D` | `2088.90` | 1,010,000,000.00 USD | 0.00 USD | 1,010,000,000.00 USD | 1,180,000.00 USD | 430,310.00 USD | 227,850.00 USD |
| `7D` | `2090.50` | 2,460,000,000.00 USD | 0.00 USD | 2,460,000,000.00 USD | 4,370,000.00 USD | 976,840.00 USD | 6,980,000.00 USD |
| `1D` | `2091.50` | 1,010,000,000.00 USD | 0.00 USD | 1,010,000,000.00 USD | 1,260,000.00 USD | 469,640.00 USD | 796,710.00 USD |
| `7D` | `2093.40` | 2,440,000,000.00 USD | 0.00 USD | 2,440,000,000.00 USD | 3,930,000.00 USD | 1,200,000.00 USD | 2,950,000.00 USD |
| `1D` | `2094.10` | 1,010,000,000.00 USD | 0.00 USD | 1,010,000,000.00 USD | 1,990,000.00 USD | 1,090,000.00 USD | 1,140,000.00 USD |
| `7D` | `2096.30` | 2,440,000,000.00 USD | 0.00 USD | 2,440,000,000.00 USD | 3,150,000.00 USD | 2,430,000.00 USD | 1,290,000.00 USD |
| `1D` | `2096.70` | 1,000,000,000.00 USD | 0.00 USD | 1,000,000,000.00 USD | 597,710.00 USD | 797,210.00 USD | 1,190,000.00 USD |
| `7D` | `2099.20` | 2,430,000,000.00 USD | 0.00 USD | 2,430,000,000.00 USD | 1,460,000.00 USD | 2,100,000.00 USD | 1,270,000.00 USD |
| `1D` | `2099.30` | 999,100,000.00 USD | 0.00 USD | 999,100,000.00 USD | 401,170.00 USD | 700,850.00 USD | 256,530.00 USD |
| `1D` | `2101.90` | 997,740,000.00 USD | 0.00 USD | 997,740,000.00 USD | 162,270.00 USD | 119,690.00 USD | 470,640.00 USD |
| `7D` | `2102.10` | 2,430,000,000.00 USD | 0.00 USD | 2,430,000,000.00 USD | 678,000.00 USD | 1,510,000.00 USD | 2,790,000.00 USD |
| `1D` | `2104.50` | 996,990,000.00 USD | 0.00 USD | 996,990,000.00 USD | 957,520.00 USD | 841,400.00 USD | 16,280.00 USD |
| `7D` | `2105.00` | 2,420,000,000.00 USD | 0.00 USD | 2,420,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 2,220,000.00 USD |
| `1D` | `2107.10` | 995,180,000.00 USD | 0.00 USD | 995,180,000.00 USD | 546,100.00 USD | 0.00 USD | 502,840.00 USD |
| `7D` | `2107.90` | 2,410,000,000.00 USD | 0.00 USD | 2,410,000,000.00 USD | 2,320,000.00 USD | 356,360.00 USD | 1,640,000.00 USD |
| `1D` | `2109.70` | 994,130,000.00 USD | 0.00 USD | 994,130,000.00 USD | 118,210.00 USD | 31,550.00 USD | 8,540.00 USD |
| `7D` | `2110.80` | 2,410,000,000.00 USD | 0.00 USD | 2,410,000,000.00 USD | 2,830,000.00 USD | 2,350,000.00 USD | 2,170,000.00 USD |
| `1D` | `2112.30` | 993,970,000.00 USD | 0.00 USD | 993,970,000.00 USD | 902,600.00 USD | 643,210.00 USD | 413,100.00 USD |
| `7D` | `2113.70` | 2,400,000,000.00 USD | 0.00 USD | 2,400,000,000.00 USD | 1,780,000.00 USD | 1,300,000.00 USD | 2,730,000.00 USD |
| `1D` | `2114.90` | 992,010,000.00 USD | 0.00 USD | 992,010,000.00 USD | 9,210.00 USD | 0.00 USD | 441,270.00 USD |
| `7D` | `2116.60` | 2,400,000,000.00 USD | 0.00 USD | 2,400,000,000.00 USD | 2,360,000.00 USD | 2,350,000.00 USD | 2,570,000.00 USD |
| `1D` | `2117.50` | 991,560,000.00 USD | 0.00 USD | 991,560,000.00 USD | 679,710.00 USD | 17,360.00 USD | 811,240.00 USD |
| `7D` | `2119.50` | 2,390,000,000.00 USD | 0.00 USD | 2,390,000,000.00 USD | 2,530,000.00 USD | 606,940.00 USD | 2,590,000.00 USD |
| `1D` | `2120.10` | 990,050,000.00 USD | 0.00 USD | 990,050,000.00 USD | 198,890.00 USD | 428,990.00 USD | 1,020,000.00 USD |
| `7D` | `2122.40` | 2,380,000,000.00 USD | 0.00 USD | 2,380,000,000.00 USD | 2,230,000.00 USD | 1,000,000.00 USD | 1,630,000.00 USD |
| `1D` | `2122.70` | 988,410,000.00 USD | 0.00 USD | 988,410,000.00 USD | 1,030,000.00 USD | 522,540.00 USD | 851,670.00 USD |
| `1D` | `2125.30` | 986,000,000.00 USD | 0.00 USD | 986,000,000.00 USD | 714,970.00 USD | 1,120,000.00 USD | 631,470.00 USD |
| `7D` | `2125.30` | 2,380,000,000.00 USD | 0.00 USD | 2,380,000,000.00 USD | 2,700,000.00 USD | 2,150,000.00 USD | 2,650,000.00 USD |
| `1D` | `2127.90` | 983,530,000.00 USD | 0.00 USD | 983,530,000.00 USD | 365,910.00 USD | 1,040,000.00 USD | 301,140.00 USD |
| `7D` | `2128.20` | 2,370,000,000.00 USD | 0.00 USD | 2,370,000,000.00 USD | 931,390.00 USD | 1,960,000.00 USD | 1,950,000.00 USD |
| `1D` | `2130.50` | 981,820,000.00 USD | 0.00 USD | 981,820,000.00 USD | 0.00 USD | 18,610.00 USD | 654,700.00 USD |
| `7D` | `2131.10` | 2,370,000,000.00 USD | 0.00 USD | 2,370,000,000.00 USD | 1,980,000.00 USD | 1,750,000.00 USD | 1,370,000.00 USD |
| `1D` | `2133.10` | 981,150,000.00 USD | 0.00 USD | 981,150,000.00 USD | 0.00 USD | 937,720.00 USD | 0.00 USD |
| `7D` | `2134.00` | 2,360,000,000.00 USD | 0.00 USD | 2,360,000,000.00 USD | 2,170,000.00 USD | 550,450.00 USD | 308,060.00 USD |
| `1D` | `2135.70` | 980,210,000.00 USD | 0.00 USD | 980,210,000.00 USD | 0.00 USD | 27,230.00 USD | 0.00 USD |
| `7D` | `2136.90` | 2,360,000,000.00 USD | 0.00 USD | 2,360,000,000.00 USD | 746,340.00 USD | 845,110.00 USD | 43,560.00 USD |
| `1D` | `2138.30` | 980,190,000.00 USD | 0.00 USD | 980,190,000.00 USD | 0.00 USD | 251,180.00 USD | 0.00 USD |
| `7D` | `2139.80` | 2,360,000,000.00 USD | 0.00 USD | 2,360,000,000.00 USD | 1,110,000.00 USD | 1,000,000.00 USD | 635,670.00 USD |
| `7D` | `2142.70` | 2,350,000,000.00 USD | 0.00 USD | 2,350,000,000.00 USD | 1,550,000.00 USD | 510,270.00 USD | 434,750.00 USD |
| `7D` | `2145.60` | 2,350,000,000.00 USD | 0.00 USD | 2,350,000,000.00 USD | 678,800.00 USD | 1,230,000.00 USD | 0.00 USD |
| `7D` | `2148.50` | 2,350,000,000.00 USD | 0.00 USD | 2,350,000,000.00 USD | 485,890.00 USD | 474,490.00 USD | 0.00 USD |
| `7D` | `2151.40` | 2,350,000,000.00 USD | 0.00 USD | 2,350,000,000.00 USD | 0.00 USD | 20,460.00 USD | 31,040.00 USD |
| `7D` | `2154.30` | 2,350,000,000.00 USD | 0.00 USD | 2,350,000,000.00 USD | 128,430.00 USD | 510,660.00 USD | 32,590.00 USD |
| `7D` | `2157.20` | 2,350,000,000.00 USD | 0.00 USD | 2,350,000,000.00 USD | 388,210.00 USD | 831,780.00 USD | 1,080,000.00 USD |
| `7D` | `2160.10` | 2,350,000,000.00 USD | 0.00 USD | 2,350,000,000.00 USD | 497,380.00 USD | 1,170,000.00 USD | 1,990,000.00 USD |
| `7D` | `2163.00` | 2,340,000,000.00 USD | 0.00 USD | 2,340,000,000.00 USD | 715,680.00 USD | 623,390.00 USD | 1,210,000.00 USD |
| `7D` | `2165.90` | 2,340,000,000.00 USD | 0.00 USD | 2,340,000,000.00 USD | 25,540.00 USD | 0.00 USD | 68,110.00 USD |
| `7D` | `2168.80` | 2,340,000,000.00 USD | 0.00 USD | 2,340,000,000.00 USD | 1,700,000.00 USD | 373,180.00 USD | 810,540.00 USD |
| `7D` | `2171.70` | 2,340,000,000.00 USD | 0.00 USD | 2,340,000,000.00 USD | 479,540.00 USD | 765,150.00 USD | 0.00 USD |
| `7D` | `2174.60` | 2,340,000,000.00 USD | 0.00 USD | 2,340,000,000.00 USD | 0.00 USD | 734,270.00 USD | 0.00 USD |
| `7D` | `2194.90` | 2,340,000,000.00 USD | 0.00 USD | 2,340,000,000.00 USD | 141,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2197.80` | 2,340,000,000.00 USD | 0.00 USD | 2,340,000,000.00 USD | 2,440,000.00 USD | 3,270,000.00 USD | 0.00 USD |
| `1D` | `2200.70` | 979,930,000.00 USD | 0.00 USD | 979,930,000.00 USD | 284,470.00 USD | 217,490.00 USD | 225,330.00 USD |
| `7D` | `2200.70` | 2,330,000,000.00 USD | 0.00 USD | 2,330,000,000.00 USD | 3,120,000.00 USD | 3,140,000.00 USD | 3,200,000.00 USD |
| `1D` | `2203.30` | 979,210,000.00 USD | 0.00 USD | 979,210,000.00 USD | 1,050,000.00 USD | 0.00 USD | 696,550.00 USD |
| `7D` | `2203.60` | 2,320,000,000.00 USD | 0.00 USD | 2,320,000,000.00 USD | 3,280,000.00 USD | 624,500.00 USD | 3,830,000.00 USD |
| `1D` | `2205.90` | 977,460,000.00 USD | 0.00 USD | 977,460,000.00 USD | 611,820.00 USD | 2,480,000.00 USD | 781,320.00 USD |
| `7D` | `2206.50` | 2,310,000,000.00 USD | 0.00 USD | 2,310,000,000.00 USD | 6,920,000.00 USD | 6,050,000.00 USD | 3,870,000.00 USD |
| `1D` | `2208.50` | 973,580,000.00 USD | 0.00 USD | 973,580,000.00 USD | 2,490,000.00 USD | 101,520.00 USD | 3,050,000.00 USD |
| `7D` | `2209.40` | 2,300,000,000.00 USD | 0.00 USD | 2,300,000,000.00 USD | 10,720,000.00 USD | 5,060,000.00 USD | 4,130,000.00 USD |
| `1D` | `2211.10` | 967,940,000.00 USD | 0.00 USD | 967,940,000.00 USD | 2,240,000.00 USD | 1,870,000.00 USD | 568,830.00 USD |
| `7D` | `2212.30` | 2,280,000,000.00 USD | 0.00 USD | 2,280,000,000.00 USD | 8,350,000.00 USD | 9,670,000.00 USD | 9,120,000.00 USD |
| `1D` | `2213.70` | 963,270,000.00 USD | 0.00 USD | 963,270,000.00 USD | 5,690,000.00 USD | 2,980,000.00 USD | 2,910,000.00 USD |
| `7D` | `2215.20` | 2,250,000,000.00 USD | 0.00 USD | 2,250,000,000.00 USD | 17,290,000.00 USD | 12,680,000.00 USD | 8,750,000.00 USD |
| `1D` | `2216.30` | 951,690,000.00 USD | 0.00 USD | 951,690,000.00 USD | 6,130,000.00 USD | 6,230,000.00 USD | 4,430,000.00 USD |
| `7D` | `2218.10` | 2,210,000,000.00 USD | 0.00 USD | 2,210,000,000.00 USD | 13,860,000.00 USD | 12,610,000.00 USD | 7,500,000.00 USD |
| `1D` | `2218.90` | 934,900,000.00 USD | 0.00 USD | 934,900,000.00 USD | 4,690,000.00 USD | 3,890,000.00 USD | 1,640,000.00 USD |
| `7D` | `2221.00` | 2,180,000,000.00 USD | 0.00 USD | 2,180,000,000.00 USD | 10,310,000.00 USD | 7,500,000.00 USD | 7,540,000.00 USD |
| `1D` | `2221.50` | 924,690,000.00 USD | 0.00 USD | 924,690,000.00 USD | 2,660,000.00 USD | 3,060,000.00 USD | 741,850.00 USD |
| `7D` | `2223.90` | 2,150,000,000.00 USD | 0.00 USD | 2,150,000,000.00 USD | 11,430,000.00 USD | 8,700,000.00 USD | 11,390,000.00 USD |
| `1D` | `2224.10` | 918,220,000.00 USD | 0.00 USD | 918,220,000.00 USD | 4,050,000.00 USD | 4,300,000.00 USD | 3,250,000.00 USD |
| `1D` | `2226.70` | 906,630,000.00 USD | 0.00 USD | 906,630,000.00 USD | 5,400,000.00 USD | 3,540,000.00 USD | 2,710,000.00 USD |
| `7D` | `2226.80` | 2,120,000,000.00 USD | 0.00 USD | 2,120,000,000.00 USD | 9,460,000.00 USD | 8,430,000.00 USD | 4,260,000.00 USD |
| `1D` | `2229.30` | 894,990,000.00 USD | 0.00 USD | 894,990,000.00 USD | 3,790,000.00 USD | 2,000,000.00 USD | 1,260,000.00 USD |
| `7D` | `2229.70` | 2,100,000,000.00 USD | 0.00 USD | 2,100,000,000.00 USD | 10,530,000.00 USD | 7,740,000.00 USD | 15,780,000.00 USD |
| `1D` | `2231.90` | 887,940,000.00 USD | 0.00 USD | 887,940,000.00 USD | 4,070,000.00 USD | 3,010,000.00 USD | 3,310,000.00 USD |
| `7D` | `2232.60` | 2,060,000,000.00 USD | 0.00 USD | 2,060,000,000.00 USD | 13,610,000.00 USD | 4,400,000.00 USD | 12,930,000.00 USD |
| `1D` | `2234.50` | 877,540,000.00 USD | 0.00 USD | 877,540,000.00 USD | 7,150,000.00 USD | 3,320,000.00 USD | 4,610,000.00 USD |
| `7D` | `2235.50` | 2,030,000,000.00 USD | 0.00 USD | 2,030,000,000.00 USD | 12,460,000.00 USD | 12,630,000.00 USD | 4,750,000.00 USD |
| `1D` | `2237.10` | 862,460,000.00 USD | 0.00 USD | 862,460,000.00 USD | 1,850,000.00 USD | 3,250,000.00 USD | 3,190,000.00 USD |
| `7D` | `2238.40` | 2,000,000,000.00 USD | 0.00 USD | 2,000,000,000.00 USD | 7,230,000.00 USD | 8,790,000.00 USD | 5,510,000.00 USD |
| `1D` | `2239.70` | 854,160,000.00 USD | 0.00 USD | 854,160,000.00 USD | 972,850.00 USD | 1,270,000.00 USD | 29,820.00 USD |
| `7D` | `2241.30` | 1,980,000,000.00 USD | 0.00 USD | 1,980,000,000.00 USD | 5,380,000.00 USD | 5,410,000.00 USD | 10,140,000.00 USD |
| `1D` | `2242.30` | 851,890,000.00 USD | 0.00 USD | 851,890,000.00 USD | 836,930.00 USD | 918,390.00 USD | 1,470,000.00 USD |
| `7D` | `2244.20` | 1,960,000,000.00 USD | 0.00 USD | 1,960,000,000.00 USD | 10,350,000.00 USD | 8,810,000.00 USD | 12,230,000.00 USD |
| `1D` | `2244.90` | 848,670,000.00 USD | 0.00 USD | 848,670,000.00 USD | 2,500,000.00 USD | 2,540,000.00 USD | 369,590.00 USD |
| `7D` | `2247.10` | 1,930,000,000.00 USD | 0.00 USD | 1,930,000,000.00 USD | 16,790,000.00 USD | 10,060,000.00 USD | 9,870,000.00 USD |
| `1D` | `2247.50` | 843,270,000.00 USD | 0.00 USD | 843,270,000.00 USD | 2,240,000.00 USD | 903,300.00 USD | 2,010,000.00 USD |
| `7D` | `2250.00` | 1,890,000,000.00 USD | 0.00 USD | 1,890,000,000.00 USD | 11,760,000.00 USD | 9,350,000.00 USD | 8,360,000.00 USD |
| `1D` | `2250.10` | 838,110,000.00 USD | 0.00 USD | 838,110,000.00 USD | 3,310,000.00 USD | 958,610.00 USD | 1,790,000.00 USD |
| `1D` | `2252.70` | 832,050,000.00 USD | 0.00 USD | 832,050,000.00 USD | 5,690,000.00 USD | 6,690,000.00 USD | 4,640,000.00 USD |
| `7D` | `2252.90` | 1,860,000,000.00 USD | 0.00 USD | 1,860,000,000.00 USD | 24,550,000.00 USD | 17,220,000.00 USD | 16,920,000.00 USD |
| `1D` | `2255.30` | 815,030,000.00 USD | 0.00 USD | 815,030,000.00 USD | 3,330,000.00 USD | 2,320,000.00 USD | 5,410,000.00 USD |
| `7D` | `2255.80` | 1,800,000,000.00 USD | 0.00 USD | 1,800,000,000.00 USD | 23,870,000.00 USD | 18,230,000.00 USD | 15,580,000.00 USD |
| `1D` | `2257.90` | 803,980,000.00 USD | 0.00 USD | 803,980,000.00 USD | 8,440,000.00 USD | 3,960,000.00 USD | 4,840,000.00 USD |
| `7D` | `2258.70` | 1,750,000,000.00 USD | 0.00 USD | 1,750,000,000.00 USD | 29,540,000.00 USD | 22,530,000.00 USD | 25,130,000.00 USD |
| `1D` | `2260.50` | 786,730,000.00 USD | 0.00 USD | 786,730,000.00 USD | 15,640,000.00 USD | 9,850,000.00 USD | 10,460,000.00 USD |
| `7D` | `2261.60` | 1,670,000,000.00 USD | 0.00 USD | 1,670,000,000.00 USD | 48,100,000.00 USD | 31,730,000.00 USD | 21,740,000.00 USD |
| `1D` | `2263.10` | 750,780,000.00 USD | 0.00 USD | 750,780,000.00 USD | 10,850,000.00 USD | 14,100,000.00 USD | 10,420,000.00 USD |
| `7D` | `2264.50` | 1,570,000,000.00 USD | 0.00 USD | 1,570,000,000.00 USD | 33,190,000.00 USD | 30,310,000.00 USD | 21,680,000.00 USD |
| `1D` | `2265.70` | 715,400,000.00 USD | 0.00 USD | 715,400,000.00 USD | 13,000,000.00 USD | 10,690,000.00 USD | 4,200,000.00 USD |
| `7D` | `2267.40` | 1,480,000,000.00 USD | 0.00 USD | 1,480,000,000.00 USD | 39,370,000.00 USD | 40,010,000.00 USD | 34,230,000.00 USD |
| `1D` | `2268.30` | 687,510,000.00 USD | 0.00 USD | 687,510,000.00 USD | 9,920,000.00 USD | 10,320,000.00 USD | 5,310,000.00 USD |
| `7D` | `2270.30` | 1,370,000,000.00 USD | 0.00 USD | 1,370,000,000.00 USD | 41,070,000.00 USD | 27,630,000.00 USD | 39,250,000.00 USD |
| `1D` | `2270.90` | 661,970,000.00 USD | 0.00 USD | 661,970,000.00 USD | 9,090,000.00 USD | 9,720,000.00 USD | 7,270,000.00 USD |
| `7D` | `2273.20` | 1,260,000,000.00 USD | 0.00 USD | 1,260,000,000.00 USD | 33,160,000.00 USD | 25,760,000.00 USD | 20,220,000.00 USD |
| `1D` | `2273.50` | 635,890,000.00 USD | 0.00 USD | 635,890,000.00 USD | 14,150,000.00 USD | 8,430,000.00 USD | 9,020,000.00 USD |
| `1D` | `2276.10` | 604,280,000.00 USD | 0.00 USD | 604,280,000.00 USD | 17,930,000.00 USD | 14,340,000.00 USD | 10,960,000.00 USD |
| `7D` | `2276.10` | 1,180,000,000.00 USD | 0.00 USD | 1,180,000,000.00 USD | 54,840,000.00 USD | 46,910,000.00 USD | 49,540,000.00 USD |
| `1D` | `2278.70` | 561,050,000.00 USD | 0.00 USD | 561,050,000.00 USD | 14,910,000.00 USD | 9,250,000.00 USD | 13,660,000.00 USD |
| `7D` | `2279.00` | 1,030,000,000.00 USD | 0.00 USD | 1,030,000,000.00 USD | 74,170,000.00 USD | 30,780,000.00 USD | 49,610,000.00 USD |
| `1D` | `2281.30` | 523,230,000.00 USD | 0.00 USD | 523,230,000.00 USD | 23,500,000.00 USD | 13,310,000.00 USD | 16,210,000.00 USD |
| `7D` | `2281.90` | 874,780,000.00 USD | 0.00 USD | 874,780,000.00 USD | 64,370,000.00 USD | 63,970,000.00 USD | 39,890,000.00 USD |
| `1D` | `2283.90` | 470,200,000.00 USD | 0.00 USD | 470,200,000.00 USD | 34,180,000.00 USD | 23,760,000.00 USD | 22,970,000.00 USD |
| `7D` | `2284.80` | 706,560,000.00 USD | 0.00 USD | 706,560,000.00 USD | 95,240,000.00 USD | 73,600,000.00 USD | 47,330,000.00 USD |
| `1D` | `2286.50` | 389,290,000.00 USD | 0.00 USD | 389,290,000.00 USD | 17,530,000.00 USD | 23,820,000.00 USD | 13,160,000.00 USD |
| `7D` | `2287.70` | 490,390,000.00 USD | 0.00 USD | 490,390,000.00 USD | 55,750,000.00 USD | 55,240,000.00 USD | 51,720,000.00 USD |
| `1D` | `2289.10` | 334,780,000.00 USD | 0.00 USD | 334,780,000.00 USD | 18,070,000.00 USD | 17,140,000.00 USD | 4,740,000.00 USD |
| `7D` | `2290.60` | 327,680,000.00 USD | 0.00 USD | 327,680,000.00 USD | 39,440,000.00 USD | 32,400,000.00 USD | 46,920,000.00 USD |
| `1D` | `2291.70` | 294,820,000.00 USD | 0.00 USD | 294,820,000.00 USD | 22,990,000.00 USD | 19,890,000.00 USD | 11,020,000.00 USD |
| `7D` | `2293.50` | 208,910,000.00 USD | 0.00 USD | 208,910,000.00 USD | 41,720,000.00 USD | 20,380,000.00 USD | 18,960,000.00 USD |
| `1D` | `2294.30` | 240,930,000.00 USD | 0.00 USD | 240,930,000.00 USD | 12,130,000.00 USD | 15,570,000.00 USD | 11,830,000.00 USD |
| `7D` | `2296.40` | 127,860,000.00 USD | 0.00 USD | 127,860,000.00 USD | 8,030,000.00 USD | 4,300,000.00 USD | 3,710,000.00 USD |
| `1D` | `2296.90` | 201,400,000.00 USD | 0.00 USD | 201,400,000.00 USD | 20,370,000.00 USD | 9,140,000.00 USD | 5,820,000.00 USD |
| `7D` | `2299.30` | 111,820,000.00 USD | 0.00 USD | 111,820,000.00 USD | 13,410,000.00 USD | 6,480,000.00 USD | 216,930.00 USD |
| `1D` | `2299.50` | 166,070,000.00 USD | 0.00 USD | 166,070,000.00 USD | 17,470,000.00 USD | 7,400,000.00 USD | 7,480,000.00 USD |
| `1D` | `2302.10` | 133,730,000.00 USD | 0.00 USD | 133,730,000.00 USD | 16,300,000.00 USD | 12,620,000.00 USD | 14,590,000.00 USD |
| `7D` | `2302.20` | 91,720,000.00 USD | 0.00 USD | 91,720,000.00 USD | 12,400,000.00 USD | 3,870,000.00 USD | 18,920,000.00 USD |
| `1D` | `2304.70` | 90,220,000.00 USD | 0.00 USD | 90,220,000.00 USD | 0.00 USD | 15,080,000.00 USD | 22,080,000.00 USD |
| `7D` | `2305.10` | 56,520,000.00 USD | 0.00 USD | 56,520,000.00 USD | 20,580,000.00 USD | 15,290,000.00 USD | 5,330,000.00 USD |
| `1D` | `2307.30` | 53,060,000.00 USD | 0.00 USD | 53,060,000.00 USD | 0.00 USD | 6,370,000.00 USD | 6,110,000.00 USD |
| `7D` | `2308.00` | 15,320,000.00 USD | 0.00 USD | 15,320,000.00 USD | 0.00 USD | 2,150,000.00 USD | 134,160.00 USD |
| `1D` | `2309.90` | 40,580,000.00 USD | 0.00 USD | 40,580,000.00 USD | 1,440,000.00 USD | 3,190,000.00 USD | 172,820.00 USD |
| `7D` | `2310.90` | 13,030,000.00 USD | 0.00 USD | 13,030,000.00 USD | 1,740,000.00 USD | 512,220.00 USD | 97,260.00 USD |
| `1D` | `2312.50` | 35,780,000.00 USD | 0.00 USD | 35,780,000.00 USD | 8,850,000.00 USD | 8,520,000.00 USD | 57,690.00 USD |
| `7D` | `2313.80` | 10,680,000.00 USD | 0.00 USD | 10,680,000.00 USD | 2,840,000.00 USD | 7,650,000.00 USD | 188,280.00 USD |
| `7D` | `2313.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2315.10` | 18,350,000.00 USD | 0.00 USD | 18,350,000.00 USD | 6,990,000.00 USD | 9,370,000.00 USD | 1,990,000.00 USD |
| `1D` | `2316.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2316.70` | 235,270.00 USD | 235,270.00 USD | 0.00 USD | 0.00 USD | 235,270.00 USD | 0.00 USD |
| `1D` | `2317.70` | 13,030,000.00 USD | 13,030,000.00 USD | 0.00 USD | 8,890,000.00 USD | 4,140,000.00 USD | 0.00 USD |
| `7D` | `2319.60` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 0.00 USD | 5,370,000.00 USD | 0.00 USD |
| `1D` | `2320.30` | 17,880,000.00 USD | 17,880,000.00 USD | 0.00 USD | 1,680,000.00 USD | 3,110,000.00 USD | 61,930.00 USD |
| `7D` | `2322.50` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 3,130,000.00 USD | 835,280.00 USD | 0.00 USD |
| `1D` | `2322.90` | 19,500,000.00 USD | 19,500,000.00 USD | 0.00 USD | 0.00 USD | 1,620,000.00 USD | 0.00 USD |
| `7D` | `2325.40` | 11,300,000.00 USD | 11,300,000.00 USD | 0.00 USD | 0.00 USD | 1,740,000.00 USD | 0.00 USD |
| `1D` | `2325.50` | 22,270,000.00 USD | 22,270,000.00 USD | 0.00 USD | 0.00 USD | 2,700,000.00 USD | 66,960.00 USD |
| `1D` | `2328.10` | 22,820,000.00 USD | 22,820,000.00 USD | 0.00 USD | 256,580.00 USD | 206,450.00 USD | 89,050.00 USD |
| `7D` | `2328.30` | 15,290,000.00 USD | 15,290,000.00 USD | 0.00 USD | 3,860,000.00 USD | 0.00 USD | 126,530.00 USD |
| `1D` | `2330.70` | 32,810,000.00 USD | 32,810,000.00 USD | 0.00 USD | 9,820,000.00 USD | 0.00 USD | 168,480.00 USD |
| `7D` | `2331.20` | 38,320,000.00 USD | 38,320,000.00 USD | 0.00 USD | 23,030,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2333.30` | 46,310,000.00 USD | 46,310,000.00 USD | 0.00 USD | 10,110,000.00 USD | 0.00 USD | 3,400,000.00 USD |
| `7D` | `2334.10` | 55,930,000.00 USD | 55,930,000.00 USD | 0.00 USD | 6,760,000.00 USD | 10,860,000.00 USD | 0.00 USD |
| `1D` | `2335.90` | 57,870,000.00 USD | 57,870,000.00 USD | 0.00 USD | 11,430,000.00 USD | 140,030.00 USD | 0.00 USD |
| `7D` | `2337.00` | 88,070,000.00 USD | 88,070,000.00 USD | 0.00 USD | 18,070,000.00 USD | 7,570,000.00 USD | 6,500,000.00 USD |
| `1D` | `2338.50` | 59,460,000.00 USD | 59,460,000.00 USD | 0.00 USD | 0.00 USD | 130,330.00 USD | 1,460,000.00 USD |
| `7D` | `2339.90` | 114,680,000.00 USD | 114,680,000.00 USD | 0.00 USD | 9,570,000.00 USD | 5,360,000.00 USD | 11,680,000.00 USD |
| `1D` | `2341.10` | 61,140,000.00 USD | 61,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,680,000.00 USD |
| `7D` | `2342.80` | 128,720,000.00 USD | 128,720,000.00 USD | 0.00 USD | 0.00 USD | 10,200,000.00 USD | 3,840,000.00 USD |
| `1D` | `2343.70` | 69,490,000.00 USD | 69,490,000.00 USD | 0.00 USD | 120,800.00 USD | 1,960,000.00 USD | 6,270,000.00 USD |
| `7D` | `2345.70` | 143,590,000.00 USD | 143,590,000.00 USD | 0.00 USD | 1,350,000.00 USD | 7,920,000.00 USD | 5,600,000.00 USD |
| `1D` | `2346.30` | 78,750,000.00 USD | 78,750,000.00 USD | 0.00 USD | 3,350,000.00 USD | 0.00 USD | 5,910,000.00 USD |
| `7D` | `2348.60` | 175,170,000.00 USD | 175,170,000.00 USD | 0.00 USD | 285,680.00 USD | 7,240,000.00 USD | 24,050,000.00 USD |
| `1D` | `2348.90` | 85,490,000.00 USD | 85,490,000.00 USD | 0.00 USD | 5,710,000.00 USD | 42,760.00 USD | 990,800.00 USD |
| `1D` | `2351.50` | 116,260,000.00 USD | 116,260,000.00 USD | 0.00 USD | 21,900,000.00 USD | 2,850,000.00 USD | 6,020,000.00 USD |
| `7D` | `2351.50` | 199,310,000.00 USD | 199,310,000.00 USD | 0.00 USD | 782,590.00 USD | 17,680,000.00 USD | 5,680,000.00 USD |
| `1D` | `2354.10` | 133,690,000.00 USD | 133,690,000.00 USD | 0.00 USD | 3,200,000.00 USD | 13,490,000.00 USD | 743,130.00 USD |
| `7D` | `2354.40` | 240,820,000.00 USD | 240,820,000.00 USD | 0.00 USD | 6,120,000.00 USD | 35,020,000.00 USD | 371,510.00 USD |
| `1D` | `2356.70` | 143,380,000.00 USD | 143,380,000.00 USD | 0.00 USD | 2,050,000.00 USD | 5,880,000.00 USD | 1,740,000.00 USD |
| `7D` | `2357.30` | 255,480,000.00 USD | 255,480,000.00 USD | 0.00 USD | 8,740,000.00 USD | 5,920,000.00 USD | 0.00 USD |
| `1D` | `2359.30` | 156,790,000.00 USD | 156,790,000.00 USD | 0.00 USD | 2,130,000.00 USD | 5,440,000.00 USD | 5,840,000.00 USD |
| `7D` | `2360.20` | 264,770,000.00 USD | 264,770,000.00 USD | 0.00 USD | 2,690,000.00 USD | 3,430,000.00 USD | 3,180,000.00 USD |
| `1D` | `2361.90` | 168,920,000.00 USD | 168,920,000.00 USD | 0.00 USD | 4,100,000.00 USD | 6,710,000.00 USD | 1,330,000.00 USD |
| `7D` | `2363.10` | 267,170,000.00 USD | 267,170,000.00 USD | 0.00 USD | 715,490.00 USD | 0.00 USD | 1,690,000.00 USD |
| `1D` | `2364.50` | 179,870,000.00 USD | 179,870,000.00 USD | 0.00 USD | 3,220,000.00 USD | 3,710,000.00 USD | 4,000,000.00 USD |
| `7D` | `2366.00` | 275,180,000.00 USD | 275,180,000.00 USD | 0.00 USD | 6,340,000.00 USD | 0.00 USD | 1,660,000.00 USD |
| `1D` | `2367.10` | 183,440,000.00 USD | 183,440,000.00 USD | 0.00 USD | 3,350,000.00 USD | 0.00 USD | 231,190.00 USD |
| `7D` | `2368.90` | 296,830,000.00 USD | 296,830,000.00 USD | 0.00 USD | 20,720,000.00 USD | 475,460.00 USD | 450,860.00 USD |
| `1D` | `2369.70` | 208,110,000.00 USD | 208,110,000.00 USD | 0.00 USD | 14,110,000.00 USD | 6,790,000.00 USD | 3,760,000.00 USD |
| `7D` | `2371.80` | 360,330,000.00 USD | 360,330,000.00 USD | 0.00 USD | 12,810,000.00 USD | 0.00 USD | 50,700,000.00 USD |
| `1D` | `2372.30` | 240,520,000.00 USD | 240,520,000.00 USD | 0.00 USD | 11,110,000.00 USD | 10,170,000.00 USD | 11,130,000.00 USD |
| `7D` | `2374.70` | 387,280,000.00 USD | 387,280,000.00 USD | 0.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD |
| `1D` | `2374.90` | 259,100,000.00 USD | 259,100,000.00 USD | 0.00 USD | 13,050,000.00 USD | 335,190.00 USD | 5,190,000.00 USD |
| `1D` | `2377.50` | 292,940,000.00 USD | 292,940,000.00 USD | 0.00 USD | 11,940,000.00 USD | 10,700,000.00 USD | 11,200,000.00 USD |
| `7D` | `2377.60` | 417,610,000.00 USD | 417,610,000.00 USD | 0.00 USD | 8,770,000.00 USD | 6,190,000.00 USD | 15,370,000.00 USD |
| `1D` | `2380.10` | 327,480,000.00 USD | 327,480,000.00 USD | 0.00 USD | 12,150,000.00 USD | 7,970,000.00 USD | 14,420,000.00 USD |
| `7D` | `2380.50` | 447,140,000.00 USD | 447,140,000.00 USD | 0.00 USD | 6,830,000.00 USD | 2,590,000.00 USD | 20,100,000.00 USD |
| `1D` | `2382.70` | 386,390,000.00 USD | 386,390,000.00 USD | 0.00 USD | 22,820,000.00 USD | 19,890,000.00 USD | 16,190,000.00 USD |
| `7D` | `2383.40` | 498,030,000.00 USD | 498,030,000.00 USD | 0.00 USD | 8,610,000.00 USD | 17,490,000.00 USD | 24,790,000.00 USD |
| `1D` | `2385.30` | 427,170,000.00 USD | 427,170,000.00 USD | 0.00 USD | 10,330,000.00 USD | 20,100,000.00 USD | 10,350,000.00 USD |
| `7D` | `2386.30` | 612,320,000.00 USD | 612,320,000.00 USD | 0.00 USD | 17,450,000.00 USD | 41,020,000.00 USD | 55,820,000.00 USD |
| `1D` | `2387.90` | 452,200,000.00 USD | 452,200,000.00 USD | 0.00 USD | 14,010,000.00 USD | 6,140,000.00 USD | 4,880,000.00 USD |
| `7D` | `2389.20` | 684,890,000.00 USD | 684,890,000.00 USD | 0.00 USD | 3,900,000.00 USD | 30,140,000.00 USD | 38,530,000.00 USD |
| `1D` | `2390.50` | 471,740,000.00 USD | 471,740,000.00 USD | 0.00 USD | 6,350,000.00 USD | 5,300,000.00 USD | 7,890,000.00 USD |
| `7D` | `2392.10` | 791,710,000.00 USD | 791,710,000.00 USD | 0.00 USD | 17,810,000.00 USD | 45,620,000.00 USD | 43,390,000.00 USD |
| `1D` | `2393.10` | 496,140,000.00 USD | 496,140,000.00 USD | 0.00 USD | 5,640,000.00 USD | 12,500,000.00 USD | 6,270,000.00 USD |
| `7D` | `2395.00` | 896,980,000.00 USD | 896,980,000.00 USD | 0.00 USD | 47,110,000.00 USD | 28,070,000.00 USD | 30,090,000.00 USD |
| `1D` | `2395.70` | 509,390,000.00 USD | 509,390,000.00 USD | 0.00 USD | 4,830,000.00 USD | 5,770,000.00 USD | 2,650,000.00 USD |
| `7D` | `2397.90` | 992,610,000.00 USD | 992,610,000.00 USD | 0.00 USD | 37,230,000.00 USD | 36,430,000.00 USD | 21,970,000.00 USD |
| `1D` | `2398.30` | 529,790,000.00 USD | 529,790,000.00 USD | 0.00 USD | 5,450,000.00 USD | 8,020,000.00 USD | 6,930,000.00 USD |
| `7D` | `2400.80` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 42,170,000.00 USD | 25,680,000.00 USD | 25,680,000.00 USD |
| `1D` | `2400.90` | 557,460,000.00 USD | 557,460,000.00 USD | 0.00 USD | 9,660,000.00 USD | 8,230,000.00 USD | 9,790,000.00 USD |
| `1D` | `2403.50` | 582,810,000.00 USD | 582,810,000.00 USD | 0.00 USD | 9,560,000.00 USD | 7,020,000.00 USD | 8,770,000.00 USD |
| `7D` | `2403.70` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 56,800,000.00 USD | 25,430,000.00 USD | 29,870,000.00 USD |
| `1D` | `2406.10` | 610,590,000.00 USD | 610,590,000.00 USD | 0.00 USD | 12,760,000.00 USD | 7,480,000.00 USD | 7,530,000.00 USD |
| `7D` | `2406.60` | 1,270,000,000.00 USD | 1,270,000,000.00 USD | 0.00 USD | 23,950,000.00 USD | 34,300,000.00 USD | 16,280,000.00 USD |
| `1D` | `2408.70` | 640,440,000.00 USD | 640,440,000.00 USD | 0.00 USD | 7,950,000.00 USD | 14,910,000.00 USD | 6,980,000.00 USD |
| `7D` | `2409.50` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 27,600,000.00 USD | 26,770,000.00 USD | 24,780,000.00 USD |
| `1D` | `2411.30` | 661,410,000.00 USD | 661,410,000.00 USD | 0.00 USD | 8,580,000.00 USD | 7,900,000.00 USD | 4,500,000.00 USD |
| `7D` | `2412.40` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 16,560,000.00 USD | 15,580,000.00 USD | 15,370,000.00 USD |
| `1D` | `2413.90` | 670,510,000.00 USD | 670,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 1,390,000.00 USD | 3,200,000.00 USD |
| `7D` | `2415.30` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 0.00 USD | 20,360,000.00 USD | 20,510,000.00 USD | 25,180,000.00 USD |
| `1D` | `2416.50` | 687,360,000.00 USD | 687,360,000.00 USD | 0.00 USD | 4,790,000.00 USD | 7,670,000.00 USD | 4,390,000.00 USD |
| `7D` | `2418.20` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 0.00 USD | 31,510,000.00 USD | 13,720,000.00 USD | 19,030,000.00 USD |
| `1D` | `2419.10` | 698,140,000.00 USD | 698,140,000.00 USD | 0.00 USD | 5,120,000.00 USD | 2,280,000.00 USD | 3,370,000.00 USD |
| `7D` | `2421.10` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 22,270,000.00 USD | 27,860,000.00 USD | 21,200,000.00 USD |
| `1D` | `2421.70` | 714,410,000.00 USD | 714,410,000.00 USD | 0.00 USD | 4,170,000.00 USD | 6,200,000.00 USD | 5,890,000.00 USD |
| `7D` | `2424.00` | 1,680,000,000.00 USD | 1,680,000,000.00 USD | 0.00 USD | 18,610,000.00 USD | 31,660,000.00 USD | 30,780,000.00 USD |
| `1D` | `2424.30` | 720,250,000.00 USD | 720,250,000.00 USD | 0.00 USD | 1,790,000.00 USD | 3,040,000.00 USD | 1,020,000.00 USD |
| `1D` | `2426.90` | 721,550,000.00 USD | 721,550,000.00 USD | 0.00 USD | 731,900.00 USD | 369,950.00 USD | 200,940.00 USD |
| `7D` | `2426.90` | 1,760,000,000.00 USD | 1,760,000,000.00 USD | 0.00 USD | 27,510,000.00 USD | 22,000,000.00 USD | 26,660,000.00 USD |
| `1D` | `2429.50` | 726,260,000.00 USD | 726,260,000.00 USD | 0.00 USD | 1,330,000.00 USD | 1,770,000.00 USD | 1,620,000.00 USD |
| `7D` | `2429.80` | 1,780,000,000.00 USD | 1,780,000,000.00 USD | 0.00 USD | 6,630,000.00 USD | 12,550,000.00 USD | 6,860,000.00 USD |
| `1D` | `2432.10` | 730,170,000.00 USD | 730,170,000.00 USD | 0.00 USD | 2,010,000.00 USD | 1,690,000.00 USD | 210,810.00 USD |
| `7D` | `2432.70` | 1,820,000,000.00 USD | 1,820,000,000.00 USD | 0.00 USD | 17,550,000.00 USD | 15,730,000.00 USD | 6,540,000.00 USD |
| `1D` | `2434.70` | 733,710,000.00 USD | 733,710,000.00 USD | 0.00 USD | 1,670,000.00 USD | 468,310.00 USD | 1,400,000.00 USD |
| `7D` | `2435.60` | 1,870,000,000.00 USD | 1,870,000,000.00 USD | 0.00 USD | 20,760,000.00 USD | 13,900,000.00 USD | 12,830,000.00 USD |
| `1D` | `2437.30` | 735,650,000.00 USD | 735,650,000.00 USD | 0.00 USD | 1,200,000.00 USD | 531,390.00 USD | 205,600.00 USD |
| `7D` | `2438.50` | 1,930,000,000.00 USD | 1,930,000,000.00 USD | 0.00 USD | 18,000,000.00 USD | 21,640,000.00 USD | 14,860,000.00 USD |
| `1D` | `2439.90` | 738,900,000.00 USD | 738,900,000.00 USD | 0.00 USD | 1,540,000.00 USD | 1,230,000.00 USD | 479,040.00 USD |
| `7D` | `2441.40` | 1,960,000,000.00 USD | 1,960,000,000.00 USD | 0.00 USD | 14,700,000.00 USD | 6,350,000.00 USD | 11,020,000.00 USD |
| `1D` | `2442.50` | 742,370,000.00 USD | 742,370,000.00 USD | 0.00 USD | 1,050,000.00 USD | 1,380,000.00 USD | 1,040,000.00 USD |
| `7D` | `2444.30` | 2,000,000,000.00 USD | 2,000,000,000.00 USD | 0.00 USD | 8,760,000.00 USD | 15,160,000.00 USD | 13,140,000.00 USD |
| `1D` | `2445.10` | 744,570,000.00 USD | 744,570,000.00 USD | 0.00 USD | 50,900.00 USD | 939,450.00 USD | 1,210,000.00 USD |
| `7D` | `2447.20` | 2,030,000,000.00 USD | 2,030,000,000.00 USD | 0.00 USD | 10,560,000.00 USD | 7,370,000.00 USD | 16,450,000.00 USD |
| `1D` | `2447.70` | 749,820,000.00 USD | 749,820,000.00 USD | 0.00 USD | 1,890,000.00 USD | 659,940.00 USD | 2,690,000.00 USD |
| `7D` | `2450.10` | 2,070,000,000.00 USD | 2,070,000,000.00 USD | 0.00 USD | 13,890,000.00 USD | 11,970,000.00 USD | 13,110,000.00 USD |
| `1D` | `2450.30` | 757,430,000.00 USD | 757,430,000.00 USD | 0.00 USD | 2,540,000.00 USD | 2,140,000.00 USD | 2,930,000.00 USD |
| `1D` | `2452.90` | 766,470,000.00 USD | 766,470,000.00 USD | 0.00 USD | 3,360,000.00 USD | 2,300,000.00 USD | 3,380,000.00 USD |
| `7D` | `2453.00` | 2,090,000,000.00 USD | 2,090,000,000.00 USD | 0.00 USD | 8,570,000.00 USD | 7,390,000.00 USD | 6,550,000.00 USD |
| `1D` | `2455.50` | 775,890,000.00 USD | 775,890,000.00 USD | 0.00 USD | 2,900,000.00 USD | 4,240,000.00 USD | 2,280,000.00 USD |
| `7D` | `2455.90` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 0.00 USD | 5,870,000.00 USD | 8,500,000.00 USD | 6,880,000.00 USD |
| `1D` | `2458.10` | 781,160,000.00 USD | 781,160,000.00 USD | 0.00 USD | 2,250,000.00 USD | 1,790,000.00 USD | 1,230,000.00 USD |
| `7D` | `2458.80` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 0.00 USD | 10,310,000.00 USD | 12,000,000.00 USD | 10,000,000.00 USD |
| `1D` | `2460.70` | 784,720,000.00 USD | 784,720,000.00 USD | 0.00 USD | 1,260,000.00 USD | 1,130,000.00 USD | 1,160,000.00 USD |
| `7D` | `2461.70` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 0.00 USD | 10,100,000.00 USD | 11,320,000.00 USD | 10,790,000.00 USD |
| `1D` | `2463.30` | 787,870,000.00 USD | 787,870,000.00 USD | 0.00 USD | 0.00 USD | 2,050,000.00 USD | 1,100,000.00 USD |
| `7D` | `2464.60` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 0.00 USD | 7,830,000.00 USD | 3,900,000.00 USD | 3,560,000.00 USD |
| `1D` | `2465.90` | 789,010,000.00 USD | 789,010,000.00 USD | 0.00 USD | 352,200.00 USD | 780,010.00 USD | 5,650.00 USD |
| `7D` | `2467.50` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 0.00 USD | 4,540,000.00 USD | 3,120,000.00 USD | 586,780.00 USD |
| `1D` | `2468.50` | 789,960,000.00 USD | 789,960,000.00 USD | 0.00 USD | 0.00 USD | 957,860.00 USD | 0.00 USD |
| `7D` | `2470.40` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 0.00 USD | 2,330,000.00 USD | 2,290,000.00 USD | 496,280.00 USD |
| `1D` | `2471.10` | 790,610,000.00 USD | 790,610,000.00 USD | 0.00 USD | 0.00 USD | 257,700.00 USD | 391,890.00 USD |
| `7D` | `2473.30` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 0.00 USD | 5,250,000.00 USD | 2,920,000.00 USD | 2,270,000.00 USD |
| `7D` | `2476.20` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 0.00 USD | 2,680,000.00 USD | 1,500,000.00 USD | 872,130.00 USD |
| `7D` | `2479.10` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 0.00 USD | 2,170,000.00 USD | 4,160,000.00 USD | 505,810.00 USD |
| `7D` | `2482.00` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 0.00 USD | 1,750,000.00 USD | 1,520,000.00 USD | 0.00 USD |
| `7D` | `2484.90` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 77,610.00 USD |
| `7D` | `2487.80` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 0.00 USD | 826,600.00 USD | 828,810.00 USD | 0.00 USD |
| `7D` | `2490.70` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 0.00 USD | 808,320.00 USD | 1,780,000.00 USD | 279,750.00 USD |
| `7D` | `2493.60` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 0.00 USD | 1,610,000.00 USD | 1,690,000.00 USD | 3,570,000.00 USD |
| `7D` | `2496.50` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 0.00 USD | 1,670,000.00 USD | 4,820,000.00 USD | 6,620,000.00 USD |
| `7D` | `2499.40` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 0.00 USD | 1,900,000.00 USD | 2,950,000.00 USD | 3,080,000.00 USD |
| `7D` | `2502.30` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 0.00 USD | 647,370.00 USD | 1,090,000.00 USD | 125,600.00 USD |
| `7D` | `2505.20` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 0.00 USD | 1,400,000.00 USD | 2,310,000.00 USD | 103,890.00 USD |
| `7D` | `2508.10` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 0.00 USD | 2,940,000.00 USD | 1,640,000.00 USD | 1,990,000.00 USD |
| `7D` | `2511.00` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 0.00 USD | 2,560,000.00 USD | 3,230,000.00 USD | 2,640,000.00 USD |
| `7D` | `2513.90` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 776,920.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2516.80` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 97,050.00 USD | 189,640.00 USD | 0.00 USD |
| `7D` | `2519.70` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD |
| `1D` | `2520.50` | 790,790,000.00 USD | 790,790,000.00 USD | 0.00 USD | 80,610.00 USD | 61,830.00 USD | 32,260.00 USD |
| `7D` | `2522.60` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 1,050,000.00 USD | 0.00 USD | 945,860.00 USD |
| `1D` | `2523.10` | 790,850,000.00 USD | 790,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 57,880.00 USD |
| `7D` | `2525.50` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 307,040.00 USD | 241,310.00 USD | 200,040.00 USD |
| `1D` | `2525.70` | 791,380,000.00 USD | 791,380,000.00 USD | 0.00 USD | 421,540.00 USD | 57,450.00 USD | 53,680.00 USD |
| `1D` | `2528.30` | 792,050,000.00 USD | 792,050,000.00 USD | 0.00 USD | 0.00 USD | 645,910.00 USD | 26,970.00 USD |
| `7D` | `2528.40` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 0.00 USD | 1,580,000.00 USD | 1,670,000.00 USD | 727,590.00 USD |
| `1D` | `2530.90` | 793,490,000.00 USD | 793,490,000.00 USD | 0.00 USD | 995,550.00 USD | 0.00 USD | 437,490.00 USD |
| `7D` | `2531.30` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 0.00 USD | 2,720,000.00 USD | 1,490,000.00 USD | 1,230,000.00 USD |
| `1D` | `2533.50` | 793,960,000.00 USD | 793,960,000.00 USD | 0.00 USD | 394,310.00 USD | 62,630.00 USD | 16,730.00 USD |
| `7D` | `2534.20` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 0.00 USD | 2,550,000.00 USD | 1,720,000.00 USD | 2,030,000.00 USD |
| `1D` | `2536.10` | 796,850,000.00 USD | 796,850,000.00 USD | 0.00 USD | 1,160,000.00 USD | 656,520.00 USD | 1,080,000.00 USD |
| `7D` | `2537.10` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 0.00 USD | 3,380,000.00 USD | 3,160,000.00 USD | 2,830,000.00 USD |
| `1D` | `2538.70` | 800,840,000.00 USD | 800,840,000.00 USD | 0.00 USD | 1,870,000.00 USD | 524,750.00 USD | 1,590,000.00 USD |
| `7D` | `2540.00` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 0.00 USD | 3,930,000.00 USD | 3,190,000.00 USD | 831,220.00 USD |
| `1D` | `2541.30` | 802,820,000.00 USD | 802,820,000.00 USD | 0.00 USD | 889,420.00 USD | 832,630.00 USD | 260,390.00 USD |
| `7D` | `2542.90` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 0.00 USD | 2,510,000.00 USD | 2,470,000.00 USD | 2,460,000.00 USD |
| `1D` | `2543.90` | 805,020,000.00 USD | 805,020,000.00 USD | 0.00 USD | 959,500.00 USD | 1,230,000.00 USD | 14,440.00 USD |
| `7D` | `2545.80` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 0.00 USD | 1,770,000.00 USD | 1,140,000.00 USD | 1,830,000.00 USD |
| `1D` | `2546.50` | 808,670,000.00 USD | 808,670,000.00 USD | 0.00 USD | 1,630,000.00 USD | 1,260,000.00 USD | 751,820.00 USD |
| `7D` | `2548.70` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 0.00 USD | 3,840,000.00 USD | 1,820,000.00 USD | 3,120,000.00 USD |
| `1D` | `2549.10` | 810,380,000.00 USD | 810,380,000.00 USD | 0.00 USD | 441,860.00 USD | 793,640.00 USD | 479,930.00 USD |
| `7D` | `2551.60` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 0.00 USD | 2,250,000.00 USD | 1,800,000.00 USD | 907,940.00 USD |
| `1D` | `2551.70` | 813,020,000.00 USD | 813,020,000.00 USD | 0.00 USD | 1,350,000.00 USD | 907,450.00 USD | 382,230.00 USD |
| `1D` | `2554.30` | 814,580,000.00 USD | 814,580,000.00 USD | 0.00 USD | 1,100,000.00 USD | 215,480.00 USD | 236,190.00 USD |
| `7D` | `2554.50` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 3,880,000.00 USD | 948,120.00 USD | 3,930,000.00 USD |
| `1D` | `2556.90` | 816,530,000.00 USD | 816,530,000.00 USD | 0.00 USD | 705,250.00 USD | 506,330.00 USD | 740,260.00 USD |
| `7D` | `2557.40` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 0.00 USD | 2,780,000.00 USD | 737,060.00 USD | 5,410,000.00 USD |
| `1D` | `2559.50` | 820,370,000.00 USD | 820,370,000.00 USD | 0.00 USD | 1,830,000.00 USD | 1,040,000.00 USD | 978,210.00 USD |
| `7D` | `2560.30` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 0.00 USD | 3,540,000.00 USD | 1,450,000.00 USD | 589,340.00 USD |
| `1D` | `2562.10` | 822,810,000.00 USD | 822,810,000.00 USD | 0.00 USD | 451,210.00 USD | 797,210.00 USD | 1,190,000.00 USD |
| `7D` | `2563.20` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 0.00 USD | 1,400,000.00 USD | 2,900,000.00 USD | 1,290,000.00 USD |
| `1D` | `2564.70` | 824,160,000.00 USD | 824,160,000.00 USD | 0.00 USD | 425,980.00 USD | 669,810.00 USD | 248,570.00 USD |
| `7D` | `2566.10` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 0.00 USD | 1,860,000.00 USD | 1,430,000.00 USD | 2,070,000.00 USD |
| `1D` | `2567.30` | 824,480,000.00 USD | 824,480,000.00 USD | 0.00 USD | 121,690.00 USD | 31,040.00 USD | 175,760.00 USD |
| `7D` | `2569.00` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 0.00 USD | 56,010.00 USD | 739,480.00 USD | 2,000,000.00 USD |
| `1D` | `2569.90` | 825,610,000.00 USD | 825,610,000.00 USD | 0.00 USD | 530,980.00 USD | 289,160.00 USD | 302,840.00 USD |
| `7D` | `2571.90` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 0.00 USD | 1,390,000.00 USD | 183,530.00 USD | 2,210,000.00 USD |
| `1D` | `2572.50` | 826,880,000.00 USD | 826,880,000.00 USD | 0.00 USD | 588,810.00 USD | 671,930.00 USD | 16,280.00 USD |
| `7D` | `2574.80` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 0.00 USD | 1,450,000.00 USD | 834,660.00 USD | 1,050,000.00 USD |
| `1D` | `2575.10` | 827,930,000.00 USD | 827,930,000.00 USD | 0.00 USD | 546,100.00 USD | 0.00 USD | 502,840.00 USD |
| `1D` | `2577.70` | 828,080,000.00 USD | 828,080,000.00 USD | 0.00 USD | 118,210.00 USD | 21,400.00 USD | 6,190.00 USD |
| `7D` | `2577.70` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 0.00 USD | 2,090,000.00 USD | 1,570,000.00 USD | 1,770,000.00 USD |
| `1D` | `2580.30` | 828,680,000.00 USD | 828,680,000.00 USD | 0.00 USD | 414,360.00 USD | 0.00 USD | 188,300.00 USD |
| `7D` | `2580.60` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 0.00 USD | 2,990,000.00 USD | 1,140,000.00 USD | 1,000,000.00 USD |
| `7D` | `2583.50` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 0.00 USD | 1,080,000.00 USD | 1,260,000.00 USD | 2,720,000.00 USD |
| `7D` | `2586.40` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 0.00 USD | 1,430,000.00 USD | 2,010,000.00 USD | 2,570,000.00 USD |
| `7D` | `2589.30` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 0.00 USD | 2,060,000.00 USD | 631,590.00 USD | 2,150,000.00 USD |
| `7D` | `2592.20` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 0.00 USD | 3,590,000.00 USD | 1,280,000.00 USD | 1,550,000.00 USD |
| `7D` | `2595.10` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 0.00 USD | 452,020.00 USD | 569,790.00 USD | 752,870.00 USD |
| `7D` | `2598.00` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 0.00 USD | 2,280,000.00 USD | 1,630,000.00 USD | 2,420,000.00 USD |
| `7D` | `2600.90` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 0.00 USD | 931,390.00 USD | 1,960,000.00 USD | 1,610,000.00 USD |
| `7D` | `2603.80` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,580,000.00 USD | 1,690,000.00 USD |
| `7D` | `2606.70` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 0.00 USD | 1,480,000.00 USD | 463,200.00 USD | 312,730.00 USD |
| `7D` | `2609.60` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 0.00 USD | 1,140,000.00 USD | 510,700.00 USD | 10,700.00 USD |
| `7D` | `2612.50` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 0.00 USD | 962,930.00 USD | 622,830.00 USD | 43,560.00 USD |
| `7D` | `2615.40` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 0.00 USD | 815,100.00 USD | 967,270.00 USD | 635,670.00 USD |
| `7D` | `2618.30` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 0.00 USD | 1,550,000.00 USD | 209,240.00 USD | 434,750.00 USD |
| `7D` | `2621.20` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 0.00 USD | 547,980.00 USD | 1,530,000.00 USD | 0.00 USD |
| `7D` | `2624.10` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 0.00 USD | 130,830.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `29.29B` | Total OI Tokens: `12,709,668.8 ETH`
  * 1h OI Change: `-1.41%` | 4h OI Change: `-4.28%` | 24h OI Change: `-3.04%`
  * Exchange Breakdown: Binance=`8.71B` | Bybit=`2.09B` | OKX=`1.74B` | Hyperliquid=`2.49B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `935.39K` | Last 24h: `2.27M` | Last 3d: `7.66M` | Last 7d: `13.85M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0083%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0052%` | **USDT KuCoin** | `0.0057%` |
| **USDT MEXC** | `0.0083%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0076%` | **USDT Bitget** | `0.0063%` |
| **CoinM Binance** | `0.0093%` | **CoinM OKX** | `0.0097%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `37.13%` | `62.87%` | `0.59` | 1,300,000,000.00 USD |
| `15M` | `Binance` | `33.93%` | `66.07%` | `0.51` | 444,250,000.00 USD |
| `15M` | `OKX` | `35.38%` | `64.62%` | `0.55` | 260,770,000.00 USD |
| `15M` | `Bybit` | `31.01%` | `68.99%` | `0.45` | 97,390,000.00 USD |
| `15M` | `KuCoin` | `45.17%` | `54.83%` | `0.82` | 2,920,000.00 USD |
| `15M` | `Gate` | `45.17%` | `54.83%` | `0.82` | 169,930,000.00 USD |
| `15M` | `Bitget` | `41.68%` | `58.32%` | `0.71` | 69,400,000.00 USD |
| `15M` | `BingX` | `45.11%` | `54.89%` | `0.82` | 25,010,000.00 USD |
| `15M` | `MEXC` | `48.29%` | `51.71%` | `0.93` | 49,920,000.00 USD |
| `15M` | `Bitunix` | `41.55%` | `58.45%` | `0.71` | 45,150,000.00 USD |
| `15M` | `Hyperliquid` | `14.69%` | `85.31%` | `0.17` | 25,880,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `46.06%` | `53.94%` | `0.85` | 4,420,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `63.35%` | `36.65%` | `1.73` | 24,740,000.00 USD |
| `15M` | `HTX` | `19.1%` | `80.9%` | `0.24` | 25,320,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `42.8%` | `57.2%` | `0.75` | 7,720,000.00 USD |
| `15M` | `Bitfinex` | `37.15%` | `62.85%` | `0.59` | 812,480.00 USD |
| `15M` | `Kraken` | `44.33%` | `55.67%` | `0.80` | 2,250,000.00 USD |
| `15M` | `Aster` | `36.67%` | `63.33%` | `0.58` | 12,380,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `40.93%` | `59.07%` | `0.69` | 27,000,000.00 USD |
| `15M` | `Whale Positions` | `33.93%` | `66.07%` | `0.51` | 444,250,000.00 USD |
| `15M` | `Global Accounts` | `37.13%` | `62.87%` | `0.59` | 1,300,000,000.00 USD |
| `1H` | `ETH` | `44.40%` | `55.60%` | `0.80` | 1,630,000,000.00 USD |
| `1H` | `Binance` | `39.65%` | `60.35%` | `0.66` | 526,840,000.00 USD |
| `1H` | `OKX` | `43.91%` | `56.09%` | `0.78` | 315,770,000.00 USD |
| `1H` | `Bybit` | `41.04%` | `58.96%` | `0.70` | 116,080,000.00 USD |
| `1H` | `KuCoin` | `40.38%` | `59.62%` | `0.68` | 2,890,000.00 USD |
| `1H` | `Gate` | `48.56%` | `51.44%` | `0.94` | 208,920,000.00 USD |
| `1H` | `Bitget` | `46.03%` | `53.97%` | `0.85` | 79,080,000.00 USD |
| `1H` | `BingX` | `40.69%` | `59.31%` | `0.69` | 31,490,000.00 USD |
| `1H` | `MEXC` | `52.74%` | `47.26%` | `1.12` | 69,410,000.00 USD |
| `1H` | `Bitunix` | `46.63%` | `53.37%` | `0.87` | 56,510,000.00 USD |
| `1H` | `Hyperliquid` | `26.51%` | `73.49%` | `0.36` | 27,100,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `37.05%` | `62.95%` | `0.59` | 8,580,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `76.89%` | `23.11%` | `3.33` | 71,450,000.00 USD |
| `1H` | `HTX` | `33.75%` | `66.25%` | `0.51` | 31,230,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `53.28%` | `46.72%` | `1.14` | 16,910,000.00 USD |
| `1H` | `Bitfinex` | `39.7%` | `60.3%` | `0.66` | 801,310.00 USD |
| `1H` | `Kraken` | `41.23%` | `58.77%` | `0.70` | 2,550,000.00 USD |
| `1H` | `Aster` | `36.74%` | `63.26%` | `0.58` | 15,510,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `44.54%` | `55.46%` | `0.80` | 45,690,000.00 USD |
| `1H` | `Whale Positions` | `39.65%` | `60.35%` | `0.66` | 526,840,000.00 USD |
| `1H` | `Global Accounts` | `44.40%` | `55.60%` | `0.80` | 1,630,000,000.00 USD |
| `4H` | `ETH` | `46.50%` | `53.50%` | `0.87` | 11,220,000,000.00 USD |
| `4H` | `Binance` | `43.56%` | `56.44%` | `0.77` | 3,470,000,000.00 USD |
| `4H` | `OKX` | `45.84%` | `54.16%` | `0.85` | 1,530,000,000.00 USD |
| `4H` | `Bybit` | `44.08%` | `55.92%` | `0.79` | 1,070,000,000.00 USD |
| `4H` | `KuCoin` | `31%` | `69%` | `0.45` | 43,030,000.00 USD |
| `4H` | `Gate` | `50.84%` | `49.16%` | `1.03` | 1,310,000,000.00 USD |
| `4H` | `Bitget` | `46.17%` | `53.83%` | `0.86` | 586,870,000.00 USD |
| `4H` | `BingX` | `51.58%` | `48.42%` | `1.07` | 214,610,000.00 USD |
| `4H` | `MEXC` | `49.46%` | `50.54%` | `0.98` | 653,350,000.00 USD |
| `4H` | `Bitunix` | `50.22%` | `49.78%` | `1.01` | 592,590,000.00 USD |
| `4H` | `Hyperliquid` | `45.2%` | `54.8%` | `0.82` | 574,840,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `55.58%` | `44.42%` | `1.25` | 80,700,000.00 USD |
| `4H` | `Crypto.com` | `49.59%` | `50.41%` | `0.98` | 81,960,000.00 USD |
| `4H` | `WhiteBIT` | `55.61%` | `44.39%` | `1.25` | 213,810,000.00 USD |
| `4H` | `HTX` | `46.48%` | `53.52%` | `0.87` | 48,280,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `55.69%` | `44.31%` | `1.26` | 291,980,000.00 USD |
| `4H` | `Bitfinex` | `34.75%` | `65.25%` | `0.53` | 8,000,000.00 USD |
| `4H` | `Kraken` | `41.22%` | `58.78%` | `0.70` | 97,570,000.00 USD |
| `4H` | `Aster` | `40.74%` | `59.26%` | `0.69` | 141,650,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.1%` | `51.9%` | `0.93` | 212,870,000.00 USD |
| `4H` | `Whale Positions` | `43.56%` | `56.44%` | `0.77` | 3,470,000,000.00 USD |
| `4H` | `Global Accounts` | `46.50%` | `53.50%` | `0.87` | 11,220,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `2335.75` | `2335.37` | `2335.75` | `2340.75` | `2330.75` | 125,556,310.13 USD | 63,692,130.92 USD | 61,864,179.21 USD | 1,827,951.70 USD | `+1.46%` | `1B / 1S` |
| `0:00 UTC` | `2337.75` | `2338.67` | `2337.75` | `2341.75` | `2335.75` | 48,324,873.75 USD | 25,087,349.31 USD | 23,237,524.44 USD | 1,849,824.87 USD | `+3.83%` | `0B / 0S` |
| `5:00 UTC` | `2340.25` | `2338.33` | `2340.25` | `2342.25` | `2333.75` | 43,794,873.23 USD | 24,013,000.37 USD | 19,781,872.86 USD | 4,231,127.51 USD | `+9.66%` | `0B / 2S` |
| `0:00 UTC` | `2327.25` | `2327.16` | `2327.25` | `2335.25` | `2323.25` | 195,411,305.09 USD | 64,523,153.35 USD | 130,888,151.74 USD | -66,364,998.40 USD | `-33.96%` | `0B / 9S` |
| `5:00 UTC` | `2331.25` | `2330.55` | `2331.25` | `2334.25` | `2325.75` | 53,213,391.28 USD | 35,445,824.71 USD | 17,767,566.57 USD | 17,678,258.14 USD | `+33.22%` | `4B / 0S` |
| `0:00 UTC` | `2327.75` | `2328.10` | `2327.75` | `2331.25` | `2326.25` | 28,953,047.89 USD | 13,068,031.79 USD | 15,885,016.10 USD | -2,816,984.30 USD | `-9.73%` | `0B / 1S` |
| `5:00 UTC` | `2326.75` | `2328.61` | `2326.75` | `2331.75` | `2325.75` | 28,646,242.16 USD | 14,157,941.65 USD | 14,488,300.51 USD | -330,358.86 USD | `-1.15%` | `0B / 1S` |
| `0:00 UTC` | `2334.75` | `2334.23` | `2334.75` | `2336.25` | `2330.25` | 36,369,004.25 USD | 19,887,478.26 USD | 16,481,525.99 USD | 3,405,952.27 USD | `+9.36%` | `1B / 1S` |
| `5:00 UTC` | `2335.75` | `2336.07` | `2335.75` | `2338.75` | `2332.75` | 54,317,401.94 USD | 19,276,795.34 USD | 35,040,606.60 USD | -15,763,811.25 USD | `-29.02%` | `0B / 1S` |
| `0:00 UTC` | `2309.25` | `2313.85` | `2309.25` | `2335.75` | `2302.25` | 464,349,545.90 USD | 184,832,164.69 USD | 279,517,381.21 USD | -94,685,216.52 USD | `-20.39%` | `0B / 21S` |

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
  * `2026-10-30 01:36:17 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:17 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:40:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:41:17 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:17 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:17 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:17 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
