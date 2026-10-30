# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 15:51:22 IST` (`2026-10-30 10:21:22 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2218.20` | **Live Ask Quote**: `2221.10` | **Mid Price**: `2219.65`
- **Spread Points**: `290.00` | **Spread BPS**: `13.07 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2219.92` | VWAP Z-Score: `+0.05` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `11.17` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `42.29` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2268.39` | Lower -3.00σ Band: `2171.46`
  * Upper +2.51σ Band: `2260.47` | Lower -2.51σ Band: `2179.37`
  * Upper +2.01σ Band: `2252.39` | Lower -2.01σ Band: `2187.45`
  * Upper +2.00σ Band: `2252.23` | Lower -2.00σ Band: `2187.61`
  * Upper +1.28σ Band: `2240.60` | Lower -1.28σ Band: `2199.24`
  * Upper +1.00σ Band: `2236.08` | Lower -1.00σ Band: `2203.77`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2224.53` | EMA-20=`2227.99` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2241.13` (Slope: `+0.0000`) | EMA-100=`2264.59`
  * Institutional Anchors: EMA-144=`2278.52` | EMA-200=`2291.38` (Slope: `-0.3669`) | EMA-233=`2296.43`
- **Range Boundaries**: 24H High=`2374.90` | 24H Low=`2167.70` | Weekly High=`2387.80` | Weekly Low=`2167.70`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2252.28` (Distance: `-1.41%`)
  * Point of Control (POC) = `2221.52` (Distance: `-0.04%`)
  * Value Area Low (VAL) = `2195.62` (Distance: `+1.14%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2339.52` | POC=`2321.58` | VAL=`2296.66`
  * Prior Day Extremes: PDH=`2374.90` | PDL=`2225.40` | PDC=`2252.70`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2354.78` | Weekly POC=`2309.30` | Weekly VAL=`2300.49`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2289.10` | Low=`2167.70`
  * London Session (08:00-16:00 UTC): High=`2251.30` | Low=`2215.10`
  * New York Session (13:00-21:00 UTC): High=`2226.58` | Low=`2216.10`
  * Initial Balance (First Hour): IB High=`2246.50` | IB Low=`2230.60`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2210.77` - `2228.53`
  * Optimal Trade Entry (OTE 0.705): `2224.09`
  * Structural Invalidation Anchor (0.786): `2237.41`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2224.75` | `2225.24` | `2223.67` | `2224.27` | `5,132` | 11,415,555.06 USD | -639,460.72 USD | `-5.60%` | -953,274,491.17 USD | `-0.01` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `2224.26` | `2224.31` | `2220.36` | `2220.98` | `8,134` | 18,072,993.37 USD | -2,576,278.21 USD | `-14.25%` | -955,850,769.38 USD | `-0.36` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `2220.98` | `2222.51` | `2220.97` | `2222.50` | `903` | 2,005,421.89 USD | 1,560,233.77 USD | `+77.80%` | -954,290,535.60 USD | `+0.37` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `2229.81` | `2229.92` | `2226.00` | `2228.42` | `23,981` | 53,422,952.94 USD | 4,795,974.76 USD | `+8.98%` | -954,048,144.99 USD | `+0.31` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `2228.43` | `2228.43` | `2221.66` | `2224.27` | `25,370` | 56,423,190.50 USD | -1,089,080.98 USD | `-1.93%` | -955,137,225.97 USD | `-0.01` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `2224.26` | `2224.31` | `2220.36` | `2222.50` | `9,037` | 20,078,415.26 USD | -1,016,044.43 USD | `-5.06%` | -956,153,270.40 USD | `-0.03` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2235.54` | `2236.80` | `2223.18` | `2227.93` | `164,265` | 366,023,334.59 USD | -37,825,356.97 USD | `-10.33%` | -969,069,546.97 USD | `+0.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `2227.92` | `2231.18` | `2220.24` | `2228.42` | `122,419` | 272,434,813.90 USD | 5,581,746.93 USD | `+2.05%` | -963,487,800.04 USD | `+0.46` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `2228.43` | `2228.43` | `2220.36` | `2221.85` | `34,011` | 75,622,412.17 USD | -2,944,619.87 USD | `-3.89%` | -966,432,419.91 USD | `+0.40` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -913,988,928.25 USD | `-0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2257.30` | `2225.47` | `2235.54` | `766,584` | 1,719,026,962.60 USD | 26,122,859.80 USD | `+1.52%` | -887,866,068.44 USD | `+0.88` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `2235.54` | `2236.80` | `2220.24` | `2221.77` | `320,700` | 714,091,172.22 USD | -35,185,390.32 USD | `-4.93%` | -923,051,458.77 USD | `+0.54` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -98,115,944.70 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2252.34` | `2,564,135` | 5,830,064,162.53 USD | -554,237,569.32 USD | `-9.51%` | -652,353,514.01 USD | `-1.25` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -913,988,928.25 USD | `-0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2257.30` | `2225.47` | `2235.54` | `766,584` | 1,719,026,962.60 USD | 26,122,859.80 USD | `+1.52%` | -887,866,068.44 USD | `+0.88` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `2235.54` | `2236.80` | `2220.24` | `2221.77` | `320,700` | 714,091,172.22 USD | -35,185,390.32 USD | `-4.93%` | -923,051,458.77 USD | `+0.54` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`2219.65`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2220.70` | `577.2751` | 1,281,954.81 USD | 13,470,403.11 USD | `11 orders` | `-0.09%` | `-` |
| `BID` | `2220.80` | `29.9345` | 66,478.54 USD | 12,188,448.29 USD | `4 orders` | `-0.08%` | `-` |
| `BID` | `2220.90` | `171.7030` | 381,335.19 USD | 12,121,969.76 USD | `7 orders` | `-0.08%` | `-` |
| `BID` | `2221.00` | `2043.9782` | 4,539,675.58 USD | 11,740,634.56 USD | `8 orders` | `-0.07%` | `-` |
| `BID` | `2221.10` | `424.0141` | 941,777.72 USD | 7,200,958.98 USD | `12 orders` | `-0.07%` | `-` |
| `BID` | `2221.20` | `203.0745` | 451,069.08 USD | 6,259,181.26 USD | `8 orders` | `-0.07%` | `-` |
| `BID` | `2221.30` | `488.0550` | 1,084,116.57 USD | 5,808,112.18 USD | `9 orders` | `-0.06%` | `-` |
| `BID` | `2221.40` | `379.1094` | 842,153.62 USD | 4,723,995.61 USD | `8 orders` | `-0.06%` | `-` |
| `BID` | `2221.50` | `245.7552` | 545,945.18 USD | 3,881,841.99 USD | `10 orders` | `-0.05%` | `-` |
| `BID` | `2221.60` | `222.0277` | 493,256.74 USD | 3,335,896.81 USD | `7 orders` | `-0.05%` | `-` |
| `BID` | `2221.70` | `43.9093` | 97,553.29 USD | 2,842,640.08 USD | `6 orders` | `-0.04%` | `-` |
| `BID` | `2221.80` | `254.5133` | 565,477.65 USD | 2,745,086.78 USD | `7 orders` | `-0.04%` | `-` |
| `BID` | `2221.90` | `186.2371` | 413,800.21 USD | 2,179,609.13 USD | `6 orders` | `-0.03%` | `-` |
| `BID` | `2222.00` | `254.1531` | 564,728.19 USD | 1,765,808.92 USD | `5 orders` | `-0.03%` | `-` |
| `BID` | `2222.10` | `129.5991` | 287,982.16 USD | 1,201,080.73 USD | `8 orders` | `-0.02%` | `-` |
| `BID` | `2222.20` | `100.3148` | 222,919.55 USD | 913,098.57 USD | `8 orders` | `-0.02%` | `-` |
| `BID` | `2222.30` | `78.6497` | 174,783.23 USD | 690,179.02 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `2222.40` | `78.6801` | 174,858.65 USD | 515,395.80 USD | `6 orders` | `-0.01%` | `-` |
| `BID` | `2222.50` | `18.5047` | 41,126.70 USD | 340,537.14 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `2222.60` | `134.7118` | 299,410.45 USD | 299,410.45 USD | `20 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2222.65` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,222.65` | `0.00%` | `-` |
| `ASK` | `2222.70` | `54.6295` | 121,424.99 USD | 121,424.99 USD | `11 orders` | `+0.00%` | `-` |
| `ASK` | `2222.80` | `124.7812` | 277,363.65 USD | 398,788.64 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `2222.90` | `174.8857` | 388,753.42 USD | 787,542.06 USD | `14 orders` | `+0.01%` | `-` |
| `ASK` | `2223.00` | `220.1000` | 489,282.30 USD | 1,276,824.36 USD | `13 orders` | `+0.02%` | `-` |
| `ASK` | `2223.10` | `257.8203` | 573,160.31 USD | 1,849,984.67 USD | `8 orders` | `+0.02%` | `-` |
| `ASK` | `2223.20` | `553.8283` | 1,231,271.08 USD | 3,081,255.75 USD | `11 orders` | `+0.02%` | `-` |
| `ASK` | `2223.30` | `446.9403` | 993,682.37 USD | 4,074,938.12 USD | `19 orders` | `+0.03%` | `-` |
| `ASK` | `2223.40` | `45.0061` | 100,066.56 USD | 4,175,004.68 USD | `18 orders` | `+0.03%` | `-` |
| `ASK` | `2223.50` | `139.8487` | 310,953.58 USD | 4,485,958.27 USD | `9 orders` | `+0.04%` | `-` |
| `ASK` | `2223.60` | `581.4809` | 1,292,980.93 USD | 5,778,939.19 USD | `10 orders` | `+0.04%` | `-` |
| `ASK` | `2223.70` | `139.9833` | 311,280.86 USD | 6,090,220.06 USD | `8 orders` | `+0.05%` | `-` |
| `ASK` | `2223.80` | `376.4334` | 837,112.59 USD | 6,927,332.65 USD | `13 orders` | `+0.05%` | `-` |
| `ASK` | `2223.90` | `201.0741` | 447,168.69 USD | 7,374,501.34 USD | `12 orders` | `+0.06%` | `-` |
| `ASK` | `2224.00` | `283.5810` | 630,684.14 USD | 8,005,185.49 USD | `7 orders` | `+0.06%` | `-` |
| `ASK` | `2224.10` | `252.0105` | 560,496.55 USD | 8,565,682.04 USD | `15 orders` | `+0.07%` | `-` |
| `ASK` | `2224.20` | `52.7821` | 117,397.95 USD | 8,683,079.99 USD | `7 orders` | `+0.07%` | `-` |
| `ASK` | `2224.30` | `481.4301` | 1,070,844.97 USD | 9,753,924.96 USD | `15 orders` | `+0.07%` | `-` |
| `ASK` | `2224.40` | `580.8191` | 1,291,974.01 USD | 11,045,898.97 USD | `9 orders` | `+0.08%` | `-` |
| `ASK` | `2224.50` | `244.7193` | 544,378.08 USD | 11,590,277.05 USD | `13 orders` | `+0.08%` | `-` |
| `ASK` | `2224.60` | `73.3965` | 163,277.85 USD | 11,753,554.90 USD | `10 orders` | `+0.09%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:50:34 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1786.06` | `30,282.40` | 54,086,279.26 USD | `AT_RISK_LIQ` | `0xde8d9e530b` | `2026-10-30 15:50:34 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1787.90` | `15,927.59` | 28,476,918.53 USD | `AT_RISK_LIQ` | `0x60468ba274` | `2026-10-30 15:50:34 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 15:50:34 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `10,000.00` | 19,261,000.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-30 15:50:34 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1930.52` | `8,092.45` | 15,622,633.76 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 15:50:34 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2121.80` | `30,641.99` | 65,016,272.46 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 15:50:34 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2129.08` | `26,025.05` | 55,409,441.07 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 15:50:34 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2175.00` | `3,533.33` | 7,684,999.71 USD | `TRIGGER_STOP` | `0x469e9a7f62` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2185.30` | `2,106.10` | 4,602,463.83 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2190.80` | `509.00` | 1,115,119.39 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2191.10` | `500.00` | 1,095,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2193.90` | `4,250.16` | 9,324,427.12 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 15:50:34 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2195.00` | `839.60` | 1,842,926.39 USD | `TRIGGER_STOP` | `0x28280399d9` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2195.50` | `1,449.07` | 3,181,431.65 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2199.90` | `346.35` | 761,925.47 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc9186f2969` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2200.00` | `361.24` | 794,719.86 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2201.10` | `500.00` | 1,100,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2203.10` | `500.00` | 1,101,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xf929122994` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2203.50` | `509.69` | 1,123,110.73 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2204.40` | `977.94` | 2,155,773.80 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2207.00` | `2,192.65` | 4,839,180.09 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2207.90` | `430.01` | 949,423.94 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2209.40` | `509.59` | 1,125,892.56 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2209.70` | `1,812.46` | 4,004,985.57 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2211.10` | `722.96` | 1,598,543.93 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2211.10` | `500.00` | 1,105,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2212.50` | `1,357.63` | 3,003,760.14 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2213.30` | `717.83` | 1,588,774.69 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2213.40` | `476.50` | 1,054,689.53 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2214.00` | `355.02` | 786,011.40 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2214.30` | `904.35` | 2,002,506.63 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2215.60` | `344.01` | 762,188.11 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2216.60` | `677.58` | 1,501,916.73 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2217.00` | `1,117.40` | 2,477,286.22 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2217.40` | `355.21` | 787,643.76 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2218.00` | `451.40` | 1,001,208.08 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 15:50:34 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2219.00` | `439.90` | 976,147.64 USD | `TRIGGER_STOP` | `0x369fd6445f` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2221.00` | `566.99` | 1,259,292.56 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x9362ca4dfd` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2224.20` | `349.22` | 776,738.68 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2224.60` | `450.11` | 1,001,304.70 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2226.20` | `674.65` | 1,501,910.28 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2228.50` | `484.93` | 1,080,662.05 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2228.60` | `898.54` | 2,002,482.68 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2230.40` | `476.39` | 1,062,540.26 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2231.40` | `1,346.13` | 3,003,745.56 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2232.30` | `1,118.70` | 2,497,272.89 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2232.80` | `349.62` | 780,633.32 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2233.00` | `731.71` | 1,633,917.81 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2233.10` | `1,793.48` | 4,005,019.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2233.80` | `344.01` | 768,449.09 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2233.90` | `509.53` | 1,138,241.30 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2239.30` | `509.66` | 1,141,277.16 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2239.70` | `964.55` | 2,160,310.25 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2241.60` | `430.01` | 963,915.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x90e56dc997` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2242.30` | `2,190.11` | 4,910,890.16 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2243.90` | `354.17` | 794,719.82 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2248.20` | `1,389.73` | 3,124,401.10 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2254.00` | `4,250.16` | 9,579,861.77 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2257.60` | `509.04` | 1,149,201.93 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 15:50:34 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2259.50` | `2,098.65` | 4,741,894.25 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 15:50:34 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2300.00` | `4,002.10` | 9,204,832.99 USD | `TRIGGER_STOP` | `0xfb941d2344` | `2026-10-30 15:50:34 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2478.67` | `22,046.99` | 54,647,122.27 USD | `AT_RISK_LIQ` | `0x8added25f8` | `2026-10-30 15:50:34 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `3,002.39` | 7,547,704.95 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-30 15:50:34 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2623.84` | `10,000.00` | 26,238,434.09 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-30 15:50:34 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2657.69` | `9,700.00` | 25,779,622.97 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-30 15:50:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 228,372,854.66 USD | `102,676.40` | `2322.74` | `2224.20` | `3731.42` | 10,118,058.48 USD | `+4.43%` | `5X Cross` |
| `5` | `0xb83d...6e36` | `SHORT` | 105,499,006.76 USD | `47,430.21` | `2375.30` | `2224.20` | `4544.40` | 7,162,269.31 USD | `+6.79%` | `5X Cross` |
| `9` | `0x77dd...e0e9` | `LONG` | 68,160,046.34 USD | `30,641.99` | `2610.31` | `2224.20` | `2121.82` | -11,825,128.70 USD | `-17.35%` | `10X Cross` |
| `10` | `0xde8d...9524` | `LONG` | 67,357,150.11 USD | `30,282.40` | `2134.45` | `2224.20` | `1786.08` | 2,720,819.53 USD | `+4.04%` | `20X Cross` |
| `15` | `0x0392...d7d9` | `LONG` | 57,884,918.66 USD | `26,025.05` | `2518.71` | `2224.20` | `2129.10` | -7,664,803.43 USD | `-13.24%` | `9X Cross` |
| `22` | `0x8add...7d2c` | `SHORT` | 49,036,912.49 USD | `22,046.99` | `2271.09` | `2224.20` | `2483.74` | 1,033,984.81 USD | `+2.11%` | `25X Cross` |
| `25` | `0x15a4...dfdb` | `SHORT` | 44,484,000.00 USD | `20,000.00` | `2228.11` | `2224.20` | `3187.78` | 78,327.68 USD | `+0.18%` | `20X Cross` |
| `26` | `0xdf95...7d72` | `SHORT` | 43,855,118.68 USD | `19,716.37` | `2402.53` | `2224.20` | `4239.86` | 3,514,138.41 USD | `+8.01%` | `25X Cross` |
| `33` | `0x6046...b21d` | `LONG` | 35,427,737.77 USD | `15,927.59` | `2410.19` | `2224.20` | `1796.75` | -2,960,881.88 USD | `-8.36%` | `6X Cross` |
| `35` | `0xefe4...194b` | `SHORT` | 33,605,198.92 USD | `15,108.89` | `2250.33` | `2224.20` | `2894.29` | 394,817.83 USD | `+1.17%` | `20X Cross` |
| `37` | `0xb695...a92d` | `SHORT` | 32,911,624.04 USD | `14,795.73` | `2557.74` | `2224.20` | `3793.83` | 4,932,090.08 USD | `+14.99%` | `20X Cross` |
| `38` | `0xeced...6210` | `SHORT` | 32,666,638.45 USD | `14,687.58` | `2522.09` | `2224.20` | `3649.40` | 4,376,879.09 USD | `+13.40%` | `20X Cross` |
| `40` | `0x45d2...4029` | `SHORT` | 31,030,380.00 USD | `13,950.00` | `2443.60` | `2224.20` | `5366.68` | 3,057,902.46 USD | `+9.85%` | `20X Cross` |
| `42` | `0xa61c...66b9` | `LONG` | 28,668,067.20 USD | `12,888.00` | `2369.69` | `2224.20` | `1495.24` | -1,872,587.34 USD | `-6.53%` | `10X Cross` |
| `44` | `0xbd1c...ff0e` | `LONG` | 26,695,200.00 USD | `12,000.00` | `2419.91` | `2224.20` | `1519.96` | -2,343,832.39 USD | `-8.78%` | `20X Cross` |
| `45` | `0x2371...0883` | `LONG` | 26,690,400.00 USD | `12,000.00` | `2421.77` | `2224.20` | `1279.06` | -2,370,894.85 USD | `-8.88%` | `20X Cross` |
| `53` | `0x6c93...59a4` | `LONG` | 24,468,400.00 USD | `11,000.00` | `2441.15` | `2224.20` | `1601.99` | -2,384,272.73 USD | `-9.74%` | `20X Cross` |
| `54` | `0x09dc...c094` | `LONG` | 24,467,300.00 USD | `11,000.00` | `2465.31` | `2224.20` | `1637.02` | -2,651,123.04 USD | `-10.84%` | `20X Cross` |
| `55` | `0xa9de...e049` | `LONG` | 24,466,200.00 USD | `11,000.00` | `2481.81` | `2224.20` | `1643.70` | -2,833,779.46 USD | `-11.58%` | `20X Cross` |
| `56` | `0x0c5d...36b3` | `LONG` | 24,466,200.00 USD | `11,000.00` | `2482.20` | `2224.20` | `1644.03` | -2,838,053.24 USD | `-11.60%` | `20X Cross` |
| `69` | `0xa2ce...3126` | `LONG` | 22,276,528.76 USD | `10,016.88` | `2162.83` | `2224.20` | `1566.77` | 611,726.71 USD | `+2.75%` | `10X Cross` |
| `70` | `0xb37f...66ca` | `SHORT` | 22,244,000.00 USD | `10,000.00` | `2290.69` | `2224.20` | `2623.86` | 662,991.85 USD | `+2.98%` | `25X Cross` |
| `71` | `0x6646...6de5` | `LONG` | 22,243,000.00 USD | `10,000.00` | `1765.80` | `2224.20` | `1720.45` | 4,584,942.55 USD | `+20.61%` | `25X Cross` |
| `72` | `0xec7f...df39` | `LONG` | 22,227,000.00 USD | `10,000.00` | `2719.35` | `2224.20` | `1720.55` | -4,966,548.52 USD | `-22.34%` | `20X Cross` |
| `74` | `0xecb6...2b00` | `SHORT` | 22,125,105.61 USD | `9,947.44` | `2239.36` | `2224.20` | `5221.79` | 150,809.43 USD | `+0.68%` | `15X Cross` |
| `75` | `0x939f...04d2` | `LONG` | 21,855,036.56 USD | `9,823.81` | `2427.28` | `2224.20` | `1714.62` | -1,990,114.04 USD | `-9.11%` | `25X Cross` |
| `77` | `0xaeaa...2416` | `SHORT` | 21,574,740.00 USD | `9,700.00` | `2311.92` | `2224.20` | `2657.71` | 850,942.40 USD | `+3.94%` | `25X Cross` |
| `85` | `0xf517...c032` | `SHORT` | 20,745,526.49 USD | `9,326.35` | `2202.91` | `2224.20` | `3122.17` | -200,388.28 USD | `-0.97%` | `25X Cross` |
| `86` | `0xca49...53c8` | `SHORT` | 20,424,189.22 USD | `9,181.89` | `2549.39` | `2224.20` | `3912.43` | 2,984,088.17 USD | `+14.61%` | `25X Cross` |
| `88` | `0xba5d...a352` | `SHORT` | 20,139,083.79 USD | `9,054.12` | `2493.89` | `2224.20` | `2767.04` | 2,440,923.47 USD | `+12.12%` | `20X Cross` |
| `89` | `0xea00...a918` | `LONG` | 20,030,812.37 USD | `9,003.83` | `2003.01` | `2224.20` | `1441.93` | 1,996,033.50 USD | `+9.96%` | `5X Cross` |
| `114` | `0x9eec...daab` | `LONG` | 18,000,850.45 USD | `8,092.45` | `1658.44` | `2224.20` | `1931.35` | 4,579,985.92 USD | `+25.44%` | `15X Cross` |
| `115` | `0x5f91...65aa` | `LONG` | 17,714,987.65 USD | `7,964.66` | `1626.99` | `2224.20` | `1843.87` | 4,756,544.59 USD | `+26.85%` | `16X Cross` |
| `125` | `0xec0b...b078` | `LONG` | 15,588,147.87 USD | `7,007.80` | `2065.97` | `2224.20` | `1059.07` | 1,110,218.28 USD | `+7.12%` | `25X Cross` |
| `130` | `0xf02d...5eb3` | `LONG` | 15,250,454.15 USD | `6,855.99` | `2383.33` | `2224.20` | `1125.10` | -1,089,634.62 USD | `-7.14%` | `20X Cross` |
| `131` | `0xcf53...ee11` | `SHORT` | 15,131,812.74 USD | `6,803.63` | `1862.69` | `2224.20` | `4194.76` | -2,458,707.35 USD | `-16.25%` | `7X Cross` |
| `136` | `0x4ff9...38d3` | `LONG` | 14,599,868.33 USD | `6,564.10` | `2447.40` | `2224.20` | `1669.64` | -1,465,154.42 USD | `-10.04%` | `3X Isolated` |
| `138` | `0x1ee7...edf5` | `LONG` | 14,457,300.00 USD | `6,500.00` | `2301.55` | `2224.20` | `2068.86` | -502,793.66 USD | `-3.48%` | `25X Cross` |
| `139` | `0xf78c...c581` | `LONG` | 14,457,142.64 USD | `6,500.22` | `2521.53` | `2224.20` | `1913.13` | -1,933,398.31 USD | `-13.37%` | `20X Cross` |
| `141` | `0x4e23...20c3` | `LONG` | 14,158,993.12 USD | `6,365.31` | `2228.10` | `2224.20` | `186.37` | -23,584.32 USD | `-0.17%` | `20X Cross` |
| `145` | `0x799f...5f4c` | `LONG` | 14,037,973.30 USD | `6,310.90` | `2390.33` | `2224.20` | `1881.49` | -1,047,191.32 USD | `-7.46%` | `20X Cross` |
| `149` | `0x08bf...7872` | `SHORT` | 13,844,771.04 USD | `6,224.05` | `2258.00` | `2224.20` | `2584.93` | 209,145.07 USD | `+1.51%` | `20X Cross` |
| `151` | `0xec4a...cf62` | `LONG` | 13,717,054.22 USD | `6,166.63` | `2225.41` | `2224.20` | `1969.92` | -6,265.22 USD | `-0.05%` | `25X Cross` |
| `154` | `0xd9e7...4aff` | `LONG` | 13,345,200.00 USD | `6,000.00` | `2480.18` | `2224.20` | `1407.42` | -1,535,924.33 USD | `-11.51%` | `20X Cross` |
| `155` | `0x524e...0de0` | `LONG` | 13,345,200.00 USD | `6,000.00` | `2246.48` | `2224.20` | `2002.83` | -133,685.04 USD | `-1.00%` | `10X Cross` |
| `157` | `0xc179...e0c8` | `LONG` | 13,022,677.27 USD | `5,854.73` | `2294.94` | `2224.20` | `1209.62` | -413,594.90 USD | `-3.18%` | `10X Cross` |
| `162` | `0x0c4a...1b19` | `LONG` | 12,583,528.76 USD | `5,660.10` | `2373.06` | `2224.20` | `2081.46` | -848,229.37 USD | `-6.74%` | `25X Isolated` |
| `169` | `0x7fda...17d1` | `LONG` | 11,823,841.85 USD | `5,315.76` | `2211.05` | `2224.20` | `0.000000` | 70,399.61 USD | `+0.60%` | `25X Cross` |
| `186` | `0x45ab...6cbc` | `LONG` | 10,945,696.22 USD | `4,920.96` | `2727.66` | `2224.20` | `1376.27` | -2,477,047.58 USD | `-22.63%` | `7X Cross` |
| `190` | `0x64b7...9da9` | `LONG` | 10,803,553.12 USD | `4,856.84` | `2604.61` | `2224.20` | `586.55` | -1,846,661.30 USD | `-17.09%` | `25X Cross` |
| `196` | `0xfb18...eb17` | `SHORT` | 10,606,296.44 USD | `4,768.16` | `2315.53` | `2224.20` | `2623.94` | 434,533.26 USD | `+4.10%` | `25X Cross` |
| `198` | `0x5559...d43b` | `SHORT` | 10,578,129.05 USD | `4,755.93` | `2262.69` | `2224.20` | `2735.81` | 183,076.83 USD | `+1.73%` | `25X Cross` |
| `211` | `0xe091...6705` | `SHORT` | 10,008,900.44 USD | `4,500.00` | `2467.33` | `2224.20` | `2463.05` | 1,094,108.06 USD | `+10.93%` | `20X Cross` |
| `212` | `0x418a...8888` | `SHORT` | 10,008,450.00 USD | `4,500.00` | `2494.55` | `2224.20` | `2998.56` | 1,217,034.41 USD | `+12.16%` | `25X Cross` |
| `219` | `0xb829...3a81` | `LONG` | 9,775,600.54 USD | `4,394.91` | `2398.60` | `2224.20` | `1451.55` | -766,041.41 USD | `-7.84%` | `20X Cross` |
| `236` | `0x28bb...fca6` | `SHORT` | 9,363,865.83 USD | `4,209.61` | `1896.10` | `2224.20` | `3033.87` | -1,381,983.26 USD | `-14.76%` | `20X Cross` |
| `238` | `0x6ea4...0ea7` | `SHORT` | 9,304,113.67 USD | `4,184.01` | `2602.13` | `2224.20` | `3424.99` | 1,583,233.00 USD | `+17.02%` | `20X Cross` |
| `252` | `0x5e9e...35ee` | `SHORT` | 8,915,208.41 USD | `4,007.56` | `1796.39` | `2224.20` | `2585.48` | -1,716,058.32 USD | `-19.25%` | `20X Cross` |
| `253` | `0xfb94...0ddf` | `SHORT` | 8,901,873.92 USD | `4,002.10` | `2382.44` | `2224.20` | `5104.38` | 632,910.23 USD | `+7.11%` | `20X Cross` |
| `254` | `0x8cc9...2b6a` | `SHORT` | 8,898,000.00 USD | `4,000.00` | `1791.18` | `2224.20` | `3521.02` | -1,733,253.33 USD | `-19.48%` | `25X Cross` |
| `255` | `0x3dc9...54b0` | `SHORT` | 8,895,710.97 USD | `3,999.69` | `2480.32` | `2224.20` | `6620.40` | 1,024,825.58 USD | `+11.52%` | `20X Cross` |
| `272` | `0x4b67...f4e7` | `LONG` | 8,498,698.64 USD | `3,820.84` | `2591.51` | `2224.20` | `1349.37` | -1,403,074.90 USD | `-16.51%` | `20X Cross` |
| `279` | `0x12d2...f97f` | `LONG` | 8,357,651.81 USD | `3,757.26` | `2446.50` | `2224.20` | `1804.13` | -834,514.58 USD | `-9.99%` | `20X Cross` |
| `296` | `0x8ae4...3d60` | `LONG` | 7,913,788.84 USD | `3,558.20` | `2482.21` | `2224.20` | `539.99` | -918,409.20 USD | `-11.61%` | `10X Cross` |
| `300` | `0x469e...58a5` | `SHORT` | 7,858,839.70 USD | `3,533.33` | `2203.63` | `2224.20` | `3074.91` | -72,676.61 USD | `-0.92%` | `25X Cross` |
| `308` | `0x218a...7da2` | `SHORT` | 7,707,351.20 USD | `3,465.07` | `2208.16` | `2224.20` | `3101.70` | -55,921.94 USD | `-0.73%` | `10X Cross` |
| `337` | `0x9c2a...f6a8` | `SHORT` | 6,677,612.71 USD | `3,002.39` | `2515.77` | `2224.20` | `2587.65` | 875,725.19 USD | `+13.11%` | `20X Cross` |
| `338` | `0x4a20...3c26` | `LONG` | 6,673,200.00 USD | `3,000.00` | `2428.72` | `2224.20` | `667.14` | -612,960.28 USD | `-9.19%` | `20X Cross` |
| `339` | `0x007d...67a0` | `LONG` | 6,673,200.00 USD | `3,000.00` | `2400.00` | `2224.20` | `1470.98` | -526,800.00 USD | `-7.89%` | `25X Cross` |
| `340` | `0xb823...9763` | `SHORT` | 6,672,900.00 USD | `3,000.00` | `2229.66` | `2224.20` | `3233.38` | 16,096.68 USD | `+0.24%` | `25X Cross` |
| `394` | `0x8328...f54a` | `SHORT` | 5,730,800.18 USD | `2,576.45` | `2292.01` | `2224.20` | `3279.22` | 174,471.11 USD | `+3.04%` | `25X Cross` |
| `397` | `0xed48...7c9b` | `SHORT` | 5,674,734.68 USD | `2,551.13` | `2460.02` | `2224.20` | `3229.17` | 601,111.73 USD | `+10.59%` | `20X Cross` |
| `399` | `0x970c...2a93` | `SHORT` | 5,560,500.00 USD | `2,500.00` | `2229.57` | `2224.20` | `5082.38` | 13,444.49 USD | `+0.24%` | `20X Cross` |
| `400` | `0x1c98...7fc7` | `LONG` | 5,560,260.01 USD | `2,500.00` | `2452.60` | `2224.20` | `1916.62` | -571,261.56 USD | `-10.27%` | `10X Cross` |
| `414` | `0xa445...329d` | `LONG` | 5,352,208.47 USD | `2,406.14` | `2354.86` | `2224.20` | `1781.74` | -313,906.81 USD | `-5.86%` | `25X Cross` |
| `416` | `0xfbe2...c8ea` | `SHORT` | 5,305,652.23 USD | `2,385.21` | `2041.57` | `2224.20` | `2622.49` | -436,085.57 USD | `-8.22%` | `20X Cross` |
| `417` | `0x6749...ce07` | `SHORT` | 5,304,958.66 USD | `2,384.89` | `2220.92` | `2224.20` | `3631.76` | -8,295.63 USD | `-0.16%` | `20X Cross` |
| `418` | `0x645b...87b8` | `SHORT` | 5,293,779.73 USD | `2,379.98` | `2421.64` | `2224.20` | `11559.17` | 469,667.23 USD | `+8.87%` | `10X Cross` |
| `427` | `0x77ee...2902` | `SHORT` | 5,094,726.30 USD | `2,290.69` | `2476.53` | `2224.20` | `6148.64` | 578,245.94 USD | `+11.35%` | `25X Cross` |
| `440` | `0x0622...8088` | `SHORT` | 4,922,582.98 USD | `2,213.19` | `2228.81` | `2224.20` | `6652.65` | 10,216.73 USD | `+0.21%` | `5X Cross` |
| `451` | `0xd507...c948` | `SHORT` | 4,831,396.58 USD | `2,172.00` | `2387.49` | `2224.20` | `2600.23` | 354,244.45 USD | `+7.33%` | `5X Isolated` |
| `459` | `0x023a...2355` | `LONG` | 4,766,493.26 USD | `2,142.82` | `2328.93` | `2224.20` | `0.000000` | -224,010.59 USD | `-4.70%` | `25X Cross` |
| `461` | `0x382b...3e39` | `SHORT` | 4,736,739.38 USD | `2,129.54` | `2296.66` | `2224.20` | `4549.61` | 154,097.83 USD | `+3.25%` | `25X Cross` |
| `495` | `0xe02e...d78b` | `LONG` | 4,448,800.00 USD | `2,000.00` | `2228.11` | `2224.20` | `2171.57` | -7,423.47 USD | `-0.17%` | `25X Cross` |
| `496` | `0x3453...b323` | `SHORT` | 4,448,673.80 USD | `2,000.12` | `2322.47` | `2224.20` | `2402.10` | 196,562.04 USD | `+4.42%` | `25X Cross` |
| `502` | `0xf3dc...1672` | `SHORT` | 4,404,521.57 USD | `1,980.36` | `2240.44` | `2224.20` | `2794.30` | 32,365.99 USD | `+0.73%` | `20X Cross` |
| `505` | `0x7a6d...f79c` | `SHORT` | 4,384,875.96 USD | `1,971.44` | `2418.41` | `2224.20` | `2544.66` | 382,885.22 USD | `+8.73%` | `25X Cross` |
| `507` | `0xac48...3201` | `SHORT` | 4,369,150.64 USD | `1,964.37` | `2272.04` | `2224.20` | `3080.09` | 93,991.66 USD | `+2.15%` | `20X Cross` |
| `520` | `0x8376...9a1e` | `SHORT` | 4,249,516.25 USD | `1,910.50` | `2477.72` | `2224.20` | `3188.59` | 484,171.92 USD | `+11.39%` | `20X Cross` |
| `524` | `0x739c...cfb2` | `SHORT` | 4,225,790.00 USD | `1,900.00` | `2418.12` | `2224.20` | `2432.33` | 368,656.38 USD | `+8.72%` | `25X Cross` |
| `547` | `0x7265...91a5` | `LONG` | 4,008,618.85 USD | `1,801.87` | `2533.96` | `2224.20` | `1987.09` | -557,247.60 USD | `-13.90%` | `20X Cross` |
| `548` | `0xc619...10f5` | `LONG` | 4,004,100.00 USD | `1,800.00` | `2313.55` | `2224.20` | `1817.94` | -160,295.83 USD | `-4.00%` | `25X Cross` |
| `549` | `0xbb34...1696` | `LONG` | 4,003,560.00 USD | `1,800.00` | `2313.95` | `2224.20` | `1986.76` | -161,558.23 USD | `-4.04%` | `25X Cross` |
| `566` | `0x91a9...3f70` | `SHORT` | 3,931,052.27 USD | `1,767.48` | `2156.23` | `2224.20` | `3668.18` | -119,948.19 USD | `-3.05%` | `4X Cross` |
| `571` | `0xbcd4...0dd2` | `SHORT` | 3,887,018.30 USD | `1,747.52` | `2233.24` | `2224.20` | `2748.58` | 15,637.92 USD | `+0.40%` | `25X Cross` |
| `592` | `0xfeec...4e9c` | `SHORT` | 3,763,259.49 USD | `1,691.81` | `2566.49` | `2224.20` | `2509.65` | 578,765.02 USD | `+15.38%` | `10X Cross` |
| `618` | `0xeee0...0b53` | `LONG` | 3,641,454.69 USD | `1,637.12` | `2468.64` | `2224.20` | `177.70` | -400,021.37 USD | `-10.99%` | `7X Cross` |
| `620` | `0x27b8...12fc` | `LONG` | 3,621,101.91 USD | `1,628.12` | `2468.73` | `2224.20` | `659.28` | -398,292.72 USD | `-11.00%` | `10X Cross` |
| `622` | `0x982b...4606` | `LONG` | 3,619,180.45 USD | `1,626.82` | `2575.24` | `2224.20` | `1547.37` | -570,272.63 USD | `-15.76%` | `5X Isolated` |
| `629` | `0x73d7...8be1` | `LONG` | 3,562,620.15 USD | `1,601.47` | `2410.40` | `2224.20` | `1771.98` | -297,558.77 USD | `-8.35%` | `25X Cross` |
| `630` | `0xad54...6203` | `LONG` | 3,553,850.80 USD | `1,597.45` | `2591.98` | `2224.20` | `2043.77` | -586,727.25 USD | `-16.51%` | `10X Isolated` |
| `636` | `0x880a...311c` | `LONG` | 3,510,834.45 USD | `1,578.40` | `2209.72` | `2224.20` | `0.000000` | 23,010.60 USD | `+0.66%` | `9X Cross` |
| `640` | `0x936c...bb0f` | `LONG` | 3,489,135.96 USD | `1,568.64` | `2232.92` | `2224.20` | `0.000000` | -13,533.66 USD | `-0.39%` | `20X Cross` |
| `653` | `0xe170...9300` | `SHORT` | 3,411,048.30 USD | `1,533.40` | `2076.39` | `2224.20` | `3107.16` | -227,098.80 USD | `-6.66%` | `25X Cross` |
| `657` | `0x4b86...df9d` | `SHORT` | 3,390,442.80 USD | `1,524.00` | `2287.40` | `2224.20` | `2759.58` | 95,554.80 USD | `+2.82%` | `9X Isolated` |
| `664` | `0x2e2b...2fab` | `LONG` | 3,352,557.19 USD | `1,507.38` | `2245.53` | `2224.20` | `1263.45` | -32,315.91 USD | `-0.96%` | `25X Cross` |
| `669` | `0x251f...6e5d` | `LONG` | 3,336,600.00 USD | `1,500.00` | `2346.68` | `2224.20` | `1912.47` | -183,430.49 USD | `-5.50%` | `20X Cross` |
| `670` | `0xde6b...3361` | `LONG` | 3,336,150.00 USD | `1,500.00` | `2216.98` | `2224.20` | `2168.50` | 10,669.26 USD | `+0.32%` | `25X Cross` |
| `689` | `0xb885...3c54` | `LONG` | 3,225,674.89 USD | `1,450.00` | `2274.34` | `2224.20` | `41.80` | -72,133.24 USD | `-2.24%` | `20X Cross` |
| `691` | `0xef70...a84c` | `SHORT` | 3,209,238.42 USD | `1,442.74` | `2424.73` | `2224.20` | `3242.72` | 289,032.41 USD | `+9.01%` | `25X Cross` |
| `701` | `0xbadb...9ee6` | `LONG` | 3,177,227.55 USD | `1,428.16` | `1936.00` | `2224.20` | `1075.57` | 412,305.91 USD | `+12.98%` | `20X Cross` |
| `742` | `0x020c...5872` | `LONG` | 3,058,825.00 USD | `1,375.00` | `2226.32` | `2224.20` | `2141.03` | -2,375.95 USD | `-0.08%` | `25X Cross` |
| `756` | `0x53f8...ceff` | `LONG` | 2,999,542.03 USD | `1,348.65` | `2276.73` | `2224.20` | `0.000000` | -70,982.44 USD | `-2.37%` | `20X Cross` |
| `774` | `0xa0fb...96be` | `LONG` | 2,928,857.88 USD | `1,317.09` | `2277.10` | `2224.20` | `1519.87` | -70,304.40 USD | `-2.40%` | `3X Cross` |
| `775` | `0x0dd5...f6ee` | `LONG` | 2,925,368.82 USD | `1,314.95` | `2288.01` | `2224.20` | `1559.42` | -83,256.66 USD | `-2.85%` | `5X Cross` |
| `779` | `0x4487...c92d` | `LONG` | 2,915,488.83 USD | `1,310.69` | `2232.11` | `2224.20` | `1562.09` | -10,106.39 USD | `-0.35%` | `10X Cross` |
| `804` | `0x1f16...6d07` | `LONG` | 2,816,090.40 USD | `1,266.00` | `2261.43` | `2224.20` | `1380.67` | -46,880.83 USD | `-1.66%` | `7X Cross` |
| `810` | `0xc435...c905` | `SHORT` | 2,776,425.60 USD | `1,248.00` | `2704.38` | `2224.20` | `3794.87` | 598,644.75 USD | `+21.56%` | `20X Cross` |
| `818` | `0x6859...7e1e` | `SHORT` | 2,751,924.91 USD | `1,237.15` | `2200.39` | `2224.20` | `4890.03` | -29,697.76 USD | `-1.08%` | `25X Cross` |
| `825` | `0x7277...0b98` | `SHORT` | 2,712,553.26 USD | `1,219.45` | `2206.05` | `2224.20` | `3413.42` | -22,365.45 USD | `-0.82%` | `20X Cross` |
| `826` | `0x7178...0854` | `LONG` | 2,710,845.77 USD | `1,218.63` | `2461.81` | `2224.20` | `1201.09` | -289,200.63 USD | `-10.67%` | `10X Cross` |
| `839` | `0xaaa1...ab8c` | `SHORT` | 2,669,040.00 USD | `1,200.00` | `2276.29` | `2224.20` | `2365.20` | 62,517.58 USD | `+2.34%` | `25X Isolated` |
| `854` | `0x07fd...689d` | `LONG` | 2,617,434.57 USD | `1,176.69` | `2416.34` | `2224.20` | `0.000000` | -225,865.36 USD | `-8.63%` | `25X Cross` |
| `890` | `0xfc27...9d9d` | `LONG` | 2,484,361.62 USD | `1,116.87` | `2237.33` | `2224.20` | `0.000000` | -14,447.12 USD | `-0.58%` | `25X Cross` |
| `911` | `0x2f80...f203` | `SHORT` | 2,421,913.90 USD | `1,088.94` | `1984.00` | `2224.20` | `2957.77` | -261,446.71 USD | `-10.80%` | `20X Cross` |
| `918` | `0x8eb7...b90f` | `LONG` | 2,397,215.30 USD | `1,077.74` | `2396.38` | `2224.20` | `1880.90` | -185,462.74 USD | `-7.74%` | `5X Isolated` |
| `921` | `0x2b61...2f6c` | `SHORT` | 2,394,459.83 USD | `1,076.60` | `2681.75` | `2224.20` | `6318.72` | 492,712.91 USD | `+20.58%` | `10X Cross` |
| `951` | `0x30af...393e` | `SHORT` | 2,315,758.97 USD | `1,041.16` | `2252.26` | `2224.20` | `2296.89` | 29,223.36 USD | `+1.26%` | `25X Cross` |
| `966` | `0x2577...4897` | `LONG` | 2,285,714.26 USD | `1,027.61` | `2231.81` | `2224.20` | `0.000000` | -7,726.55 USD | `-0.34%` | `15X Cross` |
| `967` | `0x1b2a...f7a6` | `LONG` | 2,280,726.04 USD | `1,025.37` | `2737.51` | `2224.20` | `882.04` | -526,233.90 USD | `-23.07%` | `10X Cross` |
| `977` | `0x001a...fef6` | `SHORT` | 2,240,693.73 USD | `1,007.33` | `2022.19` | `2224.20` | `3093.53` | -203,685.77 USD | `-9.09%` | `10X Cross` |
| `979` | `0x02aa...1806` | `SHORT` | 2,240,193.46 USD | `1,007.10` | `2654.68` | `2224.20` | `3612.68` | 433,338.64 USD | `+19.34%` | `20X Cross` |
| `980` | `0xdb3a...cf3b` | `LONG` | 2,231,551.67 USD | `1,003.22` | `2705.01` | `2224.20` | `0.000000` | -482,155.23 USD | `-21.61%` | `4X Cross` |
| `983` | `0xf929...d1f9` | `SHORT` | 2,224,700.00 USD | `1,000.00` | `2423.37` | `2224.20` | `2926.11` | 198,670.17 USD | `+8.93%` | `25X Cross` |
| `984` | `0x5272...fcd9` | `SHORT` | 2,224,400.00 USD | `1,000.00` | `2241.82` | `2224.20` | `2830.73` | 17,424.49 USD | `+0.78%` | `5X Cross` |
| `985` | `0x8c02...b73f` | `SHORT` | 2,224,100.00 USD | `1,000.00` | `2250.37` | `2224.20` | `8098.36` | 26,271.47 USD | `+1.18%` | `20X Cross` |
| `986` | `0x6463...42f5` | `SHORT` | 2,222,100.00 USD | `1,000.00` | `2223.43` | `2224.20` | `3704.69` | 1,334.95 USD | `+0.06%` | `5X Cross` |
| `987` | `0xd7b8...9f55` | `LONG` | 2,221,975.80 USD | `999.00` | `2195.00` | `2224.20` | `0.000000` | 29,170.80 USD | `+1.31%` | `15X Cross` |
| `1000` | `0x6f11...0389` | `SHORT` | 2,177,491.80 USD | `979.00` | `2333.39` | `2224.20` | `3051.82` | 106,898.01 USD | `+4.91%` | `25X Cross` |
| `1012` | `0xb002...ed8a` | `SHORT` | 2,141,520.45 USD | `962.78` | `2299.66` | `2224.20` | `4197.86` | 72,557.46 USD | `+3.39%` | `25X Cross` |
| `1030` | `0xb1ec...e86a` | `SHORT` | 2,076,505.17 USD | `933.64` | `2272.72` | `2224.20` | `12693.54` | 45,401.79 USD | `+2.19%` | `25X Cross` |
| `1044` | `0xb812...b5e0` | `LONG` | 2,059,477.15 USD | `925.90` | `2263.21` | `2224.20` | `1163.87` | -36,030.84 USD | `-1.75%` | `25X Cross` |
| `1062` | `0xede2...f971` | `LONG` | 2,034,070.57 USD | `914.31` | `2208.16` | `2224.20` | `1462.95` | 15,113.58 USD | `+0.74%` | `5X Cross` |
| `1063` | `0x9606...4e5d` | `SHORT` | 2,030,778.56 USD | `913.00` | `2478.70` | `2224.20` | `3785.28` | 232,275.04 USD | `+11.44%` | `20X Cross` |
| `1081` | `0x5f10...d49d` | `LONG` | 2,001,960.00 USD | `900.00` | `2249.83` | `2224.20` | `1825.32` | -22,893.47 USD | `-1.14%` | `25X Cross` |
| `1092` | `0x51f6...2b39` | `LONG` | 1,980,044.10 USD | `890.15` | `2226.49` | `2224.20` | `737.54` | -1,862.79 USD | `-0.09%` | `25X Cross` |
| `1169` | `0x2828...93a0` | `LONG` | 1,867,442.77 USD | `839.60` | `2242.41` | `2224.20` | `2192.50` | -15,289.42 USD | `-0.82%` | `25X Cross` |
| `1170` | `0xcd27...52a8` | `LONG` | 1,862,118.70 USD | `837.21` | `2553.56` | `2224.20` | `1403.18` | -275,746.07 USD | `-14.81%` | `2X Cross` |
| `1231` | `0x04a9...95aa` | `LONG` | 1,779,360.00 USD | `800.00` | `2595.13` | `2224.20` | `1876.08` | -296,746.74 USD | `-16.68%` | `5X Cross` |
| `1232` | `0x7737...bf66` | `SHORT` | 1,779,137.08 USD | `799.79` | `2494.83` | `2224.20` | `25038.67` | 216,208.95 USD | `+12.15%` | `15X Cross` |
| `1266` | `0x458d...ab3b` | `LONG` | 1,723,579.65 USD | `774.75` | `2740.41` | `2224.20` | `1886.93` | -399,549.53 USD | `-23.18%` | `3X Isolated` |
| `1328` | `0xaa53...9cb7` | `LONG` | 1,624,560.96 USD | `730.34` | `2389.70` | `2224.20` | `1941.58` | -120,728.68 USD | `-7.43%` | `20X Cross` |
| `1332` | `0x3fc5...c0c1` | `SHORT` | 1,623,424.41 USD | `729.92` | `2702.11` | `2224.20` | `4742.61` | 348,917.79 USD | `+21.49%` | `25X Cross` |
| `1343` | `0xa189...94d7` | `SHORT` | 1,601,521.29 USD | `719.98` | `2691.84` | `2224.20` | `2914.83` | 336,551.37 USD | `+21.01%` | `25X Cross` |
| `1360` | `0x2f93...4404` | `LONG` | 1,573,345.87 USD | `707.47` | `1700.45` | `2224.20` | `1368.57` | 370,319.49 USD | `+23.54%` | `4X Isolated` |
| `1374` | `0x5605...fe0f` | `SHORT` | 1,561,637.58 USD | `702.14` | `2566.90` | `2224.20` | `3084.91` | 240,695.07 USD | `+15.41%` | `20X Cross` |
| `1381` | `0x0deb...0bc5` | `LONG` | 1,557,080.00 USD | `700.00` | `2071.05` | `2224.20` | `1597.16` | 107,344.21 USD | `+6.89%` | `20X Cross` |
| `1383` | `0x26e6...6b28` | `LONG` | 1,556,940.00 USD | `700.00` | `1835.24` | `2224.20` | `2043.00` | 272,268.47 USD | `+17.49%` | `20X Cross` |
| `1384` | `0x9599...c60a` | `LONG` | 1,556,496.32 USD | `699.74` | `2233.08` | `2224.20` | `0.000000` | -6,074.51 USD | `-0.39%` | `20X Cross` |
| `1420` | `0x7b22...8a34` | `LONG` | 1,522,981.36 USD | `684.73` | `2228.49` | `2224.20` | `2181.56` | -2,942.21 USD | `-0.19%` | `25X Cross` |
| `1431` | `0x248e...6be2` | `SHORT` | 1,514,200.69 USD | `680.93` | `2282.89` | `2224.20` | `3387.80` | 40,284.97 USD | `+2.66%` | `20X Cross` |
| `1432` | `0xdbd1...29dd` | `SHORT` | 1,514,086.57 USD | `680.70` | `3030.57` | `2224.20` | `3780.11` | 548,834.55 USD | `+36.25%` | `6X Cross` |
| `1439` | `0x71e5...be04` | `LONG` | 1,507,402.03 USD | `677.67` | `2727.27` | `2224.20` | `1470.71` | -340,783.58 USD | `-22.61%` | `20X Cross` |
| `1443` | `0x0b23...f37b` | `LONG` | 1,501,267.50 USD | `675.00` | `2238.15` | `2224.20` | `596.36` | -9,489.14 USD | `-0.63%` | `5X Cross` |
| `1464` | `0x0cac...6170` | `SHORT` | 1,462,543.00 USD | `657.50` | `2146.55` | `2224.20` | `2839.17` | -51,180.80 USD | `-3.50%` | `20X Cross` |
| `1498` | `0xf00e...fe3d` | `SHORT` | 1,430,022.27 USD | `642.88` | `2333.21` | `2224.20` | `2483.38` | 69,955.70 USD | `+4.89%` | `20X Cross` |
| `1500` | `0xb15b...dbae` | `SHORT` | 1,429,559.80 USD | `642.64` | `2290.80` | `2224.20` | `2337.67` | 42,607.68 USD | `+2.98%` | `25X Cross` |
| `1506` | `0xffb2...5ed6` | `SHORT` | 1,425,193.52 USD | `640.77` | `2672.96` | `2224.20` | `2481.16` | 287,554.83 USD | `+20.18%` | `20X Cross` |
| `1517` | `0x8505...1821` | `SHORT` | 1,410,181.29 USD | `633.96` | `2239.93` | `2224.20` | `3896.08` | 9,850.31 USD | `+0.70%` | `20X Cross` |
| `1540` | `0xfce0...f4c0` | `SHORT` | 1,387,011.12 USD | `623.60` | `3129.61` | `2224.20` | `2807.77` | 564,615.46 USD | `+40.71%` | `20X Cross` |
| `1581` | `0x7050...5fff` | `SHORT` | 1,336,918.52 USD | `601.11` | `2245.52` | `2224.20` | `3281.47` | 12,881.59 USD | `+0.96%` | `25X Cross` |
| `1583` | `0xad02...eb65` | `LONG` | 1,336,019.57 USD | `600.62` | `2460.69` | `2224.20` | `1078.63` | -141,920.99 USD | `-10.62%` | `5X Cross` |
| `1584` | `0x24fb...ed0f` | `LONG` | 1,334,673.51 USD | `600.10` | `2199.85` | `2224.20` | `0.000000` | 14,550.08 USD | `+1.09%` | `15X Cross` |
| `1585` | `0x638f...f5f0` | `LONG` | 1,334,640.00 USD | `600.00` | `4011.50` | `2224.20` | `474.94` | -1,072,263.53 USD | `-80.34%` | `25X Cross` |
| `1656` | `0x9362...7d7c` | `SHORT` | 1,261,163.64 USD | `566.99` | `2226.19` | `2224.20` | `2518.63` | 1,072.18 USD | `+0.09%` | `20X Cross` |
| `1662` | `0xfb99...37f3` | `LONG` | 1,257,431.67 USD | `565.34` | `2362.35` | `2224.20` | `1258.63` | -78,104.68 USD | `-6.21%` | `3X Cross` |
| `1678` | `0x844b...7f42` | `SHORT` | 1,247,776.20 USD | `561.00` | `2026.17` | `2224.20` | `3029.25` | -111,092.79 USD | `-8.90%` | `25X Cross` |
| `1689` | `0xabe6...1d99` | `SHORT` | 1,236,775.30 USD | `556.00` | `2484.68` | `2224.20` | `3131.62` | 144,720.59 USD | `+11.70%` | `20X Cross` |
| `1693` | `0x2a76...9a53` | `LONG` | 1,234,442.22 USD | `555.03` | `2231.40` | `2224.20` | `0.000000` | -4,053.88 USD | `-0.33%` | `25X Cross` |
| `1699` | `0xbef3...0d3e` | `LONG` | 1,228,761.88 USD | `552.33` | `2233.44` | `2224.20` | `2068.60` | -4,828.94 USD | `-0.39%` | `20X Cross` |
| `1704` | `0x6a41...a3b9` | `LONG` | 1,224,961.95 USD | `550.69` | `2233.05` | `2224.20` | `2074.05` | -4,764.40 USD | `-0.39%` | `20X Cross` |
| `1706` | `0xb8eb...1dd5` | `LONG` | 1,224,643.42 USD | `550.55` | `2232.72` | `2224.20` | `0.000000` | -4,580.88 USD | `-0.37%` | `25X Cross` |
| `1707` | `0x825c...465e` | `LONG` | 1,223,420.00 USD | `550.00` | `2208.12` | `2224.20` | `1189.22` | 8,950.50 USD | `+0.73%` | `4X Cross` |
| `1716` | `0xad21...fb6a` | `LONG` | 1,217,316.02 USD | `547.26` | `2565.80` | `2224.20` | `1737.07` | -186,836.97 USD | `-15.35%` | `6X Cross` |
| `1775` | `0x2e30...4cb5` | `SHORT` | 1,157,719.90 USD | `520.46` | `2316.65` | `2224.20` | `11924.18` | 48,017.62 USD | `+4.15%` | `2X Cross` |
| `1787` | `0x6dae...90de` | `SHORT` | 1,150,082.77 USD | `517.05` | `2292.28` | `2224.20` | `3852.29` | 35,150.65 USD | `+3.06%` | `25X Cross` |
| `1811` | `0xfc66...ca06` | `SHORT` | 1,135,253.34 USD | `510.89` | `2275.19` | `2224.20` | `55748.54` | 27,128.26 USD | `+2.39%` | `20X Cross` |
| `1818` | `0x0089...2410` | `SHORT` | 1,128,539.55 USD | `507.35` | `2308.88` | `2224.20` | `3374.29` | 42,860.71 USD | `+3.80%` | `20X Cross` |
| `1833` | `0xa559...ff95` | `LONG` | 1,112,350.00 USD | `500.00` | `2260.68` | `2224.20` | `1060.77` | -17,994.36 USD | `-1.62%` | `20X Cross` |
| `1834` | `0x4044...794c` | `LONG` | 1,112,350.00 USD | `500.00` | `2260.80` | `2224.20` | `0.000000` | -18,050.00 USD | `-1.62%` | `25X Cross` |
| `1835` | `0xe282...df29` | `LONG` | 1,112,200.00 USD | `500.00` | `2309.84` | `2224.20` | `2045.08` | -42,724.21 USD | `-3.84%` | `10X Isolated` |
| `1836` | `0xb322...d51f` | `SHORT` | 1,112,200.00 USD | `500.00` | `2268.03` | `2224.20` | `3722.10` | 21,816.32 USD | `+1.96%` | `20X Cross` |
| `1837` | `0x6936...9417` | `SHORT` | 1,112,050.00 USD | `500.00` | `2315.11` | `2224.20` | `2358.68` | 45,505.21 USD | `+4.09%` | `25X Isolated` |
| `1838` | `0x89b2...9ca6` | `LONG` | 1,111,950.00 USD | `500.00` | `2363.45` | `2224.20` | `1622.41` | -69,777.42 USD | `-6.28%` | `25X Cross` |
| `1841` | `0x7298...7d6c` | `SHORT` | 1,108,033.49 USD | `498.15` | `3426.75` | `2224.20` | `5421.39` | 599,002.33 USD | `+54.06%` | `20X Cross` |
| `1860` | `0x9c68...7783` | `SHORT` | 1,097,264.54 USD | `493.31` | `2273.58` | `2224.20` | `3880.78` | 24,314.71 USD | `+2.22%` | `25X Cross` |
| `1868` | `0x404c...5f03` | `SHORT` | 1,089,233.53 USD | `489.79` | `2671.94` | `2224.20` | `5032.74` | 219,446.03 USD | `+20.15%` | `20X Cross` |
| `1872` | `0x321f...1c84` | `SHORT` | 1,085,590.26 USD | `488.02` | `2370.09` | `2224.20` | `3065.73` | 71,054.34 USD | `+6.55%` | `10X Cross` |
| `1880` | `0x94b6...e5b3` | `SHORT` | 1,081,268.16 USD | `486.05` | `2260.75` | `2224.20` | `2355.70` | 17,574.43 USD | `+1.63%` | `25X Cross` |
| `1935` | `0x82c6...fe42` | `LONG` | 1,028,692.50 USD | `462.50` | `2501.38` | `2224.20` | `2053.42` | -128,198.07 USD | `-12.46%` | `5X Isolated` |
| `1937` | `0x2de3...486d` | `LONG` | 1,028,415.75 USD | `462.33` | `2286.03` | `2224.20` | `1151.29` | -28,496.82 USD | `-2.77%` | `25X Cross` |
| `1943` | `0xe330...77a1` | `SHORT` | 1,025,757.14 USD | `461.20` | `2206.97` | `2224.20` | `6455.66` | -7,899.78 USD | `-0.77%` | `20X Cross` |
| `1952` | `0xd6e1...f256` | `LONG` | 1,020,195.92 USD | `458.64` | `2213.70` | `2224.20` | `915.29` | 4,905.04 USD | `+0.48%` | `25X Cross` |
| `1954` | `0x617e...0f97` | `SHORT` | 1,018,451.33 USD | `457.85` | `2205.60` | `2224.20` | `3346.49` | -8,607.49 USD | `-0.85%` | `10X Cross` |
| `1989` | `0xae55...2236` | `LONG` | 1,000,980.00 USD | `450.00` | `2510.21` | `2224.20` | `0.000000` | -128,617.50 USD | `-12.85%` | `25X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `2369.00` | 53.78 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.05K USD at 2369.0000 USD [API] | `2026-10-28 02:18:25` |
| `ANNOUNCEMENT` | `INFO` | `2369.00` | 32,997.80 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 33.00K USD at 2369.0000 USD [API] | `2026-10-28 02:18:25` |
| `ANNOUNCEMENT` | `INFO` | `2369.00` | 261.77 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.26K USD at 2369.0000 USD [API] | `2026-10-28 02:18:25` |
| `ANNOUNCEMENT` | `INFO` | `2369.00` | 19.66 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.02K USD at 2369.0000 USD [API] | `2026-10-28 02:18:25` |
| `ANNOUNCEMENT` | `INFO` | `2369.00` | 1,287.31 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.29K USD at 2369.0000 USD [API] | `2026-10-28 02:18:25` |
| `ANNOUNCEMENT` | `INFO` | `2369.00` | 1,810.63 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.81K USD at 2369.0000 USD [API] | `2026-10-28 02:18:25` |
| `ANNOUNCEMENT` | `INFO` | `2369.00` | 12,309.32 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 12.31K USD at 2369.0000 USD [API] | `2026-10-28 02:18:25` |
| `ANNOUNCEMENT` | `INFO` | `2369.00` | 76.52 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.08K USD at 2369.0000 USD [API] | `2026-10-28 02:18:25` |
| `ANNOUNCEMENT` | `INFO` | `2369.00` | 50,088.24 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 50.09K USD at 2369.0000 USD [API] | `2026-10-28 02:18:25` |
| `ANNOUNCEMENT` | `INFO` | `2369.00` | 12.32 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.01K USD at 2369.0000 USD [API] | `2026-10-28 02:18:25` |
| `ANNOUNCEMENT` | `INFO` | `2369.00` | 34.35 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.03K USD at 2369.0000 USD [API] | `2026-10-28 02:18:25` |
| `ANNOUNCEMENT` | `INFO` | `2317.30` | 81,784.24 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 81.78K USD at 2317.3000 USD [API] | `2026-10-29 10:14:21` |
| `ANNOUNCEMENT` | `INFO` | `2317.30` | 67,469.12 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 67.47K USD at 2317.3000 USD [API] | `2026-10-29 10:14:21` |
| `ANNOUNCEMENT` | `INFO` | `2296.60` | 65.68 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.07K USD at 2296.6000 USD [API] | `2026-10-29 02:30:57` |
| `ANNOUNCEMENT` | `INFO` | `2296.60` | 31,280.61 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 31.28K USD at 2296.6000 USD [API] | `2026-10-29 02:30:57` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 407.52 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.41K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 171.01 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.17K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 413.73 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.41K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 191.01 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.19K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 23.21 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 841.25 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.84K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 6,367.30 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 6.37K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 111.48 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.11K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 122.28 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.12K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 140.21 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.14K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 621.28 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.62K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 30.57 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.03K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 1,627.80 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.63K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 2,332.06 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 2.33K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 61.14 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.06K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 11.72 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.01K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2298.50` | 29.88 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.03K USD at 2298.5000 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 123.45 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.12K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 24,696.02 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 24.70K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 25,605.64 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 25.61K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 70,134.15 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 70.13K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 245.29 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.25K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 11,537.50 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 11.54K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 24.46 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.02K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 30,133.18 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 30.13K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 244.59 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.24K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 70,479.82 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 70.48K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 13,103.83 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 13.10K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2381.50` | 2,944.96 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 2.94K USD at 2381.5000 USD [API] | `2026-10-28 20:01:11` |
| `ANNOUNCEMENT` | `INFO` | `2381.50` | 49.77 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.05K USD at 2381.5000 USD [API] | `2026-10-28 20:01:11` |
| `ANNOUNCEMENT` | `INFO` | `2381.50` | 1,188.84 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.19K USD at 2381.5000 USD [API] | `2026-10-28 20:01:11` |
| `ANNOUNCEMENT` | `INFO` | `2381.10` | 143.34 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.14K USD at 2381.1000 USD [API] | `2026-10-28 20:01:02` |
| `ANNOUNCEMENT` | `INFO` | `2381.10` | 51.91 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.05K USD at 2381.1000 USD [API] | `2026-10-28 20:01:02` |
| `ANNOUNCEMENT` | `INFO` | `2381.10` | 356.69 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.36K USD at 2381.1000 USD [API] | `2026-10-28 20:01:02` |
| `ANNOUNCEMENT` | `INFO` | `2377.80` | 15,458.79 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 15.46K USD at 2377.8000 USD [API] | `2026-10-28 20:00:18` |
| `ANNOUNCEMENT` | `INFO` | `2377.80` | 104,644.60 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 104.64K USD at 2377.8000 USD [API] | `2026-10-28 20:00:18` |
| `ANNOUNCEMENT` | `INFO` | `2318.80` | 154,404.02 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 154.40K USD at 2318.8000 USD [API] | `2026-10-29 10:26:53` |
| `ANNOUNCEMENT` | `INFO` | `2323.90` | 66,792.84 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 66.79K USD at 2323.9000 USD [API] | `2026-10-29 10:39:31` |
| `ANNOUNCEMENT` | `INFO` | `2323.00` | 106,844.06 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 106.84K USD at 2323.0000 USD [API] | `2026-10-29 10:44:22` |
| `ANNOUNCEMENT` | `INFO` | `2324.50` | 1,412.13 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.41K USD at 2324.5000 USD [API] | `2026-10-29 10:45:49` |
| `ANNOUNCEMENT` | `INFO` | `2325.00` | 69,594.92 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 69.59K USD at 2325.0000 USD [API] | `2026-10-29 11:36:03` |
| `ANNOUNCEMENT` | `INFO` | `2325.00` | 99,895.72 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 99.90K USD at 2325.0000 USD [API] | `2026-10-29 11:36:03` |
| `ANNOUNCEMENT` | `INFO` | `2325.00` | 63,009.36 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 63.01K USD at 2325.0000 USD [API] | `2026-10-29 11:36:03` |
| `ANNOUNCEMENT` | `INFO` | `2325.90` | 70,001.45 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 70.00K USD at 2325.9000 USD [API] | `2026-10-29 11:53:41` |
| `ANNOUNCEMENT` | `INFO` | `2322.00` | 41,043.44 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 41.04K USD at 2322.0000 USD [API] | `2026-10-29 12:27:06` |
| `ANNOUNCEMENT` | `INFO` | `2322.60` | 40,051.38 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 40.05K USD at 2322.6000 USD [API] | `2026-10-29 12:52:25` |
| `ANNOUNCEMENT` | `INFO` | `2316.70` | 73,303.86 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 73.30K USD at 2316.7000 USD [API] | `2026-10-29 13:39:20` |
| `ANNOUNCEMENT` | `INFO` | `2514.40` | 294.44 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.29K USD at 2514.4000 USD [API] | `2026-09-14 23:37:58` |
| `ANNOUNCEMENT` | `INFO` | `2357.20` | 29,188.03 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 29.19K USD at 2357.2000 USD [API] | `2026-10-29 16:29:53` |
| `ANNOUNCEMENT` | `INFO` | `2429.60` | 82,377.29 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 82.38K USD at 2429.6000 USD [API] | `2026-10-08 15:56:54` |
| `ANNOUNCEMENT` | `INFO` | `2441.60` | 20,695.98 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 20.70K USD at 2441.6000 USD [API] | `2026-10-08 15:35:34` |
| `ANNOUNCEMENT` | `INFO` | `2453.30` | 5,820.21 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 5.82K USD at 2453.3000 USD [API] | `2026-10-08 15:34:56` |
| `ANNOUNCEMENT` | `INFO` | `2453.30` | 431.78 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.43K USD at 2453.3000 USD [API] | `2026-10-08 15:34:56` |
| `ANNOUNCEMENT` | `INFO` | `2453.30` | 1,497.74 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.50K USD at 2453.3000 USD [API] | `2026-10-08 15:34:56` |
| `ANNOUNCEMENT` | `INFO` | `2453.40` | 18,244.95 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 18.24K USD at 2453.4000 USD [API] | `2026-10-08 15:34:56` |
| `ANNOUNCEMENT` | `INFO` | `2478.30` | 6,609.38 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 6.61K USD at 2478.3000 USD [API] | `2026-10-08 15:20:45` |
| `ANNOUNCEMENT` | `INFO` | `2478.30` | 218.34 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.22K USD at 2478.3000 USD [API] | `2026-10-08 15:20:45` |
| `ANNOUNCEMENT` | `INFO` | `2478.30` | 12.14 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.01K USD at 2478.3000 USD [API] | `2026-10-08 15:20:45` |
| `ANNOUNCEMENT` | `INFO` | `2478.30` | 72.61 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.07K USD at 2478.3000 USD [API] | `2026-10-08 15:20:45` |
| `ANNOUNCEMENT` | `INFO` | `2478.40` | 545.25 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.55K USD at 2478.4000 USD [API] | `2026-10-08 15:20:45` |
| `ANNOUNCEMENT` | `INFO` | `2478.50` | 282.30 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.28K USD at 2478.5000 USD [API] | `2026-10-08 15:20:45` |
| `ANNOUNCEMENT` | `INFO` | `2478.50` | 925.97 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.93K USD at 2478.5000 USD [API] | `2026-10-08 15:20:45` |
| `ANNOUNCEMENT` | `INFO` | `2478.50` | 24,159.43 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 24.16K USD at 2478.5000 USD [API] | `2026-10-08 15:20:45` |
| `ANNOUNCEMENT` | `INFO` | `2553.00` | 4,921.42 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 4.92K USD at 2553.0000 USD [API] | `2026-10-07 13:39:04` |
| `ANNOUNCEMENT` | `INFO` | `2553.20` | 15,355.71 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 15.36K USD at 2553.2000 USD [API] | `2026-10-07 13:39:04` |
| `ANNOUNCEMENT` | `INFO` | `2338.40` | 43,486.99 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 43.49K USD at 2338.4000 USD [API] | `2026-10-29 17:41:19` |
| `ANNOUNCEMENT` | `INFO` | `2380.80` | 43.33 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.04K USD at 2380.8000 USD [API] | `2026-10-22 16:45:54` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`2275.30` (Vol: 35,200,000.00 USD, Dist: `+2.34%`) | Long MP=`2174.37` (Vol: 35,800,000.00 USD, Dist: `--2.20%`)
  * 48H Horizon: Short MP=`2270.12` (Vol: 35,900,000.00 USD, Dist: `+2.11%`) | Long MP=`2174.00` (Vol: 35,800,000.00 USD, Dist: `--2.21%`)
  * 3D Horizon: Short MP=`2270.12` (Vol: 35,900,000.00 USD, Dist: `+2.11%`) | Long MP=`2174.00` (Vol: 35,800,000.00 USD, Dist: `--2.21%`)
  * 7D Horizon: Short MP=`2401.80` (Vol: 50,700,000.00 USD, Dist: `+8.03%`) | Long MP=`2175.27` (Vol: 44,800,000.00 USD, Dist: `--2.16%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `445.00` | 75,450.00 USD | 786,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `455.00` | 121,330.00 USD | 786,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `465.00` | 118,030.00 USD | 786,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `475.00` | 81,110.00 USD | 786,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.00` | 2,960.00 USD | 786,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `495.00` | 140,880.00 USD | 786,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.00` | 67,370.00 USD | 786,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.00` | 39,200.00 USD | 786,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.00` | 1,870,000.00 USD | 786,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.00` | 34,560.00 USD | 784,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.00` | 53,010.00 USD | 784,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.00` | 66,580.00 USD | 784,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `565.00` | 158,160.00 USD | 784,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `575.00` | 64,830.00 USD | 783,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.00` | 44,160.00 USD | 783,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.00` | 3,330,000.00 USD | 783,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `605.00` | 154,720.00 USD | 780,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.00` | 142,040.00 USD | 780,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.00` | 1,880,000.00 USD | 780,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.00` | 51,410.00 USD | 778,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `645.00` | 1,150,000.00 USD | 778,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `655.00` | 46,320.00 USD | 777,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `665.00` | 54,620.00 USD | 777,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `675.00` | 46,090.00 USD | 777,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `685.00` | 44,110.00 USD | 776,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `695.00` | 2,640.00 USD | 776,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `705.00` | 15,790.00 USD | 776,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `715.00` | 54,550.00 USD | 776,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `725.00` | 1,080,000.00 USD | 776,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `735.00` | 78,630.00 USD | 775,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `745.00` | 9,220.00 USD | 775,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `755.00` | 55,210.00 USD | 775,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `765.00` | 5,250.00 USD | 775,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `775.00` | 72,970.00 USD | 775,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `785.00` | 16,550.00 USD | 775,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `795.00` | 6,010.00 USD | 775,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `805.00` | 85,220.00 USD | 775,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `815.00` | 95,130.00 USD | 775,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `825.00` | 129,310.00 USD | 775,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `835.00` | 62,560.00 USD | 775,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `845.00` | 375,830.00 USD | 775,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `855.00` | 214,080.00 USD | 774,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `865.00` | 17,290.00 USD | 774,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `875.00` | 88,960.00 USD | 774,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `885.00` | 964,270.00 USD | 774,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `895.00` | 175,070.00 USD | 773,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `905.00` | 18,280.00 USD | 773,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `915.00` | 605,510.00 USD | 773,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `925.00` | 164,030.00 USD | 772,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `935.00` | 297,070.00 USD | 772,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `945.00` | 91,310.00 USD | 772,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `955.00` | 294,230.00 USD | 772,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `965.00` | 47,900.00 USD | 771,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `975.00` | 183,680.00 USD | 771,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `985.00` | 105,940.00 USD | 771,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `995.00` | 336,130.00 USD | 771,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1005.00` | 113,820.00 USD | 771,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1015.00` | 155,360.00 USD | 771,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1025.00` | 63,130.00 USD | 770,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1035.00` | 60,140.00 USD | 770,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1045.00` | 702,780.00 USD | 770,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1055.00` | 7,410,000.00 USD | 770,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1065.00` | 557,690.00 USD | 762,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1075.00` | 721,980.00 USD | 762,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1085.00` | 1,890,000.00 USD | 761,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1095.00` | 676,930.00 USD | 759,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1105.00` | 217,450.00 USD | 758,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1115.00` | 206,920.00 USD | 758,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1125.00` | 7,930,000.00 USD | 758,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1135.00` | 86,940.00 USD | 750,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1145.00` | 850,610.00 USD | 750,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1155.00` | 599,140.00 USD | 749,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1165.00` | 1,630,000.00 USD | 748,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1175.00` | 261,700.00 USD | 747,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1185.00` | 2,670,000.00 USD | 747,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1195.00` | 330,450.00 USD | 744,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1205.00` | 7,250,000.00 USD | 744,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1215.00` | 80,960.00 USD | 736,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1225.00` | 405,620.00 USD | 736,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1235.00` | 116,280.00 USD | 736,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1245.00` | 53,980.00 USD | 736,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1255.00` | 1,200,000.00 USD | 736,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1265.00` | 2,220,000.00 USD | 734,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1275.00` | 15,490,000.00 USD | 732,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1285.00` | 556,180.00 USD | 717,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1295.00` | 378,160.00 USD | 716,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1305.00` | 125,780.00 USD | 716,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1315.00` | 306,940.00 USD | 716,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1325.00` | 640,550.00 USD | 715,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1335.00` | 286,420.00 USD | 715,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1345.00` | 580,160.00 USD | 714,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1355.00` | 5,240,000.00 USD | 714,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1365.00` | 1,100,000.00 USD | 709,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1375.00` | 7,130,000.00 USD | 708,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1385.00` | 2,300,000.00 USD | 700,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1395.00` | 520,350.00 USD | 698,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1405.00` | 10,130,000.00 USD | 698,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1415.00` | 554,220.00 USD | 687,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1425.00` | 372,990.00 USD | 687,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1435.00` | 1,210,000.00 USD | 687,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1445.00` | 2,120,000.00 USD | 685,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1455.00` | 19,770,000.00 USD | 683,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1465.00` | 2,030,000.00 USD | 663,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1475.00` | 5,960,000.00 USD | 661,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1485.00` | 139,630.00 USD | 655,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1495.00` | 19,510,000.00 USD | 655,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1505.00` | 293,500.00 USD | 636,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1515.00` | 20,980,000.00 USD | 636,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1525.00` | 275,130.00 USD | 615,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1535.00` | 1,060,000.00 USD | 614,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1545.00` | 2,710,000.00 USD | 613,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1555.00` | 3,810,000.00 USD | 610,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1565.00` | 16,680,000.00 USD | 607,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1575.00` | 747,200.00 USD | 590,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1585.00` | 1,100,000.00 USD | 589,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1595.00` | 1,470,000.00 USD | 588,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1605.00` | 17,980,000.00 USD | 587,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1615.00` | 410,710.00 USD | 569,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1625.00` | 1,110,000.00 USD | 568,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1635.00` | 18,690,000.00 USD | 567,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1645.00` | 36,670,000.00 USD | 548,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1655.00` | 533,660.00 USD | 512,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1665.00` | 12,350,000.00 USD | 511,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1675.00` | 1,460,000.00 USD | 499,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1685.00` | 1,220,000.00 USD | 497,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1695.00` | 870,240.00 USD | 496,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1705.00` | 17,250,000.00 USD | 495,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1715.00` | 17,850,000.00 USD | 478,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1725.00` | 19,370,000.00 USD | 460,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1735.00` | 1,390,000.00 USD | 441,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1745.00` | 1,110,000.00 USD | 440,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1755.00` | 225,470.00 USD | 438,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1765.00` | 3,830,000.00 USD | 438,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1775.00` | 4,970,000.00 USD | 434,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1785.00` | 83,330,000.00 USD | 429,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1795.00` | 1,160,000.00 USD | 346,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1805.00` | 8,320,000.00 USD | 345,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1815.00` | 2,190,000.00 USD | 337,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1825.00` | 4,200,000.00 USD | 334,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1835.00` | 1,110,000.00 USD | 330,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1845.00` | 16,340,000.00 USD | 329,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1855.00` | 1,120,000.00 USD | 313,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1865.00` | 1,300,000.00 USD | 312,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1875.00` | 18,820,000.00 USD | 310,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1885.00` | 4,920,000.00 USD | 291,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1895.00` | 1,310,000.00 USD | 287,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1905.00` | 3,660,000.00 USD | 285,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1915.00` | 17,910,000.00 USD | 282,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1925.00` | 1,370,000.00 USD | 264,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1935.00` | 17,760,000.00 USD | 262,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1945.00` | 1,690,000.00 USD | 245,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1955.00` | 1,410,000.00 USD | 243,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1965.00` | 14,400,000.00 USD | 241,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1972.30` | 736,320,000.00 USD | 736,320,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1975.00` | 1,630,000.00 USD | 227,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1975.10` | 736,180,000.00 USD | 736,180,000.00 USD | 0.00 USD | 0.00 USD | 49,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1977.90` | 736,130,000.00 USD | 736,130,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1983.50` | 733,890,000.00 USD | 733,890,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1985.00` | 5,570,000.00 USD | 225,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1986.30` | 733,690,000.00 USD | 733,690,000.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1989.10` | 729,960,000.00 USD | 729,960,000.00 USD | 0.00 USD | 1,780,000.00 USD | 38,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1991.90` | 728,140,000.00 USD | 728,140,000.00 USD | 1,390,000.00 USD | 1,320,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1994.70` | 725,430,000.00 USD | 725,430,000.00 USD | 0.00 USD | 0.00 USD | 808,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1995.00` | 5,340,000.00 USD | 220,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1997.50` | 724,630,000.00 USD | 724,630,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1999.20` | 632,340,000.00 USD | 632,340,000.00 USD | 43,520.00 USD | 104,180.00 USD | 486,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2001.60` | 631,700,000.00 USD | 631,700,000.00 USD | 676,180.00 USD | 580,080.00 USD | 590,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2003.10` | 723,280,000.00 USD | 723,280,000.00 USD | 0.00 USD | 266,430.00 USD | 594,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2004.00` | 629,860,000.00 USD | 629,860,000.00 USD | 390,870.00 USD | 358,610.00 USD | 685,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2005.00` | 13,090,000.00 USD | 214,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2005.90` | 722,420,000.00 USD | 722,420,000.00 USD | 0.00 USD | 475,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2006.40` | 628,420,000.00 USD | 628,420,000.00 USD | 641,010.00 USD | 35,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2008.70` | 721,950,000.00 USD | 721,950,000.00 USD | 807,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2008.80` | 627,750,000.00 USD | 627,750,000.00 USD | 0.00 USD | 548,050.00 USD | 126,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2011.20` | 627,070,000.00 USD | 627,070,000.00 USD | 764,070.00 USD | 490,470.00 USD | 366,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2011.50` | 721,140,000.00 USD | 721,140,000.00 USD | 170,840.00 USD | 92,470.00 USD | 689,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2013.60` | 625,450,000.00 USD | 625,450,000.00 USD | 69,570.00 USD | 258,510.00 USD | 25,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2015.00` | 2,660,000.00 USD | 201,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2016.00` | 625,100,000.00 USD | 625,100,000.00 USD | 384,540.00 USD | 605,010.00 USD | 193,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2017.10` | 720,190,000.00 USD | 720,190,000.00 USD | 0.00 USD | 0.00 USD | 21,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2018.40` | 623,910,000.00 USD | 623,910,000.00 USD | 772,840.00 USD | 885,870.00 USD | 714,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2020.80` | 621,540,000.00 USD | 621,540,000.00 USD | 622,680.00 USD | 1,430,000.00 USD | 673,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2022.70` | 720,160,000.00 USD | 720,160,000.00 USD | 1,070,000.00 USD | 0.00 USD | 934,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2023.20` | 618,810,000.00 USD | 618,810,000.00 USD | 792,850.00 USD | 120,570.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2025.00` | 1,180,000.00 USD | 199,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2025.50` | 718,160,000.00 USD | 718,160,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2025.60` | 616,460,000.00 USD | 616,460,000.00 USD | 414,330.00 USD | 1,100,000.00 USD | 231,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2028.00` | 614,720,000.00 USD | 614,720,000.00 USD | 2,770,000.00 USD | 978,910.00 USD | 615,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2028.30` | 717,980,000.00 USD | 717,980,000.00 USD | 1,100,000.00 USD | 0.00 USD | 35,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2030.40` | 610,350,000.00 USD | 610,350,000.00 USD | 87,180.00 USD | 366,120.00 USD | 654,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2031.10` | 716,850,000.00 USD | 716,850,000.00 USD | 0.00 USD | 3,520,000.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2032.80` | 609,250,000.00 USD | 609,250,000.00 USD | 1,360,000.00 USD | 1,490,000.00 USD | 707,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2033.90` | 712,280,000.00 USD | 712,280,000.00 USD | 0.00 USD | 0.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2035.00` | 1,110,000.00 USD | 198,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2035.20` | 605,690,000.00 USD | 605,690,000.00 USD | 1,150,000.00 USD | 19,490.00 USD | 165,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2036.70` | 710,920,000.00 USD | 710,920,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2037.60` | 604,350,000.00 USD | 604,350,000.00 USD | 396,700.00 USD | 458,110.00 USD | 378,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2039.50` | 710,590,000.00 USD | 710,590,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2040.00` | 603,120,000.00 USD | 603,120,000.00 USD | 542,670.00 USD | 178,560.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2042.40` | 602,360,000.00 USD | 602,360,000.00 USD | 626,840.00 USD | 0.00 USD | 166,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2044.80` | 601,570,000.00 USD | 601,570,000.00 USD | 0.00 USD | 0.00 USD | 26,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2045.00` | 6,580,000.00 USD | 196,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2045.10` | 709,140,000.00 USD | 709,140,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2047.20` | 601,540,000.00 USD | 601,540,000.00 USD | 467,370.00 USD | 0.00 USD | 367,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2049.60` | 600,710,000.00 USD | 600,710,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2050.70` | 708,840,000.00 USD | 708,840,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2053.50` | 708,620,000.00 USD | 708,620,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2054.40` | 599,600,000.00 USD | 599,600,000.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2055.00` | 3,870,000.00 USD | 190,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2056.80` | 599,480,000.00 USD | 599,480,000.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2059.10` | 706,330,000.00 USD | 706,330,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2059.20` | 599,240,000.00 USD | 599,240,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2061.60` | 598,490,000.00 USD | 598,490,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2061.90` | 705,990,000.00 USD | 705,990,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2064.00` | 598,410,000.00 USD | 598,410,000.00 USD | 563,140.00 USD | 494,150.00 USD | 510,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2064.70` | 700,730,000.00 USD | 700,730,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2065.00` | 15,510,000.00 USD | 186,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2066.40` | 596,840,000.00 USD | 596,840,000.00 USD | 387,410.00 USD | 42,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2067.50` | 698,270,000.00 USD | 698,270,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2068.80` | 596,410,000.00 USD | 596,410,000.00 USD | 57,300.00 USD | 624,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2070.30` | 696,620,000.00 USD | 696,620,000.00 USD | 3,600,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2071.20` | 595,730,000.00 USD | 595,730,000.00 USD | 47,910.00 USD | 534,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2073.10` | 689,060,000.00 USD | 689,060,000.00 USD | 2,870,000.00 USD | 2,180,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2073.60` | 595,150,000.00 USD | 595,150,000.00 USD | 25,660.00 USD | 20,640.00 USD | 420,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 3,430,000.00 USD | 170,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2075.90` | 681,980,000.00 USD | 681,980,000.00 USD | 3,910,000.00 USD | 4,290,000.00 USD | 4,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2076.00` | 594,680,000.00 USD | 594,680,000.00 USD | 354,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2078.40` | 594,320,000.00 USD | 594,320,000.00 USD | 0.00 USD | 25,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2078.70` | 669,480,000.00 USD | 669,480,000.00 USD | 4,160,000.00 USD | 3,730,000.00 USD | 2,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2080.80` | 594,300,000.00 USD | 594,300,000.00 USD | 77,960.00 USD | 29,610.00 USD | 199,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2081.50` | 659,530,000.00 USD | 659,530,000.00 USD | 4,400,000.00 USD | 1,290,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2083.20` | 593,990,000.00 USD | 593,990,000.00 USD | 827,940.00 USD | 4,240.00 USD | 209,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2084.30` | 652,620,000.00 USD | 652,620,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 3,500,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 12,820,000.00 USD | 167,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2085.60` | 592,950,000.00 USD | 592,950,000.00 USD | 528,660.00 USD | 242,120.00 USD | 817,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2087.10` | 645,230,000.00 USD | 645,230,000.00 USD | 2,920,000.00 USD | 2,750,000.00 USD | 3,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2088.00` | 591,360,000.00 USD | 591,360,000.00 USD | 438,420.00 USD | 227,880.00 USD | 306,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2089.90` | 636,550,000.00 USD | 636,550,000.00 USD | 4,130,000.00 USD | 948,120.00 USD | 3,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2090.40` | 590,390,000.00 USD | 590,390,000.00 USD | 761,770.00 USD | 224,660.00 USD | 446,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2092.70` | 628,310,000.00 USD | 628,310,000.00 USD | 4,680,000.00 USD | 737,060.00 USD | 6,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2092.80` | 588,960,000.00 USD | 588,960,000.00 USD | 752,390.00 USD | 334,060.00 USD | 176,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 1,840,000.00 USD | 154,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2095.20` | 587,690,000.00 USD | 587,690,000.00 USD | 1,840,000.00 USD | 1,130,000.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2095.50` | 616,680,000.00 USD | 616,680,000.00 USD | 2,480,000.00 USD | 2,010,000.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2097.60` | 583,230,000.00 USD | 583,230,000.00 USD | 175,830.00 USD | 488,160.00 USD | 517,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2098.30` | 611,170,000.00 USD | 611,170,000.00 USD | 3,020,000.00 USD | 3,130,000.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2100.00` | 582,050,000.00 USD | 582,050,000.00 USD | 307,340.00 USD | 779,630.00 USD | 20,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2101.10` | 603,550,000.00 USD | 603,550,000.00 USD | 631,640.00 USD | 1,240,000.00 USD | 3,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2102.40` | 580,940,000.00 USD | 580,940,000.00 USD | 211,840.00 USD | 371,740.00 USD | 513,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2103.90` | 598,270,000.00 USD | 598,270,000.00 USD | 1,130,000.00 USD | 738,240.00 USD | 2,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2104.80` | 579,850,000.00 USD | 579,850,000.00 USD | 3,570,000.00 USD | 1,160,000.00 USD | 683,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 2,360,000.00 USD | 152,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2106.70` | 594,080,000.00 USD | 594,080,000.00 USD | 1,700,000.00 USD | 834,660.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2107.20` | 574,430,000.00 USD | 574,430,000.00 USD | 677,650.00 USD | 0.00 USD | 496,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2109.50` | 590,360,000.00 USD | 590,360,000.00 USD | 7,750,000.00 USD | 1,800,000.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2109.60` | 573,260,000.00 USD | 573,260,000.00 USD | 118,210.00 USD | 31,550.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2112.00` | 573,100,000.00 USD | 573,100,000.00 USD | 490,860.00 USD | 360,140.00 USD | 221,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2112.30` | 579,050,000.00 USD | 579,050,000.00 USD | 3,920,000.00 USD | 1,480,000.00 USD | 3,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2114.40` | 572,030,000.00 USD | 572,030,000.00 USD | 614,540.00 USD | 231,420.00 USD | 286,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 2,210,000.00 USD | 150,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2115.10` | 569,930,000.00 USD | 569,930,000.00 USD | 923,330.00 USD | 3,210,000.00 USD | 1,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2116.80` | 570,900,000.00 USD | 570,900,000.00 USD | 3,030,000.00 USD | 1,240,000.00 USD | 676,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2117.90` | 563,860,000.00 USD | 563,860,000.00 USD | 8,390,000.00 USD | 578,010.00 USD | 2,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2119.20` | 565,950,000.00 USD | 565,950,000.00 USD | 3,990,000.00 USD | 3,020,000.00 USD | 916,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2120.70` | 552,310,000.00 USD | 552,310,000.00 USD | 7,060,000.00 USD | 5,780,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2121.60` | 558,030,000.00 USD | 558,030,000.00 USD | 5,220,000.00 USD | 3,820,000.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2123.50` | 537,660,000.00 USD | 537,660,000.00 USD | 7,150,000.00 USD | 7,720,000.00 USD | 1,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2124.00` | 547,580,000.00 USD | 547,580,000.00 USD | 6,610,000.00 USD | 1,490,000.00 USD | 2,330,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 123,700,000.00 USD | 148,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2126.30` | 521,380,000.00 USD | 521,380,000.00 USD | 2,740,000.00 USD | 4,400,000.00 USD | 4,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2126.40` | 537,150,000.00 USD | 537,150,000.00 USD | 3,480,000.00 USD | 2,810,000.00 USD | 306,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2128.80` | 530,560,000.00 USD | 530,560,000.00 USD | 3,180,000.00 USD | 1,860,000.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2129.10` | 509,450,000.00 USD | 509,450,000.00 USD | 4,770,000.00 USD | 1,270,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2131.20` | 524,000,000.00 USD | 524,000,000.00 USD | 363,860.00 USD | 274,200.00 USD | 344,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2131.90` | 502,300,000.00 USD | 502,300,000.00 USD | 2,170,000.00 USD | 1,620,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2133.60` | 523,020,000.00 USD | 523,020,000.00 USD | 792,080.00 USD | 690,590.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2134.70` | 497,150,000.00 USD | 497,150,000.00 USD | 1,630,000.00 USD | 790,240.00 USD | 898,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 1,490,000.00 USD | 24,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2136.00` | 520,000,000.00 USD | 520,000,000.00 USD | 2,320,000.00 USD | 2,790,000.00 USD | 3,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2137.50` | 493,840,000.00 USD | 493,840,000.00 USD | 2,120,000.00 USD | 2,390,000.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2138.40` | 511,800,000.00 USD | 511,800,000.00 USD | 783,250.00 USD | 1,210,000.00 USD | 70,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2140.30` | 487,800,000.00 USD | 487,800,000.00 USD | 3,990,000.00 USD | 1,870,000.00 USD | 801,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2140.80` | 509,730,000.00 USD | 509,730,000.00 USD | 1,530,000.00 USD | 1,450,000.00 USD | 317,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2143.10` | 481,150,000.00 USD | 481,150,000.00 USD | 2,380,000.00 USD | 618,280.00 USD | 268,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2143.20` | 506,430,000.00 USD | 506,430,000.00 USD | 1,080,000.00 USD | 2,830,000.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 5,640,000.00 USD | 23,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2145.60` | 501,360,000.00 USD | 501,360,000.00 USD | 3,170,000.00 USD | 2,360,000.00 USD | 615,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2145.90` | 477,880,000.00 USD | 477,880,000.00 USD | 978,940.00 USD | 1,450,000.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2148.00` | 495,210,000.00 USD | 495,210,000.00 USD | 728,710.00 USD | 1,810,000.00 USD | 69,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2148.70` | 473,730,000.00 USD | 473,730,000.00 USD | 26,270.00 USD | 538,910.00 USD | 399,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2150.40` | 492,610,000.00 USD | 492,610,000.00 USD | 7,580,000.00 USD | 2,090,000.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2151.50` | 472,760,000.00 USD | 472,760,000.00 USD | 11,200,000.00 USD | 363,770.00 USD | 107,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2152.80` | 480,280,000.00 USD | 480,280,000.00 USD | 2,710,000.00 USD | 2,710,000.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2154.30` | 461,090,000.00 USD | 461,090,000.00 USD | 48,150.00 USD | 2,020,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 1,690,000.00 USD | 17,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2155.20` | 472,620,000.00 USD | 472,620,000.00 USD | 2,740,000.00 USD | 3,890,000.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2157.10` | 457,450,000.00 USD | 457,450,000.00 USD | 4,270,000.00 USD | 1,330,000.00 USD | 5,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2157.60` | 463,610,000.00 USD | 463,610,000.00 USD | 3,400,000.00 USD | 1,460,000.00 USD | 3,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2159.90` | 446,790,000.00 USD | 446,790,000.00 USD | 2,980,000.00 USD | 737,260.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2160.00` | 455,070,000.00 USD | 455,070,000.00 USD | 4,390,000.00 USD | 6,230,000.00 USD | 2,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2162.40` | 441,530,000.00 USD | 441,530,000.00 USD | 15,640,000.00 USD | 9,100,000.00 USD | 783,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2162.70` | 441,230,000.00 USD | 441,230,000.00 USD | 17,980,000.00 USD | 1,990,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2164.80` | 416,000,000.00 USD | 416,000,000.00 USD | 13,250,000.00 USD | 10,700,000.00 USD | 3,720,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 6,700,000.00 USD | 15,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2165.50` | 421,260,000.00 USD | 421,260,000.00 USD | 8,990,000.00 USD | 17,170,000.00 USD | 2,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2167.20` | 388,340,000.00 USD | 388,340,000.00 USD | 13,150,000.00 USD | 4,920,000.00 USD | 6,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2168.30` | 392,150,000.00 USD | 392,150,000.00 USD | 12,770,000.00 USD | 16,150,000.00 USD | 3,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2169.60` | 363,590,000.00 USD | 363,590,000.00 USD | 13,360,000.00 USD | 7,640,000.00 USD | 5,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2171.10` | 359,460,000.00 USD | 359,460,000.00 USD | 1,860,000.00 USD | 6,380,000.00 USD | 5,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2172.00` | 337,480,000.00 USD | 337,480,000.00 USD | 21,250,000.00 USD | 9,060,000.00 USD | 5,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2173.90` | 345,660,000.00 USD | 345,660,000.00 USD | 35,100,000.00 USD | 0.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2174.40` | 301,920,000.00 USD | 301,920,000.00 USD | 5,740,000.00 USD | 1,040,000.00 USD | 2,310,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 5,690,000.00 USD | 9,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2176.70` | 309,550,000.00 USD | 309,550,000.00 USD | 0.00 USD | 1,460,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2176.80` | 292,830,000.00 USD | 292,830,000.00 USD | 893,730.00 USD | 569,650.00 USD | 2,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2179.20` | 288,970,000.00 USD | 288,970,000.00 USD | 3,870,000.00 USD | 2,680,000.00 USD | 3,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2179.50` | 305,270,000.00 USD | 305,270,000.00 USD | 2,400,000.00 USD | 133,210.00 USD | 4,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2181.60` | 279,060,000.00 USD | 279,060,000.00 USD | 3,170,000.00 USD | 4,920,000.00 USD | 8,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2182.30` | 298,590,000.00 USD | 298,590,000.00 USD | 1,760,000.00 USD | 2,160,000.00 USD | 2,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2184.00` | 262,780,000.00 USD | 262,780,000.00 USD | 4,300,000.00 USD | 1,150,000.00 USD | 894,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2185.00` | 694,330.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `2185.10` | 292,010,000.00 USD | 292,010,000.00 USD | 41,350,000.00 USD | 20,450,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2186.40` | 256,440,000.00 USD | 256,440,000.00 USD | 4,150,000.00 USD | 2,750,000.00 USD | 4,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2187.90` | 228,920,000.00 USD | 228,920,000.00 USD | 2,370,000.00 USD | 0.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2188.80` | 244,570,000.00 USD | 244,570,000.00 USD | 4,520,000.00 USD | 5,130,000.00 USD | 9,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2190.70` | 224,950,000.00 USD | 224,950,000.00 USD | 12,430,000.00 USD | 27,960,000.00 USD | 6,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2191.20` | 225,570,000.00 USD | 225,570,000.00 USD | 6,810,000.00 USD | 4,780,000.00 USD | 3,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2193.50` | 178,130,000.00 USD | 178,130,000.00 USD | 0.00 USD | 7,340,000.00 USD | 8,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2193.60` | 210,420,000.00 USD | 210,420,000.00 USD | 5,190,000.00 USD | 4,640,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 2,250,000.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2196.00` | 199,240,000.00 USD | 199,240,000.00 USD | 8,930,000.00 USD | 1,310,000.00 USD | 5,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2196.30` | 162,680,000.00 USD | 162,680,000.00 USD | 383,690.00 USD | 243,760.00 USD | 109,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2198.40` | 183,470,000.00 USD | 183,470,000.00 USD | 271,140.00 USD | 3,690,000.00 USD | 4,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2199.10` | 161,940,000.00 USD | 161,940,000.00 USD | 0.00 USD | 1,460,000.00 USD | 7,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2200.80` | 175,360,000.00 USD | 175,360,000.00 USD | 12,080,000.00 USD | 6,470,000.00 USD | 11,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2201.90` | 153,040,000.00 USD | 153,040,000.00 USD | 9,110,000.00 USD | 266,430.00 USD | 18,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2203.20` | 144,820,000.00 USD | 144,820,000.00 USD | 12,320,000.00 USD | 14,270,000.00 USD | 16,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2204.70` | 125,030,000.00 USD | 125,030,000.00 USD | 5,350,000.00 USD | 4,330,000.00 USD | 4,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 449,420.00 USD | 455,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2205.60` | 101,890,000.00 USD | 101,890,000.00 USD | 14,550,000.00 USD | 1,530,000.00 USD | 2,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2207.50` | 110,920,000.00 USD | 110,920,000.00 USD | 19,630,000.00 USD | 3,390,000.00 USD | 3,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2208.00` | 83,430,000.00 USD | 83,430,000.00 USD | 8,730,000.00 USD | 6,940,000.00 USD | 3,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2210.30` | 84,260,000.00 USD | 84,260,000.00 USD | 4,740,000.00 USD | 0.00 USD | 11,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2210.40` | 64,510,000.00 USD | 64,510,000.00 USD | 6,870,000.00 USD | 7,030,000.00 USD | 5,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2212.80` | 45,510,000.00 USD | 45,510,000.00 USD | 8,240,000.00 USD | 5,160,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2213.10` | 68,220,000.00 USD | 68,220,000.00 USD | 1,710,000.00 USD | 1,980,000.00 USD | 8,850,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 6,540.00 USD | 6,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2215.20` | 30,130,000.00 USD | 30,130,000.00 USD | 2,150,000.00 USD | 3,720,000.00 USD | 100,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2215.90` | 55,670,000.00 USD | 55,670,000.00 USD | 0.00 USD | 0.00 USD | 565,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2217.60` | 24,150,000.00 USD | 24,150,000.00 USD | 1,010,000.00 USD | 2,470,000.00 USD | 3,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2218.70` | 55,110,000.00 USD | 55,110,000.00 USD | 22,400,000.00 USD | 487,520.00 USD | 218,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2220.00` | 16,710,000.00 USD | 16,710,000.00 USD | 6,080,000.00 USD | 2,000,000.00 USD | 3,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2221.50` | 32,010,000.00 USD | 32,010,000.00 USD | 0.00 USD | 12,220,000.00 USD | 18,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2222.40` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 4,290,000.00 USD | 883,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2224.30` | 911,920.00 USD | 911,920.00 USD | 0.00 USD | 0.00 USD | 911,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2224.80` | 468,930.00 USD | 468,930.00 USD | 374,450.00 USD | 94,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2225.00` | 1,890.00 USD | 1,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2227.10` | 8,020,000.00 USD | 8,020,000.00 USD | 557,870.00 USD | 0.00 USD | 7,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2227.20` | 5,800,000.00 USD | 5,800,000.00 USD | 0.00 USD | 0.00 USD | 5,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2229.60` | 9,950,000.00 USD | 9,950,000.00 USD | 4,040,000.00 USD | 0.00 USD | 113,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2229.90` | 29,000,000.00 USD | 29,000,000.00 USD | 1,910,000.00 USD | 0.00 USD | 19,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2232.00` | 46,740,000.00 USD | 46,740,000.00 USD | 36,380,000.00 USD | 0.00 USD | 411,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2232.70` | 29,960,000.00 USD | 29,960,000.00 USD | 0.00 USD | 0.00 USD | 959,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2235.50` | 55,210,000.00 USD | 55,210,000.00 USD | 3,260,000.00 USD | 21,640,000.00 USD | 350,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2236.80` | 53,540,000.00 USD | 53,540,000.00 USD | 6,800,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2238.30` | 69,250,000.00 USD | 69,250,000.00 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2239.20` | 61,960,000.00 USD | 61,960,000.00 USD | 8,420,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2241.10` | 101,150,000.00 USD | 101,150,000.00 USD | 31,910,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2241.60` | 62,090,000.00 USD | 62,090,000.00 USD | 81,700.00 USD | 0.00 USD | 50,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2243.90` | 103,010,000.00 USD | 103,010,000.00 USD | 1,590,000.00 USD | 268,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2244.00` | 64,070,000.00 USD | 64,070,000.00 USD | 381,040.00 USD | 569,860.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2245.00` | 2,570.00 USD | 4,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2246.40` | 84,970,000.00 USD | 84,970,000.00 USD | 10,100,000.00 USD | 5,170,000.00 USD | 5,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2246.70` | 120,040,000.00 USD | 120,040,000.00 USD | 6,720,000.00 USD | 1,300,000.00 USD | 9,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2248.80` | 102,270,000.00 USD | 102,270,000.00 USD | 3,390,000.00 USD | 7,130,000.00 USD | 6,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2249.50` | 130,630,000.00 USD | 130,630,000.00 USD | 2,960,000.00 USD | 6,990,000.00 USD | 640,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2251.20` | 111,900,000.00 USD | 111,900,000.00 USD | 8,050,000.00 USD | 1,470,000.00 USD | 112,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2252.30` | 152,350,000.00 USD | 152,350,000.00 USD | 10,050,000.00 USD | 11,670,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2253.60` | 120,690,000.00 USD | 120,690,000.00 USD | 893,130.00 USD | 4,250,000.00 USD | 3,650,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2255.00` | 20,070.00 USD | 24,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2255.10` | 169,510,000.00 USD | 169,510,000.00 USD | 10,050,000.00 USD | 6,600,000.00 USD | 514,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2256.00` | 161,360,000.00 USD | 161,360,000.00 USD | 24,390,000.00 USD | 8,790,000.00 USD | 7,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2257.90` | 209,210,000.00 USD | 209,210,000.00 USD | 20,510,000.00 USD | 12,290,000.00 USD | 6,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2258.40` | 179,910,000.00 USD | 179,910,000.00 USD | 10,470,000.00 USD | 6,170,000.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2260.70` | 213,530,000.00 USD | 213,530,000.00 USD | 0.00 USD | 0.00 USD | 4,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2260.80` | 200,880,000.00 USD | 200,880,000.00 USD | 9,590,000.00 USD | 8,980,000.00 USD | 2,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2263.20` | 233,160,000.00 USD | 233,160,000.00 USD | 14,560,000.00 USD | 9,680,000.00 USD | 8,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2263.50` | 221,920,000.00 USD | 221,920,000.00 USD | 6,720,000.00 USD | 1,460,000.00 USD | 218,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2265.00` | 93,510.00 USD | 118,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2265.60` | 255,320,000.00 USD | 255,320,000.00 USD | 3,050,000.00 USD | 8,620,000.00 USD | 10,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2266.30` | 236,420,000.00 USD | 236,420,000.00 USD | 0.00 USD | 8,160,000.00 USD | 6,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2268.00` | 302,170,000.00 USD | 302,170,000.00 USD | 19,350,000.00 USD | 12,270,000.00 USD | 15,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2269.10` | 265,720,000.00 USD | 265,720,000.00 USD | 11,010,000.00 USD | 133,210.00 USD | 18,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2270.40` | 337,640,000.00 USD | 337,640,000.00 USD | 11,440,000.00 USD | 9,960,000.00 USD | 14,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2271.90` | 294,510,000.00 USD | 294,510,000.00 USD | 18,240,000.00 USD | 3,640,000.00 USD | 6,900,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2272.80` | 364,190,000.00 USD | 364,190,000.00 USD | 16,290,000.00 USD | 4,780,000.00 USD | 5,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2274.70` | 321,040,000.00 USD | 321,040,000.00 USD | 19,630,000.00 USD | 6,900,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2275.00` | 828,610.00 USD | 946,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2275.20` | 409,430,000.00 USD | 409,430,000.00 USD | 26,530,000.00 USD | 15,130,000.00 USD | 3,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2277.50` | 347,290,000.00 USD | 347,290,000.00 USD | 6,890,000.00 USD | 8,890,000.00 USD | 10,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2277.60` | 445,250,000.00 USD | 445,250,000.00 USD | 10,430,000.00 USD | 13,450,000.00 USD | 11,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2280.00` | 494,390,000.00 USD | 494,390,000.00 USD | 27,480,000.00 USD | 9,610,000.00 USD | 12,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2280.30` | 391,610,000.00 USD | 391,610,000.00 USD | 854,200.00 USD | 39,830,000.00 USD | 3,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2282.40` | 552,950,000.00 USD | 552,950,000.00 USD | 26,180,000.00 USD | 25,320,000.00 USD | 7,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2283.10` | 483,430,000.00 USD | 483,430,000.00 USD | 5,600,000.00 USD | 72,520,000.00 USD | 13,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2284.80` | 577,210,000.00 USD | 577,210,000.00 USD | 9,270,000.00 USD | 7,750,000.00 USD | 7,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2285.00` | 490,730.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2285.90` | 487,130,000.00 USD | 487,130,000.00 USD | 1,010,000.00 USD | 2,590,000.00 USD | 109,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2287.20` | 609,210,000.00 USD | 609,210,000.00 USD | 13,140,000.00 USD | 10,580,000.00 USD | 8,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2288.70` | 519,770,000.00 USD | 519,770,000.00 USD | 8,380,000.00 USD | 9,320,000.00 USD | 14,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2289.60` | 631,990,000.00 USD | 631,990,000.00 USD | 5,630,000.00 USD | 13,110,000.00 USD | 4,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2291.50` | 531,640,000.00 USD | 531,640,000.00 USD | 4,310,000.00 USD | 517,070.00 USD | 7,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2292.00` | 664,760,000.00 USD | 664,760,000.00 USD | 18,640,000.00 USD | 5,470,000.00 USD | 8,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2294.30` | 552,980,000.00 USD | 552,980,000.00 USD | 14,670,000.00 USD | 1,490,000.00 USD | 5,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2294.40` | 697,400,000.00 USD | 697,400,000.00 USD | 16,220,000.00 USD | 6,680,000.00 USD | 9,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2295.00` | 2,920,000.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2296.80` | 738,930,000.00 USD | 738,930,000.00 USD | 21,130,000.00 USD | 13,050,000.00 USD | 7,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2297.10` | 602,730,000.00 USD | 602,730,000.00 USD | 25,900,000.00 USD | 8,070,000.00 USD | 15,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2299.20` | 788,390,000.00 USD | 788,390,000.00 USD | 19,620,000.00 USD | 16,130,000.00 USD | 13,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2299.90` | 645,650,000.00 USD | 645,650,000.00 USD | 16,200,000.00 USD | 20,940,000.00 USD | 5,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2301.60` | 815,450,000.00 USD | 815,450,000.00 USD | 13,720,000.00 USD | 6,010,000.00 USD | 7,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2302.70` | 700,310,000.00 USD | 700,310,000.00 USD | 26,960,000.00 USD | 10,860,000.00 USD | 16,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2304.00` | 842,290,000.00 USD | 842,290,000.00 USD | 12,680,000.00 USD | 11,040,000.00 USD | 3,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2305.00` | 448,140.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2305.50` | 726,330,000.00 USD | 726,330,000.00 USD | 6,340,000.00 USD | 8,820,000.00 USD | 10,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2306.40` | 876,630,000.00 USD | 876,630,000.00 USD | 13,770,000.00 USD | 11,600,000.00 USD | 8,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2308.30` | 728,630,000.00 USD | 728,630,000.00 USD | 1,240,000.00 USD | 930,630.00 USD | 134,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2308.80` | 882,150,000.00 USD | 882,150,000.00 USD | 67,780.00 USD | 3,530,000.00 USD | 1,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2311.10` | 759,130,000.00 USD | 759,130,000.00 USD | 11,560,000.00 USD | 2,790,000.00 USD | 16,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2311.20` | 898,140,000.00 USD | 898,140,000.00 USD | 6,180,000.00 USD | 664,440.00 USD | 9,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2313.60` | 918,050,000.00 USD | 918,050,000.00 USD | 7,180,000.00 USD | 9,020,000.00 USD | 3,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2313.90` | 769,950,000.00 USD | 769,950,000.00 USD | 1,100,000.00 USD | 7,460,000.00 USD | 2,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2315.00` | 824,210.00 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2316.00` | 951,730,000.00 USD | 951,730,000.00 USD | 10,470,000.00 USD | 16,140,000.00 USD | 7,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2316.70` | 775,650,000.00 USD | 775,650,000.00 USD | 1,020,000.00 USD | 3,640,000.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2318.40` | 967,080,000.00 USD | 967,080,000.00 USD | 6,250,000.00 USD | 6,890,000.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2319.50` | 804,920,000.00 USD | 804,920,000.00 USD | 5,530,000.00 USD | 15,850,000.00 USD | 7,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2320.80` | 987,270,000.00 USD | 987,270,000.00 USD | 5,860,000.00 USD | 11,510,000.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2322.30` | 810,780,000.00 USD | 810,780,000.00 USD | 2,300,000.00 USD | 3,450,000.00 USD | 108,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2323.20` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 4,360,000.00 USD | 12,070,000.00 USD | 4,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2325.00` | 3,250,000.00 USD | 8,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2325.10` | 833,810,000.00 USD | 833,810,000.00 USD | 10,150,000.00 USD | 2,770,000.00 USD | 10,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2325.60` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 2,050,000.00 USD | 6,780,000.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2327.90` | 845,700,000.00 USD | 845,700,000.00 USD | 3,860,000.00 USD | 0.00 USD | 8,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2328.00` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 494,310.00 USD | 1,240,000.00 USD | 4,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2330.40` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 12,440,000.00 USD | 3,110,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2330.70` | 861,920,000.00 USD | 861,920,000.00 USD | 15,800,000.00 USD | 363,770.00 USD | 54,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2332.80` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 2,710,000.00 USD | 3,280,000.00 USD | 9,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2333.50` | 903,010,000.00 USD | 903,010,000.00 USD | 20,270,000.00 USD | 12,860,000.00 USD | 7,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2335.00` | 437,940.00 USD | 9,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2335.20` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 12,310,000.00 USD | 3,870,000.00 USD | 2,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2336.30` | 940,270,000.00 USD | 940,270,000.00 USD | 24,310,000.00 USD | 7,570,000.00 USD | 5,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2337.60` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 7,940,000.00 USD | 1,180,000.00 USD | 5,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2339.10` | 966,680,000.00 USD | 966,680,000.00 USD | 14,040,000.00 USD | 0.00 USD | 12,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2340.00` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 10,960,000.00 USD | 6,260,000.00 USD | 12,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2341.90` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 8,610,000.00 USD | 17,820,000.00 USD | 14,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2342.40` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 8,100,000.00 USD | 3,720,000.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2344.70` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 2,480,000.00 USD | 16,920,000.00 USD | 8,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2344.80` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 3,570,000.00 USD | 8,550,000.00 USD | 6,450,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2345.00` | 415,460.00 USD | 9,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2347.20` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 4,320,000.00 USD | 3,860,000.00 USD | 4,750,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2347.50` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 8,220,000.00 USD | 18,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2349.60` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 17,010,000.00 USD | 6,360,000.00 USD | 6,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2350.30` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 1,630,000.00 USD | 20,110,000.00 USD | 15,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2352.00` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 15,870,000.00 USD | 1,960,000.00 USD | 6,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2353.10` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 2,710,000.00 USD | 35,770,000.00 USD | 4,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2354.40` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 1,340,000.00 USD | 5,600,000.00 USD | 955,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 2,440,000.00 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2355.90` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 18,560,000.00 USD | 10,720,000.00 USD | 3,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2356.80` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 4,660,000.00 USD | 1,670,000.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2358.70` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 6,870,000.00 USD | 512,220.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2359.20` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 6,320,000.00 USD | 5,050,000.00 USD | 7,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2361.50` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 3,150,000.00 USD | 3,430,000.00 USD | 374,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2361.60` | 1,270,000,000.00 USD | 1,270,000,000.00 USD | 7,760,000.00 USD | 8,680,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2364.00` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 5,570,000.00 USD | 3,140,000.00 USD | 9,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2364.30` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 3,860,000.00 USD | 373,740.00 USD | 10,920,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 4,860,000.00 USD | 17,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2366.40` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 3,150,000.00 USD | 509,320.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2367.10` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 6,340,000.00 USD | 1,310,000.00 USD | 307,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2368.80` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 6,840,000.00 USD | 4,420,000.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2369.90` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 24,940,000.00 USD | 475,460.00 USD | 18,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2371.20` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 13,620,000.00 USD | 6,300,000.00 USD | 4,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2372.70` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 15,600,000.00 USD | 0.00 USD | 39,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2373.60` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 12,630,000.00 USD | 1,100,000.00 USD | 5,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 893,040.00 USD | 17,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2375.50` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 9,700,000.00 USD | 1,050,000.00 USD | 11,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2376.00` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 5,100,000.00 USD | 2,750,000.00 USD | 4,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2378.30` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 11,180,000.00 USD | 7,020,000.00 USD | 23,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2378.40` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 1,650,000.00 USD | 1,010,000.00 USD | 3,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2380.80` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 6,120,000.00 USD | 6,700,000.00 USD | 5,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2381.10` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 4,540,000.00 USD | 2,390,000.00 USD | 16,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2383.20` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 16,070,000.00 USD | 9,480,000.00 USD | 10,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2383.90` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 8,840,000.00 USD | 21,750,000.00 USD | 30,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 722,850.00 USD | 18,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2385.60` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 7,170,000.00 USD | 10,450,000.00 USD | 3,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2386.70` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 17,720,000.00 USD | 32,140,000.00 USD | 42,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2388.00` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 10,740,000.00 USD | 5,690,000.00 USD | 2,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2389.50` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 5,670,000.00 USD | 35,860,000.00 USD | 28,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2390.40` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 3,450,000.00 USD | 3,360,000.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2392.30` | 1,740,000,000.00 USD | 1,740,000,000.00 USD | 26,840,000.00 USD | 45,530,000.00 USD | 39,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2392.80` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 2,700,000.00 USD | 3,990,000.00 USD | 3,320,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 4,850,000.00 USD | 23,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2395.10` | 1,830,000,000.00 USD | 1,830,000,000.00 USD | 39,180,000.00 USD | 24,870,000.00 USD | 29,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2395.20` | 1,490,000,000.00 USD | 1,490,000,000.00 USD | 2,060,000.00 USD | 1,450,000.00 USD | 2,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2397.60` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 64,150.00 USD | 3,720,000.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2397.90` | 1,930,000,000.00 USD | 1,930,000,000.00 USD | 34,290,000.00 USD | 36,430,000.00 USD | 23,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2400.00` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 2,150,000.00 USD | 637,690.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2400.70` | 2,020,000,000.00 USD | 2,020,000,000.00 USD | 42,030,000.00 USD | 25,390,000.00 USD | 24,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2402.40` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 1,140,000.00 USD | 315,710.00 USD | 552,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2403.50` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 51,300,000.00 USD | 24,760,000.00 USD | 30,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2404.80` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 5,960,000.00 USD | 3,440,000.00 USD | 4,950,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 115,180.00 USD | 23,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2406.30` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 29,700,000.00 USD | 33,710,000.00 USD | 14,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2407.20` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 6,810,000.00 USD | 3,470,000.00 USD | 1,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2409.10` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 25,090,000.00 USD | 21,480,000.00 USD | 27,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2409.60` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 4,520,000.00 USD | 3,640,000.00 USD | 3,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2411.90` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 15,970,000.00 USD | 21,640,000.00 USD | 13,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2412.00` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 5,230,000.00 USD | 3,230,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2414.40` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 1,120,000.00 USD | 1,600,000.00 USD | 1,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2414.70` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 22,250,000.00 USD | 19,630,000.00 USD | 21,720,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 236,460.00 USD | 23,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2416.80` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 2,870,000.00 USD | 1,460,000.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2417.50` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 22,310,000.00 USD | 8,700,000.00 USD | 21,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2419.20` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 4,780,000.00 USD | 2,560,000.00 USD | 2,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2420.30` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 29,980,000.00 USD | 18,780,000.00 USD | 9,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2421.60` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 4,170,000.00 USD | 3,820,000.00 USD | 4,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2423.10` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 17,920,000.00 USD | 17,260,000.00 USD | 17,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2424.00` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 220,740.00 USD | 1,180,000.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 289,470.00 USD | 24,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2425.90` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 12,980,000.00 USD | 15,310,000.00 USD | 17,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2426.40` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 2,090,000.00 USD | 1,100,000.00 USD | 40,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2428.70` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 12,800,000.00 USD | 7,090,000.00 USD | 8,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2428.80` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 670,680.00 USD | 918,390.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2431.20` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 3,120,000.00 USD | 2,330,000.00 USD | 664,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2431.50` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 9,420,000.00 USD | 12,660,000.00 USD | 8,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2433.60` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 1,770,000.00 USD | 1,450,000.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2434.30` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 13,090,000.00 USD | 3,830,000.00 USD | 3,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 197,400.00 USD | 24,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2436.00` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 2,490,000.00 USD | 1,070,000.00 USD | 161,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2437.10` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 7,130,000.00 USD | 7,440,000.00 USD | 6,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2438.40` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 476,020.00 USD | 535,870.00 USD | 15,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2439.90` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 12,730,000.00 USD | 4,970,000.00 USD | 3,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2440.80` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 2,260,000.00 USD | 723,100.00 USD | 858,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2442.70` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 5,050,000.00 USD | 5,320,000.00 USD | 7,900,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2443.20` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 27,360.00 USD | 455,640.00 USD | 747,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 4,800,000.00 USD | 29,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2445.50` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 9,990,000.00 USD | 7,470,000.00 USD | 10,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2445.60` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 438,650.00 USD | 291,150.00 USD | 908,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2448.00` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 975,830.00 USD | 989,540.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2448.30` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 10,750,000.00 USD | 3,770,000.00 USD | 13,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2450.40` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 1,980,000.00 USD | 69,580.00 USD | 26,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2451.10` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 8,450,000.00 USD | 7,240,000.00 USD | 7,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2452.80` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 2,460,000.00 USD | 1,840,000.00 USD | 2,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2453.90` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 4,220,000.00 USD | 2,980,000.00 USD | 3,870,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 214,400.00 USD | 29,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2455.20` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 1,640,000.00 USD | 1,990,000.00 USD | 905,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2456.70` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 8,340,000.00 USD | 7,380,000.00 USD | 7,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2457.60` | 1,640,000,000.00 USD | 1,640,000,000.00 USD | 1,700,000.00 USD | 1,840,000.00 USD | 841,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2459.50` | 1,640,000,000.00 USD | 1,640,000,000.00 USD | 1,200,000.00 USD | 1,300,000.00 USD | 366,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2459.50` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 3,220,000.00 USD | 4,870,000.00 USD | 6,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2462.30` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 6,600,000.00 USD | 5,990,000.00 USD | 5,150,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 11,550,000.00 USD | 40,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2465.10` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 4,900,000.00 USD | 3,130,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2467.90` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 2,900,000.00 USD | 1,870,000.00 USD | 23,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2470.70` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 3,960,000.00 USD | 2,050,000.00 USD | 522,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2473.50` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 5,300,000.00 USD | 2,920,000.00 USD | 3,180,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 54,770,000.00 USD | 95,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2476.30` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 2,070,000.00 USD | 1,710,000.00 USD | 872,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2479.10` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 3,070,000.00 USD | 4,130,000.00 USD | 540,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2481.90` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 601,420.00 USD | 3,680,000.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2484.70` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 1,650,000.00 USD | 97,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2487.50` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 275,450.00 USD | 211,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2490.30` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 338,890.00 USD | 286,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2491.80` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 2,580,000.00 USD | 733,870.00 USD | 445,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 2,150,000.00 USD | 99,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2505.00` | 4,470,000.00 USD | 103,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2515.00` | 1,590,000.00 USD | 105,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2525.00` | 46,400.00 USD | 105,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2535.00` | 1,060,000.00 USD | 106,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2545.00` | 5,040,000.00 USD | 111,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2555.00` | 238,660.00 USD | 111,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2565.00` | 89,050.00 USD | 112,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2575.00` | 559,600.00 USD | 112,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2585.00` | 34,310,000.00 USD | 146,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2595.00` | 359,640.00 USD | 147,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2605.00` | 5,810,000.00 USD | 153,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2615.00` | 732,830.00 USD | 153,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2625.00` | 45,410,000.00 USD | 199,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2635.00` | 1,030,000.00 USD | 200,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2645.00` | 626,810.00 USD | 200,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2655.00` | 26,820,000.00 USD | 227,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2665.00` | 51,540.00 USD | 227,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2675.00` | 1,100,000.00 USD | 228,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2685.00` | 23,200.00 USD | 228,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2695.00` | 468,980.00 USD | 229,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2705.00` | 698,920.00 USD | 230,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2715.00` | 413,400.00 USD | 230,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2725.00` | 229,610.00 USD | 230,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2735.00` | 5,150,000.00 USD | 235,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2745.00` | 13,790,000.00 USD | 249,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2755.00` | 5,050,000.00 USD | 254,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2765.00` | 416,000.00 USD | 255,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2775.00` | 25,170,000.00 USD | 280,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2785.00` | 528,660.00 USD | 280,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2795.00` | 5,560,000.00 USD | 286,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2805.00` | 5,930,000.00 USD | 292,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2815.00` | 2,010,000.00 USD | 294,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2825.00` | 133,850.00 USD | 294,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2835.00` | 6,280,000.00 USD | 300,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2845.00` | 349,690.00 USD | 301,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2855.00` | 502,140.00 USD | 301,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2865.00` | 422,840.00 USD | 301,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2875.00` | 64,240.00 USD | 302,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2885.00` | 1,740,000.00 USD | 303,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2895.00` | 1,340,000.00 USD | 305,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2905.00` | 44,390,000.00 USD | 349,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2915.00` | 2,350,000.00 USD | 351,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2925.00` | 3,030,000.00 USD | 354,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2935.00` | 67,460.00 USD | 354,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2945.00` | 437,030.00 USD | 355,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2955.00` | 4,570,000.00 USD | 359,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2965.00` | 590,570.00 USD | 360,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2975.00` | 3,360,000.00 USD | 363,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2985.00` | 1,240,000.00 USD | 365,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2995.00` | 15,030,000.00 USD | 380,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3005.00` | 646,430.00 USD | 380,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3015.00` | 175,020.00 USD | 380,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3025.00` | 862,710.00 USD | 381,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3035.00` | 15,030,000.00 USD | 396,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3045.00` | 715,260.00 USD | 397,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3055.00` | 6,520.00 USD | 397,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3065.00` | 1,510,000.00 USD | 399,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3075.00` | 6,070,000.00 USD | 405,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3085.00` | 10,930,000.00 USD | 416,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3095.00` | 5,780,000.00 USD | 421,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3105.00` | 12,290,000.00 USD | 434,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3115.00` | 33,880,000.00 USD | 468,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3125.00` | 1,870,000.00 USD | 469,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3135.00` | 261,240.00 USD | 470,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3145.00` | 401,090.00 USD | 470,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3155.00` | 222,300.00 USD | 470,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3165.00` | 130,620.00 USD | 470,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3175.00` | 1,090,000.00 USD | 472,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3185.00` | 70,660,000.00 USD | 542,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3195.00` | 210,270.00 USD | 542,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3205.00` | 352,030.00 USD | 543,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3215.00` | 175,220.00 USD | 543,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3225.00` | 8,340,000.00 USD | 551,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3235.00` | 9,760,000.00 USD | 561,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3245.00` | 4,850,000.00 USD | 566,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3255.00` | 12,810.00 USD | 566,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3265.00` | 65,860.00 USD | 566,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3275.00` | 10,830,000.00 USD | 577,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3285.00` | 65,540.00 USD | 577,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3295.00` | 334,070.00 USD | 577,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3305.00` | 1,270,000.00 USD | 578,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3315.00` | 2,120,000.00 USD | 581,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3325.00` | 75,050.00 USD | 581,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3335.00` | 1,480,000.00 USD | 582,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3345.00` | 58,000.00 USD | 582,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3355.00` | 2,050,000.00 USD | 584,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3365.00` | 2,970,000.00 USD | 587,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3375.00` | 2,430,000.00 USD | 590,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3385.00` | 102,540.00 USD | 590,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3395.00` | 93,920.00 USD | 590,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3405.00` | 1,270,000.00 USD | 591,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3415.00` | 4,200,000.00 USD | 595,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3425.00` | 14,590,000.00 USD | 610,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3435.00` | 95,600.00 USD | 610,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3445.00` | 881,390.00 USD | 611,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3455.00` | 559,510.00 USD | 611,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3465.00` | 424,610.00 USD | 612,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3475.00` | 55,090.00 USD | 612,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3485.00` | 30,100.00 USD | 612,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3495.00` | 1,170,000.00 USD | 613,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3505.00` | 1,640,000.00 USD | 615,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3515.00` | 375,650.00 USD | 615,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3525.00` | 765,100.00 USD | 616,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3535.00` | 14,830,000.00 USD | 631,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3545.00` | 97,280.00 USD | 631,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3555.00` | 119,970.00 USD | 631,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3565.00` | 125,810.00 USD | 631,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3575.00` | 80,980.00 USD | 631,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3585.00` | 749,130.00 USD | 632,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3595.00` | 43,700.00 USD | 632,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3605.00` | 62,790.00 USD | 632,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3615.00` | 3,790,000.00 USD | 636,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3625.00` | 1,120,000.00 USD | 637,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3635.00` | 8,820,000.00 USD | 646,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3645.00` | 53,550,000.00 USD | 699,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3655.00` | 37,050.00 USD | 699,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3665.00` | 343,720.00 USD | 700,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3675.00` | 6,540,000.00 USD | 706,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3685.00` | 212,010.00 USD | 706,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3695.00` | 31,030.00 USD | 706,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3705.00` | 3,860,000.00 USD | 710,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3715.00` | 2,920.00 USD | 710,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3725.00` | 382,870,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3735.00` | 360,220.00 USD | 1,090,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3745.00` | 2,710,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3755.00` | 163,780.00 USD | 1,100,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3765.00` | 78,340.00 USD | 1,100,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3775.00` | 456,790.00 USD | 1,100,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3785.00` | 59,410,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3795.00` | 3,470,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3805.00` | 4,850,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3815.00` | 1,590.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3825.00` | 34,550.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3835.00` | 280,720.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3845.00` | 212,940.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3855.00` | 1,050,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3865.00` | 2,480,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3875.00` | 93,260.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3885.00` | 1,360,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3895.00` | 2,490,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3905.00` | 38,870,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3915.00` | 553,260.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3925.00` | 152,270.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3935.00` | 2,640.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3945.00` | 88,480.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3955.00` | 1,660.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3965.00` | 30,880.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3975.00` | 160,630.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3985.00` | 178,550.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3995.00` | 562,130.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4005.00` | 141,730.00 USD | 1,210,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4015.00` | 1,230,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4025.00` | 490,570.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4035.00` | 414,520.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4045.00` | 121,110.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4055.00` | 1,690,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4065.00` | 1,200,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4075.00` | 129,220.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4085.00` | 91,390.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4095.00` | 207,480.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4105.00` | 1,150,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4115.00` | 129,580.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4125.00` | 151,430.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4135.00` | 608,480.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4145.00` | 99,240.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4155.00` | 681,920.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4165.00` | 132,850.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4175.00` | 209,470.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4185.00` | 948,630.00 USD | 1,220,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4195.00` | 32,730,000.00 USD | 1,260,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4205.00` | 42,140.00 USD | 1,260,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4215.00` | 42,320.00 USD | 1,260,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4225.00` | 801,540.00 USD | 1,260,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4235.00` | 83,560,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4245.00` | 335,020.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4255.00` | 420.39 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4265.00` | 2,170,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4275.00` | 4,060.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4285.00` | 2,450.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4295.00` | 15,180.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4305.00` | 17,120.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4315.00` | 50,390.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4325.00` | 36,530.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4335.00` | 32,800.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4345.00` | 204,690.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4355.00` | 6,930.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4365.00` | 1,140,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4375.00` | 19,130.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4385.00` | 4,180.00 USD | 1,340,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4395.00` | 615,700.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4405.00` | 23,210.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4415.00` | 129,550.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4425.00` | 8,230.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4435.00` | 73,170.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4445.00` | 25,610.00 USD | 1,350,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `445.00` | 786,770,000.00 USD | 0.00 USD | 75,450.00 USD | `-79.99%` | `169.56` |
| `Live` | `Long` | `455.00` | 786,690,000.00 USD | 0.00 USD | 121,330.00 USD | `-79.54%` | `266.65` |
| `Live` | `Long` | `465.00` | 786,570,000.00 USD | 0.00 USD | 118,030.00 USD | `-79.09%` | `253.83` |
| `Live` | `Long` | `475.00` | 786,450,000.00 USD | 0.00 USD | 81,110.00 USD | `-78.64%` | `170.75` |
| `Live` | `Long` | `485.00` | 786,370,000.00 USD | 0.00 USD | 2,960.00 USD | `-78.20%` | `6.10` |
| `Live` | `Long` | `495.00` | 786,370,000.00 USD | 0.00 USD | 140,880.00 USD | `-77.75%` | `284.60` |
| `Live` | `Long` | `505.00` | 786,230,000.00 USD | 0.00 USD | 67,370.00 USD | `-77.30%` | `133.41` |
| `Live` | `Long` | `515.00` | 786,160,000.00 USD | 0.00 USD | 39,200.00 USD | `-76.85%` | `76.11` |
| `Live` | `Long` | `525.00` | 786,120,000.00 USD | 0.00 USD | 1,870,000.00 USD | `-76.40%` | `3,559.73` |
| `Live` | `Long` | `535.00` | 784,250,000.00 USD | 0.00 USD | 34,560.00 USD | `-75.95%` | `64.60` |
| `Live` | `Long` | `545.00` | 784,220,000.00 USD | 0.00 USD | 53,010.00 USD | `-75.50%` | `97.27` |
| `Live` | `Long` | `555.00` | 784,160,000.00 USD | 0.00 USD | 66,580.00 USD | `-75.05%` | `119.97` |
| `Live` | `Long` | `565.00` | 784,100,000.00 USD | 0.00 USD | 158,160.00 USD | `-74.60%` | `279.93` |
| `Live` | `Long` | `575.00` | 783,940,000.00 USD | 0.00 USD | 64,830.00 USD | `-74.15%` | `112.75` |
| `Live` | `Long` | `585.00` | 783,870,000.00 USD | 0.00 USD | 44,160.00 USD | `-73.70%` | `75.49` |
| `Live` | `Long` | `595.00` | 783,830,000.00 USD | 0.00 USD | 3,330,000.00 USD | `-73.25%` | `5,604.18` |
| `Live` | `Long` | `605.00` | 780,490,000.00 USD | 0.00 USD | 154,720.00 USD | `-72.80%` | `255.73` |
| `Live` | `Long` | `615.00` | 780,340,000.00 USD | 0.00 USD | 142,040.00 USD | `-72.35%` | `230.97` |
| `Live` | `Long` | `625.00` | 780,200,000.00 USD | 0.00 USD | 1,880,000.00 USD | `-71.90%` | `3,012.16` |
| `Live` | `Long` | `635.00` | 778,310,000.00 USD | 0.00 USD | 51,410.00 USD | `-71.45%` | `80.96` |
| `Live` | `Long` | `645.00` | 778,260,000.00 USD | 0.00 USD | 1,150,000.00 USD | `-71.00%` | `1,776.04` |
| `Live` | `Long` | `655.00` | 777,120,000.00 USD | 0.00 USD | 46,320.00 USD | `-70.55%` | `70.72` |
| `Live` | `Long` | `665.00` | 777,070,000.00 USD | 0.00 USD | 54,620.00 USD | `-70.10%` | `82.13` |
| `Live` | `Long` | `675.00` | 777,020,000.00 USD | 0.00 USD | 46,090.00 USD | `-69.65%` | `68.28` |
| `Live` | `Long` | `685.00` | 776,970,000.00 USD | 0.00 USD | 44,110.00 USD | `-69.20%` | `64.39` |
| `Live` | `Long` | `695.00` | 776,930,000.00 USD | 0.00 USD | 2,640.00 USD | `-68.75%` | `3.80` |
| `Live` | `Long` | `705.00` | 776,920,000.00 USD | 0.00 USD | 15,790.00 USD | `-68.30%` | `22.40` |
| `Live` | `Long` | `715.00` | 776,910,000.00 USD | 0.00 USD | 54,550.00 USD | `-67.86%` | `76.30` |
| `Live` | `Long` | `725.00` | 776,850,000.00 USD | 0.00 USD | 1,080,000.00 USD | `-67.41%` | `1,484.42` |
| `Live` | `Long` | `735.00` | 775,780,000.00 USD | 0.00 USD | 78,630.00 USD | `-66.96%` | `106.98` |
| `Live` | `Long` | `745.00` | 775,700,000.00 USD | 0.00 USD | 9,220.00 USD | `-66.51%` | `12.38` |
| `Live` | `Long` | `755.00` | 775,690,000.00 USD | 0.00 USD | 55,210.00 USD | `-66.06%` | `73.12` |
| `Live` | `Long` | `765.00` | 775,630,000.00 USD | 0.00 USD | 5,250.00 USD | `-65.61%` | `6.87` |
| `Live` | `Long` | `775.00` | 775,630,000.00 USD | 0.00 USD | 72,970.00 USD | `-65.16%` | `94.15` |
| `Live` | `Long` | `785.00` | 775,560,000.00 USD | 0.00 USD | 16,550.00 USD | `-64.71%` | `21.08` |
| `Live` | `Long` | `795.00` | 775,540,000.00 USD | 0.00 USD | 6,010.00 USD | `-64.26%` | `7.56` |
| `Live` | `Long` | `805.00` | 775,530,000.00 USD | 0.00 USD | 85,220.00 USD | `-63.81%` | `105.86` |
| `Live` | `Long` | `815.00` | 775,450,000.00 USD | 0.00 USD | 95,130.00 USD | `-63.36%` | `116.72` |
| `Live` | `Long` | `825.00` | 775,350,000.00 USD | 0.00 USD | 129,310.00 USD | `-62.91%` | `156.74` |
| `Live` | `Long` | `835.00` | 775,220,000.00 USD | 0.00 USD | 62,560.00 USD | `-62.46%` | `74.92` |
| `Live` | `Long` | `845.00` | 775,160,000.00 USD | 0.00 USD | 375,830.00 USD | `-62.01%` | `444.77` |
| `Live` | `Long` | `855.00` | 774,790,000.00 USD | 0.00 USD | 214,080.00 USD | `-61.56%` | `250.39` |
| `Live` | `Long` | `865.00` | 774,570,000.00 USD | 0.00 USD | 17,290.00 USD | `-61.11%` | `19.99` |
| `Live` | `Long` | `875.00` | 774,550,000.00 USD | 0.00 USD | 88,960.00 USD | `-60.66%` | `101.67` |
| `Live` | `Long` | `885.00` | 774,470,000.00 USD | 0.00 USD | 964,270.00 USD | `-60.21%` | `1,089.58` |
| `Live` | `Long` | `895.00` | 773,500,000.00 USD | 0.00 USD | 175,070.00 USD | `-59.76%` | `195.60` |
| `Live` | `Long` | `905.00` | 773,330,000.00 USD | 0.00 USD | 18,280.00 USD | `-59.31%` | `20.20` |
| `Live` | `Long` | `915.00` | 773,310,000.00 USD | 0.00 USD | 605,510.00 USD | `-58.86%` | `661.76` |
| `Live` | `Long` | `925.00` | 772,700,000.00 USD | 0.00 USD | 164,030.00 USD | `-58.41%` | `177.33` |
| `Live` | `Long` | `935.00` | 772,540,000.00 USD | 0.00 USD | 297,070.00 USD | `-57.96%` | `317.72` |
| `Live` | `Long` | `945.00` | 772,240,000.00 USD | 0.00 USD | 91,310.00 USD | `-57.51%` | `96.63` |
| `Live` | `Long` | `955.00` | 772,150,000.00 USD | 0.00 USD | 294,230.00 USD | `-57.07%` | `308.09` |
| `Live` | `Long` | `965.00` | 771,860,000.00 USD | 0.00 USD | 47,900.00 USD | `-56.62%` | `49.64` |
| `Live` | `Long` | `975.00` | 771,810,000.00 USD | 0.00 USD | 183,680.00 USD | `-56.17%` | `188.39` |
| `Live` | `Long` | `985.00` | 771,620,000.00 USD | 0.00 USD | 105,940.00 USD | `-55.72%` | `107.55` |
| `Live` | `Long` | `995.00` | 771,520,000.00 USD | 0.00 USD | 336,130.00 USD | `-55.27%` | `337.82` |
| `Live` | `Long` | `1005.00` | 771,180,000.00 USD | 0.00 USD | 113,820.00 USD | `-54.82%` | `113.26` |
| `Live` | `Long` | `1015.00` | 771,070,000.00 USD | 0.00 USD | 155,360.00 USD | `-54.37%` | `153.07` |
| `Live` | `Long` | `1025.00` | 770,910,000.00 USD | 0.00 USD | 63,130.00 USD | `-53.92%` | `61.59` |
| `Live` | `Long` | `1035.00` | 770,850,000.00 USD | 0.00 USD | 60,140.00 USD | `-53.47%` | `58.10` |
| `Live` | `Long` | `1045.00` | 770,790,000.00 USD | 0.00 USD | 702,780.00 USD | `-53.02%` | `672.51` |
| `Live` | `Long` | `1055.00` | 770,090,000.00 USD | 0.00 USD | 7,410,000.00 USD | `-52.57%` | `7,023.20` |
| `Live` | `Long` | `1065.00` | 762,680,000.00 USD | 0.00 USD | 557,690.00 USD | `-52.12%` | `523.66` |
| `Live` | `Long` | `1075.00` | 762,120,000.00 USD | 0.00 USD | 721,980.00 USD | `-51.67%` | `671.61` |
| `Live` | `Long` | `1085.00` | 761,400,000.00 USD | 0.00 USD | 1,890,000.00 USD | `-51.22%` | `1,741.70` |
| `Live` | `Long` | `1095.00` | 759,510,000.00 USD | 0.00 USD | 676,930.00 USD | `-50.77%` | `618.20` |
| `Live` | `Long` | `1105.00` | 758,830,000.00 USD | 0.00 USD | 217,450.00 USD | `-50.32%` | `196.79` |
| `Live` | `Long` | `1115.00` | 758,610,000.00 USD | 0.00 USD | 206,920.00 USD | `-49.87%` | `185.58` |
| `Live` | `Long` | `1125.00` | 758,410,000.00 USD | 0.00 USD | 7,930,000.00 USD | `-49.42%` | `7,046.35` |
| `Live` | `Long` | `1135.00` | 750,480,000.00 USD | 0.00 USD | 86,940.00 USD | `-48.97%` | `76.60` |
| `Live` | `Long` | `1145.00` | 750,390,000.00 USD | 0.00 USD | 850,610.00 USD | `-48.52%` | `742.89` |
| `Live` | `Long` | `1155.00` | 749,540,000.00 USD | 0.00 USD | 599,140.00 USD | `-48.07%` | `518.73` |
| `Live` | `Long` | `1165.00` | 748,940,000.00 USD | 0.00 USD | 1,630,000.00 USD | `-47.62%` | `1,395.42` |
| `Live` | `Long` | `1175.00` | 747,320,000.00 USD | 0.00 USD | 261,700.00 USD | `-47.17%` | `222.73` |
| `Live` | `Long` | `1185.00` | 747,060,000.00 USD | 0.00 USD | 2,670,000.00 USD | `-46.72%` | `2,251.69` |
| `Live` | `Long` | `1195.00` | 744,390,000.00 USD | 0.00 USD | 330,450.00 USD | `-46.28%` | `276.53` |
| `Live` | `Long` | `1205.00` | 744,060,000.00 USD | 0.00 USD | 7,250,000.00 USD | `-45.83%` | `6,014.73` |
| `Live` | `Long` | `1215.00` | 736,810,000.00 USD | 0.00 USD | 80,960.00 USD | `-45.38%` | `66.64` |
| `Live` | `Long` | `1225.00` | 736,730,000.00 USD | 0.00 USD | 405,620.00 USD | `-44.93%` | `331.12` |
| `Live` | `Long` | `1235.00` | 736,320,000.00 USD | 0.00 USD | 116,280.00 USD | `-44.48%` | `94.15` |
| `Live` | `Long` | `1245.00` | 736,210,000.00 USD | 0.00 USD | 53,980.00 USD | `-44.03%` | `43.36` |
| `Live` | `Long` | `1255.00` | 736,150,000.00 USD | 0.00 USD | 1,200,000.00 USD | `-43.58%` | `952.40` |
| `Live` | `Long` | `1265.00` | 734,960,000.00 USD | 0.00 USD | 2,220,000.00 USD | `-43.13%` | `1,751.91` |
| `Live` | `Long` | `1275.00` | 732,740,000.00 USD | 0.00 USD | 15,490,000.00 USD | `-42.68%` | `12,147.81` |
| `Live` | `Long` | `1285.00` | 717,250,000.00 USD | 0.00 USD | 556,180.00 USD | `-42.23%` | `432.82` |
| `Live` | `Long` | `1295.00` | 716,700,000.00 USD | 0.00 USD | 378,160.00 USD | `-41.78%` | `292.01` |
| `Live` | `Long` | `1305.00` | 716,320,000.00 USD | 0.00 USD | 125,780.00 USD | `-41.33%` | `96.38` |
| `Live` | `Long` | `1315.00` | 716,190,000.00 USD | 0.00 USD | 306,940.00 USD | `-40.88%` | `233.41` |
| `Live` | `Long` | `1325.00` | 715,880,000.00 USD | 0.00 USD | 640,550.00 USD | `-40.43%` | `483.43` |
| `Live` | `Long` | `1335.00` | 715,240,000.00 USD | 0.00 USD | 286,420.00 USD | `-39.98%` | `214.55` |
| `Live` | `Long` | `1345.00` | 714,960,000.00 USD | 0.00 USD | 580,160.00 USD | `-39.53%` | `431.35` |
| `Live` | `Long` | `1355.00` | 714,380,000.00 USD | 0.00 USD | 5,240,000.00 USD | `-39.08%` | `3,868.53` |
| `Live` | `Long` | `1365.00` | 709,140,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-38.63%` | `806.90` |
| `Live` | `Long` | `1375.00` | 708,030,000.00 USD | 0.00 USD | 7,130,000.00 USD | `-38.18%` | `5,185.78` |
| `Live` | `Long` | `1385.00` | 700,900,000.00 USD | 0.00 USD | 2,300,000.00 USD | `-37.73%` | `1,660.38` |
| `Live` | `Long` | `1395.00` | 698,600,000.00 USD | 0.00 USD | 520,350.00 USD | `-37.28%` | `373.01` |
| `Live` | `Long` | `1405.00` | 698,080,000.00 USD | 0.00 USD | 10,130,000.00 USD | `-36.83%` | `7,211.33` |
| `Live` | `Long` | `1415.00` | 687,950,000.00 USD | 0.00 USD | 554,220.00 USD | `-36.38%` | `391.67` |
| `Live` | `Long` | `1425.00` | 687,400,000.00 USD | 0.00 USD | 372,990.00 USD | `-35.93%` | `261.75` |
| `Live` | `Long` | `1435.00` | 687,020,000.00 USD | 0.00 USD | 1,210,000.00 USD | `-35.49%` | `842.87` |
| `Live` | `Long` | `1445.00` | 685,820,000.00 USD | 0.00 USD | 2,120,000.00 USD | `-35.04%` | `1,466.35` |
| `Live` | `Long` | `1455.00` | 683,700,000.00 USD | 0.00 USD | 19,770,000.00 USD | `-34.59%` | `13,585.18` |
| `Live` | `Long` | `1465.00` | 663,930,000.00 USD | 0.00 USD | 2,030,000.00 USD | `-34.14%` | `1,388.71` |
| `Live` | `Long` | `1475.00` | 661,900,000.00 USD | 0.00 USD | 5,960,000.00 USD | `-33.69%` | `4,037.91` |
| `Live` | `Long` | `1485.00` | 655,940,000.00 USD | 0.00 USD | 139,630.00 USD | `-33.24%` | `94.03` |
| `Live` | `Long` | `1495.00` | 655,800,000.00 USD | 0.00 USD | 19,510,000.00 USD | `-32.79%` | `13,050.56` |
| `Live` | `Long` | `1505.00` | 636,290,000.00 USD | 0.00 USD | 293,500.00 USD | `-32.34%` | `195.02` |
| `Live` | `Long` | `1515.00` | 636,000,000.00 USD | 0.00 USD | 20,980,000.00 USD | `-31.89%` | `13,846.62` |
| `Live` | `Long` | `1525.00` | 615,020,000.00 USD | 0.00 USD | 275,130.00 USD | `-31.44%` | `180.41` |
| `Live` | `Long` | `1535.00` | 614,740,000.00 USD | 0.00 USD | 1,060,000.00 USD | `-30.99%` | `688.26` |
| `Live` | `Long` | `1545.00` | 613,690,000.00 USD | 0.00 USD | 2,710,000.00 USD | `-30.54%` | `1,753.80` |
| `Live` | `Long` | `1555.00` | 610,980,000.00 USD | 0.00 USD | 3,810,000.00 USD | `-30.09%` | `2,449.88` |
| `Live` | `Long` | `1565.00` | 607,170,000.00 USD | 0.00 USD | 16,680,000.00 USD | `-29.64%` | `10,659.10` |
| `Live` | `Long` | `1575.00` | 590,490,000.00 USD | 0.00 USD | 747,200.00 USD | `-29.19%` | `474.41` |
| `Live` | `Long` | `1585.00` | 589,740,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-28.74%` | `691.63` |
| `Live` | `Long` | `1595.00` | 588,640,000.00 USD | 0.00 USD | 1,470,000.00 USD | `-28.29%` | `923.48` |
| `Live` | `Long` | `1605.00` | 587,170,000.00 USD | 0.00 USD | 17,980,000.00 USD | `-27.84%` | `11,204.10` |
| `Live` | `Long` | `1615.00` | 569,190,000.00 USD | 0.00 USD | 410,710.00 USD | `-27.39%` | `254.31` |
| `Live` | `Long` | `1625.00` | 568,780,000.00 USD | 0.00 USD | 1,110,000.00 USD | `-26.94%` | `684.53` |
| `Live` | `Long` | `1635.00` | 567,660,000.00 USD | 0.00 USD | 18,690,000.00 USD | `-26.49%` | `11,430.73` |
| `Live` | `Long` | `1645.00` | 548,970,000.00 USD | 0.00 USD | 36,670,000.00 USD | `-26.04%` | `22,293.51` |
| `Live` | `Long` | `1655.00` | 512,300,000.00 USD | 0.00 USD | 533,660.00 USD | `-25.59%` | `322.46` |
| `Live` | `Long` | `1665.00` | 511,770,000.00 USD | 0.00 USD | 12,350,000.00 USD | `-25.14%` | `7,418.57` |
| `Live` | `Long` | `1675.00` | 499,420,000.00 USD | 0.00 USD | 1,460,000.00 USD | `-24.70%` | `870.85` |
| `Live` | `Long` | `1685.00` | 497,960,000.00 USD | 0.00 USD | 1,220,000.00 USD | `-24.25%` | `723.34` |
| `Live` | `Long` | `1695.00` | 496,740,000.00 USD | 0.00 USD | 870,240.00 USD | `-23.80%` | `513.41` |
| `Live` | `Long` | `1705.00` | 495,870,000.00 USD | 0.00 USD | 17,250,000.00 USD | `-23.35%` | `10,116.29` |
| `Live` | `Long` | `1715.00` | 478,620,000.00 USD | 0.00 USD | 17,850,000.00 USD | `-22.90%` | `10,410.04` |
| `Live` | `Long` | `1725.00` | 460,770,000.00 USD | 0.00 USD | 19,370,000.00 USD | `-22.45%` | `11,228.05` |
| `Live` | `Long` | `1735.00` | 441,400,000.00 USD | 0.00 USD | 1,390,000.00 USD | `-22.00%` | `799.89` |
| `Live` | `Long` | `1745.00` | 440,010,000.00 USD | 0.00 USD | 1,110,000.00 USD | `-21.55%` | `638.64` |
| `Live` | `Long` | `1755.00` | 438,900,000.00 USD | 0.00 USD | 225,470.00 USD | `-21.10%` | `128.48` |
| `Live` | `Long` | `1765.00` | 438,670,000.00 USD | 0.00 USD | 3,830,000.00 USD | `-20.65%` | `2,172.77` |
| `Live` | `Long` | `1775.00` | 434,840,000.00 USD | 0.00 USD | 4,970,000.00 USD | `-20.20%` | `2,802.36` |
| `Live` | `Long` | `1785.00` | 429,860,000.00 USD | 0.00 USD | 83,330,000.00 USD | `-19.75%` | `46,685.95` |
| `Live` | `Long` | `1795.00` | 346,530,000.00 USD | 0.00 USD | 1,160,000.00 USD | `-19.30%` | `647.64` |
| `Live` | `Long` | `1805.00` | 345,360,000.00 USD | 0.00 USD | 8,320,000.00 USD | `-18.85%` | `4,611.73` |
| `Live` | `Long` | `1815.00` | 337,040,000.00 USD | 0.00 USD | 2,190,000.00 USD | `-18.40%` | `1,206.49` |
| `Live` | `Long` | `1825.00` | 334,850,000.00 USD | 0.00 USD | 4,200,000.00 USD | `-17.95%` | `2,299.74` |
| `Live` | `Long` | `1835.00` | 330,650,000.00 USD | 0.00 USD | 1,110,000.00 USD | `-17.50%` | `602.44` |
| `Live` | `Long` | `1845.00` | 329,550,000.00 USD | 0.00 USD | 16,340,000.00 USD | `-17.05%` | `8,857.35` |
| `Live` | `Long` | `1855.00` | 313,210,000.00 USD | 0.00 USD | 1,120,000.00 USD | `-16.60%` | `605.09` |
| `Live` | `Long` | `1865.00` | 312,080,000.00 USD | 0.00 USD | 1,300,000.00 USD | `-16.15%` | `698.59` |
| `Live` | `Long` | `1875.00` | 310,780,000.00 USD | 0.00 USD | 18,820,000.00 USD | `-15.70%` | `10,039.91` |
| `Live` | `Long` | `1885.00` | 291,960,000.00 USD | 0.00 USD | 4,920,000.00 USD | `-15.25%` | `2,608.83` |
| `Live` | `Long` | `1895.00` | 287,040,000.00 USD | 0.00 USD | 1,310,000.00 USD | `-14.80%` | `690.50` |
| `Live` | `Long` | `1905.00` | 285,730,000.00 USD | 0.00 USD | 3,660,000.00 USD | `-14.36%` | `1,920.54` |
| `Live` | `Long` | `1915.00` | 282,070,000.00 USD | 0.00 USD | 17,910,000.00 USD | `-13.91%` | `9,353.98` |
| `Live` | `Long` | `1925.00` | 264,160,000.00 USD | 0.00 USD | 1,370,000.00 USD | `-13.46%` | `713.08` |
| `Live` | `Long` | `1935.00` | 262,790,000.00 USD | 0.00 USD | 17,760,000.00 USD | `-13.01%` | `9,179.16` |
| `Live` | `Long` | `1945.00` | 245,020,000.00 USD | 0.00 USD | 1,690,000.00 USD | `-12.56%` | `870.97` |
| `Live` | `Long` | `1955.00` | 243,330,000.00 USD | 0.00 USD | 1,410,000.00 USD | `-12.11%` | `722.16` |
| `Live` | `Long` | `1965.00` | 241,920,000.00 USD | 0.00 USD | 14,400,000.00 USD | `-11.66%` | `7,330.61` |
| `Live` | `Long` | `1975.00` | 227,510,000.00 USD | 0.00 USD | 1,630,000.00 USD | `-11.21%` | `824.00` |
| `Live` | `Long` | `1985.00` | 225,890,000.00 USD | 0.00 USD | 5,570,000.00 USD | `-10.76%` | `2,807.01` |
| `Live` | `Long` | `1995.00` | 220,310,000.00 USD | 0.00 USD | 5,340,000.00 USD | `-10.31%` | `2,676.76` |
| `Live` | `Long` | `2005.00` | 214,970,000.00 USD | 0.00 USD | 13,090,000.00 USD | `-9.86%` | `6,528.05` |
| `Live` | `Long` | `2015.00` | 201,890,000.00 USD | 0.00 USD | 2,660,000.00 USD | `-9.41%` | `1,322.22` |
| `Live` | `Long` | `2025.00` | 199,220,000.00 USD | 0.00 USD | 1,180,000.00 USD | `-8.96%` | `583.38` |
| `Live` | `Long` | `2035.00` | 198,040,000.00 USD | 0.00 USD | 1,110,000.00 USD | `-8.51%` | `543.38` |
| `Live` | `Long` | `2045.00` | 196,930,000.00 USD | 0.00 USD | 6,580,000.00 USD | `-8.06%` | `3,219.86` |
| `Live` | `Long` | `2055.00` | 190,350,000.00 USD | 0.00 USD | 3,870,000.00 USD | `-7.61%` | `1,881.11` |
| `Live` | `Long` | `2065.00` | 186,480,000.00 USD | 0.00 USD | 15,510,000.00 USD | `-7.16%` | `7,509.62` |
| `Live` | `Long` | `2075.00` | 170,980,000.00 USD | 0.00 USD | 3,430,000.00 USD | `-6.71%` | `1,654.52` |
| `Live` | `Long` | `2085.00` | 167,540,000.00 USD | 0.00 USD | 12,820,000.00 USD | `-6.26%` | `6,147.10` |
| `Live` | `Long` | `2095.00` | 154,730,000.00 USD | 0.00 USD | 1,840,000.00 USD | `-5.81%` | `880.55` |
| `Live` | `Long` | `2105.00` | 152,880,000.00 USD | 0.00 USD | 2,360,000.00 USD | `-5.36%` | `1,121.90` |
| `Live` | `Long` | `2115.00` | 150,520,000.00 USD | 0.00 USD | 2,210,000.00 USD | `-4.91%` | `1,044.21` |
| `Live` | `Long` | `2125.00` | 148,310,000.00 USD | 0.00 USD | 123,700,000.00 USD | `-4.46%` | `58,213.47` |
| `Live` | `Long` | `2135.00` | 24,610,000.00 USD | 0.00 USD | 1,490,000.00 USD | `-4.01%` | `698.74` |
| `Live` | `Long` | `2145.00` | 23,120,000.00 USD | 0.00 USD | 5,640,000.00 USD | `-3.57%` | `2,627.08` |
| `Live` | `Long` | `2155.00` | 17,480,000.00 USD | 0.00 USD | 1,690,000.00 USD | `-3.12%` | `784.04` |
| `Live` | `Long` | `2165.00` | 15,790,000.00 USD | 0.00 USD | 6,700,000.00 USD | `-2.67%` | `3,094.58` |
| `Live` | `Long` | `2175.00` | 9,090,000.00 USD | 0.00 USD | 5,690,000.00 USD | `-2.22%` | `2,615.40` |
| `Live` | `Long` | `2185.00` | 3,400,000.00 USD | 0.00 USD | 694,330.00 USD | `-1.77%` | `317.77` |
| `Live` | `Long` | `2195.00` | 2,710,000.00 USD | 0.00 USD | 2,250,000.00 USD | `-1.32%` | `1,026.59` |
| `Live` | `Long` | `2205.00` | 455,960.00 USD | 0.00 USD | 449,420.00 USD | `-0.87%` | `203.82` |
| `Live` | `Long` | `2215.00` | 6,540.00 USD | 0.00 USD | 6,540.00 USD | `-0.42%` | `2.95` |
| `Live` | `Short` | `2225.00` | 1,890.00 USD | 1,890.00 USD | 0.00 USD | `+0.03%` | `0.85` |
| `Live` | `Short` | `2245.00` | 4,460.00 USD | 2,570.00 USD | 0.00 USD | `+0.93%` | `1.15` |
| `Live` | `Short` | `2255.00` | 24,530.00 USD | 20,070.00 USD | 0.00 USD | `+1.38%` | `8.90` |
| `Live` | `Short` | `2265.00` | 118,040.00 USD | 93,510.00 USD | 0.00 USD | `+1.83%` | `41.28` |
| `Live` | `Short` | `2275.00` | 946,650.00 USD | 828,610.00 USD | 0.00 USD | `+2.28%` | `364.22` |
| `Live` | `Short` | `2285.00` | 1,440,000.00 USD | 490,730.00 USD | 0.00 USD | `+2.73%` | `214.76` |
| `Live` | `Short` | `2295.00` | 4,360,000.00 USD | 2,920,000.00 USD | 0.00 USD | `+3.18%` | `1,272.76` |
| `Live` | `Short` | `2305.00` | 4,810,000.00 USD | 448,140.00 USD | 0.00 USD | `+3.63%` | `194.42` |
| `Live` | `Short` | `2315.00` | 5,630,000.00 USD | 824,210.00 USD | 0.00 USD | `+4.08%` | `356.03` |
| `Live` | `Short` | `2325.00` | 8,880,000.00 USD | 3,250,000.00 USD | 0.00 USD | `+4.53%` | `1,396.72` |
| `Live` | `Short` | `2335.00` | 9,320,000.00 USD | 437,940.00 USD | 0.00 USD | `+4.98%` | `187.55` |
| `Live` | `Short` | `2345.00` | 9,730,000.00 USD | 415,460.00 USD | 0.00 USD | `+5.43%` | `177.17` |
| `Live` | `Short` | `2355.00` | 12,170,000.00 USD | 2,440,000.00 USD | 0.00 USD | `+5.88%` | `1,034.09` |
| `Live` | `Short` | `2365.00` | 17,030,000.00 USD | 4,860,000.00 USD | 0.00 USD | `+6.33%` | `2,055.20` |
| `Live` | `Short` | `2375.00` | 17,920,000.00 USD | 893,040.00 USD | 0.00 USD | `+6.78%` | `376.02` |
| `Live` | `Short` | `2385.00` | 18,640,000.00 USD | 722,850.00 USD | 0.00 USD | `+7.22%` | `303.08` |
| `Live` | `Short` | `2395.00` | 23,500,000.00 USD | 4,850,000.00 USD | 0.00 USD | `+7.67%` | `2,026.67` |
| `Live` | `Short` | `2405.00` | 23,610,000.00 USD | 115,180.00 USD | 0.00 USD | `+8.12%` | `47.89` |
| `Live` | `Short` | `2415.00` | 23,850,000.00 USD | 236,460.00 USD | 0.00 USD | `+8.57%` | `97.91` |
| `Live` | `Short` | `2425.00` | 24,140,000.00 USD | 289,470.00 USD | 0.00 USD | `+9.02%` | `119.37` |
| `Live` | `Short` | `2435.00` | 24,340,000.00 USD | 197,400.00 USD | 0.00 USD | `+9.47%` | `81.07` |
| `Live` | `Short` | `2445.00` | 29,130,000.00 USD | 4,800,000.00 USD | 0.00 USD | `+9.92%` | `1,961.21` |
| `Live` | `Short` | `2455.00` | 29,350,000.00 USD | 214,400.00 USD | 0.00 USD | `+10.37%` | `87.33` |
| `Live` | `Short` | `2465.00` | 40,890,000.00 USD | 11,550,000.00 USD | 0.00 USD | `+10.82%` | `4,684.83` |
| `Live` | `Short` | `2475.00` | 95,670,000.00 USD | 54,770,000.00 USD | 0.00 USD | `+11.27%` | `22,131.28` |
| `Live` | `Short` | `2485.00` | 97,320,000.00 USD | 1,650,000.00 USD | 0.00 USD | `+11.72%` | `664.64` |
| `Live` | `Short` | `2495.00` | 99,470,000.00 USD | 2,150,000.00 USD | 0.00 USD | `+12.17%` | `860.11` |
| `Live` | `Short` | `2505.00` | 103,930,000.00 USD | 4,470,000.00 USD | 0.00 USD | `+12.62%` | `1,783.82` |
| `Live` | `Short` | `2515.00` | 105,530,000.00 USD | 1,590,000.00 USD | 0.00 USD | `+13.07%` | `634.16` |
| `Live` | `Short` | `2525.00` | 105,580,000.00 USD | 46,400.00 USD | 0.00 USD | `+13.52%` | `18.38` |
| `Live` | `Short` | `2535.00` | 106,630,000.00 USD | 1,060,000.00 USD | 0.00 USD | `+13.97%` | `416.76` |
| `Live` | `Short` | `2545.00` | 111,670,000.00 USD | 5,040,000.00 USD | 0.00 USD | `+14.42%` | `1,978.95` |
| `Live` | `Short` | `2555.00` | 111,910,000.00 USD | 238,660.00 USD | 0.00 USD | `+14.87%` | `93.41` |
| `Live` | `Short` | `2565.00` | 112,000,000.00 USD | 89,050.00 USD | 0.00 USD | `+15.32%` | `34.72` |
| `Live` | `Short` | `2575.00` | 112,560,000.00 USD | 559,600.00 USD | 0.00 USD | `+15.77%` | `217.32` |
| `Live` | `Short` | `2585.00` | 146,870,000.00 USD | 34,310,000.00 USD | 0.00 USD | `+16.22%` | `13,273.57` |
| `Live` | `Short` | `2595.00` | 147,230,000.00 USD | 359,640.00 USD | 0.00 USD | `+16.67%` | `138.59` |
| `Live` | `Short` | `2605.00` | 153,030,000.00 USD | 5,810,000.00 USD | 0.00 USD | `+17.12%` | `2,229.24` |
| `Live` | `Short` | `2615.00` | 153,770,000.00 USD | 732,830.00 USD | 0.00 USD | `+17.57%` | `280.24` |
| `Live` | `Short` | `2625.00` | 199,180,000.00 USD | 45,410,000.00 USD | 0.00 USD | `+18.01%` | `17,298.59` |
| `Live` | `Short` | `2635.00` | 200,210,000.00 USD | 1,030,000.00 USD | 0.00 USD | `+18.46%` | `390.95` |
| `Live` | `Short` | `2645.00` | 200,830,000.00 USD | 626,810.00 USD | 0.00 USD | `+18.91%` | `236.98` |
| `Live` | `Short` | `2655.00` | 227,660,000.00 USD | 26,820,000.00 USD | 0.00 USD | `+19.36%` | `10,103.19` |
| `Live` | `Short` | `2665.00` | 227,710,000.00 USD | 51,540.00 USD | 0.00 USD | `+19.81%` | `19.34` |
| `Live` | `Short` | `2675.00` | 228,810,000.00 USD | 1,100,000.00 USD | 0.00 USD | `+20.26%` | `410.36` |
| `Live` | `Short` | `2685.00` | 228,830,000.00 USD | 23,200.00 USD | 0.00 USD | `+20.71%` | `8.64` |
| `Live` | `Short` | `2695.00` | 229,300,000.00 USD | 468,980.00 USD | 0.00 USD | `+21.16%` | `174.02` |
| `Live` | `Short` | `2705.00` | 230,000,000.00 USD | 698,920.00 USD | 0.00 USD | `+21.61%` | `258.38` |
| `Live` | `Short` | `2715.00` | 230,410,000.00 USD | 413,400.00 USD | 0.00 USD | `+22.06%` | `152.27` |
| `Live` | `Short` | `2725.00` | 230,640,000.00 USD | 229,610.00 USD | 0.00 USD | `+22.51%` | `84.26` |
| `Live` | `Short` | `2735.00` | 235,790,000.00 USD | 5,150,000.00 USD | 0.00 USD | `+22.96%` | `1,882.22` |
| `Live` | `Short` | `2745.00` | 249,580,000.00 USD | 13,790,000.00 USD | 0.00 USD | `+23.41%` | `5,025.44` |
| `Live` | `Short` | `2755.00` | 254,630,000.00 USD | 5,050,000.00 USD | 0.00 USD | `+23.86%` | `1,833.58` |
| `Live` | `Short` | `2765.00` | 255,050,000.00 USD | 416,000.00 USD | 0.00 USD | `+24.31%` | `150.45` |
| `Live` | `Short` | `2775.00` | 280,230,000.00 USD | 25,170,000.00 USD | 0.00 USD | `+24.76%` | `9,071.78` |
| `Live` | `Short` | `2785.00` | 280,750,000.00 USD | 528,660.00 USD | 0.00 USD | `+25.21%` | `189.82` |
| `Live` | `Short` | `2795.00` | 286,310,000.00 USD | 5,560,000.00 USD | 0.00 USD | `+25.66%` | `1,988.20` |
| `Live` | `Short` | `2805.00` | 292,240,000.00 USD | 5,930,000.00 USD | 0.00 USD | `+26.11%` | `2,112.46` |
| `Live` | `Short` | `2815.00` | 294,240,000.00 USD | 2,010,000.00 USD | 0.00 USD | `+26.56%` | `712.55` |
| `Live` | `Short` | `2825.00` | 294,380,000.00 USD | 133,850.00 USD | 0.00 USD | `+27.01%` | `47.38` |
| `Live` | `Short` | `2835.00` | 300,660,000.00 USD | 6,280,000.00 USD | 0.00 USD | `+27.46%` | `2,215.71` |
| `Live` | `Short` | `2845.00` | 301,010,000.00 USD | 349,690.00 USD | 0.00 USD | `+27.91%` | `122.92` |
| `Live` | `Short` | `2855.00` | 301,510,000.00 USD | 502,140.00 USD | 0.00 USD | `+28.35%` | `175.88` |
| `Live` | `Short` | `2865.00` | 301,930,000.00 USD | 422,840.00 USD | 0.00 USD | `+28.80%` | `147.59` |
| `Live` | `Short` | `2875.00` | 302,000,000.00 USD | 64,240.00 USD | 0.00 USD | `+29.25%` | `22.34` |
| `Live` | `Short` | `2885.00` | 303,730,000.00 USD | 1,740,000.00 USD | 0.00 USD | `+29.70%` | `601.87` |
| `Live` | `Short` | `2895.00` | 305,070,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+30.15%` | `463.25` |
| `Live` | `Short` | `2905.00` | 349,470,000.00 USD | 44,390,000.00 USD | 0.00 USD | `+30.60%` | `15,282.00` |
| `Live` | `Short` | `2915.00` | 351,820,000.00 USD | 2,350,000.00 USD | 0.00 USD | `+31.05%` | `807.62` |
| `Live` | `Short` | `2925.00` | 354,850,000.00 USD | 3,030,000.00 USD | 0.00 USD | `+31.50%` | `1,035.76` |
| `Live` | `Short` | `2935.00` | 354,920,000.00 USD | 67,460.00 USD | 0.00 USD | `+31.95%` | `22.99` |
| `Live` | `Short` | `2945.00` | 355,360,000.00 USD | 437,030.00 USD | 0.00 USD | `+32.40%` | `148.40` |
| `Live` | `Short` | `2955.00` | 359,930,000.00 USD | 4,570,000.00 USD | 0.00 USD | `+32.85%` | `1,548.18` |
| `Live` | `Short` | `2965.00` | 360,520,000.00 USD | 590,570.00 USD | 0.00 USD | `+33.30%` | `199.18` |
| `Live` | `Short` | `2975.00` | 363,880,000.00 USD | 3,360,000.00 USD | 0.00 USD | `+33.75%` | `1,128.30` |
| `Live` | `Short` | `2985.00` | 365,120,000.00 USD | 1,240,000.00 USD | 0.00 USD | `+34.20%` | `416.92` |
| `Live` | `Short` | `2995.00` | 380,150,000.00 USD | 15,030,000.00 USD | 0.00 USD | `+34.65%` | `5,018.80` |
| `Live` | `Short` | `3005.00` | 380,800,000.00 USD | 646,430.00 USD | 0.00 USD | `+35.10%` | `215.12` |
| `Live` | `Short` | `3015.00` | 380,980,000.00 USD | 175,020.00 USD | 0.00 USD | `+35.55%` | `58.05` |
| `Live` | `Short` | `3025.00` | 381,840,000.00 USD | 862,710.00 USD | 0.00 USD | `+36.00%` | `285.19` |
| `Live` | `Short` | `3035.00` | 396,860,000.00 USD | 15,030,000.00 USD | 0.00 USD | `+36.45%` | `4,950.87` |
| `Live` | `Short` | `3045.00` | 397,580,000.00 USD | 715,260.00 USD | 0.00 USD | `+36.90%` | `234.90` |
| `Live` | `Short` | `3055.00` | 397,590,000.00 USD | 6,520.00 USD | 0.00 USD | `+37.35%` | `2.14` |
| `Live` | `Short` | `3065.00` | 399,100,000.00 USD | 1,510,000.00 USD | 0.00 USD | `+37.80%` | `492.46` |
| `Live` | `Short` | `3075.00` | 405,170,000.00 USD | 6,070,000.00 USD | 0.00 USD | `+38.25%` | `1,973.85` |
| `Live` | `Short` | `3085.00` | 416,100,000.00 USD | 10,930,000.00 USD | 0.00 USD | `+38.70%` | `3,543.92` |
| `Live` | `Short` | `3095.00` | 421,880,000.00 USD | 5,780,000.00 USD | 0.00 USD | `+39.14%` | `1,868.35` |
| `Live` | `Short` | `3105.00` | 434,170,000.00 USD | 12,290,000.00 USD | 0.00 USD | `+39.59%` | `3,956.62` |
| `Live` | `Short` | `3115.00` | 468,050,000.00 USD | 33,880,000.00 USD | 0.00 USD | `+40.04%` | `10,877.23` |
| `Live` | `Short` | `3125.00` | 469,910,000.00 USD | 1,870,000.00 USD | 0.00 USD | `+40.49%` | `597.23` |
| `Live` | `Short` | `3135.00` | 470,180,000.00 USD | 261,240.00 USD | 0.00 USD | `+40.94%` | `83.33` |
| `Live` | `Short` | `3145.00` | 470,580,000.00 USD | 401,090.00 USD | 0.00 USD | `+41.39%` | `127.53` |
| `Live` | `Short` | `3155.00` | 470,800,000.00 USD | 222,300.00 USD | 0.00 USD | `+41.84%` | `70.46` |
| `Live` | `Short` | `3165.00` | 470,930,000.00 USD | 130,620.00 USD | 0.00 USD | `+42.29%` | `41.27` |
| `Live` | `Short` | `3175.00` | 472,020,000.00 USD | 1,090,000.00 USD | 0.00 USD | `+42.74%` | `343.57` |
| `Live` | `Short` | `3185.00` | 542,680,000.00 USD | 70,660,000.00 USD | 0.00 USD | `+43.19%` | `22,183.97` |
| `Live` | `Short` | `3195.00` | 542,890,000.00 USD | 210,270.00 USD | 0.00 USD | `+43.64%` | `65.81` |
| `Live` | `Short` | `3205.00` | 543,240,000.00 USD | 352,030.00 USD | 0.00 USD | `+44.09%` | `109.84` |
| `Live` | `Short` | `3215.00` | 543,410,000.00 USD | 175,220.00 USD | 0.00 USD | `+44.54%` | `54.50` |
| `Live` | `Short` | `3225.00` | 551,750,000.00 USD | 8,340,000.00 USD | 0.00 USD | `+44.99%` | `2,584.90` |
| `Live` | `Short` | `3235.00` | 561,510,000.00 USD | 9,760,000.00 USD | 0.00 USD | `+45.44%` | `3,016.19` |
| `Live` | `Short` | `3245.00` | 566,360,000.00 USD | 4,850,000.00 USD | 0.00 USD | `+45.89%` | `1,496.04` |
| `Live` | `Short` | `3255.00` | 566,380,000.00 USD | 12,810.00 USD | 0.00 USD | `+46.34%` | `3.93` |
| `Live` | `Short` | `3265.00` | 566,440,000.00 USD | 65,860.00 USD | 0.00 USD | `+46.79%` | `20.17` |
| `Live` | `Short` | `3275.00` | 577,270,000.00 USD | 10,830,000.00 USD | 0.00 USD | `+47.24%` | `3,307.06` |
| `Live` | `Short` | `3285.00` | 577,340,000.00 USD | 65,540.00 USD | 0.00 USD | `+47.69%` | `19.95` |
| `Live` | `Short` | `3295.00` | 577,670,000.00 USD | 334,070.00 USD | 0.00 USD | `+48.14%` | `101.39` |
| `Live` | `Short` | `3305.00` | 578,940,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+48.59%` | `384.36` |
| `Live` | `Short` | `3315.00` | 581,060,000.00 USD | 2,120,000.00 USD | 0.00 USD | `+49.04%` | `639.66` |
| `Live` | `Short` | `3325.00` | 581,140,000.00 USD | 75,050.00 USD | 0.00 USD | `+49.49%` | `22.57` |
| `Live` | `Short` | `3335.00` | 582,620,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+49.93%` | `443.70` |
| `Live` | `Short` | `3345.00` | 582,680,000.00 USD | 58,000.00 USD | 0.00 USD | `+50.38%` | `17.34` |
| `Live` | `Short` | `3355.00` | 584,720,000.00 USD | 2,050,000.00 USD | 0.00 USD | `+50.83%` | `609.89` |
| `Live` | `Short` | `3365.00` | 587,690,000.00 USD | 2,970,000.00 USD | 0.00 USD | `+51.28%` | `881.89` |
| `Live` | `Short` | `3375.00` | 590,120,000.00 USD | 2,430,000.00 USD | 0.00 USD | `+51.73%` | `718.89` |
| `Live` | `Short` | `3385.00` | 590,220,000.00 USD | 102,540.00 USD | 0.00 USD | `+52.18%` | `30.29` |
| `Live` | `Short` | `3395.00` | 590,310,000.00 USD | 93,920.00 USD | 0.00 USD | `+52.63%` | `27.66` |
| `Live` | `Short` | `3405.00` | 591,580,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+53.08%` | `372.47` |
| `Live` | `Short` | `3415.00` | 595,780,000.00 USD | 4,200,000.00 USD | 0.00 USD | `+53.53%` | `1,231.30` |
| `Live` | `Short` | `3425.00` | 610,370,000.00 USD | 14,590,000.00 USD | 0.00 USD | `+53.98%` | `4,258.75` |
| `Live` | `Short` | `3435.00` | 610,470,000.00 USD | 95,600.00 USD | 0.00 USD | `+54.43%` | `27.83` |
| `Live` | `Short` | `3445.00` | 611,350,000.00 USD | 881,390.00 USD | 0.00 USD | `+54.88%` | `255.85` |
| `Live` | `Short` | `3455.00` | 611,910,000.00 USD | 559,510.00 USD | 0.00 USD | `+55.33%` | `161.94` |
| `Live` | `Short` | `3465.00` | 612,330,000.00 USD | 424,610.00 USD | 0.00 USD | `+55.78%` | `122.54` |
| `Live` | `Short` | `3475.00` | 612,390,000.00 USD | 55,090.00 USD | 0.00 USD | `+56.23%` | `15.85` |
| `Live` | `Short` | `3485.00` | 612,420,000.00 USD | 30,100.00 USD | 0.00 USD | `+56.68%` | `8.64` |
| `Live` | `Short` | `3495.00` | 613,580,000.00 USD | 1,170,000.00 USD | 0.00 USD | `+57.13%` | `334.09` |
| `Live` | `Short` | `3505.00` | 615,230,000.00 USD | 1,640,000.00 USD | 0.00 USD | `+57.58%` | `469.01` |
| `Live` | `Short` | `3515.00` | 615,600,000.00 USD | 375,650.00 USD | 0.00 USD | `+58.03%` | `106.87` |
| `Live` | `Short` | `3525.00` | 616,370,000.00 USD | 765,100.00 USD | 0.00 USD | `+58.48%` | `217.05` |
| `Live` | `Short` | `3535.00` | 631,200,000.00 USD | 14,830,000.00 USD | 0.00 USD | `+58.93%` | `4,194.93` |
| `Live` | `Short` | `3545.00` | 631,300,000.00 USD | 97,280.00 USD | 0.00 USD | `+59.38%` | `27.44` |
| `Live` | `Short` | `3555.00` | 631,420,000.00 USD | 119,970.00 USD | 0.00 USD | `+59.83%` | `33.75` |
| `Live` | `Short` | `3565.00` | 631,540,000.00 USD | 125,810.00 USD | 0.00 USD | `+60.28%` | `35.29` |
| `Live` | `Short` | `3575.00` | 631,620,000.00 USD | 80,980.00 USD | 0.00 USD | `+60.72%` | `22.65` |
| `Live` | `Short` | `3585.00` | 632,370,000.00 USD | 749,130.00 USD | 0.00 USD | `+61.17%` | `208.96` |
| `Live` | `Short` | `3595.00` | 632,420,000.00 USD | 43,700.00 USD | 0.00 USD | `+61.62%` | `12.15` |
| `Live` | `Short` | `3605.00` | 632,480,000.00 USD | 62,790.00 USD | 0.00 USD | `+62.07%` | `17.42` |
| `Live` | `Short` | `3615.00` | 636,270,000.00 USD | 3,790,000.00 USD | 0.00 USD | `+62.52%` | `1,047.50` |
| `Live` | `Short` | `3625.00` | 637,390,000.00 USD | 1,120,000.00 USD | 0.00 USD | `+62.97%` | `309.01` |
| `Live` | `Short` | `3635.00` | 646,200,000.00 USD | 8,820,000.00 USD | 0.00 USD | `+63.42%` | `2,425.46` |
| `Live` | `Short` | `3645.00` | 699,750,000.00 USD | 53,550,000.00 USD | 0.00 USD | `+63.87%` | `14,690.08` |
| `Live` | `Short` | `3655.00` | 699,780,000.00 USD | 37,050.00 USD | 0.00 USD | `+64.32%` | `10.14` |
| `Live` | `Short` | `3665.00` | 700,130,000.00 USD | 343,720.00 USD | 0.00 USD | `+64.77%` | `93.78` |
| `Live` | `Short` | `3675.00` | 706,670,000.00 USD | 6,540,000.00 USD | 0.00 USD | `+65.22%` | `1,779.72` |
| `Live` | `Short` | `3685.00` | 706,880,000.00 USD | 212,010.00 USD | 0.00 USD | `+65.67%` | `57.53` |
| `Live` | `Short` | `3695.00` | 706,910,000.00 USD | 31,030.00 USD | 0.00 USD | `+66.12%` | `8.40` |
| `Live` | `Short` | `3705.00` | 710,770,000.00 USD | 3,860,000.00 USD | 0.00 USD | `+66.57%` | `1,041.70` |
| `Live` | `Short` | `3715.00` | 710,770,000.00 USD | 2,920.00 USD | 0.00 USD | `+67.02%` | `0.79` |
| `Live` | `Short` | `3725.00` | 1,090,000,000.00 USD | 382,870,000.00 USD | 0.00 USD | `+67.47%` | `102,784.23` |
| `Live` | `Short` | `3735.00` | 1,090,000,000.00 USD | 360,220.00 USD | 0.00 USD | `+67.92%` | `96.44` |
| `Live` | `Short` | `3745.00` | 1,100,000,000.00 USD | 2,710,000.00 USD | 0.00 USD | `+68.37%` | `724.56` |
| `Live` | `Short` | `3755.00` | 1,100,000,000.00 USD | 163,780.00 USD | 0.00 USD | `+68.82%` | `43.62` |
| `Live` | `Short` | `3765.00` | 1,100,000,000.00 USD | 78,340.00 USD | 0.00 USD | `+69.27%` | `20.81` |
| `Live` | `Short` | `3775.00` | 1,100,000,000.00 USD | 456,790.00 USD | 0.00 USD | `+69.72%` | `121.00` |
| `Live` | `Short` | `3785.00` | 1,160,000,000.00 USD | 59,410,000.00 USD | 0.00 USD | `+70.17%` | `15,696.92` |
| `Live` | `Short` | `3795.00` | 1,160,000,000.00 USD | 3,470,000.00 USD | 0.00 USD | `+70.62%` | `914.81` |
| `Live` | `Short` | `3805.00` | 1,170,000,000.00 USD | 4,850,000.00 USD | 0.00 USD | `+71.07%` | `1,273.85` |
| `Live` | `Short` | `3815.00` | 1,170,000,000.00 USD | 1,590.00 USD | 0.00 USD | `+71.51%` | `0.42` |
| `Live` | `Short` | `3825.00` | 1,170,000,000.00 USD | 34,550.00 USD | 0.00 USD | `+71.96%` | `9.03` |
| `Live` | `Short` | `3835.00` | 1,170,000,000.00 USD | 280,720.00 USD | 0.00 USD | `+72.41%` | `73.20` |
| `Live` | `Short` | `3845.00` | 1,170,000,000.00 USD | 212,940.00 USD | 0.00 USD | `+72.86%` | `55.38` |
| `Live` | `Short` | `3855.00` | 1,170,000,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+73.31%` | `273.48` |
| `Live` | `Short` | `3865.00` | 1,170,000,000.00 USD | 2,480,000.00 USD | 0.00 USD | `+73.76%` | `640.80` |
| `Live` | `Short` | `3875.00` | 1,170,000,000.00 USD | 93,260.00 USD | 0.00 USD | `+74.21%` | `24.07` |
| `Live` | `Short` | `3885.00` | 1,170,000,000.00 USD | 1,360,000.00 USD | 0.00 USD | `+74.66%` | `351.03` |
| `Live` | `Short` | `3895.00` | 1,170,000,000.00 USD | 2,490,000.00 USD | 0.00 USD | `+75.11%` | `640.54` |
| `Live` | `Short` | `3905.00` | 1,210,000,000.00 USD | 38,870,000.00 USD | 0.00 USD | `+75.56%` | `9,954.89` |
| `Live` | `Short` | `3915.00` | 1,210,000,000.00 USD | 553,260.00 USD | 0.00 USD | `+76.01%` | `141.32` |
| `Live` | `Short` | `3925.00` | 1,210,000,000.00 USD | 152,270.00 USD | 0.00 USD | `+76.46%` | `38.79` |
| `Live` | `Short` | `3935.00` | 1,210,000,000.00 USD | 2,640.00 USD | 0.00 USD | `+76.91%` | `0.67` |
| `Live` | `Short` | `3945.00` | 1,210,000,000.00 USD | 88,480.00 USD | 0.00 USD | `+77.36%` | `22.43` |
| `Live` | `Short` | `3955.00` | 1,210,000,000.00 USD | 1,660.00 USD | 0.00 USD | `+77.81%` | `0.42` |
| `Live` | `Short` | `3965.00` | 1,210,000,000.00 USD | 30,880.00 USD | 0.00 USD | `+78.26%` | `7.79` |
| `Live` | `Short` | `3975.00` | 1,210,000,000.00 USD | 160,630.00 USD | 0.00 USD | `+78.71%` | `40.41` |
| `Live` | `Short` | `3985.00` | 1,210,000,000.00 USD | 178,550.00 USD | 0.00 USD | `+79.16%` | `44.80` |
| `Live` | `Short` | `3995.00` | 1,210,000,000.00 USD | 562,130.00 USD | 0.00 USD | `+79.61%` | `140.71` |
| `Live` | `Short` | `4005.00` | 1,210,000,000.00 USD | 141,730.00 USD | 0.00 USD | `+80.06%` | `35.39` |
| `Live` | `Short` | `4015.00` | 1,220,000,000.00 USD | 1,230,000.00 USD | 0.00 USD | `+80.51%` | `305.37` |
| `Live` | `Short` | `4025.00` | 1,220,000,000.00 USD | 490,570.00 USD | 0.00 USD | `+80.96%` | `121.88` |
| `Live` | `Short` | `4035.00` | 1,220,000,000.00 USD | 414,520.00 USD | 0.00 USD | `+81.41%` | `102.73` |
| `Live` | `Short` | `4045.00` | 1,220,000,000.00 USD | 121,110.00 USD | 0.00 USD | `+81.85%` | `29.94` |
| `Live` | `Short` | `4055.00` | 1,220,000,000.00 USD | 1,690,000.00 USD | 0.00 USD | `+82.30%` | `416.77` |
| `Live` | `Short` | `4065.00` | 1,220,000,000.00 USD | 1,200,000.00 USD | 0.00 USD | `+82.75%` | `295.68` |
| `Live` | `Short` | `4075.00` | 1,220,000,000.00 USD | 129,220.00 USD | 0.00 USD | `+83.20%` | `31.71` |
| `Live` | `Short` | `4085.00` | 1,220,000,000.00 USD | 91,390.00 USD | 0.00 USD | `+83.65%` | `22.37` |
| `Live` | `Short` | `4095.00` | 1,220,000,000.00 USD | 207,480.00 USD | 0.00 USD | `+84.10%` | `50.67` |
| `Live` | `Short` | `4105.00` | 1,220,000,000.00 USD | 1,150,000.00 USD | 0.00 USD | `+84.55%` | `279.04` |
| `Live` | `Short` | `4115.00` | 1,220,000,000.00 USD | 129,580.00 USD | 0.00 USD | `+85.00%` | `31.49` |
| `Live` | `Short` | `4125.00` | 1,220,000,000.00 USD | 151,430.00 USD | 0.00 USD | `+85.45%` | `36.71` |
| `Live` | `Short` | `4135.00` | 1,220,000,000.00 USD | 608,480.00 USD | 0.00 USD | `+85.90%` | `147.15` |
| `Live` | `Short` | `4145.00` | 1,220,000,000.00 USD | 99,240.00 USD | 0.00 USD | `+86.35%` | `23.94` |
| `Live` | `Short` | `4155.00` | 1,220,000,000.00 USD | 681,920.00 USD | 0.00 USD | `+86.80%` | `164.12` |
| `Live` | `Short` | `4165.00` | 1,220,000,000.00 USD | 132,850.00 USD | 0.00 USD | `+87.25%` | `31.90` |
| `Live` | `Short` | `4175.00` | 1,220,000,000.00 USD | 209,470.00 USD | 0.00 USD | `+87.70%` | `50.17` |
| `Live` | `Short` | `4185.00` | 1,220,000,000.00 USD | 948,630.00 USD | 0.00 USD | `+88.15%` | `226.67` |
| `Live` | `Short` | `4195.00` | 1,260,000,000.00 USD | 32,730,000.00 USD | 0.00 USD | `+88.60%` | `7,801.99` |
| `Live` | `Short` | `4205.00` | 1,260,000,000.00 USD | 42,140.00 USD | 0.00 USD | `+89.05%` | `10.02` |
| `Live` | `Short` | `4215.00` | 1,260,000,000.00 USD | 42,320.00 USD | 0.00 USD | `+89.50%` | `10.04` |
| `Live` | `Short` | `4225.00` | 1,260,000,000.00 USD | 801,540.00 USD | 0.00 USD | `+89.95%` | `189.71` |
| `Live` | `Short` | `4235.00` | 1,340,000,000.00 USD | 83,560,000.00 USD | 0.00 USD | `+90.40%` | `19,730.11` |
| `Live` | `Short` | `4245.00` | 1,340,000,000.00 USD | 335,020.00 USD | 0.00 USD | `+90.85%` | `78.92` |
| `Live` | `Short` | `4255.00` | 1,340,000,000.00 USD | 420.39 USD | 0.00 USD | `+91.30%` | `0.10` |
| `Live` | `Short` | `4265.00` | 1,340,000,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+91.75%` | `509.16` |
| `Live` | `Short` | `4275.00` | 1,340,000,000.00 USD | 4,060.00 USD | 0.00 USD | `+92.20%` | `0.95` |
| `Live` | `Short` | `4285.00` | 1,340,000,000.00 USD | 2,450.00 USD | 0.00 USD | `+92.64%` | `0.57` |
| `Live` | `Short` | `4295.00` | 1,340,000,000.00 USD | 15,180.00 USD | 0.00 USD | `+93.09%` | `3.54` |
| `Live` | `Short` | `4305.00` | 1,340,000,000.00 USD | 17,120.00 USD | 0.00 USD | `+93.54%` | `3.98` |
| `Live` | `Short` | `4315.00` | 1,340,000,000.00 USD | 50,390.00 USD | 0.00 USD | `+93.99%` | `11.68` |
| `Live` | `Short` | `4325.00` | 1,340,000,000.00 USD | 36,530.00 USD | 0.00 USD | `+94.44%` | `8.45` |
| `Live` | `Short` | `4335.00` | 1,340,000,000.00 USD | 32,800.00 USD | 0.00 USD | `+94.89%` | `7.57` |
| `Live` | `Short` | `4345.00` | 1,340,000,000.00 USD | 204,690.00 USD | 0.00 USD | `+95.34%` | `47.11` |
| `Live` | `Short` | `4355.00` | 1,340,000,000.00 USD | 6,930.00 USD | 0.00 USD | `+95.79%` | `1.59` |
| `Live` | `Short` | `4365.00` | 1,340,000,000.00 USD | 1,140,000.00 USD | 0.00 USD | `+96.24%` | `262.00` |
| `Live` | `Short` | `4375.00` | 1,340,000,000.00 USD | 19,130.00 USD | 0.00 USD | `+96.69%` | `4.37` |
| `Live` | `Short` | `4385.00` | 1,340,000,000.00 USD | 4,180.00 USD | 0.00 USD | `+97.14%` | `0.95` |
| `Live` | `Short` | `4395.00` | 1,350,000,000.00 USD | 615,700.00 USD | 0.00 USD | `+97.59%` | `140.09` |
| `Live` | `Short` | `4405.00` | 1,350,000,000.00 USD | 23,210.00 USD | 0.00 USD | `+98.04%` | `5.27` |
| `Live` | `Short` | `4415.00` | 1,350,000,000.00 USD | 129,550.00 USD | 0.00 USD | `+98.49%` | `29.34` |
| `Live` | `Short` | `4425.00` | 1,350,000,000.00 USD | 8,230.00 USD | 0.00 USD | `+98.94%` | `1.86` |
| `Live` | `Short` | `4435.00` | 1,350,000,000.00 USD | 73,170.00 USD | 0.00 USD | `+99.39%` | `16.50` |
| `Live` | `Short` | `4445.00` | 1,350,000,000.00 USD | 25,610.00 USD | 0.00 USD | `+99.84%` | `5.76` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `485.00` | 70,280,000.00 USD | 0.00 USD | 278.83 USD | `-78.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `505.00` | 70,280,000.00 USD | 0.00 USD | 16,100.00 USD | `-77.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.00` | 70,270,000.00 USD | 0.00 USD | 563.16 USD | `-75.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `575.00` | 70,270,000.00 USD | 0.00 USD | 170.14 USD | `-74.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `615.00` | 70,270,000.00 USD | 0.00 USD | 259.78 USD | `-72.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.00` | 70,270,000.00 USD | 0.00 USD | 583.40 USD | `-71.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `655.00` | 70,270,000.00 USD | 0.00 USD | 613.93 USD | `-70.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.00` | 70,270,000.00 USD | 0.00 USD | 578.54 USD | `-69.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.00` | 70,270,000.00 USD | 0.00 USD | 242.21 USD | `-68.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.00` | 70,260,000.00 USD | 0.00 USD | 885.90 USD | `-68.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `715.00` | 70,260,000.00 USD | 0.00 USD | 4,130.00 USD | `-67.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `725.00` | 70,260,000.00 USD | 0.00 USD | 15,090.00 USD | `-67.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `755.00` | 70,240,000.00 USD | 0.00 USD | 177.27 USD | `-66.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `805.00` | 70,240,000.00 USD | 0.00 USD | 2,400.00 USD | `-63.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `835.00` | 70,240,000.00 USD | 0.00 USD | 1,670.00 USD | `-62.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `865.00` | 70,240,000.00 USD | 0.00 USD | 139,430.00 USD | `-61.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `875.00` | 70,100,000.00 USD | 0.00 USD | 918.49 USD | `-60.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `885.00` | 70,100,000.00 USD | 0.00 USD | 3,130.00 USD | `-60.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `905.00` | 70,100,000.00 USD | 0.00 USD | 2,780.00 USD | `-59.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `985.00` | 70,090,000.00 USD | 0.00 USD | 516.34 USD | `-55.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `995.00` | 70,090,000.00 USD | 0.00 USD | 100.50 USD | `-55.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1005.00` | 70,090,000.00 USD | 0.00 USD | 223,740.00 USD | `-54.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1015.00` | 69,870,000.00 USD | 0.00 USD | 445.08 USD | `-54.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1025.00` | 69,870,000.00 USD | 0.00 USD | 112.03 USD | `-53.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1045.00` | 69,870,000.00 USD | 0.00 USD | 1,260.00 USD | `-53.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1065.00` | 69,870,000.00 USD | 0.00 USD | 1,060.00 USD | `-52.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1075.00` | 69,870,000.00 USD | 0.00 USD | 995.34 USD | `-51.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1105.00` | 69,870,000.00 USD | 0.00 USD | 1,610.00 USD | `-50.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1115.00` | 69,860,000.00 USD | 0.00 USD | 11,050.00 USD | `-49.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1125.00` | 69,850,000.00 USD | 0.00 USD | 1,320.00 USD | `-49.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1155.00` | 69,850,000.00 USD | 0.00 USD | 1,000.00 USD | `-48.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1175.00` | 69,850,000.00 USD | 0.00 USD | 476.46 USD | `-47.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1185.00` | 69,850,000.00 USD | 0.00 USD | 972.41 USD | `-46.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1195.00` | 69,850,000.00 USD | 0.00 USD | 221.55 USD | `-46.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1205.00` | 69,850,000.00 USD | 0.00 USD | 3,110.00 USD | `-45.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1225.00` | 69,850,000.00 USD | 0.00 USD | 995.93 USD | `-44.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1245.00` | 69,850,000.00 USD | 0.00 USD | 951.93 USD | `-44.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1255.00` | 69,840,000.00 USD | 0.00 USD | 2,290.00 USD | `-43.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1285.00` | 69,840,000.00 USD | 0.00 USD | 9,050.00 USD | `-42.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1295.00` | 69,830,000.00 USD | 0.00 USD | 7,030.00 USD | `-41.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1305.00` | 69,830,000.00 USD | 0.00 USD | 23,030.00 USD | `-41.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1315.00` | 69,800,000.00 USD | 0.00 USD | 1,440.00 USD | `-40.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1335.00` | 69,800,000.00 USD | 0.00 USD | 281.69 USD | `-39.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1345.00` | 69,800,000.00 USD | 0.00 USD | 144,020.00 USD | `-39.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1355.00` | 69,660,000.00 USD | 0.00 USD | 128.86 USD | `-39.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1365.00` | 69,660,000.00 USD | 0.00 USD | 1,270.00 USD | `-38.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1375.00` | 69,660,000.00 USD | 0.00 USD | 4,160.00 USD | `-38.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1385.00` | 69,650,000.00 USD | 0.00 USD | 100,800.00 USD | `-37.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1395.00` | 69,550,000.00 USD | 0.00 USD | 535,600.00 USD | `-37.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1405.00` | 69,020,000.00 USD | 0.00 USD | 18,840.00 USD | `-36.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1425.00` | 69,000,000.00 USD | 0.00 USD | 6,450.00 USD | `-35.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1435.00` | 68,990,000.00 USD | 0.00 USD | 852.10 USD | `-35.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1445.00` | 68,990,000.00 USD | 0.00 USD | 1,610.00 USD | `-35.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1455.00` | 68,990,000.00 USD | 0.00 USD | 5,090.00 USD | `-34.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1465.00` | 68,980,000.00 USD | 0.00 USD | 19,730.00 USD | `-34.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1475.00` | 68,960,000.00 USD | 0.00 USD | 2,600.00 USD | `-33.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1485.00` | 68,960,000.00 USD | 0.00 USD | 19,930.00 USD | `-33.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1495.00` | 68,940,000.00 USD | 0.00 USD | 11,460.00 USD | `-32.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1505.00` | 68,930,000.00 USD | 0.00 USD | 68,840.00 USD | `-32.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1515.00` | 68,860,000.00 USD | 0.00 USD | 11,140.00 USD | `-31.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1525.00` | 68,850,000.00 USD | 0.00 USD | 31,900.00 USD | `-31.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1535.00` | 68,820,000.00 USD | 0.00 USD | 2,090.00 USD | `-30.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1545.00` | 68,810,000.00 USD | 0.00 USD | 960.99 USD | `-30.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1555.00` | 68,810,000.00 USD | 0.00 USD | 32,880.00 USD | `-30.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1565.00` | 68,780,000.00 USD | 0.00 USD | 10,660.00 USD | `-29.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1575.00` | 68,770,000.00 USD | 0.00 USD | 198,620.00 USD | `-29.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1585.00` | 68,570,000.00 USD | 0.00 USD | 4,990.00 USD | `-28.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1595.00` | 68,570,000.00 USD | 0.00 USD | 9,090.00 USD | `-28.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1605.00` | 68,560,000.00 USD | 0.00 USD | 431,660.00 USD | `-27.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1615.00` | 68,130,000.00 USD | 0.00 USD | 25,700.00 USD | `-27.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1625.00` | 68,100,000.00 USD | 0.00 USD | 15,920.00 USD | `-26.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1635.00` | 68,080,000.00 USD | 0.00 USD | 10,560.00 USD | `-26.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1645.00` | 68,070,000.00 USD | 0.00 USD | 323,930.00 USD | `-26.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1655.00` | 67,750,000.00 USD | 0.00 USD | 114,830.00 USD | `-25.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1665.00` | 67,630,000.00 USD | 0.00 USD | 865.13 USD | `-25.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1675.00` | 67,630,000.00 USD | 0.00 USD | 289.27 USD | `-24.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1685.00` | 67,630,000.00 USD | 0.00 USD | 35,320.00 USD | `-24.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1695.00` | 67,600,000.00 USD | 0.00 USD | 42,420.00 USD | `-23.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1705.00` | 67,560,000.00 USD | 0.00 USD | 84,860.00 USD | `-23.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1715.00` | 67,470,000.00 USD | 0.00 USD | 16,350.00 USD | `-22.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1725.00` | 67,450,000.00 USD | 0.00 USD | 47,500.00 USD | `-22.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1735.00` | 67,410,000.00 USD | 0.00 USD | 28,150.00 USD | `-22.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1745.00` | 67,380,000.00 USD | 0.00 USD | 3,180.00 USD | `-21.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1755.00` | 67,380,000.00 USD | 0.00 USD | 466,520.00 USD | `-21.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1765.00` | 66,910,000.00 USD | 0.00 USD | 77,450.00 USD | `-20.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1775.00` | 66,830,000.00 USD | 0.00 USD | 3,090.00 USD | `-20.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1785.00` | 66,830,000.00 USD | 0.00 USD | 8,500.00 USD | `-19.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1795.00` | 66,820,000.00 USD | 0.00 USD | 191,050.00 USD | `-19.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1805.00` | 66,630,000.00 USD | 0.00 USD | 756,110.00 USD | `-18.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1815.00` | 65,870,000.00 USD | 0.00 USD | 264,490.00 USD | `-18.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1825.00` | 65,610,000.00 USD | 0.00 USD | 39,660.00 USD | `-17.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1835.00` | 65,570,000.00 USD | 0.00 USD | 5,260.00 USD | `-17.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1845.00` | 65,560,000.00 USD | 0.00 USD | 30,780.00 USD | `-17.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1855.00` | 65,530,000.00 USD | 0.00 USD | 789,490.00 USD | `-16.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1865.00` | 64,740,000.00 USD | 0.00 USD | 41,250.00 USD | `-16.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1875.00` | 64,700,000.00 USD | 0.00 USD | 18,200,000.00 USD | `-15.70%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1885.00` | 46,510,000.00 USD | 0.00 USD | 19,770.00 USD | `-15.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1895.00` | 46,490,000.00 USD | 0.00 USD | 61,630.00 USD | `-14.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1905.00` | 46,420,000.00 USD | 0.00 USD | 153,490.00 USD | `-14.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1915.00` | 46,270,000.00 USD | 0.00 USD | 104,860.00 USD | `-13.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1925.00` | 46,170,000.00 USD | 0.00 USD | 19,310,000.00 USD | `-13.46%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1935.00` | 26,860,000.00 USD | 0.00 USD | 117,650.00 USD | `-13.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1945.00` | 26,740,000.00 USD | 0.00 USD | 61,020.00 USD | `-12.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1955.00` | 26,680,000.00 USD | 0.00 USD | 65,650.00 USD | `-12.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1965.00` | 26,610,000.00 USD | 0.00 USD | 138,620.00 USD | `-11.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1975.00` | 26,480,000.00 USD | 0.00 USD | 69,900.00 USD | `-11.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1985.00` | 26,410,000.00 USD | 0.00 USD | 105,150.00 USD | `-10.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1995.00` | 26,300,000.00 USD | 0.00 USD | 125,080.00 USD | `-10.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2005.00` | 26,180,000.00 USD | 0.00 USD | 2,090,000.00 USD | `-9.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2015.00` | 24,090,000.00 USD | 0.00 USD | 48,350.00 USD | `-9.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2025.00` | 24,040,000.00 USD | 0.00 USD | 15,730.00 USD | `-8.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2035.00` | 24,030,000.00 USD | 0.00 USD | 177,870.00 USD | `-8.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2045.00` | 23,850,000.00 USD | 0.00 USD | 39,670.00 USD | `-8.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2055.00` | 23,810,000.00 USD | 0.00 USD | 273,990.00 USD | `-7.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2065.00` | 23,530,000.00 USD | 0.00 USD | 828,390.00 USD | `-7.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2075.00` | 22,710,000.00 USD | 0.00 USD | 761,840.00 USD | `-6.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2085.00` | 21,940,000.00 USD | 0.00 USD | 136,050.00 USD | `-6.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2095.00` | 21,810,000.00 USD | 0.00 USD | 33,120.00 USD | `-5.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2105.00` | 21,770,000.00 USD | 0.00 USD | 470,680.00 USD | `-5.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2115.00` | 21,300,000.00 USD | 0.00 USD | 176,680.00 USD | `-4.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2125.00` | 21,130,000.00 USD | 0.00 USD | 210,460.00 USD | `-4.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2135.00` | 20,920,000.00 USD | 0.00 USD | 342,670.00 USD | `-4.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2145.00` | 20,570,000.00 USD | 0.00 USD | 526,510.00 USD | `-3.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2155.00` | 20,050,000.00 USD | 0.00 USD | 1,820,000.00 USD | `-3.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2165.00` | 18,230,000.00 USD | 0.00 USD | 1,680,000.00 USD | `-2.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2175.00` | 16,540,000.00 USD | 0.00 USD | 9,750,000.00 USD | `-2.22%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2185.00` | 6,790,000.00 USD | 0.00 USD | 219,480.00 USD | `-1.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2195.00` | 6,570,000.00 USD | 0.00 USD | 3,040,000.00 USD | `-1.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2205.00` | 3,530,000.00 USD | 0.00 USD | 1,580,000.00 USD | `-0.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2215.00` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | `-0.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2225.00` | 583,300.00 USD | 583,300.00 USD | 0.00 USD | `+0.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2235.00` | 1,950,000.00 USD | 1,360,000.00 USD | 0.00 USD | `+0.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2245.00` | 2,810,000.00 USD | 865,920.00 USD | 0.00 USD | `+0.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2255.00` | 3,360,000.00 USD | 549,610.00 USD | 0.00 USD | `+1.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2265.00` | 5,250,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+1.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2275.00` | 5,700,000.00 USD | 447,920.00 USD | 0.00 USD | `+2.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2285.00` | 6,540,000.00 USD | 840,590.00 USD | 0.00 USD | `+2.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2295.00` | 6,990,000.00 USD | 444,860.00 USD | 0.00 USD | `+3.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2305.00` | 17,010,000.00 USD | 10,020,000.00 USD | 0.00 USD | `+3.63%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2315.00` | 18,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | `+4.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2325.00` | 18,690,000.00 USD | 231,970.00 USD | 0.00 USD | `+4.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2335.00` | 18,860,000.00 USD | 168,630.00 USD | 0.00 USD | `+4.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2345.00` | 20,430,000.00 USD | 1,570,000.00 USD | 0.00 USD | `+5.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2355.00` | 21,680,000.00 USD | 1,260,000.00 USD | 0.00 USD | `+5.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2365.00` | 23,890,000.00 USD | 2,210,000.00 USD | 0.00 USD | `+6.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2375.00` | 24,060,000.00 USD | 163,240.00 USD | 0.00 USD | `+6.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2385.00` | 26,020,000.00 USD | 1,970,000.00 USD | 0.00 USD | `+7.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2395.00` | 27,120,000.00 USD | 1,100,000.00 USD | 0.00 USD | `+7.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2405.00` | 29,630,000.00 USD | 2,510,000.00 USD | 0.00 USD | `+8.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2415.00` | 29,920,000.00 USD | 286,440.00 USD | 0.00 USD | `+8.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2425.00` | 32,200,000.00 USD | 2,280,000.00 USD | 0.00 USD | `+9.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2435.00` | 32,390,000.00 USD | 189,700.00 USD | 0.00 USD | `+9.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2445.00` | 34,870,000.00 USD | 2,490,000.00 USD | 0.00 USD | `+9.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2455.00` | 35,020,000.00 USD | 141,470.00 USD | 0.00 USD | `+10.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2465.00` | 37,140,000.00 USD | 2,120,000.00 USD | 0.00 USD | `+10.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2475.00` | 37,320,000.00 USD | 181,240.00 USD | 0.00 USD | `+11.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2485.00` | 39,420,000.00 USD | 2,100,000.00 USD | 0.00 USD | `+11.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2495.00` | 39,540,000.00 USD | 122,320.00 USD | 0.00 USD | `+12.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2505.00` | 44,600,000.00 USD | 5,060,000.00 USD | 0.00 USD | `+12.62%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2515.00` | 52,200,000.00 USD | 7,600,000.00 USD | 0.00 USD | `+13.07%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2525.00` | 54,820,000.00 USD | 2,610,000.00 USD | 0.00 USD | `+13.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2535.00` | 54,880,000.00 USD | 61,230.00 USD | 0.00 USD | `+13.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2545.00` | 57,060,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+14.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2555.00` | 57,260,000.00 USD | 199,370.00 USD | 0.00 USD | `+14.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2565.00` | 59,620,000.00 USD | 2,360,000.00 USD | 0.00 USD | `+15.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2575.00` | 59,710,000.00 USD | 93,110.00 USD | 0.00 USD | `+15.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2585.00` | 62,220,000.00 USD | 2,510,000.00 USD | 0.00 USD | `+16.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2595.00` | 62,240,000.00 USD | 10,500.00 USD | 0.00 USD | `+16.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2605.00` | 65,510,000.00 USD | 3,280,000.00 USD | 0.00 USD | `+17.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2615.00` | 65,590,000.00 USD | 79,040.00 USD | 0.00 USD | `+17.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2625.00` | 67,770,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+18.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2635.00` | 67,920,000.00 USD | 147,930.00 USD | 0.00 USD | `+18.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2645.00` | 70,040,000.00 USD | 2,130,000.00 USD | 0.00 USD | `+18.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2655.00` | 70,350,000.00 USD | 306,950.00 USD | 0.00 USD | `+19.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2665.00` | 72,490,000.00 USD | 2,140,000.00 USD | 0.00 USD | `+19.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2675.00` | 72,750,000.00 USD | 261,420.00 USD | 0.00 USD | `+20.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2685.00` | 74,930,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+20.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2695.00` | 75,020,000.00 USD | 94,620.00 USD | 0.00 USD | `+21.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2705.00` | 77,860,000.00 USD | 2,840,000.00 USD | 0.00 USD | `+21.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2715.00` | 77,940,000.00 USD | 76,590.00 USD | 0.00 USD | `+22.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2725.00` | 78,230,000.00 USD | 286,910.00 USD | 0.00 USD | `+22.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2735.00` | 78,270,000.00 USD | 43,050.00 USD | 0.00 USD | `+22.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2745.00` | 78,450,000.00 USD | 178,210.00 USD | 0.00 USD | `+23.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2755.00` | 79,340,000.00 USD | 892,290.00 USD | 0.00 USD | `+23.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2765.00` | 79,440,000.00 USD | 103,020.00 USD | 0.00 USD | `+24.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2775.00` | 80,020,000.00 USD | 579,030.00 USD | 0.00 USD | `+24.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2785.00` | 80,060,000.00 USD | 35,580.00 USD | 0.00 USD | `+25.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2795.00` | 80,080,000.00 USD | 17,550.00 USD | 0.00 USD | `+25.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2805.00` | 80,980,000.00 USD | 905,020.00 USD | 0.00 USD | `+26.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2815.00` | 81,030,000.00 USD | 52,490.00 USD | 0.00 USD | `+26.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2825.00` | 81,080,000.00 USD | 43,930.00 USD | 0.00 USD | `+27.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2835.00` | 81,360,000.00 USD | 286,140.00 USD | 0.00 USD | `+27.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2845.00` | 82,370,000.00 USD | 1,000,000.00 USD | 0.00 USD | `+27.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2855.00` | 83,640,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+28.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2865.00` | 83,650,000.00 USD | 11,150.00 USD | 0.00 USD | `+28.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2875.00` | 83,650,000.00 USD | 2,460.00 USD | 0.00 USD | `+29.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2885.00` | 83,960,000.00 USD | 305,820.00 USD | 0.00 USD | `+29.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2895.00` | 83,980,000.00 USD | 16,190.00 USD | 0.00 USD | `+30.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2905.00` | 85,460,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+30.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2915.00` | 85,470,000.00 USD | 10,340.00 USD | 0.00 USD | `+31.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2925.00` | 85,470,000.00 USD | 3,050.00 USD | 0.00 USD | `+31.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2935.00` | 85,530,000.00 USD | 52,370.00 USD | 0.00 USD | `+31.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2945.00` | 85,560,000.00 USD | 34,650.00 USD | 0.00 USD | `+32.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2955.00` | 85,610,000.00 USD | 44,750.00 USD | 0.00 USD | `+32.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2965.00` | 85,720,000.00 USD | 113,340.00 USD | 0.00 USD | `+33.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2975.00` | 85,860,000.00 USD | 145,510.00 USD | 0.00 USD | `+33.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2985.00` | 86,800,000.00 USD | 931,470.00 USD | 0.00 USD | `+34.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2995.00` | 91,720,000.00 USD | 4,920,000.00 USD | 0.00 USD | `+34.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3005.00` | 93,800,000.00 USD | 2,080,000.00 USD | 0.00 USD | `+35.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3015.00` | 93,810,000.00 USD | 9,740.00 USD | 0.00 USD | `+35.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3025.00` | 93,840,000.00 USD | 35,380.00 USD | 0.00 USD | `+36.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3035.00` | 93,920,000.00 USD | 74,910.00 USD | 0.00 USD | `+36.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3045.00` | 93,940,000.00 USD | 22,460.00 USD | 0.00 USD | `+36.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3055.00` | 94,710,000.00 USD | 771,070.00 USD | 0.00 USD | `+37.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3065.00` | 94,710,000.00 USD | 612.69 USD | 0.00 USD | `+37.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3075.00` | 94,760,000.00 USD | 49,330.00 USD | 0.00 USD | `+38.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3085.00` | 94,780,000.00 USD | 19,570.00 USD | 0.00 USD | `+38.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3095.00` | 94,780,000.00 USD | 928.50 USD | 0.00 USD | `+39.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3105.00` | 106,660,000.00 USD | 11,880,000.00 USD | 0.00 USD | `+39.59%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `3115.00` | 106,770,000.00 USD | 110,480.00 USD | 0.00 USD | `+40.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3125.00` | 107,150,000.00 USD | 381,020.00 USD | 0.00 USD | `+40.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3135.00` | 107,150,000.00 USD | 674.02 USD | 0.00 USD | `+40.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3145.00` | 107,150,000.00 USD | 2,660.00 USD | 0.00 USD | `+41.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3155.00` | 107,210,000.00 USD | 58,930.00 USD | 0.00 USD | `+41.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3165.00` | 107,220,000.00 USD | 9,860.00 USD | 0.00 USD | `+42.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3175.00` | 107,220,000.00 USD | 149.22 USD | 0.00 USD | `+42.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3185.00` | 107,230,000.00 USD | 1,330.00 USD | 0.00 USD | `+43.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3195.00` | 107,270,000.00 USD | 41,120.00 USD | 0.00 USD | `+43.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3205.00` | 107,930,000.00 USD | 660,240.00 USD | 0.00 USD | `+44.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3215.00` | 107,930,000.00 USD | 1,760.00 USD | 0.00 USD | `+44.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3225.00` | 108,080,000.00 USD | 156,230.00 USD | 0.00 USD | `+44.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3235.00` | 108,080,000.00 USD | 167.25 USD | 0.00 USD | `+45.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3245.00` | 108,140,000.00 USD | 57,500.00 USD | 0.00 USD | `+45.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3255.00` | 108,380,000.00 USD | 236,580.00 USD | 0.00 USD | `+46.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3265.00` | 108,390,000.00 USD | 15,710.00 USD | 0.00 USD | `+46.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3275.00` | 108,400,000.00 USD | 1,630.00 USD | 0.00 USD | `+47.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3285.00` | 108,540,000.00 USD | 141,980.00 USD | 0.00 USD | `+47.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3295.00` | 108,550,000.00 USD | 15,350.00 USD | 0.00 USD | `+48.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3305.00` | 109,970,000.00 USD | 1,410,000.00 USD | 0.00 USD | `+48.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3315.00` | 110,360,000.00 USD | 389,970.00 USD | 0.00 USD | `+49.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3325.00` | 110,380,000.00 USD | 24,200.00 USD | 0.00 USD | `+49.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3335.00` | 110,380,000.00 USD | 4,350.00 USD | 0.00 USD | `+49.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3345.00` | 110,390,000.00 USD | 2,170.00 USD | 0.00 USD | `+50.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3355.00` | 110,390,000.00 USD | 334.49 USD | 0.00 USD | `+50.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3365.00` | 110,390,000.00 USD | 295.78 USD | 0.00 USD | `+51.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3375.00` | 110,410,000.00 USD | 21,260.00 USD | 0.00 USD | `+51.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3385.00` | 110,470,000.00 USD | 58,010.00 USD | 0.00 USD | `+52.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3395.00` | 110,790,000.00 USD | 321,800.00 USD | 0.00 USD | `+52.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3405.00` | 112,270,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+53.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3415.00` | 112,280,000.00 USD | 5,700.00 USD | 0.00 USD | `+53.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3425.00` | 112,290,000.00 USD | 16,310.00 USD | 0.00 USD | `+53.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3445.00` | 112,310,000.00 USD | 15,030.00 USD | 0.00 USD | `+54.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3455.00` | 112,330,000.00 USD | 18,600.00 USD | 0.00 USD | `+55.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3465.00` | 112,330,000.00 USD | 495.50 USD | 0.00 USD | `+55.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3475.00` | 112,330,000.00 USD | 3,190.00 USD | 0.00 USD | `+56.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3485.00` | 112,370,000.00 USD | 43,610.00 USD | 0.00 USD | `+56.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3495.00` | 112,370,000.00 USD | 158.32 USD | 0.00 USD | `+57.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3505.00` | 112,820,000.00 USD | 446,770.00 USD | 0.00 USD | `+57.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3515.00` | 112,860,000.00 USD | 43,510.00 USD | 0.00 USD | `+58.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3525.00` | 112,870,000.00 USD | 3,690.00 USD | 0.00 USD | `+58.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3535.00` | 112,880,000.00 USD | 9,810.00 USD | 0.00 USD | `+58.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3555.00` | 112,970,000.00 USD | 90,810.00 USD | 0.00 USD | `+59.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3565.00` | 112,970,000.00 USD | 2,300.00 USD | 0.00 USD | `+60.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3575.00` | 112,970,000.00 USD | 2,870.00 USD | 0.00 USD | `+60.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3585.00` | 112,970,000.00 USD | 354.92 USD | 0.00 USD | `+61.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3595.00` | 112,990,000.00 USD | 13,160.00 USD | 0.00 USD | `+61.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3605.00` | 113,090,000.00 USD | 101,080.00 USD | 0.00 USD | `+62.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3615.00` | 113,090,000.00 USD | 199.55 USD | 0.00 USD | `+62.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3625.00` | 113,100,000.00 USD | 10,210.00 USD | 0.00 USD | `+62.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3635.00` | 113,110,000.00 USD | 7,790.00 USD | 0.00 USD | `+63.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3645.00` | 113,110,000.00 USD | 3,860.00 USD | 0.00 USD | `+63.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3655.00` | 113,110,000.00 USD | 820.18 USD | 0.00 USD | `+64.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3665.00` | 113,120,000.00 USD | 8,130.00 USD | 0.00 USD | `+64.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3675.00` | 113,180,000.00 USD | 55,120.00 USD | 0.00 USD | `+65.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3685.00` | 113,180,000.00 USD | 1,410.00 USD | 0.00 USD | `+65.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3705.00` | 113,180,000.00 USD | 819.92 USD | 0.00 USD | `+66.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3715.00` | 113,180,000.00 USD | 323.58 USD | 0.00 USD | `+67.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3725.00` | 113,180,000.00 USD | 1,400.00 USD | 0.00 USD | `+67.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3735.00` | 113,190,000.00 USD | 6,490.00 USD | 0.00 USD | `+67.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3745.00` | 113,190,000.00 USD | 165.90 USD | 0.00 USD | `+68.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3755.00` | 113,190,000.00 USD | 751.00 USD | 0.00 USD | `+68.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3785.00` | 113,190,000.00 USD | 286.90 USD | 0.00 USD | `+70.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3795.00` | 113,190,000.00 USD | 1,560.00 USD | 0.00 USD | `+70.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3805.00` | 113,920,000.00 USD | 732,630.00 USD | 0.00 USD | `+71.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3815.00` | 113,940,000.00 USD | 20,930.00 USD | 0.00 USD | `+71.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3825.00` | 113,950,000.00 USD | 8,380.00 USD | 0.00 USD | `+71.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3835.00` | 113,950,000.00 USD | 711.78 USD | 0.00 USD | `+72.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3845.00` | 113,950,000.00 USD | 355.28 USD | 0.00 USD | `+72.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3855.00` | 113,960,000.00 USD | 5,170.00 USD | 0.00 USD | `+73.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3885.00` | 113,980,000.00 USD | 19,430.00 USD | 0.00 USD | `+74.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3905.00` | 113,990,000.00 USD | 12,120.00 USD | 0.00 USD | `+75.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3915.00` | 114,710,000.00 USD | 717,170.00 USD | 0.00 USD | `+76.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3935.00` | 114,750,000.00 USD | 42,570.00 USD | 0.00 USD | `+76.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3945.00` | 114,810,000.00 USD | 59,170.00 USD | 0.00 USD | `+77.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3955.00` | 114,810,000.00 USD | 1,380.00 USD | 0.00 USD | `+77.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3975.00` | 114,820,000.00 USD | 6,960.00 USD | 0.00 USD | `+78.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3985.00` | 114,830,000.00 USD | 14,610.00 USD | 0.00 USD | `+79.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3995.00` | 114,830,000.00 USD | 4,280.00 USD | 0.00 USD | `+79.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4005.00` | 117,470,000.00 USD | 2,640,000.00 USD | 0.00 USD | `+80.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4035.00` | 117,470,000.00 USD | 898.59 USD | 0.00 USD | `+81.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4055.00` | 117,470,000.00 USD | 811.00 USD | 0.00 USD | `+82.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4075.00` | 117,480,000.00 USD | 4,310.00 USD | 0.00 USD | `+83.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4085.00` | 117,480,000.00 USD | 3,050.00 USD | 0.00 USD | `+83.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4105.00` | 117,520,000.00 USD | 36,740.00 USD | 0.00 USD | `+84.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4115.00` | 117,520,000.00 USD | 5,990.00 USD | 0.00 USD | `+85.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4125.00` | 117,520,000.00 USD | 372.90 USD | 0.00 USD | `+85.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4145.00` | 117,520,000.00 USD | 395.43 USD | 0.00 USD | `+86.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4185.00` | 117,520,000.00 USD | 376.65 USD | 0.00 USD | `+88.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4205.00` | 117,570,000.00 USD | 42,260.00 USD | 0.00 USD | `+89.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4215.00` | 117,570,000.00 USD | 460.70 USD | 0.00 USD | `+89.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4225.00` | 117,570,000.00 USD | 1,270.00 USD | 0.00 USD | `+89.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4255.00` | 117,570,000.00 USD | 4,300.00 USD | 0.00 USD | `+91.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4265.00` | 117,570,000.00 USD | 437.16 USD | 0.00 USD | `+91.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4275.00` | 117,640,000.00 USD | 64,550.00 USD | 0.00 USD | `+92.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4285.00` | 117,640,000.00 USD | 1,610.00 USD | 0.00 USD | `+92.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4305.00` | 117,730,000.00 USD | 94,600.00 USD | 0.00 USD | `+93.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4315.00` | 117,730,000.00 USD | 1,070.00 USD | 0.00 USD | `+93.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4345.00` | 117,750,000.00 USD | 11,270.00 USD | 0.00 USD | `+95.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4355.00` | 117,750,000.00 USD | 2,400.00 USD | 0.00 USD | `+95.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4375.00` | 117,790,000.00 USD | 43,750.00 USD | 0.00 USD | `+96.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4385.00` | 117,860,000.00 USD | 64,570.00 USD | 0.00 USD | `+97.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4395.00` | 117,860,000.00 USD | 1,050.00 USD | 0.00 USD | `+97.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4405.00` | 117,910,000.00 USD | 56,760.00 USD | 0.00 USD | `+98.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4415.00` | 117,930,000.00 USD | 11,480.00 USD | 0.00 USD | `+98.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4425.00` | 117,930,000.00 USD | 2,510.00 USD | 0.00 USD | `+98.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4435.00` | 118,110,000.00 USD | 177,400.00 USD | 0.00 USD | `+99.39%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1972.30` | 736,320,000.00 USD | 0.00 USD | 736,320,000.00 USD | 0.00 USD | 105,610.00 USD | 26,880.00 USD |
| `7D` | `1975.10` | 736,180,000.00 USD | 0.00 USD | 736,180,000.00 USD | 0.00 USD | 0.00 USD | 49,530.00 USD |
| `7D` | `1977.90` | 736,130,000.00 USD | 0.00 USD | 736,130,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1983.50` | 733,890,000.00 USD | 0.00 USD | 733,890,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD |
| `7D` | `1986.30` | 733,690,000.00 USD | 0.00 USD | 733,690,000.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1989.10` | 729,960,000.00 USD | 0.00 USD | 729,960,000.00 USD | 0.00 USD | 1,780,000.00 USD | 38,060.00 USD |
| `7D` | `1991.90` | 728,140,000.00 USD | 0.00 USD | 728,140,000.00 USD | 1,390,000.00 USD | 1,320,000.00 USD | 0.00 USD |
| `7D` | `1994.70` | 725,430,000.00 USD | 0.00 USD | 725,430,000.00 USD | 0.00 USD | 0.00 USD | 808,380.00 USD |
| `7D` | `1997.50` | 724,630,000.00 USD | 0.00 USD | 724,630,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1999.20` | 632,340,000.00 USD | 0.00 USD | 632,340,000.00 USD | 43,520.00 USD | 104,180.00 USD | 486,830.00 USD |
| `1D` | `2001.60` | 631,700,000.00 USD | 0.00 USD | 631,700,000.00 USD | 676,180.00 USD | 580,080.00 USD | 590,220.00 USD |
| `7D` | `2003.10` | 723,280,000.00 USD | 0.00 USD | 723,280,000.00 USD | 0.00 USD | 266,430.00 USD | 594,510.00 USD |
| `1D` | `2004.00` | 629,860,000.00 USD | 0.00 USD | 629,860,000.00 USD | 390,870.00 USD | 358,610.00 USD | 685,180.00 USD |
| `7D` | `2005.90` | 722,420,000.00 USD | 0.00 USD | 722,420,000.00 USD | 0.00 USD | 475,660.00 USD | 0.00 USD |
| `1D` | `2006.40` | 628,420,000.00 USD | 0.00 USD | 628,420,000.00 USD | 641,010.00 USD | 35,460.00 USD | 0.00 USD |
| `7D` | `2008.70` | 721,950,000.00 USD | 0.00 USD | 721,950,000.00 USD | 807,770.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2008.80` | 627,750,000.00 USD | 0.00 USD | 627,750,000.00 USD | 0.00 USD | 548,050.00 USD | 126,940.00 USD |
| `1D` | `2011.20` | 627,070,000.00 USD | 0.00 USD | 627,070,000.00 USD | 764,070.00 USD | 490,470.00 USD | 366,100.00 USD |
| `7D` | `2011.50` | 721,140,000.00 USD | 0.00 USD | 721,140,000.00 USD | 170,840.00 USD | 92,470.00 USD | 689,450.00 USD |
| `1D` | `2013.60` | 625,450,000.00 USD | 0.00 USD | 625,450,000.00 USD | 69,570.00 USD | 258,510.00 USD | 25,320.00 USD |
| `1D` | `2016.00` | 625,100,000.00 USD | 0.00 USD | 625,100,000.00 USD | 384,540.00 USD | 605,010.00 USD | 193,290.00 USD |
| `7D` | `2017.10` | 720,190,000.00 USD | 0.00 USD | 720,190,000.00 USD | 0.00 USD | 0.00 USD | 21,830.00 USD |
| `1D` | `2018.40` | 623,910,000.00 USD | 0.00 USD | 623,910,000.00 USD | 772,840.00 USD | 885,870.00 USD | 714,280.00 USD |
| `1D` | `2020.80` | 621,540,000.00 USD | 0.00 USD | 621,540,000.00 USD | 622,680.00 USD | 1,430,000.00 USD | 673,150.00 USD |
| `7D` | `2022.70` | 720,160,000.00 USD | 0.00 USD | 720,160,000.00 USD | 1,070,000.00 USD | 0.00 USD | 934,340.00 USD |
| `1D` | `2023.20` | 618,810,000.00 USD | 0.00 USD | 618,810,000.00 USD | 792,850.00 USD | 120,570.00 USD | 1,430,000.00 USD |
| `7D` | `2025.50` | 718,160,000.00 USD | 0.00 USD | 718,160,000.00 USD | 0.00 USD | 177,070.00 USD | 0.00 USD |
| `1D` | `2025.60` | 616,460,000.00 USD | 0.00 USD | 616,460,000.00 USD | 414,330.00 USD | 1,100,000.00 USD | 231,680.00 USD |
| `1D` | `2028.00` | 614,720,000.00 USD | 0.00 USD | 614,720,000.00 USD | 2,770,000.00 USD | 978,910.00 USD | 615,730.00 USD |
| `7D` | `2028.30` | 717,980,000.00 USD | 0.00 USD | 717,980,000.00 USD | 1,100,000.00 USD | 0.00 USD | 35,180.00 USD |
| `1D` | `2030.40` | 610,350,000.00 USD | 0.00 USD | 610,350,000.00 USD | 87,180.00 USD | 366,120.00 USD | 654,250.00 USD |
| `7D` | `2031.10` | 716,850,000.00 USD | 0.00 USD | 716,850,000.00 USD | 0.00 USD | 3,520,000.00 USD | 1,050,000.00 USD |
| `1D` | `2032.80` | 609,250,000.00 USD | 0.00 USD | 609,250,000.00 USD | 1,360,000.00 USD | 1,490,000.00 USD | 707,170.00 USD |
| `7D` | `2033.90` | 712,280,000.00 USD | 0.00 USD | 712,280,000.00 USD | 0.00 USD | 0.00 USD | 1,350,000.00 USD |
| `1D` | `2035.20` | 605,690,000.00 USD | 0.00 USD | 605,690,000.00 USD | 1,150,000.00 USD | 19,490.00 USD | 165,760.00 USD |
| `7D` | `2036.70` | 710,920,000.00 USD | 0.00 USD | 710,920,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD |
| `1D` | `2037.60` | 604,350,000.00 USD | 0.00 USD | 604,350,000.00 USD | 396,700.00 USD | 458,110.00 USD | 378,700.00 USD |
| `7D` | `2039.50` | 710,590,000.00 USD | 0.00 USD | 710,590,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2040.00` | 603,120,000.00 USD | 0.00 USD | 603,120,000.00 USD | 542,670.00 USD | 178,560.00 USD | 31,670.00 USD |
| `1D` | `2042.40` | 602,360,000.00 USD | 0.00 USD | 602,360,000.00 USD | 626,840.00 USD | 0.00 USD | 166,650.00 USD |
| `1D` | `2044.80` | 601,570,000.00 USD | 0.00 USD | 601,570,000.00 USD | 0.00 USD | 0.00 USD | 26,280.00 USD |
| `7D` | `2045.10` | 709,140,000.00 USD | 0.00 USD | 709,140,000.00 USD | 0.00 USD | 149,500.00 USD | 149,910.00 USD |
| `1D` | `2047.20` | 601,540,000.00 USD | 0.00 USD | 601,540,000.00 USD | 467,370.00 USD | 0.00 USD | 367,650.00 USD |
| `1D` | `2049.60` | 600,710,000.00 USD | 0.00 USD | 600,710,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD |
| `7D` | `2050.70` | 708,840,000.00 USD | 0.00 USD | 708,840,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2053.50` | 708,620,000.00 USD | 0.00 USD | 708,620,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD |
| `1D` | `2054.40` | 599,600,000.00 USD | 0.00 USD | 599,600,000.00 USD | 0.00 USD | 88,880.00 USD | 28,160.00 USD |
| `1D` | `2056.80` | 599,480,000.00 USD | 0.00 USD | 599,480,000.00 USD | 242,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2059.10` | 706,330,000.00 USD | 0.00 USD | 706,330,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD |
| `1D` | `2059.20` | 599,240,000.00 USD | 0.00 USD | 599,240,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `1D` | `2061.60` | 598,490,000.00 USD | 0.00 USD | 598,490,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD |
| `7D` | `2061.90` | 705,990,000.00 USD | 0.00 USD | 705,990,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD |
| `1D` | `2064.00` | 598,410,000.00 USD | 0.00 USD | 598,410,000.00 USD | 563,140.00 USD | 494,150.00 USD | 510,200.00 USD |
| `7D` | `2064.70` | 700,730,000.00 USD | 0.00 USD | 700,730,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 979,910.00 USD |
| `1D` | `2066.40` | 596,840,000.00 USD | 0.00 USD | 596,840,000.00 USD | 387,410.00 USD | 42,880.00 USD | 0.00 USD |
| `7D` | `2067.50` | 698,270,000.00 USD | 0.00 USD | 698,270,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 228,380.00 USD |
| `1D` | `2068.80` | 596,410,000.00 USD | 0.00 USD | 596,410,000.00 USD | 57,300.00 USD | 624,040.00 USD | 0.00 USD |
| `7D` | `2070.30` | 696,620,000.00 USD | 0.00 USD | 696,620,000.00 USD | 3,600,000.00 USD | 2,730,000.00 USD | 1,240,000.00 USD |
| `1D` | `2071.20` | 595,730,000.00 USD | 0.00 USD | 595,730,000.00 USD | 47,910.00 USD | 534,600.00 USD | 0.00 USD |
| `7D` | `2073.10` | 689,060,000.00 USD | 0.00 USD | 689,060,000.00 USD | 2,870,000.00 USD | 2,180,000.00 USD | 2,030,000.00 USD |
| `1D` | `2073.60` | 595,150,000.00 USD | 0.00 USD | 595,150,000.00 USD | 25,660.00 USD | 20,640.00 USD | 420,170.00 USD |
| `7D` | `2075.90` | 681,980,000.00 USD | 0.00 USD | 681,980,000.00 USD | 3,910,000.00 USD | 4,290,000.00 USD | 4,300,000.00 USD |
| `1D` | `2076.00` | 594,680,000.00 USD | 0.00 USD | 594,680,000.00 USD | 354,080.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2078.40` | 594,320,000.00 USD | 0.00 USD | 594,320,000.00 USD | 0.00 USD | 25,190.00 USD | 0.00 USD |
| `7D` | `2078.70` | 669,480,000.00 USD | 0.00 USD | 669,480,000.00 USD | 4,160,000.00 USD | 3,730,000.00 USD | 2,060,000.00 USD |
| `1D` | `2080.80` | 594,300,000.00 USD | 0.00 USD | 594,300,000.00 USD | 77,960.00 USD | 29,610.00 USD | 199,420.00 USD |
| `7D` | `2081.50` | 659,530,000.00 USD | 0.00 USD | 659,530,000.00 USD | 4,400,000.00 USD | 1,290,000.00 USD | 1,220,000.00 USD |
| `1D` | `2083.20` | 593,990,000.00 USD | 0.00 USD | 593,990,000.00 USD | 827,940.00 USD | 4,240.00 USD | 209,600.00 USD |
| `7D` | `2084.30` | 652,620,000.00 USD | 0.00 USD | 652,620,000.00 USD | 2,380,000.00 USD | 1,510,000.00 USD | 3,500,000.00 USD |
| `1D` | `2085.60` | 592,950,000.00 USD | 0.00 USD | 592,950,000.00 USD | 528,660.00 USD | 242,120.00 USD | 817,510.00 USD |
| `7D` | `2087.10` | 645,230,000.00 USD | 0.00 USD | 645,230,000.00 USD | 2,920,000.00 USD | 2,750,000.00 USD | 3,020,000.00 USD |
| `1D` | `2088.00` | 591,360,000.00 USD | 0.00 USD | 591,360,000.00 USD | 438,420.00 USD | 227,880.00 USD | 306,610.00 USD |
| `7D` | `2089.90` | 636,550,000.00 USD | 0.00 USD | 636,550,000.00 USD | 4,130,000.00 USD | 948,120.00 USD | 3,160,000.00 USD |
| `1D` | `2090.40` | 590,390,000.00 USD | 0.00 USD | 590,390,000.00 USD | 761,770.00 USD | 224,660.00 USD | 446,120.00 USD |
| `7D` | `2092.70` | 628,310,000.00 USD | 0.00 USD | 628,310,000.00 USD | 4,680,000.00 USD | 737,060.00 USD | 6,220,000.00 USD |
| `1D` | `2092.80` | 588,960,000.00 USD | 0.00 USD | 588,960,000.00 USD | 752,390.00 USD | 334,060.00 USD | 176,780.00 USD |
| `1D` | `2095.20` | 587,690,000.00 USD | 0.00 USD | 587,690,000.00 USD | 1,840,000.00 USD | 1,130,000.00 USD | 1,480,000.00 USD |
| `7D` | `2095.50` | 616,680,000.00 USD | 0.00 USD | 616,680,000.00 USD | 2,480,000.00 USD | 2,010,000.00 USD | 1,020,000.00 USD |
| `1D` | `2097.60` | 583,230,000.00 USD | 0.00 USD | 583,230,000.00 USD | 175,830.00 USD | 488,160.00 USD | 517,910.00 USD |
| `7D` | `2098.30` | 611,170,000.00 USD | 0.00 USD | 611,170,000.00 USD | 3,020,000.00 USD | 3,130,000.00 USD | 1,480,000.00 USD |
| `1D` | `2100.00` | 582,050,000.00 USD | 0.00 USD | 582,050,000.00 USD | 307,340.00 USD | 779,630.00 USD | 20,670.00 USD |
| `7D` | `2101.10` | 603,550,000.00 USD | 0.00 USD | 603,550,000.00 USD | 631,640.00 USD | 1,240,000.00 USD | 3,400,000.00 USD |
| `1D` | `2102.40` | 580,940,000.00 USD | 0.00 USD | 580,940,000.00 USD | 211,840.00 USD | 371,740.00 USD | 513,570.00 USD |
| `7D` | `2103.90` | 598,270,000.00 USD | 0.00 USD | 598,270,000.00 USD | 1,130,000.00 USD | 738,240.00 USD | 2,320,000.00 USD |
| `1D` | `2104.80` | 579,850,000.00 USD | 0.00 USD | 579,850,000.00 USD | 3,570,000.00 USD | 1,160,000.00 USD | 683,370.00 USD |
| `7D` | `2106.70` | 594,080,000.00 USD | 0.00 USD | 594,080,000.00 USD | 1,700,000.00 USD | 834,660.00 USD | 1,180,000.00 USD |
| `1D` | `2107.20` | 574,430,000.00 USD | 0.00 USD | 574,430,000.00 USD | 677,650.00 USD | 0.00 USD | 496,850.00 USD |
| `7D` | `2109.50` | 590,360,000.00 USD | 0.00 USD | 590,360,000.00 USD | 7,750,000.00 USD | 1,800,000.00 USD | 1,770,000.00 USD |
| `1D` | `2109.60` | 573,260,000.00 USD | 0.00 USD | 573,260,000.00 USD | 118,210.00 USD | 31,550.00 USD | 6,190.00 USD |
| `1D` | `2112.00` | 573,100,000.00 USD | 0.00 USD | 573,100,000.00 USD | 490,860.00 USD | 360,140.00 USD | 221,490.00 USD |
| `7D` | `2112.30` | 579,050,000.00 USD | 0.00 USD | 579,050,000.00 USD | 3,920,000.00 USD | 1,480,000.00 USD | 3,710,000.00 USD |
| `1D` | `2114.40` | 572,030,000.00 USD | 0.00 USD | 572,030,000.00 USD | 614,540.00 USD | 231,420.00 USD | 286,140.00 USD |
| `7D` | `2115.10` | 569,930,000.00 USD | 0.00 USD | 569,930,000.00 USD | 923,330.00 USD | 3,210,000.00 USD | 1,930,000.00 USD |
| `1D` | `2116.80` | 570,900,000.00 USD | 0.00 USD | 570,900,000.00 USD | 3,030,000.00 USD | 1,240,000.00 USD | 676,500.00 USD |
| `7D` | `2117.90` | 563,860,000.00 USD | 0.00 USD | 563,860,000.00 USD | 8,390,000.00 USD | 578,010.00 USD | 2,580,000.00 USD |
| `1D` | `2119.20` | 565,950,000.00 USD | 0.00 USD | 565,950,000.00 USD | 3,990,000.00 USD | 3,020,000.00 USD | 916,350.00 USD |
| `7D` | `2120.70` | 552,310,000.00 USD | 0.00 USD | 552,310,000.00 USD | 7,060,000.00 USD | 5,780,000.00 USD | 1,820,000.00 USD |
| `1D` | `2121.60` | 558,030,000.00 USD | 0.00 USD | 558,030,000.00 USD | 5,220,000.00 USD | 3,820,000.00 USD | 1,400,000.00 USD |
| `7D` | `2123.50` | 537,660,000.00 USD | 0.00 USD | 537,660,000.00 USD | 7,150,000.00 USD | 7,720,000.00 USD | 1,410,000.00 USD |
| `1D` | `2124.00` | 547,580,000.00 USD | 0.00 USD | 547,580,000.00 USD | 6,610,000.00 USD | 1,490,000.00 USD | 2,330,000.00 USD |
| `7D` | `2126.30` | 521,380,000.00 USD | 0.00 USD | 521,380,000.00 USD | 2,740,000.00 USD | 4,400,000.00 USD | 4,790,000.00 USD |
| `1D` | `2126.40` | 537,150,000.00 USD | 0.00 USD | 537,150,000.00 USD | 3,480,000.00 USD | 2,810,000.00 USD | 306,170.00 USD |
| `1D` | `2128.80` | 530,560,000.00 USD | 0.00 USD | 530,560,000.00 USD | 3,180,000.00 USD | 1,860,000.00 USD | 1,510,000.00 USD |
| `7D` | `2129.10` | 509,450,000.00 USD | 0.00 USD | 509,450,000.00 USD | 4,770,000.00 USD | 1,270,000.00 USD | 1,100,000.00 USD |
| `1D` | `2131.20` | 524,000,000.00 USD | 0.00 USD | 524,000,000.00 USD | 363,860.00 USD | 274,200.00 USD | 344,350.00 USD |
| `7D` | `2131.90` | 502,300,000.00 USD | 0.00 USD | 502,300,000.00 USD | 2,170,000.00 USD | 1,620,000.00 USD | 1,360,000.00 USD |
| `1D` | `2133.60` | 523,020,000.00 USD | 0.00 USD | 523,020,000.00 USD | 792,080.00 USD | 690,590.00 USD | 1,540,000.00 USD |
| `7D` | `2134.70` | 497,150,000.00 USD | 0.00 USD | 497,150,000.00 USD | 1,630,000.00 USD | 790,240.00 USD | 898,290.00 USD |
| `1D` | `2136.00` | 520,000,000.00 USD | 0.00 USD | 520,000,000.00 USD | 2,320,000.00 USD | 2,790,000.00 USD | 3,090,000.00 USD |
| `7D` | `2137.50` | 493,840,000.00 USD | 0.00 USD | 493,840,000.00 USD | 2,120,000.00 USD | 2,390,000.00 USD | 1,530,000.00 USD |
| `1D` | `2138.40` | 511,800,000.00 USD | 0.00 USD | 511,800,000.00 USD | 783,250.00 USD | 1,210,000.00 USD | 70,140.00 USD |
| `7D` | `2140.30` | 487,800,000.00 USD | 0.00 USD | 487,800,000.00 USD | 3,990,000.00 USD | 1,870,000.00 USD | 801,910.00 USD |
| `1D` | `2140.80` | 509,730,000.00 USD | 0.00 USD | 509,730,000.00 USD | 1,530,000.00 USD | 1,450,000.00 USD | 317,350.00 USD |
| `7D` | `2143.10` | 481,150,000.00 USD | 0.00 USD | 481,150,000.00 USD | 2,380,000.00 USD | 618,280.00 USD | 268,500.00 USD |
| `1D` | `2143.20` | 506,430,000.00 USD | 0.00 USD | 506,430,000.00 USD | 1,080,000.00 USD | 2,830,000.00 USD | 1,160,000.00 USD |
| `1D` | `2145.60` | 501,360,000.00 USD | 0.00 USD | 501,360,000.00 USD | 3,170,000.00 USD | 2,360,000.00 USD | 615,080.00 USD |
| `7D` | `2145.90` | 477,880,000.00 USD | 0.00 USD | 477,880,000.00 USD | 978,940.00 USD | 1,450,000.00 USD | 1,720,000.00 USD |
| `1D` | `2148.00` | 495,210,000.00 USD | 0.00 USD | 495,210,000.00 USD | 728,710.00 USD | 1,810,000.00 USD | 69,300.00 USD |
| `7D` | `2148.70` | 473,730,000.00 USD | 0.00 USD | 473,730,000.00 USD | 26,270.00 USD | 538,910.00 USD | 399,680.00 USD |
| `1D` | `2150.40` | 492,610,000.00 USD | 0.00 USD | 492,610,000.00 USD | 7,580,000.00 USD | 2,090,000.00 USD | 2,660,000.00 USD |
| `7D` | `2151.50` | 472,760,000.00 USD | 0.00 USD | 472,760,000.00 USD | 11,200,000.00 USD | 363,770.00 USD | 107,200.00 USD |
| `1D` | `2152.80` | 480,280,000.00 USD | 0.00 USD | 480,280,000.00 USD | 2,710,000.00 USD | 2,710,000.00 USD | 2,240,000.00 USD |
| `7D` | `2154.30` | 461,090,000.00 USD | 0.00 USD | 461,090,000.00 USD | 48,150.00 USD | 2,020,000.00 USD | 1,580,000.00 USD |
| `1D` | `2155.20` | 472,620,000.00 USD | 0.00 USD | 472,620,000.00 USD | 2,740,000.00 USD | 3,890,000.00 USD | 2,380,000.00 USD |
| `7D` | `2157.10` | 457,450,000.00 USD | 0.00 USD | 457,450,000.00 USD | 4,270,000.00 USD | 1,330,000.00 USD | 5,050,000.00 USD |
| `1D` | `2157.60` | 463,610,000.00 USD | 0.00 USD | 463,610,000.00 USD | 3,400,000.00 USD | 1,460,000.00 USD | 3,680,000.00 USD |
| `7D` | `2159.90` | 446,790,000.00 USD | 0.00 USD | 446,790,000.00 USD | 2,980,000.00 USD | 737,260.00 USD | 1,830,000.00 USD |
| `1D` | `2160.00` | 455,070,000.00 USD | 0.00 USD | 455,070,000.00 USD | 4,390,000.00 USD | 6,230,000.00 USD | 2,930,000.00 USD |
| `1D` | `2162.40` | 441,530,000.00 USD | 0.00 USD | 441,530,000.00 USD | 15,640,000.00 USD | 9,100,000.00 USD | 783,060.00 USD |
| `7D` | `2162.70` | 441,230,000.00 USD | 0.00 USD | 441,230,000.00 USD | 17,980,000.00 USD | 1,990,000.00 USD | 0.00 USD |
| `1D` | `2164.80` | 416,000,000.00 USD | 0.00 USD | 416,000,000.00 USD | 13,250,000.00 USD | 10,700,000.00 USD | 3,720,000.00 USD |
| `7D` | `2165.50` | 421,260,000.00 USD | 0.00 USD | 421,260,000.00 USD | 8,990,000.00 USD | 17,170,000.00 USD | 2,950,000.00 USD |
| `1D` | `2167.20` | 388,340,000.00 USD | 0.00 USD | 388,340,000.00 USD | 13,150,000.00 USD | 4,920,000.00 USD | 6,680,000.00 USD |
| `7D` | `2168.30` | 392,150,000.00 USD | 0.00 USD | 392,150,000.00 USD | 12,770,000.00 USD | 16,150,000.00 USD | 3,760,000.00 USD |
| `1D` | `2169.60` | 363,590,000.00 USD | 0.00 USD | 363,590,000.00 USD | 13,360,000.00 USD | 7,640,000.00 USD | 5,110,000.00 USD |
| `7D` | `2171.10` | 359,460,000.00 USD | 0.00 USD | 359,460,000.00 USD | 1,860,000.00 USD | 6,380,000.00 USD | 5,570,000.00 USD |
| `1D` | `2172.00` | 337,480,000.00 USD | 0.00 USD | 337,480,000.00 USD | 21,250,000.00 USD | 9,060,000.00 USD | 5,250,000.00 USD |
| `7D` | `2173.90` | 345,660,000.00 USD | 0.00 USD | 345,660,000.00 USD | 35,100,000.00 USD | 0.00 USD | 1,010,000.00 USD |
| `1D` | `2174.40` | 301,920,000.00 USD | 0.00 USD | 301,920,000.00 USD | 5,740,000.00 USD | 1,040,000.00 USD | 2,310,000.00 USD |
| `7D` | `2176.70` | 309,550,000.00 USD | 0.00 USD | 309,550,000.00 USD | 0.00 USD | 1,460,000.00 USD | 2,820,000.00 USD |
| `1D` | `2176.80` | 292,830,000.00 USD | 0.00 USD | 292,830,000.00 USD | 893,730.00 USD | 569,650.00 USD | 2,400,000.00 USD |
| `1D` | `2179.20` | 288,970,000.00 USD | 0.00 USD | 288,970,000.00 USD | 3,870,000.00 USD | 2,680,000.00 USD | 3,350,000.00 USD |
| `7D` | `2179.50` | 305,270,000.00 USD | 0.00 USD | 305,270,000.00 USD | 2,400,000.00 USD | 133,210.00 USD | 4,150,000.00 USD |
| `1D` | `2181.60` | 279,060,000.00 USD | 0.00 USD | 279,060,000.00 USD | 3,170,000.00 USD | 4,920,000.00 USD | 8,190,000.00 USD |
| `7D` | `2182.30` | 298,590,000.00 USD | 0.00 USD | 298,590,000.00 USD | 1,760,000.00 USD | 2,160,000.00 USD | 2,650,000.00 USD |
| `1D` | `2184.00` | 262,780,000.00 USD | 0.00 USD | 262,780,000.00 USD | 4,300,000.00 USD | 1,150,000.00 USD | 894,870.00 USD |
| `7D` | `2185.10` | 292,010,000.00 USD | 0.00 USD | 292,010,000.00 USD | 41,350,000.00 USD | 20,450,000.00 USD | 1,290,000.00 USD |
| `1D` | `2186.40` | 256,440,000.00 USD | 0.00 USD | 256,440,000.00 USD | 4,150,000.00 USD | 2,750,000.00 USD | 4,960,000.00 USD |
| `7D` | `2187.90` | 228,920,000.00 USD | 0.00 USD | 228,920,000.00 USD | 2,370,000.00 USD | 0.00 USD | 1,600,000.00 USD |
| `1D` | `2188.80` | 244,570,000.00 USD | 0.00 USD | 244,570,000.00 USD | 4,520,000.00 USD | 5,130,000.00 USD | 9,340,000.00 USD |
| `7D` | `2190.70` | 224,950,000.00 USD | 0.00 USD | 224,950,000.00 USD | 12,430,000.00 USD | 27,960,000.00 USD | 6,420,000.00 USD |
| `1D` | `2191.20` | 225,570,000.00 USD | 0.00 USD | 225,570,000.00 USD | 6,810,000.00 USD | 4,780,000.00 USD | 3,570,000.00 USD |
| `7D` | `2193.50` | 178,130,000.00 USD | 0.00 USD | 178,130,000.00 USD | 0.00 USD | 7,340,000.00 USD | 8,120,000.00 USD |
| `1D` | `2193.60` | 210,420,000.00 USD | 0.00 USD | 210,420,000.00 USD | 5,190,000.00 USD | 4,640,000.00 USD | 1,350,000.00 USD |
| `1D` | `2196.00` | 199,240,000.00 USD | 0.00 USD | 199,240,000.00 USD | 8,930,000.00 USD | 1,310,000.00 USD | 5,520,000.00 USD |
| `7D` | `2196.30` | 162,680,000.00 USD | 0.00 USD | 162,680,000.00 USD | 383,690.00 USD | 243,760.00 USD | 109,160.00 USD |
| `1D` | `2198.40` | 183,470,000.00 USD | 0.00 USD | 183,470,000.00 USD | 271,140.00 USD | 3,690,000.00 USD | 4,160,000.00 USD |
| `7D` | `2199.10` | 161,940,000.00 USD | 0.00 USD | 161,940,000.00 USD | 0.00 USD | 1,460,000.00 USD | 7,440,000.00 USD |
| `1D` | `2200.80` | 175,360,000.00 USD | 0.00 USD | 175,360,000.00 USD | 12,080,000.00 USD | 6,470,000.00 USD | 11,980,000.00 USD |
| `7D` | `2201.90` | 153,040,000.00 USD | 0.00 USD | 153,040,000.00 USD | 9,110,000.00 USD | 266,430.00 USD | 18,630,000.00 USD |
| `1D` | `2203.20` | 144,820,000.00 USD | 0.00 USD | 144,820,000.00 USD | 12,320,000.00 USD | 14,270,000.00 USD | 16,350,000.00 USD |
| `7D` | `2204.70` | 125,030,000.00 USD | 0.00 USD | 125,030,000.00 USD | 5,350,000.00 USD | 4,330,000.00 USD | 4,430,000.00 USD |
| `1D` | `2205.60` | 101,890,000.00 USD | 0.00 USD | 101,890,000.00 USD | 14,550,000.00 USD | 1,530,000.00 USD | 2,370,000.00 USD |
| `7D` | `2207.50` | 110,920,000.00 USD | 0.00 USD | 110,920,000.00 USD | 19,630,000.00 USD | 3,390,000.00 USD | 3,660,000.00 USD |
| `1D` | `2208.00` | 83,430,000.00 USD | 0.00 USD | 83,430,000.00 USD | 8,730,000.00 USD | 6,940,000.00 USD | 3,250,000.00 USD |
| `7D` | `2210.30` | 84,260,000.00 USD | 0.00 USD | 84,260,000.00 USD | 4,740,000.00 USD | 0.00 USD | 11,300,000.00 USD |
| `1D` | `2210.40` | 64,510,000.00 USD | 0.00 USD | 64,510,000.00 USD | 6,870,000.00 USD | 7,030,000.00 USD | 5,090,000.00 USD |
| `1D` | `2212.80` | 45,510,000.00 USD | 0.00 USD | 45,510,000.00 USD | 8,240,000.00 USD | 5,160,000.00 USD | 1,990,000.00 USD |
| `7D` | `2213.10` | 68,220,000.00 USD | 0.00 USD | 68,220,000.00 USD | 1,710,000.00 USD | 1,980,000.00 USD | 8,850,000.00 USD |
| `1D` | `2215.20` | 30,130,000.00 USD | 0.00 USD | 30,130,000.00 USD | 2,150,000.00 USD | 3,720,000.00 USD | 100,120.00 USD |
| `7D` | `2215.90` | 55,670,000.00 USD | 0.00 USD | 55,670,000.00 USD | 0.00 USD | 0.00 USD | 565,690.00 USD |
| `1D` | `2217.60` | 24,150,000.00 USD | 0.00 USD | 24,150,000.00 USD | 1,010,000.00 USD | 2,470,000.00 USD | 3,960,000.00 USD |
| `7D` | `2218.70` | 55,110,000.00 USD | 0.00 USD | 55,110,000.00 USD | 22,400,000.00 USD | 487,520.00 USD | 218,310.00 USD |
| `1D` | `2220.00` | 16,710,000.00 USD | 0.00 USD | 16,710,000.00 USD | 6,080,000.00 USD | 2,000,000.00 USD | 3,460,000.00 USD |
| `7D` | `2221.50` | 32,010,000.00 USD | 0.00 USD | 32,010,000.00 USD | 0.00 USD | 12,220,000.00 USD | 18,870,000.00 USD |
| `1D` | `2222.40` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 0.00 USD | 4,290,000.00 USD | 883,270.00 USD |
| `7D` | `2224.30` | 911,920.00 USD | 0.00 USD | 911,920.00 USD | 0.00 USD | 0.00 USD | 911,920.00 USD |
| `7D` | `2224.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2224.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2224.80` | 468,930.00 USD | 468,930.00 USD | 0.00 USD | 374,450.00 USD | 94,480.00 USD | 0.00 USD |
| `7D` | `2227.10` | 8,020,000.00 USD | 8,020,000.00 USD | 0.00 USD | 557,870.00 USD | 0.00 USD | 7,460,000.00 USD |
| `1D` | `2227.20` | 5,800,000.00 USD | 5,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,330,000.00 USD |
| `1D` | `2229.60` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 4,040,000.00 USD | 0.00 USD | 113,200.00 USD |
| `7D` | `2229.90` | 29,000,000.00 USD | 29,000,000.00 USD | 0.00 USD | 1,910,000.00 USD | 0.00 USD | 19,080,000.00 USD |
| `1D` | `2232.00` | 46,740,000.00 USD | 46,740,000.00 USD | 0.00 USD | 36,380,000.00 USD | 0.00 USD | 411,180.00 USD |
| `7D` | `2232.70` | 29,960,000.00 USD | 29,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 959,630.00 USD |
| `7D` | `2235.50` | 55,210,000.00 USD | 55,210,000.00 USD | 0.00 USD | 3,260,000.00 USD | 21,640,000.00 USD | 350,840.00 USD |
| `1D` | `2236.80` | 53,540,000.00 USD | 53,540,000.00 USD | 0.00 USD | 6,800,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2238.30` | 69,250,000.00 USD | 69,250,000.00 USD | 0.00 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2239.20` | 61,960,000.00 USD | 61,960,000.00 USD | 0.00 USD | 8,420,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2241.10` | 101,150,000.00 USD | 101,150,000.00 USD | 0.00 USD | 31,910,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2241.60` | 62,090,000.00 USD | 62,090,000.00 USD | 0.00 USD | 81,700.00 USD | 0.00 USD | 50,930.00 USD |
| `7D` | `2243.90` | 103,010,000.00 USD | 103,010,000.00 USD | 0.00 USD | 1,590,000.00 USD | 268,650.00 USD | 0.00 USD |
| `1D` | `2244.00` | 64,070,000.00 USD | 64,070,000.00 USD | 0.00 USD | 381,040.00 USD | 569,860.00 USD | 1,030,000.00 USD |
| `1D` | `2246.40` | 84,970,000.00 USD | 84,970,000.00 USD | 0.00 USD | 10,100,000.00 USD | 5,170,000.00 USD | 5,630,000.00 USD |
| `7D` | `2246.70` | 120,040,000.00 USD | 120,040,000.00 USD | 0.00 USD | 6,720,000.00 USD | 1,300,000.00 USD | 9,020,000.00 USD |
| `1D` | `2248.80` | 102,270,000.00 USD | 102,270,000.00 USD | 0.00 USD | 3,390,000.00 USD | 7,130,000.00 USD | 6,780,000.00 USD |
| `7D` | `2249.50` | 130,630,000.00 USD | 130,630,000.00 USD | 0.00 USD | 2,960,000.00 USD | 6,990,000.00 USD | 640,060.00 USD |
| `1D` | `2251.20` | 111,900,000.00 USD | 111,900,000.00 USD | 0.00 USD | 8,050,000.00 USD | 1,470,000.00 USD | 112,380.00 USD |
| `7D` | `2252.30` | 152,350,000.00 USD | 152,350,000.00 USD | 0.00 USD | 10,050,000.00 USD | 11,670,000.00 USD | 0.00 USD |
| `1D` | `2253.60` | 120,690,000.00 USD | 120,690,000.00 USD | 0.00 USD | 893,130.00 USD | 4,250,000.00 USD | 3,650,000.00 USD |
| `7D` | `2255.10` | 169,510,000.00 USD | 169,510,000.00 USD | 0.00 USD | 10,050,000.00 USD | 6,600,000.00 USD | 514,610.00 USD |
| `1D` | `2256.00` | 161,360,000.00 USD | 161,360,000.00 USD | 0.00 USD | 24,390,000.00 USD | 8,790,000.00 USD | 7,480,000.00 USD |
| `7D` | `2257.90` | 209,210,000.00 USD | 209,210,000.00 USD | 0.00 USD | 20,510,000.00 USD | 12,290,000.00 USD | 6,890,000.00 USD |
| `1D` | `2258.40` | 179,910,000.00 USD | 179,910,000.00 USD | 0.00 USD | 10,470,000.00 USD | 6,170,000.00 USD | 1,910,000.00 USD |
| `7D` | `2260.70` | 213,530,000.00 USD | 213,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,320,000.00 USD |
| `1D` | `2260.80` | 200,880,000.00 USD | 200,880,000.00 USD | 0.00 USD | 9,590,000.00 USD | 8,980,000.00 USD | 2,410,000.00 USD |
| `1D` | `2263.20` | 233,160,000.00 USD | 233,160,000.00 USD | 0.00 USD | 14,560,000.00 USD | 9,680,000.00 USD | 8,040,000.00 USD |
| `7D` | `2263.50` | 221,920,000.00 USD | 221,920,000.00 USD | 0.00 USD | 6,720,000.00 USD | 1,460,000.00 USD | 218,310.00 USD |
| `1D` | `2265.60` | 255,320,000.00 USD | 255,320,000.00 USD | 0.00 USD | 3,050,000.00 USD | 8,620,000.00 USD | 10,490,000.00 USD |
| `7D` | `2266.30` | 236,420,000.00 USD | 236,420,000.00 USD | 0.00 USD | 0.00 USD | 8,160,000.00 USD | 6,330,000.00 USD |
| `1D` | `2268.00` | 302,170,000.00 USD | 302,170,000.00 USD | 0.00 USD | 19,350,000.00 USD | 12,270,000.00 USD | 15,230,000.00 USD |
| `7D` | `2269.10` | 265,720,000.00 USD | 265,720,000.00 USD | 0.00 USD | 11,010,000.00 USD | 133,210.00 USD | 18,160,000.00 USD |
| `1D` | `2270.40` | 337,640,000.00 USD | 337,640,000.00 USD | 0.00 USD | 11,440,000.00 USD | 9,960,000.00 USD | 14,070,000.00 USD |
| `7D` | `2271.90` | 294,510,000.00 USD | 294,510,000.00 USD | 0.00 USD | 18,240,000.00 USD | 3,640,000.00 USD | 6,900,000.00 USD |
| `1D` | `2272.80` | 364,190,000.00 USD | 364,190,000.00 USD | 0.00 USD | 16,290,000.00 USD | 4,780,000.00 USD | 5,480,000.00 USD |
| `7D` | `2274.70` | 321,040,000.00 USD | 321,040,000.00 USD | 0.00 USD | 19,630,000.00 USD | 6,900,000.00 USD | 0.00 USD |
| `1D` | `2275.20` | 409,430,000.00 USD | 409,430,000.00 USD | 0.00 USD | 26,530,000.00 USD | 15,130,000.00 USD | 3,580,000.00 USD |
| `7D` | `2277.50` | 347,290,000.00 USD | 347,290,000.00 USD | 0.00 USD | 6,890,000.00 USD | 8,890,000.00 USD | 10,480,000.00 USD |
| `1D` | `2277.60` | 445,250,000.00 USD | 445,250,000.00 USD | 0.00 USD | 10,430,000.00 USD | 13,450,000.00 USD | 11,930,000.00 USD |
| `1D` | `2280.00` | 494,390,000.00 USD | 494,390,000.00 USD | 0.00 USD | 27,480,000.00 USD | 9,610,000.00 USD | 12,040,000.00 USD |
| `7D` | `2280.30` | 391,610,000.00 USD | 391,610,000.00 USD | 0.00 USD | 854,200.00 USD | 39,830,000.00 USD | 3,640,000.00 USD |
| `1D` | `2282.40` | 552,950,000.00 USD | 552,950,000.00 USD | 0.00 USD | 26,180,000.00 USD | 25,320,000.00 USD | 7,060,000.00 USD |
| `7D` | `2283.10` | 483,430,000.00 USD | 483,430,000.00 USD | 0.00 USD | 5,600,000.00 USD | 72,520,000.00 USD | 13,690,000.00 USD |
| `1D` | `2284.80` | 577,210,000.00 USD | 577,210,000.00 USD | 0.00 USD | 9,270,000.00 USD | 7,750,000.00 USD | 7,240,000.00 USD |
| `7D` | `2285.90` | 487,130,000.00 USD | 487,130,000.00 USD | 0.00 USD | 1,010,000.00 USD | 2,590,000.00 USD | 109,160.00 USD |
| `1D` | `2287.20` | 609,210,000.00 USD | 609,210,000.00 USD | 0.00 USD | 13,140,000.00 USD | 10,580,000.00 USD | 8,290,000.00 USD |
| `7D` | `2288.70` | 519,770,000.00 USD | 519,770,000.00 USD | 0.00 USD | 8,380,000.00 USD | 9,320,000.00 USD | 14,930,000.00 USD |
| `1D` | `2289.60` | 631,990,000.00 USD | 631,990,000.00 USD | 0.00 USD | 5,630,000.00 USD | 13,110,000.00 USD | 4,040,000.00 USD |
| `7D` | `2291.50` | 531,640,000.00 USD | 531,640,000.00 USD | 0.00 USD | 4,310,000.00 USD | 517,070.00 USD | 7,060,000.00 USD |
| `1D` | `2292.00` | 664,760,000.00 USD | 664,760,000.00 USD | 0.00 USD | 18,640,000.00 USD | 5,470,000.00 USD | 8,670,000.00 USD |
| `7D` | `2294.30` | 552,980,000.00 USD | 552,980,000.00 USD | 0.00 USD | 14,670,000.00 USD | 1,490,000.00 USD | 5,180,000.00 USD |
| `1D` | `2294.40` | 697,400,000.00 USD | 697,400,000.00 USD | 0.00 USD | 16,220,000.00 USD | 6,680,000.00 USD | 9,750,000.00 USD |
| `1D` | `2296.80` | 738,930,000.00 USD | 738,930,000.00 USD | 0.00 USD | 21,130,000.00 USD | 13,050,000.00 USD | 7,350,000.00 USD |
| `7D` | `2297.10` | 602,730,000.00 USD | 602,730,000.00 USD | 0.00 USD | 25,900,000.00 USD | 8,070,000.00 USD | 15,780,000.00 USD |
| `1D` | `2299.20` | 788,390,000.00 USD | 788,390,000.00 USD | 0.00 USD | 19,620,000.00 USD | 16,130,000.00 USD | 13,710,000.00 USD |
| `7D` | `2299.90` | 645,650,000.00 USD | 645,650,000.00 USD | 0.00 USD | 16,200,000.00 USD | 20,940,000.00 USD | 5,780,000.00 USD |
| `1D` | `2301.60` | 815,450,000.00 USD | 815,450,000.00 USD | 0.00 USD | 13,720,000.00 USD | 6,010,000.00 USD | 7,330,000.00 USD |
| `7D` | `2302.70` | 700,310,000.00 USD | 700,310,000.00 USD | 0.00 USD | 26,960,000.00 USD | 10,860,000.00 USD | 16,850,000.00 USD |
| `1D` | `2304.00` | 842,290,000.00 USD | 842,290,000.00 USD | 0.00 USD | 12,680,000.00 USD | 11,040,000.00 USD | 3,130,000.00 USD |
| `7D` | `2305.50` | 726,330,000.00 USD | 726,330,000.00 USD | 0.00 USD | 6,340,000.00 USD | 8,820,000.00 USD | 10,860,000.00 USD |
| `1D` | `2306.40` | 876,630,000.00 USD | 876,630,000.00 USD | 0.00 USD | 13,770,000.00 USD | 11,600,000.00 USD | 8,970,000.00 USD |
| `7D` | `2308.30` | 728,630,000.00 USD | 728,630,000.00 USD | 0.00 USD | 1,240,000.00 USD | 930,630.00 USD | 134,160.00 USD |
| `1D` | `2308.80` | 882,150,000.00 USD | 882,150,000.00 USD | 0.00 USD | 67,780.00 USD | 3,530,000.00 USD | 1,920,000.00 USD |
| `7D` | `2311.10` | 759,130,000.00 USD | 759,130,000.00 USD | 0.00 USD | 11,560,000.00 USD | 2,790,000.00 USD | 16,150,000.00 USD |
| `1D` | `2311.20` | 898,140,000.00 USD | 898,140,000.00 USD | 0.00 USD | 6,180,000.00 USD | 664,440.00 USD | 9,150,000.00 USD |
| `1D` | `2313.60` | 918,050,000.00 USD | 918,050,000.00 USD | 0.00 USD | 7,180,000.00 USD | 9,020,000.00 USD | 3,720,000.00 USD |
| `7D` | `2313.90` | 769,950,000.00 USD | 769,950,000.00 USD | 0.00 USD | 1,100,000.00 USD | 7,460,000.00 USD | 2,260,000.00 USD |
| `1D` | `2316.00` | 951,730,000.00 USD | 951,730,000.00 USD | 0.00 USD | 10,470,000.00 USD | 16,140,000.00 USD | 7,060,000.00 USD |
| `7D` | `2316.70` | 775,650,000.00 USD | 775,650,000.00 USD | 0.00 USD | 1,020,000.00 USD | 3,640,000.00 USD | 1,040,000.00 USD |
| `1D` | `2318.40` | 967,080,000.00 USD | 967,080,000.00 USD | 0.00 USD | 6,250,000.00 USD | 6,890,000.00 USD | 2,210,000.00 USD |
| `7D` | `2319.50` | 804,920,000.00 USD | 804,920,000.00 USD | 0.00 USD | 5,530,000.00 USD | 15,850,000.00 USD | 7,890,000.00 USD |
| `1D` | `2320.80` | 987,270,000.00 USD | 987,270,000.00 USD | 0.00 USD | 5,860,000.00 USD | 11,510,000.00 USD | 2,810,000.00 USD |
| `7D` | `2322.30` | 810,780,000.00 USD | 810,780,000.00 USD | 0.00 USD | 2,300,000.00 USD | 3,450,000.00 USD | 108,040.00 USD |
| `1D` | `2323.20` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 0.00 USD | 4,360,000.00 USD | 12,070,000.00 USD | 4,670,000.00 USD |
| `7D` | `2325.10` | 833,810,000.00 USD | 833,810,000.00 USD | 0.00 USD | 10,150,000.00 USD | 2,770,000.00 USD | 10,120,000.00 USD |
| `1D` | `2325.60` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 0.00 USD | 2,050,000.00 USD | 6,780,000.00 USD | 1,530,000.00 USD |
| `7D` | `2327.90` | 845,700,000.00 USD | 845,700,000.00 USD | 0.00 USD | 3,860,000.00 USD | 0.00 USD | 8,030,000.00 USD |
| `1D` | `2328.00` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 0.00 USD | 494,310.00 USD | 1,240,000.00 USD | 4,510,000.00 USD |
| `1D` | `2330.40` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 0.00 USD | 12,440,000.00 USD | 3,110,000.00 USD | 1,710,000.00 USD |
| `7D` | `2330.70` | 861,920,000.00 USD | 861,920,000.00 USD | 0.00 USD | 15,800,000.00 USD | 363,770.00 USD | 54,580.00 USD |
| `1D` | `2332.80` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 2,710,000.00 USD | 3,280,000.00 USD | 9,260,000.00 USD |
| `7D` | `2333.50` | 903,010,000.00 USD | 903,010,000.00 USD | 0.00 USD | 20,270,000.00 USD | 12,860,000.00 USD | 7,960,000.00 USD |
| `1D` | `2335.20` | 1,080,000,000.00 USD | 1,080,000,000.00 USD | 0.00 USD | 12,310,000.00 USD | 3,870,000.00 USD | 2,730,000.00 USD |
| `7D` | `2336.30` | 940,270,000.00 USD | 940,270,000.00 USD | 0.00 USD | 24,310,000.00 USD | 7,570,000.00 USD | 5,390,000.00 USD |
| `1D` | `2337.60` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 7,940,000.00 USD | 1,180,000.00 USD | 5,130,000.00 USD |
| `7D` | `2339.10` | 966,680,000.00 USD | 966,680,000.00 USD | 0.00 USD | 14,040,000.00 USD | 0.00 USD | 12,370,000.00 USD |
| `1D` | `2340.00` | 1,120,000,000.00 USD | 1,120,000,000.00 USD | 0.00 USD | 10,960,000.00 USD | 6,260,000.00 USD | 12,150,000.00 USD |
| `7D` | `2341.90` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 0.00 USD | 8,610,000.00 USD | 17,820,000.00 USD | 14,000,000.00 USD |
| `1D` | `2342.40` | 1,130,000,000.00 USD | 1,130,000,000.00 USD | 0.00 USD | 8,100,000.00 USD | 3,720,000.00 USD | 2,140,000.00 USD |
| `7D` | `2344.70` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 0.00 USD | 2,480,000.00 USD | 16,920,000.00 USD | 8,520,000.00 USD |
| `1D` | `2344.80` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 3,570,000.00 USD | 8,550,000.00 USD | 6,450,000.00 USD |
| `1D` | `2347.20` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 4,320,000.00 USD | 3,860,000.00 USD | 4,750,000.00 USD |
| `7D` | `2347.50` | 1,060,000,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 0.00 USD | 8,220,000.00 USD | 18,860,000.00 USD |
| `1D` | `2349.60` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 17,010,000.00 USD | 6,360,000.00 USD | 6,030,000.00 USD |
| `7D` | `2350.30` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 1,630,000.00 USD | 20,110,000.00 USD | 15,150,000.00 USD |
| `1D` | `2352.00` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 15,870,000.00 USD | 1,960,000.00 USD | 6,690,000.00 USD |
| `7D` | `2353.10` | 1,140,000,000.00 USD | 1,140,000,000.00 USD | 0.00 USD | 2,710,000.00 USD | 35,770,000.00 USD | 4,640,000.00 USD |
| `1D` | `2354.40` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 1,340,000.00 USD | 5,600,000.00 USD | 955,020.00 USD |
| `7D` | `2355.90` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 18,560,000.00 USD | 10,720,000.00 USD | 3,950,000.00 USD |
| `1D` | `2356.80` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 4,660,000.00 USD | 1,670,000.00 USD | 1,180,000.00 USD |
| `7D` | `2358.70` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 6,870,000.00 USD | 512,220.00 USD | 3,190,000.00 USD |
| `1D` | `2359.20` | 1,250,000,000.00 USD | 1,250,000,000.00 USD | 0.00 USD | 6,320,000.00 USD | 5,050,000.00 USD | 7,330,000.00 USD |
| `7D` | `2361.50` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 3,150,000.00 USD | 3,430,000.00 USD | 374,770.00 USD |
| `1D` | `2361.60` | 1,270,000,000.00 USD | 1,270,000,000.00 USD | 0.00 USD | 7,760,000.00 USD | 8,680,000.00 USD | 1,350,000.00 USD |
| `1D` | `2364.00` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 0.00 USD | 5,570,000.00 USD | 3,140,000.00 USD | 9,740,000.00 USD |
| `7D` | `2364.30` | 1,210,000,000.00 USD | 1,210,000,000.00 USD | 0.00 USD | 3,860,000.00 USD | 373,740.00 USD | 10,920,000.00 USD |
| `1D` | `2366.40` | 1,290,000,000.00 USD | 1,290,000,000.00 USD | 0.00 USD | 3,150,000.00 USD | 509,320.00 USD | 1,000,000.00 USD |
| `7D` | `2367.10` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 6,340,000.00 USD | 1,310,000.00 USD | 307,410.00 USD |
| `1D` | `2368.80` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 0.00 USD | 6,840,000.00 USD | 4,420,000.00 USD | 3,380,000.00 USD |
| `7D` | `2369.90` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 0.00 USD | 24,940,000.00 USD | 475,460.00 USD | 18,790,000.00 USD |
| `1D` | `2371.20` | 1,330,000,000.00 USD | 1,330,000,000.00 USD | 0.00 USD | 13,620,000.00 USD | 6,300,000.00 USD | 4,790,000.00 USD |
| `7D` | `2372.70` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 0.00 USD | 15,600,000.00 USD | 0.00 USD | 39,640,000.00 USD |
| `1D` | `2373.60` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 12,630,000.00 USD | 1,100,000.00 USD | 5,900,000.00 USD |
| `7D` | `2375.50` | 1,340,000,000.00 USD | 1,340,000,000.00 USD | 0.00 USD | 9,700,000.00 USD | 1,050,000.00 USD | 11,870,000.00 USD |
| `1D` | `2376.00` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 5,100,000.00 USD | 2,750,000.00 USD | 4,130,000.00 USD |
| `7D` | `2378.30` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 0.00 USD | 11,180,000.00 USD | 7,020,000.00 USD | 23,870,000.00 USD |
| `1D` | `2378.40` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 1,650,000.00 USD | 1,010,000.00 USD | 3,240,000.00 USD |
| `1D` | `2380.80` | 1,390,000,000.00 USD | 1,390,000,000.00 USD | 0.00 USD | 6,120,000.00 USD | 6,700,000.00 USD | 5,230,000.00 USD |
| `7D` | `2381.10` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 4,540,000.00 USD | 2,390,000.00 USD | 16,460,000.00 USD |
| `1D` | `2383.20` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 16,070,000.00 USD | 9,480,000.00 USD | 10,570,000.00 USD |
| `7D` | `2383.90` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 0.00 USD | 8,840,000.00 USD | 21,750,000.00 USD | 30,520,000.00 USD |
| `1D` | `2385.60` | 1,450,000,000.00 USD | 1,450,000,000.00 USD | 0.00 USD | 7,170,000.00 USD | 10,450,000.00 USD | 3,690,000.00 USD |
| `7D` | `2386.70` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 0.00 USD | 17,720,000.00 USD | 32,140,000.00 USD | 42,040,000.00 USD |
| `1D` | `2388.00` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 0.00 USD | 10,740,000.00 USD | 5,690,000.00 USD | 2,720,000.00 USD |
| `7D` | `2389.50` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 0.00 USD | 5,670,000.00 USD | 35,860,000.00 USD | 28,760,000.00 USD |
| `1D` | `2390.40` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 0.00 USD | 3,450,000.00 USD | 3,360,000.00 USD | 1,520,000.00 USD |
| `7D` | `2392.30` | 1,740,000,000.00 USD | 1,740,000,000.00 USD | 0.00 USD | 26,840,000.00 USD | 45,530,000.00 USD | 39,160,000.00 USD |
| `1D` | `2392.80` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 0.00 USD | 2,700,000.00 USD | 3,990,000.00 USD | 3,320,000.00 USD |
| `7D` | `2395.10` | 1,830,000,000.00 USD | 1,830,000,000.00 USD | 0.00 USD | 39,180,000.00 USD | 24,870,000.00 USD | 29,410,000.00 USD |
| `1D` | `2395.20` | 1,490,000,000.00 USD | 1,490,000,000.00 USD | 0.00 USD | 2,060,000.00 USD | 1,450,000.00 USD | 2,190,000.00 USD |
| `1D` | `2397.60` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 0.00 USD | 64,150.00 USD | 3,720,000.00 USD | 3,380,000.00 USD |
| `7D` | `2397.90` | 1,930,000,000.00 USD | 1,930,000,000.00 USD | 0.00 USD | 34,290,000.00 USD | 36,430,000.00 USD | 23,570,000.00 USD |
| `1D` | `2400.00` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 0.00 USD | 2,150,000.00 USD | 637,690.00 USD | 1,390,000.00 USD |
| `7D` | `2400.70` | 2,020,000,000.00 USD | 2,020,000,000.00 USD | 0.00 USD | 42,030,000.00 USD | 25,390,000.00 USD | 24,070,000.00 USD |
| `1D` | `2402.40` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 0.00 USD | 1,140,000.00 USD | 315,710.00 USD | 552,090.00 USD |
| `7D` | `2403.50` | 2,120,000,000.00 USD | 2,120,000,000.00 USD | 0.00 USD | 51,300,000.00 USD | 24,760,000.00 USD | 30,980,000.00 USD |
| `1D` | `2404.80` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 0.00 USD | 5,960,000.00 USD | 3,440,000.00 USD | 4,950,000.00 USD |
| `7D` | `2406.30` | 2,200,000,000.00 USD | 2,200,000,000.00 USD | 0.00 USD | 29,700,000.00 USD | 33,710,000.00 USD | 14,210,000.00 USD |
| `1D` | `2407.20` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 0.00 USD | 6,810,000.00 USD | 3,470,000.00 USD | 1,900,000.00 USD |
| `7D` | `2409.10` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 0.00 USD | 25,090,000.00 USD | 21,480,000.00 USD | 27,910,000.00 USD |
| `1D` | `2409.60` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 0.00 USD | 4,520,000.00 USD | 3,640,000.00 USD | 3,080,000.00 USD |
| `7D` | `2411.90` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 0.00 USD | 15,970,000.00 USD | 21,640,000.00 USD | 13,990,000.00 USD |
| `1D` | `2412.00` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 0.00 USD | 5,230,000.00 USD | 3,230,000.00 USD | 1,960,000.00 USD |
| `1D` | `2414.40` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 0.00 USD | 1,120,000.00 USD | 1,600,000.00 USD | 1,800,000.00 USD |
| `7D` | `2414.70` | 2,390,000,000.00 USD | 2,390,000,000.00 USD | 0.00 USD | 22,250,000.00 USD | 19,630,000.00 USD | 21,720,000.00 USD |
| `1D` | `2416.80` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 0.00 USD | 2,870,000.00 USD | 1,460,000.00 USD | 1,540,000.00 USD |
| `7D` | `2417.50` | 2,440,000,000.00 USD | 2,440,000,000.00 USD | 0.00 USD | 22,310,000.00 USD | 8,700,000.00 USD | 21,160,000.00 USD |
| `1D` | `2419.20` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 4,780,000.00 USD | 2,560,000.00 USD | 2,350,000.00 USD |
| `7D` | `2420.30` | 2,500,000,000.00 USD | 2,500,000,000.00 USD | 0.00 USD | 29,980,000.00 USD | 18,780,000.00 USD | 9,160,000.00 USD |
| `1D` | `2421.60` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 4,170,000.00 USD | 3,820,000.00 USD | 4,890,000.00 USD |
| `7D` | `2423.10` | 2,550,000,000.00 USD | 2,550,000,000.00 USD | 0.00 USD | 17,920,000.00 USD | 17,260,000.00 USD | 17,780,000.00 USD |
| `1D` | `2424.00` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 220,740.00 USD | 1,180,000.00 USD | 1,300,000.00 USD |
| `7D` | `2425.90` | 2,600,000,000.00 USD | 2,600,000,000.00 USD | 0.00 USD | 12,980,000.00 USD | 15,310,000.00 USD | 17,380,000.00 USD |
| `1D` | `2426.40` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 2,090,000.00 USD | 1,100,000.00 USD | 40,970.00 USD |
| `7D` | `2428.70` | 2,630,000,000.00 USD | 2,630,000,000.00 USD | 0.00 USD | 12,800,000.00 USD | 7,090,000.00 USD | 8,840,000.00 USD |
| `1D` | `2428.80` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 670,680.00 USD | 918,390.00 USD | 1,480,000.00 USD |
| `1D` | `2431.20` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 3,120,000.00 USD | 2,330,000.00 USD | 664,400.00 USD |
| `7D` | `2431.50` | 2,660,000,000.00 USD | 2,660,000,000.00 USD | 0.00 USD | 9,420,000.00 USD | 12,660,000.00 USD | 8,750,000.00 USD |
| `1D` | `2433.60` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 1,770,000.00 USD | 1,450,000.00 USD | 1,680,000.00 USD |
| `7D` | `2434.30` | 2,680,000,000.00 USD | 2,680,000,000.00 USD | 0.00 USD | 13,090,000.00 USD | 3,830,000.00 USD | 3,220,000.00 USD |
| `1D` | `2436.00` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 2,490,000.00 USD | 1,070,000.00 USD | 161,010.00 USD |
| `7D` | `2437.10` | 2,700,000,000.00 USD | 2,700,000,000.00 USD | 0.00 USD | 7,130,000.00 USD | 7,440,000.00 USD | 6,120,000.00 USD |
| `1D` | `2438.40` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 476,020.00 USD | 535,870.00 USD | 15,480.00 USD |
| `7D` | `2439.90` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 0.00 USD | 12,730,000.00 USD | 4,970,000.00 USD | 3,700,000.00 USD |
| `1D` | `2440.80` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 2,260,000.00 USD | 723,100.00 USD | 858,540.00 USD |
| `7D` | `2442.70` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 0.00 USD | 5,050,000.00 USD | 5,320,000.00 USD | 7,900,000.00 USD |
| `1D` | `2443.20` | 1,610,000,000.00 USD | 1,610,000,000.00 USD | 0.00 USD | 27,360.00 USD | 455,640.00 USD | 747,370.00 USD |
| `7D` | `2445.50` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 9,990,000.00 USD | 7,470,000.00 USD | 10,400,000.00 USD |
| `1D` | `2445.60` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 438,650.00 USD | 291,150.00 USD | 908,510.00 USD |
| `1D` | `2448.00` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 975,830.00 USD | 989,540.00 USD | 1,700,000.00 USD |
| `7D` | `2448.30` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 0.00 USD | 10,750,000.00 USD | 3,770,000.00 USD | 13,270,000.00 USD |
| `1D` | `2450.40` | 1,620,000,000.00 USD | 1,620,000,000.00 USD | 0.00 USD | 1,980,000.00 USD | 69,580.00 USD | 26,770.00 USD |
| `7D` | `2451.10` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 8,450,000.00 USD | 7,240,000.00 USD | 7,080,000.00 USD |
| `1D` | `2452.80` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 0.00 USD | 2,460,000.00 USD | 1,840,000.00 USD | 2,370,000.00 USD |
| `7D` | `2453.90` | 2,830,000,000.00 USD | 2,830,000,000.00 USD | 0.00 USD | 4,220,000.00 USD | 2,980,000.00 USD | 3,870,000.00 USD |
| `1D` | `2455.20` | 1,630,000,000.00 USD | 1,630,000,000.00 USD | 0.00 USD | 1,640,000.00 USD | 1,990,000.00 USD | 905,110.00 USD |
| `7D` | `2456.70` | 2,850,000,000.00 USD | 2,850,000,000.00 USD | 0.00 USD | 8,340,000.00 USD | 7,380,000.00 USD | 7,500,000.00 USD |
| `1D` | `2457.60` | 1,640,000,000.00 USD | 1,640,000,000.00 USD | 0.00 USD | 1,700,000.00 USD | 1,840,000.00 USD | 841,740.00 USD |
| `1D` | `2459.50` | 1,640,000,000.00 USD | 1,640,000,000.00 USD | 0.00 USD | 1,200,000.00 USD | 1,300,000.00 USD | 366,800.00 USD |
| `7D` | `2459.50` | 2,870,000,000.00 USD | 2,870,000,000.00 USD | 0.00 USD | 3,220,000.00 USD | 4,870,000.00 USD | 6,000,000.00 USD |
| `7D` | `2462.30` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 0.00 USD | 6,600,000.00 USD | 5,990,000.00 USD | 5,150,000.00 USD |
| `7D` | `2465.10` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 0.00 USD | 4,900,000.00 USD | 3,130,000.00 USD | 2,820,000.00 USD |
| `7D` | `2467.90` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 0.00 USD | 2,900,000.00 USD | 1,870,000.00 USD | 23,760.00 USD |
| `7D` | `2470.70` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 0.00 USD | 3,960,000.00 USD | 2,050,000.00 USD | 522,210.00 USD |
| `7D` | `2473.50` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 0.00 USD | 5,300,000.00 USD | 2,920,000.00 USD | 3,180,000.00 USD |
| `7D` | `2476.30` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 0.00 USD | 2,070,000.00 USD | 1,710,000.00 USD | 872,130.00 USD |
| `7D` | `2479.10` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 0.00 USD | 3,070,000.00 USD | 4,130,000.00 USD | 540,990.00 USD |
| `7D` | `2481.90` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 601,420.00 USD | 3,680,000.00 USD | 1,050,000.00 USD |
| `7D` | `2484.70` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD |
| `7D` | `2487.50` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 275,450.00 USD | 211,130.00 USD | 0.00 USD |
| `7D` | `2490.30` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 338,890.00 USD | 286,610.00 USD | 0.00 USD |
| `7D` | `2491.80` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 2,580,000.00 USD | 733,870.00 USD | 445,140.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `28.43B` | Total OI Tokens: `12,786,569.5 ETH`
  * 1h OI Change: `+0.20%` | 4h OI Change: `-1.78%` | 24h OI Change: `-5.93%`
  * Exchange Breakdown: Binance=`8.39B` | Bybit=`2.09B` | OKX=`1.75B` | Hyperliquid=`2.34B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-132.70K` | Last 24h: `195.10K` | Last 3d: `5.21M` | Last 7d: `11.81M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0030%` | **USDT OKX** | `-0.0015%` |
| **USDT Bybit** | `-0.0014%` | **USDT KuCoin** | `-0.0032%` |
| **USDT MEXC** | `-0.0030%` | **USDT BingX** | `0.0022%` |
| **USDT Gate** | `0.0065%` | **USDT Bitget** | `0.0024%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0016%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `41.46%` | `58.54%` | `0.71` | 712,370,000.00 USD |
| `15M` | `Binance` | `35.94%` | `64.06%` | `0.56` | 234,970,000.00 USD |
| `15M` | `OKX` | `51.79%` | `48.21%` | `1.07` | 105,300,000.00 USD |
| `15M` | `Bybit` | `32.46%` | `67.54%` | `0.48` | 70,110,000.00 USD |
| `15M` | `KuCoin` | `44.36%` | `55.64%` | `0.80` | 1,900,000.00 USD |
| `15M` | `Gate` | `47.66%` | `52.34%` | `0.91` | 74,060,000.00 USD |
| `15M` | `Bitget` | `37.9%` | `62.1%` | `0.61` | 35,270,000.00 USD |
| `15M` | `BingX` | `52.12%` | `47.88%` | `1.09` | 10,800,000.00 USD |
| `15M` | `MEXC` | `41.17%` | `58.83%` | `0.70` | 33,670,000.00 USD |
| `15M` | `Bitunix` | `46.07%` | `53.93%` | `0.85` | 42,520,000.00 USD |
| `15M` | `Hyperliquid` | `42.26%` | `57.74%` | `0.73` | 38,050,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `23.87%` | `76.13%` | `0.31` | 7,050,000.00 USD |
| `15M` | `Crypto.com` | `51.85%` | `48.15%` | `1.08` | 2,640,000.00 USD |
| `15M` | `WhiteBIT` | `97.09%` | `2.91%` | `33.36` | 1,240,000.00 USD |
| `15M` | `HTX` | `32.8%` | `67.2%` | `0.49` | 4,020,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `49.17%` | `50.83%` | `0.97` | 24,500,000.00 USD |
| `15M` | `Bitfinex` | `59.15%` | `40.85%` | `1.45` | 354,250.00 USD |
| `15M` | `Kraken` | `55.08%` | `44.92%` | `1.23` | 8,040,000.00 USD |
| `15M` | `Aster` | `29.05%` | `70.95%` | `0.41` | 12,150,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `54.84%` | `45.16%` | `1.21` | 5,710,000.00 USD |
| `15M` | `Whale Positions` | `35.94%` | `64.06%` | `0.56` | 234,970,000.00 USD |
| `15M` | `Global Accounts` | `41.46%` | `58.54%` | `0.71` | 712,370,000.00 USD |
| `1H` | `ETH` | `45.24%` | `54.76%` | `0.83` | 2,360,000,000.00 USD |
| `1H` | `Binance` | `41.58%` | `58.42%` | `0.71` | 707,560,000.00 USD |
| `1H` | `OKX` | `51.35%` | `48.65%` | `1.06` | 309,300,000.00 USD |
| `1H` | `Bybit` | `42.15%` | `57.85%` | `0.73` | 199,120,000.00 USD |
| `1H` | `KuCoin` | `67.22%` | `32.78%` | `2.05` | 10,210,000.00 USD |
| `1H` | `Gate` | `50.69%` | `49.31%` | `1.03` | 228,700,000.00 USD |
| `1H` | `Bitget` | `43.27%` | `56.73%` | `0.76` | 120,170,000.00 USD |
| `1H` | `BingX` | `56%` | `44%` | `1.27` | 49,110,000.00 USD |
| `1H` | `MEXC` | `47.19%` | `52.81%` | `0.89` | 139,520,000.00 USD |
| `1H` | `Bitunix` | `44.94%` | `55.06%` | `0.82` | 114,930,000.00 USD |
| `1H` | `Hyperliquid` | `62.03%` | `37.97%` | `1.63` | 166,780,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `61.72%` | `38.28%` | `1.61` | 23,430,000.00 USD |
| `1H` | `Crypto.com` | `51.15%` | `48.85%` | `1.05` | 8,370,000.00 USD |
| `1H` | `WhiteBIT` | `3.3%` | `96.7%` | `0.03` | 100,120,000.00 USD |
| `1H` | `HTX` | `39.32%` | `60.68%` | `0.65` | 9,790,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `49.01%` | `50.99%` | `0.96` | 97,090,000.00 USD |
| `1H` | `Bitfinex` | `65.31%` | `34.69%` | `1.88` | 1,490,000.00 USD |
| `1H` | `Kraken` | `47.31%` | `52.69%` | `0.90` | 20,870,000.00 USD |
| `1H` | `Aster` | `33.32%` | `66.68%` | `0.50` | 24,540,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `52.95%` | `47.05%` | `1.13` | 23,520,000.00 USD |
| `1H` | `Whale Positions` | `41.58%` | `58.42%` | `0.71` | 707,560,000.00 USD |
| `1H` | `Global Accounts` | `45.24%` | `54.76%` | `0.83` | 2,360,000,000.00 USD |
| `4H` | `ETH` | `44.77%` | `55.23%` | `0.81` | 9,920,000,000.00 USD |
| `4H` | `Binance` | `43.28%` | `56.72%` | `0.76` | 2,890,000,000.00 USD |
| `4H` | `OKX` | `46.99%` | `53.01%` | `0.89` | 1,410,000,000.00 USD |
| `4H` | `Bybit` | `41.95%` | `58.05%` | `0.72` | 859,400,000.00 USD |
| `4H` | `KuCoin` | `54.2%` | `45.8%` | `1.18` | 26,940,000.00 USD |
| `4H` | `Gate` | `49.89%` | `50.11%` | `1.00` | 967,110,000.00 USD |
| `4H` | `Bitget` | `43.16%` | `56.84%` | `0.76` | 450,090,000.00 USD |
| `4H` | `BingX` | `43.02%` | `56.98%` | `0.76` | 199,800,000.00 USD |
| `4H` | `MEXC` | `44.17%` | `55.83%` | `0.79` | 462,740,000.00 USD |
| `4H` | `Bitunix` | `45.22%` | `54.78%` | `0.83` | 399,050,000.00 USD |
| `4H` | `Hyperliquid` | `37.04%` | `62.96%` | `0.59` | 558,840,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.9%` | `49.1%` | `1.04` | 702,890,000.00 USD |
| `4H` | `Crypto.com` | `46.23%` | `53.77%` | `0.86` | 31,780,000.00 USD |
| `4H` | `WhiteBIT` | `20.94%` | `79.06%` | `0.26` | 198,790,000.00 USD |
| `4H` | `HTX` | `44.52%` | `55.48%` | `0.80` | 35,390,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `52.1%` | `47.9%` | `1.09` | 469,520,000.00 USD |
| `4H` | `Bitfinex` | `40.04%` | `59.96%` | `0.67` | 5,050,000.00 USD |
| `4H` | `Kraken` | `44.91%` | `55.09%` | `0.82` | 41,360,000.00 USD |
| `4H` | `Aster` | `44.73%` | `55.27%` | `0.81` | 90,690,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `52.88%` | `47.12%` | `1.12` | 109,500,000.00 USD |
| `4H` | `Whale Positions` | `43.28%` | `56.72%` | `0.76` | 2,890,000,000.00 USD |
| `4H` | `Global Accounts` | `44.77%` | `55.23%` | `0.81` | 9,920,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `2227.75` | `2228.98` | `2227.75` | `2236.75` | `2223.25` | 107,078,982.08 USD | 47,873,893.40 USD | 59,205,088.68 USD | -11,331,195.28 USD | `-10.58%` | `0B / 1S` |
| `5:00 UTC` | `2233.25` | `2230.29` | `2233.25` | `2234.75` | `2224.25` | 95,342,735.21 USD | 45,163,958.47 USD | 50,178,776.75 USD | -5,014,818.28 USD | `-5.26%` | `0B / 3S` |
| `0:00 UTC` | `2224.25` | `2226.52` | `2224.25` | `2230.75` | `2223.25` | 103,679,050.63 USD | 41,811,152.44 USD | 61,867,898.19 USD | -20,056,745.75 USD | `-19.35%` | `0B / 2S` |
| `5:00 UTC` | `2223.75` | `2226.83` | `2223.75` | `2231.75` | `2223.25` | 59,922,094.97 USD | 29,249,984.51 USD | 30,672,110.46 USD | -1,422,125.96 USD | `-2.37%` | `1B / 1S` |
| `0:00 UTC` | `2222.75` | `2224.81` | `2222.75` | `2229.75` | `2221.25` | 65,855,959.19 USD | 30,261,207.11 USD | 35,594,752.09 USD | -5,333,544.98 USD | `-8.10%` | `0B / 4S` |
| `5:00 UTC` | `2221.75` | `2223.05` | `2221.75` | `2226.25` | `2220.25` | 71,858,619.15 USD | 38,686,757.89 USD | 33,171,861.26 USD | 5,514,896.63 USD | `+7.67%` | `0B / 0S` |
| `0:00 UTC` | `2229.25` | `2226.54` | `2229.25` | `2231.25` | `2220.25` | 81,297,282.61 USD | 40,950,851.56 USD | 40,346,431.05 USD | 604,420.51 USD | `+0.74%` | `0B / 2S` |
| `5:00 UTC` | `2227.25` | `2227.77` | `2227.25` | `2229.75` | `2226.25` | 53,422,952.94 USD | 29,109,463.85 USD | 24,313,489.09 USD | 4,795,974.76 USD | `+8.98%` | `1B / 0S` |
| `0:00 UTC` | `2223.75` | `2224.01` | `2223.75` | `2228.25` | `2221.75` | 56,423,190.50 USD | 27,667,054.76 USD | 28,756,135.74 USD | -1,089,080.98 USD | `-1.93%` | `0B / 3S` |
| `5:00 UTC` | `2222.25` | `2222.38` | `2222.25` | `2224.25` | `2220.75` | 9,519,646.49 USD | 3,876,247.41 USD | 5,643,399.08 USD | -1,767,151.67 USD | `-18.56%` | `0B / 2S` |

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
| `5m` | -884,700.00 USD | -3,080,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -4,480,000.00 USD | 3,330,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -4,310,000.00 USD | -4,320,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -9,350,000.00 USD | 16,390,000.00 USD | **`ACCUMULATION`** |
| `2h` | -30,590,000.00 USD | -6,570,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -11,730,000.00 USD | -64,590,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -17,740,000.00 USD | -45,450,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 2,490,000.00 USD | -216,070,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -76,570,000.00 USD | -633,820,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -154,240,000.00 USD | -1,950,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -224,200,000.00 USD | -3,080,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,190,000,000.00 USD | -9,820,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-884.70K` | 15m=`-4.48M` | 1h=`-9.35M` | 24h=`-154.24M`
* Futures Capital Netflows: 5m=`-3.08M` | 15m=`+3.33M` | 1h=`+16.39M` | 24h=`-1.95B`
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
  * `2026-10-30 15:33:17 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:17 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:18:17 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:17 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `2195.62` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2177.87` (Risk Distance: `17.75` pts)
  * +2.5R Take Profit: `2240.00`
  * Mathematical Lot Sizing: **`0.56 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2252.28` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2270.03` (Risk Distance: `17.75` pts)
  * +2.5R Take Profit: `2207.90`
  * Mathematical Lot Sizing: **`0.56 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2237.41`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
