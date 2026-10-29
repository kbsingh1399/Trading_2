# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 01:14:46 IST` (`2026-10-29 19:44:46 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2330.30` | **Live Ask Quote**: `2333.20` | **Mid Price**: `2331.75`
- **Spread Points**: `290.00` | **Spread BPS**: `12.44 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2324.08` | VWAP Z-Score: `+0.15` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `10.55` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `43.14` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2378.72` | Lower -3.00σ Band: `2269.44`
  * Upper +2.51σ Band: `2369.80` | Lower -2.51σ Band: `2278.36`
  * Upper +2.01σ Band: `2360.69` | Lower -2.01σ Band: `2287.47`
  * Upper +2.00σ Band: `2360.51` | Lower -2.00σ Band: `2287.65`
  * Upper +1.28σ Band: `2347.39` | Lower -1.28σ Band: `2300.77`
  * Upper +1.00σ Band: `2342.29` | Lower -1.00σ Band: `2305.87`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2331.80` | EMA-20=`2335.36` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2332.19` (Slope: `+0.0000`) | EMA-100=`2331.68`
  * Institutional Anchors: EMA-144=`2331.45` | EMA-200=`2330.40` (Slope: `+0.0316`) | EMA-233=`2329.58`
- **Range Boundaries**: 24H High=`2387.80` | 24H Low=`2288.80` | Weekly High=`2387.80` | Weekly Low=`2288.80`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2337.30` (Distance: `-0.19%`)
  * Point of Control (POC) = `2318.94` (Distance: `+0.60%`)
  * Value Area Low (VAL) = `2297.70` (Distance: `+1.53%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `2322.42` - `2341.08`
  * Optimal Trade Entry (OTE 0.705): `2336.41`
  * Structural Invalidation Anchor (0.786): `2350.40`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2330.06` | `2336.43` | `2330.06` | `2334.08` | `8,799` | 20,537,364.06 USD | 3,554,381.72 USD | `+17.31%` | -345,322,488.49 USD | `+0.41` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `2334.08` | `2335.00` | `2332.32` | `2333.17` | `3,131` | 7,307,239.54 USD | -1,799,785.12 USD | `-24.63%` | -347,122,273.61 USD | `+0.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `2333.18` | `2336.45` | `2333.18` | `2334.99` | `2,728` | 6,369,898.54 USD | 1,557,650.25 USD | `+24.45%` | -345,564,623.36 USD | `+0.31` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `2330.22` | `2331.00` | `2326.34` | `2326.73` | `12,437` | 28,953,047.89 USD | -2,816,984.30 USD | `-9.73%` | -348,546,511.36 USD | `+0.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `2326.74` | `2331.65` | `2325.76` | `2330.06` | `12,302` | 28,646,242.16 USD | -330,358.86 USD | `-1.15%` | -348,876,870.21 USD | `+0.14` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `2330.06` | `2336.45` | `2330.06` | `2334.34` | `14,361` | 33,521,527.16 USD | 2,713,192.69 USD | `+8.09%` | -346,163,677.53 USD | `+0.34` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `2352.18` | `2353.79` | `2330.81` | `2340.62` | `199,552` | 467,616,004.62 USD | -38,816,598.96 USD | `-8.30%` | -317,086,135.71 USD | `-0.52` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2340.61` | `2342.29` | `2323.01` | `2330.23` | `146,197` | 340,744,443.34 USD | -42,605,787.87 USD | `-12.50%` | -359,691,923.58 USD | `-0.55` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2330.22` | `2336.45` | `2325.76` | `2334.91` | `39,365` | 91,740,944.43 USD | 181,461.24 USD | `+0.20%` | -359,510,462.34 USD | `+0.39` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2309.10` | `2330.05` | `2308.88` | `2324.26` | `409,016` | 949,400,649.22 USD | -49,162,247.72 USD | `-5.18%` | -277,081,181.03 USD | `+0.30` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -173,041,008.80 USD | `+1.51` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2334.34` | `639,982` | 1,502,056,738.06 USD | -187,079,259.76 USD | `-12.45%` | -360,120,268.56 USD | `-1.25` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2358.56` | `2360.38` | `2292.20` | `2308.04` | `812,683` | 1,883,052,517.85 USD | -183,572,583.45 USD | `-9.75%` | -193,002,187.18 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2308.03` | `2334.83` | `2303.75` | `2309.10` | `525,175` | 1,216,920,375.04 USD | -34,916,746.14 USD | `-2.87%` | -227,918,933.31 USD | `+0.53` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2309.10` | `2330.05` | `2308.88` | `2324.26` | `409,016` | 949,400,649.22 USD | -49,162,247.72 USD | `-5.18%` | -277,081,181.03 USD | `+0.30` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `2324.26` | `2372.42` | `2312.25` | `2368.02` | `990,448` | 2,320,004,350.90 USD | 104,040,172.24 USD | `+4.48%` | -173,041,008.80 USD | `+1.51` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2334.34` | `639,982` | 1,502,056,738.06 USD | -187,079,259.76 USD | `-12.45%` | -360,120,268.56 USD | `-1.25` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`2331.75`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2333.10` | `109.7575` | 256,075.22 USD | 8,793,056.78 USD | `9 orders` | `-0.08%` | `-` |
| `BID` | `2333.20` | `387.3989` | 903,879.11 USD | 8,536,981.55 USD | `12 orders` | `-0.08%` | `-` |
| `BID` | `2333.30` | `234.6708` | 547,557.38 USD | 7,633,102.44 USD | `19 orders` | `-0.07%` | `-` |
| `BID` | `2333.40` | `98.6759` | 230,250.35 USD | 7,085,545.06 USD | `9 orders` | `-0.07%` | `-` |
| `BID` | `2333.50` | `277.0387` | 646,469.81 USD | 6,855,294.72 USD | `11 orders` | `-0.07%` | `-` |
| `BID` | `2333.60` | `225.4315` | 526,066.95 USD | 6,208,824.91 USD | `16 orders` | `-0.06%` | `-` |
| `BID` | `2333.70` | `180.6801` | 421,653.15 USD | 5,682,757.96 USD | `16 orders` | `-0.06%` | `-` |
| `BID` | `2333.80` | `359.8165` | 839,739.75 USD | 5,261,104.81 USD | `12 orders` | `-0.05%` | `-` |
| `BID` | `2333.90` | `128.9950` | 301,061.43 USD | 4,421,365.07 USD | `15 orders` | `-0.05%` | `-` |
| `BID` | `2334.00` | `549.8267` | 1,283,295.52 USD | 4,120,303.64 USD | `23 orders` | `-0.04%` | `-` |
| `BID` | `2334.10` | `336.8862` | 786,326.08 USD | 2,837,008.12 USD | `26 orders` | `-0.04%` | `-` |
| `BID` | `2334.20` | `239.4007` | 558,809.11 USD | 2,050,682.04 USD | `22 orders` | `-0.04%` | `-` |
| `BID` | `2334.30` | `128.5244` | 300,014.51 USD | 1,491,872.92 USD | `9 orders` | `-0.03%` | `-` |
| `BID` | `2334.40` | `147.1831` | 343,584.23 USD | 1,191,858.42 USD | `7 orders` | `-0.03%` | `-` |
| `BID` | `2334.50` | `97.9086` | 228,567.63 USD | 848,274.19 USD | `11 orders` | `-0.02%` | `-` |
| `BID` | `2334.60` | `54.9106` | 128,194.29 USD | 619,706.56 USD | `10 orders` | `-0.02%` | `-` |
| `BID` | `2334.70` | `106.1502` | 247,828.87 USD | 491,512.28 USD | `10 orders` | `-0.01%` | `-` |
| `BID` | `2334.80` | `24.8723` | 58,071.85 USD | 243,683.40 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `2334.90` | `34.3012` | 80,089.87 USD | 185,611.56 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `2335.00` | `45.1913` | 105,521.69 USD | 105,521.69 USD | `10 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2335.05` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,335.05` | `0.00%` | `-` |
| `ASK` | `2335.10` | `617.5755` | 1,442,100.55 USD | 1,442,100.55 USD | `24 orders` | `+0.00%` | `-` |
| `ASK` | `2335.20` | `63.7997` | 148,985.06 USD | 1,591,085.61 USD | `13 orders` | `+0.01%` | `-` |
| `ASK` | `2335.30` | `297.2135` | 694,082.69 USD | 2,285,168.30 USD | `20 orders` | `+0.01%` | `-` |
| `ASK` | `2335.40` | `133.0462` | 310,716.10 USD | 2,595,884.39 USD | `16 orders` | `+0.01%` | `-` |
| `ASK` | `2335.50` | `253.3669` | 591,738.39 USD | 3,187,622.79 USD | `18 orders` | `+0.02%` | `-` |
| `ASK` | `2335.60` | `231.0398` | 539,616.56 USD | 3,727,239.34 USD | `21 orders` | `+0.02%` | `-` |
| `ASK` | `2335.70` | `391.7431` | 914,994.36 USD | 4,642,233.70 USD | `25 orders` | `+0.03%` | `-` |
| `ASK` | `2335.80` | `373.7427` | 872,988.20 USD | 5,515,221.90 USD | `25 orders` | `+0.03%` | `-` |
| `ASK` | `2335.90` | `289.8234` | 676,998.48 USD | 6,192,220.38 USD | `19 orders` | `+0.04%` | `-` |
| `ASK` | `2336.00` | `254.6456` | 594,852.12 USD | 6,787,072.50 USD | `18 orders` | `+0.04%` | `-` |
| `ASK` | `2336.10` | `265.8641` | 621,085.12 USD | 7,408,157.63 USD | `17 orders` | `+0.04%` | `-` |
| `ASK` | `2336.20` | `128.8402` | 300,996.48 USD | 7,709,154.10 USD | `22 orders` | `+0.05%` | `-` |
| `ASK` | `2336.30` | `436.1105` | 1,018,884.96 USD | 8,728,039.06 USD | `16 orders` | `+0.05%` | `-` |
| `ASK` | `2336.40` | `245.5492` | 573,701.15 USD | 9,301,740.21 USD | `18 orders` | `+0.06%` | `-` |
| `ASK` | `2336.50` | `236.3987` | 552,345.56 USD | 9,854,085.78 USD | `18 orders` | `+0.06%` | `-` |
| `ASK` | `2336.60` | `169.5918` | 396,268.20 USD | 10,250,353.98 USD | `22 orders` | `+0.07%` | `-` |
| `ASK` | `2336.70` | `174.9612` | 408,831.84 USD | 10,659,185.81 USD | `13 orders` | `+0.07%` | `-` |
| `ASK` | `2336.80` | `130.7038` | 305,428.64 USD | 10,964,614.45 USD | `13 orders` | `+0.07%` | `-` |
| `ASK` | `2336.90` | `603.6440` | 1,410,655.66 USD | 12,375,270.12 USD | `18 orders` | `+0.08%` | `-` |
| `ASK` | `2337.00` | `650.0822` | 1,519,242.10 USD | 13,894,512.22 USD | `22 orders` | `+0.08%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:14:07 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 01:14:07 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1918.00` | `4,184.01` | 8,024,935.59 USD | `TRIGGER_STOP` | `0x6ea486a342` | `2026-10-30 01:14:07 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1919.63` | `8,092.45` | 15,534,510.75 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 01:14:07 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `8,500.00` | 16,371,850.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-30 01:14:07 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2040.71` | `7,964.66` | 16,253,558.97 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-30 01:14:07 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2115.23` | `7,500.00` | 15,864,241.49 USD | `AT_RISK_LIQ` | `0x524ed67d71` | `2026-10-30 01:14:07 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2171.17` | `48,499.51` | 105,300,776.77 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 01:14:07 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2180.23` | `44,734.81` | 97,532,371.64 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 01:14:07 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2250.00` | `6,500.00` | 14,625,000.00 USD | `TRIGGER_STOP` | `0x6eae4120a8` | `2026-10-30 01:14:07 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2292.00` | `2,500.00` | 5,730,000.00 USD | `TRIGGER_STOP` | `0x934de82f50` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2295.30` | `5,287.01` | 12,135,262.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2295.80` | `1,928.50` | 4,427,446.63 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2303.00` | `908.97` | 2,093,354.23 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x0c4a3a7ac7` | `2026-10-30 01:14:07 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2307.20` | `599,999.99` | 1,384,319,976.93 USD | `TRIGGER_STOP` | `0x069604ebfb` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2307.90` | `1,303.69` | 3,008,777.38 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 01:14:07 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2310.00` | `2,000.00` | 4,620,000.00 USD | `TRIGGER_STOP` | `0x524ed67d71` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2312.20` | `604.97` | 1,398,809.32 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2313.20` | `345.88` | 800,091.47 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2314.20` | `1,015.35` | 2,349,715.10 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x674982e841` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2316.70` | `932.13` | 2,159,456.07 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2319.00` | `2,718.85` | 6,305,008.05 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 01:14:07 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2319.00` | `2,500.00` | 5,797,500.00 USD | `TRIGGER_STOP` | `0x524ed67d71` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2320.40` | `436.26` | 1,012,295.38 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2322.80` | `1,724.11` | 4,004,769.21 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2322.90` | `604.35` | 1,403,849.26 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2323.60` | `676.22` | 1,571,268.51 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2325.20` | `604.89` | 1,406,497.20 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2326.40` | `1,291.08` | 3,003,558.74 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2326.60` | `1,387.33` | 3,227,753.83 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2328.20` | `436.25` | 1,015,667.94 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2328.60` | `859.91` | 2,002,375.02 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2329.10` | `447.77` | 1,042,899.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2329.50` | `644.67` | 1,501,753.87 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2331.40` | `408.51` | 952,391.59 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x76bf72092b` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2331.70` | `402.92` | 939,476.91 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2332.40` | `429.21` | 1,001,097.57 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2335.60` | `410.13` | 957,908.27 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x823ecdcdfc` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2338.60` | `328.57` | 768,404.56 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2339.20` | `428.07` | 1,001,338.30 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2339.70` | `403.06` | 943,034.80 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2340.50` | `641.66` | 1,501,806.63 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2340.70` | `406.90` | 952,423.57 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x76bf72092b` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2342.30` | `854.86` | 2,002,338.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2342.30` | `436.19` | 1,021,697.21 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2343.00` | `1,388.64` | 3,253,584.69 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2343.90` | `1,281.44` | 3,003,578.23 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2344.70` | `604.58` | 1,417,565.76 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2344.80` | `680.85` | 1,596,452.16 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2344.90` | `328.23` | 769,661.84 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2347.10` | `643.11` | 1,509,444.42 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2347.20` | `1,706.17` | 4,004,715.42 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2348.70` | `604.58` | 1,419,984.09 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2349.80` | `436.05` | 1,024,630.29 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2350.70` | `395.93` | 930,708.89 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x7b7f72a28f` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2350.80` | `2,721.74` | 6,398,255.34 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2352.70` | `938.18` | 2,207,257.73 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2354.40` | `339.83` | 800,091.51 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2354.60` | `325.96` | 767,507.77 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2355.30` | `604.89` | 1,424,697.42 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2359.30` | `561.62` | 1,325,020.39 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x7b7f72a28f` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2359.40` | `5,287.01` | 12,474,159.60 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2361.80` | `1,356.30` | 3,203,314.54 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 01:14:07 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2374.20` | `2,014.03` | 4,781,706.94 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 01:14:07 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2440.00` | `4,002.10` | 9,765,127.17 USD | `TRIGGER_STOP` | `0xfb941d2344` | `2026-10-30 01:14:07 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2585.93` | `6,224.05` | 16,094,954.84 USD | `AT_RISK_LIQ` | `0x08bf75d170` | `2026-10-30 01:14:07 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2658.68` | `9,700.00` | 25,789,198.84 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-30 01:14:07 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2709.03` | `8,500.00` | 23,026,771.56 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-30 01:14:07 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 248,400,221.48 USD | `106,417.71` | `2322.74` | `2333.80` | `3827.18` | -1,219,209.33 USD | `-0.49%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 152,182,345.33 USD | `65,205.17` | `2375.30` | `2333.80` | `4376.61` | 2,699,917.77 USD | `+1.77%` | `5X Cross` |
| `6` | `0x77dd...e0e9` | `LONG` | 113,188,160.87 USD | `48,499.51` | `2610.31` | `2333.80` | `2171.19` | -13,410,722.99 USD | `-11.85%` | `10X Cross` |
| `7` | `0x0392...d7d9` | `LONG` | 104,405,238.95 USD | `44,734.81` | `2518.71` | `2333.80` | `2180.25` | -8,269,067.62 USD | `-7.92%` | `9X Cross` |
| `15` | `0xde8d...9524` | `LONG` | 70,675,193.06 USD | `30,282.40` | `2134.45` | `2333.80` | `1787.14` | 6,038,862.48 USD | `+8.54%` | `20X Cross` |
| `18` | `0x7fda...17d1` | `SHORT` | 64,901,257.14 USD | `27,814.03` | `2437.59` | `2333.80` | `3628.96` | 2,898,144.68 USD | `+4.47%` | `25X Cross` |
| `25` | `0xdf95...7d72` | `SHORT` | 52,852,341.62 USD | `22,650.36` | `2402.54` | `2333.80` | `3969.97` | 1,566,077.45 USD | `+2.96%` | `25X Cross` |
| `28` | `0xeced...6210` | `SHORT` | 43,620,540.60 USD | `18,687.58` | `2522.09` | `2333.80` | `3350.49` | 3,511,371.86 USD | `+8.05%` | `20X Cross` |
| `34` | `0xb695...a92d` | `SHORT` | 38,985,240.99 USD | `16,704.62` | `2557.74` | `2333.80` | `4031.01` | 3,740,924.06 USD | `+9.60%` | `20X Cross` |
| `35` | `0x6046...b21d` | `LONG` | 37,173,401.60 USD | `15,927.59` | `2410.19` | `2333.80` | `1547.38` | -1,215,218.05 USD | `-3.27%` | `6X Cross` |
| `38` | `0x45d2...4029` | `SHORT` | 32,556,510.00 USD | `13,950.00` | `2443.60` | `2333.80` | `4996.57` | 1,531,772.46 USD | `+4.70%` | `20X Cross` |
| `43` | `0x0622...8088` | `LONG` | 28,935,399.95 USD | `12,397.93` | `2342.25` | `2333.80` | `1521.12` | -103,752.46 USD | `-0.36%` | `5X Cross` |
| `45` | `0xbd1c...ff0e` | `LONG` | 28,006,800.00 USD | `12,000.00` | `2419.91` | `2333.80` | `1521.02` | -1,032,232.39 USD | `-3.69%` | `20X Cross` |
| `46` | `0x2371...0883` | `LONG` | 28,006,800.00 USD | `12,000.00` | `2421.77` | `2333.80` | `1280.11` | -1,054,494.85 USD | `-3.77%` | `20X Cross` |
| `50` | `0x09dc...c094` | `LONG` | 25,676,200.00 USD | `11,000.00` | `2465.31` | `2333.80` | `1638.08` | -1,442,223.04 USD | `-5.62%` | `20X Cross` |
| `51` | `0xa9de...e049` | `LONG` | 25,672,900.00 USD | `11,000.00` | `2481.81` | `2333.80` | `1644.76` | -1,627,079.46 USD | `-6.34%` | `20X Cross` |
| `52` | `0x0c5d...36b3` | `LONG` | 25,672,900.00 USD | `11,000.00` | `2482.20` | `2333.80` | `1645.09` | -1,631,353.24 USD | `-6.35%` | `20X Cross` |
| `53` | `0x6c93...59a4` | `LONG` | 25,667,400.00 USD | `11,000.00` | `2441.15` | `2333.80` | `1603.05` | -1,185,272.73 USD | `-4.62%` | `20X Cross` |
| `55` | `0xa61c...66b9` | `LONG` | 25,412,592.00 USD | `10,888.00` | `2398.32` | `2333.80` | `1403.52` | -700,365.39 USD | `-2.76%` | `10X Cross` |
| `59` | `0x4487...c92d` | `SHORT` | 24,646,154.37 USD | `10,560.07` | `2373.98` | `2333.80` | `2862.64` | 423,345.15 USD | `+1.72%` | `10X Cross` |
| `66` | `0xa2ce...3126` | `LONG` | 23,382,091.27 USD | `10,016.88` | `2162.83` | `2333.80` | `1437.30` | 1,717,289.22 USD | `+7.34%` | `10X Cross` |
| `67` | `0xec7f...df39` | `LONG` | 23,342,000.00 USD | `10,000.00` | `2719.35` | `2333.80` | `1721.61` | -3,851,548.52 USD | `-16.50%` | `20X Cross` |
| `68` | `0x6646...6de5` | `LONG` | 23,339,000.00 USD | `10,000.00` | `1765.80` | `2333.80` | `1732.68` | 5,680,942.55 USD | `+24.34%` | `25X Cross` |
| `69` | `0x15a4...dfdb` | `LONG` | 23,339,000.00 USD | `10,000.00` | `1761.94` | `2333.80` | `11.87` | 5,719,518.97 USD | `+24.51%` | `20X Cross` |
| `76` | `0xaeaa...2416` | `SHORT` | 22,638,830.00 USD | `9,700.00` | `2311.92` | `2333.80` | `2658.69` | -213,147.60 USD | `-0.94%` | `25X Cross` |
| `81` | `0xca49...53c8` | `SHORT` | 21,621,674.40 USD | `9,264.26` | `2549.47` | `2333.80` | `3728.05` | 1,997,350.34 USD | `+9.24%` | `25X Cross` |
| `83` | `0xba5d...a352` | `SHORT` | 21,131,325.03 USD | `9,054.12` | `2493.89` | `2333.80` | `2923.69` | 1,448,682.23 USD | `+6.86%` | `20X Cross` |
| `84` | `0xea00...a918` | `LONG` | 21,013,760.09 USD | `9,003.83` | `2003.01` | `2333.80` | `1232.02` | 2,978,981.22 USD | `+14.18%` | `5X Cross` |
| `93` | `0xb37f...66ca` | `SHORT` | 19,837,300.00 USD | `8,500.00` | `2308.30` | `2333.80` | `2709.05` | -216,745.81 USD | `-1.09%` | `25X Cross` |
| `102` | `0x9eec...daab` | `LONG` | 18,886,164.71 USD | `8,092.45` | `1658.44` | `2333.80` | `1918.71` | 5,465,300.18 USD | `+28.94%` | `15X Cross` |
| `109` | `0x218a...7da2` | `SHORT` | 18,666,026.68 USD | `7,997.78` | `2208.16` | `2333.80` | `2877.26` | -1,005,631.46 USD | `-5.39%` | `10X Cross` |
| `110` | `0x5f91...65aa` | `LONG` | 18,588,471.47 USD | `7,964.66` | `1626.99` | `2333.80` | `2040.72` | 5,630,028.40 USD | `+30.29%` | `16X Cross` |
| `111` | `0xecb6...2b00` | `SHORT` | 18,230,603.83 USD | `7,812.89` | `2327.65` | `2333.80` | `5853.30` | -44,871.03 USD | `-0.25%` | `15X Cross` |
| `114` | `0xcf53...ee11` | `SHORT` | 17,748,920.50 USD | `7,603.63` | `1862.69` | `2333.80` | `3992.12` | -3,585,656.56 USD | `-20.20%` | `7X Cross` |
| `115` | `0x524e...0de0` | `LONG` | 17,504,250.00 USD | `7,500.00` | `2320.35` | `2333.80` | `2115.25` | 101,563.78 USD | `+0.58%` | `10X Cross` |
| `119` | `0x939f...04d2` | `LONG` | 16,859,656.93 USD | `7,223.81` | `2500.18` | `2333.80` | `1776.52` | -1,201,233.25 USD | `-7.12%` | `25X Cross` |
| `123` | `0xec0b...b078` | `LONG` | 16,356,202.63 USD | `7,007.80` | `2065.97` | `2333.80` | `1004.73` | 1,878,273.04 USD | `+11.48%` | `25X Cross` |
| `124` | `0x1ee7...edf5` | `LONG` | 16,337,090.00 USD | `7,000.00` | `2330.22` | `2333.80` | `2153.94` | 25,527.80 USD | `+0.16%` | `25X Cross` |
| `130` | `0x418a...8888` | `SHORT` | 15,696,054.33 USD | `6,724.38` | `2494.55` | `2333.80` | `2957.76` | 1,078,268.84 USD | `+6.87%` | `25X Cross` |
| `131` | `0x4ff9...38d3` | `LONG` | 15,319,884.31 USD | `6,564.10` | `2447.40` | `2333.80` | `1670.70` | -745,138.43 USD | `-4.86%` | `3X Isolated` |
| `133` | `0xf78c...c581` | `LONG` | 15,170,671.95 USD | `6,500.22` | `2521.53` | `2333.80` | `1914.18` | -1,219,868.99 USD | `-8.04%` | `20X Cross` |
| `140` | `0x799f...5f4c` | `LONG` | 14,730,279.39 USD | `6,310.90` | `2390.33` | `2333.80` | `1712.12` | -354,885.22 USD | `-2.41%` | `20X Cross` |
| `143` | `0x08bf...7872` | `SHORT` | 14,523,192.20 USD | `6,224.05` | `2258.00` | `2333.80` | `2585.94` | -469,276.10 USD | `-3.23%` | `20X Cross` |
| `150` | `0xd9e7...4aff` | `LONG` | 14,003,400.00 USD | `6,000.00` | `2480.18` | `2333.80` | `1408.47` | -877,724.33 USD | `-6.27%` | `20X Cross` |
| `157` | `0x0c4a...1b19` | `LONG` | 13,319,846.90 USD | `5,706.39` | `2382.15` | `2333.80` | `2185.23` | -273,624.27 USD | `-2.05%` | `25X Isolated` |
| `174` | `0x645b...87b8` | `SHORT` | 11,841,086.69 USD | `5,073.52` | `2421.68` | `2333.80` | `6212.52` | 445,367.43 USD | `+3.76%` | `10X Cross` |
| `181` | `0x45ab...6cbc` | `LONG` | 11,484,886.05 USD | `4,920.96` | `2727.66` | `2333.80` | `1364.33` | -1,937,857.75 USD | `-16.87%` | `7X Cross` |
| `184` | `0xfb18...eb17` | `SHORT` | 11,371,705.20 USD | `4,872.45` | `2315.54` | `2333.80` | `2708.42` | -89,332.17 USD | `-0.79%` | `25X Cross` |
| `186` | `0x64b7...9da9` | `LONG` | 11,335,862.69 USD | `4,856.84` | `2604.61` | `2333.80` | `1432.11` | -1,314,351.72 USD | `-11.59%` | `25X Cross` |
| `193` | `0x5559...d43b` | `SHORT` | 11,099,854.06 USD | `4,755.93` | `2262.69` | `2333.80` | `2864.55` | -338,648.18 USD | `-3.05%` | `25X Cross` |
| `207` | `0xe091...6705` | `SHORT` | 10,502,550.47 USD | `4,500.00` | `2467.33` | `2333.80` | `2572.99` | 600,458.04 USD | `+5.72%` | `20X Cross` |
| `216` | `0xfe7c...b7ae` | `SHORT` | 10,275,055.45 USD | `4,402.58` | `2440.17` | `2333.80` | `4218.98` | 468,032.42 USD | `+4.56%` | `25X Cross` |
| `227` | `0xc179...e0c8` | `LONG` | 10,054,982.51 USD | `4,309.16` | `2342.89` | `2333.80` | `881.12` | -40,896.29 USD | `-0.41%` | `10X Cross` |
| `233` | `0x12d2...f97f` | `LONG` | 9,952,971.19 USD | `4,264.34` | `2623.90` | `2333.80` | `1838.07` | -1,236,263.22 USD | `-12.42%` | `20X Cross` |
| `241` | `0x28bb...fca6` | `SHORT` | 9,825,239.54 USD | `4,209.61` | `1896.10` | `2333.80` | `3047.05` | -1,843,356.98 USD | `-18.76%` | `20X Cross` |
| `242` | `0x6ea4...0ea7` | `SHORT` | 9,766,321.51 USD | `4,184.01` | `2602.13` | `2333.80` | `3426.01` | 1,121,025.16 USD | `+11.48%` | `20X Cross` |
| `253` | `0x5e9e...35ee` | `SHORT` | 9,353,234.25 USD | `4,007.56` | `1796.39` | `2333.80` | `2586.50` | -2,154,084.16 USD | `-23.03%` | `20X Cross` |
| `254` | `0xfb94...0ddf` | `SHORT` | 9,340,504.22 USD | `4,002.10` | `2382.44` | `2333.80` | `5105.40` | 194,279.93 USD | `+2.08%` | `20X Cross` |
| `255` | `0x95fe...f8fa` | `LONG` | 9,335,600.00 USD | `4,000.00` | `2341.35` | `2333.80` | `2259.00` | -29,816.51 USD | `-0.32%` | `20X Isolated` |
| `256` | `0x3dc9...54b0` | `SHORT` | 9,334,756.97 USD | `3,999.69` | `2480.32` | `2333.80` | `5942.57` | 585,779.59 USD | `+6.28%` | `20X Cross` |
| `257` | `0x8cc9...2b6a` | `SHORT` | 9,333,600.00 USD | `4,000.00` | `1791.18` | `2333.80` | `3864.92` | -2,168,853.33 USD | `-23.24%` | `25X Cross` |
| `258` | `0x77ee...2902` | `SHORT` | 9,295,319.17 USD | `3,982.23` | `2476.53` | `2333.80` | `4269.80` | 566,802.42 USD | `+6.10%` | `25X Cross` |
| `269` | `0xf02d...5eb3` | `LONG` | 9,000,255.76 USD | `3,855.99` | `2513.67` | `2333.80` | `330.72` | -692,456.56 USD | `-7.69%` | `20X Cross` |
| `271` | `0x4b67...f4e7` | `LONG` | 8,917,462.91 USD | `3,820.84` | `2591.51` | `2333.80` | `1592.25` | -984,310.63 USD | `-11.04%` | `20X Cross` |
| `291` | `0x382b...3e39` | `SHORT` | 8,307,698.06 USD | `3,560.34` | `2299.51` | `2333.80` | `3754.37` | -120,655.19 USD | `-1.45%` | `25X Cross` |
| `292` | `0x8ae4...3d60` | `LONG` | 8,305,546.47 USD | `3,558.20` | `2482.21` | `2333.80` | `349.77` | -526,651.56 USD | `-6.34%` | `10X Cross` |
| `318` | `0x9c06...0560` | `SHORT` | 7,710,225.36 USD | `3,303.58` | `2270.55` | `2333.80` | `3309.68` | -209,261.42 USD | `-2.71%` | `25X Cross` |
| `327` | `0x984e...14c2` | `SHORT` | 7,263,067.39 USD | `3,111.99` | `2357.50` | `2333.80` | `2434.97` | 73,455.37 USD | `+1.01%` | `20X Cross` |
| `333` | `0x9c2a...f6a8` | `SHORT` | 7,138,090.28 USD | `3,058.48` | `2543.83` | `2333.80` | `2592.83` | 642,170.34 USD | `+9.00%` | `20X Cross` |
| `338` | `0x39b4...5c34` | `SHORT` | 7,003,737.32 USD | `3,000.91` | `2329.97` | `2333.80` | `2401.72` | -11,693.57 USD | `-0.17%` | `25X Cross` |
| `339` | `0x007d...67a0` | `LONG` | 7,001,640.00 USD | `3,000.00` | `2400.00` | `2333.80` | `1489.07` | -198,360.00 USD | `-2.83%` | `25X Cross` |
| `340` | `0x4a20...3c26` | `LONG` | 7,001,400.00 USD | `3,000.00` | `2428.72` | `2333.80` | `260.68` | -284,760.28 USD | `-4.07%` | `20X Cross` |
| `377` | `0xf517...c032` | `SHORT` | 6,390,656.08 USD | `2,738.07` | `2053.90` | `2333.80` | `5542.31` | -766,914.17 USD | `-12.00%` | `25X Cross` |
| `396` | `0xc619...10f5` | `LONG` | 6,068,140.00 USD | `2,600.00` | `2318.40` | `2333.80` | `1859.30` | 40,291.09 USD | `+0.66%` | `25X Cross` |
| `397` | `0xbb34...1696` | `LONG` | 6,068,062.00 USD | `2,600.00` | `2318.80` | `2333.80` | `1976.46` | 39,161.15 USD | `+0.65%` | `25X Cross` |
| `399` | `0x8328...f54a` | `SHORT` | 6,013,179.22 USD | `2,576.45` | `2292.01` | `2333.80` | `3280.24` | -107,907.93 USD | `-1.79%` | `25X Cross` |
| `401` | `0xed48...7c9b` | `SHORT` | 5,953,828.36 USD | `2,551.13` | `2460.02` | `2333.80` | `3234.48` | 322,018.05 USD | `+5.41%` | `20X Cross` |
| `404` | `0x934d...92c9` | `LONG` | 5,833,500.00 USD | `2,500.00` | `2343.98` | `2333.80` | `2155.52` | -26,464.51 USD | `-0.45%` | `25X Cross` |
| `421` | `0xfbe2...c8ea` | `SHORT` | 5,610,634.44 USD | `2,404.08` | `2041.57` | `2333.80` | `2687.48` | -702,541.71 USD | `-12.52%` | `20X Cross` |
| `428` | `0x1c98...7fc7` | `LONG` | 5,504,054.10 USD | `2,358.00` | `2467.15` | `2333.80` | `1897.22` | -313,517.38 USD | `-5.70%` | `10X Cross` |
| `439` | `0x6859...7e1e` | `SHORT` | 5,192,167.39 USD | `2,224.58` | `2200.39` | `2333.80` | `3713.07` | -297,214.66 USD | `-5.72%` | `25X Cross` |
| `457` | `0xd507...c948` | `SHORT` | 5,069,447.77 USD | `2,172.00` | `2387.49` | `2333.80` | `2707.43` | 116,193.26 USD | `+2.29%` | `5X Isolated` |
| `459` | `0xb829...3a81` | `LONG` | 5,027,659.06 USD | `2,153.91` | `2537.61` | `2333.80` | `778.79` | -438,137.68 USD | `-8.71%` | `20X Cross` |
| `492` | `0x3440...32c5` | `SHORT` | 4,669,519.23 USD | `2,000.57` | `2198.21` | `2333.80` | `3533.75` | -271,856.10 USD | `-5.82%` | `25X Cross` |
| `493` | `0xf929...d1f9` | `SHORT` | 4,667,800.00 USD | `2,000.00` | `2423.37` | `2333.80` | `2548.82` | 178,940.34 USD | `+3.83%` | `25X Cross` |
| `506` | `0x0514...bdfe` | `SHORT` | 4,551,826.50 USD | `1,950.00` | `1988.74` | `2333.80` | `2938.29` | -673,766.87 USD | `-14.80%` | `25X Cross` |
| `512` | `0x8376...9a1e` | `SHORT` | 4,458,906.61 USD | `1,910.50` | `2477.72` | `2333.80` | `3156.38` | 274,781.56 USD | `+6.16%` | `20X Cross` |
| `534` | `0x7a6d...f79c` | `SHORT` | 4,259,535.54 USD | `1,825.07` | `2433.80` | `2333.80` | `2786.28` | 182,333.34 USD | `+4.28%` | `25X Cross` |
| `541` | `0x541e...071d` | `SHORT` | 4,212,509.00 USD | `1,805.00` | `2648.19` | `2333.80` | `3021.33` | 567,475.84 USD | `+13.47%` | `25X Cross` |
| `542` | `0x7265...91a5` | `LONG` | 4,205,382.99 USD | `1,801.87` | `2533.96` | `2333.80` | `1988.15` | -360,483.46 USD | `-8.57%` | `20X Cross` |
| `543` | `0x739c...cfb2` | `SHORT` | 4,200,966.00 USD | `1,800.00` | `2427.60` | `2333.80` | `2658.51` | 168,730.38 USD | `+4.02%` | `25X Cross` |
| `554` | `0xa445...329d` | `LONG` | 4,146,577.52 USD | `1,776.75` | `2398.85` | `2333.80` | `1807.30` | -115,591.84 USD | `-2.79%` | `25X Cross` |
| `557` | `0x91a9...3f70` | `SHORT` | 4,125,121.57 USD | `1,767.48` | `2156.23` | `2333.80` | `3638.39` | -314,017.49 USD | `-7.61%` | `4X Cross` |
| `561` | `0x3453...b323` | `SHORT` | 4,084,559.80 USD | `1,750.12` | `2328.82` | `2333.80` | `2393.69` | -8,827.67 USD | `-0.22%` | `25X Cross` |
| `562` | `0xd4c1...3d1d` | `SHORT` | 4,083,976.23 USD | `1,749.57` | `2336.05` | `2333.80` | `5094.79` | 3,127.26 USD | `+0.08%` | `12X Cross` |
| `588` | `0xfeec...4e9c` | `SHORT` | 3,948,850.92 USD | `1,691.81` | `2566.49` | `2333.80` | `2651.08` | 393,173.59 USD | `+9.96%` | `10X Cross` |
| `589` | `0x936c...bb0f` | `SHORT` | 3,940,379.91 USD | `1,688.69` | `2434.60` | `2333.80` | `8535.33` | 170,907.19 USD | `+4.34%` | `20X Cross` |
| `613` | `0xeee0...0b53` | `LONG` | 3,820,883.47 USD | `1,637.12` | `2468.64` | `2333.80` | `127.83` | -220,592.59 USD | `-5.77%` | `7X Cross` |
| `614` | `0x27b8...12fc` | `LONG` | 3,800,357.94 USD | `1,628.12` | `2468.73` | `2333.80` | `435.52` | -219,036.70 USD | `-5.76%` | `10X Cross` |
| `615` | `0x982b...4606` | `LONG` | 3,796,780.09 USD | `1,626.82` | `2575.24` | `2333.80` | `1548.43` | -392,672.98 USD | `-10.34%` | `5X Isolated` |
| `626` | `0x73d7...8be1` | `LONG` | 3,737,660.33 USD | `1,601.47` | `2410.40` | `2333.80` | `2046.20` | -122,518.59 USD | `-3.28%` | `25X Cross` |
| `648` | `0xe170...9300` | `SHORT` | 3,578,802.26 USD | `1,533.40` | `2076.39` | `2333.80` | `3223.08` | -394,852.76 USD | `-11.03%` | `25X Cross` |
| `657` | `0xfc27...9d9d` | `SHORT` | 3,543,743.91 USD | `1,518.44` | `2402.17` | `2333.80` | `11792.22` | 103,818.03 USD | `+2.93%` | `25X Cross` |
| `660` | `0x2e2b...2fab` | `LONG` | 3,518,067.18 USD | `1,507.38` | `2245.53` | `2333.80` | `1112.02` | 133,194.08 USD | `+3.79%` | `25X Cross` |
| `666` | `0x251f...6e5d` | `LONG` | 3,501,000.00 USD | `1,500.00` | `2346.68` | `2333.80` | `1618.51` | -19,030.49 USD | `-0.54%` | `20X Cross` |
| `679` | `0xad54...6203` | `LONG` | 3,403,247.00 USD | `1,458.18` | `2627.45` | `2333.80` | `2146.48` | -428,059.68 USD | `-12.58%` | `10X Isolated` |
| `685` | `0xef70...a84c` | `SHORT` | 3,367,363.10 USD | `1,442.74` | `2424.73` | `2333.80` | `3451.39` | 130,907.73 USD | `+3.89%` | `25X Cross` |
| `692` | `0x4b5f...0dd8` | `LONG` | 3,342,043.98 USD | `1,431.96` | `2339.45` | `2333.80` | `2148.71` | -7,948.97 USD | `-0.24%` | `10X Cross` |
| `695` | `0xbadb...9ee6` | `LONG` | 3,333,182.62 USD | `1,428.16` | `1936.00` | `2333.80` | `1043.23` | 568,260.98 USD | `+17.05%` | `20X Cross` |
| `698` | `0x023a...2355` | `LONG` | 3,309,197.78 USD | `1,418.19` | `2340.12` | `2333.80` | `0.000000` | -9,540.90 USD | `-0.29%` | `25X Cross` |
| `763` | `0x880a...311c` | `SHORT` | 3,081,664.76 USD | `1,320.22` | `2425.76` | `2333.80` | `8246.63` | 120,884.39 USD | `+3.92%` | `9X Cross` |
| `771` | `0x29de...3e93` | `LONG` | 3,057,409.00 USD | `1,310.00` | `2352.60` | `2333.80` | `1922.24` | -24,499.82 USD | `-0.80%` | `5X Isolated` |
| `807` | `0xc435...c905` | `SHORT` | 2,912,707.20 USD | `1,248.00` | `2704.38` | `2333.80` | `4868.03` | 462,363.15 USD | `+15.87%` | `20X Cross` |
| `814` | `0x4202...aaf5` | `SHORT` | 2,875,608.46 USD | `1,232.10` | `2321.73` | `2333.80` | `2733.56` | -14,984.16 USD | `-0.52%` | `5X Isolated` |
| `819` | `0x7178...0854` | `LONG` | 2,844,164.06 USD | `1,218.63` | `2461.81` | `2333.80` | `1055.84` | -155,882.34 USD | `-5.48%` | `10X Cross` |
| `863` | `0x07fd...689d` | `LONG` | 2,651,076.08 USD | `1,135.90` | `2423.84` | `2333.80` | `0.000000` | -102,167.12 USD | `-3.85%` | `25X Cross` |
| `904` | `0x2f80...f203` | `SHORT` | 2,541,806.32 USD | `1,088.94` | `1984.00` | `2333.80` | `3074.60` | -381,339.13 USD | `-15.00%` | `20X Cross` |
| `914` | `0x6f11...0389` | `SHORT` | 2,518,278.10 USD | `1,079.00` | `2333.39` | `2333.80` | `3199.70` | -549.19 USD | `-0.02%` | `25X Cross` |
| `915` | `0x2b61...2f6c` | `SHORT` | 2,512,993.18 USD | `1,076.60` | `2681.75` | `2333.80` | `6368.64` | 374,179.55 USD | `+14.89%` | `10X Cross` |
| `955` | `0x1b2a...f7a6` | `LONG` | 2,393,106.38 USD | `1,025.37` | `2737.51` | `2333.80` | `949.91` | -413,853.56 USD | `-17.29%` | `10X Cross` |
| `956` | `0xb15b...dbae` | `SHORT` | 2,392,581.71 USD | `1,025.14` | `2338.37` | `2333.80` | `2381.08` | 4,592.00 USD | `+0.19%` | `25X Cross` |
| `962` | `0x3bca...66f3` | `SHORT` | 2,375,862.98 USD | `1,018.20` | `2339.15` | `2333.80` | `9850.77` | 5,857.10 USD | `+0.25%` | `25X Cross` |
| `964` | `0x6749...ce07` | `SHORT` | 2,369,209.76 USD | `1,015.35` | `2318.56` | `2333.80` | `5902.99` | -15,066.40 USD | `-0.64%` | `20X Cross` |
| `969` | `0x02aa...1806` | `SHORT` | 2,350,571.63 USD | `1,007.10` | `2654.68` | `2333.80` | `3613.69` | 322,960.47 USD | `+13.74%` | `20X Cross` |
| `970` | `0x001a...fef6` | `SHORT` | 2,350,492.15 USD | `1,007.33` | `2022.19` | `2333.80` | `3037.68` | -313,484.20 USD | `-13.34%` | `10X Cross` |
| `979` | `0xdb3a...cf3b` | `LONG` | 2,341,403.72 USD | `1,003.22` | `2705.01` | `2333.80` | `0.000000` | -372,303.17 USD | `-15.90%` | `4X Cross` |
| `983` | `0x5986...89d9` | `LONG` | 2,334,200.00 USD | `1,000.00` | `2346.34` | `2333.80` | `1258.43` | -12,149.54 USD | `-0.52%` | `25X Cross` |
| `984` | `0xdf60...d3c7` | `LONG` | 2,333,900.00 USD | `1,000.00` | `2736.24` | `2333.80` | `2246.09` | -402,342.88 USD | `-17.24%` | `10X Isolated` |
| `985` | `0x2828...93a0` | `LONG` | 2,333,900.00 USD | `1,000.00` | `2393.30` | `2333.80` | `2270.93` | -59,409.16 USD | `-2.55%` | `25X Cross` |
| `986` | `0xfe82...ce65` | `SHORT` | 2,333,900.00 USD | `1,000.00` | `2300.50` | `2333.80` | `2718.44` | -33,392.07 USD | `-1.43%` | `25X Cross` |
| `987` | `0x4044...794c` | `LONG` | 2,333,870.00 USD | `1,000.00` | `2332.68` | `2333.80` | `0.000000` | 1,180.16 USD | `+0.05%` | `25X Cross` |
| `988` | `0x5272...fcd9` | `SHORT` | 2,333,400.00 USD | `1,000.00` | `2241.82` | `2333.80` | `2880.77` | -91,575.51 USD | `-3.92%` | `5X Cross` |
| `1015` | `0xb002...ed8a` | `SHORT` | 2,247,041.58 USD | `962.78` | `2299.66` | `2333.80` | `4191.22` | -32,963.67 USD | `-1.47%` | `25X Cross` |
| `1029` | `0x2e30...4cb5` | `SHORT` | 2,208,137.78 USD | `946.12` | `2340.09` | `2333.80` | `7236.78` | 5,881.03 USD | `+0.27%` | `2X Cross` |
| `1034` | `0xc8fe...afa4` | `LONG` | 2,185,491.78 USD | `936.37` | `2331.34` | `2333.80` | `2145.82` | 2,487.55 USD | `+0.11%` | `10X Isolated` |
| `1053` | `0x9606...4e5d` | `SHORT` | 2,130,843.00 USD | `913.00` | `2478.70` | `2333.80` | `3975.26` | 132,210.61 USD | `+6.20%` | `20X Cross` |
| `1059` | `0xaeea...bfa7` | `LONG` | 2,121,104.74 USD | `908.75` | `2339.31` | `2333.80` | `2286.73` | -4,737.36 USD | `-0.22%` | `23X Isolated` |
| `1090` | `0x60f7...d1ee` | `LONG` | 2,077,082.00 USD | `890.00` | `2343.49` | `2333.80` | `2263.99` | -8,627.96 USD | `-0.42%` | `25X Cross` |
| `1177` | `0xcd27...52a8` | `LONG` | 1,953,960.45 USD | `837.21` | `2553.56` | `2333.80` | `1404.24` | -183,904.32 USD | `-9.41%` | `2X Cross` |
| `1188` | `0xbef3...0d3e` | `LONG` | 1,939,454.56 USD | `830.99` | `2332.88` | `2333.80` | `2110.70` | 843.32 USD | `+0.04%` | `20X Cross` |
| `1190` | `0x6a41...a3b9` | `LONG` | 1,927,527.00 USD | `826.06` | `2332.61` | `2333.80` | `2112.89` | 652.15 USD | `+0.03%` | `20X Cross` |
| `1230` | `0x3fc5...c0c1` | `SHORT` | 1,877,058.21 USD | `804.26` | `2702.11` | `2333.80` | `4923.22` | 296,143.32 USD | `+15.78%` | `25X Cross` |
| `1233` | `0xf83f...625f` | `SHORT` | 1,874,236.76 USD | `803.05` | `2601.00` | `2333.80` | `6031.86` | 214,499.69 USD | `+11.44%` | `20X Cross` |
| `1236` | `0x04a9...95aa` | `LONG` | 1,867,120.00 USD | `800.00` | `2595.13` | `2333.80` | `1860.65` | -208,986.74 USD | `-11.19%` | `5X Cross` |
| `1237` | `0x7737...bf66` | `SHORT` | 1,866,634.32 USD | `799.79` | `2494.83` | `2333.80` | `24816.52` | 128,711.71 USD | `+6.90%` | `15X Cross` |
| `1273` | `0x2577...4897` | `LONG` | 1,813,571.68 USD | `777.22` | `2356.03` | `2333.80` | `0.000000` | -17,591.80 USD | `-0.97%` | `15X Cross` |
| `1276` | `0x458d...ab3b` | `LONG` | 1,808,182.02 USD | `774.75` | `2740.41` | `2333.80` | `1887.99` | -314,947.16 USD | `-17.42%` | `3X Isolated` |
| `1305` | `0x7743...e4fe` | `SHORT` | 1,751,798.17 USD | `750.56` | `2326.87` | `2333.80` | `5895.13` | -5,344.04 USD | `-0.31%` | `25X Cross` |
| `1307` | `0x5f10...d49d` | `SHORT` | 1,750,050.00 USD | `750.00` | `2350.92` | `2333.80` | `2842.53` | 13,146.61 USD | `+0.75%` | `25X Cross` |
| `1345` | `0x51a0...3543` | `SHORT` | 1,691,017.44 USD | `724.55` | `2627.71` | `2333.80` | `7706.58` | 212,879.31 USD | `+12.59%` | `20X Cross` |
| `1354` | `0x4b1c...bc38` | `SHORT` | 1,685,403.01 USD | `722.14` | `2529.31` | `2333.80` | `4510.93` | 141,118.95 USD | `+8.37%` | `10X Cross` |
| `1357` | `0xa189...94d7` | `SHORT` | 1,680,286.99 USD | `719.98` | `2691.84` | `2333.80` | `3051.94` | 257,785.67 USD | `+15.34%` | `25X Cross` |
| `1366` | `0x3ee5...4fab` | `SHORT` | 1,669,342.58 USD | `715.17` | `2759.35` | `2333.80` | `3419.84` | 304,057.39 USD | `+18.21%` | `20X Cross` |
| `1378` | `0x2f93...4404` | `LONG` | 1,651,429.50 USD | `707.47` | `1700.45` | `2333.80` | `1369.63` | 448,403.12 USD | `+27.15%` | `4X Isolated` |
| `1388` | `0x5605...fe0f` | `SHORT` | 1,638,943.59 USD | `702.14` | `2566.90` | `2333.80` | `3056.10` | 163,389.06 USD | `+9.97%` | `20X Cross` |
| `1394` | `0xaa53...9cb7` | `LONG` | 1,633,380.00 USD | `700.00` | `2394.46` | `2333.80` | `1928.38` | -42,742.07 USD | `-2.62%` | `20X Cross` |
| `1438` | `0xdbd1...29dd` | `SHORT` | 1,588,691.56 USD | `680.70` | `3030.57` | `2333.80` | `4094.79` | 474,229.56 USD | `+29.85%` | `6X Cross` |
| `1444` | `0x71e5...be04` | `LONG` | 1,581,267.71 USD | `677.67` | `2727.27` | `2333.80` | `1471.77` | -266,917.90 USD | `-16.88%` | `20X Cross` |
| `1448` | `0x0b23...f37b` | `LONG` | 1,575,585.00 USD | `675.00` | `2238.15` | `2333.80` | `580.28` | 64,828.36 USD | `+4.11%` | `5X Cross` |
| `1472` | `0x0cac...6170` | `SHORT` | 1,546,195.50 USD | `662.50` | `2146.55` | `2333.80` | `2835.40` | -124,100.51 USD | `-8.03%` | `20X Cross` |
| `1477` | `0x0082...1ae3` | `LONG` | 1,540,354.20 USD | `660.00` | `2448.58` | `2333.80` | `2244.97` | -75,714.44 USD | `-4.92%` | `25X Cross` |
| `1512` | `0xffb2...5ed6` | `SHORT` | 1,495,479.23 USD | `640.77` | `2672.96` | `2333.80` | `2566.84` | 217,269.12 USD | `+14.53%` | `20X Cross` |
| `1540` | `0xfce0...f4c0` | `SHORT` | 1,455,401.33 USD | `623.60` | `3129.61` | `2333.80` | `2788.44` | 496,225.25 USD | `+34.10%` | `20X Cross` |
| `1558` | `0x7663...cb5a` | `SHORT` | 1,431,935.87 USD | `613.54` | `2342.35` | `2333.80` | `3634.19` | 5,184.62 USD | `+0.36%` | `3X Cross` |
| `1591` | `0xad02...eb65` | `LONG` | 1,401,847.55 USD | `600.62` | `2460.69` | `2333.80` | `1079.69` | -76,093.01 USD | `-5.43%` | `5X Cross` |
| `1593` | `0x67c3...609d` | `SHORT` | 1,400,520.00 USD | `600.00` | `2386.55` | `2333.80` | `2560.78` | 31,411.89 USD | `+2.24%` | `25X Cross` |
| `1594` | `0x638f...f5f0` | `LONG` | 1,400,328.00 USD | `600.00` | `4011.50` | `2333.80` | `25.84` | -1,006,575.53 USD | `-71.88%` | `25X Cross` |
| `1595` | `0x26e6...6b28` | `LONG` | 1,400,322.00 USD | `600.00` | `1769.78` | `2333.80` | `2005.49` | 338,450.47 USD | `+24.17%` | `20X Cross` |
| `1596` | `0x0deb...0bc5` | `LONG` | 1,400,040.00 USD | `600.00` | `2038.23` | `2333.80` | `1478.70` | 177,101.36 USD | `+12.65%` | `20X Cross` |
| `1597` | `0x0a84...6ddd` | `LONG` | 1,400,040.00 USD | `600.00` | `2222.36` | `2333.80` | `1774.81` | 66,621.66 USD | `+4.76%` | `25X Cross` |
| `1606` | `0x0dd5...f6ee` | `LONG` | 1,385,557.31 USD | `593.67` | `2332.21` | `2333.80` | `821.18` | 998.35 USD | `+0.07%` | `5X Cross` |
| `1618` | `0x94b6...e5b3` | `SHORT` | 1,369,322.47 USD | `586.71` | `2377.90` | `2333.80` | `2486.70` | 25,815.77 USD | `+1.89%` | `25X Cross` |
| `1660` | `0xfb99...37f3` | `LONG` | 1,319,432.63 USD | `565.34` | `2362.35` | `2333.80` | `1207.12` | -16,103.72 USD | `-1.22%` | `3X Cross` |
| `1673` | `0x844b...7f42` | `SHORT` | 1,309,312.29 USD | `561.00` | `2026.17` | `2333.80` | `3026.12` | -172,628.88 USD | `-13.18%` | `25X Cross` |
| `1693` | `0xabe6...1d99` | `SHORT` | 1,297,713.34 USD | `556.00` | `2484.68` | `2333.80` | `2944.98` | 83,782.55 USD | `+6.46%` | `20X Cross` |
| `1742` | `0xad21...fb6a` | `LONG` | 1,241,276.57 USD | `531.87` | `2574.89` | `2333.80` | `1682.02` | -128,228.93 USD | `-10.33%` | `7X Cross` |
| `1776` | `0x8923...1bac` | `SHORT` | 1,207,106.29 USD | `517.18` | `2348.15` | `2333.80` | `3139.54` | 7,318.81 USD | `+0.61%` | `25X Cross` |
| `1794` | `0x0c7a...2f50` | `SHORT` | 1,188,476.68 USD | `509.25` | `2122.56` | `2333.80` | `4069.43` | -107,571.25 USD | `-9.05%` | `20X Cross` |
| `1799` | `0xfc66...ca06` | `LONG` | 1,185,093.26 USD | `507.88` | `2336.63` | `2333.80` | `0.000000` | -1,643.22 USD | `-0.14%` | `20X Cross` |
| `1820` | `0x89b2...9ca6` | `LONG` | 1,167,135.00 USD | `500.00` | `2484.03` | `2333.80` | `1954.22` | -74,884.35 USD | `-6.42%` | `25X Cross` |
| `1826` | `0x7298...7d6c` | `SHORT` | 1,162,615.71 USD | `498.15` | `3426.75` | `2333.80` | `5422.40` | 544,420.11 USD | `+46.83%` | `20X Cross` |
| `1840` | `0xc10f...23b3` | `LONG` | 1,143,606.10 USD | `490.00` | `2402.16` | `2333.80` | `2082.07` | -33,456.73 USD | `-2.93%` | `25X Cross` |
| `1841` | `0x404c...5f03` | `SHORT` | 1,143,291.13 USD | `489.79` | `2671.94` | `2333.80` | `4338.41` | 165,388.42 USD | `+14.47%` | `20X Cross` |
| `1847` | `0x321f...1c84` | `SHORT` | 1,138,979.14 USD | `488.02` | `2370.09` | `2333.80` | `3014.44` | 17,665.46 USD | `+1.55%` | `10X Cross` |
| `1911` | `0x82c6...fe42` | `LONG` | 1,079,414.88 USD | `462.50` | `2501.38` | `2333.80` | `2054.47` | -77,475.69 USD | `-7.18%` | `5X Isolated` |
| `1924` | `0x617e...0f97` | `SHORT` | 1,068,357.46 USD | `457.85` | `2205.60` | `2333.80` | `3677.31` | -58,513.62 USD | `-5.48%` | `10X Cross` |
| `1950` | `0xae55...2236` | `LONG` | 1,050,210.00 USD | `450.00` | `2510.21` | `2333.80` | `0.000000` | -79,387.50 USD | `-7.56%` | `25X Cross` |
| `1962` | `0xac26...a9c7` | `SHORT` | 1,041,521.03 USD | `446.28` | `2192.58` | `2333.80` | `8592.92` | -63,021.33 USD | `-6.05%` | `20X Cross` |
| `1965` | `0x53f8...ceff` | `LONG` | 1,039,980.01 USD | `445.60` | `2399.81` | `2333.80` | `0.000000` | -29,370.59 USD | `-2.82%` | `20X Cross` |
| `1985` | `0xd8a1...6687` | `LONG` | 1,030,670.48 USD | `441.53` | `2804.24` | `2333.80` | `2151.03` | -207,497.95 USD | `-20.13%` | `20X Cross` |
| `2002` | `0x248e...6be2` | `SHORT` | 1,018,635.78 USD | `436.40` | `2314.49` | `2333.80` | `4423.06` | -8,601.06 USD | `-0.84%` | `20X Cross` |
| `2009` | `0x80f2...0c3a` | `LONG` | 1,014,271.95 USD | `434.55` | `2564.17` | `2333.80` | `885.87` | -99,976.93 USD | `-9.86%` | `5X Cross` |
| `2043` | `0x15c8...045f` | `SHORT` | 1,001,090.59 USD | `428.90` | `1903.23` | `2333.80` | `3088.86` | -184,797.54 USD | `-18.46%` | `25X Cross` |

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
| `7D` | `Long Liquidation` | `2077.20` | 2,540,000,000.00 USD | 2,540,000,000.00 USD | 4,860,000.00 USD | 4,190,000.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2080.00` | 2,530,000,000.00 USD | 2,530,000,000.00 USD | 3,400,000.00 USD | 3,020,000.00 USD | 2,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2082.80` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 2,420,000.00 USD | 1,860,000.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 2,380,000.00 USD | 327,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2085.60` | 2,520,000,000.00 USD | 2,520,000,000.00 USD | 3,840,000.00 USD | 2,320,000.00 USD | 3,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2088.40` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 2,280,000.00 USD | 1,370,000.00 USD | 893,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2090.50` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 1,170,000.00 USD | 270,920.00 USD | 293,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2091.20` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 4,280,000.00 USD | 952,210.00 USD | 6,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2093.00` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 775,500.00 USD | 518,220.00 USD | 846,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2094.00` | 2,490,000,000.00 USD | 2,490,000,000.00 USD | 5,200,000.00 USD | 1,660,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 1,200,000.00 USD | 325,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2095.50` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 1,840,000.00 USD | 1,290,000.00 USD | 1,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2096.80` | 2,480,000,000.00 USD | 2,480,000,000.00 USD | 1,940,000.00 USD | 3,320,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2098.00` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 463,350.00 USD | 975,880.00 USD | 309,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2099.60` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 1,880,000.00 USD | 1,920,000.00 USD | 3,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2100.50` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 160,570.00 USD | 44,780.00 USD | 175,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2102.40` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 125,250.00 USD | 341,900.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2103.00` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 433,430.00 USD | 289,160.00 USD | 306,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 1,690,000.00 USD | 324,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2105.20` | 2,470,000,000.00 USD | 2,470,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,800,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2105.50` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 521,320.00 USD | 400,040.00 USD | 168,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2108.00` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 664,310.00 USD | 0.00 USD | 347,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2108.00` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 2,400,000.00 USD | 930,280.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2110.50` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 36,110.00 USD | 31,550.00 USD | 196,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2110.80` | 2,460,000,000.00 USD | 2,460,000,000.00 USD | 2,750,000.00 USD | 1,780,000.00 USD | 2,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2113.00` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 875,700.00 USD | 643,210.00 USD | 234,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2113.60` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 1,780,000.00 USD | 1,280,000.00 USD | 2,730,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 20,530,000.00 USD | 322,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2115.50` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 0.00 USD | 13,230.00 USD | 431,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2116.40` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 1,900,000.00 USD | 2,210,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2118.00` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 679,710.00 USD | 16,610.00 USD | 819,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2119.20` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 2,920,000.00 USD | 750,810.00 USD | 2,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2120.50` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 744,340.00 USD | 416,510.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2122.00` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 2,300,000.00 USD | 1,020,000.00 USD | 1,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2123.00` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 1,030,000.00 USD | 693,780.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2124.80` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 2,680,000.00 USD | 939,650.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 1,010,000.00 USD | 302,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2125.50` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 179,030.00 USD | 1,510,000.00 USD | 511,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2127.60` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 514,750.00 USD | 2,620,000.00 USD | 2,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2128.00` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 365,910.00 USD | 623,840.00 USD | 131,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2130.40` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 2,040,000.00 USD | 2,130,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2130.50` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 18,610.00 USD | 654,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2133.00` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 187,520.00 USD | 1,120,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2133.20` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 1,930,000.00 USD | 715,940.00 USD | 323,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 3,270,000.00 USD | 301,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2135.50` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 43,420.00 USD | 2,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2136.00` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 1,370,000.00 USD | 596,290.00 USD | 18,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2138.00` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 555,320.00 USD | 501,410.00 USD | 205,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2138.80` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 1,110,000.00 USD | 1,250,000.00 USD | 60,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2141.60` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 1,550,000.00 USD | 209,240.00 USD | 766,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2143.00` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 295,510.00 USD | 0.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2144.40` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 465,960.00 USD | 1,530,000.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 9,500,000.00 USD | 297,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2145.50` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 27,790.00 USD | 207,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2147.20` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 239,110.00 USD | 10,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2148.00` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 251,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2150.00` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 459,630.00 USD | 463,640.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2152.80` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 29,510.00 USD | 681,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 17,990,000.00 USD | 288,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2155.60` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 157,380.00 USD | 430,180.00 USD | 66,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2158.40` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 687,180.00 USD | 1,010,000.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2161.20` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 1,490,000.00 USD | 1,050,000.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2164.00` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 36,870.00 USD | 329,690.00 USD | 409,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 6,290,000.00 USD | 270,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2166.80` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 25,540.00 USD | 0.00 USD | 68,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2169.60` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 1,700,000.00 USD | 726,240.00 USD | 810,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2172.40` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 479,540.00 USD | 1,150,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 108,810,000.00 USD | 264,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2185.00` | 111,820,000.00 USD | 155,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2194.80` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 141,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 1,260,000.00 USD | 43,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2197.60` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 2,440,000.00 USD | 3,270,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2200.40` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 3,000,000.00 USD | 3,140,000.00 USD | 3,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2200.50` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 284,470.00 USD | 154,560.00 USD | 225,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2203.00` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 1,050,000.00 USD | 62,930.00 USD | 696,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2203.20` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 3,240,000.00 USD | 624,500.00 USD | 2,720,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 1,290,000.00 USD | 42,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2205.50` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 611,820.00 USD | 207,110.00 USD | 781,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2206.00` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 6,050,000.00 USD | 4,010,000.00 USD | 4,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2208.00` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 2,490,000.00 USD | 2,380,000.00 USD | 2,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2208.80` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 10,060,000.00 USD | 7,030,000.00 USD | 3,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2210.50` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 2,080,000.00 USD | 1,700,000.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2211.60` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 8,410,000.00 USD | 7,020,000.00 USD | 7,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2213.00` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 2,530,000.00 USD | 1,450,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2214.40` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 12,890,000.00 USD | 12,380,000.00 USD | 9,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 1,710,000.00 USD | 40,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2215.50` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 5,720,000.00 USD | 4,420,000.00 USD | 5,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2217.20` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 16,020,000.00 USD | 10,280,000.00 USD | 8,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2218.00` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 4,050,000.00 USD | 4,830,000.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2220.00` | 2,230,000,000.00 USD | 2,230,000,000.00 USD | 12,900,000.00 USD | 10,310,000.00 USD | 3,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2220.50` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 3,450,000.00 USD | 3,630,000.00 USD | 680,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2222.80` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 5,190,000.00 USD | 5,430,000.00 USD | 8,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2223.00` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 5,770,000.00 USD | 3,810,000.00 USD | 2,870,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2225.00` | 2,840,000.00 USD | 39,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2225.50` | 988,970,000.00 USD | 988,970,000.00 USD | 2,730,000.00 USD | 5,220,000.00 USD | 2,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2225.60` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 13,090,000.00 USD | 13,590,000.00 USD | 9,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2228.00` | 978,590,000.00 USD | 978,590,000.00 USD | 4,680,000.00 USD | 1,810,000.00 USD | 666,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2228.40` | 2,150,000,000.00 USD | 2,150,000,000.00 USD | 7,680,000.00 USD | 5,550,000.00 USD | 8,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2230.50` | 971,430,000.00 USD | 971,430,000.00 USD | 3,960,000.00 USD | 1,800,000.00 USD | 2,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2231.20` | 2,130,000,000.00 USD | 2,130,000,000.00 USD | 9,590,000.00 USD | 2,970,000.00 USD | 16,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2233.00` | 963,320,000.00 USD | 963,320,000.00 USD | 5,120,000.00 USD | 2,210,000.00 USD | 3,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2234.00` | 2,100,000,000.00 USD | 2,100,000,000.00 USD | 18,760,000.00 USD | 10,880,000.00 USD | 6,070,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2235.00` | 1,030,000.00 USD | 36,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2235.50` | 952,740,000.00 USD | 952,740,000.00 USD | 4,170,000.00 USD | 4,780,000.00 USD | 5,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2236.80` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 6,910,000.00 USD | 11,270,000.00 USD | 5,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2238.00` | 938,450,000.00 USD | 938,450,000.00 USD | 1,760,000.00 USD | 2,280,000.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2239.60` | 2,040,000,000.00 USD | 2,040,000,000.00 USD | 6,630,000.00 USD | 7,850,000.00 USD | 8,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2240.50` | 933,400,000.00 USD | 933,400,000.00 USD | 731,900.00 USD | 124,100.00 USD | 601,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2242.40` | 2,020,000,000.00 USD | 2,020,000,000.00 USD | 3,820,000.00 USD | 1,890,000.00 USD | 4,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2243.00` | 931,940,000.00 USD | 931,940,000.00 USD | 1,120,000.00 USD | 1,600,000.00 USD | 982,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2245.00` | 4,620,000.00 USD | 35,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2245.20` | 2,000,000,000.00 USD | 2,000,000,000.00 USD | 16,830,000.00 USD | 13,080,000.00 USD | 11,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2245.50` | 928,230,000.00 USD | 928,230,000.00 USD | 2,490,000.00 USD | 1,320,000.00 USD | 408,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2248.00` | 924,010,000.00 USD | 924,010,000.00 USD | 1,950,000.00 USD | 621,470.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2248.00` | 1,960,000,000.00 USD | 1,960,000,000.00 USD | 13,600,000.00 USD | 6,140,000.00 USD | 10,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2250.50` | 919,610,000.00 USD | 919,610,000.00 USD | 2,890,000.00 USD | 1,100,000.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2250.80` | 1,930,000,000.00 USD | 1,930,000,000.00 USD | 10,570,000.00 USD | 10,480,000.00 USD | 8,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2253.00` | 914,020,000.00 USD | 914,020,000.00 USD | 6,720,000.00 USD | 7,090,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2253.60` | 1,900,000,000.00 USD | 1,900,000,000.00 USD | 24,760,000.00 USD | 21,020,000.00 USD | 21,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2255.00` | 11,260,000.00 USD | 30,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2255.50` | 895,380,000.00 USD | 895,380,000.00 USD | 2,370,000.00 USD | 1,780,000.00 USD | 5,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2256.40` | 1,840,000,000.00 USD | 1,840,000,000.00 USD | 31,260,000.00 USD | 19,360,000.00 USD | 15,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2258.00` | 886,010,000.00 USD | 886,010,000.00 USD | 8,240,000.00 USD | 3,840,000.00 USD | 4,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2259.20` | 1,770,000,000.00 USD | 1,770,000,000.00 USD | 24,810,000.00 USD | 20,200,000.00 USD | 22,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2260.50` | 869,090,000.00 USD | 869,090,000.00 USD | 13,230,000.00 USD | 9,840,000.00 USD | 10,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2262.00` | 1,700,000,000.00 USD | 1,700,000,000.00 USD | 45,920,000.00 USD | 30,170,000.00 USD | 22,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2263.00` | 835,550,000.00 USD | 835,550,000.00 USD | 10,810,000.00 USD | 14,100,000.00 USD | 9,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2264.80` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 30,210,000.00 USD | 26,720,000.00 USD | 18,300,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2265.00` | 4,930,000.00 USD | 19,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2265.50` | 801,430,000.00 USD | 801,430,000.00 USD | 12,810,000.00 USD | 9,900,000.00 USD | 4,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2267.60` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 40,210,000.00 USD | 41,610,000.00 USD | 31,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2268.00` | 774,500,000.00 USD | 774,500,000.00 USD | 7,440,000.00 USD | 8,660,000.00 USD | 3,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2270.40` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 46,080,000.00 USD | 25,460,000.00 USD | 39,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2270.50` | 754,510,000.00 USD | 754,510,000.00 USD | 10,820,000.00 USD | 11,230,000.00 USD | 8,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2273.00` | 724,090,000.00 USD | 724,090,000.00 USD | 15,130,000.00 USD | 9,950,000.00 USD | 8,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2273.20` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 26,430,000.00 USD | 25,760,000.00 USD | 20,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2275.00` | 4,720,000.00 USD | 14,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2275.50` | 690,170,000.00 USD | 690,170,000.00 USD | 14,620,000.00 USD | 13,850,000.00 USD | 8,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2276.00` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 52,620,000.00 USD | 46,680,000.00 USD | 45,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2278.00` | 653,040,000.00 USD | 653,040,000.00 USD | 12,140,000.00 USD | 8,370,000.00 USD | 13,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2278.80` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 69,920,000.00 USD | 30,780,000.00 USD | 43,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2280.50` | 618,810,000.00 USD | 618,810,000.00 USD | 25,850,000.00 USD | 14,940,000.00 USD | 10,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2281.60` | 943,810,000.00 USD | 943,810,000.00 USD | 61,930,000.00 USD | 60,060,000.00 USD | 46,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2283.00` | 567,210,000.00 USD | 567,210,000.00 USD | 20,090,000.00 USD | 15,010,000.00 USD | 19,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2284.40` | 775,230,000.00 USD | 775,230,000.00 USD | 84,440,000.00 USD | 69,880,000.00 USD | 44,650,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2285.00` | 3,920,000.00 USD | 9,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2285.50` | 512,490,000.00 USD | 512,490,000.00 USD | 27,610,000.00 USD | 29,300,000.00 USD | 18,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2287.20` | 576,260,000.00 USD | 576,260,000.00 USD | 59,100,000.00 USD | 55,220,000.00 USD | 44,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2288.00` | 436,620,000.00 USD | 436,620,000.00 USD | 18,510,000.00 USD | 14,610,000.00 USD | 5,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2290.00` | 417,690,000.00 USD | 417,690,000.00 USD | 47,560,000.00 USD | 32,870,000.00 USD | 24,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2290.50` | 397,710,000.00 USD | 397,710,000.00 USD | 10,010,000.00 USD | 10,000,000.00 USD | 4,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2292.80` | 312,940,000.00 USD | 312,940,000.00 USD | 38,470,000.00 USD | 20,900,000.00 USD | 42,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2293.00` | 373,680,000.00 USD | 373,680,000.00 USD | 23,490,000.00 USD | 18,810,000.00 USD | 15,450,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2295.00` | 3,480,000.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2295.50` | 315,940,000.00 USD | 315,940,000.00 USD | 19,480,000.00 USD | 17,630,000.00 USD | 9,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2295.60` | 211,210,000.00 USD | 211,210,000.00 USD | 17,510,000.00 USD | 8,110,000.00 USD | 6,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2298.00` | 269,830,000.00 USD | 269,830,000.00 USD | 9,940,000.00 USD | 6,130,000.00 USD | 1,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2298.40` | 178,800,000.00 USD | 178,800,000.00 USD | 2,090,000.00 USD | 5,820,000.00 USD | 301,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2300.50` | 252,360,000.00 USD | 252,360,000.00 USD | 18,460,000.00 USD | 10,470,000.00 USD | 13,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2301.20` | 170,580,000.00 USD | 170,580,000.00 USD | 11,790,000.00 USD | 2,120,000.00 USD | 7,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2303.00` | 210,120,000.00 USD | 210,120,000.00 USD | 20,250,000.00 USD | 13,820,000.00 USD | 12,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2304.00` | 149,080,000.00 USD | 149,080,000.00 USD | 32,960,000.00 USD | 17,170,000.00 USD | 13,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2305.00` | 1,030,000.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2305.50` | 163,190,000.00 USD | 163,190,000.00 USD | 17,630,000.00 USD | 10,310,000.00 USD | 22,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2306.80` | 85,680,000.00 USD | 85,680,000.00 USD | 0.00 USD | 3,740,000.00 USD | 11,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2308.00` | 113,170,000.00 USD | 113,170,000.00 USD | 869,360.00 USD | 1,870,000.00 USD | 2,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2309.60` | 70,920,000.00 USD | 70,920,000.00 USD | 282,530.00 USD | 300,580.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2310.50` | 107,890,000.00 USD | 107,890,000.00 USD | 6,440,000.00 USD | 3,630,000.00 USD | 6,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2312.40` | 68,830,000.00 USD | 68,830,000.00 USD | 2,470,000.00 USD | 640,510.00 USD | 2,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2313.00` | 91,030,000.00 USD | 91,030,000.00 USD | 5,900,000.00 USD | 8,030,000.00 USD | 4,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2315.00` | 938,780.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2315.20` | 63,210,000.00 USD | 63,210,000.00 USD | 5,020,000.00 USD | 4,100,000.00 USD | 117,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2315.50` | 72,200,000.00 USD | 72,200,000.00 USD | 10,840,000.00 USD | 6,820,000.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2318.00` | 52,600,000.00 USD | 52,600,000.00 USD | 9,460,000.00 USD | 4,310,000.00 USD | 6,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2318.00` | 53,980,000.00 USD | 53,980,000.00 USD | 817,040.00 USD | 3,010,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2320.50` | 32,650,000.00 USD | 32,650,000.00 USD | 3,110,000.00 USD | 3,100,000.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2320.80` | 50,160,000.00 USD | 50,160,000.00 USD | 0.00 USD | 2,960,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2323.00` | 24,720,000.00 USD | 24,720,000.00 USD | 4,500,000.00 USD | 4,510,000.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2323.60` | 47,200,000.00 USD | 47,200,000.00 USD | 4,070,000.00 USD | 2,210,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2325.00` | 344,610.00 USD | 344,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2325.50` | 13,490,000.00 USD | 13,490,000.00 USD | 4,120,000.00 USD | 0.00 USD | 66,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2326.40` | 40,910,000.00 USD | 40,910,000.00 USD | 0.00 USD | 0.00 USD | 126,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2328.00` | 9,300,000.00 USD | 9,300,000.00 USD | 0.00 USD | 2,910,000.00 USD | 89,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2329.20` | 40,790,000.00 USD | 40,790,000.00 USD | 3,860,000.00 USD | 0.00 USD | 4,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2330.50` | 6,300,000.00 USD | 6,300,000.00 USD | 4,990,000.00 USD | 1,150,000.00 USD | 168,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2332.00` | 32,040,000.00 USD | 32,040,000.00 USD | 29,230,000.00 USD | 0.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2333.00` | 13,060,000.00 USD | 13,060,000.00 USD | 10,110,000.00 USD | 1,470,000.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2334.80` | 34,610,000.00 USD | 34,610,000.00 USD | 7,260,000.00 USD | 18,420,000.00 USD | 8,930,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2335.00` | 735.29 USD | 735.29 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2335.50` | 36,370,000.00 USD | 36,370,000.00 USD | 12,670,000.00 USD | 10,650,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2337.60` | 86,860,000.00 USD | 86,860,000.00 USD | 20,380,000.00 USD | 18,310,000.00 USD | 13,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2338.00` | 37,800,000.00 USD | 37,800,000.00 USD | 0.00 USD | 0.00 USD | 1,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2340.40` | 100,250,000.00 USD | 100,250,000.00 USD | 0.00 USD | 10,010,000.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2343.00` | 39,700,000.00 USD | 39,700,000.00 USD | 0.00 USD | 186,090.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2343.20` | 109,630,000.00 USD | 109,630,000.00 USD | 0.00 USD | 5,540,000.00 USD | 3,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2345.50` | 51,410,000.00 USD | 51,410,000.00 USD | 963,370.00 USD | 1,770,000.00 USD | 8,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2346.00` | 130,380,000.00 USD | 130,380,000.00 USD | 0.00 USD | 7,920,000.00 USD | 12,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2348.00` | 51,870,000.00 USD | 51,870,000.00 USD | 460,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2348.80` | 148,870,000.00 USD | 148,870,000.00 USD | 495,290.00 USD | 7,240,000.00 USD | 10,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2350.50` | 86,320,000.00 USD | 86,320,000.00 USD | 25,900,000.00 USD | 2,670,000.00 USD | 5,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2351.60` | 173,070,000.00 USD | 173,070,000.00 USD | 572,980.00 USD | 17,950,000.00 USD | 5,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2353.00` | 90,410,000.00 USD | 90,410,000.00 USD | 1,760,000.00 USD | 1,110,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2354.40` | 214,310,000.00 USD | 214,310,000.00 USD | 6,120,000.00 USD | 34,750,000.00 USD | 371,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2355.50` | 108,810,000.00 USD | 108,810,000.00 USD | 855,740.00 USD | 16,300,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2357.20` | 228,690,000.00 USD | 228,690,000.00 USD | 8,470,000.00 USD | 5,920,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2358.00` | 114,470,000.00 USD | 114,470,000.00 USD | 1,400,000.00 USD | 1,810,000.00 USD | 2,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2360.00` | 230,910,000.00 USD | 230,910,000.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2360.50` | 122,480,000.00 USD | 122,480,000.00 USD | 2,010,000.00 USD | 2,890,000.00 USD | 3,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2362.80` | 233,780,000.00 USD | 233,780,000.00 USD | 1,180,000.00 USD | 0.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2363.00` | 136,280,000.00 USD | 136,280,000.00 USD | 3,730,000.00 USD | 7,640,000.00 USD | 2,420,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 602.37 USD | 1,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2365.50` | 139,790,000.00 USD | 139,790,000.00 USD | 1,870,000.00 USD | 0.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2365.60` | 241,780,000.00 USD | 241,780,000.00 USD | 6,340,000.00 USD | 0.00 USD | 1,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2368.00` | 148,210,000.00 USD | 148,210,000.00 USD | 6,180,000.00 USD | 2,030,000.00 USD | 204,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2368.40` | 252,260,000.00 USD | 252,260,000.00 USD | 9,590,000.00 USD | 475,460.00 USD | 404,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2370.50` | 185,140,000.00 USD | 185,140,000.00 USD | 15,780,000.00 USD | 12,620,000.00 USD | 8,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2371.20` | 314,700,000.00 USD | 314,700,000.00 USD | 16,760,000.00 USD | 0.00 USD | 45,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2373.00` | 207,460,000.00 USD | 207,460,000.00 USD | 13,130,000.00 USD | 2,320,000.00 USD | 6,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2374.00` | 336,700,000.00 USD | 336,700,000.00 USD | 15,830,000.00 USD | 121,480.00 USD | 6,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 488,660.00 USD | 490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2375.50` | 229,950,000.00 USD | 229,950,000.00 USD | 13,390,000.00 USD | 3,370,000.00 USD | 5,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2376.80` | 376,910,000.00 USD | 376,910,000.00 USD | 12,140,000.00 USD | 5,950,000.00 USD | 22,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2378.00` | 254,240,000.00 USD | 254,240,000.00 USD | 4,330,000.00 USD | 9,290,000.00 USD | 10,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2379.60` | 404,220,000.00 USD | 404,220,000.00 USD | 7,180,000.00 USD | 2,580,000.00 USD | 17,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2380.50` | 295,960,000.00 USD | 295,960,000.00 USD | 12,280,000.00 USD | 12,870,000.00 USD | 16,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2382.40` | 446,430,000.00 USD | 446,430,000.00 USD | 8,510,000.00 USD | 12,380,000.00 USD | 21,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2383.00` | 347,200,000.00 USD | 347,200,000.00 USD | 22,360,000.00 USD | 16,150,000.00 USD | 12,730,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 3,920,000.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2385.20` | 541,560,000.00 USD | 541,560,000.00 USD | 15,440,000.00 USD | 28,990,000.00 USD | 50,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2385.50` | 381,150,000.00 USD | 381,150,000.00 USD | 9,330,000.00 USD | 14,700,000.00 USD | 9,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2388.00` | 410,370,000.00 USD | 410,370,000.00 USD | 14,850,000.00 USD | 9,150,000.00 USD | 5,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2388.00` | 615,000,000.00 USD | 615,000,000.00 USD | 4,540,000.00 USD | 34,290,000.00 USD | 34,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2390.50` | 429,400,000.00 USD | 429,400,000.00 USD | 6,210,000.00 USD | 5,300,000.00 USD | 7,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2390.80` | 713,230,000.00 USD | 713,230,000.00 USD | 5,470,000.00 USD | 44,170,000.00 USD | 48,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2393.00` | 453,800,000.00 USD | 453,800,000.00 USD | 5,640,000.00 USD | 12,500,000.00 USD | 6,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2393.60` | 812,130,000.00 USD | 812,130,000.00 USD | 44,040,000.00 USD | 23,140,000.00 USD | 31,720,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 4,260,000.00 USD | 8,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2395.50` | 470,000,000.00 USD | 470,000,000.00 USD | 6,640,000.00 USD | 6,910,000.00 USD | 2,650,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2396.40` | 899,490,000.00 USD | 899,490,000.00 USD | 29,670,000.00 USD | 34,800,000.00 USD | 22,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2398.00` | 493,060,000.00 USD | 493,060,000.00 USD | 3,940,000.00 USD | 11,190,000.00 USD | 7,930,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2399.20` | 992,010,000.00 USD | 992,010,000.00 USD | 41,690,000.00 USD | 31,030,000.00 USD | 19,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2400.50` | 524,960,000.00 USD | 524,960,000.00 USD | 14,990,000.00 USD | 5,740,000.00 USD | 11,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2402.00` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 51,500,000.00 USD | 23,600,000.00 USD | 30,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2403.00` | 546,440,000.00 USD | 546,440,000.00 USD | 5,490,000.00 USD | 8,580,000.00 USD | 7,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2404.80` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 36,380,000.00 USD | 25,660,000.00 USD | 15,080,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 9,070,000.00 USD | 17,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2405.50` | 574,220,000.00 USD | 574,220,000.00 USD | 12,330,000.00 USD | 7,980,000.00 USD | 7,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2407.60` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 26,430,000.00 USD | 30,520,000.00 USD | 18,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2408.00` | 609,730,000.00 USD | 609,730,000.00 USD | 14,030,000.00 USD | 12,000,000.00 USD | 9,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2410.40` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 22,760,000.00 USD | 27,140,000.00 USD | 24,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2410.50` | 631,590,000.00 USD | 631,590,000.00 USD | 8,210,000.00 USD | 8,870,000.00 USD | 4,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2413.00` | 649,000,000.00 USD | 649,000,000.00 USD | 8,240,000.00 USD | 5,720,000.00 USD | 3,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2413.20` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 13,250,000.00 USD | 13,960,000.00 USD | 12,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 255,650.00 USD | 17,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2415.50` | 661,910,000.00 USD | 661,910,000.00 USD | 3,460,000.00 USD | 5,780,000.00 USD | 3,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2416.00` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 27,740,000.00 USD | 17,800,000.00 USD | 32,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2418.00` | 675,070,000.00 USD | 675,070,000.00 USD | 4,860,000.00 USD | 5,350,000.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2418.80` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 29,770,000.00 USD | 16,840,000.00 USD | 12,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2420.50` | 689,740,000.00 USD | 689,740,000.00 USD | 6,760,000.00 USD | 4,030,000.00 USD | 3,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2421.60` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 22,900,000.00 USD | 25,380,000.00 USD | 18,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2423.00` | 704,330,000.00 USD | 704,330,000.00 USD | 4,440,000.00 USD | 4,770,000.00 USD | 5,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.40` | 1,660,000,000.00 USD | 1,660,000,000.00 USD | 26,330,000.00 USD | 29,850,000.00 USD | 33,610,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 815,490.00 USD | 18,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2425.50` | 708,870,000.00 USD | 708,870,000.00 USD | 1,190,000.00 USD | 2,730,000.00 USD | 629,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2427.20` | 1,730,000,000.00 USD | 1,730,000,000.00 USD | 22,440,000.00 USD | 21,730,000.00 USD | 23,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2428.00` | 711,860,000.00 USD | 711,860,000.00 USD | 1,930,000.00 USD | 464,670.00 USD | 601,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2430.00` | 1,760,000,000.00 USD | 1,760,000,000.00 USD | 8,250,000.00 USD | 16,890,000.00 USD | 7,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2430.50` | 715,200,000.00 USD | 715,200,000.00 USD | 1,100,000.00 USD | 1,230,000.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2432.80` | 1,790,000,000.00 USD | 1,790,000,000.00 USD | 15,460,000.00 USD | 10,350,000.00 USD | 5,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2433.00` | 719,890,000.00 USD | 719,890,000.00 USD | 2,000,000.00 USD | 1,070,000.00 USD | 1,630,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 7,920,000.00 USD | 26,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2435.50` | 724,760,000.00 USD | 724,760,000.00 USD | 3,190,000.00 USD | 495,600.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2435.60` | 1,840,000,000.00 USD | 1,840,000,000.00 USD | 20,760,000.00 USD | 13,900,000.00 USD | 12,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2438.00` | 725,940,000.00 USD | 725,940,000.00 USD | 634,820.00 USD | 517,090.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2438.40` | 1,890,000,000.00 USD | 1,890,000,000.00 USD | 16,830,000.00 USD | 22,750,000.00 USD | 14,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2440.50` | 730,540,000.00 USD | 730,540,000.00 USD | 1,540,000.00 USD | 2,030,000.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2441.20` | 1,930,000,000.00 USD | 1,930,000,000.00 USD | 15,870,000.00 USD | 6,990,000.00 USD | 10,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2443.00` | 733,160,000.00 USD | 733,160,000.00 USD | 1,050,000.00 USD | 667,430.00 USD | 896,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2444.00` | 1,950,000,000.00 USD | 1,950,000,000.00 USD | 6,380,000.00 USD | 13,460,000.00 USD | 7,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 158,630.00 USD | 26,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2445.50` | 735,820,000.00 USD | 735,820,000.00 USD | 177,710.00 USD | 839,480.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2446.80` | 1,990,000,000.00 USD | 1,990,000,000.00 USD | 11,620,000.00 USD | 7,020,000.00 USD | 18,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2448.00` | 740,430,000.00 USD | 740,430,000.00 USD | 1,770,000.00 USD | 999,000.00 USD | 1,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2449.60` | 2,030,000,000.00 USD | 2,030,000,000.00 USD | 18,130,000.00 USD | 10,300,000.00 USD | 14,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2450.50` | 747,940,000.00 USD | 747,940,000.00 USD | 2,540,000.00 USD | 1,810,000.00 USD | 3,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2452.40` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 7,700,000.00 USD | 8,980,000.00 USD | 7,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2453.00` | 758,110,000.00 USD | 758,110,000.00 USD | 3,540,000.00 USD | 2,750,000.00 USD | 3,890,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 98,850.00 USD | 26,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2455.20` | 2,070,000,000.00 USD | 2,070,000,000.00 USD | 6,850,000.00 USD | 5,830,000.00 USD | 3,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2455.50` | 766,170,000.00 USD | 766,170,000.00 USD | 2,720,000.00 USD | 3,790,000.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2458.00` | 771,930,000.00 USD | 771,930,000.00 USD | 2,250,000.00 USD | 2,270,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2458.00` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 11,170,000.00 USD | 11,200,000.00 USD | 13,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2460.50` | 775,950,000.00 USD | 775,950,000.00 USD | 1,260,000.00 USD | 1,430,000.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2460.80` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 7,010,000.00 USD | 10,680,000.00 USD | 9,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2463.00` | 779,270,000.00 USD | 779,270,000.00 USD | 174,920.00 USD | 2,050,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2463.60` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 10,390,000.00 USD | 9,560,000.00 USD | 5,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 79,760.00 USD | 27,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2465.50` | 781,340,000.00 USD | 781,340,000.00 USD | 820,990.00 USD | 1,240,000.00 USD | 5,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2466.40` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 4,790,000.00 USD | 2,080,000.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2468.00` | 782,350,000.00 USD | 782,350,000.00 USD | 0.00 USD | 998,350.00 USD | 7,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2469.20` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 2,490,000.00 USD | 3,570,000.00 USD | 408,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2470.50` | 785,770,000.00 USD | 785,770,000.00 USD | 1,390,000.00 USD | 883,290.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2472.00` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 3,090,000.00 USD | 2,760,000.00 USD | 814,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2473.00` | 786,010,000.00 USD | 786,010,000.00 USD | 0.00 USD | 232,740.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2474.80` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 5,400,000.00 USD | 866,790.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 836,210.00 USD | 27,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2475.50` | 786,750,000.00 USD | 786,750,000.00 USD | 738,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2477.60` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 790,860.00 USD | 3,880,000.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2478.00` | 786,800,000.00 USD | 786,800,000.00 USD | 0.00 USD | 41,760.00 USD | 7,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2480.40` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 2,110,000.00 USD | 1,740,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2480.50` | 787,350,000.00 USD | 787,350,000.00 USD | 0.00 USD | 27,720.00 USD | 518,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2483.00` | 787,970,000.00 USD | 787,970,000.00 USD | 628,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2483.20` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 1,210,000.00 USD | 1,190,000.00 USD | 77,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 2,000,000.00 USD | 29,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2486.00` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 49,690.00 USD | 925,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2488.80` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 977,620.00 USD | 857,130.00 USD | 101,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2491.60` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 2,360,000.00 USD | 2,470,000.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2494.40` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 1,470,000.00 USD | 2,730,000.00 USD | 6,820,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 886,080.00 USD | 30,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2497.20` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 3,640,000.00 USD | 3,570,000.00 USD | 4,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2500.00` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 1,110,000.00 USD | 2,430,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2502.80` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 110,450.00 USD | 1,430,000.00 USD | 170,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 120,200.00 USD | 30,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2505.60` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 3,200,000.00 USD | 2,320,000.00 USD | 59,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2508.40` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 1,810,000.00 USD | 1,270,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2511.20` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 1,900,000.00 USD | 3,230,000.00 USD | 2,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2514.00` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 776,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 142,620.00 USD | 31,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2516.80` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 97,050.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2519.60` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2520.50` | 788,150,000.00 USD | 788,150,000.00 USD | 80,610.00 USD | 61,830.00 USD | 32,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2522.40` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 1,050,000.00 USD | 0.00 USD | 945,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2523.00` | 788,210,000.00 USD | 788,210,000.00 USD | 0.00 USD | 0.00 USD | 57,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 1,070,000.00 USD | 32,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2525.20` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 307,040.00 USD | 224,130.00 USD | 200,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2525.50` | 788,740,000.00 USD | 788,740,000.00 USD | 421,540.00 USD | 57,450.00 USD | 53,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2528.00` | 789,410,000.00 USD | 789,410,000.00 USD | 0.00 USD | 645,910.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2528.00` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 1,580,000.00 USD | 1,690,000.00 USD | 727,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2530.50` | 790,840,000.00 USD | 790,840,000.00 USD | 995,550.00 USD | 0.00 USD | 437,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2530.80` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 2,080,000.00 USD | 1,110,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2533.00` | 791,220,000.00 USD | 791,220,000.00 USD | 359,430.00 USD | 0.00 USD | 16,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2533.60` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 2,680,000.00 USD | 2,100,000.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2535.00` | 1,310,000.00 USD | 33,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2535.50` | 792,280,000.00 USD | 792,280,000.00 USD | 431,500.00 USD | 134,490.00 USD | 493,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2536.40` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 3,670,000.00 USD | 2,850,000.00 USD | 2,740,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2538.00` | 797,010,000.00 USD | 797,010,000.00 USD | 1,830,000.00 USD | 904,340.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2539.20` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 2,620,000.00 USD | 2,470,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2540.50` | 799,410,000.00 USD | 799,410,000.00 USD | 1,150,000.00 USD | 1,010,000.00 USD | 237,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2542.00` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 3,400,000.00 USD | 2,740,000.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2543.00` | 801,580,000.00 USD | 801,580,000.00 USD | 1,090,000.00 USD | 1,070,000.00 USD | 19,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2544.80` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 2,170,000.00 USD | 1,830,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2545.00` | 6,130,000.00 USD | 39,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2545.50` | 802,990,000.00 USD | 802,990,000.00 USD | 590,640.00 USD | 800,740.00 USD | 12,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2547.60` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 2,380,000.00 USD | 938,680.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2548.00` | 805,930,000.00 USD | 805,930,000.00 USD | 1,370,000.00 USD | 832,850.00 USD | 743,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2550.40` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 2,920,000.00 USD | 2,690,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2550.50` | 809,080,000.00 USD | 809,080,000.00 USD | 1,070,000.00 USD | 1,460,000.00 USD | 618,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2553.00` | 810,170,000.00 USD | 810,170,000.00 USD | 781,250.00 USD | 220,540.00 USD | 89,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2553.20` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 2,590,000.00 USD | 788,360.00 USD | 2,180,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2555.00` | 924,540.00 USD | 40,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2555.50` | 811,680,000.00 USD | 811,680,000.00 USD | 1,030,000.00 USD | 124,540.00 USD | 365,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2556.00` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 2,760,000.00 USD | 255,750.00 USD | 5,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2558.00` | 813,330,000.00 USD | 813,330,000.00 USD | 525,530.00 USD | 415,210.00 USD | 710,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2558.80` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 3,850,000.00 USD | 1,640,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2560.50` | 817,440,000.00 USD | 817,440,000.00 USD | 1,840,000.00 USD | 1,100,000.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2561.60` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 2,780,000.00 USD | 1,960,000.00 USD | 785,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2563.00` | 819,370,000.00 USD | 819,370,000.00 USD | 440,660.00 USD | 504,630.00 USD | 984,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2564.40` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 1,800,000.00 USD | 1,780,000.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2565.00` | 3,420,000.00 USD | 43,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2565.50` | 820,250,000.00 USD | 820,250,000.00 USD | 183,260.00 USD | 700,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2567.20` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 575,630.00 USD | 1,560,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2568.00` | 820,480,000.00 USD | 820,480,000.00 USD | 46,810.00 USD | 0.00 USD | 175,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2570.00` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 125,250.00 USD | 290,680.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2570.50` | 821,500,000.00 USD | 821,500,000.00 USD | 422,490.00 USD | 289,160.00 USD | 306,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2572.80` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2573.00` | 822,410,000.00 USD | 822,410,000.00 USD | 485,450.00 USD | 400,040.00 USD | 27,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2575.00` | 12,110,000.00 USD | 56,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2575.50` | 823,440,000.00 USD | 823,440,000.00 USD | 546,100.00 USD | 0.00 USD | 488,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2575.60` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 2,180,000.00 USD | 344,620.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2578.00` | 823,600,000.00 USD | 823,600,000.00 USD | 118,210.00 USD | 31,550.00 USD | 8,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2578.40` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 734,040.00 USD | 1,480,000.00 USD | 1,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2580.50` | 824,290,000.00 USD | 824,290,000.00 USD | 490,860.00 USD | 8,910.00 USD | 191,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2581.20` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 3,870,000.00 USD | 912,130.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2583.00` | 825,580,000.00 USD | 825,580,000.00 USD | 420,950.00 USD | 634,310.00 USD | 235,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2584.00` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 146,630.00 USD | 1,490,000.00 USD | 3,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2585.00` | 26,480,000.00 USD | 82,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2585.50` | 826,010,000.00 USD | 826,010,000.00 USD | 0.00 USD | 0.00 USD | 426,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2586.80` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 1,900,000.00 USD | 1,970,000.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2587.70` | 827,380,000.00 USD | 827,380,000.00 USD | 665,720.00 USD | 0.00 USD | 707,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2589.60` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 2,840,000.00 USD | 446,810.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2592.40` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 2,340,000.00 USD | 1,280,000.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2595.00` | 8,300,000.00 USD | 90,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2595.20` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 452,020.00 USD | 569,790.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2598.00` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 2,280,000.00 USD | 1,630,000.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2600.80` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 931,390.00 USD | 1,960,000.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2603.60` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 1,600,000.00 USD | 1,580,000.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2605.00` | 534,220.00 USD | 91,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2606.40` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 1,480,000.00 USD | 229,360.00 USD | 320,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2609.20` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2612.00` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 770,330.00 USD | 608,060.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2614.80` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 1,060,000.00 USD | 1,000,000.00 USD | 409,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2615.00` | 926,240.00 USD | 92,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2617.60` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 1,550,000.00 USD | 209,240.00 USD | 392,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2620.40` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 47,360.00 USD | 1,120,000.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2623.20` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 418,600.00 USD | 410,460.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `475.00` | 872,180,000.00 USD | 0.00 USD | 38,510.00 USD | `-79.62%` | `81.07` |
| `Live` | `Long` | `485.00` | 872,140,000.00 USD | 0.00 USD | 16,660.00 USD | `-79.19%` | `34.36` |
| `Live` | `Long` | `495.00` | 872,120,000.00 USD | 0.00 USD | 3,730.00 USD | `-78.76%` | `7.53` |
| `Live` | `Long` | `505.00` | 872,120,000.00 USD | 0.00 USD | 1,420.00 USD | `-78.33%` | `2.81` |
| `Live` | `Long` | `515.00` | 872,120,000.00 USD | 0.00 USD | 8,360.00 USD | `-77.90%` | `16.23` |
| `Live` | `Long` | `525.00` | 872,110,000.00 USD | 0.00 USD | 7,830.00 USD | `-77.48%` | `14.91` |
| `Live` | `Long` | `535.00` | 872,100,000.00 USD | 0.00 USD | 7,800.00 USD | `-77.05%` | `14.58` |
| `Live` | `Long` | `545.00` | 872,090,000.00 USD | 0.00 USD | 183,350.00 USD | `-76.62%` | `336.42` |
| `Live` | `Long` | `555.00` | 871,910,000.00 USD | 0.00 USD | 23,730.00 USD | `-76.19%` | `42.76` |
| `Live` | `Long` | `565.00` | 871,890,000.00 USD | 0.00 USD | 77,720.00 USD | `-75.76%` | `137.57` |
| `Live` | `Long` | `575.00` | 871,810,000.00 USD | 0.00 USD | 8,530.00 USD | `-75.33%` | `14.84` |
| `Live` | `Long` | `585.00` | 871,800,000.00 USD | 0.00 USD | 461,390.00 USD | `-74.90%` | `788.71` |
| `Live` | `Long` | `595.00` | 871,340,000.00 USD | 0.00 USD | 868.52 USD | `-74.47%` | `1.46` |
| `Live` | `Long` | `605.00` | 871,340,000.00 USD | 0.00 USD | 17,020.00 USD | `-74.04%` | `28.14` |
| `Live` | `Long` | `615.00` | 871,320,000.00 USD | 0.00 USD | 34,040.00 USD | `-73.61%` | `55.35` |
| `Live` | `Long` | `625.00` | 871,290,000.00 USD | 0.00 USD | 101,730.00 USD | `-73.19%` | `162.78` |
| `Live` | `Long` | `635.00` | 871,190,000.00 USD | 0.00 USD | 4,650.00 USD | `-72.76%` | `7.32` |
| `Live` | `Long` | `645.00` | 871,180,000.00 USD | 0.00 USD | 1,310.00 USD | `-72.33%` | `2.04` |
| `Live` | `Long` | `655.00` | 871,180,000.00 USD | 0.00 USD | 37,950.00 USD | `-71.90%` | `57.93` |
| `Live` | `Long` | `665.00` | 871,140,000.00 USD | 0.00 USD | 55,130.00 USD | `-71.47%` | `82.91` |
| `Live` | `Long` | `675.00` | 871,090,000.00 USD | 0.00 USD | 106,820.00 USD | `-71.04%` | `158.26` |
| `Live` | `Long` | `685.00` | 870,980,000.00 USD | 0.00 USD | 25,510.00 USD | `-70.61%` | `37.24` |
| `Live` | `Long` | `695.00` | 870,950,000.00 USD | 0.00 USD | 16,540.00 USD | `-70.18%` | `23.80` |
| `Live` | `Long` | `705.00` | 870,940,000.00 USD | 0.00 USD | 111,270.00 USD | `-69.75%` | `157.83` |
| `Live` | `Long` | `715.00` | 870,830,000.00 USD | 0.00 USD | 2,070.00 USD | `-69.32%` | `2.90` |
| `Live` | `Long` | `725.00` | 870,820,000.00 USD | 0.00 USD | 396,310.00 USD | `-68.89%` | `546.64` |
| `Live` | `Long` | `735.00` | 870,430,000.00 USD | 0.00 USD | 47,970.00 USD | `-68.47%` | `65.27` |
| `Live` | `Long` | `745.00` | 870,380,000.00 USD | 0.00 USD | 7,620.00 USD | `-68.04%` | `10.22` |
| `Live` | `Long` | `755.00` | 870,370,000.00 USD | 0.00 USD | 26,430.00 USD | `-67.61%` | `35.00` |
| `Live` | `Long` | `765.00` | 870,350,000.00 USD | 0.00 USD | 30,660.00 USD | `-67.18%` | `40.08` |
| `Live` | `Long` | `775.00` | 870,320,000.00 USD | 0.00 USD | 1,740,000.00 USD | `-66.75%` | `2,250.86` |
| `Live` | `Long` | `785.00` | 868,570,000.00 USD | 0.00 USD | 40,690.00 USD | `-66.32%` | `51.84` |
| `Live` | `Long` | `795.00` | 868,530,000.00 USD | 0.00 USD | 58,880.00 USD | `-65.89%` | `74.06` |
| `Live` | `Long` | `805.00` | 868,470,000.00 USD | 0.00 USD | 231,460.00 USD | `-65.46%` | `287.53` |
| `Live` | `Long` | `815.00` | 868,240,000.00 USD | 0.00 USD | 51,830.00 USD | `-65.03%` | `63.59` |
| `Live` | `Long` | `825.00` | 868,190,000.00 USD | 0.00 USD | 382,270.00 USD | `-64.60%` | `463.35` |
| `Live` | `Long` | `835.00` | 867,810,000.00 USD | 0.00 USD | 129,920.00 USD | `-64.18%` | `155.59` |
| `Live` | `Long` | `845.00` | 867,680,000.00 USD | 0.00 USD | 7,240.00 USD | `-63.75%` | `8.56` |
| `Live` | `Long` | `855.00` | 867,670,000.00 USD | 0.00 USD | 2,900.00 USD | `-63.32%` | `3.39` |
| `Live` | `Long` | `865.00` | 867,670,000.00 USD | 0.00 USD | 3,780,000.00 USD | `-62.89%` | `4,371.81` |
| `Live` | `Long` | `875.00` | 863,880,000.00 USD | 0.00 USD | 44,640.00 USD | `-62.46%` | `51.01` |
| `Live` | `Long` | `885.00` | 863,840,000.00 USD | 0.00 USD | 7,390.00 USD | `-62.03%` | `8.35` |
| `Live` | `Long` | `895.00` | 863,830,000.00 USD | 0.00 USD | 407,820.00 USD | `-61.60%` | `455.67` |
| `Live` | `Long` | `905.00` | 863,420,000.00 USD | 0.00 USD | 80,220.00 USD | `-61.17%` | `88.64` |
| `Live` | `Long` | `915.00` | 863,340,000.00 USD | 0.00 USD | 740,670.00 USD | `-60.74%` | `809.48` |
| `Live` | `Long` | `925.00` | 862,600,000.00 USD | 0.00 USD | 151,670.00 USD | `-60.31%` | `163.97` |
| `Live` | `Long` | `935.00` | 862,450,000.00 USD | 0.00 USD | 1,010,000.00 USD | `-59.89%` | `1,084.12` |
| `Live` | `Long` | `945.00` | 861,440,000.00 USD | 0.00 USD | 8,990.00 USD | `-59.46%` | `9.51` |
| `Live` | `Long` | `955.00` | 861,430,000.00 USD | 0.00 USD | 179,010.00 USD | `-59.03%` | `187.45` |
| `Live` | `Long` | `965.00` | 861,250,000.00 USD | 0.00 USD | 81,690.00 USD | `-58.60%` | `84.65` |
| `Live` | `Long` | `975.00` | 861,170,000.00 USD | 0.00 USD | 73,410.00 USD | `-58.17%` | `75.29` |
| `Live` | `Long` | `985.00` | 861,090,000.00 USD | 0.00 USD | 19,550.00 USD | `-57.74%` | `19.85` |
| `Live` | `Long` | `995.00` | 861,080,000.00 USD | 0.00 USD | 199,260.00 USD | `-57.31%` | `200.26` |
| `Live` | `Long` | `1005.00` | 860,880,000.00 USD | 0.00 USD | 44,810.00 USD | `-56.88%` | `44.59` |
| `Live` | `Long` | `1015.00` | 860,830,000.00 USD | 0.00 USD | 7,140,000.00 USD | `-56.45%` | `7,038.37` |
| `Live` | `Long` | `1025.00` | 853,690,000.00 USD | 0.00 USD | 117,290.00 USD | `-56.02%` | `114.43` |
| `Live` | `Long` | `1035.00` | 853,570,000.00 USD | 0.00 USD | 1,530,000.00 USD | `-55.59%` | `1,481.74` |
| `Live` | `Long` | `1045.00` | 852,040,000.00 USD | 0.00 USD | 419,240.00 USD | `-55.17%` | `401.18` |
| `Live` | `Long` | `1055.00` | 851,620,000.00 USD | 0.00 USD | 1,310,000.00 USD | `-54.74%` | `1,243.78` |
| `Live` | `Long` | `1065.00` | 850,310,000.00 USD | 0.00 USD | 184,790.00 USD | `-54.31%` | `173.51` |
| `Live` | `Long` | `1075.00` | 850,120,000.00 USD | 0.00 USD | 670,040.00 USD | `-53.88%` | `623.30` |
| `Live` | `Long` | `1085.00` | 849,450,000.00 USD | 0.00 USD | 33,280.00 USD | `-53.45%` | `30.67` |
| `Live` | `Long` | `1095.00` | 849,420,000.00 USD | 0.00 USD | 1,700,000.00 USD | `-53.02%` | `1,556.96` |
| `Live` | `Long` | `1105.00` | 847,710,000.00 USD | 0.00 USD | 220,280.00 USD | `-52.59%` | `199.35` |
| `Live` | `Long` | `1115.00` | 847,490,000.00 USD | 0.00 USD | 102,200.00 USD | `-52.16%` | `91.66` |
| `Live` | `Long` | `1125.00` | 847,390,000.00 USD | 0.00 USD | 75,690.00 USD | `-51.73%` | `67.28` |
| `Live` | `Long` | `1135.00` | 847,310,000.00 USD | 0.00 USD | 252,620.00 USD | `-51.30%` | `222.57` |
| `Live` | `Long` | `1145.00` | 847,060,000.00 USD | 0.00 USD | 287,050.00 USD | `-50.88%` | `250.70` |
| `Live` | `Long` | `1155.00` | 846,770,000.00 USD | 0.00 USD | 471,300.00 USD | `-50.45%` | `408.05` |
| `Live` | `Long` | `1165.00` | 846,300,000.00 USD | 0.00 USD | 14,090.00 USD | `-50.02%` | `12.09` |
| `Live` | `Long` | `1175.00` | 846,290,000.00 USD | 0.00 USD | 212,590.00 USD | `-49.59%` | `180.93` |
| `Live` | `Long` | `1185.00` | 846,080,000.00 USD | 0.00 USD | 270,070.00 USD | `-49.16%` | `227.90` |
| `Live` | `Long` | `1195.00` | 845,810,000.00 USD | 0.00 USD | 346,720.00 USD | `-48.73%` | `290.14` |
| `Live` | `Long` | `1205.00` | 845,460,000.00 USD | 0.00 USD | 908,570.00 USD | `-48.30%` | `754.00` |
| `Live` | `Long` | `1215.00` | 844,550,000.00 USD | 0.00 USD | 180,900.00 USD | `-47.87%` | `148.89` |
| `Live` | `Long` | `1225.00` | 844,370,000.00 USD | 0.00 USD | 11,270,000.00 USD | `-47.44%` | `9,200.63` |
| `Live` | `Long` | `1235.00` | 833,100,000.00 USD | 0.00 USD | 195,730.00 USD | `-47.01%` | `158.49` |
| `Live` | `Long` | `1245.00` | 832,900,000.00 USD | 0.00 USD | 313,430.00 USD | `-46.58%` | `251.75` |
| `Live` | `Long` | `1255.00` | 832,590,000.00 USD | 0.00 USD | 667,560.00 USD | `-46.16%` | `531.92` |
| `Live` | `Long` | `1265.00` | 831,920,000.00 USD | 0.00 USD | 1,580,000.00 USD | `-45.73%` | `1,245.95` |
| `Live` | `Long` | `1275.00` | 830,350,000.00 USD | 0.00 USD | 66,370.00 USD | `-45.30%` | `52.06` |
| `Live` | `Long` | `1285.00` | 830,280,000.00 USD | 0.00 USD | 16,150,000.00 USD | `-44.87%` | `12,569.48` |
| `Live` | `Long` | `1295.00` | 814,130,000.00 USD | 0.00 USD | 398,630.00 USD | `-44.44%` | `307.83` |
| `Live` | `Long` | `1305.00` | 813,730,000.00 USD | 0.00 USD | 198,210.00 USD | `-44.01%` | `151.89` |
| `Live` | `Long` | `1315.00` | 813,530,000.00 USD | 0.00 USD | 504,350.00 USD | `-43.58%` | `383.54` |
| `Live` | `Long` | `1325.00` | 813,030,000.00 USD | 0.00 USD | 562,110.00 USD | `-43.15%` | `424.24` |
| `Live` | `Long` | `1335.00` | 812,460,000.00 USD | 0.00 USD | 373,490.00 USD | `-42.72%` | `279.77` |
| `Live` | `Long` | `1345.00` | 812,090,000.00 USD | 0.00 USD | 644,470.00 USD | `-42.29%` | `479.16` |
| `Live` | `Long` | `1355.00` | 811,450,000.00 USD | 0.00 USD | 61,580.00 USD | `-41.87%` | `45.44` |
| `Live` | `Long` | `1365.00` | 811,390,000.00 USD | 0.00 USD | 7,930,000.00 USD | `-41.44%` | `5,812.03` |
| `Live` | `Long` | `1375.00` | 803,450,000.00 USD | 0.00 USD | 245,580.00 USD | `-41.01%` | `178.60` |
| `Live` | `Long` | `1385.00` | 803,210,000.00 USD | 0.00 USD | 171,880.00 USD | `-40.58%` | `124.10` |
| `Live` | `Long` | `1395.00` | 803,030,000.00 USD | 0.00 USD | 302,930.00 USD | `-40.15%` | `217.15` |
| `Live` | `Long` | `1405.00` | 802,730,000.00 USD | 0.00 USD | 10,010,000.00 USD | `-39.72%` | `7,122.90` |
| `Live` | `Long` | `1415.00` | 792,720,000.00 USD | 0.00 USD | 22,360,000.00 USD | `-39.29%` | `15,802.49` |
| `Live` | `Long` | `1425.00` | 770,360,000.00 USD | 0.00 USD | 1,430,000.00 USD | `-38.86%` | `1,002.87` |
| `Live` | `Long` | `1435.00` | 768,930,000.00 USD | 0.00 USD | 451,460.00 USD | `-38.43%` | `314.60` |
| `Live` | `Long` | `1445.00` | 768,480,000.00 USD | 0.00 USD | 57,490.00 USD | `-38.00%` | `39.78` |
| `Live` | `Long` | `1455.00` | 768,430,000.00 USD | 0.00 USD | 14,630,000.00 USD | `-37.58%` | `10,055.67` |
| `Live` | `Long` | `1465.00` | 753,790,000.00 USD | 0.00 USD | 390,720.00 USD | `-37.15%` | `266.71` |
| `Live` | `Long` | `1475.00` | 753,400,000.00 USD | 0.00 USD | 2,310,000.00 USD | `-36.72%` | `1,567.94` |
| `Live` | `Long` | `1485.00` | 751,090,000.00 USD | 0.00 USD | 4,640,000.00 USD | `-36.29%` | `3,122.42` |
| `Live` | `Long` | `1495.00` | 746,450,000.00 USD | 0.00 USD | 345,390.00 USD | `-35.86%` | `231.03` |
| `Live` | `Long` | `1505.00` | 746,110,000.00 USD | 0.00 USD | 389,670.00 USD | `-35.43%` | `258.92` |
| `Live` | `Long` | `1515.00` | 745,720,000.00 USD | 0.00 USD | 415,830.00 USD | `-35.00%` | `274.48` |
| `Live` | `Long` | `1525.00` | 745,300,000.00 USD | 0.00 USD | 18,520,000.00 USD | `-34.57%` | `12,144.91` |
| `Live` | `Long` | `1535.00` | 726,780,000.00 USD | 0.00 USD | 1,030,000.00 USD | `-34.14%` | `672.43` |
| `Live` | `Long` | `1545.00` | 725,750,000.00 USD | 0.00 USD | 22,690,000.00 USD | `-33.71%` | `14,687.30` |
| `Live` | `Long` | `1555.00` | 703,060,000.00 USD | 0.00 USD | 507,200.00 USD | `-33.28%` | `326.17` |
| `Live` | `Long` | `1565.00` | 702,550,000.00 USD | 0.00 USD | 25,200,000.00 USD | `-32.86%` | `16,099.21` |
| `Live` | `Long` | `1575.00` | 677,360,000.00 USD | 0.00 USD | 277,870.00 USD | `-32.43%` | `176.43` |
| `Live` | `Long` | `1585.00` | 677,080,000.00 USD | 0.00 USD | 252,400.00 USD | `-32.00%` | `159.24` |
| `Live` | `Long` | `1595.00` | 676,830,000.00 USD | 0.00 USD | 7,530,000.00 USD | `-31.57%` | `4,722.05` |
| `Live` | `Long` | `1605.00` | 669,290,000.00 USD | 0.00 USD | 18,470,000.00 USD | `-31.14%` | `11,507.47` |
| `Live` | `Long` | `1615.00` | 650,820,000.00 USD | 0.00 USD | 266,450.00 USD | `-30.71%` | `164.98` |
| `Live` | `Long` | `1625.00` | 650,560,000.00 USD | 0.00 USD | 170,470.00 USD | `-30.28%` | `104.91` |
| `Live` | `Long` | `1635.00` | 650,390,000.00 USD | 0.00 USD | 21,150,000.00 USD | `-29.85%` | `12,935.60` |
| `Live` | `Long` | `1645.00` | 629,240,000.00 USD | 0.00 USD | 36,490,000.00 USD | `-29.42%` | `22,181.13` |
| `Live` | `Long` | `1655.00` | 592,750,000.00 USD | 0.00 USD | 965,970.00 USD | `-28.99%` | `583.67` |
| `Live` | `Long` | `1665.00` | 591,780,000.00 USD | 0.00 USD | 773,230.00 USD | `-28.57%` | `464.40` |
| `Live` | `Long` | `1675.00` | 591,010,000.00 USD | 0.00 USD | 11,590,000.00 USD | `-28.14%` | `6,920.35` |
| `Live` | `Long` | `1685.00` | 579,420,000.00 USD | 0.00 USD | 1,390,000.00 USD | `-27.71%` | `827.62` |
| `Live` | `Long` | `1695.00` | 578,020,000.00 USD | 0.00 USD | 596,490.00 USD | `-27.28%` | `351.91` |
| `Live` | `Long` | `1705.00` | 577,430,000.00 USD | 0.00 USD | 1,510,000.00 USD | `-26.85%` | `885.52` |
| `Live` | `Long` | `1715.00` | 575,920,000.00 USD | 0.00 USD | 461,590.00 USD | `-26.42%` | `269.15` |
| `Live` | `Long` | `1725.00` | 575,460,000.00 USD | 0.00 USD | 29,000,000.00 USD | `-25.99%` | `16,813.82` |
| `Live` | `Long` | `1735.00` | 546,450,000.00 USD | 0.00 USD | 18,850,000.00 USD | `-25.56%` | `10,864.50` |
| `Live` | `Long` | `1745.00` | 527,600,000.00 USD | 0.00 USD | 1,460,000.00 USD | `-25.13%` | `835.05` |
| `Live` | `Long` | `1755.00` | 526,150,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-24.70%` | `628.36` |
| `Live` | `Long` | `1765.00` | 525,040,000.00 USD | 0.00 USD | 1,230,000.00 USD | `-24.27%` | `697.92` |
| `Live` | `Long` | `1775.00` | 523,810,000.00 USD | 0.00 USD | 1,440,000.00 USD | `-23.85%` | `811.30` |
| `Live` | `Long` | `1785.00` | 522,370,000.00 USD | 0.00 USD | 54,240,000.00 USD | `-23.42%` | `30,384.44` |
| `Live` | `Long` | `1795.00` | 468,130,000.00 USD | 0.00 USD | 16,770,000.00 USD | `-22.99%` | `9,344.14` |
| `Live` | `Long` | `1805.00` | 451,360,000.00 USD | 0.00 USD | 1,860,000.00 USD | `-22.56%` | `1,029.36` |
| `Live` | `Long` | `1815.00` | 449,500,000.00 USD | 0.00 USD | 712,350.00 USD | `-22.13%` | `392.48` |
| `Live` | `Long` | `1825.00` | 448,790,000.00 USD | 0.00 USD | 620,950.00 USD | `-21.70%` | `340.25` |
| `Live` | `Long` | `1835.00` | 448,170,000.00 USD | 0.00 USD | 1,690,000.00 USD | `-21.27%` | `921.64` |
| `Live` | `Long` | `1845.00` | 446,480,000.00 USD | 0.00 USD | 1,260,000.00 USD | `-20.84%` | `684.33` |
| `Live` | `Long` | `1855.00` | 445,220,000.00 USD | 0.00 USD | 13,970,000.00 USD | `-20.41%` | `7,533.18` |
| `Live` | `Long` | `1865.00` | 431,240,000.00 USD | 0.00 USD | 2,030,000.00 USD | `-19.98%` | `1,088.91` |
| `Live` | `Long` | `1875.00` | 429,210,000.00 USD | 0.00 USD | 5,580,000.00 USD | `-19.56%` | `2,974.53` |
| `Live` | `Long` | `1885.00` | 423,630,000.00 USD | 0.00 USD | 2,740,000.00 USD | `-19.13%` | `1,452.97` |
| `Live` | `Long` | `1895.00` | 420,900,000.00 USD | 0.00 USD | 5,240,000.00 USD | `-18.70%` | `2,764.93` |
| `Live` | `Long` | `1905.00` | 415,660,000.00 USD | 0.00 USD | 1,510,000.00 USD | `-18.27%` | `793.34` |
| `Live` | `Long` | `1915.00` | 414,140,000.00 USD | 0.00 USD | 28,440,000.00 USD | `-17.84%` | `14,850.07` |
| `Live` | `Long` | `1925.00` | 385,710,000.00 USD | 0.00 USD | 4,070,000.00 USD | `-17.41%` | `2,112.81` |
| `Live` | `Long` | `1935.00` | 381,640,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-16.98%` | `584.51` |
| `Live` | `Long` | `1945.00` | 380,510,000.00 USD | 0.00 USD | 657,850.00 USD | `-16.55%` | `338.23` |
| `Live` | `Long` | `1955.00` | 379,850,000.00 USD | 0.00 USD | 3,580,000.00 USD | `-16.12%` | `1,832.18` |
| `Live` | `Long` | `1965.00` | 376,270,000.00 USD | 0.00 USD | 751,430.00 USD | `-15.69%` | `382.41` |
| `Live` | `Long` | `1975.00` | 375,520,000.00 USD | 0.00 USD | 6,100,000.00 USD | `-15.27%` | `3,086.76` |
| `Live` | `Long` | `1985.00` | 369,420,000.00 USD | 0.00 USD | 5,230,000.00 USD | `-14.84%` | `2,635.89` |
| `Live` | `Long` | `1995.00` | 364,190,000.00 USD | 0.00 USD | 576,630.00 USD | `-14.41%` | `289.04` |
| `Live` | `Long` | `2005.00` | 363,610,000.00 USD | 0.00 USD | 2,810,000.00 USD | `-13.98%` | `1,403.02` |
| `Live` | `Long` | `2015.00` | 360,800,000.00 USD | 0.00 USD | 3,250,000.00 USD | `-13.55%` | `1,610.57` |
| `Live` | `Long` | `2025.00` | 357,550,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-13.12%` | `557.23` |
| `Live` | `Long` | `2035.00` | 356,430,000.00 USD | 0.00 USD | 1,050,000.00 USD | `-12.69%` | `514.68` |
| `Live` | `Long` | `2045.00` | 355,380,000.00 USD | 0.00 USD | 20,160,000.00 USD | `-12.26%` | `9,859.28` |
| `Live` | `Long` | `2055.00` | 335,220,000.00 USD | 0.00 USD | 4,750,000.00 USD | `-11.83%` | `2,310.38` |
| `Live` | `Long` | `2065.00` | 330,470,000.00 USD | 0.00 USD | 1,260,000.00 USD | `-11.40%` | `610.96` |
| `Live` | `Long` | `2075.00` | 329,210,000.00 USD | 0.00 USD | 1,330,000.00 USD | `-10.97%` | `642.74` |
| `Live` | `Long` | `2085.00` | 327,870,000.00 USD | 0.00 USD | 2,380,000.00 USD | `-10.55%` | `1,139.12` |
| `Live` | `Long` | `2095.00` | 325,500,000.00 USD | 0.00 USD | 1,200,000.00 USD | `-10.12%` | `573.80` |
| `Live` | `Long` | `2105.00` | 324,300,000.00 USD | 0.00 USD | 1,690,000.00 USD | `-9.69%` | `800.85` |
| `Live` | `Long` | `2115.00` | 322,610,000.00 USD | 0.00 USD | 20,530,000.00 USD | `-9.26%` | `9,705.11` |
| `Live` | `Long` | `2125.00` | 302,080,000.00 USD | 0.00 USD | 1,010,000.00 USD | `-8.83%` | `477.25` |
| `Live` | `Long` | `2135.00` | 301,070,000.00 USD | 0.00 USD | 3,270,000.00 USD | `-8.40%` | `1,532.05` |
| `Live` | `Long` | `2145.00` | 297,800,000.00 USD | 0.00 USD | 9,500,000.00 USD | `-7.97%` | `4,429.12` |
| `Live` | `Long` | `2155.00` | 288,300,000.00 USD | 0.00 USD | 17,990,000.00 USD | `-7.54%` | `8,348.92` |
| `Live` | `Long` | `2165.00` | 270,310,000.00 USD | 0.00 USD | 6,290,000.00 USD | `-7.11%` | `2,907.59` |
| `Live` | `Long` | `2175.00` | 264,010,000.00 USD | 0.00 USD | 108,810,000.00 USD | `-6.68%` | `50,027.23` |
| `Live` | `Long` | `2185.00` | 155,200,000.00 USD | 0.00 USD | 111,820,000.00 USD | `-6.26%` | `51,178.44` |
| `Live` | `Long` | `2195.00` | 43,380,000.00 USD | 0.00 USD | 1,260,000.00 USD | `-5.83%` | `574.40` |
| `Live` | `Long` | `2205.00` | 42,120,000.00 USD | 0.00 USD | 1,290,000.00 USD | `-5.40%` | `585.97` |
| `Live` | `Long` | `2215.00` | 40,820,000.00 USD | 0.00 USD | 1,710,000.00 USD | `-4.97%` | `770.25` |
| `Live` | `Long` | `2225.00` | 39,120,000.00 USD | 0.00 USD | 2,840,000.00 USD | `-4.54%` | `1,274.92` |
| `Live` | `Long` | `2235.00` | 36,280,000.00 USD | 0.00 USD | 1,030,000.00 USD | `-4.11%` | `462.53` |
| `Live` | `Long` | `2245.00` | 35,250,000.00 USD | 0.00 USD | 4,620,000.00 USD | `-3.68%` | `2,059.94` |
| `Live` | `Long` | `2255.00` | 30,620,000.00 USD | 0.00 USD | 11,260,000.00 USD | `-3.25%` | `4,993.11` |
| `Live` | `Long` | `2265.00` | 19,360,000.00 USD | 0.00 USD | 4,930,000.00 USD | `-2.82%` | `2,176.83` |
| `Live` | `Long` | `2275.00` | 14,430,000.00 USD | 0.00 USD | 4,720,000.00 USD | `-2.39%` | `2,074.64` |
| `Live` | `Long` | `2285.00` | 9,710,000.00 USD | 0.00 USD | 3,920,000.00 USD | `-1.96%` | `1,716.51` |
| `Live` | `Long` | `2295.00` | 5,790,000.00 USD | 0.00 USD | 3,480,000.00 USD | `-1.54%` | `1,515.59` |
| `Live` | `Long` | `2305.00` | 2,310,000.00 USD | 0.00 USD | 1,030,000.00 USD | `-1.11%` | `446.65` |
| `Live` | `Long` | `2315.00` | 1,280,000.00 USD | 0.00 USD | 938,780.00 USD | `-0.68%` | `405.52` |
| `Live` | `Long` | `2325.00` | 344,610.00 USD | 0.00 USD | 344,610.00 USD | `-0.25%` | `148.22` |
| `Live` | `Short` | `2335.00` | 735.29 USD | 735.29 USD | 0.00 USD | `+0.18%` | `0.31` |
| `Live` | `Short` | `2365.00` | 1,340.00 USD | 602.37 USD | 0.00 USD | `+1.47%` | `0.25` |
| `Live` | `Short` | `2375.00` | 490,000.00 USD | 488,660.00 USD | 0.00 USD | `+1.90%` | `205.75` |
| `Live` | `Short` | `2385.00` | 4,410,000.00 USD | 3,920,000.00 USD | 0.00 USD | `+2.33%` | `1,642.26` |
| `Live` | `Short` | `2395.00` | 8,670,000.00 USD | 4,260,000.00 USD | 0.00 USD | `+2.75%` | `1,778.65` |
| `Live` | `Short` | `2405.00` | 17,730,000.00 USD | 9,070,000.00 USD | 0.00 USD | `+3.18%` | `3,770.50` |
| `Live` | `Short` | `2415.00` | 17,990,000.00 USD | 255,650.00 USD | 0.00 USD | `+3.61%` | `105.86` |
| `Live` | `Short` | `2425.00` | 18,810,000.00 USD | 815,490.00 USD | 0.00 USD | `+4.04%` | `336.28` |
| `Live` | `Short` | `2435.00` | 26,730,000.00 USD | 7,920,000.00 USD | 0.00 USD | `+4.47%` | `3,253.00` |
| `Live` | `Short` | `2445.00` | 26,890,000.00 USD | 158,630.00 USD | 0.00 USD | `+4.90%` | `64.88` |
| `Live` | `Short` | `2455.00` | 26,980,000.00 USD | 98,850.00 USD | 0.00 USD | `+5.33%` | `40.26` |
| `Live` | `Short` | `2465.00` | 27,060,000.00 USD | 79,760.00 USD | 0.00 USD | `+5.76%` | `32.36` |
| `Live` | `Short` | `2475.00` | 27,900,000.00 USD | 836,210.00 USD | 0.00 USD | `+6.19%` | `337.86` |
| `Live` | `Short` | `2485.00` | 29,900,000.00 USD | 2,000,000.00 USD | 0.00 USD | `+6.62%` | `804.51` |
| `Live` | `Short` | `2495.00` | 30,790,000.00 USD | 886,080.00 USD | 0.00 USD | `+7.04%` | `355.14` |
| `Live` | `Short` | `2505.00` | 30,910,000.00 USD | 120,200.00 USD | 0.00 USD | `+7.47%` | `47.98` |
| `Live` | `Short` | `2515.00` | 31,050,000.00 USD | 142,620.00 USD | 0.00 USD | `+7.90%` | `56.71` |
| `Live` | `Short` | `2525.00` | 32,120,000.00 USD | 1,070,000.00 USD | 0.00 USD | `+8.33%` | `422.78` |
| `Live` | `Short` | `2535.00` | 33,420,000.00 USD | 1,310,000.00 USD | 0.00 USD | `+8.76%` | `515.01` |
| `Live` | `Short` | `2545.00` | 39,550,000.00 USD | 6,130,000.00 USD | 0.00 USD | `+9.19%` | `2,409.85` |
| `Live` | `Short` | `2555.00` | 40,480,000.00 USD | 924,540.00 USD | 0.00 USD | `+9.62%` | `361.86` |
| `Live` | `Short` | `2565.00` | 43,900,000.00 USD | 3,420,000.00 USD | 0.00 USD | `+10.05%` | `1,333.61` |
| `Live` | `Short` | `2575.00` | 56,010,000.00 USD | 12,110,000.00 USD | 0.00 USD | `+10.48%` | `4,701.73` |
| `Live` | `Short` | `2585.00` | 82,490,000.00 USD | 26,480,000.00 USD | 0.00 USD | `+10.91%` | `10,245.03` |
| `Live` | `Short` | `2595.00` | 90,790,000.00 USD | 8,300,000.00 USD | 0.00 USD | `+11.34%` | `3,199.18` |
| `Live` | `Short` | `2605.00` | 91,330,000.00 USD | 534,220.00 USD | 0.00 USD | `+11.76%` | `205.07` |
| `Live` | `Short` | `2615.00` | 92,250,000.00 USD | 926,240.00 USD | 0.00 USD | `+12.19%` | `354.20` |
| `Live` | `Short` | `2625.00` | 92,890,000.00 USD | 637,700.00 USD | 0.00 USD | `+12.62%` | `242.93` |
| `Live` | `Short` | `2635.00` | 92,990,000.00 USD | 99,330.00 USD | 0.00 USD | `+13.05%` | `37.70` |
| `Live` | `Short` | `2645.00` | 93,670,000.00 USD | 681,840.00 USD | 0.00 USD | `+13.48%` | `257.79` |
| `Live` | `Short` | `2655.00` | 128,890,000.00 USD | 35,210,000.00 USD | 0.00 USD | `+13.91%` | `13,263.45` |
| `Live` | `Short` | `2665.00` | 128,950,000.00 USD | 62,560.00 USD | 0.00 USD | `+14.34%` | `23.47` |
| `Live` | `Short` | `2675.00` | 129,260,000.00 USD | 310,460.00 USD | 0.00 USD | `+14.77%` | `116.06` |
| `Live` | `Short` | `2685.00` | 136,580,000.00 USD | 7,320,000.00 USD | 0.00 USD | `+15.20%` | `2,727.83` |
| `Live` | `Short` | `2695.00` | 136,980,000.00 USD | 395,990.00 USD | 0.00 USD | `+15.63%` | `146.94` |
| `Live` | `Short` | `2705.00` | 166,530,000.00 USD | 29,550,000.00 USD | 0.00 USD | `+16.05%` | `10,925.64` |
| `Live` | `Short` | `2715.00` | 182,550,000.00 USD | 16,020,000.00 USD | 0.00 USD | `+16.48%` | `5,898.72` |
| `Live` | `Short` | `2725.00` | 183,000,000.00 USD | 454,310.00 USD | 0.00 USD | `+16.91%` | `166.72` |
| `Live` | `Short` | `2735.00` | 186,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | `+17.34%` | `1,319.26` |
| `Live` | `Short` | `2745.00` | 187,620,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+17.77%` | `366.27` |
| `Live` | `Short` | `2755.00` | 188,350,000.00 USD | 735,710.00 USD | 0.00 USD | `+18.20%` | `267.05` |
| `Live` | `Short` | `2765.00` | 188,500,000.00 USD | 149,020.00 USD | 0.00 USD | `+18.63%` | `53.89` |
| `Live` | `Short` | `2775.00` | 188,840,000.00 USD | 334,480.00 USD | 0.00 USD | `+19.06%` | `120.53` |
| `Live` | `Short` | `2785.00` | 195,790,000.00 USD | 6,950,000.00 USD | 0.00 USD | `+19.49%` | `2,497.20` |
| `Live` | `Short` | `2795.00` | 196,020,000.00 USD | 228,090.00 USD | 0.00 USD | `+19.92%` | `81.61` |
| `Live` | `Short` | `2805.00` | 196,610,000.00 USD | 595,820.00 USD | 0.00 USD | `+20.34%` | `212.41` |
| `Live` | `Short` | `2815.00` | 196,900,000.00 USD | 286,110.00 USD | 0.00 USD | `+20.77%` | `101.64` |
| `Live` | `Short` | `2825.00` | 196,960,000.00 USD | 58,720.00 USD | 0.00 USD | `+21.20%` | `20.78` |
| `Live` | `Short` | `2835.00` | 200,310,000.00 USD | 3,350,000.00 USD | 0.00 USD | `+21.63%` | `1,180.49` |
| `Live` | `Short` | `2845.00` | 202,600,000.00 USD | 2,290,000.00 USD | 0.00 USD | `+22.06%` | `805.66` |
| `Live` | `Short` | `2855.00` | 202,850,000.00 USD | 253,200.00 USD | 0.00 USD | `+22.49%` | `88.69` |
| `Live` | `Short` | `2865.00` | 234,140,000.00 USD | 31,290,000.00 USD | 0.00 USD | `+22.92%` | `10,920.16` |
| `Live` | `Short` | `2875.00` | 270,970,000.00 USD | 36,840,000.00 USD | 0.00 USD | `+23.35%` | `12,813.13` |
| `Live` | `Short` | `2885.00` | 275,620,000.00 USD | 4,650,000.00 USD | 0.00 USD | `+23.78%` | `1,611.30` |
| `Live` | `Short` | `2895.00` | 276,270,000.00 USD | 645,080.00 USD | 0.00 USD | `+24.21%` | `222.83` |
| `Live` | `Short` | `2905.00` | 277,000,000.00 USD | 736,740.00 USD | 0.00 USD | `+24.64%` | `253.61` |
| `Live` | `Short` | `2915.00` | 277,190,000.00 USD | 183,180.00 USD | 0.00 USD | `+25.06%` | `62.84` |
| `Live` | `Short` | `2925.00` | 303,810,000.00 USD | 26,630,000.00 USD | 0.00 USD | `+25.49%` | `9,102.89` |
| `Live` | `Short` | `2935.00` | 303,840,000.00 USD | 27,250.00 USD | 0.00 USD | `+25.92%` | `9.29` |
| `Live` | `Short` | `2945.00` | 304,760,000.00 USD | 919,870.00 USD | 0.00 USD | `+26.35%` | `312.35` |
| `Live` | `Short` | `2955.00` | 312,570,000.00 USD | 7,810,000.00 USD | 0.00 USD | `+26.78%` | `2,641.54` |
| `Live` | `Short` | `2965.00` | 333,410,000.00 USD | 20,840,000.00 USD | 0.00 USD | `+27.21%` | `7,028.13` |
| `Live` | `Short` | `2975.00` | 334,740,000.00 USD | 1,330,000.00 USD | 0.00 USD | `+27.64%` | `448.62` |
| `Live` | `Short` | `2985.00` | 335,700,000.00 USD | 955,840.00 USD | 0.00 USD | `+28.07%` | `320.22` |
| `Live` | `Short` | `2995.00` | 336,690,000.00 USD | 989,880.00 USD | 0.00 USD | `+28.50%` | `330.51` |
| `Live` | `Short` | `3005.00` | 338,910,000.00 USD | 2,230,000.00 USD | 0.00 USD | `+28.93%` | `740.94` |
| `Live` | `Short` | `3015.00` | 341,310,000.00 USD | 2,400,000.00 USD | 0.00 USD | `+29.35%` | `795.27` |
| `Live` | `Short` | `3025.00` | 343,750,000.00 USD | 2,440,000.00 USD | 0.00 USD | `+29.78%` | `808.08` |
| `Live` | `Short` | `3035.00` | 352,880,000.00 USD | 9,130,000.00 USD | 0.00 USD | `+30.21%` | `3,007.16` |
| `Live` | `Short` | `3045.00` | 367,860,000.00 USD | 14,980,000.00 USD | 0.00 USD | `+30.64%` | `4,918.60` |
| `Live` | `Short` | `3055.00` | 371,860,000.00 USD | 4,010,000.00 USD | 0.00 USD | `+31.07%` | `1,311.11` |
| `Live` | `Short` | `3065.00` | 372,190,000.00 USD | 329,030.00 USD | 0.00 USD | `+31.50%` | `107.35` |
| `Live` | `Short` | `3075.00` | 376,200,000.00 USD | 4,010,000.00 USD | 0.00 USD | `+31.93%` | `1,304.44` |
| `Live` | `Short` | `3085.00` | 377,680,000.00 USD | 1,470,000.00 USD | 0.00 USD | `+32.36%` | `477.80` |
| `Live` | `Short` | `3095.00` | 378,230,000.00 USD | 548,480.00 USD | 0.00 USD | `+32.79%` | `177.22` |
| `Live` | `Short` | `3105.00` | 378,330,000.00 USD | 102,180.00 USD | 0.00 USD | `+33.22%` | `32.91` |
| `Live` | `Short` | `3115.00` | 378,720,000.00 USD | 390,660.00 USD | 0.00 USD | `+33.65%` | `125.41` |
| `Live` | `Short` | `3125.00` | 378,870,000.00 USD | 150,120.00 USD | 0.00 USD | `+34.07%` | `48.04` |
| `Live` | `Short` | `3135.00` | 380,590,000.00 USD | 1,720,000.00 USD | 0.00 USD | `+34.50%` | `549.87` |
| `Live` | `Short` | `3145.00` | 380,880,000.00 USD | 284,010.00 USD | 0.00 USD | `+34.93%` | `90.30` |
| `Live` | `Short` | `3155.00` | 387,030,000.00 USD | 6,160,000.00 USD | 0.00 USD | `+35.36%` | `1,951.33` |
| `Live` | `Short` | `3165.00` | 387,060,000.00 USD | 28,620.00 USD | 0.00 USD | `+35.79%` | `9.04` |
| `Live` | `Short` | `3175.00` | 387,720,000.00 USD | 659,480.00 USD | 0.00 USD | `+36.22%` | `207.71` |
| `Live` | `Short` | `3185.00` | 388,520,000.00 USD | 800,040.00 USD | 0.00 USD | `+36.65%` | `251.19` |
| `Live` | `Short` | `3195.00` | 392,320,000.00 USD | 3,800,000.00 USD | 0.00 USD | `+37.08%` | `1,189.53` |
| `Live` | `Short` | `3205.00` | 392,380,000.00 USD | 57,210.00 USD | 0.00 USD | `+37.51%` | `17.85` |
| `Live` | `Short` | `3215.00` | 398,070,000.00 USD | 5,690,000.00 USD | 0.00 USD | `+37.94%` | `1,769.85` |
| `Live` | `Short` | `3225.00` | 398,300,000.00 USD | 231,490.00 USD | 0.00 USD | `+38.36%` | `71.78` |
| `Live` | `Short` | `3235.00` | 406,890,000.00 USD | 8,580,000.00 USD | 0.00 USD | `+38.79%` | `2,653.52` |
| `Live` | `Short` | `3245.00` | 407,080,000.00 USD | 192,580.00 USD | 0.00 USD | `+39.22%` | `59.35` |
| `Live` | `Short` | `3255.00` | 407,440,000.00 USD | 362,380.00 USD | 0.00 USD | `+39.65%` | `111.33` |
| `Live` | `Short` | `3265.00` | 407,450,000.00 USD | 6,720.00 USD | 0.00 USD | `+40.08%` | `2.06` |
| `Live` | `Short` | `3275.00` | 407,490,000.00 USD | 39,320.00 USD | 0.00 USD | `+40.51%` | `12.01` |
| `Live` | `Short` | `3285.00` | 416,060,000.00 USD | 8,570,000.00 USD | 0.00 USD | `+40.94%` | `2,608.84` |
| `Live` | `Short` | `3295.00` | 417,390,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+41.37%` | `405.73` |
| `Live` | `Short` | `3305.00` | 417,400,000.00 USD | 10,180.00 USD | 0.00 USD | `+41.80%` | `3.08` |
| `Live` | `Short` | `3315.00` | 429,050,000.00 USD | 11,650,000.00 USD | 0.00 USD | `+42.23%` | `3,513.67` |
| `Live` | `Short` | `3325.00` | 429,080,000.00 USD | 31,050.00 USD | 0.00 USD | `+42.65%` | `9.34` |
| `Live` | `Short` | `3335.00` | 429,140,000.00 USD | 55,420.00 USD | 0.00 USD | `+43.08%` | `16.62` |
| `Live` | `Short` | `3345.00` | 429,930,000.00 USD | 790,070.00 USD | 0.00 USD | `+43.51%` | `236.19` |
| `Live` | `Short` | `3355.00` | 495,080,000.00 USD | 65,150,000.00 USD | 0.00 USD | `+43.94%` | `19,418.91` |
| `Live` | `Short` | `3365.00` | 495,620,000.00 USD | 542,970.00 USD | 0.00 USD | `+44.37%` | `161.36` |
| `Live` | `Short` | `3375.00` | 496,220,000.00 USD | 602,790.00 USD | 0.00 USD | `+44.80%` | `178.60` |
| `Live` | `Short` | `3385.00` | 496,380,000.00 USD | 156,030.00 USD | 0.00 USD | `+45.23%` | `46.10` |
| `Live` | `Short` | `3395.00` | 496,620,000.00 USD | 240,880.00 USD | 0.00 USD | `+45.66%` | `70.95` |
| `Live` | `Short` | `3405.00` | 496,730,000.00 USD | 106,090.00 USD | 0.00 USD | `+46.09%` | `31.16` |
| `Live` | `Short` | `3415.00` | 496,760,000.00 USD | 34,350.00 USD | 0.00 USD | `+46.52%` | `10.06` |
| `Live` | `Short` | `3425.00` | 511,910,000.00 USD | 15,150,000.00 USD | 0.00 USD | `+46.95%` | `4,423.26` |
| `Live` | `Short` | `3435.00` | 512,070,000.00 USD | 158,730.00 USD | 0.00 USD | `+47.37%` | `46.21` |
| `Live` | `Short` | `3445.00` | 517,270,000.00 USD | 5,200,000.00 USD | 0.00 USD | `+47.80%` | `1,509.58` |
| `Live` | `Short` | `3455.00` | 517,960,000.00 USD | 685,470.00 USD | 0.00 USD | `+48.23%` | `198.40` |
| `Live` | `Short` | `3465.00` | 518,330,000.00 USD | 377,080.00 USD | 0.00 USD | `+48.66%` | `108.82` |
| `Live` | `Short` | `3475.00` | 519,600,000.00 USD | 1,260,000.00 USD | 0.00 USD | `+49.09%` | `363.38` |
| `Live` | `Short` | `3485.00` | 519,600,000.00 USD | 8,230.00 USD | 0.00 USD | `+49.52%` | `2.36` |
| `Live` | `Short` | `3495.00` | 520,720,000.00 USD | 1,120,000.00 USD | 0.00 USD | `+49.95%` | `319.98` |
| `Live` | `Short` | `3505.00` | 520,930,000.00 USD | 206,250.00 USD | 0.00 USD | `+50.38%` | `58.84` |
| `Live` | `Short` | `3515.00` | 520,960,000.00 USD | 35,780.00 USD | 0.00 USD | `+50.81%` | `10.18` |
| `Live` | `Short` | `3525.00` | 521,090,000.00 USD | 128,540.00 USD | 0.00 USD | `+51.24%` | `36.47` |
| `Live` | `Short` | `3535.00` | 521,110,000.00 USD | 22,000.00 USD | 0.00 USD | `+51.66%` | `6.22` |
| `Live` | `Short` | `3545.00` | 528,270,000.00 USD | 7,150,000.00 USD | 0.00 USD | `+52.09%` | `2,018.21` |
| `Live` | `Short` | `3555.00` | 528,410,000.00 USD | 143,930.00 USD | 0.00 USD | `+52.52%` | `40.49` |
| `Live` | `Short` | `3565.00` | 528,460,000.00 USD | 42,110.00 USD | 0.00 USD | `+52.95%` | `11.81` |
| `Live` | `Short` | `3575.00` | 528,550,000.00 USD | 95,920.00 USD | 0.00 USD | `+53.38%` | `26.83` |
| `Live` | `Short` | `3585.00` | 529,040,000.00 USD | 490,870.00 USD | 0.00 USD | `+53.81%` | `136.92` |
| `Live` | `Short` | `3595.00` | 529,590,000.00 USD | 550,480.00 USD | 0.00 USD | `+54.24%` | `153.12` |
| `Live` | `Short` | `3605.00` | 529,680,000.00 USD | 90,010.00 USD | 0.00 USD | `+54.67%` | `24.97` |
| `Live` | `Short` | `3615.00` | 533,680,000.00 USD | 4,000,000.00 USD | 0.00 USD | `+55.10%` | `1,105.77` |
| `Live` | `Short` | `3625.00` | 642,630,000.00 USD | 108,950,000.00 USD | 0.00 USD | `+55.53%` | `30,055.84` |
| `Live` | `Short` | `3635.00` | 644,950,000.00 USD | 2,320,000.00 USD | 0.00 USD | `+55.96%` | `637.25` |
| `Live` | `Short` | `3645.00` | 645,170,000.00 USD | 218,570.00 USD | 0.00 USD | `+56.38%` | `59.96` |
| `Live` | `Short` | `3655.00` | 645,290,000.00 USD | 117,810.00 USD | 0.00 USD | `+56.81%` | `32.23` |
| `Live` | `Short` | `3665.00` | 645,500,000.00 USD | 216,740.00 USD | 0.00 USD | `+57.24%` | `59.14` |
| `Live` | `Short` | `3675.00` | 646,370,000.00 USD | 872,350.00 USD | 0.00 USD | `+57.67%` | `237.37` |
| `Live` | `Short` | `3685.00` | 654,580,000.00 USD | 8,200,000.00 USD | 0.00 USD | `+58.10%` | `2,225.82` |
| `Live` | `Short` | `3695.00` | 656,300,000.00 USD | 1,720,000.00 USD | 0.00 USD | `+58.53%` | `465.76` |
| `Live` | `Short` | `3705.00` | 657,030,000.00 USD | 731,540.00 USD | 0.00 USD | `+58.96%` | `197.45` |
| `Live` | `Short` | `3715.00` | 657,490,000.00 USD | 459,630.00 USD | 0.00 USD | `+59.39%` | `123.72` |
| `Live` | `Short` | `3725.00` | 657,750,000.00 USD | 259,140.00 USD | 0.00 USD | `+59.82%` | `69.57` |
| `Live` | `Short` | `3735.00` | 692,510,000.00 USD | 34,760,000.00 USD | 0.00 USD | `+60.25%` | `9,306.31` |
| `Live` | `Short` | `3745.00` | 693,370,000.00 USD | 863,120.00 USD | 0.00 USD | `+60.67%` | `230.47` |
| `Live` | `Short` | `3755.00` | 706,840,000.00 USD | 13,470,000.00 USD | 0.00 USD | `+61.10%` | `3,586.22` |
| `Live` | `Short` | `3765.00` | 706,900,000.00 USD | 66,550.00 USD | 0.00 USD | `+61.53%` | `17.68` |
| `Live` | `Short` | `3775.00` | 707,270,000.00 USD | 367,220.00 USD | 0.00 USD | `+61.96%` | `97.28` |
| `Live` | `Short` | `3785.00` | 707,310,000.00 USD | 39,580.00 USD | 0.00 USD | `+62.39%` | `10.46` |
| `Live` | `Short` | `3795.00` | 707,390,000.00 USD | 81,940.00 USD | 0.00 USD | `+62.82%` | `21.59` |
| `Live` | `Short` | `3805.00` | 707,860,000.00 USD | 472,390.00 USD | 0.00 USD | `+63.25%` | `124.15` |
| `Live` | `Short` | `3815.00` | 707,870,000.00 USD | 2,690.00 USD | 0.00 USD | `+63.68%` | `0.71` |
| `Live` | `Short` | `3825.00` | 708,200,000.00 USD | 328,880.00 USD | 0.00 USD | `+64.11%` | `85.98` |
| `Live` | `Short` | `3835.00` | 1,120,000,000.00 USD | 408,860,000.00 USD | 0.00 USD | `+64.54%` | `106,612.52` |
| `Live` | `Short` | `3845.00` | 1,120,000,000.00 USD | 2,160,000.00 USD | 0.00 USD | `+64.96%` | `561.05` |
| `Live` | `Short` | `3855.00` | 1,120,000,000.00 USD | 176,530.00 USD | 0.00 USD | `+65.39%` | `45.79` |
| `Live` | `Short` | `3865.00` | 1,120,000,000.00 USD | 1,030,000.00 USD | 0.00 USD | `+65.82%` | `266.48` |
| `Live` | `Short` | `3875.00` | 1,120,000,000.00 USD | 12,320.00 USD | 0.00 USD | `+66.25%` | `3.18` |
| `Live` | `Short` | `3885.00` | 1,140,000,000.00 USD | 17,110,000.00 USD | 0.00 USD | `+66.68%` | `4,404.93` |
| `Live` | `Short` | `3895.00` | 1,140,000,000.00 USD | 100,530.00 USD | 0.00 USD | `+67.11%` | `25.81` |
| `Live` | `Short` | `3905.00` | 1,140,000,000.00 USD | 616,790.00 USD | 0.00 USD | `+67.54%` | `157.95` |
| `Live` | `Short` | `3915.00` | 1,140,000,000.00 USD | 567,550.00 USD | 0.00 USD | `+67.97%` | `144.97` |
| `Live` | `Short` | `3925.00` | 1,140,000,000.00 USD | 355,780.00 USD | 0.00 USD | `+68.40%` | `90.65` |
| `Live` | `Short` | `3935.00` | 1,140,000,000.00 USD | 57,480.00 USD | 0.00 USD | `+68.83%` | `14.61` |
| `Live` | `Short` | `3945.00` | 1,140,000,000.00 USD | 246,510.00 USD | 0.00 USD | `+69.26%` | `62.49` |
| `Live` | `Short` | `3955.00` | 1,140,000,000.00 USD | 3,410,000.00 USD | 0.00 USD | `+69.68%` | `863.16` |
| `Live` | `Short` | `3965.00` | 1,140,000,000.00 USD | 566,950.00 USD | 0.00 USD | `+70.11%` | `142.99` |
| `Live` | `Short` | `3975.00` | 1,240,000,000.00 USD | 93,670,000.00 USD | 0.00 USD | `+70.54%` | `23,564.45` |
| `Live` | `Short` | `3985.00` | 1,240,000,000.00 USD | 123,680.00 USD | 0.00 USD | `+70.97%` | `31.04` |
| `Live` | `Short` | `3995.00` | 1,270,000,000.00 USD | 30,680,000.00 USD | 0.00 USD | `+71.40%` | `7,680.68` |
| `Live` | `Short` | `4005.00` | 1,270,000,000.00 USD | 106,160.00 USD | 0.00 USD | `+71.83%` | `26.51` |
| `Live` | `Short` | `4015.00` | 1,270,000,000.00 USD | 146,060.00 USD | 0.00 USD | `+72.26%` | `36.38` |
| `Live` | `Short` | `4025.00` | 1,270,000,000.00 USD | 247,410.00 USD | 0.00 USD | `+72.69%` | `61.47` |
| `Live` | `Short` | `4035.00` | 1,270,000,000.00 USD | 660,940.00 USD | 0.00 USD | `+73.12%` | `163.80` |
| `Live` | `Short` | `4045.00` | 1,340,000,000.00 USD | 70,130,000.00 USD | 0.00 USD | `+73.55%` | `17,337.87` |
| `Live` | `Short` | `4055.00` | 1,340,000,000.00 USD | 538,130.00 USD | 0.00 USD | `+73.97%` | `132.71` |
| `Live` | `Short` | `4065.00` | 1,340,000,000.00 USD | 2,770,000.00 USD | 0.00 USD | `+74.40%` | `681.59` |
| `Live` | `Short` | `4075.00` | 1,350,000,000.00 USD | 3,490,000.00 USD | 0.00 USD | `+74.83%` | `855.76` |
| `Live` | `Short` | `4085.00` | 1,350,000,000.00 USD | 40,820.00 USD | 0.00 USD | `+75.26%` | `9.99` |
| `Live` | `Short` | `4095.00` | 1,350,000,000.00 USD | 81,900.00 USD | 0.00 USD | `+75.69%` | `20.00` |
| `Live` | `Short` | `4105.00` | 1,350,000,000.00 USD | 93,840.00 USD | 0.00 USD | `+76.12%` | `22.86` |
| `Live` | `Short` | `4115.00` | 1,350,000,000.00 USD | 1,250.00 USD | 0.00 USD | `+76.55%` | `0.30` |
| `Live` | `Short` | `4135.00` | 1,350,000,000.00 USD | 984,160.00 USD | 0.00 USD | `+77.41%` | `238.01` |
| `Live` | `Short` | `4145.00` | 1,350,000,000.00 USD | 401,910.00 USD | 0.00 USD | `+77.84%` | `96.96` |
| `Live` | `Short` | `4155.00` | 1,350,000,000.00 USD | 531,930.00 USD | 0.00 USD | `+78.26%` | `128.02` |
| `Live` | `Short` | `4165.00` | 1,350,000,000.00 USD | 257,470.00 USD | 0.00 USD | `+78.69%` | `61.82` |
| `Live` | `Short` | `4185.00` | 1,350,000,000.00 USD | 41,230.00 USD | 0.00 USD | `+79.55%` | `9.85` |
| `Live` | `Short` | `4195.00` | 1,350,000,000.00 USD | 4,060,000.00 USD | 0.00 USD | `+79.98%` | `967.23` |
| `Live` | `Short` | `4205.00` | 1,350,000,000.00 USD | 44,500.00 USD | 0.00 USD | `+80.41%` | `10.58` |
| `Live` | `Short` | `4215.00` | 1,350,000,000.00 USD | 12,850.00 USD | 0.00 USD | `+80.84%` | `3.05` |
| `Live` | `Short` | `4225.00` | 1,350,000,000.00 USD | 93,870.00 USD | 0.00 USD | `+81.27%` | `22.22` |
| `Live` | `Short` | `4235.00` | 1,370,000,000.00 USD | 18,650,000.00 USD | 0.00 USD | `+81.70%` | `4,402.92` |
| `Live` | `Short` | `4245.00` | 1,370,000,000.00 USD | 155,690.00 USD | 0.00 USD | `+82.13%` | `36.68` |
| `Live` | `Short` | `4255.00` | 1,370,000,000.00 USD | 121,540.00 USD | 0.00 USD | `+82.56%` | `28.56` |
| `Live` | `Short` | `4265.00` | 1,370,000,000.00 USD | 68,000.00 USD | 0.00 USD | `+82.98%` | `15.94` |
| `Live` | `Short` | `4275.00` | 1,370,000,000.00 USD | 1,070.00 USD | 0.00 USD | `+83.41%` | `0.25` |
| `Live` | `Short` | `4285.00` | 1,390,000,000.00 USD | 17,280,000.00 USD | 0.00 USD | `+83.84%` | `4,033.32` |
| `Live` | `Short` | `4295.00` | 1,390,000,000.00 USD | 63,150.00 USD | 0.00 USD | `+84.27%` | `14.70` |
| `Live` | `Short` | `4305.00` | 1,390,000,000.00 USD | 200,540.00 USD | 0.00 USD | `+84.70%` | `46.58` |
| `Live` | `Short` | `4315.00` | 1,390,000,000.00 USD | 6,590.00 USD | 0.00 USD | `+85.13%` | `1.53` |
| `Live` | `Short` | `4325.00` | 1,390,000,000.00 USD | 5,830.00 USD | 0.00 USD | `+85.56%` | `1.35` |
| `Live` | `Short` | `4335.00` | 1,390,000,000.00 USD | 114,010.00 USD | 0.00 USD | `+85.99%` | `26.30` |
| `Live` | `Short` | `4355.00` | 1,390,000,000.00 USD | 22,600.00 USD | 0.00 USD | `+86.85%` | `5.19` |
| `Live` | `Short` | `4365.00` | 1,390,000,000.00 USD | 591,120.00 USD | 0.00 USD | `+87.27%` | `135.42` |
| `Live` | `Short` | `4375.00` | 1,390,000,000.00 USD | 2,160,000.00 USD | 0.00 USD | `+87.70%` | `492.79` |
| `Live` | `Short` | `4385.00` | 1,390,000,000.00 USD | 849,910.00 USD | 0.00 USD | `+88.13%` | `193.82` |
| `Live` | `Short` | `4395.00` | 1,680,000,000.00 USD | 286,590,000.00 USD | 0.00 USD | `+88.56%` | `65,209.03` |
| `Live` | `Short` | `4405.00` | 1,680,000,000.00 USD | 102,320.00 USD | 0.00 USD | `+88.99%` | `23.23` |
| `Live` | `Short` | `4415.00` | 1,680,000,000.00 USD | 471,100.00 USD | 0.00 USD | `+89.42%` | `106.71` |
| `Live` | `Short` | `4425.00` | 1,680,000,000.00 USD | 259,220.00 USD | 0.00 USD | `+89.85%` | `58.58` |
| `Live` | `Short` | `4435.00` | 1,680,000,000.00 USD | 1,940,000.00 USD | 0.00 USD | `+90.28%` | `436.40` |
| `Live` | `Short` | `4445.00` | 1,680,000,000.00 USD | 446,190.00 USD | 0.00 USD | `+90.71%` | `100.38` |
| `Live` | `Short` | `4455.00` | 1,680,000,000.00 USD | 1,380,000.00 USD | 0.00 USD | `+91.14%` | `309.78` |
| `Live` | `Short` | `4465.00` | 1,680,000,000.00 USD | 319,690.00 USD | 0.00 USD | `+91.57%` | `71.60` |
| `Live` | `Short` | `4475.00` | 1,680,000,000.00 USD | 33,190.00 USD | 0.00 USD | `+91.99%` | `7.42` |
| `Live` | `Short` | `4485.00` | 1,680,000,000.00 USD | 30,710.00 USD | 0.00 USD | `+92.42%` | `6.85` |
| `Live` | `Short` | `4495.00` | 1,680,000,000.00 USD | 24,840.00 USD | 0.00 USD | `+92.85%` | `5.53` |
| `Live` | `Short` | `4505.00` | 1,680,000,000.00 USD | 99,370.00 USD | 0.00 USD | `+93.28%` | `22.06` |
| `Live` | `Short` | `4515.00` | 1,690,000,000.00 USD | 404,790.00 USD | 0.00 USD | `+93.71%` | `89.66` |
| `Live` | `Short` | `4525.00` | 1,690,000,000.00 USD | 1,080,000.00 USD | 0.00 USD | `+94.14%` | `238.54` |
| `Live` | `Short` | `4535.00` | 1,690,000,000.00 USD | 3,360,000.00 USD | 0.00 USD | `+94.57%` | `741.36` |
| `Live` | `Short` | `4545.00` | 1,690,000,000.00 USD | 17,760.00 USD | 0.00 USD | `+95.00%` | `3.91` |
| `Live` | `Short` | `4555.00` | 1,690,000,000.00 USD | 1,030,000.00 USD | 0.00 USD | `+95.43%` | `226.48` |
| `Live` | `Short` | `4565.00` | 1,690,000,000.00 USD | 95,220.00 USD | 0.00 USD | `+95.86%` | `20.86` |
| `Live` | `Short` | `4575.00` | 1,690,000,000.00 USD | 41,230.00 USD | 0.00 USD | `+96.28%` | `9.01` |
| `Live` | `Short` | `4585.00` | 1,690,000,000.00 USD | 1,160,000.00 USD | 0.00 USD | `+96.71%` | `252.89` |
| `Live` | `Short` | `4595.00` | 1,690,000,000.00 USD | 187,730.00 USD | 0.00 USD | `+97.14%` | `40.86` |
| `Live` | `Short` | `4605.00` | 1,690,000,000.00 USD | 37,010.00 USD | 0.00 USD | `+97.57%` | `8.04` |
| `Live` | `Short` | `4615.00` | 1,690,000,000.00 USD | 100,540.00 USD | 0.00 USD | `+98.00%` | `21.79` |
| `Live` | `Short` | `4625.00` | 1,690,000,000.00 USD | 412,820.00 USD | 0.00 USD | `+98.43%` | `89.26` |
| `Live` | `Short` | `4635.00` | 1,690,000,000.00 USD | 236,720.00 USD | 0.00 USD | `+98.86%` | `51.07` |
| `Live` | `Short` | `4645.00` | 1,690,000,000.00 USD | 170,520.00 USD | 0.00 USD | `+99.29%` | `36.71` |
| `Live` | `Short` | `4655.00` | 1,690,000,000.00 USD | 445,590.00 USD | 0.00 USD | `+99.72%` | `95.72` |
| `Live` | `Short` | `4665.00` | 1,690,000,000.00 USD | 29,990.00 USD | 0.00 USD | `+100.15%` | `6.43` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `505.00` | 1,500,000,000.00 USD | 0.00 USD | 16,750.00 USD | `-78.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.00` | 1,500,000,000.00 USD | 0.00 USD | 563.16 USD | `-76.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.00` | 1,500,000,000.00 USD | 0.00 USD | 885.90 USD | `-69.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `755.00` | 1,500,000,000.00 USD | 0.00 USD | 177.27 USD | `-67.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `795.00` | 1,500,000,000.00 USD | 0.00 USD | 104.22 USD | `-65.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `805.00` | 1,500,000,000.00 USD | 0.00 USD | 2,090.00 USD | `-65.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `835.00` | 1,500,000,000.00 USD | 0.00 USD | 1,670.00 USD | `-64.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `865.00` | 1,500,000,000.00 USD | 0.00 USD | 139,280.00 USD | `-62.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `885.00` | 1,500,000,000.00 USD | 0.00 USD | 3,130.00 USD | `-62.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `905.00` | 1,500,000,000.00 USD | 0.00 USD | 2,780.00 USD | `-61.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `985.00` | 1,500,000,000.00 USD | 0.00 USD | 516.34 USD | `-57.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `995.00` | 1,500,000,000.00 USD | 0.00 USD | 100.50 USD | `-57.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1005.00` | 1,500,000,000.00 USD | 0.00 USD | 222,040.00 USD | `-56.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1025.00` | 1,500,000,000.00 USD | 0.00 USD | 112.03 USD | `-56.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1065.00` | 1,500,000,000.00 USD | 0.00 USD | 1,060.00 USD | `-54.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1075.00` | 1,500,000,000.00 USD | 0.00 USD | 995.34 USD | `-53.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1105.00` | 1,500,000,000.00 USD | 0.00 USD | 1,610.00 USD | `-52.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1115.00` | 1,500,000,000.00 USD | 0.00 USD | 11,050.00 USD | `-52.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1125.00` | 1,500,000,000.00 USD | 0.00 USD | 1,320.00 USD | `-51.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1155.00` | 1,500,000,000.00 USD | 0.00 USD | 1,000.00 USD | `-50.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1175.00` | 1,500,000,000.00 USD | 0.00 USD | 203.98 USD | `-49.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1185.00` | 1,500,000,000.00 USD | 0.00 USD | 228.47 USD | `-49.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1205.00` | 1,500,000,000.00 USD | 0.00 USD | 3,110.00 USD | `-48.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1225.00` | 1,500,000,000.00 USD | 0.00 USD | 995.93 USD | `-47.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1245.00` | 1,500,000,000.00 USD | 0.00 USD | 951.93 USD | `-46.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1255.00` | 1,500,000,000.00 USD | 0.00 USD | 6,810.00 USD | `-46.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1285.00` | 1,500,000,000.00 USD | 0.00 USD | 9,050.00 USD | `-44.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1295.00` | 1,500,000,000.00 USD | 0.00 USD | 7,030.00 USD | `-44.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1305.00` | 1,500,000,000.00 USD | 0.00 USD | 23,030.00 USD | `-44.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1315.00` | 1,500,000,000.00 USD | 0.00 USD | 1,440.00 USD | `-43.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1345.00` | 1,500,000,000.00 USD | 0.00 USD | 141,950.00 USD | `-42.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1355.00` | 1,500,000,000.00 USD | 0.00 USD | 128.86 USD | `-41.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1375.00` | 1,500,000,000.00 USD | 0.00 USD | 4,160.00 USD | `-41.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1395.00` | 1,500,000,000.00 USD | 0.00 USD | 535,600.00 USD | `-40.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1405.00` | 1,500,000,000.00 USD | 0.00 USD | 20,270.00 USD | `-39.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1425.00` | 1,500,000,000.00 USD | 0.00 USD | 6,450.00 USD | `-38.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1435.00` | 1,500,000,000.00 USD | 0.00 USD | 852.10 USD | `-38.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1445.00` | 1,500,000,000.00 USD | 0.00 USD | 1,490.00 USD | `-38.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1455.00` | 1,500,000,000.00 USD | 0.00 USD | 5,680.00 USD | `-37.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1465.00` | 1,500,000,000.00 USD | 0.00 USD | 19,350.00 USD | `-37.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1475.00` | 1,500,000,000.00 USD | 0.00 USD | 2,600.00 USD | `-36.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1485.00` | 1,500,000,000.00 USD | 0.00 USD | 18,710.00 USD | `-36.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1495.00` | 1,500,000,000.00 USD | 0.00 USD | 11,460.00 USD | `-35.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1505.00` | 1,500,000,000.00 USD | 0.00 USD | 78,910.00 USD | `-35.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1515.00` | 1,500,000,000.00 USD | 0.00 USD | 11,140.00 USD | `-35.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1525.00` | 1,500,000,000.00 USD | 0.00 USD | 32,310.00 USD | `-34.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1535.00` | 1,500,000,000.00 USD | 0.00 USD | 983.78 USD | `-34.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1545.00` | 1,500,000,000.00 USD | 0.00 USD | 17,470.00 USD | `-33.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1555.00` | 1,500,000,000.00 USD | 0.00 USD | 4,210.00 USD | `-33.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1565.00` | 1,500,000,000.00 USD | 0.00 USD | 6,260.00 USD | `-32.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1575.00` | 1,500,000,000.00 USD | 0.00 USD | 190,890.00 USD | `-32.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1585.00` | 1,500,000,000.00 USD | 0.00 USD | 3,390.00 USD | `-32.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1595.00` | 1,500,000,000.00 USD | 0.00 USD | 4,040.00 USD | `-31.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1605.00` | 1,500,000,000.00 USD | 0.00 USD | 435,900.00 USD | `-31.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1615.00` | 1,500,000,000.00 USD | 0.00 USD | 25,840.00 USD | `-30.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1625.00` | 1,500,000,000.00 USD | 0.00 USD | 13,590.00 USD | `-30.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1635.00` | 1,500,000,000.00 USD | 0.00 USD | 5,510.00 USD | `-29.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1645.00` | 1,500,000,000.00 USD | 0.00 USD | 328,140.00 USD | `-29.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1655.00` | 1,500,000,000.00 USD | 0.00 USD | 22,220.00 USD | `-28.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1665.00` | 1,500,000,000.00 USD | 0.00 USD | 3,110.00 USD | `-28.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1675.00` | 1,500,000,000.00 USD | 0.00 USD | 3,440.00 USD | `-28.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1685.00` | 1,500,000,000.00 USD | 0.00 USD | 58,890.00 USD | `-27.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1695.00` | 1,500,000,000.00 USD | 0.00 USD | 6,800.00 USD | `-27.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1705.00` | 1,500,000,000.00 USD | 0.00 USD | 81,190.00 USD | `-26.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1715.00` | 1,500,000,000.00 USD | 0.00 USD | 28,180.00 USD | `-26.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1725.00` | 1,500,000,000.00 USD | 0.00 USD | 47,500.00 USD | `-25.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1735.00` | 1,500,000,000.00 USD | 0.00 USD | 28,150.00 USD | `-25.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1745.00` | 1,500,000,000.00 USD | 0.00 USD | 3,180.00 USD | `-25.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1755.00` | 1,500,000,000.00 USD | 0.00 USD | 498,170.00 USD | `-24.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1765.00` | 1,500,000,000.00 USD | 0.00 USD | 75,630.00 USD | `-24.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1775.00` | 1,500,000,000.00 USD | 0.00 USD | 3,090.00 USD | `-23.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1785.00` | 1,500,000,000.00 USD | 0.00 USD | 4,930.00 USD | `-23.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1795.00` | 1,500,000,000.00 USD | 0.00 USD | 184,330.00 USD | `-22.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1805.00` | 1,500,000,000.00 USD | 0.00 USD | 283,470.00 USD | `-22.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1815.00` | 1,500,000,000.00 USD | 0.00 USD | 114,830.00 USD | `-22.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1825.00` | 1,500,000,000.00 USD | 0.00 USD | 26,680.00 USD | `-21.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1835.00` | 1,500,000,000.00 USD | 0.00 USD | 2,390.00 USD | `-21.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1845.00` | 1,500,000,000.00 USD | 0.00 USD | 9,040.00 USD | `-20.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1855.00` | 1,500,000,000.00 USD | 0.00 USD | 467,010.00 USD | `-20.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1865.00` | 1,500,000,000.00 USD | 0.00 USD | 32,910.00 USD | `-19.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1875.00` | 1,500,000,000.00 USD | 0.00 USD | 18,210,000.00 USD | `-19.56%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1885.00` | 1,480,000,000.00 USD | 0.00 USD | 2,390.00 USD | `-19.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1895.00` | 1,480,000,000.00 USD | 0.00 USD | 61,700.00 USD | `-18.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1905.00` | 1,480,000,000.00 USD | 0.00 USD | 162,190.00 USD | `-18.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1915.00` | 1,480,000,000.00 USD | 0.00 USD | 8,110,000.00 USD | `-17.84%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1925.00` | 1,470,000,000.00 USD | 0.00 USD | 16,410,000.00 USD | `-17.41%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1935.00` | 1,450,000,000.00 USD | 0.00 USD | 79,950.00 USD | `-16.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1945.00` | 1,450,000,000.00 USD | 0.00 USD | 44,850.00 USD | `-16.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1955.00` | 1,450,000,000.00 USD | 0.00 USD | 54,180.00 USD | `-16.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1965.00` | 1,450,000,000.00 USD | 0.00 USD | 510.51 USD | `-15.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1975.00` | 1,450,000,000.00 USD | 0.00 USD | 78,230.00 USD | `-15.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1985.00` | 1,450,000,000.00 USD | 0.00 USD | 98,040.00 USD | `-14.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1995.00` | 1,450,000,000.00 USD | 0.00 USD | 104,260.00 USD | `-14.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2005.00` | 1,450,000,000.00 USD | 0.00 USD | 1,360,000.00 USD | `-13.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2015.00` | 1,450,000,000.00 USD | 0.00 USD | 69,270.00 USD | `-13.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2025.00` | 1,450,000,000.00 USD | 0.00 USD | 5,040.00 USD | `-13.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2035.00` | 1,450,000,000.00 USD | 0.00 USD | 103,890.00 USD | `-12.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2045.00` | 1,450,000,000.00 USD | 0.00 USD | 15,220.00 USD | `-12.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2055.00` | 1,450,000,000.00 USD | 0.00 USD | 212,720.00 USD | `-11.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2065.00` | 1,450,000,000.00 USD | 0.00 USD | 91,330.00 USD | `-11.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2075.00` | 1,450,000,000.00 USD | 0.00 USD | 32,400.00 USD | `-10.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2085.00` | 1,450,000,000.00 USD | 0.00 USD | 52,030.00 USD | `-10.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2095.00` | 1,450,000,000.00 USD | 0.00 USD | 29,710.00 USD | `-10.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2105.00` | 1,450,000,000.00 USD | 0.00 USD | 351,510.00 USD | `-9.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2115.00` | 1,450,000,000.00 USD | 0.00 USD | 123,820.00 USD | `-9.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2125.00` | 1,450,000,000.00 USD | 0.00 USD | 81,460.00 USD | `-8.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2135.00` | 1,450,000,000.00 USD | 0.00 USD | 19,470.00 USD | `-8.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2145.00` | 1,450,000,000.00 USD | 0.00 USD | 217,830.00 USD | `-7.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2155.00` | 1,450,000,000.00 USD | 0.00 USD | 100,400.00 USD | `-7.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2165.00` | 1,450,000,000.00 USD | 0.00 USD | 902,640.00 USD | `-7.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2175.00` | 1,450,000,000.00 USD | 0.00 USD | 1,360,000.00 USD | `-6.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2185.00` | 1,450,000,000.00 USD | 0.00 USD | 92,000.00 USD | `-6.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2195.00` | 1,450,000,000.00 USD | 0.00 USD | 438,560.00 USD | `-5.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2205.00` | 1,450,000,000.00 USD | 0.00 USD | 2,270,000.00 USD | `-5.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2215.00` | 1,440,000,000.00 USD | 0.00 USD | 1,020,000.00 USD | `-4.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2225.00` | 1,440,000,000.00 USD | 0.00 USD | 1,010,000.00 USD | `-4.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2235.00` | 1,440,000,000.00 USD | 0.00 USD | 127,280.00 USD | `-4.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2245.00` | 1,440,000,000.00 USD | 0.00 USD | 1,450,000.00 USD | `-3.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2255.00` | 1,440,000,000.00 USD | 0.00 USD | 23,300,000.00 USD | `-3.25%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2265.00` | 1,420,000,000.00 USD | 0.00 USD | 521,190.00 USD | `-2.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2275.00` | 1,420,000,000.00 USD | 0.00 USD | 4,690,000.00 USD | `-2.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2285.00` | 1,410,000,000.00 USD | 0.00 USD | 4,210,000.00 USD | `-1.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2295.00` | 1,410,000,000.00 USD | 0.00 USD | 11,280,000.00 USD | `-1.54%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2305.00` | 1,400,000,000.00 USD | 0.00 USD | 1,380,000,000.00 USD | `-1.11%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2315.00` | 12,740,000.00 USD | 0.00 USD | 11,590,000.00 USD | `-0.68%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2325.00` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | `-0.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2335.00` | 302,810.00 USD | 302,810.00 USD | 0.00 USD | `+0.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2345.00` | 891,470.00 USD | 588,660.00 USD | 0.00 USD | `+0.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2355.00` | 3,480,000.00 USD | 2,580,000.00 USD | 0.00 USD | `+1.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2365.00` | 3,810,000.00 USD | 339,140.00 USD | 0.00 USD | `+1.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2375.00` | 3,950,000.00 USD | 133,560.00 USD | 0.00 USD | `+1.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2385.00` | 5,680,000.00 USD | 1,740,000.00 USD | 0.00 USD | `+2.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2395.00` | 7,240,000.00 USD | 1,560,000.00 USD | 0.00 USD | `+2.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2405.00` | 9,590,000.00 USD | 2,350,000.00 USD | 0.00 USD | `+3.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2415.00` | 10,120,000.00 USD | 535,610.00 USD | 0.00 USD | `+3.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2425.00` | 13,600,000.00 USD | 3,470,000.00 USD | 0.00 USD | `+4.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2435.00` | 13,930,000.00 USD | 333,010.00 USD | 0.00 USD | `+4.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2445.00` | 24,480,000.00 USD | 10,550,000.00 USD | 0.00 USD | `+4.90%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2455.00` | 24,700,000.00 USD | 226,060.00 USD | 0.00 USD | `+5.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2465.00` | 26,880,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+5.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2475.00` | 27,220,000.00 USD | 344,170.00 USD | 0.00 USD | `+6.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2485.00` | 29,380,000.00 USD | 2,160,000.00 USD | 0.00 USD | `+6.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2495.00` | 29,820,000.00 USD | 440,780.00 USD | 0.00 USD | `+7.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2505.00` | 35,200,000.00 USD | 5,380,000.00 USD | 0.00 USD | `+7.47%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2515.00` | 42,980,000.00 USD | 7,780,000.00 USD | 0.00 USD | `+7.90%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2525.00` | 46,230,000.00 USD | 3,260,000.00 USD | 0.00 USD | `+8.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2535.00` | 46,300,000.00 USD | 72,380.00 USD | 0.00 USD | `+8.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2545.00` | 48,460,000.00 USD | 2,160,000.00 USD | 0.00 USD | `+9.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2555.00` | 48,800,000.00 USD | 333,630.00 USD | 0.00 USD | `+9.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2565.00` | 51,130,000.00 USD | 2,330,000.00 USD | 0.00 USD | `+10.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2575.00` | 51,290,000.00 USD | 159,570.00 USD | 0.00 USD | `+10.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2585.00` | 53,740,000.00 USD | 2,450,000.00 USD | 0.00 USD | `+10.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2595.00` | 53,760,000.00 USD | 14,580.00 USD | 0.00 USD | `+11.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2605.00` | 56,850,000.00 USD | 3,100,000.00 USD | 0.00 USD | `+11.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2615.00` | 57,030,000.00 USD | 177,120.00 USD | 0.00 USD | `+12.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2625.00` | 59,220,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+12.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2635.00` | 59,510,000.00 USD | 292,470.00 USD | 0.00 USD | `+13.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2645.00` | 61,680,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+13.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2655.00` | 61,930,000.00 USD | 251,320.00 USD | 0.00 USD | `+13.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2665.00` | 64,090,000.00 USD | 2,160,000.00 USD | 0.00 USD | `+14.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2675.00` | 64,480,000.00 USD | 393,350.00 USD | 0.00 USD | `+14.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2685.00` | 66,670,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+15.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2695.00` | 66,840,000.00 USD | 172,910.00 USD | 0.00 USD | `+15.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2705.00` | 71,510,000.00 USD | 4,670,000.00 USD | 0.00 USD | `+16.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2715.00` | 71,590,000.00 USD | 76,900.00 USD | 0.00 USD | `+16.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2725.00` | 74,060,000.00 USD | 2,470,000.00 USD | 0.00 USD | `+16.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2735.00` | 74,110,000.00 USD | 55,280.00 USD | 0.00 USD | `+17.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2745.00` | 76,410,000.00 USD | 2,300,000.00 USD | 0.00 USD | `+17.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2755.00` | 77,100,000.00 USD | 687,450.00 USD | 0.00 USD | `+18.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2765.00` | 79,480,000.00 USD | 2,380,000.00 USD | 0.00 USD | `+18.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2775.00` | 80,100,000.00 USD | 620,300.00 USD | 0.00 USD | `+19.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2785.00` | 82,400,000.00 USD | 2,290,000.00 USD | 0.00 USD | `+19.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2795.00` | 82,440,000.00 USD | 36,990.00 USD | 0.00 USD | `+19.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2805.00` | 86,420,000.00 USD | 3,990,000.00 USD | 0.00 USD | `+20.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2815.00` | 86,480,000.00 USD | 53,260.00 USD | 0.00 USD | `+20.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2825.00` | 86,540,000.00 USD | 62,020.00 USD | 0.00 USD | `+21.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2835.00` | 86,830,000.00 USD | 289,110.00 USD | 0.00 USD | `+21.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2845.00` | 87,840,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+22.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2855.00` | 89,120,000.00 USD | 1,280,000.00 USD | 0.00 USD | `+22.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2865.00` | 89,130,000.00 USD | 10,290.00 USD | 0.00 USD | `+22.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2875.00` | 89,130,000.00 USD | 3,630.00 USD | 0.00 USD | `+23.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2885.00` | 89,430,000.00 USD | 292,580.00 USD | 0.00 USD | `+23.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2895.00` | 89,450,000.00 USD | 23,020.00 USD | 0.00 USD | `+24.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2905.00` | 90,990,000.00 USD | 1,540,000.00 USD | 0.00 USD | `+24.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2915.00` | 91,000,000.00 USD | 10,340.00 USD | 0.00 USD | `+25.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2925.00` | 91,000,000.00 USD | 3,040.00 USD | 0.00 USD | `+25.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2935.00` | 91,060,000.00 USD | 54,540.00 USD | 0.00 USD | `+25.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2945.00` | 91,090,000.00 USD | 34,650.00 USD | 0.00 USD | `+26.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2955.00` | 91,170,000.00 USD | 74,770.00 USD | 0.00 USD | `+26.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2965.00` | 91,280,000.00 USD | 111,790.00 USD | 0.00 USD | `+27.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2975.00` | 91,430,000.00 USD | 148,070.00 USD | 0.00 USD | `+27.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2985.00` | 95,510,000.00 USD | 4,090,000.00 USD | 0.00 USD | `+28.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2995.00` | 97,430,000.00 USD | 1,920,000.00 USD | 0.00 USD | `+28.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3005.00` | 99,420,000.00 USD | 1,990,000.00 USD | 0.00 USD | `+28.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3015.00` | 99,430,000.00 USD | 6,950.00 USD | 0.00 USD | `+29.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3025.00` | 99,470,000.00 USD | 37,410.00 USD | 0.00 USD | `+29.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3035.00` | 99,540,000.00 USD | 70,360.00 USD | 0.00 USD | `+30.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3045.00` | 99,560,000.00 USD | 22,460.00 USD | 0.00 USD | `+30.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3055.00` | 100,350,000.00 USD | 786,100.00 USD | 0.00 USD | `+31.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3065.00` | 100,350,000.00 USD | 3,360.00 USD | 0.00 USD | `+31.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3075.00` | 100,400,000.00 USD | 50,370.00 USD | 0.00 USD | `+31.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3085.00` | 100,420,000.00 USD | 19,860.00 USD | 0.00 USD | `+32.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3095.00` | 100,420,000.00 USD | 928.50 USD | 0.00 USD | `+32.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3105.00` | 113,830,000.00 USD | 13,410,000.00 USD | 0.00 USD | `+33.22%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `3115.00` | 113,950,000.00 USD | 118,040.00 USD | 0.00 USD | `+33.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3125.00` | 114,320,000.00 USD | 367,790.00 USD | 0.00 USD | `+34.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3145.00` | 114,320,000.00 USD | 1,860.00 USD | 0.00 USD | `+34.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3155.00` | 114,390,000.00 USD | 68,940.00 USD | 0.00 USD | `+35.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3165.00` | 114,400,000.00 USD | 9,860.00 USD | 0.00 USD | `+35.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3175.00` | 114,410,000.00 USD | 16,410.00 USD | 0.00 USD | `+36.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3185.00` | 114,420,000.00 USD | 1,980.00 USD | 0.00 USD | `+36.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3195.00` | 114,450,000.00 USD | 29,580.00 USD | 0.00 USD | `+37.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3205.00` | 115,360,000.00 USD | 910,780.00 USD | 0.00 USD | `+37.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3215.00` | 115,360,000.00 USD | 1,290.00 USD | 0.00 USD | `+37.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3225.00` | 115,360,000.00 USD | 3,740.00 USD | 0.00 USD | `+38.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3235.00` | 115,390,000.00 USD | 30,790.00 USD | 0.00 USD | `+38.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3245.00` | 115,450,000.00 USD | 56,110.00 USD | 0.00 USD | `+39.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3255.00` | 115,650,000.00 USD | 204,030.00 USD | 0.00 USD | `+39.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3265.00` | 115,670,000.00 USD | 15,710.00 USD | 0.00 USD | `+40.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3275.00` | 115,670,000.00 USD | 1,630.00 USD | 0.00 USD | `+40.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3285.00` | 115,810,000.00 USD | 141,980.00 USD | 0.00 USD | `+40.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3295.00` | 115,830,000.00 USD | 16,780.00 USD | 0.00 USD | `+41.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3305.00` | 117,100,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+41.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3315.00` | 117,480,000.00 USD | 385,510.00 USD | 0.00 USD | `+42.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3325.00` | 117,500,000.00 USD | 18,270.00 USD | 0.00 USD | `+42.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3335.00` | 117,520,000.00 USD | 14,190.00 USD | 0.00 USD | `+43.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3345.00` | 117,520,000.00 USD | 617.15 USD | 0.00 USD | `+43.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3355.00` | 117,520,000.00 USD | 334.49 USD | 0.00 USD | `+43.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3365.00` | 117,520,000.00 USD | 597.29 USD | 0.00 USD | `+44.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3375.00` | 117,540,000.00 USD | 23,460.00 USD | 0.00 USD | `+44.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3385.00` | 117,600,000.00 USD | 58,010.00 USD | 0.00 USD | `+45.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3395.00` | 117,950,000.00 USD | 355,050.00 USD | 0.00 USD | `+45.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3405.00` | 119,560,000.00 USD | 1,600,000.00 USD | 0.00 USD | `+46.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3415.00` | 119,560,000.00 USD | 3,510.00 USD | 0.00 USD | `+46.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3425.00` | 119,580,000.00 USD | 16,310.00 USD | 0.00 USD | `+46.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3445.00` | 119,590,000.00 USD | 15,030.00 USD | 0.00 USD | `+47.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3455.00` | 119,610,000.00 USD | 18,600.00 USD | 0.00 USD | `+48.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3465.00` | 119,920,000.00 USD | 311,800.00 USD | 0.00 USD | `+48.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3475.00` | 119,930,000.00 USD | 2,980.00 USD | 0.00 USD | `+49.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3485.00` | 119,970,000.00 USD | 43,610.00 USD | 0.00 USD | `+49.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3495.00` | 119,970,000.00 USD | 158.32 USD | 0.00 USD | `+49.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3505.00` | 120,520,000.00 USD | 550,300.00 USD | 0.00 USD | `+50.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3515.00` | 120,560,000.00 USD | 43,200.00 USD | 0.00 USD | `+50.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3525.00` | 120,570,000.00 USD | 3,690.00 USD | 0.00 USD | `+51.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3535.00` | 120,580,000.00 USD | 9,810.00 USD | 0.00 USD | `+51.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3545.00` | 120,580,000.00 USD | 179.38 USD | 0.00 USD | `+52.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3555.00` | 120,670,000.00 USD | 90,810.00 USD | 0.00 USD | `+52.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3565.00` | 120,670,000.00 USD | 2,300.00 USD | 0.00 USD | `+52.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3585.00` | 120,670,000.00 USD | 354.92 USD | 0.00 USD | `+53.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3595.00` | 120,680,000.00 USD | 13,160.00 USD | 0.00 USD | `+54.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3605.00` | 120,790,000.00 USD | 105,860.00 USD | 0.00 USD | `+54.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3625.00` | 120,800,000.00 USD | 10,210.00 USD | 0.00 USD | `+55.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3635.00` | 120,810,000.00 USD | 7,790.00 USD | 0.00 USD | `+55.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3645.00` | 120,810,000.00 USD | 3,860.00 USD | 0.00 USD | `+56.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3655.00` | 120,820,000.00 USD | 7,740.00 USD | 0.00 USD | `+56.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3665.00` | 120,830,000.00 USD | 8,130.00 USD | 0.00 USD | `+57.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3675.00` | 120,880,000.00 USD | 55,120.00 USD | 0.00 USD | `+57.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3685.00` | 120,890,000.00 USD | 3,550.00 USD | 0.00 USD | `+58.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3705.00` | 120,890,000.00 USD | 819.92 USD | 0.00 USD | `+58.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3715.00` | 120,890,000.00 USD | 323.58 USD | 0.00 USD | `+59.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3725.00` | 120,890,000.00 USD | 1,400.00 USD | 0.00 USD | `+59.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3735.00` | 120,890,000.00 USD | 6,490.00 USD | 0.00 USD | `+60.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3755.00` | 120,900,000.00 USD | 751.00 USD | 0.00 USD | `+61.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3785.00` | 120,900,000.00 USD | 286.90 USD | 0.00 USD | `+62.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3795.00` | 120,900,000.00 USD | 1,560.00 USD | 0.00 USD | `+62.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3805.00` | 121,630,000.00 USD | 734,090.00 USD | 0.00 USD | `+63.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3815.00` | 121,650,000.00 USD | 20,930.00 USD | 0.00 USD | `+63.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3825.00` | 121,660,000.00 USD | 8,380.00 USD | 0.00 USD | `+64.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3835.00` | 121,660,000.00 USD | 711.78 USD | 0.00 USD | `+64.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3845.00` | 121,660,000.00 USD | 932.03 USD | 0.00 USD | `+64.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3855.00` | 121,870,000.00 USD | 203,880.00 USD | 0.00 USD | `+65.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3875.00` | 121,910,000.00 USD | 41,200.00 USD | 0.00 USD | `+66.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3885.00` | 121,930,000.00 USD | 21,210.00 USD | 0.00 USD | `+66.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3905.00` | 122,110,000.00 USD | 180,010.00 USD | 0.00 USD | `+67.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3915.00` | 122,760,000.00 USD | 646,840.00 USD | 0.00 USD | `+67.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3925.00` | 122,760,000.00 USD | 3,260.00 USD | 0.00 USD | `+68.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3935.00` | 122,800,000.00 USD | 42,570.00 USD | 0.00 USD | `+68.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3945.00` | 122,820,000.00 USD | 19,730.00 USD | 0.00 USD | `+69.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3955.00` | 122,820,000.00 USD | 1,380.00 USD | 0.00 USD | `+69.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3965.00` | 122,820,000.00 USD | 323.54 USD | 0.00 USD | `+70.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3975.00` | 122,830,000.00 USD | 6,960.00 USD | 0.00 USD | `+70.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3985.00` | 122,840,000.00 USD | 14,610.00 USD | 0.00 USD | `+70.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3995.00` | 122,850,000.00 USD | 4,280.00 USD | 0.00 USD | `+71.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4005.00` | 125,520,000.00 USD | 2,670,000.00 USD | 0.00 USD | `+71.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4035.00` | 125,520,000.00 USD | 898.59 USD | 0.00 USD | `+73.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4055.00` | 125,520,000.00 USD | 811.00 USD | 0.00 USD | `+73.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4075.00` | 125,520,000.00 USD | 4,310.00 USD | 0.00 USD | `+74.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4085.00` | 125,530,000.00 USD | 2,800.00 USD | 0.00 USD | `+75.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4095.00` | 125,530,000.00 USD | 2,750.00 USD | 0.00 USD | `+75.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4105.00` | 125,580,000.00 USD | 48,190.00 USD | 0.00 USD | `+76.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4115.00` | 125,580,000.00 USD | 5,990.00 USD | 0.00 USD | `+76.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4125.00` | 125,580,000.00 USD | 372.90 USD | 0.00 USD | `+76.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4145.00` | 125,580,000.00 USD | 395.43 USD | 0.00 USD | `+77.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4175.00` | 125,590,000.00 USD | 2,890.00 USD | 0.00 USD | `+79.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4185.00` | 125,590,000.00 USD | 376.65 USD | 0.00 USD | `+79.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4205.00` | 125,620,000.00 USD | 28,760.00 USD | 0.00 USD | `+80.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4215.00` | 125,620,000.00 USD | 460.70 USD | 0.00 USD | `+80.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4225.00` | 125,620,000.00 USD | 1,270.00 USD | 0.00 USD | `+81.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4255.00` | 125,620,000.00 USD | 4,300.00 USD | 0.00 USD | `+82.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4265.00` | 125,630,000.00 USD | 4,010.00 USD | 0.00 USD | `+82.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4275.00` | 125,690,000.00 USD | 64,550.00 USD | 0.00 USD | `+83.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4285.00` | 125,690,000.00 USD | 1,610.00 USD | 0.00 USD | `+83.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4305.00` | 125,790,000.00 USD | 97,670.00 USD | 0.00 USD | `+84.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4315.00` | 125,790,000.00 USD | 1,070.00 USD | 0.00 USD | `+85.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4345.00` | 125,800,000.00 USD | 11,270.00 USD | 0.00 USD | `+86.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4355.00` | 125,800,000.00 USD | 3,250.00 USD | 0.00 USD | `+86.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4375.00` | 125,850,000.00 USD | 43,750.00 USD | 0.00 USD | `+87.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4385.00` | 125,910,000.00 USD | 64,570.00 USD | 0.00 USD | `+88.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4395.00` | 125,910,000.00 USD | 1,050.00 USD | 0.00 USD | `+88.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4405.00` | 125,960,000.00 USD | 44,640.00 USD | 0.00 USD | `+88.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4415.00` | 125,970,000.00 USD | 11,480.00 USD | 0.00 USD | `+89.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4425.00` | 125,970,000.00 USD | 2,510.00 USD | 0.00 USD | `+89.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4435.00` | 126,150,000.00 USD | 177,400.00 USD | 0.00 USD | `+90.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4455.00` | 126,150,000.00 USD | 641.97 USD | 0.00 USD | `+91.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4465.00` | 126,150,000.00 USD | 1,030.00 USD | 0.00 USD | `+91.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4505.00` | 126,500,000.00 USD | 343,680.00 USD | 0.00 USD | `+93.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4515.00` | 126,500,000.00 USD | 2,280.00 USD | 0.00 USD | `+93.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4525.00` | 126,500,000.00 USD | 6,560.00 USD | 0.00 USD | `+94.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4565.00` | 126,600,000.00 USD | 97,750.00 USD | 0.00 USD | `+95.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4585.00` | 126,600,000.00 USD | 1,420.00 USD | 0.00 USD | `+96.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4595.00` | 126,610,000.00 USD | 2,610.00 USD | 0.00 USD | `+97.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4605.00` | 126,670,000.00 USD | 64,120.00 USD | 0.00 USD | `+97.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4645.00` | 126,700,000.00 USD | 27,410.00 USD | 0.00 USD | `+99.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4655.00` | 126,870,000.00 USD | 174,790.00 USD | 0.00 USD | `+99.72%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `2077.20` | 2,540,000,000.00 USD | 0.00 USD | 2,540,000,000.00 USD | 4,860,000.00 USD | 4,190,000.00 USD | 2,130,000.00 USD |
| `7D` | `2080.00` | 2,530,000,000.00 USD | 0.00 USD | 2,530,000,000.00 USD | 3,400,000.00 USD | 3,020,000.00 USD | 2,510,000.00 USD |
| `7D` | `2082.80` | 2,520,000,000.00 USD | 0.00 USD | 2,520,000,000.00 USD | 2,420,000.00 USD | 1,860,000.00 USD | 1,910,000.00 USD |
| `7D` | `2085.60` | 2,520,000,000.00 USD | 0.00 USD | 2,520,000,000.00 USD | 3,840,000.00 USD | 2,320,000.00 USD | 3,140,000.00 USD |
| `7D` | `2088.40` | 2,510,000,000.00 USD | 0.00 USD | 2,510,000,000.00 USD | 2,280,000.00 USD | 1,370,000.00 USD | 893,940.00 USD |
| `1D` | `2090.50` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 1,170,000.00 USD | 270,920.00 USD | 293,620.00 USD |
| `7D` | `2091.20` | 2,500,000,000.00 USD | 0.00 USD | 2,500,000,000.00 USD | 4,280,000.00 USD | 952,210.00 USD | 6,980,000.00 USD |
| `1D` | `2093.00` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 775,500.00 USD | 518,220.00 USD | 846,960.00 USD |
| `7D` | `2094.00` | 2,490,000,000.00 USD | 0.00 USD | 2,490,000,000.00 USD | 5,200,000.00 USD | 1,660,000.00 USD | 2,340,000.00 USD |
| `1D` | `2095.50` | 1,080,000,000.00 USD | 0.00 USD | 1,080,000,000.00 USD | 1,840,000.00 USD | 1,290,000.00 USD | 1,800,000.00 USD |
| `7D` | `2096.80` | 2,480,000,000.00 USD | 0.00 USD | 2,480,000,000.00 USD | 1,940,000.00 USD | 3,320,000.00 USD | 1,290,000.00 USD |
| `1D` | `2098.00` | 1,080,000,000.00 USD | 0.00 USD | 1,080,000,000.00 USD | 463,350.00 USD | 975,880.00 USD | 309,770.00 USD |
| `7D` | `2099.60` | 2,470,000,000.00 USD | 0.00 USD | 2,470,000,000.00 USD | 1,880,000.00 USD | 1,920,000.00 USD | 3,000,000.00 USD |
| `1D` | `2100.50` | 1,080,000,000.00 USD | 0.00 USD | 1,080,000,000.00 USD | 160,570.00 USD | 44,780.00 USD | 175,760.00 USD |
| `7D` | `2102.40` | 2,470,000,000.00 USD | 0.00 USD | 2,470,000,000.00 USD | 125,250.00 USD | 341,900.00 USD | 1,480,000.00 USD |
| `1D` | `2103.00` | 1,080,000,000.00 USD | 0.00 USD | 1,080,000,000.00 USD | 433,430.00 USD | 289,160.00 USD | 306,410.00 USD |
| `7D` | `2105.20` | 2,470,000,000.00 USD | 0.00 USD | 2,470,000,000.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,800,000.00 USD |
| `1D` | `2105.50` | 1,080,000,000.00 USD | 0.00 USD | 1,080,000,000.00 USD | 521,320.00 USD | 400,040.00 USD | 168,530.00 USD |
| `1D` | `2108.00` | 1,070,000,000.00 USD | 0.00 USD | 1,070,000,000.00 USD | 664,310.00 USD | 0.00 USD | 347,020.00 USD |
| `7D` | `2108.00` | 2,460,000,000.00 USD | 0.00 USD | 2,460,000,000.00 USD | 2,400,000.00 USD | 930,280.00 USD | 1,640,000.00 USD |
| `1D` | `2110.50` | 1,070,000,000.00 USD | 0.00 USD | 1,070,000,000.00 USD | 36,110.00 USD | 31,550.00 USD | 196,840.00 USD |
| `7D` | `2110.80` | 2,460,000,000.00 USD | 0.00 USD | 2,460,000,000.00 USD | 2,750,000.00 USD | 1,780,000.00 USD | 2,160,000.00 USD |
| `1D` | `2113.00` | 1,070,000,000.00 USD | 0.00 USD | 1,070,000,000.00 USD | 875,700.00 USD | 643,210.00 USD | 234,280.00 USD |
| `7D` | `2113.60` | 2,450,000,000.00 USD | 0.00 USD | 2,450,000,000.00 USD | 1,780,000.00 USD | 1,280,000.00 USD | 2,730,000.00 USD |
| `1D` | `2115.50` | 1,070,000,000.00 USD | 0.00 USD | 1,070,000,000.00 USD | 0.00 USD | 13,230.00 USD | 431,790.00 USD |
| `7D` | `2116.40` | 2,440,000,000.00 USD | 0.00 USD | 2,440,000,000.00 USD | 1,900,000.00 USD | 2,210,000.00 USD | 2,570,000.00 USD |
| `1D` | `2118.00` | 1,070,000,000.00 USD | 0.00 USD | 1,070,000,000.00 USD | 679,710.00 USD | 16,610.00 USD | 819,800.00 USD |
| `7D` | `2119.20` | 2,440,000,000.00 USD | 0.00 USD | 2,440,000,000.00 USD | 2,920,000.00 USD | 750,810.00 USD | 2,590,000.00 USD |
| `1D` | `2120.50` | 1,070,000,000.00 USD | 0.00 USD | 1,070,000,000.00 USD | 744,340.00 USD | 416,510.00 USD | 1,100,000.00 USD |
| `7D` | `2122.00` | 2,430,000,000.00 USD | 0.00 USD | 2,430,000,000.00 USD | 2,300,000.00 USD | 1,020,000.00 USD | 1,630,000.00 USD |
| `1D` | `2123.00` | 1,070,000,000.00 USD | 0.00 USD | 1,070,000,000.00 USD | 1,030,000.00 USD | 693,780.00 USD | 1,050,000.00 USD |
| `7D` | `2124.80` | 2,420,000,000.00 USD | 0.00 USD | 2,420,000,000.00 USD | 2,680,000.00 USD | 939,650.00 USD | 1,790,000.00 USD |
| `1D` | `2125.50` | 1,060,000,000.00 USD | 0.00 USD | 1,060,000,000.00 USD | 179,030.00 USD | 1,510,000.00 USD | 511,470.00 USD |
| `7D` | `2127.60` | 2,420,000,000.00 USD | 0.00 USD | 2,420,000,000.00 USD | 514,750.00 USD | 2,620,000.00 USD | 2,480,000.00 USD |
| `1D` | `2128.00` | 1,060,000,000.00 USD | 0.00 USD | 1,060,000,000.00 USD | 365,910.00 USD | 623,840.00 USD | 131,420.00 USD |
| `7D` | `2130.40` | 2,410,000,000.00 USD | 0.00 USD | 2,410,000,000.00 USD | 2,040,000.00 USD | 2,130,000.00 USD | 1,690,000.00 USD |
| `1D` | `2130.50` | 1,060,000,000.00 USD | 0.00 USD | 1,060,000,000.00 USD | 0.00 USD | 18,610.00 USD | 654,700.00 USD |
| `1D` | `2133.00` | 1,060,000,000.00 USD | 0.00 USD | 1,060,000,000.00 USD | 187,520.00 USD | 1,120,000.00 USD | 0.00 USD |
| `7D` | `2133.20` | 2,410,000,000.00 USD | 0.00 USD | 2,410,000,000.00 USD | 1,930,000.00 USD | 715,940.00 USD | 323,430.00 USD |
| `1D` | `2135.50` | 1,060,000,000.00 USD | 0.00 USD | 1,060,000,000.00 USD | 0.00 USD | 43,420.00 USD | 2,870.00 USD |
| `7D` | `2136.00` | 2,410,000,000.00 USD | 0.00 USD | 2,410,000,000.00 USD | 1,370,000.00 USD | 596,290.00 USD | 18,020.00 USD |
| `1D` | `2138.00` | 1,060,000,000.00 USD | 0.00 USD | 1,060,000,000.00 USD | 555,320.00 USD | 501,410.00 USD | 205,180.00 USD |
| `7D` | `2138.80` | 2,400,000,000.00 USD | 0.00 USD | 2,400,000,000.00 USD | 1,110,000.00 USD | 1,250,000.00 USD | 60,730.00 USD |
| `7D` | `2141.60` | 2,400,000,000.00 USD | 0.00 USD | 2,400,000,000.00 USD | 1,550,000.00 USD | 209,240.00 USD | 766,720.00 USD |
| `1D` | `2143.00` | 1,060,000,000.00 USD | 0.00 USD | 1,060,000,000.00 USD | 295,510.00 USD | 0.00 USD | 3,100.00 USD |
| `7D` | `2144.40` | 2,400,000,000.00 USD | 0.00 USD | 2,400,000,000.00 USD | 465,960.00 USD | 1,530,000.00 USD | 268,500.00 USD |
| `1D` | `2145.50` | 1,060,000,000.00 USD | 0.00 USD | 1,060,000,000.00 USD | 0.00 USD | 27,790.00 USD | 207,420.00 USD |
| `7D` | `2147.20` | 2,400,000,000.00 USD | 0.00 USD | 2,400,000,000.00 USD | 239,110.00 USD | 10,850.00 USD | 0.00 USD |
| `1D` | `2148.00` | 1,060,000,000.00 USD | 0.00 USD | 1,060,000,000.00 USD | 251,250.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2150.00` | 2,400,000,000.00 USD | 0.00 USD | 2,400,000,000.00 USD | 459,630.00 USD | 463,640.00 USD | 31,040.00 USD |
| `7D` | `2152.80` | 2,390,000,000.00 USD | 0.00 USD | 2,390,000,000.00 USD | 29,510.00 USD | 681,070.00 USD | 0.00 USD |
| `7D` | `2155.60` | 2,390,000,000.00 USD | 0.00 USD | 2,390,000,000.00 USD | 157,380.00 USD | 430,180.00 USD | 66,320.00 USD |
| `7D` | `2158.40` | 2,390,000,000.00 USD | 0.00 USD | 2,390,000,000.00 USD | 687,180.00 USD | 1,010,000.00 USD | 1,590,000.00 USD |
| `7D` | `2161.20` | 2,390,000,000.00 USD | 0.00 USD | 2,390,000,000.00 USD | 1,490,000.00 USD | 1,050,000.00 USD | 2,240,000.00 USD |
| `7D` | `2164.00` | 2,390,000,000.00 USD | 0.00 USD | 2,390,000,000.00 USD | 36,870.00 USD | 329,690.00 USD | 409,110.00 USD |
| `7D` | `2166.80` | 2,380,000,000.00 USD | 0.00 USD | 2,380,000,000.00 USD | 25,540.00 USD | 0.00 USD | 68,110.00 USD |
| `7D` | `2169.60` | 2,380,000,000.00 USD | 0.00 USD | 2,380,000,000.00 USD | 1,700,000.00 USD | 726,240.00 USD | 810,540.00 USD |
| `7D` | `2172.40` | 2,380,000,000.00 USD | 0.00 USD | 2,380,000,000.00 USD | 479,540.00 USD | 1,150,000.00 USD | 0.00 USD |
| `7D` | `2194.80` | 2,380,000,000.00 USD | 0.00 USD | 2,380,000,000.00 USD | 141,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2197.60` | 2,380,000,000.00 USD | 0.00 USD | 2,380,000,000.00 USD | 2,440,000.00 USD | 3,270,000.00 USD | 0.00 USD |
| `7D` | `2200.40` | 2,370,000,000.00 USD | 0.00 USD | 2,370,000,000.00 USD | 3,000,000.00 USD | 3,140,000.00 USD | 3,200,000.00 USD |
| `1D` | `2200.50` | 1,060,000,000.00 USD | 0.00 USD | 1,060,000,000.00 USD | 284,470.00 USD | 154,560.00 USD | 225,330.00 USD |
| `1D` | `2203.00` | 1,060,000,000.00 USD | 0.00 USD | 1,060,000,000.00 USD | 1,050,000.00 USD | 62,930.00 USD | 696,550.00 USD |
| `7D` | `2203.20` | 2,360,000,000.00 USD | 0.00 USD | 2,360,000,000.00 USD | 3,240,000.00 USD | 624,500.00 USD | 2,720,000.00 USD |
| `1D` | `2205.50` | 1,050,000,000.00 USD | 0.00 USD | 1,050,000,000.00 USD | 611,820.00 USD | 207,110.00 USD | 781,320.00 USD |
| `7D` | `2206.00` | 2,360,000,000.00 USD | 0.00 USD | 2,360,000,000.00 USD | 6,050,000.00 USD | 4,010,000.00 USD | 4,980,000.00 USD |
| `1D` | `2208.00` | 1,050,000,000.00 USD | 0.00 USD | 1,050,000,000.00 USD | 2,490,000.00 USD | 2,380,000.00 USD | 2,400,000.00 USD |
| `7D` | `2208.80` | 2,340,000,000.00 USD | 0.00 USD | 2,340,000,000.00 USD | 10,060,000.00 USD | 7,030,000.00 USD | 3,080,000.00 USD |
| `1D` | `2210.50` | 1,050,000,000.00 USD | 0.00 USD | 1,050,000,000.00 USD | 2,080,000.00 USD | 1,700,000.00 USD | 1,190,000.00 USD |
| `7D` | `2211.60` | 2,320,000,000.00 USD | 0.00 USD | 2,320,000,000.00 USD | 8,410,000.00 USD | 7,020,000.00 USD | 7,930,000.00 USD |
| `1D` | `2213.00` | 1,040,000,000.00 USD | 0.00 USD | 1,040,000,000.00 USD | 2,530,000.00 USD | 1,450,000.00 USD | 1,290,000.00 USD |
| `7D` | `2214.40` | 2,300,000,000.00 USD | 0.00 USD | 2,300,000,000.00 USD | 12,890,000.00 USD | 12,380,000.00 USD | 9,100,000.00 USD |
| `1D` | `2215.50` | 1,040,000,000.00 USD | 0.00 USD | 1,040,000,000.00 USD | 5,720,000.00 USD | 4,420,000.00 USD | 5,780,000.00 USD |
| `7D` | `2217.20` | 2,260,000,000.00 USD | 0.00 USD | 2,260,000,000.00 USD | 16,020,000.00 USD | 10,280,000.00 USD | 8,240,000.00 USD |
| `1D` | `2218.00` | 1,020,000,000.00 USD | 0.00 USD | 1,020,000,000.00 USD | 4,050,000.00 USD | 4,830,000.00 USD | 1,140,000.00 USD |
| `7D` | `2220.00` | 2,230,000,000.00 USD | 0.00 USD | 2,230,000,000.00 USD | 12,900,000.00 USD | 10,310,000.00 USD | 3,040,000.00 USD |
| `1D` | `2220.50` | 1,010,000,000.00 USD | 0.00 USD | 1,010,000,000.00 USD | 3,450,000.00 USD | 3,630,000.00 USD | 680,790.00 USD |
| `7D` | `2222.80` | 2,200,000,000.00 USD | 0.00 USD | 2,200,000,000.00 USD | 5,190,000.00 USD | 5,430,000.00 USD | 8,890,000.00 USD |
| `1D` | `2223.00` | 1,000,000,000.00 USD | 0.00 USD | 1,000,000,000.00 USD | 5,770,000.00 USD | 3,810,000.00 USD | 2,870,000.00 USD |
| `1D` | `2225.50` | 988,970,000.00 USD | 0.00 USD | 988,970,000.00 USD | 2,730,000.00 USD | 5,220,000.00 USD | 2,420,000.00 USD |
| `7D` | `2225.60` | 2,180,000,000.00 USD | 0.00 USD | 2,180,000,000.00 USD | 13,090,000.00 USD | 13,590,000.00 USD | 9,460,000.00 USD |
| `1D` | `2228.00` | 978,590,000.00 USD | 0.00 USD | 978,590,000.00 USD | 4,680,000.00 USD | 1,810,000.00 USD | 666,740.00 USD |
| `7D` | `2228.40` | 2,150,000,000.00 USD | 0.00 USD | 2,150,000,000.00 USD | 7,680,000.00 USD | 5,550,000.00 USD | 8,240,000.00 USD |
| `1D` | `2230.50` | 971,430,000.00 USD | 0.00 USD | 971,430,000.00 USD | 3,960,000.00 USD | 1,800,000.00 USD | 2,350,000.00 USD |
| `7D` | `2231.20` | 2,130,000,000.00 USD | 0.00 USD | 2,130,000,000.00 USD | 9,590,000.00 USD | 2,970,000.00 USD | 16,200,000.00 USD |
| `1D` | `2233.00` | 963,320,000.00 USD | 0.00 USD | 963,320,000.00 USD | 5,120,000.00 USD | 2,210,000.00 USD | 3,250,000.00 USD |
| `7D` | `2234.00` | 2,100,000,000.00 USD | 0.00 USD | 2,100,000,000.00 USD | 18,760,000.00 USD | 10,880,000.00 USD | 6,070,000.00 USD |
| `1D` | `2235.50` | 952,740,000.00 USD | 0.00 USD | 952,740,000.00 USD | 4,170,000.00 USD | 4,780,000.00 USD | 5,340,000.00 USD |
| `7D` | `2236.80` | 2,060,000,000.00 USD | 0.00 USD | 2,060,000,000.00 USD | 6,910,000.00 USD | 11,270,000.00 USD | 5,890,000.00 USD |
| `1D` | `2238.00` | 938,450,000.00 USD | 0.00 USD | 938,450,000.00 USD | 1,760,000.00 USD | 2,280,000.00 USD | 1,020,000.00 USD |
| `7D` | `2239.60` | 2,040,000,000.00 USD | 0.00 USD | 2,040,000,000.00 USD | 6,630,000.00 USD | 7,850,000.00 USD | 8,430,000.00 USD |
| `1D` | `2240.50` | 933,400,000.00 USD | 0.00 USD | 933,400,000.00 USD | 731,900.00 USD | 124,100.00 USD | 601,200.00 USD |
| `7D` | `2242.40` | 2,020,000,000.00 USD | 0.00 USD | 2,020,000,000.00 USD | 3,820,000.00 USD | 1,890,000.00 USD | 4,750,000.00 USD |
| `1D` | `2243.00` | 931,940,000.00 USD | 0.00 USD | 931,940,000.00 USD | 1,120,000.00 USD | 1,600,000.00 USD | 982,770.00 USD |
| `7D` | `2245.20` | 2,000,000,000.00 USD | 0.00 USD | 2,000,000,000.00 USD | 16,830,000.00 USD | 13,080,000.00 USD | 11,660,000.00 USD |
| `1D` | `2245.50` | 928,230,000.00 USD | 0.00 USD | 928,230,000.00 USD | 2,490,000.00 USD | 1,320,000.00 USD | 408,550.00 USD |
| `1D` | `2248.00` | 924,010,000.00 USD | 0.00 USD | 924,010,000.00 USD | 1,950,000.00 USD | 621,470.00 USD | 1,830,000.00 USD |
| `7D` | `2248.00` | 1,960,000,000.00 USD | 0.00 USD | 1,960,000,000.00 USD | 13,600,000.00 USD | 6,140,000.00 USD | 10,080,000.00 USD |
| `1D` | `2250.50` | 919,610,000.00 USD | 0.00 USD | 919,610,000.00 USD | 2,890,000.00 USD | 1,100,000.00 USD | 1,610,000.00 USD |
| `7D` | `2250.80` | 1,930,000,000.00 USD | 0.00 USD | 1,930,000,000.00 USD | 10,570,000.00 USD | 10,480,000.00 USD | 8,150,000.00 USD |
| `1D` | `2253.00` | 914,020,000.00 USD | 0.00 USD | 914,020,000.00 USD | 6,720,000.00 USD | 7,090,000.00 USD | 4,820,000.00 USD |
| `7D` | `2253.60` | 1,900,000,000.00 USD | 0.00 USD | 1,900,000,000.00 USD | 24,760,000.00 USD | 21,020,000.00 USD | 21,780,000.00 USD |
| `1D` | `2255.50` | 895,380,000.00 USD | 0.00 USD | 895,380,000.00 USD | 2,370,000.00 USD | 1,780,000.00 USD | 5,220,000.00 USD |
| `7D` | `2256.40` | 1,840,000,000.00 USD | 0.00 USD | 1,840,000,000.00 USD | 31,260,000.00 USD | 19,360,000.00 USD | 15,540,000.00 USD |
| `1D` | `2258.00` | 886,010,000.00 USD | 0.00 USD | 886,010,000.00 USD | 8,240,000.00 USD | 3,840,000.00 USD | 4,840,000.00 USD |
| `7D` | `2259.20` | 1,770,000,000.00 USD | 0.00 USD | 1,770,000,000.00 USD | 24,810,000.00 USD | 20,200,000.00 USD | 22,950,000.00 USD |
| `1D` | `2260.50` | 869,090,000.00 USD | 0.00 USD | 869,090,000.00 USD | 13,230,000.00 USD | 9,840,000.00 USD | 10,460,000.00 USD |
| `7D` | `2262.00` | 1,700,000,000.00 USD | 0.00 USD | 1,700,000,000.00 USD | 45,920,000.00 USD | 30,170,000.00 USD | 22,490,000.00 USD |
| `1D` | `2263.00` | 835,550,000.00 USD | 0.00 USD | 835,550,000.00 USD | 10,810,000.00 USD | 14,100,000.00 USD | 9,210,000.00 USD |
| `7D` | `2264.80` | 1,600,000,000.00 USD | 0.00 USD | 1,600,000,000.00 USD | 30,210,000.00 USD | 26,720,000.00 USD | 18,300,000.00 USD |
| `1D` | `2265.50` | 801,430,000.00 USD | 0.00 USD | 801,430,000.00 USD | 12,810,000.00 USD | 9,900,000.00 USD | 4,220,000.00 USD |
| `7D` | `2267.60` | 1,530,000,000.00 USD | 0.00 USD | 1,530,000,000.00 USD | 40,210,000.00 USD | 41,610,000.00 USD | 31,060,000.00 USD |
| `1D` | `2268.00` | 774,500,000.00 USD | 0.00 USD | 774,500,000.00 USD | 7,440,000.00 USD | 8,660,000.00 USD | 3,890,000.00 USD |
| `7D` | `2270.40` | 1,420,000,000.00 USD | 0.00 USD | 1,420,000,000.00 USD | 46,080,000.00 USD | 25,460,000.00 USD | 39,210,000.00 USD |
| `1D` | `2270.50` | 754,510,000.00 USD | 0.00 USD | 754,510,000.00 USD | 10,820,000.00 USD | 11,230,000.00 USD | 8,370,000.00 USD |
| `1D` | `2273.00` | 724,090,000.00 USD | 0.00 USD | 724,090,000.00 USD | 15,130,000.00 USD | 9,950,000.00 USD | 8,840,000.00 USD |
| `7D` | `2273.20` | 1,310,000,000.00 USD | 0.00 USD | 1,310,000,000.00 USD | 26,430,000.00 USD | 25,760,000.00 USD | 20,220,000.00 USD |
| `1D` | `2275.50` | 690,170,000.00 USD | 0.00 USD | 690,170,000.00 USD | 14,620,000.00 USD | 13,850,000.00 USD | 8,660,000.00 USD |
| `7D` | `2276.00` | 1,230,000,000.00 USD | 0.00 USD | 1,230,000,000.00 USD | 52,620,000.00 USD | 46,680,000.00 USD | 45,920,000.00 USD |
| `1D` | `2278.00` | 653,040,000.00 USD | 0.00 USD | 653,040,000.00 USD | 12,140,000.00 USD | 8,370,000.00 USD | 13,710,000.00 USD |
| `7D` | `2278.80` | 1,090,000,000.00 USD | 0.00 USD | 1,090,000,000.00 USD | 69,920,000.00 USD | 30,780,000.00 USD | 43,080,000.00 USD |
| `1D` | `2280.50` | 618,810,000.00 USD | 0.00 USD | 618,810,000.00 USD | 25,850,000.00 USD | 14,940,000.00 USD | 10,810,000.00 USD |
| `7D` | `2281.60` | 943,810,000.00 USD | 0.00 USD | 943,810,000.00 USD | 61,930,000.00 USD | 60,060,000.00 USD | 46,590,000.00 USD |
| `1D` | `2283.00` | 567,210,000.00 USD | 0.00 USD | 567,210,000.00 USD | 20,090,000.00 USD | 15,010,000.00 USD | 19,630,000.00 USD |
| `7D` | `2284.40` | 775,230,000.00 USD | 0.00 USD | 775,230,000.00 USD | 84,440,000.00 USD | 69,880,000.00 USD | 44,650,000.00 USD |
| `1D` | `2285.50` | 512,490,000.00 USD | 0.00 USD | 512,490,000.00 USD | 27,610,000.00 USD | 29,300,000.00 USD | 18,950,000.00 USD |
| `7D` | `2287.20` | 576,260,000.00 USD | 0.00 USD | 576,260,000.00 USD | 59,100,000.00 USD | 55,220,000.00 USD | 44,250,000.00 USD |
| `1D` | `2288.00` | 436,620,000.00 USD | 0.00 USD | 436,620,000.00 USD | 18,510,000.00 USD | 14,610,000.00 USD | 5,790,000.00 USD |
| `7D` | `2290.00` | 417,690,000.00 USD | 0.00 USD | 417,690,000.00 USD | 47,560,000.00 USD | 32,870,000.00 USD | 24,320,000.00 USD |
| `1D` | `2290.50` | 397,710,000.00 USD | 0.00 USD | 397,710,000.00 USD | 10,010,000.00 USD | 10,000,000.00 USD | 4,020,000.00 USD |
| `7D` | `2292.80` | 312,940,000.00 USD | 0.00 USD | 312,940,000.00 USD | 38,470,000.00 USD | 20,900,000.00 USD | 42,370,000.00 USD |
| `1D` | `2293.00` | 373,680,000.00 USD | 0.00 USD | 373,680,000.00 USD | 23,490,000.00 USD | 18,810,000.00 USD | 15,450,000.00 USD |
| `1D` | `2295.50` | 315,940,000.00 USD | 0.00 USD | 315,940,000.00 USD | 19,480,000.00 USD | 17,630,000.00 USD | 9,000,000.00 USD |
| `7D` | `2295.60` | 211,210,000.00 USD | 0.00 USD | 211,210,000.00 USD | 17,510,000.00 USD | 8,110,000.00 USD | 6,790,000.00 USD |
| `1D` | `2298.00` | 269,830,000.00 USD | 0.00 USD | 269,830,000.00 USD | 9,940,000.00 USD | 6,130,000.00 USD | 1,410,000.00 USD |
| `7D` | `2298.40` | 178,800,000.00 USD | 0.00 USD | 178,800,000.00 USD | 2,090,000.00 USD | 5,820,000.00 USD | 301,550.00 USD |
| `1D` | `2300.50` | 252,360,000.00 USD | 0.00 USD | 252,360,000.00 USD | 18,460,000.00 USD | 10,470,000.00 USD | 13,310,000.00 USD |
| `7D` | `2301.20` | 170,580,000.00 USD | 0.00 USD | 170,580,000.00 USD | 11,790,000.00 USD | 2,120,000.00 USD | 7,590,000.00 USD |
| `1D` | `2303.00` | 210,120,000.00 USD | 0.00 USD | 210,120,000.00 USD | 20,250,000.00 USD | 13,820,000.00 USD | 12,850,000.00 USD |
| `7D` | `2304.00` | 149,080,000.00 USD | 0.00 USD | 149,080,000.00 USD | 32,960,000.00 USD | 17,170,000.00 USD | 13,270,000.00 USD |
| `1D` | `2305.50` | 163,190,000.00 USD | 0.00 USD | 163,190,000.00 USD | 17,630,000.00 USD | 10,310,000.00 USD | 22,070,000.00 USD |
| `7D` | `2306.80` | 85,680,000.00 USD | 0.00 USD | 85,680,000.00 USD | 0.00 USD | 3,740,000.00 USD | 11,030,000.00 USD |
| `1D` | `2308.00` | 113,170,000.00 USD | 0.00 USD | 113,170,000.00 USD | 869,360.00 USD | 1,870,000.00 USD | 2,540,000.00 USD |
| `7D` | `2309.60` | 70,920,000.00 USD | 0.00 USD | 70,920,000.00 USD | 282,530.00 USD | 300,580.00 USD | 1,500,000.00 USD |
| `1D` | `2310.50` | 107,890,000.00 USD | 0.00 USD | 107,890,000.00 USD | 6,440,000.00 USD | 3,630,000.00 USD | 6,790,000.00 USD |
| `7D` | `2312.40` | 68,830,000.00 USD | 0.00 USD | 68,830,000.00 USD | 2,470,000.00 USD | 640,510.00 USD | 2,500,000.00 USD |
| `1D` | `2313.00` | 91,030,000.00 USD | 0.00 USD | 91,030,000.00 USD | 5,900,000.00 USD | 8,030,000.00 USD | 4,900,000.00 USD |
| `7D` | `2315.20` | 63,210,000.00 USD | 0.00 USD | 63,210,000.00 USD | 5,020,000.00 USD | 4,100,000.00 USD | 117,510.00 USD |
| `1D` | `2315.50` | 72,200,000.00 USD | 0.00 USD | 72,200,000.00 USD | 10,840,000.00 USD | 6,820,000.00 USD | 1,950,000.00 USD |
| `1D` | `2318.00` | 52,600,000.00 USD | 0.00 USD | 52,600,000.00 USD | 9,460,000.00 USD | 4,310,000.00 USD | 6,170,000.00 USD |
| `7D` | `2318.00` | 53,980,000.00 USD | 0.00 USD | 53,980,000.00 USD | 817,040.00 USD | 3,010,000.00 USD | 0.00 USD |
| `1D` | `2320.50` | 32,650,000.00 USD | 0.00 USD | 32,650,000.00 USD | 3,110,000.00 USD | 3,100,000.00 USD | 1,720,000.00 USD |
| `7D` | `2320.80` | 50,160,000.00 USD | 0.00 USD | 50,160,000.00 USD | 0.00 USD | 2,960,000.00 USD | 0.00 USD |
| `1D` | `2323.00` | 24,720,000.00 USD | 0.00 USD | 24,720,000.00 USD | 4,500,000.00 USD | 4,510,000.00 USD | 2,210,000.00 USD |
| `7D` | `2323.60` | 47,200,000.00 USD | 0.00 USD | 47,200,000.00 USD | 4,070,000.00 USD | 2,210,000.00 USD | 0.00 USD |
| `1D` | `2325.50` | 13,490,000.00 USD | 0.00 USD | 13,490,000.00 USD | 4,120,000.00 USD | 0.00 USD | 66,960.00 USD |
| `7D` | `2326.40` | 40,910,000.00 USD | 0.00 USD | 40,910,000.00 USD | 0.00 USD | 0.00 USD | 126,530.00 USD |
| `1D` | `2328.00` | 9,300,000.00 USD | 0.00 USD | 9,300,000.00 USD | 0.00 USD | 2,910,000.00 USD | 89,050.00 USD |
| `7D` | `2329.20` | 40,790,000.00 USD | 0.00 USD | 40,790,000.00 USD | 3,860,000.00 USD | 0.00 USD | 4,880,000.00 USD |
| `1D` | `2330.50` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 4,990,000.00 USD | 1,150,000.00 USD | 168,480.00 USD |
| `7D` | `2332.00` | 32,040,000.00 USD | 0.00 USD | 32,040,000.00 USD | 29,230,000.00 USD | 0.00 USD | 2,810,000.00 USD |
| `1D` | `2332.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2332.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2333.00` | 13,060,000.00 USD | 13,060,000.00 USD | 0.00 USD | 10,110,000.00 USD | 1,470,000.00 USD | 1,490,000.00 USD |
| `7D` | `2334.80` | 34,610,000.00 USD | 34,610,000.00 USD | 0.00 USD | 7,260,000.00 USD | 18,420,000.00 USD | 8,930,000.00 USD |
| `1D` | `2335.50` | 36,370,000.00 USD | 36,370,000.00 USD | 0.00 USD | 12,670,000.00 USD | 10,650,000.00 USD | 0.00 USD |
| `7D` | `2337.60` | 86,860,000.00 USD | 86,860,000.00 USD | 0.00 USD | 20,380,000.00 USD | 18,310,000.00 USD | 13,560,000.00 USD |
| `1D` | `2338.00` | 37,800,000.00 USD | 37,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,420,000.00 USD |
| `7D` | `2340.40` | 100,250,000.00 USD | 100,250,000.00 USD | 0.00 USD | 0.00 USD | 10,010,000.00 USD | 3,380,000.00 USD |
| `1D` | `2343.00` | 39,700,000.00 USD | 39,700,000.00 USD | 0.00 USD | 0.00 USD | 186,090.00 USD | 1,710,000.00 USD |
| `7D` | `2343.20` | 109,630,000.00 USD | 109,630,000.00 USD | 0.00 USD | 0.00 USD | 5,540,000.00 USD | 3,840,000.00 USD |
| `1D` | `2345.50` | 51,410,000.00 USD | 51,410,000.00 USD | 0.00 USD | 963,370.00 USD | 1,770,000.00 USD | 8,970,000.00 USD |
| `7D` | `2346.00` | 130,380,000.00 USD | 130,380,000.00 USD | 0.00 USD | 0.00 USD | 7,920,000.00 USD | 12,830,000.00 USD |
| `1D` | `2348.00` | 51,870,000.00 USD | 51,870,000.00 USD | 0.00 USD | 460,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2348.80` | 148,870,000.00 USD | 148,870,000.00 USD | 0.00 USD | 495,290.00 USD | 7,240,000.00 USD | 10,750,000.00 USD |
| `1D` | `2350.50` | 86,320,000.00 USD | 86,320,000.00 USD | 0.00 USD | 25,900,000.00 USD | 2,670,000.00 USD | 5,880,000.00 USD |
| `7D` | `2351.60` | 173,070,000.00 USD | 173,070,000.00 USD | 0.00 USD | 572,980.00 USD | 17,950,000.00 USD | 5,680,000.00 USD |
| `1D` | `2353.00` | 90,410,000.00 USD | 90,410,000.00 USD | 0.00 USD | 1,760,000.00 USD | 1,110,000.00 USD | 1,220,000.00 USD |
| `7D` | `2354.40` | 214,310,000.00 USD | 214,310,000.00 USD | 0.00 USD | 6,120,000.00 USD | 34,750,000.00 USD | 371,510.00 USD |
| `1D` | `2355.50` | 108,810,000.00 USD | 108,810,000.00 USD | 0.00 USD | 855,740.00 USD | 16,300,000.00 USD | 1,240,000.00 USD |
| `7D` | `2357.20` | 228,690,000.00 USD | 228,690,000.00 USD | 0.00 USD | 8,470,000.00 USD | 5,920,000.00 USD | 0.00 USD |
| `1D` | `2358.00` | 114,470,000.00 USD | 114,470,000.00 USD | 0.00 USD | 1,400,000.00 USD | 1,810,000.00 USD | 2,450,000.00 USD |
| `7D` | `2360.00` | 230,910,000.00 USD | 230,910,000.00 USD | 0.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2360.50` | 122,480,000.00 USD | 122,480,000.00 USD | 0.00 USD | 2,010,000.00 USD | 2,890,000.00 USD | 3,110,000.00 USD |
| `7D` | `2362.80` | 233,780,000.00 USD | 233,780,000.00 USD | 0.00 USD | 1,180,000.00 USD | 0.00 USD | 1,690,000.00 USD |
| `1D` | `2363.00` | 136,280,000.00 USD | 136,280,000.00 USD | 0.00 USD | 3,730,000.00 USD | 7,640,000.00 USD | 2,420,000.00 USD |
| `1D` | `2365.50` | 139,790,000.00 USD | 139,790,000.00 USD | 0.00 USD | 1,870,000.00 USD | 0.00 USD | 1,640,000.00 USD |
| `7D` | `2365.60` | 241,780,000.00 USD | 241,780,000.00 USD | 0.00 USD | 6,340,000.00 USD | 0.00 USD | 1,660,000.00 USD |
| `1D` | `2368.00` | 148,210,000.00 USD | 148,210,000.00 USD | 0.00 USD | 6,180,000.00 USD | 2,030,000.00 USD | 204,030.00 USD |
| `7D` | `2368.40` | 252,260,000.00 USD | 252,260,000.00 USD | 0.00 USD | 9,590,000.00 USD | 475,460.00 USD | 404,380.00 USD |
| `1D` | `2370.50` | 185,140,000.00 USD | 185,140,000.00 USD | 0.00 USD | 15,780,000.00 USD | 12,620,000.00 USD | 8,530,000.00 USD |
| `7D` | `2371.20` | 314,700,000.00 USD | 314,700,000.00 USD | 0.00 USD | 16,760,000.00 USD | 0.00 USD | 45,680,000.00 USD |
| `1D` | `2373.00` | 207,460,000.00 USD | 207,460,000.00 USD | 0.00 USD | 13,130,000.00 USD | 2,320,000.00 USD | 6,880,000.00 USD |
| `7D` | `2374.00` | 336,700,000.00 USD | 336,700,000.00 USD | 0.00 USD | 15,830,000.00 USD | 121,480.00 USD | 6,050,000.00 USD |
| `1D` | `2375.50` | 229,950,000.00 USD | 229,950,000.00 USD | 0.00 USD | 13,390,000.00 USD | 3,370,000.00 USD | 5,730,000.00 USD |
| `7D` | `2376.80` | 376,910,000.00 USD | 376,910,000.00 USD | 0.00 USD | 12,140,000.00 USD | 5,950,000.00 USD | 22,120,000.00 USD |
| `1D` | `2378.00` | 254,240,000.00 USD | 254,240,000.00 USD | 0.00 USD | 4,330,000.00 USD | 9,290,000.00 USD | 10,660,000.00 USD |
| `7D` | `2379.60` | 404,220,000.00 USD | 404,220,000.00 USD | 0.00 USD | 7,180,000.00 USD | 2,580,000.00 USD | 17,560,000.00 USD |
| `1D` | `2380.50` | 295,960,000.00 USD | 295,960,000.00 USD | 0.00 USD | 12,280,000.00 USD | 12,870,000.00 USD | 16,570,000.00 USD |
| `7D` | `2382.40` | 446,430,000.00 USD | 446,430,000.00 USD | 0.00 USD | 8,510,000.00 USD | 12,380,000.00 USD | 21,320,000.00 USD |
| `1D` | `2383.00` | 347,200,000.00 USD | 347,200,000.00 USD | 0.00 USD | 22,360,000.00 USD | 16,150,000.00 USD | 12,730,000.00 USD |
| `7D` | `2385.20` | 541,560,000.00 USD | 541,560,000.00 USD | 0.00 USD | 15,440,000.00 USD | 28,990,000.00 USD | 50,710,000.00 USD |
| `1D` | `2385.50` | 381,150,000.00 USD | 381,150,000.00 USD | 0.00 USD | 9,330,000.00 USD | 14,700,000.00 USD | 9,930,000.00 USD |
| `1D` | `2388.00` | 410,370,000.00 USD | 410,370,000.00 USD | 0.00 USD | 14,850,000.00 USD | 9,150,000.00 USD | 5,220,000.00 USD |
| `7D` | `2388.00` | 615,000,000.00 USD | 615,000,000.00 USD | 0.00 USD | 4,540,000.00 USD | 34,290,000.00 USD | 34,610,000.00 USD |
| `1D` | `2390.50` | 429,400,000.00 USD | 429,400,000.00 USD | 0.00 USD | 6,210,000.00 USD | 5,300,000.00 USD | 7,520,000.00 USD |
| `7D` | `2390.80` | 713,230,000.00 USD | 713,230,000.00 USD | 0.00 USD | 5,470,000.00 USD | 44,170,000.00 USD | 48,590,000.00 USD |
| `1D` | `2393.00` | 453,800,000.00 USD | 453,800,000.00 USD | 0.00 USD | 5,640,000.00 USD | 12,500,000.00 USD | 6,270,000.00 USD |
| `7D` | `2393.60` | 812,130,000.00 USD | 812,130,000.00 USD | 0.00 USD | 44,040,000.00 USD | 23,140,000.00 USD | 31,720,000.00 USD |
| `1D` | `2395.50` | 470,000,000.00 USD | 470,000,000.00 USD | 0.00 USD | 6,640,000.00 USD | 6,910,000.00 USD | 2,650,000.00 USD |
| `7D` | `2396.40` | 899,490,000.00 USD | 899,490,000.00 USD | 0.00 USD | 29,670,000.00 USD | 34,800,000.00 USD | 22,890,000.00 USD |
| `1D` | `2398.00` | 493,060,000.00 USD | 493,060,000.00 USD | 0.00 USD | 3,940,000.00 USD | 11,190,000.00 USD | 7,930,000.00 USD |
| `7D` | `2399.20` | 992,010,000.00 USD | 992,010,000.00 USD | 0.00 USD | 41,690,000.00 USD | 31,030,000.00 USD | 19,790,000.00 USD |
| `1D` | `2400.50` | 524,960,000.00 USD | 524,960,000.00 USD | 0.00 USD | 14,990,000.00 USD | 5,740,000.00 USD | 11,180,000.00 USD |
| `7D` | `2402.00` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 51,500,000.00 USD | 23,600,000.00 USD | 30,780,000.00 USD |
| `1D` | `2403.00` | 546,440,000.00 USD | 546,440,000.00 USD | 0.00 USD | 5,490,000.00 USD | 8,580,000.00 USD | 7,410,000.00 USD |
| `7D` | `2404.80` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 36,380,000.00 USD | 25,660,000.00 USD | 15,080,000.00 USD |
| `1D` | `2405.50` | 574,220,000.00 USD | 574,220,000.00 USD | 0.00 USD | 12,330,000.00 USD | 7,980,000.00 USD | 7,460,000.00 USD |
| `7D` | `2407.60` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 0.00 USD | 26,430,000.00 USD | 30,520,000.00 USD | 18,910,000.00 USD |
| `1D` | `2408.00` | 609,730,000.00 USD | 609,730,000.00 USD | 0.00 USD | 14,030,000.00 USD | 12,000,000.00 USD | 9,480,000.00 USD |
| `7D` | `2410.40` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 0.00 USD | 22,760,000.00 USD | 27,140,000.00 USD | 24,200,000.00 USD |
| `1D` | `2410.50` | 631,590,000.00 USD | 631,590,000.00 USD | 0.00 USD | 8,210,000.00 USD | 8,870,000.00 USD | 4,780,000.00 USD |
| `1D` | `2413.00` | 649,000,000.00 USD | 649,000,000.00 USD | 0.00 USD | 8,240,000.00 USD | 5,720,000.00 USD | 3,450,000.00 USD |
| `7D` | `2413.20` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 0.00 USD | 13,250,000.00 USD | 13,960,000.00 USD | 12,550,000.00 USD |
| `1D` | `2415.50` | 661,910,000.00 USD | 661,910,000.00 USD | 0.00 USD | 3,460,000.00 USD | 5,780,000.00 USD | 3,670,000.00 USD |
| `7D` | `2416.00` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 0.00 USD | 27,740,000.00 USD | 17,800,000.00 USD | 32,340,000.00 USD |
| `1D` | `2418.00` | 675,070,000.00 USD | 675,070,000.00 USD | 0.00 USD | 4,860,000.00 USD | 5,350,000.00 USD | 2,940,000.00 USD |
| `7D` | `2418.80` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 0.00 USD | 29,770,000.00 USD | 16,840,000.00 USD | 12,150,000.00 USD |
| `1D` | `2420.50` | 689,740,000.00 USD | 689,740,000.00 USD | 0.00 USD | 6,760,000.00 USD | 4,030,000.00 USD | 3,880,000.00 USD |
| `7D` | `2421.60` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 22,900,000.00 USD | 25,380,000.00 USD | 18,640,000.00 USD |
| `1D` | `2423.00` | 704,330,000.00 USD | 704,330,000.00 USD | 0.00 USD | 4,440,000.00 USD | 4,770,000.00 USD | 5,380,000.00 USD |
| `7D` | `2424.40` | 1,660,000,000.00 USD | 1,660,000,000.00 USD | 0.00 USD | 26,330,000.00 USD | 29,850,000.00 USD | 33,610,000.00 USD |
| `1D` | `2425.50` | 708,870,000.00 USD | 708,870,000.00 USD | 0.00 USD | 1,190,000.00 USD | 2,730,000.00 USD | 629,080.00 USD |
| `7D` | `2427.20` | 1,730,000,000.00 USD | 1,730,000,000.00 USD | 0.00 USD | 22,440,000.00 USD | 21,730,000.00 USD | 23,630,000.00 USD |
| `1D` | `2428.00` | 711,860,000.00 USD | 711,860,000.00 USD | 0.00 USD | 1,930,000.00 USD | 464,670.00 USD | 601,200.00 USD |
| `7D` | `2430.00` | 1,760,000,000.00 USD | 1,760,000,000.00 USD | 0.00 USD | 8,250,000.00 USD | 16,890,000.00 USD | 7,560,000.00 USD |
| `1D` | `2430.50` | 715,200,000.00 USD | 715,200,000.00 USD | 0.00 USD | 1,100,000.00 USD | 1,230,000.00 USD | 1,010,000.00 USD |
| `7D` | `2432.80` | 1,790,000,000.00 USD | 1,790,000,000.00 USD | 0.00 USD | 15,460,000.00 USD | 10,350,000.00 USD | 5,820,000.00 USD |
| `1D` | `2433.00` | 719,890,000.00 USD | 719,890,000.00 USD | 0.00 USD | 2,000,000.00 USD | 1,070,000.00 USD | 1,630,000.00 USD |
| `1D` | `2435.50` | 724,760,000.00 USD | 724,760,000.00 USD | 0.00 USD | 3,190,000.00 USD | 495,600.00 USD | 1,190,000.00 USD |
| `7D` | `2435.60` | 1,840,000,000.00 USD | 1,840,000,000.00 USD | 0.00 USD | 20,760,000.00 USD | 13,900,000.00 USD | 12,830,000.00 USD |
| `1D` | `2438.00` | 725,940,000.00 USD | 725,940,000.00 USD | 0.00 USD | 634,820.00 USD | 517,090.00 USD | 21,360.00 USD |
| `7D` | `2438.40` | 1,890,000,000.00 USD | 1,890,000,000.00 USD | 0.00 USD | 16,830,000.00 USD | 22,750,000.00 USD | 14,370,000.00 USD |
| `1D` | `2440.50` | 730,540,000.00 USD | 730,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 2,030,000.00 USD | 1,030,000.00 USD |
| `7D` | `2441.20` | 1,930,000,000.00 USD | 1,930,000,000.00 USD | 0.00 USD | 15,870,000.00 USD | 6,990,000.00 USD | 10,660,000.00 USD |
| `1D` | `2443.00` | 733,160,000.00 USD | 733,160,000.00 USD | 0.00 USD | 1,050,000.00 USD | 667,430.00 USD | 896,280.00 USD |
| `7D` | `2444.00` | 1,950,000,000.00 USD | 1,950,000,000.00 USD | 0.00 USD | 6,380,000.00 USD | 13,460,000.00 USD | 7,960,000.00 USD |
| `1D` | `2445.50` | 735,820,000.00 USD | 735,820,000.00 USD | 0.00 USD | 177,710.00 USD | 839,480.00 USD | 1,640,000.00 USD |
| `7D` | `2446.80` | 1,990,000,000.00 USD | 1,990,000,000.00 USD | 0.00 USD | 11,620,000.00 USD | 7,020,000.00 USD | 18,970,000.00 USD |
| `1D` | `2448.00` | 740,430,000.00 USD | 740,430,000.00 USD | 0.00 USD | 1,770,000.00 USD | 999,000.00 USD | 1,850,000.00 USD |
| `7D` | `2449.60` | 2,030,000,000.00 USD | 2,030,000,000.00 USD | 0.00 USD | 18,130,000.00 USD | 10,300,000.00 USD | 14,870,000.00 USD |
| `1D` | `2450.50` | 747,940,000.00 USD | 747,940,000.00 USD | 0.00 USD | 2,540,000.00 USD | 1,810,000.00 USD | 3,150,000.00 USD |
| `7D` | `2452.40` | 2,060,000,000.00 USD | 2,060,000,000.00 USD | 0.00 USD | 7,700,000.00 USD | 8,980,000.00 USD | 7,330,000.00 USD |
| `1D` | `2453.00` | 758,110,000.00 USD | 758,110,000.00 USD | 0.00 USD | 3,540,000.00 USD | 2,750,000.00 USD | 3,890,000.00 USD |
| `7D` | `2455.20` | 2,070,000,000.00 USD | 2,070,000,000.00 USD | 0.00 USD | 6,850,000.00 USD | 5,830,000.00 USD | 3,620,000.00 USD |
| `1D` | `2455.50` | 766,170,000.00 USD | 766,170,000.00 USD | 0.00 USD | 2,720,000.00 USD | 3,790,000.00 USD | 1,550,000.00 USD |
| `1D` | `2458.00` | 771,930,000.00 USD | 771,930,000.00 USD | 0.00 USD | 2,250,000.00 USD | 2,270,000.00 USD | 1,240,000.00 USD |
| `7D` | `2458.00` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 0.00 USD | 11,170,000.00 USD | 11,200,000.00 USD | 13,580,000.00 USD |
| `1D` | `2460.50` | 775,950,000.00 USD | 775,950,000.00 USD | 0.00 USD | 1,260,000.00 USD | 1,430,000.00 USD | 1,330,000.00 USD |
| `7D` | `2460.80` | 2,140,000,000.00 USD | 2,140,000,000.00 USD | 0.00 USD | 7,010,000.00 USD | 10,680,000.00 USD | 9,010,000.00 USD |
| `1D` | `2463.00` | 779,270,000.00 USD | 779,270,000.00 USD | 0.00 USD | 174,920.00 USD | 2,050,000.00 USD | 1,100,000.00 USD |
| `7D` | `2463.60` | 2,160,000,000.00 USD | 2,160,000,000.00 USD | 0.00 USD | 10,390,000.00 USD | 9,560,000.00 USD | 5,240,000.00 USD |
| `1D` | `2465.50` | 781,340,000.00 USD | 781,340,000.00 USD | 0.00 USD | 820,990.00 USD | 1,240,000.00 USD | 5,650.00 USD |
| `7D` | `2466.40` | 2,170,000,000.00 USD | 2,170,000,000.00 USD | 0.00 USD | 4,790,000.00 USD | 2,080,000.00 USD | 1,330,000.00 USD |
| `1D` | `2468.00` | 782,350,000.00 USD | 782,350,000.00 USD | 0.00 USD | 0.00 USD | 998,350.00 USD | 7,190.00 USD |
| `7D` | `2469.20` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 0.00 USD | 2,490,000.00 USD | 3,570,000.00 USD | 408,300.00 USD |
| `1D` | `2470.50` | 785,770,000.00 USD | 785,770,000.00 USD | 0.00 USD | 1,390,000.00 USD | 883,290.00 USD | 1,160,000.00 USD |
| `7D` | `2472.00` | 2,180,000,000.00 USD | 2,180,000,000.00 USD | 0.00 USD | 3,090,000.00 USD | 2,760,000.00 USD | 814,440.00 USD |
| `1D` | `2473.00` | 786,010,000.00 USD | 786,010,000.00 USD | 0.00 USD | 0.00 USD | 232,740.00 USD | 3,820.00 USD |
| `7D` | `2474.80` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 0.00 USD | 5,400,000.00 USD | 866,790.00 USD | 1,720,000.00 USD |
| `1D` | `2475.50` | 786,750,000.00 USD | 786,750,000.00 USD | 0.00 USD | 738,780.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2477.60` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 0.00 USD | 790,860.00 USD | 3,880,000.00 USD | 1,200,000.00 USD |
| `1D` | `2478.00` | 786,800,000.00 USD | 786,800,000.00 USD | 0.00 USD | 0.00 USD | 41,760.00 USD | 7,750.00 USD |
| `7D` | `2480.40` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 0.00 USD | 2,110,000.00 USD | 1,740,000.00 USD | 0.00 USD |
| `1D` | `2480.50` | 787,350,000.00 USD | 787,350,000.00 USD | 0.00 USD | 0.00 USD | 27,720.00 USD | 518,550.00 USD |
| `1D` | `2483.00` | 787,970,000.00 USD | 787,970,000.00 USD | 0.00 USD | 628,130.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2483.20` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 0.00 USD | 1,210,000.00 USD | 1,190,000.00 USD | 77,610.00 USD |
| `7D` | `2486.00` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 0.00 USD | 49,690.00 USD | 925,020.00 USD | 0.00 USD |
| `7D` | `2488.80` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 0.00 USD | 977,620.00 USD | 857,130.00 USD | 101,890.00 USD |
| `7D` | `2491.60` | 2,210,000,000.00 USD | 2,210,000,000.00 USD | 0.00 USD | 2,360,000.00 USD | 2,470,000.00 USD | 1,120,000.00 USD |
| `7D` | `2494.40` | 2,220,000,000.00 USD | 2,220,000,000.00 USD | 0.00 USD | 1,470,000.00 USD | 2,730,000.00 USD | 6,820,000.00 USD |
| `7D` | `2497.20` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 0.00 USD | 3,640,000.00 USD | 3,570,000.00 USD | 4,430,000.00 USD |
| `7D` | `2500.00` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 0.00 USD | 1,110,000.00 USD | 2,430,000.00 USD | 1,090,000.00 USD |
| `7D` | `2502.80` | 2,240,000,000.00 USD | 2,240,000,000.00 USD | 0.00 USD | 110,450.00 USD | 1,430,000.00 USD | 170,270.00 USD |
| `7D` | `2505.60` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 0.00 USD | 3,200,000.00 USD | 2,320,000.00 USD | 59,220.00 USD |
| `7D` | `2508.40` | 2,250,000,000.00 USD | 2,250,000,000.00 USD | 0.00 USD | 1,810,000.00 USD | 1,270,000.00 USD | 1,990,000.00 USD |
| `7D` | `2511.20` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 0.00 USD | 1,900,000.00 USD | 3,230,000.00 USD | 2,640,000.00 USD |
| `7D` | `2514.00` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 0.00 USD | 776,920.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2516.80` | 2,260,000,000.00 USD | 2,260,000,000.00 USD | 0.00 USD | 97,050.00 USD | 189,640.00 USD | 0.00 USD |
| `7D` | `2519.60` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 894,250.00 USD |
| `1D` | `2520.50` | 788,150,000.00 USD | 788,150,000.00 USD | 0.00 USD | 80,610.00 USD | 61,830.00 USD | 32,260.00 USD |
| `7D` | `2522.40` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 0.00 USD | 1,050,000.00 USD | 0.00 USD | 945,860.00 USD |
| `1D` | `2523.00` | 788,210,000.00 USD | 788,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 57,880.00 USD |
| `7D` | `2525.20` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 0.00 USD | 307,040.00 USD | 224,130.00 USD | 200,040.00 USD |
| `1D` | `2525.50` | 788,740,000.00 USD | 788,740,000.00 USD | 0.00 USD | 421,540.00 USD | 57,450.00 USD | 53,680.00 USD |
| `1D` | `2528.00` | 789,410,000.00 USD | 789,410,000.00 USD | 0.00 USD | 0.00 USD | 645,910.00 USD | 26,970.00 USD |
| `7D` | `2528.00` | 2,270,000,000.00 USD | 2,270,000,000.00 USD | 0.00 USD | 1,580,000.00 USD | 1,690,000.00 USD | 727,590.00 USD |
| `1D` | `2530.50` | 790,840,000.00 USD | 790,840,000.00 USD | 0.00 USD | 995,550.00 USD | 0.00 USD | 437,490.00 USD |
| `7D` | `2530.80` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 0.00 USD | 2,080,000.00 USD | 1,110,000.00 USD | 1,220,000.00 USD |
| `1D` | `2533.00` | 791,220,000.00 USD | 791,220,000.00 USD | 0.00 USD | 359,430.00 USD | 0.00 USD | 16,730.00 USD |
| `7D` | `2533.60` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 0.00 USD | 2,680,000.00 USD | 2,100,000.00 USD | 1,390,000.00 USD |
| `1D` | `2535.50` | 792,280,000.00 USD | 792,280,000.00 USD | 0.00 USD | 431,500.00 USD | 134,490.00 USD | 493,320.00 USD |
| `7D` | `2536.40` | 2,290,000,000.00 USD | 2,290,000,000.00 USD | 0.00 USD | 3,670,000.00 USD | 2,850,000.00 USD | 2,740,000.00 USD |
| `1D` | `2538.00` | 797,010,000.00 USD | 797,010,000.00 USD | 0.00 USD | 1,830,000.00 USD | 904,340.00 USD | 2,000,000.00 USD |
| `7D` | `2539.20` | 2,300,000,000.00 USD | 2,300,000,000.00 USD | 0.00 USD | 2,620,000.00 USD | 2,470,000.00 USD | 1,090,000.00 USD |
| `1D` | `2540.50` | 799,410,000.00 USD | 799,410,000.00 USD | 0.00 USD | 1,150,000.00 USD | 1,010,000.00 USD | 237,050.00 USD |
| `7D` | `2542.00` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 0.00 USD | 3,400,000.00 USD | 2,740,000.00 USD | 2,240,000.00 USD |
| `1D` | `2543.00` | 801,580,000.00 USD | 801,580,000.00 USD | 0.00 USD | 1,090,000.00 USD | 1,070,000.00 USD | 19,390.00 USD |
| `7D` | `2544.80` | 2,310,000,000.00 USD | 2,310,000,000.00 USD | 0.00 USD | 2,170,000.00 USD | 1,830,000.00 USD | 1,350,000.00 USD |
| `1D` | `2545.50` | 802,990,000.00 USD | 802,990,000.00 USD | 0.00 USD | 590,640.00 USD | 800,740.00 USD | 12,050.00 USD |
| `7D` | `2547.60` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 0.00 USD | 2,380,000.00 USD | 938,680.00 USD | 2,940,000.00 USD |
| `1D` | `2548.00` | 805,930,000.00 USD | 805,930,000.00 USD | 0.00 USD | 1,370,000.00 USD | 832,850.00 USD | 743,470.00 USD |
| `7D` | `2550.40` | 2,320,000,000.00 USD | 2,320,000,000.00 USD | 0.00 USD | 2,920,000.00 USD | 2,690,000.00 USD | 1,130,000.00 USD |
| `1D` | `2550.50` | 809,080,000.00 USD | 809,080,000.00 USD | 0.00 USD | 1,070,000.00 USD | 1,460,000.00 USD | 618,500.00 USD |
| `1D` | `2553.00` | 810,170,000.00 USD | 810,170,000.00 USD | 0.00 USD | 781,250.00 USD | 220,540.00 USD | 89,570.00 USD |
| `7D` | `2553.20` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 0.00 USD | 2,590,000.00 USD | 788,360.00 USD | 2,180,000.00 USD |
| `1D` | `2555.50` | 811,680,000.00 USD | 811,680,000.00 USD | 0.00 USD | 1,030,000.00 USD | 124,540.00 USD | 365,340.00 USD |
| `7D` | `2556.00` | 2,340,000,000.00 USD | 2,340,000,000.00 USD | 0.00 USD | 2,760,000.00 USD | 255,750.00 USD | 5,320,000.00 USD |
| `1D` | `2558.00` | 813,330,000.00 USD | 813,330,000.00 USD | 0.00 USD | 525,530.00 USD | 415,210.00 USD | 710,290.00 USD |
| `7D` | `2558.80` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 0.00 USD | 3,850,000.00 USD | 1,640,000.00 USD | 2,340,000.00 USD |
| `1D` | `2560.50` | 817,440,000.00 USD | 817,440,000.00 USD | 0.00 USD | 1,840,000.00 USD | 1,100,000.00 USD | 1,170,000.00 USD |
| `7D` | `2561.60` | 2,350,000,000.00 USD | 2,350,000,000.00 USD | 0.00 USD | 2,780,000.00 USD | 1,960,000.00 USD | 785,020.00 USD |
| `1D` | `2563.00` | 819,370,000.00 USD | 819,370,000.00 USD | 0.00 USD | 440,660.00 USD | 504,630.00 USD | 984,190.00 USD |
| `7D` | `2564.40` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 1,800,000.00 USD | 1,780,000.00 USD | 1,120,000.00 USD |
| `1D` | `2565.50` | 820,250,000.00 USD | 820,250,000.00 USD | 0.00 USD | 183,260.00 USD | 700,850.00 USD | 0.00 USD |
| `7D` | `2567.20` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 575,630.00 USD | 1,560,000.00 USD | 2,690,000.00 USD |
| `1D` | `2568.00` | 820,480,000.00 USD | 820,480,000.00 USD | 0.00 USD | 46,810.00 USD | 0.00 USD | 175,760.00 USD |
| `7D` | `2570.00` | 2,360,000,000.00 USD | 2,360,000,000.00 USD | 0.00 USD | 125,250.00 USD | 290,680.00 USD | 1,180,000.00 USD |
| `1D` | `2570.50` | 821,500,000.00 USD | 821,500,000.00 USD | 0.00 USD | 422,490.00 USD | 289,160.00 USD | 306,410.00 USD |
| `7D` | `2572.80` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 986,590.00 USD | 1,790,000.00 USD |
| `1D` | `2573.00` | 822,410,000.00 USD | 822,410,000.00 USD | 0.00 USD | 485,450.00 USD | 400,040.00 USD | 27,290.00 USD |
| `1D` | `2575.50` | 823,440,000.00 USD | 823,440,000.00 USD | 0.00 USD | 546,100.00 USD | 0.00 USD | 488,260.00 USD |
| `7D` | `2575.60` | 2,370,000,000.00 USD | 2,370,000,000.00 USD | 0.00 USD | 2,180,000.00 USD | 344,620.00 USD | 1,060,000.00 USD |
| `1D` | `2578.00` | 823,600,000.00 USD | 823,600,000.00 USD | 0.00 USD | 118,210.00 USD | 31,550.00 USD | 8,540.00 USD |
| `7D` | `2578.40` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 0.00 USD | 734,040.00 USD | 1,480,000.00 USD | 1,750,000.00 USD |
| `1D` | `2580.50` | 824,290,000.00 USD | 824,290,000.00 USD | 0.00 USD | 490,860.00 USD | 8,910.00 USD | 191,610.00 USD |
| `7D` | `2581.20` | 2,380,000,000.00 USD | 2,380,000,000.00 USD | 0.00 USD | 3,870,000.00 USD | 912,130.00 USD | 1,670,000.00 USD |
| `1D` | `2583.00` | 825,580,000.00 USD | 825,580,000.00 USD | 0.00 USD | 420,950.00 USD | 634,310.00 USD | 235,840.00 USD |
| `7D` | `2584.00` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 0.00 USD | 146,630.00 USD | 1,490,000.00 USD | 3,100,000.00 USD |
| `1D` | `2585.50` | 826,010,000.00 USD | 826,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 426,920.00 USD |
| `7D` | `2586.80` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 0.00 USD | 1,900,000.00 USD | 1,970,000.00 USD | 1,530,000.00 USD |
| `1D` | `2587.70` | 827,380,000.00 USD | 827,380,000.00 USD | 0.00 USD | 665,720.00 USD | 0.00 USD | 707,720.00 USD |
| `7D` | `2589.60` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 0.00 USD | 2,840,000.00 USD | 446,810.00 USD | 2,140,000.00 USD |
| `7D` | `2592.40` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 0.00 USD | 2,340,000.00 USD | 1,280,000.00 USD | 1,550,000.00 USD |
| `7D` | `2595.20` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 0.00 USD | 452,020.00 USD | 569,790.00 USD | 1,260,000.00 USD |
| `7D` | `2598.00` | 2,410,000,000.00 USD | 2,410,000,000.00 USD | 0.00 USD | 2,280,000.00 USD | 1,630,000.00 USD | 1,910,000.00 USD |
| `7D` | `2600.80` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 0.00 USD | 931,390.00 USD | 1,960,000.00 USD | 1,610,000.00 USD |
| `7D` | `2603.60` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,580,000.00 USD | 1,680,000.00 USD |
| `7D` | `2606.40` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 0.00 USD | 1,480,000.00 USD | 229,360.00 USD | 320,080.00 USD |
| `7D` | `2609.20` | 2,420,000,000.00 USD | 2,420,000,000.00 USD | 0.00 USD | 1,090,000.00 USD | 723,630.00 USD | 10,700.00 USD |
| `7D` | `2612.00` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 0.00 USD | 770,330.00 USD | 608,060.00 USD | 43,560.00 USD |
| `7D` | `2614.80` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 0.00 USD | 1,060,000.00 USD | 1,000,000.00 USD | 409,160.00 USD |
| `7D` | `2617.60` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 0.00 USD | 1,550,000.00 USD | 209,240.00 USD | 392,750.00 USD |
| `7D` | `2620.40` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 0.00 USD | 47,360.00 USD | 1,120,000.00 USD | 268,500.00 USD |
| `7D` | `2623.20` | 2,430,000,000.00 USD | 2,430,000,000.00 USD | 0.00 USD | 418,600.00 USD | 410,460.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `29.77B` | Total OI Tokens: `12,756,886.1 ETH`
  * 1h OI Change: `+0.01%` | 4h OI Change: `-2.60%` | 24h OI Change: `-0.96%`
  * Exchange Breakdown: Binance=`8.84B` | Bybit=`2.11B` | OKX=`1.76B` | Hyperliquid=`2.54B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `1.01M` | Last 24h: `2.27M` | Last 3d: `7.66M` | Last 7d: `13.85M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0098%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0051%` | **USDT KuCoin** | `0.0070%` |
| **USDT MEXC** | `0.0096%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0093%` | **USDT Bitget** | `0.0062%` |
| **CoinM Binance** | `0.0093%` | **CoinM OKX** | `0.0093%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `58.56%` | `41.44%` | `1.41` | 243,990,000.00 USD |
| `15M` | `Binance` | `52.91%` | `47.09%` | `1.12` | 62,240,000.00 USD |
| `15M` | `OKX` | `59.87%` | `40.13%` | `1.49` | 30,260,000.00 USD |
| `15M` | `Bybit` | `67.91%` | `32.09%` | `2.12` | 36,120,000.00 USD |
| `15M` | `KuCoin` | `44.92%` | `55.08%` | `0.82` | 43,030.00 USD |
| `15M` | `Gate` | `50.93%` | `49.07%` | `1.04` | 26,050,000.00 USD |
| `15M` | `Bitget` | `67.48%` | `32.52%` | `2.08` | 8,340,000.00 USD |
| `15M` | `BingX` | `70.74%` | `29.26%` | `2.42` | 5,460,000.00 USD |
| `15M` | `MEXC` | `66.23%` | `33.77%` | `1.96` | 20,170,000.00 USD |
| `15M` | `Bitunix` | `77.59%` | `22.41%` | `3.46` | 13,170,000.00 USD |
| `15M` | `Hyperliquid` | `63.45%` | `36.55%` | `1.74` | 6,050,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `58.93%` | `41.07%` | `1.43` | 2,340,000.00 USD |
| `15M` | `Crypto.com` | `50.47%` | `49.53%` | `1.02` | 844,500.00 USD |
| `15M` | `WhiteBIT` | `0.59%` | `99.41%` | `0.01` | 2,070,000.00 USD |
| `15M` | `HTX` | `47.25%` | `52.75%` | `0.90` | 1,540,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `54.05%` | `45.95%` | `1.18` | 9,680,000.00 USD |
| `15M` | `Bitfinex` | `44.47%` | `55.53%` | `0.80` | 158,890.00 USD |
| `15M` | `Kraken` | `56.46%` | `43.54%` | `1.30` | 1,750,000.00 USD |
| `15M` | `Aster` | `64.01%` | `35.99%` | `1.78` | 2,830,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `43.46%` | `56.54%` | `0.77` | 14,870,000.00 USD |
| `15M` | `Whale Positions` | `52.91%` | `47.09%` | `1.12` | 62,240,000.00 USD |
| `15M` | `Global Accounts` | `58.56%` | `41.44%` | `1.41` | 243,990,000.00 USD |
| `1H` | `ETH` | `56.83%` | `43.17%` | `1.32` | 1,230,000,000.00 USD |
| `1H` | `Binance` | `58.82%` | `41.18%` | `1.43` | 351,360,000.00 USD |
| `1H` | `OKX` | `55.61%` | `44.39%` | `1.25` | 156,860,000.00 USD |
| `1H` | `Bybit` | `55.49%` | `44.51%` | `1.25` | 129,000,000.00 USD |
| `1H` | `KuCoin` | `73.85%` | `26.15%` | `2.82` | 1,640,000.00 USD |
| `1H` | `Gate` | `57.46%` | `42.54%` | `1.35` | 151,990,000.00 USD |
| `1H` | `Bitget` | `58.63%` | `41.37%` | `1.42` | 49,320,000.00 USD |
| `1H` | `BingX` | `69.95%` | `30.05%` | `2.33` | 22,530,000.00 USD |
| `1H` | `MEXC` | `54.89%` | `45.11%` | `1.22` | 87,610,000.00 USD |
| `1H` | `Bitunix` | `64.4%` | `35.6%` | `1.81` | 70,430,000.00 USD |
| `1H` | `Hyperliquid` | `48.89%` | `51.11%` | `0.96` | 50,180,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `52.22%` | `47.78%` | `1.09` | 12,310,000.00 USD |
| `1H` | `Crypto.com` | `54.07%` | `45.93%` | `1.18` | 6,830,000.00 USD |
| `1H` | `WhiteBIT` | `54.14%` | `45.86%` | `1.18` | 22,740,000.00 USD |
| `1H` | `HTX` | `57.45%` | `42.55%` | `1.35` | 6,890,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `55.54%` | `44.46%` | `1.25` | 39,120,000.00 USD |
| `1H` | `Bitfinex` | `48.64%` | `51.36%` | `0.95` | 1,020,000.00 USD |
| `1H` | `Kraken` | `42.9%` | `57.1%` | `0.75` | 11,030,000.00 USD |
| `1H` | `Aster` | `56.99%` | `43.01%` | `1.33` | 13,370,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `46.21%` | `53.79%` | `0.86` | 43,540,000.00 USD |
| `1H` | `Whale Positions` | `58.82%` | `41.18%` | `1.43` | 351,360,000.00 USD |
| `1H` | `Global Accounts` | `56.83%` | `43.17%` | `1.32` | 1,230,000,000.00 USD |
| `4H` | `ETH` | `48.61%` | `51.39%` | `0.95` | 12,760,000,000.00 USD |
| `4H` | `Binance` | `45.97%` | `54.03%` | `0.85` | 3,920,000,000.00 USD |
| `4H` | `OKX` | `48.48%` | `51.52%` | `0.94` | 1,780,000,000.00 USD |
| `4H` | `Bybit` | `48.11%` | `51.89%` | `0.93` | 1,280,000,000.00 USD |
| `4H` | `KuCoin` | `40.63%` | `59.37%` | `0.68` | 54,960,000.00 USD |
| `4H` | `Gate` | `50.63%` | `49.37%` | `1.03` | 1,480,000,000.00 USD |
| `4H` | `Bitget` | `46.83%` | `53.17%` | `0.88` | 725,380,000.00 USD |
| `4H` | `BingX` | `53.28%` | `46.72%` | `1.14` | 242,100,000.00 USD |
| `4H` | `MEXC` | `50.59%` | `49.41%` | `1.02` | 715,750,000.00 USD |
| `4H` | `Bitunix` | `49.57%` | `50.43%` | `0.98` | 684,010,000.00 USD |
| `4H` | `Hyperliquid` | `52.28%` | `47.72%` | `1.10` | 640,670,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `53.39%` | `46.61%` | `1.15` | 86,190,000.00 USD |
| `4H` | `Crypto.com` | `49.05%` | `50.95%` | `0.96` | 86,430,000.00 USD |
| `4H` | `WhiteBIT` | `59.21%` | `40.79%` | `1.45` | 239,560,000.00 USD |
| `4H` | `HTX` | `46.91%` | `53.09%` | `0.88` | 54,760,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `55.41%` | `44.59%` | `1.24` | 302,170,000.00 USD |
| `4H` | `Bitfinex` | `44.64%` | `55.36%` | `0.81` | 8,660,000.00 USD |
| `4H` | `Kraken` | `47.63%` | `52.37%` | `0.91` | 93,800,000.00 USD |
| `4H` | `Aster` | `45.71%` | `54.29%` | `0.84` | 152,150,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.69%` | `51.31%` | `0.95` | 211,490,000.00 USD |
| `4H` | `Whale Positions` | `45.97%` | `54.03%` | `0.85` | 3,920,000,000.00 USD |
| `4H` | `Global Accounts` | `48.61%` | `51.39%` | `0.95` | 12,760,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `2350.25` | `2349.30` | `2350.25` | `2352.75` | `2346.75` | 77,932,643.01 USD | 38,640,268.57 USD | 39,292,374.44 USD | -652,105.87 USD | `-0.84%` | `1B / 1S` |
| `0:00 UTC` | `2340.25` | `2342.19` | `2340.25` | `2353.25` | `2334.75` | 172,183,772.38 USD | 75,695,646.18 USD | 96,488,126.21 USD | -20,792,480.03 USD | `-12.08%` | `0B / 3S` |
| `5:00 UTC` | `2335.75` | `2335.37` | `2335.75` | `2340.75` | `2330.75` | 125,556,310.13 USD | 63,692,130.92 USD | 61,864,179.21 USD | 1,827,951.70 USD | `+1.46%` | `1B / 1S` |
| `0:00 UTC` | `2337.75` | `2338.67` | `2337.75` | `2341.75` | `2335.75` | 48,324,873.75 USD | 25,087,349.31 USD | 23,237,524.44 USD | 1,849,824.87 USD | `+3.83%` | `0B / 0S` |
| `5:00 UTC` | `2340.25` | `2338.33` | `2340.25` | `2342.25` | `2333.75` | 43,794,873.23 USD | 24,013,000.37 USD | 19,781,872.86 USD | 4,231,127.51 USD | `+9.66%` | `0B / 2S` |
| `0:00 UTC` | `2327.25` | `2327.16` | `2327.25` | `2335.25` | `2323.25` | 195,411,305.09 USD | 64,523,153.35 USD | 130,888,151.74 USD | -66,364,998.40 USD | `-33.96%` | `0B / 9S` |
| `5:00 UTC` | `2331.25` | `2330.55` | `2331.25` | `2334.25` | `2325.75` | 53,213,391.28 USD | 35,445,824.71 USD | 17,767,566.57 USD | 17,678,258.14 USD | `+33.22%` | `4B / 0S` |
| `0:00 UTC` | `2327.75` | `2328.10` | `2327.75` | `2331.25` | `2326.25` | 28,953,047.89 USD | 13,068,031.79 USD | 15,885,016.10 USD | -2,816,984.30 USD | `-9.73%` | `0B / 1S` |
| `5:00 UTC` | `2326.75` | `2328.61` | `2326.75` | `2331.75` | `2325.75` | 28,646,242.16 USD | 14,157,941.65 USD | 14,488,300.51 USD | -330,358.86 USD | `-1.15%` | `0B / 1S` |
| `0:00 UTC` | `2334.25` | `2333.93` | `2334.25` | `2336.25` | `2330.25` | 28,212,044.90 USD | 15,097,628.81 USD | 13,114,416.10 USD | 1,983,212.71 USD | `+7.03%` | `1B / 1S` |

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
| `5m` | 274,310.00 USD | 14,410,000.00 USD | **`ACCUMULATION`** |
| `15m` | 2,010,000.00 USD | 26,780,000.00 USD | **`ACCUMULATION`** |
| `30m` | 3,400,000.00 USD | 27,040,000.00 USD | **`ACCUMULATION`** |
| `1h` | 5,210,000.00 USD | 45,180,000.00 USD | **`ACCUMULATION`** |
| `2h` | 4,060,000.00 USD | -141,270,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 826,270.00 USD | -374,070,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 27,160,000.00 USD | -77,170,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 18,640,000.00 USD | -89,110,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 37,320,000.00 USD | -81,990,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -21,810,000.00 USD | -451,720,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -11,200,000.00 USD | -1,080,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,010,000,000.00 USD | -8,170,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+274.31K` | 15m=`+2.01M` | 1h=`+5.21M` | 24h=`-21.81M`
* Futures Capital Netflows: 5m=`+14.41M` | 15m=`+26.78M` | 1h=`+45.18M` | 24h=`-451.72M`
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
  * `2026-10-30 00:58:08 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:08 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:17:08 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:09:08 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:09:08 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:08 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:08 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `2280.68` (Risk Distance: `17.02` pts)
  * +2.5R Take Profit: `2340.24`
  * Mathematical Lot Sizing: **`0.58 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2337.30` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2354.32` (Risk Distance: `17.02` pts)
  * +2.5R Take Profit: `2294.76`
  * Mathematical Lot Sizing: **`0.58 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2350.40`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
