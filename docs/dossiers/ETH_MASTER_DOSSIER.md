# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ETH
**Canonical Key**: `ETH` | **Broker Instrument**: `ETHUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 14:14:30 IST` (`2026-10-30 08:44:30 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `2220.00` | **Live Ask Quote**: `2223.60` | **Mid Price**: `2221.80`
- **Spread Points**: `360.00` | **Spread BPS**: `16.20 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `2219.66` | VWAP Z-Score: `+0.07` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `13.04` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `40.45` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `2271.52` | Lower -3.00σ Band: `2167.81`
  * Upper +2.51σ Band: `2263.05` | Lower -2.51σ Band: `2176.28`
  * Upper +2.01σ Band: `2254.41` | Lower -2.01σ Band: `2184.92`
  * Upper +2.00σ Band: `2254.23` | Lower -2.00σ Band: `2185.09`
  * Upper +1.28σ Band: `2241.79` | Lower -1.28σ Band: `2197.54`
  * Upper +1.00σ Band: `2236.95` | Lower -1.00σ Band: `2202.38`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`2232.02` | EMA-20=`2233.63` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`2247.20` (Slope: `+0.0000`) | EMA-100=`2270.92`
  * Institutional Anchors: EMA-144=`2284.12` | EMA-200=`2295.62` (Slope: `-0.3264`) | EMA-233=`2300.81`
- **Range Boundaries**: 24H High=`2374.90` | 24H Low=`2167.70` | Weekly High=`2387.80` | Weekly Low=`2167.70`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `2252.28` (Distance: `-1.31%`)
  * Point of Control (POC) = `2241.75` (Distance: `-0.85%`)
  * Value Area Low (VAL) = `2191.58` (Distance: `+1.42%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`2339.52` | POC=`2321.58` | VAL=`2296.66`
  * Prior Day Extremes: PDH=`2374.90` | PDL=`2225.40` | PDC=`2252.70`
  * Monday Range Blueprint: High=`2348.00` | Mid=`2318.15` | Low=`2288.30`
  * Developing Weekly Value Area: Weekly VAH=`2353.32` | Weekly POC=`2309.30` | Weekly VAL=`2300.49`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`2289.10` | Low=`2167.70`
  * London Session (08:00-16:00 UTC): High=`2251.30` | Low=`2218.90`
  * New York Session (13:00-21:00 UTC): High=`2235.13` | Low=`2208.47`
  * Initial Balance (First Hour): IB High=`2246.50` | IB Low=`2230.60`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `2212.91` - `2230.69`
  * Optimal Trade Entry (OTE 0.705): `2226.24`
  * Structural Invalidation Anchor (0.786): `2239.57`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `2225.22` | `2230.30` | `2225.21` | `2229.43` | `14,340` | 31,946,426.81 USD | -4,711,098.20 USD | `-14.75%` | -956,841,378.69 USD | `-0.31` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `2229.43` | `2230.58` | `2227.00` | `2227.51` | `8,620` | 19,211,783.33 USD | -412,455.18 USD | `-2.15%` | -957,253,833.88 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `2227.50` | `2227.53` | `2223.66` | `2223.81` | `9,234` | 20,547,775.41 USD | -9,166,327.21 USD | `-44.61%` | -966,420,161.09 USD | `-0.62` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `2235.54` | `2236.80` | `2223.18` | `2231.50` | `48,040` | 107,079,453.78 USD | -11,331,666.98 USD | `-10.58%` | -947,115,462.21 USD | `-0.83` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `2231.50` | `2234.63` | `2224.47` | `2225.21` | `42,750` | 95,342,735.21 USD | -5,014,818.28 USD | `-5.26%` | -952,130,280.49 USD | `-0.39` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `2225.22` | `2230.58` | `2223.66` | `2223.82` | `32,207` | 71,732,451.14 USD | -14,302,318.34 USD | `-19.94%` | -966,432,598.83 USD | `-0.87` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `2238.29` | `2257.30` | `2235.52` | `2252.91` | `148,815` | 334,355,627.68 USD | 27,179,417.73 USD | `+8.13%` | -922,036,231.59 USD | `+0.65` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `2252.91` | `2253.96` | `2228.21` | `2235.54` | `253,701` | 568,308,333.87 USD | -3,920,812.04 USD | `-0.69%` | -925,957,043.62 USD | `+0.36` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `2235.54` | `2236.80` | `2223.18` | `2223.81` | `122,985` | 274,128,174.53 USD | -30,636,365.86 USD | `-11.18%` | -956,593,409.49 USD | `+0.13` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -913,988,928.25 USD | `-0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2257.30` | `2225.47` | `2235.54` | `766,584` | 1,719,026,962.60 USD | 26,122,859.80 USD | `+1.52%` | -887,866,068.44 USD | `+0.88` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `2235.54` | `2236.80` | `2223.18` | `2223.82` | `122,996` | 274,154,640.13 USD | -30,648,803.60 USD | `-11.18%` | -918,514,872.05 USD | `+0.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2368.02` | `2378.69` | `2323.01` | `2335.68` | `664,456` | 1,559,227,814.77 USD | -202,156,116.94 USD | `-12.97%` | -98,115,944.70 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2335.68` | `2335.92` | `2230.20` | `2252.34` | `2,564,135` | 5,830,064,162.53 USD | -554,237,569.32 USD | `-9.51%` | -652,353,514.01 USD | `-1.25` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2252.35` | `2256.50` | `2172.85` | `2236.82` | `1,953,944` | 4,320,239,164.03 USD | -261,635,414.23 USD | `-6.06%` | -913,988,928.25 USD | `-0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `2236.81` | `2257.30` | `2225.47` | `2235.54` | `766,584` | 1,719,026,962.60 USD | 26,122,859.80 USD | `+1.52%` | -887,866,068.44 USD | `+0.88` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `2235.54` | `2236.80` | `2223.18` | `2223.82` | `122,996` | 274,154,640.13 USD | -30,648,803.60 USD | `-11.18%` | -918,514,872.05 USD | `+0.56` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`2221.80`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `2221.60` | `340.8927` | 757,327.22 USD | 7,756,137.75 USD | `11 orders` | `-0.09%` | `-` |
| `BID` | `2221.70` | `171.1214` | 380,180.41 USD | 6,998,810.53 USD | `8 orders` | `-0.08%` | `-` |
| `BID` | `2221.80` | `290.5810` | 645,612.87 USD | 6,618,630.12 USD | `6 orders` | `-0.08%` | `-` |
| `BID` | `2221.90` | `420.1582` | 933,549.50 USD | 5,973,017.25 USD | `11 orders` | `-0.07%` | `-` |
| `BID` | `2222.00` | `420.2195` | 933,727.73 USD | 5,039,467.75 USD | `6 orders` | `-0.07%` | `-` |
| `BID` | `2222.10` | `428.7257` | 952,671.38 USD | 4,105,740.02 USD | `9 orders` | `-0.07%` | `-` |
| `BID` | `2222.20` | `185.1196` | 411,372.78 USD | 3,153,068.64 USD | `4 orders` | `-0.06%` | `-` |
| `BID` | `2222.30` | `119.4263` | 265,401.07 USD | 2,741,695.86 USD | `6 orders` | `-0.06%` | `-` |
| `BID` | `2222.40` | `93.8432` | 208,557.13 USD | 2,476,294.80 USD | `8 orders` | `-0.05%` | `-` |
| `BID` | `2222.50` | `281.0980` | 624,740.31 USD | 2,267,737.67 USD | `9 orders` | `-0.05%` | `-` |
| `BID` | `2222.60` | `129.1451` | 287,037.90 USD | 1,642,997.36 USD | `7 orders` | `-0.04%` | `-` |
| `BID` | `2222.70` | `190.6956` | 423,859.11 USD | 1,355,959.47 USD | `7 orders` | `-0.04%` | `-` |
| `BID` | `2222.80` | `159.7079` | 354,998.72 USD | 932,100.36 USD | `8 orders` | `-0.03%` | `-` |
| `BID` | `2222.90` | `69.0593` | 153,511.92 USD | 577,101.63 USD | `8 orders` | `-0.03%` | `-` |
| `BID` | `2223.00` | `116.0499` | 257,978.93 USD | 423,589.72 USD | `7 orders` | `-0.02%` | `-` |
| `BID` | `2223.10` | `10.4883` | 23,316.54 USD | 165,610.79 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `2223.20` | `20.3144` | 45,162.97 USD | 142,294.25 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `2223.30` | `14.3936` | 32,001.29 USD | 97,131.28 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `2223.40` | `16.6685` | 37,060.74 USD | 65,129.98 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `2223.50` | `12.6239` | 28,069.24 USD | 28,069.24 USD | `2 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `2223.55` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 2,223.55` | `0.00%` | `-` |
| `ASK` | `2223.60` | `43.2218` | 96,107.99 USD | 96,107.99 USD | `3 orders` | `+0.00%` | `-` |
| `ASK` | `2223.70` | `333.5219` | 741,652.65 USD | 837,760.64 USD | `24 orders` | `+0.01%` | `-` |
| `ASK` | `2223.80` | `122.6152` | 272,671.68 USD | 1,110,432.33 USD | `9 orders` | `+0.01%` | `-` |
| `ASK` | `2223.90` | `362.8427` | 806,925.88 USD | 1,917,358.21 USD | `17 orders` | `+0.02%` | `-` |
| `ASK` | `2224.00` | `700.2682` | 1,557,396.48 USD | 3,474,754.68 USD | `12 orders` | `+0.02%` | `-` |
| `ASK` | `2224.10` | `188.2419` | 418,668.81 USD | 3,893,423.49 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `2224.20` | `518.4589` | 1,153,156.29 USD | 5,046,579.78 USD | `8 orders` | `+0.03%` | `-` |
| `ASK` | `2224.30` | `80.3351` | 178,689.36 USD | 5,225,269.14 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `2224.40` | `516.2735` | 1,148,398.77 USD | 6,373,667.91 USD | `9 orders` | `+0.04%` | `-` |
| `ASK` | `2224.50` | `393.3272` | 874,956.36 USD | 7,248,624.27 USD | `9 orders` | `+0.04%` | `-` |
| `ASK` | `2224.60` | `128.8369` | 286,610.57 USD | 7,535,234.84 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `2224.70` | `137.7519` | 306,456.65 USD | 7,841,691.49 USD | `5 orders` | `+0.05%` | `-` |
| `ASK` | `2224.80` | `194.2671` | 432,205.44 USD | 8,273,896.93 USD | `4 orders` | `+0.06%` | `-` |
| `ASK` | `2224.90` | `96.4506` | 214,592.94 USD | 8,488,489.87 USD | `5 orders` | `+0.06%` | `-` |
| `ASK` | `2225.00` | `104.5407` | 232,603.06 USD | 8,721,092.93 USD | `5 orders` | `+0.07%` | `-` |
| `ASK` | `2225.10` | `22.5831` | 50,249.66 USD | 8,771,342.59 USD | `5 orders` | `+0.07%` | `-` |
| `ASK` | `2225.20` | `138.4321` | 308,039.11 USD | 9,079,381.70 USD | `6 orders` | `+0.07%` | `-` |
| `ASK` | `2225.30` | `285.6285` | 635,609.10 USD | 9,714,990.80 USD | `9 orders` | `+0.08%` | `-` |
| `ASK` | `2225.40` | `402.7298` | 896,234.90 USD | 10,611,225.69 USD | `9 orders` | `+0.08%` | `-` |
| `ASK` | `2225.50` | `215.1112` | 478,729.98 USD | 11,089,955.67 USD | `7 orders` | `+0.09%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:11:10 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1786.22` | `30,282.40` | 54,091,066.38 USD | `AT_RISK_LIQ` | `0xde8d9e530b` | `2026-10-30 14:11:10 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1844.01` | `7,964.66` | 14,686,929.37 USD | `AT_RISK_LIQ` | `0x5f912dbde4` | `2026-10-30 14:11:10 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1871.10` | `9,700.00` | 18,149,670.00 USD | `TRIGGER_STOP` | `0xaeaab54bbf` | `2026-10-30 14:11:10 IST` |
| `TOP_STOPS` | `BUY_STOP` | `1926.10` | `10,000.00` | 19,261,000.00 USD | `TRIGGER_STOP` | `0xb37f083bad` | `2026-10-30 14:11:10 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `1928.06` | `8,092.45` | 15,602,701.92 USD | `AT_RISK_LIQ` | `0x9eec98d048` | `2026-10-30 14:11:10 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2121.96` | `30,641.99` | 65,021,116.42 USD | `AT_RISK_LIQ` | `0x77ddcc4b64` | `2026-10-30 14:11:10 IST` |
| `TOP_LIQUIDATIONS` | `LONG_AT_RISK` | `2129.24` | `26,025.05` | 55,413,555.18 USD | `AT_RISK_LIQ` | `0x0392a716db` | `2026-10-30 14:11:10 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2175.00` | `3,533.33` | 7,684,999.71 USD | `TRIGGER_STOP` | `0x469e9a7f62` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2189.70` | `2,054.46` | 4,498,660.04 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2191.10` | `500.00` | 1,095,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2192.00` | `508.61` | 1,114,875.31 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 14:11:10 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2195.00` | `839.60` | 1,842,926.39 USD | `TRIGGER_STOP` | `0x28280399d9` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2198.70` | `4,566.64` | 10,040,664.55 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2201.10` | `500.00` | 1,100,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2202.70` | `1,478.49` | 3,256,660.23 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2203.10` | `500.00` | 1,101,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xf929122994` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2207.80` | `359.96` | 794,719.91 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2208.60` | `508.56` | 1,123,207.82 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2209.30` | `2,361.92` | 5,218,185.22 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2209.30` | `1,030.52` | 2,276,723.86 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2211.10` | `500.00` | 1,105,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2211.10` | `500.00` | 1,105,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xf929122994` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2214.20` | `508.55` | 1,126,026.98 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2215.30` | `1,808.50` | 4,006,373.82 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2215.50` | `691.93` | 1,532,969.59 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2218.10` | `1,354.69` | 3,004,840.77 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2218.20` | `475.44` | 1,054,612.14 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2218.60` | `356.83` | 791,660.38 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2218.80` | `401.99` | 891,943.18 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xc86781f990` | `2026-10-30 14:11:10 IST` |
| `TOP_STOPS` | `SELL_STOP` | `2219.00` | `439.90` | 976,147.64 USD | `TRIGGER_STOP` | `0x369fd6445f` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2219.80` | `1,204.03` | 2,672,695.58 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2219.80` | `902.44` | 2,003,229.43 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2220.30` | `478.98` | 1,063,480.85 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2221.00` | `458.19` | 1,017,637.99 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x9362ca4dfd` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2221.10` | `500.00` | 1,110,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x418aa6bf98` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2221.10` | `500.00` | 1,110,550.00 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xf929122994` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2222.50` | `675.99` | 1,502,383.77 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2222.60` | `355.17` | 789,408.18 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `BUY` | `2224.00` | `450.34` | 1,001,562.61 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2230.00` | `449.15` | 1,001,615.20 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2231.60` | `673.26` | 1,502,450.59 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2234.20` | `896.62` | 2,003,223.04 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2234.60` | `475.55` | 1,062,659.56 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2234.80` | `476.98` | 1,065,956.02 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2236.00` | `1,343.84` | 3,004,828.48 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd911e53d53` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2237.60` | `352.30` | 788,313.42 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xd6e1a6f7bb` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2237.70` | `1,790.43` | 4,006,439.62 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb8eb97eaed` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2238.20` | `1,204.03` | 2,694,849.65 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2239.10` | `680.64` | 1,524,023.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2240.20` | `508.59` | 1,139,347.80 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2242.50` | `2,361.92` | 5,296,600.89 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2244.60` | `1,007.00` | 2,260,318.71 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2246.30` | `508.19` | 1,141,540.46 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2251.40` | `352.99` | 794,719.88 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x2e1aa624f0` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2254.60` | `1,414.72` | 3,189,635.83 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2262.60` | `508.14` | 1,149,726.61 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x71d0e11ebb` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2264.00` | `2,036.20` | 4,609,966.08 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x31dea2516b` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2265.20` | `4,565.19` | 10,341,077.68 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xab5e6f3949` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2269.70` | `620.97` | 1,409,408.35 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0x674982e841` | `2026-10-30 14:11:10 IST` |
| `L3_RESTING_ORDER` | `SELL` | `2272.20` | `2,200.51` | 4,999,999.96 USD | `HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT` | `0xb1ec7febea` | `2026-10-30 14:11:10 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2300.00` | `4,002.10` | 9,204,832.99 USD | `TRIGGER_STOP` | `0xfb941d2344` | `2026-10-30 14:11:10 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2460.03` | `22,046.99` | 54,236,312.53 USD | `AT_RISK_LIQ` | `0x8added25f8` | `2026-10-30 14:11:10 IST` |
| `TOP_STOPS` | `BUY_STOP` | `2513.90` | `3,002.39` | 7,547,704.95 USD | `TRIGGER_STOP` | `0x9c2a2a966e` | `2026-10-30 14:11:10 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2623.99` | `10,000.00` | 26,239,916.73 USD | `AT_RISK_LIQ` | `0xb37f083bad` | `2026-10-30 14:11:10 IST` |
| `TOP_LIQUIDATIONS` | `SHORT_AT_RISK` | `2657.84` | `9,700.00` | 25,781,072.85 USD | `AT_RISK_LIQ` | `0xaeaab54bbf` | `2026-10-30 14:11:10 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `0x5b5d...c060` | `SHORT` | 234,565,068.80 USD | `105,365.68` | `2322.74` | `2225.70` | `3747.56` | 10,172,336.70 USD | `+4.34%` | `5X Cross` |
| `4` | `0xb83d...6e36` | `SHORT` | 129,655,618.05 USD | `58,243.39` | `2375.30` | `2225.70` | `4469.30` | 8,690,292.80 USD | `+6.70%` | `5X Cross` |
| `9` | `0x77dd...e0e9` | `LONG` | 68,218,266.12 USD | `30,641.99` | `2610.31` | `2225.70` | `2121.88` | -11,766,908.92 USD | `-17.25%` | `10X Cross` |
| `11` | `0xde8d...9524` | `LONG` | 67,342,008.90 USD | `30,282.40` | `2134.45` | `2225.70` | `1786.14` | 2,705,678.33 USD | `+4.02%` | `20X Cross` |
| `16` | `0x0392...d7d9` | `LONG` | 57,874,508.64 USD | `26,025.05` | `2518.71` | `2225.70` | `2129.16` | -7,675,213.45 USD | `-13.26%` | `9X Cross` |
| `22` | `0x8add...7d2c` | `SHORT` | 49,100,848.76 USD | `22,046.99` | `2271.09` | `2225.70` | `2469.11` | 970,048.54 USD | `+1.98%` | `25X Cross` |
| `25` | `0x15a4...dfdb` | `SHORT` | 44,482,000.00 USD | `20,000.00` | `2228.11` | `2225.70` | `3187.84` | 80,327.68 USD | `+0.18%` | `20X Cross` |
| `26` | `0xdf95...7d72` | `SHORT` | 43,926,373.48 USD | `19,730.66` | `2402.53` | `2225.70` | `4219.37` | 3,477,224.71 USD | `+7.92%` | `25X Cross` |
| `33` | `0x6046...b21d` | `LONG` | 35,422,959.49 USD | `15,927.59` | `2410.19` | `2225.70` | `1773.99` | -2,965,660.16 USD | `-8.37%` | `6X Cross` |
| `34` | `0xeced...6210` | `SHORT` | 34,336,947.56 USD | `15,423.32` | `2522.09` | `2225.70` | `3579.41` | 4,562,199.83 USD | `+13.29%` | `20X Cross` |
| `36` | `0xb695...a92d` | `SHORT` | 33,819,232.93 USD | `15,191.46` | `2557.74` | `2225.70` | `3715.19` | 5,036,660.62 USD | `+14.89%` | `20X Cross` |
| `39` | `0x45d2...4029` | `SHORT` | 31,056,885.00 USD | `13,950.00` | `2443.60` | `2225.70` | `5335.76` | 3,031,397.46 USD | `+9.76%` | `20X Cross` |
| `41` | `0xa61c...66b9` | `LONG` | 28,665,489.60 USD | `12,888.00` | `2369.69` | `2225.70` | `1466.50` | -1,875,164.94 USD | `-6.54%` | `10X Cross` |
| `44` | `0x2371...0883` | `LONG` | 26,713,200.00 USD | `12,000.00` | `2421.77` | `2225.70` | `1279.12` | -2,348,094.85 USD | `-8.79%` | `20X Cross` |
| `45` | `0xbd1c...ff0e` | `LONG` | 26,707,200.00 USD | `12,000.00` | `2419.91` | `2225.70` | `1520.02` | -2,331,832.39 USD | `-8.73%` | `20X Cross` |
| `50` | `0xefe4...194b` | `SHORT` | 25,110,826.51 USD | `11,279.68` | `2258.96` | `2225.70` | `3193.90` | 369,616.99 USD | `+1.47%` | `20X Cross` |
| `53` | `0x09dc...c094` | `LONG` | 24,466,200.00 USD | `11,000.00` | `2465.31` | `2225.70` | `1637.09` | -2,652,223.04 USD | `-10.84%` | `20X Cross` |
| `54` | `0xa9de...e049` | `LONG` | 24,465,100.00 USD | `11,000.00` | `2481.81` | `2225.70` | `1643.76` | -2,834,879.46 USD | `-11.59%` | `20X Cross` |
| `55` | `0x0c5d...36b3` | `LONG` | 24,464,000.00 USD | `11,000.00` | `2482.20` | `2225.70` | `1644.09` | -2,840,253.24 USD | `-11.61%` | `20X Cross` |
| `56` | `0x6c93...59a4` | `LONG` | 24,461,800.00 USD | `11,000.00` | `2441.15` | `2225.70` | `1602.05` | -2,390,872.73 USD | `-9.77%` | `20X Cross` |
| `70` | `0xa2ce...3126` | `LONG` | 22,284,542.26 USD | `10,016.88` | `2162.83` | `2225.70` | `1549.12` | 619,740.21 USD | `+2.78%` | `10X Cross` |
| `71` | `0xb37f...66ca` | `SHORT` | 22,265,000.00 USD | `10,000.00` | `2290.69` | `2225.70` | `2623.92` | 641,991.85 USD | `+2.88%` | `25X Cross` |
| `72` | `0xec7f...df39` | `LONG` | 22,242,000.00 USD | `10,000.00` | `2719.35` | `2225.70` | `1720.61` | -4,951,548.52 USD | `-22.26%` | `20X Cross` |
| `73` | `0x6646...6de5` | `LONG` | 22,238,000.00 USD | `10,000.00` | `1765.80` | `2225.70` | `1720.03` | 4,579,942.55 USD | `+20.60%` | `25X Cross` |
| `75` | `0x939f...04d2` | `LONG` | 21,848,159.89 USD | `9,823.81` | `2427.28` | `2225.70` | `1725.18` | -1,996,990.71 USD | `-9.14%` | `25X Cross` |
| `77` | `0xaeaa...2416` | `SHORT` | 21,574,740.00 USD | `9,700.00` | `2311.92` | `2225.70` | `2657.77` | 850,942.40 USD | `+3.94%` | `25X Cross` |
| `84` | `0xf517...c032` | `SHORT` | 20,762,313.91 USD | `9,326.35` | `2202.91` | `2225.70` | `3128.59` | -217,175.70 USD | `-1.05%` | `25X Cross` |
| `85` | `0xca49...53c8` | `SHORT` | 20,438,978.84 USD | `9,182.34` | `2549.39` | `2225.70` | `3884.81` | 2,970,463.11 USD | `+14.53%` | `25X Cross` |
| `86` | `0xba5d...a352` | `SHORT` | 20,160,813.68 USD | `9,054.12` | `2493.89` | `2225.70` | `2765.15` | 2,419,193.58 USD | `+12.00%` | `20X Cross` |
| `88` | `0xea00...a918` | `LONG` | 20,022,708.93 USD | `9,003.83` | `2003.01` | `2225.70` | `1424.21` | 1,987,930.06 USD | `+9.93%` | `5X Cross` |
| `110` | `0xecb6...2b00` | `SHORT` | 18,364,127.94 USD | `8,249.09` | `2243.43` | `2225.70` | `6034.94` | 142,162.76 USD | `+0.77%` | `15X Cross` |
| `113` | `0x9eec...daab` | `LONG` | 18,016,226.11 USD | `8,092.45` | `1658.44` | `2225.70` | `1929.01` | 4,595,361.58 USD | `+25.51%` | `15X Cross` |
| `114` | `0x5f91...65aa` | `LONG` | 17,711,801.79 USD | `7,964.66` | `1626.99` | `2225.70` | `1843.94` | 4,753,358.73 USD | `+26.84%` | `16X Cross` |
| `124` | `0xec0b...b078` | `LONG` | 15,600,761.91 USD | `7,007.80` | `2065.97` | `2225.70` | `1057.81` | 1,122,832.32 USD | `+7.20%` | `25X Cross` |
| `130` | `0xf02d...5eb3` | `LONG` | 15,263,480.52 USD | `6,855.99` | `2383.33` | `2225.70` | `1126.83` | -1,076,608.25 USD | `-7.05%` | `20X Cross` |
| `132` | `0xcf53...ee11` | `SHORT` | 15,136,030.99 USD | `6,803.63` | `1862.69` | `2225.70` | `4196.19` | -2,462,925.60 USD | `-16.27%` | `7X Cross` |
| `136` | `0x4ff9...38d3` | `LONG` | 14,599,868.33 USD | `6,564.10` | `2447.40` | `2225.70` | `1669.71` | -1,465,154.42 USD | `-10.04%` | `3X Isolated` |
| `138` | `0xf78c...c581` | `LONG` | 14,455,192.57 USD | `6,500.22` | `2521.53` | `2225.70` | `1913.19` | -1,935,348.37 USD | `-13.39%` | `20X Cross` |
| `139` | `0x1ee7...edf5` | `LONG` | 14,454,700.00 USD | `6,500.00` | `2301.55` | `2225.70` | `2068.93` | -505,393.66 USD | `-3.50%` | `25X Cross` |
| `141` | `0x0622...8088` | `LONG` | 14,364,923.49 USD | `6,452.67` | `2229.14` | `2225.70` | `675.16` | -19,026.43 USD | `-0.13%` | `5X Cross` |
| `145` | `0x799f...5f4c` | `LONG` | 14,049,964.02 USD | `6,310.90` | `2390.33` | `2225.70` | `1852.02` | -1,035,200.60 USD | `-7.37%` | `20X Cross` |
| `149` | `0x08bf...7872` | `SHORT` | 13,856,596.73 USD | `6,224.05` | `2258.00` | `2225.70` | `2584.99` | 197,319.38 USD | `+1.42%` | `20X Cross` |
| `152` | `0x524e...0de0` | `LONG` | 13,356,600.00 USD | `6,000.00` | `2246.48` | `2225.70` | `2002.89` | -122,285.04 USD | `-0.92%` | `10X Cross` |
| `153` | `0xd9e7...4aff` | `LONG` | 13,344,600.00 USD | `6,000.00` | `2480.18` | `2225.70` | `1407.48` | -1,536,524.33 USD | `-11.51%` | `20X Cross` |
| `158` | `0xc179...e0c8` | `LONG` | 13,034,386.73 USD | `5,854.73` | `2294.94` | `2225.70` | `1159.48` | -401,885.44 USD | `-3.08%` | `10X Cross` |
| `163` | `0x0c4a...1b19` | `LONG` | 12,589,188.86 USD | `5,660.10` | `2373.06` | `2225.70` | `2081.53` | -842,569.27 USD | `-6.69%` | `25X Isolated` |
| `170` | `0x7fda...17d1` | `LONG` | 11,833,941.80 USD | `5,315.76` | `2211.05` | `2225.70` | `0.000000` | 80,499.55 USD | `+0.68%` | `25X Cross` |
| `186` | `0x418a...8888` | `SHORT` | 11,121,000.00 USD | `5,000.00` | `2494.55` | `2225.70` | `2906.42` | 1,351,760.46 USD | `+12.16%` | `25X Cross` |
| `190` | `0x45ab...6cbc` | `LONG` | 10,943,235.74 USD | `4,920.96` | `2727.66` | `2225.70` | `1378.68` | -2,479,508.06 USD | `-22.66%` | `7X Cross` |
| `194` | `0x64b7...9da9` | `LONG` | 10,812,295.43 USD | `4,856.84` | `2604.61` | `2225.70` | `601.05` | -1,837,918.99 USD | `-17.00%` | `25X Cross` |
| `200` | `0xfb18...eb17` | `SHORT` | 10,613,498.76 USD | `4,768.18` | `2315.53` | `2225.70` | `2625.63` | 427,383.03 USD | `+4.03%` | `25X Cross` |
| `203` | `0x5559...d43b` | `SHORT` | 10,577,653.46 USD | `4,755.93` | `2262.69` | `2225.70` | `2755.68` | 183,552.42 USD | `+1.74%` | `25X Cross` |
| `213` | `0xe091...6705` | `SHORT` | 10,008,450.44 USD | `4,500.00` | `2467.33` | `2225.70` | `2463.11` | 1,094,558.06 USD | `+10.94%` | `20X Cross` |
| `221` | `0xb829...3a81` | `LONG` | 9,775,161.05 USD | `4,394.91` | `2398.60` | `2225.70` | `1463.99` | -766,480.90 USD | `-7.84%` | `20X Cross` |
| `238` | `0x28bb...fca6` | `SHORT` | 9,371,443.13 USD | `4,209.61` | `1896.10` | `2225.70` | `3035.34` | -1,389,560.57 USD | `-14.83%` | `20X Cross` |
| `239` | `0x6ea4...0ea7` | `SHORT` | 9,308,172.16 USD | `4,184.01` | `2602.13` | `2225.70` | `3425.05` | 1,579,174.50 USD | `+16.97%` | `20X Cross` |
| `253` | `0x5e9e...35ee` | `SHORT` | 8,919,215.97 USD | `4,007.56` | `1796.39` | `2225.70` | `2585.54` | -1,720,065.88 USD | `-19.28%` | `20X Cross` |
| `255` | `0xfb94...0ddf` | `SHORT` | 8,900,673.29 USD | `4,002.10` | `2382.44` | `2225.70` | `5104.44` | 634,110.86 USD | `+7.12%` | `20X Cross` |
| `256` | `0x8cc9...2b6a` | `SHORT` | 8,895,200.00 USD | `4,000.00` | `1791.18` | `2225.70` | `3527.46` | -1,730,453.33 USD | `-19.45%` | `25X Cross` |
| `257` | `0x3dc9...54b0` | `SHORT` | 8,894,511.07 USD | `3,999.69` | `2480.32` | `2225.70` | `6570.35` | 1,026,025.49 USD | `+11.54%` | `20X Cross` |
| `277` | `0x4b67...f4e7` | `LONG` | 8,497,552.39 USD | `3,820.84` | `2591.51` | `2225.70` | `1354.51` | -1,404,221.16 USD | `-16.53%` | `20X Cross` |
| `283` | `0x12d2...f97f` | `LONG` | 8,356,900.36 USD | `3,757.26` | `2446.50` | `2225.70` | `1790.25` | -835,266.03 USD | `-9.99%` | `20X Cross` |
| `302` | `0x8ae4...3d60` | `LONG` | 7,914,144.66 USD | `3,558.20` | `2482.21` | `2225.70` | `508.78` | -918,053.38 USD | `-11.60%` | `10X Cross` |
| `304` | `0x469e...58a5` | `SHORT` | 7,859,546.37 USD | `3,533.33` | `2203.63` | `2225.70` | `3090.49` | -73,383.28 USD | `-0.93%` | `25X Cross` |
| `315` | `0x218a...7da2` | `SHORT` | 7,716,755.55 USD | `3,465.87` | `2208.16` | `2225.70` | `3101.55` | -63,559.77 USD | `-0.82%` | `10X Cross` |
| `330` | `0xec4a...cf62` | `LONG` | 7,049,554.15 USD | `3,166.63` | `2226.56` | `2225.70` | `1593.64` | -1,165.28 USD | `-0.02%` | `25X Cross` |
| `342` | `0x4a20...3c26` | `LONG` | 6,678,900.00 USD | `3,000.00` | `2428.72` | `2225.70` | `586.25` | -607,260.28 USD | `-9.09%` | `20X Cross` |
| `343` | `0x007d...67a0` | `LONG` | 6,677,700.00 USD | `3,000.00` | `2400.00` | `2225.70` | `1469.58` | -522,300.00 USD | `-7.82%` | `25X Cross` |
| `344` | `0x9c2a...f6a8` | `SHORT` | 6,676,711.99 USD | `3,002.39` | `2515.77` | `2225.70` | `2591.82` | 876,625.90 USD | `+13.13%` | `20X Cross` |
| `345` | `0xb823...9763` | `SHORT` | 6,672,600.00 USD | `3,000.00` | `2229.66` | `2225.70` | `3233.44` | 16,396.68 USD | `+0.25%` | `25X Cross` |
| `390` | `0xb8eb...1dd5` | `LONG` | 5,845,317.09 USD | `2,625.69` | `2232.77` | `2225.70` | `1520.07` | -17,262.61 USD | `-0.30%` | `25X Cross` |
| `398` | `0x8328...f54a` | `SHORT` | 5,730,027.25 USD | `2,576.45` | `2292.01` | `2225.70` | `3279.28` | 175,244.04 USD | `+3.06%` | `25X Cross` |
| `401` | `0xed48...7c9b` | `SHORT` | 5,680,092.06 USD | `2,551.13` | `2460.02` | `2225.70` | `3229.31` | 595,754.35 USD | `+10.49%` | `20X Cross` |
| `403` | `0x1c98...7fc7` | `LONG` | 5,566,510.02 USD | `2,500.00` | `2452.60` | `2225.70` | `1916.68` | -565,011.54 USD | `-10.15%` | `10X Cross` |
| `404` | `0x970c...2a93` | `SHORT` | 5,561,000.00 USD | `2,500.00` | `2229.57` | `2225.70` | `5069.94` | 12,944.49 USD | `+0.23%` | `20X Cross` |
| `420` | `0xa445...329d` | `LONG` | 5,356,780.13 USD | `2,406.14` | `2354.86` | `2225.70` | `1743.21` | -309,335.15 USD | `-5.77%` | `25X Cross` |
| `421` | `0xfbe2...c8ea` | `SHORT` | 5,310,661.16 USD | `2,385.21` | `2041.57` | `2225.70` | `2619.90` | -441,094.50 USD | `-8.31%` | `20X Cross` |
| `422` | `0x6749...ce07` | `SHORT` | 5,309,489.96 USD | `2,384.89` | `2220.92` | `2225.70` | `3629.67` | -12,826.93 USD | `-0.24%` | `20X Cross` |
| `423` | `0x645b...87b8` | `SHORT` | 5,298,539.68 USD | `2,379.98` | `2421.64` | `2225.70` | `11466.51` | 464,907.28 USD | `+8.77%` | `10X Cross` |
| `432` | `0x77ee...2902` | `SHORT` | 5,100,453.03 USD | `2,290.69` | `2476.53` | `2225.70` | `6073.78` | 572,519.21 USD | `+11.22%` | `25X Cross` |
| `438` | `0xd911...961e` | `LONG` | 5,043,419.81 USD | `2,265.48` | `2231.52` | `2225.70` | `1240.11` | -12,069.59 USD | `-0.24%` | `25X Cross` |
| `461` | `0xd507...c948` | `SHORT` | 4,831,179.38 USD | `2,172.00` | `2387.49` | `2225.70` | `2600.29` | 354,461.65 USD | `+7.34%` | `5X Isolated` |
| `467` | `0x023a...2355` | `LONG` | 4,759,511.19 USD | `2,137.95` | `2329.46` | `2225.70` | `0.000000` | -220,775.75 USD | `-4.64%` | `25X Cross` |
| `468` | `0x382b...3e39` | `SHORT` | 4,740,998.46 USD | `2,129.54` | `2296.66` | `2225.70` | `4574.58` | 149,838.75 USD | `+3.16%` | `25X Cross` |
| `476` | `0x4487...c92d` | `LONG` | 4,680,665.59 USD | `2,103.10` | `2232.13` | `2225.70` | `1626.54` | -13,749.82 USD | `-0.29%` | `10X Cross` |
| `502` | `0xbcd4...0dd2` | `SHORT` | 4,498,057.44 USD | `2,020.60` | `2233.24` | `2225.70` | `2705.74` | 14,444.49 USD | `+0.32%` | `25X Cross` |
| `510` | `0xe02e...d78b` | `LONG` | 4,452,600.00 USD | `2,000.00` | `2228.11` | `2225.70` | `2171.63` | -3,623.47 USD | `-0.08%` | `25X Cross` |
| `511` | `0x3453...b323` | `SHORT` | 4,447,873.75 USD | `2,000.12` | `2322.47` | `2225.70` | `2392.27` | 197,362.09 USD | `+4.44%` | `25X Cross` |
| `516` | `0xf3dc...1672` | `SHORT` | 4,403,927.46 USD | `1,980.36` | `2240.44` | `2225.70` | `2777.29` | 32,960.10 USD | `+0.75%` | `20X Cross` |
| `519` | `0x7a6d...f79c` | `SHORT` | 4,389,127.01 USD | `1,973.44` | `2418.41` | `2225.70` | `2545.95` | 383,470.99 USD | `+8.74%` | `25X Cross` |
| `522` | `0xac48...3201` | `SHORT` | 4,368,364.89 USD | `1,964.37` | `2272.04` | `2225.70` | `3094.55` | 94,777.41 USD | `+2.17%` | `20X Cross` |
| `533` | `0x8376...9a1e` | `SHORT` | 4,248,943.10 USD | `1,910.50` | `2477.72` | `2225.70` | `3184.48` | 484,745.07 USD | `+11.41%` | `20X Cross` |
| `537` | `0x739c...cfb2` | `SHORT` | 4,225,220.00 USD | `1,900.00` | `2418.12` | `2225.70` | `2459.09` | 369,226.38 USD | `+8.74%` | `25X Cross` |
| `564` | `0x7265...91a5` | `LONG` | 4,007,537.73 USD | `1,801.87` | `2533.96` | `2225.70` | `1987.16` | -558,328.72 USD | `-13.93%` | `20X Cross` |
| `565` | `0xc619...10f5` | `LONG` | 4,003,920.00 USD | `1,800.00` | `2313.55` | `2225.70` | `1811.66` | -160,475.83 USD | `-4.01%` | `25X Cross` |
| `566` | `0xbb34...1696` | `LONG` | 4,002,840.00 USD | `1,800.00` | `2313.95` | `2225.70` | `1979.90` | -162,278.23 USD | `-4.05%` | `25X Cross` |
| `580` | `0x91a9...3f70` | `SHORT` | 3,934,587.23 USD | `1,767.48` | `2156.23` | `2225.70` | `3667.03` | -123,483.15 USD | `-3.14%` | `4X Cross` |
| `605` | `0x2577...4897` | `LONG` | 3,798,459.98 USD | `1,706.25` | `2232.30` | `2225.70` | `215.95` | -10,413.44 USD | `-0.27%` | `15X Cross` |
| `611` | `0xfeec...4e9c` | `SHORT` | 3,766,304.75 USD | `1,691.81` | `2566.49` | `2225.70` | `2509.50` | 575,719.76 USD | `+15.29%` | `10X Cross` |
| `629` | `0xeee0...0b53` | `LONG` | 3,640,963.55 USD | `1,637.12` | `2468.64` | `2225.70` | `186.17` | -400,512.51 USD | `-11.00%` | `7X Cross` |
| `631` | `0x27b8...12fc` | `LONG` | 3,621,264.73 USD | `1,628.12` | `2468.73` | `2225.70` | `621.09` | -398,129.91 USD | `-10.99%` | `10X Cross` |
| `633` | `0x982b...4606` | `LONG` | 3,617,716.31 USD | `1,626.82` | `2575.24` | `2225.70` | `1547.43` | -571,736.76 USD | `-15.80%` | `5X Isolated` |
| `640` | `0x73d7...8be1` | `LONG` | 3,564,702.06 USD | `1,601.47` | `2410.40` | `2225.70` | `1764.07` | -295,476.86 USD | `-8.29%` | `25X Cross` |
| `641` | `0xad54...6203` | `LONG` | 3,558,323.66 USD | `1,597.45` | `2591.98` | `2225.70` | `2049.14` | -582,254.38 USD | `-16.36%` | `10X Isolated` |
| `644` | `0x9599...c60a` | `LONG` | 3,538,315.16 USD | `1,589.40` | `2233.08` | `2225.70` | `0.000000` | -10,936.84 USD | `-0.31%` | `20X Cross` |
| `649` | `0x880a...311c` | `LONG` | 3,513,991.25 USD | `1,578.40` | `2209.72` | `2225.70` | `0.000000` | 26,167.40 USD | `+0.74%` | `9X Cross` |
| `662` | `0x936c...bb0f` | `LONG` | 3,438,687.59 USD | `1,544.64` | `2233.05` | `2225.70` | `0.000000` | -10,585.23 USD | `-0.31%` | `20X Cross` |
| `669` | `0xe170...9300` | `SHORT` | 3,410,434.94 USD | `1,533.40` | `2076.39` | `2225.70` | `3105.92` | -226,485.44 USD | `-6.64%` | `25X Cross` |
| `672` | `0x4b86...df9d` | `SHORT` | 3,389,528.40 USD | `1,524.00` | `2287.40` | `2225.70` | `2759.64` | 96,469.20 USD | `+2.85%` | `9X Isolated` |
| `676` | `0x2e2b...2fab` | `LONG` | 3,352,104.97 USD | `1,507.38` | `2245.53` | `2225.70` | `1244.67` | -32,768.13 USD | `-0.98%` | `25X Cross` |
| `681` | `0xf929...d1f9` | `SHORT` | 3,339,900.00 USD | `1,500.00` | `2423.37` | `2225.70` | `2677.68` | 295,155.26 USD | `+8.84%` | `25X Cross` |
| `683` | `0x251f...6e5d` | `LONG` | 3,336,450.00 USD | `1,500.00` | `2346.68` | `2225.70` | `1876.30` | -183,580.49 USD | `-5.50%` | `20X Cross` |
| `684` | `0xde6b...3361` | `LONG` | 3,336,300.00 USD | `1,500.00` | `2216.98` | `2225.70` | `2168.56` | 10,819.26 USD | `+0.32%` | `25X Cross` |
| `705` | `0xb885...3c54` | `LONG` | 3,227,124.90 USD | `1,450.00` | `2274.34` | `2225.70` | `24.00` | -70,683.24 USD | `-2.19%` | `20X Cross` |
| `709` | `0xef70...a84c` | `SHORT` | 3,211,691.08 USD | `1,442.74` | `2424.73` | `2225.70` | `3264.27` | 286,579.74 USD | `+8.92%` | `25X Cross` |
| `713` | `0xe668...b5ca` | `SHORT` | 3,189,428.67 USD | `1,434.22` | `2241.90` | `2225.70` | `2314.21` | 25,971.62 USD | `+0.81%` | `25X Cross` |
| `719` | `0xbadb...9ee6` | `LONG` | 3,176,370.66 USD | `1,428.16` | `1936.00` | `2225.70` | `1076.83` | 411,449.01 USD | `+12.95%` | `20X Cross` |
| `771` | `0x53f8...ceff` | `LONG` | 2,999,137.43 USD | `1,348.65` | `2276.73` | `2225.70` | `0.000000` | -71,387.04 USD | `-2.38%` | `20X Cross` |
| `788` | `0xa0fb...96be` | `LONG` | 2,932,637.94 USD | `1,317.09` | `2277.10` | `2225.70` | `1519.93` | -66,524.35 USD | `-2.27%` | `3X Cross` |
| `789` | `0x0dd5...f6ee` | `LONG` | 2,924,580.07 USD | `1,314.95` | `2298.06` | `2225.70` | `1559.83` | -97,261.74 USD | `-3.33%` | `5X Cross` |
| `806` | `0x039c...0ebd` | `LONG` | 2,868,782.06 USD | `1,289.80` | `2226.24` | `2225.70` | `0.000000` | -2,631.88 USD | `-0.09%` | `25X Cross` |
| `819` | `0x1f16...6d07` | `LONG` | 2,818,749.00 USD | `1,266.00` | `2261.43` | `2225.70` | `1382.43` | -44,222.23 USD | `-1.57%` | `7X Cross` |
| `826` | `0xc435...c905` | `SHORT` | 2,775,676.80 USD | `1,248.00` | `2704.38` | `2225.70` | `3778.55` | 599,393.55 USD | `+21.59%` | `20X Cross` |
| `831` | `0x6859...7e1e` | `SHORT` | 2,754,151.79 USD | `1,237.15` | `2200.39` | `2225.70` | `4818.47` | -31,924.63 USD | `-1.16%` | `25X Cross` |
| `845` | `0x7277...0b98` | `SHORT` | 2,714,870.22 USD | `1,219.45` | `2206.05` | `2225.70` | `3395.29` | -24,682.42 USD | `-0.91%` | `20X Cross` |
| `848` | `0x7178...0854` | `LONG` | 2,710,723.91 USD | `1,218.63` | `2461.81` | `2225.70` | `1175.92` | -289,322.49 USD | `-10.67%` | `10X Cross` |
| `860` | `0xaaa1...ab8c` | `SHORT` | 2,668,560.00 USD | `1,200.00` | `2276.29` | `2225.70` | `2365.26` | 62,997.58 USD | `+2.36%` | `25X Isolated` |
| `872` | `0xfc27...9d9d` | `LONG` | 2,633,262.07 USD | `1,182.80` | `2237.33` | `2225.70` | `0.000000` | -13,052.62 USD | `-0.50%` | `25X Cross` |
| `875` | `0x07fd...689d` | `LONG` | 2,619,434.95 USD | `1,176.69` | `2416.34` | `2225.70` | `0.000000` | -223,864.99 USD | `-8.55%` | `25X Cross` |
| `879` | `0xa70a...4be9` | `LONG` | 2,601,526.76 USD | `1,168.91` | `2251.37` | `2225.70` | `1008.43` | -30,130.08 USD | `-1.16%` | `20X Cross` |
| `883` | `0x6e6f...82a6` | `LONG` | 2,587,350.91 USD | `1,163.32` | `2257.18` | `2225.70` | `1401.19` | -38,491.11 USD | `-1.49%` | `20X Cross` |
| `930` | `0x2f80...f203` | `SHORT` | 2,424,636.25 USD | `1,088.94` | `1984.00` | `2225.70` | `2961.44` | -264,169.06 USD | `-10.90%` | `20X Cross` |
| `937` | `0x6f11...0389` | `SHORT` | 2,401,961.90 USD | `1,079.00` | `2333.39` | `2225.70` | `3198.74` | 115,767.01 USD | `+4.82%` | `25X Cross` |
| `938` | `0x8eb7...b90f` | `LONG` | 2,396,891.98 USD | `1,077.74` | `2396.38` | `2225.70` | `1880.97` | -185,786.06 USD | `-7.75%` | `5X Isolated` |
| `939` | `0x2b61...2f6c` | `SHORT` | 2,394,567.49 USD | `1,076.60` | `2681.75` | `2225.70` | `6266.59` | 492,605.25 USD | `+20.57%` | `10X Cross` |
| `951` | `0xef96...9383` | `LONG` | 2,364,409.79 USD | `1,063.13` | `2234.39` | `2225.70` | `0.000000` | -11,046.73 USD | `-0.47%` | `25X Cross` |
| `972` | `0x30af...393e` | `SHORT` | 2,315,758.97 USD | `1,041.16` | `2252.26` | `2225.70` | `2296.95` | 29,223.36 USD | `+1.26%` | `25X Cross` |
| `984` | `0x1b2a...f7a6` | `LONG` | 2,280,418.43 USD | `1,025.37` | `2737.51` | `2225.70` | `882.10` | -526,541.51 USD | `-23.09%` | `10X Cross` |
| `988` | `0x0a97...347d` | `LONG` | 2,266,943.33 USD | `1,018.26` | `2259.32` | `2225.70` | `1429.35` | -33,628.10 USD | `-1.48%` | `20X Cross` |
| `996` | `0x001a...fef6` | `SHORT` | 2,242,607.65 USD | `1,007.33` | `2022.19` | `2225.70` | `3084.26` | -205,599.69 USD | `-9.17%` | `10X Cross` |
| `998` | `0x02aa...1806` | `SHORT` | 2,239,992.04 USD | `1,007.10` | `2654.68` | `2225.70` | `3612.74` | 433,540.06 USD | `+19.35%` | `20X Cross` |
| `1000` | `0xdb3a...cf3b` | `LONG` | 2,233,257.13 USD | `1,003.22` | `2705.01` | `2225.70` | `0.000000` | -480,449.76 USD | `-21.51%` | `4X Cross` |
| `1004` | `0x6463...42f5` | `SHORT` | 2,226,600.00 USD | `1,000.00` | `2223.43` | `2225.70` | `3745.12` | -3,165.05 USD | `-0.14%` | `5X Cross` |
| `1005` | `0x5272...fcd9` | `SHORT` | 2,226,300.00 USD | `1,000.00` | `2241.82` | `2225.70` | `2830.79` | 15,524.49 USD | `+0.70%` | `5X Cross` |
| `1006` | `0x8c02...b73f` | `SHORT` | 2,223,800.00 USD | `1,000.00` | `2250.37` | `2225.70` | `8098.42` | 26,571.47 USD | `+1.19%` | `20X Cross` |
| `1008` | `0xd7b8...9f55` | `LONG` | 2,221,875.90 USD | `999.00` | `2195.00` | `2225.70` | `0.000000` | 29,070.90 USD | `+1.31%` | `15X Cross` |
| `1039` | `0xb002...ed8a` | `SHORT` | 2,141,231.62 USD | `962.78` | `2299.66` | `2225.70` | `4197.81` | 72,846.29 USD | `+3.40%` | `25X Cross` |
| `1060` | `0xb1ec...e86a` | `SHORT` | 2,076,411.80 USD | `933.64` | `2272.72` | `2225.70` | `12583.98` | 45,495.16 USD | `+2.19%` | `25X Cross` |
| `1065` | `0xb812...b5e0` | `LONG` | 2,065,191.23 USD | `928.30` | `2263.21` | `2225.70` | `1167.18` | -35,752.99 USD | `-1.73%` | `25X Cross` |
| `1081` | `0xede2...f971` | `LONG` | 2,033,979.14 USD | `914.31` | `2208.16` | `2225.70` | `1463.01` | 15,022.15 USD | `+0.74%` | `5X Cross` |
| `1082` | `0x9606...4e5d` | `SHORT` | 2,033,700.15 USD | `913.00` | `2478.70` | `2225.70` | `4296.76` | 229,353.46 USD | `+11.28%` | `20X Cross` |
| `1103` | `0x5f10...d49d` | `LONG` | 2,003,670.00 USD | `900.00` | `2249.83` | `2225.70` | `1809.88` | -21,183.47 USD | `-1.06%` | `25X Cross` |
| `1118` | `0x51f6...2b39` | `LONG` | 1,981,735.38 USD | `890.15` | `2226.49` | `2225.70` | `761.89` | -171.51 USD | `-0.01%` | `25X Cross` |
| `1128` | `0x31de...13f2` | `LONG` | 1,962,450.73 USD | `881.52` | `2236.57` | `2225.70` | `0.000000` | -9,142.96 USD | `-0.47%` | `20X Cross` |
| `1187` | `0x2828...93a0` | `LONG` | 1,870,381.38 USD | `839.60` | `2242.41` | `2225.70` | `2192.56` | -12,350.82 USD | `-0.66%` | `25X Cross` |
| `1193` | `0xcd27...52a8` | `LONG` | 1,862,118.70 USD | `837.21` | `2553.56` | `2225.70` | `1403.25` | -275,746.07 USD | `-14.81%` | `2X Cross` |
| `1254` | `0x7737...bf66` | `SHORT` | 1,781,536.46 USD | `799.79` | `2494.83` | `2225.70` | `24936.59` | 213,809.57 USD | `+12.00%` | `15X Cross` |
| `1255` | `0x04a9...95aa` | `LONG` | 1,779,360.00 USD | `800.00` | `2595.13` | `2225.70` | `1875.81` | -296,746.74 USD | `-16.68%` | `5X Cross` |
| `1268` | `0xf910...0a2d` | `LONG` | 1,752,798.57 USD | `787.35` | `2230.44` | `2225.70` | `0.000000` | -3,338.45 USD | `-0.19%` | `5X Cross` |
| `1286` | `0x458d...ab3b` | `LONG` | 1,723,037.33 USD | `774.75` | `2740.41` | `2225.70` | `1887.00` | -400,091.86 USD | `-23.22%` | `3X Isolated` |
| `1338` | `0xaa53...9cb7` | `LONG` | 1,625,948.60 USD | `730.34` | `2389.70` | `2225.70` | `1938.13` | -119,341.04 USD | `-7.34%` | `20X Cross` |
| `1339` | `0x3fc5...c0c1` | `SHORT` | 1,623,205.44 USD | `729.92` | `2702.11` | `2225.70` | `4693.40` | 349,136.76 USD | `+21.51%` | `25X Cross` |
| `1354` | `0xa189...94d7` | `SHORT` | 1,602,889.25 USD | `719.98` | `2691.84` | `2225.70` | `2914.88` | 335,183.41 USD | `+20.91%` | `25X Cross` |
| `1373` | `0x2f93...4404` | `LONG` | 1,573,628.86 USD | `707.47` | `1700.45` | `2225.70` | `1368.63` | 370,602.48 USD | `+23.55%` | `4X Isolated` |
| `1384` | `0x5605...fe0f` | `SHORT` | 1,562,058.87 USD | `702.14` | `2566.90` | `2225.70` | `3089.14` | 240,273.78 USD | `+15.38%` | `20X Cross` |
| `1402` | `0x0deb...0bc5` | `LONG` | 1,558,410.00 USD | `700.00` | `2071.05` | `2225.70` | `1597.22` | 108,674.21 USD | `+6.97%` | `20X Cross` |
| `1403` | `0x7743...e4fe` | `SHORT` | 1,558,177.10 USD | `700.56` | `2298.56` | `2225.70` | `6178.16` | 52,097.99 USD | `+3.34%` | `25X Cross` |
| `1407` | `0x26e6...6b28` | `LONG` | 1,556,660.00 USD | `700.00` | `1835.24` | `2225.70` | `2043.06` | 271,988.47 USD | `+17.47%` | `20X Cross` |
| `1448` | `0xdbd1...29dd` | `SHORT` | 1,514,971.48 USD | `680.70` | `3030.57` | `2225.70` | `3783.88` | 547,949.64 USD | `+36.17%` | `6X Cross` |
| `1450` | `0x248e...6be2` | `SHORT` | 1,514,520.72 USD | `680.93` | `2282.89` | `2226.20` | `3393.74` | 39,964.94 USD | `+2.64%` | `20X Cross` |
| `1454` | `0x71e5...be04` | `LONG` | 1,508,689.60 USD | `677.67` | `2727.27` | `2226.20` | `1470.78` | -339,496.01 USD | `-22.50%` | `20X Cross` |
| `1461` | `0x0b23...f37b` | `LONG` | 1,501,335.00 USD | `675.00` | `2238.15` | `2226.20` | `594.78` | -9,421.64 USD | `-0.63%` | `5X Cross` |
| `1466` | `0x4e23...20c3` | `SHORT` | 1,495,829.96 USD | `672.49` | `2230.51` | `2226.20` | `21301.96` | 4,182.82 USD | `+0.28%` | `20X Cross` |
| `1475` | `0xaa7a...af37` | `LONG` | 1,478,542.60 USD | `664.13` | `2228.83` | `2226.20` | `0.000000` | -1,681.56 USD | `-0.11%` | `20X Cross` |
| `1485` | `0x0cac...6170` | `SHORT` | 1,463,529.25 USD | `657.50` | `2146.55` | `2226.20` | `2839.23` | -52,167.05 USD | `-3.56%` | `20X Cross` |
| `1513` | `0xf00e...fe3d` | `SHORT` | 1,431,179.46 USD | `642.88` | `2333.21` | `2226.20` | `2470.11` | 68,798.51 USD | `+4.81%` | `20X Cross` |
| `1517` | `0xb15b...dbae` | `SHORT` | 1,429,495.53 USD | `642.64` | `2290.80` | `2226.20` | `2311.50` | 42,671.94 USD | `+2.99%` | `25X Cross` |
| `1522` | `0xffb2...5ed6` | `SHORT` | 1,425,193.52 USD | `640.77` | `2672.96` | `2226.20` | `2498.17` | 287,554.83 USD | `+20.18%` | `20X Cross` |
| `1523` | `0xaf9f...a4fa` | `LONG` | 1,424,587.23 USD | `639.92` | `2226.44` | `2226.20` | `0.000000` | -158.95 USD | `-0.01%` | `20X Cross` |
| `1535` | `0x8505...1821` | `SHORT` | 1,411,259.02 USD | `633.96` | `2239.93` | `2226.20` | `3889.50` | 8,772.58 USD | `+0.62%` | `20X Cross` |
| `1558` | `0xfce0...f4c0` | `SHORT` | 1,386,761.68 USD | `623.60` | `3129.61` | `2226.20` | `2807.83` | 564,864.91 USD | `+40.73%` | `20X Cross` |
| `1588` | `0x2e30...4cb5` | `SHORT` | 1,363,731.64 USD | `612.56` | `2316.84` | `2226.20` | `10432.16` | 55,461.30 USD | `+4.07%` | `2X Cross` |
| `1606` | `0xad02...eb65` | `LONG` | 1,337,040.63 USD | `600.62` | `2460.69` | `2226.20` | `1078.70` | -140,899.93 USD | `-10.54%` | `5X Cross` |
| `1607` | `0x7050...5fff` | `SHORT` | 1,336,617.97 USD | `601.11` | `2245.52` | `2226.20` | `3266.31` | 13,182.14 USD | `+0.99%` | `25X Cross` |
| `1609` | `0x24fb...ed0f` | `LONG` | 1,335,873.71 USD | `600.10` | `2199.85` | `2226.20` | `0.000000` | 15,750.27 USD | `+1.18%` | `15X Cross` |
| `1610` | `0x638f...f5f0` | `LONG` | 1,335,540.00 USD | `600.00` | `4011.50` | `2226.20` | `391.49` | -1,071,363.53 USD | `-80.22%` | `25X Cross` |
| `1688` | `0xfc66...ca06` | `SHORT` | 1,262,084.26 USD | `567.43` | `2275.19` | `2226.20` | `7325.63` | 28,938.95 USD | `+2.29%` | `20X Cross` |
| `1690` | `0x9362...7d7c` | `SHORT` | 1,261,106.94 USD | `566.99` | `2226.19` | `2226.20` | `2518.69` | 1,128.88 USD | `+0.09%` | `20X Cross` |
| `1697` | `0xfb99...37f3` | `LONG` | 1,257,205.54 USD | `565.34` | `2362.35` | `2226.20` | `1250.33` | -78,330.82 USD | `-6.23%` | `3X Cross` |
| `1708` | `0x844b...7f42` | `SHORT` | 1,247,776.20 USD | `561.00` | `2026.17` | `2226.20` | `3027.80` | -111,092.79 USD | `-8.90%` | `25X Cross` |
| `1719` | `0xe86b...3664` | `LONG` | 1,240,812.05 USD | `557.89` | `2230.96` | `2226.20` | `0.000000` | -3,828.15 USD | `-0.31%` | `25X Cross` |
| `1722` | `0xabe6...1d99` | `SHORT` | 1,237,776.10 USD | `556.00` | `2484.68` | `2226.20` | `3115.63` | 143,719.78 USD | `+11.61%` | `20X Cross` |
| `1726` | `0x2a76...9a53` | `LONG` | 1,235,552.28 USD | `555.03` | `2231.40` | `2226.20` | `0.000000` | -2,943.82 USD | `-0.24%` | `25X Cross` |
| `1730` | `0xbef3...0d3e` | `LONG` | 1,228,375.25 USD | `552.33` | `2233.44` | `2226.20` | `2068.66` | -5,215.57 USD | `-0.42%` | `20X Cross` |
| `1731` | `0x6a41...a3b9` | `LONG` | 1,226,008.27 USD | `550.69` | `2233.05` | `2226.20` | `2074.11` | -3,718.08 USD | `-0.30%` | `20X Cross` |
| `1732` | `0x825c...465e` | `LONG` | 1,223,365.00 USD | `550.00` | `2208.12` | `2226.20` | `1189.29` | 8,895.50 USD | `+0.73%` | `4X Cross` |
| `1742` | `0xad21...fb6a` | `LONG` | 1,218,465.26 USD | `547.26` | `2565.80` | `2226.20` | `1730.94` | -185,687.74 USD | `-15.24%` | `6X Cross` |
| `1775` | `0xd4c1...3d1d` | `LONG` | 1,176,274.29 USD | `528.35` | `2242.60` | `2226.20` | `0.000000` | -8,617.04 USD | `-0.73%` | `12X Cross` |
| `1814` | `0x6dae...90de` | `SHORT` | 1,149,927.65 USD | `517.05` | `2292.28` | `2226.20` | `3844.63` | 35,305.77 USD | `+3.07%` | `25X Cross` |
| `1841` | `0x0089...2410` | `SHORT` | 1,129,503.51 USD | `507.35` | `2308.88` | `2226.20` | `3376.35` | 41,896.75 USD | `+3.71%` | `20X Cross` |
| `1856` | `0x020c...5872` | `LONG` | 1,113,150.00 USD | `500.00` | `2226.52` | `2226.20` | `1797.56` | -110.72 USD | `-0.01%` | `25X Cross` |
| `1857` | `0xb322...d51f` | `SHORT` | 1,113,100.00 USD | `500.00` | `2268.03` | `2226.20` | `3754.41` | 20,916.32 USD | `+1.88%` | `20X Cross` |
| `1858` | `0xe282...df29` | `LONG` | 1,113,050.00 USD | `500.00` | `2309.84` | `2226.20` | `2045.14` | -41,874.21 USD | `-3.76%` | `10X Isolated` |
| `1860` | `0x89b2...9ca6` | `LONG` | 1,112,350.00 USD | `500.00` | `2363.45` | `2226.20` | `1622.48` | -69,377.42 USD | `-6.24%` | `25X Cross` |
| `1861` | `0xa559...ff95` | `LONG` | 1,112,000.00 USD | `500.00` | `2260.68` | `2226.20` | `1058.29` | -18,344.36 USD | `-1.65%` | `20X Cross` |
| `1862` | `0x6936...9417` | `SHORT` | 1,111,900.00 USD | `500.00` | `2315.11` | `2226.20` | `2358.74` | 45,655.21 USD | `+4.11%` | `25X Isolated` |
| `1863` | `0x4044...794c` | `LONG` | 1,111,900.00 USD | `500.00` | `2260.80` | `2226.20` | `0.000000` | -18,500.00 USD | `-1.66%` | `25X Cross` |
| `1867` | `0x7298...7d6c` | `SHORT` | 1,107,884.04 USD | `498.15` | `3426.75` | `2226.20` | `5421.45` | 599,151.78 USD | `+54.08%` | `20X Cross` |
| `1878` | `0x9c68...7783` | `SHORT` | 1,097,116.55 USD | `493.31` | `2273.58` | `2226.20` | `3928.89` | 24,462.70 USD | `+2.23%` | `25X Cross` |
| `1884` | `0x404c...5f03` | `SHORT` | 1,089,625.36 USD | `489.79` | `2671.94` | `2226.20` | `5007.13` | 219,054.20 USD | `+20.10%` | `20X Cross` |
| `1890` | `0x321f...1c84` | `SHORT` | 1,085,541.46 USD | `488.02` | `2370.09` | `2226.20` | `3059.65` | 71,103.14 USD | `+6.55%` | `10X Cross` |
| `1893` | `0x94b6...e5b3` | `SHORT` | 1,081,900.03 USD | `486.05` | `2260.75` | `2226.20` | `2366.69` | 16,942.57 USD | `+1.57%` | `25X Cross` |
| `1964` | `0x82c6...fe42` | `LONG` | 1,028,507.50 USD | `462.50` | `2501.38` | `2226.20` | `2053.48` | -128,383.07 USD | `-12.48%` | `5X Isolated` |
| `1968` | `0xe330...77a1` | `SHORT` | 1,025,803.26 USD | `461.20` | `2206.97` | `2226.20` | `6440.63` | -7,945.90 USD | `-0.77%` | `20X Cross` |
| `1969` | `0x2de3...486d` | `LONG` | 1,024,988.52 USD | `460.40` | `2286.27` | `2226.20` | `1141.86` | -27,612.39 USD | `-2.69%` | `25X Cross` |
| `1973` | `0xd6e1...f256` | `LONG` | 1,021,067.34 USD | `458.64` | `2213.70` | `2226.20` | `914.93` | 5,776.45 USD | `+0.57%` | `25X Cross` |
| `1976` | `0x617e...0f97` | `SHORT` | 1,019,321.25 USD | `457.85` | `2205.60` | `2226.20` | `3358.94` | -9,477.42 USD | `-0.93%` | `10X Cross` |
| `2011` | `0xae55...2236` | `LONG` | 1,001,835.00 USD | `450.00` | `2510.21` | `2226.20` | `0.000000` | -127,762.50 USD | `-12.75%` | `25X Cross` |
| `2017` | `0xc10f...23b3` | `LONG` | 1,000,980.00 USD | `450.00` | `2366.44` | `2226.20` | `2016.55` | -63,918.27 USD | `-6.39%` | `25X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `2315.00` | 57,104.11 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 57.10K USD at 2315.0000 USD [API] | `2026-10-29 08:09:24` |
| `ANNOUNCEMENT` | `INFO` | `2315.00` | 57,875.00 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 57.88K USD at 2315.0000 USD [API] | `2026-10-29 08:09:24` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 1,111.06 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.11K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 604.10 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.60K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 5,519.08 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 5.52K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 30.46 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.03K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 1,346.20 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 1.35K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 13.61 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.01K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 7,119.10 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 7.12K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 248.52 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.25K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 543.19 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.54K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 92.07 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.09K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 393.43 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.39K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 490.81 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.49K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 342.66 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.34K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 216.44 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.22K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 6,097.80 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 6.10K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2307.50` | 12.46 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Short: 0.01K USD at 2307.5000 USD [API] | `2026-10-29 02:00:09` |
| `ANNOUNCEMENT` | `INFO` | `2387.80` | 98,170.58 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 98.17K USD at 2387.8000 USD [API] | `2026-10-28 20:01:45` |
| `ANNOUNCEMENT` | `INFO` | `2387.80` | 1,284.40 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.28K USD at 2387.8000 USD [API] | `2026-10-28 20:01:45` |
| `ANNOUNCEMENT` | `INFO` | `2378.30` | 28.30 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 0.03K USD at 2378.3000 USD [API] | `2026-10-28 20:00:38` |
| `ANNOUNCEMENT` | `INFO` | `2357.90` | 14,633.13 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 14.63K USD at 2357.9000 USD [API] | `2026-10-27 21:33:15` |
| `ANNOUNCEMENT` | `INFO` | `2357.90` | 88,980.78 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 88.98K USD at 2357.9000 USD [API] | `2026-10-27 21:33:15` |
| `ANNOUNCEMENT` | `INFO` | `2346.30` | 150,235.94 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 150.24K USD at 2346.3000 USD [API] | `2026-10-27 15:21:36` |
| `ANNOUNCEMENT` | `INFO` | `2316.50` | 40,585.08 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 40.59K USD at 2316.5000 USD [API] | `2026-10-29 08:13:10` |
| `ANNOUNCEMENT` | `INFO` | `2387.90` | 3,129.82 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 3.13K USD at 2387.9000 USD [API] | `2026-10-28 20:01:45` |
| `ANNOUNCEMENT` | `INFO` | `2377.80` | 1,657.80 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 1.66K USD at 2377.8000 USD [API] | `2026-10-28 20:00:18` |
| `ANNOUNCEMENT` | `INFO` | `2316.30` | 60,000.74 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale BUY: 60.00K USD at 2316.3000 USD [API] | `2026-10-29 08:16:55` |
| `ANNOUNCEMENT` | `INFO` | `2318.80` | 88,465.47 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 88.47K USD at 2318.8000 USD [API] | `2026-10-29 08:19:47` |
| `ANNOUNCEMENT` | `INFO` | `2377.40` | 405,605.84 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 405.61K USD at 2377.4000 USD [API] | `2026-10-28 20:00:18` |
| `ANNOUNCEMENT` | `INFO` | `2324.50` | 107,890.51 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 107.89K USD at 2324.5000 USD [API] | `2026-10-29 09:09:58` |
| `ANNOUNCEMENT` | `INFO` | `2425.50` | 2,443.69 USD | `-` | `NEWS_INTEL` | `-` | #ETH Liquidated Long: 2.44K USD at 2425.5000 USD [API] | `2026-10-16 16:02:42` |
| `ANNOUNCEMENT` | `INFO` | `2320.30` | 86,616.33 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 86.62K USD at 2320.3000 USD [API] | `2026-10-29 09:28:28` |
| `ANNOUNCEMENT` | `INFO` | `2318.30` | 115,915.00 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 115.92K USD at 2318.3000 USD [API] | `2026-10-29 09:30:17` |
| `ANNOUNCEMENT` | `INFO` | `2319.20` | 55,554.81 USD | `-` | `NEWS_INTEL` | `-` | #ETH Whale SELL: 55.55K USD at 2319.2000 USD [API] | `2026-10-29 09:42:18` |
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


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`2275.30` (Vol: 31,100,000.00 USD, Dist: `+1.89%`) | Long MP=`2174.37` (Vol: 35,800,000.00 USD, Dist: `--2.63%`)
  * 48H Horizon: Short MP=`2270.12` (Vol: 33,600,000.00 USD, Dist: `+1.66%`) | Long MP=`2174.00` (Vol: 35,800,000.00 USD, Dist: `--2.64%`)
  * 3D Horizon: Short MP=`2270.12` (Vol: 33,600,000.00 USD, Dist: `+1.66%`) | Long MP=`2174.00` (Vol: 35,800,000.00 USD, Dist: `--2.64%`)
  * 7D Horizon: Short MP=`2401.80` (Vol: 50,700,000.00 USD, Dist: `+7.56%`) | Long MP=`2175.27` (Vol: 44,800,000.00 USD, Dist: `--2.59%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `445.00` | 3,820.00 USD | 775,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `455.00` | 148,090.00 USD | 775,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `465.00` | 578.23 USD | 775,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `475.00` | 8,820.00 USD | 775,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.00` | 106,620.00 USD | 775,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `495.00` | 1,770,000.00 USD | 775,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.00` | 20,980.00 USD | 773,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.00` | 47,920.00 USD | 773,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.00` | 8,310.00 USD | 773,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.00` | 4,120.00 USD | 773,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.00` | 50,860.00 USD | 773,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.00` | 1,810,000.00 USD | 773,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `565.00` | 46,070.00 USD | 771,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `575.00` | 33,960.00 USD | 771,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.00` | 13,710.00 USD | 771,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.00` | 429,270.00 USD | 771,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `605.00` | 4,480,000.00 USD | 770,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.00` | 43,010.00 USD | 766,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.00` | 145,780.00 USD | 766,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.00` | 93,950.00 USD | 766,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `645.00` | 131,190.00 USD | 766,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `655.00` | 644,750.00 USD | 766,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `665.00` | 19,860.00 USD | 765,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `675.00` | 16,000.00 USD | 765,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `685.00` | 35,670.00 USD | 765,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `695.00` | 172,530.00 USD | 765,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `705.00` | 23,170.00 USD | 765,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `715.00` | 11,250.00 USD | 765,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `725.00` | 436,810.00 USD | 765,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `735.00` | 48,440.00 USD | 764,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `745.00` | 1,820.00 USD | 764,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `755.00` | 42,880.00 USD | 764,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `765.00` | 133,400.00 USD | 764,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `775.00` | 185,410.00 USD | 764,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `785.00` | 88,540.00 USD | 764,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `795.00` | 141,120.00 USD | 764,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `805.00` | 121,190.00 USD | 764,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `815.00` | 24,860.00 USD | 763,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `825.00` | 73,550.00 USD | 763,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `835.00` | 203,150.00 USD | 763,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `845.00` | 229,530.00 USD | 763,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `855.00` | 426,480.00 USD | 763,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `865.00` | 61,360.00 USD | 762,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `875.00` | 25,620.00 USD | 762,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `885.00` | 1,060,000.00 USD | 762,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `895.00` | 127,340.00 USD | 761,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `905.00` | 72,750.00 USD | 761,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `915.00` | 480,070.00 USD | 761,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `925.00` | 109,240.00 USD | 761,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `935.00` | 27,700.00 USD | 761,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `945.00` | 40,280.00 USD | 760,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `955.00` | 50,770.00 USD | 760,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `965.00` | 1,770,000.00 USD | 760,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `975.00` | 364,180.00 USD | 759,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `985.00` | 414,070.00 USD | 758,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `995.00` | 33,580.00 USD | 758,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1005.00` | 74,920.00 USD | 758,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1015.00` | 112,100.00 USD | 758,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1025.00` | 416,280.00 USD | 758,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1035.00` | 27,840.00 USD | 757,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1045.00` | 922,550.00 USD | 757,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1055.00` | 152,290.00 USD | 756,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1065.00` | 7,490,000.00 USD | 756,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1075.00` | 2,240,000.00 USD | 749,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1085.00` | 380,440.00 USD | 746,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1095.00` | 520,760.00 USD | 746,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1105.00` | 493,720.00 USD | 745,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1115.00` | 299,410.00 USD | 745,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1125.00` | 7,870,000.00 USD | 745,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1135.00` | 2,090,000.00 USD | 737,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1145.00` | 1,230,000.00 USD | 735,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1155.00` | 7,890,000.00 USD | 733,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1165.00` | 2,540,000.00 USD | 726,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1175.00` | 249,480.00 USD | 723,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1185.00` | 1,050,000.00 USD | 723,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1195.00` | 228,770.00 USD | 722,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1205.00` | 196,650.00 USD | 722,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1215.00` | 384,700.00 USD | 721,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1225.00` | 2,350,000.00 USD | 721,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1235.00` | 337,640.00 USD | 719,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1245.00` | 836,230.00 USD | 718,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1255.00` | 410,860.00 USD | 717,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1265.00` | 182,910.00 USD | 717,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1275.00` | 15,380,000.00 USD | 717,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1285.00` | 391,910.00 USD | 701,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1295.00` | 307,370.00 USD | 701,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1305.00` | 1,300,000.00 USD | 701,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1315.00` | 185,760.00 USD | 699,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1325.00` | 531,330.00 USD | 699,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1335.00` | 305,870.00 USD | 699,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1345.00` | 5,650,000.00 USD | 698,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1355.00` | 289,170.00 USD | 693,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1365.00` | 1,110,000.00 USD | 693,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1375.00` | 7,440,000.00 USD | 691,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1385.00` | 2,120,000.00 USD | 684,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1395.00` | 590,890.00 USD | 682,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1405.00` | 23,290,000.00 USD | 681,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1415.00` | 191,580.00 USD | 658,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1425.00` | 369,310.00 USD | 658,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1435.00` | 1,190,000.00 USD | 657,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1445.00` | 324,720.00 USD | 656,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1455.00` | 19,320,000.00 USD | 656,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1465.00` | 1,900,000.00 USD | 637,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1475.00` | 12,220,000.00 USD | 635,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1485.00` | 51,690.00 USD | 622,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1495.00` | 299,590.00 USD | 622,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1505.00` | 1,180,000.00 USD | 622,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1515.00` | 2,410,000.00 USD | 621,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1525.00` | 18,760,000.00 USD | 618,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1535.00` | 16,320,000.00 USD | 600,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1545.00` | 2,860,000.00 USD | 583,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1555.00` | 1,070,000.00 USD | 581,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1565.00` | 2,920,000.00 USD | 579,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1575.00` | 643,670.00 USD | 577,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1585.00` | 739,730.00 USD | 576,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1595.00` | 1,570,000.00 USD | 575,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1605.00` | 18,050,000.00 USD | 574,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1615.00` | 316,290.00 USD | 556,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1625.00` | 1,720,000.00 USD | 555,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1635.00` | 19,250,000.00 USD | 554,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1645.00` | 36,970,000.00 USD | 534,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1655.00` | 866,150.00 USD | 497,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1665.00` | 12,090,000.00 USD | 496,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1675.00` | 1,260,000.00 USD | 484,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1685.00` | 578,780.00 USD | 483,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1695.00` | 708,290.00 USD | 483,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1705.00` | 577,620.00 USD | 482,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1715.00` | 644,480.00 USD | 481,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1725.00` | 41,350,000.00 USD | 481,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1735.00` | 505,710.00 USD | 439,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1745.00` | 4,250,000.00 USD | 439,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1755.00` | 45,550,000.00 USD | 434,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1765.00` | 3,530,000.00 USD | 389,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1775.00` | 7,600,000.00 USD | 385,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1785.00` | 54,780,000.00 USD | 378,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1795.00` | 3,930,000.00 USD | 323,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1805.00` | 3,110,000.00 USD | 319,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1815.00` | 456,010.00 USD | 316,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1825.00` | 1,230,000.00 USD | 316,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1835.00` | 13,290,000.00 USD | 314,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1845.00` | 15,910,000.00 USD | 301,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1855.00` | 4,250,000.00 USD | 285,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1865.00` | 913,020.00 USD | 281,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1875.00` | 7,580,000.00 USD | 280,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1885.00` | 5,330,000.00 USD | 272,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1895.00` | 647,820.00 USD | 267,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1905.00` | 952,610.00 USD | 266,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1915.00` | 17,810,000.00 USD | 265,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1925.00` | 16,590,000.00 USD | 248,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1935.00` | 1,100,000.00 USD | 231,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1945.00` | 1,370,000.00 USD | 230,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1955.00` | 2,920,000.00 USD | 229,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1965.00` | 5,640,000.00 USD | 226,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1971.40` | 764,320,000.00 USD | 764,320,000.00 USD | 0.00 USD | 0.00 USD | 26,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1974.40` | 764,290,000.00 USD | 764,290,000.00 USD | 0.00 USD | 105,610.00 USD | 49,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1975.00` | 1,430,000.00 USD | 220,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1977.40` | 764,140,000.00 USD | 764,140,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1983.40` | 761,900,000.00 USD | 761,900,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1985.00` | 5,530,000.00 USD | 219,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1986.40` | 761,690,000.00 USD | 761,690,000.00 USD | 3,730,000.00 USD | 1,780,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1989.40` | 756,190,000.00 USD | 756,190,000.00 USD | 0.00 USD | 1,320,000.00 USD | 38,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1992.40` | 754,830,000.00 USD | 754,830,000.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1995.00` | 1,640,000.00 USD | 213,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1995.40` | 753,440,000.00 USD | 753,440,000.00 USD | 1,340,000.00 USD | 0.00 USD | 808,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2000.30` | 647,650,000.00 USD | 647,650,000.00 USD | 16,160.00 USD | 80,240.00 USD | 497,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2002.80` | 647,060,000.00 USD | 647,060,000.00 USD | 0.00 USD | 455,960.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2004.40` | 751,290,000.00 USD | 751,290,000.00 USD | 0.00 USD | 266,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2005.00` | 14,200,000.00 USD | 211,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2005.30` | 646,590,000.00 USD | 646,590,000.00 USD | 493,990.00 USD | 13,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2007.40` | 751,020,000.00 USD | 751,020,000.00 USD | 807,770.00 USD | 42,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2007.80` | 646,090,000.00 USD | 646,090,000.00 USD | 0.00 USD | 431,390.00 USD | 126,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2010.30` | 645,530,000.00 USD | 645,530,000.00 USD | 484,920.00 USD | 490,130.00 USD | 362,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2010.40` | 750,170,000.00 USD | 750,170,000.00 USD | 170,840.00 USD | 92,470.00 USD | 689,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2012.80` | 644,190,000.00 USD | 644,190,000.00 USD | 323,800.00 USD | 239,210.00 USD | 25,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2015.00` | 3,300,000.00 USD | 197,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2015.30` | 643,600,000.00 USD | 643,600,000.00 USD | 355,800.00 USD | 159,880.00 USD | 194,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2017.80` | 642,890,000.00 USD | 642,890,000.00 USD | 537,580.00 USD | 1,360,000.00 USD | 553,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2019.40` | 749,220,000.00 USD | 749,220,000.00 USD | 0.00 USD | 0.00 USD | 21,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2020.30` | 640,440,000.00 USD | 640,440,000.00 USD | 548,260.00 USD | 1,150,000.00 USD | 696,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2022.40` | 749,200,000.00 USD | 749,200,000.00 USD | 0.00 USD | 0.00 USD | 934,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2022.80` | 638,040,000.00 USD | 638,040,000.00 USD | 1,160,000.00 USD | 312,480.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2025.00` | 923,670.00 USD | 194,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2025.30` | 635,000,000.00 USD | 635,000,000.00 USD | 414,330.00 USD | 1,190,000.00 USD | 231,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2025.40` | 748,260,000.00 USD | 748,260,000.00 USD | 1,070,000.00 USD | 177,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2027.80` | 633,160,000.00 USD | 633,160,000.00 USD | 2,770,000.00 USD | 978,910.00 USD | 312,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2028.40` | 747,020,000.00 USD | 747,020,000.00 USD | 1,100,000.00 USD | 0.00 USD | 35,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2030.30` | 629,100,000.00 USD | 629,100,000.00 USD | 87,180.00 USD | 366,120.00 USD | 957,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2031.40` | 745,880,000.00 USD | 745,880,000.00 USD | 0.00 USD | 3,520,000.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2032.80` | 627,690,000.00 USD | 627,690,000.00 USD | 1,360,000.00 USD | 1,490,000.00 USD | 707,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2034.40` | 741,310,000.00 USD | 741,310,000.00 USD | 0.00 USD | 0.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2035.00` | 606,700.00 USD | 193,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2035.30` | 624,130,000.00 USD | 624,130,000.00 USD | 1,150,000.00 USD | 19,490.00 USD | 165,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2037.40` | 739,960,000.00 USD | 739,960,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2037.80` | 622,800,000.00 USD | 622,800,000.00 USD | 396,700.00 USD | 458,110.00 USD | 388,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2040.30` | 621,550,000.00 USD | 621,550,000.00 USD | 834,710.00 USD | 178,560.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2040.40` | 739,620,000.00 USD | 739,620,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2042.80` | 620,520,000.00 USD | 620,520,000.00 USD | 334,790.00 USD | 0.00 USD | 174,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2043.40` | 738,170,000.00 USD | 738,170,000.00 USD | 0.00 USD | 0.00 USD | 149,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2045.00` | 1,800,000.00 USD | 192,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2045.30` | 620,010,000.00 USD | 620,010,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2046.40` | 738,020,000.00 USD | 738,020,000.00 USD | 0.00 USD | 149,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2047.80` | 619,980,000.00 USD | 619,980,000.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2049.40` | 737,870,000.00 USD | 737,870,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2050.30` | 619,150,000.00 USD | 619,150,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2052.40` | 737,650,000.00 USD | 737,650,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2055.00` | 7,150,000.00 USD | 191,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2055.30` | 618,050,000.00 USD | 618,050,000.00 USD | 242,080.00 USD | 88,880.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2058.40` | 735,360,000.00 USD | 735,360,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2060.30` | 617,690,000.00 USD | 617,690,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2061.40` | 735,020,000.00 USD | 735,020,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2062.80` | 616,930,000.00 USD | 616,930,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2064.40` | 729,770,000.00 USD | 729,770,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 945,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2065.00` | 14,220,000.00 USD | 183,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2065.30` | 616,850,000.00 USD | 616,850,000.00 USD | 563,140.00 USD | 537,030.00 USD | 510,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2067.40` | 727,330,000.00 USD | 727,330,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 262,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2067.80` | 615,240,000.00 USD | 615,240,000.00 USD | 387,410.00 USD | 304,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2070.30` | 614,550,000.00 USD | 614,550,000.00 USD | 57,300.00 USD | 319,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2070.40` | 725,660,000.00 USD | 725,660,000.00 USD | 3,600,000.00 USD | 2,730,000.00 USD | 1,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2072.80` | 614,170,000.00 USD | 614,170,000.00 USD | 47,910.00 USD | 555,250.00 USD | 420,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2073.40` | 717,450,000.00 USD | 717,450,000.00 USD | 3,300,000.00 USD | 2,180,000.00 USD | 2,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2075.00` | 1,540,000.00 USD | 169,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2075.30` | 613,150,000.00 USD | 613,150,000.00 USD | 379,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2076.40` | 709,920,000.00 USD | 709,920,000.00 USD | 5,230,000.00 USD | 5,030,000.00 USD | 3,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2077.80` | 612,770,000.00 USD | 612,770,000.00 USD | 0.00 USD | 25,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2079.40` | 695,980,000.00 USD | 695,980,000.00 USD | 4,150,000.00 USD | 3,020,000.00 USD | 3,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2080.30` | 612,740,000.00 USD | 612,740,000.00 USD | 116,140.00 USD | 29,610.00 USD | 200,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2082.40` | 685,680,000.00 USD | 685,680,000.00 USD | 2,640,000.00 USD | 1,860,000.00 USD | 1,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2082.80` | 612,400,000.00 USD | 612,400,000.00 USD | 827,940.00 USD | 4,240.00 USD | 211,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2085.00` | 13,750,000.00 USD | 168,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2085.30` | 611,350,000.00 USD | 611,350,000.00 USD | 691,080.00 USD | 207,610.00 USD | 821,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2085.40` | 679,240,000.00 USD | 679,240,000.00 USD | 4,090,000.00 USD | 1,860,000.00 USD | 3,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2087.80` | 609,630,000.00 USD | 609,630,000.00 USD | 525,540.00 USD | 573,160.00 USD | 440,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2088.40` | 669,450,000.00 USD | 669,450,000.00 USD | 2,280,000.00 USD | 1,820,000.00 USD | 907,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2090.30` | 608,100,000.00 USD | 608,100,000.00 USD | 761,770.00 USD | 217,840.00 USD | 451,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2091.40` | 664,440,000.00 USD | 664,440,000.00 USD | 4,410,000.00 USD | 952,210.00 USD | 7,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2092.80` | 606,660,000.00 USD | 606,660,000.00 USD | 752,390.00 USD | 342,580.00 USD | 395,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2094.40` | 651,480,000.00 USD | 651,480,000.00 USD | 5,720,000.00 USD | 1,660,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2095.00` | 1,810,000.00 USD | 154,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2095.30` | 605,170,000.00 USD | 605,170,000.00 USD | 1,840,000.00 USD | 1,130,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2097.40` | 641,760,000.00 USD | 641,760,000.00 USD | 1,830,000.00 USD | 3,580,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2097.80` | 600,510,000.00 USD | 600,510,000.00 USD | 187,470.00 USD | 488,160.00 USD | 309,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2100.30` | 599,520,000.00 USD | 599,520,000.00 USD | 295,710.00 USD | 928,890.00 USD | 50,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2100.40` | 635,060,000.00 USD | 635,060,000.00 USD | 1,830,000.00 USD | 1,850,000.00 USD | 3,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2102.80` | 598,240,000.00 USD | 598,240,000.00 USD | 211,840.00 USD | 222,480.00 USD | 483,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2103.40` | 628,070,000.00 USD | 628,070,000.00 USD | 679,880.00 USD | 554,710.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2105.00` | 2,320,000.00 USD | 152,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2105.30` | 597,330,000.00 USD | 597,330,000.00 USD | 3,570,000.00 USD | 1,160,000.00 USD | 833,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2106.40` | 624,580,000.00 USD | 624,580,000.00 USD | 1,660,000.00 USD | 986,590.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2107.80` | 591,760,000.00 USD | 591,760,000.00 USD | 734,860.00 USD | 0.00 USD | 347,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2109.40` | 619,980,000.00 USD | 619,980,000.00 USD | 8,310,000.00 USD | 1,830,000.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2110.30` | 590,680,000.00 USD | 590,680,000.00 USD | 61,010.00 USD | 31,550.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2112.40` | 608,080,000.00 USD | 608,080,000.00 USD | 3,920,000.00 USD | 1,480,000.00 USD | 3,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2112.80` | 590,580,000.00 USD | 590,580,000.00 USD | 902,600.00 USD | 506,690.00 USD | 244,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2115.00` | 1,970,000.00 USD | 150,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2115.30` | 588,930,000.00 USD | 588,930,000.00 USD | 410,020.00 USD | 400,200.00 USD | 939,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2115.40` | 598,960,000.00 USD | 598,960,000.00 USD | 923,330.00 USD | 3,210,000.00 USD | 1,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2117.80` | 587,180,000.00 USD | 587,180,000.00 USD | 4,540,000.00 USD | 3,940,000.00 USD | 302,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2118.40` | 592,890,000.00 USD | 592,890,000.00 USD | 8,390,000.00 USD | 639,610.00 USD | 2,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2120.30` | 578,390,000.00 USD | 578,390,000.00 USD | 5,430,000.00 USD | 325,610.00 USD | 671,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2121.40` | 581,020,000.00 USD | 581,020,000.00 USD | 8,120,000.00 USD | 5,720,000.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2122.80` | 571,960,000.00 USD | 571,960,000.00 USD | 4,680,000.00 USD | 3,490,000.00 USD | 2,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2124.40` | 565,520,000.00 USD | 565,520,000.00 USD | 7,730,000.00 USD | 8,120,000.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2125.00` | 123,220,000.00 USD | 148,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2125.30` | 561,710,000.00 USD | 561,710,000.00 USD | 5,280,000.00 USD | 1,830,000.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2127.40` | 548,120,000.00 USD | 548,120,000.00 USD | 1,600,000.00 USD | 4,460,000.00 USD | 5,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2127.80` | 552,720,000.00 USD | 552,720,000.00 USD | 4,430,000.00 USD | 4,330,000.00 USD | 782,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2130.30` | 543,170,000.00 USD | 543,170,000.00 USD | 1,230,000.00 USD | 18,610.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2130.40` | 536,760,000.00 USD | 536,760,000.00 USD | 5,390,000.00 USD | 2,130,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2132.80` | 540,820,000.00 USD | 540,820,000.00 USD | 0.00 USD | 177,810.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2133.40` | 527,540,000.00 USD | 527,540,000.00 USD | 2,120,000.00 USD | 715,940.00 USD | 323,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2135.00` | 5,550,000.00 USD | 25,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2135.30` | 539,390,000.00 USD | 539,390,000.00 USD | 41,690.00 USD | 1,170,000.00 USD | 43,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2136.40` | 524,380,000.00 USD | 524,380,000.00 USD | 1,170,000.00 USD | 845,110.00 USD | 43,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2137.80` | 538,140,000.00 USD | 538,140,000.00 USD | 17,770.00 USD | 1,040,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2139.40` | 522,320,000.00 USD | 522,320,000.00 USD | 1,110,000.00 USD | 1,780,000.00 USD | 409,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2140.30` | 537,080,000.00 USD | 537,080,000.00 USD | 1,370,000.00 USD | 945,770.00 USD | 64,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2142.40` | 519,030,000.00 USD | 519,030,000.00 USD | 4,320,000.00 USD | 1,100,000.00 USD | 661,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2142.80` | 534,700,000.00 USD | 534,700,000.00 USD | 1,080,000.00 USD | 2,500,000.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2145.00` | 1,600,000.00 USD | 19,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2145.30` | 530,080,000.00 USD | 530,080,000.00 USD | 2,870,000.00 USD | 2,390,000.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2145.40` | 512,950,000.00 USD | 512,950,000.00 USD | 2,210,000.00 USD | 1,760,000.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2147.80` | 523,790,000.00 USD | 523,790,000.00 USD | 1,040,000.00 USD | 1,140,000.00 USD | 79,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2148.40` | 507,250,000.00 USD | 507,250,000.00 USD | 26,270.00 USD | 538,910.00 USD | 152,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2150.30` | 521,530,000.00 USD | 521,530,000.00 USD | 7,580,000.00 USD | 3,090,000.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2151.40` | 506,540,000.00 USD | 506,540,000.00 USD | 11,200,000.00 USD | 363,770.00 USD | 354,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2152.80` | 508,210,000.00 USD | 508,210,000.00 USD | 2,710,000.00 USD | 2,710,000.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2154.40` | 494,620,000.00 USD | 494,620,000.00 USD | 48,150.00 USD | 2,020,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2155.00` | 2,930,000.00 USD | 17,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2155.30` | 500,550,000.00 USD | 500,550,000.00 USD | 2,740,000.00 USD | 3,890,000.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2157.40` | 490,970,000.00 USD | 490,970,000.00 USD | 6,950,000.00 USD | 1,330,000.00 USD | 5,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2157.80` | 491,540,000.00 USD | 491,540,000.00 USD | 3,400,000.00 USD | 1,640,000.00 USD | 3,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2160.30` | 482,810,000.00 USD | 482,810,000.00 USD | 5,200,000.00 USD | 6,510,000.00 USD | 2,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2160.40` | 477,640,000.00 USD | 477,640,000.00 USD | 397,220.00 USD | 767,490.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2162.80` | 468,190,000.00 USD | 468,190,000.00 USD | 17,840,000.00 USD | 10,480,000.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2163.40` | 474,610,000.00 USD | 474,610,000.00 USD | 26,080,000.00 USD | 10,840,000.00 USD | 131,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2165.00` | 5,980,000.00 USD | 14,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2165.30` | 437,910,000.00 USD | 437,910,000.00 USD | 10,250,000.00 USD | 9,180,000.00 USD | 5,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2166.40` | 437,560,000.00 USD | 437,560,000.00 USD | 5,300,000.00 USD | 14,900,000.00 USD | 2,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2167.80` | 413,420,000.00 USD | 413,420,000.00 USD | 18,870,000.00 USD | 9,790,000.00 USD | 5,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2169.40` | 414,500,000.00 USD | 414,500,000.00 USD | 8,360,000.00 USD | 14,630,000.00 USD | 4,800,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2170.30` | 379,620,000.00 USD | 379,620,000.00 USD | 23,930,000.00 USD | 8,680,000.00 USD | 7,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2172.40` | 386,710,000.00 USD | 386,710,000.00 USD | 8,830,000.00 USD | 1,650,000.00 USD | 4,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2172.80` | 339,610,000.00 USD | 339,610,000.00 USD | 7,120,000.00 USD | 3,860,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2175.00` | 5,790,000.00 USD | 9,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2175.30` | 325,170,000.00 USD | 325,170,000.00 USD | 3,540,000.00 USD | 0.00 USD | 836,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2175.40` | 371,700,000.00 USD | 371,700,000.00 USD | 28,130,000.00 USD | 1,330,000.00 USD | 3,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2177.80` | 320,800,000.00 USD | 320,800,000.00 USD | 730,100.00 USD | 355,620.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2180.30` | 316,890,000.00 USD | 316,890,000.00 USD | 894,580.00 USD | 1,550,000.00 USD | 1,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2181.40` | 338,420,000.00 USD | 338,420,000.00 USD | 1,760,000.00 USD | 0.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2182.80` | 313,030,000.00 USD | 313,030,000.00 USD | 169,090.00 USD | 1,320,000.00 USD | 3,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2184.40` | 335,260,000.00 USD | 335,260,000.00 USD | 26,960,000.00 USD | 2,700,000.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2185.00` | 574,460.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2185.30` | 308,510,000.00 USD | 308,510,000.00 USD | 2,650,000.00 USD | 1,800,000.00 USD | 5,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2187.40` | 303,050,000.00 USD | 303,050,000.00 USD | 14,380,000.00 USD | 17,750,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2187.80` | 298,440,000.00 USD | 298,440,000.00 USD | 5,040,000.00 USD | 4,100,000.00 USD | 7,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2190.30` | 281,370,000.00 USD | 281,370,000.00 USD | 8,990,000.00 USD | 4,390,000.00 USD | 4,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2190.40` | 270,920,000.00 USD | 270,920,000.00 USD | 14,800,000.00 USD | 27,960,000.00 USD | 8,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2192.80` | 263,960,000.00 USD | 263,960,000.00 USD | 5,000,000.00 USD | 5,400,000.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2193.40` | 220,130,000.00 USD | 220,130,000.00 USD | 0.00 USD | 7,340,000.00 USD | 8,120,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2195.00` | 1,990,000.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2195.30` | 252,370,000.00 USD | 252,370,000.00 USD | 6,640,000.00 USD | 2,370,000.00 USD | 5,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2196.40` | 204,670,000.00 USD | 204,670,000.00 USD | 383,690.00 USD | 243,760.00 USD | 109,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2197.80` | 237,410,000.00 USD | 237,410,000.00 USD | 3,630,000.00 USD | 1,780,000.00 USD | 4,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2199.40` | 203,940,000.00 USD | 203,940,000.00 USD | 0.00 USD | 1,190,000.00 USD | 7,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2200.30` | 227,510,000.00 USD | 227,510,000.00 USD | 6,260,000.00 USD | 4,750,000.00 USD | 9,470,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2202.40` | 195,310,000.00 USD | 195,310,000.00 USD | 9,660,000.00 USD | 0.00 USD | 12,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2202.80` | 207,030,000.00 USD | 207,030,000.00 USD | 5,760,000.00 USD | 5,460,000.00 USD | 5,630,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2205.00` | 663,550.00 USD | 664,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2205.30` | 190,180,000.00 USD | 190,180,000.00 USD | 6,220,000.00 USD | 3,940,000.00 USD | 2,870,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2205.40` | 173,310,000.00 USD | 173,310,000.00 USD | 0.00 USD | 429,830.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2207.80` | 177,150,000.00 USD | 177,150,000.00 USD | 11,640,000.00 USD | 4,990,000.00 USD | 2,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2208.40` | 169,500,000.00 USD | 169,500,000.00 USD | 19,630,000.00 USD | 2,960,000.00 USD | 5,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2210.30` | 158,470,000.00 USD | 158,470,000.00 USD | 8,640,000.00 USD | 5,850,000.00 USD | 6,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2211.40` | 141,370,000.00 USD | 141,370,000.00 USD | 6,450,000.00 USD | 0.00 USD | 17,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2212.80` | 137,690,000.00 USD | 137,690,000.00 USD | 8,240,000.00 USD | 6,700,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2214.40` | 117,620,000.00 USD | 117,620,000.00 USD | 0.00 USD | 1,980,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2215.00` | 412.88 USD | 628.26 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2215.30` | 120,760,000.00 USD | 120,760,000.00 USD | 2,150,000.00 USD | 3,720,000.00 USD | 736,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2217.40` | 115,640,000.00 USD | 115,640,000.00 USD | 22,400,000.00 USD | 487,520.00 USD | 565,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2217.80` | 114,150,000.00 USD | 114,150,000.00 USD | 2,630,000.00 USD | 2,470,000.00 USD | 3,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2220.30` | 105,730,000.00 USD | 105,730,000.00 USD | 6,700,000.00 USD | 2,140,000.00 USD | 3,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2220.40` | 92,190,000.00 USD | 92,190,000.00 USD | 308,930.00 USD | 4,700,000.00 USD | 6,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2222.80` | 93,370,000.00 USD | 93,370,000.00 USD | 12,630,000.00 USD | 9,400,000.00 USD | 8,940,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2223.40` | 80,300,000.00 USD | 80,300,000.00 USD | 9,270,000.00 USD | 14,350,000.00 USD | 24,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `2225.00` | 215.38 USD | 215.38 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `2225.30` | 62,400,000.00 USD | 62,400,000.00 USD | 18,130,000.00 USD | 1,920,000.00 USD | 13,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `2226.40` | 32,330,000.00 USD | 32,330,000.00 USD | 820,020.00 USD | 6,650,000.00 USD | 24,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `2227.80` | 28,460,000.00 USD | 28,460,000.00 USD | 3,850,000.00 USD | 18,120,000.00 USD | 6,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2229.40` | 23,170,000.00 USD | 23,170,000.00 USD | 2,140,000.00 USD | 0.00 USD | 21,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2229.40` | 46,350,000.00 USD | 46,350,000.00 USD | 2,140,000.00 USD | 0.00 USD | 21,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2230.30` | 33,100,000.00 USD | 33,100,000.00 USD | 31,830,000.00 USD | 1,030,000.00 USD | 241,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2232.40` | 48,260,000.00 USD | 48,260,000.00 USD | 0.00 USD | 0.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2232.80` | 49,890,000.00 USD | 49,890,000.00 USD | 16,510,000.00 USD | 0.00 USD | 282,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2235.00` | 497.96 USD | 497.96 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2235.40` | 73,510,000.00 USD | 73,510,000.00 USD | 3,260,000.00 USD | 21,640,000.00 USD | 350,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2237.80` | 57,890,000.00 USD | 57,890,000.00 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2238.40` | 87,540,000.00 USD | 87,540,000.00 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2240.30` | 65,100,000.00 USD | 65,100,000.00 USD | 7,220,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2241.40` | 119,940,000.00 USD | 119,940,000.00 USD | 32,390,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2242.80` | 65,300,000.00 USD | 65,300,000.00 USD | 0.00 USD | 141,810.00 USD | 50,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2244.40` | 121,410,000.00 USD | 121,410,000.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2245.30` | 65,340,000.00 USD | 65,340,000.00 USD | 0.00 USD | 0.00 USD | 45,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2247.40` | 125,230,000.00 USD | 125,230,000.00 USD | 1,670,000.00 USD | 1,030,000.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2247.80` | 67,990,000.00 USD | 67,990,000.00 USD | 0.00 USD | 2,580,000.00 USD | 70,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2250.30` | 73,970,000.00 USD | 73,970,000.00 USD | 5,560,000.00 USD | 365,980.00 USD | 55,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2250.40` | 132,210,000.00 USD | 132,210,000.00 USD | 3,660,000.00 USD | 3,090,000.00 USD | 228,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2252.80` | 76,070,000.00 USD | 76,070,000.00 USD | 155,320.00 USD | 497,910.00 USD | 1,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2253.40` | 153,780,000.00 USD | 153,780,000.00 USD | 10,110,000.00 USD | 11,240,000.00 USD | 216,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2255.00` | 19,760.00 USD | 20,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2255.30` | 102,270,000.00 USD | 102,270,000.00 USD | 13,680,000.00 USD | 6,830,000.00 USD | 5,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2256.40` | 194,000,000.00 USD | 194,000,000.00 USD | 17,810,000.00 USD | 15,220,000.00 USD | 7,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2257.80` | 139,020,000.00 USD | 139,020,000.00 USD | 21,630,000.00 USD | 9,290,000.00 USD | 5,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2259.40` | 213,580,000.00 USD | 213,580,000.00 USD | 11,860,000.00 USD | 3,670,000.00 USD | 4,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2260.30` | 158,960,000.00 USD | 158,960,000.00 USD | 8,050,000.00 USD | 9,340,000.00 USD | 2,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2262.40` | 222,030,000.00 USD | 222,030,000.00 USD | 6,720,000.00 USD | 1,460,000.00 USD | 280,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2262.80` | 189,830,000.00 USD | 189,830,000.00 USD | 14,830,000.00 USD | 9,830,000.00 USD | 6,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2265.00` | 10,060.00 USD | 30,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2265.30` | 215,350,000.00 USD | 215,350,000.00 USD | 4,560,000.00 USD | 9,540,000.00 USD | 11,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2265.40` | 224,630,000.00 USD | 224,630,000.00 USD | 0.00 USD | 2,380,000.00 USD | 218,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2267.80` | 246,340,000.00 USD | 246,340,000.00 USD | 12,410,000.00 USD | 9,520,000.00 USD | 9,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2268.40` | 249,890,000.00 USD | 249,890,000.00 USD | 8,610,000.00 USD | 5,650,000.00 USD | 10,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2270.30` | 280,920,000.00 USD | 280,920,000.00 USD | 12,260,000.00 USD | 7,850,000.00 USD | 14,470,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2271.40` | 285,330,000.00 USD | 285,330,000.00 USD | 17,870,000.00 USD | 1,330,000.00 USD | 16,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2272.80` | 305,680,000.00 USD | 305,680,000.00 USD | 14,460,000.00 USD | 4,820,000.00 USD | 5,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2274.40` | 312,380,000.00 USD | 312,380,000.00 USD | 20,010,000.00 USD | 7,040,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2275.00` | 94,600.00 USD | 124,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2275.30` | 353,340,000.00 USD | 353,340,000.00 USD | 30,000,000.00 USD | 14,070,000.00 USD | 3,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2277.40` | 338,630,000.00 USD | 338,630,000.00 USD | 6,890,000.00 USD | 8,890,000.00 USD | 10,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2277.80` | 388,960,000.00 USD | 388,960,000.00 USD | 6,960,000.00 USD | 13,450,000.00 USD | 15,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2280.30` | 438,850,000.00 USD | 438,850,000.00 USD | 30,250,000.00 USD | 10,870,000.00 USD | 8,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2280.40` | 382,950,000.00 USD | 382,950,000.00 USD | 854,200.00 USD | 39,830,000.00 USD | 3,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2282.80` | 504,140,000.00 USD | 504,140,000.00 USD | 28,930,000.00 USD | 26,510,000.00 USD | 9,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2283.40` | 476,630,000.00 USD | 476,630,000.00 USD | 5,600,000.00 USD | 74,390,000.00 USD | 13,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2285.00` | 169,810.00 USD | 294,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2285.30` | 524,890,000.00 USD | 524,890,000.00 USD | 7,270,000.00 USD | 8,910,000.00 USD | 4,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2286.40` | 480,320,000.00 USD | 480,320,000.00 USD | 2,380,000.00 USD | 727,530.00 USD | 592,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2287.80` | 553,260,000.00 USD | 553,260,000.00 USD | 12,070,000.00 USD | 8,140,000.00 USD | 8,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2289.40` | 511,680,000.00 USD | 511,680,000.00 USD | 7,010,000.00 USD | 9,840,000.00 USD | 14,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2290.30` | 591,820,000.00 USD | 591,820,000.00 USD | 17,620,000.00 USD | 14,910,000.00 USD | 6,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2292.40` | 534,950,000.00 USD | 534,950,000.00 USD | 13,240,000.00 USD | 0.00 USD | 10,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2292.80` | 621,230,000.00 USD | 621,230,000.00 USD | 13,390,000.00 USD | 4,760,000.00 USD | 11,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2295.00` | 4,430,000.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2295.30` | 653,600,000.00 USD | 653,600,000.00 USD | 11,190,000.00 USD | 13,200,000.00 USD | 7,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2295.40` | 572,450,000.00 USD | 572,450,000.00 USD | 22,930,000.00 USD | 6,820,000.00 USD | 7,740,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2297.80` | 701,090,000.00 USD | 701,090,000.00 USD | 28,850,000.00 USD | 12,660,000.00 USD | 5,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2298.40` | 601,820,000.00 USD | 601,820,000.00 USD | 10,950,000.00 USD | 7,970,000.00 USD | 10,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2300.30` | 742,580,000.00 USD | 742,580,000.00 USD | 13,080,000.00 USD | 13,230,000.00 USD | 15,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2301.40` | 648,940,000.00 USD | 648,940,000.00 USD | 17,870,000.00 USD | 23,740,000.00 USD | 5,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2302.80` | 771,240,000.00 USD | 771,240,000.00 USD | 18,360,000.00 USD | 3,050,000.00 USD | 7,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2304.40` | 703,160,000.00 USD | 703,160,000.00 USD | 23,020,000.00 USD | 5,550,000.00 USD | 25,640,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2305.00` | 3,870,000.00 USD | 8,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2305.30` | 809,000,000.00 USD | 809,000,000.00 USD | 13,500,000.00 USD | 16,910,000.00 USD | 7,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2307.40` | 719,970,000.00 USD | 719,970,000.00 USD | 7,580,000.00 USD | 7,040,000.00 USD | 2,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2307.80` | 819,370,000.00 USD | 819,370,000.00 USD | 4,370,000.00 USD | 4,020,000.00 USD | 1,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2310.30` | 838,540,000.00 USD | 838,540,000.00 USD | 5,900,000.00 USD | 2,630,000.00 USD | 10,650,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2310.40` | 739,440,000.00 USD | 739,440,000.00 USD | 11,460,000.00 USD | 2,650,000.00 USD | 5,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2312.80` | 850,740,000.00 USD | 850,740,000.00 USD | 4,670,000.00 USD | 7,190,000.00 USD | 338,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2313.40` | 753,850,000.00 USD | 753,850,000.00 USD | 0.00 USD | 3,430,000.00 USD | 10,980,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2315.00` | 862,340.00 USD | 9,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2315.30` | 873,070,000.00 USD | 873,070,000.00 USD | 4,530,000.00 USD | 11,770,000.00 USD | 6,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2316.40` | 761,490,000.00 USD | 761,490,000.00 USD | 1,020,000.00 USD | 5,590,000.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2317.80` | 894,660,000.00 USD | 894,660,000.00 USD | 6,980,000.00 USD | 11,000,000.00 USD | 3,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2319.40` | 791,770,000.00 USD | 791,770,000.00 USD | 5,530,000.00 USD | 16,850,000.00 USD | 7,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2320.30` | 918,070,000.00 USD | 918,070,000.00 USD | 9,870,000.00 USD | 11,090,000.00 USD | 2,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2322.40` | 800,750,000.00 USD | 800,750,000.00 USD | 5,430,000.00 USD | 3,450,000.00 USD | 108,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2322.80` | 936,500,000.00 USD | 936,500,000.00 USD | 3,860,000.00 USD | 9,520,000.00 USD | 5,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2325.00` | 1,930,000.00 USD | 11,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2325.30` | 950,110,000.00 USD | 950,110,000.00 USD | 2,550,000.00 USD | 9,550,000.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2325.40` | 820,660,000.00 USD | 820,660,000.00 USD | 7,020,000.00 USD | 2,770,000.00 USD | 10,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2327.80` | 956,380,000.00 USD | 956,380,000.00 USD | 494,310.00 USD | 1,240,000.00 USD | 4,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2328.40` | 832,670,000.00 USD | 832,670,000.00 USD | 3,860,000.00 USD | 121,880.00 USD | 8,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2330.30` | 972,100,000.00 USD | 972,100,000.00 USD | 11,050,000.00 USD | 2,970,000.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2331.40` | 856,590,000.00 USD | 856,590,000.00 USD | 23,030,000.00 USD | 835,790.00 USD | 54,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2332.80` | 988,880,000.00 USD | 988,880,000.00 USD | 4,100,000.00 USD | 3,420,000.00 USD | 9,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2334.40` | 904,110,000.00 USD | 904,110,000.00 USD | 20,300,000.00 USD | 15,180,000.00 USD | 12,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2335.00` | 485,570.00 USD | 11,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2335.30` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 12,410,000.00 USD | 3,980,000.00 USD | 3,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2337.40` | 944,500,000.00 USD | 944,500,000.00 USD | 31,080,000.00 USD | 4,650,000.00 USD | 4,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2337.80` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 7,830,000.00 USD | 1,570,000.00 USD | 4,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2340.30` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 10,960,000.00 USD | 6,230,000.00 USD | 12,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2340.40` | 979,730,000.00 USD | 979,730,000.00 USD | 4,720,000.00 USD | 10,900,000.00 USD | 19,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2342.80` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 8,670,000.00 USD | 6,510,000.00 USD | 3,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2343.40` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 5,030,000.00 USD | 11,860,000.00 USD | 7,250,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2345.00` | 767,790.00 USD | 12,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2345.30` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 5,430,000.00 USD | 5,870,000.00 USD | 10,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2346.40` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 1,350,000.00 USD | 19,690,000.00 USD | 15,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2347.80` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 3,940,000.00 USD | 3,280,000.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2349.40` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 1,320,000.00 USD | 10,630,000.00 USD | 22,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2350.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 27,810,000.00 USD | 7,790,000.00 USD | 10,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2352.40` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 2,710,000.00 USD | 27,380,000.00 USD | 5,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2352.80` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 3,960,000.00 USD | 2,860,000.00 USD | 2,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2355.00` | 1,410,000.00 USD | 14,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2355.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 3,190,000.00 USD | 3,410,000.00 USD | 951,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2355.40` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 18,620,000.00 USD | 29,090,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2357.80` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 3,760,000.00 USD | 4,660,000.00 USD | 3,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2358.40` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 7,110,000.00 USD | 512,220.00 USD | 4,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2360.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 10,760,000.00 USD | 3,880,000.00 USD | 5,470,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2361.40` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 2,430,000.00 USD | 3,430,000.00 USD | 374,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2362.80` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 6,460,000.00 USD | 7,190,000.00 USD | 7,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2364.40` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 4,570,000.00 USD | 373,740.00 USD | 10,920,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2365.00` | 3,940,000.00 USD | 17,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2365.30` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 4,830,000.00 USD | 2,660,000.00 USD | 3,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2367.40` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 8,180,000.00 USD | 1,310,000.00 USD | 307,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2367.80` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 3,070,000.00 USD | 2,080,000.00 USD | 1,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2370.30` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 14,770,000.00 USD | 7,590,000.00 USD | 6,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2370.40` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 23,100,000.00 USD | 475,460.00 USD | 47,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2372.80` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 10,040,000.00 USD | 2,830,000.00 USD | 6,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2373.40` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 21,210,000.00 USD | 121,480.00 USD | 11,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2375.00` | 2,240,000.00 USD | 20,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2375.30` | 1,300,000,000.00 USD | 1,300,000,000.00 USD | 10,840,000.00 USD | 1,890,000.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2376.40` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 11,470,000.00 USD | 5,950,000.00 USD | 22,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2377.80` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 1,460,000.00 USD | 1,920,000.00 USD | 3,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2379.40` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 7,850,000.00 USD | 2,580,000.00 USD | 12,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2380.30` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 6,310,000.00 USD | 5,360,000.00 USD | 5,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2382.40` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 8,510,000.00 USD | 12,380,000.00 USD | 27,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2382.80` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 15,730,000.00 USD | 9,540,000.00 USD | 11,420,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2385.00` | 5,550,000.00 USD | 25,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2385.30` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 7,510,000.00 USD | 11,630,000.00 USD | 4,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2385.40` | 1,510,000,000.00 USD | 1,510,000,000.00 USD | 15,900,000.00 USD | 32,250,000.00 USD | 42,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2387.80` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 9,900,000.00 USD | 5,870,000.00 USD | 2,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2388.40` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 4,500,000.00 USD | 36,520,000.00 USD | 37,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2390.30` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 4,300,000.00 USD | 3,360,000.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2391.40` | 1,680,000,000.00 USD | 1,680,000,000.00 USD | 6,180,000.00 USD | 50,800,000.00 USD | 35,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2392.80` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 2,700,000.00 USD | 3,990,000.00 USD | 3,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2394.40` | 1,810,000,000.00 USD | 1,810,000,000.00 USD | 59,450,000.00 USD | 27,550,000.00 USD | 39,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2395.00` | 13,960.00 USD | 25,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2395.30` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 2,060,000.00 USD | 1,450,000.00 USD | 2,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2397.40` | 1,900,000,000.00 USD | 1,900,000,000.00 USD | 26,820,000.00 USD | 40,480,000.00 USD | 23,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2397.80` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 64,150.00 USD | 3,720,000.00 USD | 3,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2400.30` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 2,150,000.00 USD | 637,690.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2400.40` | 2,000,000,000.00 USD | 2,000,000,000.00 USD | 53,610,000.00 USD | 26,460,000.00 USD | 21,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2402.80` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 1,180,000.00 USD | 467,060.00 USD | 555,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2403.40` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 51,380,000.00 USD | 24,860,000.00 USD | 33,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2405.00` | 133,330.00 USD | 25,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2405.30` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 6,820,000.00 USD | 3,310,000.00 USD | 5,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2406.40` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 30,580,000.00 USD | 35,580,000.00 USD | 17,010,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2407.80` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 6,400,000.00 USD | 3,510,000.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2409.40` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 29,180,000.00 USD | 24,710,000.00 USD | 27,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2410.30` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 5,140,000.00 USD | 4,530,000.00 USD | 4,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2412.40` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 16,820,000.00 USD | 18,190,000.00 USD | 16,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2412.80` | 1,490,000,000.00 USD | 1,490,000,000.00 USD | 5,630,000.00 USD | 3,710,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2415.00` | 698,300.00 USD | 26,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2415.30` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 2,830,000.00 USD | 2,350,000.00 USD | 2,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2415.40` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 22,500,000.00 USD | 20,300,000.00 USD | 25,180,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2417.80` | 1,510,000,000.00 USD | 1,510,000,000.00 USD | 2,680,000.00 USD | 1,770,000.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2418.40` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 27,870,000.00 USD | 11,330,000.00 USD | 19,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2420.30` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 6,350,000.00 USD | 3,220,000.00 USD | 4,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2421.40` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 22,110,000.00 USD | 21,710,000.00 USD | 12,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2422.80` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 1,380,000.00 USD | 2,790,000.00 USD | 3,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2424.40` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 20,650,000.00 USD | 18,010,000.00 USD | 25,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2425.00` | 215,570.00 USD | 26,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2425.30` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 1,280,000.00 USD | 623,850.00 USD | 888,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2427.40` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 17,580,000.00 USD | 11,600,000.00 USD | 13,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2427.80` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 1,490,000.00 USD | 1,520,000.00 USD | 609,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2430.30` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 1,460,000.00 USD | 1,550,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2430.40` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 8,480,000.00 USD | 15,370,000.00 USD | 9,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2432.80` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 2,680,000.00 USD | 2,230,000.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2433.40` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 14,840,000.00 USD | 5,270,000.00 USD | 4,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2435.00` | 183,230.00 USD | 27,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2435.30` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 2,480,000.00 USD | 572,900.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2436.40` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 6,380,000.00 USD | 8,830,000.00 USD | 5,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2437.80` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 1,360,000.00 USD | 1,040,000.00 USD | 30,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2439.40` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 13,950,000.00 USD | 7,290,000.00 USD | 5,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2440.30` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 1,240,000.00 USD | 515,920.00 USD | 304,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2442.40` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 6,350,000.00 USD | 5,550,000.00 USD | 7,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2442.80` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 1,030,000.00 USD | 673,960.00 USD | 823,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2445.00` | 105,580.00 USD | 27,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2445.30` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 0.00 USD | 486,350.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2445.40` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 9,990,000.00 USD | 8,050,000.00 USD | 10,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2447.80` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 472,100.00 USD | 743,310.00 USD | 694,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2448.40` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 11,190,000.00 USD | 3,790,000.00 USD | 15,190,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2450.30` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 1,710,000.00 USD | 69,580.00 USD | 26,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2451.40` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 8,550,000.00 USD | 7,920,000.00 USD | 6,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2452.80` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 2,460,000.00 USD | 1,840,000.00 USD | 2,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2454.40` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 5,080,000.00 USD | 3,080,000.00 USD | 4,450,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2455.00` | 638,010.00 USD | 27,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2455.30` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 1,640,000.00 USD | 1,860,000.00 USD | 905,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2457.40` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 8,580,000.00 USD | 7,900,000.00 USD | 8,690,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2457.80` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 1,770,000.00 USD | 1,980,000.00 USD | 845,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2460.30` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 1,530,000.00 USD | 1,410,000.00 USD | 388,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2460.40` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 3,700,000.00 USD | 7,320,000.00 USD | 4,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2462.80` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 355,800.00 USD | 618,870.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2463.40` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 6,140,000.00 USD | 5,730,000.00 USD | 6,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2465.00` | 65,780,000.00 USD | 93,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2465.30` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 537,580.00 USD | 876,630.00 USD | 345,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2466.40` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 5,680,000.00 USD | 2,080,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2467.80` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 288,920.00 USD | 980,750.00 USD | 377,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2469.40` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 2,520,000.00 USD | 3,570,000.00 USD | 408,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2470.30` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 1,010,000.00 USD | 1,660,000.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2472.40` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 4,130,000.00 USD | 2,760,000.00 USD | 2,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2472.80` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 404,980.00 USD | 92,950.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2475.00` | 5,220,000.00 USD | 98,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `2475.30` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 414,330.00 USD | 1,100,000.00 USD | 231,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2475.40` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 5,400,000.00 USD | 1,040,000.00 USD | 1,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2477.80` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 2,200,000.00 USD | 238,300.00 USD | 167,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2478.40` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 3,140,000.00 USD | 5,290,000.00 USD | 540,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2480.30` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 567,450.00 USD | 943,540.00 USD | 731,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2481.40` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 729,480.00 USD | 3,680,000.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `2482.50` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 437,940.00 USD | 156,850.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2484.40` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2485.00` | 47,080.00 USD | 98,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2487.40` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 275,450.00 USD | 211,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2490.40` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 385,480.00 USD | 301,010.00 USD | 137,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2493.40` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 3,000,000.00 USD | 733,870.00 USD | 1,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2495.00` | 1,720,000.00 USD | 100,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2496.40` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 993,060.00 USD | 812,060.00 USD | 4,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2499.40` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 0.00 USD | 1,310,000.00 USD | 241,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2502.40` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 0.00 USD | 55,050.00 USD | 125,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2505.00` | 6,600,000.00 USD | 107,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2505.40` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2508.40` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 1,090,000.00 USD | 882,660.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2514.40` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2515.00` | 1,520,000.00 USD | 108,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `2517.40` | 2,970,000,000.00 USD | 2,970,000,000.00 USD | 975,520.00 USD | 965,900.00 USD | 815,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2520.40` | 2,970,000,000.00 USD | 2,970,000,000.00 USD | 722,920.00 USD | 1,170,000.00 USD | 894,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `2523.40` | 2,970,000,000.00 USD | 2,970,000,000.00 USD | 1,050,000.00 USD | 0.00 USD | 945,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `2525.00` | 49,110.00 USD | 108,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2535.00` | 902,070.00 USD | 109,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2545.00` | 5,140,000.00 USD | 114,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2555.00` | 178,910.00 USD | 114,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2565.00` | 47,080.00 USD | 114,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2575.00` | 98,600.00 USD | 115,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2585.00` | 26,890,000.00 USD | 141,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2595.00` | 7,990,000.00 USD | 149,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2605.00` | 5,940,000.00 USD | 155,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2615.00` | 693,160.00 USD | 156,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2625.00` | 32,900,000.00 USD | 189,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2635.00` | 20,390,000.00 USD | 209,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2645.00` | 636,110.00 USD | 210,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2655.00` | 26,160,000.00 USD | 236,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2665.00` | 590,500.00 USD | 237,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2675.00` | 4,380,000.00 USD | 241,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2685.00` | 115,800.00 USD | 241,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2695.00` | 77,870.00 USD | 241,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2705.00` | 631,700.00 USD | 242,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2715.00` | 142,740.00 USD | 242,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2725.00` | 427,530.00 USD | 243,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2735.00` | 156,260.00 USD | 243,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2745.00` | 727,130.00 USD | 243,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2755.00` | 5,750,000.00 USD | 249,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2765.00` | 5,530,000.00 USD | 255,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2775.00` | 13,470,000.00 USD | 268,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2785.00` | 32,450.00 USD | 268,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2795.00` | 16,360,000.00 USD | 285,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2805.00` | 4,350,000.00 USD | 289,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2815.00` | 1,160,000.00 USD | 290,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2825.00` | 535,360.00 USD | 291,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2835.00` | 6,010,000.00 USD | 297,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2845.00` | 542,980.00 USD | 297,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2855.00` | 376,680.00 USD | 298,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2865.00` | 92,670.00 USD | 298,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2875.00` | 141,320.00 USD | 298,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2885.00` | 935,060.00 USD | 299,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2895.00` | 15,540,000.00 USD | 314,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2905.00` | 26,880,000.00 USD | 341,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2915.00` | 2,660,000.00 USD | 344,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2925.00` | 890,390.00 USD | 345,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2935.00` | 31,460.00 USD | 345,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2945.00` | 449,420.00 USD | 345,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2955.00` | 205,630.00 USD | 345,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2965.00` | 3,910,000.00 USD | 349,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2975.00` | 95,430.00 USD | 349,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2985.00` | 1,280,000.00 USD | 351,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2995.00` | 1,860,000.00 USD | 352,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3005.00` | 1,140,000.00 USD | 354,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3015.00` | 136,300.00 USD | 354,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3025.00` | 2,530,000.00 USD | 356,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3035.00` | 12,850,000.00 USD | 369,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3045.00` | 82,000.00 USD | 369,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3055.00` | 2,140,000.00 USD | 371,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3065.00` | 13,620.00 USD | 371,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3075.00` | 9,640,000.00 USD | 381,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3085.00` | 2,200,000.00 USD | 383,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3095.00` | 381,870.00 USD | 384,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3105.00` | 14,150,000.00 USD | 398,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3115.00` | 323,410.00 USD | 398,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3125.00` | 364,040.00 USD | 398,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3135.00` | 586,000.00 USD | 399,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3145.00` | 29,430,000.00 USD | 428,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3155.00` | 4,980,000.00 USD | 433,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3165.00` | 180,110.00 USD | 434,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3175.00` | 861,010.00 USD | 434,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3185.00` | 6,910,000.00 USD | 441,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3195.00` | 3,770,000.00 USD | 445,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3205.00` | 141,980.00 USD | 445,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3215.00` | 175,900.00 USD | 445,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3225.00` | 8,260,000.00 USD | 454,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3235.00` | 9,760,000.00 USD | 463,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3245.00` | 182,560.00 USD | 464,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3255.00` | 33,240.00 USD | 464,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3265.00` | 2,020,000.00 USD | 466,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3275.00` | 8,470,000.00 USD | 474,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3285.00` | 72,510.00 USD | 474,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3295.00` | 5,140,000.00 USD | 479,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3305.00` | 2,700,000.00 USD | 482,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3315.00` | 909,270.00 USD | 483,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3325.00` | 87,690.00 USD | 483,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3335.00` | 687,410.00 USD | 484,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3345.00` | 1,380,000.00 USD | 485,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3355.00` | 2,150,000.00 USD | 487,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3365.00` | 118,210.00 USD | 487,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3375.00` | 77,100.00 USD | 487,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3385.00` | 6,000,000.00 USD | 493,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3395.00` | 1,210,000.00 USD | 495,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3405.00` | 186,760.00 USD | 495,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3415.00` | 2,340,000.00 USD | 497,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3425.00` | 14,720,000.00 USD | 512,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3435.00` | 1,120,000.00 USD | 513,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3445.00` | 561,170.00 USD | 514,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3455.00` | 486,520.00 USD | 514,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3465.00` | 166,590.00 USD | 514,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3475.00` | 58,040,000.00 USD | 572,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3485.00` | 658,610.00 USD | 573,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3495.00` | 2,100,000.00 USD | 575,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3505.00` | 860,620.00 USD | 576,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3515.00` | 6,450.00 USD | 576,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3525.00` | 45,290,000.00 USD | 621,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3535.00` | 255,300.00 USD | 621,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3545.00` | 77,430.00 USD | 622,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3555.00` | 255,740.00 USD | 622,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3565.00` | 507,900.00 USD | 622,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3575.00` | 118,760.00 USD | 622,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3585.00` | 761,910.00 USD | 623,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3595.00` | 31,380.00 USD | 623,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3605.00` | 47,860.00 USD | 623,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3615.00` | 3,640,000.00 USD | 627,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3625.00` | 568,820.00 USD | 628,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3635.00` | 8,740,000.00 USD | 636,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3645.00` | 22,040.00 USD | 636,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3655.00` | 24,470.00 USD | 636,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3665.00` | 6,820,000.00 USD | 643,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3675.00` | 76,200.00 USD | 643,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3685.00` | 212,440.00 USD | 643,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3695.00` | 30,730.00 USD | 643,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3705.00` | 399,380.00 USD | 644,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3715.00` | 1,330,000.00 USD | 645,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3725.00` | 460,700.00 USD | 646,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3735.00` | 360,470.00 USD | 646,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3745.00` | 839,100.00 USD | 647,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3755.00` | 259,520.00 USD | 647,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3765.00` | 1,970,000.00 USD | 649,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3775.00` | 302,220.00 USD | 649,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3785.00` | 189,510.00 USD | 650,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3795.00` | 2,590,000.00 USD | 652,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3805.00` | 410,440,000.00 USD | 1,060,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3815.00` | 100.33 USD | 1,060,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3825.00` | 1,980,000.00 USD | 1,070,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3835.00` | 378,000.00 USD | 1,070,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3845.00` | 299.14 USD | 1,070,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3855.00` | 1,170,000.00 USD | 1,070,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3865.00` | 651,040.00 USD | 1,070,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3875.00` | 35,590,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3885.00` | 1,360,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3895.00` | 2,520,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3905.00` | 1,220,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3915.00` | 20,140.00 USD | 1,110,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3925.00` | 148,130.00 USD | 1,110,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3935.00` | 4,920.00 USD | 1,110,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3945.00` | 88,410.00 USD | 1,110,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3955.00` | 2,020,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3965.00` | 74,010.00 USD | 1,110,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3975.00` | 201,740.00 USD | 1,110,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3985.00` | 63,150,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `3995.00` | 1,040,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4005.00` | 62,810.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4015.00` | 85,510.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4025.00` | 131,080.00 USD | 1,170,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4035.00` | 364,900.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4045.00` | 80,660.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4055.00` | 1,970,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4065.00` | 1,230,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4075.00` | 70,020.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4085.00` | 2,230.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4095.00` | 9,520.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4105.00` | 2,610,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4115.00` | 3,300.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4125.00` | 283,580.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4135.00` | 678,960.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4145.00` | 232,930.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4155.00` | 175,260.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4165.00` | 206,800.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4175.00` | 837,830.00 USD | 1,180,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4185.00` | 83,610,000.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4195.00` | 5,670,000.00 USD | 1,270,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4205.00` | 28,680,000.00 USD | 1,300,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4215.00` | 447.21 USD | 1,300,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4225.00` | 7,020.00 USD | 1,300,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4235.00` | 776,260.00 USD | 1,300,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4245.00` | 3,980.00 USD | 1,300,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4255.00` | 5,400,000.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4265.00` | 58,530.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4275.00` | 7,630.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4285.00` | 187,650.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4295.00` | 4,510,000.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4305.00` | 5,450.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4315.00` | 47,050.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4325.00` | 557,660.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4335.00` | 211,680.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4345.00` | 14,450.00 USD | 1,310,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4355.00` | 281,690,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4365.00` | 547,470.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4375.00` | 464,420.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4385.00` | 117.96 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4395.00` | 15,230.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4405.00` | 175,600.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4415.00` | 56,700.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4425.00` | 97,080.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4445.00` | 446,720.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4455.00` | 11,510.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4465.00` | 24,920.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4475.00` | 58,650.00 USD | 1,600,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `445.00` | 775,420,000.00 USD | 0.00 USD | 3,820.00 USD | `-80.09%` | `8.58` |
| `Live` | `Long` | `455.00` | 775,420,000.00 USD | 0.00 USD | 148,090.00 USD | `-79.64%` | `325.48` |
| `Live` | `Long` | `465.00` | 775,270,000.00 USD | 0.00 USD | 578.23 USD | `-79.20%` | `1.24` |
| `Live` | `Long` | `475.00` | 775,270,000.00 USD | 0.00 USD | 8,820.00 USD | `-78.75%` | `18.57` |
| `Live` | `Long` | `485.00` | 775,260,000.00 USD | 0.00 USD | 106,620.00 USD | `-78.30%` | `219.83` |
| `Live` | `Long` | `495.00` | 775,160,000.00 USD | 0.00 USD | 1,770,000.00 USD | `-77.85%` | `3,582.49` |
| `Live` | `Long` | `505.00` | 773,380,000.00 USD | 0.00 USD | 20,980.00 USD | `-77.41%` | `41.54` |
| `Live` | `Long` | `515.00` | 773,360,000.00 USD | 0.00 USD | 47,920.00 USD | `-76.96%` | `93.04` |
| `Live` | `Long` | `525.00` | 773,310,000.00 USD | 0.00 USD | 8,310.00 USD | `-76.51%` | `15.83` |
| `Live` | `Long` | `535.00` | 773,310,000.00 USD | 0.00 USD | 4,120.00 USD | `-76.06%` | `7.71` |
| `Live` | `Long` | `545.00` | 773,300,000.00 USD | 0.00 USD | 50,860.00 USD | `-75.62%` | `93.32` |
| `Live` | `Long` | `555.00` | 773,250,000.00 USD | 0.00 USD | 1,810,000.00 USD | `-75.17%` | `3,259.24` |
| `Live` | `Long` | `565.00` | 771,440,000.00 USD | 0.00 USD | 46,070.00 USD | `-74.72%` | `81.54` |
| `Live` | `Long` | `575.00` | 771,400,000.00 USD | 0.00 USD | 33,960.00 USD | `-74.27%` | `59.07` |
| `Live` | `Long` | `585.00` | 771,360,000.00 USD | 0.00 USD | 13,710.00 USD | `-73.83%` | `23.43` |
| `Live` | `Long` | `595.00` | 771,350,000.00 USD | 0.00 USD | 429,270.00 USD | `-73.38%` | `721.47` |
| `Live` | `Long` | `605.00` | 770,920,000.00 USD | 0.00 USD | 4,480,000.00 USD | `-72.93%` | `7,407.05` |
| `Live` | `Long` | `615.00` | 766,440,000.00 USD | 0.00 USD | 43,010.00 USD | `-72.48%` | `69.94` |
| `Live` | `Long` | `625.00` | 766,390,000.00 USD | 0.00 USD | 145,780.00 USD | `-72.04%` | `233.26` |
| `Live` | `Long` | `635.00` | 766,250,000.00 USD | 0.00 USD | 93,950.00 USD | `-71.59%` | `147.95` |
| `Live` | `Long` | `645.00` | 766,150,000.00 USD | 0.00 USD | 131,190.00 USD | `-71.14%` | `203.40` |
| `Live` | `Long` | `655.00` | 766,020,000.00 USD | 0.00 USD | 644,750.00 USD | `-70.69%` | `984.35` |
| `Live` | `Long` | `665.00` | 765,380,000.00 USD | 0.00 USD | 19,860.00 USD | `-70.25%` | `29.86` |
| `Live` | `Long` | `675.00` | 765,360,000.00 USD | 0.00 USD | 16,000.00 USD | `-69.80%` | `23.71` |
| `Live` | `Long` | `685.00` | 765,340,000.00 USD | 0.00 USD | 35,670.00 USD | `-69.35%` | `52.07` |
| `Live` | `Long` | `695.00` | 765,310,000.00 USD | 0.00 USD | 172,530.00 USD | `-68.91%` | `248.25` |
| `Live` | `Long` | `705.00` | 765,130,000.00 USD | 0.00 USD | 23,170.00 USD | `-68.46%` | `32.86` |
| `Live` | `Long` | `715.00` | 765,110,000.00 USD | 0.00 USD | 11,250.00 USD | `-68.01%` | `15.73` |
| `Live` | `Long` | `725.00` | 765,100,000.00 USD | 0.00 USD | 436,810.00 USD | `-67.56%` | `602.49` |
| `Live` | `Long` | `735.00` | 764,660,000.00 USD | 0.00 USD | 48,440.00 USD | `-67.12%` | `65.91` |
| `Live` | `Long` | `745.00` | 764,620,000.00 USD | 0.00 USD | 1,820.00 USD | `-66.67%` | `2.44` |
| `Live` | `Long` | `755.00` | 764,610,000.00 USD | 0.00 USD | 42,880.00 USD | `-66.22%` | `56.79` |
| `Live` | `Long` | `765.00` | 764,570,000.00 USD | 0.00 USD | 133,400.00 USD | `-65.77%` | `174.38` |
| `Live` | `Long` | `775.00` | 764,440,000.00 USD | 0.00 USD | 185,410.00 USD | `-65.33%` | `239.24` |
| `Live` | `Long` | `785.00` | 764,250,000.00 USD | 0.00 USD | 88,540.00 USD | `-64.88%` | `112.79` |
| `Live` | `Long` | `795.00` | 764,160,000.00 USD | 0.00 USD | 141,120.00 USD | `-64.43%` | `177.50` |
| `Live` | `Long` | `805.00` | 764,020,000.00 USD | 0.00 USD | 121,190.00 USD | `-63.98%` | `150.54` |
| `Live` | `Long` | `815.00` | 763,900,000.00 USD | 0.00 USD | 24,860.00 USD | `-63.54%` | `30.50` |
| `Live` | `Long` | `825.00` | 763,880,000.00 USD | 0.00 USD | 73,550.00 USD | `-63.09%` | `89.16` |
| `Live` | `Long` | `835.00` | 763,800,000.00 USD | 0.00 USD | 203,150.00 USD | `-62.64%` | `243.29` |
| `Live` | `Long` | `845.00` | 763,600,000.00 USD | 0.00 USD | 229,530.00 USD | `-62.19%` | `271.63` |
| `Live` | `Long` | `855.00` | 763,370,000.00 USD | 0.00 USD | 426,480.00 USD | `-61.75%` | `498.80` |
| `Live` | `Long` | `865.00` | 762,940,000.00 USD | 0.00 USD | 61,360.00 USD | `-61.30%` | `70.94` |
| `Live` | `Long` | `875.00` | 762,880,000.00 USD | 0.00 USD | 25,620.00 USD | `-60.85%` | `29.28` |
| `Live` | `Long` | `885.00` | 762,860,000.00 USD | 0.00 USD | 1,060,000.00 USD | `-60.40%` | `1,193.08` |
| `Live` | `Long` | `895.00` | 761,800,000.00 USD | 0.00 USD | 127,340.00 USD | `-59.96%` | `142.28` |
| `Live` | `Long` | `905.00` | 761,670,000.00 USD | 0.00 USD | 72,750.00 USD | `-59.51%` | `80.38` |
| `Live` | `Long` | `915.00` | 761,600,000.00 USD | 0.00 USD | 480,070.00 USD | `-59.06%` | `524.67` |
| `Live` | `Long` | `925.00` | 761,120,000.00 USD | 0.00 USD | 109,240.00 USD | `-58.61%` | `118.09` |
| `Live` | `Long` | `935.00` | 761,010,000.00 USD | 0.00 USD | 27,700.00 USD | `-58.17%` | `29.63` |
| `Live` | `Long` | `945.00` | 760,980,000.00 USD | 0.00 USD | 40,280.00 USD | `-57.72%` | `42.63` |
| `Live` | `Long` | `955.00` | 760,940,000.00 USD | 0.00 USD | 50,770.00 USD | `-57.27%` | `53.16` |
| `Live` | `Long` | `965.00` | 760,890,000.00 USD | 0.00 USD | 1,770,000.00 USD | `-56.83%` | `1,835.63` |
| `Live` | `Long` | `975.00` | 759,120,000.00 USD | 0.00 USD | 364,180.00 USD | `-56.38%` | `373.52` |
| `Live` | `Long` | `985.00` | 758,760,000.00 USD | 0.00 USD | 414,070.00 USD | `-55.93%` | `420.38` |
| `Live` | `Long` | `995.00` | 758,340,000.00 USD | 0.00 USD | 33,580.00 USD | `-55.48%` | `33.75` |
| `Live` | `Long` | `1005.00` | 758,310,000.00 USD | 0.00 USD | 74,920.00 USD | `-55.04%` | `74.55` |
| `Live` | `Long` | `1015.00` | 758,230,000.00 USD | 0.00 USD | 112,100.00 USD | `-54.59%` | `110.44` |
| `Live` | `Long` | `1025.00` | 758,120,000.00 USD | 0.00 USD | 416,280.00 USD | `-54.14%` | `406.13` |
| `Live` | `Long` | `1035.00` | 757,710,000.00 USD | 0.00 USD | 27,840.00 USD | `-53.69%` | `26.90` |
| `Live` | `Long` | `1045.00` | 757,680,000.00 USD | 0.00 USD | 922,550.00 USD | `-53.25%` | `882.82` |
| `Live` | `Long` | `1055.00` | 756,760,000.00 USD | 0.00 USD | 152,290.00 USD | `-52.80%` | `144.35` |
| `Live` | `Long` | `1065.00` | 756,600,000.00 USD | 0.00 USD | 7,490,000.00 USD | `-52.35%` | `7,035.58` |
| `Live` | `Long` | `1075.00` | 749,110,000.00 USD | 0.00 USD | 2,240,000.00 USD | `-51.90%` | `2,079.09` |
| `Live` | `Long` | `1085.00` | 746,880,000.00 USD | 0.00 USD | 380,440.00 USD | `-51.46%` | `350.64` |
| `Live` | `Long` | `1095.00` | 746,490,000.00 USD | 0.00 USD | 520,760.00 USD | `-51.01%` | `475.58` |
| `Live` | `Long` | `1105.00` | 745,970,000.00 USD | 0.00 USD | 493,720.00 USD | `-50.56%` | `446.81` |
| `Live` | `Long` | `1115.00` | 745,480,000.00 USD | 0.00 USD | 299,410.00 USD | `-50.11%` | `268.53` |
| `Live` | `Long` | `1125.00` | 745,180,000.00 USD | 0.00 USD | 7,870,000.00 USD | `-49.67%` | `6,994.71` |
| `Live` | `Long` | `1135.00` | 737,310,000.00 USD | 0.00 USD | 2,090,000.00 USD | `-49.22%` | `1,839.95` |
| `Live` | `Long` | `1145.00` | 735,220,000.00 USD | 0.00 USD | 1,230,000.00 USD | `-48.77%` | `1,074.00` |
| `Live` | `Long` | `1155.00` | 733,990,000.00 USD | 0.00 USD | 7,890,000.00 USD | `-48.32%` | `6,829.29` |
| `Live` | `Long` | `1165.00` | 726,110,000.00 USD | 0.00 USD | 2,540,000.00 USD | `-47.88%` | `2,177.62` |
| `Live` | `Long` | `1175.00` | 723,570,000.00 USD | 0.00 USD | 249,480.00 USD | `-47.43%` | `212.32` |
| `Live` | `Long` | `1185.00` | 723,320,000.00 USD | 0.00 USD | 1,050,000.00 USD | `-46.98%` | `882.93` |
| `Live` | `Long` | `1195.00` | 722,270,000.00 USD | 0.00 USD | 228,770.00 USD | `-46.53%` | `191.44` |
| `Live` | `Long` | `1205.00` | 722,040,000.00 USD | 0.00 USD | 196,650.00 USD | `-46.09%` | `163.19` |
| `Live` | `Long` | `1215.00` | 721,850,000.00 USD | 0.00 USD | 384,700.00 USD | `-45.64%` | `316.62` |
| `Live` | `Long` | `1225.00` | 721,460,000.00 USD | 0.00 USD | 2,350,000.00 USD | `-45.19%` | `1,921.45` |
| `Live` | `Long` | `1235.00` | 719,110,000.00 USD | 0.00 USD | 337,640.00 USD | `-44.75%` | `273.39` |
| `Live` | `Long` | `1245.00` | 718,770,000.00 USD | 0.00 USD | 836,230.00 USD | `-44.30%` | `671.67` |
| `Live` | `Long` | `1255.00` | 717,940,000.00 USD | 0.00 USD | 410,860.00 USD | `-43.85%` | `327.38` |
| `Live` | `Long` | `1265.00` | 717,520,000.00 USD | 0.00 USD | 182,910.00 USD | `-43.40%` | `144.59` |
| `Live` | `Long` | `1275.00` | 717,340,000.00 USD | 0.00 USD | 15,380,000.00 USD | `-42.96%` | `12,060.97` |
| `Live` | `Long` | `1285.00` | 701,960,000.00 USD | 0.00 USD | 391,910.00 USD | `-42.51%` | `304.99` |
| `Live` | `Long` | `1295.00` | 701,570,000.00 USD | 0.00 USD | 307,370.00 USD | `-42.06%` | `237.35` |
| `Live` | `Long` | `1305.00` | 701,260,000.00 USD | 0.00 USD | 1,300,000.00 USD | `-41.61%` | `996.91` |
| `Live` | `Long` | `1315.00` | 699,960,000.00 USD | 0.00 USD | 185,760.00 USD | `-41.17%` | `141.26` |
| `Live` | `Long` | `1325.00` | 699,780,000.00 USD | 0.00 USD | 531,330.00 USD | `-40.72%` | `401.01` |
| `Live` | `Long` | `1335.00` | 699,250,000.00 USD | 0.00 USD | 305,870.00 USD | `-40.27%` | `229.12` |
| `Live` | `Long` | `1345.00` | 698,940,000.00 USD | 0.00 USD | 5,650,000.00 USD | `-39.82%` | `4,198.61` |
| `Live` | `Long` | `1355.00` | 693,290,000.00 USD | 0.00 USD | 289,170.00 USD | `-39.38%` | `213.41` |
| `Live` | `Long` | `1365.00` | 693,000,000.00 USD | 0.00 USD | 1,110,000.00 USD | `-38.93%` | `810.32` |
| `Live` | `Long` | `1375.00` | 691,900,000.00 USD | 0.00 USD | 7,440,000.00 USD | `-38.48%` | `5,411.22` |
| `Live` | `Long` | `1385.00` | 684,460,000.00 USD | 0.00 USD | 2,120,000.00 USD | `-38.03%` | `1,528.39` |
| `Live` | `Long` | `1395.00` | 682,340,000.00 USD | 0.00 USD | 590,890.00 USD | `-37.59%` | `423.58` |
| `Live` | `Long` | `1405.00` | 681,750,000.00 USD | 0.00 USD | 23,290,000.00 USD | `-37.14%` | `16,579.92` |
| `Live` | `Long` | `1415.00` | 658,460,000.00 USD | 0.00 USD | 191,580.00 USD | `-36.69%` | `135.39` |
| `Live` | `Long` | `1425.00` | 658,260,000.00 USD | 0.00 USD | 369,310.00 USD | `-36.24%` | `259.16` |
| `Live` | `Long` | `1435.00` | 657,890,000.00 USD | 0.00 USD | 1,190,000.00 USD | `-35.80%` | `832.50` |
| `Live` | `Long` | `1445.00` | 656,700,000.00 USD | 0.00 USD | 324,720.00 USD | `-35.35%` | `224.72` |
| `Live` | `Long` | `1455.00` | 656,380,000.00 USD | 0.00 USD | 19,320,000.00 USD | `-34.90%` | `13,281.24` |
| `Live` | `Long` | `1465.00` | 637,050,000.00 USD | 0.00 USD | 1,900,000.00 USD | `-34.45%` | `1,295.71` |
| `Live` | `Long` | `1475.00` | 635,150,000.00 USD | 0.00 USD | 12,220,000.00 USD | `-34.01%` | `8,282.68` |
| `Live` | `Long` | `1485.00` | 622,940,000.00 USD | 0.00 USD | 51,690.00 USD | `-33.56%` | `34.81` |
| `Live` | `Long` | `1495.00` | 622,880,000.00 USD | 0.00 USD | 299,590.00 USD | `-33.11%` | `200.39` |
| `Live` | `Long` | `1505.00` | 622,580,000.00 USD | 0.00 USD | 1,180,000.00 USD | `-32.67%` | `783.10` |
| `Live` | `Long` | `1515.00` | 621,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | `-32.22%` | `1,591.83` |
| `Live` | `Long` | `1525.00` | 618,990,000.00 USD | 0.00 USD | 18,760,000.00 USD | `-31.77%` | `12,303.30` |
| `Live` | `Long` | `1535.00` | 600,230,000.00 USD | 0.00 USD | 16,320,000.00 USD | `-31.32%` | `10,632.12` |
| `Live` | `Long` | `1545.00` | 583,910,000.00 USD | 0.00 USD | 2,860,000.00 USD | `-30.88%` | `1,851.70` |
| `Live` | `Long` | `1555.00` | 581,050,000.00 USD | 0.00 USD | 1,070,000.00 USD | `-30.43%` | `687.62` |
| `Live` | `Long` | `1565.00` | 579,980,000.00 USD | 0.00 USD | 2,920,000.00 USD | `-29.98%` | `1,866.13` |
| `Live` | `Long` | `1575.00` | 577,060,000.00 USD | 0.00 USD | 643,670.00 USD | `-29.53%` | `408.68` |
| `Live` | `Long` | `1585.00` | 576,420,000.00 USD | 0.00 USD | 739,730.00 USD | `-29.09%` | `466.70` |
| `Live` | `Long` | `1595.00` | 575,680,000.00 USD | 0.00 USD | 1,570,000.00 USD | `-28.64%` | `984.24` |
| `Live` | `Long` | `1605.00` | 574,110,000.00 USD | 0.00 USD | 18,050,000.00 USD | `-28.19%` | `11,245.11` |
| `Live` | `Long` | `1615.00` | 556,060,000.00 USD | 0.00 USD | 316,290.00 USD | `-27.74%` | `195.84` |
| `Live` | `Long` | `1625.00` | 555,740,000.00 USD | 0.00 USD | 1,720,000.00 USD | `-27.30%` | `1,057.06` |
| `Live` | `Long` | `1635.00` | 554,030,000.00 USD | 0.00 USD | 19,250,000.00 USD | `-26.85%` | `11,774.80` |
| `Live` | `Long` | `1645.00` | 534,770,000.00 USD | 0.00 USD | 36,970,000.00 USD | `-26.40%` | `22,474.02` |
| `Live` | `Long` | `1655.00` | 497,800,000.00 USD | 0.00 USD | 866,150.00 USD | `-25.95%` | `523.35` |
| `Live` | `Long` | `1665.00` | 496,940,000.00 USD | 0.00 USD | 12,090,000.00 USD | `-25.51%` | `7,264.15` |
| `Live` | `Long` | `1675.00` | 484,840,000.00 USD | 0.00 USD | 1,260,000.00 USD | `-25.06%` | `752.52` |
| `Live` | `Long` | `1685.00` | 483,580,000.00 USD | 0.00 USD | 578,780.00 USD | `-24.61%` | `343.49` |
| `Live` | `Long` | `1695.00` | 483,000,000.00 USD | 0.00 USD | 708,290.00 USD | `-24.16%` | `417.87` |
| `Live` | `Long` | `1705.00` | 482,300,000.00 USD | 0.00 USD | 577,620.00 USD | `-23.72%` | `338.78` |
| `Live` | `Long` | `1715.00` | 481,720,000.00 USD | 0.00 USD | 644,480.00 USD | `-23.27%` | `375.79` |
| `Live` | `Long` | `1725.00` | 481,070,000.00 USD | 0.00 USD | 41,350,000.00 USD | `-22.82%` | `23,971.70` |
| `Live` | `Long` | `1735.00` | 439,720,000.00 USD | 0.00 USD | 505,710.00 USD | `-22.37%` | `291.47` |
| `Live` | `Long` | `1745.00` | 439,220,000.00 USD | 0.00 USD | 4,250,000.00 USD | `-21.93%` | `2,436.41` |
| `Live` | `Long` | `1755.00` | 434,960,000.00 USD | 0.00 USD | 45,550,000.00 USD | `-21.48%` | `25,957.26` |
| `Live` | `Long` | `1765.00` | 389,410,000.00 USD | 0.00 USD | 3,530,000.00 USD | `-21.03%` | `1,999.58` |
| `Live` | `Long` | `1775.00` | 385,880,000.00 USD | 0.00 USD | 7,600,000.00 USD | `-20.59%` | `4,280.34` |
| `Live` | `Long` | `1785.00` | 378,280,000.00 USD | 0.00 USD | 54,780,000.00 USD | `-20.14%` | `30,688.18` |
| `Live` | `Long` | `1795.00` | 323,500,000.00 USD | 0.00 USD | 3,930,000.00 USD | `-19.69%` | `2,189.19` |
| `Live` | `Long` | `1805.00` | 319,570,000.00 USD | 0.00 USD | 3,110,000.00 USD | `-19.24%` | `1,723.60` |
| `Live` | `Long` | `1815.00` | 316,460,000.00 USD | 0.00 USD | 456,010.00 USD | `-18.80%` | `251.24` |
| `Live` | `Long` | `1825.00` | 316,010,000.00 USD | 0.00 USD | 1,230,000.00 USD | `-18.35%` | `674.21` |
| `Live` | `Long` | `1835.00` | 314,780,000.00 USD | 0.00 USD | 13,290,000.00 USD | `-17.90%` | `7,242.42` |
| `Live` | `Long` | `1845.00` | 301,490,000.00 USD | 0.00 USD | 15,910,000.00 USD | `-17.45%` | `8,624.72` |
| `Live` | `Long` | `1855.00` | 285,570,000.00 USD | 0.00 USD | 4,250,000.00 USD | `-17.01%` | `2,289.50` |
| `Live` | `Long` | `1865.00` | 281,330,000.00 USD | 0.00 USD | 913,020.00 USD | `-16.56%` | `489.55` |
| `Live` | `Long` | `1875.00` | 280,410,000.00 USD | 0.00 USD | 7,580,000.00 USD | `-16.11%` | `4,042.25` |
| `Live` | `Long` | `1885.00` | 272,840,000.00 USD | 0.00 USD | 5,330,000.00 USD | `-15.66%` | `2,826.09` |
| `Live` | `Long` | `1895.00` | 267,510,000.00 USD | 0.00 USD | 647,820.00 USD | `-15.22%` | `341.85` |
| `Live` | `Long` | `1905.00` | 266,860,000.00 USD | 0.00 USD | 952,610.00 USD | `-14.77%` | `500.06` |
| `Live` | `Long` | `1915.00` | 265,910,000.00 USD | 0.00 USD | 17,810,000.00 USD | `-14.32%` | `9,298.44` |
| `Live` | `Long` | `1925.00` | 248,100,000.00 USD | 0.00 USD | 16,590,000.00 USD | `-13.87%` | `8,619.79` |
| `Live` | `Long` | `1935.00` | 231,510,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-13.43%` | `569.98` |
| `Live` | `Long` | `1945.00` | 230,410,000.00 USD | 0.00 USD | 1,370,000.00 USD | `-12.98%` | `703.06` |
| `Live` | `Long` | `1955.00` | 229,040,000.00 USD | 0.00 USD | 2,920,000.00 USD | `-12.53%` | `1,495.67` |
| `Live` | `Long` | `1965.00` | 226,110,000.00 USD | 0.00 USD | 5,640,000.00 USD | `-12.08%` | `2,869.99` |
| `Live` | `Long` | `1975.00` | 220,470,000.00 USD | 0.00 USD | 1,430,000.00 USD | `-11.64%` | `721.82` |
| `Live` | `Long` | `1985.00` | 219,050,000.00 USD | 0.00 USD | 5,530,000.00 USD | `-11.19%` | `2,786.84` |
| `Live` | `Long` | `1995.00` | 213,520,000.00 USD | 0.00 USD | 1,640,000.00 USD | `-10.74%` | `822.74` |
| `Live` | `Long` | `2005.00` | 211,880,000.00 USD | 0.00 USD | 14,200,000.00 USD | `-10.29%` | `7,080.02` |
| `Live` | `Long` | `2015.00` | 197,680,000.00 USD | 0.00 USD | 3,300,000.00 USD | `-9.85%` | `1,635.95` |
| `Live` | `Long` | `2025.00` | 194,380,000.00 USD | 0.00 USD | 923,670.00 USD | `-9.40%` | `456.13` |
| `Live` | `Long` | `2035.00` | 193,460,000.00 USD | 0.00 USD | 606,700.00 USD | `-8.95%` | `298.13` |
| `Live` | `Long` | `2045.00` | 192,850,000.00 USD | 0.00 USD | 1,800,000.00 USD | `-8.51%` | `881.41` |
| `Live` | `Long` | `2055.00` | 191,050,000.00 USD | 0.00 USD | 7,150,000.00 USD | `-8.06%` | `3,479.76` |
| `Live` | `Long` | `2065.00` | 183,900,000.00 USD | 0.00 USD | 14,220,000.00 USD | `-7.61%` | `6,887.90` |
| `Live` | `Long` | `2075.00` | 169,680,000.00 USD | 0.00 USD | 1,540,000.00 USD | `-7.16%` | `742.14` |
| `Live` | `Long` | `2085.00` | 168,140,000.00 USD | 0.00 USD | 13,750,000.00 USD | `-6.72%` | `6,594.10` |
| `Live` | `Long` | `2095.00` | 154,390,000.00 USD | 0.00 USD | 1,810,000.00 USD | `-6.27%` | `864.74` |
| `Live` | `Long` | `2105.00` | 152,580,000.00 USD | 0.00 USD | 2,320,000.00 USD | `-5.82%` | `1,102.04` |
| `Live` | `Long` | `2115.00` | 150,260,000.00 USD | 0.00 USD | 1,970,000.00 USD | `-5.37%` | `929.61` |
| `Live` | `Long` | `2125.00` | 148,290,000.00 USD | 0.00 USD | 123,220,000.00 USD | `-4.93%` | `57,985.68` |
| `Live` | `Long` | `2135.00` | 25,070,000.00 USD | 0.00 USD | 5,550,000.00 USD | `-4.48%` | `2,598.87` |
| `Live` | `Long` | `2145.00` | 19,520,000.00 USD | 0.00 USD | 1,600,000.00 USD | `-4.03%` | `745.98` |
| `Live` | `Long` | `2155.00` | 17,920,000.00 USD | 0.00 USD | 2,930,000.00 USD | `-3.58%` | `1,358.75` |
| `Live` | `Long` | `2165.00` | 14,990,000.00 USD | 0.00 USD | 5,980,000.00 USD | `-3.14%` | `2,760.95` |
| `Live` | `Long` | `2175.00` | 9,020,000.00 USD | 0.00 USD | 5,790,000.00 USD | `-2.69%` | `2,662.66` |
| `Live` | `Long` | `2185.00` | 3,220,000.00 USD | 0.00 USD | 574,460.00 USD | `-2.24%` | `262.91` |
| `Live` | `Long` | `2195.00` | 2,650,000.00 USD | 0.00 USD | 1,990,000.00 USD | `-1.79%` | `904.93` |
| `Live` | `Long` | `2205.00` | 664,180.00 USD | 0.00 USD | 663,550.00 USD | `-1.35%` | `300.93` |
| `Live` | `Long` | `2215.00` | 628.26 USD | 0.00 USD | 412.88 USD | `-0.90%` | `0.19` |
| `Live` | `Long` | `2225.00` | 215.38 USD | 0.00 USD | 215.38 USD | `-0.45%` | `0.10` |
| `Live` | `Short` | `2235.00` | 497.96 USD | 497.96 USD | 0.00 USD | `-0.00%` | `0.22` |
| `Live` | `Short` | `2255.00` | 20,260.00 USD | 19,760.00 USD | 0.00 USD | `+0.89%` | `8.76` |
| `Live` | `Short` | `2265.00` | 30,320.00 USD | 10,060.00 USD | 0.00 USD | `+1.34%` | `4.44` |
| `Live` | `Short` | `2275.00` | 124,920.00 USD | 94,600.00 USD | 0.00 USD | `+1.79%` | `41.58` |
| `Live` | `Short` | `2285.00` | 294,730.00 USD | 169,810.00 USD | 0.00 USD | `+2.23%` | `74.31` |
| `Live` | `Short` | `2295.00` | 4,720,000.00 USD | 4,430,000.00 USD | 0.00 USD | `+2.68%` | `1,930.37` |
| `Live` | `Short` | `2305.00` | 8,590,000.00 USD | 3,870,000.00 USD | 0.00 USD | `+3.13%` | `1,677.49` |
| `Live` | `Short` | `2315.00` | 9,450,000.00 USD | 862,340.00 USD | 0.00 USD | `+3.57%` | `372.50` |
| `Live` | `Short` | `2325.00` | 11,380,000.00 USD | 1,930,000.00 USD | 0.00 USD | `+4.02%` | `828.93` |
| `Live` | `Short` | `2335.00` | 11,870,000.00 USD | 485,570.00 USD | 0.00 USD | `+4.47%` | `207.95` |
| `Live` | `Short` | `2345.00` | 12,630,000.00 USD | 767,790.00 USD | 0.00 USD | `+4.92%` | `327.42` |
| `Live` | `Short` | `2355.00` | 14,050,000.00 USD | 1,410,000.00 USD | 0.00 USD | `+5.36%` | `600.22` |
| `Live` | `Short` | `2365.00` | 17,990,000.00 USD | 3,940,000.00 USD | 0.00 USD | `+5.81%` | `1,664.99` |
| `Live` | `Short` | `2375.00` | 20,220,000.00 USD | 2,240,000.00 USD | 0.00 USD | `+6.26%` | `941.67` |
| `Live` | `Short` | `2385.00` | 25,770,000.00 USD | 5,550,000.00 USD | 0.00 USD | `+6.71%` | `2,326.93` |
| `Live` | `Short` | `2395.00` | 25,790,000.00 USD | 13,960.00 USD | 0.00 USD | `+7.15%` | `5.83` |
| `Live` | `Short` | `2405.00` | 25,920,000.00 USD | 133,330.00 USD | 0.00 USD | `+7.60%` | `55.44` |
| `Live` | `Short` | `2415.00` | 26,620,000.00 USD | 698,300.00 USD | 0.00 USD | `+8.05%` | `289.15` |
| `Live` | `Short` | `2425.00` | 26,830,000.00 USD | 215,570.00 USD | 0.00 USD | `+8.50%` | `88.89` |
| `Live` | `Short` | `2435.00` | 27,020,000.00 USD | 183,230.00 USD | 0.00 USD | `+8.94%` | `75.25` |
| `Live` | `Short` | `2445.00` | 27,120,000.00 USD | 105,580.00 USD | 0.00 USD | `+9.39%` | `43.18` |
| `Live` | `Short` | `2455.00` | 27,760,000.00 USD | 638,010.00 USD | 0.00 USD | `+9.84%` | `259.88` |
| `Live` | `Short` | `2465.00` | 93,540,000.00 USD | 65,780,000.00 USD | 0.00 USD | `+10.29%` | `26,684.24` |
| `Live` | `Short` | `2475.00` | 98,760,000.00 USD | 5,220,000.00 USD | 0.00 USD | `+10.73%` | `2,110.02` |
| `Live` | `Short` | `2485.00` | 98,810,000.00 USD | 47,080.00 USD | 0.00 USD | `+11.18%` | `18.95` |
| `Live` | `Short` | `2495.00` | 100,530,000.00 USD | 1,720,000.00 USD | 0.00 USD | `+11.63%` | `689.82` |
| `Live` | `Short` | `2505.00` | 107,130,000.00 USD | 6,600,000.00 USD | 0.00 USD | `+12.08%` | `2,635.75` |
| `Live` | `Short` | `2515.00` | 108,650,000.00 USD | 1,520,000.00 USD | 0.00 USD | `+12.52%` | `604.40` |
| `Live` | `Short` | `2525.00` | 108,700,000.00 USD | 49,110.00 USD | 0.00 USD | `+12.97%` | `19.45` |
| `Live` | `Short` | `2535.00` | 109,600,000.00 USD | 902,070.00 USD | 0.00 USD | `+13.42%` | `355.85` |
| `Live` | `Short` | `2545.00` | 114,740,000.00 USD | 5,140,000.00 USD | 0.00 USD | `+13.87%` | `2,020.59` |
| `Live` | `Short` | `2555.00` | 114,920,000.00 USD | 178,910.00 USD | 0.00 USD | `+14.31%` | `70.02` |
| `Live` | `Short` | `2565.00` | 114,970,000.00 USD | 47,080.00 USD | 0.00 USD | `+14.76%` | `18.36` |
| `Live` | `Short` | `2575.00` | 115,070,000.00 USD | 98,600.00 USD | 0.00 USD | `+15.21%` | `38.29` |
| `Live` | `Short` | `2585.00` | 141,960,000.00 USD | 26,890,000.00 USD | 0.00 USD | `+15.65%` | `10,403.50` |
| `Live` | `Short` | `2595.00` | 149,950,000.00 USD | 7,990,000.00 USD | 0.00 USD | `+16.10%` | `3,079.62` |
| `Live` | `Short` | `2605.00` | 155,890,000.00 USD | 5,940,000.00 USD | 0.00 USD | `+16.55%` | `2,278.48` |
| `Live` | `Short` | `2615.00` | 156,580,000.00 USD | 693,160.00 USD | 0.00 USD | `+17.00%` | `265.07` |
| `Live` | `Short` | `2625.00` | 189,480,000.00 USD | 32,900,000.00 USD | 0.00 USD | `+17.44%` | `12,531.95` |
| `Live` | `Short` | `2635.00` | 209,870,000.00 USD | 20,390,000.00 USD | 0.00 USD | `+17.89%` | `7,739.38` |
| `Live` | `Short` | `2645.00` | 210,510,000.00 USD | 636,110.00 USD | 0.00 USD | `+18.34%` | `240.49` |
| `Live` | `Short` | `2655.00` | 236,660,000.00 USD | 26,160,000.00 USD | 0.00 USD | `+18.79%` | `9,851.64` |
| `Live` | `Short` | `2665.00` | 237,250,000.00 USD | 590,500.00 USD | 0.00 USD | `+19.23%` | `221.58` |
| `Live` | `Short` | `2675.00` | 241,630,000.00 USD | 4,380,000.00 USD | 0.00 USD | `+19.68%` | `1,635.72` |
| `Live` | `Short` | `2685.00` | 241,740,000.00 USD | 115,800.00 USD | 0.00 USD | `+20.13%` | `43.13` |
| `Live` | `Short` | `2695.00` | 241,820,000.00 USD | 77,870.00 USD | 0.00 USD | `+20.58%` | `28.90` |
| `Live` | `Short` | `2705.00` | 242,450,000.00 USD | 631,700.00 USD | 0.00 USD | `+21.02%` | `233.53` |
| `Live` | `Short` | `2715.00` | 242,600,000.00 USD | 142,740.00 USD | 0.00 USD | `+21.47%` | `52.58` |
| `Live` | `Short` | `2725.00` | 243,020,000.00 USD | 427,530.00 USD | 0.00 USD | `+21.92%` | `156.89` |
| `Live` | `Short` | `2735.00` | 243,180,000.00 USD | 156,260.00 USD | 0.00 USD | `+22.37%` | `57.13` |
| `Live` | `Short` | `2745.00` | 243,910,000.00 USD | 727,130.00 USD | 0.00 USD | `+22.81%` | `264.89` |
| `Live` | `Short` | `2755.00` | 249,650,000.00 USD | 5,750,000.00 USD | 0.00 USD | `+23.26%` | `2,085.69` |
| `Live` | `Short` | `2765.00` | 255,180,000.00 USD | 5,530,000.00 USD | 0.00 USD | `+23.71%` | `1,998.99` |
| `Live` | `Short` | `2775.00` | 268,650,000.00 USD | 13,470,000.00 USD | 0.00 USD | `+24.16%` | `4,854.40` |
| `Live` | `Short` | `2785.00` | 268,680,000.00 USD | 32,450.00 USD | 0.00 USD | `+24.60%` | `11.65` |
| `Live` | `Short` | `2795.00` | 285,040,000.00 USD | 16,360,000.00 USD | 0.00 USD | `+25.05%` | `5,853.42` |
| `Live` | `Short` | `2805.00` | 289,400,000.00 USD | 4,350,000.00 USD | 0.00 USD | `+25.50%` | `1,551.98` |
| `Live` | `Short` | `2815.00` | 290,550,000.00 USD | 1,160,000.00 USD | 0.00 USD | `+25.95%` | `410.88` |
| `Live` | `Short` | `2825.00` | 291,090,000.00 USD | 535,360.00 USD | 0.00 USD | `+26.39%` | `189.51` |
| `Live` | `Short` | `2835.00` | 297,100,000.00 USD | 6,010,000.00 USD | 0.00 USD | `+26.84%` | `2,119.34` |
| `Live` | `Short` | `2845.00` | 297,640,000.00 USD | 542,980.00 USD | 0.00 USD | `+27.29%` | `190.85` |
| `Live` | `Short` | `2855.00` | 298,020,000.00 USD | 376,680.00 USD | 0.00 USD | `+27.73%` | `131.94` |
| `Live` | `Short` | `2865.00` | 298,110,000.00 USD | 92,670.00 USD | 0.00 USD | `+28.18%` | `32.34` |
| `Live` | `Short` | `2875.00` | 298,250,000.00 USD | 141,320.00 USD | 0.00 USD | `+28.63%` | `49.15` |
| `Live` | `Short` | `2885.00` | 299,190,000.00 USD | 935,060.00 USD | 0.00 USD | `+29.08%` | `324.11` |
| `Live` | `Short` | `2895.00` | 314,730,000.00 USD | 15,540,000.00 USD | 0.00 USD | `+29.52%` | `5,367.91` |
| `Live` | `Short` | `2905.00` | 341,600,000.00 USD | 26,880,000.00 USD | 0.00 USD | `+29.97%` | `9,252.12` |
| `Live` | `Short` | `2915.00` | 344,260,000.00 USD | 2,660,000.00 USD | 0.00 USD | `+30.42%` | `911.50` |
| `Live` | `Short` | `2925.00` | 345,150,000.00 USD | 890,390.00 USD | 0.00 USD | `+30.87%` | `304.41` |
| `Live` | `Short` | `2935.00` | 345,180,000.00 USD | 31,460.00 USD | 0.00 USD | `+31.31%` | `10.72` |
| `Live` | `Short` | `2945.00` | 345,630,000.00 USD | 449,420.00 USD | 0.00 USD | `+31.76%` | `152.61` |
| `Live` | `Short` | `2955.00` | 345,840,000.00 USD | 205,630.00 USD | 0.00 USD | `+32.21%` | `69.59` |
| `Live` | `Short` | `2965.00` | 349,750,000.00 USD | 3,910,000.00 USD | 0.00 USD | `+32.66%` | `1,317.89` |
| `Live` | `Short` | `2975.00` | 349,840,000.00 USD | 95,430.00 USD | 0.00 USD | `+33.10%` | `32.08` |
| `Live` | `Short` | `2985.00` | 351,120,000.00 USD | 1,280,000.00 USD | 0.00 USD | `+33.55%` | `427.83` |
| `Live` | `Short` | `2995.00` | 352,980,000.00 USD | 1,860,000.00 USD | 0.00 USD | `+34.00%` | `619.83` |
| `Live` | `Short` | `3005.00` | 354,120,000.00 USD | 1,140,000.00 USD | 0.00 USD | `+34.45%` | `380.06` |
| `Live` | `Short` | `3015.00` | 354,250,000.00 USD | 136,300.00 USD | 0.00 USD | `+34.89%` | `45.21` |
| `Live` | `Short` | `3025.00` | 356,780,000.00 USD | 2,530,000.00 USD | 0.00 USD | `+35.34%` | `836.62` |
| `Live` | `Short` | `3035.00` | 369,640,000.00 USD | 12,850,000.00 USD | 0.00 USD | `+35.79%` | `4,234.45` |
| `Live` | `Short` | `3045.00` | 369,720,000.00 USD | 82,000.00 USD | 0.00 USD | `+36.24%` | `26.93` |
| `Live` | `Short` | `3055.00` | 371,850,000.00 USD | 2,140,000.00 USD | 0.00 USD | `+36.68%` | `698.98` |
| `Live` | `Short` | `3065.00` | 371,870,000.00 USD | 13,620.00 USD | 0.00 USD | `+37.13%` | `4.44` |
| `Live` | `Short` | `3075.00` | 381,500,000.00 USD | 9,640,000.00 USD | 0.00 USD | `+37.58%` | `3,134.10` |
| `Live` | `Short` | `3085.00` | 383,700,000.00 USD | 2,200,000.00 USD | 0.00 USD | `+38.03%` | `712.23` |
| `Live` | `Short` | `3095.00` | 384,080,000.00 USD | 381,870.00 USD | 0.00 USD | `+38.47%` | `123.38` |
| `Live` | `Short` | `3105.00` | 398,230,000.00 USD | 14,150,000.00 USD | 0.00 USD | `+38.92%` | `4,556.27` |
| `Live` | `Short` | `3115.00` | 398,550,000.00 USD | 323,410.00 USD | 0.00 USD | `+39.37%` | `103.82` |
| `Live` | `Short` | `3125.00` | 398,920,000.00 USD | 364,040.00 USD | 0.00 USD | `+39.81%` | `116.49` |
| `Live` | `Short` | `3135.00` | 399,500,000.00 USD | 586,000.00 USD | 0.00 USD | `+40.26%` | `186.92` |
| `Live` | `Short` | `3145.00` | 428,930,000.00 USD | 29,430,000.00 USD | 0.00 USD | `+40.71%` | `9,357.50` |
| `Live` | `Short` | `3155.00` | 433,910,000.00 USD | 4,980,000.00 USD | 0.00 USD | `+41.16%` | `1,576.87` |
| `Live` | `Short` | `3165.00` | 434,090,000.00 USD | 180,110.00 USD | 0.00 USD | `+41.60%` | `56.91` |
| `Live` | `Short` | `3175.00` | 434,950,000.00 USD | 861,010.00 USD | 0.00 USD | `+42.05%` | `271.18` |
| `Live` | `Short` | `3185.00` | 441,860,000.00 USD | 6,910,000.00 USD | 0.00 USD | `+42.50%` | `2,168.51` |
| `Live` | `Short` | `3195.00` | 445,620,000.00 USD | 3,770,000.00 USD | 0.00 USD | `+42.95%` | `1,178.63` |
| `Live` | `Short` | `3205.00` | 445,760,000.00 USD | 141,980.00 USD | 0.00 USD | `+43.39%` | `44.30` |
| `Live` | `Short` | `3215.00` | 445,940,000.00 USD | 175,900.00 USD | 0.00 USD | `+43.84%` | `54.71` |
| `Live` | `Short` | `3225.00` | 454,200,000.00 USD | 8,260,000.00 USD | 0.00 USD | `+44.29%` | `2,561.10` |
| `Live` | `Short` | `3235.00` | 463,960,000.00 USD | 9,760,000.00 USD | 0.00 USD | `+44.74%` | `3,017.59` |
| `Live` | `Short` | `3245.00` | 464,140,000.00 USD | 182,560.00 USD | 0.00 USD | `+45.18%` | `56.26` |
| `Live` | `Short` | `3255.00` | 464,180,000.00 USD | 33,240.00 USD | 0.00 USD | `+45.63%` | `10.21` |
| `Live` | `Short` | `3265.00` | 466,200,000.00 USD | 2,020,000.00 USD | 0.00 USD | `+46.08%` | `619.35` |
| `Live` | `Short` | `3275.00` | 474,670,000.00 USD | 8,470,000.00 USD | 0.00 USD | `+46.53%` | `2,585.86` |
| `Live` | `Short` | `3285.00` | 474,740,000.00 USD | 72,510.00 USD | 0.00 USD | `+46.97%` | `22.07` |
| `Live` | `Short` | `3295.00` | 479,880,000.00 USD | 5,140,000.00 USD | 0.00 USD | `+47.42%` | `1,558.48` |
| `Live` | `Short` | `3305.00` | 482,580,000.00 USD | 2,700,000.00 USD | 0.00 USD | `+47.87%` | `817.04` |
| `Live` | `Short` | `3315.00` | 483,490,000.00 USD | 909,270.00 USD | 0.00 USD | `+48.32%` | `274.29` |
| `Live` | `Short` | `3325.00` | 483,570,000.00 USD | 87,690.00 USD | 0.00 USD | `+48.76%` | `26.37` |
| `Live` | `Short` | `3335.00` | 484,260,000.00 USD | 687,410.00 USD | 0.00 USD | `+49.21%` | `206.12` |
| `Live` | `Short` | `3345.00` | 485,640,000.00 USD | 1,380,000.00 USD | 0.00 USD | `+49.66%` | `413.61` |
| `Live` | `Short` | `3355.00` | 487,790,000.00 USD | 2,150,000.00 USD | 0.00 USD | `+50.11%` | `640.83` |
| `Live` | `Short` | `3365.00` | 487,910,000.00 USD | 118,210.00 USD | 0.00 USD | `+50.55%` | `35.13` |
| `Live` | `Short` | `3375.00` | 487,990,000.00 USD | 77,100.00 USD | 0.00 USD | `+51.00%` | `22.84` |
| `Live` | `Short` | `3385.00` | 493,990,000.00 USD | 6,000,000.00 USD | 0.00 USD | `+51.45%` | `1,771.65` |
| `Live` | `Short` | `3395.00` | 495,190,000.00 USD | 1,210,000.00 USD | 0.00 USD | `+51.89%` | `355.73` |
| `Live` | `Short` | `3405.00` | 495,380,000.00 USD | 186,760.00 USD | 0.00 USD | `+52.34%` | `54.85` |
| `Live` | `Short` | `3415.00` | 497,720,000.00 USD | 2,340,000.00 USD | 0.00 USD | `+52.79%` | `686.14` |
| `Live` | `Short` | `3425.00` | 512,450,000.00 USD | 14,720,000.00 USD | 0.00 USD | `+53.24%` | `4,299.22` |
| `Live` | `Short` | `3435.00` | 513,570,000.00 USD | 1,120,000.00 USD | 0.00 USD | `+53.68%` | `327.32` |
| `Live` | `Short` | `3445.00` | 514,130,000.00 USD | 561,170.00 USD | 0.00 USD | `+54.13%` | `162.89` |
| `Live` | `Short` | `3455.00` | 514,620,000.00 USD | 486,520.00 USD | 0.00 USD | `+54.58%` | `140.82` |
| `Live` | `Short` | `3465.00` | 514,790,000.00 USD | 166,590.00 USD | 0.00 USD | `+55.03%` | `48.08` |
| `Live` | `Short` | `3475.00` | 572,830,000.00 USD | 58,040,000.00 USD | 0.00 USD | `+55.47%` | `16,701.51` |
| `Live` | `Short` | `3485.00` | 573,480,000.00 USD | 658,610.00 USD | 0.00 USD | `+55.92%` | `188.98` |
| `Live` | `Short` | `3495.00` | 575,580,000.00 USD | 2,100,000.00 USD | 0.00 USD | `+56.37%` | `600.75` |
| `Live` | `Short` | `3505.00` | 576,440,000.00 USD | 860,620.00 USD | 0.00 USD | `+56.82%` | `245.54` |
| `Live` | `Short` | `3515.00` | 576,450,000.00 USD | 6,450.00 USD | 0.00 USD | `+57.26%` | `1.84` |
| `Live` | `Short` | `3525.00` | 621,740,000.00 USD | 45,290,000.00 USD | 0.00 USD | `+57.71%` | `12,847.91` |
| `Live` | `Short` | `3535.00` | 621,990,000.00 USD | 255,300.00 USD | 0.00 USD | `+58.16%` | `72.22` |
| `Live` | `Short` | `3545.00` | 622,070,000.00 USD | 77,430.00 USD | 0.00 USD | `+58.61%` | `21.84` |
| `Live` | `Short` | `3555.00` | 622,330,000.00 USD | 255,740.00 USD | 0.00 USD | `+59.05%` | `71.94` |
| `Live` | `Short` | `3565.00` | 622,840,000.00 USD | 507,900.00 USD | 0.00 USD | `+59.50%` | `142.47` |
| `Live` | `Short` | `3575.00` | 622,950,000.00 USD | 118,760.00 USD | 0.00 USD | `+59.95%` | `33.22` |
| `Live` | `Short` | `3585.00` | 623,720,000.00 USD | 761,910.00 USD | 0.00 USD | `+60.40%` | `212.53` |
| `Live` | `Short` | `3595.00` | 623,750,000.00 USD | 31,380.00 USD | 0.00 USD | `+60.84%` | `8.73` |
| `Live` | `Short` | `3605.00` | 623,800,000.00 USD | 47,860.00 USD | 0.00 USD | `+61.29%` | `13.28` |
| `Live` | `Short` | `3615.00` | 627,440,000.00 USD | 3,640,000.00 USD | 0.00 USD | `+61.74%` | `1,007.19` |
| `Live` | `Short` | `3625.00` | 628,010,000.00 USD | 568,820.00 USD | 0.00 USD | `+62.19%` | `156.92` |
| `Live` | `Short` | `3635.00` | 636,750,000.00 USD | 8,740,000.00 USD | 0.00 USD | `+62.63%` | `2,404.89` |
| `Live` | `Short` | `3645.00` | 636,770,000.00 USD | 22,040.00 USD | 0.00 USD | `+63.08%` | `6.05` |
| `Live` | `Short` | `3655.00` | 636,790,000.00 USD | 24,470.00 USD | 0.00 USD | `+63.53%` | `6.70` |
| `Live` | `Short` | `3665.00` | 643,620,000.00 USD | 6,820,000.00 USD | 0.00 USD | `+63.97%` | `1,862.09` |
| `Live` | `Short` | `3675.00` | 643,690,000.00 USD | 76,200.00 USD | 0.00 USD | `+64.42%` | `20.73` |
| `Live` | `Short` | `3685.00` | 643,910,000.00 USD | 212,440.00 USD | 0.00 USD | `+64.87%` | `57.65` |
| `Live` | `Short` | `3695.00` | 643,940,000.00 USD | 30,730.00 USD | 0.00 USD | `+65.32%` | `8.32` |
| `Live` | `Short` | `3705.00` | 644,340,000.00 USD | 399,380.00 USD | 0.00 USD | `+65.76%` | `107.80` |
| `Live` | `Short` | `3715.00` | 645,670,000.00 USD | 1,330,000.00 USD | 0.00 USD | `+66.21%` | `358.87` |
| `Live` | `Short` | `3725.00` | 646,130,000.00 USD | 460,700.00 USD | 0.00 USD | `+66.66%` | `123.68` |
| `Live` | `Short` | `3735.00` | 646,490,000.00 USD | 360,470.00 USD | 0.00 USD | `+67.11%` | `96.51` |
| `Live` | `Short` | `3745.00` | 647,330,000.00 USD | 839,100.00 USD | 0.00 USD | `+67.55%` | `224.06` |
| `Live` | `Short` | `3755.00` | 647,590,000.00 USD | 259,520.00 USD | 0.00 USD | `+68.00%` | `69.11` |
| `Live` | `Short` | `3765.00` | 649,560,000.00 USD | 1,970,000.00 USD | 0.00 USD | `+68.45%` | `524.08` |
| `Live` | `Short` | `3775.00` | 649,870,000.00 USD | 302,220.00 USD | 0.00 USD | `+68.90%` | `80.06` |
| `Live` | `Short` | `3785.00` | 650,050,000.00 USD | 189,510.00 USD | 0.00 USD | `+69.34%` | `50.07` |
| `Live` | `Short` | `3795.00` | 652,650,000.00 USD | 2,590,000.00 USD | 0.00 USD | `+69.79%` | `682.59` |
| `Live` | `Short` | `3805.00` | 1,060,000,000.00 USD | 410,440,000.00 USD | 0.00 USD | `+70.24%` | `107,867.54` |
| `Live` | `Short` | `3815.00` | 1,060,000,000.00 USD | 100.33 USD | 0.00 USD | `+70.69%` | `0.03` |
| `Live` | `Short` | `3825.00` | 1,070,000,000.00 USD | 1,980,000.00 USD | 0.00 USD | `+71.13%` | `517.86` |
| `Live` | `Short` | `3835.00` | 1,070,000,000.00 USD | 378,000.00 USD | 0.00 USD | `+71.58%` | `98.56` |
| `Live` | `Short` | `3845.00` | 1,070,000,000.00 USD | 299.14 USD | 0.00 USD | `+72.03%` | `0.08` |
| `Live` | `Short` | `3855.00` | 1,070,000,000.00 USD | 1,170,000.00 USD | 0.00 USD | `+72.48%` | `303.54` |
| `Live` | `Short` | `3865.00` | 1,070,000,000.00 USD | 651,040.00 USD | 0.00 USD | `+72.92%` | `168.44` |
| `Live` | `Short` | `3875.00` | 1,100,000,000.00 USD | 35,590,000.00 USD | 0.00 USD | `+73.37%` | `9,183.53` |
| `Live` | `Short` | `3885.00` | 1,100,000,000.00 USD | 1,360,000.00 USD | 0.00 USD | `+73.82%` | `350.13` |
| `Live` | `Short` | `3895.00` | 1,110,000,000.00 USD | 2,520,000.00 USD | 0.00 USD | `+74.27%` | `646.74` |
| `Live` | `Short` | `3905.00` | 1,110,000,000.00 USD | 1,220,000.00 USD | 0.00 USD | `+74.71%` | `311.94` |
| `Live` | `Short` | `3915.00` | 1,110,000,000.00 USD | 20,140.00 USD | 0.00 USD | `+75.16%` | `5.14` |
| `Live` | `Short` | `3925.00` | 1,110,000,000.00 USD | 148,130.00 USD | 0.00 USD | `+75.61%` | `37.74` |
| `Live` | `Short` | `3935.00` | 1,110,000,000.00 USD | 4,920.00 USD | 0.00 USD | `+76.05%` | `1.25` |
| `Live` | `Short` | `3945.00` | 1,110,000,000.00 USD | 88,410.00 USD | 0.00 USD | `+76.50%` | `22.41` |
| `Live` | `Short` | `3955.00` | 1,110,000,000.00 USD | 2,020,000.00 USD | 0.00 USD | `+76.95%` | `510.64` |
| `Live` | `Short` | `3965.00` | 1,110,000,000.00 USD | 74,010.00 USD | 0.00 USD | `+77.40%` | `18.67` |
| `Live` | `Short` | `3975.00` | 1,110,000,000.00 USD | 201,740.00 USD | 0.00 USD | `+77.84%` | `50.75` |
| `Live` | `Short` | `3985.00` | 1,170,000,000.00 USD | 63,150,000.00 USD | 0.00 USD | `+78.29%` | `15,845.79` |
| `Live` | `Short` | `3995.00` | 1,170,000,000.00 USD | 1,040,000.00 USD | 0.00 USD | `+78.74%` | `260.72` |
| `Live` | `Short` | `4005.00` | 1,170,000,000.00 USD | 62,810.00 USD | 0.00 USD | `+79.19%` | `15.68` |
| `Live` | `Short` | `4015.00` | 1,170,000,000.00 USD | 85,510.00 USD | 0.00 USD | `+79.63%` | `21.30` |
| `Live` | `Short` | `4025.00` | 1,170,000,000.00 USD | 131,080.00 USD | 0.00 USD | `+80.08%` | `32.57` |
| `Live` | `Short` | `4035.00` | 1,180,000,000.00 USD | 364,900.00 USD | 0.00 USD | `+80.53%` | `90.43` |
| `Live` | `Short` | `4045.00` | 1,180,000,000.00 USD | 80,660.00 USD | 0.00 USD | `+80.98%` | `19.94` |
| `Live` | `Short` | `4055.00` | 1,180,000,000.00 USD | 1,970,000.00 USD | 0.00 USD | `+81.42%` | `485.72` |
| `Live` | `Short` | `4065.00` | 1,180,000,000.00 USD | 1,230,000.00 USD | 0.00 USD | `+81.87%` | `301.38` |
| `Live` | `Short` | `4075.00` | 1,180,000,000.00 USD | 70,020.00 USD | 0.00 USD | `+82.32%` | `17.18` |
| `Live` | `Short` | `4085.00` | 1,180,000,000.00 USD | 2,230.00 USD | 0.00 USD | `+82.77%` | `0.55` |
| `Live` | `Short` | `4095.00` | 1,180,000,000.00 USD | 9,520.00 USD | 0.00 USD | `+83.21%` | `2.32` |
| `Live` | `Short` | `4105.00` | 1,180,000,000.00 USD | 2,610,000.00 USD | 0.00 USD | `+83.66%` | `634.76` |
| `Live` | `Short` | `4115.00` | 1,180,000,000.00 USD | 3,300.00 USD | 0.00 USD | `+84.11%` | `0.80` |
| `Live` | `Short` | `4125.00` | 1,180,000,000.00 USD | 283,580.00 USD | 0.00 USD | `+84.56%` | `68.75` |
| `Live` | `Short` | `4135.00` | 1,180,000,000.00 USD | 678,960.00 USD | 0.00 USD | `+85.00%` | `164.20` |
| `Live` | `Short` | `4145.00` | 1,180,000,000.00 USD | 232,930.00 USD | 0.00 USD | `+85.45%` | `56.20` |
| `Live` | `Short` | `4155.00` | 1,180,000,000.00 USD | 175,260.00 USD | 0.00 USD | `+85.90%` | `42.18` |
| `Live` | `Short` | `4165.00` | 1,180,000,000.00 USD | 206,800.00 USD | 0.00 USD | `+86.35%` | `49.65` |
| `Live` | `Short` | `4175.00` | 1,180,000,000.00 USD | 837,830.00 USD | 0.00 USD | `+86.79%` | `200.68` |
| `Live` | `Short` | `4185.00` | 1,270,000,000.00 USD | 83,610,000.00 USD | 0.00 USD | `+87.24%` | `19,977.62` |
| `Live` | `Short` | `4195.00` | 1,270,000,000.00 USD | 5,670,000.00 USD | 0.00 USD | `+87.69%` | `1,352.17` |
| `Live` | `Short` | `4205.00` | 1,300,000,000.00 USD | 28,680,000.00 USD | 0.00 USD | `+88.13%` | `6,819.54` |
| `Live` | `Short` | `4215.00` | 1,300,000,000.00 USD | 447.21 USD | 0.00 USD | `+88.58%` | `0.11` |
| `Live` | `Short` | `4225.00` | 1,300,000,000.00 USD | 7,020.00 USD | 0.00 USD | `+89.03%` | `1.66` |
| `Live` | `Short` | `4235.00` | 1,300,000,000.00 USD | 776,260.00 USD | 0.00 USD | `+89.48%` | `183.30` |
| `Live` | `Short` | `4245.00` | 1,300,000,000.00 USD | 3,980.00 USD | 0.00 USD | `+89.92%` | `0.94` |
| `Live` | `Short` | `4255.00` | 1,310,000,000.00 USD | 5,400,000.00 USD | 0.00 USD | `+90.37%` | `1,270.04` |
| `Live` | `Short` | `4265.00` | 1,310,000,000.00 USD | 58,530.00 USD | 0.00 USD | `+90.82%` | `13.72` |
| `Live` | `Short` | `4275.00` | 1,310,000,000.00 USD | 7,630.00 USD | 0.00 USD | `+91.27%` | `1.79` |
| `Live` | `Short` | `4285.00` | 1,310,000,000.00 USD | 187,650.00 USD | 0.00 USD | `+91.71%` | `43.79` |
| `Live` | `Short` | `4295.00` | 1,310,000,000.00 USD | 4,510,000.00 USD | 0.00 USD | `+92.16%` | `1,049.24` |
| `Live` | `Short` | `4305.00` | 1,310,000,000.00 USD | 5,450.00 USD | 0.00 USD | `+92.61%` | `1.27` |
| `Live` | `Short` | `4315.00` | 1,310,000,000.00 USD | 47,050.00 USD | 0.00 USD | `+93.06%` | `10.90` |
| `Live` | `Short` | `4325.00` | 1,310,000,000.00 USD | 557,660.00 USD | 0.00 USD | `+93.50%` | `128.94` |
| `Live` | `Short` | `4335.00` | 1,310,000,000.00 USD | 211,680.00 USD | 0.00 USD | `+93.95%` | `48.83` |
| `Live` | `Short` | `4345.00` | 1,310,000,000.00 USD | 14,450.00 USD | 0.00 USD | `+94.40%` | `3.33` |
| `Live` | `Short` | `4355.00` | 1,600,000,000.00 USD | 281,690,000.00 USD | 0.00 USD | `+94.85%` | `64,682.17` |
| `Live` | `Short` | `4365.00` | 1,600,000,000.00 USD | 547,470.00 USD | 0.00 USD | `+95.29%` | `125.42` |
| `Live` | `Short` | `4375.00` | 1,600,000,000.00 USD | 464,420.00 USD | 0.00 USD | `+95.74%` | `106.15` |
| `Live` | `Short` | `4385.00` | 1,600,000,000.00 USD | 117.96 USD | 0.00 USD | `+96.19%` | `0.03` |
| `Live` | `Short` | `4395.00` | 1,600,000,000.00 USD | 15,230.00 USD | 0.00 USD | `+96.64%` | `3.46` |
| `Live` | `Short` | `4405.00` | 1,600,000,000.00 USD | 175,600.00 USD | 0.00 USD | `+97.08%` | `39.86` |
| `Live` | `Short` | `4415.00` | 1,600,000,000.00 USD | 56,700.00 USD | 0.00 USD | `+97.53%` | `12.84` |
| `Live` | `Short` | `4425.00` | 1,600,000,000.00 USD | 97,080.00 USD | 0.00 USD | `+97.98%` | `21.94` |
| `Live` | `Short` | `4445.00` | 1,600,000,000.00 USD | 446,720.00 USD | 0.00 USD | `+98.87%` | `100.50` |
| `Live` | `Short` | `4455.00` | 1,600,000,000.00 USD | 11,510.00 USD | 0.00 USD | `+99.32%` | `2.58` |
| `Live` | `Short` | `4465.00` | 1,600,000,000.00 USD | 24,920.00 USD | 0.00 USD | `+99.77%` | `5.58` |
| `Live` | `Short` | `4475.00` | 1,600,000,000.00 USD | 58,650.00 USD | 0.00 USD | `+100.21%` | `13.11` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `485.00` | 73,390,000.00 USD | 0.00 USD | 278.83 USD | `-78.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `505.00` | 73,390,000.00 USD | 0.00 USD | 16,130.00 USD | `-77.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.00` | 73,380,000.00 USD | 0.00 USD | 563.16 USD | `-75.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.00` | 73,380,000.00 USD | 0.00 USD | 583.40 USD | `-71.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `655.00` | 73,380,000.00 USD | 0.00 USD | 16,690.00 USD | `-70.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.00` | 73,360,000.00 USD | 0.00 USD | 578.54 USD | `-69.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.00` | 73,360,000.00 USD | 0.00 USD | 242.21 USD | `-68.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.00` | 73,360,000.00 USD | 0.00 USD | 885.90 USD | `-68.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `755.00` | 73,360,000.00 USD | 0.00 USD | 177.27 USD | `-66.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `805.00` | 73,360,000.00 USD | 0.00 USD | 2,400.00 USD | `-63.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `835.00` | 73,360,000.00 USD | 0.00 USD | 1,670.00 USD | `-62.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `865.00` | 73,350,000.00 USD | 0.00 USD | 139,430.00 USD | `-61.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `875.00` | 73,220,000.00 USD | 0.00 USD | 918.49 USD | `-60.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `885.00` | 73,210,000.00 USD | 0.00 USD | 3,130.00 USD | `-60.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `905.00` | 73,210,000.00 USD | 0.00 USD | 2,780.00 USD | `-59.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `985.00` | 73,210,000.00 USD | 0.00 USD | 516.34 USD | `-55.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `995.00` | 73,210,000.00 USD | 0.00 USD | 100.50 USD | `-55.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1005.00` | 73,210,000.00 USD | 0.00 USD | 223,740.00 USD | `-55.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1015.00` | 72,980,000.00 USD | 0.00 USD | 445.08 USD | `-54.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1025.00` | 72,980,000.00 USD | 0.00 USD | 112.03 USD | `-54.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1045.00` | 72,980,000.00 USD | 0.00 USD | 1,260.00 USD | `-53.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1065.00` | 72,980,000.00 USD | 0.00 USD | 1,060.00 USD | `-52.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1075.00` | 72,980,000.00 USD | 0.00 USD | 995.34 USD | `-51.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1105.00` | 72,980,000.00 USD | 0.00 USD | 1,610.00 USD | `-50.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1115.00` | 72,980,000.00 USD | 0.00 USD | 11,050.00 USD | `-50.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1125.00` | 72,970,000.00 USD | 0.00 USD | 1,320.00 USD | `-49.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1155.00` | 72,970,000.00 USD | 0.00 USD | 1,000.00 USD | `-48.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1175.00` | 72,970,000.00 USD | 0.00 USD | 476.46 USD | `-47.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1185.00` | 72,960,000.00 USD | 0.00 USD | 972.41 USD | `-46.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1195.00` | 72,960,000.00 USD | 0.00 USD | 221.55 USD | `-46.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1205.00` | 72,960,000.00 USD | 0.00 USD | 3,110.00 USD | `-46.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1225.00` | 72,960,000.00 USD | 0.00 USD | 995.93 USD | `-45.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1245.00` | 72,960,000.00 USD | 0.00 USD | 951.93 USD | `-44.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1255.00` | 72,960,000.00 USD | 0.00 USD | 2,290.00 USD | `-43.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1285.00` | 72,960,000.00 USD | 0.00 USD | 9,050.00 USD | `-42.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1295.00` | 72,950,000.00 USD | 0.00 USD | 7,030.00 USD | `-42.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1305.00` | 72,940,000.00 USD | 0.00 USD | 25,040.00 USD | `-41.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1315.00` | 72,910,000.00 USD | 0.00 USD | 1,440.00 USD | `-41.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1335.00` | 72,910,000.00 USD | 0.00 USD | 281.69 USD | `-40.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1345.00` | 72,910,000.00 USD | 0.00 USD | 141,950.00 USD | `-39.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1355.00` | 72,770,000.00 USD | 0.00 USD | 128.86 USD | `-39.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1365.00` | 72,770,000.00 USD | 0.00 USD | 1,270.00 USD | `-38.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1375.00` | 72,770,000.00 USD | 0.00 USD | 4,160.00 USD | `-38.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1385.00` | 72,770,000.00 USD | 0.00 USD | 100,800.00 USD | `-38.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1395.00` | 72,660,000.00 USD | 0.00 USD | 535,600.00 USD | `-37.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1405.00` | 72,130,000.00 USD | 0.00 USD | 18,840.00 USD | `-37.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1425.00` | 72,110,000.00 USD | 0.00 USD | 6,450.00 USD | `-36.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1435.00` | 72,100,000.00 USD | 0.00 USD | 852.10 USD | `-35.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1445.00` | 72,100,000.00 USD | 0.00 USD | 1,610.00 USD | `-35.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1455.00` | 72,100,000.00 USD | 0.00 USD | 5,090.00 USD | `-34.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1465.00` | 72,100,000.00 USD | 0.00 USD | 19,730.00 USD | `-34.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1475.00` | 72,080,000.00 USD | 0.00 USD | 2,600.00 USD | `-34.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1485.00` | 72,070,000.00 USD | 0.00 USD | 19,930.00 USD | `-33.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1495.00` | 72,050,000.00 USD | 0.00 USD | 11,460.00 USD | `-33.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1505.00` | 72,040,000.00 USD | 0.00 USD | 70,590.00 USD | `-32.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1515.00` | 71,970,000.00 USD | 0.00 USD | 11,140.00 USD | `-32.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1525.00` | 71,960,000.00 USD | 0.00 USD | 31,900.00 USD | `-31.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1535.00` | 71,930,000.00 USD | 0.00 USD | 2,090.00 USD | `-31.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1545.00` | 71,930,000.00 USD | 0.00 USD | 960.99 USD | `-30.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1555.00` | 71,930,000.00 USD | 0.00 USD | 25,420.00 USD | `-30.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1565.00` | 71,900,000.00 USD | 0.00 USD | 10,660.00 USD | `-29.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1575.00` | 71,890,000.00 USD | 0.00 USD | 198,620.00 USD | `-29.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1585.00` | 71,690,000.00 USD | 0.00 USD | 4,990.00 USD | `-29.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1595.00` | 71,690,000.00 USD | 0.00 USD | 7,240.00 USD | `-28.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1605.00` | 71,680,000.00 USD | 0.00 USD | 431,660.00 USD | `-28.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1615.00` | 71,250,000.00 USD | 0.00 USD | 25,700.00 USD | `-27.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1625.00` | 71,220,000.00 USD | 0.00 USD | 15,920.00 USD | `-27.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1635.00` | 71,210,000.00 USD | 0.00 USD | 10,560.00 USD | `-26.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1645.00` | 71,200,000.00 USD | 0.00 USD | 323,930.00 USD | `-26.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1655.00` | 70,870,000.00 USD | 0.00 USD | 114,830.00 USD | `-25.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1665.00` | 70,760,000.00 USD | 0.00 USD | 865.13 USD | `-25.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1675.00` | 70,760,000.00 USD | 0.00 USD | 289.27 USD | `-25.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1685.00` | 70,760,000.00 USD | 0.00 USD | 35,320.00 USD | `-24.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1695.00` | 70,720,000.00 USD | 0.00 USD | 42,420.00 USD | `-24.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1705.00` | 70,680,000.00 USD | 0.00 USD | 84,860.00 USD | `-23.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1715.00` | 70,590,000.00 USD | 0.00 USD | 16,350.00 USD | `-23.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1725.00` | 70,580,000.00 USD | 0.00 USD | 47,500.00 USD | `-22.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1735.00` | 70,530,000.00 USD | 0.00 USD | 28,150.00 USD | `-22.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1745.00` | 70,500,000.00 USD | 0.00 USD | 3,180.00 USD | `-21.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1755.00` | 70,500,000.00 USD | 0.00 USD | 466,520.00 USD | `-21.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1765.00` | 70,030,000.00 USD | 0.00 USD | 77,450.00 USD | `-21.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1775.00` | 69,950,000.00 USD | 0.00 USD | 3,090.00 USD | `-20.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1785.00` | 69,950,000.00 USD | 0.00 USD | 8,500.00 USD | `-20.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1795.00` | 69,940,000.00 USD | 0.00 USD | 191,050.00 USD | `-19.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1805.00` | 69,750,000.00 USD | 0.00 USD | 737,430.00 USD | `-19.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1815.00` | 69,010,000.00 USD | 0.00 USD | 263,270.00 USD | `-18.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1825.00` | 68,750,000.00 USD | 0.00 USD | 39,660.00 USD | `-18.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1835.00` | 68,710,000.00 USD | 0.00 USD | 5,320.00 USD | `-17.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1845.00` | 68,710,000.00 USD | 0.00 USD | 30,780.00 USD | `-17.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1855.00` | 68,670,000.00 USD | 0.00 USD | 789,490.00 USD | `-17.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1865.00` | 67,890,000.00 USD | 0.00 USD | 43,120.00 USD | `-16.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1875.00` | 67,840,000.00 USD | 0.00 USD | 18,200,000.00 USD | `-16.11%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1885.00` | 49,640,000.00 USD | 0.00 USD | 17,580.00 USD | `-15.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1895.00` | 49,630,000.00 USD | 0.00 USD | 61,630.00 USD | `-15.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1905.00` | 49,570,000.00 USD | 0.00 USD | 148,960.00 USD | `-14.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1915.00` | 49,420,000.00 USD | 0.00 USD | 104,860.00 USD | `-14.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1925.00` | 49,310,000.00 USD | 0.00 USD | 19,310,000.00 USD | `-13.87%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `1935.00` | 30,010,000.00 USD | 0.00 USD | 107,770.00 USD | `-13.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1945.00` | 29,900,000.00 USD | 0.00 USD | 61,020.00 USD | `-12.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1955.00` | 29,840,000.00 USD | 0.00 USD | 65,650.00 USD | `-12.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1965.00` | 29,770,000.00 USD | 0.00 USD | 138,620.00 USD | `-12.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1975.00` | 29,630,000.00 USD | 0.00 USD | 74,320.00 USD | `-11.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1985.00` | 29,560,000.00 USD | 0.00 USD | 105,590.00 USD | `-11.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1995.00` | 29,450,000.00 USD | 0.00 USD | 125,460.00 USD | `-10.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2005.00` | 29,330,000.00 USD | 0.00 USD | 2,080,000.00 USD | `-10.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2015.00` | 27,240,000.00 USD | 0.00 USD | 48,350.00 USD | `-9.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2025.00` | 27,190,000.00 USD | 0.00 USD | 15,730.00 USD | `-9.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2035.00` | 27,180,000.00 USD | 0.00 USD | 177,750.00 USD | `-8.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2045.00` | 27,000,000.00 USD | 0.00 USD | 12,210.00 USD | `-8.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2055.00` | 26,990,000.00 USD | 0.00 USD | 273,500.00 USD | `-8.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2065.00` | 26,710,000.00 USD | 0.00 USD | 814,210.00 USD | `-7.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2075.00` | 25,900,000.00 USD | 0.00 USD | 161,070.00 USD | `-7.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2085.00` | 25,740,000.00 USD | 0.00 USD | 135,860.00 USD | `-6.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2095.00` | 25,600,000.00 USD | 0.00 USD | 34,710.00 USD | `-6.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2105.00` | 25,570,000.00 USD | 0.00 USD | 481,360.00 USD | `-5.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2115.00` | 25,090,000.00 USD | 0.00 USD | 161,500.00 USD | `-5.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2125.00` | 24,930,000.00 USD | 0.00 USD | 147,510.00 USD | `-4.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2135.00` | 24,780,000.00 USD | 0.00 USD | 347,360.00 USD | `-4.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2145.00` | 24,430,000.00 USD | 0.00 USD | 378,740.00 USD | `-4.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2155.00` | 24,050,000.00 USD | 0.00 USD | 2,270,000.00 USD | `-3.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2165.00` | 21,790,000.00 USD | 0.00 USD | 4,720,000.00 USD | `-3.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2175.00` | 17,070,000.00 USD | 0.00 USD | 9,610,000.00 USD | `-2.69%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `2185.00` | 7,460,000.00 USD | 0.00 USD | 130,780.00 USD | `-2.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2195.00` | 7,330,000.00 USD | 0.00 USD | 2,870,000.00 USD | `-1.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2205.00` | 4,460,000.00 USD | 0.00 USD | 862,500.00 USD | `-1.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2215.00` | 3,590,000.00 USD | 0.00 USD | 2,250,000.00 USD | `-0.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2225.00` | 1,350,000.00 USD | 0.00 USD | 1,250,000.00 USD | `-0.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2235.00` | 95,680.00 USD | 0.00 USD | 95,680.00 USD | `-0.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2245.00` | 111,420.00 USD | 111,420.00 USD | 0.00 USD | `+0.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2255.00` | 909,710.00 USD | 798,290.00 USD | 0.00 USD | `+0.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2265.00` | 2,810,000.00 USD | 1,900,000.00 USD | 0.00 USD | `+1.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2275.00` | 3,060,000.00 USD | 249,390.00 USD | 0.00 USD | `+1.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2285.00` | 3,900,000.00 USD | 845,360.00 USD | 0.00 USD | `+2.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2295.00` | 4,370,000.00 USD | 461,220.00 USD | 0.00 USD | `+2.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2305.00` | 14,310,000.00 USD | 9,950,000.00 USD | 0.00 USD | `+3.13%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2315.00` | 15,810,000.00 USD | 1,500,000.00 USD | 0.00 USD | `+3.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2325.00` | 16,020,000.00 USD | 205,370.00 USD | 0.00 USD | `+4.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2335.00` | 16,200,000.00 USD | 182,220.00 USD | 0.00 USD | `+4.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2345.00` | 17,760,000.00 USD | 1,560,000.00 USD | 0.00 USD | `+4.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2355.00` | 19,080,000.00 USD | 1,310,000.00 USD | 0.00 USD | `+5.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2365.00` | 21,250,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+5.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2375.00` | 21,400,000.00 USD | 147,230.00 USD | 0.00 USD | `+6.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2385.00` | 23,360,000.00 USD | 1,960,000.00 USD | 0.00 USD | `+6.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2395.00` | 24,470,000.00 USD | 1,110,000.00 USD | 0.00 USD | `+7.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2405.00` | 26,970,000.00 USD | 2,490,000.00 USD | 0.00 USD | `+7.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2415.00` | 27,220,000.00 USD | 250,590.00 USD | 0.00 USD | `+8.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2425.00` | 29,410,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+8.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2435.00` | 29,600,000.00 USD | 184,810.00 USD | 0.00 USD | `+8.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2445.00` | 32,090,000.00 USD | 2,490,000.00 USD | 0.00 USD | `+9.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2455.00` | 32,230,000.00 USD | 141,370.00 USD | 0.00 USD | `+9.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2465.00` | 34,350,000.00 USD | 2,120,000.00 USD | 0.00 USD | `+10.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2475.00` | 34,530,000.00 USD | 184,150.00 USD | 0.00 USD | `+10.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2485.00` | 36,640,000.00 USD | 2,100,000.00 USD | 0.00 USD | `+11.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2495.00` | 36,830,000.00 USD | 190,130.00 USD | 0.00 USD | `+11.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2505.00` | 41,880,000.00 USD | 5,060,000.00 USD | 0.00 USD | `+12.08%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2515.00` | 49,480,000.00 USD | 7,600,000.00 USD | 0.00 USD | `+12.52%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `2525.00` | 52,100,000.00 USD | 2,620,000.00 USD | 0.00 USD | `+12.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2535.00` | 52,160,000.00 USD | 61,230.00 USD | 0.00 USD | `+13.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2545.00` | 54,340,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+13.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2555.00` | 54,560,000.00 USD | 218,500.00 USD | 0.00 USD | `+14.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2565.00` | 56,910,000.00 USD | 2,360,000.00 USD | 0.00 USD | `+14.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2575.00` | 57,010,000.00 USD | 93,110.00 USD | 0.00 USD | `+15.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2585.00` | 59,520,000.00 USD | 2,510,000.00 USD | 0.00 USD | `+15.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2595.00` | 59,530,000.00 USD | 10,500.00 USD | 0.00 USD | `+16.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2605.00` | 62,810,000.00 USD | 3,280,000.00 USD | 0.00 USD | `+16.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2615.00` | 62,890,000.00 USD | 79,030.00 USD | 0.00 USD | `+17.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2625.00` | 65,070,000.00 USD | 2,180,000.00 USD | 0.00 USD | `+17.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2635.00` | 65,220,000.00 USD | 147,930.00 USD | 0.00 USD | `+17.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2645.00` | 67,340,000.00 USD | 2,120,000.00 USD | 0.00 USD | `+18.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2655.00` | 67,650,000.00 USD | 306,950.00 USD | 0.00 USD | `+18.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2665.00` | 69,790,000.00 USD | 2,140,000.00 USD | 0.00 USD | `+19.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2675.00` | 70,050,000.00 USD | 261,420.00 USD | 0.00 USD | `+19.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2685.00` | 72,230,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+20.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2695.00` | 72,320,000.00 USD | 94,620.00 USD | 0.00 USD | `+20.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2705.00` | 75,170,000.00 USD | 2,850,000.00 USD | 0.00 USD | `+21.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2715.00` | 75,240,000.00 USD | 78,290.00 USD | 0.00 USD | `+21.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2725.00` | 75,530,000.00 USD | 286,910.00 USD | 0.00 USD | `+21.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2735.00` | 75,570,000.00 USD | 43,050.00 USD | 0.00 USD | `+22.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2745.00` | 75,750,000.00 USD | 178,210.00 USD | 0.00 USD | `+22.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2755.00` | 76,650,000.00 USD | 892,870.00 USD | 0.00 USD | `+23.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2765.00` | 76,750,000.00 USD | 103,020.00 USD | 0.00 USD | `+23.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2775.00` | 77,330,000.00 USD | 577,610.00 USD | 0.00 USD | `+24.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2785.00` | 77,360,000.00 USD | 35,580.00 USD | 0.00 USD | `+24.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2795.00` | 77,380,000.00 USD | 17,550.00 USD | 0.00 USD | `+25.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2805.00` | 78,290,000.00 USD | 907,290.00 USD | 0.00 USD | `+25.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2815.00` | 78,340,000.00 USD | 52,870.00 USD | 0.00 USD | `+25.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2825.00` | 78,380,000.00 USD | 43,930.00 USD | 0.00 USD | `+26.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2835.00` | 78,670,000.00 USD | 286,140.00 USD | 0.00 USD | `+26.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2845.00` | 79,670,000.00 USD | 1,000,000.00 USD | 0.00 USD | `+27.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2855.00` | 80,940,000.00 USD | 1,270,000.00 USD | 0.00 USD | `+27.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2865.00` | 80,960,000.00 USD | 11,150.00 USD | 0.00 USD | `+28.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2875.00` | 80,960,000.00 USD | 2,460.00 USD | 0.00 USD | `+28.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2885.00` | 81,260,000.00 USD | 305,820.00 USD | 0.00 USD | `+29.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2895.00` | 81,280,000.00 USD | 16,190.00 USD | 0.00 USD | `+29.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2905.00` | 82,770,000.00 USD | 1,480,000.00 USD | 0.00 USD | `+29.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2915.00` | 82,780,000.00 USD | 10,340.00 USD | 0.00 USD | `+30.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2925.00` | 82,780,000.00 USD | 3,050.00 USD | 0.00 USD | `+30.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2935.00` | 82,830,000.00 USD | 52,370.00 USD | 0.00 USD | `+31.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2945.00` | 82,870,000.00 USD | 34,650.00 USD | 0.00 USD | `+31.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2955.00` | 82,910,000.00 USD | 43,460.00 USD | 0.00 USD | `+32.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2965.00` | 83,020,000.00 USD | 113,340.00 USD | 0.00 USD | `+32.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2975.00` | 83,170,000.00 USD | 145,510.00 USD | 0.00 USD | `+33.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2985.00` | 84,100,000.00 USD | 931,470.00 USD | 0.00 USD | `+33.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2995.00` | 89,020,000.00 USD | 4,920,000.00 USD | 0.00 USD | `+34.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3005.00` | 91,190,000.00 USD | 2,170,000.00 USD | 0.00 USD | `+34.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3015.00` | 91,200,000.00 USD | 9,740.00 USD | 0.00 USD | `+34.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3025.00` | 91,230,000.00 USD | 35,380.00 USD | 0.00 USD | `+35.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3035.00` | 91,310,000.00 USD | 74,910.00 USD | 0.00 USD | `+35.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3045.00` | 91,330,000.00 USD | 22,460.00 USD | 0.00 USD | `+36.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3055.00` | 92,100,000.00 USD | 771,070.00 USD | 0.00 USD | `+36.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3065.00` | 92,100,000.00 USD | 612.69 USD | 0.00 USD | `+37.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3075.00` | 92,150,000.00 USD | 49,500.00 USD | 0.00 USD | `+37.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3085.00` | 92,170,000.00 USD | 19,570.00 USD | 0.00 USD | `+38.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3095.00` | 92,170,000.00 USD | 928.50 USD | 0.00 USD | `+38.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3105.00` | 104,130,000.00 USD | 11,960,000.00 USD | 0.00 USD | `+38.92%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `3115.00` | 104,240,000.00 USD | 110,480.00 USD | 0.00 USD | `+39.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3125.00` | 104,620,000.00 USD | 381,020.00 USD | 0.00 USD | `+39.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3145.00` | 104,620,000.00 USD | 2,660.00 USD | 0.00 USD | `+40.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3155.00` | 104,680,000.00 USD | 58,930.00 USD | 0.00 USD | `+41.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3165.00` | 104,690,000.00 USD | 9,860.00 USD | 0.00 USD | `+41.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3175.00` | 104,690,000.00 USD | 149.22 USD | 0.00 USD | `+42.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3185.00` | 104,690,000.00 USD | 1,330.00 USD | 0.00 USD | `+42.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3195.00` | 104,730,000.00 USD | 41,120.00 USD | 0.00 USD | `+42.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3205.00` | 105,390,000.00 USD | 658,320.00 USD | 0.00 USD | `+43.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3215.00` | 105,400,000.00 USD | 2,400.00 USD | 0.00 USD | `+43.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3225.00` | 105,550,000.00 USD | 156,230.00 USD | 0.00 USD | `+44.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3235.00` | 105,550,000.00 USD | 167.25 USD | 0.00 USD | `+44.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3245.00` | 105,610,000.00 USD | 57,500.00 USD | 0.00 USD | `+45.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3255.00` | 105,850,000.00 USD | 236,580.00 USD | 0.00 USD | `+45.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3265.00` | 105,860,000.00 USD | 15,710.00 USD | 0.00 USD | `+46.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3275.00` | 105,860,000.00 USD | 1,630.00 USD | 0.00 USD | `+46.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3285.00` | 106,010,000.00 USD | 141,980.00 USD | 0.00 USD | `+46.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3295.00` | 106,020,000.00 USD | 15,350.00 USD | 0.00 USD | `+47.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3305.00` | 107,430,000.00 USD | 1,410,000.00 USD | 0.00 USD | `+47.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3315.00` | 107,820,000.00 USD | 389,970.00 USD | 0.00 USD | `+48.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3325.00` | 107,850,000.00 USD | 24,200.00 USD | 0.00 USD | `+48.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3335.00` | 107,850,000.00 USD | 4,350.00 USD | 0.00 USD | `+49.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3345.00` | 107,850,000.00 USD | 2,170.00 USD | 0.00 USD | `+49.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3355.00` | 107,860,000.00 USD | 2,520.00 USD | 0.00 USD | `+50.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3365.00` | 107,860,000.00 USD | 2,780.00 USD | 0.00 USD | `+50.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3375.00` | 107,880,000.00 USD | 21,260.00 USD | 0.00 USD | `+51.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3385.00` | 107,940,000.00 USD | 58,140.00 USD | 0.00 USD | `+51.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3395.00` | 108,260,000.00 USD | 321,800.00 USD | 0.00 USD | `+51.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3405.00` | 109,770,000.00 USD | 1,510,000.00 USD | 0.00 USD | `+52.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3415.00` | 109,780,000.00 USD | 5,700.00 USD | 0.00 USD | `+52.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3425.00` | 109,800,000.00 USD | 16,310.00 USD | 0.00 USD | `+53.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3445.00` | 109,810,000.00 USD | 15,030.00 USD | 0.00 USD | `+54.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3455.00` | 109,830,000.00 USD | 18,600.00 USD | 0.00 USD | `+54.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3465.00` | 109,830,000.00 USD | 495.50 USD | 0.00 USD | `+55.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3475.00` | 109,830,000.00 USD | 3,190.00 USD | 0.00 USD | `+55.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3485.00` | 109,880,000.00 USD | 43,610.00 USD | 0.00 USD | `+55.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3495.00` | 109,880,000.00 USD | 158.32 USD | 0.00 USD | `+56.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3505.00` | 110,320,000.00 USD | 446,770.00 USD | 0.00 USD | `+56.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3515.00` | 110,370,000.00 USD | 43,460.00 USD | 0.00 USD | `+57.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3525.00` | 110,370,000.00 USD | 3,690.00 USD | 0.00 USD | `+57.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3535.00` | 110,380,000.00 USD | 9,810.00 USD | 0.00 USD | `+58.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3555.00` | 110,470,000.00 USD | 90,810.00 USD | 0.00 USD | `+59.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3565.00` | 110,470,000.00 USD | 2,300.00 USD | 0.00 USD | `+59.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3575.00` | 110,480,000.00 USD | 2,870.00 USD | 0.00 USD | `+59.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3585.00` | 110,480,000.00 USD | 354.92 USD | 0.00 USD | `+60.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3595.00` | 110,490,000.00 USD | 13,160.00 USD | 0.00 USD | `+60.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3605.00` | 110,590,000.00 USD | 101,080.00 USD | 0.00 USD | `+61.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3615.00` | 110,590,000.00 USD | 199.55 USD | 0.00 USD | `+61.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3625.00` | 110,600,000.00 USD | 10,210.00 USD | 0.00 USD | `+62.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3635.00` | 110,610,000.00 USD | 7,790.00 USD | 0.00 USD | `+62.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3645.00` | 110,610,000.00 USD | 3,860.00 USD | 0.00 USD | `+63.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3655.00` | 110,620,000.00 USD | 8,090.00 USD | 0.00 USD | `+63.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3665.00` | 110,630,000.00 USD | 8,130.00 USD | 0.00 USD | `+63.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3675.00` | 110,690,000.00 USD | 55,120.00 USD | 0.00 USD | `+64.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3685.00` | 110,690,000.00 USD | 1,410.00 USD | 0.00 USD | `+64.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3705.00` | 110,690,000.00 USD | 819.92 USD | 0.00 USD | `+65.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3715.00` | 110,690,000.00 USD | 323.58 USD | 0.00 USD | `+66.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3725.00` | 110,690,000.00 USD | 1,400.00 USD | 0.00 USD | `+66.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3735.00` | 110,700,000.00 USD | 6,490.00 USD | 0.00 USD | `+67.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3745.00` | 110,700,000.00 USD | 165.90 USD | 0.00 USD | `+67.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3755.00` | 110,700,000.00 USD | 751.00 USD | 0.00 USD | `+68.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3785.00` | 110,700,000.00 USD | 286.90 USD | 0.00 USD | `+69.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3795.00` | 110,700,000.00 USD | 1,560.00 USD | 0.00 USD | `+69.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3805.00` | 111,430,000.00 USD | 732,630.00 USD | 0.00 USD | `+70.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3815.00` | 111,450,000.00 USD | 20,930.00 USD | 0.00 USD | `+70.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3825.00` | 111,460,000.00 USD | 8,380.00 USD | 0.00 USD | `+71.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3835.00` | 111,460,000.00 USD | 711.78 USD | 0.00 USD | `+71.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3845.00` | 111,460,000.00 USD | 355.28 USD | 0.00 USD | `+72.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3855.00` | 111,470,000.00 USD | 5,170.00 USD | 0.00 USD | `+72.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3885.00` | 111,490,000.00 USD | 19,430.00 USD | 0.00 USD | `+73.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3905.00` | 111,500,000.00 USD | 12,120.00 USD | 0.00 USD | `+74.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3915.00` | 112,220,000.00 USD | 717,170.00 USD | 0.00 USD | `+75.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3935.00` | 112,260,000.00 USD | 42,570.00 USD | 0.00 USD | `+76.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3945.00` | 112,320,000.00 USD | 59,170.00 USD | 0.00 USD | `+76.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3955.00` | 112,320,000.00 USD | 1,380.00 USD | 0.00 USD | `+76.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3975.00` | 112,330,000.00 USD | 6,960.00 USD | 0.00 USD | `+77.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3985.00` | 112,340,000.00 USD | 14,610.00 USD | 0.00 USD | `+78.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `3995.00` | 112,340,000.00 USD | 4,280.00 USD | 0.00 USD | `+78.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4005.00` | 114,980,000.00 USD | 2,640,000.00 USD | 0.00 USD | `+79.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4035.00` | 114,980,000.00 USD | 898.59 USD | 0.00 USD | `+80.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4055.00` | 114,980,000.00 USD | 811.00 USD | 0.00 USD | `+81.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4075.00` | 114,990,000.00 USD | 4,310.00 USD | 0.00 USD | `+82.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4085.00` | 114,990,000.00 USD | 3,050.00 USD | 0.00 USD | `+82.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4105.00` | 115,030,000.00 USD | 36,740.00 USD | 0.00 USD | `+83.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4115.00` | 115,030,000.00 USD | 5,990.00 USD | 0.00 USD | `+84.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4125.00` | 115,030,000.00 USD | 372.90 USD | 0.00 USD | `+84.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4145.00` | 115,030,000.00 USD | 395.43 USD | 0.00 USD | `+85.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4185.00` | 115,030,000.00 USD | 376.65 USD | 0.00 USD | `+87.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4205.00` | 115,080,000.00 USD | 42,260.00 USD | 0.00 USD | `+88.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4215.00` | 115,080,000.00 USD | 460.70 USD | 0.00 USD | `+88.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4225.00` | 115,080,000.00 USD | 1,270.00 USD | 0.00 USD | `+89.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4255.00` | 115,080,000.00 USD | 4,300.00 USD | 0.00 USD | `+90.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4265.00` | 115,080,000.00 USD | 437.16 USD | 0.00 USD | `+90.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4275.00` | 115,150,000.00 USD | 64,550.00 USD | 0.00 USD | `+91.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4285.00` | 115,150,000.00 USD | 1,610.00 USD | 0.00 USD | `+91.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4305.00` | 115,240,000.00 USD | 94,600.00 USD | 0.00 USD | `+92.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4315.00` | 115,250,000.00 USD | 1,070.00 USD | 0.00 USD | `+93.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4345.00` | 115,260,000.00 USD | 11,270.00 USD | 0.00 USD | `+94.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4355.00` | 115,260,000.00 USD | 2,400.00 USD | 0.00 USD | `+94.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4375.00` | 115,300,000.00 USD | 43,750.00 USD | 0.00 USD | `+95.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4385.00` | 115,370,000.00 USD | 64,570.00 USD | 0.00 USD | `+96.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4395.00` | 115,370,000.00 USD | 1,050.00 USD | 0.00 USD | `+96.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4405.00` | 115,660,000.00 USD | 296,830.00 USD | 0.00 USD | `+97.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4415.00` | 115,680,000.00 USD | 11,480.00 USD | 0.00 USD | `+97.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4425.00` | 115,680,000.00 USD | 2,510.00 USD | 0.00 USD | `+97.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4435.00` | 115,860,000.00 USD | 177,400.00 USD | 0.00 USD | `+98.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4455.00` | 115,860,000.00 USD | 2,040.00 USD | 0.00 USD | `+99.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4465.00` | 115,860,000.00 USD | 1,030.00 USD | 0.00 USD | `+99.77%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1971.40` | 764,320,000.00 USD | 0.00 USD | 764,320,000.00 USD | 0.00 USD | 0.00 USD | 26,880.00 USD |
| `7D` | `1974.40` | 764,290,000.00 USD | 0.00 USD | 764,290,000.00 USD | 0.00 USD | 105,610.00 USD | 49,530.00 USD |
| `7D` | `1977.40` | 764,140,000.00 USD | 0.00 USD | 764,140,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1983.40` | 761,900,000.00 USD | 0.00 USD | 761,900,000.00 USD | 0.00 USD | 206,830.00 USD | 0.00 USD |
| `7D` | `1986.40` | 761,690,000.00 USD | 0.00 USD | 761,690,000.00 USD | 3,730,000.00 USD | 1,780,000.00 USD | 0.00 USD |
| `7D` | `1989.40` | 756,190,000.00 USD | 0.00 USD | 756,190,000.00 USD | 0.00 USD | 1,320,000.00 USD | 38,060.00 USD |
| `7D` | `1992.40` | 754,830,000.00 USD | 0.00 USD | 754,830,000.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1995.40` | 753,440,000.00 USD | 0.00 USD | 753,440,000.00 USD | 1,340,000.00 USD | 0.00 USD | 808,380.00 USD |
| `1D` | `2000.30` | 647,650,000.00 USD | 0.00 USD | 647,650,000.00 USD | 16,160.00 USD | 80,240.00 USD | 497,140.00 USD |
| `1D` | `2002.80` | 647,060,000.00 USD | 0.00 USD | 647,060,000.00 USD | 0.00 USD | 455,960.00 USD | 7,040.00 USD |
| `7D` | `2004.40` | 751,290,000.00 USD | 0.00 USD | 751,290,000.00 USD | 0.00 USD | 266,430.00 USD | 0.00 USD |
| `1D` | `2005.30` | 646,590,000.00 USD | 0.00 USD | 646,590,000.00 USD | 493,990.00 USD | 13,410.00 USD | 0.00 USD |
| `7D` | `2007.40` | 751,020,000.00 USD | 0.00 USD | 751,020,000.00 USD | 807,770.00 USD | 42,980.00 USD | 0.00 USD |
| `1D` | `2007.80` | 646,090,000.00 USD | 0.00 USD | 646,090,000.00 USD | 0.00 USD | 431,390.00 USD | 126,940.00 USD |
| `1D` | `2010.30` | 645,530,000.00 USD | 0.00 USD | 645,530,000.00 USD | 484,920.00 USD | 490,130.00 USD | 362,200.00 USD |
| `7D` | `2010.40` | 750,170,000.00 USD | 0.00 USD | 750,170,000.00 USD | 170,840.00 USD | 92,470.00 USD | 689,450.00 USD |
| `1D` | `2012.80` | 644,190,000.00 USD | 0.00 USD | 644,190,000.00 USD | 323,800.00 USD | 239,210.00 USD | 25,520.00 USD |
| `1D` | `2015.30` | 643,600,000.00 USD | 0.00 USD | 643,600,000.00 USD | 355,800.00 USD | 159,880.00 USD | 194,190.00 USD |
| `1D` | `2017.80` | 642,890,000.00 USD | 0.00 USD | 642,890,000.00 USD | 537,580.00 USD | 1,360,000.00 USD | 553,080.00 USD |
| `7D` | `2019.40` | 749,220,000.00 USD | 0.00 USD | 749,220,000.00 USD | 0.00 USD | 0.00 USD | 21,830.00 USD |
| `1D` | `2020.30` | 640,440,000.00 USD | 0.00 USD | 640,440,000.00 USD | 548,260.00 USD | 1,150,000.00 USD | 696,790.00 USD |
| `7D` | `2022.40` | 749,200,000.00 USD | 0.00 USD | 749,200,000.00 USD | 0.00 USD | 0.00 USD | 934,340.00 USD |
| `1D` | `2022.80` | 638,040,000.00 USD | 0.00 USD | 638,040,000.00 USD | 1,160,000.00 USD | 312,480.00 USD | 1,570,000.00 USD |
| `1D` | `2025.30` | 635,000,000.00 USD | 0.00 USD | 635,000,000.00 USD | 414,330.00 USD | 1,190,000.00 USD | 231,680.00 USD |
| `7D` | `2025.40` | 748,260,000.00 USD | 0.00 USD | 748,260,000.00 USD | 1,070,000.00 USD | 177,070.00 USD | 0.00 USD |
| `1D` | `2027.80` | 633,160,000.00 USD | 0.00 USD | 633,160,000.00 USD | 2,770,000.00 USD | 978,910.00 USD | 312,840.00 USD |
| `7D` | `2028.40` | 747,020,000.00 USD | 0.00 USD | 747,020,000.00 USD | 1,100,000.00 USD | 0.00 USD | 35,180.00 USD |
| `1D` | `2030.30` | 629,100,000.00 USD | 0.00 USD | 629,100,000.00 USD | 87,180.00 USD | 366,120.00 USD | 957,140.00 USD |
| `7D` | `2031.40` | 745,880,000.00 USD | 0.00 USD | 745,880,000.00 USD | 0.00 USD | 3,520,000.00 USD | 1,050,000.00 USD |
| `1D` | `2032.80` | 627,690,000.00 USD | 0.00 USD | 627,690,000.00 USD | 1,360,000.00 USD | 1,490,000.00 USD | 707,170.00 USD |
| `7D` | `2034.40` | 741,310,000.00 USD | 0.00 USD | 741,310,000.00 USD | 0.00 USD | 0.00 USD | 1,350,000.00 USD |
| `1D` | `2035.30` | 624,130,000.00 USD | 0.00 USD | 624,130,000.00 USD | 1,150,000.00 USD | 19,490.00 USD | 165,760.00 USD |
| `7D` | `2037.40` | 739,960,000.00 USD | 0.00 USD | 739,960,000.00 USD | 146,420.00 USD | 186,130.00 USD | 0.00 USD |
| `1D` | `2037.80` | 622,800,000.00 USD | 0.00 USD | 622,800,000.00 USD | 396,700.00 USD | 458,110.00 USD | 388,420.00 USD |
| `1D` | `2040.30` | 621,550,000.00 USD | 0.00 USD | 621,550,000.00 USD | 834,710.00 USD | 178,560.00 USD | 21,940.00 USD |
| `7D` | `2040.40` | 739,620,000.00 USD | 0.00 USD | 739,620,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2042.80` | 620,520,000.00 USD | 0.00 USD | 620,520,000.00 USD | 334,790.00 USD | 0.00 USD | 174,920.00 USD |
| `7D` | `2043.40` | 738,170,000.00 USD | 0.00 USD | 738,170,000.00 USD | 0.00 USD | 0.00 USD | 149,910.00 USD |
| `1D` | `2045.30` | 620,010,000.00 USD | 0.00 USD | 620,010,000.00 USD | 0.00 USD | 0.00 USD | 27,710.00 USD |
| `7D` | `2046.40` | 738,020,000.00 USD | 0.00 USD | 738,020,000.00 USD | 0.00 USD | 149,500.00 USD | 0.00 USD |
| `1D` | `2047.80` | 619,980,000.00 USD | 0.00 USD | 619,980,000.00 USD | 467,370.00 USD | 0.00 USD | 357,950.00 USD |
| `7D` | `2049.40` | 737,870,000.00 USD | 0.00 USD | 737,870,000.00 USD | 222,640.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2050.30` | 619,150,000.00 USD | 0.00 USD | 619,150,000.00 USD | 51,070.00 USD | 338,980.00 USD | 717,780.00 USD |
| `7D` | `2052.40` | 737,650,000.00 USD | 0.00 USD | 737,650,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,190,000.00 USD |
| `1D` | `2055.30` | 618,050,000.00 USD | 0.00 USD | 618,050,000.00 USD | 242,080.00 USD | 88,880.00 USD | 28,160.00 USD |
| `7D` | `2058.40` | 735,360,000.00 USD | 0.00 USD | 735,360,000.00 USD | 153,480.00 USD | 189,640.00 USD | 0.00 USD |
| `1D` | `2060.30` | 617,690,000.00 USD | 0.00 USD | 617,690,000.00 USD | 0.00 USD | 0.00 USD | 755,050.00 USD |
| `7D` | `2061.40` | 735,020,000.00 USD | 0.00 USD | 735,020,000.00 USD | 1,600,000.00 USD | 1,940,000.00 USD | 1,710,000.00 USD |
| `1D` | `2062.80` | 616,930,000.00 USD | 0.00 USD | 616,930,000.00 USD | 0.00 USD | 59,640.00 USD | 20,330.00 USD |
| `7D` | `2064.40` | 729,770,000.00 USD | 0.00 USD | 729,770,000.00 USD | 1,230,000.00 USD | 249,960.00 USD | 945,860.00 USD |
| `1D` | `2065.30` | 616,850,000.00 USD | 0.00 USD | 616,850,000.00 USD | 563,140.00 USD | 537,030.00 USD | 510,200.00 USD |
| `7D` | `2067.40` | 727,330,000.00 USD | 0.00 USD | 727,330,000.00 USD | 292,400.00 USD | 1,120,000.00 USD | 262,430.00 USD |
| `1D` | `2067.80` | 615,240,000.00 USD | 0.00 USD | 615,240,000.00 USD | 387,410.00 USD | 304,560.00 USD | 0.00 USD |
| `1D` | `2070.30` | 614,550,000.00 USD | 0.00 USD | 614,550,000.00 USD | 57,300.00 USD | 319,490.00 USD | 0.00 USD |
| `7D` | `2070.40` | 725,660,000.00 USD | 0.00 USD | 725,660,000.00 USD | 3,600,000.00 USD | 2,730,000.00 USD | 1,880,000.00 USD |
| `1D` | `2072.80` | 614,170,000.00 USD | 0.00 USD | 614,170,000.00 USD | 47,910.00 USD | 555,250.00 USD | 420,170.00 USD |
| `7D` | `2073.40` | 717,450,000.00 USD | 0.00 USD | 717,450,000.00 USD | 3,300,000.00 USD | 2,180,000.00 USD | 2,050,000.00 USD |
| `1D` | `2075.30` | 613,150,000.00 USD | 0.00 USD | 613,150,000.00 USD | 379,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2076.40` | 709,920,000.00 USD | 0.00 USD | 709,920,000.00 USD | 5,230,000.00 USD | 5,030,000.00 USD | 3,680,000.00 USD |
| `1D` | `2077.80` | 612,770,000.00 USD | 0.00 USD | 612,770,000.00 USD | 0.00 USD | 25,190.00 USD | 0.00 USD |
| `7D` | `2079.40` | 695,980,000.00 USD | 0.00 USD | 695,980,000.00 USD | 4,150,000.00 USD | 3,020,000.00 USD | 3,130,000.00 USD |
| `1D` | `2080.30` | 612,740,000.00 USD | 0.00 USD | 612,740,000.00 USD | 116,140.00 USD | 29,610.00 USD | 200,920.00 USD |
| `7D` | `2082.40` | 685,680,000.00 USD | 0.00 USD | 685,680,000.00 USD | 2,640,000.00 USD | 1,860,000.00 USD | 1,930,000.00 USD |
| `1D` | `2082.80` | 612,400,000.00 USD | 0.00 USD | 612,400,000.00 USD | 827,940.00 USD | 4,240.00 USD | 211,520.00 USD |
| `1D` | `2085.30` | 611,350,000.00 USD | 0.00 USD | 611,350,000.00 USD | 691,080.00 USD | 207,610.00 USD | 821,110.00 USD |
| `7D` | `2085.40` | 679,240,000.00 USD | 0.00 USD | 679,240,000.00 USD | 4,090,000.00 USD | 1,860,000.00 USD | 3,840,000.00 USD |
| `1D` | `2087.80` | 609,630,000.00 USD | 0.00 USD | 609,630,000.00 USD | 525,540.00 USD | 573,160.00 USD | 440,740.00 USD |
| `7D` | `2088.40` | 669,450,000.00 USD | 0.00 USD | 669,450,000.00 USD | 2,280,000.00 USD | 1,820,000.00 USD | 907,940.00 USD |
| `1D` | `2090.30` | 608,100,000.00 USD | 0.00 USD | 608,100,000.00 USD | 761,770.00 USD | 217,840.00 USD | 451,040.00 USD |
| `7D` | `2091.40` | 664,440,000.00 USD | 0.00 USD | 664,440,000.00 USD | 4,410,000.00 USD | 952,210.00 USD | 7,590,000.00 USD |
| `1D` | `2092.80` | 606,660,000.00 USD | 0.00 USD | 606,660,000.00 USD | 752,390.00 USD | 342,580.00 USD | 395,890.00 USD |
| `7D` | `2094.40` | 651,480,000.00 USD | 0.00 USD | 651,480,000.00 USD | 5,720,000.00 USD | 1,660,000.00 USD | 2,340,000.00 USD |
| `1D` | `2095.30` | 605,170,000.00 USD | 0.00 USD | 605,170,000.00 USD | 1,840,000.00 USD | 1,130,000.00 USD | 1,690,000.00 USD |
| `7D` | `2097.40` | 641,760,000.00 USD | 0.00 USD | 641,760,000.00 USD | 1,830,000.00 USD | 3,580,000.00 USD | 1,290,000.00 USD |
| `1D` | `2097.80` | 600,510,000.00 USD | 0.00 USD | 600,510,000.00 USD | 187,470.00 USD | 488,160.00 USD | 309,770.00 USD |
| `1D` | `2100.30` | 599,520,000.00 USD | 0.00 USD | 599,520,000.00 USD | 295,710.00 USD | 928,890.00 USD | 50,560.00 USD |
| `7D` | `2100.40` | 635,060,000.00 USD | 0.00 USD | 635,060,000.00 USD | 1,830,000.00 USD | 1,850,000.00 USD | 3,310,000.00 USD |
| `1D` | `2102.80` | 598,240,000.00 USD | 0.00 USD | 598,240,000.00 USD | 211,840.00 USD | 222,480.00 USD | 483,690.00 USD |
| `7D` | `2103.40` | 628,070,000.00 USD | 0.00 USD | 628,070,000.00 USD | 679,880.00 USD | 554,710.00 USD | 2,250,000.00 USD |
| `1D` | `2105.30` | 597,330,000.00 USD | 0.00 USD | 597,330,000.00 USD | 3,570,000.00 USD | 1,160,000.00 USD | 833,200.00 USD |
| `7D` | `2106.40` | 624,580,000.00 USD | 0.00 USD | 624,580,000.00 USD | 1,660,000.00 USD | 986,590.00 USD | 1,960,000.00 USD |
| `1D` | `2107.80` | 591,760,000.00 USD | 0.00 USD | 591,760,000.00 USD | 734,860.00 USD | 0.00 USD | 347,020.00 USD |
| `7D` | `2109.40` | 619,980,000.00 USD | 0.00 USD | 619,980,000.00 USD | 8,310,000.00 USD | 1,830,000.00 USD | 1,770,000.00 USD |
| `1D` | `2110.30` | 590,680,000.00 USD | 0.00 USD | 590,680,000.00 USD | 61,010.00 USD | 31,550.00 USD | 6,190.00 USD |
| `7D` | `2112.40` | 608,080,000.00 USD | 0.00 USD | 608,080,000.00 USD | 3,920,000.00 USD | 1,480,000.00 USD | 3,710,000.00 USD |
| `1D` | `2112.80` | 590,580,000.00 USD | 0.00 USD | 590,580,000.00 USD | 902,600.00 USD | 506,690.00 USD | 244,160.00 USD |
| `1D` | `2115.30` | 588,930,000.00 USD | 0.00 USD | 588,930,000.00 USD | 410,020.00 USD | 400,200.00 USD | 939,960.00 USD |
| `7D` | `2115.40` | 598,960,000.00 USD | 0.00 USD | 598,960,000.00 USD | 923,330.00 USD | 3,210,000.00 USD | 1,930,000.00 USD |
| `1D` | `2117.80` | 587,180,000.00 USD | 0.00 USD | 587,180,000.00 USD | 4,540,000.00 USD | 3,940,000.00 USD | 302,800.00 USD |
| `7D` | `2118.40` | 592,890,000.00 USD | 0.00 USD | 592,890,000.00 USD | 8,390,000.00 USD | 639,610.00 USD | 2,840,000.00 USD |
| `1D` | `2120.30` | 578,390,000.00 USD | 0.00 USD | 578,390,000.00 USD | 5,430,000.00 USD | 325,610.00 USD | 671,270.00 USD |
| `7D` | `2121.40` | 581,020,000.00 USD | 0.00 USD | 581,020,000.00 USD | 8,120,000.00 USD | 5,720,000.00 USD | 1,670,000.00 USD |
| `1D` | `2122.80` | 571,960,000.00 USD | 0.00 USD | 571,960,000.00 USD | 4,680,000.00 USD | 3,490,000.00 USD | 2,070,000.00 USD |
| `7D` | `2124.40` | 565,520,000.00 USD | 0.00 USD | 565,520,000.00 USD | 7,730,000.00 USD | 8,120,000.00 USD | 1,550,000.00 USD |
| `1D` | `2125.30` | 561,710,000.00 USD | 0.00 USD | 561,710,000.00 USD | 5,280,000.00 USD | 1,830,000.00 USD | 1,870,000.00 USD |
| `7D` | `2127.40` | 548,120,000.00 USD | 0.00 USD | 548,120,000.00 USD | 1,600,000.00 USD | 4,460,000.00 USD | 5,290,000.00 USD |
| `1D` | `2127.80` | 552,720,000.00 USD | 0.00 USD | 552,720,000.00 USD | 4,430,000.00 USD | 4,330,000.00 USD | 782,350.00 USD |
| `1D` | `2130.30` | 543,170,000.00 USD | 0.00 USD | 543,170,000.00 USD | 1,230,000.00 USD | 18,610.00 USD | 1,110,000.00 USD |
| `7D` | `2130.40` | 536,760,000.00 USD | 0.00 USD | 536,760,000.00 USD | 5,390,000.00 USD | 2,130,000.00 USD | 1,690,000.00 USD |
| `1D` | `2132.80` | 540,820,000.00 USD | 0.00 USD | 540,820,000.00 USD | 0.00 USD | 177,810.00 USD | 1,250,000.00 USD |
| `7D` | `2133.40` | 527,540,000.00 USD | 0.00 USD | 527,540,000.00 USD | 2,120,000.00 USD | 715,940.00 USD | 323,430.00 USD |
| `1D` | `2135.30` | 539,390,000.00 USD | 0.00 USD | 539,390,000.00 USD | 41,690.00 USD | 1,170,000.00 USD | 43,360.00 USD |
| `7D` | `2136.40` | 524,380,000.00 USD | 0.00 USD | 524,380,000.00 USD | 1,170,000.00 USD | 845,110.00 USD | 43,560.00 USD |
| `1D` | `2137.80` | 538,140,000.00 USD | 0.00 USD | 538,140,000.00 USD | 17,770.00 USD | 1,040,000.00 USD | 0.00 USD |
| `7D` | `2139.40` | 522,320,000.00 USD | 0.00 USD | 522,320,000.00 USD | 1,110,000.00 USD | 1,780,000.00 USD | 409,160.00 USD |
| `1D` | `2140.30` | 537,080,000.00 USD | 0.00 USD | 537,080,000.00 USD | 1,370,000.00 USD | 945,770.00 USD | 64,360.00 USD |
| `7D` | `2142.40` | 519,030,000.00 USD | 0.00 USD | 519,030,000.00 USD | 4,320,000.00 USD | 1,100,000.00 USD | 661,260.00 USD |
| `1D` | `2142.80` | 534,700,000.00 USD | 0.00 USD | 534,700,000.00 USD | 1,080,000.00 USD | 2,500,000.00 USD | 1,050,000.00 USD |
| `1D` | `2145.30` | 530,080,000.00 USD | 0.00 USD | 530,080,000.00 USD | 2,870,000.00 USD | 2,390,000.00 USD | 1,030,000.00 USD |
| `7D` | `2145.40` | 512,950,000.00 USD | 0.00 USD | 512,950,000.00 USD | 2,210,000.00 USD | 1,760,000.00 USD | 1,720,000.00 USD |
| `1D` | `2147.80` | 523,790,000.00 USD | 0.00 USD | 523,790,000.00 USD | 1,040,000.00 USD | 1,140,000.00 USD | 79,080.00 USD |
| `7D` | `2148.40` | 507,250,000.00 USD | 0.00 USD | 507,250,000.00 USD | 26,270.00 USD | 538,910.00 USD | 152,010.00 USD |
| `1D` | `2150.30` | 521,530,000.00 USD | 0.00 USD | 521,530,000.00 USD | 7,580,000.00 USD | 3,090,000.00 USD | 2,660,000.00 USD |
| `7D` | `2151.40` | 506,540,000.00 USD | 0.00 USD | 506,540,000.00 USD | 11,200,000.00 USD | 363,770.00 USD | 354,860.00 USD |
| `1D` | `2152.80` | 508,210,000.00 USD | 0.00 USD | 508,210,000.00 USD | 2,710,000.00 USD | 2,710,000.00 USD | 2,240,000.00 USD |
| `7D` | `2154.40` | 494,620,000.00 USD | 0.00 USD | 494,620,000.00 USD | 48,150.00 USD | 2,020,000.00 USD | 1,580,000.00 USD |
| `1D` | `2155.30` | 500,550,000.00 USD | 0.00 USD | 500,550,000.00 USD | 2,740,000.00 USD | 3,890,000.00 USD | 2,380,000.00 USD |
| `7D` | `2157.40` | 490,970,000.00 USD | 0.00 USD | 490,970,000.00 USD | 6,950,000.00 USD | 1,330,000.00 USD | 5,050,000.00 USD |
| `1D` | `2157.80` | 491,540,000.00 USD | 0.00 USD | 491,540,000.00 USD | 3,400,000.00 USD | 1,640,000.00 USD | 3,680,000.00 USD |
| `1D` | `2160.30` | 482,810,000.00 USD | 0.00 USD | 482,810,000.00 USD | 5,200,000.00 USD | 6,510,000.00 USD | 2,920,000.00 USD |
| `7D` | `2160.40` | 477,640,000.00 USD | 0.00 USD | 477,640,000.00 USD | 397,220.00 USD | 767,490.00 USD | 1,860,000.00 USD |
| `1D` | `2162.80` | 468,190,000.00 USD | 0.00 USD | 468,190,000.00 USD | 17,840,000.00 USD | 10,480,000.00 USD | 1,950,000.00 USD |
| `7D` | `2163.40` | 474,610,000.00 USD | 0.00 USD | 474,610,000.00 USD | 26,080,000.00 USD | 10,840,000.00 USD | 131,020.00 USD |
| `1D` | `2165.30` | 437,910,000.00 USD | 0.00 USD | 437,910,000.00 USD | 10,250,000.00 USD | 9,180,000.00 USD | 5,070,000.00 USD |
| `7D` | `2166.40` | 437,560,000.00 USD | 0.00 USD | 437,560,000.00 USD | 5,300,000.00 USD | 14,900,000.00 USD | 2,860,000.00 USD |
| `1D` | `2167.80` | 413,420,000.00 USD | 0.00 USD | 413,420,000.00 USD | 18,870,000.00 USD | 9,790,000.00 USD | 5,130,000.00 USD |
| `7D` | `2169.40` | 414,500,000.00 USD | 0.00 USD | 414,500,000.00 USD | 8,360,000.00 USD | 14,630,000.00 USD | 4,800,000.00 USD |
| `1D` | `2170.30` | 379,620,000.00 USD | 0.00 USD | 379,620,000.00 USD | 23,930,000.00 USD | 8,680,000.00 USD | 7,400,000.00 USD |
| `7D` | `2172.40` | 386,710,000.00 USD | 0.00 USD | 386,710,000.00 USD | 8,830,000.00 USD | 1,650,000.00 USD | 4,540,000.00 USD |
| `1D` | `2172.80` | 339,610,000.00 USD | 0.00 USD | 339,610,000.00 USD | 7,120,000.00 USD | 3,860,000.00 USD | 3,470,000.00 USD |
| `1D` | `2175.30` | 325,170,000.00 USD | 0.00 USD | 325,170,000.00 USD | 3,540,000.00 USD | 0.00 USD | 836,880.00 USD |
| `7D` | `2175.40` | 371,700,000.00 USD | 0.00 USD | 371,700,000.00 USD | 28,130,000.00 USD | 1,330,000.00 USD | 3,830,000.00 USD |
| `1D` | `2177.80` | 320,800,000.00 USD | 0.00 USD | 320,800,000.00 USD | 730,100.00 USD | 355,620.00 USD | 2,830,000.00 USD |
| `1D` | `2180.30` | 316,890,000.00 USD | 0.00 USD | 316,890,000.00 USD | 894,580.00 USD | 1,550,000.00 USD | 1,410,000.00 USD |
| `7D` | `2181.40` | 338,420,000.00 USD | 0.00 USD | 338,420,000.00 USD | 1,760,000.00 USD | 0.00 USD | 1,400,000.00 USD |
| `1D` | `2182.80` | 313,030,000.00 USD | 0.00 USD | 313,030,000.00 USD | 169,090.00 USD | 1,320,000.00 USD | 3,040,000.00 USD |
| `7D` | `2184.40` | 335,260,000.00 USD | 0.00 USD | 335,260,000.00 USD | 26,960,000.00 USD | 2,700,000.00 USD | 2,550,000.00 USD |
| `1D` | `2185.30` | 308,510,000.00 USD | 0.00 USD | 308,510,000.00 USD | 2,650,000.00 USD | 1,800,000.00 USD | 5,620,000.00 USD |
| `7D` | `2187.40` | 303,050,000.00 USD | 0.00 USD | 303,050,000.00 USD | 14,380,000.00 USD | 17,750,000.00 USD | 0.00 USD |
| `1D` | `2187.80` | 298,440,000.00 USD | 0.00 USD | 298,440,000.00 USD | 5,040,000.00 USD | 4,100,000.00 USD | 7,930,000.00 USD |
| `1D` | `2190.30` | 281,370,000.00 USD | 0.00 USD | 281,370,000.00 USD | 8,990,000.00 USD | 4,390,000.00 USD | 4,040,000.00 USD |
| `7D` | `2190.40` | 270,920,000.00 USD | 0.00 USD | 270,920,000.00 USD | 14,800,000.00 USD | 27,960,000.00 USD | 8,020,000.00 USD |
| `1D` | `2192.80` | 263,960,000.00 USD | 0.00 USD | 263,960,000.00 USD | 5,000,000.00 USD | 5,400,000.00 USD | 1,200,000.00 USD |
| `7D` | `2193.40` | 220,130,000.00 USD | 0.00 USD | 220,130,000.00 USD | 0.00 USD | 7,340,000.00 USD | 8,120,000.00 USD |
| `1D` | `2195.30` | 252,370,000.00 USD | 0.00 USD | 252,370,000.00 USD | 6,640,000.00 USD | 2,370,000.00 USD | 5,950,000.00 USD |
| `7D` | `2196.40` | 204,670,000.00 USD | 0.00 USD | 204,670,000.00 USD | 383,690.00 USD | 243,760.00 USD | 109,160.00 USD |
| `1D` | `2197.80` | 237,410,000.00 USD | 0.00 USD | 237,410,000.00 USD | 3,630,000.00 USD | 1,780,000.00 USD | 4,480,000.00 USD |
| `7D` | `2199.40` | 203,940,000.00 USD | 0.00 USD | 203,940,000.00 USD | 0.00 USD | 1,190,000.00 USD | 7,440,000.00 USD |
| `1D` | `2200.30` | 227,510,000.00 USD | 0.00 USD | 227,510,000.00 USD | 6,260,000.00 USD | 4,750,000.00 USD | 9,470,000.00 USD |
| `7D` | `2202.40` | 195,310,000.00 USD | 0.00 USD | 195,310,000.00 USD | 9,660,000.00 USD | 0.00 USD | 12,340,000.00 USD |
| `1D` | `2202.80` | 207,030,000.00 USD | 0.00 USD | 207,030,000.00 USD | 5,760,000.00 USD | 5,460,000.00 USD | 5,630,000.00 USD |
| `1D` | `2205.30` | 190,180,000.00 USD | 0.00 USD | 190,180,000.00 USD | 6,220,000.00 USD | 3,940,000.00 USD | 2,870,000.00 USD |
| `7D` | `2205.40` | 173,310,000.00 USD | 0.00 USD | 173,310,000.00 USD | 0.00 USD | 429,830.00 USD | 3,380,000.00 USD |
| `1D` | `2207.80` | 177,150,000.00 USD | 0.00 USD | 177,150,000.00 USD | 11,640,000.00 USD | 4,990,000.00 USD | 2,050,000.00 USD |
| `7D` | `2208.40` | 169,500,000.00 USD | 0.00 USD | 169,500,000.00 USD | 19,630,000.00 USD | 2,960,000.00 USD | 5,550,000.00 USD |
| `1D` | `2210.30` | 158,470,000.00 USD | 0.00 USD | 158,470,000.00 USD | 8,640,000.00 USD | 5,850,000.00 USD | 6,290,000.00 USD |
| `7D` | `2211.40` | 141,370,000.00 USD | 0.00 USD | 141,370,000.00 USD | 6,450,000.00 USD | 0.00 USD | 17,290,000.00 USD |
| `1D` | `2212.80` | 137,690,000.00 USD | 0.00 USD | 137,690,000.00 USD | 8,240,000.00 USD | 6,700,000.00 USD | 1,990,000.00 USD |
| `7D` | `2214.40` | 117,620,000.00 USD | 0.00 USD | 117,620,000.00 USD | 0.00 USD | 1,980,000.00 USD | 0.00 USD |
| `1D` | `2215.30` | 120,760,000.00 USD | 0.00 USD | 120,760,000.00 USD | 2,150,000.00 USD | 3,720,000.00 USD | 736,470.00 USD |
| `7D` | `2217.40` | 115,640,000.00 USD | 0.00 USD | 115,640,000.00 USD | 22,400,000.00 USD | 487,520.00 USD | 565,690.00 USD |
| `1D` | `2217.80` | 114,150,000.00 USD | 0.00 USD | 114,150,000.00 USD | 2,630,000.00 USD | 2,470,000.00 USD | 3,320,000.00 USD |
| `1D` | `2220.30` | 105,730,000.00 USD | 0.00 USD | 105,730,000.00 USD | 6,700,000.00 USD | 2,140,000.00 USD | 3,520,000.00 USD |
| `7D` | `2220.40` | 92,190,000.00 USD | 0.00 USD | 92,190,000.00 USD | 308,930.00 USD | 4,700,000.00 USD | 6,890,000.00 USD |
| `1D` | `2222.80` | 93,370,000.00 USD | 0.00 USD | 93,370,000.00 USD | 12,630,000.00 USD | 9,400,000.00 USD | 8,940,000.00 USD |
| `7D` | `2223.40` | 80,300,000.00 USD | 0.00 USD | 80,300,000.00 USD | 9,270,000.00 USD | 14,350,000.00 USD | 24,350,000.00 USD |
| `1D` | `2225.30` | 62,400,000.00 USD | 0.00 USD | 62,400,000.00 USD | 18,130,000.00 USD | 1,920,000.00 USD | 13,880,000.00 USD |
| `7D` | `2226.40` | 32,330,000.00 USD | 0.00 USD | 32,330,000.00 USD | 820,020.00 USD | 6,650,000.00 USD | 24,860,000.00 USD |
| `1D` | `2227.80` | 28,460,000.00 USD | 0.00 USD | 28,460,000.00 USD | 3,850,000.00 USD | 18,120,000.00 USD | 6,490,000.00 USD |
| `1D` | `2229.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2229.40` | 23,170,000.00 USD | 23,170,000.00 USD | 0.00 USD | 2,140,000.00 USD | 0.00 USD | 21,030,000.00 USD |
| `7D` | `2229.40` | 46,350,000.00 USD | 46,350,000.00 USD | 0.00 USD | 2,140,000.00 USD | 0.00 USD | 21,030,000.00 USD |
| `1D` | `2230.30` | 33,100,000.00 USD | 33,100,000.00 USD | 0.00 USD | 31,830,000.00 USD | 1,030,000.00 USD | 241,600.00 USD |
| `7D` | `2232.40` | 48,260,000.00 USD | 48,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,910,000.00 USD |
| `1D` | `2232.80` | 49,890,000.00 USD | 49,890,000.00 USD | 0.00 USD | 16,510,000.00 USD | 0.00 USD | 282,770.00 USD |
| `7D` | `2235.40` | 73,510,000.00 USD | 73,510,000.00 USD | 0.00 USD | 3,260,000.00 USD | 21,640,000.00 USD | 350,840.00 USD |
| `1D` | `2237.80` | 57,890,000.00 USD | 57,890,000.00 USD | 0.00 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2238.40` | 87,540,000.00 USD | 87,540,000.00 USD | 0.00 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2240.30` | 65,100,000.00 USD | 65,100,000.00 USD | 0.00 USD | 7,220,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2241.40` | 119,940,000.00 USD | 119,940,000.00 USD | 0.00 USD | 32,390,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2242.80` | 65,300,000.00 USD | 65,300,000.00 USD | 0.00 USD | 0.00 USD | 141,810.00 USD | 50,930.00 USD |
| `7D` | `2244.40` | 121,410,000.00 USD | 121,410,000.00 USD | 0.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `2245.30` | 65,340,000.00 USD | 65,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 45,350.00 USD |
| `7D` | `2247.40` | 125,230,000.00 USD | 125,230,000.00 USD | 0.00 USD | 1,670,000.00 USD | 1,030,000.00 USD | 1,120,000.00 USD |
| `1D` | `2247.80` | 67,990,000.00 USD | 67,990,000.00 USD | 0.00 USD | 0.00 USD | 2,580,000.00 USD | 70,380.00 USD |
| `1D` | `2250.30` | 73,970,000.00 USD | 73,970,000.00 USD | 0.00 USD | 5,560,000.00 USD | 365,980.00 USD | 55,780.00 USD |
| `7D` | `2250.40` | 132,210,000.00 USD | 132,210,000.00 USD | 0.00 USD | 3,660,000.00 USD | 3,090,000.00 USD | 228,120.00 USD |
| `1D` | `2252.80` | 76,070,000.00 USD | 76,070,000.00 USD | 0.00 USD | 155,320.00 USD | 497,910.00 USD | 1,440,000.00 USD |
| `7D` | `2253.40` | 153,780,000.00 USD | 153,780,000.00 USD | 0.00 USD | 10,110,000.00 USD | 11,240,000.00 USD | 216,090.00 USD |
| `1D` | `2255.30` | 102,270,000.00 USD | 102,270,000.00 USD | 0.00 USD | 13,680,000.00 USD | 6,830,000.00 USD | 5,700,000.00 USD |
| `7D` | `2256.40` | 194,000,000.00 USD | 194,000,000.00 USD | 0.00 USD | 17,810,000.00 USD | 15,220,000.00 USD | 7,190,000.00 USD |
| `1D` | `2257.80` | 139,020,000.00 USD | 139,020,000.00 USD | 0.00 USD | 21,630,000.00 USD | 9,290,000.00 USD | 5,820,000.00 USD |
| `7D` | `2259.40` | 213,580,000.00 USD | 213,580,000.00 USD | 0.00 USD | 11,860,000.00 USD | 3,670,000.00 USD | 4,040,000.00 USD |
| `1D` | `2260.30` | 158,960,000.00 USD | 158,960,000.00 USD | 0.00 USD | 8,050,000.00 USD | 9,340,000.00 USD | 2,540,000.00 USD |
| `7D` | `2262.40` | 222,030,000.00 USD | 222,030,000.00 USD | 0.00 USD | 6,720,000.00 USD | 1,460,000.00 USD | 280,820.00 USD |
| `1D` | `2262.80` | 189,830,000.00 USD | 189,830,000.00 USD | 0.00 USD | 14,830,000.00 USD | 9,830,000.00 USD | 6,220,000.00 USD |
| `1D` | `2265.30` | 215,350,000.00 USD | 215,350,000.00 USD | 0.00 USD | 4,560,000.00 USD | 9,540,000.00 USD | 11,410,000.00 USD |
| `7D` | `2265.40` | 224,630,000.00 USD | 224,630,000.00 USD | 0.00 USD | 0.00 USD | 2,380,000.00 USD | 218,310.00 USD |
| `1D` | `2267.80` | 246,340,000.00 USD | 246,340,000.00 USD | 0.00 USD | 12,410,000.00 USD | 9,520,000.00 USD | 9,070,000.00 USD |
| `7D` | `2268.40` | 249,890,000.00 USD | 249,890,000.00 USD | 0.00 USD | 8,610,000.00 USD | 5,650,000.00 USD | 10,990,000.00 USD |
| `1D` | `2270.30` | 280,920,000.00 USD | 280,920,000.00 USD | 0.00 USD | 12,260,000.00 USD | 7,850,000.00 USD | 14,470,000.00 USD |
| `7D` | `2271.40` | 285,330,000.00 USD | 285,330,000.00 USD | 0.00 USD | 17,870,000.00 USD | 1,330,000.00 USD | 16,240,000.00 USD |
| `1D` | `2272.80` | 305,680,000.00 USD | 305,680,000.00 USD | 0.00 USD | 14,460,000.00 USD | 4,820,000.00 USD | 5,480,000.00 USD |
| `7D` | `2274.40` | 312,380,000.00 USD | 312,380,000.00 USD | 0.00 USD | 20,010,000.00 USD | 7,040,000.00 USD | 0.00 USD |
| `1D` | `2275.30` | 353,340,000.00 USD | 353,340,000.00 USD | 0.00 USD | 30,000,000.00 USD | 14,070,000.00 USD | 3,580,000.00 USD |
| `7D` | `2277.40` | 338,630,000.00 USD | 338,630,000.00 USD | 0.00 USD | 6,890,000.00 USD | 8,890,000.00 USD | 10,480,000.00 USD |
| `1D` | `2277.80` | 388,960,000.00 USD | 388,960,000.00 USD | 0.00 USD | 6,960,000.00 USD | 13,450,000.00 USD | 15,200,000.00 USD |
| `1D` | `2280.30` | 438,850,000.00 USD | 438,850,000.00 USD | 0.00 USD | 30,250,000.00 USD | 10,870,000.00 USD | 8,770,000.00 USD |
| `7D` | `2280.40` | 382,950,000.00 USD | 382,950,000.00 USD | 0.00 USD | 854,200.00 USD | 39,830,000.00 USD | 3,640,000.00 USD |
| `1D` | `2282.80` | 504,140,000.00 USD | 504,140,000.00 USD | 0.00 USD | 28,930,000.00 USD | 26,510,000.00 USD | 9,860,000.00 USD |
| `7D` | `2283.40` | 476,630,000.00 USD | 476,630,000.00 USD | 0.00 USD | 5,600,000.00 USD | 74,390,000.00 USD | 13,690,000.00 USD |
| `1D` | `2285.30` | 524,890,000.00 USD | 524,890,000.00 USD | 0.00 USD | 7,270,000.00 USD | 8,910,000.00 USD | 4,570,000.00 USD |
| `7D` | `2286.40` | 480,320,000.00 USD | 480,320,000.00 USD | 0.00 USD | 2,380,000.00 USD | 727,530.00 USD | 592,240.00 USD |
| `1D` | `2287.80` | 553,260,000.00 USD | 553,260,000.00 USD | 0.00 USD | 12,070,000.00 USD | 8,140,000.00 USD | 8,160,000.00 USD |
| `7D` | `2289.40` | 511,680,000.00 USD | 511,680,000.00 USD | 0.00 USD | 7,010,000.00 USD | 9,840,000.00 USD | 14,500,000.00 USD |
| `1D` | `2290.30` | 591,820,000.00 USD | 591,820,000.00 USD | 0.00 USD | 17,620,000.00 USD | 14,910,000.00 USD | 6,040,000.00 USD |
| `7D` | `2292.40` | 534,950,000.00 USD | 534,950,000.00 USD | 0.00 USD | 13,240,000.00 USD | 0.00 USD | 10,040,000.00 USD |
| `1D` | `2292.80` | 621,230,000.00 USD | 621,230,000.00 USD | 0.00 USD | 13,390,000.00 USD | 4,760,000.00 USD | 11,270,000.00 USD |
| `1D` | `2295.30` | 653,600,000.00 USD | 653,600,000.00 USD | 0.00 USD | 11,190,000.00 USD | 13,200,000.00 USD | 7,970,000.00 USD |
| `7D` | `2295.40` | 572,450,000.00 USD | 572,450,000.00 USD | 0.00 USD | 22,930,000.00 USD | 6,820,000.00 USD | 7,740,000.00 USD |
| `1D` | `2297.80` | 701,090,000.00 USD | 701,090,000.00 USD | 0.00 USD | 28,850,000.00 USD | 12,660,000.00 USD | 5,980,000.00 USD |
| `7D` | `2298.40` | 601,820,000.00 USD | 601,820,000.00 USD | 0.00 USD | 10,950,000.00 USD | 7,970,000.00 USD | 10,450,000.00 USD |
| `1D` | `2300.30` | 742,580,000.00 USD | 742,580,000.00 USD | 0.00 USD | 13,080,000.00 USD | 13,230,000.00 USD | 15,190,000.00 USD |
| `7D` | `2301.40` | 648,940,000.00 USD | 648,940,000.00 USD | 0.00 USD | 17,870,000.00 USD | 23,740,000.00 USD | 5,510,000.00 USD |
| `1D` | `2302.80` | 771,240,000.00 USD | 771,240,000.00 USD | 0.00 USD | 18,360,000.00 USD | 3,050,000.00 USD | 7,240,000.00 USD |
| `7D` | `2304.40` | 703,160,000.00 USD | 703,160,000.00 USD | 0.00 USD | 23,020,000.00 USD | 5,550,000.00 USD | 25,640,000.00 USD |
| `1D` | `2305.30` | 809,000,000.00 USD | 809,000,000.00 USD | 0.00 USD | 13,500,000.00 USD | 16,910,000.00 USD | 7,340,000.00 USD |
| `7D` | `2307.40` | 719,970,000.00 USD | 719,970,000.00 USD | 0.00 USD | 7,580,000.00 USD | 7,040,000.00 USD | 2,200,000.00 USD |
| `1D` | `2307.80` | 819,370,000.00 USD | 819,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 4,020,000.00 USD | 1,980,000.00 USD |
| `1D` | `2310.30` | 838,540,000.00 USD | 838,540,000.00 USD | 0.00 USD | 5,900,000.00 USD | 2,630,000.00 USD | 10,650,000.00 USD |
| `7D` | `2310.40` | 739,440,000.00 USD | 739,440,000.00 USD | 0.00 USD | 11,460,000.00 USD | 2,650,000.00 USD | 5,350,000.00 USD |
| `1D` | `2312.80` | 850,740,000.00 USD | 850,740,000.00 USD | 0.00 USD | 4,670,000.00 USD | 7,190,000.00 USD | 338,820.00 USD |
| `7D` | `2313.40` | 753,850,000.00 USD | 753,850,000.00 USD | 0.00 USD | 0.00 USD | 3,430,000.00 USD | 10,980,000.00 USD |
| `1D` | `2315.30` | 873,070,000.00 USD | 873,070,000.00 USD | 0.00 USD | 4,530,000.00 USD | 11,770,000.00 USD | 6,040,000.00 USD |
| `7D` | `2316.40` | 761,490,000.00 USD | 761,490,000.00 USD | 0.00 USD | 1,020,000.00 USD | 5,590,000.00 USD | 1,040,000.00 USD |
| `1D` | `2317.80` | 894,660,000.00 USD | 894,660,000.00 USD | 0.00 USD | 6,980,000.00 USD | 11,000,000.00 USD | 3,610,000.00 USD |
| `7D` | `2319.40` | 791,770,000.00 USD | 791,770,000.00 USD | 0.00 USD | 5,530,000.00 USD | 16,850,000.00 USD | 7,890,000.00 USD |
| `1D` | `2320.30` | 918,070,000.00 USD | 918,070,000.00 USD | 0.00 USD | 9,870,000.00 USD | 11,090,000.00 USD | 2,460,000.00 USD |
| `7D` | `2322.40` | 800,750,000.00 USD | 800,750,000.00 USD | 0.00 USD | 5,430,000.00 USD | 3,450,000.00 USD | 108,040.00 USD |
| `1D` | `2322.80` | 936,500,000.00 USD | 936,500,000.00 USD | 0.00 USD | 3,860,000.00 USD | 9,520,000.00 USD | 5,050,000.00 USD |
| `1D` | `2325.30` | 950,110,000.00 USD | 950,110,000.00 USD | 0.00 USD | 2,550,000.00 USD | 9,550,000.00 USD | 1,510,000.00 USD |
| `7D` | `2325.40` | 820,660,000.00 USD | 820,660,000.00 USD | 0.00 USD | 7,020,000.00 USD | 2,770,000.00 USD | 10,120,000.00 USD |
| `1D` | `2327.80` | 956,380,000.00 USD | 956,380,000.00 USD | 0.00 USD | 494,310.00 USD | 1,240,000.00 USD | 4,530,000.00 USD |
| `7D` | `2328.40` | 832,670,000.00 USD | 832,670,000.00 USD | 0.00 USD | 3,860,000.00 USD | 121,880.00 USD | 8,030,000.00 USD |
| `1D` | `2330.30` | 972,100,000.00 USD | 972,100,000.00 USD | 0.00 USD | 11,050,000.00 USD | 2,970,000.00 USD | 1,710,000.00 USD |
| `7D` | `2331.40` | 856,590,000.00 USD | 856,590,000.00 USD | 0.00 USD | 23,030,000.00 USD | 835,790.00 USD | 54,580.00 USD |
| `1D` | `2332.80` | 988,880,000.00 USD | 988,880,000.00 USD | 0.00 USD | 4,100,000.00 USD | 3,420,000.00 USD | 9,260,000.00 USD |
| `7D` | `2334.40` | 904,110,000.00 USD | 904,110,000.00 USD | 0.00 USD | 20,300,000.00 USD | 15,180,000.00 USD | 12,040,000.00 USD |
| `1D` | `2335.30` | 1,010,000,000.00 USD | 1,010,000,000.00 USD | 0.00 USD | 12,410,000.00 USD | 3,980,000.00 USD | 3,120,000.00 USD |
| `7D` | `2337.40` | 944,500,000.00 USD | 944,500,000.00 USD | 0.00 USD | 31,080,000.00 USD | 4,650,000.00 USD | 4,650,000.00 USD |
| `1D` | `2337.80` | 1,020,000,000.00 USD | 1,020,000,000.00 USD | 0.00 USD | 7,830,000.00 USD | 1,570,000.00 USD | 4,770,000.00 USD |
| `1D` | `2340.30` | 1,050,000,000.00 USD | 1,050,000,000.00 USD | 0.00 USD | 10,960,000.00 USD | 6,230,000.00 USD | 12,110,000.00 USD |
| `7D` | `2340.40` | 979,730,000.00 USD | 979,730,000.00 USD | 0.00 USD | 4,720,000.00 USD | 10,900,000.00 USD | 19,610,000.00 USD |
| `1D` | `2342.80` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 0.00 USD | 8,670,000.00 USD | 6,510,000.00 USD | 3,140,000.00 USD |
| `7D` | `2343.40` | 1,000,000,000.00 USD | 1,000,000,000.00 USD | 0.00 USD | 5,030,000.00 USD | 11,860,000.00 USD | 7,250,000.00 USD |
| `1D` | `2345.30` | 1,090,000,000.00 USD | 1,090,000,000.00 USD | 0.00 USD | 5,430,000.00 USD | 5,870,000.00 USD | 10,340,000.00 USD |
| `7D` | `2346.40` | 1,040,000,000.00 USD | 1,040,000,000.00 USD | 0.00 USD | 1,350,000.00 USD | 19,690,000.00 USD | 15,350,000.00 USD |
| `1D` | `2347.80` | 1,100,000,000.00 USD | 1,100,000,000.00 USD | 0.00 USD | 3,940,000.00 USD | 3,280,000.00 USD | 1,770,000.00 USD |
| `7D` | `2349.40` | 1,070,000,000.00 USD | 1,070,000,000.00 USD | 0.00 USD | 1,320,000.00 USD | 10,630,000.00 USD | 22,310,000.00 USD |
| `1D` | `2350.30` | 1,150,000,000.00 USD | 1,150,000,000.00 USD | 0.00 USD | 27,810,000.00 USD | 7,790,000.00 USD | 10,500,000.00 USD |
| `7D` | `2352.40` | 1,110,000,000.00 USD | 1,110,000,000.00 USD | 0.00 USD | 2,710,000.00 USD | 27,380,000.00 USD | 5,540,000.00 USD |
| `1D` | `2352.80` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 3,960,000.00 USD | 2,860,000.00 USD | 2,260,000.00 USD |
| `1D` | `2355.30` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 3,190,000.00 USD | 3,410,000.00 USD | 951,670.00 USD |
| `7D` | `2355.40` | 1,160,000,000.00 USD | 1,160,000,000.00 USD | 0.00 USD | 18,620,000.00 USD | 29,090,000.00 USD | 2,760,000.00 USD |
| `1D` | `2357.80` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 3,760,000.00 USD | 4,660,000.00 USD | 3,450,000.00 USD |
| `7D` | `2358.40` | 1,170,000,000.00 USD | 1,170,000,000.00 USD | 0.00 USD | 7,110,000.00 USD | 512,220.00 USD | 4,510,000.00 USD |
| `1D` | `2360.30` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 10,760,000.00 USD | 3,880,000.00 USD | 5,470,000.00 USD |
| `7D` | `2361.40` | 1,180,000,000.00 USD | 1,180,000,000.00 USD | 0.00 USD | 2,430,000.00 USD | 3,430,000.00 USD | 374,770.00 USD |
| `1D` | `2362.80` | 1,220,000,000.00 USD | 1,220,000,000.00 USD | 0.00 USD | 6,460,000.00 USD | 7,190,000.00 USD | 7,920,000.00 USD |
| `7D` | `2364.40` | 1,190,000,000.00 USD | 1,190,000,000.00 USD | 0.00 USD | 4,570,000.00 USD | 373,740.00 USD | 10,920,000.00 USD |
| `1D` | `2365.30` | 1,230,000,000.00 USD | 1,230,000,000.00 USD | 0.00 USD | 4,830,000.00 USD | 2,660,000.00 USD | 3,680,000.00 USD |
| `7D` | `2367.40` | 1,200,000,000.00 USD | 1,200,000,000.00 USD | 0.00 USD | 8,180,000.00 USD | 1,310,000.00 USD | 307,410.00 USD |
| `1D` | `2367.80` | 1,240,000,000.00 USD | 1,240,000,000.00 USD | 0.00 USD | 3,070,000.00 USD | 2,080,000.00 USD | 1,920,000.00 USD |
| `1D` | `2370.30` | 1,260,000,000.00 USD | 1,260,000,000.00 USD | 0.00 USD | 14,770,000.00 USD | 7,590,000.00 USD | 6,160,000.00 USD |
| `7D` | `2370.40` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 0.00 USD | 23,100,000.00 USD | 475,460.00 USD | 47,910,000.00 USD |
| `1D` | `2372.80` | 1,280,000,000.00 USD | 1,280,000,000.00 USD | 0.00 USD | 10,040,000.00 USD | 2,830,000.00 USD | 6,290,000.00 USD |
| `7D` | `2373.40` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 0.00 USD | 21,210,000.00 USD | 121,480.00 USD | 11,210,000.00 USD |
| `1D` | `2375.30` | 1,300,000,000.00 USD | 1,300,000,000.00 USD | 0.00 USD | 10,840,000.00 USD | 1,890,000.00 USD | 2,660,000.00 USD |
| `7D` | `2376.40` | 1,350,000,000.00 USD | 1,350,000,000.00 USD | 0.00 USD | 11,470,000.00 USD | 5,950,000.00 USD | 22,120,000.00 USD |
| `1D` | `2377.80` | 1,310,000,000.00 USD | 1,310,000,000.00 USD | 0.00 USD | 1,460,000.00 USD | 1,920,000.00 USD | 3,990,000.00 USD |
| `7D` | `2379.40` | 1,370,000,000.00 USD | 1,370,000,000.00 USD | 0.00 USD | 7,850,000.00 USD | 2,580,000.00 USD | 12,980,000.00 USD |
| `1D` | `2380.30` | 1,320,000,000.00 USD | 1,320,000,000.00 USD | 0.00 USD | 6,310,000.00 USD | 5,360,000.00 USD | 5,110,000.00 USD |
| `7D` | `2382.40` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 8,510,000.00 USD | 12,380,000.00 USD | 27,930,000.00 USD |
| `1D` | `2382.80` | 1,360,000,000.00 USD | 1,360,000,000.00 USD | 0.00 USD | 15,730,000.00 USD | 9,540,000.00 USD | 11,420,000.00 USD |
| `1D` | `2385.30` | 1,380,000,000.00 USD | 1,380,000,000.00 USD | 0.00 USD | 7,510,000.00 USD | 11,630,000.00 USD | 4,890,000.00 USD |
| `7D` | `2385.40` | 1,510,000,000.00 USD | 1,510,000,000.00 USD | 0.00 USD | 15,900,000.00 USD | 32,250,000.00 USD | 42,810,000.00 USD |
| `1D` | `2387.80` | 1,400,000,000.00 USD | 1,400,000,000.00 USD | 0.00 USD | 9,900,000.00 USD | 5,870,000.00 USD | 2,790,000.00 USD |
| `7D` | `2388.40` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 4,500,000.00 USD | 36,520,000.00 USD | 37,690,000.00 USD |
| `1D` | `2390.30` | 1,410,000,000.00 USD | 1,410,000,000.00 USD | 0.00 USD | 4,300,000.00 USD | 3,360,000.00 USD | 1,520,000.00 USD |
| `7D` | `2391.40` | 1,680,000,000.00 USD | 1,680,000,000.00 USD | 0.00 USD | 6,180,000.00 USD | 50,800,000.00 USD | 35,290,000.00 USD |
| `1D` | `2392.80` | 1,420,000,000.00 USD | 1,420,000,000.00 USD | 0.00 USD | 2,700,000.00 USD | 3,990,000.00 USD | 3,320,000.00 USD |
| `7D` | `2394.40` | 1,810,000,000.00 USD | 1,810,000,000.00 USD | 0.00 USD | 59,450,000.00 USD | 27,550,000.00 USD | 39,900,000.00 USD |
| `1D` | `2395.30` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 2,060,000.00 USD | 1,450,000.00 USD | 2,190,000.00 USD |
| `7D` | `2397.40` | 1,900,000,000.00 USD | 1,900,000,000.00 USD | 0.00 USD | 26,820,000.00 USD | 40,480,000.00 USD | 23,300,000.00 USD |
| `1D` | `2397.80` | 1,430,000,000.00 USD | 1,430,000,000.00 USD | 0.00 USD | 64,150.00 USD | 3,720,000.00 USD | 3,380,000.00 USD |
| `1D` | `2400.30` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 0.00 USD | 2,150,000.00 USD | 637,690.00 USD | 1,390,000.00 USD |
| `7D` | `2400.40` | 2,000,000,000.00 USD | 2,000,000,000.00 USD | 0.00 USD | 53,610,000.00 USD | 26,460,000.00 USD | 21,480,000.00 USD |
| `1D` | `2402.80` | 1,440,000,000.00 USD | 1,440,000,000.00 USD | 0.00 USD | 1,180,000.00 USD | 467,060.00 USD | 555,850.00 USD |
| `7D` | `2403.40` | 2,110,000,000.00 USD | 2,110,000,000.00 USD | 0.00 USD | 51,380,000.00 USD | 24,860,000.00 USD | 33,750,000.00 USD |
| `1D` | `2405.30` | 1,460,000,000.00 USD | 1,460,000,000.00 USD | 0.00 USD | 6,820,000.00 USD | 3,310,000.00 USD | 5,010,000.00 USD |
| `7D` | `2406.40` | 2,190,000,000.00 USD | 2,190,000,000.00 USD | 0.00 USD | 30,580,000.00 USD | 35,580,000.00 USD | 17,010,000.00 USD |
| `1D` | `2407.80` | 1,470,000,000.00 USD | 1,470,000,000.00 USD | 0.00 USD | 6,400,000.00 USD | 3,510,000.00 USD | 1,860,000.00 USD |
| `7D` | `2409.40` | 2,280,000,000.00 USD | 2,280,000,000.00 USD | 0.00 USD | 29,180,000.00 USD | 24,710,000.00 USD | 27,940,000.00 USD |
| `1D` | `2410.30` | 1,480,000,000.00 USD | 1,480,000,000.00 USD | 0.00 USD | 5,140,000.00 USD | 4,530,000.00 USD | 4,180,000.00 USD |
| `7D` | `2412.40` | 2,330,000,000.00 USD | 2,330,000,000.00 USD | 0.00 USD | 16,820,000.00 USD | 18,190,000.00 USD | 16,320,000.00 USD |
| `1D` | `2412.80` | 1,490,000,000.00 USD | 1,490,000,000.00 USD | 0.00 USD | 5,630,000.00 USD | 3,710,000.00 USD | 1,290,000.00 USD |
| `1D` | `2415.30` | 1,500,000,000.00 USD | 1,500,000,000.00 USD | 0.00 USD | 2,830,000.00 USD | 2,350,000.00 USD | 2,970,000.00 USD |
| `7D` | `2415.40` | 2,400,000,000.00 USD | 2,400,000,000.00 USD | 0.00 USD | 22,500,000.00 USD | 20,300,000.00 USD | 25,180,000.00 USD |
| `1D` | `2417.80` | 1,510,000,000.00 USD | 1,510,000,000.00 USD | 0.00 USD | 2,680,000.00 USD | 1,770,000.00 USD | 1,580,000.00 USD |
| `7D` | `2418.40` | 2,450,000,000.00 USD | 2,450,000,000.00 USD | 0.00 USD | 27,870,000.00 USD | 11,330,000.00 USD | 19,260,000.00 USD |
| `1D` | `2420.30` | 1,520,000,000.00 USD | 1,520,000,000.00 USD | 0.00 USD | 6,350,000.00 USD | 3,220,000.00 USD | 4,290,000.00 USD |
| `7D` | `2421.40` | 2,510,000,000.00 USD | 2,510,000,000.00 USD | 0.00 USD | 22,110,000.00 USD | 21,710,000.00 USD | 12,200,000.00 USD |
| `1D` | `2422.80` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 0.00 USD | 1,380,000.00 USD | 2,790,000.00 USD | 3,170,000.00 USD |
| `7D` | `2424.40` | 2,570,000,000.00 USD | 2,570,000,000.00 USD | 0.00 USD | 20,650,000.00 USD | 18,010,000.00 USD | 25,130,000.00 USD |
| `1D` | `2425.30` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 0.00 USD | 1,280,000.00 USD | 623,850.00 USD | 888,640.00 USD |
| `7D` | `2427.40` | 2,620,000,000.00 USD | 2,620,000,000.00 USD | 0.00 USD | 17,580,000.00 USD | 11,600,000.00 USD | 13,310,000.00 USD |
| `1D` | `2427.80` | 1,530,000,000.00 USD | 1,530,000,000.00 USD | 0.00 USD | 1,490,000.00 USD | 1,520,000.00 USD | 609,950.00 USD |
| `1D` | `2430.30` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 0.00 USD | 1,460,000.00 USD | 1,550,000.00 USD | 1,360,000.00 USD |
| `7D` | `2430.40` | 2,650,000,000.00 USD | 2,650,000,000.00 USD | 0.00 USD | 8,480,000.00 USD | 15,370,000.00 USD | 9,620,000.00 USD |
| `1D` | `2432.80` | 1,540,000,000.00 USD | 1,540,000,000.00 USD | 0.00 USD | 2,680,000.00 USD | 2,230,000.00 USD | 1,030,000.00 USD |
| `7D` | `2433.40` | 2,670,000,000.00 USD | 2,670,000,000.00 USD | 0.00 USD | 14,840,000.00 USD | 5,270,000.00 USD | 4,190,000.00 USD |
| `1D` | `2435.30` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 0.00 USD | 2,480,000.00 USD | 572,900.00 USD | 1,010,000.00 USD |
| `7D` | `2436.40` | 2,690,000,000.00 USD | 2,690,000,000.00 USD | 0.00 USD | 6,380,000.00 USD | 8,830,000.00 USD | 5,020,000.00 USD |
| `1D` | `2437.80` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 0.00 USD | 1,360,000.00 USD | 1,040,000.00 USD | 30,250.00 USD |
| `7D` | `2439.40` | 2,720,000,000.00 USD | 2,720,000,000.00 USD | 0.00 USD | 13,950,000.00 USD | 7,290,000.00 USD | 5,790,000.00 USD |
| `1D` | `2440.30` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 0.00 USD | 1,240,000.00 USD | 515,920.00 USD | 304,820.00 USD |
| `7D` | `2442.40` | 2,740,000,000.00 USD | 2,740,000,000.00 USD | 0.00 USD | 6,350,000.00 USD | 5,550,000.00 USD | 7,930,000.00 USD |
| `1D` | `2442.80` | 1,550,000,000.00 USD | 1,550,000,000.00 USD | 0.00 USD | 1,030,000.00 USD | 673,960.00 USD | 823,660.00 USD |
| `1D` | `2445.30` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 0.00 USD | 0.00 USD | 486,350.00 USD | 1,130,000.00 USD |
| `7D` | `2445.40` | 2,770,000,000.00 USD | 2,770,000,000.00 USD | 0.00 USD | 9,990,000.00 USD | 8,050,000.00 USD | 10,380,000.00 USD |
| `1D` | `2447.80` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 0.00 USD | 472,100.00 USD | 743,310.00 USD | 694,310.00 USD |
| `7D` | `2448.40` | 2,800,000,000.00 USD | 2,800,000,000.00 USD | 0.00 USD | 11,190,000.00 USD | 3,790,000.00 USD | 15,190,000.00 USD |
| `1D` | `2450.30` | 1,560,000,000.00 USD | 1,560,000,000.00 USD | 0.00 USD | 1,710,000.00 USD | 69,580.00 USD | 26,770.00 USD |
| `7D` | `2451.40` | 2,820,000,000.00 USD | 2,820,000,000.00 USD | 0.00 USD | 8,550,000.00 USD | 7,920,000.00 USD | 6,780,000.00 USD |
| `1D` | `2452.80` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 2,460,000.00 USD | 1,840,000.00 USD | 2,370,000.00 USD |
| `7D` | `2454.40` | 2,840,000,000.00 USD | 2,840,000,000.00 USD | 0.00 USD | 5,080,000.00 USD | 3,080,000.00 USD | 4,450,000.00 USD |
| `1D` | `2455.30` | 1,570,000,000.00 USD | 1,570,000,000.00 USD | 0.00 USD | 1,640,000.00 USD | 1,860,000.00 USD | 905,110.00 USD |
| `7D` | `2457.40` | 2,860,000,000.00 USD | 2,860,000,000.00 USD | 0.00 USD | 8,580,000.00 USD | 7,900,000.00 USD | 8,690,000.00 USD |
| `1D` | `2457.80` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 1,770,000.00 USD | 1,980,000.00 USD | 845,630.00 USD |
| `1D` | `2460.30` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 1,530,000.00 USD | 1,410,000.00 USD | 388,420.00 USD |
| `7D` | `2460.40` | 2,880,000,000.00 USD | 2,880,000,000.00 USD | 0.00 USD | 3,700,000.00 USD | 7,320,000.00 USD | 4,650,000.00 USD |
| `1D` | `2462.80` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 355,800.00 USD | 618,870.00 USD | 1,020,000.00 USD |
| `7D` | `2463.40` | 2,890,000,000.00 USD | 2,890,000,000.00 USD | 0.00 USD | 6,140,000.00 USD | 5,730,000.00 USD | 6,170,000.00 USD |
| `1D` | `2465.30` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 537,580.00 USD | 876,630.00 USD | 345,350.00 USD |
| `7D` | `2466.40` | 2,900,000,000.00 USD | 2,900,000,000.00 USD | 0.00 USD | 5,680,000.00 USD | 2,080,000.00 USD | 1,350,000.00 USD |
| `1D` | `2467.80` | 1,580,000,000.00 USD | 1,580,000,000.00 USD | 0.00 USD | 288,920.00 USD | 980,750.00 USD | 377,900.00 USD |
| `7D` | `2469.40` | 2,910,000,000.00 USD | 2,910,000,000.00 USD | 0.00 USD | 2,520,000.00 USD | 3,570,000.00 USD | 408,300.00 USD |
| `1D` | `2470.30` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 1,010,000.00 USD | 1,660,000.00 USD | 1,480,000.00 USD |
| `7D` | `2472.40` | 2,920,000,000.00 USD | 2,920,000,000.00 USD | 0.00 USD | 4,130,000.00 USD | 2,760,000.00 USD | 2,710,000.00 USD |
| `1D` | `2472.80` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 404,980.00 USD | 92,950.00 USD | 1,020,000.00 USD |
| `1D` | `2475.30` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 414,330.00 USD | 1,100,000.00 USD | 231,680.00 USD |
| `7D` | `2475.40` | 2,930,000,000.00 USD | 2,930,000,000.00 USD | 0.00 USD | 5,400,000.00 USD | 1,040,000.00 USD | 1,450,000.00 USD |
| `1D` | `2477.80` | 1,590,000,000.00 USD | 1,590,000,000.00 USD | 0.00 USD | 2,200,000.00 USD | 238,300.00 USD | 167,580.00 USD |
| `7D` | `2478.40` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 3,140,000.00 USD | 5,290,000.00 USD | 540,990.00 USD |
| `1D` | `2480.30` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 567,450.00 USD | 943,540.00 USD | 731,890.00 USD |
| `7D` | `2481.40` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 729,480.00 USD | 3,680,000.00 USD | 1,050,000.00 USD |
| `1D` | `2482.50` | 1,600,000,000.00 USD | 1,600,000,000.00 USD | 0.00 USD | 437,940.00 USD | 156,850.00 USD | 1,030,000.00 USD |
| `7D` | `2484.40` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 0.00 USD | 200,980.00 USD | 1,350,000.00 USD |
| `7D` | `2487.40` | 2,940,000,000.00 USD | 2,940,000,000.00 USD | 0.00 USD | 275,450.00 USD | 211,130.00 USD | 0.00 USD |
| `7D` | `2490.40` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 0.00 USD | 385,480.00 USD | 301,010.00 USD | 137,010.00 USD |
| `7D` | `2493.40` | 2,950,000,000.00 USD | 2,950,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 733,870.00 USD | 1,470,000.00 USD |
| `7D` | `2496.40` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 0.00 USD | 993,060.00 USD | 812,060.00 USD | 4,560,000.00 USD |
| `7D` | `2499.40` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 0.00 USD | 0.00 USD | 1,310,000.00 USD | 241,000.00 USD |
| `7D` | `2502.40` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 0.00 USD | 0.00 USD | 55,050.00 USD | 125,600.00 USD |
| `7D` | `2505.40` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 0.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2508.40` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 0.00 USD | 1,090,000.00 USD | 882,660.00 USD | 1,190,000.00 USD |
| `7D` | `2514.40` | 2,960,000,000.00 USD | 2,960,000,000.00 USD | 0.00 USD | 56,430.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `2517.40` | 2,970,000,000.00 USD | 2,970,000,000.00 USD | 0.00 USD | 975,520.00 USD | 965,900.00 USD | 815,620.00 USD |
| `7D` | `2520.40` | 2,970,000,000.00 USD | 2,970,000,000.00 USD | 0.00 USD | 722,920.00 USD | 1,170,000.00 USD | 894,250.00 USD |
| `7D` | `2523.40` | 2,970,000,000.00 USD | 2,970,000,000.00 USD | 0.00 USD | 1,050,000.00 USD | 0.00 USD | 945,860.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `28.44B` | Total OI Tokens: `12,781,130.7 ETH`
  * 1h OI Change: `-0.43%` | 4h OI Change: `-2.38%` | 24h OI Change: `-5.79%`
  * Exchange Breakdown: Binance=`8.39B` | Bybit=`2.09B` | OKX=`1.75B` | Hyperliquid=`2.39B`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-436.45K` | Last 24h: `195.10K` | Last 3d: `5.21M` | Last 7d: `11.81M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0047%` | **USDT OKX** | `-0.0074%` |
| **USDT Bybit** | `-0.0084%` | **USDT KuCoin** | `-0.0075%` |
| **USDT MEXC** | `-0.0046%` | **USDT BingX** | `-0.0019%` |
| **USDT Gate** | `0.0003%` | **USDT Bitget** | `-0.0023%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0008%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ETH` | `42.80%` | `57.20%` | `0.75` | 490,260,000.00 USD |
| `15M` | `Binance` | `36.22%` | `63.78%` | `0.57` | 145,570,000.00 USD |
| `15M` | `OKX` | `49.82%` | `50.18%` | `0.99` | 71,530,000.00 USD |
| `15M` | `Bybit` | `54.32%` | `45.68%` | `1.19` | 38,920,000.00 USD |
| `15M` | `KuCoin` | `31.04%` | `68.96%` | `0.45` | 1,070,000.00 USD |
| `15M` | `Gate` | `57.2%` | `42.8%` | `1.34` | 55,680,000.00 USD |
| `15M` | `Bitget` | `46.39%` | `53.61%` | `0.87` | 21,930,000.00 USD |
| `15M` | `BingX` | `53.47%` | `46.53%` | `1.15` | 10,980,000.00 USD |
| `15M` | `MEXC` | `33.73%` | `66.27%` | `0.51` | 22,950,000.00 USD |
| `15M` | `Bitunix` | `56.27%` | `43.73%` | `1.29` | 23,210,000.00 USD |
| `15M` | `Hyperliquid` | `8.74%` | `91.26%` | `0.10` | 45,790,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.4%` | `50.6%` | `0.98` | 12,950,000.00 USD |
| `15M` | `Crypto.com` | `39.77%` | `60.23%` | `0.66` | 1,600,000.00 USD |
| `15M` | `WhiteBIT` | `99.59%` | `0.41%` | `242.90` | 4,000,000.00 USD |
| `15M` | `HTX` | `40.67%` | `59.33%` | `0.69` | 1,990,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `50.01%` | `49.99%` | `1.00` | 20,680,000.00 USD |
| `15M` | `Bitfinex` | `63.36%` | `36.64%` | `1.73` | 158,700.00 USD |
| `15M` | `Kraken` | `46.9%` | `53.1%` | `0.88` | 2,600,000.00 USD |
| `15M` | `Aster` | `33.89%` | `66.11%` | `0.51` | 4,450,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `54.42%` | `45.58%` | `1.19` | 4,220,000.00 USD |
| `15M` | `Whale Positions` | `36.22%` | `63.78%` | `0.57` | 145,570,000.00 USD |
| `15M` | `Global Accounts` | `42.80%` | `57.20%` | `0.75` | 490,260,000.00 USD |
| `1H` | `ETH` | `45.02%` | `54.98%` | `0.82` | 3,400,000,000.00 USD |
| `1H` | `Binance` | `44.76%` | `55.24%` | `0.81` | 853,710,000.00 USD |
| `1H` | `OKX` | `47.56%` | `52.44%` | `0.91` | 494,170,000.00 USD |
| `1H` | `Bybit` | `45.49%` | `54.51%` | `0.83` | 227,090,000.00 USD |
| `1H` | `KuCoin` | `44.67%` | `55.33%` | `0.81` | 5,530,000.00 USD |
| `1H` | `Gate` | `50.73%` | `49.27%` | `1.03` | 293,520,000.00 USD |
| `1H` | `Bitget` | `40.82%` | `59.18%` | `0.69` | 139,420,000.00 USD |
| `1H` | `BingX` | `42%` | `58%` | `0.72` | 62,920,000.00 USD |
| `1H` | `MEXC` | `43.88%` | `56.12%` | `0.78` | 114,710,000.00 USD |
| `1H` | `Bitunix` | `45.25%` | `54.75%` | `0.83` | 113,420,000.00 USD |
| `1H` | `Hyperliquid` | `16.17%` | `83.83%` | `0.19` | 202,620,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.15%` | `49.85%` | `1.01` | 569,660,000.00 USD |
| `1H` | `Crypto.com` | `43.68%` | `56.32%` | `0.78` | 9,770,000.00 USD |
| `1H` | `WhiteBIT` | `30.62%` | `69.38%` | `0.44` | 72,860,000.00 USD |
| `1H` | `HTX` | `41.86%` | `58.14%` | `0.72` | 10,670,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `54.66%` | `45.34%` | `1.21` | 165,980,000.00 USD |
| `1H` | `Bitfinex` | `36.66%` | `63.34%` | `0.58` | 1,110,000.00 USD |
| `1H` | `Kraken` | `64.13%` | `35.87%` | `1.79` | 9,560,000.00 USD |
| `1H` | `Aster` | `48.92%` | `51.08%` | `0.96` | 21,750,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `54.33%` | `45.67%` | `1.19` | 24,280,000.00 USD |
| `1H` | `Whale Positions` | `44.76%` | `55.24%` | `0.81` | 853,710,000.00 USD |
| `1H` | `Global Accounts` | `45.02%` | `54.98%` | `0.82` | 3,400,000,000.00 USD |
| `4H` | `ETH` | `46.75%` | `53.25%` | `0.88` | 9,880,000,000.00 USD |
| `4H` | `Binance` | `45.01%` | `54.99%` | `0.82` | 3,060,000,000.00 USD |
| `4H` | `OKX` | `47.44%` | `52.56%` | `0.90` | 1,430,000,000.00 USD |
| `4H` | `Bybit` | `46.52%` | `53.48%` | `0.87` | 843,140,000.00 USD |
| `4H` | `KuCoin` | `52.64%` | `47.36%` | `1.11` | 23,160,000.00 USD |
| `4H` | `Gate` | `49.3%` | `50.7%` | `0.97` | 1,000,000,000.00 USD |
| `4H` | `Bitget` | `46.52%` | `53.48%` | `0.87` | 481,090,000.00 USD |
| `4H` | `BingX` | `40.1%` | `59.9%` | `0.67` | 177,090,000.00 USD |
| `4H` | `MEXC` | `44.11%` | `55.89%` | `0.79` | 411,190,000.00 USD |
| `4H` | `Bitunix` | `44.47%` | `55.53%` | `0.80` | 363,710,000.00 USD |
| `4H` | `Hyperliquid` | `36.31%` | `63.69%` | `0.57` | 495,420,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.76%` | `49.24%` | `1.03` | 677,380,000.00 USD |
| `4H` | `Crypto.com` | `46.55%` | `53.45%` | `0.87` | 27,930,000.00 USD |
| `4H` | `WhiteBIT` | `66.55%` | `33.45%` | `1.99` | 197,780,000.00 USD |
| `4H` | `HTX` | `46.68%` | `53.32%` | `0.88` | 35,640,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `51.63%` | `48.37%` | `1.07` | 423,770,000.00 USD |
| `4H` | `Bitfinex` | `35.27%` | `64.73%` | `0.54` | 5,490,000.00 USD |
| `4H` | `Kraken` | `63.02%` | `36.98%` | `1.70` | 9,950,000.00 USD |
| `4H` | `Aster` | `54.36%` | `45.64%` | `1.19` | 94,090,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `53.18%` | `46.82%` | `1.14` | 115,480,000.00 USD |
| `4H` | `Whale Positions` | `45.01%` | `54.99%` | `0.82` | 3,060,000,000.00 USD |
| `4H` | `Global Accounts` | `46.75%` | `53.25%` | `0.88` | 9,880,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `2248.25` | `2247.78` | `2248.25` | `2251.25` | `2242.75` | 54,657,138.04 USD | 27,616,704.22 USD | 27,040,433.82 USD | 576,270.40 USD | `+1.05%` | `3B / 1S` |
| `0:00 UTC` | `2247.25` | `2251.75` | `2247.25` | `2257.25` | `2246.75` | 87,188,538.32 USD | 46,292,419.67 USD | 40,896,118.65 USD | 5,396,301.02 USD | `+6.19%` | `2B / 0S` |
| `5:00 UTC` | `2251.75` | `2248.99` | `2251.75` | `2253.75` | `2242.25` | 85,642,088.43 USD | 41,477,047.01 USD | 44,165,041.41 USD | -2,687,994.40 USD | `-3.14%` | `3B / 1S` |
| `0:00 UTC` | `2252.25` | `2251.61` | `2252.25` | `2253.75` | `2247.75` | 100,086,564.92 USD | 38,681,627.31 USD | 61,404,937.61 USD | -22,723,310.29 USD | `-22.70%` | `0B / 5S` |
| `5:00 UTC` | `2244.75` | `2247.34` | `2244.75` | `2250.75` | `2244.25` | 75,332,127.88 USD | 44,642,781.21 USD | 30,689,346.67 USD | 13,953,434.54 USD | `+18.52%` | `1B / 0S` |
| `0:00 UTC` | `2230.25` | `2237.42` | `2230.25` | `2248.75` | `2228.25` | 239,005,598.88 USD | 101,154,920.14 USD | 137,850,678.73 USD | -36,695,758.59 USD | `-15.35%` | `0B / 8S` |
| `5:00 UTC` | `2232.75` | `2233.33` | `2232.75` | `2238.25` | `2228.25` | 153,884,513.89 USD | 97,714,432.25 USD | 56,170,081.64 USD | 41,544,350.61 USD | `+27.00%` | `5B / 1S` |
| `0:00 UTC` | `2227.75` | `2228.98` | `2227.75` | `2236.75` | `2223.25` | 107,078,982.08 USD | 47,873,893.40 USD | 59,205,088.68 USD | -11,331,195.28 USD | `-10.58%` | `0B / 1S` |
| `5:00 UTC` | `2233.25` | `2230.29` | `2233.25` | `2234.75` | `2224.25` | 95,342,735.21 USD | 45,163,958.47 USD | 50,178,776.75 USD | -5,014,818.28 USD | `-5.26%` | `0B / 3S` |
| `0:00 UTC` | `2226.25` | `2227.73` | `2226.25` | `2230.25` | `2225.25` | 41,279,036.36 USD | 17,343,091.96 USD | 23,935,944.41 USD | -6,592,852.45 USD | `-15.97%` | `0B / 0S` |

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
| `5m` | -1,690,000.00 USD | -2,070,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -9,420,000.00 USD | -18,250,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -7,990,000.00 USD | 19,460,000.00 USD | **`ACCUMULATION`** |
| `1h` | -4,530,000.00 USD | -59,810,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 3,730,000.00 USD | -96,320,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 15,660,000.00 USD | -67,500,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 13,510,000.00 USD | 12,210,000.00 USD | **`ACCUMULATION`** |
| `8h` | -17,650,000.00 USD | -646,730,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -108,890,000.00 USD | -1,300,000,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -127,350,000.00 USD | -1,930,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -202,120,000.00 USD | -3,140,000,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -3,120,000,000.00 USD | -9,570,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-1.69M` | 15m=`-9.42M` | 1h=`-4.53M` | 24h=`-127.35M`
* Futures Capital Netflows: 5m=`-2.07M` | 15m=`-18.25M` | 1h=`-59.81M` | 24h=`-1.93B`
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
  * `2026-10-30 13:52:16 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:16 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:32:16 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:16 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:16 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 13:22:16 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 13:21:16 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:06:16 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:06:16 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:06:16 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:06:16 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:06:16 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:05:16 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:05:16 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:05:16 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `2191.58` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `2170.54` (Risk Distance: `21.04` pts)
  * +2.5R Take Profit: `2244.19`
  * Mathematical Lot Sizing: **`0.47 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `2252.28` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2273.32` (Risk Distance: `21.04` pts)
  * +2.5R Take Profit: `2199.67`
  * Mathematical Lot Sizing: **`0.47 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`2239.57`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
