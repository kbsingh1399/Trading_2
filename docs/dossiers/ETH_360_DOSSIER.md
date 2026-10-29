# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 00:23:15 IST` (`2026-10-29 18:53:15 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2325.40` | **Live Ask Quote**: `2328.50` | **Mid Price**: `2326.95`
- **Spread Points**: `310.00` | **Spread BPS**: `13.32 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2326.95` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `5.82` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2343.24` | Lower -3.00σ Band: `2310.66`
  * Upper +2.51σ Band: `2339.75` | Lower -2.51σ Band: `2314.15`
  * Upper +2.01σ Band: `2336.72` | Lower -2.01σ Band: `2317.18`
  * Upper +2.00σ Band: `2336.26` | Lower -2.00σ Band: `2317.64`
  * Upper +1.28σ Band: `2333.47` | Lower -1.28σ Band: `2320.43`
  * Upper +1.00σ Band: `2331.60` | Lower -1.00σ Band: `2322.30`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2326.95` | EMA-20=`2326.95` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2326.95` (Slope: `+0.0000`) | EMA-100=`2326.95`
  * Institutional Anchors: EMA-144=`2326.95` | EMA-200=`2326.95` (Slope: `+0.0000`) | EMA-233=`2326.95`
- **Range Boundaries**: 24H High=`2350.22` | 24H Low=`2303.68` | Weekly High=`2373.49` | Weekly Low=`2280.41`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2338.45` (Distance: `-0.47%`)
  * Point of Control (POC) = `2318.94` (Distance: `+0.37%`)
  * Value Area Low (VAL) = `2297.12` (Distance: `+1.32%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `2317.64` - `2336.26`
  * Optimal Trade Entry (OTE 0.705): `2331.60`
  * Structural Invalidation Anchor (0.786): `2345.57`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2337.64` | `2338.28` | `2333.60` | `2334.21` | `6,677` | 15,593,988.57 USD | -1,759,304.77 USD | `-11.28%` | -308,150,985.98 USD | `+0.08` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `2334.21` | `2335.00` | `2324.14` | `2327.97` | `53,745` | 125,095,417.74 USD | -52,709,065.50 USD | `-42.14%` | -360,860,051.48 USD | `-3.83` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `2327.97` | `2328.09` | `2326.68` | `2327.73` | `1,859` | 4,326,691.06 USD | 69,214.46 USD | `+1.60%` | -360,790,837.02 USD | `+0.35` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `2340.61` | `2341.50` | `2335.68` | `2339.94` | `20,663` | 48,324,873.75 USD | 1,849,824.87 USD | `+3.83%` | -307,706,337.98 USD | `+0.10` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `2339.94` | `2342.29` | `2333.60` | `2334.21` | `18,730` | 43,794,873.23 USD | 4,231,127.51 USD | `+9.66%` | -303,475,210.46 USD | `+0.22` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `2334.21` | `2335.00` | `2324.14` | `2327.32` | `55,858` | 130,011,805.47 USD | -53,228,816.80 USD | `-40.94%` | -356,704,027.26 USD | `-1.56` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `2368.02` | `2378.69` | `2350.25` | `2352.18` | `255,135` | 602,581,670.57 USD | -105,228,527.95 USD | `-17.46%` | -260,746,003.15 USD | `-2.06` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `2352.18` | `2353.79` | `2330.81` | `2340.62` | `199,552` | 467,616,004.62 USD | -38,816,598.96 USD | `-8.30%` | -299,562,602.11 USD | `-0.52` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2340.61` | `2342.29` | `2324.14` | `2327.24` | `95,274` | 222,186,299.10 USD | -47,165,370.40 USD | `-21.23%` | -346,727,972.51 USD | `-0.65` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `2309.10` | `2330.05` | `2308.88` | `2324.26` | `409,016` | 949,400,649.22 USD | -49,162,247.72 USD | `-5.18%` | -277,081,181.03 USD | `+0.30` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -173,041,008.80 USD | `+1.51` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2324.14` | `2327.24` | `549,962` | 1,292,383,974.29 USD | -191,210,497.32 USD | `-14.80%` | -364,251,506.12 USD | `-1.28` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2358.56` | `2360.38` | `2292.20` | `2308.04` | `812,683` | 1,883,052,517.85 USD | -183,572,583.45 USD | `-9.75%` | -193,002,187.18 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2308.03` | `2334.83` | `2303.75` | `2309.10` | `525,175` | 1,216,920,375.04 USD | -34,916,746.14 USD | `-2.87%` | -227,918,933.31 USD | `+0.53` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2309.10` | `2330.05` | `2308.88` | `2324.26` | `409,016` | 949,400,649.22 USD | -49,162,247.72 USD | `-5.18%` | -277,081,181.03 USD | `+0.30` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -173,041,008.80 USD | `+1.51` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2328.57` | `578,436` | 1,358,624,132.17 USD | -203,880,860.12 USD | `-15.01%` | -376,921,868.91 USD | `-1.34` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`2326.95`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2326.80` | `120.6049` | 280,623.48 USD | 10,424,626.16 USD | `13 orders` | `-0.08%` | `-` |
| `BID` | `2326.90` | `205.9294` | 479,177.12 USD | 10,144,002.68 USD | `26 orders` | `-0.08%` | `-` |
| `BID` | `2327.00` | `200.7208` | 467,077.30 USD | 9,664,825.56 USD | `20 orders` | `-0.08%` | `-` |
| `BID` | `2327.10` | `284.2886` | 661,568.00 USD | 9,197,748.26 USD | `16 orders` | `-0.07%` | `-` |
| `BID` | `2327.20` | `373.2661` | 868,664.87 USD | 8,536,180.26 USD | `19 orders` | `-0.07%` | `-` |
| `BID` | `2327.30` | `238.2227` | 554,415.69 USD | 7,667,515.39 USD | `28 orders` | `-0.06%` | `-` |
| `BID` | `2327.40` | `286.7909` | 667,477.14 USD | 7,113,099.70 USD | `14 orders` | `-0.06%` | `-` |
| `BID` | `2327.50` | `268.1214` | 624,052.56 USD | 6,445,622.56 USD | `13 orders` | `-0.05%` | `-` |
| `BID` | `2327.60` | `284.3223` | 661,788.59 USD | 5,821,570.00 USD | `13 orders` | `-0.05%` | `-` |
| `BID` | `2327.70` | `146.2052` | 340,321.84 USD | 5,159,781.42 USD | `13 orders` | `-0.05%` | `-` |
| `BID` | `2327.80` | `470.0665` | 1,094,220.80 USD | 4,819,459.57 USD | `26 orders` | `-0.04%` | `-` |
| `BID` | `2327.90` | `140.0542` | 326,032.17 USD | 3,725,238.77 USD | `19 orders` | `-0.04%` | `-` |
| `BID` | `2328.00` | `315.9922` | 735,629.84 USD | 3,399,206.60 USD | `17 orders` | `-0.03%` | `-` |
| `BID` | `2328.10` | `202.2853` | 470,940.41 USD | 2,663,576.76 USD | `16 orders` | `-0.03%` | `-` |
| `BID` | `2328.20` | `243.7839` | 567,577.68 USD | 2,192,636.35 USD | `16 orders` | `-0.02%` | `-` |
| `BID` | `2328.30` | `138.2483` | 321,883.52 USD | 1,625,058.68 USD | `15 orders` | `-0.02%` | `-` |
| `BID` | `2328.40` | `81.4376` | 189,619.31 USD | 1,303,175.16 USD | `13 orders` | `-0.02%` | `-` |
| `BID` | `2328.50` | `332.5073` | 774,243.25 USD | 1,113,555.85 USD | `48 orders` | `-0.01%` | `-` |
| `BID` | `2328.60` | `127.5316` | 296,970.08 USD | 339,312.60 USD | `45 orders` | `-0.01%` | `-` |
| `BID` | `2328.70` | `18.1829` | 42,342.52 USD | 42,342.52 USD | `3 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2328.75` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,328.75` | `0.00%` | `-` |
| `ASK` | `2328.80` | `2.8126` | 6,549.98 USD | 6,549.98 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `2328.90` | `34.8673` | 81,202.45 USD | 87,752.44 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `2329.00` | `72.7634` | 169,465.96 USD | 257,218.40 USD | `7 orders` | `+0.01%` | `-` |
| `ASK` | `2329.10` | `318.9683` | 742,909.07 USD | 1,000,127.46 USD | `21 orders` | `+0.02%` | `-` |
| `ASK` | `2329.20` | `196.6410` | 458,016.22 USD | 1,458,143.68 USD | `13 orders` | `+0.02%` | `-` |
| `ASK` | `2329.30` | `326.5487` | 760,629.89 USD | 2,218,773.57 USD | `18 orders` | `+0.02%` | `-` |
| `ASK` | `2329.40` | `306.6921` | 714,408.58 USD | 2,933,182.15 USD | `20 orders` | `+0.03%` | `-` |
| `ASK` | `2329.50` | `343.1759` | 799,428.26 USD | 3,732,610.40 USD | `25 orders` | `+0.03%` | `-` |
| `ASK` | `2329.60` | `178.8002` | 416,532.95 USD | 4,149,143.35 USD | `11 orders` | `+0.04%` | `-` |
| `ASK` | `2329.70` | `195.7627` | 456,068.36 USD | 4,605,211.71 USD | `15 orders` | `+0.04%` | `-` |
| `ASK` | `2329.80` | `298.3931` | 695,196.24 USD | 5,300,407.96 USD | `16 orders` | `+0.05%` | `-` |
| `ASK` | `2329.90` | `362.8123` | 845,316.38 USD | 6,145,724.34 USD | `22 orders` | `+0.05%` | `-` |
| `ASK` | `2330.00` | `208.1196` | 484,918.67 USD | 6,630,643.00 USD | `22 orders` | `+0.05%` | `-` |
| `ASK` | `2330.10` | `189.9894` | 442,694.30 USD | 7,073,337.30 USD | `28 orders` | `+0.06%` | `-` |
| `ASK` | `2330.20` | `162.7687` | 379,283.62 USD | 7,452,620.93 USD | `15 orders` | `+0.06%` | `-` |
| `ASK` | `2330.30` | `257.8259` | 600,811.69 USD | 8,053,432.62 USD | `13 orders` | `+0.07%` | `-` |
| `ASK` | `2330.40` | `118.9152` | 277,119.98 USD | 8,330,552.61 USD | `17 orders` | `+0.07%` | `-` |
| `ASK` | `2330.50` | `181.1493` | 422,168.44 USD | 8,752,721.05 USD | `15 orders` | `+0.08%` | `-` |
| `ASK` | `2330.60` | `177.8501` | 414,497.44 USD | 9,167,218.49 USD | `15 orders` | `+0.08%` | `-` |
| `ASK` | `2330.70` | `386.8262` | 901,575.82 USD | 10,068,794.32 USD | `12 orders` | `+0.08%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:15:45 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 00:15:45 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1918.00` | `4,184.01` | 8,024,935.59 USD | `TRIGGER_STOP` | `0x6ea486a342` | `2026-10-30 00:15:45 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1918.99` | `8,092.45` | 15,529,329.85 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 00:15:45 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `8,500.00` | 16,371,850.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-30 00:15:45 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2040.68` | `7,964.66` | 16,253,321.14 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-30 00:15:45 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2115.20` | `7,500.00` | 15,864,017.53 USD | `AT_RISK_LIQ` | `0x524ed67d71` | `2026-10-30 00:15:45 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2171.14` | `48,499.51` | 105,299,308.58 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 00:15:45 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2180.20` | `44,734.81` | 97,531,035.84 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 00:15:45 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2250.00` | `6,500.00` | 14,625,000.00 USD | `TRIGGER_STOP` | `0x6eae4120a8` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2287.00` | `2,066.36` | 4,725,765.09 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 00:15:45 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2292.00` | `2,500.00` | 5,730,000.00 USD | `TRIGGER_STOP` | `0x934de82f50` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2295.30` | `5,287.01` | 12,135,262.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2298.20` | `1,344.77` | 3,090,542.83 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2300.00` | `502.36` | 1,155,425.70 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xa5d0a11e20` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2303.00` | `908.97` | 2,093,354.23 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x0c4a3a7ac7` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2305.70` | `605.37` | 1,395,792.39 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2307.10` | `964.92` | 2,226,172.93 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2307.10` | `346.80` | 800,091.44 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2307.10` | `332.67` | 767,507.80 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 00:15:45 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2307.20` | `599,999.99` | 1,384,319,976.93 USD | `TRIGGER_STOP` | `0x069604ebfb` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2310.30` | `2,726.98` | 6,300,145.36 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2310.40` | `396.40` | 915,849.72 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x7b7f72a28f` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2311.50` | `437.77` | 1,011,912.29 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2311.80` | `1,732.22` | 4,004,553.59 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2311.90` | `606.91` | 1,403,119.85 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2314.00` | `1,297.90` | 3,003,345.46 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2314.30` | `607.05` | 1,404,891.19 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2314.40` | `677.80` | 1,568,695.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2314.70` | `1,015.35` | 2,350,222.78 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x674982e841` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2316.70` | `864.26` | 2,002,235.78 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2317.70` | `1,392.51` | 3,227,431.09 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2317.70` | `437.97` | 1,015,083.07 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2318.30` | `647.74` | 1,501,657.50 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2318.50` | `465.45` | 1,079,149.77 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 00:15:45 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2319.00` | `2,500.00` | 5,797,500.00 USD | `TRIGGER_STOP` | `0x524ed67d71` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2320.00` | `431.51` | 1,001,103.66 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2320.40` | `396.67` | 920,422.39 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x76bf72092b` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2321.80` | `404.75` | 939,748.55 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2328.50` | `429.95` | 1,001,139.27 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2329.10` | `330.68` | 770,194.24 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2329.60` | `404.74` | 942,889.29 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2330.40` | `471.66` | 1,099,151.10 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2330.70` | `644.32` | 1,501,708.23 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2332.30` | `396.19` | 924,026.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x76bf72092b` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2332.40` | `858.47` | 2,002,304.99 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2332.50` | `437.74` | 1,021,026.22 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2333.60` | `1,394.09` | 3,253,253.09 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2335.60` | `606.60` | 1,416,774.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2336.50` | `1,713.91` | 4,004,548.85 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2337.10` | `686.18` | 1,603,664.73 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2337.20` | `438.19` | 1,024,135.33 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2337.80` | `607.07` | 1,419,215.26 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2338.80` | `1,284.19` | 3,003,453.28 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2344.10` | `978.50` | 2,293,702.79 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2344.30` | `396.69` | 929,954.51 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x7b7f72a28f` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2344.40` | `2,726.98` | 6,393,135.43 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2348.00` | `340.75` | 800,091.33 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2348.10` | `326.86` | 767,507.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2349.10` | `606.30` | 1,424,259.33 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2353.50` | `1,403.82` | 3,303,893.19 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2359.40` | `5,287.01` | 12,474,159.60 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 00:15:45 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2365.30` | `2,009.36` | 4,752,730.22 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 00:15:45 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2440.00` | `4,002.10` | 9,765,127.17 USD | `TRIGGER_STOP` | `0xfb941d2344` | `2026-10-30 00:15:45 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2585.90` | `6,224.05` | 16,094,776.27 USD | `AT_RISK_LIQ` | `0x08bf75d170` | `2026-10-30 00:15:45 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2658.65` | `9,700.00` | 25,788,913.40 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-30 00:15:45 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2709.00` | `8,500.00` | 23,026,520.04 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-30 00:15:45 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 247,570,163.34 USD | `106,417.71` | `2322.74` | `2326.32` | `3834.55` | -389,151.18 USD | `-0.16%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 151,784,593.79 USD | `65,205.17` | `2375.30` | `2326.32` | `4383.88` | 3,097,669.30 USD | `+2.04%` | `5X Cross` |
| `6` | `0x77dd...e0e9` | `LONG` | 112,911,713.65 USD | `48,499.51` | `2610.31` | `2326.32` | `2171.17` | -13,687,170.21 USD | `-12.12%` | `10X Cross` |
| `7` | `0x0392...d7d9` | `LONG` | 104,133,698.63 USD | `44,734.81` | `2518.71` | `2326.32` | `2180.23` | -8,540,607.94 USD | `-8.20%` | `9X Cross` |
| `15` | `0xde8d...9524` | `LONG` | 70,485,322.39 USD | `30,282.40` | `2134.45` | `2326.32` | `1787.12` | 5,848,991.81 USD | `+8.30%` | `20X Cross` |
| `18` | `0x7fda...17d1` | `SHORT` | 64,811,144.57 USD | `27,858.99` | `2437.60` | `2326.32` | `3615.66` | 3,098,119.93 USD | `+4.78%` | `25X Cross` |
| `25` | `0xdf95...7d72` | `SHORT` | 52,693,789.13 USD | `22,650.36` | `2402.54` | `2326.32` | `3974.11` | 1,724,629.95 USD | `+3.27%` | `25X Cross` |
| `29` | `0xeced...6210` | `SHORT` | 43,474,777.50 USD | `18,687.58` | `2522.09` | `2326.32` | `3353.31` | 3,657,134.95 USD | `+8.41%` | `20X Cross` |
| `34` | `0xb695...a92d` | `SHORT` | 38,849,933.57 USD | `16,704.62` | `2557.74` | `2326.32` | `4042.90` | 3,876,231.48 USD | `+9.98%` | `20X Cross` |
| `35` | `0x6046...b21d` | `LONG` | 37,058,722.95 USD | `15,927.59` | `2410.19` | `2326.32` | `1565.35` | -1,329,896.69 USD | `-3.59%` | `6X Cross` |
| `38` | `0x45d2...4029` | `SHORT` | 32,443,515.00 USD | `13,950.00` | `2443.60` | `2326.32` | `4985.18` | 1,644,767.46 USD | `+5.07%` | `20X Cross` |
| `43` | `0x0622...8088` | `LONG` | 29,317,327.46 USD | `12,602.01` | `2342.49` | `2326.32` | `1535.01` | -202,824.07 USD | `-0.69%` | `5X Cross` |
| `45` | `0xbd1c...ff0e` | `LONG` | 27,936,000.00 USD | `12,000.00` | `2419.91` | `2326.32` | `1521.00` | -1,103,032.39 USD | `-3.95%` | `20X Cross` |
| `46` | `0x2371...0883` | `LONG` | 27,933,600.00 USD | `12,000.00` | `2421.77` | `2326.32` | `1280.10` | -1,127,694.85 USD | `-4.04%` | `20X Cross` |
| `50` | `0xa9de...e049` | `LONG` | 25,593,700.00 USD | `11,000.00` | `2481.81` | `2326.32` | `1644.74` | -1,706,279.46 USD | `-6.67%` | `20X Cross` |
| `51` | `0x0c5d...36b3` | `LONG` | 25,593,700.00 USD | `11,000.00` | `2482.20` | `2326.32` | `1645.07` | -1,710,553.24 USD | `-6.68%` | `20X Cross` |
| `52` | `0x09dc...c094` | `LONG` | 25,590,400.00 USD | `11,000.00` | `2465.31` | `2326.32` | `1638.07` | -1,528,023.04 USD | `-5.97%` | `20X Cross` |
| `53` | `0x6c93...59a4` | `LONG` | 25,589,300.00 USD | `11,000.00` | `2441.15` | `2326.32` | `1603.03` | -1,263,372.73 USD | `-4.94%` | `20X Cross` |
| `55` | `0xa61c...66b9` | `LONG` | 25,341,820.00 USD | `10,888.00` | `2398.32` | `2326.32` | `1416.66` | -771,137.39 USD | `-3.04%` | `10X Cross` |
| `59` | `0x4487...c92d` | `SHORT` | 24,683,305.01 USD | `10,611.45` | `2373.98` | `2326.32` | `2860.06` | 508,174.36 USD | `+2.06%` | `10X Cross` |
| `66` | `0xa2ce...3126` | `LONG` | 23,300,253.40 USD | `10,016.88` | `2162.83` | `2326.32` | `1450.59` | 1,635,451.35 USD | `+7.02%` | `10X Cross` |
| `67` | `0x6646...6de5` | `LONG` | 23,282,000.00 USD | `10,000.00` | `1765.80` | `2326.32` | `1731.36` | 5,623,942.55 USD | `+24.16%` | `25X Cross` |
| `68` | `0x15a4...dfdb` | `LONG` | 23,267,000.00 USD | `10,000.00` | `1761.94` | `2326.32` | `35.03` | 5,647,518.97 USD | `+24.27%` | `20X Cross` |
| `69` | `0xec7f...df39` | `LONG` | 23,264,000.00 USD | `10,000.00` | `2719.35` | `2326.32` | `1721.59` | -3,929,548.52 USD | `-16.89%` | `20X Cross` |
| `75` | `0xaeaa...2416` | `SHORT` | 22,579,660.00 USD | `9,700.00` | `2311.92` | `2326.32` | `2658.68` | -153,977.60 USD | `-0.68%` | `25X Cross` |
| `81` | `0xca49...53c8` | `SHORT` | 21,549,598.44 USD | `9,264.26` | `2549.47` | `2326.32` | `3737.55` | 2,069,426.30 USD | `+9.60%` | `25X Cross` |
| `82` | `0xba5d...a352` | `SHORT` | 21,063,509.65 USD | `9,054.12` | `2493.89` | `2326.32` | `2924.58` | 1,516,497.61 USD | `+7.20%` | `20X Cross` |
| `84` | `0xea00...a918` | `LONG` | 20,957,306.10 USD | `9,003.83` | `2003.01` | `2326.32` | `1218.03` | 2,922,527.23 USD | `+13.95%` | `5X Cross` |
| `95` | `0xb37f...66ca` | `SHORT` | 19,768,450.00 USD | `8,500.00` | `2308.30` | `2326.32` | `2709.03` | -147,895.81 USD | `-0.75%` | `25X Cross` |
| `107` | `0xecb6...2b00` | `SHORT` | 18,873,082.62 USD | `8,112.57` | `2327.64` | `2326.32` | `5710.71` | 10,115.35 USD | `+0.05%` | `15X Cross` |
| `108` | `0x9eec...daab` | `LONG` | 18,820,615.85 USD | `8,092.45` | `1658.44` | `2326.32` | `1919.69` | 5,399,751.32 USD | `+28.69%` | `15X Cross` |
| `110` | `0x218a...7da2` | `SHORT` | 18,608,442.64 USD | `7,997.78` | `2208.16` | `2326.32` | `2877.25` | -948,047.42 USD | `-5.09%` | `10X Cross` |
| `111` | `0x5f91...65aa` | `LONG` | 18,538,533.07 USD | `7,964.66` | `1626.99` | `2326.32` | `2040.71` | 5,580,090.01 USD | `+30.10%` | `16X Cross` |
| `114` | `0xcf53...ee11` | `SHORT` | 17,686,798.86 USD | `7,603.63` | `1862.69` | `2326.32` | `3992.27` | -3,523,534.92 USD | `-19.92%` | `7X Cross` |
| `115` | `0x524e...0de0` | `LONG` | 17,458,500.00 USD | `7,500.00` | `2320.35` | `2326.32` | `2115.23` | 55,813.78 USD | `+0.32%` | `10X Cross` |
| `120` | `0x939f...04d2` | `LONG` | 16,807,645.47 USD | `7,223.81` | `2500.18` | `2326.32` | `1806.38` | -1,253,244.70 USD | `-7.46%` | `25X Cross` |
| `123` | `0xec0b...b078` | `LONG` | 16,310,651.94 USD | `7,007.80` | `2065.97` | `2326.32` | `1011.14` | 1,832,722.35 USD | `+11.24%` | `25X Cross` |
| `124` | `0x1ee7...edf5` | `LONG` | 16,293,200.00 USD | `7,000.00` | `2330.22` | `2326.32` | `2153.93` | -18,362.20 USD | `-0.11%` | `25X Cross` |
| `130` | `0x418a...8888` | `SHORT` | 15,643,604.15 USD | `6,724.38` | `2494.55` | `2326.32` | `2961.79` | 1,130,719.03 USD | `+7.23%` | `25X Cross` |
| `131` | `0x4ff9...38d3` | `LONG` | 15,270,719.22 USD | `6,564.10` | `2447.40` | `2326.32` | `1670.69` | -794,303.53 USD | `-5.20%` | `3X Isolated` |
| `135` | `0xf78c...c581` | `LONG` | 15,131,215.61 USD | `6,500.22` | `2521.53` | `2326.32` | `1914.17` | -1,259,325.34 USD | `-8.32%` | `20X Cross` |
| `140` | `0x799f...5f4c` | `LONG` | 14,681,054.35 USD | `6,310.90` | `2390.33` | `2326.32` | `1723.83` | -404,110.27 USD | `-2.75%` | `20X Cross` |
| `143` | `0x08bf...7872` | `SHORT` | 14,477,756.66 USD | `6,224.05` | `2258.00` | `2326.32` | `2585.93` | -423,840.55 USD | `-2.93%` | `20X Cross` |
| `151` | `0xd9e7...4aff` | `LONG` | 13,960,200.00 USD | `6,000.00` | `2480.18` | `2326.32` | `1408.46` | -920,924.33 USD | `-6.60%` | `20X Cross` |
| `159` | `0x0c4a...1b19` | `LONG` | 13,289,032.42 USD | `5,706.39` | `2382.15` | `2326.32` | `2185.22` | -304,438.76 USD | `-2.29%` | `25X Isolated` |
| `176` | `0x645b...87b8` | `SHORT` | 11,804,557.36 USD | `5,073.52` | `2421.68` | `2326.32` | `6157.12` | 481,896.77 USD | `+4.08%` | `10X Cross` |
| `183` | `0x45ab...6cbc` | `LONG` | 11,454,031.62 USD | `4,920.96` | `2727.66` | `2326.32` | `1366.69` | -1,968,712.18 USD | `-17.19%` | `7X Cross` |
| `185` | `0xfb18...eb17` | `SHORT` | 11,333,797.57 USD | `4,872.45` | `2315.54` | `2326.32` | `2710.28` | -51,424.54 USD | `-0.45%` | `25X Cross` |
| `186` | `0x64b7...9da9` | `LONG` | 11,304,293.24 USD | `4,856.84` | `2604.61` | `2326.32` | `1414.94` | -1,345,921.18 USD | `-11.91%` | `25X Cross` |
| `194` | `0x5559...d43b` | `SHORT` | 11,065,611.40 USD | `4,755.93` | `2262.69` | `2326.32` | `2872.64` | -304,405.52 USD | `-2.75%` | `25X Cross` |
| `208` | `0xe091...6705` | `SHORT` | 10,470,150.47 USD | `4,500.00` | `2467.33` | `2326.32` | `2572.98` | 632,858.04 USD | `+6.04%` | `20X Cross` |
| `217` | `0xfe7c...b7ae` | `SHORT` | 10,247,451.26 USD | `4,402.58` | `2440.17` | `2326.32` | `4220.86` | 495,636.61 USD | `+4.84%` | `25X Cross` |
| `230` | `0xc179...e0c8` | `LONG` | 10,024,818.42 USD | `4,309.16` | `2342.89` | `2326.32` | `858.20` | -71,060.37 USD | `-0.71%` | `10X Cross` |
| `237` | `0x12d2...f97f` | `LONG` | 9,925,252.98 USD | `4,264.34` | `2623.90` | `2326.32` | `1847.43` | -1,263,981.44 USD | `-12.74%` | `20X Cross` |
| `240` | `0x28bb...fca6` | `SHORT` | 9,797,877.05 USD | `4,209.61` | `1896.10` | `2326.32` | `3045.65` | -1,815,994.49 USD | `-18.53%` | `20X Cross` |
| `241` | `0x6ea4...0ea7` | `SHORT` | 9,743,727.84 USD | `4,184.01` | `2602.13` | `2326.32` | `3425.99` | 1,143,618.82 USD | `+11.74%` | `20X Cross` |
| `251` | `0x5e9e...35ee` | `SHORT` | 9,329,589.67 USD | `4,007.56` | `1796.39` | `2326.32` | `2586.49` | -2,130,439.58 USD | `-22.84%` | `20X Cross` |
| `252` | `0xfb94...0ddf` | `SHORT` | 9,315,290.99 USD | `4,002.10` | `2382.44` | `2326.32` | `5105.38` | 219,493.16 USD | `+2.36%` | `20X Cross` |
| `253` | `0x95fe...f8fa` | `LONG` | 9,311,600.00 USD | `4,000.00` | `2341.35` | `2326.32` | `2258.99` | -53,816.51 USD | `-0.58%` | `20X Isolated` |
| `254` | `0x3dc9...54b0` | `SHORT` | 9,310,478.85 USD | `3,999.69` | `2480.32` | `2326.32` | `5918.26` | 610,057.70 USD | `+6.55%` | `20X Cross` |
| `255` | `0x8cc9...2b6a` | `SHORT` | 9,305,600.00 USD | `4,000.00` | `1791.18` | `2326.32` | `3878.45` | -2,140,853.33 USD | `-23.01%` | `25X Cross` |
| `258` | `0x77ee...2902` | `SHORT` | 9,264,257.78 USD | `3,982.23` | `2476.53` | `2326.32` | `4288.31` | 597,863.80 USD | `+6.45%` | `25X Cross` |
| `268` | `0xf02d...5eb3` | `LONG` | 8,970,179.07 USD | `3,855.99` | `2513.67` | `2326.32` | `314.62` | -722,533.25 USD | `-8.05%` | `20X Cross` |
| `272` | `0x4b67...f4e7` | `LONG` | 8,893,391.61 USD | `3,820.84` | `2591.51` | `2326.32` | `1597.05` | -1,008,381.94 USD | `-11.34%` | `20X Cross` |
| `293` | `0x382b...3e39` | `SHORT` | 8,289,879.61 USD | `3,561.56` | `2299.50` | `2326.32` | `3757.38` | -100,054.14 USD | `-1.21%` | `25X Cross` |
| `295` | `0x8ae4...3d60` | `LONG` | 8,277,792.53 USD | `3,558.20` | `2482.21` | `2326.32` | `354.78` | -554,405.51 USD | `-6.70%` | `10X Cross` |
| `319` | `0x9c06...0560` | `SHORT` | 7,685,448.51 USD | `3,303.58` | `2270.55` | `2326.32` | `3313.88` | -184,484.57 USD | `-2.40%` | `25X Cross` |
| `329` | `0x984e...14c2` | `SHORT` | 7,238,793.89 USD | `3,111.99` | `2357.50` | `2326.32` | `2434.95` | 97,728.87 USD | `+1.35%` | `20X Cross` |
| `335` | `0x9c2a...f6a8` | `SHORT` | 7,119,525.32 USD | `3,058.48` | `2543.83` | `2326.32` | `2597.99` | 660,735.30 USD | `+9.28%` | `20X Cross` |
| `338` | `0x39b4...5c34` | `SHORT` | 6,985,521.79 USD | `3,000.91` | `2329.97` | `2326.32` | `2405.88` | 6,521.96 USD | `+0.09%` | `25X Cross` |
| `339` | `0x4a20...3c26` | `LONG` | 6,984,300.00 USD | `3,000.00` | `2428.72` | `2326.32` | `258.34` | -301,860.28 USD | `-4.32%` | `20X Cross` |
| `340` | `0x007d...67a0` | `LONG` | 6,978,300.00 USD | `3,000.00` | `2400.00` | `2326.32` | `1488.32` | -221,700.00 USD | `-3.18%` | `25X Cross` |
| `380` | `0xf517...c032` | `SHORT` | 6,372,858.62 USD | `2,738.07` | `2053.90` | `2326.32` | `5649.07` | -749,116.71 USD | `-11.75%` | `25X Cross` |
| `397` | `0xbb34...1696` | `LONG` | 6,051,760.00 USD | `2,600.00` | `2318.80` | `2326.32` | `1971.13` | 22,859.15 USD | `+0.38%` | `25X Cross` |
| `398` | `0xc619...10f5` | `LONG` | 6,048,640.00 USD | `2,600.00` | `2318.40` | `2326.32` | `1855.83` | 20,791.09 USD | `+0.34%` | `25X Cross` |
| `400` | `0x8328...f54a` | `SHORT` | 5,995,144.06 USD | `2,576.45` | `2292.01` | `2326.32` | `3280.23` | -89,872.78 USD | `-1.50%` | `25X Cross` |
| `401` | `0xed48...7c9b` | `SHORT` | 5,933,164.20 USD | `2,551.13` | `2460.02` | `2326.32` | `3240.01` | 342,682.21 USD | `+5.78%` | `20X Cross` |
| `404` | `0x934d...92c9` | `LONG` | 5,815,750.00 USD | `2,500.00` | `2343.98` | `2326.32` | `2165.14` | -44,214.51 USD | `-0.76%` | `25X Cross` |
| `423` | `0xfbe2...c8ea` | `SHORT` | 5,591,161.41 USD | `2,404.08` | `2041.57` | `2326.32` | `2689.24` | -683,068.69 USD | `-12.22%` | `20X Cross` |
| `429` | `0x1c98...7fc7` | `LONG` | 5,485,661.67 USD | `2,358.00` | `2467.15` | `2326.32` | `1897.21` | -331,909.81 USD | `-6.05%` | `10X Cross` |
| `442` | `0x6859...7e1e` | `SHORT` | 5,177,707.62 USD | `2,224.58` | `2200.39` | `2326.32` | `3672.99` | -282,754.90 USD | `-5.46%` | `25X Cross` |
| `458` | `0xd507...c948` | `SHORT` | 5,055,329.77 USD | `2,172.00` | `2387.49` | `2326.32` | `2707.41` | 130,311.26 USD | `+2.58%` | `5X Isolated` |
| `462` | `0xb829...3a81` | `LONG` | 5,010,858.55 USD | `2,153.91` | `2537.61` | `2326.32` | `780.22` | -454,938.18 USD | `-9.08%` | `20X Cross` |
| `495` | `0x3440...32c5` | `SHORT` | 4,653,914.82 USD | `2,000.57` | `2198.21` | `2326.32` | `3549.23` | -256,251.69 USD | `-5.51%` | `25X Cross` |
| `496` | `0xf929...d1f9` | `SHORT` | 4,653,400.00 USD | `2,000.00` | `2423.37` | `2326.32` | `2548.81` | 193,340.34 USD | `+4.15%` | `25X Cross` |
| `506` | `0x0514...bdfe` | `SHORT` | 4,535,895.00 USD | `1,950.00` | `1988.74` | `2326.32` | `2954.54` | -657,835.37 USD | `-14.50%` | `25X Cross` |
| `512` | `0x8376...9a1e` | `SHORT` | 4,446,870.49 USD | `1,910.50` | `2477.72` | `2326.32` | `3157.99` | 286,817.68 USD | `+6.45%` | `20X Cross` |
| `514` | `0xd4c1...3d1d` | `SHORT` | 4,436,434.25 USD | `1,906.09` | `2336.05` | `2326.32` | `4853.03` | 16,311.29 USD | `+0.37%` | `12X Cross` |
| `538` | `0x7a6d...f79c` | `SHORT` | 4,246,395.02 USD | `1,825.07` | `2433.80` | `2326.32` | `2786.52` | 195,473.86 USD | `+4.60%` | `25X Cross` |
| `543` | `0x541e...071d` | `SHORT` | 4,202,220.50 USD | `1,805.00` | `2648.19` | `2326.32` | `3032.05` | 577,764.34 USD | `+13.75%` | `25X Cross` |
| `544` | `0x7265...91a5` | `LONG` | 4,192,409.53 USD | `1,801.87` | `2533.96` | `2326.32` | `1988.14` | -373,456.92 USD | `-8.91%` | `20X Cross` |
| `545` | `0x739c...cfb2` | `SHORT` | 4,190,040.00 USD | `1,800.00` | `2427.60` | `2326.32` | `2658.07` | 179,656.38 USD | `+4.29%` | `25X Cross` |
| `556` | `0xa445...329d` | `LONG` | 4,132,185.85 USD | `1,776.75` | `2398.85` | `2326.32` | `1793.63` | -129,983.50 USD | `-3.15%` | `25X Cross` |
| `560` | `0x91a9...3f70` | `SHORT` | 4,114,339.94 USD | `1,767.48` | `2156.23` | `2326.32` | `3624.40` | -303,235.86 USD | `-7.37%` | `4X Cross` |
| `565` | `0x3453...b323` | `SHORT` | 4,073,936.55 USD | `1,750.12` | `2328.82` | `2326.32` | `2398.02` | 1,795.58 USD | `+0.04%` | `25X Cross` |
| `591` | `0xfeec...4e9c` | `SHORT` | 3,935,654.81 USD | `1,691.81` | `2566.49` | `2326.32` | `2651.15` | 406,369.70 USD | `+10.33%` | `10X Cross` |
| `594` | `0x936c...bb0f` | `SHORT` | 3,927,377.03 USD | `1,688.69` | `2434.60` | `2326.32` | `8531.35` | 183,910.08 USD | `+4.68%` | `20X Cross` |
| `611` | `0xeee0...0b53` | `LONG` | 3,809,423.60 USD | `1,637.12` | `2468.64` | `2326.32` | `133.58` | -232,052.46 USD | `-6.09%` | `7X Cross` |
| `616` | `0x27b8...12fc` | `LONG` | 3,791,566.09 USD | `1,628.12` | `2468.73` | `2326.32` | `437.43` | -227,828.55 USD | `-6.01%` | `10X Cross` |
| `617` | `0x982b...4606` | `LONG` | 3,786,579.95 USD | `1,626.82` | `2575.24` | `2326.32` | `1548.41` | -402,873.13 USD | `-10.64%` | `5X Isolated` |
| `626` | `0x73d7...8be1` | `LONG` | 3,725,168.90 USD | `1,601.47` | `2410.40` | `2326.32` | `2044.81` | -135,010.02 USD | `-3.62%` | `25X Cross` |
| `650` | `0xe170...9300` | `SHORT` | 3,567,301.76 USD | `1,533.40` | `2076.39` | `2326.32` | `3213.63` | -383,352.26 USD | `-10.75%` | `25X Cross` |
| `656` | `0xfc27...9d9d` | `SHORT` | 3,545,376.39 USD | `1,524.43` | `2402.17` | `2326.32` | `11988.64` | 116,575.51 USD | `+3.29%` | `25X Cross` |
| `663` | `0x2e2b...2fab` | `LONG` | 3,509,022.92 USD | `1,507.38` | `2245.53` | `2326.32` | `1084.76` | 124,149.82 USD | `+3.54%` | `25X Cross` |
| `668` | `0x251f...6e5d` | `LONG` | 3,491,250.00 USD | `1,500.00` | `2346.68` | `2326.32` | `1633.89` | -28,780.49 USD | `-0.82%` | `20X Cross` |
| `680` | `0xad54...6203` | `LONG` | 3,392,748.10 USD | `1,458.18` | `2627.45` | `2326.32` | `2146.47` | -438,558.58 USD | `-12.93%` | `10X Isolated` |
| `686` | `0xef70...a84c` | `SHORT` | 3,357,985.26 USD | `1,442.74` | `2424.73` | `2326.32` | `3453.63` | 140,285.56 USD | `+4.18%` | `25X Cross` |
| `693` | `0x4b5f...0dd8` | `LONG` | 3,333,452.23 USD | `1,431.96` | `2339.45` | `2326.32` | `2148.70` | -16,540.71 USD | `-0.50%` | `10X Cross` |
| `696` | `0xbadb...9ee6` | `LONG` | 3,322,899.87 USD | `1,428.16` | `1936.00` | `2326.32` | `1030.33` | 557,978.23 USD | `+16.79%` | `20X Cross` |
| `751` | `0x023a...2355` | `LONG` | 3,127,973.45 USD | `1,344.56` | `2340.68` | `2326.32` | `0.000000` | -19,213.55 USD | `-0.61%` | `25X Cross` |
| `767` | `0x880a...311c` | `SHORT` | 3,071,367.02 USD | `1,320.22` | `2425.76` | `2326.32` | `8260.99` | 131,182.13 USD | `+4.27%` | `9X Cross` |
| `774` | `0x29de...3e93` | `LONG` | 3,049,418.00 USD | `1,310.00` | `2352.60` | `2326.32` | `1922.23` | -32,490.82 USD | `-1.07%` | `5X Isolated` |
| `807` | `0xc435...c905` | `SHORT` | 2,903,721.60 USD | `1,248.00` | `2704.38` | `2326.32` | `4866.19` | 471,348.75 USD | `+16.23%` | `20X Cross` |
| `816` | `0x4202...aaf5` | `SHORT` | 2,868,339.04 USD | `1,232.10` | `2321.73` | `2326.32` | `2733.54` | -7,714.74 USD | `-0.27%` | `5X Isolated` |
| `824` | `0x7178...0854` | `LONG` | 2,835,024.32 USD | `1,218.63` | `2461.81` | `2326.32` | `1058.16` | -165,022.08 USD | `-5.82%` | `10X Cross` |
| `868` | `0x07fd...689d` | `LONG` | 2,644,147.09 USD | `1,135.90` | `2423.84` | `2326.32` | `0.000000` | -109,096.11 USD | `-4.13%` | `25X Cross` |
| `905` | `0x2f80...f203` | `SHORT` | 2,533,312.58 USD | `1,088.94` | `1984.00` | `2326.32` | `3073.20` | -372,845.39 USD | `-14.72%` | `20X Cross` |
| `912` | `0x6f11...0389` | `SHORT` | 2,511,696.20 USD | `1,079.00` | `2333.39` | `2326.32` | `3199.68` | 6,032.71 USD | `+0.24%` | `25X Cross` |
| `914` | `0x2b61...2f6c` | `SHORT` | 2,504,595.73 USD | `1,076.60` | `2681.75` | `2326.32` | `6314.74` | 382,577.01 USD | `+15.28%` | `10X Cross` |
| `955` | `0x1b2a...f7a6` | `LONG` | 2,386,646.56 USD | `1,025.37` | `2737.51` | `2326.32` | `930.17` | -420,313.38 USD | `-17.61%` | `10X Cross` |
| `956` | `0xb15b...dbae` | `SHORT` | 2,384,893.14 USD | `1,025.14` | `2338.37` | `2326.32` | `2381.06` | 12,280.58 USD | `+0.51%` | `25X Cross` |
| `963` | `0x6749...ce07` | `SHORT` | 2,362,000.80 USD | `1,015.35` | `2318.56` | `2326.32` | `5889.00` | -7,857.44 USD | `-0.33%` | `20X Cross` |
| `970` | `0x02aa...1806` | `SHORT` | 2,344,025.48 USD | `1,007.10` | `2654.68` | `2326.32` | `3613.68` | 329,506.62 USD | `+14.06%` | `20X Cross` |
| `973` | `0x001a...fef6` | `SHORT` | 2,343,340.15 USD | `1,007.33` | `2022.19` | `2326.32` | `3037.75` | -306,332.19 USD | `-13.07%` | `10X Cross` |
| `976` | `0xdb3a...cf3b` | `LONG` | 2,335,284.11 USD | `1,003.22` | `2705.01` | `2326.32` | `0.000000` | -378,422.78 USD | `-16.20%` | `4X Cross` |
| `982` | `0x5986...89d9` | `LONG` | 2,328,800.00 USD | `1,000.00` | `2346.34` | `2326.32` | `1256.66` | -17,549.54 USD | `-0.75%` | `25X Cross` |
| `983` | `0xdf60...d3c7` | `LONG` | 2,327,900.00 USD | `1,000.00` | `2736.24` | `2326.32` | `2246.08` | -408,342.88 USD | `-17.54%` | `10X Isolated` |
| `984` | `0xfe82...ce65` | `SHORT` | 2,327,900.00 USD | `1,000.00` | `2300.50` | `2326.32` | `2718.42` | -27,392.07 USD | `-1.18%` | `25X Cross` |
| `985` | `0x4044...794c` | `LONG` | 2,327,600.00 USD | `1,000.00` | `2332.68` | `2326.32` | `0.000000` | -5,089.84 USD | `-0.22%` | `25X Cross` |
| `986` | `0x2828...93a0` | `LONG` | 2,326,700.00 USD | `1,000.00` | `2393.30` | `2326.32` | `2274.75` | -66,609.16 USD | `-2.86%` | `25X Cross` |
| `987` | `0x5272...fcd9` | `SHORT` | 2,326,300.00 USD | `1,000.00` | `2241.82` | `2326.32` | `2880.75` | -84,475.51 USD | `-3.63%` | `5X Cross` |
| `1010` | `0xb002...ed8a` | `SHORT` | 2,240,302.09 USD | `962.78` | `2299.66` | `2326.32` | `4192.72` | -26,224.18 USD | `-1.17%` | `25X Cross` |
| `1027` | `0x2e30...4cb5` | `SHORT` | 2,206,914.13 USD | `948.76` | `2340.09` | `2326.32` | `7266.17` | 13,280.90 USD | `+0.60%` | `2X Cross` |
| `1035` | `0xc8fe...afa4` | `LONG` | 2,179,405.36 USD | `936.37` | `2331.34` | `2326.32` | `2145.81` | -3,598.87 USD | `-0.17%` | `10X Isolated` |
| `1052` | `0x9606...4e5d` | `SHORT` | 2,123,995.52 USD | `913.00` | `2478.70` | `2326.32` | `3969.94` | 139,058.08 USD | `+6.55%` | `20X Cross` |
| `1057` | `0xaeea...bfa7` | `LONG` | 2,114,016.52 USD | `908.75` | `2339.31` | `2326.32` | `2286.72` | -11,825.58 USD | `-0.56%` | `23X Isolated` |
| `1089` | `0x60f7...d1ee` | `LONG` | 2,072,009.00 USD | `890.00` | `2343.49` | `2326.32` | `2269.23` | -13,700.96 USD | `-0.66%` | `25X Cross` |
| `1172` | `0xcd27...52a8` | `LONG` | 1,948,853.48 USD | `837.21` | `2553.56` | `2326.32` | `1404.23` | -189,011.29 USD | `-9.70%` | `2X Cross` |
| `1183` | `0xbef3...0d3e` | `LONG` | 1,933,637.61 USD | `830.99` | `2332.88` | `2326.32` | `2110.69` | -4,973.64 USD | `-0.26%` | `20X Cross` |
| `1187` | `0x6a41...a3b9` | `LONG` | 1,921,661.98 USD | `826.06` | `2332.61` | `2326.32` | `2112.87` | -5,212.87 USD | `-0.27%` | `20X Cross` |
| `1219` | `0x2577...4897` | `LONG` | 1,879,950.81 USD | `808.09` | `2356.16` | `2326.32` | `0.000000` | -24,053.07 USD | `-1.28%` | `15X Cross` |
| `1224` | `0x3fc5...c0c1` | `SHORT` | 1,872,152.24 USD | `804.26` | `2702.11` | `2326.32` | `4929.27` | 301,049.29 USD | `+16.08%` | `25X Cross` |
| `1226` | `0xf83f...625f` | `SHORT` | 1,867,972.98 USD | `803.05` | `2601.00` | `2326.32` | `6042.93` | 220,763.48 USD | `+11.82%` | `20X Cross` |
| `1230` | `0x04a9...95aa` | `LONG` | 1,862,240.00 USD | `800.00` | `2595.13` | `2326.32` | `1862.26` | -213,866.74 USD | `-11.48%` | `5X Cross` |
| `1231` | `0x7737...bf66` | `SHORT` | 1,860,635.88 USD | `799.79` | `2494.83` | `2326.32` | `24837.17` | 134,710.15 USD | `+7.24%` | `15X Cross` |
| `1268` | `0x458d...ab3b` | `LONG` | 1,802,758.79 USD | `774.75` | `2740.41` | `2326.32` | `1887.98` | -320,370.39 USD | `-17.77%` | `3X Isolated` |
| `1303` | `0x7743...e4fe` | `SHORT` | 1,746,919.56 USD | `750.56` | `2326.87` | `2326.32` | `5895.11` | -465.42 USD | `-0.03%` | `25X Cross` |
| `1305` | `0x5f10...d49d` | `SHORT` | 1,744,575.00 USD | `750.00` | `2350.92` | `2326.32` | `2842.52` | 18,621.61 USD | `+1.07%` | `25X Cross` |
| `1344` | `0x51a0...3543` | `SHORT` | 1,686,597.71 USD | `724.55` | `2627.71` | `2326.32` | `7682.13` | 217,299.04 USD | `+12.88%` | `20X Cross` |
| `1349` | `0x4b1c...bc38` | `SHORT` | 1,680,853.53 USD | `722.14` | `2529.31` | `2326.32` | `4533.90` | 145,668.43 USD | `+8.67%` | `10X Cross` |
| `1356` | `0xa189...94d7` | `SHORT` | 1,674,455.16 USD | `719.98` | `2691.84` | `2326.32` | `3051.93` | 263,617.50 USD | `+15.74%` | `25X Cross` |
| `1363` | `0x3ee5...4fab` | `SHORT` | 1,663,764.28 USD | `715.17` | `2759.35` | `2326.32` | `3361.76` | 309,635.69 USD | `+18.61%` | `20X Cross` |
| `1371` | `0x2f93...4404` | `LONG` | 1,647,135.15 USD | `707.47` | `1700.45` | `2326.32` | `1369.61` | 444,108.77 USD | `+26.96%` | `4X Isolated` |
| `1378` | `0x5605...fe0f` | `SHORT` | 1,635,152.02 USD | `702.14` | `2566.90` | `2326.32` | `3034.84` | 167,180.63 USD | `+10.22%` | `20X Cross` |
| `1387` | `0xaa53...9cb7` | `LONG` | 1,628,410.00 USD | `700.00` | `2394.46` | `2326.32` | `1952.16` | -47,712.07 USD | `-2.93%` | `20X Cross` |
| `1433` | `0xdbd1...29dd` | `SHORT` | 1,584,811.56 USD | `680.70` | `3030.57` | `2326.32` | `4065.16` | 478,109.56 USD | `+30.17%` | `6X Cross` |
| `1438` | `0x71e5...be04` | `LONG` | 1,576,456.28 USD | `677.67` | `2727.27` | `2326.32` | `1471.76` | -271,729.33 USD | `-17.24%` | `20X Cross` |
| `1442` | `0x0b23...f37b` | `LONG` | 1,570,320.00 USD | `675.00` | `2238.15` | `2326.32` | `582.22` | 59,563.36 USD | `+3.79%` | `5X Cross` |
| `1469` | `0x0cac...6170` | `SHORT` | 1,541,041.25 USD | `662.50` | `2146.55` | `2326.32` | `2835.39` | -118,946.26 USD | `-7.72%` | `20X Cross` |
| `1472` | `0x0082...1ae3` | `LONG` | 1,536,348.00 USD | `660.00` | `2448.58` | `2326.32` | `2244.96` | -79,720.64 USD | `-5.19%` | `25X Cross` |
| `1505` | `0xffb2...5ed6` | `SHORT` | 1,490,679.88 USD | `640.77` | `2672.96` | `2326.32` | `2569.89` | 222,068.46 USD | `+14.90%` | `20X Cross` |
| `1520` | `0x0dd5...f6ee` | `LONG` | 1,467,631.54 USD | `630.86` | `2332.29` | `2326.32` | `912.89` | -3,718.36 USD | `-0.25%` | `5X Cross` |
| `1522` | `0x3bca...66f3` | `SHORT` | 1,466,411.35 USD | `630.04` | `2345.27` | `2326.32` | `14517.65` | 11,200.73 USD | `+0.76%` | `25X Cross` |
| `1533` | `0xfce0...f4c0` | `SHORT` | 1,451,616.08 USD | `623.60` | `3129.61` | `2326.32` | `2788.42` | 500,010.51 USD | `+34.45%` | `20X Cross` |
| `1557` | `0x7663...cb5a` | `SHORT` | 1,428,316.00 USD | `613.54` | `2342.35` | `2326.32` | `3636.44` | 8,804.49 USD | `+0.62%` | `3X Cross` |
| `1588` | `0xad02...eb65` | `LONG` | 1,397,943.52 USD | `600.62` | `2460.69` | `2326.32` | `1079.68` | -79,997.04 USD | `-5.72%` | `5X Cross` |
| `1590` | `0x638f...f5f0` | `LONG` | 1,396,860.00 USD | `600.00` | `4011.50` | `2326.32` | `34.59` | -1,010,043.53 USD | `-72.31%` | `25X Cross` |
| `1591` | `0x26e6...6b28` | `LONG` | 1,396,560.00 USD | `600.00` | `1769.78` | `2326.32` | `2005.48` | 334,688.47 USD | `+23.97%` | `20X Cross` |
| `1592` | `0x67c3...609d` | `SHORT` | 1,395,840.00 USD | `600.00` | `2386.55` | `2326.32` | `2560.77` | 36,091.89 USD | `+2.59%` | `25X Cross` |
| `1593` | `0x0deb...0bc5` | `LONG` | 1,395,780.00 USD | `600.00` | `2038.23` | `2326.32` | `1478.69` | 172,841.36 USD | `+12.38%` | `20X Cross` |
| `1594` | `0x0a84...6ddd` | `LONG` | 1,395,780.00 USD | `600.00` | `2222.36` | `2326.32` | `1774.80` | 62,361.66 USD | `+4.47%` | `25X Cross` |
| `1615` | `0x94b6...e5b3` | `SHORT` | 1,365,778.74 USD | `586.71` | `2377.90` | `2326.32` | `2486.69` | 29,359.50 USD | `+2.15%` | `25X Cross` |
| `1659` | `0xfb99...37f3` | `LONG` | 1,315,887.94 USD | `565.34` | `2362.35` | `2326.32` | `1210.07` | -19,648.41 USD | `-1.49%` | `3X Cross` |
| `1675` | `0x844b...7f42` | `SHORT` | 1,305,110.40 USD | `561.00` | `2026.17` | `2326.32` | `3013.17` | -168,426.99 USD | `-12.91%` | `25X Cross` |
| `1689` | `0xabe6...1d99` | `SHORT` | 1,294,099.31 USD | `556.00` | `2484.68` | `2326.32` | `2952.92` | 87,396.58 USD | `+6.75%` | `20X Cross` |
| `1739` | `0xad21...fb6a` | `LONG` | 1,236,968.43 USD | `531.87` | `2574.89` | `2326.32` | `1684.33` | -132,537.07 USD | `-10.71%` | `7X Cross` |
| `1773` | `0x8923...1bac` | `SHORT` | 1,203,744.60 USD | `517.18` | `2348.15` | `2326.32` | `3138.14` | 10,680.50 USD | `+0.89%` | `25X Cross` |
| `1791` | `0x0c7a...2f50` | `SHORT` | 1,184,555.49 USD | `509.25` | `2122.56` | `2326.32` | `4071.93` | -103,650.06 USD | `-8.75%` | `20X Cross` |
| `1813` | `0x89b2...9ca6` | `LONG` | 1,163,050.00 USD | `500.00` | `2484.03` | `2326.32` | `1954.21` | -78,969.35 USD | `-6.79%` | `25X Cross` |
| `1819` | `0x7298...7d6c` | `SHORT` | 1,159,492.31 USD | `498.15` | `3426.75` | `2326.32` | `5422.39` | 547,543.51 USD | `+47.22%` | `20X Cross` |
| `1841` | `0x404c...5f03` | `SHORT` | 1,140,465.07 USD | `489.79` | `2671.94` | `2326.32` | `4354.38` | 168,214.49 USD | `+14.75%` | `20X Cross` |
| `1842` | `0xc10f...23b3` | `LONG` | 1,139,936.00 USD | `490.00` | `2402.16` | `2326.32` | `2082.05` | -37,126.83 USD | `-3.26%` | `25X Cross` |
| `1849` | `0x321f...1c84` | `SHORT` | 1,135,319.03 USD | `488.02` | `2370.09` | `2326.32` | `3022.90` | 21,325.57 USD | `+1.88%` | `10X Cross` |
| `1907` | `0x82c6...fe42` | `LONG` | 1,076,607.50 USD | `462.50` | `2501.38` | `2326.32` | `2054.46` | -80,283.07 USD | `-7.46%` | `5X Isolated` |
| `1923` | `0x617e...0f97` | `SHORT` | 1,065,106.69 USD | `457.85` | `2205.60` | `2326.32` | `3691.47` | -55,262.86 USD | `-5.19%` | `10X Cross` |
| `1949` | `0xae55...2236` | `LONG` | 1,047,645.00 USD | `450.00` | `2510.21` | `2326.32` | `0.000000` | -81,952.50 USD | `-7.82%` | `25X Cross` |
| `1964` | `0xac26...a9c7` | `SHORT` | 1,038,977.25 USD | `446.28` | `2192.58` | `2326.32` | `8693.98` | -60,477.55 USD | `-5.82%` | `20X Cross` |
| `1965` | `0x53f8...ceff` | `LONG` | 1,037,261.86 USD | `445.60` | `2399.81` | `2326.32` | `0.000000` | -32,088.74 USD | `-3.09%` | `20X Cross` |
| `1981` | `0xd8a1...6687` | `LONG` | 1,027,049.91 USD | `441.53` | `2804.24` | `2326.32` | `2151.01` | -211,118.52 USD | `-20.56%` | `20X Cross` |
| `2000` | `0xfc66...ca06` | `LONG` | 1,016,316.69 USD | `436.86` | `2337.70` | `2326.32` | `0.000000` | -4,937.73 USD | `-0.49%` | `20X Cross` |
| `2003` | `0x248e...6be2` | `SHORT` | 1,015,231.89 USD | `436.40` | `2314.49` | `2326.32` | `4432.65` | -5,197.17 USD | `-0.51%` | `20X Cross` |
| `2011` | `0x80f2...0c3a` | `LONG` | 1,010,882.50 USD | `434.55` | `2564.17` | `2326.32` | `895.98` | -103,366.38 USD | `-10.23%` | `5X Cross` |
| `2016` | `0x823e...76c9` | `LONG` | 1,006,534.54 USD | `432.39` | `2339.20` | `2326.32` | `1988.63` | -4,903.26 USD | `-0.49%` | `25X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `ANNOUNCEMENT` | `INFO` | `4217.50` | 7,256.21 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 7.26K USD at 4217.5000 USD [API] | `2025-08-19 03:43:25` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`2401.93` (Vol: 17,300,000.00 USD, Dist: `+2.88%`) | Long MP=`2284.33` (Vol: 27,300,000.00 USD, Dist: `--2.16%`)
  * 48H Horizon: Short MP=`2401.93` (Vol: 25,300,000.00 USD, Dist: `+2.88%`) | Long MP=`2284.33` (Vol: 30,000,000.00 USD, Dist: `--2.16%`)
  * 3D Horizon: Short MP=`2401.93` (Vol: 26,700,000.00 USD, Dist: `+2.88%`) | Long MP=`2286.29` (Vol: 37,900,000.00 USD, Dist: `--2.08%`)
  * 7D Horizon: Short MP=`2402.93` (Vol: 47,100,000.00 USD, Dist: `+2.92%`) | Long MP=`2284.60` (Vol: 72,300,000.00 USD, Dist: `--2.15%`)
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
| `7D` | `Long Liquidation` | `2074.60` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 3,960,000.00 USD | 3,150,000.00 USD | 2,680,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 599,560.00 USD | 328,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2077.40` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 4,430,000.00 USD | 3,940,000.00 USD | 1,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2080.20` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 3,480,000.00 USD | 2,740,000.00 USD | 2,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2083.00` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 2,340,000.00 USD | 1,900,000.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 2,870,000.00 USD | 327,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2085.80` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 4,270,000.00 USD | 2,570,000.00 USD | 3,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2088.60` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 1,920,000.00 USD | 1,480,000.00 USD | 1,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2090.00` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 915,380.00 USD | 261,190.00 USD | 178,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2091.40` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 4,210,000.00 USD | 549,010.00 USD | 6,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2092.60` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 773,260.00 USD | 522,240.00 USD | 876,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2094.20` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 5,310,000.00 USD | 1,660,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 5,740,000.00 USD | 325,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2095.20` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 2,100,000.00 USD | 1,280,000.00 USD | 1,760,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2097.00` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 1,830,000.00 USD | 3,320,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2097.80` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 440,660.00 USD | 975,880.00 USD | 517,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2099.80` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 1,880,000.00 USD | 1,920,000.00 USD | 3,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2100.40` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 160,570.00 USD | 44,780.00 USD | 175,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2102.60` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 125,250.00 USD | 341,900.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2103.00` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 433,430.00 USD | 182,720.00 USD | 132,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 1,420,000.00 USD | 319,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2105.40` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 2,050,000.00 USD | 986,590.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2105.60` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 585,230.00 USD | 400,040.00 USD | 419,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2108.20` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 600,390.00 USD | 9,120.00 USD | 96,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2108.20` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 2,350,000.00 USD | 1,090,000.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2110.80` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 36,110.00 USD | 22,440.00 USD | 200,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2111.00` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 3,450,000.00 USD | 1,620,000.00 USD | 2,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2113.40` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 875,700.00 USD | 643,210.00 USD | 235,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2113.80` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 1,080,000.00 USD | 1,300,000.00 USD | 2,730,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 17,610,000.00 USD | 317,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2116.00` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 13,230.00 USD | 426,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2116.60` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 2,360,000.00 USD | 2,350,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2118.60` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 1,120,000.00 USD | 16,610.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2119.40` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 2,530,000.00 USD | 606,940.00 USD | 2,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2121.20` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 1,030,000.00 USD | 870,210.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2122.20` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 2,230,000.00 USD | 1,000,000.00 USD | 1,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2123.80` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 966,890.00 USD | 928,560.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2125.00` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 2,700,000.00 USD | 2,150,000.00 USD | 2,640,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 1,030,000.00 USD | 300,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2126.40` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 58,860.00 USD | 852,390.00 USD | 630,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2127.80` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 496,060.00 USD | 1,960,000.00 USD | 1,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2129.00` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 356,740.00 USD | 616,780.00 USD | 323,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2130.60` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 2,040,000.00 USD | 1,750,000.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2131.60` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 644,330.00 USD | 336,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2133.40` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 2,120,000.00 USD | 550,450.00 USD | 316,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2134.20` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 187,520.00 USD | 497,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 2,720,000.00 USD | 299,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2136.20` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 1,170,000.00 USD | 845,110.00 USD | 18,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2136.80` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 544,840.00 USD | 2,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2139.00` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 1,110,000.00 USD | 1,000,000.00 USD | 276,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2139.40` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 555,320.00 USD | 0.00 USD | 205,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2141.80` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 1,550,000.00 USD | 209,240.00 USD | 819,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2142.00` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 295,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2144.60` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 16,700.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2144.60` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 547,980.00 USD | 1,530,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 9,660,000.00 USD | 296,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2147.20` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 11,090.00 USD | 207,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2147.40` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 157,100.00 USD | 32,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2149.80` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 251,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2150.20` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 459,630.00 USD | 482,820.00 USD | 537,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2153.00` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 29,510.00 USD | 681,070.00 USD | 800,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 23,300,000.00 USD | 286,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2155.80` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 191,860.00 USD | 454,940.00 USD | 66,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2158.60` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 774,660.00 USD | 1,260,000.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2161.40` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 1,450,000.00 USD | 804,860.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2164.20` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 36,870.00 USD | 329,690.00 USD | 409,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 857,510.00 USD | 263,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2167.00` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 25,540.00 USD | 0.00 USD | 84,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2169.80` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 1,700,000.00 USD | 726,240.00 USD | 794,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2172.60` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 479,540.00 USD | 1,150,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 108,630,000.00 USD | 262,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2185.00` | 111,630,000.00 USD | 154,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2195.00` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 141,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 1,510,000.00 USD | 42,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2197.80` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 2,440,000.00 USD | 3,270,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2199.20` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 0.00 USD | 80,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2200.60` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 3,120,000.00 USD | 3,140,000.00 USD | 3,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2201.80` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 284,470.00 USD | 217,490.00 USD | 144,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2203.40` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 3,280,000.00 USD | 624,500.00 USD | 2,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2204.40` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 1,050,000.00 USD | 207,110.00 USD | 792,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 1,240,000.00 USD | 40,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2206.20` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 6,770,000.00 USD | 4,010,000.00 USD | 4,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2207.00` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 2,070,000.00 USD | 2,330,000.00 USD | 1,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2209.00` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 9,190,000.00 USD | 7,030,000.00 USD | 4,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2209.60` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 1,770,000.00 USD | 610,890.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2211.80` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 8,790,000.00 USD | 8,110,000.00 USD | 6,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2212.20` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 2,580,000.00 USD | 1,580,000.00 USD | 1,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2214.60` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 14,850,000.00 USD | 14,220,000.00 USD | 10,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2214.80` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 6,410,000.00 USD | 4,340,000.00 USD | 5,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 1,970,000.00 USD | 39,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2217.40` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 4,250,000.00 USD | 5,300,000.00 USD | 1,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2217.40` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 13,750,000.00 USD | 10,950,000.00 USD | 7,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2220.00` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 3,690,000.00 USD | 3,840,000.00 USD | 453,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2220.20` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 12,830,000.00 USD | 7,840,000.00 USD | 3,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2222.60` | 992,510,000.00 USD | 992,510,000.00 USD | 5,420,000.00 USD | 3,840,000.00 USD | 2,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2223.00` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 6,930,000.00 USD | 5,300,000.00 USD | 11,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2225.00` | 2,130,000.00 USD | 37,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2225.20` | 980,290,000.00 USD | 980,290,000.00 USD | 1,930,000.00 USD | 4,150,000.00 USD | 2,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2225.80` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 11,900,000.00 USD | 12,610,000.00 USD | 6,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2227.80` | 971,770,000.00 USD | 971,770,000.00 USD | 5,720,000.00 USD | 2,770,000.00 USD | 801,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2228.60` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 7,530,000.00 USD | 5,580,000.00 USD | 9,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2230.40` | 962,470,000.00 USD | 962,470,000.00 USD | 3,880,000.00 USD | 2,030,000.00 USD | 2,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2231.40` | 2,080,000,000.00 USD | 2,080,000,000.00 USD | 10,960,000.00 USD | 2,990,000.00 USD | 14,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2233.00` | 954,450,000.00 USD | 954,450,000.00 USD | 5,430,000.00 USD | 2,440,000.00 USD | 3,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2234.20` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 17,000,000.00 USD | 12,020,000.00 USD | 7,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2235.00` | 671,070.00 USD | 35,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2235.60` | 943,070,000.00 USD | 943,070,000.00 USD | 3,880,000.00 USD | 4,850,000.00 USD | 5,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2237.00` | 2,020,000,000.00 USD | 2,020,000,000.00 USD | 6,950,000.00 USD | 11,130,000.00 USD | 4,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2238.20` | 928,850,000.00 USD | 928,850,000.00 USD | 1,800,000.00 USD | 2,210,000.00 USD | 844,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2239.80` | 2,000,000,000.00 USD | 2,000,000,000.00 USD | 7,410,000.00 USD | 6,730,000.00 USD | 9,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2240.80` | 924,000,000.00 USD | 924,000,000.00 USD | 634,700.00 USD | 542,280.00 USD | 601,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2242.60` | 1,970,000,000.00 USD | 1,970,000,000.00 USD | 7,790,000.00 USD | 2,710,000.00 USD | 4,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2243.40` | 922,220,000.00 USD | 922,220,000.00 USD | 1,210,000.00 USD | 881,310.00 USD | 555,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2245.00` | 4,720,000.00 USD | 34,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2245.40` | 1,960,000,000.00 USD | 1,960,000,000.00 USD | 12,040,000.00 USD | 12,530,000.00 USD | 10,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2246.00` | 919,570,000.00 USD | 919,570,000.00 USD | 2,560,000.00 USD | 1,790,000.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2248.20` | 1,920,000,000.00 USD | 1,920,000,000.00 USD | 13,950,000.00 USD | 5,870,000.00 USD | 11,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2248.60` | 913,660,000.00 USD | 913,660,000.00 USD | 4,610,000.00 USD | 601,150.00 USD | 2,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2251.00` | 1,890,000,000.00 USD | 1,890,000,000.00 USD | 12,710,000.00 USD | 11,300,000.00 USD | 8,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2251.20` | 906,380,000.00 USD | 906,380,000.00 USD | 304,760.00 USD | 1,060,000.00 USD | 683,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2253.80` | 904,330,000.00 USD | 904,330,000.00 USD | 8,560,000.00 USD | 6,780,000.00 USD | 6,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2253.80` | 1,860,000,000.00 USD | 1,860,000,000.00 USD | 25,660,000.00 USD | 20,190,000.00 USD | 19,820,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2255.00` | 11,410,000.00 USD | 30,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2256.40` | 882,050,000.00 USD | 882,050,000.00 USD | 3,260,000.00 USD | 2,980,000.00 USD | 3,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2256.60` | 1,790,000,000.00 USD | 1,790,000,000.00 USD | 29,170,000.00 USD | 24,230,000.00 USD | 17,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2259.00` | 871,930,000.00 USD | 871,930,000.00 USD | 8,870,000.00 USD | 4,580,000.00 USD | 4,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2259.40` | 1,720,000,000.00 USD | 1,720,000,000.00 USD | 25,970,000.00 USD | 15,650,000.00 USD | 27,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2261.60` | 853,870,000.00 USD | 853,870,000.00 USD | 14,160,000.00 USD | 11,590,000.00 USD | 15,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2262.20` | 1,650,000,000.00 USD | 1,650,000,000.00 USD | 46,580,000.00 USD | 30,720,000.00 USD | 19,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2264.20` | 812,710,000.00 USD | 812,710,000.00 USD | 13,110,000.00 USD | 12,080,000.00 USD | 6,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2265.00` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 29,070,000.00 USD | 25,860,000.00 USD | 16,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2265.00` | 5,260,000.00 USD | 18,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2266.80` | 781,320,000.00 USD | 781,320,000.00 USD | 11,660,000.00 USD | 11,820,000.00 USD | 3,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2267.80` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 41,280,000.00 USD | 43,110,000.00 USD | 32,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2269.40` | 753,980,000.00 USD | 753,980,000.00 USD | 13,850,000.00 USD | 11,370,000.00 USD | 8,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2270.60` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 43,030,000.00 USD | 30,540,000.00 USD | 36,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2272.00` | 720,660,000.00 USD | 720,660,000.00 USD | 12,250,000.00 USD | 12,340,000.00 USD | 9,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2273.40` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 27,330,000.00 USD | 19,600,000.00 USD | 20,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2274.60` | 686,840,000.00 USD | 686,840,000.00 USD | 10,260,000.00 USD | 6,240,000.00 USD | 5,490,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2275.00` | 3,330,000.00 USD | 13,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2276.20` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 55,750,000.00 USD | 46,480,000.00 USD | 59,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2277.20` | 664,840,000.00 USD | 664,840,000.00 USD | 18,320,000.00 USD | 14,850,000.00 USD | 15,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2279.00` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 71,690,000.00 USD | 30,780,000.00 USD | 36,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2279.80` | 615,950,000.00 USD | 615,950,000.00 USD | 19,100,000.00 USD | 14,830,000.00 USD | 11,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2281.80` | 889,350,000.00 USD | 889,350,000.00 USD | 64,270,000.00 USD | 63,850,000.00 USD | 39,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2282.40` | 570,430,000.00 USD | 570,430,000.00 USD | 26,760,000.00 USD | 17,540,000.00 USD | 21,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2284.60` | 721,740,000.00 USD | 721,740,000.00 USD | 84,980,000.00 USD | 71,990,000.00 USD | 47,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2285.00` | 505,060,000.00 USD | 505,060,000.00 USD | 24,940,000.00 USD | 23,280,000.00 USD | 19,680,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2285.00` | 5,830,000.00 USD | 10,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2287.40` | 517,180,000.00 USD | 517,180,000.00 USD | 57,800,000.00 USD | 54,380,000.00 USD | 45,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2287.60` | 437,160,000.00 USD | 437,160,000.00 USD | 17,430,000.00 USD | 15,630,000.00 USD | 6,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2290.20` | 397,690,000.00 USD | 397,690,000.00 USD | 15,700,000.00 USD | 15,930,000.00 USD | 3,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2290.20` | 359,240,000.00 USD | 359,240,000.00 USD | 45,650,000.00 USD | 33,150,000.00 USD | 39,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2292.80` | 362,960,000.00 USD | 362,960,000.00 USD | 21,580,000.00 USD | 18,140,000.00 USD | 15,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2293.00` | 241,410,000.00 USD | 241,410,000.00 USD | 33,030,000.00 USD | 15,200,000.00 USD | 23,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2295.00` | 1,910,000.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2295.40` | 308,240,000.00 USD | 308,240,000.00 USD | 20,210,000.00 USD | 18,280,000.00 USD | 9,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2295.80` | 170,040,000.00 USD | 170,040,000.00 USD | 17,510,000.00 USD | 9,480,000.00 USD | 6,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2298.00` | 260,260,000.00 USD | 260,260,000.00 USD | 11,100,000.00 USD | 6,170,000.00 USD | 1,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2298.60` | 136,260,000.00 USD | 136,260,000.00 USD | 2,760,000.00 USD | 4,450,000.00 USD | 358,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2300.60` | 241,570,000.00 USD | 241,570,000.00 USD | 18,640,000.00 USD | 11,200,000.00 USD | 13,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2301.40` | 128,690,000.00 USD | 128,690,000.00 USD | 11,120,000.00 USD | 2,120,000.00 USD | 7,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2303.20` | 198,430,000.00 USD | 198,430,000.00 USD | 26,500,000.00 USD | 16,170,000.00 USD | 16,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2304.20` | 107,910,000.00 USD | 107,910,000.00 USD | 32,960,000.00 USD | 16,920,000.00 USD | 13,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2305.00` | 1,080,000.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2305.80` | 139,180,000.00 USD | 139,180,000.00 USD | 9,950,000.00 USD | 7,080,000.00 USD | 18,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2307.00` | 44,760,000.00 USD | 44,760,000.00 USD | 0.00 USD | 3,740,000.00 USD | 10,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2308.40` | 103,880,000.00 USD | 103,880,000.00 USD | 1,030,000.00 USD | 2,010,000.00 USD | 2,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2309.80` | 30,130,000.00 USD | 30,130,000.00 USD | 282,530.00 USD | 300,580.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2311.00` | 98,300,000.00 USD | 98,300,000.00 USD | 6,780,000.00 USD | 5,300,000.00 USD | 6,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2312.60` | 28,040,000.00 USD | 28,040,000.00 USD | 2,470,000.00 USD | 640,510.00 USD | 2,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2313.60` | 79,360,000.00 USD | 79,360,000.00 USD | 6,200,000.00 USD | 5,150,000.00 USD | 3,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2315.00` | 657,320.00 USD | 657,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2315.40` | 22,310,000.00 USD | 22,310,000.00 USD | 5,830,000.00 USD | 4,100,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2316.20` | 64,880,000.00 USD | 64,880,000.00 USD | 10,440,000.00 USD | 8,800,000.00 USD | 5,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2318.20` | 12,380,000.00 USD | 12,380,000.00 USD | 0.00 USD | 3,010,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2318.80` | 39,800,000.00 USD | 39,800,000.00 USD | 11,680,000.00 USD | 4,080,000.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2321.00` | 9,370,000.00 USD | 9,370,000.00 USD | 947,800.00 USD | 2,960,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2321.40` | 21,780,000.00 USD | 21,780,000.00 USD | 255,100.00 USD | 2,970,000.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2323.80` | 5,460,000.00 USD | 5,460,000.00 USD | 3,130,000.00 USD | 2,210,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2324.00` | 16,840,000.00 USD | 16,840,000.00 USD | 8,620,000.00 USD | 2,890,000.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2325.00` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2326.60` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 3,040,000.00 USD | 66,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2326.60` | 126,530.00 USD | 126,530.00 USD | 0.00 USD | 0.00 USD | 126,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2329.20` | 3,540,000.00 USD | 3,540,000.00 USD | 1,890,000.00 USD | 1,370,000.00 USD | 287,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2329.40` | 8,740,000.00 USD | 8,740,000.00 USD | 3,860,000.00 USD | 0.00 USD | 4,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2331.80` | 16,860,000.00 USD | 16,860,000.00 USD | 13,200,000.00 USD | 0.00 USD | 107,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2332.20` | 40,790,000.00 USD | 40,790,000.00 USD | 29,230,000.00 USD | 0.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2334.40` | 41,550,000.00 USD | 41,550,000.00 USD | 11,210,000.00 USD | 12,110,000.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2335.00` | 81,690,000.00 USD | 81,690,000.00 USD | 13,560,000.00 USD | 18,420,000.00 USD | 8,930,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2335.00` | 1,060.00 USD | 1,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2337.00` | 44,440,000.00 USD | 44,440,000.00 USD | 1,460,000.00 USD | 0.00 USD | 1,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2337.80` | 127,650,000.00 USD | 127,650,000.00 USD | 14,090,000.00 USD | 18,310,000.00 USD | 13,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2340.60` | 146,580,000.00 USD | 146,580,000.00 USD | 0.00 USD | 15,560,000.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2343.40` | 153,750,000.00 USD | 153,750,000.00 USD | 0.00 USD | 0.00 USD | 7,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2344.80` | 57,440,000.00 USD | 57,440,000.00 USD | 963,370.00 USD | 1,960,000.00 USD | 10,070,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2345.00` | 5,140.00 USD | 662,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2346.20` | 171,170,000.00 USD | 171,170,000.00 USD | 0.00 USD | 7,920,000.00 USD | 9,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2347.40` | 58,220,000.00 USD | 58,220,000.00 USD | 166,240.00 USD | 0.00 USD | 615,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2349.00` | 199,590,000.00 USD | 199,590,000.00 USD | 495,290.00 USD | 11,840,000.00 USD | 16,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2350.00` | 90,680,000.00 USD | 90,680,000.00 USD | 24,070,000.00 USD | 2,510,000.00 USD | 5,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2351.80` | 213,610,000.00 USD | 213,610,000.00 USD | 572,980.00 USD | 13,100,000.00 USD | 351,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2352.60` | 94,570,000.00 USD | 94,570,000.00 USD | 2,620,000.00 USD | 121,980.00 USD | 1,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2354.60` | 258,400,000.00 USD | 258,400,000.00 USD | 9,800,000.00 USD | 34,750,000.00 USD | 237,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 73,520.00 USD | 735,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2355.20` | 113,540,000.00 USD | 113,540,000.00 USD | 628,820.00 USD | 17,100,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2357.40` | 269,350,000.00 USD | 269,350,000.00 USD | 5,040,000.00 USD | 5,920,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2357.80` | 119,390,000.00 USD | 119,390,000.00 USD | 1,400,000.00 USD | 2,000,000.00 USD | 2,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2360.20` | 271,790,000.00 USD | 271,790,000.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2360.40` | 124,310,000.00 USD | 124,310,000.00 USD | 1,730,000.00 USD | 1,830,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2363.00` | 138,390,000.00 USD | 138,390,000.00 USD | 4,020,000.00 USD | 7,640,000.00 USD | 2,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2363.00` | 274,190,000.00 USD | 274,190,000.00 USD | 715,490.00 USD | 0.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 2,900.00 USD | 738,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2365.60` | 141,900,000.00 USD | 141,900,000.00 USD | 1,870,000.00 USD | 0.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2365.80` | 282,190,000.00 USD | 282,190,000.00 USD | 6,340,000.00 USD | 0.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2368.20` | 150,850,000.00 USD | 150,850,000.00 USD | 6,250,000.00 USD | 2,170,000.00 USD | 532,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2368.60` | 292,670,000.00 USD | 292,670,000.00 USD | 9,590,000.00 USD | 475,460.00 USD | 404,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2370.80` | 189,500,000.00 USD | 189,500,000.00 USD | 16,400,000.00 USD | 13,050,000.00 USD | 9,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2371.40` | 358,480,000.00 USD | 358,480,000.00 USD | 18,630,000.00 USD | 0.00 USD | 47,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2373.40` | 211,160,000.00 USD | 211,160,000.00 USD | 14,040,000.00 USD | 1,720,000.00 USD | 5,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2374.20` | 376,990,000.00 USD | 376,990,000.00 USD | 13,960,000.00 USD | 0.00 USD | 4,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 16,680.00 USD | 755,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2376.00` | 234,470,000.00 USD | 234,470,000.00 USD | 11,540,000.00 USD | 3,310,000.00 USD | 8,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2377.00` | 417,370,000.00 USD | 417,370,000.00 USD | 12,140,000.00 USD | 6,190,000.00 USD | 22,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2378.60` | 261,610,000.00 USD | 261,610,000.00 USD | 6,450,000.00 USD | 11,410,000.00 USD | 9,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2379.80` | 445,570,000.00 USD | 445,570,000.00 USD | 7,180,000.00 USD | 2,330,000.00 USD | 18,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2381.20` | 310,740,000.00 USD | 310,740,000.00 USD | 16,330,000.00 USD | 12,790,000.00 USD | 20,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2382.60` | 486,960,000.00 USD | 486,960,000.00 USD | 8,620,000.00 USD | 12,380,000.00 USD | 20,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2383.80` | 355,250,000.00 USD | 355,250,000.00 USD | 19,270,000.00 USD | 15,610,000.00 USD | 9,630,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 3,320,000.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2385.40` | 583,310,000.00 USD | 583,310,000.00 USD | 15,530,000.00 USD | 30,320,000.00 USD | 50,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2386.40` | 394,330,000.00 USD | 394,330,000.00 USD | 13,990,000.00 USD | 13,800,000.00 USD | 11,280,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2388.20` | 660,270,000.00 USD | 660,270,000.00 USD | 4,500,000.00 USD | 34,050,000.00 USD | 38,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2389.00` | 421,440,000.00 USD | 421,440,000.00 USD | 12,210,000.00 USD | 8,980,000.00 USD | 5,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2391.00` | 756,660,000.00 USD | 756,660,000.00 USD | 5,620,000.00 USD | 45,790,000.00 USD | 44,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2391.60` | 446,050,000.00 USD | 446,050,000.00 USD | 4,230,000.00 USD | 11,920,000.00 USD | 8,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2393.80` | 868,970,000.00 USD | 868,970,000.00 USD | 48,290,000.00 USD | 27,870,000.00 USD | 36,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2394.20` | 468,780,000.00 USD | 468,780,000.00 USD | 9,780,000.00 USD | 10,200,000.00 USD | 2,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 91,230.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2396.60` | 943,260,000.00 USD | 943,260,000.00 USD | 26,490,000.00 USD | 29,530,000.00 USD | 18,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2396.80` | 481,130,000.00 USD | 481,130,000.00 USD | 2,300,000.00 USD | 6,100,000.00 USD | 3,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2399.40` | 521,040,000.00 USD | 521,040,000.00 USD | 17,090,000.00 USD | 9,220,000.00 USD | 13,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2399.40` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 49,120,000.00 USD | 29,120,000.00 USD | 19,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2402.00` | 544,940,000.00 USD | 544,940,000.00 USD | 8,130,000.00 USD | 9,740,000.00 USD | 6,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2402.20` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 45,210,000.00 USD | 27,170,000.00 USD | 31,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2404.60` | 579,290,000.00 USD | 579,290,000.00 USD | 13,540,000.00 USD | 10,180,000.00 USD | 10,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2405.00` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 35,270,000.00 USD | 26,450,000.00 USD | 17,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 13,290,000.00 USD | 17,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2407.20` | 609,380,000.00 USD | 609,380,000.00 USD | 13,020,000.00 USD | 10,550,000.00 USD | 6,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2407.80` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 26,280,000.00 USD | 26,510,000.00 USD | 16,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2409.80` | 634,730,000.00 USD | 634,730,000.00 USD | 7,750,000.00 USD | 8,870,000.00 USD | 8,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2410.60` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 23,140,000.00 USD | 26,640,000.00 USD | 27,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2412.40` | 658,690,000.00 USD | 658,690,000.00 USD | 11,210,000.00 USD | 7,480,000.00 USD | 5,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2413.40` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 15,370,000.00 USD | 14,870,000.00 USD | 9,740,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2415.00` | 671,390,000.00 USD | 671,390,000.00 USD | 3,530,000.00 USD | 6,090,000.00 USD | 3,070,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 362,060.00 USD | 17,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2416.20` | 1,490,000,000.00 USD | 1,490,000,000.00 USD | 25,850,000.00 USD | 16,790,000.00 USD | 32,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2417.60` | 684,160,000.00 USD | 684,160,000.00 USD | 5,030,000.00 USD | 4,910,000.00 USD | 2,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2419.00` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 30,180,000.00 USD | 17,120,000.00 USD | 11,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2420.20` | 699,110,000.00 USD | 699,110,000.00 USD | 6,880,000.00 USD | 4,370,000.00 USD | 3,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2421.80` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 21,830,000.00 USD | 26,230,000.00 USD | 20,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2422.80` | 715,140,000.00 USD | 715,140,000.00 USD | 4,760,000.00 USD | 4,990,000.00 USD | 6,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.60` | 1,700,000,000.00 USD | 1,700,000,000.00 USD | 25,990,000.00 USD | 31,850,000.00 USD | 32,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 890,120.00 USD | 18,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2425.40` | 719,540,000.00 USD | 719,540,000.00 USD | 1,130,000.00 USD | 2,650,000.00 USD | 629,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2427.40` | 1,770,000,000.00 USD | 1,770,000,000.00 USD | 25,000,000.00 USD | 18,790,000.00 USD | 24,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2428.00` | 722,610,000.00 USD | 722,610,000.00 USD | 1,930,000.00 USD | 542,280.00 USD | 601,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2430.20` | 1,800,000,000.00 USD | 1,800,000,000.00 USD | 6,090,000.00 USD | 16,890,000.00 USD | 6,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2430.60` | 725,240,000.00 USD | 725,240,000.00 USD | 1,100,000.00 USD | 964,820.00 USD | 571,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2433.00` | 1,830,000,000.00 USD | 1,830,000,000.00 USD | 15,680,000.00 USD | 12,450,000.00 USD | 5,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2433.20` | 731,190,000.00 USD | 731,190,000.00 USD | 2,160,000.00 USD | 1,540,000.00 USD | 2,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 7,770,000.00 USD | 26,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2435.80` | 735,810,000.00 USD | 735,810,000.00 USD | 3,600,000.00 USD | 452,500.00 USD | 564,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2435.80` | 1,880,000,000.00 USD | 1,880,000,000.00 USD | 20,300,000.00 USD | 12,070,000.00 USD | 17,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2438.40` | 737,180,000.00 USD | 737,180,000.00 USD | 214,470.00 USD | 664,070.00 USD | 492,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2438.60` | 1,940,000,000.00 USD | 1,940,000,000.00 USD | 20,380,000.00 USD | 23,980,000.00 USD | 15,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2441.00` | 742,390,000.00 USD | 742,390,000.00 USD | 2,420,000.00 USD | 2,020,000.00 USD | 767,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2441.40` | 1,980,000,000.00 USD | 1,980,000,000.00 USD | 13,390,000.00 USD | 6,350,000.00 USD | 13,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2443.60` | 744,370,000.00 USD | 744,370,000.00 USD | 73,920.00 USD | 566,480.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2444.20` | 2,010,000,000.00 USD | 2,010,000,000.00 USD | 9,430,000.00 USD | 15,220,000.00 USD | 11,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 149,300.00 USD | 26,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2446.20` | 748,600,000.00 USD | 748,600,000.00 USD | 2,310,000.00 USD | 675,040.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2447.00` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 11,560,000.00 USD | 5,380,000.00 USD | 18,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2448.80` | 754,830,000.00 USD | 754,830,000.00 USD | 2,120,000.00 USD | 1,520,000.00 USD | 2,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2449.80` | 2,090,000,000.00 USD | 2,090,000,000.00 USD | 16,990,000.00 USD | 11,970,000.00 USD | 11,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2451.40` | 765,670,000.00 USD | 765,670,000.00 USD | 3,330,000.00 USD | 3,450,000.00 USD | 4,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2452.60` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 6,280,000.00 USD | 7,310,000.00 USD | 6,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2454.00` | 777,470,000.00 USD | 777,470,000.00 USD | 5,050,000.00 USD | 3,030,000.00 USD | 3,720,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 288,140.00 USD | 26,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2455.40` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 8,340,000.00 USD | 10,630,000.00 USD | 5,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2456.60` | 783,760,000.00 USD | 783,760,000.00 USD | 1,340,000.00 USD | 3,200,000.00 USD | 1,750,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2458.20` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 9,800,000.00 USD | 7,130,000.00 USD | 11,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2459.20` | 789,680,000.00 USD | 789,680,000.00 USD | 2,870,000.00 USD | 1,980,000.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2461.00` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 6,890,000.00 USD | 10,680,000.00 USD | 9,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2461.80` | 792,240,000.00 USD | 792,240,000.00 USD | 174,920.00 USD | 490,260.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2463.80` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 10,390,000.00 USD | 8,820,000.00 USD | 5,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2464.40` | 794,940,000.00 USD | 794,940,000.00 USD | 352,200.00 USD | 2,340,000.00 USD | 5,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 180,420.00 USD | 27,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2466.60` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 4,840,000.00 USD | 2,680,000.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2467.00` | 796,240,000.00 USD | 796,240,000.00 USD | 468,790.00 USD | 833,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2469.40` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 2,470,000.00 USD | 2,980,000.00 USD | 408,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2469.60` | 798,920,000.00 USD | 798,920,000.00 USD | 0.00 USD | 1,510,000.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2472.20` | 800,310,000.00 USD | 800,310,000.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2472.20` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 3,060,000.00 USD | 2,760,000.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2474.80` | 800,540,000.00 USD | 800,540,000.00 USD | 0.00 USD | 232,740.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2475.00` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 5,400,000.00 USD | 866,790.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 32,880.00 USD | 27,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2477.40` | 801,330,000.00 USD | 801,330,000.00 USD | 738,780.00 USD | 41,760.00 USD | 7,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2477.80` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 1,840,000.00 USD | 5,290,000.00 USD | 505,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2480.00` | 801,880,000.00 USD | 801,880,000.00 USD | 0.00 USD | 27,720.00 USD | 518,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2480.60` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 1,070,000.00 USD | 350,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2482.60` | 802,510,000.00 USD | 802,510,000.00 USD | 628,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2483.40` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 1,310,000.00 USD | 1,290,000.00 USD | 2,070,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 589,540.00 USD | 27,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2486.20` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 586,480.00 USD | 1,240,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2489.00` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 1,020,000.00 USD | 857,130.00 USD | 2,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2491.80` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 2,400,000.00 USD | 3,310,000.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2494.60` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 1,600,000.00 USD | 1,950,000.00 USD | 6,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 2,340,000.00 USD | 30,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2497.40` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 3,640,000.00 USD | 3,570,000.00 USD | 4,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2500.20` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 1,160,000.00 USD | 2,430,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2503.00` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 111,800.00 USD | 1,430,000.00 USD | 170,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 244,330.00 USD | 30,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2505.80` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 4,240,000.00 USD | 2,320,000.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2508.60` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 714,660.00 USD | 1,270,000.00 USD | 629,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2511.40` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 1,900,000.00 USD | 3,230,000.00 USD | 2,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2514.20` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 776,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 118,730.00 USD | 30,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2517.00` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 97,050.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2519.80` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2521.60` | 802,740,000.00 USD | 802,740,000.00 USD | 80,610.00 USD | 61,830.00 USD | 90,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2522.60` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 1,050,000.00 USD | 0.00 USD | 945,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2524.20` | 803,190,000.00 USD | 803,190,000.00 USD | 421,540.00 USD | 0.00 USD | 30,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 1,080,000.00 USD | 31,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2525.40` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 307,040.00 USD | 224,130.00 USD | 200,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2526.80` | 803,270,000.00 USD | 803,270,000.00 USD | 0.00 USD | 57,450.00 USD | 23,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2528.20` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 1,580,000.00 USD | 1,690,000.00 USD | 727,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2529.40` | 804,960,000.00 USD | 804,960,000.00 USD | 583,810.00 USD | 645,910.00 USD | 464,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2531.00` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 2,080,000.00 USD | 1,480,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2532.00` | 805,720,000.00 USD | 805,720,000.00 USD | 752,010.00 USD | 0.00 USD | 7,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2533.80` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 2,750,000.00 USD | 1,730,000.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2534.60` | 806,320,000.00 USD | 806,320,000.00 USD | 54,030.00 USD | 41,990.00 USD | 499,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2535.00` | 1,510,000.00 USD | 33,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2536.60` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 3,590,000.00 USD | 2,850,000.00 USD | 2,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2537.20` | 811,050,000.00 USD | 811,050,000.00 USD | 2,220,000.00 USD | 901,140.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2539.40` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 2,620,000.00 USD | 2,580,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2539.80` | 813,640,000.00 USD | 813,640,000.00 USD | 1,140,000.00 USD | 820,030.00 USD | 632,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2542.20` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 3,400,000.00 USD | 2,620,000.00 USD | 2,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2542.40` | 816,090,000.00 USD | 816,090,000.00 USD | 1,100,000.00 USD | 1,330,000.00 USD | 19,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2545.00` | 816,650,000.00 USD | 816,650,000.00 USD | 227,010.00 USD | 322,670.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2545.00` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 2,170,000.00 USD | 1,830,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2545.00` | 6,150,000.00 USD | 39,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2547.60` | 820,270,000.00 USD | 820,270,000.00 USD | 1,540,000.00 USD | 1,330,000.00 USD | 745,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2547.80` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 2,380,000.00 USD | 938,680.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2550.20` | 823,460,000.00 USD | 823,460,000.00 USD | 1,260,000.00 USD | 1,450,000.00 USD | 483,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2550.60` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 2,920,000.00 USD | 2,720,000.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2552.80` | 824,620,000.00 USD | 824,620,000.00 USD | 781,250.00 USD | 149,300.00 USD | 225,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2553.40` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 2,590,000.00 USD | 756,730.00 USD | 2,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2555.00` | 943,640.00 USD | 40,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2555.40` | 825,880,000.00 USD | 825,880,000.00 USD | 791,770.00 USD | 203,910.00 USD | 266,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2556.20` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 2,760,000.00 USD | 255,750.00 USD | 4,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2558.00` | 827,870,000.00 USD | 827,870,000.00 USD | 758,880.00 USD | 415,210.00 USD | 808,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2559.00` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 4,380,000.00 USD | 1,640,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2560.60` | 831,960,000.00 USD | 831,960,000.00 USD | 1,840,000.00 USD | 1,090,000.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2561.80` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 2,260,000.00 USD | 1,960,000.00 USD | 802,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2563.20` | 834,190,000.00 USD | 834,190,000.00 USD | 440,660.00 USD | 802,390.00 USD | 984,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2564.60` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 1,800,000.00 USD | 2,100,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2565.00` | 2,030,000.00 USD | 42,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2565.80` | 834,750,000.00 USD | 834,750,000.00 USD | 160,570.00 USD | 403,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2567.40` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 575,630.00 USD | 1,240,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2568.40` | 835,100,000.00 USD | 835,100,000.00 USD | 46,810.00 USD | 0.00 USD | 304,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2570.20` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 125,250.00 USD | 290,680.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2571.00` | 835,710,000.00 USD | 835,710,000.00 USD | 422,490.00 USD | 182,720.00 USD | 3,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2573.00` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2573.60` | 837,080,000.00 USD | 837,080,000.00 USD | 549,360.00 USD | 400,040.00 USD | 419,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2575.00` | 11,890,000.00 USD | 54,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2575.80` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 2,180,000.00 USD | 344,620.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2576.20` | 837,720,000.00 USD | 837,720,000.00 USD | 539,390.00 USD | 0.00 USD | 96,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2578.60` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 797,100.00 USD | 1,500,000.00 USD | 1,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2578.80` | 837,820,000.00 USD | 837,820,000.00 USD | 61,010.00 USD | 31,550.00 USD | 8,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2581.40` | 839,140,000.00 USD | 839,140,000.00 USD | 490,860.00 USD | 416,230.00 USD | 413,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2581.40` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 3,860,000.00 USD | 895,740.00 USD | 3,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2584.00` | 839,970,000.00 USD | 839,970,000.00 USD | 420,950.00 USD | 226,990.00 USD | 182,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2584.20` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 88,840.00 USD | 1,820,000.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2585.00` | 36,040,000.00 USD | 90,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2586.60` | 840,580,000.00 USD | 840,580,000.00 USD | 0.00 USD | 13,230.00 USD | 596,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2587.00` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 2,360,000.00 USD | 1,800,000.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2589.20` | 842,330,000.00 USD | 842,330,000.00 USD | 1,120,000.00 USD | 16,610.00 USD | 619,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2589.80` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 2,470,000.00 USD | 287,400.00 USD | 2,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2591.80` | 844,730,000.00 USD | 844,730,000.00 USD | 818,160.00 USD | 416,510.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2592.60` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 2,300,000.00 USD | 1,280,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2594.40` | 846,430,000.00 USD | 846,430,000.00 USD | 488,970.00 USD | 525,250.00 USD | 684,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2595.00` | 332,910.00 USD | 90,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2595.10` | 847,940,000.00 USD | 847,940,000.00 USD | 526,760.00 USD | 693,240.00 USD | 291,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2595.40` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 413,920.00 USD | 569,790.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2598.20` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 2,280,000.00 USD | 1,910,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2601.00` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 931,390.00 USD | 1,670,000.00 USD | 955,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2603.80` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 1,600,000.00 USD | 1,580,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2605.00` | 533,700.00 USD | 90,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2606.60` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 1,480,000.00 USD | 463,200.00 USD | 312,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2609.40` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 1,090,000.00 USD | 489,790.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2612.20` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 770,330.00 USD | 608,060.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2615.00` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 1,060,000.00 USD | 1,000,000.00 USD | 635,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2615.00` | 1,190,000.00 USD | 92,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2617.80` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 1,550,000.00 USD | 209,240.00 USD | 434,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2620.60` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 465,960.00 USD | 1,530,000.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `7D` | `2074.60` | 2,510,000,000.00 USD | 0.00 USD | 2,510,000,000.00 USD | 3,960,000.00 USD | 3,150,000.00 USD | 2,680,000.00 USD |
| `7D` | `2077.40` | 2,500,000,000.00 USD | 0.00 USD | 2,500,000,000.00 USD | 4,430,000.00 USD | 3,940,000.00 USD | 1,980,000.00 USD |
| `7D` | `2080.20` | 2,490,000,000.00 USD | 0.00 USD | 2,490,000,000.00 USD | 3,480,000.00 USD | 2,740,000.00 USD | 2,540,000.00 USD |
| `7D` | `2083.00` | 2,480,000,000.00 USD | 0.00 USD | 2,480,000,000.00 USD | 2,340,000.00 USD | 1,900,000.00 USD | 1,890,000.00 USD |
| `7D` | `2085.80` | 2,480,000,000.00 USD | 0.00 USD | 2,480,000,000.00 USD | 4,270,000.00 USD | 2,570,000.00 USD | 3,130,000.00 USD |
| `7D` | `2088.60` | 2,470,000,000.00 USD | 0.00 USD | 2,470,000,000.00 USD | 1,920,000.00 USD | 1,480,000.00 USD | 1,470,000.00 USD |
| `1D` | `2090.00` | 1,080,000,000.00 USD | 0.00 USD | 1,080,000,000.00 USD | 915,380.00 USD | 261,190.00 USD | 178,100.00 USD |
| `7D` | `2091.40` | 2,460,000,000.00 USD | 0.00 USD | 2,460,000,000.00 USD | 4,210,000.00 USD | 549,010.00 USD | 6,400,000.00 USD |
| `1D` | `2092.60` | 1,080,000,000.00 USD | 0.00 USD | 1,080,000,000.00 USD | 773,260.00 USD | 522,240.00 USD | 876,790.00 USD |
| `7D` | `2094.20` | 2,450,000,000.00 USD | 0.00 USD | 2,450,000,000.00 USD | 5,310,000.00 USD | 1,660,000.00 USD | 2,340,000.00 USD |
| `1D` | `2095.20` | 1,070,000,000.00 USD | 0.00 USD | 1,070,000,000.00 USD | 2,100,000.00 USD | 1,280,000.00 USD | 1,760,000.00 USD |
| `7D` | `2097.00` | 2,440,000,000.00 USD | 0.00 USD | 2,440,000,000.00 USD | 1,830,000.00 USD | 3,320,000.00 USD | 1,290,000.00 USD |
| `1D` | `2097.80` | 1,070,000,000.00 USD | 0.00 USD | 1,070,000,000.00 USD | 440,660.00 USD | 975,880.00 USD | 517,910.00 USD |
| `7D` | `2099.80` | 2,430,000,000.00 USD | 0.00 USD | 2,430,000,000.00 USD | 1,880,000.00 USD | 1,920,000.00 USD | 3,300,000.00 USD |
| `1D` | `2100.40` | 1,070,000,000.00 USD | 0.00 USD | 1,070,000,000.00 USD | 160,570.00 USD | 44,780.00 USD | 175,760.00 USD |
| `7D` | `2102.60` | 2,430,000,000.00 USD | 0.00 USD | 2,430,000,000.00 USD | 125,250.00 USD | 341,900.00 USD | 1,190,000.00 USD |
| `1D` | `2103.00` | 1,070,000,000.00 USD | 0.00 USD | 1,070,000,000.00 USD | 433,430.00 USD | 182,720.00 USD | 132,000.00 USD |
| `7D` | `2105.40` | 2,430,000,000.00 USD | 0.00 USD | 2,430,000,000.00 USD | 2,050,000.00 USD | 986,590.00 USD | 1,790,000.00 USD |
| `1D` | `2105.60` | 1,070,000,000.00 USD | 0.00 USD | 1,070,000,000.00 USD | 585,230.00 USD | 400,040.00 USD | 419,370.00 USD |
| `1D` | `2108.20` | 1,060,000,000.00 USD | 0.00 USD | 1,060,000,000.00 USD | 600,390.00 USD | 9,120.00 USD | 96,180.00 USD |
| `7D` | `2108.20` | 2,420,000,000.00 USD | 0.00 USD | 2,420,000,000.00 USD | 2,350,000.00 USD | 1,090,000.00 USD | 1,640,000.00 USD |
| `1D` | `2110.80` | 1,060,000,000.00 USD | 0.00 USD | 1,060,000,000.00 USD | 36,110.00 USD | 22,440.00 USD | 200,160.00 USD |
| `7D` | `2111.00` | 2,420,000,000.00 USD | 0.00 USD | 2,420,000,000.00 USD | 3,450,000.00 USD | 1,620,000.00 USD | 2,160,000.00 USD |
| `1D` | `2113.40` | 1,060,000,000.00 USD | 0.00 USD | 1,060,000,000.00 USD | 875,700.00 USD | 643,210.00 USD | 235,840.00 USD |
| `7D` | `2113.80` | 2,410,000,000.00 USD | 0.00 USD | 2,410,000,000.00 USD | 1,080,000.00 USD | 1,300,000.00 USD | 2,730,000.00 USD |
| `1D` | `2116.00` | 1,060,000,000.00 USD | 0.00 USD | 1,060,000,000.00 USD | 0.00 USD | 13,230.00 USD | 426,920.00 USD |
| `7D` | `2116.60` | 2,400,000,000.00 USD | 0.00 USD | 2,400,000,000.00 USD | 2,360,000.00 USD | 2,350,000.00 USD | 2,570,000.00 USD |
| `1D` | `2118.60` | 1,060,000,000.00 USD | 0.00 USD | 1,060,000,000.00 USD | 1,120,000.00 USD | 16,610.00 USD | 1,080,000.00 USD |
| `7D` | `2119.40` | 2,400,000,000.00 USD | 0.00 USD | 2,400,000,000.00 USD | 2,530,000.00 USD | 606,940.00 USD | 2,590,000.00 USD |
| `1D` | `2121.20` | 1,060,000,000.00 USD | 0.00 USD | 1,060,000,000.00 USD | 1,030,000.00 USD | 870,210.00 USD | 1,040,000.00 USD |
| `7D` | `2122.20` | 2,390,000,000.00 USD | 0.00 USD | 2,390,000,000.00 USD | 2,230,000.00 USD | 1,000,000.00 USD | 1,630,000.00 USD |
| `1D` | `2123.80` | 1,060,000,000.00 USD | 0.00 USD | 1,060,000,000.00 USD | 966,890.00 USD | 928,560.00 USD | 1,000,000.00 USD |
| `7D` | `2125.00` | 2,380,000,000.00 USD | 0.00 USD | 2,380,000,000.00 USD | 2,700,000.00 USD | 2,150,000.00 USD | 2,640,000.00 USD |
| `1D` | `2126.40` | 1,050,000,000.00 USD | 0.00 USD | 1,050,000,000.00 USD | 58,860.00 USD | 852,390.00 USD | 630,650.00 USD |
| `7D` | `2127.80` | 2,380,000,000.00 USD | 0.00 USD | 2,380,000,000.00 USD | 496,060.00 USD | 1,960,000.00 USD | 1,630,000.00 USD |
| `1D` | `2129.00` | 1,050,000,000.00 USD | 0.00 USD | 1,050,000,000.00 USD | 356,740.00 USD | 616,780.00 USD | 323,070.00 USD |
| `7D` | `2130.60` | 2,370,000,000.00 USD | 0.00 USD | 2,370,000,000.00 USD | 2,040,000.00 USD | 1,750,000.00 USD | 1,700,000.00 USD |
| `1D` | `2131.60` | 1,050,000,000.00 USD | 0.00 USD | 1,050,000,000.00 USD | 0.00 USD | 644,330.00 USD | 336,530.00 USD |
| `7D` | `2133.40` | 2,370,000,000.00 USD | 0.00 USD | 2,370,000,000.00 USD | 2,120,000.00 USD | 550,450.00 USD | 316,050.00 USD |
| `1D` | `2134.20` | 1,050,000,000.00 USD | 0.00 USD | 1,050,000,000.00 USD | 187,520.00 USD | 497,320.00 USD | 0.00 USD |
| `7D` | `2136.20` | 2,360,000,000.00 USD | 0.00 USD | 2,360,000,000.00 USD | 1,170,000.00 USD | 845,110.00 USD | 18,020.00 USD |
| `1D` | `2136.80` | 1,050,000,000.00 USD | 0.00 USD | 1,050,000,000.00 USD | 0.00 USD | 544,840.00 USD | 2,870.00 USD |
| `7D` | `2139.00` | 2,360,000,000.00 USD | 0.00 USD | 2,360,000,000.00 USD | 1,110,000.00 USD | 1,000,000.00 USD | 276,890.00 USD |
| `1D` | `2139.40` | 1,050,000,000.00 USD | 0.00 USD | 1,050,000,000.00 USD | 555,320.00 USD | 0.00 USD | 205,180.00 USD |
| `7D` | `2141.80` | 2,360,000,000.00 USD | 0.00 USD | 2,360,000,000.00 USD | 1,550,000.00 USD | 209,240.00 USD | 819,060.00 USD |
| `1D` | `2142.00` | 1,050,000,000.00 USD | 0.00 USD | 1,050,000,000.00 USD | 295,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2144.60` | 1,050,000,000.00 USD | 0.00 USD | 1,050,000,000.00 USD | 0.00 USD | 16,700.00 USD | 3,100.00 USD |
| `7D` | `2144.60` | 2,360,000,000.00 USD | 0.00 USD | 2,360,000,000.00 USD | 547,980.00 USD | 1,530,000.00 USD | 0.00 USD |
| `1D` | `2147.20` | 1,050,000,000.00 USD | 0.00 USD | 1,050,000,000.00 USD | 0.00 USD | 11,090.00 USD | 207,420.00 USD |
| `7D` | `2147.40` | 2,360,000,000.00 USD | 0.00 USD | 2,360,000,000.00 USD | 157,100.00 USD | 32,210.00 USD | 0.00 USD |
| `1D` | `2149.80` | 1,050,000,000.00 USD | 0.00 USD | 1,050,000,000.00 USD | 251,250.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2150.20` | 2,360,000,000.00 USD | 0.00 USD | 2,360,000,000.00 USD | 459,630.00 USD | 482,820.00 USD | 537,180.00 USD |
| `7D` | `2153.00` | 2,350,000,000.00 USD | 0.00 USD | 2,350,000,000.00 USD | 29,510.00 USD | 681,070.00 USD | 800,440.00 USD |
| `7D` | `2155.80` | 2,350,000,000.00 USD | 0.00 USD | 2,350,000,000.00 USD | 191,860.00 USD | 454,940.00 USD | 66,320.00 USD |
| `7D` | `2158.60` | 2,350,000,000.00 USD | 0.00 USD | 2,350,000,000.00 USD | 774,660.00 USD | 1,260,000.00 USD | 1,660,000.00 USD |
| `7D` | `2161.40` | 2,350,000,000.00 USD | 0.00 USD | 2,350,000,000.00 USD | 1,450,000.00 USD | 804,860.00 USD | 2,170,000.00 USD |
| `7D` | `2164.20` | 2,340,000,000.00 USD | 0.00 USD | 2,340,000,000.00 USD | 36,870.00 USD | 329,690.00 USD | 409,110.00 USD |
| `7D` | `2167.00` | 2,340,000,000.00 USD | 0.00 USD | 2,340,000,000.00 USD | 25,540.00 USD | 0.00 USD | 84,450.00 USD |
| `7D` | `2169.80` | 2,340,000,000.00 USD | 0.00 USD | 2,340,000,000.00 USD | 1,700,000.00 USD | 726,240.00 USD | 794,200.00 USD |
| `7D` | `2172.60` | 2,340,000,000.00 USD | 0.00 USD | 2,340,000,000.00 USD | 479,540.00 USD | 1,150,000.00 USD | 0.00 USD |
| `7D` | `2195.00` | 2,340,000,000.00 USD | 0.00 USD | 2,340,000,000.00 USD | 141,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2197.80` | 2,340,000,000.00 USD | 0.00 USD | 2,340,000,000.00 USD | 2,440,000.00 USD | 3,270,000.00 USD | 0.00 USD |
| `1D` | `2199.20` | 1,050,000,000.00 USD | 0.00 USD | 1,050,000,000.00 USD | 0.00 USD | 0.00 USD | 80,640.00 USD |
| `7D` | `2200.60` | 2,330,000,000.00 USD | 0.00 USD | 2,330,000,000.00 USD | 3,120,000.00 USD | 3,140,000.00 USD | 3,200,000.00 USD |
| `1D` | `2201.80` | 1,050,000,000.00 USD | 0.00 USD | 1,050,000,000.00 USD | 284,470.00 USD | 217,490.00 USD | 144,690.00 USD |
| `7D` | `2203.40` | 2,320,000,000.00 USD | 0.00 USD | 2,320,000,000.00 USD | 3,280,000.00 USD | 624,500.00 USD | 2,720,000.00 USD |
| `1D` | `2204.40` | 1,050,000,000.00 USD | 0.00 USD | 1,050,000,000.00 USD | 1,050,000.00 USD | 207,110.00 USD | 792,260.00 USD |
| `7D` | `2206.20` | 2,320,000,000.00 USD | 0.00 USD | 2,320,000,000.00 USD | 6,770,000.00 USD | 4,010,000.00 USD | 4,980,000.00 USD |
| `1D` | `2207.00` | 1,040,000,000.00 USD | 0.00 USD | 1,040,000,000.00 USD | 2,070,000.00 USD | 2,330,000.00 USD | 1,800,000.00 USD |
| `7D` | `2209.00` | 2,300,000,000.00 USD | 0.00 USD | 2,300,000,000.00 USD | 9,190,000.00 USD | 7,030,000.00 USD | 4,130,000.00 USD |
| `1D` | `2209.60` | 1,040,000,000.00 USD | 0.00 USD | 1,040,000,000.00 USD | 1,770,000.00 USD | 610,890.00 USD | 1,950,000.00 USD |
| `7D` | `2211.80` | 2,280,000,000.00 USD | 0.00 USD | 2,280,000,000.00 USD | 8,790,000.00 USD | 8,110,000.00 USD | 6,870,000.00 USD |
| `1D` | `2212.20` | 1,030,000,000.00 USD | 0.00 USD | 1,030,000,000.00 USD | 2,580,000.00 USD | 1,580,000.00 USD | 1,780,000.00 USD |
| `7D` | `2214.60` | 2,260,000,000.00 USD | 0.00 USD | 2,260,000,000.00 USD | 14,850,000.00 USD | 14,220,000.00 USD | 10,020,000.00 USD |
| `1D` | `2214.80` | 1,030,000,000.00 USD | 0.00 USD | 1,030,000,000.00 USD | 6,410,000.00 USD | 4,340,000.00 USD | 5,100,000.00 USD |
| `1D` | `2217.40` | 1,010,000,000.00 USD | 0.00 USD | 1,010,000,000.00 USD | 4,250,000.00 USD | 5,300,000.00 USD | 1,840,000.00 USD |
| `7D` | `2217.40` | 2,220,000,000.00 USD | 0.00 USD | 2,220,000,000.00 USD | 13,750,000.00 USD | 10,950,000.00 USD | 7,320,000.00 USD |
| `1D` | `2220.00` | 1,000,000,000.00 USD | 0.00 USD | 1,000,000,000.00 USD | 3,690,000.00 USD | 3,840,000.00 USD | 453,520.00 USD |
| `7D` | `2220.20` | 2,190,000,000.00 USD | 0.00 USD | 2,190,000,000.00 USD | 12,830,000.00 USD | 7,840,000.00 USD | 3,390,000.00 USD |
| `1D` | `2222.60` | 992,510,000.00 USD | 0.00 USD | 992,510,000.00 USD | 5,420,000.00 USD | 3,840,000.00 USD | 2,960,000.00 USD |
| `7D` | `2223.00` | 2,160,000,000.00 USD | 0.00 USD | 2,160,000,000.00 USD | 6,930,000.00 USD | 5,300,000.00 USD | 11,550,000.00 USD |
| `1D` | `2225.20` | 980,290,000.00 USD | 0.00 USD | 980,290,000.00 USD | 1,930,000.00 USD | 4,150,000.00 USD | 2,440,000.00 USD |
| `7D` | `2225.80` | 2,140,000,000.00 USD | 0.00 USD | 2,140,000,000.00 USD | 11,900,000.00 USD | 12,610,000.00 USD | 6,520,000.00 USD |
| `1D` | `2227.80` | 971,770,000.00 USD | 0.00 USD | 971,770,000.00 USD | 5,720,000.00 USD | 2,770,000.00 USD | 801,240.00 USD |
| `7D` | `2228.60` | 2,110,000,000.00 USD | 0.00 USD | 2,110,000,000.00 USD | 7,530,000.00 USD | 5,580,000.00 USD | 9,590,000.00 USD |
| `1D` | `2230.40` | 962,470,000.00 USD | 0.00 USD | 962,470,000.00 USD | 3,880,000.00 USD | 2,030,000.00 USD | 2,110,000.00 USD |
| `7D` | `2231.40` | 2,080,000,000.00 USD | 0.00 USD | 2,080,000,000.00 USD | 10,960,000.00 USD | 2,990,000.00 USD | 14,790,000.00 USD |
| `1D` | `2233.00` | 954,450,000.00 USD | 0.00 USD | 954,450,000.00 USD | 5,430,000.00 USD | 2,440,000.00 USD | 3,500,000.00 USD |
| `7D` | `2234.20` | 2,050,000,000.00 USD | 0.00 USD | 2,050,000,000.00 USD | 17,000,000.00 USD | 12,020,000.00 USD | 7,540,000.00 USD |
| `1D` | `2235.60` | 943,070,000.00 USD | 0.00 USD | 943,070,000.00 USD | 3,880,000.00 USD | 4,850,000.00 USD | 5,490,000.00 USD |
| `7D` | `2237.00` | 2,020,000,000.00 USD | 0.00 USD | 2,020,000,000.00 USD | 6,950,000.00 USD | 11,130,000.00 USD | 4,810,000.00 USD |
| `1D` | `2238.20` | 928,850,000.00 USD | 0.00 USD | 928,850,000.00 USD | 1,800,000.00 USD | 2,210,000.00 USD | 844,590.00 USD |
| `7D` | `2239.80` | 2,000,000,000.00 USD | 0.00 USD | 2,000,000,000.00 USD | 7,410,000.00 USD | 6,730,000.00 USD | 9,280,000.00 USD |
| `1D` | `2240.80` | 924,000,000.00 USD | 0.00 USD | 924,000,000.00 USD | 634,700.00 USD | 542,280.00 USD | 601,200.00 USD |
| `7D` | `2242.60` | 1,970,000,000.00 USD | 0.00 USD | 1,970,000,000.00 USD | 7,790,000.00 USD | 2,710,000.00 USD | 4,500,000.00 USD |
| `1D` | `2243.40` | 922,220,000.00 USD | 0.00 USD | 922,220,000.00 USD | 1,210,000.00 USD | 881,310.00 USD | 555,680.00 USD |
| `7D` | `2245.40` | 1,960,000,000.00 USD | 0.00 USD | 1,960,000,000.00 USD | 12,040,000.00 USD | 12,530,000.00 USD | 10,610,000.00 USD |
| `1D` | `2246.00` | 919,570,000.00 USD | 0.00 USD | 919,570,000.00 USD | 2,560,000.00 USD | 1,790,000.00 USD | 1,560,000.00 USD |
| `7D` | `2248.20` | 1,920,000,000.00 USD | 0.00 USD | 1,920,000,000.00 USD | 13,950,000.00 USD | 5,870,000.00 USD | 11,630,000.00 USD |
| `1D` | `2248.60` | 913,660,000.00 USD | 0.00 USD | 913,660,000.00 USD | 4,610,000.00 USD | 601,150.00 USD | 2,070,000.00 USD |
| `7D` | `2251.00` | 1,890,000,000.00 USD | 0.00 USD | 1,890,000,000.00 USD | 12,710,000.00 USD | 11,300,000.00 USD | 8,550,000.00 USD |
| `1D` | `2251.20` | 906,380,000.00 USD | 0.00 USD | 906,380,000.00 USD | 304,760.00 USD | 1,060,000.00 USD | 683,530.00 USD |
| `1D` | `2253.80` | 904,330,000.00 USD | 0.00 USD | 904,330,000.00 USD | 8,560,000.00 USD | 6,780,000.00 USD | 6,950,000.00 USD |
| `7D` | `2253.80` | 1,860,000,000.00 USD | 0.00 USD | 1,860,000,000.00 USD | 25,660,000.00 USD | 20,190,000.00 USD | 19,820,000.00 USD |
| `1D` | `2256.40` | 882,050,000.00 USD | 0.00 USD | 882,050,000.00 USD | 3,260,000.00 USD | 2,980,000.00 USD | 3,880,000.00 USD |
| `7D` | `2256.60` | 1,790,000,000.00 USD | 0.00 USD | 1,790,000,000.00 USD | 29,170,000.00 USD | 24,230,000.00 USD | 17,560,000.00 USD |
| `1D` | `2259.00` | 871,930,000.00 USD | 0.00 USD | 871,930,000.00 USD | 8,870,000.00 USD | 4,580,000.00 USD | 4,610,000.00 USD |
| `7D` | `2259.40` | 1,720,000,000.00 USD | 0.00 USD | 1,720,000,000.00 USD | 25,970,000.00 USD | 15,650,000.00 USD | 27,050,000.00 USD |
| `1D` | `2261.60` | 853,870,000.00 USD | 0.00 USD | 853,870,000.00 USD | 14,160,000.00 USD | 11,590,000.00 USD | 15,410,000.00 USD |
| `7D` | `2262.20` | 1,650,000,000.00 USD | 0.00 USD | 1,650,000,000.00 USD | 46,580,000.00 USD | 30,720,000.00 USD | 19,820,000.00 USD |
| `1D` | `2264.20` | 812,710,000.00 USD | 0.00 USD | 812,710,000.00 USD | 13,110,000.00 USD | 12,080,000.00 USD | 6,200,000.00 USD |
| `7D` | `2265.00` | 1,560,000,000.00 USD | 0.00 USD | 1,560,000,000.00 USD | 29,070,000.00 USD | 25,860,000.00 USD | 16,140,000.00 USD |
| `1D` | `2266.80` | 781,320,000.00 USD | 0.00 USD | 781,320,000.00 USD | 11,660,000.00 USD | 11,820,000.00 USD | 3,870,000.00 USD |
| `7D` | `2267.80` | 1,480,000,000.00 USD | 0.00 USD | 1,480,000,000.00 USD | 41,280,000.00 USD | 43,110,000.00 USD | 32,090,000.00 USD |
| `1D` | `2269.40` | 753,980,000.00 USD | 0.00 USD | 753,980,000.00 USD | 13,850,000.00 USD | 11,370,000.00 USD | 8,090,000.00 USD |
| `7D` | `2270.60` | 1,370,000,000.00 USD | 0.00 USD | 1,370,000,000.00 USD | 43,030,000.00 USD | 30,540,000.00 USD | 36,990,000.00 USD |
| `1D` | `2272.00` | 720,660,000.00 USD | 0.00 USD | 720,660,000.00 USD | 12,250,000.00 USD | 12,340,000.00 USD | 9,240,000.00 USD |
| `7D` | `2273.40` | 1,260,000,000.00 USD | 0.00 USD | 1,260,000,000.00 USD | 27,330,000.00 USD | 19,600,000.00 USD | 20,130,000.00 USD |
| `1D` | `2274.60` | 686,840,000.00 USD | 0.00 USD | 686,840,000.00 USD | 10,260,000.00 USD | 6,240,000.00 USD | 5,490,000.00 USD |
| `7D` | `2276.20` | 1,190,000,000.00 USD | 0.00 USD | 1,190,000,000.00 USD | 55,750,000.00 USD | 46,480,000.00 USD | 59,460,000.00 USD |
| `1D` | `2277.20` | 664,840,000.00 USD | 0.00 USD | 664,840,000.00 USD | 18,320,000.00 USD | 14,850,000.00 USD | 15,720,000.00 USD |
| `7D` | `2279.00` | 1,030,000,000.00 USD | 0.00 USD | 1,030,000,000.00 USD | 71,690,000.00 USD | 30,780,000.00 USD | 36,640,000.00 USD |
| `1D` | `2279.80` | 615,950,000.00 USD | 0.00 USD | 615,950,000.00 USD | 19,100,000.00 USD | 14,830,000.00 USD | 11,580,000.00 USD |
| `7D` | `2281.80` | 889,350,000.00 USD | 0.00 USD | 889,350,000.00 USD | 64,270,000.00 USD | 63,850,000.00 USD | 39,490,000.00 USD |
| `1D` | `2282.40` | 570,430,000.00 USD | 0.00 USD | 570,430,000.00 USD | 26,760,000.00 USD | 17,540,000.00 USD | 21,070,000.00 USD |
| `7D` | `2284.60` | 721,740,000.00 USD | 0.00 USD | 721,740,000.00 USD | 84,980,000.00 USD | 71,990,000.00 USD | 47,600,000.00 USD |
| `1D` | `2285.00` | 505,060,000.00 USD | 0.00 USD | 505,060,000.00 USD | 24,940,000.00 USD | 23,280,000.00 USD | 19,680,000.00 USD |
| `7D` | `2287.40` | 517,180,000.00 USD | 0.00 USD | 517,180,000.00 USD | 57,800,000.00 USD | 54,380,000.00 USD | 45,750,000.00 USD |
| `1D` | `2287.60` | 437,160,000.00 USD | 0.00 USD | 437,160,000.00 USD | 17,430,000.00 USD | 15,630,000.00 USD | 6,410,000.00 USD |
| `1D` | `2290.20` | 397,690,000.00 USD | 0.00 USD | 397,690,000.00 USD | 15,700,000.00 USD | 15,930,000.00 USD | 3,100,000.00 USD |
| `7D` | `2290.20` | 359,240,000.00 USD | 0.00 USD | 359,240,000.00 USD | 45,650,000.00 USD | 33,150,000.00 USD | 39,040,000.00 USD |
| `1D` | `2292.80` | 362,960,000.00 USD | 0.00 USD | 362,960,000.00 USD | 21,580,000.00 USD | 18,140,000.00 USD | 15,000,000.00 USD |
| `7D` | `2293.00` | 241,410,000.00 USD | 0.00 USD | 241,410,000.00 USD | 33,030,000.00 USD | 15,200,000.00 USD | 23,140,000.00 USD |
| `1D` | `2295.40` | 308,240,000.00 USD | 0.00 USD | 308,240,000.00 USD | 20,210,000.00 USD | 18,280,000.00 USD | 9,490,000.00 USD |
| `7D` | `2295.80` | 170,040,000.00 USD | 0.00 USD | 170,040,000.00 USD | 17,510,000.00 USD | 9,480,000.00 USD | 6,790,000.00 USD |
| `1D` | `2298.00` | 260,260,000.00 USD | 0.00 USD | 260,260,000.00 USD | 11,100,000.00 USD | 6,170,000.00 USD | 1,410,000.00 USD |
| `7D` | `2298.60` | 136,260,000.00 USD | 0.00 USD | 136,260,000.00 USD | 2,760,000.00 USD | 4,450,000.00 USD | 358,390.00 USD |
| `1D` | `2300.60` | 241,570,000.00 USD | 0.00 USD | 241,570,000.00 USD | 18,640,000.00 USD | 11,200,000.00 USD | 13,310,000.00 USD |
| `7D` | `2301.40` | 128,690,000.00 USD | 0.00 USD | 128,690,000.00 USD | 11,120,000.00 USD | 2,120,000.00 USD | 7,540,000.00 USD |
| `1D` | `2303.20` | 198,430,000.00 USD | 0.00 USD | 198,430,000.00 USD | 26,500,000.00 USD | 16,170,000.00 USD | 16,580,000.00 USD |
| `7D` | `2304.20` | 107,910,000.00 USD | 0.00 USD | 107,910,000.00 USD | 32,960,000.00 USD | 16,920,000.00 USD | 13,270,000.00 USD |
| `1D` | `2305.80` | 139,180,000.00 USD | 0.00 USD | 139,180,000.00 USD | 9,950,000.00 USD | 7,080,000.00 USD | 18,270,000.00 USD |
| `7D` | `2307.00` | 44,760,000.00 USD | 0.00 USD | 44,760,000.00 USD | 0.00 USD | 3,740,000.00 USD | 10,890,000.00 USD |
| `1D` | `2308.40` | 103,880,000.00 USD | 0.00 USD | 103,880,000.00 USD | 1,030,000.00 USD | 2,010,000.00 USD | 2,540,000.00 USD |
| `7D` | `2309.80` | 30,130,000.00 USD | 0.00 USD | 30,130,000.00 USD | 282,530.00 USD | 300,580.00 USD | 1,500,000.00 USD |
| `1D` | `2311.00` | 98,300,000.00 USD | 0.00 USD | 98,300,000.00 USD | 6,780,000.00 USD | 5,300,000.00 USD | 6,850,000.00 USD |
| `7D` | `2312.60` | 28,040,000.00 USD | 0.00 USD | 28,040,000.00 USD | 2,470,000.00 USD | 640,510.00 USD | 2,620,000.00 USD |
| `1D` | `2313.60` | 79,360,000.00 USD | 0.00 USD | 79,360,000.00 USD | 6,200,000.00 USD | 5,150,000.00 USD | 3,130,000.00 USD |
| `7D` | `2315.40` | 22,310,000.00 USD | 0.00 USD | 22,310,000.00 USD | 5,830,000.00 USD | 4,100,000.00 USD | 0.00 USD |
| `1D` | `2316.20` | 64,880,000.00 USD | 0.00 USD | 64,880,000.00 USD | 10,440,000.00 USD | 8,800,000.00 USD | 5,830,000.00 USD |
| `7D` | `2318.20` | 12,380,000.00 USD | 0.00 USD | 12,380,000.00 USD | 0.00 USD | 3,010,000.00 USD | 0.00 USD |
| `1D` | `2318.80` | 39,800,000.00 USD | 0.00 USD | 39,800,000.00 USD | 11,680,000.00 USD | 4,080,000.00 USD | 2,250,000.00 USD |
| `7D` | `2321.00` | 9,370,000.00 USD | 0.00 USD | 9,370,000.00 USD | 947,800.00 USD | 2,960,000.00 USD | 0.00 USD |
| `1D` | `2321.40` | 21,780,000.00 USD | 0.00 USD | 21,780,000.00 USD | 255,100.00 USD | 2,970,000.00 USD | 1,720,000.00 USD |
| `7D` | `2323.80` | 5,460,000.00 USD | 0.00 USD | 5,460,000.00 USD | 3,130,000.00 USD | 2,210,000.00 USD | 0.00 USD |
| `1D` | `2324.00` | 16,840,000.00 USD | 0.00 USD | 16,840,000.00 USD | 8,620,000.00 USD | 2,890,000.00 USD | 2,210,000.00 USD |
| `1D` | `2326.60` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 0.00 USD | 3,040,000.00 USD | 66,960.00 USD |
| `7D` | `2326.60` | 126,530.00 USD | 0.00 USD | 126,530.00 USD | 0.00 USD | 0.00 USD | 126,530.00 USD |
| `7D` | `2327.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2327.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2329.20` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 1,890,000.00 USD | 1,370,000.00 USD | 287,800.00 USD |
| `7D` | `2329.40` | 8,740,000.00 USD | 8,740,000.00 USD | 0.00 USD | 3,860,000.00 USD | 0.00 USD | 4,880,000.00 USD |
| `1D` | `2331.80` | 16,860,000.00 USD | 16,860,000.00 USD | 0.00 USD | 13,200,000.00 USD | 0.00 USD | 107,090.00 USD |
| `7D` | `2332.20` | 40,790,000.00 USD | 40,790,000.00 USD | 0.00 USD | 29,230,000.00 USD | 0.00 USD | 2,810,000.00 USD |
| `1D` | `2334.40` | 41,550,000.00 USD | 41,550,000.00 USD | 0.00 USD | 11,210,000.00 USD | 12,110,000.00 USD | 1,380,000.00 USD |
| `7D` | `2335.00` | 81,690,000.00 USD | 81,690,000.00 USD | 0.00 USD | 13,560,000.00 USD | 18,420,000.00 USD | 8,930,000.00 USD |
| `1D` | `2337.00` | 44,440,000.00 USD | 44,440,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD | 1,420,000.00 USD |
| `7D` | `2337.80` | 127,650,000.00 USD | 127,650,000.00 USD | 0.00 USD | 14,090,000.00 USD | 18,310,000.00 USD | 13,560,000.00 USD |
| `7D` | `2340.60` | 146,580,000.00 USD | 146,580,000.00 USD | 0.00 USD | 0.00 USD | 15,560,000.00 USD | 3,380,000.00 USD |
| `7D` | `2343.40` | 153,750,000.00 USD | 153,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,160,000.00 USD |
| `1D` | `2344.80` | 57,440,000.00 USD | 57,440,000.00 USD | 0.00 USD | 963,370.00 USD | 1,960,000.00 USD | 10,070,000.00 USD |
| `7D` | `2346.20` | 171,170,000.00 USD | 171,170,000.00 USD | 0.00 USD | 0.00 USD | 7,920,000.00 USD | 9,500,000.00 USD |
| `1D` | `2347.40` | 58,220,000.00 USD | 58,220,000.00 USD | 0.00 USD | 166,240.00 USD | 0.00 USD | 615,370.00 USD |
| `7D` | `2349.00` | 199,590,000.00 USD | 199,590,000.00 USD | 0.00 USD | 495,290.00 USD | 11,840,000.00 USD | 16,080,000.00 USD |
| `1D` | `2350.00` | 90,680,000.00 USD | 90,680,000.00 USD | 0.00 USD | 24,070,000.00 USD | 2,510,000.00 USD | 5,880,000.00 USD |
| `7D` | `2351.80` | 213,610,000.00 USD | 213,610,000.00 USD | 0.00 USD | 572,980.00 USD | 13,100,000.00 USD | 351,920.00 USD |
| `1D` | `2352.60` | 94,570,000.00 USD | 94,570,000.00 USD | 0.00 USD | 2,620,000.00 USD | 121,980.00 USD | 1,150,000.00 USD |
| `7D` | `2354.60` | 258,400,000.00 USD | 258,400,000.00 USD | 0.00 USD | 9,800,000.00 USD | 34,750,000.00 USD | 237,340.00 USD |
| `1D` | `2355.20` | 113,540,000.00 USD | 113,540,000.00 USD | 0.00 USD | 628,820.00 USD | 17,100,000.00 USD | 1,240,000.00 USD |
| `7D` | `2357.40` | 269,350,000.00 USD | 269,350,000.00 USD | 0.00 USD | 5,040,000.00 USD | 5,920,000.00 USD | 0.00 USD |
| `1D` | `2357.80` | 119,390,000.00 USD | 119,390,000.00 USD | 0.00 USD | 1,400,000.00 USD | 2,000,000.00 USD | 2,450,000.00 USD |
| `7D` | `2360.20` | 271,790,000.00 USD | 271,790,000.00 USD | 0.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2360.40` | 124,310,000.00 USD | 124,310,000.00 USD | 0.00 USD | 1,730,000.00 USD | 1,830,000.00 USD | 1,360,000.00 USD |
| `1D` | `2363.00` | 138,390,000.00 USD | 138,390,000.00 USD | 0.00 USD | 4,020,000.00 USD | 7,640,000.00 USD | 2,420,000.00 USD |
| `7D` | `2363.00` | 274,190,000.00 USD | 274,190,000.00 USD | 0.00 USD | 715,490.00 USD | 0.00 USD | 1,690,000.00 USD |
| `1D` | `2365.60` | 141,900,000.00 USD | 141,900,000.00 USD | 0.00 USD | 1,870,000.00 USD | 0.00 USD | 1,640,000.00 USD |
| `7D` | `2365.80` | 282,190,000.00 USD | 282,190,000.00 USD | 0.00 USD | 6,340,000.00 USD | 0.00 USD | 1,660,000.00 USD |
| `1D` | `2368.20` | 150,850,000.00 USD | 150,850,000.00 USD | 0.00 USD | 6,250,000.00 USD | 2,170,000.00 USD | 532,260.00 USD |
| `7D` | `2368.60` | 292,670,000.00 USD | 292,670,000.00 USD | 0.00 USD | 9,590,000.00 USD | 475,460.00 USD | 404,380.00 USD |
| `1D` | `2370.80` | 189,500,000.00 USD | 189,500,000.00 USD | 0.00 USD | 16,400,000.00 USD | 13,050,000.00 USD | 9,190,000.00 USD |
| `7D` | `2371.40` | 358,480,000.00 USD | 358,480,000.00 USD | 0.00 USD | 18,630,000.00 USD | 0.00 USD | 47,190,000.00 USD |
| `1D` | `2373.40` | 211,160,000.00 USD | 211,160,000.00 USD | 0.00 USD | 14,040,000.00 USD | 1,720,000.00 USD | 5,890,000.00 USD |
| `7D` | `2374.20` | 376,990,000.00 USD | 376,990,000.00 USD | 0.00 USD | 13,960,000.00 USD | 0.00 USD | 4,550,000.00 USD |
| `1D` | `2376.00` | 234,470,000.00 USD | 234,470,000.00 USD | 0.00 USD | 11,540,000.00 USD | 3,310,000.00 USD | 8,460,000.00 USD |
| `7D` | `2377.00` | 417,370,000.00 USD | 417,370,000.00 USD | 0.00 USD | 12,140,000.00 USD | 6,190,000.00 USD | 22,050,000.00 USD |
| `1D` | `2378.60` | 261,610,000.00 USD | 261,610,000.00 USD | 0.00 USD | 6,450,000.00 USD | 11,410,000.00 USD | 9,290,000.00 USD |
| `7D` | `2379.80` | 445,570,000.00 USD | 445,570,000.00 USD | 0.00 USD | 7,180,000.00 USD | 2,330,000.00 USD | 18,680,000.00 USD |
| `1D` | `2381.20` | 310,740,000.00 USD | 310,740,000.00 USD | 0.00 USD | 16,330,000.00 USD | 12,790,000.00 USD | 20,000,000.00 USD |
| `7D` | `2382.60` | 486,960,000.00 USD | 486,960,000.00 USD | 0.00 USD | 8,620,000.00 USD | 12,380,000.00 USD | 20,400,000.00 USD |
| `1D` | `2383.80` | 355,250,000.00 USD | 355,250,000.00 USD | 0.00 USD | 19,270,000.00 USD | 15,610,000.00 USD | 9,630,000.00 USD |
| `7D` | `2385.40` | 583,310,000.00 USD | 583,310,000.00 USD | 0.00 USD | 15,530,000.00 USD | 30,320,000.00 USD | 50,510,000.00 USD |
| `1D` | `2386.40` | 394,330,000.00 USD | 394,330,000.00 USD | 0.00 USD | 13,990,000.00 USD | 13,800,000.00 USD | 11,280,000.00 USD |
| `7D` | `2388.20` | 660,270,000.00 USD | 660,270,000.00 USD | 0.00 USD | 4,500,000.00 USD | 34,050,000.00 USD | 38,400,000.00 USD |
| `1D` | `2389.00` | 421,440,000.00 USD | 421,440,000.00 USD | 0.00 USD | 12,210,000.00 USD | 8,980,000.00 USD | 5,920,000.00 USD |
| `7D` | `2391.00` | 756,660,000.00 USD | 756,660,000.00 USD | 0.00 USD | 5,620,000.00 USD | 45,790,000.00 USD | 44,980,000.00 USD |
| `1D` | `2391.60` | 446,050,000.00 USD | 446,050,000.00 USD | 0.00 USD | 4,230,000.00 USD | 11,920,000.00 USD | 8,460,000.00 USD |
| `7D` | `2393.80` | 868,970,000.00 USD | 868,970,000.00 USD | 0.00 USD | 48,290,000.00 USD | 27,870,000.00 USD | 36,150,000.00 USD |
| `1D` | `2394.20` | 468,780,000.00 USD | 468,780,000.00 USD | 0.00 USD | 9,780,000.00 USD | 10,200,000.00 USD | 2,750,000.00 USD |
| `7D` | `2396.60` | 943,260,000.00 USD | 943,260,000.00 USD | 0.00 USD | 26,490,000.00 USD | 29,530,000.00 USD | 18,270,000.00 USD |
| `1D` | `2396.80` | 481,130,000.00 USD | 481,130,000.00 USD | 0.00 USD | 2,300,000.00 USD | 6,100,000.00 USD | 3,950,000.00 USD |
| `1D` | `2399.40` | 521,040,000.00 USD | 521,040,000.00 USD | 0.00 USD | 17,090,000.00 USD | 9,220,000.00 USD | 13,600,000.00 USD |
| `7D` | `2399.40` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 0.00 USD | 49,120,000.00 USD | 29,120,000.00 USD | 19,940,000.00 USD |
| `1D` | `2402.00` | 544,940,000.00 USD | 544,940,000.00 USD | 0.00 USD | 8,130,000.00 USD | 9,740,000.00 USD | 6,030,000.00 USD |
| `7D` | `2402.20` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 45,210,000.00 USD | 27,170,000.00 USD | 31,130,000.00 USD |
| `1D` | `2404.60` | 579,290,000.00 USD | 579,290,000.00 USD | 0.00 USD | 13,540,000.00 USD | 10,180,000.00 USD | 10,630,000.00 USD |
| `7D` | `2405.00` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 35,270,000.00 USD | 26,450,000.00 USD | 17,010,000.00 USD |
| `1D` | `2407.20` | 609,380,000.00 USD | 609,380,000.00 USD | 0.00 USD | 13,020,000.00 USD | 10,550,000.00 USD | 6,520,000.00 USD |
| `7D` | `2407.80` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 0.00 USD | 26,280,000.00 USD | 26,510,000.00 USD | 16,810,000.00 USD |
| `1D` | `2409.80` | 634,730,000.00 USD | 634,730,000.00 USD | 0.00 USD | 7,750,000.00 USD | 8,870,000.00 USD | 8,730,000.00 USD |
| `7D` | `2410.60` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 23,140,000.00 USD | 26,640,000.00 USD | 27,330,000.00 USD |
| `1D` | `2412.40` | 658,690,000.00 USD | 658,690,000.00 USD | 0.00 USD | 11,210,000.00 USD | 7,480,000.00 USD | 5,270,000.00 USD |
| `7D` | `2413.40` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 15,370,000.00 USD | 14,870,000.00 USD | 9,740,000.00 USD |
| `1D` | `2415.00` | 671,390,000.00 USD | 671,390,000.00 USD | 0.00 USD | 3,530,000.00 USD | 6,090,000.00 USD | 3,070,000.00 USD |
| `7D` | `2416.20` | 1,490,000,000.00 USD | 1,490,000,000.00 USD | 0.00 USD | 25,850,000.00 USD | 16,790,000.00 USD | 32,420,000.00 USD |
| `1D` | `2417.60` | 684,160,000.00 USD | 684,160,000.00 USD | 0.00 USD | 5,030,000.00 USD | 4,910,000.00 USD | 2,840,000.00 USD |
| `7D` | `2419.00` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 0.00 USD | 30,180,000.00 USD | 17,120,000.00 USD | 11,520,000.00 USD |
| `1D` | `2420.20` | 699,110,000.00 USD | 699,110,000.00 USD | 0.00 USD | 6,880,000.00 USD | 4,370,000.00 USD | 3,690,000.00 USD |
| `7D` | `2421.80` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 21,830,000.00 USD | 26,230,000.00 USD | 20,940,000.00 USD |
| `1D` | `2422.80` | 715,140,000.00 USD | 715,140,000.00 USD | 0.00 USD | 4,760,000.00 USD | 4,990,000.00 USD | 6,290,000.00 USD |
| `7D` | `2424.60` | 1,700,000,000.00 USD | 1,700,000,000.00 USD | 0.00 USD | 25,990,000.00 USD | 31,850,000.00 USD | 32,010,000.00 USD |
| `1D` | `2425.40` | 719,540,000.00 USD | 719,540,000.00 USD | 0.00 USD | 1,130,000.00 USD | 2,650,000.00 USD | 629,080.00 USD |
| `7D` | `2427.40` | 1,770,000,000.00 USD | 1,770,000,000.00 USD | 0.00 USD | 25,000,000.00 USD | 18,790,000.00 USD | 24,200,000.00 USD |
| `1D` | `2428.00` | 722,610,000.00 USD | 722,610,000.00 USD | 0.00 USD | 1,930,000.00 USD | 542,280.00 USD | 601,200.00 USD |
| `7D` | `2430.20` | 1,800,000,000.00 USD | 1,800,000,000.00 USD | 0.00 USD | 6,090,000.00 USD | 16,890,000.00 USD | 6,180,000.00 USD |
| `1D` | `2430.60` | 725,240,000.00 USD | 725,240,000.00 USD | 0.00 USD | 1,100,000.00 USD | 964,820.00 USD | 571,180.00 USD |
| `7D` | `2433.00` | 1,830,000,000.00 USD | 1,830,000,000.00 USD | 0.00 USD | 15,680,000.00 USD | 12,450,000.00 USD | 5,820,000.00 USD |
| `1D` | `2433.20` | 731,190,000.00 USD | 731,190,000.00 USD | 0.00 USD | 2,160,000.00 USD | 1,540,000.00 USD | 2,260,000.00 USD |
| `1D` | `2435.80` | 735,810,000.00 USD | 735,810,000.00 USD | 0.00 USD | 3,600,000.00 USD | 452,500.00 USD | 564,100.00 USD |
| `7D` | `2435.80` | 1,880,000,000.00 USD | 1,880,000,000.00 USD | 0.00 USD | 20,300,000.00 USD | 12,070,000.00 USD | 17,110,000.00 USD |
| `1D` | `2438.40` | 737,180,000.00 USD | 737,180,000.00 USD | 0.00 USD | 214,470.00 USD | 664,070.00 USD | 492,100.00 USD |
| `7D` | `2438.60` | 1,940,000,000.00 USD | 1,940,000,000.00 USD | 0.00 USD | 20,380,000.00 USD | 23,980,000.00 USD | 15,730,000.00 USD |
| `1D` | `2441.00` | 742,390,000.00 USD | 742,390,000.00 USD | 0.00 USD | 2,420,000.00 USD | 2,020,000.00 USD | 767,510.00 USD |
| `7D` | `2441.40` | 1,980,000,000.00 USD | 1,980,000,000.00 USD | 0.00 USD | 13,390,000.00 USD | 6,350,000.00 USD | 13,870,000.00 USD |
| `1D` | `2443.60` | 744,370,000.00 USD | 744,370,000.00 USD | 0.00 USD | 73,920.00 USD | 566,480.00 USD | 1,340,000.00 USD |
| `7D` | `2444.20` | 2,010,000,000.00 USD | 2,010,000,000.00 USD | 0.00 USD | 9,430,000.00 USD | 15,220,000.00 USD | 11,100,000.00 USD |
| `1D` | `2446.20` | 748,600,000.00 USD | 748,600,000.00 USD | 0.00 USD | 2,310,000.00 USD | 675,040.00 USD | 1,250,000.00 USD |
| `7D` | `2447.00` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 0.00 USD | 11,560,000.00 USD | 5,380,000.00 USD | 18,490,000.00 USD |
| `1D` | `2448.80` | 754,830,000.00 USD | 754,830,000.00 USD | 0.00 USD | 2,120,000.00 USD | 1,520,000.00 USD | 2,600,000.00 USD |
| `7D` | `2449.80` | 2,090,000,000.00 USD | 2,090,000,000.00 USD | 0.00 USD | 16,990,000.00 USD | 11,970,000.00 USD | 11,930,000.00 USD |
| `1D` | `2451.40` | 765,670,000.00 USD | 765,670,000.00 USD | 0.00 USD | 3,330,000.00 USD | 3,450,000.00 USD | 4,060,000.00 USD |
| `7D` | `2452.60` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 0.00 USD | 6,280,000.00 USD | 7,310,000.00 USD | 6,840,000.00 USD |
| `1D` | `2454.00` | 777,470,000.00 USD | 777,470,000.00 USD | 0.00 USD | 5,050,000.00 USD | 3,030,000.00 USD | 3,720,000.00 USD |
| `7D` | `2455.40` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 0.00 USD | 8,340,000.00 USD | 10,630,000.00 USD | 5,580,000.00 USD |
| `1D` | `2456.60` | 783,760,000.00 USD | 783,760,000.00 USD | 0.00 USD | 1,340,000.00 USD | 3,200,000.00 USD | 1,750,000.00 USD |
| `7D` | `2458.20` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 0.00 USD | 9,800,000.00 USD | 7,130,000.00 USD | 11,540,000.00 USD |
| `1D` | `2459.20` | 789,680,000.00 USD | 789,680,000.00 USD | 0.00 USD | 2,870,000.00 USD | 1,980,000.00 USD | 1,070,000.00 USD |
| `7D` | `2461.00` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 0.00 USD | 6,890,000.00 USD | 10,680,000.00 USD | 9,050,000.00 USD |
| `1D` | `2461.80` | 792,240,000.00 USD | 792,240,000.00 USD | 0.00 USD | 174,920.00 USD | 490,260.00 USD | 1,890,000.00 USD |
| `7D` | `2463.80` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 0.00 USD | 10,390,000.00 USD | 8,820,000.00 USD | 5,210,000.00 USD |
| `1D` | `2464.40` | 794,940,000.00 USD | 794,940,000.00 USD | 0.00 USD | 352,200.00 USD | 2,340,000.00 USD | 5,650.00 USD |
| `7D` | `2466.60` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 0.00 USD | 4,840,000.00 USD | 2,680,000.00 USD | 1,330,000.00 USD |
| `1D` | `2467.00` | 796,240,000.00 USD | 796,240,000.00 USD | 0.00 USD | 468,790.00 USD | 833,710.00 USD | 0.00 USD |
| `7D` | `2469.40` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 0.00 USD | 2,470,000.00 USD | 2,980,000.00 USD | 408,300.00 USD |
| `1D` | `2469.60` | 798,920,000.00 USD | 798,920,000.00 USD | 0.00 USD | 0.00 USD | 1,510,000.00 USD | 1,160,000.00 USD |
| `1D` | `2472.20` | 800,310,000.00 USD | 800,310,000.00 USD | 0.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2472.20` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 0.00 USD | 3,060,000.00 USD | 2,760,000.00 USD | 1,210,000.00 USD |
| `1D` | `2474.80` | 800,540,000.00 USD | 800,540,000.00 USD | 0.00 USD | 0.00 USD | 232,740.00 USD | 3,820.00 USD |
| `7D` | `2475.00` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 0.00 USD | 5,400,000.00 USD | 866,790.00 USD | 2,020,000.00 USD |
| `1D` | `2477.40` | 801,330,000.00 USD | 801,330,000.00 USD | 0.00 USD | 738,780.00 USD | 41,760.00 USD | 7,750.00 USD |
| `7D` | `2477.80` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 0.00 USD | 1,840,000.00 USD | 5,290,000.00 USD | 505,810.00 USD |
| `1D` | `2480.00` | 801,880,000.00 USD | 801,880,000.00 USD | 0.00 USD | 0.00 USD | 27,720.00 USD | 518,550.00 USD |
| `7D` | `2480.60` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 0.00 USD | 1,070,000.00 USD | 350,090.00 USD | 0.00 USD |
| `1D` | `2482.60` | 802,510,000.00 USD | 802,510,000.00 USD | 0.00 USD | 628,130.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2483.40` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 0.00 USD | 1,310,000.00 USD | 1,290,000.00 USD | 2,070,000.00 USD |
| `7D` | `2486.20` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 0.00 USD | 586,480.00 USD | 1,240,000.00 USD | 0.00 USD |
| `7D` | `2489.00` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 0.00 USD | 1,020,000.00 USD | 857,130.00 USD | 2,100,000.00 USD |
| `7D` | `2491.80` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 0.00 USD | 2,400,000.00 USD | 3,310,000.00 USD | 1,720,000.00 USD |
| `7D` | `2494.60` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,950,000.00 USD | 6,220,000.00 USD |
| `7D` | `2497.40` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 3,640,000.00 USD | 3,570,000.00 USD | 4,430,000.00 USD |
| `7D` | `2500.20` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 0.00 USD | 1,160,000.00 USD | 2,430,000.00 USD | 1,090,000.00 USD |
| `7D` | `2503.00` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 0.00 USD | 111,800.00 USD | 1,430,000.00 USD | 170,270.00 USD |
| `7D` | `2505.80` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 0.00 USD | 4,240,000.00 USD | 2,320,000.00 USD | 2,040,000.00 USD |
| `7D` | `2508.60` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 0.00 USD | 714,660.00 USD | 1,270,000.00 USD | 629,120.00 USD |
| `7D` | `2511.40` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 0.00 USD | 1,900,000.00 USD | 3,230,000.00 USD | 2,010,000.00 USD |
| `7D` | `2514.20` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 0.00 USD | 776,920.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2517.00` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 0.00 USD | 97,050.00 USD | 189,640.00 USD | 0.00 USD |
| `7D` | `2519.80` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD |
| `1D` | `2521.60` | 802,740,000.00 USD | 802,740,000.00 USD | 0.00 USD | 80,610.00 USD | 61,830.00 USD | 90,130.00 USD |
| `7D` | `2522.60` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 0.00 USD | 1,050,000.00 USD | 0.00 USD | 945,860.00 USD |
| `1D` | `2524.20` | 803,190,000.00 USD | 803,190,000.00 USD | 0.00 USD | 421,540.00 USD | 0.00 USD | 30,180.00 USD |
| `7D` | `2525.40` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 0.00 USD | 307,040.00 USD | 224,130.00 USD | 200,040.00 USD |
| `1D` | `2526.80` | 803,270,000.00 USD | 803,270,000.00 USD | 0.00 USD | 0.00 USD | 57,450.00 USD | 23,500.00 USD |
| `7D` | `2528.20` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 0.00 USD | 1,580,000.00 USD | 1,690,000.00 USD | 727,590.00 USD |
| `1D` | `2529.40` | 804,960,000.00 USD | 804,960,000.00 USD | 0.00 USD | 583,810.00 USD | 645,910.00 USD | 464,460.00 USD |
| `7D` | `2531.00` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 0.00 USD | 2,080,000.00 USD | 1,480,000.00 USD | 1,230,000.00 USD |
| `1D` | `2532.00` | 805,720,000.00 USD | 805,720,000.00 USD | 0.00 USD | 752,010.00 USD | 0.00 USD | 7,120.00 USD |
| `7D` | `2533.80` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 0.00 USD | 2,750,000.00 USD | 1,730,000.00 USD | 1,370,000.00 USD |
| `1D` | `2534.60` | 806,320,000.00 USD | 806,320,000.00 USD | 0.00 USD | 54,030.00 USD | 41,990.00 USD | 499,440.00 USD |
| `7D` | `2536.60` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 0.00 USD | 3,590,000.00 USD | 2,850,000.00 USD | 2,750,000.00 USD |
| `1D` | `2537.20` | 811,050,000.00 USD | 811,050,000.00 USD | 0.00 USD | 2,220,000.00 USD | 901,140.00 USD | 1,610,000.00 USD |
| `7D` | `2539.40` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 2,620,000.00 USD | 2,580,000.00 USD | 1,090,000.00 USD |
| `1D` | `2539.80` | 813,640,000.00 USD | 813,640,000.00 USD | 0.00 USD | 1,140,000.00 USD | 820,030.00 USD | 632,440.00 USD |
| `7D` | `2542.20` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 3,400,000.00 USD | 2,620,000.00 USD | 2,230,000.00 USD |
| `1D` | `2542.40` | 816,090,000.00 USD | 816,090,000.00 USD | 0.00 USD | 1,100,000.00 USD | 1,330,000.00 USD | 19,390.00 USD |
| `1D` | `2545.00` | 816,650,000.00 USD | 816,650,000.00 USD | 0.00 USD | 227,010.00 USD | 322,670.00 USD | 8,690.00 USD |
| `7D` | `2545.00` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 0.00 USD | 2,170,000.00 USD | 1,830,000.00 USD | 1,350,000.00 USD |
| `1D` | `2547.60` | 820,270,000.00 USD | 820,270,000.00 USD | 0.00 USD | 1,540,000.00 USD | 1,330,000.00 USD | 745,450.00 USD |
| `7D` | `2547.80` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 938,680.00 USD | 2,940,000.00 USD |
| `1D` | `2550.20` | 823,460,000.00 USD | 823,460,000.00 USD | 0.00 USD | 1,260,000.00 USD | 1,450,000.00 USD | 483,830.00 USD |
| `7D` | `2550.60` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 0.00 USD | 2,920,000.00 USD | 2,720,000.00 USD | 1,610,000.00 USD |
| `1D` | `2552.80` | 824,620,000.00 USD | 824,620,000.00 USD | 0.00 USD | 781,250.00 USD | 149,300.00 USD | 225,630.00 USD |
| `7D` | `2553.40` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 0.00 USD | 2,590,000.00 USD | 756,730.00 USD | 2,090,000.00 USD |
| `1D` | `2555.40` | 825,880,000.00 USD | 825,880,000.00 USD | 0.00 USD | 791,770.00 USD | 203,910.00 USD | 266,770.00 USD |
| `7D` | `2556.20` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 0.00 USD | 2,760,000.00 USD | 255,750.00 USD | 4,940,000.00 USD |
| `1D` | `2558.00` | 827,870,000.00 USD | 827,870,000.00 USD | 0.00 USD | 758,880.00 USD | 415,210.00 USD | 808,860.00 USD |
| `7D` | `2559.00` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 0.00 USD | 4,380,000.00 USD | 1,640,000.00 USD | 2,340,000.00 USD |
| `1D` | `2560.60` | 831,960,000.00 USD | 831,960,000.00 USD | 0.00 USD | 1,840,000.00 USD | 1,090,000.00 USD | 1,170,000.00 USD |
| `7D` | `2561.80` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 0.00 USD | 2,260,000.00 USD | 1,960,000.00 USD | 802,060.00 USD |
| `1D` | `2563.20` | 834,190,000.00 USD | 834,190,000.00 USD | 0.00 USD | 440,660.00 USD | 802,390.00 USD | 984,190.00 USD |
| `7D` | `2564.60` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 0.00 USD | 1,800,000.00 USD | 2,100,000.00 USD | 1,100,000.00 USD |
| `1D` | `2565.80` | 834,750,000.00 USD | 834,750,000.00 USD | 0.00 USD | 160,570.00 USD | 403,100.00 USD | 0.00 USD |
| `7D` | `2567.40` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 0.00 USD | 575,630.00 USD | 1,240,000.00 USD | 2,690,000.00 USD |
| `1D` | `2568.40` | 835,100,000.00 USD | 835,100,000.00 USD | 0.00 USD | 46,810.00 USD | 0.00 USD | 304,180.00 USD |
| `7D` | `2570.20` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 0.00 USD | 125,250.00 USD | 290,680.00 USD | 1,210,000.00 USD |
| `1D` | `2571.00` | 835,710,000.00 USD | 835,710,000.00 USD | 0.00 USD | 422,490.00 USD | 182,720.00 USD | 3,580.00 USD |
| `7D` | `2573.00` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,770,000.00 USD |
| `1D` | `2573.60` | 837,080,000.00 USD | 837,080,000.00 USD | 0.00 USD | 549,360.00 USD | 400,040.00 USD | 419,370.00 USD |
| `7D` | `2575.80` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 0.00 USD | 2,180,000.00 USD | 344,620.00 USD | 1,060,000.00 USD |
| `1D` | `2576.20` | 837,720,000.00 USD | 837,720,000.00 USD | 0.00 USD | 539,390.00 USD | 0.00 USD | 96,180.00 USD |
| `7D` | `2578.60` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 0.00 USD | 797,100.00 USD | 1,500,000.00 USD | 1,760,000.00 USD |
| `1D` | `2578.80` | 837,820,000.00 USD | 837,820,000.00 USD | 0.00 USD | 61,010.00 USD | 31,550.00 USD | 8,540.00 USD |
| `1D` | `2581.40` | 839,140,000.00 USD | 839,140,000.00 USD | 0.00 USD | 490,860.00 USD | 416,230.00 USD | 413,100.00 USD |
| `7D` | `2581.40` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 0.00 USD | 3,860,000.00 USD | 895,740.00 USD | 3,210,000.00 USD |
| `1D` | `2584.00` | 839,970,000.00 USD | 839,970,000.00 USD | 0.00 USD | 420,950.00 USD | 226,990.00 USD | 182,690.00 USD |
| `7D` | `2584.20` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 0.00 USD | 88,840.00 USD | 1,820,000.00 USD | 1,570,000.00 USD |
| `1D` | `2586.60` | 840,580,000.00 USD | 840,580,000.00 USD | 0.00 USD | 0.00 USD | 13,230.00 USD | 596,890.00 USD |
| `7D` | `2587.00` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 0.00 USD | 2,360,000.00 USD | 1,800,000.00 USD | 1,510,000.00 USD |
| `1D` | `2589.20` | 842,330,000.00 USD | 842,330,000.00 USD | 0.00 USD | 1,120,000.00 USD | 16,610.00 USD | 619,100.00 USD |
| `7D` | `2589.80` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 0.00 USD | 2,470,000.00 USD | 287,400.00 USD | 2,590,000.00 USD |
| `1D` | `2591.80` | 844,730,000.00 USD | 844,730,000.00 USD | 0.00 USD | 818,160.00 USD | 416,510.00 USD | 1,160,000.00 USD |
| `7D` | `2592.60` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 0.00 USD | 2,300,000.00 USD | 1,280,000.00 USD | 1,130,000.00 USD |
| `1D` | `2594.40` | 846,430,000.00 USD | 846,430,000.00 USD | 0.00 USD | 488,970.00 USD | 525,250.00 USD | 684,070.00 USD |
| `1D` | `2595.10` | 847,940,000.00 USD | 847,940,000.00 USD | 0.00 USD | 526,760.00 USD | 693,240.00 USD | 291,980.00 USD |
| `7D` | `2595.40` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 0.00 USD | 413,920.00 USD | 569,790.00 USD | 1,240,000.00 USD |
| `7D` | `2598.20` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 0.00 USD | 2,280,000.00 USD | 1,910,000.00 USD | 2,570,000.00 USD |
| `7D` | `2601.00` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 0.00 USD | 931,390.00 USD | 1,670,000.00 USD | 955,630.00 USD |
| `7D` | `2603.80` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,580,000.00 USD | 1,690,000.00 USD |
| `7D` | `2606.60` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 0.00 USD | 1,480,000.00 USD | 463,200.00 USD | 312,730.00 USD |
| `7D` | `2609.40` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 0.00 USD | 1,090,000.00 USD | 489,790.00 USD | 10,700.00 USD |
| `7D` | `2612.20` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 0.00 USD | 770,330.00 USD | 608,060.00 USD | 43,560.00 USD |
| `7D` | `2615.00` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 0.00 USD | 1,060,000.00 USD | 1,000,000.00 USD | 635,670.00 USD |
| `7D` | `2617.80` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 0.00 USD | 1,550,000.00 USD | 209,240.00 USD | 434,750.00 USD |
| `7D` | `2620.60` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 0.00 USD | 465,960.00 USD | 1,530,000.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `29.72B` | Total OI Tokens: `12,776,205.9 ETH`
  * 1h OI Change: `-0.72%` | 4h OI Change: `-2.23%` | 24h OI Change: `-0.45%`
  * Exchange Breakdown: Binance=`8.82B` | Bybit=`2.11B` | OKX=`1.77B` | Hyperliquid=`2.53B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `1.11M` | Last 24h: `2.27M` | Last 3d: `7.66M` | Last 7d: `13.85M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0074%` | **USDT KuCoin** | `0.0077%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0099%` | **USDT Bitget** | `0.0051%` |
| **CoinM Binance** | `0.0089%` | **CoinM OKX** | `0.0080%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `46.45%` | `53.55%` | `0.87` | 613,020,000.00 USD |
| `15M` | `Binance` | `46.87%` | `53.13%` | `0.88` | 164,660,000.00 USD |
| `15M` | `OKX` | `45.3%` | `54.7%` | `0.83` | 89,090,000.00 USD |
| `15M` | `Bybit` | `38.42%` | `61.58%` | `0.62` | 57,650,000.00 USD |
| `15M` | `KuCoin` | `50%` | `50%` | `1.00` | 3,440,000.00 USD |
| `15M` | `Gate` | `53.86%` | `46.14%` | `1.17` | 75,720,000.00 USD |
| `15M` | `Bitget` | `47.17%` | `52.83%` | `0.89` | 30,390,000.00 USD |
| `15M` | `BingX` | `62.07%` | `37.93%` | `1.64` | 11,830,000.00 USD |
| `15M` | `MEXC` | `56.66%` | `43.34%` | `1.31` | 42,410,000.00 USD |
| `15M` | `Bitunix` | `52.43%` | `47.57%` | `1.10` | 42,120,000.00 USD |
| `15M` | `Hyperliquid` | `29.43%` | `70.57%` | `0.42` | 38,300,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `59.12%` | `40.88%` | `1.45` | 5,070,000.00 USD |
| `15M` | `Crypto.com` | `51.19%` | `48.81%` | `1.05` | 4,320,000.00 USD |
| `15M` | `WhiteBIT` | `42.73%` | `57.27%` | `0.75` | 4,720,000.00 USD |
| `15M` | `HTX` | `45.33%` | `54.67%` | `0.83` | 2,430,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `34.25%` | `65.75%` | `0.52` | 18,330,000.00 USD |
| `15M` | `Bitfinex` | `20.48%` | `79.52%` | `0.26` | 574,770.00 USD |
| `15M` | `Kraken` | `22.48%` | `77.52%` | `0.29` | 6,620,000.00 USD |
| `15M` | `Aster` | `52.2%` | `47.8%` | `1.09` | 5,720,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `44.71%` | `55.29%` | `0.81` | 9,620,000.00 USD |
| `15M` | `Whale Positions` | `46.87%` | `53.13%` | `0.88` | 164,660,000.00 USD |
| `15M` | `Global Accounts` | `46.45%` | `53.55%` | `0.87` | 613,020,000.00 USD |
| `1H` | `ETH` | `48.96%` | `51.04%` | `0.96` | 2,170,000,000.00 USD |
| `1H` | `Binance` | `46.86%` | `53.14%` | `0.88` | 556,670,000.00 USD |
| `1H` | `OKX` | `47.51%` | `52.49%` | `0.91` | 309,870,000.00 USD |
| `1H` | `Bybit` | `42.11%` | `57.89%` | `0.73` | 197,970,000.00 USD |
| `1H` | `KuCoin` | `46.85%` | `53.15%` | `0.88` | 9,050,000.00 USD |
| `1H` | `Gate` | `54.52%` | `45.48%` | `1.20` | 262,510,000.00 USD |
| `1H` | `Bitget` | `53.49%` | `46.51%` | `1.15` | 113,480,000.00 USD |
| `1H` | `BingX` | `57.16%` | `42.84%` | `1.33` | 48,480,000.00 USD |
| `1H` | `MEXC` | `51.92%` | `48.08%` | `1.08` | 139,880,000.00 USD |
| `1H` | `Bitunix` | `56.84%` | `43.16%` | `1.32` | 139,650,000.00 USD |
| `1H` | `Hyperliquid` | `40.79%` | `59.21%` | `0.69` | 141,520,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.72%` | `48.28%` | `1.07` | 16,770,000.00 USD |
| `1H` | `Crypto.com` | `52.23%` | `47.77%` | `1.09` | 23,450,000.00 USD |
| `1H` | `WhiteBIT` | `32.56%` | `67.44%` | `0.48` | 38,020,000.00 USD |
| `1H` | `HTX` | `43.08%` | `56.92%` | `0.76` | 9,280,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `59.64%` | `40.36%` | `1.48` | 88,600,000.00 USD |
| `1H` | `Bitfinex` | `27.24%` | `72.76%` | `0.37` | 1,420,000.00 USD |
| `1H` | `Kraken` | `42.68%` | `57.32%` | `0.74` | 15,110,000.00 USD |
| `1H` | `Aster` | `50.14%` | `49.86%` | `1.01` | 22,310,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `48.53%` | `51.47%` | `0.94` | 34,580,000.00 USD |
| `1H` | `Whale Positions` | `46.86%` | `53.14%` | `0.88` | 556,670,000.00 USD |
| `1H` | `Global Accounts` | `48.96%` | `51.04%` | `0.96` | 2,170,000,000.00 USD |
| `4H` | `ETH` | `48.48%` | `51.52%` | `0.94` | 15,840,000,000.00 USD |
| `4H` | `Binance` | `46.02%` | `53.98%` | `0.85` | 4,890,000,000.00 USD |
| `4H` | `OKX` | `47.52%` | `52.48%` | `0.91` | 2,230,000,000.00 USD |
| `4H` | `Bybit` | `48.21%` | `51.79%` | `0.93` | 1,570,000,000.00 USD |
| `4H` | `KuCoin` | `38.47%` | `61.53%` | `0.63` | 67,690,000.00 USD |
| `4H` | `Gate` | `50.92%` | `49.08%` | `1.04` | 1,810,000,000.00 USD |
| `4H` | `Bitget` | `46.18%` | `53.82%` | `0.86` | 918,150,000.00 USD |
| `4H` | `BingX` | `52.62%` | `47.38%` | `1.11` | 318,220,000.00 USD |
| `4H` | `MEXC` | `49.88%` | `50.12%` | `1.00` | 876,220,000.00 USD |
| `4H` | `Bitunix` | `48.62%` | `51.38%` | `0.95` | 828,350,000.00 USD |
| `4H` | `Hyperliquid` | `52.68%` | `47.32%` | `1.11` | 857,890,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.09%` | `48.91%` | `1.04` | 105,540,000.00 USD |
| `4H` | `Crypto.com` | `48.31%` | `51.69%` | `0.93` | 113,650,000.00 USD |
| `4H` | `WhiteBIT` | `63.83%` | `36.17%` | `1.76` | 315,190,000.00 USD |
| `4H` | `HTX` | `45.21%` | `54.79%` | `0.83` | 66,730,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `54.71%` | `45.29%` | `1.21` | 327,370,000.00 USD |
| `4H` | `Bitfinex` | `48.86%` | `51.14%` | `0.96` | 11,980,000.00 USD |
| `4H` | `Kraken` | `48.82%` | `51.18%` | `0.95` | 116,090,000.00 USD |
| `4H` | `Aster` | `45.6%` | `54.4%` | `0.84` | 179,580,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `49.93%` | `50.07%` | `1.00` | 222,360,000.00 USD |
| `4H` | `Whale Positions` | `46.02%` | `53.98%` | `0.85` | 4,890,000,000.00 USD |
| `4H` | `Global Accounts` | `48.48%` | `51.52%` | `0.94` | 15,840,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `2358.25` | `2354.41` | `2358.25` | `2359.25` | `2350.25` | 125,220,561.61 USD | 53,594,674.80 USD | 71,625,886.81 USD | -18,031,212.02 USD | `-14.40%` | `0B / 1S` |
| `5:00 UTC` | `2353.75` | `2353.63` | `2353.75` | `2358.25` | `2350.75` | 70,925,128.95 USD | 26,607,996.94 USD | 44,317,132.01 USD | -17,709,135.06 USD | `-24.97%` | `0B / 2S` |
| `0:00 UTC` | `2350.75` | `2351.46` | `2350.75` | `2353.75` | `2348.75` | 91,943,279.10 USD | 36,371,657.16 USD | 55,571,621.93 USD | -19,199,964.77 USD | `-20.88%` | `0B / 3S` |
| `5:00 UTC` | `2350.25` | `2349.30` | `2350.25` | `2352.75` | `2346.75` | 77,932,643.01 USD | 38,640,268.57 USD | 39,292,374.44 USD | -652,105.87 USD | `-0.84%` | `1B / 1S` |
| `0:00 UTC` | `2340.25` | `2342.19` | `2340.25` | `2353.25` | `2334.75` | 172,183,772.38 USD | 75,695,646.18 USD | 96,488,126.21 USD | -20,792,480.03 USD | `-12.08%` | `0B / 3S` |
| `5:00 UTC` | `2335.75` | `2335.37` | `2335.75` | `2340.75` | `2330.75` | 125,556,310.13 USD | 63,692,130.92 USD | 61,864,179.21 USD | 1,827,951.70 USD | `+1.46%` | `1B / 1S` |
| `0:00 UTC` | `2337.75` | `2338.67` | `2337.75` | `2341.75` | `2335.75` | 48,324,873.75 USD | 25,087,349.31 USD | 23,237,524.44 USD | 1,849,824.87 USD | `+3.83%` | `0B / 0S` |
| `5:00 UTC` | `2340.25` | `2338.33` | `2340.25` | `2342.25` | `2333.75` | 43,794,873.23 USD | 24,013,000.37 USD | 19,781,872.86 USD | 4,231,127.51 USD | `+9.66%` | `0B / 2S` |
| `0:00 UTC` | `2327.25` | `2327.16` | `2327.25` | `2335.25` | `2323.25` | 195,411,305.09 USD | 64,523,153.35 USD | 130,888,151.74 USD | -66,364,998.40 USD | `-33.96%` | `0B / 9S` |
| `5:00 UTC` | `2326.25` | `2328.32` | `2326.25` | `2331.25` | `2325.75` | 22,481,991.97 USD | 14,323,703.92 USD | 8,158,288.06 USD | 6,165,415.86 USD | `+27.42%` | `4B / 0S` |

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
| `5m` | 4,620,000.00 USD | -10,520,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -5,970,000.00 USD | -129,480,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 1,950,000.00 USD | -137,320,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -832,990.00 USD | -126,550,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -9,930,000.00 USD | -300,000,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,900,000.00 USD | -344,370,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 14,830,000.00 USD | -117,910,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 14,240,000.00 USD | -195,750,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 32,020,000.00 USD | -168,580,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -23,200,000.00 USD | -544,120,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -11,130,000.00 USD | -1,130,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,020,000,000.00 USD | -8,320,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+4.62M` | 15m=`-5.97M` | 1h=`-832.99K` | 24h=`-23.20M`
* Futures Capital Netflows: 5m=`-10.52M` | 15m=`-129.48M` | 1h=`-126.55M` | 24h=`-544.12M`
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
  * `2026-10-30 00:16:45 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:45 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:45 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:19:45 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:21:45 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:21:45 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:21:45 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `2285.49` (Risk Distance: `11.63` pts)
  * +2.5R Take Profit: `2326.20`
  * Mathematical Lot Sizing: **`0.85 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2338.45` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2350.08` (Risk Distance: `11.63` pts)
  * +2.5R Take Profit: `2309.37`
  * Mathematical Lot Sizing: **`0.85 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2345.57`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
