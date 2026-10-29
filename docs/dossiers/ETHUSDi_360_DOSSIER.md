# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-29 22:45:58 IST` (`2026-10-29 17:15:58 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2349.30` | **Live Ask Quote**: `2352.30` | **Mid Price**: `2350.80`
- **Spread Points**: `300.00` | **Spread BPS**: `12.76 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2322.63` | VWAP Z-Score: `+1.40` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `11.88` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `58.41` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2379.20` | Lower -3.00σ Band: `2266.05`
  * Upper +2.51σ Band: `2369.96` | Lower -2.51σ Band: `2275.30`
  * Upper +2.01σ Band: `2360.53` | Lower -2.01σ Band: `2284.72`
  * Upper +2.00σ Band: `2360.35` | Lower -2.00σ Band: `2284.91`
  * Upper +1.28σ Band: `2346.77` | Lower -1.28σ Band: `2298.49`
  * Upper +1.00σ Band: `2341.49` | Lower -1.00σ Band: `2303.77`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2351.71` | EMA-20=`2342.12` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2331.99` (Slope: `+0.0000`) | EMA-100=`2331.46`
  * Institutional Anchors: EMA-144=`2331.43` | EMA-200=`2329.96` (Slope: `+0.1101`) | EMA-233=`2328.74`
- **Range Boundaries**: 24H High=`2387.80` | 24H Low=`2288.80` | Weekly High=`2387.80` | Weekly Low=`2288.80`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2335.58` (Distance: `+0.68%`)
  * Point of Control (POC) = `2318.94` (Distance: `+1.40%`)
  * Value Area Low (VAL) = `2293.68` (Distance: `+2.52%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `2341.40` - `2360.20`
  * Optimal Trade Entry (OTE 0.705): `2355.50`
  * Structural Invalidation Anchor (0.786): `2369.61`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2352.18` | `2353.79` | `2350.00` | `2353.79` | `13,805` | 32,462,893.88 USD | -317,375.68 USD | `-0.98%` | -179,537,727.83 USD | `+0.26` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `2353.79` | `2353.79` | `2349.45` | `2351.71` | `13,763` | 32,358,139.73 USD | -11,287,923.12 USD | `-34.88%` | -190,825,650.94 USD | `-0.37` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `2351.72` | `2353.50` | `2350.11` | `2353.15` | `9,238` | 21,725,893.59 USD | -4,938,920.34 USD | `-22.73%` | -195,764,571.28 USD | `+0.17` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `2356.68` | `2359.44` | `2350.25` | `2357.70` | `53,186` | 125,220,561.61 USD | -18,031,212.02 USD | `-14.40%` | -161,511,217.08 USD | `-0.60` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `2357.71` | `2358.31` | `2350.50` | `2352.18` | `30,135` | 70,925,128.95 USD | -17,709,135.06 USD | `-24.97%` | -179,220,352.15 USD | `-0.60` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `2352.18` | `2353.79` | `2349.45` | `2353.49` | `36,639` | 86,154,992.74 USD | -16,262,187.97 USD | `-18.88%` | -195,482,540.12 USD | `-0.53` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `2343.79` | `2372.42` | `2343.64` | `2368.02` | `352,713` | 832,609,165.45 USD | 75,422,863.20 USD | `+9.06%` | -132,463,849.43 USD | `+2.09` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `2368.02` | `2378.69` | `2350.25` | `2352.18` | `255,135` | 602,581,670.57 USD | -105,228,527.95 USD | `-17.46%` | -237,692,377.38 USD | `-2.06` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `2352.18` | `2353.79` | `2349.45` | `2353.49` | `36,639` | 86,154,992.74 USD | -16,262,187.97 USD | `-18.88%` | -253,954,565.35 USD | `-0.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2309.10` | `2330.05` | `2308.88` | `2324.26` | `409,016` | 949,400,649.22 USD | -49,162,247.72 USD | `-5.18%` | -277,081,181.03 USD | `+0.30` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -173,041,008.80 USD | `+1.51` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2349.45` | `2353.39` | `291,870` | 688,963,312.65 USD | -121,611,415.41 USD | `-17.65%` | -294,652,424.21 USD | `-0.81` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `2358.56` | `2360.38` | `2292.20` | `2308.04` | `812,683` | 1,883,052,517.85 USD | -183,572,583.45 USD | `-9.75%` | -193,002,187.18 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2308.03` | `2334.83` | `2303.75` | `2309.10` | `525,175` | 1,216,920,375.04 USD | -34,916,746.14 USD | `-2.87%` | -227,918,933.31 USD | `+0.53` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2309.10` | `2330.05` | `2308.88` | `2324.26` | `409,016` | 949,400,649.22 USD | -49,162,247.72 USD | `-5.18%` | -277,081,181.03 USD | `+0.30` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -173,041,008.80 USD | `+1.51` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2349.45` | `2353.39` | `291,870` | 688,963,312.65 USD | -121,611,415.41 USD | `-17.65%` | -294,652,424.21 USD | `-0.81` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`2350.80`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2351.20` | `893.9978` | 2,101,967.63 USD | 16,843,725.35 USD | `13 orders` | `-0.08%` | `-` |
| `BID` | `2351.30` | `249.8888` | 587,563.54 USD | 14,741,757.72 USD | `13 orders` | `-0.08%` | `-` |
| `BID` | `2351.40` | `319.6143` | 751,541.07 USD | 14,154,194.19 USD | `15 orders` | `-0.07%` | `-` |
| `BID` | `2351.50` | `134.6662` | 316,667.57 USD | 13,402,653.12 USD | `9 orders` | `-0.07%` | `-` |
| `BID` | `2351.60` | `292.2230` | 687,191.61 USD | 13,085,985.56 USD | `12 orders` | `-0.07%` | `-` |
| `BID` | `2351.70` | `568.5051` | 1,336,953.44 USD | 12,398,793.95 USD | `17 orders` | `-0.06%` | `-` |
| `BID` | `2351.80` | `325.1930` | 764,788.90 USD | 11,061,840.50 USD | `15 orders` | `-0.06%` | `-` |
| `BID` | `2351.90` | `477.3844` | 1,122,760.37 USD | 10,297,051.61 USD | `14 orders` | `-0.05%` | `-` |
| `BID` | `2352.00` | `165.6122` | 389,519.89 USD | 9,174,291.24 USD | `14 orders` | `-0.05%` | `-` |
| `BID` | `2352.10` | `726.3121` | 1,708,358.69 USD | 8,784,771.34 USD | `19 orders` | `-0.04%` | `-` |
| `BID` | `2352.20` | `347.6676` | 817,783.73 USD | 7,076,412.65 USD | `16 orders` | `-0.04%` | `-` |
| `BID` | `2352.30` | `177.4499` | 417,415.40 USD | 6,258,628.92 USD | `14 orders` | `-0.04%` | `-` |
| `BID` | `2352.40` | `473.8616` | 1,114,712.03 USD | 5,841,213.52 USD | `18 orders` | `-0.03%` | `-` |
| `BID` | `2352.50` | `530.7515` | 1,248,592.90 USD | 4,726,501.50 USD | `21 orders` | `-0.03%` | `-` |
| `BID` | `2352.60` | `441.9494` | 1,039,730.16 USD | 3,477,908.59 USD | `22 orders` | `-0.02%` | `-` |
| `BID` | `2352.70` | `224.5788` | 528,366.54 USD | 2,438,178.43 USD | `15 orders` | `-0.02%` | `-` |
| `BID` | `2352.80` | `308.0777` | 724,845.21 USD | 1,909,811.89 USD | `15 orders` | `-0.01%` | `-` |
| `BID` | `2352.90` | `137.0920` | 322,563.77 USD | 1,184,966.68 USD | `15 orders` | `-0.01%` | `-` |
| `BID` | `2353.00` | `105.9162` | 249,220.82 USD | 862,402.91 USD | `8 orders` | `-0.01%` | `-` |
| `BID` | `2353.10` | `260.5848` | 613,182.09 USD | 613,182.09 USD | `35 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2353.15` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,353.15` | `0.00%` | `-` |
| `ASK` | `2353.20` | `7.1009` | 16,709.84 USD | 16,709.84 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `2353.40` | `13.5684` | 31,931.87 USD | 48,641.71 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `2353.50` | `82.5493` | 194,279.78 USD | 242,921.49 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `2353.60` | `50.4147` | 118,656.04 USD | 361,577.53 USD | `9 orders` | `+0.02%` | `-` |
| `ASK` | `2353.70` | `79.1905` | 186,390.68 USD | 547,968.21 USD | `14 orders` | `+0.02%` | `-` |
| `ASK` | `2353.80` | `187.2331` | 440,709.27 USD | 988,677.48 USD | `17 orders` | `+0.03%` | `-` |
| `ASK` | `2353.90` | `683.5992` | 1,609,124.16 USD | 2,597,801.63 USD | `21 orders` | `+0.03%` | `-` |
| `ASK` | `2354.00` | `330.6174` | 778,273.36 USD | 3,376,074.99 USD | `17 orders` | `+0.04%` | `-` |
| `ASK` | `2354.10` | `518.9844` | 1,221,741.18 USD | 4,597,816.17 USD | `15 orders` | `+0.04%` | `-` |
| `ASK` | `2354.20` | `61.4991` | 144,781.18 USD | 4,742,597.35 USD | `12 orders` | `+0.04%` | `-` |
| `ASK` | `2354.30` | `492.3741` | 1,159,196.34 USD | 5,901,793.69 USD | `21 orders` | `+0.05%` | `-` |
| `ASK` | `2354.40` | `370.8840` | 873,209.29 USD | 6,775,002.98 USD | `15 orders` | `+0.05%` | `-` |
| `ASK` | `2354.50` | `430.9326` | 1,014,630.81 USD | 7,789,633.79 USD | `15 orders` | `+0.06%` | `-` |
| `ASK` | `2354.60` | `481.0130` | 1,132,593.21 USD | 8,922,227.00 USD | `20 orders` | `+0.06%` | `-` |
| `ASK` | `2354.70` | `89.1655` | 209,958.00 USD | 9,132,185.00 USD | `14 orders` | `+0.07%` | `-` |
| `ASK` | `2354.80` | `620.6239` | 1,461,445.16 USD | 10,593,630.16 USD | `19 orders` | `+0.07%` | `-` |
| `ASK` | `2354.90` | `359.9878` | 847,735.27 USD | 11,441,365.43 USD | `14 orders` | `+0.07%` | `-` |
| `ASK` | `2355.00` | `79.1221` | 186,332.55 USD | 11,627,697.98 USD | `14 orders` | `+0.08%` | `-` |
| `ASK` | `2355.10` | `542.1502` | 1,276,817.94 USD | 12,904,515.91 USD | `16 orders` | `+0.08%` | `-` |
| `ASK` | `2355.20` | `114.1749` | 268,904.72 USD | 13,173,420.64 USD | `17 orders` | `+0.09%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:44:58 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1892.00` | `8,092.45` | 15,310,914.71 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-29 22:44:58 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1918.00` | `4,184.01` | 8,024,935.59 USD | `TRIGGER_STOP` | `0x6ea486a342` | `2026-10-29 22:44:58 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `8,500.00` | 16,371,850.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-29 22:44:58 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2040.65` | `7,964.66` | 16,253,082.08 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-29 22:44:58 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2101.66` | `10,000.00` | 21,016,620.86 USD | `AT_RISK_LIQ` | `0x469e9a7f62` | `2026-10-29 22:44:58 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2171.11` | `48,499.51` | 105,297,832.78 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-29 22:44:58 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2180.17` | `44,734.81` | 97,529,693.12 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-29 22:44:58 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2250.00` | `6,500.00` | 14,625,000.00 USD | `TRIGGER_STOP` | `0x6eae4120a8` | `2026-10-29 22:44:58 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2292.00` | `2,500.00` | 5,730,000.00 USD | `TRIGGER_STOP` | `0x934de82f50` | `2026-10-29 22:44:58 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2307.20` | `599,999.99` | 1,384,319,976.93 USD | `TRIGGER_STOP` | `0x069604ebfb` | `2026-10-29 22:44:58 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2310.00` | `2,000.00` | 4,620,000.00 USD | `TRIGGER_STOP` | `0x524ed67d71` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2311.00` | `1,015.35` | 2,346,465.99 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x674982e841` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2311.80` | `1,879.74` | 4,345,591.72 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 22:44:58 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2319.00` | `2,500.00` | 5,797,500.00 USD | `TRIGGER_STOP` | `0x524ed67d71` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2324.50` | `1,361.76` | 3,165,401.59 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2326.50` | `5,403.31` | 12,570,805.37 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2326.60` | `474.51` | 1,103,984.26 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x7b7f72a28f` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2329.00` | `343.53` | 800,091.38 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2329.00` | `329.54` | 767,507.74 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2331.80` | `599.49` | 1,397,879.12 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2333.50` | `915.75` | 2,136,899.59 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2334.80` | `2,794.82` | 6,525,348.07 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2334.90` | `405.66` | 947,182.07 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x7b7f72a28f` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2337.50` | `433.03` | 1,012,202.95 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2338.70` | `1,712.18` | 4,004,266.48 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2338.90` | `600.30` | 1,404,036.99 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2340.70` | `645.66` | 1,511,304.55 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2341.80` | `1,282.45` | 3,003,235.79 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2342.60` | `600.34` | 1,406,358.83 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2342.70` | `1,425.93` | 3,340,524.57 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2345.20` | `853.72` | 2,002,135.70 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2345.30` | `433.07` | 1,015,683.76 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2345.40` | `444.49` | 1,042,496.53 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2346.00` | `640.07` | 1,501,612.43 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2346.80` | `356.66` | 837,018.37 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x76bf72092b` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2348.10` | `400.20` | 939,714.32 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2348.70` | `426.22` | 1,001,063.62 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2355.00` | `324.83` | 764,986.42 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2355.20` | `425.09` | 1,001,165.84 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2355.30` | `354.71` | 835,442.81 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x76bf72092b` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2355.70` | `324.11` | 763,516.29 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2356.30` | `400.16` | 942,889.94 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2356.60` | `637.22` | 1,501,677.37 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2358.20` | `433.11` | 1,021,369.43 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2358.60` | `468.56` | 1,105,136.89 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2359.20` | `1,427.39` | 3,367,494.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2359.20` | `848.67` | 2,002,192.64 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2360.90` | `600.18` | 1,416,972.04 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2363.20` | `1,270.87` | 3,003,315.49 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2363.20` | `695.65` | 1,643,971.42 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2364.30` | `1,693.69` | 4,004,398.36 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2364.70` | `600.05` | 1,418,940.60 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2366.00` | `433.04` | 1,024,563.18 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2366.90` | `2,797.90` | 6,622,353.06 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2370.30` | `942.63` | 2,234,324.42 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2372.00` | `600.41` | 1,424,163.03 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2375.30` | `336.84` | 800,099.14 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2375.30` | `323.12` | 767,513.82 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2378.90` | `1,351.41` | 3,214,879.48 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2388.70` | `5,408.95` | 12,920,349.79 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2391.40` | `1,975.55` | 4,724,334.34 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-29 22:44:58 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2396.00` | `500.00` | 1,198,000.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xaa53f4044a` | `2026-10-29 22:44:58 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2440.00` | `4,002.10` | 9,765,127.17 USD | `TRIGGER_STOP` | `0xfb941d2344` | `2026-10-29 22:44:58 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `3,058.48` | 7,688,708.10 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-29 22:44:58 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2658.62` | `9,700.00` | 25,788,617.00 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-29 22:44:58 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2708.97` | `8,500.00` | 23,026,257.07 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-29 22:44:58 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 250,134,830.18 USD | `106,417.71` | `2322.74` | `2350.40` | `3786.96` | -2,953,818.02 USD | `-1.18%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 153,271,271.66 USD | `65,205.17` | `2375.30` | `2350.40` | `4307.02` | 1,610,991.43 USD | `+1.05%` | `5X Cross` |
| `6` | `0x77dd...e0e9` | `LONG` | 114,085,401.84 USD | `48,499.51` | `2610.31` | `2350.40` | `2171.14` | -12,513,482.02 USD | `-10.97%` | `10X Cross` |
| `7` | `0x0392...d7d9` | `LONG` | 105,233,280.35 USD | `44,734.81` | `2518.71` | `2350.40` | `2180.20` | -7,441,026.23 USD | `-7.07%` | `9X Cross` |
| `15` | `0xde8d...9524` | `LONG` | 71,215,128.31 USD | `30,282.40` | `2134.45` | `2350.40` | `1787.09` | 6,578,797.73 USD | `+9.24%` | `20X Cross` |
| `17` | `0x7fda...17d1` | `SHORT` | 66,032,638.10 USD | `28,093.02` | `2437.87` | `2350.40` | `3706.90` | 2,454,592.53 USD | `+3.72%` | `25X Cross` |
| `25` | `0xdf95...7d72` | `SHORT` | 53,244,312.01 USD | `22,652.33` | `2402.54` | `2350.40` | `3945.46` | 1,178,860.95 USD | `+2.21%` | `25X Cross` |
| `29` | `0xeced...6210` | `SHORT` | 43,941,966.91 USD | `18,687.58` | `2522.09` | `2350.40` | `3359.09` | 3,189,945.55 USD | `+7.26%` | `20X Cross` |
| `34` | `0xb695...a92d` | `SHORT` | 39,294,276.45 USD | `16,704.62` | `2557.74` | `2350.40` | `4005.73` | 3,431,888.60 USD | `+8.73%` | `20X Cross` |
| `35` | `0x6046...b21d` | `LONG` | 37,458,505.46 USD | `15,927.59` | `2410.19` | `2350.40` | `1528.57` | -930,114.19 USD | `-2.48%` | `6X Cross` |
| `39` | `0x45d2...4029` | `SHORT` | 32,817,375.00 USD | `13,950.00` | `2443.60` | `2350.40` | `4852.63` | 1,270,907.46 USD | `+3.87%` | `20X Cross` |
| `45` | `0xbd1c...ff0e` | `LONG` | 28,240,800.00 USD | `12,000.00` | `2419.91` | `2350.40` | `1520.97` | -798,232.39 USD | `-2.83%` | `20X Cross` |
| `46` | `0x2371...0883` | `LONG` | 28,207,200.00 USD | `12,000.00` | `2421.77` | `2350.40` | `1280.07` | -854,094.85 USD | `-3.03%` | `20X Cross` |
| `50` | `0x09dc...c094` | `LONG` | 25,872,880.00 USD | `11,000.00` | `2465.31` | `2350.40` | `1638.04` | -1,245,543.04 USD | `-4.81%` | `20X Cross` |
| `51` | `0xa9de...e049` | `LONG` | 25,869,800.00 USD | `11,000.00` | `2481.81` | `2350.40` | `1644.71` | -1,430,179.46 USD | `-5.53%` | `20X Cross` |
| `52` | `0x0c5d...36b3` | `LONG` | 25,868,700.00 USD | `11,000.00` | `2482.20` | `2350.40` | `1645.04` | -1,435,553.24 USD | `-5.55%` | `20X Cross` |
| `54` | `0x6c93...59a4` | `LONG` | 25,858,800.00 USD | `11,000.00` | `2441.15` | `2350.40` | `1603.00` | -993,872.73 USD | `-3.84%` | `20X Cross` |
| `57` | `0xa61c...66b9` | `LONG` | 25,592,244.00 USD | `10,888.00` | `2398.32` | `2350.40` | `1384.85` | -520,713.39 USD | `-2.03%` | `10X Cross` |
| `60` | `0x4487...c92d` | `SHORT` | 25,173,364.79 USD | `10,701.14` | `2374.04` | `2350.40` | `2880.35` | 231,612.79 USD | `+0.92%` | `10X Cross` |
| `61` | `0xecb6...2b00` | `SHORT` | 25,075,011.54 USD | `10,667.95` | `2327.55` | `2350.40` | `5447.09` | -244,786.76 USD | `-0.98%` | `15X Cross` |
| `70` | `0xa2ce...3126` | `LONG` | 23,544,665.16 USD | `10,016.88` | `2162.83` | `2350.40` | `1445.48` | 1,879,863.11 USD | `+7.98%` | `10X Cross` |
| `71` | `0x469e...58a5` | `LONG` | 23,525,000.00 USD | `10,000.00` | `2463.91` | `2350.40` | `2106.51` | -1,114,141.54 USD | `-4.74%` | `25X Cross` |
| `73` | `0x15a4...dfdb` | `LONG` | 23,517,000.00 USD | `10,000.00` | `1761.94` | `2350.40` | `0.000000` | 5,897,518.97 USD | `+25.08%` | `20X Cross` |
| `74` | `0x6646...6de5` | `LONG` | 23,515,900.00 USD | `10,000.00` | `1765.80` | `2350.40` | `1735.84` | 5,857,842.55 USD | `+24.91%` | `25X Cross` |
| `75` | `0xec7f...df39` | `LONG` | 23,514,000.00 USD | `10,000.00` | `2719.35` | `2350.40` | `1721.56` | -3,679,548.52 USD | `-15.65%` | `20X Cross` |
| `80` | `0xaeaa...2416` | `SHORT` | 22,800,820.00 USD | `9,700.00` | `2311.92` | `2350.40` | `2658.65` | -375,137.60 USD | `-1.65%` | `25X Cross` |
| `85` | `0xca49...53c8` | `SHORT` | 21,793,248.52 USD | `9,264.26` | `2549.47` | `2350.40` | `3698.22` | 1,825,776.22 USD | `+8.38%` | `25X Cross` |
| `87` | `0xba5d...a352` | `SHORT` | 21,300,727.65 USD | `9,054.12` | `2493.89` | `2350.40` | `2888.12` | 1,279,279.61 USD | `+6.01%` | `20X Cross` |
| `88` | `0xea00...a918` | `LONG` | 21,174,298.31 USD | `9,003.83` | `2003.01` | `2350.40` | `1155.75` | 3,139,519.44 USD | `+14.83%` | `5X Cross` |
| `96` | `0xb37f...66ca` | `SHORT` | 19,984,350.00 USD | `8,500.00` | `2308.30` | `2350.40` | `2709.00` | -363,795.81 USD | `-1.82%` | `25X Cross` |
| `108` | `0x9eec...daab` | `LONG` | 19,035,875.07 USD | `8,092.45` | `1658.44` | `2350.40` | `1892.61` | 5,615,010.55 USD | `+29.50%` | `15X Cross` |
| `109` | `0x218a...7da2` | `SHORT` | 18,813,825.71 USD | `7,997.78` | `2208.16` | `2350.40` | `2877.22` | -1,153,430.50 USD | `-6.13%` | `10X Cross` |
| `110` | `0x5f91...65aa` | `LONG` | 18,730,481.28 USD | `7,964.66` | `1626.99` | `2350.40` | `2040.68` | 5,772,038.22 USD | `+30.82%` | `16X Cross` |
| `115` | `0xcf53...ee11` | `SHORT` | 17,880,615.33 USD | `7,603.63` | `1862.69` | `2350.40` | `3977.58` | -3,717,351.39 USD | `-20.79%` | `7X Cross` |
| `116` | `0x524e...0de0` | `LONG` | 17,629,500.00 USD | `7,500.00` | `2320.35` | `2350.40` | `2115.20` | 226,813.78 USD | `+1.29%` | `10X Cross` |
| `121` | `0x939f...04d2` | `LONG` | 16,988,963.18 USD | `7,223.81` | `2500.18` | `2350.40` | `1866.78` | -1,071,927.00 USD | `-6.31%` | `25X Cross` |
| `124` | `0xec0b...b078` | `LONG` | 16,473,232.87 USD | `7,007.80` | `2065.97` | `2350.40` | `990.20` | 1,995,303.29 USD | `+12.11%` | `25X Cross` |
| `130` | `0x418a...8888` | `SHORT` | 15,811,713.72 USD | `6,724.38` | `2494.55` | `2350.40` | `2953.68` | 962,609.46 USD | `+6.09%` | `25X Cross` |
| `133` | `0x4ff9...38d3` | `LONG` | 15,434,821.68 USD | `6,564.10` | `2447.40` | `2350.40` | `1670.66` | -630,201.06 USD | `-4.08%` | `3X Isolated` |
| `135` | `0x1ee7...edf5` | `LONG` | 15,290,470.00 USD | `6,500.00` | `2328.85` | `2350.40` | `2135.22` | 152,923.34 USD | `+1.00%` | `25X Cross` |
| `136` | `0xf78c...c581` | `LONG` | 15,274,220.48 USD | `6,500.22` | `2521.53` | `2350.40` | `1914.14` | -1,116,320.47 USD | `-7.31%` | `20X Cross` |
| `142` | `0x799f...5f4c` | `LONG` | 14,835,671.48 USD | `6,310.90` | `2390.33` | `2350.40` | `1703.66` | -249,493.14 USD | `-1.68%` | `20X Cross` |
| `144` | `0x08bf...7872` | `SHORT` | 14,633,357.84 USD | `6,224.05` | `2258.00` | `2350.40` | `2585.90` | -579,441.73 USD | `-3.96%` | `20X Cross` |
| `147` | `0x0c4a...1b19` | `LONG` | 14,431,948.15 USD | `6,135.77` | `2382.15` | `2350.40` | `2186.42` | -184,383.21 USD | `-1.28%` | `25X Isolated` |
| `153` | `0xd9e7...4aff` | `LONG` | 14,110,800.00 USD | `6,000.00` | `2480.18` | `2350.40` | `1408.43` | -770,324.33 USD | `-5.46%` | `20X Cross` |
| `154` | `0xec4a...cf62` | `LONG` | 14,104,200.00 USD | `6,000.00` | `2318.70` | `2350.40` | `2081.79` | 191,954.88 USD | `+1.36%` | `25X Cross` |
| `181` | `0x645b...87b8` | `SHORT` | 11,934,895.67 USD | `5,073.54` | `2421.68` | `2350.40` | `5993.64` | 351,610.28 USD | `+2.95%` | `10X Cross` |
| `188` | `0x45ab...6cbc` | `LONG` | 11,573,118.90 USD | `4,920.96` | `2727.66` | `2350.40` | `1350.19` | -1,849,624.90 USD | `-15.98%` | `7X Cross` |
| `190` | `0xfb18...eb17` | `SHORT` | 11,461,942.91 USD | `4,872.45` | `2315.54` | `2350.40` | `2744.90` | -179,569.88 USD | `-1.57%` | `25X Cross` |
| `193` | `0x64b7...9da9` | `LONG` | 11,416,000.54 USD | `4,856.84` | `2604.61` | `2350.40` | `1385.25` | -1,234,213.87 USD | `-10.81%` | `25X Cross` |
| `200` | `0x5559...d43b` | `SHORT` | 11,184,509.53 USD | `4,755.93` | `2262.69` | `2350.40` | `2885.03` | -423,303.65 USD | `-3.78%` | `25X Cross` |
| `216` | `0xe091...6705` | `SHORT` | 10,582,650.47 USD | `4,500.00` | `2467.33` | `2350.40` | `2572.95` | 520,358.04 USD | `+4.92%` | `20X Cross` |
| `224` | `0xfe7c...b7ae` | `SHORT` | 10,353,553.50 USD | `4,402.58` | `2440.17` | `2350.40` | `4105.78` | 389,534.37 USD | `+3.76%` | `25X Cross` |
| `233` | `0xc179...e0c8` | `LONG` | 10,128,669.06 USD | `4,309.16` | `2342.89` | `2350.40` | `836.74` | 32,790.27 USD | `+0.32%` | `10X Cross` |
| `238` | `0x0622...8088` | `LONG` | 10,059,132.91 USD | `4,279.03` | `2357.74` | `2350.40` | `0.000000` | -29,728.64 USD | `-0.30%` | `5X Cross` |
| `239` | `0x12d2...f97f` | `LONG` | 10,023,332.82 USD | `4,264.34` | `2623.90` | `2350.40` | `1813.41` | -1,165,901.60 USD | `-11.63%` | `20X Cross` |
| `244` | `0x28bb...fca6` | `SHORT` | 9,894,698.18 USD | `4,209.61` | `1896.10` | `2350.40` | `3047.49` | -1,912,815.61 USD | `-19.33%` | `20X Cross` |
| `245` | `0x6ea4...0ea7` | `SHORT` | 9,838,286.52 USD | `4,184.01` | `2602.13` | `2350.40` | `3425.97` | 1,049,060.15 USD | `+10.66%` | `20X Cross` |
| `256` | `0x5e9e...35ee` | `SHORT` | 9,431,381.58 USD | `4,007.56` | `1796.39` | `2350.40` | `2586.46` | -2,232,231.49 USD | `-23.67%` | `20X Cross` |
| `258` | `0xfb94...0ddf` | `SHORT` | 9,414,463.06 USD | `4,002.10` | `2382.44` | `2350.40` | `5105.36` | 120,321.09 USD | `+1.28%` | `20X Cross` |
| `259` | `0x3dc9...54b0` | `SHORT` | 9,410,471.10 USD | `3,999.69` | `2480.32` | `2350.40` | `5669.24` | 510,065.45 USD | `+5.42%` | `20X Cross` |
| `260` | `0x8cc9...2b6a` | `SHORT` | 9,407,200.00 USD | `4,000.00` | `1791.18` | `2350.40` | `3801.69` | -2,242,453.33 USD | `-23.84%` | `25X Cross` |
| `261` | `0x95fe...f8fa` | `LONG` | 9,400,800.00 USD | `4,000.00` | `2341.35` | `2350.40` | `2258.96` | 35,383.49 USD | `+0.38%` | `20X Isolated` |
| `262` | `0x77ee...2902` | `SHORT` | 9,363,813.51 USD | `3,982.23` | `2476.53` | `2350.40` | `4333.52` | 498,308.08 USD | `+5.32%` | `25X Cross` |
| `274` | `0xf02d...5eb3` | `LONG` | 9,064,650.71 USD | `3,855.99` | `2513.67` | `2350.40` | `305.96` | -628,061.60 USD | `-6.93%` | `20X Cross` |
| `276` | `0x4b67...f4e7` | `LONG` | 8,985,473.90 USD | `3,820.84` | `2591.51` | `2350.40` | `1571.30` | -916,299.65 USD | `-10.20%` | `20X Cross` |
| `292` | `0x382b...3e39` | `SHORT` | 8,523,892.92 USD | `3,626.42` | `2299.42` | `2350.40` | `3736.95` | -185,211.56 USD | `-2.17%` | `25X Cross` |
| `300` | `0x8ae4...3d60` | `LONG` | 8,366,747.48 USD | `3,558.20` | `2482.21` | `2350.40` | `304.67` | -465,450.55 USD | `-5.56%` | `10X Cross` |
| `327` | `0x9c06...0560` | `SHORT` | 7,769,029.09 USD | `3,303.58` | `2270.55` | `2350.40` | `3265.92` | -268,065.14 USD | `-3.45%` | `25X Cross` |
| `336` | `0x984e...14c2` | `SHORT` | 7,318,118.45 USD | `3,111.99` | `2357.50` | `2350.40` | `2434.93` | 18,404.31 USD | `+0.25%` | `20X Cross` |
| `339` | `0x9c2a...f6a8` | `SHORT` | 7,186,811.84 USD | `3,058.48` | `2543.83` | `2350.40` | `2593.20` | 593,448.78 USD | `+8.26%` | `20X Cross` |
| `341` | `0x4a20...3c26` | `LONG` | 7,056,900.00 USD | `3,000.00` | `2428.72` | `2350.40` | `162.31` | -229,260.28 USD | `-3.25%` | `20X Cross` |
| `342` | `0x007d...67a0` | `LONG` | 7,056,600.00 USD | `3,000.00` | `2400.00` | `2350.40` | `1493.65` | -143,400.00 USD | `-2.03%` | `25X Cross` |
| `344` | `0x39b4...5c34` | `SHORT` | 7,051,541.84 USD | `3,000.91` | `2329.97` | `2350.40` | `2405.85` | -59,498.09 USD | `-0.84%` | `25X Cross` |
| `386` | `0xf517...c032` | `SHORT` | 6,435,834.24 USD | `2,738.07` | `2053.90` | `2350.40` | `5677.76` | -812,092.33 USD | `-12.62%` | `25X Cross` |
| `400` | `0xc619...10f5` | `LONG` | 6,114,966.00 USD | `2,600.00` | `2318.40` | `2350.40` | `1832.38` | 87,117.09 USD | `+1.42%` | `25X Cross` |
| `401` | `0xbb34...1696` | `LONG` | 6,114,420.00 USD | `2,600.00` | `2318.80` | `2350.40` | `1949.49` | 85,519.15 USD | `+1.40%` | `25X Cross` |
| `406` | `0x8328...f54a` | `SHORT` | 6,059,040.05 USD | `2,576.45` | `2292.01` | `2350.40` | `3280.20` | -153,768.76 USD | `-2.54%` | `25X Cross` |
| `407` | `0xed48...7c9b` | `SHORT` | 5,997,962.92 USD | `2,551.13` | `2460.02` | `2350.40` | `3242.74` | 277,883.49 USD | `+4.63%` | `20X Cross` |
| `411` | `0x934d...92c9` | `LONG` | 5,877,000.00 USD | `2,500.00` | `2343.98` | `2350.40` | `2148.38` | 17,035.49 USD | `+0.29%` | `25X Cross` |
| `432` | `0xfbe2...c8ea` | `SHORT` | 5,652,224.96 USD | `2,404.08` | `2041.57` | `2350.40` | `2712.70` | -744,132.24 USD | `-13.17%` | `20X Cross` |
| `442` | `0x1c98...7fc7` | `LONG` | 5,544,611.78 USD | `2,358.00` | `2467.15` | `2350.40` | `1897.18` | -272,959.70 USD | `-4.92%` | `10X Cross` |
| `461` | `0x6859...7e1e` | `SHORT` | 5,229,317.86 USD | `2,224.58` | `2200.39` | `2350.40` | `3612.64` | -334,365.13 USD | `-6.39%` | `25X Cross` |
| `473` | `0xd507...c948` | `SHORT` | 5,105,720.16 USD | `2,172.00` | `2387.49` | `2350.40` | `2707.38` | 79,920.86 USD | `+1.57%` | `5X Isolated` |
| `475` | `0xb829...3a81` | `LONG` | 5,066,170.98 USD | `2,153.91` | `2537.61` | `2350.40` | `807.20` | -399,625.75 USD | `-7.89%` | `20X Cross` |
| `508` | `0xd4c1...3d1d` | `SHORT` | 4,709,394.73 USD | `2,003.40` | `2336.05` | `2350.40` | `4547.53` | -29,334.92 USD | `-0.62%` | `12X Cross` |
| `510` | `0xf929...d1f9` | `SHORT` | 4,703,400.00 USD | `2,000.00` | `2423.37` | `2350.40` | `2548.78` | 143,340.34 USD | `+3.05%` | `25X Cross` |
| `511` | `0x3440...32c5` | `SHORT` | 4,702,728.62 USD | `2,000.57` | `2198.21` | `2350.40` | `3507.83` | -305,065.48 USD | `-6.49%` | `25X Cross` |
| `524` | `0x0514...bdfe` | `SHORT` | 4,587,570.00 USD | `1,950.00` | `1988.74` | `2350.40` | `2921.05` | -709,510.37 USD | `-15.47%` | `25X Cross` |
| `530` | `0x8376...9a1e` | `SHORT` | 4,492,913.44 USD | `1,910.50` | `2477.72` | `2350.40` | `3151.49` | 240,774.73 USD | `+5.36%` | `20X Cross` |
| `551` | `0x7a6d...f79c` | `SHORT` | 4,292,204.33 USD | `1,825.07` | `2433.80` | `2350.40` | `2775.30` | 149,664.55 USD | `+3.49%` | `25X Cross` |
| `557` | `0x541e...071d` | `SHORT` | 4,243,735.50 USD | `1,805.00` | `2648.19` | `2350.40` | `2985.96` | 536,249.34 USD | `+12.64%` | `25X Cross` |
| `558` | `0x7265...91a5` | `LONG` | 4,237,456.27 USD | `1,801.87` | `2533.96` | `2350.40` | `1988.11` | -328,410.19 USD | `-7.75%` | `20X Cross` |
| `560` | `0x739c...cfb2` | `SHORT` | 4,229,640.00 USD | `1,800.00` | `2427.60` | `2350.40` | `2696.32` | 140,056.38 USD | `+3.31%` | `25X Cross` |
| `568` | `0xa445...329d` | `LONG` | 4,179,447.38 USD | `1,776.75` | `2398.85` | `2350.40` | `1776.74` | -82,721.97 USD | `-1.98%` | `25X Cross` |
| `572` | `0x91a9...3f70` | `SHORT` | 4,154,638.49 USD | `1,767.48` | `2156.23` | `2350.40` | `3612.05` | -343,534.41 USD | `-8.27%` | `4X Cross` |
| `580` | `0x3453...b323` | `SHORT` | 4,115,939.51 USD | `1,750.12` | `2328.82` | `2350.40` | `2399.98` | -40,207.37 USD | `-0.98%` | `25X Cross` |
| `602` | `0xfeec...4e9c` | `SHORT` | 3,976,934.95 USD | `1,691.81` | `2566.49` | `2350.40` | `2649.68` | 365,089.57 USD | `+9.18%` | `10X Cross` |
| `604` | `0x936c...bb0f` | `SHORT` | 3,969,256.44 USD | `1,688.69` | `2434.60` | `2350.40` | `8393.78` | 142,030.66 USD | `+3.58%` | `20X Cross` |
| `621` | `0xeee0...0b53` | `LONG` | 3,850,024.28 USD | `1,637.12` | `2468.64` | `2350.40` | `71.09` | -191,451.79 USD | `-4.97%` | `7X Cross` |
| `625` | `0xfc27...9d9d` | `SHORT` | 3,835,154.31 USD | `1,631.63` | `2402.17` | `2350.40` | `10920.65` | 84,308.68 USD | `+2.20%` | `25X Cross` |
| `626` | `0x27b8...12fc` | `LONG` | 3,828,361.60 USD | `1,628.12` | `2468.73` | `2350.40` | `394.68` | -191,033.03 USD | `-4.99%` | `10X Cross` |
| `627` | `0x982b...4606` | `LONG` | 3,825,786.24 USD | `1,626.82` | `2575.24` | `2350.40` | `1548.38` | -363,666.83 USD | `-9.51%` | `5X Isolated` |
| `633` | `0x73d7...8be1` | `LONG` | 3,766,967.15 USD | `1,601.47` | `2410.40` | `2350.40` | `2031.92` | -93,211.77 USD | `-2.47%` | `25X Cross` |
| `662` | `0xe170...9300` | `SHORT` | 3,606,250.12 USD | `1,533.40` | `2076.39` | `2350.40` | `3197.56` | -422,300.62 USD | `-11.71%` | `25X Cross` |
| `675` | `0x2e2b...2fab` | `LONG` | 3,542,637.43 USD | `1,507.38` | `2245.53` | `2350.40` | `1034.19` | 157,764.33 USD | `+4.45%` | `25X Cross` |
| `679` | `0x251f...6e5d` | `LONG` | 3,525,750.00 USD | `1,500.00` | `2346.68` | `2350.40` | `1558.69` | 5,719.51 USD | `+0.16%` | `20X Cross` |
| `687` | `0xad54...6203` | `LONG` | 3,430,194.17 USD | `1,458.18` | `2627.45` | `2350.40` | `2146.44` | -401,112.51 USD | `-11.69%` | `10X Isolated` |
| `698` | `0xef70...a84c` | `SHORT` | 3,391,168.36 USD | `1,442.74` | `2424.73` | `2350.40` | `3494.62` | 107,102.46 USD | `+3.16%` | `25X Cross` |
| `703` | `0x4b5f...0dd8` | `LONG` | 3,365,384.87 USD | `1,431.96` | `2339.45` | `2350.40` | `2148.67` | 15,391.93 USD | `+0.46%` | `10X Cross` |
| `708` | `0xbadb...9ee6` | `LONG` | 3,358,746.69 USD | `1,428.16` | `1936.00` | `2350.40` | `1015.25` | 593,825.04 USD | `+17.68%` | `20X Cross` |
| `768` | `0x880a...311c` | `SHORT` | 3,104,372.60 USD | `1,320.22` | `2425.76` | `2350.40` | `8041.21` | 98,176.56 USD | `+3.16%` | `9X Cross` |
| `777` | `0x29de...3e93` | `LONG` | 3,079,155.00 USD | `1,310.00` | `2352.60` | `2350.40` | `1922.20` | -2,753.82 USD | `-0.09%` | `5X Isolated` |
| `780` | `0x023a...2355` | `LONG` | 3,068,924.68 USD | `1,305.65` | `2341.05` | `2350.40` | `0.000000` | 12,334.38 USD | `+0.40%` | `25X Cross` |
| `813` | `0xc435...c905` | `SHORT` | 2,935,046.40 USD | `1,248.00` | `2704.38` | `2350.40` | `4736.44` | 440,023.95 USD | `+14.99%` | `20X Cross` |
| `821` | `0x4202...aaf5` | `SHORT` | 2,898,155.97 USD | `1,232.10` | `2321.73` | `2350.40` | `2733.52` | -37,531.67 USD | `-1.30%` | `5X Isolated` |
| `833` | `0x7178...0854` | `LONG` | 2,866,099.42 USD | `1,218.63` | `2461.81` | `2350.40` | `1021.02` | -133,946.98 USD | `-4.67%` | `10X Cross` |
| `880` | `0x07fd...689d` | `LONG` | 2,669,932.01 USD | `1,135.90` | `2423.84` | `2350.40` | `0.000000` | -83,311.19 USD | `-3.12%` | `25X Cross` |
| `911` | `0x2f80...f203` | `SHORT` | 2,561,276.58 USD | `1,088.94` | `1984.00` | `2350.40` | `3076.45` | -400,809.39 USD | `-15.65%` | `20X Cross` |
| `926` | `0x6f11...0389` | `SHORT` | 2,536,297.40 USD | `1,079.00` | `2333.39` | `2350.40` | `3199.65` | -18,568.49 USD | `-0.73%` | `25X Cross` |
| `928` | `0x2b61...2f6c` | `SHORT` | 2,531,510.66 USD | `1,076.60` | `2681.75` | `2350.40` | `6396.91` | 355,662.08 USD | `+14.05%` | `10X Cross` |
| `964` | `0x1b2a...f7a6` | `LONG` | 2,411,460.46 USD | `1,025.37` | `2737.51` | `2350.40` | `912.59` | -395,499.48 USD | `-16.40%` | `10X Cross` |
| `965` | `0xb15b...dbae` | `SHORT` | 2,410,931.78 USD | `1,025.14` | `2338.37` | `2350.40` | `2381.04` | -13,758.06 USD | `-0.57%` | `25X Cross` |
| `971` | `0x6749...ce07` | `SHORT` | 2,386,876.79 USD | `1,015.35` | `2318.56` | `2350.40` | `5892.40` | -32,733.43 USD | `-1.37%` | `20X Cross` |
| `977` | `0x001a...fef6` | `SHORT` | 2,368,019.61 USD | `1,007.33` | `2022.19` | `2350.40` | `3025.21` | -331,011.65 USD | `-13.98%` | `10X Cross` |
| `979` | `0x02aa...1806` | `SHORT` | 2,367,188.79 USD | `1,007.10` | `2654.68` | `2350.40` | `3613.65` | 306,343.32 USD | `+12.94%` | `20X Cross` |
| `983` | `0xdb3a...cf3b` | `LONG` | 2,358,157.41 USD | `1,003.22` | `2705.01` | `2350.40` | `0.000000` | -355,549.48 USD | `-15.08%` | `4X Cross` |
| `989` | `0x2828...93a0` | `LONG` | 2,351,800.00 USD | `1,000.00` | `2393.30` | `2350.40` | `2260.02` | -41,509.16 USD | `-1.76%` | `25X Cross` |
| `990` | `0x4044...794c` | `LONG` | 2,351,800.00 USD | `1,000.00` | `2332.68` | `2350.40` | `0.000000` | 19,110.16 USD | `+0.81%` | `25X Cross` |
| `992` | `0x5986...89d9` | `LONG` | 2,351,400.00 USD | `1,000.00` | `2346.34` | `2350.40` | `1193.72` | 5,050.46 USD | `+0.21%` | `25X Cross` |
| `994` | `0x5272...fcd9` | `SHORT` | 2,350,800.00 USD | `1,000.00` | `2241.82` | `2350.40` | `2880.72` | -108,975.51 USD | `-4.64%` | `5X Cross` |
| `995` | `0xdf60...d3c7` | `LONG` | 2,350,200.00 USD | `1,000.00` | `2736.24` | `2350.40` | `2246.05` | -386,042.88 USD | `-16.43%` | `10X Isolated` |
| `996` | `0xfe82...ce65` | `SHORT` | 2,350,200.00 USD | `1,000.00` | `2300.50` | `2350.40` | `2718.39` | -49,692.07 USD | `-2.11%` | `25X Cross` |
| `997` | `0x004e...1bb8` | `SHORT` | 2,350,200.00 USD | `1,000.00` | `2363.71` | `2350.40` | `2423.03` | 13,510.06 USD | `+0.57%` | `25X Cross` |
| `1028` | `0xb002...ed8a` | `SHORT` | 2,264,275.41 USD | `962.78` | `2299.66` | `2350.40` | `4191.55` | -50,197.50 USD | `-2.22%` | `25X Cross` |
| `1033` | `0x2e30...4cb5` | `SHORT` | 2,251,555.20 USD | `956.72` | `2340.06` | `2350.40` | `7151.31` | -12,754.84 USD | `-0.57%` | `2X Cross` |
| `1046` | `0xc8fe...afa4` | `LONG` | 2,200,941.92 USD | `936.37` | `2331.34` | `2350.40` | `2145.78` | 17,937.68 USD | `+0.82%` | `10X Isolated` |
| `1061` | `0x9606...4e5d` | `SHORT` | 2,147,824.74 USD | `913.00` | `2478.70` | `2350.40` | `3840.13` | 115,228.87 USD | `+5.36%` | `20X Cross` |
| `1066` | `0xaeea...bfa7` | `LONG` | 2,136,280.80 USD | `908.75` | `2339.31` | `2350.40` | `2286.69` | 10,438.70 USD | `+0.49%` | `23X Isolated` |
| `1094` | `0x60f7...d1ee` | `LONG` | 2,093,725.00 USD | `890.00` | `2343.49` | `2350.40` | `2265.94` | 8,015.04 USD | `+0.38%` | `25X Cross` |
| `1159` | `0x2577...4897` | `LONG` | 1,988,805.06 USD | `846.12` | `2357.57` | `2350.40` | `0.000000` | -5,989.21 USD | `-0.30%` | `15X Cross` |
| `1180` | `0xcd27...52a8` | `LONG` | 1,967,941.83 USD | `837.21` | `2553.56` | `2350.40` | `1404.20` | -169,922.95 USD | `-8.63%` | `2X Cross` |
| `1234` | `0x3fc5...c0c1` | `SHORT` | 1,889,845.92 USD | `804.26` | `2702.11` | `2350.40` | `4741.95` | 283,355.61 USD | `+14.99%` | `25X Cross` |
| `1235` | `0xf83f...625f` | `SHORT` | 1,889,494.70 USD | `803.05` | `2601.00` | `2350.40` | `6012.51` | 199,241.75 USD | `+10.54%` | `20X Cross` |
| `1245` | `0x7737...bf66` | `SHORT` | 1,880,950.59 USD | `799.79` | `2494.83` | `2350.40` | `25727.04` | 114,395.44 USD | `+6.08%` | `15X Cross` |
| `1246` | `0x834c...dd93` | `SHORT` | 1,880,640.00 USD | `800.00` | `2360.52` | `2350.40` | `2422.53` | 7,777.44 USD | `+0.41%` | `25X Cross` |
| `1247` | `0x04a9...95aa` | `LONG` | 1,880,480.00 USD | `800.00` | `2595.13` | `2350.40` | `1854.38` | -195,626.74 USD | `-10.40%` | `5X Cross` |
| `1268` | `0xbef3...0d3e` | `LONG` | 1,836,739.34 USD | `780.99` | `2332.46` | `2350.40` | `2092.90` | 15,098.09 USD | `+0.82%` | `20X Cross` |
| `1279` | `0x6a41...a3b9` | `LONG` | 1,824,360.44 USD | `776.06` | `2332.17` | `2350.40` | `2095.12` | 14,455.58 USD | `+0.79%` | `20X Cross` |
| `1283` | `0x458d...ab3b` | `LONG` | 1,822,049.99 USD | `774.75` | `2740.41` | `2350.40` | `1887.95` | -301,079.19 USD | `-16.52%` | `3X Isolated` |
| `1325` | `0x4b1c...bc38` | `SHORT` | 1,746,246.07 USD | `742.51` | `2529.31` | `2350.40` | `4404.64` | 131,809.48 USD | `+7.55%` | `10X Cross` |
| `1355` | `0x51a0...3543` | `SHORT` | 1,703,117.36 USD | `724.55` | `2627.71` | `2350.40` | `7736.06` | 200,779.40 USD | `+11.79%` | `20X Cross` |
| `1363` | `0xa189...94d7` | `SHORT` | 1,693,606.60 USD | `719.98` | `2691.84` | `2350.40` | `3051.90` | 244,466.06 USD | `+14.43%` | `25X Cross` |
| `1371` | `0x3ee5...4fab` | `SHORT` | 1,682,430.13 USD | `715.17` | `2759.35` | `2350.40` | `3576.91` | 290,969.84 USD | `+17.29%` | `20X Cross` |
| `1381` | `0x2f93...4404` | `LONG` | 1,664,397.45 USD | `707.47` | `1700.45` | `2350.40` | `1369.58` | 461,371.08 USD | `+27.72%` | `4X Isolated` |
| `1392` | `0x5605...fe0f` | `SHORT` | 1,651,020.46 USD | `702.14` | `2566.90` | `2350.40` | `3023.98` | 151,312.19 USD | `+9.16%` | `20X Cross` |
| `1394` | `0xaa53...9cb7` | `LONG` | 1,645,770.00 USD | `700.00` | `2394.46` | `2350.40` | `1968.66` | -30,352.07 USD | `-1.84%` | `20X Cross` |
| `1446` | `0xdbd1...29dd` | `SHORT` | 1,601,624.91 USD | `680.70` | `3030.57` | `2350.40` | `4080.72` | 461,296.21 USD | `+28.80%` | `6X Cross` |
| `1453` | `0x71e5...be04` | `LONG` | 1,593,059.11 USD | `677.67` | `2727.27` | `2350.40` | `1471.73` | -255,126.49 USD | `-16.01%` | `20X Cross` |
| `1457` | `0x0b23...f37b` | `LONG` | 1,587,937.50 USD | `675.00` | `2238.15` | `2350.40` | `574.83` | 77,180.86 USD | `+4.86%` | `5X Cross` |
| `1482` | `0x0cac...6170` | `SHORT` | 1,558,531.25 USD | `662.50` | `2146.55` | `2350.40` | `2835.36` | -136,436.26 USD | `-8.75%` | `20X Cross` |
| `1489` | `0x0082...1ae3` | `LONG` | 1,552,570.80 USD | `660.00` | `2448.58` | `2350.40` | `2244.93` | -63,497.84 USD | `-4.09%` | `25X Cross` |
| `1503` | `0x7743...e4fe` | `SHORT` | 1,529,132.35 USD | `650.56` | `2325.23` | `2350.40` | `6449.04` | -16,438.21 USD | `-1.08%` | `25X Cross` |
| `1512` | `0xffb2...5ed6` | `SHORT` | 1,507,467.97 USD | `640.77` | `2672.96` | `2350.40` | `2599.99` | 205,280.37 USD | `+13.62%` | `20X Cross` |
| `1525` | `0xb1ec...e86a` | `SHORT` | 1,495,354.68 USD | `636.38` | `2357.26` | `2350.40` | `18562.68` | 4,750.03 USD | `+0.32%` | `25X Cross` |
| `1554` | `0xfce0...f4c0` | `SHORT` | 1,466,831.92 USD | `623.60` | `3129.61` | `2350.40` | `2788.39` | 484,794.66 USD | `+33.05%` | `20X Cross` |
| `1568` | `0x3bca...66f3` | `SHORT` | 1,448,151.56 USD | `616.05` | `2348.07` | `2350.40` | `14807.93` | -1,616.04 USD | `-0.11%` | `25X Cross` |
| `1580` | `0x7663...cb5a` | `SHORT` | 1,443,163.61 USD | `613.54` | `2342.35` | `2350.40` | `3614.00` | -6,043.13 USD | `-0.42%` | `3X Cross` |
| `1604` | `0xad02...eb65` | `LONG` | 1,411,757.78 USD | `600.62` | `2460.69` | `2350.40` | `1079.65` | -66,182.78 USD | `-4.69%` | `5X Cross` |
| `1605` | `0x638f...f5f0` | `LONG` | 1,411,440.00 USD | `600.00` | `4011.50` | `2350.40` | `0.000000` | -995,463.53 USD | `-70.53%` | `25X Cross` |
| `1606` | `0x67c3...609d` | `SHORT` | 1,411,260.00 USD | `600.00` | `2386.55` | `2350.40` | `2560.74` | 20,671.89 USD | `+1.46%` | `25X Cross` |
| `1607` | `0x26e6...6b28` | `LONG` | 1,411,080.00 USD | `600.00` | `1769.78` | `2350.40` | `2005.45` | 349,208.47 USD | `+24.75%` | `20X Cross` |
| `1608` | `0x0deb...0bc5` | `LONG` | 1,410,480.00 USD | `600.00` | `2038.23` | `2350.40` | `1478.66` | 187,541.36 USD | `+13.30%` | `20X Cross` |
| `1609` | `0x0a84...6ddd` | `LONG` | 1,410,480.00 USD | `600.00` | `2222.36` | `2350.40` | `1774.77` | 77,061.66 USD | `+5.46%` | `25X Cross` |
| `1632` | `0x94b6...e5b3` | `SHORT` | 1,380,059.26 USD | `586.71` | `2377.90` | `2350.40` | `2508.81` | 15,078.98 USD | `+1.09%` | `25X Cross` |
| `1671` | `0xfb99...37f3` | `LONG` | 1,329,897.10 USD | `565.34` | `2362.35` | `2350.40` | `1202.73` | -5,639.26 USD | `-0.42%` | `3X Cross` |
| `1688` | `0x844b...7f42` | `SHORT` | 1,319,640.30 USD | `561.00` | `2026.17` | `2350.40` | `2937.86` | -182,956.89 USD | `-13.86%` | `25X Cross` |
| `1705` | `0xabe6...1d99` | `SHORT` | 1,306,998.60 USD | `556.00` | `2484.68` | `2350.40` | `2928.23` | 74,497.29 USD | `+5.70%` | `20X Cross` |
| `1734` | `0xa0fb...96be` | `SHORT` | 1,279,930.32 USD | `544.07` | `2333.07` | `2350.40` | `4030.93` | -10,569.08 USD | `-0.83%` | `3X Cross` |
| `1747` | `0xad21...fb6a` | `LONG` | 1,250,477.91 USD | `531.87` | `2574.89` | `2350.40` | `1677.93` | -119,027.59 USD | `-9.52%` | `7X Cross` |
| `1792` | `0x8923...1bac` | `SHORT` | 1,215,639.82 USD | `517.18` | `2348.15` | `2350.40` | `3220.61` | -1,214.72 USD | `-0.10%` | `25X Cross` |
| `1801` | `0xf910...0a2d` | `LONG` | 1,209,515.86 USD | `514.64` | `2356.76` | `2350.40` | `0.000000` | -3,379.92 USD | `-0.28%` | `5X Cross` |
| `1812` | `0x0c7a...2f50` | `SHORT` | 1,197,286.62 USD | `509.25` | `2122.56` | `2350.40` | `4061.16` | -116,381.19 USD | `-9.72%` | `20X Cross` |
| `1833` | `0x0e1c...ce6d` | `LONG` | 1,175,850.00 USD | `500.00` | `2329.15` | `2350.40` | `1993.20` | 11,273.27 USD | `+0.96%` | `15X Cross` |
| `1834` | `0x89b2...9ca6` | `LONG` | 1,175,795.00 USD | `500.00` | `2484.03` | `2350.40` | `1954.18` | -66,224.35 USD | `-5.63%` | `25X Cross` |
| `1841` | `0x7298...7d6c` | `SHORT` | 1,171,497.71 USD | `498.15` | `3426.75` | `2350.40` | `5422.36` | 535,538.11 USD | `+45.71%` | `20X Cross` |
| `1866` | `0xc10f...23b3` | `LONG` | 1,152,186.00 USD | `490.00` | `2402.16` | `2350.40` | `2082.02` | -24,876.83 USD | `-2.16%` | `25X Cross` |
| `1868` | `0x404c...5f03` | `SHORT` | 1,151,774.21 USD | `489.79` | `2671.94` | `2350.40` | `4108.66` | 156,905.34 USD | `+13.62%` | `20X Cross` |
| `1874` | `0x321f...1c84` | `SHORT` | 1,147,763.42 USD | `488.02` | `2370.09` | `2350.40` | `3007.26` | 8,881.18 USD | `+0.77%` | `10X Cross` |
| `1934` | `0x82c6...fe42` | `LONG` | 1,088,170.00 USD | `462.50` | `2501.38` | `2350.40` | `2054.43` | -68,720.57 USD | `-6.32%` | `5X Isolated` |
| `1952` | `0x617e...0f97` | `SHORT` | 1,076,186.77 USD | `457.85` | `2205.60` | `2350.40` | `3593.39` | -66,342.93 USD | `-6.16%` | `10X Cross` |
| `1981` | `0xae55...2236` | `LONG` | 1,058,625.00 USD | `450.00` | `2510.21` | `2350.40` | `0.000000` | -70,972.50 USD | `-6.70%` | `25X Cross` |
| `1990` | `0xac26...a9c7` | `SHORT` | 1,049,777.15 USD | `446.28` | `2192.58` | `2350.40` | `8716.30` | -71,277.45 USD | `-6.79%` | `20X Cross` |
| `1994` | `0x53f8...ceff` | `LONG` | 1,047,243.24 USD | `445.60` | `2399.81` | `2350.40` | `0.000000` | -22,107.35 USD | `-2.11%` | `20X Cross` |
| `2002` | `0xd8a1...6687` | `LONG` | 1,038,304.59 USD | `441.53` | `2804.24` | `2350.40` | `2150.99` | -199,863.85 USD | `-19.25%` | `20X Cross` |
| `2016` | `0x248e...6be2` | `SHORT` | 1,026,141.79 USD | `436.40` | `2314.49` | `2350.40` | `4363.37` | -16,107.07 USD | `-1.57%` | `20X Cross` |
| `2025` | `0x80f2...0c3a` | `LONG` | 1,021,485.40 USD | `434.55` | `2564.17` | `2350.40` | `916.42` | -92,763.48 USD | `-9.08%` | `5X Cross` |
| `2051` | `0x15c8...045f` | `SHORT` | 1,008,253.18 USD | `428.90` | `1903.23` | `2350.40` | `3079.62` | -191,960.14 USD | `-19.04%` | `25X Cross` |
| `2057` | `0x4e6b...b7d4` | `LONG` | 1,005,480.91 USD | `427.77` | `2744.83` | `2350.40` | `67.37` | -168,684.12 USD | `-16.78%` | `25X Cross` |

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
  * 24H Horizon: Short MP=`2341.17` (Vol: 32,000,000.00 USD, Dist: `+0.44%`) | Long MP=`2284.33` (Vol: 28,700,000.00 USD, Dist: `--2.00%`)
  * 48H Horizon: Short MP=`2341.17` (Vol: 32,000,000.00 USD, Dist: `+0.44%`) | Long MP=`2284.33` (Vol: 30,000,000.00 USD, Dist: `--2.00%`)
  * 3D Horizon: Short MP=`2341.17` (Vol: 32,000,000.00 USD, Dist: `+0.44%`) | Long MP=`2284.33` (Vol: 44,100,000.00 USD, Dist: `--2.00%`)
  * 7D Horizon: Short MP=`2428.28` (Vol: 47,300,000.00 USD, Dist: `+4.18%`) | Long MP=`2284.60` (Vol: 72,300,000.00 USD, Dist: `--1.99%`)
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
| `7D` | `Long Liquidation` | `2068.70` | 2,730,000,000.00 USD | 2,730,000,000.00 USD | 1,890,000.00 USD | 1,910,000.00 USD | 939,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2071.50` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 2,760,000.00 USD | 1,510,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2074.30` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 3,850,000.00 USD | 2,610,000.00 USD | 2,930,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 13,750,000.00 USD | 362,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2077.10` | 2,710,000,000.00 USD | 2,710,000,000.00 USD | 4,430,000.00 USD | 4,120,000.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2079.90` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 3,400,000.00 USD | 3,020,000.00 USD | 2,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2082.70` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 2,420,000.00 USD | 1,860,000.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 1,810,000.00 USD | 348,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2085.50` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 3,840,000.00 USD | 1,860,000.00 USD | 3,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2088.30` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 2,280,000.00 USD | 1,820,000.00 USD | 907,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2091.10` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 4,280,000.00 USD | 952,210.00 USD | 6,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2093.90` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 5,200,000.00 USD | 1,640,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 4,620,000.00 USD | 346,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2096.70` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 1,940,000.00 USD | 3,330,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2099.50` | 2,640,000,000.00 USD | 2,640,000,000.00 USD | 1,880,000.00 USD | 1,520,000.00 USD | 2,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2102.30` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 125,250.00 USD | 688,260.00 USD | 2,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 23,040,000.00 USD | 342,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2105.10` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2107.90` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 2,320,000.00 USD | 356,360.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2110.70` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 2,830,000.00 USD | 2,300,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2113.50` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 1,730,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2114.20` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 1,130,000.00 USD | 1,080,000.00 USD | 532,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 16,720,000.00 USD | 319,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2116.30` | 2,610,000,000.00 USD | 2,610,000,000.00 USD | 1,480,000.00 USD | 2,030,000.00 USD | 2,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2116.80` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 1,070,000.00 USD | 335,670.00 USD | 697,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2119.10` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 3,390,000.00 USD | 935,590.00 USD | 2,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2119.40` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 493,030.00 USD | 256,720.00 USD | 987,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2121.90` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 2,300,000.00 USD | 973,690.00 USD | 1,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2122.00` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 982,960.00 USD | 704,400.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2124.60` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 1,010,000.00 USD | 1,150,000.00 USD | 849,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2124.70` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 2,110,000.00 USD | 983,790.00 USD | 989,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 1,140,000.00 USD | 302,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2127.20` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 258,900.00 USD | 724,120.00 USD | 306,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2127.50` | 2,590,000,000.00 USD | 2,590,000,000.00 USD | 1,080,000.00 USD | 2,620,000.00 USD | 3,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2129.80` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 107,010.00 USD | 472,480.00 USD | 318,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2130.30` | 2,580,000,000.00 USD | 2,580,000,000.00 USD | 2,040,000.00 USD | 2,130,000.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2132.40` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 937,720.00 USD | 336,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2133.10` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 1,930,000.00 USD | 715,940.00 USD | 330,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2135.00` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 187,520.00 USD | 228,740.00 USD | 2,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 15,440,000.00 USD | 301,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2135.90` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 1,370,000.00 USD | 596,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2137.60` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 555,320.00 USD | 501,410.00 USD | 205,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2138.70` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 909,440.00 USD | 1,250,000.00 USD | 78,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2141.50` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 1,750,000.00 USD | 199,980.00 USD | 776,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2142.80` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 295,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2144.30` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 465,960.00 USD | 1,540,000.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 16,180,000.00 USD | 285,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2145.40` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 16,700.00 USD | 210,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2147.10` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 311,920.00 USD | 32,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2148.00` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 251,250.00 USD | 11,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2149.90` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 459,630.00 USD | 482,820.00 USD | 537,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2152.70` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 58,340.00 USD | 681,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 2,580,000.00 USD | 269,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2155.50` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 191,860.00 USD | 454,940.00 USD | 866,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2158.30` | 2,560,000,000.00 USD | 2,560,000,000.00 USD | 738,850.00 USD | 717,210.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2161.10` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 1,490,000.00 USD | 1,350,000.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2163.90` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 36,870.00 USD | 329,690.00 USD | 409,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 1,660,000.00 USD | 266,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2166.70` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 25,540.00 USD | 0.00 USD | 68,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2169.50` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 1,700,000.00 USD | 726,240.00 USD | 810,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2172.30` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 479,540.00 USD | 1,150,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 109,510,000.00 USD | 265,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2185.00` | 113,580,000.00 USD | 155,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2194.70` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 141,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 1,210,000.00 USD | 42,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2197.50` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 2,440,000.00 USD | 3,270,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2200.00` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 201,540.00 USD | 154,560.00 USD | 169,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2200.30` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 3,000,000.00 USD | 3,140,000.00 USD | 3,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2202.60` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 1,140,000.00 USD | 62,930.00 USD | 751,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2203.10` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 3,240,000.00 USD | 624,500.00 USD | 2,720,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 1,160,000.00 USD | 41,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2205.20` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 207,110.00 USD | 95,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2205.90` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 6,050,000.00 USD | 4,010,000.00 USD | 3,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2207.80` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 3,100,000.00 USD | 2,380,000.00 USD | 3,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2208.70` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 10,060,000.00 USD | 6,100,000.00 USD | 4,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2210.40` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 1,610,000.00 USD | 1,180,000.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2211.50` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 7,320,000.00 USD | 7,940,000.00 USD | 7,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2213.00` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 3,000,000.00 USD | 1,970,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2214.30` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 13,980,000.00 USD | 12,380,000.00 USD | 9,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 2,240,000.00 USD | 39,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2215.60` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 6,210,000.00 USD | 4,500,000.00 USD | 5,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2217.10` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 16,020,000.00 USD | 10,300,000.00 USD | 8,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2218.20` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 4,620,000.00 USD | 4,760,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2219.90` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 12,620,000.00 USD | 10,310,000.00 USD | 3,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2220.80` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 3,730,000.00 USD | 3,970,000.00 USD | 533,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2222.70` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 5,480,000.00 USD | 5,400,000.00 USD | 8,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2223.40` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 4,480,000.00 USD | 3,950,000.00 USD | 3,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2225.00` | 1,560,000.00 USD | 37,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2225.50` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 12,980,000.00 USD | 13,620,000.00 USD | 9,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2226.00` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 5,320,000.00 USD | 5,400,000.00 USD | 2,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2228.30` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 7,790,000.00 USD | 5,070,000.00 USD | 7,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2228.60` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 3,180,000.00 USD | 1,360,000.00 USD | 664,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2231.10` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 9,590,000.00 USD | 3,450,000.00 USD | 17,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2231.20` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 3,000,000.00 USD | 2,830,000.00 USD | 2,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2233.80` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 7,220,000.00 USD | 3,760,000.00 USD | 2,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2233.90` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 18,230,000.00 USD | 10,390,000.00 USD | 6,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2235.00` | 789,970.00 USD | 36,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2236.40` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 2,550,000.00 USD | 2,090,000.00 USD | 3,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2236.70` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 7,440,000.00 USD | 11,700,000.00 USD | 5,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2239.00` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 1,030,000.00 USD | 2,370,000.00 USD | 855,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2239.50` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 6,630,000.00 USD | 6,820,000.00 USD | 6,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2241.60` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 321,680.00 USD | 145,710.00 USD | 284,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2242.30` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 3,580,000.00 USD | 2,780,000.00 USD | 7,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2244.20` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 2,480,000.00 USD | 423,680.00 USD | 238,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2245.00` | 4,680,000.00 USD | 35,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2245.10` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 16,710,000.00 USD | 13,060,000.00 USD | 11,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2246.80` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 1,570,000.00 USD | 914,360.00 USD | 1,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2247.90` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 13,600,000.00 USD | 6,160,000.00 USD | 9,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2249.40` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 3,680,000.00 USD | 1,540,000.00 USD | 2,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2250.70` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 10,570,000.00 USD | 10,360,000.00 USD | 8,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2252.00` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 4,480,000.00 USD | 6,430,000.00 USD | 2,750,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2253.50` | 2,070,000,000.00 USD | 2,070,000,000.00 USD | 24,760,000.00 USD | 21,020,000.00 USD | 19,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2254.60` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 8,120,000.00 USD | 3,660,000.00 USD | 7,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2255.00` | 13,270,000.00 USD | 30,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2256.30` | 2,000,000,000.00 USD | 2,000,000,000.00 USD | 31,260,000.00 USD | 19,100,000.00 USD | 18,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2257.20` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 5,380,000.00 USD | 5,380,000.00 USD | 2,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2259.10` | 1,940,000,000.00 USD | 1,940,000,000.00 USD | 21,420,000.00 USD | 19,400,000.00 USD | 22,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2259.80` | 1,030,000,000.00 USD | 1,030,000,000.00 USD | 13,220,000.00 USD | 6,980,000.00 USD | 8,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2261.90` | 1,870,000,000.00 USD | 1,870,000,000.00 USD | 48,180,000.00 USD | 29,390,000.00 USD | 21,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2262.40` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 15,720,000.00 USD | 15,880,000.00 USD | 13,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2264.70` | 1,770,000,000.00 USD | 1,770,000,000.00 USD | 30,320,000.00 USD | 28,050,000.00 USD | 19,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2265.00` | 956,060,000.00 USD | 956,060,000.00 USD | 14,360,000.00 USD | 11,480,000.00 USD | 6,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2265.00` | 3,530,000.00 USD | 17,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2267.50` | 1,700,000,000.00 USD | 1,700,000,000.00 USD | 40,120,000.00 USD | 40,100,000.00 USD | 31,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2267.60` | 924,010,000.00 USD | 924,010,000.00 USD | 4,850,000.00 USD | 7,350,000.00 USD | 3,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2270.20` | 908,010,000.00 USD | 908,010,000.00 USD | 14,410,000.00 USD | 11,370,000.00 USD | 8,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2270.30` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 39,480,000.00 USD | 27,490,000.00 USD | 39,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2272.80` | 873,920,000.00 USD | 873,920,000.00 USD | 15,080,000.00 USD | 12,460,000.00 USD | 9,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2273.10` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 33,160,000.00 USD | 25,760,000.00 USD | 19,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2275.00` | 4,430,000.00 USD | 13,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2275.40` | 836,940,000.00 USD | 836,940,000.00 USD | 8,710,000.00 USD | 13,510,000.00 USD | 4,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2275.90` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 48,240,000.00 USD | 42,710,000.00 USD | 44,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2278.00` | 810,240,000.00 USD | 810,240,000.00 USD | 17,980,000.00 USD | 8,710,000.00 USD | 18,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2278.70` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 74,310,000.00 USD | 34,750,000.00 USD | 42,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2280.60` | 765,310,000.00 USD | 765,310,000.00 USD | 25,850,000.00 USD | 15,120,000.00 USD | 7,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2281.50` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 56,100,000.00 USD | 59,940,000.00 USD | 49,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2283.20` | 716,450,000.00 USD | 716,450,000.00 USD | 23,970,000.00 USD | 18,060,000.00 USD | 28,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2284.30` | 947,650,000.00 USD | 947,650,000.00 USD | 89,220,000.00 USD | 69,840,000.00 USD | 44,200,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2285.00` | 5,990,000.00 USD | 9,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2285.80` | 646,000,000.00 USD | 646,000,000.00 USD | 26,180,000.00 USD | 26,480,000.00 USD | 12,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2287.10` | 744,380,000.00 USD | 744,380,000.00 USD | 58,910,000.00 USD | 53,380,000.00 USD | 45,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2288.40` | 580,550,000.00 USD | 580,550,000.00 USD | 17,180,000.00 USD | 15,670,000.00 USD | 3,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2289.90` | 586,910,000.00 USD | 586,910,000.00 USD | 48,430,000.00 USD | 34,490,000.00 USD | 22,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2291.00` | 544,690,000.00 USD | 544,690,000.00 USD | 14,820,000.00 USD | 12,810,000.00 USD | 3,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2292.70` | 481,810,000.00 USD | 481,810,000.00 USD | 38,110,000.00 USD | 20,900,000.00 USD | 44,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2293.60` | 513,660,000.00 USD | 513,660,000.00 USD | 16,600,000.00 USD | 17,360,000.00 USD | 14,330,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2295.00` | 1,460,000.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2295.50` | 378,730,000.00 USD | 378,730,000.00 USD | 17,510,000.00 USD | 8,110,000.00 USD | 7,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2296.20` | 465,370,000.00 USD | 465,370,000.00 USD | 22,580,000.00 USD | 10,920,000.00 USD | 7,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2298.30` | 345,890,000.00 USD | 345,890,000.00 USD | 2,090,000.00 USD | 5,410,000.00 USD | 301,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2298.80` | 424,260,000.00 USD | 424,260,000.00 USD | 10,240,000.00 USD | 8,320,000.00 USD | 3,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2301.10` | 338,090,000.00 USD | 338,090,000.00 USD | 11,790,000.00 USD | 2,200,000.00 USD | 7,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2301.40` | 402,160,000.00 USD | 402,160,000.00 USD | 16,890,000.00 USD | 11,600,000.00 USD | 12,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2303.90` | 316,510,000.00 USD | 316,510,000.00 USD | 31,030,000.00 USD | 17,020,000.00 USD | 13,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2304.00` | 361,320,000.00 USD | 361,320,000.00 USD | 28,790,000.00 USD | 16,100,000.00 USD | 13,840,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2305.00` | 280,710.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2306.60` | 302,590,000.00 USD | 302,590,000.00 USD | 2,760,000.00 USD | 4,390,000.00 USD | 14,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2306.70` | 255,220,000.00 USD | 255,220,000.00 USD | 0.00 USD | 3,740,000.00 USD | 10,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2309.20` | 281,320,000.00 USD | 281,320,000.00 USD | 3,370,000.00 USD | 1,990,000.00 USD | 743,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2309.50` | 240,590,000.00 USD | 240,590,000.00 USD | 282,530.00 USD | 300,580.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2311.80` | 275,220,000.00 USD | 275,220,000.00 USD | 7,740,000.00 USD | 5,840,000.00 USD | 5,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2312.30` | 238,510,000.00 USD | 238,510,000.00 USD | 1,740,000.00 USD | 128,300.00 USD | 2,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2314.40` | 256,550,000.00 USD | 256,550,000.00 USD | 6,800,000.00 USD | 3,480,000.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2315.00` | 267,770.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2315.10` | 234,130,000.00 USD | 234,130,000.00 USD | 4,300,000.00 USD | 4,100,000.00 USD | 117,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2317.00` | 244,630,000.00 USD | 244,630,000.00 USD | 6,200,000.00 USD | 2,460,000.00 USD | 2,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2317.90` | 225,610,000.00 USD | 225,610,000.00 USD | 817,040.00 USD | 3,010,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2319.60` | 233,220,000.00 USD | 233,220,000.00 USD | 5,480,000.00 USD | 3,000,000.00 USD | 795,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2320.70` | 221,790,000.00 USD | 221,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2322.20` | 223,940,000.00 USD | 223,940,000.00 USD | 4,760,000.00 USD | 1,780,000.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2323.50` | 219,000,000.00 USD | 219,000,000.00 USD | 4,070,000.00 USD | 1,900,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2324.80` | 215,740,000.00 USD | 215,740,000.00 USD | 4,120,000.00 USD | 2,830,000.00 USD | 2,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2325.00` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2326.30` | 213,020,000.00 USD | 213,020,000.00 USD | 0.00 USD | 0.00 USD | 75,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2327.40` | 206,530,000.00 USD | 206,530,000.00 USD | 0.00 USD | 3,130,000.00 USD | 3,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2329.10` | 212,950,000.00 USD | 212,950,000.00 USD | 0.00 USD | 0.00 USD | 4,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2330.00` | 200,030,000.00 USD | 200,030,000.00 USD | 4,080,000.00 USD | 1,150,000.00 USD | 3,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2331.90` | 208,080,000.00 USD | 208,080,000.00 USD | 29,230,000.00 USD | 1,090,000.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2332.60` | 191,770,000.00 USD | 191,770,000.00 USD | 22,980,000.00 USD | 2,290,000.00 USD | 107,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2334.70` | 174,940,000.00 USD | 174,940,000.00 USD | 7,260,000.00 USD | 18,420,000.00 USD | 8,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2335.20` | 166,390,000.00 USD | 166,390,000.00 USD | 25,380,000.00 USD | 25,170,000.00 USD | 19,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2337.50` | 140,330,000.00 USD | 140,330,000.00 USD | 20,380,000.00 USD | 18,560,000.00 USD | 13,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2337.80` | 95,930,000.00 USD | 95,930,000.00 USD | 6,510,000.00 USD | 23,080,000.00 USD | 10,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2340.30` | 87,820,000.00 USD | 87,820,000.00 USD | 1,630,000.00 USD | 10,010,000.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2340.40` | 55,440,000.00 USD | 55,440,000.00 USD | 5,620,000.00 USD | 28,460,000.00 USD | 2,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2343.00` | 18,850,000.00 USD | 18,850,000.00 USD | 1,880,000.00 USD | 764,610.00 USD | 3,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2343.10` | 72,800,000.00 USD | 72,800,000.00 USD | 0.00 USD | 5,540,000.00 USD | 3,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2345.60` | 13,030,000.00 USD | 13,030,000.00 USD | 963,370.00 USD | 1,770,000.00 USD | 8,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2345.90` | 63,410,000.00 USD | 63,410,000.00 USD | 0.00 USD | 8,310,000.00 USD | 12,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2348.20` | 1,310,000.00 USD | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2348.70` | 42,270,000.00 USD | 42,270,000.00 USD | 285,680.00 USD | 7,340,000.00 USD | 10,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2350.80` | 32,810,000.00 USD | 32,810,000.00 USD | 30,280,000.00 USD | 2,510,000.00 USD | 23,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2351.50` | 23,900,000.00 USD | 23,900,000.00 USD | 782,590.00 USD | 17,440,000.00 USD | 5,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2353.40` | 40,220,000.00 USD | 40,220,000.00 USD | 3,700,000.00 USD | 3,610,000.00 USD | 107,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2354.30` | 47,370,000.00 USD | 47,370,000.00 USD | 12,110,000.00 USD | 35,020,000.00 USD | 237,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 35,020.00 USD | 35,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2356.00` | 55,340,000.00 USD | 55,340,000.00 USD | 318,080.00 USD | 13,480,000.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2357.10` | 60,670,000.00 USD | 60,670,000.00 USD | 7,900,000.00 USD | 5,400,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2358.60` | 55,460,000.00 USD | 55,460,000.00 USD | 0.00 USD | 0.00 USD | 114,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2359.90` | 62,880,000.00 USD | 62,880,000.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2361.20` | 57,610,000.00 USD | 57,610,000.00 USD | 2,040,000.00 USD | 0.00 USD | 110,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2362.70` | 65,040,000.00 USD | 65,040,000.00 USD | 467,570.00 USD | 0.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2363.80` | 60,520,000.00 USD | 60,520,000.00 USD | 742,460.00 USD | 1,840,000.00 USD | 324,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 153.25 USD | 35,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2365.50` | 73,040,000.00 USD | 73,040,000.00 USD | 6,340,000.00 USD | 0.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2366.40` | 60,850,000.00 USD | 60,850,000.00 USD | 122,070.00 USD | 0.00 USD | 211,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2368.30` | 83,010,000.00 USD | 83,010,000.00 USD | 9,590,000.00 USD | 0.00 USD | 370,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2369.00` | 79,000,000.00 USD | 79,000,000.00 USD | 13,760,000.00 USD | 3,260,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2371.10` | 144,800,000.00 USD | 144,800,000.00 USD | 16,760,000.00 USD | 0.00 USD | 45,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2371.60` | 113,190,000.00 USD | 113,190,000.00 USD | 11,360,000.00 USD | 13,360,000.00 USD | 9,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2373.90` | 167,320,000.00 USD | 167,320,000.00 USD | 15,830,000.00 USD | 0.00 USD | 6,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2374.20` | 128,410,000.00 USD | 128,410,000.00 USD | 13,920,000.00 USD | 349,710.00 USD | 945,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 14,790.00 USD | 49,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2376.70` | 203,580,000.00 USD | 203,580,000.00 USD | 8,280,000.00 USD | 5,950,000.00 USD | 22,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2376.80` | 155,240,000.00 USD | 155,240,000.00 USD | 9,620,000.00 USD | 5,340,000.00 USD | 11,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2379.40` | 185,610,000.00 USD | 185,610,000.00 USD | 6,610,000.00 USD | 11,890,000.00 USD | 11,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2379.50` | 230,900,000.00 USD | 230,900,000.00 USD | 7,180,000.00 USD | 2,580,000.00 USD | 17,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2382.00` | 230,210,000.00 USD | 230,210,000.00 USD | 18,560,000.00 USD | 11,220,000.00 USD | 14,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2382.30` | 272,240,000.00 USD | 272,240,000.00 USD | 7,910,000.00 USD | 12,120,000.00 USD | 21,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2384.60` | 275,650,000.00 USD | 275,650,000.00 USD | 18,560,000.00 USD | 17,070,000.00 USD | 9,810,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 3,380,000.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2385.10` | 358,990,000.00 USD | 358,990,000.00 USD | 14,990,000.00 USD | 28,990,000.00 USD | 42,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2387.20` | 305,860,000.00 USD | 305,860,000.00 USD | 12,110,000.00 USD | 11,050,000.00 USD | 7,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2387.90` | 439,130,000.00 USD | 439,130,000.00 USD | 4,870,000.00 USD | 32,720,000.00 USD | 42,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2389.80` | 331,290,000.00 USD | 331,290,000.00 USD | 8,210,000.00 USD | 11,220,000.00 USD | 5,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2390.70` | 538,810,000.00 USD | 538,810,000.00 USD | 5,470,000.00 USD | 45,700,000.00 USD | 48,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2392.40` | 360,770,000.00 USD | 360,770,000.00 USD | 9,370,000.00 USD | 11,000,000.00 USD | 9,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2393.50` | 637,280,000.00 USD | 637,280,000.00 USD | 43,890,000.00 USD | 22,890,000.00 USD | 31,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2395.00` | 386,830,000.00 USD | 386,830,000.00 USD | 10,550,000.00 USD | 13,400,000.00 USD | 2,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 4,430,000.00 USD | 7,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2396.30` | 721,290,000.00 USD | 721,290,000.00 USD | 29,820,000.00 USD | 32,850,000.00 USD | 21,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2397.60` | 410,130,000.00 USD | 410,130,000.00 USD | 6,340,000.00 USD | 9,590,000.00 USD | 7,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2399.10` | 808,890,000.00 USD | 808,890,000.00 USD | 37,420,000.00 USD | 31,200,000.00 USD | 18,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2400.20` | 447,310,000.00 USD | 447,310,000.00 USD | 17,230,000.00 USD | 8,470,000.00 USD | 11,470,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2401.90` | 919,670,000.00 USD | 919,670,000.00 USD | 53,530,000.00 USD | 24,490,000.00 USD | 32,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2402.80` | 476,150,000.00 USD | 476,150,000.00 USD | 8,970,000.00 USD | 11,160,000.00 USD | 8,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2404.70` | 997,410,000.00 USD | 997,410,000.00 USD | 36,370,000.00 USD | 25,840,000.00 USD | 15,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 11,200,000.00 USD | 19,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2405.40` | 507,700,000.00 USD | 507,700,000.00 USD | 13,610,000.00 USD | 9,110,000.00 USD | 8,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2407.50` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 22,760,000.00 USD | 29,510,000.00 USD | 18,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2408.00` | 544,540,000.00 USD | 544,540,000.00 USD | 14,360,000.00 USD | 12,120,000.00 USD | 10,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2410.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 26,620,000.00 USD | 26,620,000.00 USD | 23,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2410.60` | 568,350,000.00 USD | 568,350,000.00 USD | 9,470,000.00 USD | 9,130,000.00 USD | 5,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2413.10` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 13,360,000.00 USD | 15,180,000.00 USD | 13,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2413.20` | 585,660,000.00 USD | 585,660,000.00 USD | 8,240,000.00 USD | 5,620,000.00 USD | 3,450,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 666,630.00 USD | 19,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2415.80` | 598,350,000.00 USD | 598,350,000.00 USD | 3,180,000.00 USD | 5,730,000.00 USD | 3,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2415.90` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 28,030,000.00 USD | 17,450,000.00 USD | 32,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2418.40` | 612,330,000.00 USD | 612,330,000.00 USD | 5,720,000.00 USD | 5,340,000.00 USD | 2,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2418.70` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 28,840,000.00 USD | 18,500,000.00 USD | 12,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2421.00` | 625,960,000.00 USD | 625,960,000.00 USD | 5,930,000.00 USD | 5,130,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2421.50` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 23,440,000.00 USD | 25,120,000.00 USD | 18,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2423.60` | 640,620,000.00 USD | 640,620,000.00 USD | 4,620,000.00 USD | 4,540,000.00 USD | 5,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.30` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 25,250,000.00 USD | 29,620,000.00 USD | 33,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 3,250,000.00 USD | 22,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2426.20` | 643,370,000.00 USD | 643,370,000.00 USD | 516,070.00 USD | 1,960,000.00 USD | 271,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2427.10` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 24,580,000.00 USD | 22,020,000.00 USD | 23,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2428.80` | 645,840,000.00 USD | 645,840,000.00 USD | 2,190,000.00 USD | 12,140.00 USD | 270,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2429.90` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 6,160,000.00 USD | 14,060,000.00 USD | 8,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2431.40` | 650,220,000.00 USD | 650,220,000.00 USD | 2,140,000.00 USD | 943,730.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2432.70` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 17,740,000.00 USD | 13,220,000.00 USD | 6,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2434.00` | 653,470,000.00 USD | 653,470,000.00 USD | 2,220,000.00 USD | 98,290.00 USD | 939,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 8,030,000.00 USD | 31,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2435.50` | 1,670,000,000.00 USD | 1,670,000,000.00 USD | 22,360,000.00 USD | 14,140,000.00 USD | 15,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2436.60` | 657,380,000.00 USD | 657,380,000.00 USD | 1,580,000.00 USD | 1,540,000.00 USD | 791,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2438.30` | 1,730,000,000.00 USD | 1,730,000,000.00 USD | 17,900,000.00 USD | 23,900,000.00 USD | 15,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2439.20` | 661,250,000.00 USD | 661,250,000.00 USD | 1,340,000.00 USD | 1,340,000.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2441.10` | 1,760,000,000.00 USD | 1,760,000,000.00 USD | 17,250,000.00 USD | 6,990,000.00 USD | 14,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2441.80` | 669,720,000.00 USD | 669,720,000.00 USD | 4,350,000.00 USD | 3,360,000.00 USD | 759,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2443.90` | 1,790,000,000.00 USD | 1,790,000,000.00 USD | 6,650,000.00 USD | 13,590,000.00 USD | 7,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2444.40` | 674,420,000.00 USD | 674,420,000.00 USD | 1,510,000.00 USD | 1,650,000.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 748,180.00 USD | 31,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2446.70` | 1,830,000,000.00 USD | 1,830,000,000.00 USD | 10,910,000.00 USD | 7,020,000.00 USD | 18,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2447.00` | 680,230,000.00 USD | 680,230,000.00 USD | 3,140,000.00 USD | 642,690.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2449.50` | 1,870,000,000.00 USD | 1,870,000,000.00 USD | 15,780,000.00 USD | 9,650,000.00 USD | 14,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2449.60` | 688,050,000.00 USD | 688,050,000.00 USD | 2,290,000.00 USD | 2,280,000.00 USD | 3,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2452.20` | 699,090,000.00 USD | 699,090,000.00 USD | 3,620,000.00 USD | 3,170,000.00 USD | 4,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2452.30` | 1,900,000,000.00 USD | 1,900,000,000.00 USD | 10,050,000.00 USD | 9,630,000.00 USD | 7,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2454.80` | 709,450,000.00 USD | 709,450,000.00 USD | 4,190,000.00 USD | 3,920,000.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 108,990.00 USD | 31,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2455.10` | 1,910,000,000.00 USD | 1,910,000,000.00 USD | 5,550,000.00 USD | 5,830,000.00 USD | 3,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2457.40` | 716,110,000.00 USD | 716,110,000.00 USD | 2,140,000.00 USD | 2,260,000.00 USD | 2,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2457.90` | 1,950,000,000.00 USD | 1,950,000,000.00 USD | 12,470,000.00 USD | 11,200,000.00 USD | 13,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2460.00` | 721,780,000.00 USD | 721,780,000.00 USD | 2,370,000.00 USD | 1,970,000.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2460.70` | 1,970,000,000.00 USD | 1,970,000,000.00 USD | 7,010,000.00 USD | 10,640,000.00 USD | 5,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2462.60` | 725,110,000.00 USD | 725,110,000.00 USD | 174,920.00 USD | 2,050,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2463.50` | 2,000,000,000.00 USD | 2,000,000,000.00 USD | 9,490,000.00 USD | 9,600,000.00 USD | 8,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 296,600.00 USD | 32,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2465.20` | 727,180,000.00 USD | 727,180,000.00 USD | 820,990.00 USD | 1,240,000.00 USD | 5,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2466.30` | 2,010,000,000.00 USD | 2,010,000,000.00 USD | 5,400,000.00 USD | 2,080,000.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2467.80` | 727,560,000.00 USD | 727,560,000.00 USD | 0.00 USD | 370,410.00 USD | 7,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2469.10` | 2,020,000,000.00 USD | 2,020,000,000.00 USD | 2,770,000.00 USD | 3,570,000.00 USD | 408,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2470.40` | 731,610,000.00 USD | 731,610,000.00 USD | 1,390,000.00 USD | 1,510,000.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2471.90` | 2,020,000,000.00 USD | 2,020,000,000.00 USD | 3,090,000.00 USD | 2,760,000.00 USD | 814,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2473.00` | 731,850,000.00 USD | 731,850,000.00 USD | 0.00 USD | 232,740.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2474.70` | 2,030,000,000.00 USD | 2,030,000,000.00 USD | 5,400,000.00 USD | 866,790.00 USD | 1,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 444,190.00 USD | 32,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2475.60` | 732,590,000.00 USD | 732,590,000.00 USD | 738,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2477.50` | 2,040,000,000.00 USD | 2,040,000,000.00 USD | 790,860.00 USD | 3,880,000.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2478.20` | 732,640,000.00 USD | 732,640,000.00 USD | 0.00 USD | 41,760.00 USD | 7,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2480.30` | 2,040,000,000.00 USD | 2,040,000,000.00 USD | 2,300,000.00 USD | 1,740,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2480.80` | 733,180,000.00 USD | 733,180,000.00 USD | 0.00 USD | 27,720.00 USD | 518,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2483.10` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 2,010,000.00 USD | 1,330,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2483.40` | 733,810,000.00 USD | 733,810,000.00 USD | 628,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 528,130.00 USD | 33,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2485.90` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 586,480.00 USD | 1,560,000.00 USD | 77,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2488.70` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 1,710,000.00 USD | 842,740.00 USD | 2,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2491.50` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 1,660,000.00 USD | 2,550,000.00 USD | 672,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2494.30` | 2,070,000,000.00 USD | 2,070,000,000.00 USD | 2,380,000.00 USD | 2,730,000.00 USD | 5,000,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 939,880.00 USD | 34,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2497.10` | 2,080,000,000.00 USD | 2,080,000,000.00 USD | 3,640,000.00 USD | 3,570,000.00 USD | 6,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2499.90` | 2,090,000,000.00 USD | 2,090,000,000.00 USD | 1,110,000.00 USD | 2,430,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2502.70` | 2,090,000,000.00 USD | 2,090,000,000.00 USD | 110,450.00 USD | 1,430,000.00 USD | 170,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 217,400.00 USD | 34,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2505.50` | 2,090,000,000.00 USD | 2,090,000,000.00 USD | 3,200,000.00 USD | 2,320,000.00 USD | 59,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2508.30` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 1,150,000.00 USD | 1,270,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2511.10` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 2,560,000.00 USD | 3,230,000.00 USD | 2,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2513.90` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 776,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 1,670,000.00 USD | 35,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2516.70` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 97,050.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2519.50` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2522.30` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 1,050,000.00 USD | 0.00 USD | 945,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2522.40` | 734,040,000.00 USD | 734,040,000.00 USD | 80,610.00 USD | 61,830.00 USD | 90,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2525.00` | 734,520,000.00 USD | 734,520,000.00 USD | 421,540.00 USD | 0.00 USD | 53,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 1,000,000.00 USD | 36,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2525.10` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 307,040.00 USD | 224,130.00 USD | 178,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2527.60` | 735,250,000.00 USD | 735,250,000.00 USD | 0.00 USD | 703,360.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2527.90` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 1,520,000.00 USD | 871,200.00 USD | 749,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2530.20` | 736,680,000.00 USD | 736,680,000.00 USD | 995,550.00 USD | 0.00 USD | 437,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2530.70` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 2,140,000.00 USD | 1,930,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2532.80` | 737,050,000.00 USD | 737,050,000.00 USD | 359,430.00 USD | 0.00 USD | 8,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2533.50` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 2,620,000.00 USD | 1,770,000.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2535.00` | 941,310.00 USD | 37,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2535.40` | 737,820,000.00 USD | 737,820,000.00 USD | 229,190.00 USD | 41,990.00 USD | 501,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2536.30` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 2,810,000.00 USD | 2,460,000.00 USD | 2,740,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2538.00` | 742,850,000.00 USD | 742,850,000.00 USD | 2,030,000.00 USD | 996,850.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2539.10` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 3,530,000.00 USD | 3,180,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2540.60` | 745,250,000.00 USD | 745,250,000.00 USD | 1,150,000.00 USD | 1,010,000.00 USD | 237,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2541.90` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 3,400,000.00 USD | 2,740,000.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2543.20` | 747,420,000.00 USD | 747,420,000.00 USD | 1,090,000.00 USD | 1,070,000.00 USD | 19,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2544.70` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 2,170,000.00 USD | 1,830,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2545.00` | 6,810,000.00 USD | 44,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2545.80` | 749,360,000.00 USD | 749,360,000.00 USD | 648,140.00 USD | 1,180,000.00 USD | 111,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2547.50` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 2,380,000.00 USD | 938,680.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2548.40` | 752,270,000.00 USD | 752,270,000.00 USD | 1,310,000.00 USD | 797,730.00 USD | 803,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2550.30` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 2,860,000.00 USD | 2,690,000.00 USD | 1,800,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2551.00` | 755,320,000.00 USD | 755,320,000.00 USD | 1,460,000.00 USD | 1,120,000.00 USD | 460,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2553.10` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 2,120,000.00 USD | 788,360.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2553.60` | 756,290,000.00 USD | 756,290,000.00 USD | 669,670.00 USD | 220,540.00 USD | 89,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2555.00` | 316,850.00 USD | 45,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2555.90` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 3,290,000.00 USD | 255,750.00 USD | 5,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2556.20` | 758,140,000.00 USD | 758,140,000.00 USD | 738,200.00 USD | 462,600.00 USD | 646,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2558.70` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 3,850,000.00 USD | 1,200,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2558.80` | 760,330,000.00 USD | 760,330,000.00 USD | 1,250,000.00 USD | 475,980.00 USD | 465,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2561.40` | 764,030,000.00 USD | 764,030,000.00 USD | 1,190,000.00 USD | 1,190,000.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2561.50` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 2,780,000.00 USD | 2,030,000.00 USD | 426,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2564.00` | 765,380,000.00 USD | 765,380,000.00 USD | 365,900.00 USD | 674,520.00 USD | 309,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2564.30` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 1,800,000.00 USD | 2,150,000.00 USD | 1,460,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2565.00` | 1,770,000.00 USD | 46,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2566.60` | 765,620,000.00 USD | 765,620,000.00 USD | 121,690.00 USD | 14,540.00 USD | 109,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2567.10` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 575,630.00 USD | 1,510,000.00 USD | 2,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2569.20` | 765,880,000.00 USD | 765,880,000.00 USD | 162,270.00 USD | 0.00 USD | 98,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2569.90` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 125,250.00 USD | 290,680.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2571.80` | 767,020,000.00 USD | 767,020,000.00 USD | 782,640.00 USD | 344,090.00 USD | 10,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2572.70` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 2,000,000.00 USD | 890,480.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2574.40` | 767,800,000.00 USD | 767,800,000.00 USD | 384,300.00 USD | 17,140.00 USD | 375,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2575.00` | 11,780,000.00 USD | 58,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2575.50` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 2,180,000.00 USD | 440,740.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2577.00` | 768,210,000.00 USD | 768,210,000.00 USD | 163,580.00 USD | 221,850.00 USD | 28,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2578.30` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 734,040.00 USD | 1,480,000.00 USD | 1,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2579.60` | 769,540,000.00 USD | 769,540,000.00 USD | 344,810.00 USD | 301,720.00 USD | 685,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2581.10` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 3,270,000.00 USD | 864,580.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2582.20` | 772,210,000.00 USD | 772,210,000.00 USD | 1,510,000.00 USD | 927,000.00 USD | 234,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2583.90` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 740,840.00 USD | 1,260,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2584.80` | 773,210,000.00 USD | 773,210,000.00 USD | 287,140.00 USD | 153,810.00 USD | 554,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2585.00` | 34,400,000.00 USD | 92,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2586.70` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 1,900,000.00 USD | 2,190,000.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2587.40` | 775,050,000.00 USD | 775,050,000.00 USD | 1,070,000.00 USD | 337,700.00 USD | 439,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2589.50` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 2,840,000.00 USD | 446,810.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2590.00` | 776,370,000.00 USD | 776,370,000.00 USD | 445,920.00 USD | 97,410.00 USD | 774,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2592.30` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 2,340,000.00 USD | 1,280,000.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2592.60` | 779,090,000.00 USD | 779,090,000.00 USD | 1,020,000.00 USD | 787,380.00 USD | 908,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2595.00` | 526,600.00 USD | 93,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2595.10` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 452,020.00 USD | 569,790.00 USD | 752,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2595.20` | 781,840,000.00 USD | 781,840,000.00 USD | 898,410.00 USD | 853,630.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2597.80` | 783,230,000.00 USD | 783,230,000.00 USD | 118,170.00 USD | 927,690.00 USD | 339,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2597.90` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 2,280,000.00 USD | 1,630,000.00 USD | 2,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2600.40` | 784,510,000.00 USD | 784,510,000.00 USD | 365,910.00 USD | 623,840.00 USD | 295,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2600.70` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 496,060.00 USD | 1,960,000.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2603.00` | 784,850,000.00 USD | 784,850,000.00 USD | 0.00 USD | 18,610.00 USD | 318,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2603.50` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 2,040,000.00 USD | 1,580,000.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2605.00` | 2,280,000.00 USD | 95,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2605.60` | 785,810,000.00 USD | 785,810,000.00 USD | 0.00 USD | 625,720.00 USD | 336,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2606.30` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 1,480,000.00 USD | 229,360.00 USD | 342,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2608.20` | 786,490,000.00 USD | 786,490,000.00 USD | 187,520.00 USD | 497,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2609.10` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2610.80` | 786,790,000.00 USD | 786,790,000.00 USD | 0.00 USD | 294,600.00 USD | 2,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2611.90` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 724,220.00 USD | 608,060.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2613.40` | 787,800,000.00 USD | 787,800,000.00 USD | 555,320.00 USD | 250,240.00 USD | 205,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2614.70` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 1,110,000.00 USD | 1,000,000.00 USD | 409,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2615.00` | 1,400,000.00 USD | 97,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2617.50` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 1,550,000.00 USD | 209,240.00 USD | 402,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2618.60` | 788,100,000.00 USD | 788,100,000.00 USD | 295,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2620.30` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 47,360.00 USD | 1,120,000.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2623.10` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 631,440.00 USD | 410,460.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `7D` | `2068.70` | 2,730,000,000.00 USD | 0.00 USD | 2,730,000,000.00 USD | 1,890,000.00 USD | 1,910,000.00 USD | 939,150.00 USD |
| `7D` | `2071.50` | 2,720,000,000.00 USD | 0.00 USD | 2,720,000,000.00 USD | 2,760,000.00 USD | 1,510,000.00 USD | 1,220,000.00 USD |
| `7D` | `2074.30` | 2,720,000,000.00 USD | 0.00 USD | 2,720,000,000.00 USD | 3,850,000.00 USD | 2,610,000.00 USD | 2,930,000.00 USD |
| `7D` | `2077.10` | 2,710,000,000.00 USD | 0.00 USD | 2,710,000,000.00 USD | 4,430,000.00 USD | 4,120,000.00 USD | 2,000,000.00 USD |
| `7D` | `2079.90` | 2,700,000,000.00 USD | 0.00 USD | 2,700,000,000.00 USD | 3,400,000.00 USD | 3,020,000.00 USD | 2,510,000.00 USD |
| `7D` | `2082.70` | 2,690,000,000.00 USD | 0.00 USD | 2,690,000,000.00 USD | 2,420,000.00 USD | 1,860,000.00 USD | 1,910,000.00 USD |
| `7D` | `2085.50` | 2,680,000,000.00 USD | 0.00 USD | 2,680,000,000.00 USD | 3,840,000.00 USD | 1,860,000.00 USD | 3,120,000.00 USD |
| `7D` | `2088.30` | 2,670,000,000.00 USD | 0.00 USD | 2,670,000,000.00 USD | 2,280,000.00 USD | 1,820,000.00 USD | 907,940.00 USD |
| `7D` | `2091.10` | 2,670,000,000.00 USD | 0.00 USD | 2,670,000,000.00 USD | 4,280,000.00 USD | 952,210.00 USD | 6,980,000.00 USD |
| `7D` | `2093.90` | 2,660,000,000.00 USD | 0.00 USD | 2,660,000,000.00 USD | 5,200,000.00 USD | 1,640,000.00 USD | 2,340,000.00 USD |
| `7D` | `2096.70` | 2,650,000,000.00 USD | 0.00 USD | 2,650,000,000.00 USD | 1,940,000.00 USD | 3,330,000.00 USD | 1,290,000.00 USD |
| `7D` | `2099.50` | 2,640,000,000.00 USD | 0.00 USD | 2,640,000,000.00 USD | 1,880,000.00 USD | 1,520,000.00 USD | 2,070,000.00 USD |
| `7D` | `2102.30` | 2,630,000,000.00 USD | 0.00 USD | 2,630,000,000.00 USD | 125,250.00 USD | 688,260.00 USD | 2,010,000.00 USD |
| `7D` | `2105.10` | 2,630,000,000.00 USD | 0.00 USD | 2,630,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 2,210,000.00 USD |
| `7D` | `2107.90` | 2,630,000,000.00 USD | 0.00 USD | 2,630,000,000.00 USD | 2,320,000.00 USD | 356,360.00 USD | 1,640,000.00 USD |
| `7D` | `2110.70` | 2,620,000,000.00 USD | 0.00 USD | 2,620,000,000.00 USD | 2,830,000.00 USD | 2,300,000.00 USD | 1,960,000.00 USD |
| `7D` | `2113.50` | 2,610,000,000.00 USD | 0.00 USD | 2,610,000,000.00 USD | 1,730,000.00 USD | 1,280,000.00 USD | 2,940,000.00 USD |
| `1D` | `2114.20` | 1,230,000,000.00 USD | 0.00 USD | 1,230,000,000.00 USD | 1,130,000.00 USD | 1,080,000.00 USD | 532,450.00 USD |
| `7D` | `2116.30` | 2,610,000,000.00 USD | 0.00 USD | 2,610,000,000.00 USD | 1,480,000.00 USD | 2,030,000.00 USD | 2,560,000.00 USD |
| `1D` | `2116.80` | 1,230,000,000.00 USD | 0.00 USD | 1,230,000,000.00 USD | 1,070,000.00 USD | 335,670.00 USD | 697,640.00 USD |
| `7D` | `2119.10` | 2,600,000,000.00 USD | 0.00 USD | 2,600,000,000.00 USD | 3,390,000.00 USD | 935,590.00 USD | 2,590,000.00 USD |
| `1D` | `2119.40` | 1,230,000,000.00 USD | 0.00 USD | 1,230,000,000.00 USD | 493,030.00 USD | 256,720.00 USD | 987,290.00 USD |
| `7D` | `2121.90` | 2,600,000,000.00 USD | 0.00 USD | 2,600,000,000.00 USD | 2,300,000.00 USD | 973,690.00 USD | 1,630,000.00 USD |
| `1D` | `2122.00` | 1,220,000,000.00 USD | 0.00 USD | 1,220,000,000.00 USD | 982,960.00 USD | 704,400.00 USD | 1,180,000.00 USD |
| `1D` | `2124.60` | 1,220,000,000.00 USD | 0.00 USD | 1,220,000,000.00 USD | 1,010,000.00 USD | 1,150,000.00 USD | 849,420.00 USD |
| `7D` | `2124.70` | 2,590,000,000.00 USD | 0.00 USD | 2,590,000,000.00 USD | 2,110,000.00 USD | 983,790.00 USD | 989,650.00 USD |
| `1D` | `2127.20` | 1,220,000,000.00 USD | 0.00 USD | 1,220,000,000.00 USD | 258,900.00 USD | 724,120.00 USD | 306,050.00 USD |
| `7D` | `2127.50` | 2,590,000,000.00 USD | 0.00 USD | 2,590,000,000.00 USD | 1,080,000.00 USD | 2,620,000.00 USD | 3,270,000.00 USD |
| `1D` | `2129.80` | 1,220,000,000.00 USD | 0.00 USD | 1,220,000,000.00 USD | 107,010.00 USD | 472,480.00 USD | 318,170.00 USD |
| `7D` | `2130.30` | 2,580,000,000.00 USD | 0.00 USD | 2,580,000,000.00 USD | 2,040,000.00 USD | 2,130,000.00 USD | 1,680,000.00 USD |
| `1D` | `2132.40` | 1,220,000,000.00 USD | 0.00 USD | 1,220,000,000.00 USD | 0.00 USD | 937,720.00 USD | 336,530.00 USD |
| `7D` | `2133.10` | 2,570,000,000.00 USD | 0.00 USD | 2,570,000,000.00 USD | 1,930,000.00 USD | 715,940.00 USD | 330,780.00 USD |
| `1D` | `2135.00` | 1,220,000,000.00 USD | 0.00 USD | 1,220,000,000.00 USD | 187,520.00 USD | 228,740.00 USD | 2,870.00 USD |
| `7D` | `2135.90` | 2,570,000,000.00 USD | 0.00 USD | 2,570,000,000.00 USD | 1,370,000.00 USD | 596,290.00 USD | 0.00 USD |
| `1D` | `2137.60` | 1,210,000,000.00 USD | 0.00 USD | 1,210,000,000.00 USD | 555,320.00 USD | 501,410.00 USD | 205,180.00 USD |
| `7D` | `2138.70` | 2,570,000,000.00 USD | 0.00 USD | 2,570,000,000.00 USD | 909,440.00 USD | 1,250,000.00 USD | 78,760.00 USD |
| `7D` | `2141.50` | 2,570,000,000.00 USD | 0.00 USD | 2,570,000,000.00 USD | 1,750,000.00 USD | 199,980.00 USD | 776,560.00 USD |
| `1D` | `2142.80` | 1,210,000,000.00 USD | 0.00 USD | 1,210,000,000.00 USD | 295,510.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2144.30` | 2,560,000,000.00 USD | 0.00 USD | 2,560,000,000.00 USD | 465,960.00 USD | 1,540,000.00 USD | 268,500.00 USD |
| `1D` | `2145.40` | 1,210,000,000.00 USD | 0.00 USD | 1,210,000,000.00 USD | 0.00 USD | 16,700.00 USD | 210,520.00 USD |
| `7D` | `2147.10` | 2,560,000,000.00 USD | 0.00 USD | 2,560,000,000.00 USD | 311,920.00 USD | 32,210.00 USD | 0.00 USD |
| `1D` | `2148.00` | 1,210,000,000.00 USD | 0.00 USD | 1,210,000,000.00 USD | 251,250.00 USD | 11,090.00 USD | 0.00 USD |
| `7D` | `2149.90` | 2,560,000,000.00 USD | 0.00 USD | 2,560,000,000.00 USD | 459,630.00 USD | 482,820.00 USD | 537,180.00 USD |
| `7D` | `2152.70` | 2,560,000,000.00 USD | 0.00 USD | 2,560,000,000.00 USD | 58,340.00 USD | 681,070.00 USD | 0.00 USD |
| `7D` | `2155.50` | 2,560,000,000.00 USD | 0.00 USD | 2,560,000,000.00 USD | 191,860.00 USD | 454,940.00 USD | 866,760.00 USD |
| `7D` | `2158.30` | 2,560,000,000.00 USD | 0.00 USD | 2,560,000,000.00 USD | 738,850.00 USD | 717,210.00 USD | 1,590,000.00 USD |
| `7D` | `2161.10` | 2,550,000,000.00 USD | 0.00 USD | 2,550,000,000.00 USD | 1,490,000.00 USD | 1,350,000.00 USD | 2,240,000.00 USD |
| `7D` | `2163.90` | 2,550,000,000.00 USD | 0.00 USD | 2,550,000,000.00 USD | 36,870.00 USD | 329,690.00 USD | 409,110.00 USD |
| `7D` | `2166.70` | 2,550,000,000.00 USD | 0.00 USD | 2,550,000,000.00 USD | 25,540.00 USD | 0.00 USD | 68,110.00 USD |
| `7D` | `2169.50` | 2,550,000,000.00 USD | 0.00 USD | 2,550,000,000.00 USD | 1,700,000.00 USD | 726,240.00 USD | 810,540.00 USD |
| `7D` | `2172.30` | 2,550,000,000.00 USD | 0.00 USD | 2,550,000,000.00 USD | 479,540.00 USD | 1,150,000.00 USD | 0.00 USD |
| `7D` | `2194.70` | 2,540,000,000.00 USD | 0.00 USD | 2,540,000,000.00 USD | 141,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2197.50` | 2,540,000,000.00 USD | 0.00 USD | 2,540,000,000.00 USD | 2,440,000.00 USD | 3,270,000.00 USD | 0.00 USD |
| `1D` | `2200.00` | 1,210,000,000.00 USD | 0.00 USD | 1,210,000,000.00 USD | 201,540.00 USD | 154,560.00 USD | 169,890.00 USD |
| `7D` | `2200.30` | 2,540,000,000.00 USD | 0.00 USD | 2,540,000,000.00 USD | 3,000,000.00 USD | 3,140,000.00 USD | 3,200,000.00 USD |
| `1D` | `2202.60` | 1,210,000,000.00 USD | 0.00 USD | 1,210,000,000.00 USD | 1,140,000.00 USD | 62,930.00 USD | 751,990.00 USD |
| `7D` | `2203.10` | 2,530,000,000.00 USD | 0.00 USD | 2,530,000,000.00 USD | 3,240,000.00 USD | 624,500.00 USD | 2,720,000.00 USD |
| `1D` | `2205.20` | 1,210,000,000.00 USD | 0.00 USD | 1,210,000,000.00 USD | 0.00 USD | 207,110.00 USD | 95,720.00 USD |
| `7D` | `2205.90` | 2,520,000,000.00 USD | 0.00 USD | 2,520,000,000.00 USD | 6,050,000.00 USD | 4,010,000.00 USD | 3,950,000.00 USD |
| `1D` | `2207.80` | 1,210,000,000.00 USD | 0.00 USD | 1,210,000,000.00 USD | 3,100,000.00 USD | 2,380,000.00 USD | 3,090,000.00 USD |
| `7D` | `2208.70` | 2,510,000,000.00 USD | 0.00 USD | 2,510,000,000.00 USD | 10,060,000.00 USD | 6,100,000.00 USD | 4,070,000.00 USD |
| `1D` | `2210.40` | 1,200,000,000.00 USD | 0.00 USD | 1,200,000,000.00 USD | 1,610,000.00 USD | 1,180,000.00 USD | 1,190,000.00 USD |
| `7D` | `2211.50` | 2,490,000,000.00 USD | 0.00 USD | 2,490,000,000.00 USD | 7,320,000.00 USD | 7,940,000.00 USD | 7,060,000.00 USD |
| `1D` | `2213.00` | 1,200,000,000.00 USD | 0.00 USD | 1,200,000,000.00 USD | 3,000,000.00 USD | 1,970,000.00 USD | 1,290,000.00 USD |
| `7D` | `2214.30` | 2,470,000,000.00 USD | 0.00 USD | 2,470,000,000.00 USD | 13,980,000.00 USD | 12,380,000.00 USD | 9,960,000.00 USD |
| `1D` | `2215.60` | 1,190,000,000.00 USD | 0.00 USD | 1,190,000,000.00 USD | 6,210,000.00 USD | 4,500,000.00 USD | 5,780,000.00 USD |
| `7D` | `2217.10` | 2,430,000,000.00 USD | 0.00 USD | 2,430,000,000.00 USD | 16,020,000.00 USD | 10,300,000.00 USD | 8,280,000.00 USD |
| `1D` | `2218.20` | 1,170,000,000.00 USD | 0.00 USD | 1,170,000,000.00 USD | 4,620,000.00 USD | 4,760,000.00 USD | 1,290,000.00 USD |
| `7D` | `2219.90` | 2,390,000,000.00 USD | 0.00 USD | 2,390,000,000.00 USD | 12,620,000.00 USD | 10,310,000.00 USD | 3,040,000.00 USD |
| `1D` | `2220.80` | 1,160,000,000.00 USD | 0.00 USD | 1,160,000,000.00 USD | 3,730,000.00 USD | 3,970,000.00 USD | 533,270.00 USD |
| `7D` | `2222.70` | 2,370,000,000.00 USD | 0.00 USD | 2,370,000,000.00 USD | 5,480,000.00 USD | 5,400,000.00 USD | 8,890,000.00 USD |
| `1D` | `2223.40` | 1,160,000,000.00 USD | 0.00 USD | 1,160,000,000.00 USD | 4,480,000.00 USD | 3,950,000.00 USD | 3,140,000.00 USD |
| `7D` | `2225.50` | 2,350,000,000.00 USD | 0.00 USD | 2,350,000,000.00 USD | 12,980,000.00 USD | 13,620,000.00 USD | 9,460,000.00 USD |
| `1D` | `2226.00` | 1,140,000,000.00 USD | 0.00 USD | 1,140,000,000.00 USD | 5,320,000.00 USD | 5,400,000.00 USD | 2,580,000.00 USD |
| `7D` | `2228.30` | 2,310,000,000.00 USD | 0.00 USD | 2,310,000,000.00 USD | 7,790,000.00 USD | 5,070,000.00 USD | 7,280,000.00 USD |
| `1D` | `2228.60` | 1,130,000,000.00 USD | 0.00 USD | 1,130,000,000.00 USD | 3,180,000.00 USD | 1,360,000.00 USD | 664,340.00 USD |
| `7D` | `2231.10` | 2,290,000,000.00 USD | 0.00 USD | 2,290,000,000.00 USD | 9,590,000.00 USD | 3,450,000.00 USD | 17,130,000.00 USD |
| `1D` | `2231.20` | 1,130,000,000.00 USD | 0.00 USD | 1,130,000,000.00 USD | 3,000,000.00 USD | 2,830,000.00 USD | 2,930,000.00 USD |
| `1D` | `2233.80` | 1,120,000,000.00 USD | 0.00 USD | 1,120,000,000.00 USD | 7,220,000.00 USD | 3,760,000.00 USD | 2,510,000.00 USD |
| `7D` | `2233.90` | 2,260,000,000.00 USD | 0.00 USD | 2,260,000,000.00 USD | 18,230,000.00 USD | 10,390,000.00 USD | 6,100,000.00 USD |
| `1D` | `2236.40` | 1,100,000,000.00 USD | 0.00 USD | 1,100,000,000.00 USD | 2,550,000.00 USD | 2,090,000.00 USD | 3,720,000.00 USD |
| `7D` | `2236.70` | 2,230,000,000.00 USD | 0.00 USD | 2,230,000,000.00 USD | 7,440,000.00 USD | 11,700,000.00 USD | 5,850,000.00 USD |
| `1D` | `2239.00` | 1,100,000,000.00 USD | 0.00 USD | 1,100,000,000.00 USD | 1,030,000.00 USD | 2,370,000.00 USD | 855,250.00 USD |
| `7D` | `2239.50` | 2,200,000,000.00 USD | 0.00 USD | 2,200,000,000.00 USD | 6,630,000.00 USD | 6,820,000.00 USD | 6,100,000.00 USD |
| `1D` | `2241.60` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 321,680.00 USD | 145,710.00 USD | 284,370.00 USD |
| `7D` | `2242.30` | 2,180,000,000.00 USD | 0.00 USD | 2,180,000,000.00 USD | 3,580,000.00 USD | 2,780,000.00 USD | 7,090,000.00 USD |
| `1D` | `2244.20` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 2,480,000.00 USD | 423,680.00 USD | 238,690.00 USD |
| `7D` | `2245.10` | 2,170,000,000.00 USD | 0.00 USD | 2,170,000,000.00 USD | 16,710,000.00 USD | 13,060,000.00 USD | 11,660,000.00 USD |
| `1D` | `2246.80` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 1,570,000.00 USD | 914,360.00 USD | 1,410,000.00 USD |
| `7D` | `2247.90` | 2,130,000,000.00 USD | 0.00 USD | 2,130,000,000.00 USD | 13,600,000.00 USD | 6,160,000.00 USD | 9,920,000.00 USD |
| `1D` | `2249.40` | 1,080,000,000.00 USD | 0.00 USD | 1,080,000,000.00 USD | 3,680,000.00 USD | 1,540,000.00 USD | 2,180,000.00 USD |
| `7D` | `2250.70` | 2,100,000,000.00 USD | 0.00 USD | 2,100,000,000.00 USD | 10,570,000.00 USD | 10,360,000.00 USD | 8,310,000.00 USD |
| `1D` | `2252.00` | 1,080,000,000.00 USD | 0.00 USD | 1,080,000,000.00 USD | 4,480,000.00 USD | 6,430,000.00 USD | 2,750,000.00 USD |
| `7D` | `2253.50` | 2,070,000,000.00 USD | 0.00 USD | 2,070,000,000.00 USD | 24,760,000.00 USD | 21,020,000.00 USD | 19,300,000.00 USD |
| `1D` | `2254.60` | 1,060,000,000.00 USD | 0.00 USD | 1,060,000,000.00 USD | 8,120,000.00 USD | 3,660,000.00 USD | 7,190,000.00 USD |
| `7D` | `2256.30` | 2,000,000,000.00 USD | 0.00 USD | 2,000,000,000.00 USD | 31,260,000.00 USD | 19,100,000.00 USD | 18,020,000.00 USD |
| `1D` | `2257.20` | 1,040,000,000.00 USD | 0.00 USD | 1,040,000,000.00 USD | 5,380,000.00 USD | 5,380,000.00 USD | 2,360,000.00 USD |
| `7D` | `2259.10` | 1,940,000,000.00 USD | 0.00 USD | 1,940,000,000.00 USD | 21,420,000.00 USD | 19,400,000.00 USD | 22,950,000.00 USD |
| `1D` | `2259.80` | 1,030,000,000.00 USD | 0.00 USD | 1,030,000,000.00 USD | 13,220,000.00 USD | 6,980,000.00 USD | 8,830,000.00 USD |
| `7D` | `2261.90` | 1,870,000,000.00 USD | 0.00 USD | 1,870,000,000.00 USD | 48,180,000.00 USD | 29,390,000.00 USD | 21,430,000.00 USD |
| `1D` | `2262.40` | 1,000,000,000.00 USD | 0.00 USD | 1,000,000,000.00 USD | 15,720,000.00 USD | 15,880,000.00 USD | 13,100,000.00 USD |
| `7D` | `2264.70` | 1,770,000,000.00 USD | 0.00 USD | 1,770,000,000.00 USD | 30,320,000.00 USD | 28,050,000.00 USD | 19,360,000.00 USD |
| `1D` | `2265.00` | 956,060,000.00 USD | 0.00 USD | 956,060,000.00 USD | 14,360,000.00 USD | 11,480,000.00 USD | 6,210,000.00 USD |
| `7D` | `2267.50` | 1,700,000,000.00 USD | 0.00 USD | 1,700,000,000.00 USD | 40,120,000.00 USD | 40,100,000.00 USD | 31,060,000.00 USD |
| `1D` | `2267.60` | 924,010,000.00 USD | 0.00 USD | 924,010,000.00 USD | 4,850,000.00 USD | 7,350,000.00 USD | 3,810,000.00 USD |
| `1D` | `2270.20` | 908,010,000.00 USD | 0.00 USD | 908,010,000.00 USD | 14,410,000.00 USD | 11,370,000.00 USD | 8,320,000.00 USD |
| `7D` | `2270.30` | 1,580,000,000.00 USD | 0.00 USD | 1,580,000,000.00 USD | 39,480,000.00 USD | 27,490,000.00 USD | 39,210,000.00 USD |
| `1D` | `2272.80` | 873,920,000.00 USD | 0.00 USD | 873,920,000.00 USD | 15,080,000.00 USD | 12,460,000.00 USD | 9,440,000.00 USD |
| `7D` | `2273.10` | 1,480,000,000.00 USD | 0.00 USD | 1,480,000,000.00 USD | 33,160,000.00 USD | 25,760,000.00 USD | 19,780,000.00 USD |
| `1D` | `2275.40` | 836,940,000.00 USD | 0.00 USD | 836,940,000.00 USD | 8,710,000.00 USD | 13,510,000.00 USD | 4,490,000.00 USD |
| `7D` | `2275.90` | 1,400,000,000.00 USD | 0.00 USD | 1,400,000,000.00 USD | 48,240,000.00 USD | 42,710,000.00 USD | 44,210,000.00 USD |
| `1D` | `2278.00` | 810,240,000.00 USD | 0.00 USD | 810,240,000.00 USD | 17,980,000.00 USD | 8,710,000.00 USD | 18,230,000.00 USD |
| `7D` | `2278.70` | 1,260,000,000.00 USD | 0.00 USD | 1,260,000,000.00 USD | 74,310,000.00 USD | 34,750,000.00 USD | 42,010,000.00 USD |
| `1D` | `2280.60` | 765,310,000.00 USD | 0.00 USD | 765,310,000.00 USD | 25,850,000.00 USD | 15,120,000.00 USD | 7,880,000.00 USD |
| `7D` | `2281.50` | 1,110,000,000.00 USD | 0.00 USD | 1,110,000,000.00 USD | 56,100,000.00 USD | 59,940,000.00 USD | 49,270,000.00 USD |
| `1D` | `2283.20` | 716,450,000.00 USD | 0.00 USD | 716,450,000.00 USD | 23,970,000.00 USD | 18,060,000.00 USD | 28,420,000.00 USD |
| `7D` | `2284.30` | 947,650,000.00 USD | 0.00 USD | 947,650,000.00 USD | 89,220,000.00 USD | 69,840,000.00 USD | 44,200,000.00 USD |
| `1D` | `2285.80` | 646,000,000.00 USD | 0.00 USD | 646,000,000.00 USD | 26,180,000.00 USD | 26,480,000.00 USD | 12,800,000.00 USD |
| `7D` | `2287.10` | 744,380,000.00 USD | 0.00 USD | 744,380,000.00 USD | 58,910,000.00 USD | 53,380,000.00 USD | 45,180,000.00 USD |
| `1D` | `2288.40` | 580,550,000.00 USD | 0.00 USD | 580,550,000.00 USD | 17,180,000.00 USD | 15,670,000.00 USD | 3,010,000.00 USD |
| `7D` | `2289.90` | 586,910,000.00 USD | 0.00 USD | 586,910,000.00 USD | 48,430,000.00 USD | 34,490,000.00 USD | 22,190,000.00 USD |
| `1D` | `2291.00` | 544,690,000.00 USD | 0.00 USD | 544,690,000.00 USD | 14,820,000.00 USD | 12,810,000.00 USD | 3,400,000.00 USD |
| `7D` | `2292.70` | 481,810,000.00 USD | 0.00 USD | 481,810,000.00 USD | 38,110,000.00 USD | 20,900,000.00 USD | 44,070,000.00 USD |
| `1D` | `2293.60` | 513,660,000.00 USD | 0.00 USD | 513,660,000.00 USD | 16,600,000.00 USD | 17,360,000.00 USD | 14,330,000.00 USD |
| `7D` | `2295.50` | 378,730,000.00 USD | 0.00 USD | 378,730,000.00 USD | 17,510,000.00 USD | 8,110,000.00 USD | 7,220,000.00 USD |
| `1D` | `2296.20` | 465,370,000.00 USD | 0.00 USD | 465,370,000.00 USD | 22,580,000.00 USD | 10,920,000.00 USD | 7,610,000.00 USD |
| `7D` | `2298.30` | 345,890,000.00 USD | 0.00 USD | 345,890,000.00 USD | 2,090,000.00 USD | 5,410,000.00 USD | 301,550.00 USD |
| `1D` | `2298.80` | 424,260,000.00 USD | 0.00 USD | 424,260,000.00 USD | 10,240,000.00 USD | 8,320,000.00 USD | 3,540,000.00 USD |
| `7D` | `2301.10` | 338,090,000.00 USD | 0.00 USD | 338,090,000.00 USD | 11,790,000.00 USD | 2,200,000.00 USD | 7,590,000.00 USD |
| `1D` | `2301.40` | 402,160,000.00 USD | 0.00 USD | 402,160,000.00 USD | 16,890,000.00 USD | 11,600,000.00 USD | 12,350,000.00 USD |
| `7D` | `2303.90` | 316,510,000.00 USD | 0.00 USD | 316,510,000.00 USD | 31,030,000.00 USD | 17,020,000.00 USD | 13,250,000.00 USD |
| `1D` | `2304.00` | 361,320,000.00 USD | 0.00 USD | 361,320,000.00 USD | 28,790,000.00 USD | 16,100,000.00 USD | 13,840,000.00 USD |
| `1D` | `2306.60` | 302,590,000.00 USD | 0.00 USD | 302,590,000.00 USD | 2,760,000.00 USD | 4,390,000.00 USD | 14,130,000.00 USD |
| `7D` | `2306.70` | 255,220,000.00 USD | 0.00 USD | 255,220,000.00 USD | 0.00 USD | 3,740,000.00 USD | 10,880,000.00 USD |
| `1D` | `2309.20` | 281,320,000.00 USD | 0.00 USD | 281,320,000.00 USD | 3,370,000.00 USD | 1,990,000.00 USD | 743,190.00 USD |
| `7D` | `2309.50` | 240,590,000.00 USD | 0.00 USD | 240,590,000.00 USD | 282,530.00 USD | 300,580.00 USD | 1,500,000.00 USD |
| `1D` | `2311.80` | 275,220,000.00 USD | 0.00 USD | 275,220,000.00 USD | 7,740,000.00 USD | 5,840,000.00 USD | 5,090,000.00 USD |
| `7D` | `2312.30` | 238,510,000.00 USD | 0.00 USD | 238,510,000.00 USD | 1,740,000.00 USD | 128,300.00 USD | 2,500,000.00 USD |
| `1D` | `2314.40` | 256,550,000.00 USD | 0.00 USD | 256,550,000.00 USD | 6,800,000.00 USD | 3,480,000.00 USD | 1,650,000.00 USD |
| `7D` | `2315.10` | 234,130,000.00 USD | 0.00 USD | 234,130,000.00 USD | 4,300,000.00 USD | 4,100,000.00 USD | 117,510.00 USD |
| `1D` | `2317.00` | 244,630,000.00 USD | 0.00 USD | 244,630,000.00 USD | 6,200,000.00 USD | 2,460,000.00 USD | 2,740,000.00 USD |
| `7D` | `2317.90` | 225,610,000.00 USD | 0.00 USD | 225,610,000.00 USD | 817,040.00 USD | 3,010,000.00 USD | 0.00 USD |
| `1D` | `2319.60` | 233,220,000.00 USD | 0.00 USD | 233,220,000.00 USD | 5,480,000.00 USD | 3,000,000.00 USD | 795,520.00 USD |
| `7D` | `2320.70` | 221,790,000.00 USD | 0.00 USD | 221,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 0.00 USD |
| `1D` | `2322.20` | 223,940,000.00 USD | 0.00 USD | 223,940,000.00 USD | 4,760,000.00 USD | 1,780,000.00 USD | 1,660,000.00 USD |
| `7D` | `2323.50` | 219,000,000.00 USD | 0.00 USD | 219,000,000.00 USD | 4,070,000.00 USD | 1,900,000.00 USD | 0.00 USD |
| `1D` | `2324.80` | 215,740,000.00 USD | 0.00 USD | 215,740,000.00 USD | 4,120,000.00 USD | 2,830,000.00 USD | 2,260,000.00 USD |
| `7D` | `2326.30` | 213,020,000.00 USD | 0.00 USD | 213,020,000.00 USD | 0.00 USD | 0.00 USD | 75,760.00 USD |
| `1D` | `2327.40` | 206,530,000.00 USD | 0.00 USD | 206,530,000.00 USD | 0.00 USD | 3,130,000.00 USD | 3,370,000.00 USD |
| `7D` | `2329.10` | 212,950,000.00 USD | 0.00 USD | 212,950,000.00 USD | 0.00 USD | 0.00 USD | 4,870,000.00 USD |
| `1D` | `2330.00` | 200,030,000.00 USD | 0.00 USD | 200,030,000.00 USD | 4,080,000.00 USD | 1,150,000.00 USD | 3,040,000.00 USD |
| `7D` | `2331.90` | 208,080,000.00 USD | 0.00 USD | 208,080,000.00 USD | 29,230,000.00 USD | 1,090,000.00 USD | 2,810,000.00 USD |
| `1D` | `2332.60` | 191,770,000.00 USD | 0.00 USD | 191,770,000.00 USD | 22,980,000.00 USD | 2,290,000.00 USD | 107,090.00 USD |
| `7D` | `2334.70` | 174,940,000.00 USD | 0.00 USD | 174,940,000.00 USD | 7,260,000.00 USD | 18,420,000.00 USD | 8,930,000.00 USD |
| `1D` | `2335.20` | 166,390,000.00 USD | 0.00 USD | 166,390,000.00 USD | 25,380,000.00 USD | 25,170,000.00 USD | 19,910,000.00 USD |
| `7D` | `2337.50` | 140,330,000.00 USD | 0.00 USD | 140,330,000.00 USD | 20,380,000.00 USD | 18,560,000.00 USD | 13,560,000.00 USD |
| `1D` | `2337.80` | 95,930,000.00 USD | 0.00 USD | 95,930,000.00 USD | 6,510,000.00 USD | 23,080,000.00 USD | 10,900,000.00 USD |
| `7D` | `2340.30` | 87,820,000.00 USD | 0.00 USD | 87,820,000.00 USD | 1,630,000.00 USD | 10,010,000.00 USD | 3,380,000.00 USD |
| `1D` | `2340.40` | 55,440,000.00 USD | 0.00 USD | 55,440,000.00 USD | 5,620,000.00 USD | 28,460,000.00 USD | 2,520,000.00 USD |
| `1D` | `2343.00` | 18,850,000.00 USD | 0.00 USD | 18,850,000.00 USD | 1,880,000.00 USD | 764,610.00 USD | 3,180,000.00 USD |
| `7D` | `2343.10` | 72,800,000.00 USD | 0.00 USD | 72,800,000.00 USD | 0.00 USD | 5,540,000.00 USD | 3,840,000.00 USD |
| `1D` | `2345.60` | 13,030,000.00 USD | 0.00 USD | 13,030,000.00 USD | 963,370.00 USD | 1,770,000.00 USD | 8,970,000.00 USD |
| `7D` | `2345.90` | 63,410,000.00 USD | 0.00 USD | 63,410,000.00 USD | 0.00 USD | 8,310,000.00 USD | 12,830,000.00 USD |
| `1D` | `2348.20` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2348.70` | 42,270,000.00 USD | 0.00 USD | 42,270,000.00 USD | 285,680.00 USD | 7,340,000.00 USD | 10,750,000.00 USD |
| `1D` | `2350.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2350.80` | 32,810,000.00 USD | 32,810,000.00 USD | 0.00 USD | 30,280,000.00 USD | 2,510,000.00 USD | 23,220.00 USD |
| `7D` | `2351.50` | 23,900,000.00 USD | 0.00 USD | 23,900,000.00 USD | 782,590.00 USD | 17,440,000.00 USD | 5,680,000.00 USD |
| `7D` | `2351.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2353.40` | 40,220,000.00 USD | 40,220,000.00 USD | 0.00 USD | 3,700,000.00 USD | 3,610,000.00 USD | 107,380.00 USD |
| `7D` | `2354.30` | 47,370,000.00 USD | 47,370,000.00 USD | 0.00 USD | 12,110,000.00 USD | 35,020,000.00 USD | 237,340.00 USD |
| `1D` | `2356.00` | 55,340,000.00 USD | 55,340,000.00 USD | 0.00 USD | 318,080.00 USD | 13,480,000.00 USD | 1,330,000.00 USD |
| `7D` | `2357.10` | 60,670,000.00 USD | 60,670,000.00 USD | 0.00 USD | 7,900,000.00 USD | 5,400,000.00 USD | 0.00 USD |
| `1D` | `2358.60` | 55,460,000.00 USD | 55,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 114,560.00 USD |
| `7D` | `2359.90` | 62,880,000.00 USD | 62,880,000.00 USD | 0.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2361.20` | 57,610,000.00 USD | 57,610,000.00 USD | 0.00 USD | 2,040,000.00 USD | 0.00 USD | 110,060.00 USD |
| `7D` | `2362.70` | 65,040,000.00 USD | 65,040,000.00 USD | 0.00 USD | 467,570.00 USD | 0.00 USD | 1,690,000.00 USD |
| `1D` | `2363.80` | 60,520,000.00 USD | 60,520,000.00 USD | 0.00 USD | 742,460.00 USD | 1,840,000.00 USD | 324,580.00 USD |
| `7D` | `2365.50` | 73,040,000.00 USD | 73,040,000.00 USD | 0.00 USD | 6,340,000.00 USD | 0.00 USD | 1,660,000.00 USD |
| `1D` | `2366.40` | 60,850,000.00 USD | 60,850,000.00 USD | 0.00 USD | 122,070.00 USD | 0.00 USD | 211,320.00 USD |
| `7D` | `2368.30` | 83,010,000.00 USD | 83,010,000.00 USD | 0.00 USD | 9,590,000.00 USD | 0.00 USD | 370,810.00 USD |
| `1D` | `2369.00` | 79,000,000.00 USD | 79,000,000.00 USD | 0.00 USD | 13,760,000.00 USD | 3,260,000.00 USD | 1,130,000.00 USD |
| `7D` | `2371.10` | 144,800,000.00 USD | 144,800,000.00 USD | 0.00 USD | 16,760,000.00 USD | 0.00 USD | 45,040,000.00 USD |
| `1D` | `2371.60` | 113,190,000.00 USD | 113,190,000.00 USD | 0.00 USD | 11,360,000.00 USD | 13,360,000.00 USD | 9,480,000.00 USD |
| `7D` | `2373.90` | 167,320,000.00 USD | 167,320,000.00 USD | 0.00 USD | 15,830,000.00 USD | 0.00 USD | 6,680,000.00 USD |
| `1D` | `2374.20` | 128,410,000.00 USD | 128,410,000.00 USD | 0.00 USD | 13,920,000.00 USD | 349,710.00 USD | 945,930.00 USD |
| `7D` | `2376.70` | 203,580,000.00 USD | 203,580,000.00 USD | 0.00 USD | 8,280,000.00 USD | 5,950,000.00 USD | 22,040,000.00 USD |
| `1D` | `2376.80` | 155,240,000.00 USD | 155,240,000.00 USD | 0.00 USD | 9,620,000.00 USD | 5,340,000.00 USD | 11,870,000.00 USD |
| `1D` | `2379.40` | 185,610,000.00 USD | 185,610,000.00 USD | 0.00 USD | 6,610,000.00 USD | 11,890,000.00 USD | 11,870,000.00 USD |
| `7D` | `2379.50` | 230,900,000.00 USD | 230,900,000.00 USD | 0.00 USD | 7,180,000.00 USD | 2,580,000.00 USD | 17,560,000.00 USD |
| `1D` | `2382.00` | 230,210,000.00 USD | 230,210,000.00 USD | 0.00 USD | 18,560,000.00 USD | 11,220,000.00 USD | 14,810,000.00 USD |
| `7D` | `2382.30` | 272,240,000.00 USD | 272,240,000.00 USD | 0.00 USD | 7,910,000.00 USD | 12,120,000.00 USD | 21,320,000.00 USD |
| `1D` | `2384.60` | 275,650,000.00 USD | 275,650,000.00 USD | 0.00 USD | 18,560,000.00 USD | 17,070,000.00 USD | 9,810,000.00 USD |
| `7D` | `2385.10` | 358,990,000.00 USD | 358,990,000.00 USD | 0.00 USD | 14,990,000.00 USD | 28,990,000.00 USD | 42,760,000.00 USD |
| `1D` | `2387.20` | 305,860,000.00 USD | 305,860,000.00 USD | 0.00 USD | 12,110,000.00 USD | 11,050,000.00 USD | 7,060,000.00 USD |
| `7D` | `2387.90` | 439,130,000.00 USD | 439,130,000.00 USD | 0.00 USD | 4,870,000.00 USD | 32,720,000.00 USD | 42,550,000.00 USD |
| `1D` | `2389.80` | 331,290,000.00 USD | 331,290,000.00 USD | 0.00 USD | 8,210,000.00 USD | 11,220,000.00 USD | 5,990,000.00 USD |
| `7D` | `2390.70` | 538,810,000.00 USD | 538,810,000.00 USD | 0.00 USD | 5,470,000.00 USD | 45,700,000.00 USD | 48,520,000.00 USD |
| `1D` | `2392.40` | 360,770,000.00 USD | 360,770,000.00 USD | 0.00 USD | 9,370,000.00 USD | 11,000,000.00 USD | 9,120,000.00 USD |
| `7D` | `2393.50` | 637,280,000.00 USD | 637,280,000.00 USD | 0.00 USD | 43,890,000.00 USD | 22,890,000.00 USD | 31,690,000.00 USD |
| `1D` | `2395.00` | 386,830,000.00 USD | 386,830,000.00 USD | 0.00 USD | 10,550,000.00 USD | 13,400,000.00 USD | 2,110,000.00 USD |
| `7D` | `2396.30` | 721,290,000.00 USD | 721,290,000.00 USD | 0.00 USD | 29,820,000.00 USD | 32,850,000.00 USD | 21,340,000.00 USD |
| `1D` | `2397.60` | 410,130,000.00 USD | 410,130,000.00 USD | 0.00 USD | 6,340,000.00 USD | 9,590,000.00 USD | 7,360,000.00 USD |
| `7D` | `2399.10` | 808,890,000.00 USD | 808,890,000.00 USD | 0.00 USD | 37,420,000.00 USD | 31,200,000.00 USD | 18,980,000.00 USD |
| `1D` | `2400.20` | 447,310,000.00 USD | 447,310,000.00 USD | 0.00 USD | 17,230,000.00 USD | 8,470,000.00 USD | 11,470,000.00 USD |
| `7D` | `2401.90` | 919,670,000.00 USD | 919,670,000.00 USD | 0.00 USD | 53,530,000.00 USD | 24,490,000.00 USD | 32,770,000.00 USD |
| `1D` | `2402.80` | 476,150,000.00 USD | 476,150,000.00 USD | 0.00 USD | 8,970,000.00 USD | 11,160,000.00 USD | 8,710,000.00 USD |
| `7D` | `2404.70` | 997,410,000.00 USD | 997,410,000.00 USD | 0.00 USD | 36,370,000.00 USD | 25,840,000.00 USD | 15,520,000.00 USD |
| `1D` | `2405.40` | 507,700,000.00 USD | 507,700,000.00 USD | 0.00 USD | 13,610,000.00 USD | 9,110,000.00 USD | 8,840,000.00 USD |
| `7D` | `2407.50` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 0.00 USD | 22,760,000.00 USD | 29,510,000.00 USD | 18,930,000.00 USD |
| `1D` | `2408.00` | 544,540,000.00 USD | 544,540,000.00 USD | 0.00 USD | 14,360,000.00 USD | 12,120,000.00 USD | 10,350,000.00 USD |
| `7D` | `2410.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 26,620,000.00 USD | 26,620,000.00 USD | 23,370,000.00 USD |
| `1D` | `2410.60` | 568,350,000.00 USD | 568,350,000.00 USD | 0.00 USD | 9,470,000.00 USD | 9,130,000.00 USD | 5,210,000.00 USD |
| `7D` | `2413.10` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 13,360,000.00 USD | 15,180,000.00 USD | 13,360,000.00 USD |
| `1D` | `2413.20` | 585,660,000.00 USD | 585,660,000.00 USD | 0.00 USD | 8,240,000.00 USD | 5,620,000.00 USD | 3,450,000.00 USD |
| `1D` | `2415.80` | 598,350,000.00 USD | 598,350,000.00 USD | 0.00 USD | 3,180,000.00 USD | 5,730,000.00 USD | 3,770,000.00 USD |
| `7D` | `2415.90` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 0.00 USD | 28,030,000.00 USD | 17,450,000.00 USD | 32,370,000.00 USD |
| `1D` | `2418.40` | 612,330,000.00 USD | 612,330,000.00 USD | 0.00 USD | 5,720,000.00 USD | 5,340,000.00 USD | 2,920,000.00 USD |
| `7D` | `2418.70` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 0.00 USD | 28,840,000.00 USD | 18,500,000.00 USD | 12,150,000.00 USD |
| `1D` | `2421.00` | 625,960,000.00 USD | 625,960,000.00 USD | 0.00 USD | 5,930,000.00 USD | 5,130,000.00 USD | 2,570,000.00 USD |
| `7D` | `2421.50` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 23,440,000.00 USD | 25,120,000.00 USD | 18,550,000.00 USD |
| `1D` | `2423.60` | 640,620,000.00 USD | 640,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 4,540,000.00 USD | 5,500,000.00 USD |
| `7D` | `2424.30` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 0.00 USD | 25,250,000.00 USD | 29,620,000.00 USD | 33,670,000.00 USD |
| `1D` | `2426.20` | 643,370,000.00 USD | 643,370,000.00 USD | 0.00 USD | 516,070.00 USD | 1,960,000.00 USD | 271,280.00 USD |
| `7D` | `2427.10` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 0.00 USD | 24,580,000.00 USD | 22,020,000.00 USD | 23,680,000.00 USD |
| `1D` | `2428.80` | 645,840,000.00 USD | 645,840,000.00 USD | 0.00 USD | 2,190,000.00 USD | 12,140.00 USD | 270,050.00 USD |
| `7D` | `2429.90` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 6,160,000.00 USD | 14,060,000.00 USD | 8,450,000.00 USD |
| `1D` | `2431.40` | 650,220,000.00 USD | 650,220,000.00 USD | 0.00 USD | 2,140,000.00 USD | 943,730.00 USD | 1,300,000.00 USD |
| `7D` | `2432.70` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 17,740,000.00 USD | 13,220,000.00 USD | 6,540,000.00 USD |
| `1D` | `2434.00` | 653,470,000.00 USD | 653,470,000.00 USD | 0.00 USD | 2,220,000.00 USD | 98,290.00 USD | 939,710.00 USD |
| `7D` | `2435.50` | 1,670,000,000.00 USD | 1,670,000,000.00 USD | 0.00 USD | 22,360,000.00 USD | 14,140,000.00 USD | 15,430,000.00 USD |
| `1D` | `2436.60` | 657,380,000.00 USD | 657,380,000.00 USD | 0.00 USD | 1,580,000.00 USD | 1,540,000.00 USD | 791,610.00 USD |
| `7D` | `2438.30` | 1,730,000,000.00 USD | 1,730,000,000.00 USD | 0.00 USD | 17,900,000.00 USD | 23,900,000.00 USD | 15,750,000.00 USD |
| `1D` | `2439.20` | 661,250,000.00 USD | 661,250,000.00 USD | 0.00 USD | 1,340,000.00 USD | 1,340,000.00 USD | 1,190,000.00 USD |
| `7D` | `2441.10` | 1,760,000,000.00 USD | 1,760,000,000.00 USD | 0.00 USD | 17,250,000.00 USD | 6,990,000.00 USD | 14,660,000.00 USD |
| `1D` | `2441.80` | 669,720,000.00 USD | 669,720,000.00 USD | 0.00 USD | 4,350,000.00 USD | 3,360,000.00 USD | 759,220.00 USD |
| `7D` | `2443.90` | 1,790,000,000.00 USD | 1,790,000,000.00 USD | 0.00 USD | 6,650,000.00 USD | 13,590,000.00 USD | 7,950,000.00 USD |
| `1D` | `2444.40` | 674,420,000.00 USD | 674,420,000.00 USD | 0.00 USD | 1,510,000.00 USD | 1,650,000.00 USD | 1,540,000.00 USD |
| `7D` | `2446.70` | 1,830,000,000.00 USD | 1,830,000,000.00 USD | 0.00 USD | 10,910,000.00 USD | 7,020,000.00 USD | 18,970,000.00 USD |
| `1D` | `2447.00` | 680,230,000.00 USD | 680,230,000.00 USD | 0.00 USD | 3,140,000.00 USD | 642,690.00 USD | 2,030,000.00 USD |
| `7D` | `2449.50` | 1,870,000,000.00 USD | 1,870,000,000.00 USD | 0.00 USD | 15,780,000.00 USD | 9,650,000.00 USD | 14,870,000.00 USD |
| `1D` | `2449.60` | 688,050,000.00 USD | 688,050,000.00 USD | 0.00 USD | 2,290,000.00 USD | 2,280,000.00 USD | 3,240,000.00 USD |
| `1D` | `2452.20` | 699,090,000.00 USD | 699,090,000.00 USD | 0.00 USD | 3,620,000.00 USD | 3,170,000.00 USD | 4,250,000.00 USD |
| `7D` | `2452.30` | 1,900,000,000.00 USD | 1,900,000,000.00 USD | 0.00 USD | 10,050,000.00 USD | 9,630,000.00 USD | 7,330,000.00 USD |
| `1D` | `2454.80` | 709,450,000.00 USD | 709,450,000.00 USD | 0.00 USD | 4,190,000.00 USD | 3,920,000.00 USD | 2,240,000.00 USD |
| `7D` | `2455.10` | 1,910,000,000.00 USD | 1,910,000,000.00 USD | 0.00 USD | 5,550,000.00 USD | 5,830,000.00 USD | 3,620,000.00 USD |
| `1D` | `2457.40` | 716,110,000.00 USD | 716,110,000.00 USD | 0.00 USD | 2,140,000.00 USD | 2,260,000.00 USD | 2,260,000.00 USD |
| `7D` | `2457.90` | 1,950,000,000.00 USD | 1,950,000,000.00 USD | 0.00 USD | 12,470,000.00 USD | 11,200,000.00 USD | 13,240,000.00 USD |
| `1D` | `2460.00` | 721,780,000.00 USD | 721,780,000.00 USD | 0.00 USD | 2,370,000.00 USD | 1,970,000.00 USD | 1,340,000.00 USD |
| `7D` | `2460.70` | 1,970,000,000.00 USD | 1,970,000,000.00 USD | 0.00 USD | 7,010,000.00 USD | 10,640,000.00 USD | 5,770,000.00 USD |
| `1D` | `2462.60` | 725,110,000.00 USD | 725,110,000.00 USD | 0.00 USD | 174,920.00 USD | 2,050,000.00 USD | 1,100,000.00 USD |
| `7D` | `2463.50` | 2,000,000,000.00 USD | 2,000,000,000.00 USD | 0.00 USD | 9,490,000.00 USD | 9,600,000.00 USD | 8,830,000.00 USD |
| `1D` | `2465.20` | 727,180,000.00 USD | 727,180,000.00 USD | 0.00 USD | 820,990.00 USD | 1,240,000.00 USD | 5,650.00 USD |
| `7D` | `2466.30` | 2,010,000,000.00 USD | 2,010,000,000.00 USD | 0.00 USD | 5,400,000.00 USD | 2,080,000.00 USD | 1,330,000.00 USD |
| `1D` | `2467.80` | 727,560,000.00 USD | 727,560,000.00 USD | 0.00 USD | 0.00 USD | 370,410.00 USD | 7,190.00 USD |
| `7D` | `2469.10` | 2,020,000,000.00 USD | 2,020,000,000.00 USD | 0.00 USD | 2,770,000.00 USD | 3,570,000.00 USD | 408,300.00 USD |
| `1D` | `2470.40` | 731,610,000.00 USD | 731,610,000.00 USD | 0.00 USD | 1,390,000.00 USD | 1,510,000.00 USD | 1,160,000.00 USD |
| `7D` | `2471.90` | 2,020,000,000.00 USD | 2,020,000,000.00 USD | 0.00 USD | 3,090,000.00 USD | 2,760,000.00 USD | 814,440.00 USD |
| `1D` | `2473.00` | 731,850,000.00 USD | 731,850,000.00 USD | 0.00 USD | 0.00 USD | 232,740.00 USD | 3,820.00 USD |
| `7D` | `2474.70` | 2,030,000,000.00 USD | 2,030,000,000.00 USD | 0.00 USD | 5,400,000.00 USD | 866,790.00 USD | 1,750,000.00 USD |
| `1D` | `2475.60` | 732,590,000.00 USD | 732,590,000.00 USD | 0.00 USD | 738,780.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2477.50` | 2,040,000,000.00 USD | 2,040,000,000.00 USD | 0.00 USD | 790,860.00 USD | 3,880,000.00 USD | 2,000,000.00 USD |
| `1D` | `2478.20` | 732,640,000.00 USD | 732,640,000.00 USD | 0.00 USD | 0.00 USD | 41,760.00 USD | 7,750.00 USD |
| `7D` | `2480.30` | 2,040,000,000.00 USD | 2,040,000,000.00 USD | 0.00 USD | 2,300,000.00 USD | 1,740,000.00 USD | 0.00 USD |
| `1D` | `2480.80` | 733,180,000.00 USD | 733,180,000.00 USD | 0.00 USD | 0.00 USD | 27,720.00 USD | 518,550.00 USD |
| `7D` | `2483.10` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 0.00 USD | 2,010,000.00 USD | 1,330,000.00 USD | 1,990,000.00 USD |
| `1D` | `2483.40` | 733,810,000.00 USD | 733,810,000.00 USD | 0.00 USD | 628,130.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2485.90` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 0.00 USD | 586,480.00 USD | 1,560,000.00 USD | 77,610.00 USD |
| `7D` | `2488.70` | 2,050,000,000.00 USD | 2,050,000,000.00 USD | 0.00 USD | 1,710,000.00 USD | 842,740.00 USD | 2,100,000.00 USD |
| `7D` | `2491.50` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 0.00 USD | 1,660,000.00 USD | 2,550,000.00 USD | 672,990.00 USD |
| `7D` | `2494.30` | 2,070,000,000.00 USD | 2,070,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,730,000.00 USD | 5,000,000.00 USD |
| `7D` | `2497.10` | 2,080,000,000.00 USD | 2,080,000,000.00 USD | 0.00 USD | 3,640,000.00 USD | 3,570,000.00 USD | 6,690,000.00 USD |
| `7D` | `2499.90` | 2,090,000,000.00 USD | 2,090,000,000.00 USD | 0.00 USD | 1,110,000.00 USD | 2,430,000.00 USD | 1,090,000.00 USD |
| `7D` | `2502.70` | 2,090,000,000.00 USD | 2,090,000,000.00 USD | 0.00 USD | 110,450.00 USD | 1,430,000.00 USD | 170,270.00 USD |
| `7D` | `2505.50` | 2,090,000,000.00 USD | 2,090,000,000.00 USD | 0.00 USD | 3,200,000.00 USD | 2,320,000.00 USD | 59,220.00 USD |
| `7D` | `2508.30` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 0.00 USD | 1,150,000.00 USD | 1,270,000.00 USD | 1,990,000.00 USD |
| `7D` | `2511.10` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 0.00 USD | 2,560,000.00 USD | 3,230,000.00 USD | 2,640,000.00 USD |
| `7D` | `2513.90` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 0.00 USD | 776,920.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2516.70` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 0.00 USD | 97,050.00 USD | 189,640.00 USD | 0.00 USD |
| `7D` | `2519.50` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD |
| `7D` | `2522.30` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 0.00 USD | 1,050,000.00 USD | 0.00 USD | 945,860.00 USD |
| `1D` | `2522.40` | 734,040,000.00 USD | 734,040,000.00 USD | 0.00 USD | 80,610.00 USD | 61,830.00 USD | 90,130.00 USD |
| `1D` | `2525.00` | 734,520,000.00 USD | 734,520,000.00 USD | 0.00 USD | 421,540.00 USD | 0.00 USD | 53,680.00 USD |
| `7D` | `2525.10` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 0.00 USD | 307,040.00 USD | 224,130.00 USD | 178,180.00 USD |
| `1D` | `2527.60` | 735,250,000.00 USD | 735,250,000.00 USD | 0.00 USD | 0.00 USD | 703,360.00 USD | 26,970.00 USD |
| `7D` | `2527.90` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 0.00 USD | 1,520,000.00 USD | 871,200.00 USD | 749,440.00 USD |
| `1D` | `2530.20` | 736,680,000.00 USD | 736,680,000.00 USD | 0.00 USD | 995,550.00 USD | 0.00 USD | 437,490.00 USD |
| `7D` | `2530.70` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 0.00 USD | 2,140,000.00 USD | 1,930,000.00 USD | 1,220,000.00 USD |
| `1D` | `2532.80` | 737,050,000.00 USD | 737,050,000.00 USD | 0.00 USD | 359,430.00 USD | 0.00 USD | 8,470.00 USD |
| `7D` | `2533.50` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 0.00 USD | 2,620,000.00 USD | 1,770,000.00 USD | 1,390,000.00 USD |
| `1D` | `2535.40` | 737,820,000.00 USD | 737,820,000.00 USD | 0.00 USD | 229,190.00 USD | 41,990.00 USD | 501,570.00 USD |
| `7D` | `2536.30` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 0.00 USD | 2,810,000.00 USD | 2,460,000.00 USD | 2,740,000.00 USD |
| `1D` | `2538.00` | 742,850,000.00 USD | 742,850,000.00 USD | 0.00 USD | 2,030,000.00 USD | 996,850.00 USD | 2,000,000.00 USD |
| `7D` | `2539.10` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 0.00 USD | 3,530,000.00 USD | 3,180,000.00 USD | 1,090,000.00 USD |
| `1D` | `2540.60` | 745,250,000.00 USD | 745,250,000.00 USD | 0.00 USD | 1,150,000.00 USD | 1,010,000.00 USD | 237,050.00 USD |
| `7D` | `2541.90` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 0.00 USD | 3,400,000.00 USD | 2,740,000.00 USD | 2,240,000.00 USD |
| `1D` | `2543.20` | 747,420,000.00 USD | 747,420,000.00 USD | 0.00 USD | 1,090,000.00 USD | 1,070,000.00 USD | 19,390.00 USD |
| `7D` | `2544.70` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 0.00 USD | 2,170,000.00 USD | 1,830,000.00 USD | 1,350,000.00 USD |
| `1D` | `2545.80` | 749,360,000.00 USD | 749,360,000.00 USD | 0.00 USD | 648,140.00 USD | 1,180,000.00 USD | 111,050.00 USD |
| `7D` | `2547.50` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 938,680.00 USD | 2,240,000.00 USD |
| `1D` | `2548.40` | 752,270,000.00 USD | 752,270,000.00 USD | 0.00 USD | 1,310,000.00 USD | 797,730.00 USD | 803,840.00 USD |
| `7D` | `2550.30` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 0.00 USD | 2,860,000.00 USD | 2,690,000.00 USD | 1,800,000.00 USD |
| `1D` | `2551.00` | 755,320,000.00 USD | 755,320,000.00 USD | 0.00 USD | 1,460,000.00 USD | 1,120,000.00 USD | 460,790.00 USD |
| `7D` | `2553.10` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 0.00 USD | 2,120,000.00 USD | 788,360.00 USD | 1,670,000.00 USD |
| `1D` | `2553.60` | 756,290,000.00 USD | 756,290,000.00 USD | 0.00 USD | 669,670.00 USD | 220,540.00 USD | 89,000.00 USD |
| `7D` | `2555.90` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 0.00 USD | 3,290,000.00 USD | 255,750.00 USD | 5,860,000.00 USD |
| `1D` | `2556.20` | 758,140,000.00 USD | 758,140,000.00 USD | 0.00 USD | 738,200.00 USD | 462,600.00 USD | 646,460.00 USD |
| `7D` | `2558.70` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 0.00 USD | 3,850,000.00 USD | 1,200,000.00 USD | 2,340,000.00 USD |
| `1D` | `2558.80` | 760,330,000.00 USD | 760,330,000.00 USD | 0.00 USD | 1,250,000.00 USD | 475,980.00 USD | 465,270.00 USD |
| `1D` | `2561.40` | 764,030,000.00 USD | 764,030,000.00 USD | 0.00 USD | 1,190,000.00 USD | 1,190,000.00 USD | 1,320,000.00 USD |
| `7D` | `2561.50` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 0.00 USD | 2,780,000.00 USD | 2,030,000.00 USD | 426,110.00 USD |
| `1D` | `2564.00` | 765,380,000.00 USD | 765,380,000.00 USD | 0.00 USD | 365,900.00 USD | 674,520.00 USD | 309,770.00 USD |
| `7D` | `2564.30` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 0.00 USD | 1,800,000.00 USD | 2,150,000.00 USD | 1,460,000.00 USD |
| `1D` | `2566.60` | 765,620,000.00 USD | 765,620,000.00 USD | 0.00 USD | 121,690.00 USD | 14,540.00 USD | 109,180.00 USD |
| `7D` | `2567.10` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 0.00 USD | 575,630.00 USD | 1,510,000.00 USD | 2,700,000.00 USD |
| `1D` | `2569.20` | 765,880,000.00 USD | 765,880,000.00 USD | 0.00 USD | 162,270.00 USD | 0.00 USD | 98,100.00 USD |
| `7D` | `2569.90` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 0.00 USD | 125,250.00 USD | 290,680.00 USD | 1,180,000.00 USD |
| `1D` | `2571.80` | 767,020,000.00 USD | 767,020,000.00 USD | 0.00 USD | 782,640.00 USD | 344,090.00 USD | 10,690.00 USD |
| `7D` | `2572.70` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 890,480.00 USD | 1,790,000.00 USD |
| `1D` | `2574.40` | 767,800,000.00 USD | 767,800,000.00 USD | 0.00 USD | 384,300.00 USD | 17,140.00 USD | 375,890.00 USD |
| `7D` | `2575.50` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 0.00 USD | 2,180,000.00 USD | 440,740.00 USD | 1,060,000.00 USD |
| `1D` | `2577.00` | 768,210,000.00 USD | 768,210,000.00 USD | 0.00 USD | 163,580.00 USD | 221,850.00 USD | 28,710.00 USD |
| `7D` | `2578.30` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 0.00 USD | 734,040.00 USD | 1,480,000.00 USD | 1,750,000.00 USD |
| `1D` | `2579.60` | 769,540,000.00 USD | 769,540,000.00 USD | 0.00 USD | 344,810.00 USD | 301,720.00 USD | 685,680.00 USD |
| `7D` | `2581.10` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 0.00 USD | 3,270,000.00 USD | 864,580.00 USD | 1,220,000.00 USD |
| `1D` | `2582.20` | 772,210,000.00 USD | 772,210,000.00 USD | 0.00 USD | 1,510,000.00 USD | 927,000.00 USD | 234,280.00 USD |
| `7D` | `2583.90` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 0.00 USD | 740,840.00 USD | 1,260,000.00 USD | 3,550,000.00 USD |
| `1D` | `2584.80` | 773,210,000.00 USD | 773,210,000.00 USD | 0.00 USD | 287,140.00 USD | 153,810.00 USD | 554,400.00 USD |
| `7D` | `2586.70` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 0.00 USD | 1,900,000.00 USD | 2,190,000.00 USD | 1,510,000.00 USD |
| `1D` | `2587.40` | 775,050,000.00 USD | 775,050,000.00 USD | 0.00 USD | 1,070,000.00 USD | 337,700.00 USD | 439,060.00 USD |
| `7D` | `2589.50` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 0.00 USD | 2,840,000.00 USD | 446,810.00 USD | 2,140,000.00 USD |
| `1D` | `2590.00` | 776,370,000.00 USD | 776,370,000.00 USD | 0.00 USD | 445,920.00 USD | 97,410.00 USD | 774,680.00 USD |
| `7D` | `2592.30` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 0.00 USD | 2,340,000.00 USD | 1,280,000.00 USD | 1,550,000.00 USD |
| `1D` | `2592.60` | 779,090,000.00 USD | 779,090,000.00 USD | 0.00 USD | 1,020,000.00 USD | 787,380.00 USD | 908,780.00 USD |
| `7D` | `2595.10` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 0.00 USD | 452,020.00 USD | 569,790.00 USD | 752,870.00 USD |
| `1D` | `2595.20` | 781,840,000.00 USD | 781,840,000.00 USD | 0.00 USD | 898,410.00 USD | 853,630.00 USD | 1,000,000.00 USD |
| `1D` | `2597.80` | 783,230,000.00 USD | 783,230,000.00 USD | 0.00 USD | 118,170.00 USD | 927,690.00 USD | 339,860.00 USD |
| `7D` | `2597.90` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 0.00 USD | 2,280,000.00 USD | 1,630,000.00 USD | 2,420,000.00 USD |
| `1D` | `2600.40` | 784,510,000.00 USD | 784,510,000.00 USD | 0.00 USD | 365,910.00 USD | 623,840.00 USD | 295,680.00 USD |
| `7D` | `2600.70` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 0.00 USD | 496,060.00 USD | 1,960,000.00 USD | 1,610,000.00 USD |
| `1D` | `2603.00` | 784,850,000.00 USD | 784,850,000.00 USD | 0.00 USD | 0.00 USD | 18,610.00 USD | 318,170.00 USD |
| `7D` | `2603.50` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 0.00 USD | 2,040,000.00 USD | 1,580,000.00 USD | 1,660,000.00 USD |
| `1D` | `2605.60` | 785,810,000.00 USD | 785,810,000.00 USD | 0.00 USD | 0.00 USD | 625,720.00 USD | 336,530.00 USD |
| `7D` | `2606.30` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 0.00 USD | 1,480,000.00 USD | 229,360.00 USD | 342,240.00 USD |
| `1D` | `2608.20` | 786,490,000.00 USD | 786,490,000.00 USD | 0.00 USD | 187,520.00 USD | 497,320.00 USD | 0.00 USD |
| `7D` | `2609.10` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 0.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD |
| `1D` | `2610.80` | 786,790,000.00 USD | 786,790,000.00 USD | 0.00 USD | 0.00 USD | 294,600.00 USD | 2,870.00 USD |
| `7D` | `2611.90` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 0.00 USD | 724,220.00 USD | 608,060.00 USD | 43,560.00 USD |
| `1D` | `2613.40` | 787,800,000.00 USD | 787,800,000.00 USD | 0.00 USD | 555,320.00 USD | 250,240.00 USD | 205,180.00 USD |
| `7D` | `2614.70` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 0.00 USD | 1,110,000.00 USD | 1,000,000.00 USD | 409,160.00 USD |
| `7D` | `2617.50` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 0.00 USD | 1,550,000.00 USD | 209,240.00 USD | 402,600.00 USD |
| `1D` | `2618.60` | 788,100,000.00 USD | 788,100,000.00 USD | 0.00 USD | 295,510.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2620.30` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 0.00 USD | 47,360.00 USD | 1,120,000.00 USD | 268,500.00 USD |
| `7D` | `2623.10` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 0.00 USD | 631,440.00 USD | 410,460.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `30.28B` | Total OI Tokens: `12,885,622.9 ETH`
  * 1h OI Change: `-0.98%` | 4h OI Change: `+0.21%` | 24h OI Change: `+1.49%`
  * Exchange Breakdown: Binance=`8.98B` | Bybit=`2.13B` | OKX=`1.84B` | Hyperliquid=`2.59B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `1.13M` | Last 24h: `2.27M` | Last 3d: `7.66M` | Last 7d: `13.85M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0099%` | **USDT OKX** | `0.0087%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0071%` |
| **USDT MEXC** | `0.0098%` | **USDT BingX** | `0.0098%` |
| **USDT Gate** | `0.0079%` | **USDT Bitget** | `0.0031%` |
| **CoinM Binance** | `0.0098%` | **CoinM OKX** | `0.0061%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `42.89%` | `57.11%` | `0.75` | 641,890,000.00 USD |
| `15M` | `Binance` | `37.98%` | `62.02%` | `0.61` | 252,730,000.00 USD |
| `15M` | `OKX` | `48.76%` | `51.24%` | `0.95` | 76,540,000.00 USD |
| `15M` | `Bybit` | `36.97%` | `63.03%` | `0.59` | 59,290,000.00 USD |
| `15M` | `KuCoin` | `45.08%` | `54.92%` | `0.82` | 1,740,000.00 USD |
| `15M` | `Gate` | `45.27%` | `54.73%` | `0.83` | 67,240,000.00 USD |
| `15M` | `Bitget` | `45.78%` | `54.22%` | `0.84` | 28,760,000.00 USD |
| `15M` | `BingX` | `51.74%` | `48.26%` | `1.07` | 8,500,000.00 USD |
| `15M` | `MEXC` | `45.24%` | `54.76%` | `0.83` | 30,850,000.00 USD |
| `15M` | `Bitunix` | `51.28%` | `48.72%` | `1.05` | 25,930,000.00 USD |
| `15M` | `Hyperliquid` | `48.25%` | `51.75%` | `0.93` | 22,030,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `81.28%` | `18.72%` | `4.34` | 6,300,000.00 USD |
| `15M` | `Crypto.com` | `45.67%` | `54.33%` | `0.84` | 6,650,000.00 USD |
| `15M` | `WhiteBIT` | `51.23%` | `48.77%` | `1.05` | 17,600,000.00 USD |
| `15M` | `HTX` | `40.04%` | `59.96%` | `0.67` | 2,350,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `48.3%` | `51.7%` | `0.93` | 10,990,000.00 USD |
| `15M` | `Bitfinex` | `35.76%` | `64.24%` | `0.56` | 345,040.00 USD |
| `15M` | `Kraken` | `70.1%` | `29.9%` | `2.34` | 2,720,000.00 USD |
| `15M` | `Aster` | `26.67%` | `73.33%` | `0.36` | 9,870,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `46.33%` | `53.67%` | `0.86` | 11,460,000.00 USD |
| `15M` | `Whale Positions` | `37.98%` | `62.02%` | `0.61` | 252,730,000.00 USD |
| `15M` | `Global Accounts` | `42.89%` | `57.11%` | `0.75` | 641,890,000.00 USD |
| `1H` | `ETH` | `45.66%` | `54.34%` | `0.84` | 4,400,000,000.00 USD |
| `1H` | `Binance` | `42.76%` | `57.24%` | `0.75` | 1,510,000,000.00 USD |
| `1H` | `OKX` | `45.66%` | `54.34%` | `0.84` | 591,870,000.00 USD |
| `1H` | `Bybit` | `44.91%` | `55.09%` | `0.82` | 425,170,000.00 USD |
| `1H` | `KuCoin` | `24.65%` | `75.35%` | `0.33` | 17,640,000.00 USD |
| `1H` | `Gate` | `48.75%` | `51.25%` | `0.95` | 495,220,000.00 USD |
| `1H` | `Bitget` | `42.92%` | `57.08%` | `0.75` | 248,950,000.00 USD |
| `1H` | `BingX` | `50.53%` | `49.47%` | `1.02` | 79,160,000.00 USD |
| `1H` | `MEXC` | `49.85%` | `50.15%` | `0.99` | 217,660,000.00 USD |
| `1H` | `Bitunix` | `47.1%` | `52.9%` | `0.89` | 212,120,000.00 USD |
| `1H` | `Hyperliquid` | `44.28%` | `55.72%` | `0.79` | 195,440,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `56.8%` | `43.2%` | `1.31` | 32,510,000.00 USD |
| `1H` | `Crypto.com` | `45.01%` | `54.99%` | `0.82` | 25,990,000.00 USD |
| `1H` | `WhiteBIT` | `68.72%` | `31.28%` | `2.20` | 72,930,000.00 USD |
| `1H` | `HTX` | `46.67%` | `53.33%` | `0.88` | 16,900,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `54.84%` | `45.16%` | `1.21` | 90,930,000.00 USD |
| `1H` | `Bitfinex` | `41.95%` | `58.05%` | `0.72` | 2,800,000.00 USD |
| `1H` | `Kraken` | `49%` | `51%` | `0.96` | 31,380,000.00 USD |
| `1H` | `Aster` | `39.47%` | `60.53%` | `0.65` | 57,310,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `49.59%` | `50.41%` | `0.98` | 71,720,000.00 USD |
| `1H` | `Whale Positions` | `42.76%` | `57.24%` | `0.75` | 1,510,000,000.00 USD |
| `1H` | `Global Accounts` | `45.66%` | `54.34%` | `0.84` | 4,400,000,000.00 USD |
| `4H` | `ETH` | `50.50%` | `49.50%` | `1.02` | 20,620,000,000.00 USD |
| `4H` | `Binance` | `50.57%` | `49.43%` | `1.02` | 6,590,000,000.00 USD |
| `4H` | `OKX` | `50.31%` | `49.69%` | `1.01` | 2,960,000,000.00 USD |
| `4H` | `Bybit` | `49.83%` | `50.17%` | `0.99` | 2,050,000,000.00 USD |
| `4H` | `KuCoin` | `47.84%` | `52.16%` | `0.92` | 83,260,000.00 USD |
| `4H` | `Gate` | `50.24%` | `49.76%` | `1.01` | 2,420,000,000.00 USD |
| `4H` | `Bitget` | `49.84%` | `50.16%` | `0.99` | 1,230,000,000.00 USD |
| `4H` | `BingX` | `49.14%` | `50.86%` | `0.97` | 374,260,000.00 USD |
| `4H` | `MEXC` | `54.39%` | `45.61%` | `1.19` | 1,120,000,000.00 USD |
| `4H` | `Bitunix` | `47.68%` | `52.32%` | `0.91` | 1,060,000,000.00 USD |
| `4H` | `Hyperliquid` | `52.07%` | `47.93%` | `1.09` | 924,120,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.36%` | `51.64%` | `0.94` | 131,600,000.00 USD |
| `4H` | `Crypto.com` | `47.87%` | `52.13%` | `0.92` | 133,370,000.00 USD |
| `4H` | `WhiteBIT` | `53.94%` | `46.06%` | `1.17` | 352,570,000.00 USD |
| `4H` | `HTX` | `47.38%` | `52.62%` | `0.90` | 82,620,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `50.99%` | `49.01%` | `1.04` | 422,310,000.00 USD |
| `4H` | `Bitfinex` | `66.71%` | `33.29%` | `2.00` | 28,630,000.00 USD |
| `4H` | `Kraken` | `52.32%` | `47.68%` | `1.10` | 157,580,000.00 USD |
| `4H` | `Aster` | `48.76%` | `51.24%` | `0.95` | 218,100,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.18%` | `49.82%` | `1.01` | 260,210,000.00 USD |
| `4H` | `Whale Positions` | `50.57%` | `49.43%` | `1.02` | 6,590,000,000.00 USD |
| `4H` | `Global Accounts` | `50.50%` | `49.50%` | `1.02` | 20,620,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `2341.25` | `2340.35` | `2341.25` | `2346.75` | `2333.25` | 199,004,346.85 USD | 81,689,385.17 USD | 117,314,961.68 USD | -35,625,576.50 USD | `-17.90%` | `0B / 6S` |
| `0:00 UTC` | `2361.25` | `2356.05` | `2361.25` | `2364.75` | `2343.75` | 331,920,007.02 USD | 204,886,521.51 USD | 127,033,485.50 USD | 77,853,036.01 USD | `+23.46%` | `11B / 0S` |
| `5:00 UTC` | `2357.75` | `2358.45` | `2357.75` | `2365.75` | `2355.25` | 136,642,531.53 USD | 60,568,643.70 USD | 76,073,887.82 USD | -15,505,244.12 USD | `-11.35%` | `1B / 5S` |
| `0:00 UTC` | `2364.75` | `2364.47` | `2364.75` | `2369.25` | `2356.75` | 211,703,599.24 USD | 122,647,689.31 USD | 89,055,909.93 USD | 33,591,779.37 USD | `+15.87%` | `9B / 0S` |
| `5:00 UTC` | `2370.25` | `2367.30` | `2370.25` | `2372.25` | `2362.75` | 152,368,912.49 USD | 65,939,044.63 USD | 86,429,867.86 USD | -20,490,823.24 USD | `-13.45%` | `0B / 0S` |
| `0:00 UTC` | `2367.25` | `2370.68` | `2367.25` | `2378.75` | `2362.25` | 227,963,041.65 USD | 108,724,843.75 USD | 119,238,197.91 USD | -10,513,354.16 USD | `-4.61%` | `6B / 3S` |
| `5:00 UTC` | `2360.25` | `2359.15` | `2360.25` | `2367.25` | `2354.75` | 178,447,053.53 USD | 59,723,171.00 USD | 118,723,882.53 USD | -59,000,711.54 USD | `-33.06%` | `0B / 9S` |
| `0:00 UTC` | `2358.25` | `2354.41` | `2358.25` | `2359.25` | `2350.25` | 125,220,561.61 USD | 53,594,674.80 USD | 71,625,886.81 USD | -18,031,212.02 USD | `-14.40%` | `0B / 1S` |
| `5:00 UTC` | `2353.75` | `2353.63` | `2353.75` | `2358.25` | `2350.75` | 70,925,128.95 USD | 26,607,996.94 USD | 44,317,132.01 USD | -17,709,135.06 USD | `-24.97%` | `0B / 2S` |
| `0:00 UTC` | `2350.75` | `2351.46` | `2350.75` | `2353.75` | `2349.25` | 70,494,165.00 USD | 28,961,502.64 USD | 41,532,662.36 USD | -12,571,159.73 USD | `-17.83%` | `0B / 2S` |

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
  * `2026-10-29 22:05:54 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [bea.gov] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `2274.92` (Risk Distance: `18.76` pts)
  * +2.5R Take Profit: `2340.58`
  * Mathematical Lot Sizing: **`0.53 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2335.58` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2354.34` (Risk Distance: `18.76` pts)
  * +2.5R Take Profit: `2288.68`
  * Mathematical Lot Sizing: **`0.53 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2369.61`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
