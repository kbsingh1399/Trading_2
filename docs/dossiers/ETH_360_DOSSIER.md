# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 02:18:32 IST` (`2026-10-29 20:48:32 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2245.90` | **Live Ask Quote**: `2251.70` | **Mid Price**: `2248.80`
- **Spread Points**: `580.00` | **Spread BPS**: `25.79 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
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
  * Value Area High (VAH) = `2336.14` (Distance: `-3.58%`)
  * Point of Control (POC) = `2321.20` (Distance: `-2.96%`)
  * Value Area Low (VAL) = `2296.91` (Distance: `-1.93%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2367.21` | POC=`2350.17` | VAL=`2335.02`
  * Prior Day Extremes: PDH=`2387.80` | PDL=`2316.80` | PDC=`2356.60`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2340.37` | Weekly POC=`2309.77` | Weekly VAL=`2299.57`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2367.70` | Low=`2288.80`
  * London Session (08:00-16:00 UTC): High=`2331.00` | Low=`2299.00`
  * New York Session (13:00-21:00 UTC): High=`2374.90` | Low=`2307.50`
  * Initial Balance (First Hour): IB High=`2331.00` | IB Low=`2299.30`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2239.80` - `2257.80`
  * Optimal Trade Entry (OTE 0.705): `2253.30`
  * Structural Invalidation Anchor (0.786): `2266.79`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2316.30` | `2319.33` | `2286.40` | `2296.35` | `176,799` | 406,074,551.15 USD | -107,664,556.47 USD | `-26.51%` | -526,335,187.53 USD | `-3.31` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `2296.34` | `2305.01` | `2283.13` | `2300.69` | `154,610` | 354,908,357.20 USD | -3,214,479.82 USD | `-0.91%` | -529,549,667.35 USD | `+0.24` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `2300.68` | `2300.68` | `2238.27` | `2252.96` | `321,706` | 728,822,940.26 USD | -185,908,585.08 USD | `-25.51%` | -715,458,252.43 USD | `-3.46` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `2335.68` | `2335.92` | `2302.29` | `2314.66` | `213,441` | 493,862,056.10 USD | -85,150,839.70 USD | `-17.24%` | -423,421,399.14 USD | `-2.59` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `2314.67` | `2318.97` | `2312.06` | `2316.29` | `38,399` | 88,922,002.19 USD | 4,750,768.08 USD | `+5.34%` | -418,670,631.06 USD | `+0.66` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `2316.30` | `2319.33` | `2238.27` | `2252.52` | `652,842` | 1,489,188,927.15 USD | -296,583,156.69 USD | `-19.92%` | -715,253,787.75 USD | `-4.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `2340.61` | `2342.29` | `2323.01` | `2330.23` | `146,197` | 340,744,443.34 USD | -42,605,787.87 USD | `-12.50%` | -327,552,864.00 USD | `-0.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2330.22` | `2338.58` | `2325.76` | `2335.68` | `63,571` | 148,285,696.23 USD | -15,505,202.15 USD | `-10.46%` | -343,058,066.15 USD | `+0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `2335.68` | `2335.92` | `2238.27` | `2252.52` | `904,682` | 2,071,972,985.44 USD | -376,983,228.31 USD | `-18.19%` | -720,041,294.46 USD | `-3.78` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -163,611,405.07 USD | `+1.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -365,767,522.01 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2238.27` | `2251.60` | `904,036` | 2,070,518,995.83 USD | -377,029,546.91 USD | `-18.21%` | -742,797,068.92 USD | `-1.66` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `2308.03` | `2334.83` | `2303.75` | `2309.10` | `525,175` | 1,216,920,375.04 USD | -34,916,746.14 USD | `-2.87%` | -218,489,329.59 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2309.10` | `2330.05` | `2308.88` | `2324.26` | `409,016` | 949,400,649.22 USD | -49,162,247.72 USD | `-5.18%` | -267,651,577.31 USD | `+0.60` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -163,611,405.07 USD | `+1.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -365,767,522.01 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2238.27` | `2251.60` | `904,036` | 2,070,518,995.83 USD | -377,029,546.91 USD | `-18.21%` | -742,797,068.92 USD | `-1.66` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`2248.80`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:14:34 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 02:14:34 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1918.00` | `4,184.01` | 8,024,935.59 USD | `TRIGGER_STOP` | `0x6ea486a342` | `2026-10-30 02:14:34 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `8,500.00` | 16,371,850.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-30 02:14:34 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2040.72` | `7,964.66` | 16,253,666.81 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-30 02:14:34 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2115.25` | `7,500.00` | 15,864,343.04 USD | `AT_RISK_LIQ` | `0x524ed67d71` | `2026-10-30 02:14:34 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2153.94` | `7,000.00` | 15,077,588.76 USD | `AT_RISK_LIQ` | `0x1ee7a73cb5` | `2026-10-30 02:14:34 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2171.19` | `48,499.51` | 105,301,442.50 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 02:14:34 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2180.25` | `44,734.81` | 97,532,977.35 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 02:14:34 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2250.00` | `6,500.00` | 14,625,000.00 USD | `TRIGGER_STOP` | `0x6eae4120a8` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2253.30` | `2,216.47` | 4,994,368.47 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2256.00` | `443.26` | 999,999.97 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x9c062c0575` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2258.00` | `442.87` | 999,999.78 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x9c062c0575` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2268.50` | `1,399.96` | 3,175,816.97 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2268.90` | `5,351.93` | 12,143,003.73 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2270.00` | `881.06` | 1,999,999.84 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x9c062c0575` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2270.40` | `352.40` | 800,091.46 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2271.90` | `337.83` | 767,507.80 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2274.80` | `542.10` | 1,233,178.18 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2277.30` | `994.98` | 2,265,878.43 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2279.30` | `373.95` | 852,337.40 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2279.60` | `2,764.53` | 6,302,016.89 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2282.30` | `688.29` | 1,570,874.68 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2282.80` | `517.35` | 1,181,008.86 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2283.80` | `332.97` | 760,434.83 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2284.70` | `1,752.83` | 4,004,690.47 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2285.90` | `1,313.95` | 3,003,560.36 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2287.30` | `1,410.47` | 3,226,175.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2287.80` | `517.21` | 1,183,263.89 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2288.70` | `715.81` | 1,638,270.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2289.30` | `874.66` | 2,002,351.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2290.00` | `373.16` | 854,545.56 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2290.40` | `655.67` | 1,501,754.13 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2291.90` | `436.81` | 1,001,122.78 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 02:14:34 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2292.00` | `2,500.00` | 5,730,000.00 USD | `TRIGGER_STOP` | `0x934de82f50` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2292.80` | `345.37` | 791,859.75 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2295.30` | `327.14` | 750,877.56 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2300.40` | `326.42` | 750,906.46 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2301.60` | `332.24` | 764,692.79 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2302.30` | `409.29` | 942,296.86 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2303.30` | `434.69` | 1,001,221.94 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2305.20` | `651.52` | 1,501,879.99 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2305.80` | `868.41` | 2,002,377.47 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2306.40` | `442.33` | 1,020,189.91 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2306.60` | `613.87` | 1,415,947.93 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:14:34 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2307.20` | `599,999.99` | 1,384,319,976.93 USD | `TRIGGER_STOP` | `0x069604ebfb` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2307.60` | `1,410.41` | 3,254,653.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2307.60` | `485.04` | 1,119,289.15 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2308.20` | `1,734.99` | 4,004,710.38 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2309.60` | `1,300.44` | 3,003,499.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 02:14:34 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2310.00` | `2,000.00` | 4,620,000.00 USD | `TRIGGER_STOP` | `0x524ed67d71` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2311.60` | `321.29` | 742,691.88 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2311.80` | `675.97` | 1,562,707.45 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2313.80` | `614.39` | 1,421,573.27 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2315.40` | `2,764.05` | 6,399,888.32 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2316.30` | `442.81` | 1,025,673.85 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:14:34 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2319.00` | `2,500.00` | 5,797,500.00 USD | `TRIGGER_STOP` | `0x524ed67d71` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2319.60` | `1,060.06` | 2,458,907.52 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2321.40` | `614.41` | 1,426,289.05 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2324.30` | `5,371.96` | 12,486,046.16 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2326.80` | `343.86` | 800,091.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2327.70` | `329.73` | 767,507.63 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2329.60` | `1,472.79` | 3,431,000.63 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:14:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2336.20` | `2,218.51` | 5,182,875.59 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 02:14:34 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2401.87` | `3,000.91` | 7,207,789.90 USD | `AT_RISK_LIQ` | `0x39b4b3be8d` | `2026-10-30 02:14:34 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2434.97` | `3,111.99` | 7,577,585.59 USD | `AT_RISK_LIQ` | `0x984ec0b4ca` | `2026-10-30 02:14:34 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2440.00` | `4,002.10` | 9,765,127.17 USD | `TRIGGER_STOP` | `0xfb941d2344` | `2026-10-30 02:14:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 240,269,908.35 USD | `106,417.71` | `2322.74` | `2243.00` | `3971.88` | 6,911,103.81 USD | `+2.88%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 149,574,138.55 USD | `65,205.17` | `2375.30` | `2243.00` | `4515.38` | 5,308,124.55 USD | `+3.55%` | `5X Cross` |
| `6` | `0x77dd...e0e9` | `LONG` | 109,671,946.26 USD | `48,499.51` | `2610.31` | `2243.00` | `2171.20` | -16,926,937.61 USD | `-15.43%` | `10X Cross` |
| `7` | `0x0392...d7d9` | `LONG` | 103,511,884.73 USD | `44,734.81` | `2518.71` | `2243.00` | `2180.26` | -9,162,421.85 USD | `-8.85%` | `9X Cross` |
| `14` | `0xde8d...9524` | `LONG` | 70,197,639.55 USD | `30,282.40` | `2134.45` | `2243.00` | `1787.15` | 5,561,308.98 USD | `+7.92%` | `20X Cross` |
| `18` | `0xe813...6d74` | `LONG` | 62,984,796.03 USD | `27,953.86` | `2259.70` | `2243.00` | `1516.78` | -182,681.93 USD | `-0.29%` | `25X Cross` |
| `21` | `0x7fda...17d1` | `SHORT` | 56,798,283.73 USD | `25,108.65` | `2435.72` | `2243.00` | `3998.17` | 4,359,570.26 USD | `+7.68%` | `25X Cross` |
| `25` | `0xdf95...7d72` | `SHORT` | 51,296,929.94 USD | `22,641.65` | `2402.54` | `2243.00` | `4066.88` | 3,100,553.55 USD | `+6.04%` | `25X Cross` |
| `29` | `0xeced...6210` | `SHORT` | 43,211,095.80 USD | `18,687.58` | `2522.09` | `2243.00` | `3345.81` | 3,920,816.65 USD | `+9.07%` | `20X Cross` |
| `35` | `0xb695...a92d` | `SHORT` | 37,715,689.91 USD | `16,704.62` | `2557.74` | `2243.00` | `4139.16` | 5,010,475.14 USD | `+13.28%` | `20X Cross` |
| `36` | `0x6046...b21d` | `LONG` | 36,829,365.66 USD | `15,927.59` | `2410.19` | `2243.00` | `1592.19` | -1,559,253.99 USD | `-4.23%` | `6X Cross` |
| `39` | `0x45d2...4029` | `SHORT` | 31,529,790.00 USD | `13,950.00` | `2443.60` | `2243.00` | `5374.81` | 2,558,492.46 USD | `+8.11%` | `20X Cross` |
| `44` | `0x2371...0883` | `LONG` | 27,526,800.00 USD | `12,000.00` | `2421.77` | `2243.00` | `1280.13` | -1,534,494.85 USD | `-5.57%` | `20X Cross` |
| `45` | `0xbd1c...ff0e` | `LONG` | 27,206,400.00 USD | `12,000.00` | `2419.91` | `2243.00` | `1521.03` | -1,832,632.39 USD | `-6.74%` | `20X Cross` |
| `50` | `0xa9de...e049` | `LONG` | 25,510,100.00 USD | `11,000.00` | `2481.81` | `2243.00` | `1644.77` | -1,789,879.46 USD | `-7.02%` | `20X Cross` |
| `51` | `0x0c5d...36b3` | `LONG` | 25,510,100.00 USD | `11,000.00` | `2482.20` | `2243.00` | `1645.10` | -1,794,153.24 USD | `-7.03%` | `20X Cross` |
| `53` | `0x09dc...c094` | `LONG` | 25,485,900.00 USD | `11,000.00` | `2465.31` | `2243.00` | `1638.10` | -1,632,523.04 USD | `-6.41%` | `20X Cross` |
| `55` | `0x6c93...59a4` | `LONG` | 25,279,100.00 USD | `11,000.00` | `2441.15` | `2243.00` | `1603.06` | -1,573,572.73 USD | `-6.22%` | `20X Cross` |
| `56` | `0xa61c...66b9` | `LONG` | 25,040,222.40 USD | `10,888.00` | `2398.32` | `2243.00` | `1445.37` | -1,072,734.99 USD | `-4.28%` | `10X Cross` |
| `63` | `0x15a4...dfdb` | `LONG` | 23,191,000.00 USD | `10,000.00` | `1761.94` | `2243.00` | `55.52` | 5,571,518.97 USD | `+24.02%` | `20X Cross` |
| `64` | `0xec7f...df39` | `LONG` | 23,165,000.00 USD | `10,000.00` | `2719.35` | `2243.00` | `1721.62` | -4,028,548.52 USD | `-17.39%` | `20X Cross` |
| `67` | `0xa2ce...3126` | `LONG` | 22,660,175.08 USD | `10,016.88` | `2162.83` | `2243.00` | `1520.83` | 995,373.03 USD | `+4.39%` | `10X Cross` |
| `68` | `0x6646...6de5` | `LONG` | 22,656,000.00 USD | `10,000.00` | `1765.80` | `2243.00` | `1718.12` | 4,997,942.55 USD | `+22.06%` | `25X Cross` |
| `72` | `0xaeaa...2416` | `SHORT` | 22,250,830.00 USD | `9,700.00` | `2311.92` | `2243.00` | `2658.71` | 174,852.40 USD | `+0.79%` | `25X Cross` |
| `73` | `0x4487...c92d` | `SHORT` | 21,985,072.18 USD | `9,697.01` | `2368.57` | `2243.00` | `2758.52` | 983,070.11 USD | `+4.47%` | `10X Cross` |
| `81` | `0xca49...53c8` | `SHORT` | 20,976,140.66 USD | `9,264.26` | `2549.47` | `2243.00` | `3856.79` | 2,642,884.08 USD | `+12.60%` | `25X Cross` |
| `82` | `0xba5d...a352` | `SHORT` | 20,970,252.20 USD | `9,054.12` | `2493.89` | `2243.00` | `2940.24` | 1,609,755.06 USD | `+7.68%` | `20X Cross` |
| `83` | `0xea00...a918` | `LONG` | 20,833,953.68 USD | `9,003.83` | `2003.01` | `2243.00` | `1293.48` | 2,799,174.81 USD | `+13.44%` | `5X Cross` |
| `100` | `0xb37f...66ca` | `SHORT` | 19,191,300.00 USD | `8,500.00` | `2308.30` | `2243.00` | `2709.06` | 429,254.19 USD | `+2.24%` | `25X Cross` |
| `105` | `0x218a...7da2` | `SHORT` | 18,547,659.48 USD | `7,997.78` | `2208.16` | `2243.00` | `2877.27` | -887,264.27 USD | `-4.78%` | `10X Cross` |
| `107` | `0x5f91...65aa` | `LONG` | 18,418,266.77 USD | `7,964.66` | `1626.99` | `2243.00` | `2040.74` | 5,459,823.70 USD | `+29.64%` | `16X Cross` |
| `109` | `0x9eec...daab` | `LONG` | 18,292,987.97 USD | `8,092.45` | `1658.44` | `2243.00` | `1926.97` | 4,872,123.44 USD | `+26.63%` | `15X Cross` |
| `115` | `0xab81...c608` | `SHORT` | 17,382,749.25 USD | `7,716.75` | `2307.68` | `2243.00` | `2493.28` | 425,085.77 USD | `+2.45%` | `20X Cross` |
| `118` | `0xcf53...ee11` | `SHORT` | 17,135,535.84 USD | `7,603.63` | `1862.69` | `2243.00` | `4013.88` | -2,972,271.89 USD | `-17.35%` | `7X Cross` |
| `120` | `0x0622...8088` | `LONG` | 16,952,812.14 USD | `7,482.70` | `2286.42` | `2243.00` | `1004.73` | -155,790.29 USD | `-0.92%` | `5X Cross` |
| `123` | `0x939f...04d2` | `LONG` | 16,332,318.59 USD | `7,223.81` | `2500.18` | `2243.00` | `1574.84` | -1,728,571.59 USD | `-10.58%` | `25X Cross` |
| `124` | `0x1ee7...edf5` | `LONG` | 16,230,900.00 USD | `7,000.00` | `2330.22` | `2243.00` | `2153.96` | -80,662.20 USD | `-0.50%` | `25X Cross` |
| `126` | `0xec0b...b078` | `LONG` | 16,084,300.04 USD | `7,007.80` | `2065.97` | `2243.00` | `1021.15` | 1,606,370.45 USD | `+9.99%` | `25X Cross` |
| `133` | `0x0c4a...1b19` | `LONG` | 15,317,192.27 USD | `6,615.35` | `2373.06` | `2243.00` | `2197.06` | -381,449.72 USD | `-2.49%` | `25X Isolated` |
| `134` | `0x4ff9...38d3` | `LONG` | 15,208,360.28 USD | `6,564.10` | `2447.40` | `2243.00` | `1670.72` | -856,662.47 USD | `-5.63%` | `3X Isolated` |
| `135` | `0x418a...8888` | `SHORT` | 15,200,467.32 USD | `6,724.38` | `2494.55` | `2243.00` | `3000.05` | 1,573,855.86 USD | `+10.35%` | `25X Cross` |
| `136` | `0xf78c...c581` | `LONG` | 15,043,462.62 USD | `6,500.22` | `2521.53` | `2243.00` | `1914.20` | -1,347,078.33 USD | `-8.95%` | `20X Cross` |
| `141` | `0x799f...5f4c` | `LONG` | 14,496,775.97 USD | `6,310.90` | `2390.33` | `2243.00` | `1765.58` | -588,388.65 USD | `-4.06%` | `20X Cross` |
| `143` | `0x08bf...7872` | `SHORT` | 14,305,350.54 USD | `6,224.05` | `2258.00` | `2243.00` | `2585.96` | -251,434.44 USD | `-1.76%` | `20X Cross` |
| `151` | `0xd9e7...4aff` | `LONG` | 13,873,800.00 USD | `6,000.00` | `2480.18` | `2243.00` | `1408.49` | -1,007,324.33 USD | `-7.26%` | `20X Cross` |
| `169` | `0xecb6...2b00` | `SHORT` | 12,336,428.51 USD | `5,457.39` | `2288.97` | `2243.00` | `7334.95` | 155,379.14 USD | `+1.26%` | `15X Cross` |
| `180` | `0x645b...87b8` | `SHORT` | 11,370,814.22 USD | `5,015.36` | `2421.67` | `2243.00` | `6622.28` | 774,738.55 USD | `+6.81%` | `10X Cross` |
| `182` | `0x45ab...6cbc` | `LONG` | 11,296,068.73 USD | `4,920.96` | `2727.66` | `2243.00` | `1374.16` | -2,126,675.07 USD | `-18.83%` | `7X Cross` |
| `188` | `0x64b7...9da9` | `LONG` | 11,153,245.54 USD | `4,856.84` | `2604.61` | `2243.00` | `1480.56` | -1,496,968.88 USD | `-13.42%` | `25X Cross` |
| `195` | `0xfb18...eb17` | `SHORT` | 11,001,947.98 USD | `4,863.60` | `2315.54` | `2243.00` | `2589.29` | 259,939.19 USD | `+2.36%` | `25X Cross` |
| `196` | `0x5559...d43b` | `SHORT` | 10,997,126.07 USD | `4,755.93` | `2262.69` | `2243.00` | `2843.73` | -235,920.19 USD | `-2.15%` | `25X Cross` |
| `212` | `0xe091...6705` | `SHORT` | 10,405,350.46 USD | `4,500.00` | `2467.33` | `2243.00` | `2573.01` | 697,658.05 USD | `+6.70%` | `20X Cross` |
| `231` | `0xfe7c...b7ae` | `SHORT` | 9,919,018.60 USD | `4,402.58` | `2440.17` | `2243.00` | `4489.96` | 824,069.27 USD | `+8.31%` | `25X Cross` |
| `237` | `0x12d2...f97f` | `LONG` | 9,784,956.17 USD | `4,264.34` | `2623.90` | `2243.00` | `1895.94` | -1,404,278.25 USD | `-14.35%` | `20X Cross` |
| `239` | `0xc179...e0c8` | `LONG` | 9,722,746.65 USD | `4,309.16` | `2342.89` | `2243.00` | `742.33` | -373,132.14 USD | `-3.84%` | `10X Cross` |
| `242` | `0x6ea4...0ea7` | `SHORT` | 9,690,590.89 USD | `4,184.01` | `2602.13` | `2243.00` | `3426.02` | 1,196,755.78 USD | `+12.35%` | `20X Cross` |
| `243` | `0x28bb...fca6` | `SHORT` | 9,659,759.61 USD | `4,209.61` | `1896.10` | `2243.00` | `3042.30` | -1,677,877.05 USD | `-17.37%` | `20X Cross` |
| `249` | `0x3dc9...54b0` | `SHORT` | 9,274,081.67 USD | `3,999.69` | `2480.32` | `2243.00` | `6122.25` | 646,454.89 USD | `+6.97%` | `20X Cross` |
| `251` | `0xfb94...0ddf` | `SHORT` | 9,254,859.26 USD | `4,002.10` | `2382.44` | `2243.00` | `5105.41` | 279,924.89 USD | `+3.02%` | `20X Cross` |
| `253` | `0x77ee...2902` | `SHORT` | 9,220,453.26 USD | `3,982.23` | `2476.53` | `2243.00` | `4294.33` | 641,668.32 USD | `+6.96%` | `25X Cross` |
| `257` | `0x95fe...f8fa` | `LONG` | 9,179,200.00 USD | `4,000.00` | `2341.35` | `2243.00` | `2259.02` | -186,216.51 USD | `-2.03%` | `20X Isolated` |
| `258` | `0x8cc9...2b6a` | `SHORT` | 9,156,800.00 USD | `4,000.00` | `1791.18` | `2243.00` | `3956.84` | -1,992,053.33 USD | `-21.75%` | `25X Cross` |
| `262` | `0x5e9e...35ee` | `SHORT` | 9,085,930.28 USD | `4,007.56` | `1796.39` | `2243.00` | `2586.51` | -1,886,780.19 USD | `-20.77%` | `20X Cross` |
| `271` | `0xf02d...5eb3` | `LONG` | 8,861,440.28 USD | `3,855.99` | `2513.67` | `2243.00` | `333.53` | -831,272.04 USD | `-9.38%` | `20X Cross` |
| `272` | `0x4b67...f4e7` | `LONG` | 8,857,093.61 USD | `3,820.84` | `2591.51` | `2243.00` | `1600.62` | -1,044,679.93 USD | `-11.79%` | `20X Cross` |
| `292` | `0x8ae4...3d60` | `LONG` | 8,241,143.08 USD | `3,558.20` | `2482.21` | `2243.00` | `384.40` | -591,054.95 USD | `-7.17%` | `10X Cross` |
| `320` | `0x9c06...0560` | `SHORT` | 7,658,359.16 USD | `3,303.58` | `2270.55` | `2243.00` | `3340.13` | -157,395.21 USD | `-2.06%` | `25X Cross` |
| `334` | `0x9c2a...f6a8` | `SHORT` | 7,078,235.87 USD | `3,058.48` | `2543.83` | `2243.00` | `2590.00` | 702,024.76 USD | `+9.92%` | `20X Cross` |
| `335` | `0x984e...14c2` | `SHORT` | 7,055,497.83 USD | `3,111.99` | `2357.50` | `2243.00` | `2434.98` | 281,024.93 USD | `+3.98%` | `20X Cross` |
| `344` | `0x007d...67a0` | `LONG` | 6,786,300.00 USD | `3,000.00` | `2400.00` | `2243.00` | `1471.91` | -413,700.00 USD | `-6.10%` | `25X Cross` |
| `345` | `0x4a20...3c26` | `LONG` | 6,773,400.00 USD | `3,000.00` | `2428.72` | `2243.00` | `544.60` | -512,760.28 USD | `-7.57%` | `20X Cross` |
| `385` | `0xf517...c032` | `SHORT` | 6,287,704.64 USD | `2,738.07` | `2053.90` | `2243.00` | `5376.48` | -663,962.73 USD | `-10.56%` | `25X Cross` |
| `397` | `0xbb34...1696` | `LONG` | 6,028,620.00 USD | `2,600.00` | `2318.80` | `2243.00` | `1996.74` | -280.85 USD | `-0.00%` | `25X Cross` |
| `398` | `0xc619...10f5` | `LONG` | 6,021,860.00 USD | `2,600.00` | `2318.40` | `2243.00` | `1881.22` | -5,988.91 USD | `-0.10%` | `25X Cross` |
| `400` | `0x8328...f54a` | `SHORT` | 5,975,047.75 USD | `2,576.45` | `2292.01` | `2243.00` | `3280.25` | -69,776.46 USD | `-1.17%` | `25X Cross` |
| `407` | `0xed48...7c9b` | `SHORT` | 5,759,942.44 USD | `2,551.13` | `2460.02` | `2243.00` | `3230.28` | 515,903.97 USD | `+8.96%` | `20X Cross` |
| `427` | `0x1c98...7fc7` | `LONG` | 5,459,723.62 USD | `2,358.00` | `2467.15` | `2243.00` | `1897.24` | -357,847.86 USD | `-6.55%` | `10X Cross` |
| `430` | `0xfbe2...c8ea` | `SHORT` | 5,427,924.60 USD | `2,404.08` | `2041.57` | `2243.00` | `2615.54` | -519,831.87 USD | `-9.58%` | `20X Cross` |
| `449` | `0x6859...7e1e` | `SHORT` | 5,116,086.78 USD | `2,224.58` | `2200.39` | `2243.00` | `3876.62` | -221,134.06 USD | `-4.32%` | `25X Cross` |
| `452` | `0x023a...2355` | `LONG` | 5,030,160.56 USD | `2,232.35` | `2330.15` | `2243.00` | `0.000000` | -171,568.17 USD | `-3.41%` | `25X Cross` |
| `455` | `0xb829...3a81` | `LONG` | 4,988,673.27 USD | `2,153.91` | `2537.61` | `2243.00` | `757.55` | -477,123.47 USD | `-9.56%` | `20X Cross` |
| `456` | `0xd507...c948` | `SHORT` | 4,985,174.17 USD | `2,172.00` | `2387.49` | `2243.00` | `2707.44` | 200,466.85 USD | `+4.02%` | `5X Isolated` |
| `476` | `0x382b...3e39` | `SHORT` | 4,817,236.05 USD | `2,129.54` | `2296.66` | `2243.00` | `4610.82` | 73,601.16 USD | `+1.53%` | `25X Cross` |
| `483` | `0x39b4...5c34` | `SHORT` | 4,701,728.43 USD | `2,078.39` | `2329.97` | `2243.00` | `2490.62` | 140,859.24 USD | `+3.00%` | `25X Cross` |
| `488` | `0xf929...d1f9` | `SHORT` | 4,638,200.00 USD | `2,000.00` | `2423.37` | `2243.00` | `2548.84` | 208,540.34 USD | `+4.50%` | `25X Cross` |
| `495` | `0x3440...32c5` | `SHORT` | 4,591,697.25 USD | `2,000.57` | `2198.21` | `2243.00` | `3632.81` | -194,034.11 USD | `-4.23%` | `25X Cross` |
| `506` | `0x8376...9a1e` | `SHORT` | 4,428,720.78 USD | `1,910.50` | `2477.72` | `2243.00` | `3162.12` | 304,967.39 USD | `+6.89%` | `20X Cross` |
| `511` | `0x0514...bdfe` | `SHORT` | 4,408,794.00 USD | `1,950.00` | `1988.74` | `2243.00` | `3040.77` | -530,734.37 USD | `-12.04%` | `25X Cross` |
| `513` | `0x7a6d...f79c` | `SHORT` | 4,382,660.84 USD | `1,933.07` | `2424.40` | `2243.00` | `2665.86` | 303,888.24 USD | `+6.93%` | `25X Cross` |
| `537` | `0x7265...91a5` | `LONG` | 4,166,462.61 USD | `1,801.87` | `2533.96` | `2243.00` | `1988.16` | -399,403.84 USD | `-9.59%` | `20X Cross` |
| `538` | `0x739c...cfb2` | `SHORT` | 4,165,020.00 USD | `1,800.00` | `2427.60` | `2243.00` | `2604.56` | 204,676.38 USD | `+4.91%` | `25X Cross` |
| `551` | `0x541e...071d` | `SHORT` | 4,075,329.00 USD | `1,805.00` | `2648.19` | `2243.00` | `3151.95` | 704,655.84 USD | `+17.29%` | `25X Cross` |
| `555` | `0x91a9...3f70` | `SHORT` | 4,053,538.63 USD | `1,767.48` | `2156.23` | `2243.00` | `3663.93` | -242,434.55 USD | `-5.98%` | `4X Cross` |
| `556` | `0x3453...b323` | `SHORT` | 4,049,609.84 USD | `1,750.12` | `2328.82` | `2243.00` | `2399.97` | 26,122.29 USD | `+0.65%` | `25X Cross` |
| `566` | `0xa445...329d` | `LONG` | 4,015,808.77 USD | `1,776.75` | `2398.85` | `2243.00` | `1970.12` | -246,360.58 USD | `-6.13%` | `25X Cross` |
| `593` | `0xfeec...4e9c` | `SHORT` | 3,886,253.99 USD | `1,691.81` | `2566.49` | `2243.00` | `2653.12` | 455,770.52 USD | `+11.73%` | `10X Cross` |
| `602` | `0x936c...bb0f` | `SHORT` | 3,816,768.10 USD | `1,688.69` | `2434.60` | `2243.00` | `8712.90` | 294,519.01 USD | `+7.72%` | `20X Cross` |
| `609` | `0xeee0...0b53` | `LONG` | 3,785,521.59 USD | `1,637.12` | `2468.64` | `2243.00` | `158.25` | -255,954.47 USD | `-6.76%` | `7X Cross` |
| `613` | `0x27b8...12fc` | `LONG` | 3,769,749.28 USD | `1,628.12` | `2468.73` | `2243.00` | `476.68` | -249,645.35 USD | `-6.62%` | `10X Cross` |
| `615` | `0x982b...4606` | `LONG` | 3,762,015.01 USD | `1,626.82` | `2575.24` | `2243.00` | `1548.44` | -427,438.07 USD | `-11.36%` | `5X Isolated` |
| `630` | `0xb15b...dbae` | `SHORT` | 3,645,603.80 USD | `1,591.83` | `2326.10` | `2243.00` | `2337.25` | 57,151.44 USD | `+1.57%` | `25X Cross` |
| `632` | `0x73d7...8be1` | `LONG` | 3,630,842.58 USD | `1,601.47` | `2410.40` | `2243.00` | `2079.62` | -229,336.34 USD | `-6.32%` | `25X Cross` |
| `646` | `0xe170...9300` | `SHORT` | 3,545,527.48 USD | `1,533.40` | `2076.39` | `2243.00` | `3240.60` | -361,577.98 USD | `-10.20%` | `25X Cross` |
| `656` | `0x2e2b...2fab` | `LONG` | 3,488,522.59 USD | `1,507.38` | `2245.53` | `2243.00` | `1164.16` | 103,649.49 USD | `+2.97%` | `25X Cross` |
| `666` | `0x3bca...66f3` | `SHORT` | 3,453,623.43 USD | `1,508.00` | `2313.35` | `2243.00` | `7667.51` | 34,920.02 USD | `+1.01%` | `25X Cross` |
| `667` | `0x251f...6e5d` | `LONG` | 3,442,800.00 USD | `1,500.00` | `2346.68` | `2243.00` | `1767.36` | -77,230.49 USD | `-2.24%` | `20X Cross` |
| `668` | `0xd911...961e` | `SHORT` | 3,439,828.85 USD | `1,525.76` | `2263.98` | `2243.00` | `3813.01` | 14,476.46 USD | `+0.42%` | `25X Cross` |
| `674` | `0xfc66...ca06` | `LONG` | 3,404,571.35 USD | `1,506.31` | `2303.59` | `2243.00` | `0.000000` | -65,362.24 USD | `-1.92%` | `20X Cross` |
| `680` | `0xad54...6203` | `LONG` | 3,371,604.49 USD | `1,458.18` | `2627.45` | `2243.00` | `2145.32` | -459,702.19 USD | `-13.63%` | `10X Isolated` |
| `692` | `0xbadb...9ee6` | `LONG` | 3,310,760.51 USD | `1,428.16` | `1936.00` | `2243.00` | `1059.83` | 545,838.87 USD | `+16.49%` | `20X Cross` |
| `693` | `0xef70...a84c` | `SHORT` | 3,310,519.01 USD | `1,442.74` | `2424.73` | `2243.00` | `3375.05` | 187,751.82 USD | `+5.67%` | `25X Cross` |
| `695` | `0x4b5f...0dd8` | `LONG` | 3,291,352.70 USD | `1,431.96` | `2339.45` | `2243.00` | `2148.73` | -58,640.24 USD | `-1.78%` | `10X Cross` |
| `704` | `0xd4c1...3d1d` | `SHORT` | 3,236,346.25 USD | `1,431.88` | `2336.05` | `2243.00` | `6603.26` | 108,619.12 USD | `+3.36%` | `12X Cross` |
| `765` | `0x880a...311c` | `SHORT` | 3,035,456.95 USD | `1,320.22` | `2425.76` | `2243.00` | `8343.54` | 167,092.20 USD | `+5.50%` | `9X Cross` |
| `767` | `0x0dd5...f6ee` | `LONG` | 3,008,119.09 USD | `1,314.85` | `2312.84` | `2243.00` | `1656.79` | -32,933.37 USD | `-1.09%` | `5X Cross` |
| `787` | `0xb8eb...1dd5` | `LONG` | 2,940,918.63 USD | `1,305.33` | `2259.72` | `2243.00` | `593.67` | -8,777.03 USD | `-0.30%` | `25X Cross` |
| `798` | `0xc435...c905` | `SHORT` | 2,894,236.80 USD | `1,248.00` | `2704.38` | `2243.00` | `4945.84` | 480,833.55 USD | `+16.61%` | `20X Cross` |
| `813` | `0x2577...4897` | `LONG` | 2,838,341.80 USD | `1,253.57` | `2315.75` | `2243.00` | `0.000000` | -64,623.32 USD | `-2.28%` | `15X Cross` |
| `817` | `0x7178...0854` | `LONG` | 2,824,178.50 USD | `1,218.63` | `2461.81` | `2243.00` | `1079.20` | -175,867.90 USD | `-6.23%` | `10X Cross` |
| `818` | `0xfc27...9d9d` | `SHORT` | 2,823,700.26 USD | `1,248.27` | `2398.18` | `2243.00` | `16353.32` | 169,864.36 USD | `+6.02%` | `25X Cross` |
| `864` | `0x07fd...689d` | `LONG` | 2,637,326.74 USD | `1,166.49` | `2419.97` | `2243.00` | `0.000000` | -185,565.07 USD | `-7.04%` | `25X Cross` |
| `901` | `0x2f80...f203` | `SHORT` | 2,522,096.48 USD | `1,088.94` | `1984.00` | `2243.00` | `3071.71` | -361,629.29 USD | `-14.34%` | `20X Cross` |
| `910` | `0x2b61...2f6c` | `SHORT` | 2,493,506.77 USD | `1,076.60` | `2681.75` | `2243.00` | `6327.25` | 393,665.96 USD | `+15.79%` | `10X Cross` |
| `917` | `0x6f11...0389` | `SHORT` | 2,475,118.10 USD | `1,079.00` | `2333.39` | `2243.00` | `3199.71` | 42,610.81 USD | `+1.72%` | `25X Cross` |
| `950` | `0x1b2a...f7a6` | `LONG` | 2,370,958.43 USD | `1,025.37` | `2737.51` | `2243.00` | `883.11` | -436,001.51 USD | `-18.39%` | `10X Cross` |
| `969` | `0x4044...794c` | `LONG` | 2,318,700.00 USD | `1,000.00` | `2332.68` | `2243.00` | `0.000000` | -13,989.84 USD | `-0.60%` | `25X Cross` |
| `972` | `0x02aa...1806` | `SHORT` | 2,316,128.81 USD | `1,007.10` | `2654.68` | `2243.00` | `3613.71` | 357,403.29 USD | `+15.43%` | `20X Cross` |
| `973` | `0x001a...fef6` | `SHORT` | 2,315,235.78 USD | `1,007.33` | `2022.19` | `2243.00` | `3060.59` | -278,227.82 USD | `-12.02%` | `10X Cross` |
| `974` | `0x5986...89d9` | `LONG` | 2,312,800.00 USD | `1,000.00` | `2346.34` | `2243.00` | `1283.38` | -33,549.54 USD | `-1.45%` | `25X Cross` |
| `976` | `0x2828...93a0` | `LONG` | 2,312,300.00 USD | `1,000.00` | `2393.30` | `2243.00` | `2283.50` | -81,009.16 USD | `-3.50%` | `25X Cross` |
| `981` | `0xdb3a...cf3b` | `LONG` | 2,301,475.76 USD | `1,003.22` | `2705.01` | `2243.00` | `0.000000` | -412,231.13 USD | `-17.91%` | `4X Cross` |
| `982` | `0xfe82...ce65` | `SHORT` | 2,298,500.00 USD | `1,000.00` | `2300.50` | `2243.00` | `2718.45` | 2,007.93 USD | `+0.09%` | `25X Cross` |
| `983` | `0x5272...fcd9` | `SHORT` | 2,298,100.00 USD | `1,000.00` | `2241.82` | `2243.00` | `2880.78` | -56,275.51 USD | `-2.45%` | `5X Cross` |
| `987` | `0xdf60...d3c7` | `LONG` | 2,294,800.00 USD | `1,000.00` | `2736.24` | `2243.00` | `2246.10` | -441,442.88 USD | `-19.24%` | `10X Isolated` |
| `1005` | `0xb002...ed8a` | `SHORT` | 2,231,829.59 USD | `962.78` | `2299.66` | `2243.00` | `4195.93` | -17,751.68 USD | `-0.80%` | `25X Cross` |
| `1036` | `0xc8fe...afa4` | `LONG` | 2,150,284.20 USD | `936.37` | `2331.34` | `2243.00` | `2145.83` | -32,720.03 USD | `-1.52%` | `10X Isolated` |
| `1041` | `0x2e30...4cb5` | `SHORT` | 2,137,733.59 USD | `945.02` | `2340.09` | `2243.00` | `7573.97` | 73,704.85 USD | `+3.45%` | `2X Cross` |
| `1054` | `0x9606...4e5d` | `SHORT` | 2,116,508.95 USD | `913.00` | `2478.70` | `2243.00` | `4054.78` | 146,544.65 USD | `+6.92%` | `20X Cross` |
| `1072` | `0xaeea...bfa7` | `LONG` | 2,088,389.87 USD | `908.75` | `2339.31` | `2243.00` | `2286.75` | -37,452.23 USD | `-1.79%` | `23X Isolated` |
| `1084` | `0x5238...54e5` | `SHORT` | 2,065,140.00 USD | `900.00` | `2289.53` | `2243.00` | `5110.21` | -4,557.58 USD | `-0.22%` | `25X Cross` |
| `1102` | `0xbef3...0d3e` | `LONG` | 2,025,314.81 USD | `880.99` | `2330.82` | `2243.00` | `2123.97` | -28,125.97 USD | `-1.39%` | `20X Cross` |
| `1113` | `0x6a41...a3b9` | `LONG` | 2,013,272.11 USD | `876.06` | `2330.62` | `2243.00` | `2126.17` | -28,489.82 USD | `-1.42%` | `20X Cross` |
| `1147` | `0x20ad...8183` | `SHORT` | 1,978,722.37 USD | `876.39` | `2308.01` | `2243.00` | `2352.21` | 44,005.90 USD | `+2.22%` | `25X Isolated` |
| `1185` | `0xcd27...52a8` | `LONG` | 1,920,472.12 USD | `837.21` | `2553.56` | `2243.00` | `1404.25` | -217,392.66 USD | `-11.32%` | `2X Cross` |
| `1222` | `0x7737...bf66` | `SHORT` | 1,852,557.98 USD | `799.79` | `2494.83` | `2243.00` | `24700.47` | 142,788.05 USD | `+7.71%` | `15X Cross` |
| `1234` | `0xa0fb...96be` | `LONG` | 1,842,767.66 USD | `803.93` | `2310.75` | `2243.00` | `1130.96` | -14,914.48 USD | `-0.81%` | `3X Cross` |
| `1242` | `0x04a9...95aa` | `LONG` | 1,835,120.00 USD | `800.00` | `2595.13` | `2243.00` | `1872.22` | -240,986.74 USD | `-13.13%` | `5X Cross` |
| `1257` | `0xf83f...625f` | `SHORT` | 1,819,388.49 USD | `803.05` | `2601.00` | `2243.00` | `6130.17` | 269,347.96 USD | `+14.80%` | `20X Cross` |
| `1262` | `0x3fc5...c0c1` | `SHORT` | 1,811,350.32 USD | `804.26` | `2702.11` | `2243.00` | `5487.28` | 361,851.21 USD | `+19.98%` | `25X Cross` |
| `1276` | `0x458d...ab3b` | `LONG` | 1,796,715.77 USD | `774.75` | `2740.41` | `2243.00` | `1888.01` | -326,413.42 USD | `-18.17%` | `3X Isolated` |
| `1308` | `0x5f10...d49d` | `SHORT` | 1,723,800.00 USD | `750.00` | `2350.92` | `2243.00` | `2842.54` | 39,396.61 USD | `+2.29%` | `25X Cross` |
| `1326` | `0xf910...0a2d` | `SHORT` | 1,691,402.59 USD | `748.34` | `2262.51` | `2243.00` | `10477.05` | 1,732.99 USD | `+0.10%` | `5X Cross` |
| `1344` | `0x51a0...3543` | `SHORT` | 1,665,585.89 USD | `724.55` | `2627.71` | `2243.00` | `7570.18` | 238,310.87 USD | `+14.31%` | `20X Cross` |
| `1352` | `0xaa53...9cb7` | `LONG` | 1,659,023.96 USD | `721.82` | `2391.31` | `2243.00` | `1924.04` | -67,069.71 USD | `-4.04%` | `20X Cross` |
| `1355` | `0x3ee5...4fab` | `SHORT` | 1,655,897.44 USD | `715.17` | `2759.35` | `2243.00` | `3262.99` | 317,502.53 USD | `+19.17%` | `20X Cross` |
| `1361` | `0x621c...63ab` | `LONG` | 1,649,992.30 USD | `728.28` | `2281.90` | `2243.00` | `0.000000` | -11,878.00 USD | `-0.72%` | `20X Cross` |
| `1374` | `0x4b1c...bc38` | `SHORT` | 1,633,213.15 USD | `714.35` | `2529.31` | `2243.00` | `4495.13` | 173,599.11 USD | `+10.63%` | `10X Cross` |
| `1377` | `0xa189...94d7` | `SHORT` | 1,627,800.52 USD | `719.98` | `2691.84` | `2243.00` | `3051.96` | 310,272.14 USD | `+19.06%` | `25X Cross` |
| `1380` | `0x5605...fe0f` | `SHORT` | 1,625,813.51 USD | `702.14` | `2566.90` | `2243.00` | `3072.22` | 176,519.14 USD | `+10.86%` | `20X Cross` |
| `1394` | `0x7743...e4fe` | `SHORT` | 1,610,999.04 USD | `700.56` | `2326.87` | `2243.00` | `6154.41` | 19,111.10 USD | `+1.19%` | `25X Cross` |
| `1400` | `0xaa7a...af37` | `LONG` | 1,607,118.44 USD | `712.63` | `2279.53` | `2243.00` | `0.000000` | -17,341.90 USD | `-1.08%` | `20X Cross` |
| `1413` | `0x2f93...4404` | `LONG` | 1,598,178.12 USD | `707.47` | `1700.45` | `2243.00` | `1369.64` | 395,151.74 USD | `+24.73%` | `4X Isolated` |
| `1444` | `0x07fd...082a` | `LONG` | 1,563,436.54 USD | `680.45` | `2308.98` | `2243.00` | `1968.63` | -7,705.84 USD | `-0.49%` | `25X Cross` |
| `1445` | `0x31de...13f2` | `LONG` | 1,562,577.02 USD | `690.76` | `2302.23` | `2243.00` | `0.000000` | -27,726.71 USD | `-1.77%` | `20X Cross` |
| `1451` | `0x0b23...f37b` | `LONG` | 1,560,795.75 USD | `675.00` | `2238.15` | `2243.00` | `588.25` | 50,039.11 USD | `+3.21%` | `5X Cross` |
| `1455` | `0x71e5...be04` | `LONG` | 1,557,346.07 USD | `677.67` | `2727.27` | `2243.00` | `1471.79` | -290,839.53 USD | `-18.68%` | `20X Cross` |
| `1472` | `0xdbd1...29dd` | `SHORT` | 1,539,885.20 USD | `680.70` | `3030.57` | `2243.00` | `4142.95` | 523,035.93 USD | `+33.97%` | `6X Cross` |
| `1489` | `0x0082...1ae3` | `LONG` | 1,515,030.00 USD | `660.00` | `2448.58` | `2243.00` | `2244.99` | -101,038.64 USD | `-6.67%` | `25X Cross` |
| `1490` | `0x8923...1bac` | `SHORT` | 1,514,868.03 USD | `660.02` | `2339.81` | `2243.00` | `2919.62` | 29,448.78 USD | `+1.94%` | `25X Cross` |
| `1500` | `0xb7bd...2f3a` | `LONG` | 1,502,549.71 USD | `667.44` | `2267.95` | `2243.00` | `1037.76` | -11,180.89 USD | `-0.74%` | `20X Cross` |
| `1513` | `0x0cac...6170` | `SHORT` | 1,488,711.50 USD | `657.50` | `2146.55` | `2243.00` | `2840.20` | -77,349.30 USD | `-5.20%` | `20X Cross` |
| `1519` | `0xffb2...5ed6` | `SHORT` | 1,481,638.66 USD | `640.77` | `2672.96` | `2243.00` | `2546.12` | 231,109.68 USD | `+15.60%` | `20X Cross` |
| `1526` | `0x9599...c60a` | `LONG` | 1,466,743.17 USD | `648.63` | `2296.80` | `2243.00` | `0.000000` | -23,029.19 USD | `-1.57%` | `20X Cross` |
| `1541` | `0xfce0...f4c0` | `SHORT` | 1,444,257.60 USD | `623.60` | `3129.61` | `2243.00` | `2788.45` | 507,368.98 USD | `+35.13%` | `20X Cross` |
| `1590` | `0x7663...cb5a` | `SHORT` | 1,391,012.90 USD | `613.54` | `2342.35` | `2243.00` | `3754.39` | 46,107.59 USD | `+3.31%` | `3X Cross` |
| `1592` | `0x67c3...609d` | `SHORT` | 1,389,240.00 USD | `600.00` | `2386.55` | `2243.00` | `2560.80` | 42,691.89 USD | `+3.07%` | `25X Cross` |
| `1603` | `0x0deb...0bc5` | `LONG` | 1,378,860.00 USD | `600.00` | `2038.23` | `2243.00` | `1478.72` | 155,921.36 USD | `+11.31%` | `20X Cross` |
| `1604` | `0x0a84...6ddd` | `LONG` | 1,378,860.00 USD | `600.00` | `2222.36` | `2243.00` | `1774.83` | 45,441.66 USD | `+3.30%` | `25X Cross` |
| `1605` | `0xad02...eb65` | `LONG` | 1,377,882.80 USD | `600.62` | `2460.69` | `2243.00` | `1079.70` | -100,057.76 USD | `-7.26%` | `5X Cross` |
| `1606` | `0x26e6...6b28` | `LONG` | 1,377,300.00 USD | `600.00` | `1769.78` | `2243.00` | `2005.51` | 315,428.47 USD | `+22.90%` | `20X Cross` |
| `1621` | `0x638f...f5f0` | `LONG` | 1,357,260.00 USD | `600.00` | `4011.50` | `2243.00` | `347.05` | -1,049,643.53 USD | `-77.34%` | `25X Cross` |
| `1642` | `0x94b6...e5b3` | `SHORT` | 1,328,428.78 USD | `586.71` | `2377.90` | `2243.00` | `2408.69` | 66,709.46 USD | `+5.02%` | `25X Cross` |
| `1657` | `0xfb99...37f3` | `LONG` | 1,310,856.41 USD | `565.34` | `2362.35` | `2243.00` | `1213.80` | -24,679.95 USD | `-1.88%` | `3X Cross` |
| `1663` | `0x72d0...62ea` | `SHORT` | 1,304,771.90 USD | `577.33` | `2260.06` | `2243.00` | `4397.34` | 36.52 USD | `+0.00%` | `5X Cross` |
| `1676` | `0x844b...7f42` | `SHORT` | 1,297,144.20 USD | `561.00` | `2026.17` | `2243.00` | `3089.67` | -160,460.79 USD | `-12.37%` | `25X Cross` |
| `1699` | `0xabe6...1d99` | `SHORT` | 1,276,140.38 USD | `556.00` | `2484.68` | `2243.00` | `3034.27` | 105,355.51 USD | `+8.26%` | `20X Cross` |
| `1755` | `0xc10f...23b3` | `LONG` | 1,216,138.00 USD | `530.00` | `2394.36` | `2243.00` | `2102.04` | -52,874.66 USD | `-4.35%` | `25X Cross` |
| `1772` | `0xad21...fb6a` | `LONG` | 1,199,471.65 USD | `531.87` | `2574.89` | `2243.00` | `1704.24` | -170,033.85 USD | `-14.18%` | `7X Cross` |
| `1804` | `0x0c7a...2f50` | `SHORT` | 1,170,449.40 USD | `509.25` | `2122.56` | `2243.00` | `4090.66` | -89,543.97 USD | `-7.65%` | `20X Cross` |
| `1828` | `0x7298...7d6c` | `SHORT` | 1,151,970.26 USD | `498.15` | `3426.75` | `2243.00` | `5422.42` | 555,065.57 USD | `+48.18%` | `20X Cross` |
| `1844` | `0x89b2...9ca6` | `LONG` | 1,130,460.00 USD | `500.00` | `2484.03` | `2243.00` | `1954.23` | -111,559.35 USD | `-9.87%` | `25X Cross` |
| `1845` | `0x6463...42f5` | `LONG` | 1,128,900.00 USD | `500.00` | `2256.58` | `2243.00` | `0.000000` | 605.08 USD | `+0.05%` | `5X Cross` |
| `1846` | `0x321f...1c84` | `SHORT` | 1,128,389.21 USD | `488.02` | `2370.09` | `2243.00` | `3022.61` | 28,255.39 USD | `+2.50%` | `10X Cross` |
| `1847` | `0xbc76...417c` | `LONG` | 1,128,253.48 USD | `499.45` | `2254.73` | `2243.00` | `1689.45` | 2,129.04 USD | `+0.19%` | `25X Cross` |
| `1879` | `0x404c...5f03` | `SHORT` | 1,107,992.31 USD | `489.79` | `2671.94` | `2243.00` | `5002.44` | 200,687.25 USD | `+18.11%` | `20X Cross` |
| `1893` | `0x9c68...7783` | `SHORT` | 1,094,257.81 USD | `485.39` | `2262.21` | `2243.00` | `3892.64` | 3,793.26 USD | `+0.35%` | `25X Cross` |
| `1932` | `0x82c6...fe42` | `LONG` | 1,061,622.50 USD | `462.50` | `2501.38` | `2243.00` | `2054.49` | -95,268.07 USD | `-8.97%` | `5X Isolated` |
| `1944` | `0x617e...0f97` | `SHORT` | 1,052,332.55 USD | `457.85` | `2205.60` | `2243.00` | `3751.06` | -42,488.72 USD | `-4.04%` | `10X Cross` |
| `1965` | `0x53f8...ceff` | `LONG` | 1,031,246.29 USD | `445.60` | `2399.81` | `2243.00` | `0.000000` | -38,104.31 USD | `-3.69%` | `20X Cross` |
| `1970` | `0x60f7...d1ee` | `LONG` | 1,029,927.94 USD | `455.68` | `2343.49` | `2243.00` | `2231.54` | -37,955.56 USD | `-3.69%` | `25X Cross` |
| `1988` | `0xae55...2236` | `LONG` | 1,017,090.00 USD | `450.00` | `2510.21` | `2243.00` | `0.000000` | -112,507.50 USD | `-11.06%` | `25X Cross` |
| `1996` | `0x248e...6be2` | `SHORT` | 1,010,737.01 USD | `436.40` | `2314.49` | `2243.00` | `4423.77` | -702.29 USD | `-0.07%` | `20X Cross` |
| `2000` | `0xac26...a9c7` | `SHORT` | 1,009,522.98 USD | `446.28` | `2192.58` | `2243.00` | `8484.50` | -31,023.28 USD | `-3.07%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `ANNOUNCEMENT` | `INFO` | `2517.10` | 24,790.92 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 24.79K USD at 2517.1000 USD [API] | `2026-10-08 13:40:14` |
| `ANNOUNCEMENT` | `INFO` | `2517.10` | 328.98 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.33K USD at 2517.1000 USD [API] | `2026-10-08 13:40:14` |
| `ANNOUNCEMENT` | `INFO` | `2358.70` | 40,060.63 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 40.06K USD at 2358.7000 USD [API] | `2026-10-28 02:49:29` |
| `ANNOUNCEMENT` | `INFO` | `2358.30` | 40,591.06 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 40.59K USD at 2358.3000 USD [API] | `2026-10-28 02:58:44` |
| `ANNOUNCEMENT` | `INFO` | `2363.90` | 49,342.16 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 49.34K USD at 2363.9000 USD [API] | `2026-10-28 03:50:11` |
| `ANNOUNCEMENT` | `INFO` | `2362.10` | 54,053.59 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 54.05K USD at 2362.1000 USD [API] | `2026-10-28 03:54:16` |
| `ANNOUNCEMENT` | `INFO` | `2362.10` | 40,060.27 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 40.06K USD at 2362.1000 USD [API] | `2026-10-28 03:54:16` |
| `ANNOUNCEMENT` | `INFO` | `2362.10` | 95,323.96 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 95.32K USD at 2362.1000 USD [API] | `2026-10-28 03:54:16` |
| `ANNOUNCEMENT` | `INFO` | `2355.00` | 95,995.45 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 96.00K USD at 2355.0000 USD [API] | `2026-10-28 04:11:37` |
| `ANNOUNCEMENT` | `INFO` | `2368.70` | 851.55 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.85K USD at 2368.7000 USD [API] | `2026-10-25 02:38:02` |
| `ANNOUNCEMENT` | `INFO` | `2368.70` | 916.21 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.92K USD at 2368.7000 USD [API] | `2026-10-25 02:38:02` |
| `ANNOUNCEMENT` | `INFO` | `2333.60` | 1,022.82 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.02K USD at 2333.6000 USD [API] | `2026-10-24 18:29:59` |
| `ANNOUNCEMENT` | `INFO` | `2333.60` | 1,211.37 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.21K USD at 2333.6000 USD [API] | `2026-10-24 18:29:59` |
| `ANNOUNCEMENT` | `INFO` | `2360.40` | 59,588.77 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 59.59K USD at 2360.4000 USD [API] | `2026-10-23 22:53:38` |
| `ANNOUNCEMENT` | `INFO` | `2368.10` | 88.33 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.09K USD at 2368.1000 USD [API] | `2026-10-23 22:48:54` |
| `ANNOUNCEMENT` | `INFO` | `2368.10` | 700.25 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.70K USD at 2368.1000 USD [API] | `2026-10-23 22:48:54` |
| `ANNOUNCEMENT` | `INFO` | `2368.10` | 1,170.79 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.17K USD at 2368.1000 USD [API] | `2026-10-23 22:48:54` |
| `ANNOUNCEMENT` | `INFO` | `2368.10` | 1,856.12 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.86K USD at 2368.1000 USD [API] | `2026-10-23 22:48:54` |
| `ANNOUNCEMENT` | `INFO` | `2368.10` | 518.14 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.52K USD at 2368.1000 USD [API] | `2026-10-23 22:48:54` |
| `ANNOUNCEMENT` | `INFO` | `2402.20` | 7,572.46 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 7.57K USD at 2402.2000 USD [API] | `2026-10-22 09:03:55` |
| `ANNOUNCEMENT` | `INFO` | `2402.20` | 613.76 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.61K USD at 2402.2000 USD [API] | `2026-10-22 09:03:55` |
| `ANNOUNCEMENT` | `INFO` | `2403.00` | 698.55 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.70K USD at 2403.0000 USD [API] | `2026-10-22 09:03:52` |
| `ANNOUNCEMENT` | `INFO` | `2357.80` | 299,004.41 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 299.00K USD at 2357.8000 USD [API] | `2026-10-28 04:33:41` |
| `ANNOUNCEMENT` | `INFO` | `2357.80` | 75,685.38 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 75.69K USD at 2357.8000 USD [API] | `2026-10-28 04:33:41` |
| `ANNOUNCEMENT` | `INFO` | `2357.80` | 401,086.30 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 401.09K USD at 2357.8000 USD [API] | `2026-10-28 04:33:41` |
| `ANNOUNCEMENT` | `INFO` | `2356.90` | 40,997.80 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 41.00K USD at 2356.9000 USD [API] | `2026-10-28 04:38:32` |
| `ANNOUNCEMENT` | `INFO` | `2412.30` | 18,405.85 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 18.41K USD at 2412.3000 USD [API] | `2026-10-18 23:27:51` |
| `ANNOUNCEMENT` | `INFO` | `2461.00` | 8,952.63 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 8.95K USD at 2461.0000 USD [API] | `2026-10-12 23:02:14` |
| `ANNOUNCEMENT` | `INFO` | `2461.00` | 2,202.60 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 2.20K USD at 2461.0000 USD [API] | `2026-10-12 23:02:14` |
| `ANNOUNCEMENT` | `INFO` | `2461.00` | 864.80 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.86K USD at 2461.0000 USD [API] | `2026-10-12 23:02:14` |
| `ANNOUNCEMENT` | `INFO` | `2461.00` | 1,940.50 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.94K USD at 2461.0000 USD [API] | `2026-10-12 23:02:14` |
| `ANNOUNCEMENT` | `INFO` | `2461.00` | 257.42 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.26K USD at 2461.0000 USD [API] | `2026-10-12 23:02:14` |
| `ANNOUNCEMENT` | `INFO` | `2461.00` | 121.82 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.12K USD at 2461.0000 USD [API] | `2026-10-12 23:02:14` |
| `ANNOUNCEMENT` | `INFO` | `2461.00` | 603.68 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.60K USD at 2461.0000 USD [API] | `2026-10-12 23:02:14` |
| `ANNOUNCEMENT` | `INFO` | `2461.00` | 22.40 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.02K USD at 2461.0000 USD [API] | `2026-10-12 23:02:14` |
| `ANNOUNCEMENT` | `INFO` | `2461.10` | 7,183.46 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 7.18K USD at 2461.1000 USD [API] | `2026-10-12 23:02:14` |
| `ANNOUNCEMENT` | `INFO` | `2479.30` | 27,091.81 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 27.09K USD at 2479.3000 USD [API] | `2026-10-08 15:20:45` |
| `ANNOUNCEMENT` | `INFO` | `2355.90` | 40,059.72 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 40.06K USD at 2355.9000 USD [API] | `2026-10-28 04:50:04` |


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
| `Live` | `Long Liquidation` | `455.00` | 81,350.00 USD | 871,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `7D` | `Long Liquidation` | `2057.30` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2060.30` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 975,520.00 USD | 1,310,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2062.80` | 682,320,000.00 USD | 682,320,000.00 USD | 80,610.00 USD | 121,470.00 USD | 88,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2063.30` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 1,770,000.00 USD | 826,260.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2065.00` | 1,360,000.00 USD | 330,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2065.50` | 682,030,000.00 USD | 682,030,000.00 USD | 984,680.00 USD | 494,150.00 USD | 562,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2066.30` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 406,250.00 USD | 1,270,000.00 USD | 1,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2068.20` | 679,990,000.00 USD | 679,990,000.00 USD | 333,430.00 USD | 1,010,000.00 USD | 50,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2069.30` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 1,580,000.00 USD | 2,090,000.00 USD | 781,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2070.90` | 678,600,000.00 USD | 678,600,000.00 USD | 1,040,000.00 USD | 0.00 USD | 437,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2072.30` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 4,410,000.00 USD | 2,160,000.00 USD | 2,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2073.60` | 677,110,000.00 USD | 677,110,000.00 USD | 419,970.00 USD | 62,630.00 USD | 926,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 921,260.00 USD | 329,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2075.30` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 4,120,000.00 USD | 3,560,000.00 USD | 4,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2076.30` | 675,710,000.00 USD | 675,710,000.00 USD | 2,580,000.00 USD | 926,330.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2078.30` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 4,150,000.00 USD | 3,500,000.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2079.00` | 670,580,000.00 USD | 670,580,000.00 USD | 1,320,000.00 USD | 1,100,000.00 USD | 816,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2081.30` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 4,720,000.00 USD | 2,960,000.00 USD | 2,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2081.70` | 667,330,000.00 USD | 667,330,000.00 USD | 1,430,000.00 USD | 1,260,000.00 USD | 227,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2084.30` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 3,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2084.40` | 664,420,000.00 USD | 664,420,000.00 USD | 2,110,000.00 USD | 1,490,000.00 USD | 753,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 2,640,000.00 USD | 328,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2087.10` | 660,070,000.00 USD | 660,070,000.00 USD | 1,990,000.00 USD | 1,460,000.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2087.30` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 2,990,000.00 USD | 2,750,000.00 USD | 3,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2089.80` | 655,030,000.00 USD | 655,030,000.00 USD | 929,970.00 USD | 225,710.00 USD | 307,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2090.30` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 4,840,000.00 USD | 976,840.00 USD | 5,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2092.50` | 653,560,000.00 USD | 653,560,000.00 USD | 966,030.00 USD | 518,530.00 USD | 876,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2093.30` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 4,420,000.00 USD | 1,200,000.00 USD | 4,890,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 1,420,000.00 USD | 325,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2095.20` | 651,200,000.00 USD | 651,200,000.00 USD | 2,100,000.00 USD | 1,310,000.00 USD | 1,760,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2096.30` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 3,150,000.00 USD | 2,430,000.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2097.90` | 646,030,000.00 USD | 646,030,000.00 USD | 474,990.00 USD | 1,170,000.00 USD | 517,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2099.30` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 1,460,000.00 USD | 2,870,000.00 USD | 2,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2100.60` | 643,860,000.00 USD | 643,860,000.00 USD | 160,570.00 USD | 44,780.00 USD | 175,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2102.30` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 678,000.00 USD | 739,480.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2103.30` | 643,480,000.00 USD | 643,480,000.00 USD | 634,340.00 USD | 289,160.00 USD | 306,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 1,220,000.00 USD | 324,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2105.30` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2106.00` | 642,250,000.00 USD | 642,250,000.00 USD | 568,860.00 USD | 671,930.00 USD | 515,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2108.30` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 2,400,000.00 USD | 1,090,000.00 USD | 1,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2108.70` | 640,500,000.00 USD | 640,500,000.00 USD | 580,900.00 USD | 21,400.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2111.30` | 2,090,000,000.00 USD | 2,090,000,000.00 USD | 3,450,000.00 USD | 1,630,000.00 USD | 1,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2111.40` | 639,890,000.00 USD | 639,890,000.00 USD | 490,860.00 USD | 146,050.00 USD | 193,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2114.10` | 639,060,000.00 USD | 639,060,000.00 USD | 420,950.00 USD | 507,320.00 USD | 398,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2114.30` | 2,080,000,000.00 USD | 2,080,000,000.00 USD | 1,080,000.00 USD | 1,830,000.00 USD | 3,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 20,470,000.00 USD | 323,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2116.80` | 637,730,000.00 USD | 637,730,000.00 USD | 679,710.00 USD | 13,230.00 USD | 692,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2117.30` | 2,080,000,000.00 USD | 2,080,000,000.00 USD | 2,410,000.00 USD | 2,020,000.00 USD | 2,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2119.50` | 636,340,000.00 USD | 636,340,000.00 USD | 15,360.00 USD | 256,720.00 USD | 904,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2120.30` | 2,070,000,000.00 USD | 2,070,000,000.00 USD | 3,660,000.00 USD | 771,920.00 USD | 1,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2122.20` | 635,170,000.00 USD | 635,170,000.00 USD | 926,060.00 USD | 689,080.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2123.30` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 1,470,000.00 USD | 1,140,000.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2124.90` | 632,370,000.00 USD | 632,370,000.00 USD | 1,010,000.00 USD | 1,130,000.00 USD | 769,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 1,030,000.00 USD | 302,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2126.30` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 2,280,000.00 USD | 2,560,000.00 USD | 3,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2127.60` | 629,460,000.00 USD | 629,460,000.00 USD | 365,910.00 USD | 1,040,000.00 USD | 301,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2129.30` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 1,410,000.00 USD | 1,270,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2130.30` | 627,760,000.00 USD | 627,760,000.00 USD | 0.00 USD | 18,610.00 USD | 654,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2132.30` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 2,610,000.00 USD | 1,560,000.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2133.00` | 627,080,000.00 USD | 627,080,000.00 USD | 0.00 USD | 937,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 3,440,000.00 USD | 301,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2135.30` | 2,040,000,000.00 USD | 2,040,000,000.00 USD | 1,440,000.00 USD | 744,540.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2135.70` | 626,150,000.00 USD | 626,150,000.00 USD | 0.00 USD | 27,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2138.30` | 2,040,000,000.00 USD | 2,040,000,000.00 USD | 1,290,000.00 USD | 660,600.00 USD | 78,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2138.40` | 626,120,000.00 USD | 626,120,000.00 USD | 0.00 USD | 251,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2141.30` | 2,040,000,000.00 USD | 2,040,000,000.00 USD | 1,750,000.00 USD | 1,130,000.00 USD | 766,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2144.30` | 2,030,000,000.00 USD | 2,030,000,000.00 USD | 465,960.00 USD | 1,540,000.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 9,300,000.00 USD | 298,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2147.30` | 2,030,000,000.00 USD | 2,030,000,000.00 USD | 239,110.00 USD | 10,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2150.30` | 2,030,000,000.00 USD | 2,030,000,000.00 USD | 459,630.00 USD | 463,640.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2153.30` | 2,030,000,000.00 USD | 2,030,000,000.00 USD | 109,800.00 USD | 331,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 23,380,000.00 USD | 288,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2156.30` | 2,030,000,000.00 USD | 2,030,000,000.00 USD | 406,850.00 USD | 1,030,000.00 USD | 305,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2159.30` | 2,030,000,000.00 USD | 2,030,000,000.00 USD | 345,270.00 USD | 863,480.00 USD | 2,280,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2162.30` | 2,020,000,000.00 USD | 2,020,000,000.00 USD | 867,790.00 USD | 598,340.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 904,350.00 USD | 265,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2165.30` | 2,020,000,000.00 USD | 2,020,000,000.00 USD | 25,540.00 USD | 329,690.00 USD | 402,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2168.30` | 2,020,000,000.00 USD | 2,020,000,000.00 USD | 1,210,000.00 USD | 373,180.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2171.30` | 2,020,000,000.00 USD | 2,020,000,000.00 USD | 438,050.00 USD | 765,150.00 USD | 794,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2174.30` | 2,020,000,000.00 USD | 2,020,000,000.00 USD | 479,540.00 USD | 363,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 109,710,000.00 USD | 264,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2185.00` | 112,420,000.00 USD | 154,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2195.00` | 909,930.00 USD | 42,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2195.30` | 2,020,000,000.00 USD | 2,020,000,000.00 USD | 141,070.00 USD | 474,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2198.30` | 2,020,000,000.00 USD | 2,020,000,000.00 USD | 2,720,000.00 USD | 2,800,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2200.50` | 625,870,000.00 USD | 625,870,000.00 USD | 284,470.00 USD | 433,420.00 USD | 276,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2201.30` | 2,010,000,000.00 USD | 2,010,000,000.00 USD | 5,520,000.00 USD | 3,360,000.00 USD | 5,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2203.20` | 624,870,000.00 USD | 624,870,000.00 USD | 2,510,000.00 USD | 1,170,000.00 USD | 1,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2204.30` | 2,000,000,000.00 USD | 2,000,000,000.00 USD | 1,910,000.00 USD | 3,010,000.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 1,470,000.00 USD | 41,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2205.90` | 619,220,000.00 USD | 619,220,000.00 USD | 1,450,000.00 USD | 3,240,000.00 USD | 781,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2207.30` | 1,990,000,000.00 USD | 1,990,000,000.00 USD | 7,040,000.00 USD | 7,160,000.00 USD | 3,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2208.60` | 613,750,000.00 USD | 613,750,000.00 USD | 2,490,000.00 USD | 101,520.00 USD | 3,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2210.30` | 1,970,000,000.00 USD | 1,970,000,000.00 USD | 13,680,000.00 USD | 7,280,000.00 USD | 6,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2211.30` | 608,110,000.00 USD | 608,110,000.00 USD | 2,890,000.00 USD | 1,870,000.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2213.30` | 1,940,000,000.00 USD | 1,940,000,000.00 USD | 8,860,000.00 USD | 9,440,000.00 USD | 13,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2214.00` | 601,730,000.00 USD | 601,730,000.00 USD | 6,250,000.00 USD | 3,800,000.00 USD | 5,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 1,830,000.00 USD | 39,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2216.30` | 1,910,000,000.00 USD | 1,910,000,000.00 USD | 19,200,000.00 USD | 12,720,000.00 USD | 6,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2216.70` | 586,430,000.00 USD | 586,430,000.00 USD | 5,840,000.00 USD | 5,850,000.00 USD | 2,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2219.30` | 1,870,000,000.00 USD | 1,870,000,000.00 USD | 16,080,000.00 USD | 12,970,000.00 USD | 9,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2219.40` | 571,970,000.00 USD | 571,970,000.00 USD | 4,640,000.00 USD | 4,380,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2222.10` | 561,850,000.00 USD | 561,850,000.00 USD | 6,000,000.00 USD | 3,530,000.00 USD | 2,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2222.30` | 1,840,000,000.00 USD | 1,840,000,000.00 USD | 7,180,000.00 USD | 6,030,000.00 USD | 8,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2224.80` | 549,460,000.00 USD | 549,460,000.00 USD | 4,770,000.00 USD | 4,280,000.00 USD | 4,840,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2225.00` | 1,590,000.00 USD | 38,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2225.30` | 1,810,000,000.00 USD | 1,810,000,000.00 USD | 15,150,000.00 USD | 14,490,000.00 USD | 11,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2227.50` | 535,570,000.00 USD | 535,570,000.00 USD | 5,760,000.00 USD | 3,110,000.00 USD | 1,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2228.30` | 1,770,000,000.00 USD | 1,770,000,000.00 USD | 8,280,000.00 USD | 5,190,000.00 USD | 7,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2230.20` | 525,240,000.00 USD | 525,240,000.00 USD | 3,710,000.00 USD | 2,180,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2231.30` | 1,750,000,000.00 USD | 1,750,000,000.00 USD | 11,350,000.00 USD | 3,450,000.00 USD | 18,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2232.90` | 517,390,000.00 USD | 517,390,000.00 USD | 5,100,000.00 USD | 2,460,000.00 USD | 3,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2234.30` | 1,720,000,000.00 USD | 1,720,000,000.00 USD | 17,500,000.00 USD | 12,130,000.00 USD | 7,560,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2235.00` | 1,290,000.00 USD | 36,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2235.60` | 505,930,000.00 USD | 505,930,000.00 USD | 5,540,000.00 USD | 4,910,000.00 USD | 5,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2237.30` | 1,680,000,000.00 USD | 1,680,000,000.00 USD | 6,520,000.00 USD | 11,210,000.00 USD | 4,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2238.30` | 489,850,000.00 USD | 489,850,000.00 USD | 1,880,000.00 USD | 2,700,000.00 USD | 844,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2240.30` | 1,660,000,000.00 USD | 1,660,000,000.00 USD | 8,440,000.00 USD | 6,650,000.00 USD | 9,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2241.00` | 484,420,000.00 USD | 484,420,000.00 USD | 634,700.00 USD | 542,280.00 USD | 601,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2243.30` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 7,400,000.00 USD | 9,450,000.00 USD | 8,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2243.70` | 482,640,000.00 USD | 482,640,000.00 USD | 1,640,000.00 USD | 1,310,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2245.00` | 4,640,000.00 USD | 35,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2246.30` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 13,980,000.00 USD | 9,520,000.00 USD | 10,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2246.40` | 478,460,000.00 USD | 478,460,000.00 USD | 2,780,000.00 USD | 3,030,000.00 USD | 2,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2249.10` | 470,640,000.00 USD | 470,640,000.00 USD | 7,320,000.00 USD | 2,840,000.00 USD | 4,280,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2249.30` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 14,130,000.00 USD | 8,010,000.00 USD | 9,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2251.80` | 456,200,000.00 USD | 456,200,000.00 USD | 4,400,000.00 USD | 7,100,000.00 USD | 2,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2252.30` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 27,030,000.00 USD | 23,830,000.00 USD | 15,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2254.50` | 442,650,000.00 USD | 442,650,000.00 USD | 6,130,000.00 USD | 2,230,000.00 USD | 6,870,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2255.00` | 10,910,000.00 USD | 30,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2255.30` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 25,980,000.00 USD | 16,790,000.00 USD | 18,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2257.20` | 427,430,000.00 USD | 427,430,000.00 USD | 4,890,000.00 USD | 4,320,000.00 USD | 4,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2258.30` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 26,340,000.00 USD | 24,750,000.00 USD | 27,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2259.90` | 413,520,000.00 USD | 413,520,000.00 USD | 13,480,000.00 USD | 6,500,000.00 USD | 8,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2261.30` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 45,180,000.00 USD | 27,760,000.00 USD | 25,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2262.60` | 384,730,000.00 USD | 384,730,000.00 USD | 14,960,000.00 USD | 15,790,000.00 USD | 13,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2264.30` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 39,820,000.00 USD | 32,460,000.00 USD | 24,120,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2265.00` | 3,260,000.00 USD | 19,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2265.30` | 340,100,000.00 USD | 340,100,000.00 USD | 15,940,000.00 USD | 11,630,000.00 USD | 5,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2267.30` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 45,000,000.00 USD | 33,340,000.00 USD | 27,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2268.00` | 307,110,000.00 USD | 307,110,000.00 USD | 12,020,000.00 USD | 9,560,000.00 USD | 5,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2270.30` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 44,170,000.00 USD | 37,480,000.00 USD | 47,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2270.70` | 280,430,000.00 USD | 280,430,000.00 USD | 20,010,000.00 USD | 15,460,000.00 USD | 17,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2273.30` | 907,030,000.00 USD | 907,030,000.00 USD | 33,900,000.00 USD | 35,430,000.00 USD | 20,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2273.40` | 227,040,000.00 USD | 227,040,000.00 USD | 17,480,000.00 USD | 13,060,000.00 USD | 8,920,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2275.00` | 6,850,000.00 USD | 16,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2276.10` | 187,570,000.00 USD | 187,570,000.00 USD | 17,930,000.00 USD | 14,350,000.00 USD | 10,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2276.30` | 817,480,000.00 USD | 817,480,000.00 USD | 58,660,000.00 USD | 46,730,000.00 USD | 59,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2278.80` | 144,320,000.00 USD | 144,320,000.00 USD | 19,120,000.00 USD | 9,120,000.00 USD | 16,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2279.30` | 652,630,000.00 USD | 652,630,000.00 USD | 84,810,000.00 USD | 43,190,000.00 USD | 43,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2281.50` | 100,030,000.00 USD | 100,030,000.00 USD | 19,770,000.00 USD | 13,730,000.00 USD | 21,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2282.30` | 480,920,000.00 USD | 480,920,000.00 USD | 57,660,000.00 USD | 66,030,000.00 USD | 62,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2284.20` | 44,630,000.00 USD | 44,630,000.00 USD | 22,710,000.00 USD | 14,080,000.00 USD | 7,770,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2285.00` | 4,100,000.00 USD | 9,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2285.30` | 294,700,000.00 USD | 294,700,000.00 USD | 83,870,000.00 USD | 19,620,000.00 USD | 32,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2288.30` | 158,380,000.00 USD | 158,380,000.00 USD | 61,070,000.00 USD | 0.00 USD | 11,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2291.30` | 85,850,000.00 USD | 85,850,000.00 USD | 49,180,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2294.30` | 36,670,000.00 USD | 36,670,000.00 USD | 30,090,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2295.00` | 3,310,000.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2297.30` | 6,580,000.00 USD | 6,580,000.00 USD | 6,580,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2297.70` | 70,480.00 USD | 70,480.00 USD | 0.00 USD | 32,370.00 USD | 38,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2300.30` | 9,500,000.00 USD | 9,500,000.00 USD | 9,500,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2300.40` | 208,270.00 USD | 208,270.00 USD | 0.00 USD | 18,850.00 USD | 189,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2303.10` | 8,650,000.00 USD | 8,650,000.00 USD | 8,350,000.00 USD | 0.00 USD | 95,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2303.30` | 21,650,000.00 USD | 21,650,000.00 USD | 12,090,000.00 USD | 0.00 USD | 63,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2305.00` | 940,780.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2305.80` | 13,040,000.00 USD | 13,040,000.00 USD | 0.00 USD | 4,390,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2306.30` | 25,530,000.00 USD | 25,530,000.00 USD | 0.00 USD | 3,740,000.00 USD | 134,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2308.50` | 15,000,000.00 USD | 15,000,000.00 USD | 0.00 USD | 1,960,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2309.30` | 25,630,000.00 USD | 25,630,000.00 USD | 0.00 USD | 0.00 USD | 97,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2312.30` | 25,700,000.00 USD | 25,700,000.00 USD | 0.00 USD | 0.00 USD | 70,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2313.90` | 19,950,000.00 USD | 19,950,000.00 USD | 0.00 USD | 4,750,000.00 USD | 203,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2315.00` | 932,620.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2315.30` | 33,270,000.00 USD | 33,270,000.00 USD | 0.00 USD | 7,460,000.00 USD | 117,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2316.60` | 47,570,000.00 USD | 47,570,000.00 USD | 5,840,000.00 USD | 16,670,000.00 USD | 5,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2318.30` | 38,230,000.00 USD | 38,230,000.00 USD | 992,100.00 USD | 3,800,000.00 USD | 170,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2319.30` | 56,130,000.00 USD | 56,130,000.00 USD | 3,330,000.00 USD | 5,160,000.00 USD | 61,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2321.30` | 51,050,000.00 USD | 51,050,000.00 USD | 0.00 USD | 12,820,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2322.00` | 58,740,000.00 USD | 58,740,000.00 USD | 0.00 USD | 2,610,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2324.30` | 55,910,000.00 USD | 55,910,000.00 USD | 3,130,000.00 USD | 1,740,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2324.70` | 61,960,000.00 USD | 61,960,000.00 USD | 479,120.00 USD | 2,700,000.00 USD | 48,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2325.00` | 321,320.00 USD | 329,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2327.30` | 69,660,000.00 USD | 69,660,000.00 USD | 4,980,000.00 USD | 805,740.00 USD | 7,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2327.40` | 66,640,000.00 USD | 66,640,000.00 USD | 256,580.00 USD | 206,450.00 USD | 4,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2330.10` | 75,630,000.00 USD | 75,630,000.00 USD | 8,530,000.00 USD | 251,940.00 USD | 203,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2330.30` | 79,030,000.00 USD | 79,030,000.00 USD | 9,370,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2332.80` | 93,750,000.00 USD | 93,750,000.00 USD | 13,380,000.00 USD | 1,260,000.00 USD | 3,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2333.30` | 113,140,000.00 USD | 113,140,000.00 USD | 26,700,000.00 USD | 7,400,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2335.00` | 7,680.00 USD | 7,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2335.50` | 111,690,000.00 USD | 111,690,000.00 USD | 15,450,000.00 USD | 405,770.00 USD | 2,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2336.30` | 152,830,000.00 USD | 152,830,000.00 USD | 22,160,000.00 USD | 11,020,000.00 USD | 6,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2338.20` | 122,510,000.00 USD | 122,510,000.00 USD | 6,030,000.00 USD | 688,030.00 USD | 4,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2339.30` | 171,900,000.00 USD | 171,900,000.00 USD | 10,060,000.00 USD | 616,960.00 USD | 8,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2340.90` | 142,250,000.00 USD | 142,250,000.00 USD | 7,730,000.00 USD | 2,210,000.00 USD | 9,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2342.30` | 210,090,000.00 USD | 210,090,000.00 USD | 4,200,000.00 USD | 20,070,000.00 USD | 13,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2343.60` | 152,770,000.00 USD | 152,770,000.00 USD | 1,790,000.00 USD | 3,480,000.00 USD | 5,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2345.30` | 225,300,000.00 USD | 225,300,000.00 USD | 1,350,000.00 USD | 7,920,000.00 USD | 5,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2346.30` | 162,030,000.00 USD | 162,030,000.00 USD | 3,350,000.00 USD | 0.00 USD | 5,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2348.30` | 256,890,000.00 USD | 256,890,000.00 USD | 847,620.00 USD | 7,640,000.00 USD | 23,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2349.00` | 173,540,000.00 USD | 173,540,000.00 USD | 5,950,000.00 USD | 145,980.00 USD | 5,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2351.30` | 285,640,000.00 USD | 285,640,000.00 USD | 782,590.00 USD | 17,680,000.00 USD | 10,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2351.70` | 201,890,000.00 USD | 201,890,000.00 USD | 21,900,000.00 USD | 2,740,000.00 USD | 3,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2354.30` | 327,340,000.00 USD | 327,340,000.00 USD | 5,960,000.00 USD | 35,020,000.00 USD | 723,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2354.40` | 224,280,000.00 USD | 224,280,000.00 USD | 3,320,000.00 USD | 17,740,000.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2357.10` | 233,140,000.00 USD | 233,140,000.00 USD | 2,930,000.00 USD | 2,470,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2357.30` | 348,490,000.00 USD | 348,490,000.00 USD | 12,050,000.00 USD | 5,920,000.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2359.80` | 250,220,000.00 USD | 250,220,000.00 USD | 6,590,000.00 USD | 5,500,000.00 USD | 4,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2360.30` | 356,640,000.00 USD | 356,640,000.00 USD | 4,730,000.00 USD | 3,430,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2362.50` | 268,840,000.00 USD | 268,840,000.00 USD | 8,420,000.00 USD | 6,710,000.00 USD | 3,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2363.30` | 364,710,000.00 USD | 364,710,000.00 USD | 2,820,000.00 USD | 0.00 USD | 5,250,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 1,020.00 USD | 1,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2365.20` | 279,960,000.00 USD | 279,960,000.00 USD | 1,870,000.00 USD | 3,710,000.00 USD | 5,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2366.30` | 372,710,000.00 USD | 372,710,000.00 USD | 6,340,000.00 USD | 0.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2367.90` | 287,560,000.00 USD | 287,560,000.00 USD | 5,640,000.00 USD | 1,740,000.00 USD | 216,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2369.30` | 407,740,000.00 USD | 407,740,000.00 USD | 20,720,000.00 USD | 475,460.00 USD | 13,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2370.60` | 327,500,000.00 USD | 327,500,000.00 USD | 17,490,000.00 USD | 12,900,000.00 USD | 9,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2372.30` | 464,250,000.00 USD | 464,250,000.00 USD | 16,520,000.00 USD | 0.00 USD | 39,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2373.30` | 350,800,000.00 USD | 350,800,000.00 USD | 14,350,000.00 USD | 2,370,000.00 USD | 6,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 47,010.00 USD | 48,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2375.30` | 486,610,000.00 USD | 486,610,000.00 USD | 9,700,000.00 USD | 121,480.00 USD | 12,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2376.00` | 375,790,000.00 USD | 375,790,000.00 USD | 12,200,000.00 USD | 4,350,000.00 USD | 8,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2378.30` | 529,620,000.00 USD | 529,620,000.00 USD | 11,180,000.00 USD | 7,950,000.00 USD | 23,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2378.70` | 398,380,000.00 USD | 398,380,000.00 USD | 5,240,000.00 USD | 7,340,000.00 USD | 10,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2381.30` | 555,840,000.00 USD | 555,840,000.00 USD | 4,540,000.00 USD | 2,390,000.00 USD | 19,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2381.40` | 445,410,000.00 USD | 445,410,000.00 USD | 15,780,000.00 USD | 12,940,000.00 USD | 18,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2384.10` | 498,850,000.00 USD | 498,850,000.00 USD | 23,340,000.00 USD | 18,150,000.00 USD | 11,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2384.30` | 624,070,000.00 USD | 624,070,000.00 USD | 16,580,000.00 USD | 22,660,000.00 USD | 28,990,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 3,730,000.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2386.80` | 536,760,000.00 USD | 536,760,000.00 USD | 13,400,000.00 USD | 12,760,000.00 USD | 11,750,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2387.30` | 728,880,000.00 USD | 728,880,000.00 USD | 11,380,000.00 USD | 36,580,000.00 USD | 56,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2389.50` | 560,380,000.00 USD | 560,380,000.00 USD | 11,060,000.00 USD | 6,460,000.00 USD | 6,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2390.30` | 831,900,000.00 USD | 831,900,000.00 USD | 5,280,000.00 USD | 51,540,000.00 USD | 46,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2392.20` | 582,100,000.00 USD | 582,100,000.00 USD | 3,100,000.00 USD | 11,880,000.00 USD | 6,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2393.30` | 932,690,000.00 USD | 932,690,000.00 USD | 41,100,000.00 USD | 34,590,000.00 USD | 25,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2394.90` | 602,020,000.00 USD | 602,020,000.00 USD | 8,320,000.00 USD | 8,870,000.00 USD | 2,730,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 4,420,000.00 USD | 8,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2396.30` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 33,360,000.00 USD | 33,060,000.00 USD | 31,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2397.60` | 620,080,000.00 USD | 620,080,000.00 USD | 3,500,000.00 USD | 6,310,000.00 USD | 8,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2399.30` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 44,060,000.00 USD | 33,280,000.00 USD | 23,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2400.30` | 644,780,000.00 USD | 644,780,000.00 USD | 11,310,000.00 USD | 4,850,000.00 USD | 8,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2402.30` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 52,600,000.00 USD | 27,170,000.00 USD | 31,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2403.00` | 666,920,000.00 USD | 666,920,000.00 USD | 6,510,000.00 USD | 7,590,000.00 USD | 8,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 9,120,000.00 USD | 17,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2405.30` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 41,170,000.00 USD | 27,570,000.00 USD | 18,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2405.70` | 698,420,000.00 USD | 698,420,000.00 USD | 14,960,000.00 USD | 8,590,000.00 USD | 7,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2408.30` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 29,480,000.00 USD | 33,990,000.00 USD | 28,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2408.40` | 728,720,000.00 USD | 728,720,000.00 USD | 11,990,000.00 USD | 10,910,000.00 USD | 7,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2411.10` | 754,840,000.00 USD | 754,840,000.00 USD | 9,330,000.00 USD | 9,450,000.00 USD | 7,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2411.30` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 18,580,000.00 USD | 20,460,000.00 USD | 21,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2413.80` | 766,310,000.00 USD | 766,310,000.00 USD | 4,700,000.00 USD | 3,670,000.00 USD | 3,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2414.30` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 20,830,000.00 USD | 23,120,000.00 USD | 21,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 459,730.00 USD | 17,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2416.50` | 783,590,000.00 USD | 783,590,000.00 USD | 5,200,000.00 USD | 7,670,000.00 USD | 4,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2417.30` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 25,250,000.00 USD | 7,450,000.00 USD | 22,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2419.20` | 794,990,000.00 USD | 794,990,000.00 USD | 5,120,000.00 USD | 2,900,000.00 USD | 3,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2420.30` | 1,690,000,000.00 USD | 1,690,000,000.00 USD | 34,500,000.00 USD | 31,850,000.00 USD | 18,740,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2421.90` | 810,390,000.00 USD | 810,390,000.00 USD | 4,170,000.00 USD | 5,160,000.00 USD | 6,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2423.30` | 1,760,000,000.00 USD | 1,760,000,000.00 USD | 18,720,000.00 USD | 26,340,000.00 USD | 30,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2424.60` | 815,690,000.00 USD | 815,690,000.00 USD | 1,790,000.00 USD | 2,670,000.00 USD | 844,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 816,560.00 USD | 18,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2426.30` | 1,840,000,000.00 USD | 1,840,000,000.00 USD | 24,650,000.00 USD | 28,530,000.00 USD | 28,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2427.30` | 817,150,000.00 USD | 817,150,000.00 USD | 731,900.00 USD | 124,100.00 USD | 601,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2429.30` | 1,880,000,000.00 USD | 1,880,000,000.00 USD | 12,010,000.00 USD | 15,290,000.00 USD | 10,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2430.00` | 821,680,000.00 USD | 821,680,000.00 USD | 1,550,000.00 USD | 1,770,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2432.30` | 1,920,000,000.00 USD | 1,920,000,000.00 USD | 12,170,000.00 USD | 12,970,000.00 USD | 8,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2432.70` | 825,710,000.00 USD | 825,710,000.00 USD | 2,090,000.00 USD | 1,690,000.00 USD | 247,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 8,040,000.00 USD | 26,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2435.30` | 1,970,000,000.00 USD | 1,970,000,000.00 USD | 25,850,000.00 USD | 17,900,000.00 USD | 11,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2435.40` | 829,540,000.00 USD | 829,540,000.00 USD | 1,790,000.00 USD | 495,600.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2438.10` | 831,020,000.00 USD | 831,020,000.00 USD | 777,840.00 USD | 683,870.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2438.30` | 2,010,000,000.00 USD | 2,010,000,000.00 USD | 11,720,000.00 USD | 17,290,000.00 USD | 10,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2440.80` | 837,240,000.00 USD | 837,240,000.00 USD | 2,570,000.00 USD | 2,430,000.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2441.30` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 15,870,000.00 USD | 6,990,000.00 USD | 11,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2443.50` | 839,140,000.00 USD | 839,140,000.00 USD | 23,020.00 USD | 534,250.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2444.30` | 2,080,000,000.00 USD | 2,080,000,000.00 USD | 8,760,000.00 USD | 15,160,000.00 USD | 13,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 143,630.00 USD | 26,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2446.20` | 842,610,000.00 USD | 842,610,000.00 USD | 1,880,000.00 USD | 347,060.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2447.30` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 11,130,000.00 USD | 7,420,000.00 USD | 16,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2448.90` | 845,750,000.00 USD | 845,750,000.00 USD | 403,160.00 USD | 640,750.00 USD | 2,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2450.30` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 13,320,000.00 USD | 12,230,000.00 USD | 14,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2451.60` | 855,540,000.00 USD | 855,540,000.00 USD | 3,100,000.00 USD | 3,030,000.00 USD | 3,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2453.30` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 8,570,000.00 USD | 6,560,000.00 USD | 5,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2454.30` | 866,530,000.00 USD | 866,530,000.00 USD | 4,830,000.00 USD | 2,910,000.00 USD | 3,250,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 106,960.00 USD | 26,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2456.30` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 5,870,000.00 USD | 8,700,000.00 USD | 6,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2457.00` | 872,730,000.00 USD | 872,730,000.00 USD | 1,800,000.00 USD | 2,660,000.00 USD | 1,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2459.30` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 11,550,000.00 USD | 12,370,000.00 USD | 11,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2459.70` | 877,280,000.00 USD | 877,280,000.00 USD | 1,880,000.00 USD | 1,190,000.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2462.30` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 9,000,000.00 USD | 11,030,000.00 USD | 8,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2462.40` | 880,180,000.00 USD | 880,180,000.00 USD | 0.00 USD | 2,050,000.00 USD | 841,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 483,330.00 USD | 27,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2465.10` | 881,310,000.00 USD | 881,310,000.00 USD | 352,200.00 USD | 780,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2465.30` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 6,340,000.00 USD | 3,130,000.00 USD | 2,800,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2467.80` | 881,380,000.00 USD | 881,380,000.00 USD | 0.00 USD | 68,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2468.30` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 3,850,000.00 USD | 2,950,000.00 USD | 368,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2470.50` | 882,400,000.00 USD | 882,400,000.00 USD | 0.00 USD | 627,940.00 USD | 391,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2471.30` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 3,230,000.00 USD | 3,380,000.00 USD | 177,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2474.30` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 5,650,000.00 USD | 843,640.00 USD | 2,420,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 386,010.00 USD | 27,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2477.30` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 1,030,000.00 USD | 3,900,000.00 USD | 692,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2480.30` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 2,110,000.00 USD | 1,740,000.00 USD | 505,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2483.30` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 1,210,000.00 USD | 1,190,000.00 USD | 77,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 2,000,000.00 USD | 29,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2486.30` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 49,690.00 USD | 51,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2489.30` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 1,400,000.00 USD | 1,360,000.00 USD | 101,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2492.30` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 1,730,000.00 USD | 2,780,000.00 USD | 3,730,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 941,300.00 USD | 30,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2495.30` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 972,540.00 USD | 2,980,000.00 USD | 4,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2498.30` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 2,250,000.00 USD | 3,770,000.00 USD | 3,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2501.30` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 1,040,000.00 USD | 1,460,000.00 USD | 881,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2504.30` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 47,940.00 USD | 1,320,000.00 USD | 170,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 119,320.00 USD | 30,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2507.30` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 4,160,000.00 USD | 3,090,000.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2510.30` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 1,200,000.00 USD | 2,300,000.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2513.30` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 720,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 139,000.00 USD | 30,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2516.30` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2519.10` | 882,480,000.00 USD | 882,480,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2519.30` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2521.80` | 883,310,000.00 USD | 883,310,000.00 USD | 113,940.00 USD | 113,720.00 USD | 600,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2522.30` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 1,150,000.00 USD | 88,100.00 USD | 945,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2524.50` | 884,730,000.00 USD | 884,730,000.00 USD | 951,350.00 USD | 442,250.00 USD | 30,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 1,160,000.00 USD | 32,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2525.30` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 307,040.00 USD | 1,160,000.00 USD | 200,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2527.20` | 885,480,000.00 USD | 885,480,000.00 USD | 333,430.00 USD | 362,000.00 USD | 50,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2528.30` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 1,580,000.00 USD | 1,690,000.00 USD | 727,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2529.90` | 887,560,000.00 USD | 887,560,000.00 USD | 995,550.00 USD | 645,910.00 USD | 437,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2531.30` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 2,720,000.00 USD | 1,490,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2532.60` | 887,970,000.00 USD | 887,970,000.00 USD | 407,340.00 USD | 0.00 USD | 8,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2534.30` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 2,660,000.00 USD | 2,230,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2535.00` | 663,280.00 USD | 32,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2535.30` | 889,210,000.00 USD | 889,210,000.00 USD | 254,850.00 USD | 62,630.00 USD | 921,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2537.30` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 3,480,000.00 USD | 3,860,000.00 USD | 3,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2538.00` | 894,620,000.00 USD | 894,620,000.00 USD | 2,380,000.00 USD | 1,020,000.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2540.30` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 4,080,000.00 USD | 2,050,000.00 USD | 1,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2540.70` | 897,240,000.00 USD | 897,240,000.00 USD | 1,180,000.00 USD | 1,010,000.00 USD | 436,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2543.30` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 3,910,000.00 USD | 2,510,000.00 USD | 1,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2543.40` | 899,870,000.00 USD | 899,870,000.00 USD | 1,510,000.00 USD | 1,100,000.00 USD | 21,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2545.00` | 6,460,000.00 USD | 39,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2546.10` | 902,750,000.00 USD | 902,750,000.00 USD | 1,290,000.00 USD | 1,180,000.00 USD | 417,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2546.30` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 941,430.00 USD | 1,090,000.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2548.80` | 906,840,000.00 USD | 906,840,000.00 USD | 1,520,000.00 USD | 944,970.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2549.30` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 4,150,000.00 USD | 2,290,000.00 USD | 3,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2551.50` | 909,760,000.00 USD | 909,760,000.00 USD | 1,350,000.00 USD | 984,950.00 USD | 590,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2552.30` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 1,850,000.00 USD | 1,350,000.00 USD | 893,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2554.20` | 911,150,000.00 USD | 911,150,000.00 USD | 929,970.00 USD | 224,110.00 USD | 236,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2555.00` | 2,830,000.00 USD | 42,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2555.30` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 4,340,000.00 USD | 952,210.00 USD | 6,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2556.90` | 913,280,000.00 USD | 913,280,000.00 USD | 874,550.00 USD | 509,280.00 USD | 740,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2558.30` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 3,930,000.00 USD | 1,200,000.00 USD | 2,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2559.60` | 917,210,000.00 USD | 917,210,000.00 USD | 1,830,000.00 USD | 1,040,000.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2561.30` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 2,740,000.00 USD | 2,030,000.00 USD | 461,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2562.30` | 919,560,000.00 USD | 919,560,000.00 USD | 451,210.00 USD | 797,210.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2564.30` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 1,840,000.00 USD | 2,150,000.00 USD | 1,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2565.00` | 920,910,000.00 USD | 920,910,000.00 USD | 425,980.00 USD | 669,810.00 USD | 248,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2565.00` | 1,790,000.00 USD | 43,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2567.30` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 575,630.00 USD | 1,560,000.00 USD | 2,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2567.70` | 921,240,000.00 USD | 921,240,000.00 USD | 121,690.00 USD | 31,040.00 USD | 175,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2570.30` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 125,250.00 USD | 290,680.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2570.40` | 922,430,000.00 USD | 922,430,000.00 USD | 598,470.00 USD | 289,160.00 USD | 306,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2573.10` | 923,790,000.00 USD | 923,790,000.00 USD | 521,320.00 USD | 671,930.00 USD | 168,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2573.30` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 2,050,000.00 USD | 986,590.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2575.00` | 11,830,000.00 USD | 55,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2575.80` | 924,670,000.00 USD | 924,670,000.00 USD | 526,800.00 USD | 0.00 USD | 347,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2576.30` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 2,270,000.00 USD | 356,360.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2579.30` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 2,250,000.00 USD | 1,920,000.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2582.30` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 2,270,000.00 USD | 1,030,000.00 USD | 3,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2585.00` | 26,470,000.00 USD | 82,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2585.30` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 923,330.00 USD | 2,700,000.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2588.30` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 2,590,000.00 USD | 578,010.00 USD | 2,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2591.30` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 2,630,000.00 USD | 748,650.00 USD | 726,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2594.30` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 1,060,000.00 USD | 634,780.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2595.00` | 8,180,000.00 USD | 90,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2597.30` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 2,700,000.00 USD | 2,150,000.00 USD | 2,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2600.30` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 496,060.00 USD | 1,400,000.00 USD | 1,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2603.30` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 1,660,000.00 USD | 1,250,000.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2605.00` | 660,550.00 USD | 91,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2606.30` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 1,850,000.00 USD | 1,110,000.00 USD | 360,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2609.30` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2612.30` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 1,010,000.00 USD | 608,060.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2615.00` | 1,190,000.00 USD | 92,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2615.30` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 815,100.00 USD | 1,000,000.00 USD | 635,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2618.30` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 1,550,000.00 USD | 209,240.00 USD | 434,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2621.30` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 547,980.00 USD | 1,530,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2624.30` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 130,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2625.00` | 453,080.00 USD | 92,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2626.50` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 459,630.00 USD | 463,640.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `455.00` | 871,550,000.00 USD | 0.00 USD | 81,350.00 USD | `-80.52%` | `178.80` |
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
  * Total Open Interest: `28.73B` | Total OI Tokens: `12,766,476.6 ETH`
  * 1h OI Change: `-3.48%` | 4h OI Change: `-5.46%` | 24h OI Change: `-3.68%`
  * Exchange Breakdown: Binance=`8.49B` | Bybit=`2.05B` | OKX=`1.70B` | Hyperliquid=`2.48B`
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
| `15M` | `ETH` | `37.46%` | `62.54%` | `0.60` | 7,110,000,000.00 USD |
| `15M` | `Binance` | `37.32%` | `62.68%` | `0.60` | 2,330,000,000.00 USD |
| `15M` | `OKX` | `36.87%` | `63.13%` | `0.58` | 990,360,000.00 USD |
| `15M` | `Bybit` | `32.57%` | `67.43%` | `0.48` | 938,480,000.00 USD |
| `15M` | `KuCoin` | `36.64%` | `63.36%` | `0.58` | 48,820,000.00 USD |
| `15M` | `Gate` | `49.62%` | `50.38%` | `0.98` | 313,050,000.00 USD |
| `15M` | `Bitget` | `48.92%` | `51.08%` | `0.96` | 255,040,000.00 USD |
| `15M` | `BingX` | `46.18%` | `53.82%` | `0.86` | 114,270,000.00 USD |
| `15M` | `MEXC` | `47.29%` | `52.71%` | `0.90` | 354,190,000.00 USD |
| `15M` | `Bitunix` | `45.93%` | `54.07%` | `0.85` | 375,030,000.00 USD |
| `15M` | `Hyperliquid` | `32.14%` | `67.86%` | `0.47` | 475,260,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `54.19%` | `45.81%` | `1.18` | 42,460,000.00 USD |
| `15M` | `Crypto.com` | `50.15%` | `49.85%` | `1.01` | 32,000,000.00 USD |
| `15M` | `WhiteBIT` | `19.73%` | `80.27%` | `0.25` | 487,190,000.00 USD |
| `15M` | `HTX` | `38.25%` | `61.75%` | `0.62` | 30,540,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `47.32%` | `52.68%` | `0.90` | 111,090,000.00 USD |
| `15M` | `Bitfinex` | `15.86%` | `84.14%` | `0.19` | 3,480,000.00 USD |
| `15M` | `Kraken` | `33.08%` | `66.92%` | `0.49` | 67,900,000.00 USD |
| `15M` | `Aster` | `37.85%` | `62.15%` | `0.61` | 79,040,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `45.03%` | `54.97%` | `0.82` | 57,560,000.00 USD |
| `15M` | `Whale Positions` | `37.32%` | `62.68%` | `0.60` | 2,330,000,000.00 USD |
| `15M` | `Global Accounts` | `37.46%` | `62.54%` | `0.60` | 7,110,000,000.00 USD |
| `1H` | `ETH` | `43.17%` | `56.83%` | `0.76` | 9,500,000,000.00 USD |
| `1H` | `Binance` | `41.54%` | `58.46%` | `0.71` | 3,080,000,000.00 USD |
| `1H` | `OKX` | `41.22%` | `58.78%` | `0.70` | 1,290,000,000.00 USD |
| `1H` | `Bybit` | `36.98%` | `63.02%` | `0.59` | 1,160,000,000.00 USD |
| `1H` | `KuCoin` | `49.12%` | `50.88%` | `0.97` | 54,020,000.00 USD |
| `1H` | `Gate` | `48.29%` | `51.71%` | `0.93` | 686,520,000.00 USD |
| `1H` | `Bitget` | `49%` | `51%` | `0.96` | 343,790,000.00 USD |
| `1H` | `BingX` | `44.75%` | `55.25%` | `0.81` | 138,050,000.00 USD |
| `1H` | `MEXC` | `45.26%` | `54.74%` | `0.83` | 508,880,000.00 USD |
| `1H` | `Bitunix` | `44.02%` | `55.98%` | `0.79` | 522,050,000.00 USD |
| `1H` | `Hyperliquid` | `43.21%` | `56.79%` | `0.76` | 621,960,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.83%` | `49.17%` | `1.03` | 56,300,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 45,810,000.00 USD |
| `1H` | `WhiteBIT` | `48.08%` | `51.92%` | `0.93` | 471,160,000.00 USD |
| `1H` | `HTX` | `33.8%` | `66.2%` | `0.51` | 40,650,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `43.43%` | `56.57%` | `0.77` | 167,430,000.00 USD |
| `1H` | `Bitfinex` | `23.08%` | `76.92%` | `0.30` | 5,700,000.00 USD |
| `1H` | `Kraken` | `49.22%` | `50.78%` | `0.97` | 99,710,000.00 USD |
| `1H` | `Aster` | `46.48%` | `53.52%` | `0.87` | 105,480,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `47.57%` | `52.43%` | `0.91` | 94,350,000.00 USD |
| `1H` | `Whale Positions` | `41.54%` | `58.46%` | `0.71` | 3,080,000,000.00 USD |
| `1H` | `Global Accounts` | `43.17%` | `56.83%` | `0.76` | 9,500,000,000.00 USD |
| `4H` | `ETH` | `42.81%` | `57.19%` | `0.75` | 16,760,000,000.00 USD |
| `4H` | `Binance` | `41.21%` | `58.79%` | `0.70` | 5,240,000,000.00 USD |
| `4H` | `OKX` | `41.96%` | `58.04%` | `0.72` | 2,240,000,000.00 USD |
| `4H` | `Bybit` | `38.53%` | `61.47%` | `0.63` | 1,840,000,000.00 USD |
| `4H` | `KuCoin` | `37.62%` | `62.38%` | `0.60` | 81,860,000.00 USD |
| `4H` | `Gate` | `51.02%` | `48.98%` | `1.04` | 1,440,000,000.00 USD |
| `4H` | `Bitget` | `48.02%` | `51.98%` | `0.92` | 731,690,000.00 USD |
| `4H` | `BingX` | `51.05%` | `48.95%` | `1.04` | 281,610,000.00 USD |
| `4H` | `MEXC` | `48.53%` | `51.47%` | `0.94` | 945,380,000.00 USD |
| `4H` | `Bitunix` | `48.99%` | `51.01%` | `0.96` | 888,230,000.00 USD |
| `4H` | `Hyperliquid` | `40.04%` | `59.96%` | `0.67` | 1,010,000,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `57.11%` | `42.89%` | `1.33` | 110,120,000.00 USD |
| `4H` | `Crypto.com` | `50.73%` | `49.27%` | `1.03` | 109,820,000.00 USD |
| `4H` | `WhiteBIT` | `25.82%` | `74.18%` | `0.35` | 805,240,000.00 USD |
| `4H` | `HTX` | `42.58%` | `57.42%` | `0.74` | 70,480,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `53%` | `47%` | `1.13` | 392,850,000.00 USD |
| `4H` | `Bitfinex` | `26.61%` | `73.39%` | `0.36` | 9,960,000.00 USD |
| `4H` | `Kraken` | `38.73%` | `61.27%` | `0.63` | 157,010,000.00 USD |
| `4H` | `Aster` | `40.55%` | `59.45%` | `0.68` | 185,580,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `46.93%` | `53.07%` | `0.88` | 235,760,000.00 USD |
| `4H` | `Whale Positions` | `41.21%` | `58.79%` | `0.70` | 5,240,000,000.00 USD |
| `4H` | `Global Accounts` | `42.81%` | `57.19%` | `0.75` | 16,760,000,000.00 USD |


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
| `0:00 UTC` | `2300.25` | `2296.32` | `2300.25` | `2319.25` | `2283.25` | 777,199,735.55 USD | 330,087,673.11 USD | 447,112,062.44 USD | -117,024,389.33 USD | `-15.06%` | `1B / 16S` |

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
| `5m` | -35,340,000.00 USD | -341,720,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -57,840,000.00 USD | -627,900,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -54,330,000.00 USD | -629,070,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -61,520,000.00 USD | -880,170,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -38,520,000.00 USD | -799,640,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -43,230,000.00 USD | -1,100,000,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -35,270,000.00 USD | -1,150,000,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -51,740,000.00 USD | -948,020,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -53,980,000.00 USD | -973,650,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -90,800,000.00 USD | -1,320,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -85,330,000.00 USD | -1,900,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,080,000,000.00 USD | -9,050,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-35.34M` | 15m=`-57.84M` | 1h=`-61.52M` | 24h=`-90.80M`
* Futures Capital Netflows: 5m=`-341.72M` | 15m=`-627.90M` | 1h=`-880.17M` | 24h=`-1.32B`
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
  * `2026-10-30 01:35:25 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:09:25 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:09:25 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:09:25 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:08:25 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:08:25 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:10:25 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:10:25 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:10:25 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:10:25 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:25 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:25 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:25 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:25 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:25 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `2296.91` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2274.17` (Risk Distance: `22.74` pts)
  * +2.5R Take Profit: `2353.75`
  * Mathematical Lot Sizing: **`0.43 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2336.14` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2358.88` (Risk Distance: `22.74` pts)
  * +2.5R Take Profit: `2279.30`
  * Mathematical Lot Sizing: **`0.43 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2266.79`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
