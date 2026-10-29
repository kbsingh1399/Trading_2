# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 02:09:26 IST` (`2026-10-29 20:39:26 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2297.10` | **Live Ask Quote**: `2300.70` | **Mid Price**: `2298.90`
- **Spread Points**: `360.00` | **Spread BPS**: `15.66 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2323.68` | VWAP Z-Score: `-0.60` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `11.70` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `36.14` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2376.87` | Lower -3.00σ Band: `2270.49`
  * Upper +2.51σ Band: `2368.18` | Lower -2.51σ Band: `2279.18`
  * Upper +2.01σ Band: `2359.32` | Lower -2.01σ Band: `2288.04`
  * Upper +2.00σ Band: `2359.14` | Lower -2.00σ Band: `2288.22`
  * Upper +1.28σ Band: `2346.37` | Lower -1.28σ Band: `2300.99`
  * Upper +1.00σ Band: `2341.41` | Lower -1.00σ Band: `2305.95`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2324.73` | EMA-20=`2330.60` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2330.61` (Slope: `+0.0000`) | EMA-100=`2330.89`
  * Institutional Anchors: EMA-144=`2330.87` | EMA-200=`2330.00` (Slope: `-0.0150`) | EMA-233=`2329.73`
- **Range Boundaries**: 24H High=`2374.90` | 24H Low=`2288.80` | Weekly High=`2387.80` | Weekly Low=`2288.80`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2335.43` (Distance: `-2.04%`)
  * Point of Control (POC) = `2318.90` (Distance: `-1.34%`)
  * Value Area Low (VAL) = `2298.09` (Distance: `-0.45%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2367.21` | POC=`2350.17` | VAL=`2335.02`
  * Prior Day Extremes: PDH=`2387.80` | PDL=`2316.80` | PDC=`2356.60`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2339.99` | Weekly POC=`2308.58` | Weekly VAL=`2299.50`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2367.70` | Low=`2288.80`
  * London Session (08:00-16:00 UTC): High=`2331.00` | Low=`2299.00`
  * New York Session (13:00-21:00 UTC): High=`2374.90` | Low=`2307.50`
  * Initial Balance (First Hour): IB High=`2331.00` | IB Low=`2299.30`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2289.70` - `2308.10`
  * Optimal Trade Entry (OTE 0.705): `2303.50`
  * Structural Invalidation Anchor (0.786): `2317.29`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2317.38` | `2318.97` | `2313.55` | `2315.91` | `9,389` | 21,750,469.58 USD | 3,533,988.89 USD | `+16.25%` | -418,630,845.30 USD | `+0.36` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `2315.91` | `2318.93` | `2313.70` | `2316.29` | `16,477` | 38,155,889.30 USD | -8,870,484.92 USD | `-23.25%` | -427,501,330.22 USD | `-0.25` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `2316.30` | `2319.33` | `2293.22` | `2293.68` | `89,001` | 204,958,459.15 USD | -82,524,860.15 USD | `-40.26%` | -510,026,190.37 USD | `-2.88` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `2335.68` | `2335.92` | `2302.29` | `2314.66` | `213,441` | 493,862,056.10 USD | -85,150,839.70 USD | `-17.24%` | -423,421,399.14 USD | `-2.59` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `2314.67` | `2318.97` | `2312.06` | `2316.29` | `38,399` | 88,922,002.19 USD | 4,750,768.08 USD | `+5.34%` | -418,670,631.06 USD | `+0.66` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `2316.30` | `2319.33` | `2287.88` | `2289.06` | `113,099` | 260,148,181.58 USD | -94,406,404.58 USD | `-36.29%` | -513,077,035.64 USD | `-2.43` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `2340.61` | `2342.29` | `2323.01` | `2330.23` | `146,197` | 340,744,443.34 USD | -42,605,787.87 USD | `-12.50%` | -327,552,864.00 USD | `-0.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2330.22` | `2338.58` | `2325.76` | `2335.68` | `63,571` | 148,285,696.23 USD | -15,505,202.15 USD | `-10.46%` | -343,058,066.15 USD | `+0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `2335.68` | `2335.92` | `2293.22` | `2293.68` | `340,841` | 787,742,517.44 USD | -162,924,931.77 USD | `-20.68%` | -505,982,997.92 USD | `-2.51` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -163,611,405.07 USD | `+1.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -365,767,522.01 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2293.22` | `2293.68` | `340,841` | 787,742,517.44 USD | -162,924,931.77 USD | `-20.68%` | -528,692,453.78 USD | `-0.70` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `2308.03` | `2334.83` | `2303.75` | `2309.10` | `525,175` | 1,216,920,375.04 USD | -34,916,746.14 USD | `-2.87%` | -218,489,329.59 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2309.10` | `2330.05` | `2308.88` | `2324.26` | `409,016` | 949,400,649.22 USD | -49,162,247.72 USD | `-5.18%` | -267,651,577.31 USD | `+0.60` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -163,611,405.07 USD | `+1.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -365,767,522.01 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2293.22` | `2293.68` | `340,841` | 787,742,517.44 USD | -162,924,931.77 USD | `-20.68%` | -528,692,453.78 USD | `-0.70` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`2298.90`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2292.60` | `3.9059` | 8,954.67 USD | 416,980.52 USD | `4 orders` | `-0.10%` | `-` |
| `BID` | `2292.70` | `3.4892` | 7,999.69 USD | 408,025.85 USD | `2 orders` | `-0.09%` | `-` |
| `BID` | `2292.80` | `20.6465` | 47,338.30 USD | 400,026.17 USD | `5 orders` | `-0.09%` | `-` |
| `BID` | `2292.90` | `8.1290` | 18,638.98 USD | 352,687.87 USD | `5 orders` | `-0.08%` | `-` |
| `BID` | `2293.00` | `22.5764` | 51,767.69 USD | 334,048.89 USD | `5 orders` | `-0.08%` | `-` |
| `BID` | `2293.10` | `1.0597` | 2,430.00 USD | 282,281.20 USD | `20 orders` | `-0.08%` | `-` |
| `BID` | `2293.20` | `2.1188` | 4,858.83 USD | 279,851.20 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `2293.30` | `24.7192` | 56,688.54 USD | 274,992.37 USD | `10 orders` | `-0.07%` | `-` |
| `BID` | `2293.40` | `0.3488` | 799.94 USD | 218,303.83 USD | `3 orders` | `-0.06%` | `-` |
| `BID` | `2293.50` | `21.4384` | 49,168.97 USD | 217,503.89 USD | `27 orders` | `-0.06%` | `-` |
| `BID` | `2293.60` | `0.0600` | 137.62 USD | 168,334.92 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `2293.70` | `7.3432` | 16,843.10 USD | 168,197.31 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `2293.80` | `16.1715` | 37,094.19 USD | 151,354.21 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `2293.90` | `0.0880` | 201.86 USD | 114,260.02 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `2294.00` | `1.9971` | 4,581.35 USD | 114,058.16 USD | `5 orders` | `-0.04%` | `-` |
| `BID` | `2294.10` | `0.1144` | 262.45 USD | 109,476.81 USD | `22 orders` | `-0.03%` | `-` |
| `BID` | `2294.20` | `0.6516` | 1,494.90 USD | 109,214.37 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `2294.30` | `28.8259` | 66,135.26 USD | 107,719.46 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `2294.50` | `1.0912` | 2,503.76 USD | 41,584.20 USD | `5 orders` | `-0.02%` | `-` |
| `BID` | `2294.80` | `17.0300` | 39,080.44 USD | 39,080.44 USD | `2 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2294.85` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,294.85` | `0.00%` | `-` |
| `ASK` | `2294.90` | `61.8241` | 141,880.13 USD | 141,880.13 USD | `8 orders` | `+0.00%` | `-` |
| `ASK` | `2295.00` | `25.1351` | 57,685.05 USD | 199,565.18 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `2295.10` | `206.3876` | 473,680.18 USD | 673,245.36 USD | `21 orders` | `+0.01%` | `-` |
| `ASK` | `2295.20` | `252.9344` | 580,535.03 USD | 1,253,780.40 USD | `25 orders` | `+0.02%` | `-` |
| `ASK` | `2295.30` | `118.5815` | 272,180.12 USD | 1,525,960.51 USD | `18 orders` | `+0.02%` | `-` |
| `ASK` | `2295.40` | `148.8441` | 341,656.75 USD | 1,867,617.26 USD | `16 orders` | `+0.02%` | `-` |
| `ASK` | `2295.50` | `92.4619` | 212,246.29 USD | 2,079,863.55 USD | `15 orders` | `+0.03%` | `-` |
| `ASK` | `2295.60` | `772.2585` | 1,772,796.61 USD | 3,852,660.17 USD | `19 orders` | `+0.03%` | `-` |
| `ASK` | `2295.70` | `23.0170` | 52,840.13 USD | 3,905,500.29 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `2295.80` | `567.9061` | 1,303,798.82 USD | 5,209,299.12 USD | `19 orders` | `+0.04%` | `-` |
| `ASK` | `2295.90` | `85.5335` | 196,376.36 USD | 5,405,675.48 USD | `13 orders` | `+0.05%` | `-` |
| `ASK` | `2296.00` | `210.1498` | 482,503.94 USD | 5,888,179.42 USD | `11 orders` | `+0.05%` | `-` |
| `ASK` | `2296.10` | `122.1987` | 280,580.44 USD | 6,168,759.86 USD | `13 orders` | `+0.05%` | `-` |
| `ASK` | `2296.20` | `51.5999` | 118,483.69 USD | 6,287,243.55 USD | `9 orders` | `+0.06%` | `-` |
| `ASK` | `2296.30` | `97.1502` | 223,086.00 USD | 6,510,329.55 USD | `10 orders` | `+0.06%` | `-` |
| `ASK` | `2296.40` | `7.8496` | 18,025.82 USD | 6,528,355.37 USD | `4 orders` | `+0.07%` | `-` |
| `ASK` | `2296.50` | `26.8727` | 61,713.16 USD | 6,590,068.53 USD | `6 orders` | `+0.07%` | `-` |
| `ASK` | `2296.60` | `2.8147` | 6,464.24 USD | 6,596,532.77 USD | `1 orders` | `+0.08%` | `-` |
| `ASK` | `2296.70` | `88.3595` | 202,935.26 USD | 6,799,468.03 USD | `5 orders` | `+0.08%` | `-` |
| `ASK` | `2296.80` | `41.6630` | 95,691.58 USD | 6,895,159.61 USD | `7 orders` | `+0.08%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:04:34 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 02:04:34 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1918.00` | `4,184.01` | 8,024,935.59 USD | `TRIGGER_STOP` | `0x6ea486a342` | `2026-10-30 02:04:34 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `8,500.00` | 16,371,850.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-30 02:04:34 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2250.00` | `6,500.00` | 14,625,000.00 USD | `TRIGGER_STOP` | `0x6eae4120a8` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2270.00` | `881.06` | 1,999,999.84 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x9c062c0575` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2274.10` | `2,042.44` | 4,644,722.81 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2285.60` | `1,422.45` | 3,251,160.18 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2286.10` | `5,312.54` | 12,145,008.90 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 02:04:34 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2292.00` | `2,500.00` | 5,730,000.00 USD | `TRIGGER_STOP` | `0x934de82f50` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2294.30` | `977.21` | 2,242,013.59 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2295.00` | `334.43` | 767,507.67 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2295.10` | `609.40` | 1,398,629.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2295.40` | `348.56` | 800,091.51 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2301.00` | `2,740.15` | 6,305,095.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2301.10` | `384.37` | 884,481.86 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x7b7f72a28f` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2301.20` | `439.74` | 1,011,938.89 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2302.50` | `609.34` | 1,402,996.14 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2303.10` | `685.80` | 1,579,455.16 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2304.10` | `1,738.04` | 4,004,617.27 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2306.30` | `609.29` | 1,405,210.14 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:04:34 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2307.20` | `599,999.99` | 1,384,319,976.93 USD | `TRIGGER_STOP` | `0x069604ebfb` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2307.40` | `867.77` | 2,002,302.88 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2307.50` | `1,301.64` | 3,003,545.61 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2307.70` | `480.03` | 1,107,772.85 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2308.80` | `1,398.04` | 3,227,790.37 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2308.80` | `439.60` | 1,014,957.72 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2309.90` | `344.55` | 795,870.73 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x76bf72092b` | `2026-10-30 02:04:34 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2310.00` | `2,000.00` | 4,620,000.00 USD | `TRIGGER_STOP` | `0x524ed67d71` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2310.60` | `649.95` | 1,501,779.32 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2310.60` | `406.42` | 939,080.98 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2311.00` | `335.11` | 774,440.83 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2311.90` | `433.00` | 1,001,047.38 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2317.70` | `329.87` | 764,544.33 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2318.10` | `330.87` | 766,988.36 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 02:04:34 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2319.00` | `2,500.00` | 5,797,500.00 USD | `TRIGGER_STOP` | `0x524ed67d71` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2319.50` | `343.13` | 795,893.98 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x76bf72092b` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2320.40` | `431.49` | 1,001,240.53 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2320.60` | `406.45` | 943,219.47 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2322.20` | `439.76` | 1,021,206.03 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2322.30` | `646.67` | 1,501,770.57 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2323.50` | `861.79` | 2,002,378.13 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2324.80` | `609.36` | 1,416,647.10 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2325.10` | `461.59` | 1,073,233.61 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2325.40` | `1,398.98` | 3,253,196.93 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2326.10` | `1,291.21` | 3,003,481.25 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2327.70` | `1,720.46` | 4,004,710.32 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2328.60` | `439.95` | 1,024,458.26 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2329.60` | `609.65` | 1,420,240.64 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2330.10` | `682.61` | 1,590,559.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2335.20` | `399.44` | 932,765.98 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x7b7f72a28f` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2335.30` | `2,740.15` | 6,399,083.27 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2335.70` | `1,007.37` | 2,352,918.31 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2338.10` | `609.77` | 1,425,698.56 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2338.20` | `328.25` | 767,507.84 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2338.50` | `342.14` | 800,091.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2344.70` | `1,389.90` | 3,258,899.70 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2350.60` | `5,310.95` | 12,483,916.01 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 02:04:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2356.70` | `2,089.13` | 4,923,448.66 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:04:34 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2440.00` | `4,002.10` | 9,765,127.17 USD | `TRIGGER_STOP` | `0xfb941d2344` | `2026-10-30 02:04:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 243,462,439.68 USD | `106,417.71` | `2322.74` | `2291.50` | `3907.08` | 3,718,572.47 USD | `+1.53%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 150,930,406.07 USD | `65,205.17` | `2375.30` | `2291.50` | `4454.87` | 3,951,857.02 USD | `+2.62%` | `5X Cross` |
| `6` | `0x77dd...e0e9` | `LONG` | 110,957,183.32 USD | `48,499.51` | `2610.31` | `2291.50` | `2171.20` | -15,641,700.54 USD | `-14.10%` | `10X Cross` |
| `7` | `0x0392...d7d9` | `LONG` | 103,511,884.73 USD | `44,734.81` | `2518.71` | `2291.50` | `2180.26` | -9,162,421.85 USD | `-8.85%` | `9X Cross` |
| `15` | `0xde8d...9524` | `LONG` | 70,197,639.55 USD | `30,282.40` | `2134.45` | `2291.50` | `1787.15` | 5,561,308.98 USD | `+7.92%` | `20X Cross` |
| `19` | `0x7fda...17d1` | `SHORT` | 59,827,598.20 USD | `26,119.89` | `2436.71` | `2291.50` | `3819.15` | 3,819,083.09 USD | `+6.38%` | `25X Cross` |
| `25` | `0xdf95...7d72` | `SHORT` | 51,798,834.07 USD | `22,648.26` | `2402.54` | `2291.50` | `4019.74` | 2,614,539.66 USD | `+5.05%` | `25X Cross` |
| `28` | `0xeced...6210` | `SHORT` | 43,211,095.80 USD | `18,687.58` | `2522.09` | `2291.50` | `3345.81` | 3,920,816.65 USD | `+9.07%` | `20X Cross` |
| `34` | `0xb695...a92d` | `SHORT` | 38,295,340.20 USD | `16,704.62` | `2557.74` | `2291.50` | `4086.82` | 4,430,824.85 USD | `+11.57%` | `20X Cross` |
| `35` | `0x6046...b21d` | `LONG` | 36,829,365.66 USD | `15,927.59` | `2410.19` | `2291.50` | `1592.19` | -1,559,253.99 USD | `-4.23%` | `6X Cross` |
| `38` | `0x45d2...4029` | `SHORT` | 31,905,045.00 USD | `13,950.00` | `2443.60` | `2291.50` | `5194.38` | 2,183,237.46 USD | `+6.84%` | `20X Cross` |
| `43` | `0x2371...0883` | `LONG` | 27,640,800.00 USD | `12,000.00` | `2421.77` | `2291.50` | `1280.13` | -1,420,494.85 USD | `-5.14%` | `20X Cross` |
| `44` | `0xbd1c...ff0e` | `LONG` | 27,505,200.00 USD | `12,000.00` | `2419.91` | `2291.50` | `1521.03` | -1,533,832.39 USD | `-5.58%` | `20X Cross` |
| `46` | `0xe813...6d74` | `LONG` | 26,958,828.37 USD | `11,769.84` | `2297.56` | `2291.50` | `475.96` | -83,123.29 USD | `-0.31%` | `25X Cross` |
| `50` | `0xa9de...e049` | `LONG` | 25,510,100.00 USD | `11,000.00` | `2481.81` | `2291.50` | `1644.77` | -1,789,879.46 USD | `-7.02%` | `20X Cross` |
| `51` | `0x0c5d...36b3` | `LONG` | 25,510,100.00 USD | `11,000.00` | `2482.20` | `2291.50` | `1645.10` | -1,794,153.24 USD | `-7.03%` | `20X Cross` |
| `52` | `0x09dc...c094` | `LONG` | 25,485,900.00 USD | `11,000.00` | `2465.31` | `2291.50` | `1638.10` | -1,632,523.04 USD | `-6.41%` | `20X Cross` |
| `55` | `0x6c93...59a4` | `LONG` | 25,359,400.00 USD | `11,000.00` | `2441.15` | `2291.50` | `1603.06` | -1,493,272.73 USD | `-5.89%` | `20X Cross` |
| `56` | `0xa61c...66b9` | `LONG` | 25,216,608.00 USD | `10,888.00` | `2398.32` | `2291.50` | `1424.82` | -896,349.39 USD | `-3.55%` | `10X Cross` |
| `65` | `0x15a4...dfdb` | `LONG` | 23,191,000.00 USD | `10,000.00` | `1761.94` | `2291.50` | `55.52` | 5,571,518.97 USD | `+24.02%` | `20X Cross` |
| `66` | `0xec7f...df39` | `LONG` | 23,165,000.00 USD | `10,000.00` | `2719.35` | `2291.50` | `1721.62` | -4,028,548.52 USD | `-17.39%` | `20X Cross` |
| `69` | `0xa2ce...3126` | `LONG` | 22,958,477.62 USD | `10,016.88` | `2162.83` | `2291.50` | `1476.46` | 1,293,675.57 USD | `+5.63%` | `10X Cross` |
| `70` | `0x4487...c92d` | `SHORT` | 22,924,226.96 USD | `10,001.93` | `2373.98` | `2291.50` | `2870.40` | 820,250.66 USD | `+3.58%` | `10X Cross` |
| `71` | `0x6646...6de5` | `LONG` | 22,919,800.00 USD | `10,000.00` | `1765.80` | `2291.50` | `1726.44` | 5,261,742.55 USD | `+22.96%` | `25X Cross` |
| `75` | `0xaeaa...2416` | `SHORT` | 22,460,350.00 USD | `9,700.00` | `2311.92` | `2291.50` | `2658.71` | -34,667.60 USD | `-0.15%` | `25X Cross` |
| `78` | `0xab81...c608` | `SHORT` | 22,179,926.67 USD | `9,661.51` | `2307.68` | `2291.50` | `2444.03` | 115,804.00 USD | `+0.52%` | `20X Cross` |
| `79` | `0x0622...8088` | `LONG` | 22,119,368.37 USD | `9,671.36` | `2318.68` | `2291.50` | `1273.98` | -305,491.13 USD | `-1.38%` | `5X Cross` |
| `84` | `0xca49...53c8` | `SHORT` | 21,219,790.74 USD | `9,264.26` | `2549.47` | `2291.50` | `3793.06` | 2,399,234.00 USD | `+11.31%` | `25X Cross` |
| `85` | `0xba5d...a352` | `SHORT` | 20,970,252.20 USD | `9,054.12` | `2493.89` | `2291.50` | `2940.24` | 1,609,755.06 USD | `+7.68%` | `20X Cross` |
| `86` | `0xea00...a918` | `LONG` | 20,833,953.68 USD | `9,003.83` | `2003.01` | `2291.50` | `1293.48` | 2,799,174.81 USD | `+13.44%` | `5X Cross` |
| `99` | `0xb37f...66ca` | `SHORT` | 19,486,250.00 USD | `8,500.00` | `2308.30` | `2291.50` | `2709.06` | 134,304.19 USD | `+0.69%` | `25X Cross` |
| `107` | `0x218a...7da2` | `SHORT` | 18,547,659.48 USD | `7,997.78` | `2208.16` | `2291.50` | `2877.27` | -887,264.27 USD | `-4.78%` | `10X Cross` |
| `109` | `0x9eec...daab` | `LONG` | 18,513,911.91 USD | `8,092.45` | `1658.44` | `2291.50` | `1922.71` | 5,093,047.39 USD | `+27.51%` | `15X Cross` |
| `112` | `0x5f91...65aa` | `LONG` | 18,418,266.77 USD | `7,964.66` | `1626.99` | `2291.50` | `2040.74` | 5,459,823.70 USD | `+29.64%` | `16X Cross` |
| `117` | `0xcf53...ee11` | `SHORT` | 17,455,648.57 USD | `7,603.63` | `1862.69` | `2291.50` | `4001.36` | -3,292,384.63 USD | `-18.86%` | `7X Cross` |
| `121` | `0x939f...04d2` | `LONG` | 16,752,744.50 USD | `7,223.81` | `2500.18` | `2291.50` | `1713.17` | -1,308,145.68 USD | `-7.81%` | `25X Cross` |
| `123` | `0x1ee7...edf5` | `LONG` | 16,230,900.00 USD | `7,000.00` | `2330.22` | `2291.50` | `2153.96` | -80,662.20 USD | `-0.50%` | `25X Cross` |
| `124` | `0xec0b...b078` | `LONG` | 16,230,763.03 USD | `7,007.80` | `2065.97` | `2291.50` | `1006.89` | 1,752,833.44 USD | `+10.80%` | `25X Cross` |
| `131` | `0x418a...8888` | `SHORT` | 15,396,146.86 USD | `6,724.38` | `2494.55` | `2291.50` | `2977.47` | 1,378,176.32 USD | `+8.95%` | `25X Cross` |
| `132` | `0x0c4a...1b19` | `LONG` | 15,317,192.27 USD | `6,615.35` | `2373.06` | `2291.50` | `2197.06` | -381,449.72 USD | `-2.49%` | `25X Isolated` |
| `134` | `0x4ff9...38d3` | `LONG` | 15,208,360.28 USD | `6,564.10` | `2447.40` | `2291.50` | `1670.72` | -856,662.47 USD | `-5.63%` | `3X Isolated` |
| `135` | `0xf78c...c581` | `LONG` | 15,043,462.62 USD | `6,500.22` | `2521.53` | `2291.50` | `1914.20` | -1,347,078.33 USD | `-8.95%` | `20X Cross` |
| `140` | `0x799f...5f4c` | `LONG` | 14,616,683.13 USD | `6,310.90` | `2390.33` | `2291.50` | `1735.84` | -468,481.48 USD | `-3.21%` | `20X Cross` |
| `143` | `0x08bf...7872` | `SHORT` | 14,424,852.25 USD | `6,224.05` | `2258.00` | `2291.50` | `2585.96` | -370,936.15 USD | `-2.57%` | `20X Cross` |
| `145` | `0xecb6...2b00` | `SHORT` | 14,269,066.86 USD | `6,235.12` | `2327.06` | `2291.50` | `7034.41` | 240,476.98 USD | `+1.69%` | `15X Cross` |
| `152` | `0xd9e7...4aff` | `LONG` | 13,873,800.00 USD | `6,000.00` | `2480.18` | `2291.50` | `1408.49` | -1,007,324.33 USD | `-7.26%` | `20X Cross` |
| `177` | `0x645b...87b8` | `SHORT` | 11,586,400.88 USD | `5,047.00` | `2421.68` | `2291.50` | `6432.80` | 635,830.31 USD | `+5.49%` | `10X Cross` |
| `181` | `0x45ab...6cbc` | `LONG` | 11,379,725.09 USD | `4,920.96` | `2727.66` | `2291.50` | `1372.23` | -2,043,018.71 USD | `-17.95%` | `7X Cross` |
| `185` | `0x64b7...9da9` | `LONG` | 11,248,439.59 USD | `4,856.84` | `2604.61` | `2291.50` | `1474.64` | -1,401,774.83 USD | `-12.46%` | `25X Cross` |
| `189` | `0xfb18...eb17` | `SHORT` | 11,160,338.48 USD | `4,872.45` | `2315.54` | `2291.50` | `2639.59` | 122,034.55 USD | `+1.09%` | `25X Cross` |
| `194` | `0x5559...d43b` | `SHORT` | 10,997,126.07 USD | `4,755.93` | `2262.69` | `2291.50` | `2843.73` | -235,920.19 USD | `-2.15%` | `25X Cross` |
| `213` | `0xe091...6705` | `SHORT` | 10,405,350.46 USD | `4,500.00` | `2467.33` | `2291.50` | `2573.01` | 697,658.05 USD | `+6.70%` | `20X Cross` |
| `223` | `0xfe7c...b7ae` | `SHORT` | 10,198,406.49 USD | `4,402.58` | `2440.17` | `2291.50` | `4302.38` | 544,681.38 USD | `+5.34%` | `25X Cross` |
| `235` | `0xc179...e0c8` | `LONG` | 9,882,961.04 USD | `4,309.16` | `2342.89` | `2291.50` | `815.41` | -212,917.76 USD | `-2.15%` | `10X Cross` |
| `236` | `0x12d2...f97f` | `LONG` | 9,876,213.06 USD | `4,264.34` | `2623.90` | `2291.50` | `1861.90` | -1,313,021.36 USD | `-13.29%` | `20X Cross` |
| `241` | `0x28bb...fca6` | `SHORT` | 9,749,466.49 USD | `4,209.61` | `1896.10` | `2291.50` | `3041.97` | -1,767,583.92 USD | `-18.13%` | `20X Cross` |
| `244` | `0x6ea4...0ea7` | `SHORT` | 9,690,590.89 USD | `4,184.01` | `2602.13` | `2291.50` | `3426.02` | 1,196,755.78 USD | `+12.35%` | `20X Cross` |
| `249` | `0x3dc9...54b0` | `SHORT` | 9,274,081.67 USD | `3,999.69` | `2480.32` | `2291.50` | `6122.25` | 646,454.89 USD | `+6.97%` | `20X Cross` |
| `250` | `0x95fe...f8fa` | `LONG` | 9,257,200.00 USD | `4,000.00` | `2341.35` | `2291.50` | `2259.02` | -108,216.51 USD | `-1.17%` | `20X Isolated` |
| `253` | `0xfb94...0ddf` | `SHORT` | 9,254,859.26 USD | `4,002.10` | `2382.44` | `2291.50` | `5105.41` | 279,924.89 USD | `+3.02%` | `20X Cross` |
| `256` | `0x77ee...2902` | `SHORT` | 9,220,453.26 USD | `3,982.23` | `2476.53` | `2291.50` | `4294.33` | 641,668.32 USD | `+6.96%` | `25X Cross` |
| `261` | `0x5e9e...35ee` | `SHORT` | 9,179,306.33 USD | `4,007.56` | `1796.39` | `2291.50` | `2586.51` | -1,980,156.24 USD | `-21.57%` | `20X Cross` |
| `262` | `0x8cc9...2b6a` | `SHORT` | 9,148,400.00 USD | `4,000.00` | `1791.18` | `2291.50` | `3940.50` | -1,983,653.33 USD | `-21.68%` | `25X Cross` |
| `272` | `0xf02d...5eb3` | `LONG` | 8,887,275.38 USD | `3,855.99` | `2513.67` | `2291.50` | `333.48` | -805,436.93 USD | `-9.06%` | `20X Cross` |
| `277` | `0x4b67...f4e7` | `LONG` | 8,857,093.61 USD | `3,820.84` | `2591.51` | `2291.50` | `1600.62` | -1,044,679.93 USD | `-11.79%` | `20X Cross` |
| `294` | `0x8ae4...3d60` | `LONG` | 8,241,143.08 USD | `3,558.20` | `2482.21` | `2291.50` | `384.40` | -591,054.95 USD | `-7.17%` | `10X Cross` |
| `320` | `0x9c06...0560` | `SHORT` | 7,658,359.16 USD | `3,303.58` | `2270.55` | `2291.50` | `3340.13` | -157,395.21 USD | `-2.06%` | `25X Cross` |
| `330` | `0x984e...14c2` | `SHORT` | 7,132,986.32 USD | `3,111.99` | `2357.50` | `2291.50` | `2434.98` | 203,536.44 USD | `+2.85%` | `20X Cross` |
| `331` | `0x9c2a...f6a8` | `SHORT` | 7,078,235.87 USD | `3,058.48` | `2543.83` | `2291.50` | `2590.00` | 702,024.76 USD | `+9.92%` | `20X Cross` |
| `340` | `0x007d...67a0` | `LONG` | 6,871,500.00 USD | `3,000.00` | `2400.00` | `2291.50` | `1481.95` | -328,500.00 USD | `-4.78%` | `25X Cross` |
| `341` | `0x4a20...3c26` | `LONG` | 6,861,300.00 USD | `3,000.00` | `2428.72` | `2291.50` | `413.93` | -424,860.28 USD | `-6.19%` | `20X Cross` |
| `343` | `0x39b4...5c34` | `SHORT` | 6,821,768.02 USD | `2,948.17` | `2329.97` | `2291.50` | `2409.15` | 47,386.88 USD | `+0.69%` | `25X Cross` |
| `385` | `0xf517...c032` | `SHORT` | 6,277,026.16 USD | `2,738.07` | `2053.90` | `2291.50` | `5410.20` | -653,284.25 USD | `-10.41%` | `25X Cross` |
| `395` | `0xbb34...1696` | `LONG` | 6,028,620.00 USD | `2,600.00` | `2318.80` | `2291.50` | `1996.74` | -280.85 USD | `-0.00%` | `25X Cross` |
| `396` | `0xc619...10f5` | `LONG` | 6,021,860.00 USD | `2,600.00` | `2318.40` | `2291.50` | `1881.22` | -5,988.91 USD | `-0.10%` | `25X Cross` |
| `398` | `0x8328...f54a` | `SHORT` | 5,975,047.75 USD | `2,576.45` | `2292.01` | `2291.50` | `3280.25` | -69,776.46 USD | `-1.17%` | `25X Cross` |
| `402` | `0xed48...7c9b` | `SHORT` | 5,848,466.67 USD | `2,551.13` | `2460.02` | `2291.50` | `3236.32` | 427,379.74 USD | `+7.31%` | `20X Cross` |
| `403` | `0x934d...92c9` | `LONG` | 5,763,500.00 USD | `2,500.00` | `2343.98` | `2291.50` | `2184.15` | -96,464.51 USD | `-1.67%` | `25X Cross` |
| `421` | `0xfbe2...c8ea` | `SHORT` | 5,511,346.06 USD | `2,404.08` | `2041.57` | `2291.50` | `2659.91` | -603,253.34 USD | `-10.95%` | `20X Cross` |
| `427` | `0x1c98...7fc7` | `LONG` | 5,459,723.62 USD | `2,358.00` | `2467.15` | `2291.50` | `1897.24` | -357,847.86 USD | `-6.55%` | `10X Cross` |
| `448` | `0x6859...7e1e` | `SHORT` | 5,128,766.88 USD | `2,224.58` | `2200.39` | `2291.50` | `3822.09` | -233,814.16 USD | `-4.56%` | `25X Cross` |
| `449` | `0x023a...2355` | `LONG` | 5,107,176.74 USD | `2,232.35` | `2330.15` | `2291.50` | `0.000000` | -94,552.00 USD | `-1.85%` | `25X Cross` |
| `457` | `0xd507...c948` | `SHORT` | 5,007,545.77 USD | `2,172.00` | `2387.49` | `2291.50` | `2707.44` | 178,095.25 USD | `+3.56%` | `5X Isolated` |
| `460` | `0xb829...3a81` | `LONG` | 4,988,673.27 USD | `2,153.91` | `2537.61` | `2291.50` | `757.55` | -477,123.47 USD | `-9.56%` | `20X Cross` |
| `488` | `0xf929...d1f9` | `SHORT` | 4,638,200.00 USD | `2,000.00` | `2423.37` | `2291.50` | `2548.84` | 208,540.34 USD | `+4.50%` | `25X Cross` |
| `490` | `0x3440...32c5` | `SHORT` | 4,633,509.06 USD | `2,000.57` | `2198.21` | `2291.50` | `3572.79` | -235,845.93 USD | `-5.09%` | `25X Cross` |
| `501` | `0x0514...bdfe` | `SHORT` | 4,469,361.00 USD | `1,950.00` | `1988.74` | `2291.50` | `2991.10` | -591,301.37 USD | `-13.23%` | `25X Cross` |
| `508` | `0x8376...9a1e` | `SHORT` | 4,428,720.78 USD | `1,910.50` | `2477.72` | `2291.50` | `3162.12` | 304,967.39 USD | `+6.89%` | `20X Cross` |
| `515` | `0x382b...3e39` | `SHORT` | 4,391,483.76 USD | `1,920.28` | `2298.81` | `2291.50` | `4966.61` | 22,884.24 USD | `+0.52%` | `25X Cross` |
| `532` | `0x7a6d...f79c` | `SHORT` | 4,236,222.69 USD | `1,847.07` | `2432.10` | `2291.50` | `2677.23` | 256,043.39 USD | `+6.04%` | `25X Cross` |
| `540` | `0x7265...91a5` | `LONG` | 4,166,462.61 USD | `1,801.87` | `2533.96` | `2291.50` | `1988.16` | -399,403.84 USD | `-9.59%` | `20X Cross` |
| `541` | `0x739c...cfb2` | `SHORT` | 4,165,020.00 USD | `1,800.00` | `2427.60` | `2291.50` | `2604.56` | 204,676.38 USD | `+4.91%` | `25X Cross` |
| `546` | `0x541e...071d` | `SHORT` | 4,137,962.50 USD | `1,805.00` | `2648.19` | `2291.50` | `3094.98` | 642,022.34 USD | `+15.52%` | `25X Cross` |
| `557` | `0x91a9...3f70` | `SHORT` | 4,091,185.96 USD | `1,767.48` | `2156.23` | `2291.50` | `3654.81` | -280,081.88 USD | `-6.85%` | `4X Cross` |
| `561` | `0xa445...329d` | `LONG` | 4,064,847.05 USD | `1,776.75` | `2398.85` | `2291.50` | `1881.30` | -197,322.30 USD | `-4.85%` | `25X Cross` |
| `566` | `0x3453...b323` | `SHORT` | 4,049,609.84 USD | `1,750.12` | `2328.82` | `2291.50` | `2399.97` | 26,122.29 USD | `+0.65%` | `25X Cross` |
| `594` | `0xfeec...4e9c` | `SHORT` | 3,899,280.92 USD | `1,691.81` | `2566.49` | `2291.50` | `2652.54` | 442,743.59 USD | `+11.35%` | `10X Cross` |
| `597` | `0x936c...bb0f` | `SHORT` | 3,861,856.01 USD | `1,688.69` | `2434.60` | `2291.50` | `8620.27` | 249,431.09 USD | `+6.46%` | `20X Cross` |
| `609` | `0xeee0...0b53` | `LONG` | 3,785,521.59 USD | `1,637.12` | `2468.64` | `2291.50` | `158.25` | -255,954.47 USD | `-6.76%` | `7X Cross` |
| `612` | `0x27b8...12fc` | `LONG` | 3,769,749.28 USD | `1,628.12` | `2468.73` | `2291.50` | `476.68` | -249,645.35 USD | `-6.62%` | `10X Cross` |
| `614` | `0x982b...4606` | `LONG` | 3,762,015.01 USD | `1,626.82` | `2575.24` | `2291.50` | `1548.44` | -427,438.07 USD | `-11.36%` | `5X Isolated` |
| `628` | `0x73d7...8be1` | `LONG` | 3,668,156.73 USD | `1,601.47` | `2410.40` | `2291.50` | `2062.68` | -192,022.19 USD | `-5.23%` | `25X Cross` |
| `645` | `0xe170...9300` | `SHORT` | 3,545,527.48 USD | `1,533.40` | `2076.39` | `2291.50` | `3240.60` | -361,577.98 USD | `-10.20%` | `25X Cross` |
| `659` | `0x2e2b...2fab` | `LONG` | 3,488,522.59 USD | `1,507.38` | `2245.53` | `2291.50` | `1164.16` | 103,649.49 USD | `+2.97%` | `25X Cross` |
| `662` | `0x251f...6e5d` | `LONG` | 3,474,150.00 USD | `1,500.00` | `2346.68` | `2291.50` | `1681.33` | -45,880.49 USD | `-1.32%` | `20X Cross` |
| `675` | `0xad54...6203` | `LONG` | 3,371,604.49 USD | `1,458.18` | `2627.45` | `2291.50` | `2145.32` | -459,702.19 USD | `-13.63%` | `10X Isolated` |
| `679` | `0xef70...a84c` | `SHORT` | 3,341,393.71 USD | `1,442.74` | `2424.73` | `2291.50` | `3402.28` | 156,877.11 USD | `+4.69%` | `25X Cross` |
| `683` | `0x4b5f...0dd8` | `LONG` | 3,314,120.82 USD | `1,431.96` | `2339.45` | `2291.50` | `2148.73` | -35,872.13 USD | `-1.08%` | `10X Cross` |
| `686` | `0xbadb...9ee6` | `LONG` | 3,310,760.51 USD | `1,428.16` | `1936.00` | `2291.50` | `1059.83` | 545,838.87 USD | `+16.49%` | `20X Cross` |
| `693` | `0xd4c1...3d1d` | `SHORT` | 3,275,866.27 USD | `1,431.88` | `2336.05` | `2291.50` | `6128.56` | 69,099.10 USD | `+2.11%` | `12X Cross` |
| `703` | `0xfc27...9d9d` | `SHORT` | 3,241,273.09 USD | `1,417.20` | `2402.13` | `2291.50` | `13578.90` | 163,030.07 USD | `+5.03%` | `25X Cross` |
| `762` | `0x880a...311c` | `SHORT` | 3,041,001.89 USD | `1,320.22` | `2425.76` | `2291.50` | `8350.49` | 161,547.27 USD | `+5.31%` | `9X Cross` |
| `763` | `0x29de...3e93` | `LONG` | 3,033,960.00 USD | `1,310.00` | `2352.60` | `2291.50` | `1922.26` | -47,948.82 USD | `-1.58%` | `5X Isolated` |
| `772` | `0x0dd5...f6ee` | `LONG` | 3,008,119.09 USD | `1,314.85` | `2312.84` | `2291.50` | `1656.79` | -32,933.37 USD | `-1.09%` | `5X Cross` |
| `788` | `0xb15b...dbae` | `SHORT` | 2,937,496.84 USD | `1,267.53` | `2334.38` | `2291.50` | `2360.09` | 21,398.48 USD | `+0.73%` | `25X Cross` |
| `797` | `0xc435...c905` | `SHORT` | 2,894,236.80 USD | `1,248.00` | `2704.38` | `2291.50` | `4945.84` | 480,833.55 USD | `+16.61%` | `20X Cross` |
| `815` | `0x7178...0854` | `LONG` | 2,824,178.50 USD | `1,218.63` | `2461.81` | `2291.50` | `1079.20` | -175,867.90 USD | `-6.23%` | `10X Cross` |
| `816` | `0x4202...aaf5` | `SHORT` | 2,823,958.64 USD | `1,232.10` | `2321.73` | `2291.50` | `2733.57` | 36,665.66 USD | `+1.30%` | `5X Isolated` |
| `860` | `0x07fd...689d` | `LONG` | 2,634,878.84 USD | `1,146.10` | `2422.77` | `2291.50` | `0.000000` | -141,856.93 USD | `-5.38%` | `25X Cross` |
| `899` | `0x2f80...f203` | `SHORT` | 2,522,096.48 USD | `1,088.94` | `1984.00` | `2291.50` | `3071.71` | -361,629.29 USD | `-14.34%` | `20X Cross` |
| `906` | `0x6f11...0389` | `SHORT` | 2,498,424.50 USD | `1,079.00` | `2333.39` | `2291.50` | `3199.71` | 19,304.41 USD | `+0.77%` | `25X Cross` |
| `910` | `0x2b61...2f6c` | `SHORT` | 2,493,506.77 USD | `1,076.60` | `2681.75` | `2291.50` | `6327.25` | 393,665.96 USD | `+15.79%` | `10X Cross` |
| `914` | `0xfc66...ca06` | `LONG` | 2,479,169.90 USD | `1,081.67` | `2319.45` | `2291.50` | `0.000000` | -29,717.83 USD | `-1.20%` | `20X Cross` |
| `947` | `0x3bca...66f3` | `SHORT` | 2,388,220.03 USD | `1,042.57` | `2323.01` | `2291.50` | `10063.75` | 33,676.52 USD | `+1.41%` | `25X Cross` |
| `952` | `0x1b2a...f7a6` | `LONG` | 2,370,958.43 USD | `1,025.37` | `2737.51` | `2291.50` | `883.11` | -436,001.51 USD | `-18.39%` | `10X Cross` |
| `968` | `0xdb3a...cf3b` | `LONG` | 2,322,944.56 USD | `1,003.22` | `2705.01` | `2291.50` | `0.000000` | -390,762.33 USD | `-16.82%` | `4X Cross` |
| `969` | `0x001a...fef6` | `SHORT` | 2,322,287.06 USD | `1,007.33` | `2022.19` | `2291.50` | `3053.55` | -285,279.10 USD | `-12.28%` | `10X Cross` |
| `970` | `0x02aa...1806` | `SHORT` | 2,321,869.28 USD | `1,007.10` | `2654.68` | `2291.50` | `3613.71` | 351,662.82 USD | `+15.15%` | `20X Cross` |
| `971` | `0x4044...794c` | `LONG` | 2,318,700.00 USD | `1,000.00` | `2332.68` | `2291.50` | `0.000000` | -13,989.84 USD | `-0.60%` | `25X Cross` |
| `974` | `0xdf60...d3c7` | `LONG` | 2,314,300.00 USD | `1,000.00` | `2736.24` | `2291.50` | `2246.10` | -421,942.88 USD | `-18.23%` | `10X Isolated` |
| `975` | `0xfe82...ce65` | `SHORT` | 2,314,300.00 USD | `1,000.00` | `2300.50` | `2291.50` | `2718.45` | -13,792.07 USD | `-0.60%` | `25X Cross` |
| `977` | `0x5986...89d9` | `LONG` | 2,312,800.00 USD | `1,000.00` | `2346.34` | `2291.50` | `1283.38` | -33,549.54 USD | `-1.45%` | `25X Cross` |
| `979` | `0x2828...93a0` | `LONG` | 2,312,300.00 USD | `1,000.00` | `2393.30` | `2291.50` | `2283.50` | -81,009.16 USD | `-3.50%` | `25X Cross` |
| `982` | `0x5272...fcd9` | `SHORT` | 2,305,400.00 USD | `1,000.00` | `2241.82` | `2291.50` | `2880.78` | -63,575.51 USD | `-2.76%` | `5X Cross` |
| `1006` | `0xb002...ed8a` | `SHORT` | 2,231,829.59 USD | `962.78` | `2299.66` | `2291.50` | `4195.93` | -17,751.68 USD | `-0.80%` | `25X Cross` |
| `1030` | `0xc8fe...afa4` | `LONG` | 2,168,637.09 USD | `936.37` | `2331.34` | `2291.50` | `2145.83` | -14,367.14 USD | `-0.66%` | `10X Isolated` |
| `1031` | `0x2e30...4cb5` | `SHORT` | 2,164,572.20 USD | `945.02` | `2340.09` | `2291.50` | `7393.42` | 46,866.24 USD | `+2.17%` | `2X Cross` |
| `1052` | `0x9606...4e5d` | `SHORT` | 2,116,508.95 USD | `913.00` | `2478.70` | `2291.50` | `4054.78` | 146,544.65 USD | `+6.92%` | `20X Cross` |
| `1054` | `0x2577...4897` | `LONG` | 2,111,906.17 USD | `922.35` | `2333.88` | `2291.50` | `0.000000` | -40,750.99 USD | `-1.93%` | `15X Cross` |
| `1064` | `0xaeea...bfa7` | `LONG` | 2,094,478.47 USD | `908.75` | `2339.31` | `2291.50` | `2286.75` | -31,363.63 USD | `-1.50%` | `23X Isolated` |
| `1101` | `0x60f7...d1ee` | `LONG` | 2,035,519.00 USD | `890.00` | `2343.49` | `2291.50` | `2272.51` | -50,190.96 USD | `-2.47%` | `25X Cross` |
| `1119` | `0x20ad...8183` | `SHORT` | 2,009,133.25 USD | `876.39` | `2308.01` | `2291.50` | `2352.21` | 13,595.03 USD | `+0.68%` | `25X Isolated` |
| `1142` | `0x71d0...8c26` | `LONG` | 1,986,689.68 USD | `867.36` | `2313.61` | `2291.50` | `0.000000` | -20,048.10 USD | `-1.01%` | `25X Cross` |
| `1176` | `0xcd27...52a8` | `LONG` | 1,938,555.82 USD | `837.21` | `2553.56` | `2291.50` | `1404.25` | -199,308.96 USD | `-10.28%` | `2X Cross` |
| `1185` | `0xbef3...0d3e` | `LONG` | 1,926,324.87 USD | `830.99` | `2332.88` | `2291.50` | `2110.71` | -12,286.37 USD | `-0.64%` | `20X Cross` |
| `1197` | `0x6a41...a3b9` | `LONG` | 1,904,397.34 USD | `826.06` | `2332.61` | `2291.50` | `2112.90` | -22,477.51 USD | `-1.18%` | `20X Cross` |
| `1201` | `0xb8eb...1dd5` | `SHORT` | 1,898,574.31 USD | `830.12` | `2288.54` | `2291.50` | `4870.34` | 1,196.53 USD | `+0.06%` | `25X Cross` |
| `1225` | `0x7737...bf66` | `SHORT` | 1,852,557.98 USD | `799.79` | `2494.83` | `2291.50` | `24700.47` | 142,788.05 USD | `+7.71%` | `15X Cross` |
| `1226` | `0x04a9...95aa` | `LONG` | 1,852,400.00 USD | `800.00` | `2595.13` | `2291.50` | `1867.34` | -223,706.74 USD | `-12.08%` | `5X Cross` |
| `1242` | `0x3fc5...c0c1` | `SHORT` | 1,842,394.68 USD | `804.26` | `2702.11` | `2291.50` | `5199.60` | 330,806.84 USD | `+17.96%` | `25X Cross` |
| `1246` | `0xf83f...625f` | `SHORT` | 1,840,572.93 USD | `803.05` | `2601.00` | `2291.50` | `6081.38` | 248,163.52 USD | `+13.48%` | `20X Cross` |
| `1273` | `0x458d...ab3b` | `LONG` | 1,796,715.77 USD | `774.75` | `2740.41` | `2291.50` | `1888.01` | -326,413.42 USD | `-18.17%` | `3X Isolated` |
| `1304` | `0xc926...98d3` | `LONG` | 1,724,787.15 USD | `752.53` | `2286.56` | `2291.50` | `1001.26` | 4,074.27 USD | `+0.24%` | `25X Cross` |
| `1315` | `0x5f10...d49d` | `SHORT` | 1,718,032.50 USD | `750.00` | `2350.92` | `2291.50` | `2842.54` | 45,164.11 USD | `+2.63%` | `25X Cross` |
| `1343` | `0x51a0...3543` | `SHORT` | 1,677,685.80 USD | `724.55` | `2627.71` | `2291.50` | `7562.16` | 226,210.95 USD | `+13.48%` | `20X Cross` |
| `1361` | `0x3ee5...4fab` | `SHORT` | 1,655,897.44 USD | `715.17` | `2759.35` | `2291.50` | `3262.99` | 317,502.53 USD | `+19.17%` | `20X Cross` |
| `1369` | `0xa189...94d7` | `SHORT` | 1,646,663.97 USD | `719.98` | `2691.84` | `2291.50` | `3051.96` | 291,408.69 USD | `+17.70%` | `25X Cross` |
| `1371` | `0x4b1c...bc38` | `SHORT` | 1,645,174.99 USD | `718.26` | `2529.31` | `2291.50` | `4458.89` | 171,533.22 USD | `+10.43%` | `10X Cross` |
| `1384` | `0x5605...fe0f` | `SHORT` | 1,625,813.51 USD | `702.14` | `2566.90` | `2291.50` | `3072.22` | 176,519.14 USD | `+10.86%` | `20X Cross` |
| `1389` | `0xaa53...9cb7` | `LONG` | 1,621,900.00 USD | `700.00` | `2394.46` | `2291.50` | `1924.66` | -54,222.07 USD | `-3.34%` | `20X Cross` |
| `1390` | `0x2f93...4404` | `LONG` | 1,621,510.53 USD | `707.47` | `1700.45` | `2291.50` | `1369.64` | 418,484.15 USD | `+25.81%` | `4X Isolated` |
| `1395` | `0x7743...e4fe` | `SHORT` | 1,615,202.37 USD | `700.56` | `2326.87` | `2291.50` | `6154.41` | 14,907.77 USD | `+0.92%` | `25X Cross` |
| `1448` | `0x71e5...be04` | `LONG` | 1,570,153.98 USD | `677.67` | `2727.27` | `2291.50` | `1471.79` | -278,031.63 USD | `-17.71%` | `20X Cross` |
| `1456` | `0x0b23...f37b` | `LONG` | 1,560,795.75 USD | `675.00` | `2238.15` | `2291.50` | `588.25` | 50,039.11 USD | `+3.21%` | `5X Cross` |
| `1457` | `0xdbd1...29dd` | `SHORT` | 1,560,156.52 USD | `680.70` | `3030.57` | `2291.50` | `4105.21` | 502,764.61 USD | `+32.23%` | `6X Cross` |
| `1479` | `0x0082...1ae3` | `LONG` | 1,530,342.00 USD | `660.00` | `2448.58` | `2291.50` | `2244.99` | -85,726.64 USD | `-5.60%` | `25X Cross` |
| `1490` | `0x8923...1bac` | `SHORT` | 1,521,666.20 USD | `660.02` | `2339.81` | `2291.50` | `2932.63` | 22,650.62 USD | `+1.49%` | `25X Cross` |
| `1491` | `0x0cac...6170` | `SHORT` | 1,517,456.25 USD | `662.50` | `2146.55` | `2291.50` | `2835.42` | -95,361.26 USD | `-6.28%` | `20X Cross` |
| `1518` | `0xffb2...5ed6` | `SHORT` | 1,481,638.66 USD | `640.77` | `2672.96` | `2291.50` | `2546.12` | 231,109.68 USD | `+15.60%` | `20X Cross` |
| `1545` | `0xfce0...f4c0` | `SHORT` | 1,444,257.60 USD | `623.60` | `3129.61` | `2291.50` | `2788.45` | 507,368.98 USD | `+35.13%` | `20X Cross` |
| `1575` | `0x7663...cb5a` | `SHORT` | 1,406,216.37 USD | `613.54` | `2342.35` | `2291.50` | `3726.35` | 30,904.12 USD | `+2.20%` | `3X Cross` |
| `1590` | `0xad02...eb65` | `LONG` | 1,391,036.38 USD | `600.62` | `2460.69` | `2291.50` | `1079.70` | -86,904.18 USD | `-6.25%` | `5X Cross` |
| `1591` | `0x0deb...0bc5` | `LONG` | 1,390,200.00 USD | `600.00` | `2038.23` | `2291.50` | `1478.72` | 167,261.36 USD | `+12.03%` | `20X Cross` |
| `1593` | `0x67c3...609d` | `SHORT` | 1,389,240.00 USD | `600.00` | `2386.55` | `2291.50` | `2560.80` | 42,691.89 USD | `+3.07%` | `25X Cross` |
| `1595` | `0x26e6...6b28` | `LONG` | 1,388,340.00 USD | `600.00` | `1769.78` | `2291.50` | `2005.51` | 326,468.47 USD | `+23.52%` | `20X Cross` |
| `1604` | `0x0a84...6ddd` | `LONG` | 1,383,240.00 USD | `600.00` | `2222.36` | `2291.50` | `1774.83` | 49,821.66 USD | `+3.60%` | `25X Cross` |
| `1613` | `0x638f...f5f0` | `LONG` | 1,374,300.00 USD | `600.00` | `4011.50` | `2291.50` | `178.56` | -1,032,603.53 USD | `-75.14%` | `25X Cross` |
| `1626` | `0x94b6...e5b3` | `SHORT` | 1,345,607.65 USD | `586.71` | `2377.90` | `2291.50` | `2451.72` | 49,530.59 USD | `+3.68%` | `25X Cross` |
| `1651` | `0xfb99...37f3` | `LONG` | 1,310,856.41 USD | `565.34` | `2362.35` | `2291.50` | `1213.80` | -24,679.95 USD | `-1.88%` | `3X Cross` |
| `1667` | `0x9599...c60a` | `LONG` | 1,298,530.90 USD | `566.55` | `2306.73` | `2291.50` | `0.000000` | -8,360.85 USD | `-0.64%` | `20X Cross` |
| `1670` | `0x844b...7f42` | `SHORT` | 1,297,144.20 USD | `561.00` | `2026.17` | `2291.50` | `3089.67` | -160,460.79 USD | `-12.37%` | `25X Cross` |
| `1688` | `0xabe6...1d99` | `SHORT` | 1,281,867.22 USD | `556.00` | `2484.68` | `2291.50` | `3002.99` | 99,628.67 USD | `+7.77%` | `20X Cross` |
| `1754` | `0xad21...fb6a` | `LONG` | 1,216,331.90 USD | `531.87` | `2574.89` | `2291.50` | `1693.68` | -153,173.60 USD | `-12.59%` | `7X Cross` |
| `1795` | `0x31de...13f2` | `LONG` | 1,174,232.10 USD | `513.10` | `2316.96` | `2291.50` | `0.000000` | -14,606.34 USD | `-1.24%` | `20X Cross` |
| `1796` | `0x0c7a...2f50` | `SHORT` | 1,173,963.19 USD | `509.25` | `2122.56` | `2291.50` | `4084.03` | -93,057.76 USD | `-7.93%` | `20X Cross` |
| `1813` | `0xaf9f...a4fa` | `LONG` | 1,158,872.20 USD | `506.70` | `2311.59` | `2291.50` | `0.000000` | -12,411.14 USD | `-1.07%` | `20X Cross` |
| `1825` | `0x7298...7d6c` | `SHORT` | 1,151,970.26 USD | `498.15` | `3426.75` | `2291.50` | `5422.42` | 555,065.57 USD | `+48.18%` | `20X Cross` |
| `1831` | `0x89b2...9ca6` | `LONG` | 1,145,990.00 USD | `500.00` | `2484.03` | `2291.50` | `1954.23` | -96,029.35 USD | `-8.38%` | `25X Cross` |
| `1839` | `0xc10f...23b3` | `LONG` | 1,135,575.00 USD | `490.00` | `2402.16` | `2291.50` | `2082.08` | -41,487.83 USD | `-3.65%` | `25X Cross` |
| `1850` | `0x321f...1c84` | `SHORT` | 1,128,389.21 USD | `488.02` | `2370.09` | `2291.50` | `3022.61` | 28,255.39 USD | `+2.50%` | `10X Cross` |
| `1856` | `0x404c...5f03` | `SHORT` | 1,122,578.11 USD | `489.79` | `2671.94` | `2291.50` | `4645.19` | 186,101.45 USD | `+16.58%` | `20X Cross` |
| `1917` | `0x82c6...fe42` | `LONG` | 1,071,150.00 USD | `462.50` | `2501.38` | `2291.50` | `2054.49` | -85,740.57 USD | `-8.00%` | `5X Isolated` |
| `1943` | `0x617e...0f97` | `SHORT` | 1,048,811.65 USD | `457.85` | `2205.60` | `2291.50` | `3754.39` | -38,967.82 USD | `-3.72%` | `10X Cross` |
| `1958` | `0xf910...0a2d` | `LONG` | 1,034,449.13 USD | `452.16` | `2304.81` | `2291.50` | `0.000000` | -7,691.97 USD | `-0.74%` | `5X Cross` |
| `1967` | `0x53f8...ceff` | `LONG` | 1,031,246.29 USD | `445.60` | `2399.81` | `2291.50` | `0.000000` | -38,104.31 USD | `-3.69%` | `20X Cross` |
| `1973` | `0xae55...2236` | `LONG` | 1,029,195.00 USD | `450.00` | `2510.21` | `2291.50` | `0.000000` | -100,402.50 USD | `-9.76%` | `25X Cross` |
| `1984` | `0xac26...a9c7` | `SHORT` | 1,020,679.90 USD | `446.28` | `2192.58` | `2291.50` | `8512.55` | -42,180.20 USD | `-4.13%` | `20X Cross` |
| `1987` | `0xd6e1...f256` | `LONG` | 1,018,309.70 USD | `444.19` | `2295.13` | `2291.50` | `1042.86` | -1,172.53 USD | `-0.12%` | `25X Cross` |
| `1994` | `0xd8a1...6687` | `LONG` | 1,013,627.31 USD | `441.53` | `2804.24` | `2291.50` | `2151.04` | -224,541.13 USD | `-22.15%` | `20X Cross` |
| `2001` | `0x248e...6be2` | `SHORT` | 1,010,737.01 USD | `436.40` | `2314.49` | `2291.50` | `4423.77` | -702.29 USD | `-0.07%` | `20X Cross` |
| `2019` | `0x80f2...0c3a` | `LONG` | 1,001,539.78 USD | `434.55` | `2564.17` | `2291.50` | `864.19` | -112,709.10 USD | `-11.25%` | `5X Cross` |

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
| `ANNOUNCEMENT` | `INFO` | `2356.30` | 47,126.00 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 47.13K USD at 2356.3000 USD [API] | `2026-10-15 02:24:27` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`2403.57` (Vol: 16,800,000.00 USD, Dist: `+3.87%`) | Long MP=`2294.75` (Vol: 27,100,000.00 USD, Dist: `--0.83%`)
  * 48H Horizon: Short MP=`2401.93` (Vol: 25,300,000.00 USD, Dist: `+3.80%`) | Long MP=`2284.33` (Vol: 30,000,000.00 USD, Dist: `--1.28%`)
  * 3D Horizon: Short MP=`2401.93` (Vol: 26,700,000.00 USD, Dist: `+3.80%`) | Long MP=`2286.29` (Vol: 37,900,000.00 USD, Dist: `--1.20%`)
  * 7D Horizon: Short MP=`2402.93` (Vol: 47,100,000.00 USD, Dist: `+3.84%`) | Long MP=`2284.60` (Vol: 72,300,000.00 USD, Dist: `--1.27%`)
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
| `7D` | `Long Liquidation` | `2067.30` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 452,190.00 USD | 295,290.00 USD | 262,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2070.20` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 2,800,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2071.00` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 995,550.00 USD | 57,450.00 USD | 487,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2073.10` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 3,550,000.00 USD | 2,100,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2073.60` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 419,970.00 USD | 62,630.00 USD | 506,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 921,260.00 USD | 329,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2076.00` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 3,910,000.00 USD | 4,290,000.00 USD | 3,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2076.20` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 2,580,000.00 USD | 926,330.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2078.80` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 1,320,000.00 USD | 1,100,000.00 USD | 820,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2078.90` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 4,500,000.00 USD | 3,730,000.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2081.40` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 1,400,000.00 USD | 1,260,000.00 USD | 227,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2081.80` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 4,050,000.00 USD | 1,290,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2084.00` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 2,120,000.00 USD | 1,300,000.00 USD | 753,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2084.70` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 4,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 2,640,000.00 USD | 328,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2086.60` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 1,600,000.00 USD | 1,640,000.00 USD | 898,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2087.60` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 3,960,000.00 USD | 2,750,000.00 USD | 2,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2089.20` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 812,220.00 USD | 228,670.00 USD | 226,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2090.50` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 4,370,000.00 USD | 976,840.00 USD | 6,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2091.80` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 1,280,000.00 USD | 514,440.00 USD | 837,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2093.40` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 3,930,000.00 USD | 1,200,000.00 USD | 2,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2094.40` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 2,160,000.00 USD | 1,050,000.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 1,420,000.00 USD | 325,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2096.30` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 3,150,000.00 USD | 2,430,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2097.00` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 594,350.00 USD | 785,260.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2099.20` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 1,460,000.00 USD | 2,100,000.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2099.60` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 194,900.00 USD | 700,850.00 USD | 11,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2102.10` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 678,000.00 USD | 1,510,000.00 USD | 2,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2102.20` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 327,300.00 USD | 119,690.00 USD | 466,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2104.80` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 792,480.00 USD | 841,400.00 USD | 22,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2105.00` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 2,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 1,220,000.00 USD | 324,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2107.40` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 546,100.00 USD | 0.00 USD | 496,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2107.90` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 2,320,000.00 USD | 356,360.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2110.00` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 118,210.00 USD | 31,550.00 USD | 8,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2110.80` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 2,830,000.00 USD | 2,350,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2112.60` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 911,810.00 USD | 643,210.00 USD | 422,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2113.70` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 1,780,000.00 USD | 1,300,000.00 USD | 2,730,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 20,470,000.00 USD | 323,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2115.20` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 0.00 USD | 13,230.00 USD | 431,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2116.60` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 2,360,000.00 USD | 2,350,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2117.80` | 999,760,000.00 USD | 999,760,000.00 USD | 679,710.00 USD | 4,130.00 USD | 811,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2119.50` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 2,530,000.00 USD | 606,940.00 USD | 2,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2120.40` | 998,260,000.00 USD | 998,260,000.00 USD | 198,890.00 USD | 428,990.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2122.40` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 2,230,000.00 USD | 1,000,000.00 USD | 1,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2123.00` | 996,520,000.00 USD | 996,520,000.00 USD | 1,570,000.00 USD | 693,780.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 1,030,000.00 USD | 302,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2125.30` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 2,700,000.00 USD | 2,150,000.00 USD | 2,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2125.60` | 993,210,000.00 USD | 993,210,000.00 USD | 179,030.00 USD | 1,510,000.00 USD | 504,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2128.20` | 991,020,000.00 USD | 991,020,000.00 USD | 365,910.00 USD | 482,820.00 USD | 129,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2128.20` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 931,390.00 USD | 1,960,000.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2130.80` | 990,040,000.00 USD | 990,040,000.00 USD | 0.00 USD | 644,330.00 USD | 654,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2131.10` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 1,980,000.00 USD | 1,750,000.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2133.40` | 988,740,000.00 USD | 988,740,000.00 USD | 0.00 USD | 312,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2134.00` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 2,170,000.00 USD | 550,450.00 USD | 308,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 3,440,000.00 USD | 301,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2136.00` | 988,430,000.00 USD | 988,430,000.00 USD | 0.00 USD | 278,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2136.90` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 746,340.00 USD | 845,110.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2139.80` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 1,110,000.00 USD | 1,000,000.00 USD | 635,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2142.70` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 1,550,000.00 USD | 510,270.00 USD | 434,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 9,300,000.00 USD | 298,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2145.60` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 678,800.00 USD | 1,230,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2148.50` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 485,890.00 USD | 474,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2151.40` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 20,460.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2154.30` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 128,430.00 USD | 510,660.00 USD | 32,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 23,380,000.00 USD | 288,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2157.20` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 388,210.00 USD | 831,780.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2160.10` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 497,380.00 USD | 1,170,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2163.00` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 715,680.00 USD | 623,390.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 904,350.00 USD | 265,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2165.90` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 25,540.00 USD | 0.00 USD | 68,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2168.80` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 1,650,000.00 USD | 373,180.00 USD | 794,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2171.70` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 479,540.00 USD | 765,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2174.60` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 0.00 USD | 734,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 109,710,000.00 USD | 264,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2185.00` | 112,420,000.00 USD | 154,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2194.90` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 141,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 909,930.00 USD | 42,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2197.80` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 2,440,000.00 USD | 3,270,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2200.70` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 3,120,000.00 USD | 3,140,000.00 USD | 3,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2201.00` | 988,150,000.00 USD | 988,150,000.00 USD | 284,470.00 USD | 217,490.00 USD | 225,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2203.60` | 987,420,000.00 USD | 987,420,000.00 USD | 1,050,000.00 USD | 0.00 USD | 755,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2203.60` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 3,280,000.00 USD | 624,500.00 USD | 3,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 1,470,000.00 USD | 41,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2206.20` | 985,610,000.00 USD | 985,610,000.00 USD | 611,820.00 USD | 2,480,000.00 USD | 722,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2206.50` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 6,920,000.00 USD | 6,050,000.00 USD | 3,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2208.80` | 981,800,000.00 USD | 981,800,000.00 USD | 2,490,000.00 USD | 668,670.00 USD | 3,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2209.40` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 10,720,000.00 USD | 5,060,000.00 USD | 4,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2211.40` | 975,590,000.00 USD | 975,590,000.00 USD | 2,830,000.00 USD | 1,640,000.00 USD | 573,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2212.30` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 8,350,000.00 USD | 9,670,000.00 USD | 9,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2214.00` | 970,550,000.00 USD | 970,550,000.00 USD | 6,190,000.00 USD | 3,470,000.00 USD | 5,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 1,830,000.00 USD | 39,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2215.20` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 17,290,000.00 USD | 12,680,000.00 USD | 8,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2216.60` | 955,650,000.00 USD | 955,650,000.00 USD | 5,840,000.00 USD | 5,840,000.00 USD | 2,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2218.10` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 15,430,000.00 USD | 12,610,000.00 USD | 9,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2219.20` | 941,200,000.00 USD | 941,200,000.00 USD | 4,540,000.00 USD | 4,130,000.00 USD | 990,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2221.00` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 11,330,000.00 USD | 7,500,000.00 USD | 5,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2221.80` | 931,530,000.00 USD | 931,530,000.00 USD | 5,110,000.00 USD | 3,780,000.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2223.90` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 12,480,000.00 USD | 8,700,000.00 USD | 13,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2224.40` | 920,810,000.00 USD | 920,810,000.00 USD | 5,580,000.00 USD | 3,340,000.00 USD | 3,610,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2225.00` | 1,590,000.00 USD | 38,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2226.80` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 9,460,000.00 USD | 8,430,000.00 USD | 4,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2227.00` | 908,280,000.00 USD | 908,280,000.00 USD | 4,970,000.00 USD | 3,570,000.00 USD | 2,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2229.60` | 897,350,000.00 USD | 897,350,000.00 USD | 4,610,000.00 USD | 2,120,000.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2229.70` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 10,530,000.00 USD | 7,740,000.00 USD | 15,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2232.20` | 889,280,000.00 USD | 889,280,000.00 USD | 3,950,000.00 USD | 2,920,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2232.60` | 2,070,000,000.00 USD | 2,070,000,000.00 USD | 13,610,000.00 USD | 4,400,000.00 USD | 12,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2234.80` | 878,940,000.00 USD | 878,940,000.00 USD | 6,460,000.00 USD | 3,260,000.00 USD | 4,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2235.00` | 1,290,000.00 USD | 36,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2235.50` | 2,040,000,000.00 USD | 2,040,000,000.00 USD | 12,460,000.00 USD | 12,630,000.00 USD | 4,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2237.40` | 864,860,000.00 USD | 864,860,000.00 USD | 1,850,000.00 USD | 4,150,000.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2238.40` | 2,010,000,000.00 USD | 2,010,000,000.00 USD | 7,230,000.00 USD | 8,790,000.00 USD | 5,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2240.00` | 855,670,000.00 USD | 855,670,000.00 USD | 972,850.00 USD | 369,950.00 USD | 39,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2241.30` | 1,990,000,000.00 USD | 1,990,000,000.00 USD | 5,380,000.00 USD | 5,410,000.00 USD | 10,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2242.60` | 854,290,000.00 USD | 854,290,000.00 USD | 1,290,000.00 USD | 1,770,000.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2244.20` | 1,970,000,000.00 USD | 1,970,000,000.00 USD | 10,350,000.00 USD | 8,810,000.00 USD | 12,230,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2245.00` | 4,640,000.00 USD | 35,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2245.20` | 849,680,000.00 USD | 849,680,000.00 USD | 2,050,000.00 USD | 1,690,000.00 USD | 634,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2247.10` | 1,940,000,000.00 USD | 1,940,000,000.00 USD | 16,790,000.00 USD | 10,060,000.00 USD | 9,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2247.80` | 845,310,000.00 USD | 845,310,000.00 USD | 2,660,000.00 USD | 930,590.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2250.00` | 1,900,000,000.00 USD | 1,900,000,000.00 USD | 11,760,000.00 USD | 9,350,000.00 USD | 8,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2250.40` | 839,880,000.00 USD | 839,880,000.00 USD | 2,890,000.00 USD | 931,320.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2252.90` | 1,870,000,000.00 USD | 1,870,000,000.00 USD | 24,550,000.00 USD | 17,220,000.00 USD | 16,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2253.00` | 834,460,000.00 USD | 834,460,000.00 USD | 6,720,000.00 USD | 7,260,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2255.00` | 10,910,000.00 USD | 30,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2255.60` | 815,660,000.00 USD | 815,660,000.00 USD | 3,620,000.00 USD | 1,780,000.00 USD | 5,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2255.80` | 1,810,000,000.00 USD | 1,810,000,000.00 USD | 23,870,000.00 USD | 18,230,000.00 USD | 15,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2258.20` | 805,030,000.00 USD | 805,030,000.00 USD | 7,130,000.00 USD | 3,950,000.00 USD | 5,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2258.70` | 1,750,000,000.00 USD | 1,750,000,000.00 USD | 29,540,000.00 USD | 22,530,000.00 USD | 25,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2260.80` | 788,430,000.00 USD | 788,430,000.00 USD | 15,650,000.00 USD | 10,070,000.00 USD | 10,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2261.60` | 1,680,000,000.00 USD | 1,680,000,000.00 USD | 48,100,000.00 USD | 31,730,000.00 USD | 21,740,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2263.40` | 752,540,000.00 USD | 752,540,000.00 USD | 12,500,000.00 USD | 14,000,000.00 USD | 11,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2264.50` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 36,330,000.00 USD | 30,310,000.00 USD | 24,870,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2265.00` | 3,260,000.00 USD | 19,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2266.00` | 714,780,000.00 USD | 714,780,000.00 USD | 14,420,000.00 USD | 12,090,000.00 USD | 3,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2267.40` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 41,410,000.00 USD | 40,010,000.00 USD | 31,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2268.60` | 685,240,000.00 USD | 685,240,000.00 USD | 15,490,000.00 USD | 10,340,000.00 USD | 8,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2270.30` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 43,180,000.00 USD | 27,630,000.00 USD | 42,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2271.20` | 651,000,000.00 USD | 651,000,000.00 USD | 8,870,000.00 USD | 8,780,000.00 USD | 9,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2273.20` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 33,160,000.00 USD | 25,760,000.00 USD | 20,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2273.80` | 623,450,000.00 USD | 623,450,000.00 USD | 15,730,000.00 USD | 9,060,000.00 USD | 5,320,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2275.00` | 6,850,000.00 USD | 16,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2276.10` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 54,840,000.00 USD | 46,910,000.00 USD | 49,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2276.40` | 593,340,000.00 USD | 593,340,000.00 USD | 15,970,000.00 USD | 13,870,000.00 USD | 16,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2279.00` | 547,240,000.00 USD | 547,240,000.00 USD | 18,830,000.00 USD | 8,690,000.00 USD | 11,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2279.00` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 74,170,000.00 USD | 30,780,000.00 USD | 49,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2281.60` | 508,360,000.00 USD | 508,360,000.00 USD | 21,700,000.00 USD | 13,850,000.00 USD | 17,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2281.90` | 872,350,000.00 USD | 872,350,000.00 USD | 64,370,000.00 USD | 63,970,000.00 USD | 39,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2284.20` | 455,770,000.00 USD | 455,770,000.00 USD | 32,070,000.00 USD | 26,910,000.00 USD | 22,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2284.80` | 704,130,000.00 USD | 704,130,000.00 USD | 95,240,000.00 USD | 73,600,000.00 USD | 47,330,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2285.00` | 4,100,000.00 USD | 9,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2286.80` | 373,890,000.00 USD | 373,890,000.00 USD | 20,910,000.00 USD | 21,270,000.00 USD | 9,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2287.70` | 487,960,000.00 USD | 487,960,000.00 USD | 62,030,000.00 USD | 55,240,000.00 USD | 58,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2289.40` | 322,270,000.00 USD | 322,270,000.00 USD | 21,670,000.00 USD | 19,020,000.00 USD | 7,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2290.60` | 312,590,000.00 USD | 312,590,000.00 USD | 43,520,000.00 USD | 32,400,000.00 USD | 40,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2292.00` | 274,110,000.00 USD | 274,110,000.00 USD | 30,860,000.00 USD | 18,540,000.00 USD | 12,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2293.50` | 196,100,000.00 USD | 196,100,000.00 USD | 45,930,000.00 USD | 20,380,000.00 USD | 26,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2294.60` | 212,400,000.00 USD | 212,400,000.00 USD | 14,960,000.00 USD | 17,280,000.00 USD | 15,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2295.00` | 3,310,000.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2296.40` | 103,720,000.00 USD | 103,720,000.00 USD | 8,030,000.00 USD | 4,300,000.00 USD | 3,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2297.20` | 165,110,000.00 USD | 165,110,000.00 USD | 20,990,000.00 USD | 7,900,000.00 USD | 3,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2299.30` | 87,680,000.00 USD | 87,680,000.00 USD | 13,410,000.00 USD | 6,480,000.00 USD | 216,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2299.80` | 133,010,000.00 USD | 133,010,000.00 USD | 16,170,000.00 USD | 9,020,000.00 USD | 8,940,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2302.20` | 67,580,000.00 USD | 67,580,000.00 USD | 13,430,000.00 USD | 3,870,000.00 USD | 18,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2302.40` | 98,880,000.00 USD | 98,880,000.00 USD | 16,130,000.00 USD | 11,080,000.00 USD | 17,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2305.00` | 54,640,000.00 USD | 54,640,000.00 USD | 0.00 USD | 15,990,000.00 USD | 21,200,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2305.00` | 940,780.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2305.10` | 31,350,000.00 USD | 31,350,000.00 USD | 0.00 USD | 15,290,000.00 USD | 5,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2307.60` | 17,460,000.00 USD | 17,460,000.00 USD | 0.00 USD | 2,770,000.00 USD | 2,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2308.00` | 10,740,000.00 USD | 10,740,000.00 USD | 0.00 USD | 2,150,000.00 USD | 134,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2310.90` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 512,220.00 USD | 97,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2312.80` | 11,740,000.00 USD | 11,740,000.00 USD | 0.00 USD | 2,370,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2313.80` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 7,650,000.00 USD | 188,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2315.00` | 932,620.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2315.40` | 9,370,000.00 USD | 9,370,000.00 USD | 0.00 USD | 9,370,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2316.70` | 235,270.00 USD | 235,270.00 USD | 0.00 USD | 235,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2316.70` | 470,540.00 USD | 470,540.00 USD | 0.00 USD | 235,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2318.00` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2319.60` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 5,370,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2320.60` | 7,310,000.00 USD | 7,310,000.00 USD | 0.00 USD | 3,050,000.00 USD | 61,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2322.50` | 9,800,000.00 USD | 9,800,000.00 USD | 3,130,000.00 USD | 835,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2323.20` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 4,320,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2325.00` | 321,320.00 USD | 329,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2325.40` | 11,540,000.00 USD | 11,540,000.00 USD | 0.00 USD | 1,740,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2325.80` | 11,700,000.00 USD | 11,700,000.00 USD | 0.00 USD | 0.00 USD | 66,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2328.30` | 15,530,000.00 USD | 15,530,000.00 USD | 3,860,000.00 USD | 0.00 USD | 126,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2328.40` | 14,280,000.00 USD | 14,280,000.00 USD | 2,140,000.00 USD | 206,450.00 USD | 237,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2331.00` | 26,720,000.00 USD | 26,720,000.00 USD | 12,060,000.00 USD | 251,940.00 USD | 126,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2331.20` | 38,550,000.00 USD | 38,550,000.00 USD | 23,030,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2333.60` | 39,480,000.00 USD | 39,480,000.00 USD | 7,960,000.00 USD | 1,420,000.00 USD | 3,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2334.10` | 68,830,000.00 USD | 68,830,000.00 USD | 13,040,000.00 USD | 10,860,000.00 USD | 6,380,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2335.00` | 7,680.00 USD | 7,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2336.20` | 61,370,000.00 USD | 61,370,000.00 USD | 19,560,000.00 USD | 249,730.00 USD | 2,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2337.00` | 98,690,000.00 USD | 98,690,000.00 USD | 22,160,000.00 USD | 7,570,000.00 USD | 141,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2338.80` | 66,500,000.00 USD | 66,500,000.00 USD | 3,540,000.00 USD | 130,330.00 USD | 1,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2339.90` | 136,630,000.00 USD | 136,630,000.00 USD | 13,780,000.00 USD | 5,360,000.00 USD | 18,800,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2341.40` | 73,830,000.00 USD | 73,830,000.00 USD | 3,180,000.00 USD | 0.00 USD | 4,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2342.80` | 150,660,000.00 USD | 150,660,000.00 USD | 0.00 USD | 10,200,000.00 USD | 3,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2344.00` | 82,120,000.00 USD | 82,120,000.00 USD | 1,080,000.00 USD | 1,960,000.00 USD | 5,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2345.70` | 165,540,000.00 USD | 165,540,000.00 USD | 1,350,000.00 USD | 7,920,000.00 USD | 5,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2346.60` | 90,420,000.00 USD | 90,420,000.00 USD | 2,380,000.00 USD | 0.00 USD | 5,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2348.60` | 197,110,000.00 USD | 197,110,000.00 USD | 285,680.00 USD | 7,240,000.00 USD | 24,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2349.20` | 103,750,000.00 USD | 103,750,000.00 USD | 9,870,000.00 USD | 145,980.00 USD | 3,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2351.50` | 221,260,000.00 USD | 221,260,000.00 USD | 782,590.00 USD | 17,680,000.00 USD | 5,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2351.80` | 128,290,000.00 USD | 128,290,000.00 USD | 18,090,000.00 USD | 2,740,000.00 USD | 3,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2354.40` | 150,330,000.00 USD | 150,330,000.00 USD | 2,970,000.00 USD | 17,740,000.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2354.40` | 262,770,000.00 USD | 262,770,000.00 USD | 6,120,000.00 USD | 35,020,000.00 USD | 371,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2357.00` | 157,590,000.00 USD | 157,590,000.00 USD | 2,930,000.00 USD | 2,470,000.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2357.30` | 283,750,000.00 USD | 283,750,000.00 USD | 11,880,000.00 USD | 5,920,000.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2359.60` | 176,030,000.00 USD | 176,030,000.00 USD | 6,360,000.00 USD | 5,500,000.00 USD | 6,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2360.20` | 291,910,000.00 USD | 291,910,000.00 USD | 4,730,000.00 USD | 3,430,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2362.20` | 189,550,000.00 USD | 189,550,000.00 USD | 5,710,000.00 USD | 6,710,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2363.10` | 299,970,000.00 USD | 299,970,000.00 USD | 2,820,000.00 USD | 0.00 USD | 5,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2364.80` | 203,180,000.00 USD | 203,180,000.00 USD | 4,810,000.00 USD | 3,710,000.00 USD | 5,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 1,020.00 USD | 1,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2366.00` | 307,980,000.00 USD | 307,980,000.00 USD | 6,340,000.00 USD | 0.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2367.40` | 206,770,000.00 USD | 206,770,000.00 USD | 3,370,000.00 USD | 0.00 USD | 220,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2368.90` | 329,630,000.00 USD | 329,630,000.00 USD | 20,720,000.00 USD | 475,460.00 USD | 450,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2370.00` | 240,420,000.00 USD | 240,420,000.00 USD | 15,180,000.00 USD | 11,410,000.00 USD | 7,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2371.80` | 393,130,000.00 USD | 393,130,000.00 USD | 12,810,000.00 USD | 0.00 USD | 50,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2372.60` | 268,270,000.00 USD | 268,270,000.00 USD | 14,450,000.00 USD | 5,550,000.00 USD | 7,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2374.70` | 420,080,000.00 USD | 420,080,000.00 USD | 13,410,000.00 USD | 121,480.00 USD | 13,410,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 47,010.00 USD | 48,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2375.20` | 292,720,000.00 USD | 292,720,000.00 USD | 15,710,000.00 USD | 2,070,000.00 USD | 6,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2377.60` | 450,420,000.00 USD | 450,420,000.00 USD | 8,770,000.00 USD | 6,190,000.00 USD | 15,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2377.80` | 320,040,000.00 USD | 320,040,000.00 USD | 5,320,000.00 USD | 11,130,000.00 USD | 10,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2380.40` | 357,690,000.00 USD | 357,690,000.00 USD | 12,180,000.00 USD | 11,590,000.00 USD | 13,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2380.50` | 479,940,000.00 USD | 479,940,000.00 USD | 6,830,000.00 USD | 2,590,000.00 USD | 20,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2383.00` | 415,120,000.00 USD | 415,120,000.00 USD | 23,330,000.00 USD | 18,180,000.00 USD | 15,930,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2383.40` | 530,830,000.00 USD | 530,830,000.00 USD | 8,610,000.00 USD | 17,490,000.00 USD | 24,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 3,730,000.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2385.60` | 447,000,000.00 USD | 447,000,000.00 USD | 7,900,000.00 USD | 14,010,000.00 USD | 9,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2386.30` | 645,120,000.00 USD | 645,120,000.00 USD | 17,450,000.00 USD | 41,020,000.00 USD | 55,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2388.20` | 476,380,000.00 USD | 476,380,000.00 USD | 16,730,000.00 USD | 6,000,000.00 USD | 6,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2389.20` | 717,690,000.00 USD | 717,690,000.00 USD | 3,900,000.00 USD | 30,140,000.00 USD | 38,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2390.80` | 493,750,000.00 USD | 493,750,000.00 USD | 3,630,000.00 USD | 5,350,000.00 USD | 8,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2392.10` | 824,520,000.00 USD | 824,520,000.00 USD | 17,810,000.00 USD | 45,620,000.00 USD | 43,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2393.40` | 517,430,000.00 USD | 517,430,000.00 USD | 5,640,000.00 USD | 14,040,000.00 USD | 4,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2395.00` | 929,780,000.00 USD | 929,780,000.00 USD | 47,110,000.00 USD | 28,070,000.00 USD | 30,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 4,420,000.00 USD | 8,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2396.00` | 529,090,000.00 USD | 529,090,000.00 USD | 4,830,000.00 USD | 3,240,000.00 USD | 3,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2397.90` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 37,230,000.00 USD | 36,430,000.00 USD | 21,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2398.60` | 552,670,000.00 USD | 552,670,000.00 USD | 6,540,000.00 USD | 7,660,000.00 USD | 9,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2400.80` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 42,030,000.00 USD | 25,680,000.00 USD | 25,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2401.20` | 577,570,000.00 USD | 577,570,000.00 USD | 9,230,000.00 USD | 8,570,000.00 USD | 7,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2403.70` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 58,510,000.00 USD | 25,430,000.00 USD | 29,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2403.80` | 604,950,000.00 USD | 604,950,000.00 USD | 10,540,000.00 USD | 9,010,000.00 USD | 7,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 9,120,000.00 USD | 17,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2406.40` | 633,840,000.00 USD | 633,840,000.00 USD | 13,690,000.00 USD | 8,010,000.00 USD | 7,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2406.60` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 24,970,000.00 USD | 34,300,000.00 USD | 16,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2409.00` | 662,330,000.00 USD | 662,330,000.00 USD | 8,870,000.00 USD | 11,200,000.00 USD | 8,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2409.50` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 28,650,000.00 USD | 26,770,000.00 USD | 26,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2411.60` | 682,910,000.00 USD | 682,910,000.00 USD | 9,650,000.00 USD | 7,290,000.00 USD | 3,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2412.40` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 16,560,000.00 USD | 15,580,000.00 USD | 15,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2414.20` | 691,460,000.00 USD | 691,460,000.00 USD | 3,480,000.00 USD | 2,270,000.00 USD | 2,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 459,730.00 USD | 17,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2415.30` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 20,360,000.00 USD | 20,510,000.00 USD | 25,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2416.80` | 708,360,000.00 USD | 708,360,000.00 USD | 4,790,000.00 USD | 7,130,000.00 USD | 4,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2418.20` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 31,510,000.00 USD | 13,720,000.00 USD | 19,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2419.40` | 719,440,000.00 USD | 719,440,000.00 USD | 5,080,000.00 USD | 3,230,000.00 USD | 2,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2421.10` | 1,640,000,000.00 USD | 1,640,000,000.00 USD | 22,270,000.00 USD | 27,860,000.00 USD | 21,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2422.00` | 734,060,000.00 USD | 734,060,000.00 USD | 4,170,000.00 USD | 4,490,000.00 USD | 5,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.00` | 1,720,000,000.00 USD | 1,720,000,000.00 USD | 18,610,000.00 USD | 31,660,000.00 USD | 30,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2424.60` | 739,360,000.00 USD | 739,360,000.00 USD | 1,790,000.00 USD | 2,670,000.00 USD | 844,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 816,560.00 USD | 18,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2426.90` | 1,800,000,000.00 USD | 1,800,000,000.00 USD | 27,510,000.00 USD | 20,690,000.00 USD | 26,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2427.20` | 740,820,000.00 USD | 740,820,000.00 USD | 731,900.00 USD | 124,100.00 USD | 601,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2429.80` | 745,190,000.00 USD | 745,190,000.00 USD | 1,390,000.00 USD | 1,770,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2429.80` | 1,820,000,000.00 USD | 1,820,000,000.00 USD | 6,630,000.00 USD | 12,550,000.00 USD | 6,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2432.40` | 749,070,000.00 USD | 749,070,000.00 USD | 1,950,000.00 USD | 1,690,000.00 USD | 247,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2432.70` | 1,860,000,000.00 USD | 1,860,000,000.00 USD | 17,550,000.00 USD | 15,730,000.00 USD | 6,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2435.00` | 753,180,000.00 USD | 753,180,000.00 USD | 2,100,000.00 USD | 468,310.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 8,040,000.00 USD | 26,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2435.60` | 1,910,000,000.00 USD | 1,910,000,000.00 USD | 20,240,000.00 USD | 13,900,000.00 USD | 12,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2437.60` | 754,510,000.00 USD | 754,510,000.00 USD | 777,840.00 USD | 531,390.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2438.50` | 1,960,000,000.00 USD | 1,960,000,000.00 USD | 15,350,000.00 USD | 21,640,000.00 USD | 14,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2440.20` | 757,790,000.00 USD | 757,790,000.00 USD | 1,540,000.00 USD | 1,250,000.00 USD | 479,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2441.40` | 1,990,000,000.00 USD | 1,990,000,000.00 USD | 14,700,000.00 USD | 6,350,000.00 USD | 11,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2442.80` | 761,340,000.00 USD | 761,340,000.00 USD | 1,050,000.00 USD | 1,460,000.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2444.30` | 2,030,000,000.00 USD | 2,030,000,000.00 USD | 8,760,000.00 USD | 15,160,000.00 USD | 13,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 143,630.00 USD | 26,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2445.40` | 763,580,000.00 USD | 763,580,000.00 USD | 177,710.00 USD | 839,480.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2447.20` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 10,560,000.00 USD | 7,370,000.00 USD | 16,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2448.00` | 769,020,000.00 USD | 769,020,000.00 USD | 1,770,000.00 USD | 999,000.00 USD | 2,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2450.10` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 13,890,000.00 USD | 11,320,000.00 USD | 13,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2450.60` | 776,870,000.00 USD | 776,870,000.00 USD | 2,550,000.00 USD | 1,810,000.00 USD | 3,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2453.00` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 8,570,000.00 USD | 7,390,000.00 USD | 6,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2453.20` | 787,320,000.00 USD | 787,320,000.00 USD | 4,190,000.00 USD | 2,730,000.00 USD | 3,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 106,960.00 USD | 26,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2455.80` | 794,730,000.00 USD | 794,730,000.00 USD | 2,340,000.00 USD | 3,540,000.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2455.90` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 5,870,000.00 USD | 8,500,000.00 USD | 6,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2458.40` | 799,890,000.00 USD | 799,890,000.00 USD | 2,400,000.00 USD | 1,520,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2458.80` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 10,050,000.00 USD | 12,000,000.00 USD | 10,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2461.00` | 802,650,000.00 USD | 802,650,000.00 USD | 470,530.00 USD | 1,130,000.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2461.70` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 8,780,000.00 USD | 11,320,000.00 USD | 10,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2463.60` | 806,680,000.00 USD | 806,680,000.00 USD | 352,200.00 USD | 2,830,000.00 USD | 841,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2464.60` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 7,830,000.00 USD | 3,900,000.00 USD | 3,560,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 483,330.00 USD | 27,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2467.50` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 4,540,000.00 USD | 3,120,000.00 USD | 586,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2468.80` | 807,770,000.00 USD | 807,770,000.00 USD | 0.00 USD | 696,010.00 USD | 391,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2470.40` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 2,330,000.00 USD | 2,290,000.00 USD | 496,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2473.30` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 5,250,000.00 USD | 2,920,000.00 USD | 2,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 386,010.00 USD | 27,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2476.20` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 2,680,000.00 USD | 1,500,000.00 USD | 872,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2479.10` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 2,170,000.00 USD | 4,160,000.00 USD | 505,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2482.00` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 1,750,000.00 USD | 1,520,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2484.90` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 0.00 USD | 0.00 USD | 77,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 2,000,000.00 USD | 29,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2487.80` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 826,600.00 USD | 828,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2490.70` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 808,320.00 USD | 1,780,000.00 USD | 279,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2493.60` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 1,610,000.00 USD | 1,690,000.00 USD | 3,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 941,300.00 USD | 30,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2496.50` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 1,670,000.00 USD | 4,820,000.00 USD | 6,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2499.40` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 1,900,000.00 USD | 2,630,000.00 USD | 3,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2502.30` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 647,370.00 USD | 1,090,000.00 USD | 125,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 119,320.00 USD | 30,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2505.20` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 1,270,000.00 USD | 2,310,000.00 USD | 63,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2508.10` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 2,940,000.00 USD | 1,640,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2511.00` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 1,900,000.00 USD | 3,230,000.00 USD | 2,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2513.90` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 776,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 139,000.00 USD | 30,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2516.80` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 97,050.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2519.70` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2520.80` | 807,980,000.00 USD | 807,980,000.00 USD | 80,610.00 USD | 61,830.00 USD | 67,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2522.60` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 1,050,000.00 USD | 0.00 USD | 945,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2523.40` | 808,030,000.00 USD | 808,030,000.00 USD | 0.00 USD | 0.00 USD | 52,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 1,160,000.00 USD | 32,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2525.50` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 307,040.00 USD | 241,310.00 USD | 200,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2526.00` | 808,530,000.00 USD | 808,530,000.00 USD | 421,540.00 USD | 57,450.00 USD | 23,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2528.40` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 1,580,000.00 USD | 1,670,000.00 USD | 727,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2528.60` | 810,230,000.00 USD | 810,230,000.00 USD | 583,810.00 USD | 645,910.00 USD | 464,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2531.20` | 810,640,000.00 USD | 810,640,000.00 USD | 411,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2531.30` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 2,720,000.00 USD | 1,490,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2533.80` | 811,120,000.00 USD | 811,120,000.00 USD | 394,310.00 USD | 62,630.00 USD | 18,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2534.20` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 2,550,000.00 USD | 1,720,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2535.00` | 663,280.00 USD | 32,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2536.40` | 814,510,000.00 USD | 814,510,000.00 USD | 1,580,000.00 USD | 656,520.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2537.10` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 3,380,000.00 USD | 3,160,000.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2539.00` | 819,030,000.00 USD | 819,030,000.00 USD | 1,850,000.00 USD | 1,090,000.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2540.00` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 3,930,000.00 USD | 3,190,000.00 USD | 831,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2541.60` | 820,610,000.00 USD | 820,610,000.00 USD | 831,040.00 USD | 545,930.00 USD | 206,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2542.90` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 3,200,000.00 USD | 2,470,000.00 USD | 2,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2544.20` | 822,920,000.00 USD | 822,920,000.00 USD | 1,090,000.00 USD | 997,870.00 USD | 220,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2545.00` | 6,460,000.00 USD | 39,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2545.80` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 1,770,000.00 USD | 1,140,000.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2546.80` | 827,000,000.00 USD | 827,000,000.00 USD | 2,070,000.00 USD | 1,260,000.00 USD | 753,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2548.70` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 3,840,000.00 USD | 1,820,000.00 USD | 3,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2549.40` | 829,350,000.00 USD | 829,350,000.00 USD | 676,470.00 USD | 786,540.00 USD | 891,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2551.60` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 2,250,000.00 USD | 1,800,000.00 USD | 907,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2552.00` | 831,850,000.00 USD | 831,850,000.00 USD | 1,360,000.00 USD | 909,150.00 USD | 221,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2554.50` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 3,880,000.00 USD | 948,120.00 USD | 3,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2554.60` | 833,650,000.00 USD | 833,650,000.00 USD | 1,350,000.00 USD | 215,710.00 USD | 231,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2555.00` | 2,830,000.00 USD | 42,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2557.20` | 835,340,000.00 USD | 835,340,000.00 USD | 454,490.00 USD | 504,400.00 USD | 737,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2557.40` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 2,780,000.00 USD | 737,060.00 USD | 5,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2559.80` | 839,480,000.00 USD | 839,480,000.00 USD | 2,020,000.00 USD | 1,050,000.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2560.30` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 3,540,000.00 USD | 1,450,000.00 USD | 589,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2562.40` | 841,610,000.00 USD | 841,610,000.00 USD | 241,580.00 USD | 785,260.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2563.20` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 1,400,000.00 USD | 2,900,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2565.00` | 842,960,000.00 USD | 842,960,000.00 USD | 425,980.00 USD | 669,810.00 USD | 248,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2565.00` | 1,790,000.00 USD | 43,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2566.10` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 1,860,000.00 USD | 1,430,000.00 USD | 2,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2567.60` | 843,290,000.00 USD | 843,290,000.00 USD | 121,690.00 USD | 31,040.00 USD | 175,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2569.00` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 56,010.00 USD | 739,480.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2570.20` | 844,480,000.00 USD | 844,480,000.00 USD | 598,470.00 USD | 289,160.00 USD | 302,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2571.90` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 1,390,000.00 USD | 183,530.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2572.80` | 845,690,000.00 USD | 845,690,000.00 USD | 521,320.00 USD | 671,930.00 USD | 16,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2574.80` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 1,450,000.00 USD | 834,660.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2575.00` | 11,830,000.00 USD | 55,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2575.40` | 846,620,000.00 USD | 846,620,000.00 USD | 443,390.00 USD | 0.00 USD | 488,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2577.70` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 2,090,000.00 USD | 1,570,000.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2580.60` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 2,990,000.00 USD | 1,140,000.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2583.50` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 1,080,000.00 USD | 1,260,000.00 USD | 2,720,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2585.00` | 26,470,000.00 USD | 82,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2586.40` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 1,430,000.00 USD | 2,010,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2589.30` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 2,060,000.00 USD | 631,590.00 USD | 2,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2592.20` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 3,590,000.00 USD | 1,280,000.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2595.00` | 8,180,000.00 USD | 90,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2595.10` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 452,020.00 USD | 569,790.00 USD | 752,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2598.00` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 2,280,000.00 USD | 1,630,000.00 USD | 2,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2600.90` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 931,390.00 USD | 1,960,000.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2603.80` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 1,600,000.00 USD | 1,580,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2605.00` | 660,550.00 USD | 91,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2606.70` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 1,480,000.00 USD | 463,200.00 USD | 312,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2609.60` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 1,140,000.00 USD | 510,700.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2612.50` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 962,930.00 USD | 622,830.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2615.00` | 1,190,000.00 USD | 92,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2615.40` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 815,100.00 USD | 967,270.00 USD | 635,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2618.30` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 1,550,000.00 USD | 209,240.00 USD | 434,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2621.20` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 547,980.00 USD | 1,530,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2624.10` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 130,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `Sell Stop` | `1115.00` | 1,500,000,000.00 USD | 0.00 USD | 11,860.00 USD | `-52.27%` | `TACTICAL (Retail Cluster)` |
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
| `Sell Stop` | `1855.00` | 1,500,000,000.00 USD | 0.00 USD | 466,540.00 USD | `-20.59%` | `TACTICAL (Retail Cluster)` |
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
| `Sell Stop` | `2005.00` | 1,450,000,000.00 USD | 0.00 USD | 1,320,000.00 USD | `-14.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2015.00` | 1,450,000,000.00 USD | 0.00 USD | 69,200.00 USD | `-13.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2025.00` | 1,450,000,000.00 USD | 0.00 USD | 5,040.00 USD | `-13.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2035.00` | 1,450,000,000.00 USD | 0.00 USD | 103,890.00 USD | `-12.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2045.00` | 1,450,000,000.00 USD | 0.00 USD | 15,220.00 USD | `-12.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2055.00` | 1,450,000,000.00 USD | 0.00 USD | 212,720.00 USD | `-12.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2065.00` | 1,450,000,000.00 USD | 0.00 USD | 91,330.00 USD | `-11.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2075.00` | 1,450,000,000.00 USD | 0.00 USD | 32,400.00 USD | `-11.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2085.00` | 1,450,000,000.00 USD | 0.00 USD | 52,030.00 USD | `-10.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2095.00` | 1,450,000,000.00 USD | 0.00 USD | 29,710.00 USD | `-10.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2105.00` | 1,450,000,000.00 USD | 0.00 USD | 350,500.00 USD | `-9.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2115.00` | 1,450,000,000.00 USD | 0.00 USD | 127,980.00 USD | `-9.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2125.00` | 1,450,000,000.00 USD | 0.00 USD | 81,460.00 USD | `-9.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2135.00` | 1,450,000,000.00 USD | 0.00 USD | 19,470.00 USD | `-8.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2145.00` | 1,450,000,000.00 USD | 0.00 USD | 214,010.00 USD | `-8.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2155.00` | 1,450,000,000.00 USD | 0.00 USD | 95,600.00 USD | `-7.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2165.00` | 1,450,000,000.00 USD | 0.00 USD | 902,640.00 USD | `-7.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2175.00` | 1,450,000,000.00 USD | 0.00 USD | 1,360,000.00 USD | `-6.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2185.00` | 1,450,000,000.00 USD | 0.00 USD | 91,890.00 USD | `-6.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2195.00` | 1,450,000,000.00 USD | 0.00 USD | 438,560.00 USD | `-6.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2205.00` | 1,450,000,000.00 USD | 0.00 USD | 1,910,000.00 USD | `-5.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2215.00` | 1,450,000,000.00 USD | 0.00 USD | 1,020,000.00 USD | `-5.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2225.00` | 1,440,000,000.00 USD | 0.00 USD | 1,160,000.00 USD | `-4.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2235.00` | 1,440,000,000.00 USD | 0.00 USD | 127,280.00 USD | `-4.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2245.00` | 1,440,000,000.00 USD | 0.00 USD | 1,470,000.00 USD | `-3.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2255.00` | 1,440,000,000.00 USD | 0.00 USD | 23,230,000.00 USD | `-3.46%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2265.00` | 1,420,000,000.00 USD | 0.00 USD | 441,430.00 USD | `-3.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2275.00` | 1,420,000,000.00 USD | 0.00 USD | 4,690,000.00 USD | `-2.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2285.00` | 1,410,000,000.00 USD | 0.00 USD | 4,330,000.00 USD | `-2.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2295.00` | 1,410,000,000.00 USD | 0.00 USD | 11,200,000.00 USD | `-1.75%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2305.00` | 1,400,000,000.00 USD | 0.00 USD | 1,380,000,000.00 USD | `-1.32%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2315.00` | 12,820,000.00 USD | 0.00 USD | 11,740,000.00 USD | `-0.90%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2325.00` | 1,080,000.00 USD | 0.00 USD | 878,040.00 USD | `-0.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2335.00` | 201,710.00 USD | 0.00 USD | 201,710.00 USD | `-0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2345.00` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+0.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2355.00` | 3,290,000.00 USD | 2,240,000.00 USD | 0.00 USD | `+0.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2365.00` | 3,640,000.00 USD | 349,620.00 USD | 0.00 USD | `+1.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2375.00` | 3,950,000.00 USD | 316,910.00 USD | 0.00 USD | `+1.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2385.00` | 5,300,000.00 USD | 1,350,000.00 USD | 0.00 USD | `+2.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2395.00` | 6,930,000.00 USD | 1,630,000.00 USD | 0.00 USD | `+2.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2405.00` | 9,280,000.00 USD | 2,350,000.00 USD | 0.00 USD | `+2.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2415.00` | 9,820,000.00 USD | 535,870.00 USD | 0.00 USD | `+3.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2425.00` | 13,360,000.00 USD | 3,540,000.00 USD | 0.00 USD | `+3.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2435.00` | 13,690,000.00 USD | 335,450.00 USD | 0.00 USD | `+4.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2445.00` | 24,240,000.00 USD | 10,550,000.00 USD | 0.00 USD | `+4.67%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2455.00` | 24,450,000.00 USD | 207,320.00 USD | 0.00 USD | `+5.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2465.00` | 26,620,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+5.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2475.00` | 26,970,000.00 USD | 344,050.00 USD | 0.00 USD | `+5.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2485.00` | 29,120,000.00 USD | 2,160,000.00 USD | 0.00 USD | `+6.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2495.00` | 29,560,000.00 USD | 441,150.00 USD | 0.00 USD | `+6.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2505.00` | 34,930,000.00 USD | 5,370,000.00 USD | 0.00 USD | `+7.24%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2515.00` | 42,710,000.00 USD | 7,780,000.00 USD | 0.00 USD | `+7.67%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2525.00` | 45,990,000.00 USD | 3,280,000.00 USD | 0.00 USD | `+8.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2535.00` | 46,070,000.00 USD | 75,320.00 USD | 0.00 USD | `+8.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2545.00` | 48,220,000.00 USD | 2,160,000.00 USD | 0.00 USD | `+8.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2555.00` | 48,560,000.00 USD | 333,630.00 USD | 0.00 USD | `+9.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2565.00` | 50,890,000.00 USD | 2,330,000.00 USD | 0.00 USD | `+9.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2575.00` | 51,050,000.00 USD | 161,450.00 USD | 0.00 USD | `+10.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2585.00` | 53,510,000.00 USD | 2,450,000.00 USD | 0.00 USD | `+10.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2595.00` | 53,520,000.00 USD | 14,580.00 USD | 0.00 USD | `+11.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2605.00` | 56,620,000.00 USD | 3,100,000.00 USD | 0.00 USD | `+11.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2615.00` | 56,790,000.00 USD | 177,120.00 USD | 0.00 USD | `+11.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2625.00` | 58,980,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+12.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2635.00` | 59,280,000.00 USD | 292,470.00 USD | 0.00 USD | `+12.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2645.00` | 61,440,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+13.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2655.00` | 61,700,000.00 USD | 251,320.00 USD | 0.00 USD | `+13.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2665.00` | 63,850,000.00 USD | 2,160,000.00 USD | 0.00 USD | `+14.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2675.00` | 64,240,000.00 USD | 393,350.00 USD | 0.00 USD | `+14.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2685.00` | 66,430,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+14.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2695.00` | 66,600,000.00 USD | 172,910.00 USD | 0.00 USD | `+15.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2705.00` | 71,280,000.00 USD | 4,670,000.00 USD | 0.00 USD | `+15.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2715.00` | 71,350,000.00 USD | 76,900.00 USD | 0.00 USD | `+16.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2725.00` | 73,830,000.00 USD | 2,480,000.00 USD | 0.00 USD | `+16.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2735.00` | 73,890,000.00 USD | 55,280.00 USD | 0.00 USD | `+17.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2745.00` | 76,190,000.00 USD | 2,300,000.00 USD | 0.00 USD | `+17.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2755.00` | 76,880,000.00 USD | 687,450.00 USD | 0.00 USD | `+17.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2765.00` | 79,260,000.00 USD | 2,380,000.00 USD | 0.00 USD | `+18.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2775.00` | 79,880,000.00 USD | 620,300.00 USD | 0.00 USD | `+18.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2785.00` | 82,180,000.00 USD | 2,290,000.00 USD | 0.00 USD | `+19.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2795.00` | 82,210,000.00 USD | 36,990.00 USD | 0.00 USD | `+19.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2805.00` | 86,480,000.00 USD | 4,270,000.00 USD | 0.00 USD | `+20.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2815.00` | 86,540,000.00 USD | 53,260.00 USD | 0.00 USD | `+20.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2825.00` | 86,600,000.00 USD | 62,020.00 USD | 0.00 USD | `+20.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2835.00` | 86,890,000.00 USD | 289,110.00 USD | 0.00 USD | `+21.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2845.00` | 87,900,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+21.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2855.00` | 89,180,000.00 USD | 1,280,000.00 USD | 0.00 USD | `+22.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2865.00` | 89,190,000.00 USD | 10,290.00 USD | 0.00 USD | `+22.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2875.00` | 89,190,000.00 USD | 3,630.00 USD | 0.00 USD | `+23.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2885.00` | 89,480,000.00 USD | 293,070.00 USD | 0.00 USD | `+23.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2895.00` | 89,510,000.00 USD | 23,020.00 USD | 0.00 USD | `+23.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2905.00` | 91,050,000.00 USD | 1,540,000.00 USD | 0.00 USD | `+24.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2915.00` | 91,060,000.00 USD | 10,340.00 USD | 0.00 USD | `+24.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2925.00` | 91,060,000.00 USD | 3,040.00 USD | 0.00 USD | `+25.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2935.00` | 91,110,000.00 USD | 54,540.00 USD | 0.00 USD | `+25.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2945.00` | 91,150,000.00 USD | 34,650.00 USD | 0.00 USD | `+26.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2955.00` | 91,220,000.00 USD | 74,770.00 USD | 0.00 USD | `+26.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2965.00` | 91,340,000.00 USD | 111,790.00 USD | 0.00 USD | `+26.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2975.00` | 91,480,000.00 USD | 148,070.00 USD | 0.00 USD | `+27.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2985.00` | 95,570,000.00 USD | 4,090,000.00 USD | 0.00 USD | `+27.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2995.00` | 97,490,000.00 USD | 1,920,000.00 USD | 0.00 USD | `+28.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3005.00` | 99,480,000.00 USD | 1,990,000.00 USD | 0.00 USD | `+28.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3015.00` | 99,490,000.00 USD | 6,950.00 USD | 0.00 USD | `+29.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3025.00` | 99,530,000.00 USD | 37,410.00 USD | 0.00 USD | `+29.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3035.00` | 99,600,000.00 USD | 72,990.00 USD | 0.00 USD | `+29.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3045.00` | 99,620,000.00 USD | 22,460.00 USD | 0.00 USD | `+30.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3055.00` | 100,410,000.00 USD | 786,100.00 USD | 0.00 USD | `+30.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3065.00` | 100,410,000.00 USD | 3,360.00 USD | 0.00 USD | `+31.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3075.00` | 100,460,000.00 USD | 50,370.00 USD | 0.00 USD | `+31.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3085.00` | 100,480,000.00 USD | 19,860.00 USD | 0.00 USD | `+32.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3095.00` | 100,480,000.00 USD | 928.50 USD | 0.00 USD | `+32.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3105.00` | 113,890,000.00 USD | 13,410,000.00 USD | 0.00 USD | `+32.92%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `3115.00` | 114,010,000.00 USD | 118,040.00 USD | 0.00 USD | `+33.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3125.00` | 114,380,000.00 USD | 367,790.00 USD | 0.00 USD | `+33.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3145.00` | 114,380,000.00 USD | 1,860.00 USD | 0.00 USD | `+34.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3155.00` | 114,450,000.00 USD | 68,940.00 USD | 0.00 USD | `+35.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3165.00` | 114,460,000.00 USD | 9,860.00 USD | 0.00 USD | `+35.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3175.00` | 114,470,000.00 USD | 16,410.00 USD | 0.00 USD | `+35.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3185.00` | 114,480,000.00 USD | 1,980.00 USD | 0.00 USD | `+36.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3195.00` | 114,510,000.00 USD | 29,580.00 USD | 0.00 USD | `+36.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3205.00` | 115,420,000.00 USD | 910,780.00 USD | 0.00 USD | `+37.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3215.00` | 115,420,000.00 USD | 1,290.00 USD | 0.00 USD | `+37.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3225.00` | 115,420,000.00 USD | 3,740.00 USD | 0.00 USD | `+38.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3235.00` | 115,450,000.00 USD | 30,790.00 USD | 0.00 USD | `+38.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3245.00` | 115,510,000.00 USD | 56,110.00 USD | 0.00 USD | `+38.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3255.00` | 115,710,000.00 USD | 204,030.00 USD | 0.00 USD | `+39.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3265.00` | 115,730,000.00 USD | 15,710.00 USD | 0.00 USD | `+39.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3275.00` | 115,730,000.00 USD | 1,630.00 USD | 0.00 USD | `+40.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3285.00` | 115,870,000.00 USD | 141,980.00 USD | 0.00 USD | `+40.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3295.00` | 115,890,000.00 USD | 16,780.00 USD | 0.00 USD | `+41.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3305.00` | 117,160,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+41.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3315.00` | 117,540,000.00 USD | 385,510.00 USD | 0.00 USD | `+41.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3325.00` | 117,560,000.00 USD | 18,270.00 USD | 0.00 USD | `+42.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3335.00` | 117,580,000.00 USD | 14,190.00 USD | 0.00 USD | `+42.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3345.00` | 117,580,000.00 USD | 617.15 USD | 0.00 USD | `+43.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3355.00` | 117,580,000.00 USD | 334.49 USD | 0.00 USD | `+43.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3365.00` | 117,580,000.00 USD | 597.29 USD | 0.00 USD | `+44.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3375.00` | 117,600,000.00 USD | 23,460.00 USD | 0.00 USD | `+44.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3385.00` | 117,660,000.00 USD | 58,010.00 USD | 0.00 USD | `+44.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3395.00` | 118,020,000.00 USD | 355,050.00 USD | 0.00 USD | `+45.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3405.00` | 119,620,000.00 USD | 1,610,000.00 USD | 0.00 USD | `+45.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3415.00` | 119,620,000.00 USD | 3,510.00 USD | 0.00 USD | `+46.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3425.00` | 119,640,000.00 USD | 16,310.00 USD | 0.00 USD | `+46.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3445.00` | 119,660,000.00 USD | 15,030.00 USD | 0.00 USD | `+47.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3455.00` | 119,670,000.00 USD | 18,600.00 USD | 0.00 USD | `+47.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3465.00` | 119,990,000.00 USD | 311,800.00 USD | 0.00 USD | `+48.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3475.00` | 119,990,000.00 USD | 2,980.00 USD | 0.00 USD | `+48.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3485.00` | 120,030,000.00 USD | 43,610.00 USD | 0.00 USD | `+49.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3495.00` | 120,030,000.00 USD | 158.32 USD | 0.00 USD | `+49.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3505.00` | 120,580,000.00 USD | 550,300.00 USD | 0.00 USD | `+50.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3515.00` | 120,630,000.00 USD | 43,200.00 USD | 0.00 USD | `+50.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3525.00` | 120,630,000.00 USD | 3,690.00 USD | 0.00 USD | `+50.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3535.00` | 120,640,000.00 USD | 9,810.00 USD | 0.00 USD | `+51.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3545.00` | 120,640,000.00 USD | 179.38 USD | 0.00 USD | `+51.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3555.00` | 120,730,000.00 USD | 90,810.00 USD | 0.00 USD | `+52.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3565.00` | 120,730,000.00 USD | 2,300.00 USD | 0.00 USD | `+52.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3585.00` | 120,730,000.00 USD | 354.92 USD | 0.00 USD | `+53.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3595.00` | 120,750,000.00 USD | 13,160.00 USD | 0.00 USD | `+53.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3605.00` | 120,850,000.00 USD | 105,860.00 USD | 0.00 USD | `+54.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3625.00` | 120,860,000.00 USD | 10,210.00 USD | 0.00 USD | `+55.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3635.00` | 120,870,000.00 USD | 7,790.00 USD | 0.00 USD | `+55.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3645.00` | 120,870,000.00 USD | 3,860.00 USD | 0.00 USD | `+56.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3655.00` | 120,880,000.00 USD | 7,740.00 USD | 0.00 USD | `+56.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3665.00` | 120,890,000.00 USD | 8,130.00 USD | 0.00 USD | `+56.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3675.00` | 120,950,000.00 USD | 55,120.00 USD | 0.00 USD | `+57.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3685.00` | 120,950,000.00 USD | 3,550.00 USD | 0.00 USD | `+57.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3705.00` | 120,950,000.00 USD | 819.92 USD | 0.00 USD | `+58.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3715.00` | 120,950,000.00 USD | 323.58 USD | 0.00 USD | `+59.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3725.00` | 120,950,000.00 USD | 1,400.00 USD | 0.00 USD | `+59.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3735.00` | 120,960,000.00 USD | 6,490.00 USD | 0.00 USD | `+59.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3755.00` | 120,960,000.00 USD | 751.00 USD | 0.00 USD | `+60.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3785.00` | 120,960,000.00 USD | 286.90 USD | 0.00 USD | `+62.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3795.00` | 120,960,000.00 USD | 1,560.00 USD | 0.00 USD | `+62.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3805.00` | 121,700,000.00 USD | 734,090.00 USD | 0.00 USD | `+62.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3815.00` | 121,720,000.00 USD | 20,930.00 USD | 0.00 USD | `+63.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3825.00` | 121,720,000.00 USD | 8,380.00 USD | 0.00 USD | `+63.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3835.00` | 121,730,000.00 USD | 711.78 USD | 0.00 USD | `+64.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3845.00` | 121,730,000.00 USD | 932.03 USD | 0.00 USD | `+64.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3855.00` | 121,930,000.00 USD | 203,880.00 USD | 0.00 USD | `+65.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3885.00` | 121,950,000.00 USD | 21,210.00 USD | 0.00 USD | `+66.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3905.00` | 122,130,000.00 USD | 180,010.00 USD | 0.00 USD | `+67.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3915.00` | 122,780,000.00 USD | 646,840.00 USD | 0.00 USD | `+67.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3925.00` | 122,780,000.00 USD | 3,260.00 USD | 0.00 USD | `+68.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3935.00` | 122,820,000.00 USD | 42,570.00 USD | 0.00 USD | `+68.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3945.00` | 122,840,000.00 USD | 19,730.00 USD | 0.00 USD | `+68.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3955.00` | 122,840,000.00 USD | 1,380.00 USD | 0.00 USD | `+69.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3965.00` | 122,850,000.00 USD | 323.54 USD | 0.00 USD | `+69.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3975.00` | 122,850,000.00 USD | 6,960.00 USD | 0.00 USD | `+70.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3985.00` | 122,870,000.00 USD | 14,610.00 USD | 0.00 USD | `+70.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3995.00` | 122,870,000.00 USD | 4,280.00 USD | 0.00 USD | `+71.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4005.00` | 125,530,000.00 USD | 2,660,000.00 USD | 0.00 USD | `+71.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4035.00` | 125,530,000.00 USD | 898.59 USD | 0.00 USD | `+72.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4055.00` | 125,530,000.00 USD | 811.00 USD | 0.00 USD | `+73.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4075.00` | 125,540,000.00 USD | 4,310.00 USD | 0.00 USD | `+74.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4085.00` | 125,540,000.00 USD | 2,800.00 USD | 0.00 USD | `+74.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4095.00` | 125,540,000.00 USD | 2,750.00 USD | 0.00 USD | `+75.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4105.00` | 125,590,000.00 USD | 48,190.00 USD | 0.00 USD | `+75.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4115.00` | 125,600,000.00 USD | 5,990.00 USD | 0.00 USD | `+76.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4125.00` | 125,600,000.00 USD | 372.90 USD | 0.00 USD | `+76.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4145.00` | 125,600,000.00 USD | 395.43 USD | 0.00 USD | `+77.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4185.00` | 125,600,000.00 USD | 376.65 USD | 0.00 USD | `+79.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4205.00` | 125,620,000.00 USD | 28,760.00 USD | 0.00 USD | `+80.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4215.00` | 125,630,000.00 USD | 460.70 USD | 0.00 USD | `+80.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4225.00` | 125,630,000.00 USD | 1,270.00 USD | 0.00 USD | `+80.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4255.00` | 125,630,000.00 USD | 4,300.00 USD | 0.00 USD | `+82.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4265.00` | 125,630,000.00 USD | 4,010.00 USD | 0.00 USD | `+82.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4275.00` | 125,700,000.00 USD | 64,550.00 USD | 0.00 USD | `+83.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4285.00` | 125,700,000.00 USD | 1,610.00 USD | 0.00 USD | `+83.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4305.00` | 125,800,000.00 USD | 97,670.00 USD | 0.00 USD | `+84.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4315.00` | 125,800,000.00 USD | 1,070.00 USD | 0.00 USD | `+84.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4345.00` | 125,810,000.00 USD | 11,270.00 USD | 0.00 USD | `+86.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4355.00` | 125,810,000.00 USD | 3,250.00 USD | 0.00 USD | `+86.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4375.00` | 125,860,000.00 USD | 43,750.00 USD | 0.00 USD | `+87.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4385.00` | 125,920,000.00 USD | 64,570.00 USD | 0.00 USD | `+87.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4395.00` | 125,920,000.00 USD | 1,050.00 USD | 0.00 USD | `+88.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4405.00` | 125,970,000.00 USD | 44,640.00 USD | 0.00 USD | `+88.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4415.00` | 125,980,000.00 USD | 11,480.00 USD | 0.00 USD | `+89.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4425.00` | 125,980,000.00 USD | 2,510.00 USD | 0.00 USD | `+89.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4435.00` | 126,160,000.00 USD | 177,400.00 USD | 0.00 USD | `+89.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4455.00` | 126,160,000.00 USD | 641.97 USD | 0.00 USD | `+90.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4465.00` | 126,160,000.00 USD | 1,030.00 USD | 0.00 USD | `+91.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4505.00` | 126,510,000.00 USD | 343,680.00 USD | 0.00 USD | `+92.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4515.00` | 126,510,000.00 USD | 2,280.00 USD | 0.00 USD | `+93.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4525.00` | 126,510,000.00 USD | 6,560.00 USD | 0.00 USD | `+93.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4565.00` | 126,610,000.00 USD | 97,750.00 USD | 0.00 USD | `+95.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4585.00` | 126,610,000.00 USD | 1,420.00 USD | 0.00 USD | `+96.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4595.00` | 126,620,000.00 USD | 2,610.00 USD | 0.00 USD | `+96.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4605.00` | 126,680,000.00 USD | 64,120.00 USD | 0.00 USD | `+97.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4645.00` | 126,710,000.00 USD | 27,410.00 USD | 0.00 USD | `+98.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4655.00` | 126,880,000.00 USD | 174,790.00 USD | 0.00 USD | `+99.28%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `2057.30` | 2,210,000,000.00 USD | 0.00 USD | 2,210,000,000.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2060.30` | 2,210,000,000.00 USD | 0.00 USD | 2,210,000,000.00 USD | 975,520.00 USD | 1,310,000.00 USD | 0.00 USD |
| `1D` | `2062.80` | 682,320,000.00 USD | 0.00 USD | 682,320,000.00 USD | 80,610.00 USD | 121,470.00 USD | 88,290.00 USD |
| `7D` | `2063.30` | 2,210,000,000.00 USD | 0.00 USD | 2,210,000,000.00 USD | 1,770,000.00 USD | 826,260.00 USD | 894,250.00 USD |
| `1D` | `2065.50` | 682,030,000.00 USD | 0.00 USD | 682,030,000.00 USD | 984,680.00 USD | 494,150.00 USD | 562,550.00 USD |
| `7D` | `2066.30` | 2,200,000,000.00 USD | 0.00 USD | 2,200,000,000.00 USD | 406,250.00 USD | 1,270,000.00 USD | 1,150,000.00 USD |
| `1D` | `2068.20` | 679,990,000.00 USD | 0.00 USD | 679,990,000.00 USD | 333,430.00 USD | 1,010,000.00 USD | 50,470.00 USD |
| `7D` | `2069.30` | 2,200,000,000.00 USD | 0.00 USD | 2,200,000,000.00 USD | 1,580,000.00 USD | 2,090,000.00 USD | 781,940.00 USD |
| `1D` | `2070.90` | 678,600,000.00 USD | 0.00 USD | 678,600,000.00 USD | 1,040,000.00 USD | 0.00 USD | 437,490.00 USD |
| `7D` | `2072.30` | 2,200,000,000.00 USD | 0.00 USD | 2,200,000,000.00 USD | 4,410,000.00 USD | 2,160,000.00 USD | 2,060,000.00 USD |
| `1D` | `2073.60` | 677,110,000.00 USD | 0.00 USD | 677,110,000.00 USD | 419,970.00 USD | 62,630.00 USD | 926,730.00 USD |
| `7D` | `2075.30` | 2,190,000,000.00 USD | 0.00 USD | 2,190,000,000.00 USD | 4,120,000.00 USD | 3,560,000.00 USD | 4,010,000.00 USD |
| `1D` | `2076.30` | 675,710,000.00 USD | 0.00 USD | 675,710,000.00 USD | 2,580,000.00 USD | 926,330.00 USD | 1,620,000.00 USD |
| `7D` | `2078.30` | 2,170,000,000.00 USD | 0.00 USD | 2,170,000,000.00 USD | 4,150,000.00 USD | 3,500,000.00 USD | 1,590,000.00 USD |
| `1D` | `2079.00` | 670,580,000.00 USD | 0.00 USD | 670,580,000.00 USD | 1,320,000.00 USD | 1,100,000.00 USD | 816,960.00 USD |
| `7D` | `2081.30` | 2,170,000,000.00 USD | 0.00 USD | 2,170,000,000.00 USD | 4,720,000.00 USD | 2,960,000.00 USD | 2,480,000.00 USD |
| `1D` | `2081.70` | 667,330,000.00 USD | 0.00 USD | 667,330,000.00 USD | 1,430,000.00 USD | 1,260,000.00 USD | 227,550.00 USD |
| `7D` | `2084.30` | 2,160,000,000.00 USD | 0.00 USD | 2,160,000,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 3,500,000.00 USD |
| `1D` | `2084.40` | 664,420,000.00 USD | 0.00 USD | 664,420,000.00 USD | 2,110,000.00 USD | 1,490,000.00 USD | 753,020.00 USD |
| `1D` | `2087.10` | 660,070,000.00 USD | 0.00 USD | 660,070,000.00 USD | 1,990,000.00 USD | 1,460,000.00 USD | 1,600,000.00 USD |
| `7D` | `2087.30` | 2,150,000,000.00 USD | 0.00 USD | 2,150,000,000.00 USD | 2,990,000.00 USD | 2,750,000.00 USD | 3,020,000.00 USD |
| `1D` | `2089.80` | 655,030,000.00 USD | 0.00 USD | 655,030,000.00 USD | 929,970.00 USD | 225,710.00 USD | 307,510.00 USD |
| `7D` | `2090.30` | 2,140,000,000.00 USD | 0.00 USD | 2,140,000,000.00 USD | 4,840,000.00 USD | 976,840.00 USD | 5,070,000.00 USD |
| `1D` | `2092.50` | 653,560,000.00 USD | 0.00 USD | 653,560,000.00 USD | 966,030.00 USD | 518,530.00 USD | 876,790.00 USD |
| `7D` | `2093.30` | 2,130,000,000.00 USD | 0.00 USD | 2,130,000,000.00 USD | 4,420,000.00 USD | 1,200,000.00 USD | 4,890,000.00 USD |
| `1D` | `2095.20` | 651,200,000.00 USD | 0.00 USD | 651,200,000.00 USD | 2,100,000.00 USD | 1,310,000.00 USD | 1,760,000.00 USD |
| `7D` | `2096.30` | 2,120,000,000.00 USD | 0.00 USD | 2,120,000,000.00 USD | 3,150,000.00 USD | 2,430,000.00 USD | 1,300,000.00 USD |
| `1D` | `2097.90` | 646,030,000.00 USD | 0.00 USD | 646,030,000.00 USD | 474,990.00 USD | 1,170,000.00 USD | 517,910.00 USD |
| `7D` | `2099.30` | 2,110,000,000.00 USD | 0.00 USD | 2,110,000,000.00 USD | 1,460,000.00 USD | 2,870,000.00 USD | 2,050,000.00 USD |
| `1D` | `2100.60` | 643,860,000.00 USD | 0.00 USD | 643,860,000.00 USD | 160,570.00 USD | 44,780.00 USD | 175,760.00 USD |
| `7D` | `2102.30` | 2,100,000,000.00 USD | 0.00 USD | 2,100,000,000.00 USD | 678,000.00 USD | 739,480.00 USD | 2,020,000.00 USD |
| `1D` | `2103.30` | 643,480,000.00 USD | 0.00 USD | 643,480,000.00 USD | 634,340.00 USD | 289,160.00 USD | 306,410.00 USD |
| `7D` | `2105.30` | 2,100,000,000.00 USD | 0.00 USD | 2,100,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 2,210,000.00 USD |
| `1D` | `2106.00` | 642,250,000.00 USD | 0.00 USD | 642,250,000.00 USD | 568,860.00 USD | 671,930.00 USD | 515,540.00 USD |
| `7D` | `2108.30` | 2,100,000,000.00 USD | 0.00 USD | 2,100,000,000.00 USD | 2,400,000.00 USD | 1,090,000.00 USD | 1,840,000.00 USD |
| `1D` | `2108.70` | 640,500,000.00 USD | 0.00 USD | 640,500,000.00 USD | 580,900.00 USD | 21,400.00 USD | 6,190.00 USD |
| `7D` | `2111.30` | 2,090,000,000.00 USD | 0.00 USD | 2,090,000,000.00 USD | 3,450,000.00 USD | 1,630,000.00 USD | 1,970,000.00 USD |
| `1D` | `2111.40` | 639,890,000.00 USD | 0.00 USD | 639,890,000.00 USD | 490,860.00 USD | 146,050.00 USD | 193,960.00 USD |
| `1D` | `2114.10` | 639,060,000.00 USD | 0.00 USD | 639,060,000.00 USD | 420,950.00 USD | 507,320.00 USD | 398,790.00 USD |
| `7D` | `2114.30` | 2,080,000,000.00 USD | 0.00 USD | 2,080,000,000.00 USD | 1,080,000.00 USD | 1,830,000.00 USD | 3,790,000.00 USD |
| `1D` | `2116.80` | 637,730,000.00 USD | 0.00 USD | 637,730,000.00 USD | 679,710.00 USD | 13,230.00 USD | 692,230.00 USD |
| `7D` | `2117.30` | 2,080,000,000.00 USD | 0.00 USD | 2,080,000,000.00 USD | 2,410,000.00 USD | 2,020,000.00 USD | 2,600,000.00 USD |
| `1D` | `2119.50` | 636,340,000.00 USD | 0.00 USD | 636,340,000.00 USD | 15,360.00 USD | 256,720.00 USD | 904,950.00 USD |
| `7D` | `2120.30` | 2,070,000,000.00 USD | 0.00 USD | 2,070,000,000.00 USD | 3,660,000.00 USD | 771,920.00 USD | 1,970,000.00 USD |
| `1D` | `2122.20` | 635,170,000.00 USD | 0.00 USD | 635,170,000.00 USD | 926,060.00 USD | 689,080.00 USD | 1,180,000.00 USD |
| `7D` | `2123.30` | 2,060,000,000.00 USD | 0.00 USD | 2,060,000,000.00 USD | 1,470,000.00 USD | 1,140,000.00 USD | 1,390,000.00 USD |
| `1D` | `2124.90` | 632,370,000.00 USD | 0.00 USD | 632,370,000.00 USD | 1,010,000.00 USD | 1,130,000.00 USD | 769,690.00 USD |
| `7D` | `2126.30` | 2,060,000,000.00 USD | 0.00 USD | 2,060,000,000.00 USD | 2,280,000.00 USD | 2,560,000.00 USD | 3,280,000.00 USD |
| `1D` | `2127.60` | 629,460,000.00 USD | 0.00 USD | 629,460,000.00 USD | 365,910.00 USD | 1,040,000.00 USD | 301,140.00 USD |
| `7D` | `2129.30` | 2,050,000,000.00 USD | 0.00 USD | 2,050,000,000.00 USD | 1,410,000.00 USD | 1,270,000.00 USD | 1,100,000.00 USD |
| `1D` | `2130.30` | 627,760,000.00 USD | 0.00 USD | 627,760,000.00 USD | 0.00 USD | 18,610.00 USD | 654,700.00 USD |
| `7D` | `2132.30` | 2,050,000,000.00 USD | 0.00 USD | 2,050,000,000.00 USD | 2,610,000.00 USD | 1,560,000.00 USD | 1,650,000.00 USD |
| `1D` | `2133.00` | 627,080,000.00 USD | 0.00 USD | 627,080,000.00 USD | 0.00 USD | 937,720.00 USD | 0.00 USD |
| `7D` | `2135.30` | 2,040,000,000.00 USD | 0.00 USD | 2,040,000,000.00 USD | 1,440,000.00 USD | 744,540.00 USD | 10,700.00 USD |
| `1D` | `2135.70` | 626,150,000.00 USD | 0.00 USD | 626,150,000.00 USD | 0.00 USD | 27,230.00 USD | 0.00 USD |
| `7D` | `2138.30` | 2,040,000,000.00 USD | 0.00 USD | 2,040,000,000.00 USD | 1,290,000.00 USD | 660,600.00 USD | 78,760.00 USD |
| `1D` | `2138.40` | 626,120,000.00 USD | 0.00 USD | 626,120,000.00 USD | 0.00 USD | 251,180.00 USD | 0.00 USD |
| `7D` | `2141.30` | 2,040,000,000.00 USD | 0.00 USD | 2,040,000,000.00 USD | 1,750,000.00 USD | 1,130,000.00 USD | 766,720.00 USD |
| `7D` | `2144.30` | 2,030,000,000.00 USD | 0.00 USD | 2,030,000,000.00 USD | 465,960.00 USD | 1,540,000.00 USD | 268,500.00 USD |
| `7D` | `2147.30` | 2,030,000,000.00 USD | 0.00 USD | 2,030,000,000.00 USD | 239,110.00 USD | 10,850.00 USD | 0.00 USD |
| `7D` | `2150.30` | 2,030,000,000.00 USD | 0.00 USD | 2,030,000,000.00 USD | 459,630.00 USD | 463,640.00 USD | 31,040.00 USD |
| `7D` | `2153.30` | 2,030,000,000.00 USD | 0.00 USD | 2,030,000,000.00 USD | 109,800.00 USD | 331,520.00 USD | 0.00 USD |
| `7D` | `2156.30` | 2,030,000,000.00 USD | 0.00 USD | 2,030,000,000.00 USD | 406,850.00 USD | 1,030,000.00 USD | 305,570.00 USD |
| `7D` | `2159.30` | 2,030,000,000.00 USD | 0.00 USD | 2,030,000,000.00 USD | 345,270.00 USD | 863,480.00 USD | 2,280,000.00 USD |
| `7D` | `2162.30` | 2,020,000,000.00 USD | 0.00 USD | 2,020,000,000.00 USD | 867,790.00 USD | 598,340.00 USD | 1,370,000.00 USD |
| `7D` | `2165.30` | 2,020,000,000.00 USD | 0.00 USD | 2,020,000,000.00 USD | 25,540.00 USD | 329,690.00 USD | 402,900.00 USD |
| `7D` | `2168.30` | 2,020,000,000.00 USD | 0.00 USD | 2,020,000,000.00 USD | 1,210,000.00 USD | 373,180.00 USD | 17,870.00 USD |
| `7D` | `2171.30` | 2,020,000,000.00 USD | 0.00 USD | 2,020,000,000.00 USD | 438,050.00 USD | 765,150.00 USD | 794,200.00 USD |
| `7D` | `2174.30` | 2,020,000,000.00 USD | 0.00 USD | 2,020,000,000.00 USD | 479,540.00 USD | 363,040.00 USD | 0.00 USD |
| `7D` | `2195.30` | 2,020,000,000.00 USD | 0.00 USD | 2,020,000,000.00 USD | 141,070.00 USD | 474,090.00 USD | 0.00 USD |
| `7D` | `2198.30` | 2,020,000,000.00 USD | 0.00 USD | 2,020,000,000.00 USD | 2,720,000.00 USD | 2,800,000.00 USD | 0.00 USD |
| `1D` | `2200.50` | 625,870,000.00 USD | 0.00 USD | 625,870,000.00 USD | 284,470.00 USD | 433,420.00 USD | 276,160.00 USD |
| `7D` | `2201.30` | 2,010,000,000.00 USD | 0.00 USD | 2,010,000,000.00 USD | 5,520,000.00 USD | 3,360,000.00 USD | 5,600,000.00 USD |
| `1D` | `2203.20` | 624,870,000.00 USD | 0.00 USD | 624,870,000.00 USD | 2,510,000.00 USD | 1,170,000.00 USD | 1,970,000.00 USD |
| `7D` | `2204.30` | 2,000,000,000.00 USD | 0.00 USD | 2,000,000,000.00 USD | 1,910,000.00 USD | 3,010,000.00 USD | 1,520,000.00 USD |
| `1D` | `2205.90` | 619,220,000.00 USD | 0.00 USD | 619,220,000.00 USD | 1,450,000.00 USD | 3,240,000.00 USD | 781,320.00 USD |
| `7D` | `2207.30` | 1,990,000,000.00 USD | 0.00 USD | 1,990,000,000.00 USD | 7,040,000.00 USD | 7,160,000.00 USD | 3,950,000.00 USD |
| `1D` | `2208.60` | 613,750,000.00 USD | 0.00 USD | 613,750,000.00 USD | 2,490,000.00 USD | 101,520.00 USD | 3,050,000.00 USD |
| `7D` | `2210.30` | 1,970,000,000.00 USD | 0.00 USD | 1,970,000,000.00 USD | 13,680,000.00 USD | 7,280,000.00 USD | 6,220,000.00 USD |
| `1D` | `2211.30` | 608,110,000.00 USD | 0.00 USD | 608,110,000.00 USD | 2,890,000.00 USD | 1,870,000.00 USD | 1,620,000.00 USD |
| `7D` | `2213.30` | 1,940,000,000.00 USD | 0.00 USD | 1,940,000,000.00 USD | 8,860,000.00 USD | 9,440,000.00 USD | 13,140,000.00 USD |
| `1D` | `2214.00` | 601,730,000.00 USD | 0.00 USD | 601,730,000.00 USD | 6,250,000.00 USD | 3,800,000.00 USD | 5,240,000.00 USD |
| `7D` | `2216.30` | 1,910,000,000.00 USD | 0.00 USD | 1,910,000,000.00 USD | 19,200,000.00 USD | 12,720,000.00 USD | 6,120,000.00 USD |
| `1D` | `2216.70` | 586,430,000.00 USD | 0.00 USD | 586,430,000.00 USD | 5,840,000.00 USD | 5,850,000.00 USD | 2,770,000.00 USD |
| `7D` | `2219.30` | 1,870,000,000.00 USD | 0.00 USD | 1,870,000,000.00 USD | 16,080,000.00 USD | 12,970,000.00 USD | 9,280,000.00 USD |
| `1D` | `2219.40` | 571,970,000.00 USD | 0.00 USD | 571,970,000.00 USD | 4,640,000.00 USD | 4,380,000.00 USD | 1,100,000.00 USD |
| `1D` | `2222.10` | 561,850,000.00 USD | 0.00 USD | 561,850,000.00 USD | 6,000,000.00 USD | 3,530,000.00 USD | 2,860,000.00 USD |
| `7D` | `2222.30` | 1,840,000,000.00 USD | 0.00 USD | 1,840,000,000.00 USD | 7,180,000.00 USD | 6,030,000.00 USD | 8,610,000.00 USD |
| `1D` | `2224.80` | 549,460,000.00 USD | 0.00 USD | 549,460,000.00 USD | 4,770,000.00 USD | 4,280,000.00 USD | 4,840,000.00 USD |
| `7D` | `2225.30` | 1,810,000,000.00 USD | 0.00 USD | 1,810,000,000.00 USD | 15,150,000.00 USD | 14,490,000.00 USD | 11,170,000.00 USD |
| `1D` | `2227.50` | 535,570,000.00 USD | 0.00 USD | 535,570,000.00 USD | 5,760,000.00 USD | 3,110,000.00 USD | 1,460,000.00 USD |
| `7D` | `2228.30` | 1,770,000,000.00 USD | 0.00 USD | 1,770,000,000.00 USD | 8,280,000.00 USD | 5,190,000.00 USD | 7,670,000.00 USD |
| `1D` | `2230.20` | 525,240,000.00 USD | 0.00 USD | 525,240,000.00 USD | 3,710,000.00 USD | 2,180,000.00 USD | 1,960,000.00 USD |
| `7D` | `2231.30` | 1,750,000,000.00 USD | 0.00 USD | 1,750,000,000.00 USD | 11,350,000.00 USD | 3,450,000.00 USD | 18,680,000.00 USD |
| `1D` | `2232.90` | 517,390,000.00 USD | 0.00 USD | 517,390,000.00 USD | 5,100,000.00 USD | 2,460,000.00 USD | 3,900,000.00 USD |
| `7D` | `2234.30` | 1,720,000,000.00 USD | 0.00 USD | 1,720,000,000.00 USD | 17,500,000.00 USD | 12,130,000.00 USD | 7,560,000.00 USD |
| `1D` | `2235.60` | 505,930,000.00 USD | 0.00 USD | 505,930,000.00 USD | 5,540,000.00 USD | 4,910,000.00 USD | 5,630,000.00 USD |
| `7D` | `2237.30` | 1,680,000,000.00 USD | 0.00 USD | 1,680,000,000.00 USD | 6,520,000.00 USD | 11,210,000.00 USD | 4,840,000.00 USD |
| `1D` | `2238.30` | 489,850,000.00 USD | 0.00 USD | 489,850,000.00 USD | 1,880,000.00 USD | 2,700,000.00 USD | 844,590.00 USD |
| `7D` | `2240.30` | 1,660,000,000.00 USD | 0.00 USD | 1,660,000,000.00 USD | 8,440,000.00 USD | 6,650,000.00 USD | 9,830,000.00 USD |
| `1D` | `2241.00` | 484,420,000.00 USD | 0.00 USD | 484,420,000.00 USD | 634,700.00 USD | 542,280.00 USD | 601,200.00 USD |
| `7D` | `2243.30` | 1,630,000,000.00 USD | 0.00 USD | 1,630,000,000.00 USD | 7,400,000.00 USD | 9,450,000.00 USD | 8,120,000.00 USD |
| `1D` | `2243.70` | 482,640,000.00 USD | 0.00 USD | 482,640,000.00 USD | 1,640,000.00 USD | 1,310,000.00 USD | 1,230,000.00 USD |
| `7D` | `2246.30` | 1,610,000,000.00 USD | 0.00 USD | 1,610,000,000.00 USD | 13,980,000.00 USD | 9,520,000.00 USD | 10,560,000.00 USD |
| `1D` | `2246.40` | 478,460,000.00 USD | 0.00 USD | 478,460,000.00 USD | 2,780,000.00 USD | 3,030,000.00 USD | 2,010,000.00 USD |
| `1D` | `2249.10` | 470,640,000.00 USD | 0.00 USD | 470,640,000.00 USD | 7,320,000.00 USD | 2,840,000.00 USD | 4,280,000.00 USD |
| `7D` | `2249.30` | 1,580,000,000.00 USD | 0.00 USD | 1,580,000,000.00 USD | 14,130,000.00 USD | 8,010,000.00 USD | 9,730,000.00 USD |
| `1D` | `2251.80` | 456,200,000.00 USD | 0.00 USD | 456,200,000.00 USD | 4,400,000.00 USD | 7,100,000.00 USD | 2,050,000.00 USD |
| `7D` | `2252.30` | 1,540,000,000.00 USD | 0.00 USD | 1,540,000,000.00 USD | 27,030,000.00 USD | 23,830,000.00 USD | 15,760,000.00 USD |
| `1D` | `2254.50` | 442,650,000.00 USD | 0.00 USD | 442,650,000.00 USD | 6,130,000.00 USD | 2,230,000.00 USD | 6,870,000.00 USD |
| `7D` | `2255.30` | 1,480,000,000.00 USD | 0.00 USD | 1,480,000,000.00 USD | 25,980,000.00 USD | 16,790,000.00 USD | 18,760,000.00 USD |
| `1D` | `2257.20` | 427,430,000.00 USD | 0.00 USD | 427,430,000.00 USD | 4,890,000.00 USD | 4,320,000.00 USD | 4,700,000.00 USD |
| `7D` | `2258.30` | 1,420,000,000.00 USD | 0.00 USD | 1,420,000,000.00 USD | 26,340,000.00 USD | 24,750,000.00 USD | 27,990,000.00 USD |
| `1D` | `2259.90` | 413,520,000.00 USD | 0.00 USD | 413,520,000.00 USD | 13,480,000.00 USD | 6,500,000.00 USD | 8,800,000.00 USD |
| `7D` | `2261.30` | 1,340,000,000.00 USD | 0.00 USD | 1,340,000,000.00 USD | 45,180,000.00 USD | 27,760,000.00 USD | 25,230,000.00 USD |
| `1D` | `2262.60` | 384,730,000.00 USD | 0.00 USD | 384,730,000.00 USD | 14,960,000.00 USD | 15,790,000.00 USD | 13,880,000.00 USD |
| `7D` | `2264.30` | 1,240,000,000.00 USD | 0.00 USD | 1,240,000,000.00 USD | 39,820,000.00 USD | 32,460,000.00 USD | 24,120,000.00 USD |
| `1D` | `2265.30` | 340,100,000.00 USD | 0.00 USD | 340,100,000.00 USD | 15,940,000.00 USD | 11,630,000.00 USD | 5,430,000.00 USD |
| `7D` | `2267.30` | 1,140,000,000.00 USD | 0.00 USD | 1,140,000,000.00 USD | 45,000,000.00 USD | 33,340,000.00 USD | 27,400,000.00 USD |
| `1D` | `2268.00` | 307,110,000.00 USD | 0.00 USD | 307,110,000.00 USD | 12,020,000.00 USD | 9,560,000.00 USD | 5,100,000.00 USD |
| `7D` | `2270.30` | 1,040,000,000.00 USD | 0.00 USD | 1,040,000,000.00 USD | 44,170,000.00 USD | 37,480,000.00 USD | 47,400,000.00 USD |
| `1D` | `2270.70` | 280,430,000.00 USD | 0.00 USD | 280,430,000.00 USD | 20,010,000.00 USD | 15,460,000.00 USD | 17,920,000.00 USD |
| `7D` | `2273.30` | 907,030,000.00 USD | 0.00 USD | 907,030,000.00 USD | 33,900,000.00 USD | 35,430,000.00 USD | 20,220,000.00 USD |
| `1D` | `2273.40` | 227,040,000.00 USD | 0.00 USD | 227,040,000.00 USD | 17,480,000.00 USD | 13,060,000.00 USD | 8,920,000.00 USD |
| `1D` | `2276.10` | 187,570,000.00 USD | 0.00 USD | 187,570,000.00 USD | 17,930,000.00 USD | 14,350,000.00 USD | 10,970,000.00 USD |
| `7D` | `2276.30` | 817,480,000.00 USD | 0.00 USD | 817,480,000.00 USD | 58,660,000.00 USD | 46,730,000.00 USD | 59,460,000.00 USD |
| `1D` | `2278.80` | 144,320,000.00 USD | 0.00 USD | 144,320,000.00 USD | 19,120,000.00 USD | 9,120,000.00 USD | 16,050,000.00 USD |
| `7D` | `2279.30` | 652,630,000.00 USD | 0.00 USD | 652,630,000.00 USD | 84,810,000.00 USD | 43,190,000.00 USD | 43,700,000.00 USD |
| `1D` | `2281.50` | 100,030,000.00 USD | 0.00 USD | 100,030,000.00 USD | 19,770,000.00 USD | 13,730,000.00 USD | 21,900,000.00 USD |
| `7D` | `2282.30` | 480,920,000.00 USD | 0.00 USD | 480,920,000.00 USD | 57,660,000.00 USD | 66,030,000.00 USD | 62,530,000.00 USD |
| `1D` | `2284.20` | 44,630,000.00 USD | 0.00 USD | 44,630,000.00 USD | 22,710,000.00 USD | 14,080,000.00 USD | 7,770,000.00 USD |
| `7D` | `2285.30` | 294,700,000.00 USD | 0.00 USD | 294,700,000.00 USD | 83,870,000.00 USD | 19,620,000.00 USD | 32,830,000.00 USD |
| `7D` | `2288.30` | 158,380,000.00 USD | 0.00 USD | 158,380,000.00 USD | 61,070,000.00 USD | 0.00 USD | 11,450,000.00 USD |
| `7D` | `2291.30` | 85,850,000.00 USD | 0.00 USD | 85,850,000.00 USD | 49,180,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2294.30` | 36,670,000.00 USD | 0.00 USD | 36,670,000.00 USD | 30,090,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2297.30` | 6,580,000.00 USD | 0.00 USD | 6,580,000.00 USD | 6,580,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2297.70` | 70,480.00 USD | 0.00 USD | 70,480.00 USD | 0.00 USD | 32,370.00 USD | 38,100.00 USD |
| `7D` | `2298.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2298.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2300.30` | 9,500,000.00 USD | 9,500,000.00 USD | 0.00 USD | 9,500,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2300.40` | 208,270.00 USD | 208,270.00 USD | 0.00 USD | 0.00 USD | 18,850.00 USD | 189,410.00 USD |
| `1D` | `2303.10` | 8,650,000.00 USD | 8,650,000.00 USD | 0.00 USD | 8,350,000.00 USD | 0.00 USD | 95,020.00 USD |
| `7D` | `2303.30` | 21,650,000.00 USD | 21,650,000.00 USD | 0.00 USD | 12,090,000.00 USD | 0.00 USD | 63,260.00 USD |
| `1D` | `2305.80` | 13,040,000.00 USD | 13,040,000.00 USD | 0.00 USD | 0.00 USD | 4,390,000.00 USD | 0.00 USD |
| `7D` | `2306.30` | 25,530,000.00 USD | 25,530,000.00 USD | 0.00 USD | 0.00 USD | 3,740,000.00 USD | 134,160.00 USD |
| `1D` | `2308.50` | 15,000,000.00 USD | 15,000,000.00 USD | 0.00 USD | 0.00 USD | 1,960,000.00 USD | 0.00 USD |
| `7D` | `2309.30` | 25,630,000.00 USD | 25,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 97,260.00 USD |
| `7D` | `2312.30` | 25,700,000.00 USD | 25,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 70,770.00 USD |
| `1D` | `2313.90` | 19,950,000.00 USD | 19,950,000.00 USD | 0.00 USD | 0.00 USD | 4,750,000.00 USD | 203,330.00 USD |
| `7D` | `2315.30` | 33,270,000.00 USD | 33,270,000.00 USD | 0.00 USD | 0.00 USD | 7,460,000.00 USD | 117,510.00 USD |
| `1D` | `2316.60` | 47,570,000.00 USD | 47,570,000.00 USD | 0.00 USD | 5,840,000.00 USD | 16,670,000.00 USD | 5,100,000.00 USD |
| `7D` | `2318.30` | 38,230,000.00 USD | 38,230,000.00 USD | 0.00 USD | 992,100.00 USD | 3,800,000.00 USD | 170,850.00 USD |
| `1D` | `2319.30` | 56,130,000.00 USD | 56,130,000.00 USD | 0.00 USD | 3,330,000.00 USD | 5,160,000.00 USD | 61,930.00 USD |
| `7D` | `2321.30` | 51,050,000.00 USD | 51,050,000.00 USD | 0.00 USD | 0.00 USD | 12,820,000.00 USD | 0.00 USD |
| `1D` | `2322.00` | 58,740,000.00 USD | 58,740,000.00 USD | 0.00 USD | 0.00 USD | 2,610,000.00 USD | 0.00 USD |
| `7D` | `2324.30` | 55,910,000.00 USD | 55,910,000.00 USD | 0.00 USD | 3,130,000.00 USD | 1,740,000.00 USD | 0.00 USD |
| `1D` | `2324.70` | 61,960,000.00 USD | 61,960,000.00 USD | 0.00 USD | 479,120.00 USD | 2,700,000.00 USD | 48,770.00 USD |
| `7D` | `2327.30` | 69,660,000.00 USD | 69,660,000.00 USD | 0.00 USD | 4,980,000.00 USD | 805,740.00 USD | 7,960,000.00 USD |
| `1D` | `2327.40` | 66,640,000.00 USD | 66,640,000.00 USD | 0.00 USD | 256,580.00 USD | 206,450.00 USD | 4,220,000.00 USD |
| `1D` | `2330.10` | 75,630,000.00 USD | 75,630,000.00 USD | 0.00 USD | 8,530,000.00 USD | 251,940.00 USD | 203,390.00 USD |
| `7D` | `2330.30` | 79,030,000.00 USD | 79,030,000.00 USD | 0.00 USD | 9,370,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2332.80` | 93,750,000.00 USD | 93,750,000.00 USD | 0.00 USD | 13,380,000.00 USD | 1,260,000.00 USD | 3,480,000.00 USD |
| `7D` | `2333.30` | 113,140,000.00 USD | 113,140,000.00 USD | 0.00 USD | 26,700,000.00 USD | 7,400,000.00 USD | 0.00 USD |
| `1D` | `2335.50` | 111,690,000.00 USD | 111,690,000.00 USD | 0.00 USD | 15,450,000.00 USD | 405,770.00 USD | 2,080,000.00 USD |
| `7D` | `2336.30` | 152,830,000.00 USD | 152,830,000.00 USD | 0.00 USD | 22,160,000.00 USD | 11,020,000.00 USD | 6,520,000.00 USD |
| `1D` | `2338.20` | 122,510,000.00 USD | 122,510,000.00 USD | 0.00 USD | 6,030,000.00 USD | 688,030.00 USD | 4,110,000.00 USD |
| `7D` | `2339.30` | 171,900,000.00 USD | 171,900,000.00 USD | 0.00 USD | 10,060,000.00 USD | 616,960.00 USD | 8,390,000.00 USD |
| `1D` | `2340.90` | 142,250,000.00 USD | 142,250,000.00 USD | 0.00 USD | 7,730,000.00 USD | 2,210,000.00 USD | 9,800,000.00 USD |
| `7D` | `2342.30` | 210,090,000.00 USD | 210,090,000.00 USD | 0.00 USD | 4,200,000.00 USD | 20,070,000.00 USD | 13,910,000.00 USD |
| `1D` | `2343.60` | 152,770,000.00 USD | 152,770,000.00 USD | 0.00 USD | 1,790,000.00 USD | 3,480,000.00 USD | 5,250,000.00 USD |
| `7D` | `2345.30` | 225,300,000.00 USD | 225,300,000.00 USD | 0.00 USD | 1,350,000.00 USD | 7,920,000.00 USD | 5,940,000.00 USD |
| `1D` | `2346.30` | 162,030,000.00 USD | 162,030,000.00 USD | 0.00 USD | 3,350,000.00 USD | 0.00 USD | 5,910,000.00 USD |
| `7D` | `2348.30` | 256,890,000.00 USD | 256,890,000.00 USD | 0.00 USD | 847,620.00 USD | 7,640,000.00 USD | 23,110,000.00 USD |
| `1D` | `2349.00` | 173,540,000.00 USD | 173,540,000.00 USD | 0.00 USD | 5,950,000.00 USD | 145,980.00 USD | 5,410,000.00 USD |
| `7D` | `2351.30` | 285,640,000.00 USD | 285,640,000.00 USD | 0.00 USD | 782,590.00 USD | 17,680,000.00 USD | 10,280,000.00 USD |
| `1D` | `2351.70` | 201,890,000.00 USD | 201,890,000.00 USD | 0.00 USD | 21,900,000.00 USD | 2,740,000.00 USD | 3,710,000.00 USD |
| `7D` | `2354.30` | 327,340,000.00 USD | 327,340,000.00 USD | 0.00 USD | 5,960,000.00 USD | 35,020,000.00 USD | 723,430.00 USD |
| `1D` | `2354.40` | 224,280,000.00 USD | 224,280,000.00 USD | 0.00 USD | 3,320,000.00 USD | 17,740,000.00 USD | 1,320,000.00 USD |
| `1D` | `2357.10` | 233,140,000.00 USD | 233,140,000.00 USD | 0.00 USD | 2,930,000.00 USD | 2,470,000.00 USD | 3,470,000.00 USD |
| `7D` | `2357.30` | 348,490,000.00 USD | 348,490,000.00 USD | 0.00 USD | 12,050,000.00 USD | 5,920,000.00 USD | 3,190,000.00 USD |
| `1D` | `2359.80` | 250,220,000.00 USD | 250,220,000.00 USD | 0.00 USD | 6,590,000.00 USD | 5,500,000.00 USD | 4,980,000.00 USD |
| `7D` | `2360.30` | 356,640,000.00 USD | 356,640,000.00 USD | 0.00 USD | 4,730,000.00 USD | 3,430,000.00 USD | 0.00 USD |
| `1D` | `2362.50` | 268,840,000.00 USD | 268,840,000.00 USD | 0.00 USD | 8,420,000.00 USD | 6,710,000.00 USD | 3,490,000.00 USD |
| `7D` | `2363.30` | 364,710,000.00 USD | 364,710,000.00 USD | 0.00 USD | 2,820,000.00 USD | 0.00 USD | 5,250,000.00 USD |
| `1D` | `2365.20` | 279,960,000.00 USD | 279,960,000.00 USD | 0.00 USD | 1,870,000.00 USD | 3,710,000.00 USD | 5,540,000.00 USD |
| `7D` | `2366.30` | 372,710,000.00 USD | 372,710,000.00 USD | 0.00 USD | 6,340,000.00 USD | 0.00 USD | 1,660,000.00 USD |
| `1D` | `2367.90` | 287,560,000.00 USD | 287,560,000.00 USD | 0.00 USD | 5,640,000.00 USD | 1,740,000.00 USD | 216,170.00 USD |
| `7D` | `2369.30` | 407,740,000.00 USD | 407,740,000.00 USD | 0.00 USD | 20,720,000.00 USD | 475,460.00 USD | 13,820,000.00 USD |
| `1D` | `2370.60` | 327,500,000.00 USD | 327,500,000.00 USD | 0.00 USD | 17,490,000.00 USD | 12,900,000.00 USD | 9,540,000.00 USD |
| `7D` | `2372.30` | 464,250,000.00 USD | 464,250,000.00 USD | 0.00 USD | 16,520,000.00 USD | 0.00 USD | 39,990,000.00 USD |
| `1D` | `2373.30` | 350,800,000.00 USD | 350,800,000.00 USD | 0.00 USD | 14,350,000.00 USD | 2,370,000.00 USD | 6,580,000.00 USD |
| `7D` | `2375.30` | 486,610,000.00 USD | 486,610,000.00 USD | 0.00 USD | 9,700,000.00 USD | 121,480.00 USD | 12,540,000.00 USD |
| `1D` | `2376.00` | 375,790,000.00 USD | 375,790,000.00 USD | 0.00 USD | 12,200,000.00 USD | 4,350,000.00 USD | 8,440,000.00 USD |
| `7D` | `2378.30` | 529,620,000.00 USD | 529,620,000.00 USD | 0.00 USD | 11,180,000.00 USD | 7,950,000.00 USD | 23,870,000.00 USD |
| `1D` | `2378.70` | 398,380,000.00 USD | 398,380,000.00 USD | 0.00 USD | 5,240,000.00 USD | 7,340,000.00 USD | 10,010,000.00 USD |
| `7D` | `2381.30` | 555,840,000.00 USD | 555,840,000.00 USD | 0.00 USD | 4,540,000.00 USD | 2,390,000.00 USD | 19,290,000.00 USD |
| `1D` | `2381.40` | 445,410,000.00 USD | 445,410,000.00 USD | 0.00 USD | 15,780,000.00 USD | 12,940,000.00 USD | 18,310,000.00 USD |
| `1D` | `2384.10` | 498,850,000.00 USD | 498,850,000.00 USD | 0.00 USD | 23,340,000.00 USD | 18,150,000.00 USD | 11,960,000.00 USD |
| `7D` | `2384.30` | 624,070,000.00 USD | 624,070,000.00 USD | 0.00 USD | 16,580,000.00 USD | 22,660,000.00 USD | 28,990,000.00 USD |
| `1D` | `2386.80` | 536,760,000.00 USD | 536,760,000.00 USD | 0.00 USD | 13,400,000.00 USD | 12,760,000.00 USD | 11,750,000.00 USD |
| `7D` | `2387.30` | 728,880,000.00 USD | 728,880,000.00 USD | 0.00 USD | 11,380,000.00 USD | 36,580,000.00 USD | 56,840,000.00 USD |
| `1D` | `2389.50` | 560,380,000.00 USD | 560,380,000.00 USD | 0.00 USD | 11,060,000.00 USD | 6,460,000.00 USD | 6,110,000.00 USD |
| `7D` | `2390.30` | 831,900,000.00 USD | 831,900,000.00 USD | 0.00 USD | 5,280,000.00 USD | 51,540,000.00 USD | 46,200,000.00 USD |
| `1D` | `2392.20` | 582,100,000.00 USD | 582,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 11,880,000.00 USD | 6,740,000.00 USD |
| `7D` | `2393.30` | 932,690,000.00 USD | 932,690,000.00 USD | 0.00 USD | 41,100,000.00 USD | 34,590,000.00 USD | 25,090,000.00 USD |
| `1D` | `2394.90` | 602,020,000.00 USD | 602,020,000.00 USD | 0.00 USD | 8,320,000.00 USD | 8,870,000.00 USD | 2,730,000.00 USD |
| `7D` | `2396.30` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 0.00 USD | 33,360,000.00 USD | 33,060,000.00 USD | 31,360,000.00 USD |
| `1D` | `2397.60` | 620,080,000.00 USD | 620,080,000.00 USD | 0.00 USD | 3,500,000.00 USD | 6,310,000.00 USD | 8,250,000.00 USD |
| `7D` | `2399.30` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 44,060,000.00 USD | 33,280,000.00 USD | 23,530,000.00 USD |
| `1D` | `2400.30` | 644,780,000.00 USD | 644,780,000.00 USD | 0.00 USD | 11,310,000.00 USD | 4,850,000.00 USD | 8,530,000.00 USD |
| `7D` | `2402.30` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 52,600,000.00 USD | 27,170,000.00 USD | 31,130,000.00 USD |
| `1D` | `2403.00` | 666,920,000.00 USD | 666,920,000.00 USD | 0.00 USD | 6,510,000.00 USD | 7,590,000.00 USD | 8,040,000.00 USD |
| `7D` | `2405.30` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 41,170,000.00 USD | 27,570,000.00 USD | 18,960,000.00 USD |
| `1D` | `2405.70` | 698,420,000.00 USD | 698,420,000.00 USD | 0.00 USD | 14,960,000.00 USD | 8,590,000.00 USD | 7,950,000.00 USD |
| `7D` | `2408.30` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 29,480,000.00 USD | 33,990,000.00 USD | 28,360,000.00 USD |
| `1D` | `2408.40` | 728,720,000.00 USD | 728,720,000.00 USD | 0.00 USD | 11,990,000.00 USD | 10,910,000.00 USD | 7,390,000.00 USD |
| `1D` | `2411.10` | 754,840,000.00 USD | 754,840,000.00 USD | 0.00 USD | 9,330,000.00 USD | 9,450,000.00 USD | 7,340,000.00 USD |
| `7D` | `2411.30` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 0.00 USD | 18,580,000.00 USD | 20,460,000.00 USD | 21,540,000.00 USD |
| `1D` | `2413.80` | 766,310,000.00 USD | 766,310,000.00 USD | 0.00 USD | 4,700,000.00 USD | 3,670,000.00 USD | 3,090,000.00 USD |
| `7D` | `2414.30` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 0.00 USD | 20,830,000.00 USD | 23,120,000.00 USD | 21,590,000.00 USD |
| `1D` | `2416.50` | 783,590,000.00 USD | 783,590,000.00 USD | 0.00 USD | 5,200,000.00 USD | 7,670,000.00 USD | 4,410,000.00 USD |
| `7D` | `2417.30` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 25,250,000.00 USD | 7,450,000.00 USD | 22,010,000.00 USD |
| `1D` | `2419.20` | 794,990,000.00 USD | 794,990,000.00 USD | 0.00 USD | 5,120,000.00 USD | 2,900,000.00 USD | 3,370,000.00 USD |
| `7D` | `2420.30` | 1,690,000,000.00 USD | 1,690,000,000.00 USD | 0.00 USD | 34,500,000.00 USD | 31,850,000.00 USD | 18,740,000.00 USD |
| `1D` | `2421.90` | 810,390,000.00 USD | 810,390,000.00 USD | 0.00 USD | 4,170,000.00 USD | 5,160,000.00 USD | 6,060,000.00 USD |
| `7D` | `2423.30` | 1,760,000,000.00 USD | 1,760,000,000.00 USD | 0.00 USD | 18,720,000.00 USD | 26,340,000.00 USD | 30,210,000.00 USD |
| `1D` | `2424.60` | 815,690,000.00 USD | 815,690,000.00 USD | 0.00 USD | 1,790,000.00 USD | 2,670,000.00 USD | 844,590.00 USD |
| `7D` | `2426.30` | 1,840,000,000.00 USD | 1,840,000,000.00 USD | 0.00 USD | 24,650,000.00 USD | 28,530,000.00 USD | 28,350,000.00 USD |
| `1D` | `2427.30` | 817,150,000.00 USD | 817,150,000.00 USD | 0.00 USD | 731,900.00 USD | 124,100.00 USD | 601,200.00 USD |
| `7D` | `2429.30` | 1,880,000,000.00 USD | 1,880,000,000.00 USD | 0.00 USD | 12,010,000.00 USD | 15,290,000.00 USD | 10,550,000.00 USD |
| `1D` | `2430.00` | 821,680,000.00 USD | 821,680,000.00 USD | 0.00 USD | 1,550,000.00 USD | 1,770,000.00 USD | 1,220,000.00 USD |
| `7D` | `2432.30` | 1,920,000,000.00 USD | 1,920,000,000.00 USD | 0.00 USD | 12,170,000.00 USD | 12,970,000.00 USD | 8,420,000.00 USD |
| `1D` | `2432.70` | 825,710,000.00 USD | 825,710,000.00 USD | 0.00 USD | 2,090,000.00 USD | 1,690,000.00 USD | 247,270.00 USD |
| `7D` | `2435.30` | 1,970,000,000.00 USD | 1,970,000,000.00 USD | 0.00 USD | 25,850,000.00 USD | 17,900,000.00 USD | 11,210,000.00 USD |
| `1D` | `2435.40` | 829,540,000.00 USD | 829,540,000.00 USD | 0.00 USD | 1,790,000.00 USD | 495,600.00 USD | 1,540,000.00 USD |
| `1D` | `2438.10` | 831,020,000.00 USD | 831,020,000.00 USD | 0.00 USD | 777,840.00 USD | 683,870.00 USD | 21,360.00 USD |
| `7D` | `2438.30` | 2,010,000,000.00 USD | 2,010,000,000.00 USD | 0.00 USD | 11,720,000.00 USD | 17,290,000.00 USD | 10,890,000.00 USD |
| `1D` | `2440.80` | 837,240,000.00 USD | 837,240,000.00 USD | 0.00 USD | 2,570,000.00 USD | 2,430,000.00 USD | 1,210,000.00 USD |
| `7D` | `2441.30` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 0.00 USD | 15,870,000.00 USD | 6,990,000.00 USD | 11,510,000.00 USD |
| `1D` | `2443.50` | 839,140,000.00 USD | 839,140,000.00 USD | 0.00 USD | 23,020.00 USD | 534,250.00 USD | 1,350,000.00 USD |
| `7D` | `2444.30` | 2,080,000,000.00 USD | 2,080,000,000.00 USD | 0.00 USD | 8,760,000.00 USD | 15,160,000.00 USD | 13,140,000.00 USD |
| `1D` | `2446.20` | 842,610,000.00 USD | 842,610,000.00 USD | 0.00 USD | 1,880,000.00 USD | 347,060.00 USD | 1,240,000.00 USD |
| `7D` | `2447.30` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 0.00 USD | 11,130,000.00 USD | 7,420,000.00 USD | 16,450,000.00 USD |
| `1D` | `2448.90` | 845,750,000.00 USD | 845,750,000.00 USD | 0.00 USD | 403,160.00 USD | 640,750.00 USD | 2,090,000.00 USD |
| `7D` | `2450.30` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 0.00 USD | 13,320,000.00 USD | 12,230,000.00 USD | 14,320,000.00 USD |
| `1D` | `2451.60` | 855,540,000.00 USD | 855,540,000.00 USD | 0.00 USD | 3,100,000.00 USD | 3,030,000.00 USD | 3,660,000.00 USD |
| `7D` | `2453.30` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 0.00 USD | 8,570,000.00 USD | 6,560,000.00 USD | 5,590,000.00 USD |
| `1D` | `2454.30` | 866,530,000.00 USD | 866,530,000.00 USD | 0.00 USD | 4,830,000.00 USD | 2,910,000.00 USD | 3,250,000.00 USD |
| `7D` | `2456.30` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 0.00 USD | 5,870,000.00 USD | 8,700,000.00 USD | 6,560,000.00 USD |
| `1D` | `2457.00` | 872,730,000.00 USD | 872,730,000.00 USD | 0.00 USD | 1,800,000.00 USD | 2,660,000.00 USD | 1,740,000.00 USD |
| `7D` | `2459.30` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 0.00 USD | 11,550,000.00 USD | 12,370,000.00 USD | 11,370,000.00 USD |
| `1D` | `2459.70` | 877,280,000.00 USD | 877,280,000.00 USD | 0.00 USD | 1,880,000.00 USD | 1,190,000.00 USD | 1,490,000.00 USD |
| `7D` | `2462.30` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 0.00 USD | 9,000,000.00 USD | 11,030,000.00 USD | 8,180,000.00 USD |
| `1D` | `2462.40` | 880,180,000.00 USD | 880,180,000.00 USD | 0.00 USD | 0.00 USD | 2,050,000.00 USD | 841,340.00 USD |
| `1D` | `2465.10` | 881,310,000.00 USD | 881,310,000.00 USD | 0.00 USD | 352,200.00 USD | 780,010.00 USD | 0.00 USD |
| `7D` | `2465.30` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 0.00 USD | 6,340,000.00 USD | 3,130,000.00 USD | 2,800,000.00 USD |
| `1D` | `2467.80` | 881,380,000.00 USD | 881,380,000.00 USD | 0.00 USD | 0.00 USD | 68,070.00 USD | 0.00 USD |
| `7D` | `2468.30` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 0.00 USD | 3,850,000.00 USD | 2,950,000.00 USD | 368,200.00 USD |
| `1D` | `2470.50` | 882,400,000.00 USD | 882,400,000.00 USD | 0.00 USD | 0.00 USD | 627,940.00 USD | 391,890.00 USD |
| `7D` | `2471.30` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 3,230,000.00 USD | 3,380,000.00 USD | 177,760.00 USD |
| `7D` | `2474.30` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 0.00 USD | 5,650,000.00 USD | 843,640.00 USD | 2,420,000.00 USD |
| `7D` | `2477.30` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 0.00 USD | 1,030,000.00 USD | 3,900,000.00 USD | 692,670.00 USD |
| `7D` | `2480.30` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 0.00 USD | 2,110,000.00 USD | 1,740,000.00 USD | 505,810.00 USD |
| `7D` | `2483.30` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 0.00 USD | 1,210,000.00 USD | 1,190,000.00 USD | 77,610.00 USD |
| `7D` | `2486.30` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 0.00 USD | 49,690.00 USD | 51,150.00 USD | 0.00 USD |
| `7D` | `2489.30` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 0.00 USD | 1,400,000.00 USD | 1,360,000.00 USD | 101,890.00 USD |
| `7D` | `2492.30` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 0.00 USD | 1,730,000.00 USD | 2,780,000.00 USD | 3,730,000.00 USD |
| `7D` | `2495.30` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 0.00 USD | 972,540.00 USD | 2,980,000.00 USD | 4,980,000.00 USD |
| `7D` | `2498.30` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 0.00 USD | 2,250,000.00 USD | 3,770,000.00 USD | 3,860,000.00 USD |
| `7D` | `2501.30` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 0.00 USD | 1,040,000.00 USD | 1,460,000.00 USD | 881,650.00 USD |
| `7D` | `2504.30` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 0.00 USD | 47,940.00 USD | 1,320,000.00 USD | 170,270.00 USD |
| `7D` | `2507.30` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 0.00 USD | 4,160,000.00 USD | 3,090,000.00 USD | 2,000,000.00 USD |
| `7D` | `2510.30` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 1,200,000.00 USD | 2,300,000.00 USD | 1,370,000.00 USD |
| `7D` | `2513.30` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 720,490.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2516.30` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD |
| `1D` | `2519.10` | 882,480,000.00 USD | 882,480,000.00 USD | 0.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD |
| `7D` | `2519.30` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD |
| `1D` | `2521.80` | 883,310,000.00 USD | 883,310,000.00 USD | 0.00 USD | 113,940.00 USD | 113,720.00 USD | 600,330.00 USD |
| `7D` | `2522.30` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 0.00 USD | 1,150,000.00 USD | 88,100.00 USD | 945,860.00 USD |
| `1D` | `2524.50` | 884,730,000.00 USD | 884,730,000.00 USD | 0.00 USD | 951,350.00 USD | 442,250.00 USD | 30,180.00 USD |
| `7D` | `2525.30` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 0.00 USD | 307,040.00 USD | 1,160,000.00 USD | 200,040.00 USD |
| `1D` | `2527.20` | 885,480,000.00 USD | 885,480,000.00 USD | 0.00 USD | 333,430.00 USD | 362,000.00 USD | 50,470.00 USD |
| `7D` | `2528.30` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 0.00 USD | 1,580,000.00 USD | 1,690,000.00 USD | 727,590.00 USD |
| `1D` | `2529.90` | 887,560,000.00 USD | 887,560,000.00 USD | 0.00 USD | 995,550.00 USD | 645,910.00 USD | 437,490.00 USD |
| `7D` | `2531.30` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 0.00 USD | 2,720,000.00 USD | 1,490,000.00 USD | 1,230,000.00 USD |
| `1D` | `2532.60` | 887,970,000.00 USD | 887,970,000.00 USD | 0.00 USD | 407,340.00 USD | 0.00 USD | 8,470.00 USD |
| `7D` | `2534.30` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 0.00 USD | 2,660,000.00 USD | 2,230,000.00 USD | 2,030,000.00 USD |
| `1D` | `2535.30` | 889,210,000.00 USD | 889,210,000.00 USD | 0.00 USD | 254,850.00 USD | 62,630.00 USD | 921,740.00 USD |
| `7D` | `2537.30` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 0.00 USD | 3,480,000.00 USD | 3,860,000.00 USD | 3,640,000.00 USD |
| `1D` | `2538.00` | 894,620,000.00 USD | 894,620,000.00 USD | 0.00 USD | 2,380,000.00 USD | 1,020,000.00 USD | 2,000,000.00 USD |
| `7D` | `2540.30` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 0.00 USD | 4,080,000.00 USD | 2,050,000.00 USD | 1,310,000.00 USD |
| `1D` | `2540.70` | 897,240,000.00 USD | 897,240,000.00 USD | 0.00 USD | 1,180,000.00 USD | 1,010,000.00 USD | 436,470.00 USD |
| `7D` | `2543.30` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 0.00 USD | 3,910,000.00 USD | 2,510,000.00 USD | 1,970,000.00 USD |
| `1D` | `2543.40` | 899,870,000.00 USD | 899,870,000.00 USD | 0.00 USD | 1,510,000.00 USD | 1,100,000.00 USD | 21,960.00 USD |
| `1D` | `2546.10` | 902,750,000.00 USD | 902,750,000.00 USD | 0.00 USD | 1,290,000.00 USD | 1,180,000.00 USD | 417,430.00 USD |
| `7D` | `2546.30` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 0.00 USD | 941,430.00 USD | 1,090,000.00 USD | 1,830,000.00 USD |
| `1D` | `2548.80` | 906,840,000.00 USD | 906,840,000.00 USD | 0.00 USD | 1,520,000.00 USD | 944,970.00 USD | 1,620,000.00 USD |
| `7D` | `2549.30` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 0.00 USD | 4,150,000.00 USD | 2,290,000.00 USD | 3,830,000.00 USD |
| `1D` | `2551.50` | 909,760,000.00 USD | 909,760,000.00 USD | 0.00 USD | 1,350,000.00 USD | 984,950.00 USD | 590,610.00 USD |
| `7D` | `2552.30` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 0.00 USD | 1,850,000.00 USD | 1,350,000.00 USD | 893,940.00 USD |
| `1D` | `2554.20` | 911,150,000.00 USD | 911,150,000.00 USD | 0.00 USD | 929,970.00 USD | 224,110.00 USD | 236,190.00 USD |
| `7D` | `2555.30` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 0.00 USD | 4,340,000.00 USD | 952,210.00 USD | 6,980,000.00 USD |
| `1D` | `2556.90` | 913,280,000.00 USD | 913,280,000.00 USD | 0.00 USD | 874,550.00 USD | 509,280.00 USD | 740,260.00 USD |
| `7D` | `2558.30` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 0.00 USD | 3,930,000.00 USD | 1,200,000.00 USD | 2,910,000.00 USD |
| `1D` | `2559.60` | 917,210,000.00 USD | 917,210,000.00 USD | 0.00 USD | 1,830,000.00 USD | 1,040,000.00 USD | 1,060,000.00 USD |
| `7D` | `2561.30` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 0.00 USD | 2,740,000.00 USD | 2,030,000.00 USD | 461,700.00 USD |
| `1D` | `2562.30` | 919,560,000.00 USD | 919,560,000.00 USD | 0.00 USD | 451,210.00 USD | 797,210.00 USD | 1,110,000.00 USD |
| `7D` | `2564.30` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 0.00 USD | 1,840,000.00 USD | 2,150,000.00 USD | 1,460,000.00 USD |
| `1D` | `2565.00` | 920,910,000.00 USD | 920,910,000.00 USD | 0.00 USD | 425,980.00 USD | 669,810.00 USD | 248,570.00 USD |
| `7D` | `2567.30` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 0.00 USD | 575,630.00 USD | 1,560,000.00 USD | 2,700,000.00 USD |
| `1D` | `2567.70` | 921,240,000.00 USD | 921,240,000.00 USD | 0.00 USD | 121,690.00 USD | 31,040.00 USD | 175,760.00 USD |
| `7D` | `2570.30` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 0.00 USD | 125,250.00 USD | 290,680.00 USD | 1,210,000.00 USD |
| `1D` | `2570.40` | 922,430,000.00 USD | 922,430,000.00 USD | 0.00 USD | 598,470.00 USD | 289,160.00 USD | 306,410.00 USD |
| `1D` | `2573.10` | 923,790,000.00 USD | 923,790,000.00 USD | 0.00 USD | 521,320.00 USD | 671,930.00 USD | 168,530.00 USD |
| `7D` | `2573.30` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 0.00 USD | 2,050,000.00 USD | 986,590.00 USD | 1,770,000.00 USD |
| `1D` | `2575.80` | 924,670,000.00 USD | 924,670,000.00 USD | 0.00 USD | 526,800.00 USD | 0.00 USD | 347,020.00 USD |
| `7D` | `2576.30` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 0.00 USD | 2,270,000.00 USD | 356,360.00 USD | 1,640,000.00 USD |
| `7D` | `2579.30` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 0.00 USD | 2,250,000.00 USD | 1,920,000.00 USD | 1,640,000.00 USD |
| `7D` | `2582.30` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 0.00 USD | 2,270,000.00 USD | 1,030,000.00 USD | 3,260,000.00 USD |
| `7D` | `2585.30` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 0.00 USD | 923,330.00 USD | 2,700,000.00 USD | 1,870,000.00 USD |
| `7D` | `2588.30` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 0.00 USD | 2,590,000.00 USD | 578,010.00 USD | 2,580,000.00 USD |
| `7D` | `2591.30` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 0.00 USD | 2,630,000.00 USD | 748,650.00 USD | 726,680.00 USD |
| `7D` | `2594.30` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 0.00 USD | 1,060,000.00 USD | 634,780.00 USD | 1,820,000.00 USD |
| `7D` | `2597.30` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 0.00 USD | 2,700,000.00 USD | 2,150,000.00 USD | 2,440,000.00 USD |
| `7D` | `2600.30` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 0.00 USD | 496,060.00 USD | 1,400,000.00 USD | 1,630,000.00 USD |
| `7D` | `2603.30` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 0.00 USD | 1,660,000.00 USD | 1,250,000.00 USD | 1,640,000.00 USD |
| `7D` | `2606.30` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 0.00 USD | 1,850,000.00 USD | 1,110,000.00 USD | 360,550.00 USD |
| `7D` | `2609.30` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 0.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD |
| `7D` | `2612.30` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 0.00 USD | 1,010,000.00 USD | 608,060.00 USD | 43,560.00 USD |
| `7D` | `2615.30` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 0.00 USD | 815,100.00 USD | 1,000,000.00 USD | 635,670.00 USD |
| `7D` | `2618.30` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 0.00 USD | 1,550,000.00 USD | 209,240.00 USD | 434,750.00 USD |
| `7D` | `2621.30` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 0.00 USD | 547,980.00 USD | 1,530,000.00 USD | 0.00 USD |
| `7D` | `2624.30` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 0.00 USD | 130,830.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2626.50` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 0.00 USD | 459,630.00 USD | 463,640.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `29.31B` | Total OI Tokens: `12,788,266.8 ETH`
  * 1h OI Change: `-1.55%` | 4h OI Change: `-3.24%` | 24h OI Change: `-1.78%`
  * Exchange Breakdown: Binance=`8.73B` | Bybit=`2.14B` | OKX=`1.72B` | Hyperliquid=`2.53B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `845.06K` | Last 24h: `2.27M` | Last 3d: `7.66M` | Last 7d: `13.85M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0075%` | **USDT OKX** | `0.0098%` |
| **USDT Bybit** | `0.0050%` | **USDT KuCoin** | `0.0047%` |
| **USDT MEXC** | `0.0077%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0081%` | **USDT Bitget** | `0.0065%` |
| **CoinM Binance** | `0.0085%` | **CoinM OKX** | `0.0086%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `42.15%` | `57.85%` | `0.73` | 2,020,000,000.00 USD |
| `15M` | `Binance` | `40.27%` | `59.73%` | `0.67` | 696,740,000.00 USD |
| `15M` | `OKX` | `42.44%` | `57.56%` | `0.74` | 402,220,000.00 USD |
| `15M` | `Bybit` | `27.13%` | `72.87%` | `0.37` | 187,400,000.00 USD |
| `15M` | `KuCoin` | `49.96%` | `50.04%` | `1.00` | 10,880,000.00 USD |
| `15M` | `Gate` | `46.51%` | `53.49%` | `0.87` | 182,990,000.00 USD |
| `15M` | `Bitget` | `46.62%` | `53.38%` | `0.87` | 89,690,000.00 USD |
| `15M` | `BingX` | `44.66%` | `55.34%` | `0.81` | 12,160,000.00 USD |
| `15M` | `MEXC` | `39.42%` | `60.58%` | `0.65` | 60,130,000.00 USD |
| `15M` | `Bitunix` | `45.59%` | `54.41%` | `0.84` | 72,990,000.00 USD |
| `15M` | `Hyperliquid` | `38.76%` | `61.24%` | `0.63` | 119,080,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `47.65%` | `52.35%` | `0.91` | 4,820,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `66.92%` | `33.08%` | `2.02` | 121,640,000.00 USD |
| `15M` | `HTX` | `34.42%` | `65.58%` | `0.52` | 13,540,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `40.92%` | `59.08%` | `0.69` | 10,240,000.00 USD |
| `15M` | `Bitfinex` | `18.02%` | `81.98%` | `0.22` | 983,500.00 USD |
| `15M` | `Kraken` | `48.69%` | `51.31%` | `0.95` | 4,360,000.00 USD |
| `15M` | `Aster` | `56.29%` | `43.71%` | `1.29` | 18,250,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `31.45%` | `68.55%` | `0.46` | 16,030,000.00 USD |
| `15M` | `Whale Positions` | `40.27%` | `59.73%` | `0.67` | 696,740,000.00 USD |
| `15M` | `Global Accounts` | `42.15%` | `57.85%` | `0.73` | 2,020,000,000.00 USD |
| `1H` | `ETH` | `44.53%` | `55.47%` | `0.80` | 4,290,000,000.00 USD |
| `1H` | `Binance` | `42.7%` | `57.3%` | `0.75` | 1,450,000,000.00 USD |
| `1H` | `OKX` | `42.83%` | `57.17%` | `0.75` | 829,000,000.00 USD |
| `1H` | `Bybit` | `32.4%` | `67.6%` | `0.48` | 329,250,000.00 USD |
| `1H` | `KuCoin` | `46.86%` | `53.14%` | `0.88` | 17,690,000.00 USD |
| `1H` | `Gate` | `47.95%` | `52.05%` | `0.92` | 569,840,000.00 USD |
| `1H` | `Bitget` | `46.17%` | `53.83%` | `0.86` | 198,690,000.00 USD |
| `1H` | `BingX` | `50.93%` | `49.07%` | `1.04` | 58,880,000.00 USD |
| `1H` | `MEXC` | `47.52%` | `52.48%` | `0.91` | 138,120,000.00 USD |
| `1H` | `Bitunix` | `47.96%` | `52.04%` | `0.92` | 155,020,000.00 USD |
| `1H` | `Hyperliquid` | `49.85%` | `50.15%` | `0.99` | 160,970,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `44.01%` | `55.99%` | `0.79` | 13,790,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `67.02%` | `32.98%` | `2.03` | 172,420,000.00 USD |
| `1H` | `HTX` | `28.58%` | `71.42%` | `0.40` | 47,560,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `43.94%` | `56.06%` | `0.78` | 27,050,000.00 USD |
| `1H` | `Bitfinex` | `22.71%` | `77.29%` | `0.29` | 2,290,000.00 USD |
| `1H` | `Kraken` | `58.92%` | `41.08%` | `1.43` | 9,500,000.00 USD |
| `1H` | `Aster` | `48.22%` | `51.78%` | `0.93` | 40,590,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `47.45%` | `52.55%` | `0.90` | 75,570,000.00 USD |
| `1H` | `Whale Positions` | `42.7%` | `57.3%` | `0.75` | 1,450,000,000.00 USD |
| `1H` | `Global Accounts` | `44.53%` | `55.47%` | `0.80` | 4,290,000,000.00 USD |
| `4H` | `ETH` | `47.13%` | `52.87%` | `0.89` | 9,210,000,000.00 USD |
| `4H` | `Binance` | `44.5%` | `55.5%` | `0.80` | 2,870,000,000.00 USD |
| `4H` | `OKX` | `45.07%` | `54.93%` | `0.82` | 1,740,000,000.00 USD |
| `4H` | `Bybit` | `42.79%` | `57.21%` | `0.75` | 652,840,000.00 USD |
| `4H` | `KuCoin` | `46.46%` | `53.54%` | `0.87` | 28,860,000.00 USD |
| `4H` | `Gate` | `49.05%` | `50.95%` | `0.96` | 1,370,000,000.00 USD |
| `4H` | `Bitget` | `49.63%` | `50.37%` | `0.99` | 475,440,000.00 USD |
| `4H` | `BingX` | `51.02%` | `48.98%` | `1.04` | 126,570,000.00 USD |
| `4H` | `MEXC` | `50.44%` | `49.56%` | `1.02` | 368,660,000.00 USD |
| `4H` | `Bitunix` | `48.5%` | `51.5%` | `0.94` | 348,910,000.00 USD |
| `4H` | `Hyperliquid` | `54.18%` | `45.82%` | `1.18` | 279,570,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.06%` | `51.94%` | `0.93` | 28,400,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `66.4%` | `33.6%` | `1.98` | 448,820,000.00 USD |
| `4H` | `HTX` | `27.28%` | `72.72%` | `0.38` | 132,050,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `47.48%` | `52.52%` | `0.90` | 64,500,000.00 USD |
| `4H` | `Bitfinex` | `23.9%` | `76.1%` | `0.31` | 2,960,000.00 USD |
| `4H` | `Kraken` | `48.8%` | `51.2%` | `0.95` | 25,260,000.00 USD |
| `4H` | `Aster` | `42.58%` | `57.42%` | `0.74` | 93,540,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `49.63%` | `50.37%` | `0.99` | 161,680,000.00 USD |
| `4H` | `Whale Positions` | `44.5%` | `55.5%` | `0.80` | 2,870,000,000.00 USD |
| `4H` | `Global Accounts` | `47.13%` | `52.87%` | `0.89` | 9,210,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `2340.25` | `2338.33` | `2340.25` | `2342.25` | `2333.75` | 43,794,873.23 USD | 24,013,000.37 USD | 19,781,872.86 USD | 4,231,127.51 USD | `+9.66%` | `0B / 2S` |
| `0:00 UTC` | `2327.25` | `2327.16` | `2327.25` | `2335.25` | `2323.25` | 195,411,305.09 USD | 64,523,153.35 USD | 130,888,151.74 USD | -66,364,998.40 USD | `-33.96%` | `0B / 9S` |
| `5:00 UTC` | `2331.25` | `2330.55` | `2331.25` | `2334.25` | `2325.75` | 53,213,391.28 USD | 35,445,824.71 USD | 17,767,566.57 USD | 17,678,258.14 USD | `+33.22%` | `4B / 0S` |
| `0:00 UTC` | `2327.75` | `2328.10` | `2327.75` | `2331.25` | `2326.25` | 28,953,047.89 USD | 13,068,031.79 USD | 15,885,016.10 USD | -2,816,984.30 USD | `-9.73%` | `0B / 1S` |
| `5:00 UTC` | `2326.75` | `2328.61` | `2326.75` | `2331.75` | `2325.75` | 28,646,242.16 USD | 14,157,941.65 USD | 14,488,300.51 USD | -330,358.86 USD | `-1.15%` | `0B / 1S` |
| `0:00 UTC` | `2334.75` | `2334.23` | `2334.75` | `2336.25` | `2330.25` | 36,369,004.25 USD | 19,887,478.26 USD | 16,481,525.99 USD | 3,405,952.27 USD | `+9.36%` | `1B / 1S` |
| `5:00 UTC` | `2335.75` | `2336.07` | `2335.75` | `2338.75` | `2332.75` | 54,317,401.94 USD | 19,276,795.34 USD | 35,040,606.60 USD | -15,763,811.25 USD | `-29.02%` | `0B / 1S` |
| `0:00 UTC` | `2309.25` | `2313.87` | `2309.25` | `2335.75` | `2302.25` | 493,849,561.51 USD | 204,343,201.57 USD | 289,506,359.94 USD | -85,163,158.37 USD | `-17.24%` | `0B / 20S` |
| `5:00 UTC` | `2315.25` | `2315.75` | `2315.25` | `2318.75` | `2312.25` | 88,922,002.19 USD | 46,836,385.14 USD | 42,085,617.06 USD | 4,750,768.08 USD | `+5.34%` | `3B / 0S` |
| `0:00 UTC` | `2314.75` | `2315.42` | `2314.75` | `2316.75` | `2314.75` | 13,195,841.34 USD | 6,670,225.78 USD | 6,525,615.56 USD | 144,610.23 USD | `+1.10%` | `0B / 0S` |

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
| `5m` | -20,880,000.00 USD | -10,300,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -18,500,000.00 USD | -15,000,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -24,360,000.00 USD | -181,930,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -37,820,000.00 USD | -249,180,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -32,000,000.00 USD | -217,180,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -38,060,000.00 USD | -495,550,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -19,000,000.00 USD | -352,780,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -14,920,000.00 USD | -344,250,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -14,870,000.00 USD | -343,560,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -55,820,000.00 USD | -717,790,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -52,740,000.00 USD | -1,270,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,050,000,000.00 USD | -8,430,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-20.88M` | 15m=`-18.50M` | 1h=`-37.82M` | 24h=`-55.82M`
* Futures Capital Netflows: 5m=`-10.30M` | 15m=`-15.00M` | 1h=`-249.18M` | 24h=`-717.79M`
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
  * `2026-10-30 01:35:49 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:59:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:59:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:59:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:49 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:49 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:49 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:00:49 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:00:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:00:49 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:00:49 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `2298.09` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2278.65` (Risk Distance: `19.44` pts)
  * +2.5R Take Profit: `2346.68`
  * Mathematical Lot Sizing: **`0.51 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2335.43` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2354.87` (Risk Distance: `19.44` pts)
  * +2.5R Take Profit: `2286.84`
  * Mathematical Lot Sizing: **`0.51 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2317.29`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
